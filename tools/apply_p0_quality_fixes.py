"""Apply the 7 user-approved P0 quality-review fixes (2026-11-21).

Approved by the user ("duyệt cả 7 mục") after the P0 final report.
Decisions applied:
  1. "pussy" default crude "lồn"; fix the 2 S0840 cat misreadings only.
     ("hèn" kept where it means coward; "pussycat" -> "mèo con" untouched.)
  2. "fuck with" by sense; fix only S0142_AF3DBA69 ("thích").
  3. "skunk ape": keep loanword in UI labels (C0898), "vượn hôi" in dialogue
     (fix the 10 S0422 dialogue rows; S0424/S0567 already "vượn hôi").
  4. "Mr. Mangrove" -> "Ông Mangrove" everywhere (10 "Ngài" rows fixed).
  5. "Minimap" -> "Bản đồ thu nhỏ" everywhere (3 C0898 rows fixed).
  6. Restore "%" as "{number}%" (3 rows).
  7. S0705_0BC3777F "white boy" -> cocaine ("coke").

Each fix is an exact string replacement on the stored `vi`, asserted to
match exactly once (or the expected count). Status stays `machine`,
origin untouched. Run once; re-validates every changed row afterwards.
"""
import sqlite3
import sys

sys.path.insert(0, 'src/pipeline')
from validate import validate

DB = 'data/gta6.db'

# (source_id, old_fragment, new_fragment, expected_occurrences)
FIXES = [
    # 1. pussy cat misreadings
    ('S0840_8B70AAA0', 'một con mèo xinh đẹp', 'một con lồn xinh đẹp', 1),
    ('S0840_DE38CAED', 'con mèo to đùng', 'con lồn to đùng', 1),
    # 2. fuck with -> thích
    ('S0142_AF3DBA69', 'tao địt với đủ thể loại nhạc', 'tao thích đủ thể loại nhạc', 1),
    # 7. white boy = cocaine
    ('S0705_0BC3777F', 'tao hút một ít thằng da trắng Keys ngon',
     'tao hút một ít coke Keys xịn', 1),
    # 6. lost % sign
    ('C0898_3A87E3C0', 'Ừ {number} cái đó sus vãi', 'Ừ {number}% cái đó sus vãi', 1),
    ('C0898_556FBED7', 'Độ chính xác {number} ở mọi màn',
     'Độ chính xác {number}% ở mọi màn', 1),
    ('S0261_4A2B90B6', 'Nhóm {number}.', 'Nhóm {number}%.', 1),
]

# 3. skunk ape dialogue rows (S0422): loanword -> "vượn hôi"
SKUNK_APE_IDS = [
    'S0422_0794D363', 'S0422_12DC204B', 'S0422_18872D3C', 'S0422_19A37780',
    'S0422_319AFCF3', 'S0422_6E8D8968', 'S0422_84442189', 'S0422_89187B74',
    'S0422_AFFB0E03', 'S0422_CCBF6B74',
]

# 5. Minimap C0898 rows: "Bản đồ nhỏ" -> "Bản đồ thu nhỏ"
MINIMAP_IDS = ['C0898_48A01C61', 'C0898_C63C5811', 'C0898_C6F5F1E3']

db = sqlite3.connect(DB)
changed = []

def apply(sid, old, new, expected=1):
    row = db.execute(
        "SELECT t.vi, s.en, m.en_skel FROM translations t "
        "JOIN source_strings s ON s.id=t.source_id "
        "JOIN match_index m ON m.source_id=t.source_id "
        "WHERE t.source_id=? AND t.origin='pipeline_muse'", (sid,)).fetchone()
    assert row, f'no muse row for {sid}'
    vi, en, skel = row
    n = vi.count(old)
    assert n == expected, f'{sid}: expected {expected}x {old!r}, found {n} in {vi!r}'
    new_vi = vi.replace(old, new)
    db.execute("UPDATE translations SET vi=? WHERE source_id=? AND origin='pipeline_muse'",
               (new_vi, sid))
    changed.append((sid, en, skel, new_vi))

for sid, old, new, exp in FIXES:
    apply(sid, old, new, exp)

for sid in SKUNK_APE_IDS:
    row = db.execute(
        "SELECT t.vi, s.en, m.en_skel FROM translations t "
        "JOIN source_strings s ON s.id=t.source_id "
        "JOIN match_index m ON m.source_id=t.source_id "
        "WHERE t.source_id=? AND t.origin='pipeline_muse'", (sid,)).fetchone()
    assert row, f'no muse row for {sid}'
    vi, en, skel = row
    assert 'skunk ape' in vi.lower(), f'{sid}: no skunk ape in {vi!r}'
    new_vi = vi.replace('skunk apes', 'vượn hôi').replace('skunk ape', 'vượn hôi')
    assert 'skunk ape' not in new_vi.lower(), f'{sid}: leftover in {new_vi!r}'
    db.execute("UPDATE translations SET vi=? WHERE source_id=? AND origin='pipeline_muse'",
               (new_vi, sid))
    changed.append((sid, en, skel, new_vi))

# 4. Mr. Mangrove: all "Ngài Mangrove" -> "Ông Mangrove"
for (sid,) in db.execute(
        "SELECT source_id FROM translations WHERE vi LIKE '%Ngài Mangrove%' "
        "AND origin='pipeline_muse'").fetchall():
    row = db.execute(
        "SELECT t.vi, s.en, m.en_skel FROM translations t "
        "JOIN source_strings s ON s.id=t.source_id "
        "JOIN match_index m ON m.source_id=t.source_id "
        "WHERE t.source_id=? AND t.origin='pipeline_muse'", (sid,)).fetchone()
    vi, en, skel = row
    new_vi = vi.replace('Ngài Mangrove', 'Ông Mangrove')
    db.execute("UPDATE translations SET vi=? WHERE source_id=? AND origin='pipeline_muse'",
               (new_vi, sid))
    changed.append((sid, en, skel, new_vi))

for sid in MINIMAP_IDS:
    apply(sid, 'Bản đồ nhỏ', 'Bản đồ thu nhỏ', 1)

db.commit()
print(f'updated {len(changed)} rows')

# Re-validate every changed row with the pipeline validator
bad = 0
for sid, en, skel, vi in changed:
    ok, errs = validate(en, skel, vi)
    if not ok:
        bad += 1
        print(f'VALIDATE FAIL {sid}: {errs} | vi={vi!r}')
print(f'validated {len(changed)} rows, failures: {bad}')
assert bad == 0
print('ALL FIXES APPLIED + VALIDATED')
