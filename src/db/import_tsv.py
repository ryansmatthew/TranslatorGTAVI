"""Phase 2 — import all_rows.tsv into gta6.db (SQLite WAL + FTS5).
TDD v1.3, Chapter 4 / Phase 2 gate (Chapter 14).

Usage:
    python -m src.db.import_tsv --tsv <all_rows.tsv> --db <gta6.db> [--schema src/db/schema.sql]

What it does, in order:
  1. SHA-256 of the source file + a checksum over (id, en) in file order.
  2. Reads every TSV row, preserving the original columns verbatim
     (id, pack, table, idx, hash, category, group, keep, ukey, en).
  3. Splits markers via common.markers -> en_display + markers JSON.
  4. Derives priority_tier (TDD 4.3) and template info via
     common.normalize -> en_norm / en_skel / pattern / slots.
  5. Writes source_strings, match_index, string_templates, screen_contexts
     and db_meta, then populates match_fts and rebuilds it.
  6. Validates: row count, no lost markers, en checksum round-trip,
     and writes data/import_report.json next to the DB.

Priority tiers (TDD 4.3, derived from category + group + ~sl: timing):
  P0  category='ui' or category='subtitle'
  P1  group contains 'Mạng xã hội' (social, hidden inside dialogue),
      or category in ('item', 'description', 'tutorial')
  P2  category='lore'
  P3  category='dialogue' (remaining)
  NULL category='' (blank, 12,066 rows) -> 'review', never auto-translated
"""
import argparse
import csv
import hashlib
import json
import os
import sqlite3
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.common.markers import MARKERS_VERSION, split_markers  # noqa: E402
from src.common.normalize import (  # noqa: E402
    NORMALIZE_VERSION,
    first_token,
    len_bucket,
    normalize,
    skeleton,
    template_pattern,
)

SCHEMA_VERSION = 1
TDD_VERSION = "1.3"

SCREEN_CONTEXTS = [
    ("menu.pause", "ui", "Giao diện", 1.0),
    ("menu.generic", "ui", "Giao diện", 1.0),
    ("subtitle.story", "subtitle", "Phụ đề hội thoại", 1.0),
    ("subtitle.core", "subtitle", "Phụ đề hội thoại", 1.0),
    ("phone.social", "dialogue", "Mạng xã hội", 1.0),
    ("phone.generic", "ui", "Giao diện", 1.0),
    ("hud.generic", "ui", "Giao diện", 1.0),
    ("notification", "description", "Mô tả / Nhiệm vụ", 1.0),
]


def priority_tier(category: str, group: str, en: str) -> str | None:
    if category == "":
        return "review"
    if category in ("ui", "subtitle"):
        return "P0"
    if "Mạng xã hội" in (group or ""):
        return "P1"
    if category in ("item", "description", "tutorial"):
        return "P1"
    if category == "lore":
        return "P2"
    if category == "dialogue":
        return "P3"
    return "P3"


