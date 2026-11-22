# Phase 3 — P3 Milestone Report: 155,000 Unique Strings

**Date:** 2026-11-21 (after wave 153 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **155,435 / 357,142 (43.5%)**; P3 remaining **201,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 155,435 = **241,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 347,540 = distinct source_ids (no duplicates)
**Waves in this milestone period (149–153):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 149 | 2326–2335 | 151,435 | Canadian tourist tail C0467 (2326) → street/AAVE C0468 (2327–2329) → police C0469 (2330–2332) → C0470 generic confrontation barks (2333–2334) → C0471 "dude"/bro voice (2335) |
| 150 | 2336–2345 | 152,435 | "dude"/bro C0471 (2336–2337) → hunter/swamp C0472 (2338–2342) → barrio gang C0473 (2342–2345) |
| 151 | 2346–2355 | 153,435 | Barrio gang tail C0473 (2346) → street/AAVE C0474 (2347–2349) → police C0475 (2349–2352) → firefighter C0476 (2352) → C0477 mixed civilian/staff/paranoid/rideshare (2352–2355) → police C0478 (2355) |
| 152 | 2356–2365 | 154,435 | Police C0478–C0480 (2356–2363) → street/AAVE C0481 (2363–2365) |
| 153 | 2366–2375 | 155,435 | Street/AAVE C0481 (2366–2367) → Spanglish gang/"the Beast" C0482 (2368–2371) → wellness/drag NPC C0483 (2371–2374) → street/AAVE C0484–C0485 (2374–2375) |

## Incidents (all resolved, none outstanding)

- **Wave 149:** no incidents. All 10 files passed the full structure check; spot-checks aligned. Chunk 2330's agent had a recorded exec failure during merge, but the final file was verified 100/100 by the agent and by the parent before loading.
- **Wave 150:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 151:** no incidents. Chunk 2354's first merge had idx 13/14 swapped (C0477_89B21A34 / C0477_89BBE061) — the agent self-fixed before writing the final file, verified on disk.
- **Wave 152:** no incidents. Chunk 2356's first check found 1 id typo at idx 12 (C0478_431C6122 instead of C0478_431C612F) — the agent self-fixed and re-verified. All 10 files passed the full structure check; spot-checks idx 0/49/99 on chunks 2356 and 2365 aligned.
- **Wave 153:** no incidents. All 10 handoffs arrived before loading. All 10 files passed the full structure check; spot-checks idx 0/49/99 on chunks 2366 and 2375 aligned.

## Conventions settled / reinforced in this period

- **Police voice (C0469–C0480, waves 149–152):** direct orders with the suspect use "tao/mày", radio self-reports use "tôi", polite questions to civilians use "tôi/anh/thưa bà", people calling the police use "tôi". "Dispatch" → "trung tâm điều phối", "perp" → "nghi phạm", "K9"/"PIT"/"SWAT" kept, "officer down" → "cảnh sát gục rồi", "officer hit" → "cảnh sát bị bắn rồi", "visual" → "dấu" ("lost visual" → "mất dấu"), "pinned down" → "bị kìm chân" (majority; "ghì chặt" in chunk 2359 — split), "furry" kept, "furry vehicle" → "xe furry", "paws" → "tay" hands side vs "chân" furry/K9 side, "stun gun" → "súng chích điện", "shocker" → "súng điện" device side vs "súng chích điện" (chunks 2352, 2360, 2363), "ma'am" → "thưa bà", "bike" → "xe đạp" majority, "body" → "cái xác" corpse side, "take you in" → "đưa về đồn", "put you down" → "bắn chết mày" (shooting) vs "hạ mày" (knock-down), sobriety-test lines use "tôi/anh" as in sample C0000_9E9FA62C. Slots: unit numbers "874"/"484"/"279"/"748"/"911"/"433"/"641"/"575" → `{number}`; "10-4" → `{number} {number}` (chunk 2357). "set the box" → "Chặn nó lại!" majority.
- **Firefighter voice (C0476, chunk 2352):** "TSS" kept, "fire call" → "vụ cháy", "engine" → "xe cứu hỏa", "cops" → "cớm".
- **Hunter / swamp voice (C0472, wave 150):** species/hunting terms translated (scalps → "da đầu", taxidermist → "thợ nhồi xác", prey → "con mồi", park ranger → "kiểm lâm", coast guard → "cảnh sát biển", houseboat → "nhà thuyền"); "Grassrivers" kept; "airboat" split: "thuyền quạt" (chunk 2338) vs kept loanword (chunk 2339).
- **Barrio gang voice (C0473, C0482, waves 150–153):** "the Seven"/"Sevens"/"Siete" kept as the gang name; "the Beast"/"la Bestia" KEPT as a name from wave 151 onward (brief rule added 2026-11-21; earlier "Quái Vật" chunks 2342/2345 and "Quái Thú" chunk 2344 remain status `machine` for later review); "M7" kept; "barrio"/"mara"/"hyna" kept; "stripes" → "uy tín"; "jump you in" → "ăn đòn nhập hội"; the sacrifice ritual (take heart/tongue/skin for the Beast); "In Spanish:" cues are heavy — chunk 2369: 42, chunk 2370: 31, chunk 2368: ~40, chunk 2371: 20; "serote"/"cerote" → "thằng ngu" per chunk 2345 vs kept loanword (chunk 2368, chunk 2371 "¡Fijáte cerota!" kept as-is); "putas" kept; "mi amor"/"chele"/"mami"/"Oye" kept; "the Beast" as a deity ("Ngài") in prayers (chunk 2370); "Go fuck your mother!" → "Đi mà địt mẹ mày đi!" (chunk 2370 C0482_C105CCF8 — a different "go fuck..." family, not part of the pending decision).
- **Street / AAVE barks (C0471, C0474, C0481, C0484–C0485, waves 149–153):** "tao/mày" throughout, crude register kept ("bitch" → "con đĩ", "fuck" → "địt mẹ"/"đéo", "motherfucker" → "thằng chó chết"); "fuck with" → "dây với" (dominant default); "trippin'" → "phê" default but by context: "hoang mang" (chunk 2363), "không cuống" (chunk 2364 "I ain't trippin'"), "bận tâm" when "trip about" (chunk 2367); "throw down" → "đánh nhau" vs "walk" → "chuồn" (chunk 2363); "big dog" → "đại ca"; "baddie" → "em ngon"; "crackhead" → "thằng nghiện crack"; "a piece" → "súng"; "op" → "địch"; "vest" → "áo chống đạn"; "whip" → "xe"; "smoke" → "đánh nhau" fight side vs "ăn đòn" (chunk 2374) vs hút cần (chunk 2367, flagged); "deadass" → "nói thật"; "undercover" → "cớm chìm"; "bob and weave" → "né qua né lại"; "albino python" → "trăn bạch tạng"; "Mozambique super-drill" kept; "Peekhole" kept; "Marbles"/"Stiffy"/"Mamacita"/"Gator Girth"/"Lil Bob"/"Cane"/"McKenna"/"King Girth" kept as names; "simp" kept; "Thicc Nasty"/"Era of the Thiccness"/"The Thicc-verse" kept; "fenty" kept (chunk 2367); "k-hole" kept; "bread" → "tiền"; "you got it" concession side → "mày thắng rồi!" (chunk 2375); "strapped up" → mang súng; "bang" → dân băng đảng; "get this work" → "ăn đòn"; "woofing" → "sủa"; "pump fake" → giả vờ rút súng (chunk 2375); "learn you" → dạy cho một bài học (Southern, chunk 2375); "short bus" → "xe buýt đặc biệt" (chunks 2307, 2375); "nigga" → "thằng này" (no direct equivalent, chunk 2374); "slim" ambiguous — dropped in one translation (chunk 2374 C0484_4B786697).
- **Canadian tourist tail (C0467, chunk 2326):** "eff"/"effin'" → "đệt" renderings continue.
- **Paranoid NPC (C0441/C0444/C0458/C0477):** "tao/mày"; "deep state" → "nhà nước ngầm", "handlers" → "kẻ điều khiển", "meth" kept.
- **Cellerica voice (C0451–C0452):** "tôi/cậu" throughout; "Cellerica", ranks "Whisper"/"Pillar"/"Tender"/"Essential", "girlboss", "literally", "manifest" kept.
- **Wellness / drag NPC (C0483, chunks 2371–2374):** a flamboyant wellness/spiritual voice with therapy jargon: "honey"/"darling"/"girl"/"hon"/"babe"/"baby" → "cưng"/"em gái", "manifest" kept, "cishet" kept, "inner child" → "đứa trẻ bên trong", "read a bitch" → "chửi thẳng mặt một con đĩ", "Shadow self" → "Bản Ngã Bóng Tối", "hold space" → "dành chỗ", "at capacity" → "hết sức chứa", "chakras" → "luân xa", "Saturn is in return" → "Sao Thổ đang hồi vị", "Borderline Personality Disorder" → "Rối loạn nhân cách ranh giới", "life coaching certificate" → "chứng chỉ huấn luyện cuộc sống", "plantar fasciitis" → "viêm cân gan chân", "aura" → "hào quang", "cosmic accountability" → "trách nhiệm vũ trụ", "calm your tits" → "bình tĩnh cái vú lại đi", "dick around" → "địt dạo", "Call me mother" → "Gọi tao là mẹ đi" (ballroom "mother"), "fashion police" → "cảnh sát thời trang", "cops aren't Virgos" → "mấy thằng cớm này không phải cung Xử Nữ", "I don't do pro bono emotional labor" → "Tao không làm lao động cảm xúc miễn phí", "every doll for herself" → "mỗi búp bê tự lo cho mình", "charcoal enema" → "thụt tháo than hoạt tính", "my books are closed" → "tao hết lịch rồi", "get a grip" → "bình tĩnh lại đi"; "gagged" → "bị choáng" (drag slang), "snatched" → "trông đỉnh" (drag slang), "apparate" → "hiện ra" (Harry Potter term; "độn thổ" alternative flagged); "t-girl" kept; "sis" → "Chị ơi".
- **"RydeMe"** kept (rideshare app, C0477). **"Lu-Chia"** kept as a mispronunciation of Lucia (chunk 2355). "troglodyte" → "người hang", "written up" → "bị ghi lỗi" (chunk 2355).
- **"pussy"** → coward sense "đồ hèn" remains the clear default; crude sense "lồn" only where the sentence is clearly sexual / body-part.
- **"get down"** — nine-way split continues: "nằm xuống" default / "xuống khỏi đó" high-place / "xuống đây" come-here / "quẩy" party side / "chơi" / "đánh nhau" / "xuống xe" / "đi xuống" / "làm tới" — still by context, flagged per row.
- **Slots kept correctly this period:** "433"/"641"/"575" unit numbers → `{number}` (many chunks); "10-4" → `{number} {number}` (chunk 2357).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" — DECISION STILL PENDING with the user.** New crude-side rows this period: chunk 2335 C0471_36D4341D, first-person variant "I'll just go fuck myself..." → "Tao sẽ tự đi đụ mình..."; chunk 2365 C0481_7BC21DC5, plural variant "All y'all can go fuck yourselves." → "Tất cả bọn mày đi mà tự đụ đi!". Related variant: chunk 2370 C0482_C105CCF8 "Go fuck your mother!" → "Đi mà địt mẹ mày đi!" — a different family, not part of the decision. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"tao/mày" vs "tôi" for polite NPC lines — STILL OPEN.** New evidence this period: chunk 2337 "Hello, police?" used "tao"; chunk 2353 polite/service lines used "tao/mày" per brief but the agent flagged they should be "tôi"; chunk 2355 "Police? Come quick! We're being robbed!" used "tao"; chunk 2359 surrender "Wait, don't shoot, don't shoot! You win! You beat me!" used "tao/mày" vs the chunk 2350 precedent "tôi"; chunk 2361 "Let me live!" used "tôi" (police begging) vs the chunks 2323/2336 "tao" precedent; chunk 2362 "Wait, wait, wait, I give up! I give up!" used "tôi" per chunk 2350; the C0483 wellness coach: chunk 2372 "I'm calling the cops" used "tao" per brief vs chunks 2373/2374 used "tôi" per the police-call precedent — a NEW split inside one voice; chunk 2374's C0483 speaker used "tôi" (polite + condescending) while the listener stays "mày". Still undecided, rows left as-is.
- **"boxed in" three-way split:** "Giữ nó bị chặn lại!" (chunk 2264) vs "bị vây chặt" (chunk 2357 C0478_DDFAE9C1) vs "Chặn được nó rồi!" (chunk 2358) — still inconsistent.
- **"pinned down" split:** "bị kìm chân" (majority) vs "ghì chặt" (chunk 2359, "Got her pinned down!").
- **"shocker" split:** "súng điện" device side vs "súng chích điện" (chunks 2352, 2360, 2363).
- **"the Beast" split (waves ≤150):** "Quái Vật" (2342, 2345) vs "Quái Thú" (2344) vs kept "the Beast"/"la Bestia" (2343, and 2346+ per the new brief rule) — the keep-as-name rule is settled from wave 151 onward; the older rows remain status `machine` for later review.
- **"airboat" split:** "thuyền quạt" (chunk 2338) vs kept loanword (chunk 2339).
- **"coast guard" split risk:** "cảnh sát biển" (chunks 2340, 2341) vs possible "tuần duyên" (flagged in chunk 2341 C0472_B478809F).
- **"Cuban royalty" split:** "hoàng gia Cuba" (chunk 2310) vs "Hoàng tộc Cuba" (chunk 2312 C0461_FAB9BB0A) — still inconsistent.
- **"networking" three-way split (chunk 2319):** verb → "giao lưu" (majority) vs noun "network" → "mạng lưới" (C0465_0D9924A1) vs "you'll network like crazy" → "kết nối điên cuồng" (C0465_128CD678) — still inconsistent.
- **"drip" split:** kept loanword (chunk 2322) vs "Chất." (chunk 2323) — still inconsistent.
- **"set the box" split:** "Chặn nó lại!" (chunks 2212, 2262, 2274, 2287/2288, 2330, 2331) vs "lập vòng vây" (chunk 2258, chunk 2296 C0456_8CEAF731) vs "Lập vòng vây đi!" (chunk 2275 C0449_92F13772, chunk 2298 C0457_7208DCDA); "boxed in" → see above.
- **"paws" split:** "chân" furry/K9 side vs "tay" hands side (chunks 2222, 2240, 2287, 2296, 2325, 2351 C0475_CAA30176, 2352 C0475_DCCCA5C9, 2358 C0478_FB46AC75) — by context, flagged per row.
- **"officer down"** → "cảnh sát gục rồi" settled vs chunk 2243's one-off "cảnh sát bị đánh nặng rồi" (C0438_A5A8E389).
- **"sleeper agent" three-way split in C0441:** "đặc vụ ngủ" (2249, 2252) vs "đặc vụ ngủ đông" (2251) vs "đặc vụ ngủ quên" (2250).
- **"pig(s)" police-insult split:** "lũ cớm" (chunks 2259, 2335, 2337) vs "đồ lợn" (chunk 2252 C0441_C16919C7) vs literal pig readings elsewhere; "cops" split: "lũ cớm"/"cớm" vs "cảnh sát" (inside chunk 2336: C0471_3DDE5AD7 vs C0471_492DEE7D/C0471_59092B0A).
- **"smelled pussy" split:** coward "mùi hèn" (chunk 2138 C0396_9F5E1C87; chunk 2253 C0442_344B8D80) vs body side "mùi lồn" (chunk 2188 C0416_3BE188C7; chunk 2253 C0442_39ED4D5B).
- **"let this shit go" split:** letting-go (chunk 2157 C0404_10F051B6; chunk 2279 C0450_DCD58A9B; chunk 2328 C0468_7B1FC4F5) vs shooting (chunk 2158 C0404_40993863, C0404_5B84CC3B).
- **"I got you" / "you got it" / "you got me"** — still by context (caught / reassure / understand / concession / attention / win-lose sides all attested this period).
- **"trippin'"** — many-way split ("phê" default / "hoang mang" / "không cuống" / "bận tâm" / panicking) — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent as a class (new: chunk 2362 C0480_B7009A80 "Kitty Litter junkie").
- **"bike"** — "xe đạp" majority vs "mô-tô" minority — still inconsistent.
- **"body"** — corpse vs living person — by context.
- **"call it"** — end-it dominant — still by context.
- **"ASAP" / "pronto"** — translated vs kept — still inconsistent.
- **"VC"** — expanded vs kept — still inconsistent.
- **"daddy"** — "bố" majority vs kept loanword as flirtatious address — still by context.
- **"lowkey"** — many-way split — still by context.
- **"vibe"** — kept vs translated — still by context.
- **"the Y" / "Y Hotel"** — kept vs "khách sạn Y" — still unresolved.
- **"eff" / "eff-you"** — "đệt" renderings continue (chunk 2326) — deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"serote" / "cerote" split:** → "thằng ngu" (chunks 2345, 2369 C0482_426CBAE4, 2370) vs kept loanword (chunk 2368 "Throw down some cash, serote"; chunk 2371 "¡Fijáte cerota!" kept as-is).
- **"white boy"** — real person (chunk 2366 "cross-eyed white boy") vs cocaine slang (P0 S0705_0BC3777F → "coke Keys xịn") — by context.
- **"smoke" split:** fight side "đánh nhau" (chunk 2365) / "ăn đòn" (chunk 2374) vs hút cần (chunk 2367, flagged) vs shooting context.
- **"$"-loss and "%"-loss via the placeholder-slot exception** continue; skeleton decimal splits continue; skeleton-forced slots on non-numbers continue ("433"/"641"/"575" unit numbers → `{number}`, "10-4" → `{number} {number}`).
- **Source artifacts preserved as-is this period:** broken "I assuming all of you are guilty!" (chunk 2363 C0480_FD61966C); "knock if off" (chunk 2362 C0480_AB503CD3); "Got a people over here..." (chunk 2369 C0482_3F98CA38); "you're disassociating..." (chunk 2374 C0483_EAA44AF3); truncated "Shi..." (chunk 2375 C0485_1D085665).

## Next

- Wave 154 (chunks 2376–2385) is being spawned now.
- Next milestone: **160,000** (wave 158).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
