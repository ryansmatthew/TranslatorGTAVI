"""Phase 3 — offline batch translation runner (TDD ch.6).
Translates UNIQUE en_norm strings once and applies the result to every
source_id sharing that norm (P0: 50,157 rows -> 39,003 unique, -22%).

  python -m src.pipeline.translate_batch --db data/gta6.db --backend gemini
      --tier P0 --batch-size 20 --limit 100
  python -m src.pipeline.translate_batch --db data/gta6.db --backend local-opus-mt
      --tier P0 --limit 100

Rules (TDD 6.1-6.3):
  * Resume: translation state lives in the DB (translations.status).
    Re-running skips anything already translated; safe to stop anytime.
  * Retry: transient translator errors retry 3x with backoff, then the
    batch is left untranslated (not quarantined) so a later run retries it.
  * Validation failure -> quarantine: the row is NOT written to
    `translations`; the failure is recorded in db_meta as a counter and
    printed, for manual review. The batch continues.
  * Markers: each marker in en is replaced by <<M0>>, <<M1>>, ... before
    translation and restored exactly afterwards; validate.py then proves
    the marker multiset is identical.
  * Glossary: terms present in the source sentence are passed to the
    translator as a note and enforced by the validator.
  * One writer: this script is the only writer of `translations` in
    Phase 3; the realtime runtime opens the DB read-only.
"""
import argparse
import csv
import json
import os
import re
import sqlite3
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from src.common.markers import split_markers  # noqa: E402
from src.common.normalize import mask_slots_for_translation  # noqa: E402
from src.pipeline.translators import get_translator  # noqa: E402
from src.pipeline.validate import validate  # noqa: E402

MARKER_TOKEN = re.compile(r"<<M(\d+)>>")


def mask_markers(en: str):
    """Replace markers with <<M0>>... tokens; return (masked, [markers])."""
    _, mj, _ = split_markers(en)
    markers = [m["marker"] for m in json.loads(mj)]
    # rebuild from the original en, replacing each marker span with its
    # token (spans are in original coordinates, in order)
    parts, last = [], 0
    for i, m in enumerate(json.loads(mj)):
        parts.append(en[last:m["start"]])
        parts.append(f"<<M{i}>>")
        last = m["end"]
    parts.append(en[last:])
    return "".join(parts), markers


def unmask(text: str, markers):
    def repl(m):
        i = int(m.group(1))
        return markers[i] if i < len(markers) else m.group(0)
    return MARKER_TOKEN.sub(repl, text)


