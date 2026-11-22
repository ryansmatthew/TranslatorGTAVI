"""Load translations produced by Muse (the assistant) into `translations`.
Same rules as translate_batch.py: every row is validated first
(marker multiset/order, slots, length) and failures are quarantined
(printed, NOT written). A translation is applied to every source_id
sharing the same en_norm, with status 'machine', origin 'pipeline_muse'.

  python3 tools/load_muse_translations.py data/sample_batch_muse.json
"""
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.pipeline.validate import validate  # noqa: E402

if len(sys.argv) < 2:
    print("usage: load_muse_translations.py <translations.json>", file=sys.stderr)
    raise SystemExit(2)

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    items = json.load(f)

db = sqlite3.connect("data/gta6.db")
db.execute("PRAGMA journal_mode=WAL")
now = datetime.now(timezone.utc).isoformat()
done = quarantined = 0
# all source_ids already translated (built once; see note below on why
# the UNIQUE constraint can't be relied on when context_key is NULL)
already = {r[0] for r in db.execute(
    "SELECT source_id FROM translations WHERE status IN "
    "('machine','reviewed','approved')")}
for it in items:
    sid, vi = it["id"], it["vi"]
    row = db.execute(
        "SELECT s.en, m.en_norm, m.en_skel FROM source_strings s "
        "JOIN match_index m ON m.source_id = s.id WHERE s.id = ?", (sid,)).fetchone()
    if not row:
        print(f"QUARANTINE {sid}: not found in DB", flush=True)
        quarantined += 1
        continue
    en, en_norm, en_skel = row
    ok, reasons = validate(en, en_skel, vi, glossary=[])
    if not ok:
        print(f"QUARANTINE {sid}: {reasons} | en={en[:80]!r} vi={vi[:80]!r}", flush=True)
        quarantined += 1
        continue
    targets = [r[0] for r in db.execute(
        "SELECT source_id FROM match_index WHERE en_norm = ?", (en_norm,))]
    # skip targets already translated: the UNIQUE(source_id, version,
    # context_key) constraint does NOT fire when context_key is NULL
    # (SQLite treats NULLs as distinct), so INSERT OR IGNORE alone
    # would silently create duplicate rows for the same source_id.
    inserted = 0
    for tid in targets:
        if tid in already:
            continue
        db.execute(
            "INSERT INTO translations (source_id, vi, version, status, "
            "origin, context_key, created_at) VALUES (?,?,1,'machine','pipeline_muse',NULL,?)",
            (tid, vi, now))
        already.add(tid)
        inserted += 1
    done += inserted
db.commit()
db.execute(
    "INSERT INTO db_meta (key, value, updated_at) VALUES ('pipeline_backend', 'muse', ?) "
    "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
    (now,))
db.commit()
print(f"DONE muse_translations input={len(items)} translated_rows={done} "
      f"quarantined={quarantined}")
db.close()
