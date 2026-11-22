# P0 Quality-Review Checklist (DRAFT — snapshot, re-run after P0 completes)

Prepared 2026-11-21 ~13:20 +07 (Asia/Bangkok), from a read-only check of
`gta-vi-vi-translator/data/gta6.db` while wave 37 was still loading.
At that moment: 90,822 translation rows (up from 87,915 at the 35,000 milestone),
all 365 chunk outputs on disk, P0 at 35,530 / 39,003 unique strings (~91%) per the
35,000 milestone report. Counts below are a snapshot — re-run the queries after
the final P0 report before applying any fix, because wave 37 rows were still landing.

All rows are status `machine`, so every fix below is a DB update, not a re-translation.
Source IDs are given so fixes can be applied by ID.

## Decisions needed (pick one rendering per term, then bulk-fix the rest)

### 1. "pussy" — 3 registers in the DB (205 translated rows containing "pussy")
- Crude "lồn": 178 rows (the dominant, intended register for insults/sex).
- Softened "hèn" (coward): 16 rows — e.g. C0081_6073489D "You pussy." → "Đồ hèn.",
  C0380_57BC7373 "level fourteen pussies" → "mấy thằng hèn cấp mười bốn".
  Note: in those lines "pussy" really means coward, so "hèn" may be *correct*, not a
  softening — decide per line, don't blanket-replace.
- Literal cat "mèo": 4 rows — the real errors:
  - S0840_8B70AAA0 "Shit, I'm a good-looking pussy..." → "một con mèo xinh đẹp" (wrong: means a hot person)
  - S0840_DE38CAED "Oh, big ol' pussy!" → "con mèo to đùng!" (check scene context; likely crude, not a cat)
  - S0840_CC99144D mixes both: "big cats" → "mèo lớn" (correct) but "get some pussy" → "chịch gái" (acceptable) — probably fine as-is.
  - S0928_02EF436C "Where'd you go, pussycat?" → "mèo con" — CORRECT, "pussycat" is literally a cat. Do not touch.
- Decision: confirm "lồn" as default for "pussy" (insult/sex), keep "hèn" where it means
  coward, fix the 2 S0840 cat readings.

### 2. "fuck with" — 3 senses, not 1 inconsistency (46 rows)
- "thích" (like): 4 rows, e.g. S0103_242CB8D8 "You fuck with me?" → "Mày thích tao à?" — correct.
- "đùa / chọc phá" (mess with): 4+ rows, e.g. S0715_3BFC4756 "Don't fuck with me!" →
  "Đừng có đùa với tao!" and S0734_4666B712 "fuck with our camp" → "đùa với trại" —
  acceptable for the "mess with" sense, though "đụng vào / gây sự với" may fit better.
- Literal "địt với": 1 clear error — S0142_AF3DBA69 "I fuck with all kinds of music" →
  "tao địt với đủ thể loại nhạc" (should be "thích").
- Decision: keep sense-based rendering (thích / đừng đụng vào), fix only S0142_AF3DBA69
  and check the remaining ~37 rows for which sense each line uses.

### 3. "skunk ape" — loanword vs "vượn hôi" (22 rows)
- Keeps "skunk ape": 14 rows — mostly UI labels where it is arguably a proper noun:
  C0898_081E425D "SKUNK APE CROSSING" → "SKUNK APE BĂNG QUA ĐƯỜNG",
  C0898_C80F125D "Search for the Skunk Ape" → "Tìm Skunk Ape",
  C0898_CB69E1A3 "Advanced Skunk Apeonomics" → unchanged.
  But dialogue S0422 also keeps it: S0422_0794D363 "Oh it's a skunk ape..." → "nó là skunk ape".
- "vượn hôi": 8 rows, all dialogue S0424, e.g. S0424_E7279C27.
- Decision: likely rule = keep loanword in UI labels / proper-noun uses, "vượn hôi" in
  dialogue — then fix the S0422 dialogue rows to "vượn hôi" (or decide the reverse
  and fix S0424). Do not blanket-replace the UI labels without deciding.

### 4. "Mr. Mangrove" — "Ông" vs "Ngài" in the SAME scene (32 rows)
- "Ông Mangrove": 5 rows, all S0424 (e.g. S0424_A426A113).
- "Ngài Mangrove": 10 rows, also mostly S0424 (e.g. S0424_54FF3445, S0424_78DF86CC)
  plus C1092_A8F0FAFA "Mister Mangrove???" and S0593_6DBDCC82 "Mister Mangrove".
- Decision: pick one ("Ông" fits the swamp-cryptid tone better; "Ngài" is more formal).
  Same-scene split, so this is a clean bulk fix once decided.

### 5. "Minimap" — split by pack, easy bulk fix (11 rows)
- "bản đồ nhỏ": 7 rows, all C0898 (e.g. C0898_48A01C61 "Minimap (Dynamic)").
- "Bản đồ thu nhỏ": 4 rows, all C1090 (e.g. C1090_05FB301F "Minimap").
- Decision: pick one rendering; the split is systematic per pack, so it is a
  find-and-replace by pack, not 11 individual judgements.

### 6. Lost "%" sign — only 3 rows (36 translated rows contain "%" in English)
- C0898_3A87E3C0 "Yah 100% that's sus af" → "Ừ {number} cái đó sus vãi" (lost %)
- C0898_556FBED7 "100% Accuracy in all Stages" → "Độ chính xác {number} ở mọi màn" (lost %)
- S0261_4A2B90B6 "The 0.00001%." → "Nhóm {number}." (lost %)
- Fix: render as "{number}%" as chunk 333 already does ("1.3%" → "{number}%").

### 7. "white boy" = cocaine in one line
- S0705_0BC3777F "I smoke some fine Keys white boy..." → "tao hút một ít thằng da trắng
  Keys ngon..." — wrong: "smoke white boy" is drug slang (cocaine/crack), "Keys" is
  the Florida Keys. All other sampled "white boy" rows are literally a white person
  and fine. Fix just this one (check S0208 "white girls" the same way — sampled rows
  look literal, but the drug reading was flagged in the 25,000 milestone).

## How to re-run after P0 completes
```sql
-- counts per term (read-only, on a copy or mode=ro)
SELECT COUNT(*) FROM source_strings s JOIN translations t ON t.source_id=s.id
WHERE lower(s.en) LIKE '%pussy%' AND t.vi LIKE '%mèo%';
-- same pattern for '%lồn%', '%hèn%', '%fuck with%', '%skunk ape%', 'Mangrove', 'Minimap', '%\%%'
```
Then apply fixes by source_id (listed above) with status kept `machine` until the
review pass signs them off.
