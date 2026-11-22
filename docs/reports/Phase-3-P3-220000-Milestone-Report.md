# Phase 3 — P3 Milestone Report: 220,000 Unique Strings

**Date:** 2026-11-22 (after wave 218 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **220,435 / 357,142 (61.7%)**; P3 remaining **136,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 220,435 = **306,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 421,056 = distinct source_ids (no duplicates)
**Waves in this milestone period (214–218):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 214 | 2976–2985 | 216,435 | Story S0126–S0129 (post-pardon deal, Kat in labor / hospital race, bag/hard-drive/statue chase, hospital + train chase) |
| 215 | 2986–2995 | 217,435 | Story S0129–S0139 (chase/hospital tail, street dialogue/chase, Giorgio's garage, combat barks) |
| 216 | 2996–3005 | 218,435 | Story S0139–S0153 (combat barks, street AAVE at Big Mike's, chase/driving crew, shop robbery, frightened civilians, adult-film set) |
| 217 | 3006–3015 | 219,435 | Story S0153–S0163 (frightened civilians, adult-film sets, street AAVE, wrestling promo "The Gentrifier", crew everyday chat, frightened assistant on a boat) |
| 218 | 3016–3025 | 220,435 | Story S0163–S0173 (frightened assistant on a boat, boat fights/parties, aquarium/sea, street NPC small talk, glass-eye character, civilians calling the police, crew chat around Dunk and a dog) |

## Incidents (all resolved except wave 218's one outstanding handoff)

- **Wave 214:** chunks 2983 and 2984 handoffs arrived late and their notes are folded into the wave-214 MEMORY.md entry — wave 214 is now fully documented. Chunk 2980's draft part file had an id typo (FDD4690 missing an F), fixed before merging and re-verified. All 10 files passed the full structure check.
- **Wave 215:** chunks 2986, 2987 and 2989 handoffs arrived late and their notes are folded into the wave-215 MEMORY.md entry — wave 215 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 216:** chunk 3003's handoff arrived late and its notes are folded into the wave-216 MEMORY.md entry — wave 216 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 217:** chunks 3010 and 3014 handoffs arrived late and their notes are folded into the wave-217 MEMORY.md entry — wave 217 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 218:** chunk 3017's handoff never arrived before loading; file verified 100/100 on disk and loaded per the late-handoff precedent. Its counts are from the input files and its notes will be folded into the wave-218 MEMORY.md entry when the handoff arrives. No merge incidents. All 10 files passed the full structure check.

## Conventions settled / reinforced in this period

- **S0126–S0129 hospital thread (wave 214):** "Labor and Delivery" → "Khoa Sản", "contractions" → "cơn co thắt", "C-Section" → "mổ lấy thai khẩn cấp", "ER" → "phòng cấp cứu", "HIPAA" kept, hospital staff polite "tôi/anh/thưa ông/quý vị", "hard drive"/"drive" → "ổ cứng", "statue" → "bức tượng", "locker" → "tủ khóa", "fob" → "chìa khóa xe", "Family Savings" → "Quỹ Tiết kiệm Gia đình", "state department" → "Bộ Ngoại giao", "pool" → "bi-a". "[grunts]" → "[tiếng gừ]" vs "[groan]" → "[rên rỉ]" (precedent).
- **S0130–S0139 chase and combat barks (waves 215–216):** "tweakin'" → "lên cơn" (per "tweaker" → "thằng nghiện đá"), "motherfucker" → "chó đẻ" in "that hurts like a motherfucker" → "đau như chó đẻ", "put 'em down"/"put you down"/"drop that runner" shooting side, "Go fuck a bear trap!" crude (same family as "Go fuck a donkey!"), a few polite NPC lines translated with NO pronoun to avoid choosing wrong (2990).
- **S0139–S0143 combat and crew (wave 216):** "off the clock" off-shift side, "bodies" people vs corpses (both sides in chunk 2997), "I'm out" out-of-ammo side, "Kingfishers" kept as a group name, "climax" orgasm scene vs cinematic, "twelve" → "cớm", "you got that shit on" → "mặc bộ đó đẹp đấy" (compliment), "no más conversación" kept in Spanish, "De nada." kept in Spanish.
- **S0150 shop robbery / S0151 civilians / S0152 adult-film set (wave 216):** "register" → "ngăn kéo tiền", "cops" → "cớm" in threats vs "cảnh sát" in 911 calls, shop employee fearful/begging "tôi" vs confrontational "tao/mày", frightened civilians "tôi/anh" begging/calling police vs "tao/mày" challenging, "shoot" = filming, "climax" → "cảnh lên đỉnh", "mise-en-scène"/"dramedy"/"cuck"/"AD" kept as loanwords.
- **S0153–S0158 adult-film sets (wave 217):** "talent" (film-set actors) → "diễn viên", "fee" → "cát-xê", "gang bang" kept as a loanword, "get off" → "cút ra" (chasing-off side) vs "get off me" → "buông tao ra" (being-held side), "fuck me" (exclamation) → "Địt mẹ", "kink shame" kept "kink" as a loanword, "bottom" kept as a loanword, "don't poop where you eat" → "đừng có ỉa ngay chỗ mình ăn".
- **S0160 street AAVE / S0161 wrestling promo (wave 217):** "zooted" → "phê", "floor this shit" → "đạp ga hết cỡ đi", "The Gentrifier" kept as a character name, "get down" → "chơi kiểu gì" (how-they-play/fight side), "big dog" → "đại ca", "hangry" → "đói đến phát cáu", "shrinkflation" kept.
- **S0162 crew everyday chat (waves 217–218):** "pick it up" hurry-up side, "You got it, Lu!" encouragement side, "lovebirds" → "hai con chim yêu", "brain fart" → "não đơ", "grill" → "vỉ nướng" (BBQ side), "dock it" → "neo thuyền", "life vests" → "áo phao", "seasick" → "say sóng", "clock's tickin'" racing-against-time side, "pool table" → "bàn bi-a", "lady days" → "ngày đèn đỏ", "down the rabbit hole" → "xuống hang thỏ", "Abandon ship!" → "Bỏ tàu đi!", "Ooh, fuck me." → "Ooh, địt mẹ." (exclamation side), "Kiop" kept as a loanword (meaning unclear).
- **S0163 frightened assistant on a boat (waves 217–218):** "tôi/ông" voice per the service/civilian-voice precedent, "Mister Nobody" → "Ông Nobody", "officers" → "cảnh sát" (not "cớm", since the speaker is a polite civilian), "ten knots" → "mười hải lý" (spelled out, no slot).
- **S0164–S0168 boat threads (wave 218):** "wetsuit" → "bộ đồ lặn", "choppy" (water) → "sóng gập ghềnh", "abandon ship" → "bỏ tàu", "getting my sea legs" → "tập quen với sóng biển", "Cazafortunas" kept as a name, "coke" kept as a loanword, "shrooms" → "nấm ảo giác", "best man" → "phù rể", "Wahey!" → "Hú!".
- **S0169 NPC small talk (wave 218):** "belle of my balls" kept the wordplay ("nàng hoa hậu của cặp bi tao"), "walk that back" → "rút lại lời đó", "dip" → "chuồn", "roll out" → "cút đi", "Ooowee"/"Oowee" → "Úi chà", "shroom cupcakes" → "bánh cupcake... có nấm", "shot o'clock" → "giờ làm một ly", "hot bod" → "thân hình nóng bỏng", "tan your hide" → "đánh cho mày một trận", "fried tomato" kept literal, "Howdy" → "Chào nhé", "Toodle-oo" → "Tạm biệt nhé".
- **S0170 glass-eye character / S0171 civilians calling the police (wave 218):** "glass eye" → "mắt giả", "kid"/"kiddo"/"youngen" → "nhóc", "WhatUp group" kept as a name, "hands on ten and two" → "Tay để ở mười giờ và hai giờ!" (spelled out, no slot), "talk your shit" → "chém gió", "Get down!" → "Nằm xuống!", "Hello?" (phone) → "A-lô?", "community council" → "ban quản lý khu dân cư", "sheriff" → "cảnh sát trưởng", "I'll call the cops!" → "Tôi sẽ gọi cớm!" (threat side), "screw you" → "cút mẹ mày đi".
- **S0173 crew chat around Dunk and a dog (wave 218):** "her" (the female dog) → "nó", "lost cause" → "đồ vô phương cứu chữa", "product" → "hàng" (the dealing thread).
- **Markers in this period:** `~n~~m~` kept throughout (wave 214: 34; wave 215: 1; wave 216: 3; waves 217–218: 0 — 38 in total, known chunks). `~tone~` kept with bracketed sounds translated (wave 214: 11 — [groans] → [rên rỉ], [soft panting] → [thở hổn hển khẽ], [winces] → [nhăn mặt], [grunts] → [tiếng gừ]; wave 215: 1 — [groggily] → [ngái ngủ]; waves 216–218: 0 — 12 in total, known chunks).
- **Slots in this period:** 5 in total, known chunks — wave 216: 2 (3004 ×2 `{number}`: "911" skeleton-forced); wave 217: 3 (3009 ×1 `{number}` "size 12", 3012 ×1 `{number}-{number}` "10-4", 3013 ×1 `{number}` "Street Trash 3!", 3014 ×1 `{number}` "911" — all skeleton-forced). Waves 214, 215, 218: 0.
- **Language cues in this period (known chunks):** "In Spanish:" 8 (wave 214 ×3, wave 218 ×5 — all 5 in wave 218 WITHOUT `~t~` in source → none in translation, 2848 precedent); "In Italian:" 29 (wave 214 ×29); "Unknown Language:" 37 (wave 214 ×21, wave 215 ×1, wave 217 ×15 — all 15 in wave 217 WITHOUT `~t~` in source → none in translation, 2848 precedent); "In Russian:"/"In French:" 0 in this period.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" — DECISION STILL PENDING with the user.** New lines this period: 2979 DA527032 "Yeah... right, man. Go fuck yourself." → softened "Đi mà tự sướng đi!"; 3016 1BCB8BCB "¡Jalabolas! Go fuck yourself and your mother!" → crude "Đi mà tự đụ đi, và cả mẹ mày nữa!"; 2987 4694F1DE "Yo, fuck yourself!" → softened "Yo, đi mà tự sướng đi!"; 3007 92D9D498 "Try fucking yourself." → crude "Thử tự địt mình đi." The family is now split 2 softened / 2 crude in this period. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"nigga" — STILL UNRESOLVED.** 10 occurrences in this period, all kept as a loanword: wave 216 ×9 (2997 ×1, 2998 ×6, 2999 ×2), wave 217 ×1 (3008 S0160_56F15EB5 "Bitch-ass niggas."). Rows left as-is.
- **"tao/mày" vs "tôi" for polite NPC lines — STILL OPEN.** This period's evidence: hospital staff/nurses/reception "tôi/anh/thưa bà" (2979, 2983, 2984, 2985), shop staff being robbed "tôi" (3004), frightened civilians "tôi" (3005), polite lines translated with NO pronoun to avoid choosing wrong (2990, 3022), the glass-eye character's two begging lines use "tôi" but his other lines in the same chunk use "tao" (3023), "I'll call the cops!" — "cớm" in threats vs "cảnh sát" in real 911 calls (3024). Rows left as-is.
- **Couple voice (Lucia/Jason) — STILL OPEN, and the same line exists in both voices:** "em/anh" (2977 1FBFACE1, 2980 FDD4690F, 2983 "Tell Jason I love him.") vs "tao/mày" (2974 AB92D65A, 2978 8C332E82). If the couple voice should be "em/anh", the "tao/mày" couple lines need changing.
- **"Coast Guard" split continues:** kept (2952, 2964) vs "cảnh sát biển" (2974, 3016 E8ABA3B5).
- **"off the clock" split (new, wave 216):** off-shift side (3000, 3001, 3002) vs racing-against-time side (2897, 2979).
- **"bodies" split continues:** people vs corpses — both sides in chunk 2997.
- **"I'm out" split (new, wave 216):** out-of-ammo side (3000) vs leaving side (3000 flag, 3009).
- **"climax" split (new, wave 216):** orgasm scene vs cinematic (3005).
- **"Kingfishers" split (new, wave 216):** group name vs literal birds (3002 flag).
- **"get down" split continues:** how-they-play/fight side (3009) vs party/dance side ("quẩy", 3009 flag) vs "nằm xuống" (brief).
- **"happy ending" split (new, wave 217):** happy ending (3007) vs porn-sense "happy ending" (3007 flag).
- **"a bump" split (new, wave 217):** a dose of cocaine (3011) vs a jolt (3011 flag).
- **"shot" split (new, wave 217):** a shot of liquor (3012) vs an injection (3012 flag).
- **"rod" split (new, wave 217):** a fishing rod (3012) vs a sexual metaphor (3012 flag).
- **"I get you" split (new, wave 218):** understanding side (3019) vs catching side.
- **"my lady" split (new, wave 218):** "cô nàng của tao" (3020) vs wife/girlfriend.
- **"carry" split (new, wave 218):** carry a gun (3020) vs carry stuff.
- **"bears" split (new, wave 218):** real bears (3020) vs slang (3020 flag).
- **"hit a donut" split (new, wave 218):** donut spin (3020) vs eat a donut.
- **"charges" split (new, wave 218):** accusations (3020) vs money charges.
- **"piglets" split (new, wave 218):** literal piglets (3022) vs cops.
- **"grid girl" split (new, wave 218):** kept loanword (3022).
- **"turkey" split (new, wave 218):** idiot (3023) vs turkey bird.
- **"a little hit" split (new, wave 218):** drug dose (3023) vs a sip.
- **"room" split (new, wave 218):** space (3024) vs a hotel room.
- **"I'll call the cops!" split (new, wave 218):** "cớm" threat side (3024) vs "cảnh sát" real-call side.
- **"sheriff" split (new, wave 218):** → "cảnh sát trưởng" (3024) vs kept loanword (3024 flag).
- **"her" split (new, wave 218):** the female dog → "nó" (3025) vs a woman.
- **"close" split (new, wave 218):** close call (3025) vs "gần".
- **"$"-loss and "%"-loss via the placeholder-slot exception** continue; skeleton-forced `{number}` slots on non-numbers continue ("911", "10-4", "size 12", "Street Trash 3!").
- **Source typos rendered by sense this period:** "It morning yet?" missing "Is" (2982), "a fucking a wheelchair" extra "a" (2984), "I'm doing you favor" missing "a" (2984), "hand" for "handle" (2987), "seem" for "seen" (2992), "Why don't hit me" (2995), "eveything" (3004), "lasanga" for "lasagna" (3004), "consentual" for "consensual" (3003), "do it this" garbled (3003), "nothow" for "not how" (3019), "Jeez,where" missing space (3009), "Oh,  I" double space (3010).

## Next

- Wave 219 (chunks 3026–3035) spawned 2026-11-22, in progress.
- Next milestone: **225,000** (wave 223).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
