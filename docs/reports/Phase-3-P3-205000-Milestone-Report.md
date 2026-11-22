# Phase 3 — P3 Milestone Report: 205,000 Unique Strings

**Date:** 2026-11-22 (after wave 203 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **205,435 / 357,142 (57.5%)**; P3 remaining **151,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 205,435 = **291,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 403,424 = distinct source_ids (no duplicates)
**Waves in this milestone period (199–203):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 199 | 2826–2835 | 201,435 | Story S0077–S0079 (airport heist continues) |
| 200 | 2836–2845 | 202,435 | Story S0079–S0082 |
| 201 | 2846–2855 | 203,435 | Story S0082–S0084 (tailing, gym Ajax, heist planning + chase) |
| 202 | 2856–2865 | 204,435 | Story S0084–S0087 (post-heist chase, Vault, Andrés, Rafa rescue) |
| 203 | 2866–2875 | 205,435 | Story S0087–S0092 (party chase, statue heist in Capri) |

## Incidents (all resolved, none outstanding)

- **Wave 199:** chunks 2830 and 2831 handoffs arrived late (after loading); files verified 100/100 on disk before loading; notes folded into the wave-199 MEMORY.md entry afterwards (2831 first, 2830 later). No merge incidents. All 10 files passed the full structure check.
- **Wave 200:** chunks 2839 and 2840 handoffs never arrived before loading; files verified 100/100 on disk and loaded per the late-handoff precedent — their notes will be folded into the wave-200 MEMORY.md entry when the handoffs arrive. No merge incidents. All 10 files passed the full structure check.
- **Wave 201:** chunk 2854 handoff never arrived before loading; file verified 100/100 on disk and loaded per the late-handoff precedent — its notes will be folded into the wave-201 MEMORY.md entry when the handoff arrives. No merge incidents. All 10 files passed the full structure check.
- **Wave 202:** chunks 2857, 2860 and 2865 handoffs never arrived before loading; files verified 100/100 on disk and loaded per the late-handoff precedent — their notes will be folded into the wave-202 MEMORY.md entry when the handoffs arrive. Chunk 2863 merge incident: 2 swapped pairs in the draft (94C11AEF/94920AAF and A1B33A16/A1FC4A76), fixed to input order and re-verified. All 10 files passed the full structure check.
- **Wave 203:** chunks 2868 and 2872 handoffs never arrived before loading; files verified 100/100 on disk and loaded per the late-handoff precedent — their notes will be folded into the wave-203 MEMORY.md entry when the handoffs arrive. No merge incidents. All 10 files passed the full structure check.

## Conventions settled / reinforced in this period

- **Airport heist S0077 continues (wave 199):** "copy that" → "rõ rồi", "stay close" → "bám sát vào", "put him down" → "bắn chết hắn đi" (shooting), "get down" → "nằm xuống", "I got you" → "Tao lo cho mày" (reassure) vs "Tao tóm được mày rồi" (caught), "I got it" → "Tao hiểu rồi" (understand) vs "Hắn có nó rồi." (possession), "get it together" → "chấn chỉnh lại", "control tower" → "tháp điều khiển", "cabana" kept ("cabana số chín"), "Cartagena" kept, "mano"/"cabrone" kept, "pass" → "thẻ" (2831), "fuck with me" → "dây với tao" (2831), "nigga" dropped at 2831 per the 2824 precedent. "In Spanish:" ×14 in wave 199 (2826 ×2, 2827 ×3, 2828 ×2, 2830 ×5, 2831 ×1, 2832 ×1; all with `~t~` → `~t~Nói tiếng Tây Ban Nha:`).
- **S0082–S0084 (wave 201):** tailing, gym, hotel, investigating Gallo/Mattia; gym Ajax — Lucia infiltrates to reach Kordell; S0084 heist planning + chase.
- **Post-heist chase S0084–S0087 (wave 202):** "ride" → "xe", "cop car" → "xe cớm", "van" → "xe tải", "vault city" → "thành phố két sắt", "Suck my dick, motherfuckers." → "Bú cặc tao đi, lũ chó đẻ.", "moving on this" → "triển vụ này đi", "take her out" (kill) → "xử", "mask up" → "đeo mặt nạ vào", "two-way ticket" → "vé khứ hồi", "heat" (cops pressing) → "đổ thêm cớm lên đầu", "get us some heat" → "khiến bọn mình bị cớm sờ gáy", "car note" → "tiền góp xe", "tow truck" → "xe cứu hộ", "push up with me" → "tiến lên cùng tao" (advance in shootout, not push-ups), "Know who you fucking with!" → "Biết mày đang dây với ai đi!", "spic" kept loanword, "la rata"/"abuela" kept, "flush freaks" literal, "Nine1Nine" kept (place), "catering truck" → "xe catering", "Fuck. You." → "Địt. Mày.", "Fuck it! Vamos!" → "Kệ mẹ nó! Vamos!", "looking the part" → "đúng vai rồi", "Put 'em down!" → "Bắn chết bọn nó đi!", "pick it up" → "nhanh lên" (hurry), "Pussy!" (taunt) → "Đồ hèn!", "I got your back" → "Tao chống lưng cho mày", "lucky son of a bitch" → "thằng khốn may mắn", "bad boys for life" → "bad boys cả đời", "gonorreas"/"caza fortunas" kept, "creep" → "biến thái", "Showtime!" → "Tới giờ diễn rồi!", "get low" → "cúi thấp xuống", "what you on?" (drugs) → "mày đang phê cái gì thế?", "J, the man!" → "J, đúng là số một!", "seven bullets" → "bảy viên đạn" (spelled out, no slot), "¡Jueputa!" kept, "get straight" → "tỉnh táo lại", "bumpy ride" → "chuyến xe này xóc quá", "evasive maneuver" → "động tác né tránh", "FAP" kept (unknown abbreviation), "jugo" kept loanword, "I fuck with that" → "Tao thích cái đó." (AAVE "thích"), "go out" (die) → "chết", "Load up, dog!" → "Lên đạn đi, dog!", "Step on it"/"Foot down, baby!" → "Đạp ga đi"/"Đạp ga đi, cưng!", "bodyshop" → "tiệm sửa xe", "vault" as place name → "Cái Két", "chopper" → "trực thăng" (aircraft), "brosky" kept, "zooted" → "phê", "Good lookin' out, J!" → "Cảm ơn đã để ý, J!", "lay low" → "nằm im", "I gotta bounce" → "tao phải chuồn đây", "we might be fucked" → "bọn mình tiêu rồi", pleading "Just don't hurt me." → "Làm ơn đừng làm hại tôi." ("tôi"), distress call "Help, I can't move!" → "Cứu với! Không cử động được!" (no pronoun), "Five-oh" → "cớm" (not "Năm mươi"), "exec protection" → "bảo vệ yếu nhân", PA announcement voice "quý vị". "In Spanish:" ×31 in wave 202, most with NO `~t~` marker in source (2848 precedent) — translation also has none.
- **Party / chase S0087 (wave 203):** Whisper / Tens / She-E-O / diva / "yaas" / "Manifesticks" / "PEACH" kept; "manifest" → "hiện thực hóa"; "Slay!" → "Đỉnh quá!"; "bag a She-E-O" → "tóm một bà She-E-O"; "Lock and load, diva, it's go-time!" → "Lên đạn đi, diva, tới giờ hành động rồi!"; "golf cart" → "xe golf"; "mansion" → "biệt thự"; "poison" (drink) → "uống gì"; "PMSing" → "đang tới tháng"; "Cellerichain" kept; "glow up" → "màn thăng hạng"; "hit" (drug dose) → "một liều"; "hot" → "quyến rũ"; "Ten outta ten" → "Mười trên mười" (score 10, not the group Ten).
- **Statue heist in Capri S0088–S0092 (wave 203):** "rat" → "thằng chuột" (snitch); "wasted him" → "xử hắn rồi"; "haul" → "chiến lợi phẩm"; "set up" → "cái bẫy"; "Suck my willy, you fatuous git!" → "Bú cặc tao đi, đồ ngu đần!" ("willy" British = cặc); "bugger off" → "cút đi"; "boo-hoo" → "cứ khóc đi"; "bite us in the ass" → "quay lại cắn bọn mình"; "fuck with us" → "dây với bọn tao"; "appraisal" → "thẩm định"; "bronze" → "tượng đồng"; "antique dealers" → "mấy tay buôn đồ cổ"; British upper-class voice uses "tôi"/"các người" ("Appalled, such a disgusting accusation." → "Tôi phẫn nộ, một lời buộc tội thật kinh tởm.", "Barbarians, all of you!" → "Lũ man rợ, tất cả các người!"); "Venus" = statue name; "cat statue" kept literal. **New cue: "In French:" ×1** (2870 S0089_1A680A39, with `~t~` → `~t~Nói tiếng Pháp:`). "our lady" (statue, she/her) → "cô nàng của bọn mình"; "Bronze Venus" → "Venus bằng đồng"; "Regency style" → "Phong cách Regency"; "swap meet" → "chợ trời"; "yacht" → "du thuyền"; "dock" → "neo đậu"; "provenance" → "xuất xứ"; "smash and grab" → "đập phá rồi cướp"; "break-in" → "đột nhập"; "all clear" → "sạch rồi"; "Not on me" → "không phải lỗi của tao"; "bleach my eyes" → "rửa mắt cái đã" (idiom "want to unsee"); "Finders keepers." → "Ai tìm được thì của người đó."; "swipe these credit cards" → "chôm mấy cái thẻ tín dụng này"; "vibes" kept loanword; "daddy" kept (flirtatious address); "the piece" → "món đồ" (art-appraisal context, NOT a gun); "cut us out" → "gạt bọn mình ra"; "cops up our ass" → "lũ cớm đang bám đít bọn mình"; "fuck you the fuck up" → "đập mày tơi tả"; "full of shit" → "toàn nói láo"; "Too many irons in the fire." → "Ôm đồm quá nhiều việc cùng lúc."; "Capri cops" → "cớm Capri"; "sugar granny" → "bà bồ già bao nuôi"; "dead birds look judgy" → "mấy con chim chết cũng nhìn kiểu phán xét"; "nightmare material" → "thứ chỉ có trong ác mộng"; "Fingers crossed..." → "Cầu mong là được..."; "mint juleps" kept; "back-channel" → "qua kênh ngầm"; "I'm coming." → "Tao tới đây." (arriving side); "You fuckin' amateurs, Jesus Christ!" → "Lũ nghiệp dư chết tiệt, Chúa ơi!"; "slippery motherfucker" → "thằng chó đẻ trơn tuột". The source's she/it switching for the statue is kept ("see what she's worth?" → "xem cô nàng đáng giá bao nhiêu?" vs "see what it's worth." → "xem nó đáng giá bao nhiêu."). **"bronze lady" inconsistency (new):** "bà đồng" (2873) vs "bức tượng quý bà bằng đồng" (2875).
- **Markers in this period:** `~n~~m~` kept throughout (wave 202: 2856 ×1, 2858 ×1; wave 203: 2869 ×6, 2870 ×6, 2871 ×2, 2873 ×4, 2874 ×3, 2875 ×1); `~tone~` kept with bracketed sounds translated ([shudders]/[shuddering] → [rùng mình], [silenced grunting] → [tiếng rên bị bịt lại], [accent slipping] → [giọng giả bị lộ], [snorts] → [khịt mũi], [soft laughter] → [cười khẽ], [muttering] → [lẩm bẩm], [screams] → [hét lên], [laughs] → [cười]).
- **Slots in this period:** 0 in waves 202–203 (skeleton-forced slots remain rare in Story dialogue).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" — DECISION STILL PENDING with the user.** No new "go fuck yourself" lines in this period. **Related (NOT the pending decision):** chunk 2828 "Fuck you, motherfucker." → crude; chunk 2863 "Fuck you!" → "Địt mẹ mày!" (just "fuck you", not the decision). Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"nigga" — STILL UNRESOLVED.** 2831 dropped it (per 2824 precedent); 2841 kept it; 2855 kept it ×4. Waves 202–203: no occurrences reported in the known chunks (2857/2860/2865/2868/2872 unknown). Rows left as-is.
- **"tao/mày" vs "tôi" for polite NPC lines — STILL OPEN.** This period's evidence: British upper-class "tôi"/"các người", French appraiser formal "tôi"/"chúng tôi"/"các vị", antique-dealer formal "tôi/anh", fearful pleading "tôi", distress calls with no pronoun, PA announcements "quý vị", staff/guard-at-door lines split "anh" (polite) vs "mày" (guard-order voice). Rows left as-is.
- **Couple voice (Lucia/Jason) — STILL OPEN:** "tao/mày" default; if the couple voice should be "em/anh", the relevant scenes need changing.
- **"bronze lady" split (new, wave 203):** "bà đồng" vs "bức tượng quý bà bằng đồng" — by chunk, unresolved as a class.
- **"juice" split (new, wave 203):** drink vs steroid — "Now I really need a juice!" (2863) flagged.
- **"the Y Hotel" still unresolved** (latest: wave 202).
- **"I got you" / "you got it" / "I got it" splits:** reassure vs caught vs understanding vs possession — latest: chunk 2830 (reassure "Tao lo cho mày" vs understanding "Tao hiểu rồi" vs possession "Hắn có nó rồi.").
- **"get smoked" split:** racing "bị cho hít khói" vs shooting "bị bắn chết".
- **"get down" split:** party/join/fight — latest: "Get down!" → "Nằm xuống" (shooting side).
- **"Extraction"/"evac" split:** "di tản" vs "sơ tán" vs "Rút lui".
- **"bike" split continues:** "xe đạp" majority vs "xe máy".
- **"bodies" split:** people vs corpses.
- **"lady" many-way split:** mocking vs flirting vs polite vs neutral — latest: 2862 "my lady" = girlfriend/wife.
- **"sir"/"ma'am" formal vs sarcastic split:** by line, unresolved as a class.
- **"fuck with" split:** "dây với" vs AAVE "thích" — latest: 2863 "I fuck with that" → "thích" vs 2858 "Know who you fucking with!" → "dây với".
- **"white boy" / "white girls" split:** person vs cocaine slang.
- **"bump" split:** driving jolt vs drug — latest: chunks 2861, 2864.
- **"rounds" split:** patrol rounds vs drinks round — latest: chunk 2858.
- **"chopper" split:** helicopter vs biker — latest: 2864 chose helicopter (flying context).
- **"puppy" split:** car vs dog.
- **"oil" split:** goods vs drug vs lubricant.
- **"gear" split:** bánh răng / trang bị / đồ.
- **"estupid" split:** kept vs translated.
- **"baddie" split:** translated vs kept.
- **M0002 "ta/ngươi" vs "tôi/cậu" two-voice split; M0003 "Chronos" person/tank/substance.**
- **"$"-loss and "%"-loss via the placeholder-slot exception** continue; skeleton-forced `{number}` slots on non-numbers continue; skeleton decimal splits continue.
- **Source typos rendered by sense this period:** "I'm mean" for "I mean" (2864); "Nobody's nice to should've been" garbled (2863); "mothefuckers" (2855); "Don't slow up up" (2844); "They just me told" (2842); "You supposed be up here?" missing "to" (2830); "harrassed" for "harassed" (2869); "you'd to like" for "you'd like" (2871).

## Next

- Wave 204 (chunks 2876–2885, Story S0092–S0103) spawned 2026-11-22, in progress.
- Next milestone: **210,000** (wave 208).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
