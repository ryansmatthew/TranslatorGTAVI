# Phase 3 — P3 Milestone Report: 215,000 Unique Strings

**Date:** 2026-11-22 (after wave 213 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **215,435 / 357,142 (60.3%)**; P3 remaining **141,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 215,435 = **301,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 415,355 = distinct source_ids (no duplicates)
**Waves in this milestone period (209–213):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 209 | 2926–2935 | 211,435 | Story S0108–S0117 (porn-set cover + safe heist tail, bank recon, fearful civilians, raceway, street/NPC, robbery victims 911, police radio/orders, panicking celebrity, street AAVE, mafia/Italian) |
| 210 | 2936–2945 | 212,435 | Story S0117–S0120 (cartel changes direction, hard drive hunt, Tauro party, yacht party/Italian mafia house) |
| 211 | 2946–2955 | 213,435 | Story S0120–S0123 (yacht party/Italian mafia house, Jason's house fire + police investigation, S0123 start) |
| 212 | 2956–2965 | 214,435 | Story S0123–S0125 (motel chase, hard drive job / Pegassi Tower, Grassrivers locker, police sweep) |
| 213 | 2966–2975 | 215,435 | Story S0125–S0126 (police sweep/locker 17, pardon/DOJ deal, Jason in jail, court testimony, life after crime) |

## Incidents (all resolved, none outstanding)

- **Wave 209:** chunk 2928's handoff arrived late (its halves were written 51/49 — an off-by-one at the cut; a draft part file also had an id typo, `S0109_45392CA6` instead of `S0109_45392C80`, fixed before merging; final file independently verified 100 items in order). Wave 209 is now fully documented.
- **Wave 210:** chunks 2936 and 2938 handoffs never arrived before loading; files verified 100/100 on disk and loaded per the late-handoff precedent. All 6 late handoffs (2936, 2938, 2939, 2940, 2943, 2945) arrived afterwards and their notes are folded into the wave-210 MEMORY.md entry — wave 210 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 211:** chunk 2954's handoff never arrived before loading; files verified 100/100 on disk and loaded per the late-handoff precedent. Both late handoffs (2954, 2955) arrived afterwards and their notes are folded into the wave-211 MEMORY.md entry — wave 211 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 212:** chunk 2956's handoff never arrived before loading; file verified 100/100 on disk and loaded per the late-handoff precedent. Chunk 2956's handoff arrived late and its notes are folded into the wave-212 MEMORY.md entry — wave 212 is now fully documented. No merge incidents. All 10 files passed the full structure check.
- **Wave 213:** chunk 2967's handoff never arrived before loading; file verified 100/100 on disk and loaded per the late-handoff precedent. Chunk 2967's handoff arrived late and its notes are folded into the wave-213 MEMORY.md entry — wave 213 is now fully documented. No merge incidents. All 10 files passed the full structure check.

## Conventions settled / reinforced in this period

- **S0108/S0109 bank recon (wave 209):** polite bank staff "tôi/quý khách/thưa ông/thưa bà" vs crew "tao/mày"; Karim counted 105 camera coverage points; "dingleberry" → "thằng ngu" (2931) vs "đồ cứt khô" (2932); "ace" → "cao thủ" (2931) vs kept loanword (2932/2933); "pool boy" → "cậu bé hồ bơi" (2926/2927/2928) vs kept loanword (2920/2922) vs "thằng dọn hồ bơi" (2923); "rig" → "cái giàn" (2927) vs "cái xe" (2908).
- **S0110–S0117 (wave 209):** fearful civilians "tôi", robbery victims "tôi", police-call threats "tao", police radio/orders, panicking celebrity, street AAVE, mafia/Italian. "10-4" → `{number}-{number}` (skeleton-forced), "911" → `{number}` (skeleton-forced).
- **S0118 hard drive hunt (wave 210):** "cartel" kept, "product" → "hàng", "hard drive" → "ổ cứng", "cops" → "cớm", "heat" → "cớm đang bám theo", "lose 'em" → "cắt đuôi bọn nó", "bleachers" → "khán đài", "babe"/"girl" → "cưng", "Bet, bet." → "Chốt, chốt.", phone "Hello?" → "A-lô?", "lock-up" → "chỗ khóa tạm", "switch it up" → "đổi trò", "I have this" → "Tao lo vụ này." (per "I got this"), "pat you down" → "khám người", "hang back" → "lùi lại", "boss" → "sếp", "back on top" → "trở lại đỉnh cao". "prosciutto"/"Dio" kept as Italian loanwords.
- **S0120 yacht party (waves 210–211):** "single shots" — shooting side (2950) vs photo side (2951); "pick it up" — lift-object (2948) vs hurry-up (2949/2950); "get smoked" — shooting side (2947); "ghosted" — "lặn mất tăm" (2949) vs "bơ tao rồi" (2952); "lady" — sarcastic "bà này" (2952); "shorty" → "em gái" (2945); "PO" kept loanword (parole officer, 2945); "white yay" → "coke trắng" (2945); song lyrics with ♪; Italian interludes; US Coast Guard kept.
- **S0121 Jason's house fire (wave 211):** frightened civilians "tôi", police orders no-pronoun imperatives, radio reports "tôi/bọn tôi", PA announcements "quý vị".
- **S0123 motel chase (wave 212):** hunters speaking an unknown language searching room by room for "the couple" (Lucia/Jason, room six / zero six); room numbers spelled out with no slot ("Six" → "Sáu", "Zero six" → "Không sáu", per "Four-five-one" → "Bốn-năm-một"); "Eja, eja, eja!" kept; "ninety pound" → "chín mươi pao" (spelled out, no slot, per "buck-oh-five"); "neck of the woods" → "khu này".
- **S0124 hard drive / Pegassi Tower (wave 212):** "chopper" → "trực thăng" (per wave 206), "floor it" → "đạp ga hết cỡ đi" (per "floor it"), "give 'em hell" → "cho bọn nó một trận đi", "light 'em up" → "nã đạn vào bọn nó đi", "hold 'em off" → "cầm chân bọn nó", "draw 'em off" → "dụ bọn nó đi chỗ khác", "You got this!" → "Mày làm được!" (per brief), "go out" (die) → "chết" (per "I'm not gonna go out like this"), "take it" → "lấy nó", "ready to roll" → "sẵn sàng lăn bánh", "bird" → "máy bay" (per 2895), "put your foot down" → "đạp ga xuống" (per wave 208), "on me" → "theo tao", "get cover" → "tìm chỗ nấp", "pick up Tommy" → "đón Tommy", "hanging this on us" → "đổ tội cho bọn mình", "go-fast" kept as a loanword (go-fast boat), "Mamma mia"/"Cazzo" kept as Italian loanwords, "penthouse" kept as "căn penthouse".
- **S0125 locker / police sweep (waves 212–213):** "locker" → "tủ khóa", "cafeteria" → "nhà ăn", "roadblock" → "chốt chặn" (per 2953), "officer down" → "cảnh sát gục rồi", "Dispatch" → "trung tâm điều phối", "backup" → "tiếp viện", "task force" → "lực lượng đặc nhiệm", "Sergeant" → "Trung sĩ" (flag: brief only records "Sarge" → "Sếp"), "deconflict" kept as a loanword, "Coast Guard" kept (per "US Coast Guard" 2952) vs "cảnh sát biển" in 2974 (generic noun in a narrative sentence — split), "Keys" kept as a place name (Florida Keys), "pinned in" → "bị kìm chân", "put 'em down" → "bắn chết bọn nó đi" (shooting side, per brief), "Tagged him!" → "Bắn trúng hắn rồi!", "thin 'em out" → "tỉa bớt bọn nó", "cupcake"/"sweeties" → "cưng", "piece of shit" → "đồ cứt" (per wave 204), "sleep on it" → "suy nghĩ thêm", "you got it" → "mày làm được" (encouragement, per brief), "punch it" → "Đạp ga hết cỡ đi", "Gas it" → "Đạp ga đi", "bail" → "chuồn", "set us up" → "gài bẫy bọn tao", "stay on my ass" → "bám sát đít tao", "ten K" → "mười nghìn đô" (spelled out, no slot), "ma'am" → "thưa bà", "VCPD"/"Coño"/"coast guard" kept, "second floor" → "tầng hai", "cuffs" → "còng", "on the clock" → "đang chạy đua với thời gian" (time-pressure side, per 2897 — still split vs on-shift), "On your six" → "Sau lưng mày", "STK" kept (unknown abbreviation), radio codes "10-00"/"10-32" → `{number}-{number}` (skeleton-forced).
- **S0126 pardon / DOJ deal (wave 213):** "pardon" → "lệnh ân xá"/"ân xá", "immunity" → "miễn truy tố", "statewide prosecutor" → "công tố viên toàn bang", "DOJ" kept, "signal six" → "tín hiệu sáu" (spelled out, no slot), "cut a deal" → "thỏa thuận", "turn yourself in" → "ra đầu thú", "the ink is dry" → "mực đã khô", "green light" → "đèn xanh", "out of the woods" → "thoát khỏi rắc rối rồi", "railroaded" → "bị xử ép", "tweaker" → "thằng nghiện đá", "screw ourselves" → "tự hại mình" (per "you just fucked yourself" → "mày vừa tự hại mình rồi"), "wop" kept as a loanword (per "spic" precedent), "cunt" → "lồn" (per brief), "fingerbang" → "móc lồn" (kept crude), "magnum opus" → "kiệt tác", "retreat" → "kỳ nghỉ", "gorilla" → "thằng khỉ đột" (per wave 202), "want a scalp" → "muốn lấy một cái đầu", "Hit me back" → "gọi lại cho tao", Italian kept: "Subito"/"perfetto"/"Cazzo"/"Dai"/"Andiamo"/"amico"/"In un momento", Spanish kept: "hombre", "Family Savings" → "tài khoản Tiết kiệm Gia đình"/"quỹ tiết kiệm gia đình", "minivans and dirty diapers" → "xe minivan với tã bẩn", "pot" (pool) → "đánh vào lỗ", "bodies" → "cái xác" (corpses side), "pool" → "bi-a" ("He's playing pool with Dardan."), "Whippets" kept (flagged: nitrous? dog breed?), "Eris Elites" → "xe Eris Elite" (flagged), "Karen" kept ("bà Karen"), "drive-thru" kept as "quầy drive-thru".
- **Markers in this period:** `~n~~m~` kept throughout (wave 209: 8; wave 210: 31; wave 211: 43; wave 212: 48; wave 213: 71 — 201 in total, known chunks). `~tone~` kept with bracketed sounds translated ([laughs] → [cười], [half laughs] → [cười nửa miệng], [sighs]/[sigh] → [thở dài], [sniffs] → [sụt sịt], [soft grunt] → [tiếng rên khẽ], [exhales] → [thở ra], [imitates screeching, explosion] → [bắt chước tiếng rít, vụ nổ], [imitates car] → [bắt chước tiếng xe], [quietly] → [nói khẽ], [groan]/[groans] → [rên rỉ], [wincing] → [nhăn mặt], [scoffs] → [khịt mũi], [pained groans] → [tiếng rên rỉ đau đớn], [pained groaning] → [rên rỉ vì đau], [inhales] → [hít vào], [panicked breathing] → [thở hổn hển vì hoảng sợ]).
- **Slots in this period:** 16 in total, known chunks — wave 209: 3 (2931 ×2 skeleton-forced incl. "10-4" → `{number}-{number}`, 2934 ×1 "911"); wave 210: 2 (2936 ×1 "since 2012." → `{number}`, 2945 ×1 "Assholes- 1." → `{number}`); wave 211: 2 (2952 ×1 "Our SS-19." → "SS-{number}", 2955 ×1 with 2 `{number}` slots: "5'10\", IQ genius..." → "Cao {number}'{number}\", ..."); wave 212: 4 (2962 ×1 "Locker 17." → `{number}`, 2963 ×1 "Locker 17." → `{number}`, 2964 ×1 "10-00" → `{number}-{number}`, 2965 ×1 "10-00" → `{number}-{number}`); wave 213: 5 (2966 ×1 "10-32" → `{number}-{number}`, 2967 ×2 "10-00" → `{number}-{number}` (one line with 2 slots), 2968 ×2 "locker 17" → `{number}`, "10-00" → `{number}-{number}`). All skeleton-forced on numbers/radio codes.
- **Language cues in this period (known chunks):** "In Spanish:" 33 (wave 209 ×24, wave 213 ×9; waves 210–212 = 0); "In Italian:" 62 (wave 209 ×1, wave 210 ×30, wave 211 ×17, wave 212 ×4, wave 213 ×10); "Unknown Language:" 47 (wave 210 ×1, wave 211 ×14, wave 212 ×32; waves 209/213 = 0) — all with `~t~` → `~t~Ngôn ngữ không rõ:`, except 2961 A78BA594 (no `~t~` in source → none in translation, 2848 precedent) and 2955 004C85FA (same precedent). "In Russian:"/"In French:" 0 in this period.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" — DECISION STILL PENDING with the user.** No new "go fuck yourself" lines in this period. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"nigga" — STILL UNRESOLVED.** No occurrences in this period's known chunks. Rows left as-is.
- **"tao/mày" vs "tôi" for polite NPC lines — STILL OPEN.** This period's evidence: police radio self-reports "tôi/bọn tôi", dispatch reports "bọn tôi", polite service lines "tôi/anh", lawyer-formal "tôi/anh" (2969, 2974), formal prosecutor "anh" (2973), one polite line translated with NO pronoun to avoid choosing wrong (2951), surrender lines "tôi"/"bọn tôi" (2959, 2961), one formal polite line "tôi/chúng tôi/anh" (2963). Rows left as-is.
- **Couple voice (Lucia/Jason) — STILL OPEN, and now the same line exists in both voices:** chunk 2953 used "em/anh" for "Love you." lines; chunk 2975 used "em/anh" for "I love you, Jay. I do." (CBBD50A1); chunk 2974 used "tao/mày" for the same line (AB92D65A). If the couple voice should be "em/anh", the "tao/mày" couple lines need changing.
- **"get down" split continues:** lie down (shooting) vs get down here (from above, 2962) vs party/join/fight.
- **"get smoked" split:** racing "bị cho hít khói" vs shooting "bị bắn chết" — latest: shooting side (2950, 2951).
- **"single shots" split (new, wave 211):** shooting side (2950) vs photo side (2951).
- **"ghosted" split (new, wave 211):** "lặn mất tăm" (2949) vs "bơ tao rồi" (2952).
- **"pick it up" split continues:** hurry-up vs lift-object (2948).
- **"lady" split:** "cô nàng" vs sarcastic "bà này" (2952, 2958).
- **"I got you" / "you got it" / "I got it" splits continue:** reassure "Tao lo cho mày" (2963, 2965, 2966), encouragement "mày làm được" (2960, 2961, 2969, 2970), understanding "Tao hiểu rồi" (2957), caught "Tao tóm được hắn rồi" (2957).
- **"put 'em down" split:** shooting side (per brief) vs "lower your guns" — 2959's "I said put 'em down! They're with me." contradicts the shooting side.
- **"Sergeant" → "Trung sĩ" (2963) vs brief "Sarge" → "Sếp" — flag.**
- **"deconflict" kept as a loanword (2964, 2965).**
- **"Coast Guard" split:** kept (2952, 2964) vs "cảnh sát biển" (2974, generic noun in a narrative sentence).
- **"on the clock" split continues:** time pressure (2968) vs on-shift.
- **"bird" split:** "máy bay" (2962) vs "con chim".
- **"bodies" split:** people vs corpses — latest: "cái xác" (2973).
- **"pool" split:** "hồ bơi" (pool party) vs "bi-a" (2973 "He's playing pool with Dardan.").
- **"pool boy" split continues:** kept loanword vs "thằng dọn hồ bơi" vs "cậu bé hồ bơi".
- **"rig" split:** "cái giàn" vs "cái xe".
- **"dingleberry" split (new, wave 209):** "thằng ngu" (2931) vs "đồ cứt khô" (2932).
- **"ace" split (new, wave 209):** "cao thủ" (2931) vs kept loanword (2932/2933).
- **"signal zeros" / "signal six" police codes:** translated literally ("tín hiệu số không", "tín hiệu sáu") — unclear codes, flagged.
- **"$"-loss and "%"-loss via the placeholder-slot exception** continue; skeleton-forced `{number}` slots on non-numbers continue; skeleton decimal splits continue.
- **Source typos rendered by sense this period:** "Seargent" for "Sergeant" (2915), "get be" extra "be" (2902), "want me drop" missing "to" (2942), "she have" (2929), "I gonna want you" missing "am" (2926), "you had a me at 'yacht'" (2948), "I think I tell you?" missing "did" (2947), "decison" for "decision" (2951), "dont" missing apostrophe (2946), "well" for "we'll" (2958), "a long a time" (2943), "from here on on out" (2975), "supposed go" missing "to" (2964), "don't'" double apostrophe (2965), "deencryption" for "decryption" (2960), "Where you go you" (2957), "What you hanging out?" (2963).

## Next

- Wave 214 (chunks 2976–2985) spawned 2026-11-22, in progress.
- Next milestone: **220,000** (wave 218).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
