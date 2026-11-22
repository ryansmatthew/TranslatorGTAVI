# Phase 3 — P3 Milestone Report: 140,000 Unique Strings

**Date:** 2026-11-21 (after wave 138 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **140,435 / 357,142 (39.3%)**; P3 remaining **216,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 140,435 = **226,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 330,887 = distinct source_ids (no duplicates)
**Waves in this milestone period (134–138):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 134 | 2176–2185 | 136,435 | Street/AAVE C0411–C0412 (heavy "In Spanish:" counts) → gym-bro C0413 → street/AAVE C0414 → C0415 head (macho challenge / muscle-pride) |
| 135 | 2186–2195 | 137,435 | Gym-bro / alpha-beta / manosphere C0415 → street/AAVE C0416–C0417 → C0418 → C0419 head |
| 136 | 2196–2205 | 138,435 | Shop-clerk robbery voice C0419–C0421 → metalhead / mosh pit C0422 → shop-clerk robbery voice C0423 |
| 137 | 2206–2215 | 139,435 | Shop-clerk robbery voice C0423–C0425 → police voice C0426 → street/AAVE + "In Spanish:" C0428 |
| 138 | 2216–2225 | 140,435 | Street/AAVE + "In Spanish:" C0428–C0429 → police voice C0430 → posh rich / foreign NPC C0431 → Southern old-lady / homeless voice C0432 |

## Incidents (all resolved, none outstanding)

- **Wave 134:** no incidents. Chunks 2183 and 2185 handoffs arrived late and were folded into the wave record afterwards. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 135:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 136:** no incidents. All 10 files were complete and verified on disk before loading; chunks 2200 and 2201 were loaded from disk-verified files before their handoffs arrived (post-load DB checks ran 100/100 each); the chunk 2205 handoff arrived late and its notes were folded into the wave record afterwards.
- **Wave 137:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 138:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.

## Conventions settled / reinforced in this period

- **Shop-clerk robbery voice (C0419–C0425, waves 135–137):** clerk begging / police lines intentionally "tôi/cậu", confrontation "tao/mày" (chunks 2127–2133, 2149–2153, 2170–2171, 2196–2209); "register" → "ngăn kéo tiền" per the "Till"/"Cash Drawer" precedent (chunks 2196, 2197, 2201); "safe" → "két" per chunk 2131 (chunks 2196, 2199, 2200, 2208); "bulletproof glass" → "kính chống đạn" (chunks 2197, 2201, 2210); "ATM" kept (chunks 2196, 2199, 2201, 2206, 2218); "Snapmatic" kept app name (chunks 2208, 2210); "Peekhole" kept app name (chunks 2200, 2201); "Kitty Litter" kept as-is — drug name vs cat litter still undecided (chunk 2201 C0421_9061A132); "911" → "{number}" (chunks 2196, 2198, 2201); "cops" → "cớm" throughout; "movin' weight" → "chuyển hàng" drug-dealing side (chunks 2198, 2208); "smoke your ass" → "bắn chết mày" shooting side per chunk 2138 (chunk 2199 C0420_FB38FF8F); "get down" default "nằm xuống" in the robbery (chunks 2204, 2208, 2209) vs come-here "xuống đây" (chunk 2198) vs high-place "xuống khỏi đó" (chunks 2196, 2200, 2206).
- **Metalhead / mosh pit voice (C0422, wave 136):** "headbutt" → "húc đầu" throughout (chunk 2202); "mosh pit" → "hố mosh" (chunk 2202) vs kept loanword (chunk 2203); "metal" / "sludge metal" / "metalcore" / "Death Metal Week" kept (chunk 2202); "metalhead" kept loanword (chunk 2203); "sellout" → "Đồ bán rẻ" (chunk 2202 C0422_369E131E) vs "bán linh hồn" (chunk 2203, 4 occurrences) — still inconsistent; "poser" kept (chunk 2203); "square" → "thằng vuông vức" (chunk 2202); "shill" → "thằng tay sai" (chunk 2202); "Nu Metal Appreciation Month" → "Tháng Tri Ân Nu Metal" (chunk 2203); "DIY show" kept (chunk 2203); "Kowaachobee" kept name (chunk 2203).
- **Police voice (C0426, C0430, waves 137–138):** "Dispatch" → "trung tâm điều phối" per P0; direct orders to suspects in "tao/mày", radio self-reports in "tôi" per the police/service-call precedent (chunks 2211, 2213, 2219, 2220, 2221) — with one excited radio call still in "tao" (chunk 2221 C0430_A6B55F96 "Ôi, trung tâm điều phối! Tao tóm được thằng furry ngay đây rồi!"); "PIT" kept (chunks 2211, 2212, 2219, 2220, 2221); "perp" → "nghi phạm" (chunks 2211, 2212, 2213, 2219, 2222) vs "thủ phạm" (chunk 2213); "Officer down" → "cảnh sát gục rồi" (chunks 2212, 2219, 2220); "SWAT" kept; "K9" kept; "cruiser" → "xe tuần tra"; "shocker" → "súng điện" device side (chunks 2211, 2222); "stun gun" → "súng chích điện" (chunk 2219); "COs" → "cán bộ quản chế" per the "P.O." precedent (chunk 2220 C0430_3C11ADF5); "furry" kept loanword throughout (chunks 2211, 2212, 2213, 2220, 2221); "furry vehicle" → "xe furry" (chunk 2221); "paws" → "chân" K9 dog side (chunk 2212; chunk 2219 C0430_076B3176) vs "tay" hands side when police order a suspect's hands up (chunk 2222 C0430_F9A695ED — flagged, may need fixing); "visual" → "mục tiêu" / "mất dấu" in lost-sight context (chunks 2211, 2221, 2222); "back the blue" → "ủng hộ cảnh sát" (chunks 2211, 2212); "calling it" → "kết thúc vụ này" end-it side (chunks 2213, 2221); "Set the box!" → "Chặn nó lại!" PIT box-in maneuver (chunk 2212); "lock this shit down" → "khóa chặt cái cứt này lại" (chunks 2212, 2221); "set a perimeter" → "lập vòng vây" (chunk 2221); "taking fire" → "đang bị bắn" (chunk 2221); "pinned down" → "đang bị kìm chân" (chunk 2221); "fire rescue" → "cứu hỏa" (chunk 2221); "runner" → "kẻ chạy trốn" (chunks 2211, 2220); "body" → "cái xác" corpse side (chunks 2211, 2220, 2222); "724" → "{number}" (chunks 2220, 2221, 2222); "267" → "{number}" (chunks 2211, 2212, 2213); "10-91" → "{number} {number}" (chunk 2213 C0426_D24C5CA2).
- **Street / AAVE + "In Spanish:" (C0428–C0429, waves 137–138):** "In Spanish:" cues rendered "Nói tiếng Tây Ban Nha:" + translated content throughout — heaviest counts this period: chunk 2214: 45 cues; chunk 2215: 44 cues; chunk 2216: 35 cues; chunk 2217: 29 cues; chunk 2218: 19 cues; chunk 2219: 14 cues. Spanish words kept per chunk 2214 ("Coño", "¡Agárralo!", "Discúlpame", "¡Mira!", "jalabolas", "pelabola", "¡Nada!", "¡Aquí está!", "Coño 'e la madre...", "Bienvenidos.", "Psicópata...", "Obviamente...", "Un momento. ¿Qué?", "Ay jesucristo!", "¡Vete!", "¡Por favor!", "¡Jesus Cristo!", "¡Ay puñeta!", "¡Oye-oye!", "gracias", "reina", "¡Attaca!", "Qué...", "careverga", "Oye", "pana", "adiós", "bebesote", "mami"); "yeyo" kept loanword (chunks 2216, 2208); "fuck with" → "dây với" mess-with default; "go" → "đánh nhau" challenge side per chunk 1960 (chunks 2216, 2217); "get down" default "nằm xuống" vs come-here "xuống đây" (chunk 2218 C0429_A8F1E3BA); "you got it" → "mày thắng rồi" concession per chunks 2038/2065 (chunks 2218, 2219); "vibes" kept loanword per chunks 2115–2117 (chunk 2217); "tough love" → "yêu thương cứng rắn" (chunk 2217); "literally" kept as Gen-Z loanword per chunk 1926 (chunk 2219 C0429_C5340C24).
- **Gym-bro / alpha-beta / manosphere (C0415, wave 135):** "alpha" kept, "beta male" → "thằng beta", "shit test" kept, "dysphoria" kept, "body count" kept sexual, "high-value man/male" → "người đàn ông giá trị cao", "low-value individuals" → "mấy đứa giá trị thấp", "pussified" → "bị hèn hóa", "grindset mindset" → "Tư duy cày cuốc", "T levels" → "mức T", "low T" → "testosterone thấp", "tetherball" kept, "biohacking apps" kept, "beast mode" kept; "bench" → "đẩy tạ" per chunk 2182; "bulking" → "xả cơ", "cut" → "siết cơ" (chunk 2181); "tapped out" → "đầu hàng" (chunk 2180); "150 pounds" → "{number}" (chunk 2182); "911"/"375" → "{number}" slots (chunk 2186).
- **Posh rich / foreign NPC (C0431, wave 138):** "tôi/cậu" throughout per the posh precedent (C0403/C0408, chunks 2154–2157, 2167–2169), keeping the posh tone even when swearing; "habibi"/"habibti" kept (chunks 2222, 2223, 2224); "Alhamdulillah" kept (chunk 2223); "haram" kept (chunk 2223); "penthouse" kept (chunk 2223); "my love" → "em yêu" (chunk 2223); "my friend" → "bạn tôi" (chunk 2223); "boss" → "sếp" (chunk 2222) vs kept (chunk 2223) — still split; "chief" → "sếp" (chunk 2224) vs kept (chunk 2223) — still split; "secret police for the wealthy" → "cảnh sát mật cho giới nhà giàu" (chunk 2222); "lifeguard" → "nhân viên cứu hộ" (chunk 2223); "big man" → "anh lớn" (chunks 2223, 2224); "my brother" → "anh bạn" (chunk 2224); "my man" → "người của tôi" (chunk 2224); "I swear to God" → "Tôi thề với Chúa" (chunk 2224).
- **Southern old-lady / homeless voice (C0432, wave 138):** "heck" (euphemism for hell) → "địa ngục" ("See you in fucking heck!" → "Hẹn gặp mày ở địa ngục chết tiệt!"); "devil spawn" → "con quỷ" (chunk 2225); "ol' lady" → "bà già" self-address; "honey" → "cưng"; "daddy" → "bố" (chunks 2225 C0432_0C2B65A5, C0432_4078F748); "Granny May" kept name (chunk 2225); "peasant" → "dân đen" (chunk 2225); "yankee" kept (chunk 2225); "whoop ass" → "đánh cho tơi tả" per chunk 2104 (chunk 2225); "get down" → "xuống khỏi đó" high-place side (chunk 2225 C0432_3A271FD2); "pay it forward" → "đi giúp người khác đi" (chunk 2225); "Cat got your tongue?" → "Mèo cắn mất lưỡi mày rồi à?" (chunk 2225); swearing/threatening in "tao/mày", begging/fearful in "tôi" (chunk 2225).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default (chunks 2198, 2199, 2204, 2206, 2208, 2216); crude sense "lồn" only where the sentence is clearly sexual / body-part (chunk 2215 C0428_88A1F5A2; chunk 2218 C0429_AC528CEB).
- **"get fucked"** — passive side "bị địt" (chunk 2183 C0414_5F8C85BC) vs active readings elsewhere — still by context.
- **"cooked"** — active "đỉnh" vs passive "toang" per chunks 2001/2062 (chunk 2177 passive "toang" C0412_2593D91D; chunk 2180 passive "toang" C0413_22D16558) — still split.
- **"I got you" / "you got it" / "you got me"** — still by context ("got you" → "tao hiểu mày rồi" understand side chunk 2206 C0423_BA3B6108; "you got it" → "mày thắng rồi" concession chunks 2204, 2206, 2210, 2215, 2218, 2219; "you got me" prank side chunk 2190 C0416_D37A8B77 vs caught side chunks 2188/2189).
- **"fuck on"** → "cút đi" read as a "fuck off" variant (chunks 2185, 2189) vs sexual side when context is explicit — by context.
- **"pop off"** → shoot side (chunk 2184 C0414_C4736793) — held.
- **"smoke" (conflict)** → "gây sự" (chunks 2185, 2187) vs drug side vs shoot side — by context.
- **"on God"** → translated "thề với Chúa" (chunks 2182, 2185) vs kept loanword — still inconsistent.
- **"lowkey"** — kept loanword per chunks 2169/2170 (chunk 2210 C0425_EB227C0D) — now consistent in recent waves.
- **"jit"** → kept loanword (chunk 2206; chunk 2182) vs "thằng nhóc" / "nhóc" — still inconsistent.
- **"Matic"** — kept as an app name (chunk 2185 "'Matic" C0414_EADD20EE) — still unresolved.
- **"OTN"** — kept, "on to the next" (chunk 2185 C0415_08287416).
- **"fenty"** — kept, read as fentanyl (chunk 2192 C0417_804EF1DF).
- **Slots kept correctly this period:** "911" → "{number}" (chunks 2196, 2198, 2201); "724" → "{number}" (chunks 2220, 2221, 2222); "267" → "{number}" (chunks 2211, 2212, 2213); "10-91" → "{number} {number}" (chunk 2213); "911"/"375" → "{number}" (chunk 2186); "150 pounds" → "{number}" (chunk 2182).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** One more crude-side row this period: chunk 2196 C0419_7107EDF5 "And don't come back! And go fuck yourself!" → "Và đừng quay lại nữa! Và đi mà tự đụ đi!" — rendered crude per chunk 2139. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"You just fucked yourself..."** — chunk 2221 C0430_D64011E1 read as self-sabotage "Mày vừa tự hại mình rồi..." — distinct from the pending "Go fuck yourself!" decision.
- **"smelled pussy" split** — chunk 2138 read "Look at this pussy! Smells like one too." as coward "mùi hèn" (C0396_9F5E1C87) vs chunk 2188 read "Thought I smelled pussy!" as body side "mùi lồn" (C0416_3BE188C7) — still inconsistent.
- **"let this shit go"** — chunk 2157 letting-go reading (C0404_10F051B6) vs chunk 2158 shooting reading (C0404_40993863, C0404_5B84CC3B) — still split.
- **"paws"** — "chân" K9 dog side (chunks 2212, 2219) vs "tay" hands side when police order a suspect's hands up (chunk 2222 C0430_F9A695ED "Paws in the air, do it!") — flagged, may need fixing.
- **"sellout"** — "Đồ bán rẻ" (chunk 2202) vs "bán linh hồn" (chunk 2203) — still inconsistent.
- **"boss" / "chief"** — translated "sếp" vs kept loanword — still split in C0431.
- **"eff" / "fuggin'"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"ASAP"** — translated "ngay lập tức" (chunks 2207, 2210, 2219) vs kept loanword — still inconsistent.
- **"get laid"** — crude "được địt" vs soft readings — unresolved.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address — still by context.
- **"you got me"** — caught vs concession vs challenge vs prank — still by context.
- **"trippin'"** — many-way split ("phê" default / "làm quá lên" / panicking) — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent.
- **"bike"** — "xe đạp" (majority) vs "mô-tô" / "xe máy" (minority) — still inconsistent.
- **"body"** — corpse vs living person — by context; "bodies" corpse vs manpower — by context (chunk 2222 corpse side C0430_F9B114DA).
- **"bail"** — "bảo lãnh" vs "chuồn" vs "cứu ra khỏi vụ này" — still inconsistent.
- **"good looks"** — thanks vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" — by context.
- **"FYI"** — kept vs translated — still inconsistent.
- **"Madone!"** — kept — still undecided.
- **"mistress"** — "cô chủ" — still undecided.
- **"That's Negative."** — "phủ định" (majority) vs "Không phải." — still inconsistent.
- **"DOA"** — kept vs translated — still undecided.
- **"PIT"** — kept — still undecided.
- **"call it"** — many-way split (end-it side dominant; chunk 2221 end-it C0430_AA95DC36) — still by context.
- **"officer down" / "casualty"** — dead-vs-hurt ambiguity ("cảnh sát gục rồi" deliberately covers both).
- **"US Army"** — "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" — still inconsistent.
- **"ma'am"** — "thưa bà" vs "thưa cô" vs "cô ạ" — still inconsistent.
- **"move out"** — "rút lui" vs "di chuyển thôi" vs "chạy thoát" (chunk 2212) vs "cút khỏi đây" (chunk 2219) — still inconsistent.
- **"shocker"** — device "súng điện" (majority) vs name — still undecided.
- **"stun gun"** — "súng chích điện" (majority) vs "súng điện" — still inconsistent.
- **"jerkoff"** — "thằng thủ dâm" vs "thằng quay tay" — still inconsistent.
- **"lib" / "libs" / "libtard"** — renderings vary.
- **"Fire"** — blaze vs gunfire — still by context.
- **"M7"** — unknown (kept; chunk 2210 C0425_98ACDC82 "Should set M7 on yo' ass, loser.").
- **"take a shot"** — three-way (shoot / drink / try / fight) — still by context.
- **"Skid mark"** — "Vệt phanh" vs "vết ố" — still split.
- **"Clown Town"** — translated vs place name — still inconsistent.
- **"Evil Eye"** — "Mắt Quỷ" vs loanword — still inconsistent.
- **"white trash" vs "trailer trash"** — handling split.
- **"vibe"** — kept vs translated — still by context.
- **"bag(s)"** — money vs drug sense vs literal — still by context.
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — "thao túng" vs kept — still by context.
- **"Tsou"** — kept as-is — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent ("ra tay" / "kiếm chác" / "đang hành động" / "chơi tới đi" / "chơi tới bến") — still inconsistent.
- **"bump"** — drug sense vs collision sense vs fight sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent.
- **"pheromones"** — kept loanword — now consistent.
- **"smoke" (conflict)** — "gây sự" vs drug side "hút thuốc" vs shoot side "bắn chết" — by context.
- **"go left"** — "toang" vs "rẽ sang hướng xấu" — still split.
- **"joint"** — a woman vs other readings — by context.
- **"on the gas"** — drug side — driving alternative noted.
- **"pop it off"** — shoot side vs start-it ambiguous vs fight side — still by context.
- **"alpha"** — "kèo trên" vs "đầu đàn" vs kept — still split.
- **"Pussycat"** — kept as magazine name vs "mèo con" per the P0 rule — flagged for review.
- **"the woes"** — gang reading vs female reading — by context.
- **"creampuff"** — literal "đồ bánh kem" vs weak-person "thằng bánh bèo" — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines vs as a person elsewhere — by context; "Lilith" read as a dog vs a person — by context.
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
- **Source artifacts preserved as-is:** source typos read as intended ("assess" read as "asses", chunk 2218 C0429_544348D0; "answers" read as "answer's", chunk 2216 C0428_CA95842D; "too" read as "to", chunk 2219 C0429_FD7F65E9; "seem" read as "see", chunk 2211 C0426_2A627861; "terrible way" missing "a", chunk 2222 C0431_02BD092B; "leave from me" probably "leave me alone", chunk 2224 C0431_A2027804; "Why are staying here?" missing "you", chunk 2224 C0431_A76ADBAE; "I will kick sand your eye" missing "in", chunk 2223 C0431_5D449174; "Fuck don't you get?" probably "What the fuck don't you get?", chunk 2217 C0428_E71320FB; "Or look do whatever you want" probably "Or look, do whatever you want", chunk 2217 C0429_19946F5F; "you need more check the back" probably "you need to check the back more", chunk 2208 C0424_A7CBC9C2; "I hate it doing shit" probably "I hate doing this shit", chunk 2198 C0420_66ADC661; "what you what" probably "what you want", chunk 2196 C0419_36993A63; "mess some shit up" missing "who/that", chunk 2207 C0424_561052E9; "Fuck I do?" probably "What the fuck did I do?", chunk 2210 C0425_CF524386; "Oh well f..." cut-off swear, chunk 2225 C0432_5865FC38; "Now how did-" truncated, chunk 2225 C0432_34E0DB6C; "I almost... Fuck!" truncated, chunk 2211 C0425_FD5603D8; "I'm out. This what insurance for..." truncated, chunk 2206 C0423_BAA125E0; "Look, if this a setup... shit..." truncated, chunk 2206 C0423_C6C90298; "Bitch. If you gonna pick that shit up..." truncated, chunk 2206 C0423_A361BD5A; "What the? Oh, I know you ain't!" truncated, chunk 2205 C0423_6D80086C).

## Next

- Wave 139 (chunks 2226–2235, C0432→) is translating now.
- Next milestone: **145,000** (wave 143).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
