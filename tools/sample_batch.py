"""Build the Phase 3 sample batch: 30 representative P0 strings.
10 UI (short labels), 10 subtitle (long, slang, dialogue), 5 templates
(money/numbers/placeholders), 5 with markers (~INPUT_~, ~n~, ~sl:).
Output: tools/sample_batch.json — the exact set the API-vs-local
decision is made from (TDD: decide at Phase 3 start from a sample batch).
"""
import json
import os
import sqlite3
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.common.markers import split_markers  # noqa: E402

DB = os.path.join(os.path.dirname(__file__), "..", "data", "gta6.db")
con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)

def pick(sql, n, label, seen):
    rows = con.execute(sql).fetchall()
    out = []
    for sid, en in rows:
        if sid in seen:
            continue
        seen.add(sid)
        display, mj, _ = split_markers(en)
        out.append({"id": sid, "group": label, "en": en,
                    "en_display": display, "markers": json.loads(mj)})
        if len(out) >= n:
            break
    return out

sample = []
seen = set()
sample += pick(
    "SELECT id, en FROM source_strings WHERE category='ui' AND LENGTH(en) BETWEEN 2 AND 25 "
    "AND TRIM(en) != '' ORDER BY id LIMIT 10", 10, "ui-short", seen)
sample += pick(
    "SELECT id, en_display FROM source_strings WHERE category='subtitle' "
    "AND LENGTH(en_display) > 60 ORDER BY id LIMIT 10", 10, "subtitle-long", seen)
sample += pick(
    "SELECT s.id, s.en FROM source_strings s JOIN string_templates t ON t.source_id = s.id "
    "WHERE s.priority_tier='P0' ORDER BY s.id LIMIT 5", 5, "template", seen)
sample += pick(
    "SELECT id, en FROM source_strings WHERE priority_tier='P0' AND markers LIKE '%sl:%' "
    "AND LENGTH(en) > 30 ORDER BY id LIMIT 50", 5, "with-markers", seen)
# LIMIT 50 (not 5): pick() skips ids already taken by the subtitle-long
# group, and the SQL LIMIT applies before that de-dup — LIMIT 5 yielded
# only 1 new row.
# NOTE: ~INPUT_~ markers do not occur in P0 at all (0 rows; the 869
# INPUT-marker rows live in P1 tutorial/description). The dominant P0
# marker type is ~sl: subtitle timing (22,978 rows), so the marker
# group tests those instead — previously this pick returned 0 rows
# and the batch shipped with 25 strings, not the intended 30.

out = os.path.join(os.path.dirname(__file__), "sample_batch.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(sample, f, ensure_ascii=False, indent=2)
print(f"wrote {len(sample)} strings to {out}")
for s in sample:
    print(f"[{s['group']}] {s['id']}: {s['en_display'][:110]!r}")