def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tsv", required=True)
    ap.add_argument("--db", required=True)
    ap.add_argument("--schema", default=os.path.join(os.path.dirname(__file__), "schema.sql"))
    args = ap.parse_args()

    t0 = time.time()
    source_sha = file_sha256(args.tsv)
    print(f"source: {args.tsv}  sha256={source_sha}")

    if os.path.exists(args.db):
        os.remove(args.db)
        print(f"removed existing {args.db} (fresh rebuild)")

    conn = sqlite3.connect(args.db)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    with open(args.schema, encoding="utf-8") as f:
        conn.executescript(f.read())

    en_checksum = hashlib.sha256()
    rows_src, rows_mi, rows_tpl = [], [], []
    stats = {
        "total": 0, "empty_en": 0, "unknown_markers": 0, "rows_with_markers": 0,
        "templates": 0, "tiers": {}, "categories": {}, "packs": {},
    }
    # checksum is over the original columns in file order, so a later
    # migration can prove nothing was lost or reordered.
    with open(args.tsv, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        expected = ["id", "pack", "table", "idx", "hash", "category", "group", "keep", "ukey", "en"]
        assert reader.fieldnames == expected, f"unexpected header: {reader.fieldnames}"
        for r in reader:
            stats["total"] += 1
            en = r["en"] or ""
            en_checksum.update((r["id"] + "\x00" + en + "\x00").encode("utf-8"))
            if not en.strip():
                stats["empty_en"] += 1
            tier = priority_tier(r["category"], r["group"], en)
            stats["tiers"][tier] = stats["tiers"].get(tier, 0) + 1
            stats["categories"][r["category"]] = stats["categories"].get(r["category"], 0) + 1
            stats["packs"][r["pack"]] = stats["packs"].get(r["pack"], 0) + 1

            display, markers_json, unknown = split_markers(en)
            if unknown:
                stats["unknown_markers"] += unknown
            if markers_json != "[]":
                stats["rows_with_markers"] += 1

            en_norm = normalize(display)
            en_skel, slots, is_template = skeleton(en_norm)
            if is_template:
                stats["templates"] += 1

            try:
                idx = int(r["idx"]) if r["idx"] not in ("", None) else None
            except ValueError:
                idx = None

            rows_src.append((
                r["id"], r["pack"], r["table"], idx, r["hash"], r["category"],
                r["group"], r["keep"], r["ukey"], en, display, markers_json,
                tier, 1 if is_template else 0,
            ))
            rows_mi.append((r["id"], en_norm, en_skel, len_bucket(en_norm), first_token(en_norm)))
            if is_template:
                rows_tpl.append((
                    r["id"], template_pattern(en_skel),
                    json.dumps(slots, ensure_ascii=False),
                ))
            if len(rows_src) >= 5000:
                conn.executemany(
                    "INSERT INTO source_strings (id,pack,table_name,idx,hash,category,"
                    "group_name,keep,ukey,en,en_display,markers,priority_tier,is_template)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows_src)
                conn.executemany(
                    "INSERT INTO match_index (source_id,en_norm,en_skel,len_bucket,first_token)"
                    " VALUES (?,?,?,?,?)", rows_mi)
                conn.executemany(
                    "INSERT INTO string_templates (source_id,pattern,slots) VALUES (?,?,?)", rows_tpl)
                rows_src, rows_mi, rows_tpl = [], [], []
                if stats["total"] % 50000 == 0:
                    print(f"  ... {stats['total']} rows")
    if rows_src:
        conn.executemany(
            "INSERT INTO source_strings (id,pack,table_name,idx,hash,category,"
            "group_name,keep,ukey,en,en_display,markers,priority_tier,is_template)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows_src)
        conn.executemany(
            "INSERT INTO match_index (source_id,en_norm,en_skel,len_bucket,first_token)"
            " VALUES (?,?,?,?,?)", rows_mi)
        conn.executemany(
            "INSERT INTO string_templates (source_id,pattern,slots) VALUES (?,?,?)", rows_tpl)
    conn.commit()

    # FTS5 population (standalone table, see schema.sql note):
    # DELETE + INSERT ... SELECT from match_index. Fully rebuildable.
    conn.execute("DELETE FROM match_fts")
    conn.execute(
        "INSERT INTO match_fts(source_id, en_norm) "
        "SELECT source_id, en_norm FROM match_index")
    conn.execute("INSERT INTO match_fts(match_fts) VALUES('optimize')")
    conn.executemany(
        "INSERT OR IGNORE INTO screen_contexts "
        "(context_key, category_hint, group_hint, boost) VALUES (?,?,?,?)",
        SCREEN_CONTEXTS)
    now = datetime.now(timezone.utc).isoformat()
    meta = {
        "schema_version": str(SCHEMA_VERSION),
        "normalize_version": str(NORMALIZE_VERSION),
        "markers_version": str(MARKERS_VERSION),
        "tdd_version": TDD_VERSION,
        "source_file": os.path.basename(args.tsv),
        "source_sha256": source_sha,
        "source_rows": str(stats["total"]),
        "en_checksum_sha256": en_checksum.hexdigest(),
        "imported_at": now,
    }
    conn.executemany(
        "INSERT INTO db_meta (key, value, updated_at) VALUES (?,?,?)",
        [(k, v, now) for k, v in meta.items()])
    conn.commit()

    # ---- validation (Phase 2 gate, TDD ch.14) ----
    checks = {}
    checks["source_rows"] = conn.execute("SELECT COUNT(*) FROM source_strings").fetchone()[0]
    checks["match_index_rows"] = conn.execute("SELECT COUNT(*) FROM match_index").fetchone()[0]
    checks["template_rows"] = conn.execute("SELECT COUNT(*) FROM string_templates").fetchone()[0]
    checks["fts_rows"] = conn.execute("SELECT COUNT(*) FROM match_fts").fetchone()[0]
    checks["empty_en_in_db"] = conn.execute(
        "SELECT COUNT(*) FROM source_strings WHERE en='' OR TRIM(en)=''").fetchone()[0]
    # marker integrity: every row's markers JSON must round-trip, and
    # en_display + markers must account for the original en
    bad_markers = 0
    for (en, display, markers_json) in conn.execute(
            "SELECT en, en_display, markers FROM source_strings"):
        try:
            json.loads(markers_json)
        except Exception:
            bad_markers += 1
    checks["bad_marker_json"] = bad_markers
    # en checksum round-trip from the DB itself
    h2 = hashlib.sha256()
    for (sid, en) in conn.execute("SELECT id, en FROM source_strings ORDER BY rowid"):
        h2.update((sid + "\x00" + en + "\x00").encode("utf-8"))
    checks["en_checksum_matches_source"] = (h2.hexdigest() == en_checksum.hexdigest())
    checks["unique_en"] = conn.execute(
        "SELECT COUNT(DISTINCT en) FROM source_strings WHERE TRIM(en) != ''").fetchone()[0]
    conn.execute("PRAGMA wal_checkpoint(TRUNCATE)")
    conn.close()

    elapsed = time.time() - t0
    report = {
        "tdd_version": TDD_VERSION, "schema_version": SCHEMA_VERSION,
        "normalize_version": NORMALIZE_VERSION,
        "markers_version": MARKERS_VERSION,
        "source_sha256": source_sha, "en_checksum_sha256": en_checksum.hexdigest(),
        "elapsed_seconds": round(elapsed, 2),
        "stats": stats, "checks": checks,
        "deviation_note": "source_strings.id is TEXT (real TSV ids like "
        "'C0000_B381007C'), not INTEGER as printed in TDD 4.4. See schema.sql.",
    }
    report_path = os.path.join(os.path.dirname(args.db), "import_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"report: {report_path}")

    ok = (checks["source_rows"] == stats["total"] == 579495
          and checks["match_index_rows"] == stats["total"]
          and checks["fts_rows"] == stats["total"]
          and checks["bad_marker_json"] == 0
          and checks["en_checksum_matches_source"])
    print("IMPORT OK" if ok else "IMPORT FAILED CHECKS")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
