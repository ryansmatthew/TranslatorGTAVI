# Phase 3 — P3 Milestone Report: 145,000 Unique Strings

**Date:** 2026-11-21 (after wave 143 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **145,435 / 357,142 (40.7%)**; P3 remaining **211,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 145,435 = **231,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 336,480 = distinct source_ids (no duplicates)
**Waves in this milestone period (139–143):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 139 | 2226–2235 | 141,435 | Southern old-lady / homeless voice C0432 → street/AAVE C0433 → gym-bro + "In Spanish:" C0434 → posh foreign NPC / Italian tourist C0435 |
| 140 | 2236–2245 | 142,435 | Italian tourist NPC tail C0435 → French tourist NPC C0436 → police voice C0437–C0439 |
| 141 | 2246–2255 | 143,435 | Police tail C0439 → street/AAVE + Spanglish C0440 → paranoid conspiracy NPC C0441 → street fight barks C0442 |
| 142 | 2256–2265 | 144,435 | Street tail C0442 → police voice C0443–C0446, alternating with paranoid/drug NPC C0444 |
| 143 | 2266–2275 | 145,435 | Police voice C0446 → street/AAVE C0447 → street/AAVE + Spanglish C0448 → police voice C0449 |

## Incidents (all resolved, none outstanding)

- **Wave 139:** no incidents. Chunk 2226's handoff arrived late (after loading) and its notes were folded into the wave record afterwards. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 140:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 141:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 142:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 143:** no incidents. Chunk 2274 was loaded from a disk-verified file before its handoff arrived (its agent hit an exec failure mid-task; the file verified 100/100, ids in order, 0 adjacent dups, spot-checks idx 0/49/99 aligned before loading). All other 9 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **Police voice (C0437–C0449, waves 139–143):** "Dispatch" → "trung tâm điều phối" per P0; direct orders to suspects in "tao/mày", radio self-reports in "tôi" per the police/service-call precedent — with polite questions to civilians in "tôi/anh" or "thưa bà" (chunks 2240, 2258, 2266, 2273) and surrender/begging/wounded-officer lines in "tôi" (chunks 2244, 2258, 2265); "PIT" kept (chunks 2241, 2243, 2244, 2257, 2262, 2263); "K9" kept; "SWAT" kept; "furry" kept loanword throughout (chunks 2240, 2241, 2244, 2245, 2262, 2263, 2264, 2265, 2275); "furry vehicle" → "xe furry" (chunks 2241, 2262, 2266); "perp" → "nghi phạm" (chunks 2240–2245, 2256–2258, 2262–2265, 2267, 2275) vs "thủ phạm" (chunk 2213, older); "officer down" → "cảnh sát gục rồi" (chunks 2239–2245, 2258, 2262, 2265, 2267) — with one one-off deviation in chunk 2243 ("cảnh sát bị đánh nặng rồi", C0438_A5A8E389); "cruiser" → "xe tuần tra"; "shocker" → "súng điện" device side (chunks 2240, 2242, 2243, 2256, 2262, 2264); "stun gun" → "súng chích điện" (chunks 2243, 2257, 2258, 2264, 2265, 2275); "COs" → "cán bộ quản chế" per the "P.O." precedent (chunk 2242 C0438_59F83890); "EMT" kept (chunk 2241); "EMS" kept (chunk 2263); "ASAP" → "ngay lập tức" (chunks 2241, 2242, 2244, 2257, 2267, 2275); "pronto" → "ngay lập tức" (chunk 2263 C0445_746273A2); "set a perimeter" → "lập vòng vây" (chunks 2241, 2243, 2244, 2262, 2264, 2267); "set the box" → "Chặn nó lại!" (chunks 2239, 2241, 2262) vs "Lập vòng vây đi!" (chunk 2275 C0449_92F13772) — still split; "boxed in" → "Giữ nó bị chặn lại!" (chunk 2264 C0445_EFB8F596); "taking fire" → "đang bị bắn" (chunks 2239, 2242); "pinned (down)" → "kìm chân" / "ghì chặt" / "ghì xuống" (chunks 2239, 2241, 2242, 2244, 2245, 2257, 2263, 2266); "fire rescue" → "cứu hỏa" (chunks 2239, 2275); "visual" → "thấy" / "mất dấu" by context; "calling it" → "kết thúc vụ này" end-it side (chunk 2240); "clear out" → "cút khỏi đây"; "get down" default "nằm xuống" (chunks 2241, 2262) vs high-place "xuống khỏi đó" (chunks 2245, 2258, 2263) vs come-here "xuống đây" (chunk 2243); "go down" → "nằm xuống" default (chunk 2275 C0449_8E913673); "come down" → "xuống đây" come-here side (chunks 2243, 2275); "move out" → "rút lui" (chunk 2243 C0438_A185E5B9); "fall back" → "rút lui" (chunk 2267); "push up" → "tiến lên" advancing side per chunk 2242 (chunks 2242, 2256, 2257, 2265); "runner" → "kẻ chạy trốn"; "body" → "cái xác" corpse side (chunks 2242–2244, 2261–2264, 2267, 2275); "vics" → "nạn nhân" (chunk 2245 C0439_7A3C5614); "bird in the sky" → "trực thăng" (chunk 2245 C0439_683450A4); "casualty" → "thương vong" (chunk 2257 C0443_5E7FCFEE); "scene is cold" → "hiện trường đã nguội" (chunks 2256, 2273); "I got you" → "tao tóm được mày rồi" caught side (chunks 2241, 2244, 2246, 2263, 2265, 2275); "Gotcha!" → "tóm được mày rồi!" (chunk 2275 C0449_A1E82840); "ma'am" → "thưa bà" (chunks 2241, 2264, 2275); "Pumpkin" kept as a name, probably a K9 dog's name (chunk 2266 C0446_6E0D57BA); "Pleadin' the fifth" → "viện tới Tu chính án thứ năm" (chunk 2267 C0446_CEC57B7A); "OT" → "tiền làm thêm giờ" (chunk 2267 C0446_E37DDEA4); "Perp is on a hog!" → "Nghi phạm đang đi mô-tô!" — "hog" read as a motorcycle (chunk 2262 C0445_46CEFBF7); "Spray 'em up!" → "Nã đạn vào bọn nó!" — read as spraying bullets; if it is pepper spray it needs fixing to "Xịt hơi cay vào bọn nó!" (chunk 2262 C0445_14A3424A).
- **"paws" split — still the liveliest inconsistency:** "chân" furry/K9 side (chunks 2239 C0437_28B62711, 2244 C0439_2026E832, 2246 C0439_B24D8C81, 2264 C0445_CEF2A417/C0445_DD5140D4, 2265 C0446_30F369AE, 2266 C0446_54FAB1BC, 2275 C0449_8DC45E20/C0449_A3659633) vs "tay" suspect-hands side (chunks 2222 C0430_F9A695ED, 2240 C0437_6EDA335C) — by context, still flagged per row.
- **French tourist NPC (C0436, wave 140):** "tôi/cậu" throughout per the posh precedent (chunks 2154–2157, 2167–2169, 2222–2224), even when swearing stays crude ("Go suck a bunch of dicks!" → "Đi mà bú một đống cu đi!", "Au revoir, bitch!" → "Au revoir, con đĩ!"); French kept (Non, Oui, Merci, Putain, Merde, chérie, ma chérie, j'adore, mon cheri, Au revoir, s'il vous plaît, Oh là là, déjà vu, pute-de-crack, D'accord, Monsieur, Sérieux, excusez-moi, Allo, Quoi?); 5 "In French:" cues in chunk 2236 and 7 in each of chunks 2237/2238, all rendered "Nói tiếng Pháp:" + translated content per the "In Spanish:" precedent; "surrender monkey" → "con khỉ đầu hàng" kept the image (chunks 2237, 2238); "fuck you up" → "đánh cậu tơi tả" per chunk 2104 (chunk 2238 C0436_DBDA72E1); "screw with" → "dây với" mess-with default (chunk 2238 C0436_C9EE84F0); "get off your high horse" → "xuống khỏi con ngựa cao của cậu" kept the image (chunk 2238 C0436_E8960951); "you're chopped" → "mày bị chặt rồi" kept the looks-insult reading in the slang-practice line (chunk 2238 C0436_DCD76C22); "face card" → "cái mặt... cố khoe ra" (chunk 2236 C0436_09DBADDD); "pallet cleanser" → "đổi vị một chút" (chunk 2236 C0436_2EC7B280, source writes "pallet" for "palate"); "I'm French!" → "Tôi là người Pháp!" (chunk 2239 C0436_FE802711).
- **Italian tourist NPC tail (C0435, wave 140):** "tôi/cậu" throughout, formal/stiff English (posh style like chunks 2222–2224), even when swearing stays crude ("pig whore" → "đĩ lợn", "testicle" → "hòn dái", "Fuck your own ass!" → "Địt mẹ cái đít của mày đi!"); "Ciao, bella!" kept (chunk 2236 C0435_E1071528); "pasta amatriciana" kept dish name (chunk 2236 C0435_E59E2063); "I got this one" → "Để tôi lo vụ này..." reassurance side (chunk 2236 C0435_FBEA3C84); "biter" → "loại hay cắn người" (chunk 2236 C0435_CD87C184); "Miss lady" → "Cô nương à" (chunk 2236 C0435_FF05B6D2).
- **Street / AAVE + "In Spanish:" (C0440, C0448, waves 141, 143):** "In Spanish:" cues rendered "Nói tiếng Tây Ban Nha:" + translated content throughout — heaviest counts this period: chunk 2248: 50+ cues; chunk 2247: 47 cues; chunk 2271: 36 cues; chunk 2272: 34 cues; chunk 2249: 24 cues; chunk 2273: 18 cues; chunk 2270: 3 cues. Spanish kept per chunk (guey, Ay, Órale, Si, bro, dude, Puta madre, gringo, ¿Policía?, Papo, Oye, Mami, Vamos, Mario, René); "play a round" + "Get your cue" read as pool ("Muốn chơi một ván không?", "Lấy cơ bi-a của mày đi.", chunks 2248/2249); "I got papers" → "Tao có giấy tờ đây" (immigration papers, chunk 2249); "Marieta, from Hamlet" kept as a name (chunk 2249 C0440_F10461A6); "boss" → "sếp" per chunks 2222–2224 (chunk 2272 C0448_A85C13B2); "Backup, gimme backup now!" → "Chi viện, cho tao chi viện ngay!" (chunk 2272 C0448_AA9F75C8); "bitch out" → "hèn nhát bỏ chạy" (chunk 2272 C0448_98F809E2); "Don't play about it, be about it." → "Đừng chỉ nói suông, làm thật đi." (chunk 2272 C0448_BE22ACC8); "count your blessings" → "biết ơn đi" (chunk 2272 C0448_B28B49DC); "butter fingers" → "Tay bơ!" (chunk 2270 C0448_0F3470FD); "fuck on" → "cút" per the "fuck off" precedent (chunk 2270 C0447_E16809A1); "fall back" → "lùi lại" (chunk 2270 C0447_EBF2DD16); "Calm your tits, bro." → "Bình tĩnh cái vú mày lại đi, bro." — kept the crude literal image (chunk 2273 C0448_DE22A714).
- **Paranoid conspiracy NPC (C0441, C0444, waves 141–142):** "tao/mày" throughout; IAA kept; "sleeper agent" → "đặc vụ ngủ" / "đặc vụ ngủ quên" / "đặc vụ ngủ đông" (chunks 2249, 2250, 2251 — still split); "sleeper cells" → "tế bào ngủ"; "handlers" → "người điều khiển" / "kẻ điều khiển" (chunks 2250, 2251 — still split); "false flag" → "cờ giả"; "plant" → "tay cài cắm" (chunk 2251 C0441_97F7B14E); "tails" → "mấy tay theo dõi của IAA" (chunk 2249); "implanted memory" → "ký ức bị cấy vào" (chunk 2249); "assassinators" → "sát thủ" (chunk 2249); "Bootlicker!"/"Boot-licker!" → "Đồ bợ đít!" (chunk 2249); "mother-mother-Fer" → "mẹ-mẹ-khốn kiếp" (chunk 2249 C0441_0ABDE940); "Jezebel siren" → "Nàng tiên cá Jezebel" — "siren" read as a mermaid (chunk 2249 C0441_0F6CB0FA); "shadow government" → "chính phủ ngầm" (chunks 2260, 2261); "shadow president" → "tổng thống ngầm" (chunk 2259 C0444_0E0366F6); "shadow agents"/"secret agents" → "đặc vụ bóng tối"/"đặc vụ bí mật" (chunk 2261); "Yaldabaoth" kept as a name (chunk 2260 C0444_7B4DB1E1); "Kitty Litter" kept as the drug name per chunk 2201 (chunks 2252 C0441_D786EAF5, 2259 C0444_5DEABF9E); "meth" kept (chunks 2252, 2259); "ice cream" is a running protection motif in chunk 2251 — kept ("cách bảo vệ duy nhất là kem", C0441_B10BE9AF); "Fregoli delusion" kept as the psychiatric term (chunk 2251 C0441_ACD3B378); "Neptune" → "Sao Hải Vương" when it is the planet name, "Neptunian" → "tiếng Sao Hải Vương" / "Người Sao Hải Vương" (chunk 2252); "Uncle! Uncle!" (surrender cry) → "Tôi xin thua! Tôi xin thua!" (chunk 2252 C0442_017AEC14); "fried" → "phê toang" drug side per the "toang" precedent (chunk 2260 C0444_679B27C6); "vibing" → "chill" (chunk 2261 C0444_D40362DB); "homegirl" → "em gái" (chunk 2261 C0444_FFAAEC2B); "pigs" (police insult) → "lũ cớm" (chunk 2259 C0444_2074E659, C0444_24834550); "baddie" → "em ngon" (chunk 2259 C0444_3E52AEA9); "déjà vu-ing" → "làm tao bị déjà vu" (chunk 2259 C0444_43C6F10A); "done-zo" → "xong hẳn rồi" (chunk 2259 C0444_1376C348); "goo-glumping" → "nhão nhoẹt hết cả lên" (chunk 2258 C0444_01025C5C); "I'm fucking on one" read as being high on a dose (chunk 2258 C0444_0134DFB4).
- **Street fight barks (C0442, C0447, waves 141, 143):** "tao/mày" throughout, crude register kept; "pussy" coward side → "đồ hèn" (chunks 2254, 2255, 2270) vs body side "lồn" where clearly sexual (chunk 2253 C0442_39ED4D5B) vs "mùi hèn" smell side (chunk 2253 C0442_344B8D80 per chunk 2138); "fuck with" → "dây với" mess-with default (chunks 2255, 2269, 2273); "get down" default "nằm xuống" (chunk 2254 C0442_5A0161C2) vs high-place "xuống khỏi đó" (chunk 2269 C0447_B9C6BEAC) vs come-here "xuống đây" (chunk 2228, older); "you got me" → win/lose side (chunk 2254 C0442_9800F7B1); "bitch-ass move" → "nước đi hèn, con đĩ!" per chunk 1972 (chunk 2254 C0442_73A10414); "eat your ass" → "liếm đít mày" sexual crude side (chunk 2254 C0442_70356151); "sunned my nuts"/"sunnin' his nuts" kept the literal perineum-sunning reading (chunks 2253, 2255); "nepo hires" → "mấy thằng con ông cháu cha" (chunk 2255 C0442_F3E56060); "momma or your daddy" → "má hay bố mày" (chunk 2255 C0442_EA396555); "You like pool?" → "Mày thích bi-a không?" — "pool" read as the billiards side per the precedent (chunk 2255 C0442_BE96C03A); "What, you gonna throw them? Get a cue." → "Gì, mày định ném chúng à? Lấy cây cơ đi." — "cue" read as a pool cue (chunk 2255 C0442_E04EB623); "I'll break." → "Tao sẽ gãy mất." — read as "I will break/collapse" (chunk 2255 C0442_F1B420F8) vs "Tao phá." breaking in pool (chunk 2248 C0440_845ACAAE) — still split by context; "You gonna run to the little girl's room next?" → "Tiếp theo mày định chạy vào nhà vệ sinh nữ à?" (chunk 2255 C0442_B1A52803); "ass clown" → "thằng hề đít" (chunk 2269 C0447_95D6C430, C0447_96945A3C); "chickenshit" → "thằng hèn" (chunk 2269 C0447_A5C57447); "fuckface" → "thằng mặt lồn" (chunks 2268, 2269); "get the fuck on" → "cút mẹ đi" "fuck off" side per the precedent (chunk 2269 C0447_87CDA324); "pussy face" → "mặt hèn" coward side (chunk 2268 C0447_2E0FAB5E); "put 'em over your knee" → "quật bọn nó qua đầu gối" (chunk 2268 C0447_52D87557); "I'll let you pussy out" → "tao sẽ để mày chuồn như đồ hèn" (chunk 2270 C0447_EC4255DE); "They killed the boy!" → "Bọn nó giết thằng nhóc rồi!" — "the boy" read as a young man/boy; if it is a dog (K9/dog, per the "boy" dog precedent) it needs fixing (chunk 2270 C0447_EF858341).
- **Southern old-lady / homeless voice (C0432, wave 139):** "devil/demon" throughout; "heck" → "địa ngục"; "aristocracker" kept wordplay (chunks 2226, 2227); "yankee" kept; "MeeMaw" kept (chunk 2227); "Liberty City" kept (chunk 2227); "plumb crazy" → "điên hẳn" (chunks 2226, 2227).
- **Gym-bro + "In Spanish:" (C0434, wave 139):** "chicken legs" → "chân gà"; "bench" → "đẩy tạ"; "Mexican creatine" → "creatine Mexico" (chunk 2232); "Hotbox" kept name (chunk 2231); "you got it" → attention side (chunk 2233 C0434_EA23533C); "chama"/"pana"/"mamis"/"cabrón"/"Mierda" kept Spanish.
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default (chunks 2228, 2229, 2230, 2232, 2234, 2254, 2255, 2261, 2268, 2269, 2270); crude sense "lồn" only where the sentence is clearly sexual / body-part (chunk 2253 C0442_39ED4D5B; chunk 2215 C0428_88A1F5A2; chunk 2218 C0429_AC528CEB); real-cat reading where the context is calling a cat (chunk 2087, older).
- **"get fucked"** — passive side "bị địt" / "đi mà bị địt đi" (chunks 2213, 2215, 2261) vs active readings elsewhere — still by context.
- **"cooked"** — active "đỉnh" vs passive "toang" per chunks 2001/2062 (chunk 2230 "Cook this fool." → beating side C0433_E0D24B8E) — still by context.
- **"I got you" / "you got it" / "you got me"** — still by context ("I got you" caught side chunks 2241, 2244, 2246, 2263, 2265, 2275; "you got it" attention side chunk 2233 C0434_EA23533C vs concession side chunks 2204–2219; "you got me" win/lose side chunk 2254 C0442_9800F7B1).
- **"fuck on"** → "cút đi" read as a "fuck off" variant (chunks 2229, 2270) vs sexual side when context is explicit — by context.
- **"pop off"** → shoot side — held.
- **"smoke" (conflict)** → "gây sự" (chunk 2229 C0433_7044F142) vs drug side "hút thuốc" vs shoot side "bắn chết" (chunks 2228, 2230) — by context.
- **"on God"** → translated "thề với Chúa" (chunk 2224 C0431_EE66DB8C) vs kept loanword — still inconsistent.
- **"lowkey"** — "nói nhỏ nhé" (chunk 2273 C0449_00EFB9E6) vs kept loanword (chunks 2169/2170, 2210) vs "thật ra" / "thầm" — still split many ways.
- **"jit"** → kept loanword (chunk 2206) vs "thằng nhóc" / "nhóc" — still inconsistent.
- **"Matic"** — kept as an app name — still unresolved.
- **"OTN"** — kept, "on to the next" — still unresolved.
- **"fenty"** — kept, read as fentanyl — still unresolved.
- **"vibe"** — kept loanword (chunks 2217, 2275 C0449_9820AB72) vs translated — still by context.
- **Slots kept correctly this period:** "741" → "{number}" (chunks 2239, 2240, 2241); "621" → "{number}" (chunks 2241–2244); "724" → "{number}" (chunks 2220–2222, older); "911" → "{number}" (chunks 2249, 2259); "412" → "{number}" (chunks 2256, 2257, 2258); "691" → "{number}" (chunks 2273, 2275); "267" → "{number}" (chunks 2211–2213, older); "10-91" → "{number} {number}" (chunk 2213, older).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** More crude-side rows this period: chunk 2234 C0435_5C0FB353 "I recommend you fuck yourself!" → "Tôi khuyên cậu tự đụ đi!"; chunk 2235 C0435_A31776D0 "Go fuck yourself in the ass!" → "Đi mà tự đụ vào đít đi!"; chunk 2237 C0436_4DB3BA32 "Screw you! Go fuck yourself!" → "Địt mẹ mày! Đi mà tự đụ đi!"; chunk 2248 C0440_8E422F21 "Bah, go fuck yourself.", C0440_A990FD74, C0440_B5951FA8 "Go fuck yourself, bro." — all rendered crude "Đi mà tự đụ đi" per chunk 2139; chunk 2249 C0440_E6D352D9 "In Spanish: Stop messing with decent people, go fuck yourself." → "Nói tiếng Tây Ban Nha: Đừng có dây với người tử tế nữa, đi mà tự đụ đi."; chunk 2250 C0441_5CE91436 "tell my IAA handlers thanks and uh to go fuck themselves." → "bảo bọn chúng đi mà tự đụ đi."; chunk 2253 C0442_1A96B936 "Yeah, fuck yourself!" → "Ừ, tự đụ đi!". Also chunk 2236 C0435_FF3FA1BA "Fuck your own ass!" → "Địt mẹ cái đít của mày đi!" — a "fuck yourself" variant that may relate to the pending decision. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"You just fucked yourself..."** — chunk 2221 C0430_D64011E1 read as self-sabotage "Mày vừa tự hại mình rồi..." — distinct from the pending "Go fuck yourself!" decision.
- **"smelled pussy" split** — chunk 2138 read "Look at this pussy! Smells like one too." as coward "mùi hèn" (C0396_9F5E1C87) vs chunk 2188 read "Thought I smelled pussy!" as body side "mùi lồn" (C0416_3BE188C7) — still inconsistent.
- **"let this shit go"** — chunk 2157 letting-go reading (C0404_10F051B6) vs chunk 2158 shooting reading (C0404_40993863, C0404_5B84CC3B) — still split.
- **"paws"** — "chân" furry/K9 side (chunks 2239, 2244, 2246, 2264, 2265, 2266, 2275) vs "tay" suspect-hands side (chunks 2222, 2240) — still split, flagged per row.
- **"officer down"** — "cảnh sát gục rồi" settled vs chunk 2243's one-off "cảnh sát bị đánh nặng rồi" (C0438_A5A8E389).
- **"sellout"** — "Đồ bán rẻ" (chunk 2202) vs "bán linh hồn" (chunk 2203) — still inconsistent.
- **"boss" / "chief"** — translated "sếp" vs kept loanword — still split in C0431 (chunks 2222–2224) and C0448 (chunk 2272 "sếp").
- **"eff" / "fuggin'"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"ASAP"** — translated "ngay lập tức" (chunks 2241, 2242, 2244, 2257, 2267, 2275) vs kept loanword — still inconsistent.
- **"get laid"** — crude "được địt" vs soft readings — unresolved.
- **"the Y" / "Y Hotel"** — "khách sạn Y" (chunk 2235 C0435_9C921E7C) vs kept as name — still unresolved.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"daddy"** — "bố" (majority, chunks 2225, 2255) vs kept loanword as flirtatious address — still by context.
- **"you got me"** — caught vs concession vs challenge vs prank vs win/lose — still by context.
- **"trippin'"** — many-way split ("phê" default / "làm quá lên" / panicking) — still by context (chunk 2228 "phê" ×3).
- **"Kitty Litter"** — drug name (chunks 2252, 2259) vs literal cat litter — still inconsistent as a class.
- **"bike"** — "xe đạp" (majority, chunks 2246, 2263, 2266) vs "mô-tô" / "xe máy" (minority) — still inconsistent; "hog" → "mô-tô" (chunk 2262) vs "bicycle" → "xe đạp" (chunks 2264, 2273).
- **"body"** — corpse vs living person — by context; "bodies" corpse vs manpower — by context.
- **"bail"** — "bảo lãnh" vs "chuồn" vs "cứu ra khỏi vụ này" — still inconsistent.
- **"good looks"** — thanks vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" — by context (chunk 2228 "chuồn" C0433_26C29BDC).
- **"FYI"** — kept vs translated — still inconsistent.
- **"Madone!"** — kept — still undecided.
- **"mistress"** — "cô chủ" — still undecided.
- **"That's Negative."** — "phủ định" (majority) vs "Không phải." — still inconsistent.
- **"DOA"** — kept vs translated — still undecided.
- **"PIT"** — kept — still undecided.
- **"call it"** — many-way split (end-it side dominant; chunk 2240 end-it C0437_7706F882) — still by context.
- **"officer down" / "casualty"** — dead-vs-hurt ambiguity ("cảnh sát gục rồi" deliberately covers both).
- **"US Army"** — "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" — still inconsistent.
- **"ma'am"** — "thưa bà" (chunks 2241, 2264, 2275) vs "thưa cô" vs "cô ạ" — still inconsistent.
- **"move out"** — "rút lui" (chunk 2243) vs "di chuyển thôi" vs "chạy thoát" (chunk 2212) — still inconsistent.
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
- **"vibe"** — kept (chunks 2217, 2275) vs translated — still by context.
- **"bag(s)"** — money vs drug sense vs literal — still by context.
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — "thao túng" vs kept — still by context.
- **"Tsou"** — kept as-is — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent ("ra tay" / "kiếm chác" / "đang hành động" / "chơi tới đi" / "chơi tới bến" / "làm lại từ đầu") — still inconsistent.
- **"bump"** — drug sense vs collision sense vs fight sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent (chunk 2253 "girlie" → "cô em" C0442_2CD6CE0B).
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
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines vs as a person elsewhere — by context ("Pumpkin" is probably a K9 dog's name, chunk 2266; "They killed the boy!" read as a young man, chunk 2270 C0447_EF858341 — if it is a dog it needs fixing).
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
- **"sleeper agent"** — "đặc vụ ngủ" vs "đặc vụ ngủ quên" vs "đặc vụ ngủ đông" — still split (chunks 2249, 2250, 2251).
- **"handlers"** — "người điều khiển" vs "kẻ điều khiển" — still split (chunks 2250, 2251).
- **"set the box"** — "Chặn nó lại!" (chunks 2239, 2241, 2262) vs "Lập vòng vây đi!" (chunk 2275) — still split.
- **"I'll break."** — "Tao sẽ gãy mất." (chunk 2255) vs "Tao phá." breaking in pool (chunk 2248) — still split by context.
- **"lowkey"** — "nói nhỏ nhé" (chunk 2273) vs kept / "thật ra" / "thầm" — still split many ways.
- **"stray"** — "kẻ lang thang" (person) vs "con chó hoang" (dog) — still split (chunk 2273 C0449_1BA57B77).
- **"take a tail" / "a tail"** — follower (chunk 2240) vs a literal tail (chunk 2265 C0446_3F20DF9E "locate a tail") — still split.
- **"Spray 'em up!"** — "Nã đạn vào bọn nó!" (bullets) vs "Xịt hơi cay vào bọn nó!" (pepper spray) — still split (chunk 2262 C0445_14A3424A).
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot ("fifteen weeks" → "mười lăm tuần", chunk 2237; "hundred-meter radius" → "bán kính trăm mét", chunk 2237; "Five more hours." kept as words, chunk 2270).
- **Source artifacts preserved as-is:** source typos read as intended ("feign" read as "fiend", chunk 2230 C0433_DEE087E1; "I've think" probably "I think", chunk 2234 C0435_4D06B821; "he deserve" grammar error, chunk 2234 C0435_239957C1; "You're going head that way" probably "go ahead that way", chunk 2235 C0435_B1DDD163; "You got to be joking me?" broken, chunk 2235 C0435_947CBFDF; "Oh well f..." cut-off swear, chunk 2225 C0432_5865FC38; "Now how did-" truncated, chunk 2225 C0432_34E0DB6C; "Pana, you do something..." truncated, chunk 2233 C0434_D969DF6A; "What'd you got here?" broken grammar, read as "What have you got here?", chunk 2251 C0441_72366E95; "wonder" probably a typo for "wander", chunk 2251 C0441_7DB88FE8; "You park like a you drive with your ass!" broken ("like a you drive"), chunk 2253 C0442_1F075E0C; "Looks at this little shit." probably "Look at", chunk 2254 C0442_7827B579; "I wouldn't do this I was you..." missing "if", chunk 2263 C0445_6652D2B6; "Wh- Fuck! Stop right now!" cut-off ("What-"), chunk 2264 C0446_05DCEDF4; "This is what they want you do to, lady!" broken ("want you do to"), chunk 2250 C0441_343E4F9A; "I know you didn't say what I thought you said." garbled, chunk 2275 C0449_A7DE51FC; "Get a fucking life, and leave us alone. In Spanish: Go." — the "In Spanish:" cue sits at the end of the line and applies only to "Go", chunk 2249 C0440_F5EFA60C).

## Next

- Wave 144 (chunks 2276–2285, C0449→) is translating now.
- Next milestone: **150,000** (wave 148).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
