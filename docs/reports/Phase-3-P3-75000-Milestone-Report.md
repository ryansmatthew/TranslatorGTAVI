# Phase 3 — P3 Milestone Report: 75,000 Unique Strings

**Date:** 2026-11-21 (after wave 73 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **75,435 / 357,142 (21.1%)**; P3 remaining **281,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 256,293 = distinct source_ids (no duplicates)
**Waves in this milestone period (69–73):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 69 | 1526–1535 | 71,435 | AAVE/street C0200 → police/radio C0201 → "woke"/wellness C0202 |
| 70 | 1536–1545 | 72,435 | "Woke" C0202 tail → street C0203 → conservative/redneck C0204 → AAVE C0205 |
| 71 | 1546–1555 | 73,435 | AAVE C0205–C0206 → alpha/bro/grindset C0207 → older conservative Watson Bay C0208 |
| 72 | 1556–1565 | 74,435 | Older/conservative C0208 → rich club-owner C0209 → British NPCs C0210 → tourists (German) C0211 → AAVE/club C0212 |
| 73 | 1566–1575 | 75,435 | AAVE/club C0212 → street C0213–C0214 → rich/Spanglish female C0215 |

## Incidents (all resolved, none outstanding)

- **Wave 69, chunk 1532:** first draft had 101 items (duplicate id pair C0201_EB040366 / C0201_EBAC0A72 at idx 85–86). Agent removed the extra item by script and re-checked 100/100 in order, 0 adjacent dups before loading; spot-check of the affected ids aligned on disk.
- **Wave 71, chunk 1551:** handoff never arrived. Output file verified on disk (100/100, ids in order, 0 adjacent dups; spot-checks aligned) and loaded per the established precedent. The handoff later arrived (2026-11-21 ~19:03) and a post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into MEMORY.md.
- **Wave 72, chunk 1560:** handoff never arrived; file verified on disk and loaded per precedent. Handoff later arrived; its notes folded into MEMORY.md (British C0210 voice, polite "tôi" / confrontational "tao/mày" split).
- **Wave 73, chunks 1566 / 1573:** handoffs never arrived. Both output files were found on disk and verified OK (100 items, ids in order, keys {id, vi}, 0 adjacent dups; spot-checks idx 0/49/99 aligned for both) and loaded per the established precedent. No agent notes available for these two chunks.
- **Waves 69 / 70 / 72 / 73 (other chunks):** no incidents. All files passed structure check (100 items, ids in order, keys {id, vi}, 0 adjacent dups) plus spot-checks.

## Conventions settled / reinforced in this period

- **British NPC voice (C0210, chunks 1560/1561):** polite/neutral lines use "tôi/bạn" ("Uhh, can I help you?" → "Ờ, tôi giúp gì được cho anh không?"); direct insults switch to "tao/mày". "mate" → "bạn ơi" (chunk 1561) vs kept loanword (chunk 1560); "arsehole" → "lỗ đít" (chunk 1561) vs "thằng khốn" (chunk 1560) — still inconsistent as a class. "bellend" → "đầu buồi" (literal, both chunks); "twat" → "lồn" (chunk 1561) vs kept loanword (chunk 1560) — still inconsistent. "wank stain" → "vết thủ dâm"; "tosser" → "thằng quay tay chết tiệt"; "pleb" → "thằng dân đen chết tiệt"; "piss off"/"sod off"/"jog on" → "cút đi"; "bloody hell" → "quái quỷ gì"/"chết tiệt"; "shag" → "ngủ với"; "Toodles" → "Tạm biệt nhé".
- **German tourist voice (C0211, chunks 1562–1564):** German words kept ("Auf Wiedersehen", "Blitzkrieg", "Scheisse", "Prost"); "Eurotrash" kept; "papi chulo" kept; polite/scared lines use "tôi", confrontation lines use "tao/mày".
- **"get laid"** → crude "được địt" side reinforced (chunk 1562 "I came to Vice City to get laid!" → "tao tới Vice City để được địt!") vs soft "được làm tình" (older chunks) — still inconsistent as a class.
- **"pussy"** → coward sense "đồ hèn" per the P0 rule is now the clear default in street contexts (chunks 1571/1572/1574/1575, multiple rows each); crude sense "lồn" only where the sentence is clearly sexual (chunk 1556 "Crazy pussy right there.").
- **"In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content** — the settled convention, used ×30 in chunk 1574 and ×~40 in chunk 1575 (C0215), including mid-sentence cues. Spanish words inside the content are kept (por favor, mija, idiota, cabron, Andale, Adiosito, mi reinita, mamasita, mami, Oye, cojones, ¡Adios!, ¡Vámonos!, ¿Hola?, ¿Policia?, ¡Dios mio!, ¡Por favor!, narcos).
- **"queen" → "chị đại"** (chunks 1569, 1575, per chunk 1508 precedent) — now settled.
- **"you got it"** → "mày thắng rồi" (concession side) in street/club contexts (chunks 1567, 1568, 1570) vs reassure side ("Tao lo cho mày", chunk 1568 "Any club you want, I got you!") — still by context.
- **"I got you"** — reassure side ("Tao lo cho mày", chunk 1568) vs caught/arrest side — still by context.
- **"trippin'"** → "phê" (default side, chunk 1569 "Nah, this weed got me trippin'.") vs don't-bother side (chunk 1567 "Don't even trip off us...") — still by context.
- **"fuck with"** → "dây với" (mess-with side) is now the default in street dialogue (chunks 1567, 1570, 1572); "thích" (like side) only where the sentence clearly means liking.
- **"ho" read as car** — chunk 1569 "Whatever, at least this ho still drive." → "Kệ đi, ít ra con xe này vẫn chạy được." (per "bitch"-as-car precedent, chunk 1511) — a real ambiguity class.
- **"motherfucker" read as weapon** — chunk 1569 "why you not concealing that motherfucker?" → "sao mày không giấu khẩu súng đó đi?" (per chunk 1511 precedent) — a real ambiguity class.
- **"call it quits"** → "dừng vụ này ở đây" (end-it side, chunk 1571) — now dominant.
- **"get down"** → "nằm xuống" (majority side, chunks 1575) vs "xuống đây" (high-place side, chunk 1568 "Come down!") — still by context.
- **"run a fade"** → "đánh tay đôi" (chunk 1567, per chunk 1510) — now settled.
- **"Sak kap fèt"** kept Haitian Creole (chunks 1565, 1567); **"Cardiaque"** kept as drug name (chunk 1565); **"clout"/"vibe"/"DM"/"bouncers"/"fam"/"bruh"/"yo"/"dog"** kept loanwords in AAVE/club chunks.
- **"daddy" → "bố" (majority side)** reinforced (chunk 1558 "Uhh, daddy." → "Uhh, bố ơi.") vs kept as flirtatious address (chunk 1489, chunk 1509).
- **"pigs" → "cớm"** (chunk 1571) vs "lũ lợn" (chunk 1572) — still inconsistent.
- **"lowkey"** — kept loanword (chunk 1568) vs "kín đáo" reading (chunk 1568 "I set this shit up lowkey!") vs "ngầm"/"thật ra"/"hơi" (earlier chunks) — still inconsistent.
- **"get off"** → "cút khỏi"/"cút ra" (dismissive side, chunks 1551/1565) vs "xuống khỏi" (high-place/person side, chunk 1562) — still by context.
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.
- **Police register (stable):** calls to police use polite "tôi" (chunks 1569, 1575); radio/reports use professional "tôi"; orders to suspects use "tao/mày" or direct imperatives.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1527 C0200_615CDA73, chunk 1528 C0200_A6F02807, chunk 1529 C0200_D3547161, chunk 1544 C0204_FDBA925F — all "Đi mà tự đụ đi". The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"VC"** — kept loanword (chunks 1557/1558/1568) vs "Vice City" — still inconsistent.
- **"heat"** — "súng" (chunk 1549) vs "độ nóng" (wanted level) — still by context.
- **"party-movil"** — kept (chunks 1556/1557) vs "xe tiệc" (chunk 1559) — still inconsistent.
- **"the Y" / "Y Hotel"** — kept as name vs "khách sạn Y" — still unresolved.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception (e.g. "Pay (~1$~)" → "({number})"); skeleton decimal splits; "3k" kept literal where the skeleton has no slot (chunk 1564).
- **"bitch"/"ho"/"motherfucker" read as car/weapon** — plausible by context but a real ambiguity class (chunks 1569, 1511, 1519).
- **Source artifacts preserved as-is:** C0208_BDEEC859 keeps the trailing "0301_AI_Main" internal-code suffix in both `en` and `vi` (chunk 1556); C0215_54F28C34 "Please hit me! In Spanish: Please!" rendered literally (chunk 1574).

## Next

- Wave 74 (chunks 1576–1585, C0215→C0218) is translating now.
- Next milestone: **80,000** (wave 78).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
