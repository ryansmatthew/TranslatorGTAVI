# Phase 3 — P3 Milestone Report: 70,000 Unique Strings

**Date:** 2026-11-21 (after wave 68 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **70,435 / 357,142 (19.7%)**; P3 remaining **286,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 250,489 = distinct source_ids (no duplicates)
**Waves in this milestone period (64–68):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 64 | 1476–1485 | 66,435 | Karen/conservative C0185 → AAVE/street C0186–C0187 |
| 65 | 1486–1495 | 67,435 | AAVE/street C0187 tail → police/radio C0188–C0190 |
| 66 | 1496–1505 | 68,435 | Police/radio C0190–C0191 → AAVE/street C0192 → police C0193 → rich sassy female C0194 |
| 67 | 1506–1515 | 69,435 | Rich sassy female C0194 → AAVE/street C0195–C0196 |
| 68 | 1516–1525 | 70,435 | AAVE/street C0196 → police/radio C0197 → AAVE/street C0198 → older female/Spanglish C0199 → AAVE/street C0200 |

## Incidents (all resolved, none outstanding)

- **Wave 64, chunk 1484:** first draft had 102 items (agent duplicated C0187_8F11E310 and C0187_8F6BA027). Agent removed the duplicates by script; disk re-check confirmed exactly 100 items in input order before loading.
- **Wave 65, chunks 1487 / 1488 / 1495:** handoffs arrived late. Per the established precedent, output files were verified on disk before loading; post-load DB checks verified all 100 rows match the final file for each chunk (no reload needed). Notes folded into MEMORY.md.
- **Wave 66 / 67 / 68:** no incidents. All 10 handoffs per wave arrived before loading; all files passed structure check (100 items, ids in order, keys {id, vi}, 0 adjacent dups) plus spot-checks.

## Conventions settled / reinforced in this period

- **Police register (stable):** radio/reports use polite professional "tôi" ("Dispatch" → "trung tâm điều phối", "perp" → "nghi phạm", "officer down" → "cảnh sát gục rồi", "stun gun" → "súng chích điện", "ASAP" → "ngay lập tức"); orders to suspects use "tao/mày" or direct imperatives. Exceptions noted: chunk 1466's gruff "tao" police call; chunk 1516's radio line in "tao" (officer reporting to a teammate).
- **Unit numbers:** "238" (chunks 1497/1498/1499), "299" (chunks 1486–1488), "531" (chunks 1493–1495), "476" (chunks 1516–1518), "514" (chunks 1502–1505) → `{number}` slots, all kept.
- **"PIT" kept** as loanword across all police waves (vs "húc xoay" — still unsettled as a class, but "PIT" is the standing side).
- **"call it"** → "dừng vụ này ở đây" (end-it side) is now dominant in police contexts (chunks 1427, 1436, 1478, 1493, 1497, 1516).
- **"get down"** → "nằm xuống" (majority side) across police and street contexts; pool-party "quẩy" (chunk 1467) and fight sense remain context-dependent exceptions.
- **"fuck with"** → "dây với" (mess-with side) is now the default in street dialogue; "thích" (like side) only where the sentence clearly means liking (e.g. chunk 1507 "I fuck with that!").
- **"pussy"** → coward sense "đồ hèn" per the P0 rule in most street contexts; crude sense "lồn" only where the sentence is clearly sexual (e.g. chunk 1500 "dry ass pussy", chunk 1514 "you don't like pussy?", chunk 1515 "lick my pussy" in earlier waves).
- **"sugar daddy" → "bố đường"; "sugar baby" → "bé đường"** (chunk 1506) vs kept loanword (chunk 1509) — still inconsistent as a class.
- **"Daddy" → "bố" (majority side)** in C0194 (chunks 1507/1508), vs kept as flirtatious address in chunk 1489 and chunk 1509 ("What's up, Daddy?").
- **"In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content** — the settled convention, used ×30 in each of chunks 1523/1524/1525 (C0199). Spanish words inside the content are kept (gracias, amor, Dios Mio, abuelita, hyna).
- **Furry joke continues:** "furry" kept loanword; "paws" → "chân" in furry contexts (chunks 1498/1499/1505) vs "tay" where there is no furry context (chunks 1418, 1514).
- **"get dropped" → "bị hạ gục"; "get popped" → "bị bắn"; "get smoked" → "bị xử"** — settled in street dialogue.
- **"I got you"** — reassure side ("Tao lo cho mày", chunks 1436/1485/1513/1517) vs caught/arrest side (chunks 1488/1491) — still by context.
- **"trippin'" → "phê" (default side)** vs don't-bother side (chunk 1483, chunk 1510 "I wasn't trippin' off...") — still by context.
- **"muttin'" → "làm hỏng"** (chunks 1434, 1482, 1519) — now the settled side vs earlier "lẩm bẩm"/"cư xử ngu ngốc".
- **"bike" → "xe đạp" (majority side)** vs "xe máy" (chunk 1520 "my motherfuckin' bike" read as motorbike) — still by context.
- **"body" → "cái xác" (majority side)** for corpses; "casualty" → "người thương vong" (covers dead/injured, unsettled).
- **"FD" → "đội cứu hỏa"** (chunks 1398, 1499) vs kept (chunk 1399) — still inconsistent.
- **"EMS" kept** (chunk 1517) vs "đội cứu hỏa" for FD — inconsistent as a class.
- **"take a shot"** — three-way (shoot / drink / try) still unsettled; chunk 1521 used the shoot side, chunk 1504 the try side.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1523 C0199_465AD62C ("Go fuck yourself." → "Đi mà tự đụ đi.", with the "In Spanish:" cue). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"get laid"** — crude "được địt" (chunks 1454/1458/1460) vs soft "được làm tình" (chunks 1455/1456, old-lady voice) — still inconsistent.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"lowkey"** — "ngầm" vs "thật ra" vs "hơi"/degree reading vs kept loanword — still inconsistent.
- **"VC"** — "Vice City" vs kept loanword — still inconsistent.
- **"heat"** — "súng" (chunk 1522 "leave ya heat with me") vs "độ nóng" (wanted level) — still by context.
- **Slot-forced awkwardness** continues: unit numbers and "411" forced into `{number}` slots; "$"-loss via the placeholder-slot exception continues (e.g. "Pay (~1$~)" → "({number})").
- **"bitch" read as car/weapon** in several street lines (chunks 1511, 1519 "I'm in that ho!") — plausible by context but a real ambiguity class.

## Next

- Wave 69 (chunks 1526–1535, C0200→C0202) is translating now.
- Next milestone: **75,000** (wave 73).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
