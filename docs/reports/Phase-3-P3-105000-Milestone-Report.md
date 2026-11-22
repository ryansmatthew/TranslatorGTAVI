# Phase 3 — P3 Milestone Report: 105,000 Unique Strings

**Date:** 2026-11-21 (after wave 103 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **105,435 / 357,142 (29.5%)**; P3 remaining **251,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 290,764 = distinct source_ids (no duplicates)
**Waves in this milestone period (99–103):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 99 | 1826–1835 | 101,435 | Spanglish/santera C0302 tail → street/AAVE C0303 → female street/AAVE C0304 → street/AAVE C0305 head |
| 100 | 1836–1845 | 102,435 | Street/AAVE C0305 → street/AAVE C0306 → swamp/rural Florida C0307 → swamp/river folk C0308 head |
| 101 | 1846–1855 | 103,435 | Street/swamp C0308 → swamp/hunter Florida C0309 → street/AAVE C0310 |
| 102 | 1856–1865 | 104,435 | Street/AAVE C0310 tail → street/AAVE C0311 → street/AAVE C0312 → beach/valley girl C0313 head |
| 103 | 1866–1875 | 105,435 | Beach/valley girl C0313 tail → ordinary/Gen-Z + shop-clerk C0314 → paranoid santera old lady C0315 → street/AAVE C0316 |

## Incidents (all resolved, none outstanding)

- **Wave 99, chunk 1834:** handoff arrived late (2026-11-21 ~20:03, after loading). The file had passed the full structure check on disk and was loaded per the established precedent; post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into the wave-99 MEMORY.md entry.
- **Wave 100, chunks 1843 and 1845:** handoffs arrived late (2026-11-21 ~20:04 and ~20:05, after loading). Same pattern: files verified on disk, loaded per precedent, post-load DB checks verified 100/100 rows match the final files for both — no reload needed. Notes folded into the wave-100 MEMORY.md entry.
- **Wave 101:** no incidents. All 10 handoffs arrived before loading. (Chunk 1847's output file appeared on disk at 20:06, after an earlier missing check, and its handoff arrived before loading.)
- **Wave 102, chunks 1860 and 1861:** output files were seen partial on disk at 20:09 (51 and 10 items) and complete (100/100) at 20:09:28; their handoffs arrived 2026-11-21 ~20:09:36 and ~20:09:43, after loading. The final files passed the full structure check before loading. Chunk 1860's agent also recorded one failed exec during its own verification step; the final file was verified independently. No reload needed.
- **Wave 102, chunk 1862:** handoff arrived late (2026-11-21 ~20:10, after loading). File verified on disk, loaded per precedent, post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into the wave-102 MEMORY.md entry.
- **Wave 103, chunks 1868 and 1873:** output files were seen malformed on disk at 20:11 (JSON parse errors — the agents were still writing them); their handoffs arrived 2026-11-21 ~20:11:46 and ~20:11:50, after loading had begun. The final files passed the full structure check before loading. Chunk 1873's agent also recorded one failed exec during its own verification step; the final file was verified independently. No reload needed.

## Conventions settled / reinforced in this period

- **Street/AAVE (C0303–C0316, the bulk of the period):** "fuck with" → "dây với" (mess-with side) remains the default; the like side appears only in clear flirting lines (chunks 1832, 1839, 1873 C0316_2FD13E82 "Fuck wit' me." → "Chơi với tao đi."); "trippin'" → "phê" (default) vs don't-care ("trippin' off") vs don't-worry; "I got you" / "I got it" → "tao lo cho mày" / "tao hiểu rồi" (reassure / understand, by context); "you got it" → "mày thắng rồi" (concession, dominant) vs "Được rồi, bro." (agreement, chunk 1865); "I'm out" / "bounce" / "dip" / "slide" → "chuồn" — settled; "on God" → "thề với Chúa" (majority side); "Bet." → "Chốt."; "lick" → "vụ cướp" (chunks 1840, 1860, 1862); "bread" → "tiền"; "whip" → "xe"; "strapped" → "mang súng"; "opp" kept loanword; "nigga(s)" kept loanword; "make moves" → "ra tay" (chunks 1781, 1850, 1874); "shoot the fair one" → "đánh tay đôi công bằng" (chunks 1841, 1863); "lock this shit down" → "khóa chặt chuyện này lại" (chunks 1835, 1845, 1875); "It's on sight" → "Gặp mặt là xử luôn" (chunks 1807, 1839, 1864); "flip a bitch" → "quay xe" (chunk 1859); "get smoked" → "bị bắn chết" (chunk 1864); "throw hands" → "đánh nhau" (chunk 1862); "go left" → "toang" (chunk 1862) vs "rẽ sang hướng xấu" (chunk 1863) — still split; "smoke" → "gây sự" (conflict side, chunks 1851, 1863).
- **Swamp / rural Florida (C0307–C0309, chunks 1844–1852):** "y'all" kept loanword; "fanboat" → "thuyền quạt"; "houseboat" → "nhà thuyền"; "gators" → "cá sấu"; "hunter" → "thợ săn"; "tour group" → "đoàn du lịch"; "boat tour" → "tour thuyền"; "moor up" → "neo thuyền"; "Speaky Ingles" kept (chunk 1850, per the "Habla Ingles?" chunk-1844 precedent); "freezer" → "tủ đông"; "get fucked" → "bị địt" (passive side).
- **Beach / valley girl (C0313, chunks 1864–1866):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content, heavy in this voice (7–14 items per chunk in C0313–C0315); "literally" → "thật sự" / "đúng nghĩa đen"; "loser" kept loanword; "VC" kept loanword; "sugar daddy" kept loanword (chunks 1786, 1864, 1865); "balsero" kept (chunk 1865); "bike bitch" → "con đĩ xe đạp" (chunk 1865); "Coño" / "Oye" / "Mira pa lante" / "Adios" kept Spanish; "wamp wamp wamp" kept as sound (chunk 1865); "buh-bye" → "Bái bai!".
- **Ordinary / Gen-Z NPC (C0314, chunks 1867–1869):** register "tôi/cậu" throughout for the ordinary/fear voice per the chunk-1802 precedent, "tao/mày" only in direct threats/insults; "highkey" → "thật sự" / "lắm luôn"; "lowkey" → "hơi" / "thật ra"; "deadass" → "thật đấy"; "vibe" / "aura" kept loanwords; "get lit" → "quẩy"; "lock in" → "tập trung vào"; "frickin'" / "freakin'" → "chết tiệt"; "whip" → "xe"; "code yellow" → "mã vàng"; "Snapmatic" kept; "squad" kept loanword.
- **Police register (stable, reinforced in C0314–C0315):** 911 calls and calls to police use polite "tôi" ("Chú cảnh sát ạ?", "Tôi đang bị cướp..."); "cops" → "cớm" in threat lines but "cảnh sát" in the 911 call itself; fear/begging lines use "tôi", confrontation/swearing lines use "tao/mày" (chunk 1800/1801 precedent).
- **Shop clerk being robbed (C0314, chunk 1868):** register split per the chunk-1800/1801 precedent — fear/begging/police-call lines use polite "tôi", confrontation/swearing lines use "tao/mày"; "rager" → "bữa quẩy"; "baller" → "đại gia"; "vibe check" kept; "cringe" kept; "IRL" kept.
- **Paranoid santera old lady (C0315, chunks 1870–1872):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (11–17 items per chunk); Spanish kept (Mierda, Satanas, mamita, mija, Oye, dios mio, culo, ayahuasca, Demonio, Coño); "clone" → "bản sao"; "devil" / "demon" → "quỷ"; "Illuminati" kept; "socialists" → "lũ xã hội chủ nghĩa"; "spiritual enema" → "thụt rửa tâm linh"; "colonic irrigation" → "thụt rửa ruột kết"; "collapsed arches" → "vòm bàn chân bị sụp"; "pearly gates" → "cổng ngọc"; "orgasmo" kept (chunk 1871); "sixty percent" kept in words (no slot in skeleton).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts; crude sense "lồn" only where the sentence is clearly sexual (chunks 1842, 1846, 1855, 1856, 1859, 1860); "pussy bitch" → "con đĩ lồn" (general insult); "pussies" female side vs coward side by context (chunk 1843).
- **"daddy"** → "bố" (majority side, chunks 1846, 1855) vs kept loanword as flirtatious address (chunk 1853 C0310_270DEF92, per chunks 1489/1509/1781/1786) vs "Bố" when spoken to a dog (chunk 1800) — still by context.
- **"get down"** → now six ways: "nằm xuống" (majority) vs "xuống khỏi đó" (high-place) vs "xuống đây" (come-here) vs "quẩy" (party) vs "đánh nhau" (fight, chunk 1849) vs "cúi xuống" (chunk 1867, before a backflip) — still by context.
- **"get fucked"** → "bị địt" (passive side, chunks 1851, 1865) vs active readings elsewhere — still by context.
- **"joint"** → a woman (chunks 1863, 1872) vs other readings — still by context.
- **"sumbitch"** → "khẩu súng chết tiệt", read as the gun by context (chunk 1854 C0310_88658EAC, silver-bullet context).
- **Slots kept correctly this period:** "911" → `{number}` (chunks 1847, 1867); "6969" → `{number}` (chunk 1868); "magic 8 ball" → "quả bóng ma thuật {number}" (chunk 1854); numbers kept as words where the skeleton has no slot ("one-eighty", "a hundred yards", "sixty percent", "eighty-seven percent").
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1846 C0308_27950089 "Yeah, alright, fuck yourself." → "Ừ, được rồi, tự đụ đi." and C0308_3B1B62D1 "Ugh. Go fuck yourself, man!" → "Ugh. Đi mà tự đụ đi, man!" (the agent noted the decision is still pending; if the user picks the softened side these two rows need fixing). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1869 renders "Eff off!" as "Đệt, cút đi!" (C0314_BFC04472, per the chunk-1802 precedent). Still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address (chunk 1853) vs "Bố" when spoken to a dog — still by context.
- **"you got it"** — concession ("mày thắng rồi") vs reassure vs agreement ("Được rồi, bro.") vs understand — still by context.
- **"I got you" / "I got it" / "gotcha"** — reassure ("tao lo cho mày") vs understand ("tao hiểu rồi") vs caught ("tao tóm được mày rồi") — still by context.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"go left"** — "toang" (chunk 1862) vs "rẽ sang hướng xấu" (chunk 1863) — still split.
- **"smoke"** — conflict side ("gây sự", chunks 1851, 1863) vs drug side ("hút thuốc", chunk 1873) — still by context.
- **"get down"** — six ways now (see conventions) — still by context.
- **"get fucked"** — passive "bị địt" vs active readings — still by context.
- **"boy" read as a dog** in guard-dog/K9 command lines (chunks 1791, 1796, 1798, 1799) vs as a person elsewhere — by context.
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunks 1764, 1795) — still inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797) — minor inconsistency.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("Tskm" → "Tsk", chunk 1853; "Your hear something you like?" → "Mày nghe thấy thứ gì mày thích à?", chunk 1849; "one more one word" → "one more word", chunk 1854; "Hell even was that?" read as intended, chunk 1854).

## Next

- Wave 104 (chunks 1876–1885, C0316→) is translating now.
- Next milestone: **110,000** (wave 108).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
