# Phase 3 — P3 Milestone Report: 330,000 Unique Strings

**Date:** 2026-11-22 (after wave 328 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **330,435 / 357,142 (92.5%)**; P3 remaining **26,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 330,435 = **416,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 540,025 = distinct source_ids (no duplicates)
**Waves in this milestone period (324–328):** 5,000 strings, 0 quarantined in total

## Period totals

- Language cues: **195** in the whole period (324 ×5, 325 ×24, 326 ×22, 327 ×84, 328 ×60). Mostly "~t~In Spanish:" → "~t~Nói tiếng Tây Ban Nha:" with `~t~` kept. Cue-form variants: 4125 ×13 "In Spanish:" with no `~t~` in source (wave 328, per the 2848 precedent — the translation also has none); 4108 ×1, 4110 ×1, 4112 ×1 "In Spanish:" with no `~t~` in source (wave 327). Italian cues: 4084 ×1, 4085 ×4 "~t~In Italian:" (wave 324); 4086 ×6, 4087 ×6, 4088 ×2 (wave 325); 4105 ×1 "~t~In Italian:" (wave 326); 4106 ×2 "~t~In Italian:" (wave 327). Spanish fragments kept without a cue — 4076 F7465A34 "vieja", 4079 FD8C51C9 "vieja", 4079 FF4E0CAB "Ciao" (Italian, wave 324); 4090 "Bien", "¡Mierda!", "¡Dios Mio!", "Mierda" (wave 325); 4097 "sin lima", "Sí", 4101 "tequila sin lima", 4102 "Cazafortunas, soda sin lima. Por favor, bro." (wave 326); 4107 "Papi", "por favor", "Bienvenidos", 4111 "puta", 4115 "Papá" 3CA56A63 (wave 327); 4119 "pendejo" DC93699F, "Mierda!" F6AD1A4C, "chula" F9CDC7FC, "jugo" E07213F2 (wave 328). Whole Spanish sentences kept untranslated without a cue — 4116 5729B4F0 "Buenas noches, señoras.", 5F75B804 "Hola, Andrés.", 6261D69C "Papá! Papá!" (wave 328).
- Slots: **7** in the whole period (324 ×1: 4081 B53AC686 "She's like a 6 max..." → "{number}"; 325 ×1: 4088 ADD55A06 "locked in on the Enus at 300" → "{number}"; 326 ×2: 4104 0A0725AF "Okay, 701." and 4105 3E09EA99 "I'm looking for 701?" — both skeleton-forced "{number}"; 327 ×1: 4106 85C93368 "the VIPs staying in room 701." → "phòng {number}"; 328 ×2: 4121 8860F6CF "What you hit in that ride? 200, 210?" → "{number}, {number}"). The "701" hotel-room numbers are skeleton-forced `{number}` slots on non-numbers — a recurring pattern.
- `~n~~m~`: **114** in the whole period (324 ×0, 325 ×6, 326 ×24, 327 ×36, 328 ×48).
- `~tone~`: **42** in the whole period (324 ×0, 325 ×8, 326 ×12, 327 ×15, 328 ×7).
- `~rp~`: **11 items** in the whole period (324 ×0, 325 ×0, 326 ×0, 327 ×4 items / 5 occurrences — all in 4115, first `~rp~` hits since wave 309; 328 ×7 items: 4116 ×1, 4117 ×1 item 2 occurrences, 4118 ×5 in 2 items, 4119 ×2 items 3 occurrences, 4120 ×1).
- "go fuck yourself": **1 new exact, softened** in the whole period — 4097 1307C445 "Go fuck yourself. ~tone~ [laughs] ~tone~Alright, there's a problem with the table..." → "Đi mà tự sướng đi! ~tone~ [cười] ~tone~..." (wave 326, pending the user's bulk decision). Related variants: **1 "Get fucked in your ass!" crude literal** (324: 4084 07204492); **1 "fuck up your own car"** (325: 4095 AB6FFC52). No new plural or bare variant in the whole period.
- "nigga": **13** in the whole period (324 ×7: 4081 ×1, 4082 ×4, 4083 ×2 — kept loanword; 325 ×0; 326 ×0; 327 ×0; 328 ×6: 4122 ×2 026B1D1D/0CBEBE15, 4123 ×2 7953C026/8C557397, 4124 ×2 D874E552/EEB91FDF — all kept as loanword per brief).

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 324 | 4076–4085 | 326,435 | S0867 tail (4076–4079 + 4080 ×24 = 424), **S0868** (AAVE street barks, 4080 ×23), **S0869** (neighborhood/roommate voice around Jason, Bert, Louise, Mandy, 4080 ×53 + 4081 ×43 = 96), **S0870** (AAVE neighborhood gossip/banter, 4081 ×57 + 4082 + 4083 + 4084 ×15 = 272), **S0871** (posh/upper-class voice, polite "tôi/anh" even when swearing, 4084 ×19), **S0872** (Italian family around Lucia, boat/yacht + race threads, 4084 ×66 + 4085 ×100 = 166) |
| 325 | 4086–4095 | 327,435 | S0872 tail (4086–4087 + 4088 ×54 = 254), **S0873** (Jonny car-dealership voice, 4088 ×38), **S0874** (combat/chase barks hunting Duval/Caminos, 4088 ×8 + 4089 ×68 = 76), **S0875** (Lucia driving recklessly / driving-lesson, 4089 ×32 + 4090 + 4091 ×5 = 137), **S0877** (Lucia & Jason at a car dealership/showroom, 4091 ×95 + 4092–4095 = 495). No S0876 appeared |
| 326 | 4096–4105 | 328,435 | S0877 tail (4096 ×78), **S0878** (nightclub scene at The Vault around Andrés de León, 4096 ×22 + 4097–4103 + 4104 ×72 = 794), **S0879** (hotel check-in — Lucia & Jason at The Y Hotel under Mr./Mrs. Walker cover identities, 4104 ×28 + 4105 = 128) |
| 327 | 4106–4115 | 329,435 | S0879 tail (4106 + 4107 ×38 = 138), **S0880** (kidnapping/ransom/rescue around Rafa, Andrés de León's son, held by Gustavo's side/FAP, 4107 ×62 + 4108–4113 + 4114 ×43 = 705), **S0881** (Megamundo party / Andrés de León job scene mixed with Y hotel check-in, 4114 ×57 + 4115 = 157) |
| 328 | 4116–4125 | 330,435 | S0881 tail (4116–4119 + 4120 ×11 = 411), **S0882** (ambient NPC greetings/small talk directed at Jason/Lucia — shop talk, car compliments, greetings, plus a few hostile chase-offs, 4120 ×89 + 4121 + 4122 ×25 = 214), **S0883** (strip-club scene — female dancers talking to Lucia, AAVE flirty/teasing voice, VIP section, drinks/shots, studio session, scam talk, "securing the bag", 4122 ×75 + 4123 + 4124 + 4125 ×8 = 283), **S0884** (intense confrontation/fight barks, many "In Spanish:" cues, the "fuck the alligator" thread, 4125 ×32), **S0885** (a prank/joke gone wrong around a truck, 4125 ×60) |

## Incidents

- **Wave 324:** 10/10 handoffs arrived before loading. 4078 agent self-caught a typo'd id at item 99; 4079 first draft split 54/46, rewrote 50/50. All 10 files passed the full structure check.
- **Wave 325:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 326:** 10/10 handoffs arrived before loading. 4098 agent self-caught swapped items 83/84 in the part-2 draft, corrected before merging. All 10 files passed the full structure check.
- **Wave 327:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 328:** 9/10 handoffs arrived before loading — chunk 4119's handoff never arrived; its output file was verified on disk (100 items, ids in order, keys exactly {id, vi}, 0 adjacent dups) per the late-handoff precedent, and its notes were folded into the MEMORY entry afterwards. All 10 files passed the full structure check.
- No loader errors, no quarantines, no duplicate rows in the whole period (muse rows == distinct source_ids after every wave).

## Conventions settled / reinforced in this period

### Period-wide

- "panic room"/"safe room" → "phòng an toàn" (4115, 4116) — settled.
- "blow" cocaine → "bột" (waves 326–327) — settled.
- "Mr. Mangrove" → "Ông Mangrove" (per the P0 quality fix) — consistent across this period's S0872 Italian-family lines.
- "mamma" kept Italian loanword (4086) vs "Má" — NOT unified.
- "polizia" kept Italian (4086, 4088) vs translated — NOT unified.
- "cocaina" kept Italian spelling (4086) — kept as loanword.
- "Madonna" kept Italian exclamation (4087) vs "Trời ơi" — NOT unified.
- "Big Ball" kept as a name (4108, 4112, 4113) — unresolved.
- "ho" → "con đĩ" (4098) vs kept loanword — NOT unified.
- "bands" cash stacks (4104) vs music bands (4100) — NOT unified.
- "siphoned" fuel side (4112) vs money side (4107) — NOT unified.
- "omelettes" → "trứng ốp la" (4105) vs "trứng tráng" — NOT unified.
- "juice" drink side (4120 FDB01C40 "juice run" → "đi mua nước ép"; "jugo" kept 4118 C53B2B4F, 4119 E07213F2) vs steroid side (4120 6DC63176 "you juicing?" → "chích steroid") — NOT unified.
- "Portie" Portuguese-people side (4120 047EB4A9/5248D03C, 4122 E33BFD9E) — unresolved.
- "perra" kept as Spanish loanword (4116 49D25DD9) vs translated "con đĩ" — NOT unified.
- "Little mama" → "Cô em nhỏ" (4125 0BD3CD98) vs "Má"/"mẹ" vs kept loanword — NOT unified.
- "fuck me" retort side (4121 AA642C79) vs exasperated "Địt mẹ" (4140 92F49DBF) vs crude literal per 4002/4005 — NOT unified.
- "get off" chase-off "cút ra" (4125 00BBFE1D) vs being-held "buông tao ra" (4125 593BBCDF) — NOT unified.
- "put me down" set-me-down side (4125 2A25EC50) vs shooting/knock-down side — NOT unified.
- "take you up" upstairs side (4119 E2F8A452) vs take-you-up-on-an-offer side (4114 040A1C30) — NOT unified.
- "babysit" literal side (4118 A1D1BBCA) vs guard-duty side — NOT unified.
- "lines" drug-lines side (4118 9E5E0CFA) vs dialogue-lines side — NOT unified.
- "total smokeshow" → "cực phẩm" (4119 E3BD9AC0) — settled.
- "champ" kept (4119 F41CF799) — kept as loanword.
- "Bee Saliva" kept as a drink name (4116 6A4817DE, 4119 EDE354E1) — kept.
- "extraction" "Rút lui" (4098, 4102, 4104) vs "Di tản" (chunk 498) — still inconsistent.
- "cue" pool-cue side vs hint/signal side — NOT unified.
- "tank" big heavy car (4093) vs tank vehicle (4092) vs fish-tank (4124 D1E759A8) — NOT unified.
- "give it up" quit side (4125 81E612B2) vs applause side — NOT unified.
- "eat" slang "ate"/performed-flawlessly (4093) vs literal — NOT unified.
- "lose you" race side vs lost-track (4093) — NOT unified.
- "white boy" person side "thằng da trắng" (4081, 4083) vs cocaine slang per the P0 fix — NOT unified.
- "your boy"/"your guy" boyfriend side vs friend side — NOT unified.
- "kid" child side (Rafa) vs young-accomplice side (wave 327) — NOT unified.
- "my boy" son side vs friend side (friend side 4117 81635605) — NOT unified.
- Polite-NPC pattern continues: S0871 posh voice polite "tôi/anh" (4084); S0877 sales-staff polite "tôi/anh/chị" vs couple crew "tao/mày" (wave 325); S0878 polite staff lines (4097, 4101, 4103, 4104) and S0879 hotel-staff polite "tôi/anh/thưa ông/thưa bà" (4104, 4105) (wave 326); S0880 polite "tôi/thưa ông" lines (4109, 4112) and S0881 polite staff lines (4114, 4115) (wave 327); S0881 polite staff/investigator lines (4116, 4117, 4118, 4119) and S0882 polite service lines (4120) (wave 328). Rows left as-is (status `machine`).
- Couple-voice question continues: S0880 "I love you, too." crew "tao/mày" (4111 95A4F0D4); S0882 "mama" → "má" (4121 D8AEAED4).
- Skeleton-forced `{number}` slots on non-numbers continue: "701" in 4104/4105/4106 (hotel room), "200, 210" in 4121, "300" in 4088, "6 max" in 4081.
- Source typos rendered by sense (latest: 4109 "titanius").

## New / deepened splits this period

- **"juice" / "jugo"** — the drink side (4120 "juice run" → "đi mua nước ép") vs the steroid side (4120 "you juicing?" → "chích steroid"), with the Spanish "jugo" kept untranslated in 4118/4119 — three renderings of one word family in a single wave.
- **"Portie"** — new unresolved split: Portuguese-people side (4120, 4122) with no settled rendering.
- **"perra"** — kept as a Spanish loanword (4116) vs translated "con đĩ" — the same split as "puta" in earlier waves, now with a second word in the family.
- **"extraction"** — the "Rút lui" (4098, 4102, 4104) vs "Di tản" (chunk 498) inconsistency resurfaces in this period.
- **"white boy"** — person side "thằng da trắng" (4081, 4083) vs the cocaine-slang side settled by the P0 fix — the split is back in dialogue.
- **"I'm done" / "I'm good" / "I'm down" / "I'm out"** — all deepened again in this period (see MEMORY.md wave entries for per-wave id lists).
- **"knuckle duster"** → "găng tay đấm bốc" (chunk 3582) — known likely-wrong rendering, should likely be "quả đấm sắt" (carried from earlier milestone).
- **"eff"/"effin'"** → "đệt" renderings keep accumulating — deferred until after the "Go fuck yourself!" decision.

## Open questions carried forward

- **"Go fuck yourself!" (pending):** fresh DB recount at 07:16 on 2026-11-22: 178 rows, 106 softened vs 71 crude. New softened-side addition in this period: 4097 1307C445 (exact, wave 326). New crude-side additions: none in this period. Option A (recommended): crude "Đi mà tự đụ đi" — follows the no-sanitizing rule. Option B: softened — fix the crude rows. Bulk fix to be applied after P3 finishes.
- **"nigga" (unresolved):** kept as loanword in most waves; 13 in this period (waves 324 and 328). Rows left as-is (status `machine`).
- **Polite-NPC pronoun question (open):** the long consistent "tôi" pattern for fearful/polite/sales lines, real police calls, people requesting police, fearful begging/surrender, polite civilian questions, witness statements, legal declarations, radio self-reports, formal staff voices, PA announcements, Jason's and Lucia's polite self-introductions — vs crew "tao/mày" on cooperate lines. New evidence this period listed above under "Polite-NPC pattern continues". Rows left as-is (status `machine`).
- **Couple-voice question (wave 194) and family-voice extension (wave 246):** Lucia/Jason couple scenes generally use "tao/mày"; mother↔daughter "mẹ/con" vs "tao/mày" — same open question family. "Ma" → "Má" vs "Mẹ" — NOT unified. "mama" → "Mẹ" vs kept loanword vs "Má" — NOT unified. "Mommy" → "Mẹ" vs kept loanword — NOT unified. "momma" → "mẹ" vs kept loanword vs "Má" — NOT unified.
- **"eff"/"eff-you" and "cougar":** deferred until after the "Go fuck yourself!" decision.
- **Standing P3-wide unresolved splits:** the full per-wave lists live in the MEMORY.md wave entries (waves 324–328) — consult them rather than re-deriving. Families include: "I got you"/"I got it"/"You got it" by context; "fuck with" mess-with vs AAVE "thích" vs joking vs teasing vs tampering; "get down" default vs high-place/come-here/arrival/fall-die/party; "I'm out" leaving vs out-of-ammo/money/stuff vs out-of-prison; "I'm done" finished vs fed-up vs doomed vs giving-up; "inside" prison vs elsewhere; "put you down" knock-down vs shooting vs land-the-plane; "take a shot"/"get a shot" shooting vs drink vs attempt vs photo; "Back up!" step-back vs calling-for-backup vs reverse-the-car; "hit" by context; "the Y" kept, unresolved; "lady"/"miss"/"officer" polite vs mocking/casual; "Hello" phone vs calling-out; "Princess" kept vs "công chúa"; "fence" physical vs stolen-goods; "bird" literal vs aircraft; "bike" "xe đạp" vs "xe máy"; "heat" cops-pressing vs pressure/teasing; "cover" yểm trợ vs chỗ nấp vs guarding-the-doors; "pool" hồ bơi vs bi-a; "piece" gun vs girlfriend vs share vs said-my-piece; "good shit" hàng ngon vs praise; "suck" be-bad vs literal; "milking" literal vs dragging-it-out; "call it" end-it vs call someone; "charge" battery vs money vs attack; "eat shit" fail side vs literal insult; "screw you" crude vs softened vs mild-but-crude.
