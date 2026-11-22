# Phase 3 — P3 Milestone Report: 130,000 Unique Strings

**Date:** 2026-11-21 (after wave 128 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **130,435 / 357,142 (36.5%)**; P3 remaining **226,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 130,435 = **216,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 319,446 = distinct source_ids (no duplicates)
**Waves in this milestone period (124–128):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 124 | 2076–2085 | 126,435 | Street/AAVE C0374 → civilian/flamboyant NPC C0375 → "patriot"/sovereign-citizen/conspiracy C0376 → store clerk / store robbery C0377 |
| 125 | 2086–2095 | 127,435 | Store-robbery tail C0377 → conspiracy-paranoid NPC C0378 → delusional/hallucinating NPC C0379 → dominance/submission C0380 → posh older rich lady C0381 |
| 126 | 2096–2105 | 128,435 | Posh lady C0381 → grumpy old man with dog Rufus C0382 → street/AAVE C0383 → female confrontational NPC C0384 → Big Mama / posh lady C0385 head |
| 127 | 2106–2115 | 129,435 | Big Mama / posh lady C0385 → sharp-tongued "auntie" C0386 → RydeMe driver / gig worker C0387 → wellness/new-age NPC C0388 head |
| 128 | 2116–2125 | 130,435 | Wellness/new-age C0388 → ex-Navy veteran / security guard C0389 → street/AAVE C0390 → C0391 head |

## Incidents (all resolved, none outstanding)

- **Wave 124, chunk 2077:** the first merged file had a mistyped id — C0375_2DE66B55ED instead of C0375_2DE66B4E ("Pump up the volume!") — the agent caught it in its own cross-check, fixed it and re-verified by script before finishing. All other chunks clean.
- **Wave 125:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 126:** the entire wave was loaded from disk-verified files before any handoff arrived, per the late-handoff precedent. Chunk 2096's agent had one failed merge exec in its progress log, but its final file on disk was complete and verified 100/100 before loading. Late handoffs were folded into the wave record afterwards; post-load DB checks verified 100/100 rows match the final files for all 10 chunks.
- **Wave 127:** loaded from disk-verified files before 3 handoffs arrived (2106, 2107, 2109); their notes were folded into the wave record afterwards. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 128, chunk 2113:** the first merge reported an id-order mismatch — the agent had mistyped C0387_6184492B instead of C0387_6184492D ("Screw it...") at idx 18; it fixed the id, re-merged and re-verified 100/100 in order before finishing. All other chunks clean.

## Conventions settled / reinforced in this period

- **"Big Mama" → "Mama Lớn"** (per chunk 2088, held in chunks 2096–2108; "North Wing" kept place name, C0385_050BA0F3). Capitalization note: chunks 2106/2107 wrote "Mama lớn" (lowercase "lớn") while chunks 2088/2108 wrote "Mama Lớn" — flagged for later review.
- **"auntie" → "dì"** (per chunks 2046/2047, held in chunks 2109, 2110, 2111); "home training" → "dạy dỗ ở nhà" per chunks 2068/2072 (chunk 2111); "granny gang" → "băng đảng bà già" (chunk 2111).
- **RydeMe / gig worker (C0387, wave 127):** "RydeMe" kept app name (chunks 2112, 2113, 2114, 2115); "gig worker" → "dân làm gig" (chunk 2113) / "thằng làm gig" (chunk 2114); "bookie" → "thằng cá độ" (chunks 2112, 2114) vs "chủ cái" (chunk 2113) — still inconsistent; "on sight" → "gặp mặt là xử luôn" per chunk 1807 (chunk 2113); "off the grid" → "trốn khỏi hệ thống" per chunk 2087 (chunk 2113); "paint job" → "lớp sơn xe" per chunk 2092 (chunk 2113); "go postal" → "nổi điên" (chunk 2113); "rock bottom" → "đáy vực" per chunk 2080 (chunk 2114); "touch grass" kept literally "đi chạm cỏ" (chunk 2114); "hip-check" → "húc hông" (chunk 2114); "service dog" → "chó nghiệp vụ" (chunk 2114); "Tight" → "Chất" (chunk 2114); "parlay" kept betting loanword (chunk 2115); "flow state" → "trạng thái flow" (chunk 2115); "dating pool" → "thị trường hẹn hò" (chunk 2115).
- **Wellness / new-age (C0388, waves 127–128):** "enlightened" → "giác ngộ" throughout (chunk 2115, C0388_126140C0, C0388_1C41A091, C0388_287A89D7); "toxic masculinity" → "nam tính độc hại" (chunk 2115); "heal holistically" → "chữa lành toàn diện" (chunk 2115); "sweat lodge" → "lều xông hơi" (chunk 2115); "vibe police" → "cảnh sát vibe" (chunk 2115); "bad vibes" → "vibe xấu" (chunk 2115); "vibes" kept loanword (chunk 2116); "empath" kept (chunk 2116, C0388_48538B51, C0388_5B7E76D0); "commune" kept (chunk 2116); "inner wolf" → "sói nội tâm", "Awoo!" → "Auuu!" (chunk 2116); "ayahuasca" kept (chunk 2116); "sound bath" → "buổi tắm âm thanh" (chunks 2115, 2118); "vibropractor" kept loanword, made-up word (chunk 2118); "love bomb" → "dội bom tình yêu" per chunk 2077 (chunk 2118); "FIB" kept (chunk 2118); "King Roger" kept guru name (chunk 2118); "Namaste" kept (chunk 2118); "K hole" kept (chunk 2118); "cooked" → "toang" passive side per chunks 2001/2062 (chunk 2116); "seventy-eight" → "bảy mươi tám" as words because the skeleton has no slot (chunk 2115); "six"/"four" kept as words because the skeleton has no slot (chunk 2115 C0387_F1A54AB3).
- **Ex-Navy veteran (C0389, wave 128):** "Navy" → "Hải quân" (chunks 2120, 2121); "civvie"/"civvies"/"civilian" → "dân thường" civilian-vs-military side (chunk 2120); "run a tight ship" → "quản lý mọi thứ chặt chẽ" (chunk 2120); "C.O." → "chỉ huy" (chunk 2120); "assholes and elbows" → "chổng mông chổng khuỷu" kept the military image (chunk 2120); "drill sergeant" → "trung sĩ huấn luyện" (chunk 2120); "PTSD" kept (chunk 2120); "battery powered USB sticks" → "mấy cái USB chạy bằng pin" (chunk 2121); "backup unit" → "đơn vị hỗ trợ" (chunk 2121); "missy" → "cô em" (chunk 2121); "boy" → "nhóc" when addressing a person vs "cún" when commanding the dog (chunk 2120); "my dog"/"him" read as a real dog throughout (chunk 2120).
- **Street / AAVE (C0390–C0391, wave 128):** "tweakin'" → "ngáo" per chunk 1957 (chunks 2123, 2124); "Bet" → "Chốt" (chunk 2123); "fuck all the way off" → "cút hẳn đi" (chunk 2123); "small fry" → "tép riu" (chunk 2123); "on sight" → "gặp mặt là xử luôn" per chunk 1807 (chunk 2124); "You want to go?" → "Mày muốn đánh nhau à?" fight side per chunk 1960 (chunk 2124); "get fucked" → "bị địt" passive per chunks 1782/1845 (chunk 2124); "GPS" kept (chunk 2124); "OD'ing" → "phê thuốc quá liều" (chunk 2124); "bogey" → "một thằng" target side (chunk 2124); "homie" kept (chunk 2124); "Gargle these nuts!" → "Súc miệng bằng hai hòn dái này đi!" per chunk 2083 ("Gargle my balls") (chunk 2124); "what you on" → "đang phê cái đéo gì" per chunk 1804 (chunk 2122); "get your ass on down" → "xuống đây" come-here (chunk 2122); "get on down" → "nằm xuống" default (chunk 2122); "Sic 'em!" → "Cắn bọn nó đi!" dog-command side (chunk 2122); "The Taint Lickers" → "Bọn Liếm Đáy Chậu" (chunk 2122); "chicky-dicks" → "mấy con gà con có cu" kept the source image (chunk 2122).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default (chunks 2104, 2105, 2106, 2110, 2111, 2123, 2124); crude sense "lồn" only where the sentence is clearly sexual (chunk 2109 C0386_071E55B7; chunk 2124 C0391_1E24DA0B body-part side); "pussy bitch" → "con đĩ lồn" (chunk 2104); "fat pussy" → "thằng hèn béo" coward (chunks 2104, 2105); "pussy-ass ho" → "con đĩ hèn" (chunk 2122).
- **"daddy"** → kept loanword as flirtatious address in chunks 2077/2079/2080 vs "bố" (majority side) — still by context.
- **"deep state"** → "nhà nước ngầm" (majority, chunks 2080–2083, 2086–2089) vs "chính phủ ngầm" — still inconsistent.
- **"heat"** → "cớm" police side (chunk 2097 C0382_0BFE3D54 "three digits away" = 911) vs its other unresolved senses.
- **"body count"** → sexual side "số người đã ngủ" (chunk 2100 C0382_F123660D) vs the P2 three-way split.
- **"on God"** → translated "thề với Chúa" (majority, chunks 2062/2063/2075) vs kept loanword — still inconsistent.
- **"literally"** kept as Gen-Z loanword per chunk 1926 (chunks 2111, 2112, 2116) — settled precedent in C0343–C0390.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines (chunks 2081, 2084, 2086, 2097, 2098, 2100, 2101, 2102, 2120) vs as a person elsewhere (chunks 2100, 2101, 2120, 2122) — by context.
- **"Rufus"** kept as the dog's name (chunks 2097, 2098, 2099, 2100).
- **"queen"** → "chị đại" (settled side, chunk 2078 C0375_44CBCB05) vs "nữ hoàng" sarcastic/literal elsewhere — still by context.
- **"run it"** → challenge side "Chơi tới đi" (chunk 2104 C0384_7AF3B8D8) / "chơi tới bến" (chunk 2105 C0384_FE2D8C97) — still inconsistent with "ra tay" / "kiếm chác" elsewhere.
- **"sugar daddy"** kept loanword per the "sugar baby" chunk-1786 precedent (chunk 2103 C0384_1408E7D9); "sugar babies" kept (chunks 2110, 2111).
- **Slots kept correctly this period:** "911" → "{number}" (chunk 2098 C0382_628FA1B8); "45" / "'83" → "{number}" (chunk 2099); "29 states" → "{number}" (chunk 2108); "since 1989" → "{number}" (chunk 2109); "200k" / "100k" / "10k" kept as numbers because the skeleton has no slot (chunks 2112, 2113); "six G's" → "sáu nghìn đô" (G = grand, chunk 2112 C0387_35019F17).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** One more crude-side row this period: chunk 2106 C0385_4A781FA0 "God, please, go fuck yourself!" → "Chúa ơi, làm ơn, đi mà tự đụ đi!". The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"Big Mama" capitalization** — "Mama lớn" (chunks 2106, 2107) vs "Mama Lớn" (chunks 2088, 2108) — inconsistent, needs a bulk fix once the form is decided.
- **"ASAP"** — translated "ngay lập tức" (chunk 2113 C0387_8C108F53; chunk 2047) vs kept loanword (chunk 2046; chunk 2079 C0375_A7934762) — still inconsistent.
- **"get laid"** — crude "được địt" (chunk 2111 C0387_0091EE30) vs soft readings elsewhere — unresolved.
- **"dominate / dominance" (C0380, wave 125)** — "khuất phục" / "thống trị" (chunk 2091) vs "áp đảo" (chunks 2093, 2094); "siêu thống trị cấp ba" (chunks 2091, 2092) vs "siêu áp đảo hạng ba" (chunk 2093) — inconsistent as a class.
- **"Null nie"** — kept as-is (chunks 2068, 2069, 2070); meaning unknown (possibly German "null nie" = "never ever") — unresolved.
- **"Dappa"** — kept as-is (chunk 2065 C0371_43CBEDF7) — meaning unknown, unresolved.
- **"wet wet"** — kept literal (chunk 2074 C0373_EACE2736) — meaning unknown, unresolved.
- **"chile"** — "cưng" (chunks 2072, 2073) vs kept loanword (chunk 2071) — still inconsistent.
- **"bless yo' heart"** — "Thương mày quá" sarcastic (chunks 2071, 2074) vs "Chúa phù hộ cho mày" (chunk 2072) — still inconsistent.
- **"plumb crazy"** — four renderings ("điên thật" / "điên hẳn" / "điên hẳn rồi" / "điên hết cả") — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword (chunks 2078, 2099, 2113) vs "Vice City" — still inconsistent.
- **"lowkey"** — many-way split (kept / "thật ra" / "kín đáo" / "ngầm" / "hơi") — still inconsistent.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address vs "Bố" when spoken to a dog — still by context.
- **"you got it"** — concession ("mày thắng rồi", chunks 2102, 2071, 2073) vs reassure vs agreement vs understand vs attention vs encouragement — still by context.
- **"I got you" / "I got it" / "gotcha"** — reassure vs understand vs caught — still by context.
- **"trippin'"** — many-way split ("phê" default / "nổi điên" / alarm / bother / don't-worry / don't-care / panicking / agitated "làm quá lên") — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent.
- **"bike"** — "xe đạp" (majority) vs "mô-tô" / "xe máy" (minority) — still inconsistent.
- **"body"** — corpse vs living person — by context; "bodies" corpse vs manpower — by context.
- **"bail"** — "bảo lãnh" vs "chuồn" vs "cứu ra khỏi vụ này" — still inconsistent.
- **"good looks"** — thanks vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" — by context.
- **"FYI"** — kept vs translated — still inconsistent.
- **"Madone!"** — kept — still undecided.
- **"mistress"** — "cô chủ" — still undecided.
- **"That's Negative."** — "phủ định" (majority) vs "Không phải." — still inconsistent.
- **"DOA"** — kept vs translated — still undecided.
- **"PIT"** — kept (waves 53–85) — still undecided.
- **"call it"** — many-way split (end-it side dominant) — still by context.
- **"officer down" / "casualty"** — dead-vs-hurt ambiguity ("cảnh sát gục rồi" deliberately covers both).
- **"US Army"** — "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" — still inconsistent.
- **"ma'am"** — "thưa bà" vs "thưa cô" vs "cô ạ" — still inconsistent.
- **"move out"** — "rút lui" vs "di chuyển thôi" — still inconsistent.
- **"shocker"** — device vs name — still undecided ("súng điện" majority side, chunk 2109; "súng chích điện" in chunk 2113 area — still split with "stun gun").
- **"stun gun"** — "súng chích điện" (majority) vs "súng điện" — still inconsistent.
- **"jerkoff"** — "thằng thủ dâm" vs "thằng quay tay" — still inconsistent.
- **"lib" / "libs" / "libtard"** — renderings vary.
- **"Fire"** — blaze vs gunfire — still by context.
- **"M7"** — unknown (kept).
- **"take a shot"** — three-way (shoot / drink / try / fight) — still by context.
- **"Skid mark"** — "Vệt phanh" vs "vết ố" — still split ("human skid mark" → "vệt cứt biết đi", chunk 2113 C0387_75EE7D77).
- **"Clown Town"** — translated vs place name — still inconsistent.
- **"Evil Eye"** — "Mắt Quỷ" vs loanword — still inconsistent.
- **"white trash" vs "trailer trash"** — handling split.
- **"vibe"** — kept vs translated — still by context.
- **"bag(s)"** — money vs drug sense — still by context.
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — "thao túng" (chunks 1896, 1972, 1973) vs kept — still by context.
- **"Tsou"** — kept as-is (chunks 1717, 1718) — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent ("ra tay" / "kiếm chác" / "đang hành động" / "chơi tới đi" / "chơi tới bến") — still inconsistent.
- **"bump"** — drug sense vs collision sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent.
- **"pheromones"** — kept loanword (chunks 1848, 1851, 1967) — now consistent.
- **"smoke" (conflict)** — "gây sự" vs drug side "hút thuốc" vs shoot side "bắn chết" — by context.
- **"go left"** — "toang" vs "rẽ sang hướng xấu" — still split.
- **"joint"** — a woman vs other readings — by context.
- **"on the gas"** — drug side in chunks 1881 and 1882 — driving alternative noted in both.
- **"pop it off"** — shoot side vs start-it ambiguous vs fight side — still by context.
- **"alpha"** — "kèo trên" vs "đầu đàn" vs kept — still split.
- **"Pussycat"** — kept as magazine name (chunk 1922 C0330_3E6829D5) vs "mèo con" per the P0 rule — flagged for review.
- **"the woes"** — gang reading vs female reading — by context.
- **"creampuff"** — literal "đồ bánh kem" vs weak-person "thằng bánh bèo" — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines vs as a person elsewhere — by context; "Lilith" read as a dog (chunk 1972) vs a person — by context.
- **"succubus"** — kept loanword vs "nữ quỷ" — still inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" vs "lồn bỏ túi" — minor inconsistency.
- **"fuck with"** — hang-out / like-side readings vs the mess-with default "dây với" — by context; dislike reading "không ưa" added in chunk 1950.
- **"fuck on"** — "cút đi" read as a "fuck off" variant vs sexual side when context is explicit — by context.
- **"crash on"** — attack side vs flirting side — by context.
- **"fuck your shit"** — dismissal side vs sexual side — by context.
- **"free lick"** — renderings vary ("vụ cướp dễ ăn" / "món hời dễ ăn" / "vụ ăn cắp miễn phí") — still inconsistent; "hit a lick" → "cướp được (một) vụ" consistent.
- **"parole"** — "việc tại ngoại" vs "án treo" — still inconsistent.
- **"pack"** — corpse vs drug package vs group/bầy — by context.
- **"cooked"** — active "đỉnh" vs passive "toang" — by context.
- **"Bitch move"** — "Nước đi hèn, con đĩ!" vs "Con đĩ, biến đi!" dismissal side vs "nước đi hèn" — by context.
- **"Hundo p."** — kept vs "a hundo p" → "một trăm phần trăm" — still inconsistent.
- **"cougar"** — see the deferred item above.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("unforetold" read as "untold", chunk 2113 C0387_85254996; "pickeball" read as "pickleball", chunk 2109 C0386_28B74C38; "then" read as "than", chunk 2077 C0374_F0481229; "Did you really just?" truncated, chunk 2078; "Hell happening over here?" missing "what the", chunk 2083; "Can you get from over there please?" missing "away", chunk 2086 C0377_E3BF3C56; "This between A and B, C your bitch ass..." garbled, chunk 2100 C0383_242E25C7); "worf" read as "worth", "Can't right no" read as "can't right now", "no you see" read as "now you see", "for I make ya" read as "before I make you", "accordian" read as "accordion" (chunks 2066–2067).

## Next

- Wave 129 (chunks 2126–2135, C0391→) is translating now.
- Next milestone: **135,000** (wave 133).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