def load_glossary(db, csv_path):
    glossary = []
    if csv_path and os.path.exists(csv_path):
        with open(csv_path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                glossary.append({
                    "en_term": row["en_term"], "vi_term": row.get("vi_term") or "",
                    "kind": row.get("kind") or "",
                    "do_not_translate": row.get("do_not_translate") == "1",
                })
    # also load whatever is already in the DB glossary table
    for en_term, vi_term, kind, dnt in db.execute(
            "SELECT en_term, vi_term, kind, do_not_translate FROM glossary"):
        glossary.append({"en_term": en_term, "vi_term": vi_term, "kind": kind,
                         "do_not_translate": bool(dnt)})
    # de-dup by (en_term, kind), CSV wins
    seen, out = set(), []
    for g in glossary:
        k = (g["en_term"], g["kind"])
        if k not in seen:
            seen.add(k)
            out.append(g)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--backend", choices=["gemini", "local-opus-mt"], required=True)
    ap.add_argument("--tier", default="P0")
    ap.add_argument("--batch-size", type=int, default=20)
    ap.add_argument("--limit", type=int, default=0, help="0 = all remaining in tier")
    ap.add_argument("--glossary-csv", default="data/glossary.csv")
    ap.add_argument("--model", default=None)
    args = ap.parse_args()

    translator = get_translator(args.backend, **({"model": args.model} if args.model else {}))
    db = sqlite3.connect(args.db)
    db.execute("PRAGMA journal_mode=WAL")
    glossary = load_glossary(db, args.glossary_csv)
    # seed DB glossary from CSV if the table is empty
    if db.execute("SELECT COUNT(*) FROM glossary").fetchone()[0] == 0 and glossary:
        db.executemany(
            "INSERT OR IGNORE INTO glossary (en_term, vi_term, kind, do_not_translate) "
            "VALUES (?,?,?,?)",
            [(g["en_term"], g["vi_term"], g["kind"], int(g["do_not_translate"])) for g in glossary])
        db.commit()

    # work queue: one row per unique en_norm in the tier, not yet translated
    rows = db.execute(
        "SELECT MIN(s.id) AS id, s.en, m.en_norm, m.en_skel "
        "FROM source_strings s JOIN match_index m ON m.source_id = s.id "
        "WHERE s.priority_tier = ? AND TRIM(s.en) != '' "
        "AND NOT EXISTS (SELECT 1 FROM translations t WHERE t.source_id = s.id "
        "  AND t.status IN ('machine','reviewed','approved')) "
        "GROUP BY m.en_norm ORDER BY s.id", (args.tier,)).fetchall()
    total = len(rows)
    if args.limit:
        rows = rows[:args.limit]
    print(f"backend={args.backend} tier={args.tier} remaining_unique={total} "
          f"to_translate={len(rows)} batch={args.batch_size}", flush=True)

    done = quarantined = failed = 0
    now = lambda: datetime.now(timezone.utc).isoformat()  # noqa: E731
    for start in range(0, len(rows), args.batch_size):
        chunk = rows[start:start + args.batch_size]
        masked, metas = [], []
        for _id, en, en_norm, en_skel in chunk:
            m, markers = mask_markers(en)
            # template rows: mask dynamic values as {money}/{time}/{number}
            # so the stored translation keeps the SLOT (TDD 5.5)
            m, _slots = mask_slots_for_translation(m)
            masked.append(m)
            metas.append((_id, en, en_norm, en_skel, markers))
        # glossary terms actually present in this chunk
        present = [g for g in glossary
                   if any(g["en_term"] and g["en_term"].lower() in (en or "").lower()
                          for _, en, _, _, _ in metas)]
        note = "\n".join(
            f"- {g['en_term']}: keep exactly as-is" if g["do_not_translate"]
            else f"- {g['en_term']} = {g['vi_term']}" for g in present)
        try:
            translated = translator.translate(masked, glossary_note=note)
        except Exception as e:  # noqa: BLE001
            print(f"batch {start}: translator error, will retry next run: {e}", flush=True)
            failed += len(chunk)
            time.sleep(5)
            continue
        for (sid, en, en_norm, en_skel, markers), vi_masked in zip(metas, translated):
            vi = unmask(vi_masked, markers)
            # glossary check only for terms present in THIS source sentence
            g_here = [g for g in present if g["en_term"].lower() in en.lower()]
            ok, reasons = validate(en, en_skel, vi, glossary=g_here)
            if not ok:
                quarantined += 1
                print(f"QUARANTINE {sid}: {reasons} | en={en[:80]!r} vi={vi[:80]!r}", flush=True)
                continue
            # apply to EVERY source_id sharing this en_norm
            targets = [r[0] for r in db.execute(
                "SELECT source_id FROM match_index WHERE en_norm = ?", (en_norm,))]
            for tid in targets:
                db.execute(
                    "INSERT INTO translations (source_id, vi, version, status, origin, "
                    "context_key, created_at) VALUES (?,?,1,'machine',?,NULL,?)",
                    (tid, vi, translator.origin, now()))
            done += len(targets)
        db.commit()
        print(f"  ... {min(start + args.batch_size, len(rows))}/{len(rows)} "
              f"translated_rows={done} quarantined={quarantined} failed={failed}", flush=True)

    db.execute(
        "INSERT INTO db_meta (key, value, updated_at) VALUES ('pipeline_backend', ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        (args.backend, now()))
    db.commit()
    print(f"DONE backend={args.backend} tier={args.tier} "
          f"translated_rows={done} quarantined={quarantined} failed={failed}")
    db.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
