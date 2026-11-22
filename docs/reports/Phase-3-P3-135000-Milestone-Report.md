# Phase 3 — P3 Milestone Report: 135,000 Unique Strings

**Date:** 2026-11-21 (after wave 133 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **135,435 / 357,142 (37.9%)**; P3 remaining **221,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 135,435 = **221,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 325,202 = distinct source_ids (no duplicates)
**Waves in this milestone period (129–133):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 129 | 2126–2135 | 131,435 | Street/AAVE C0391 → store-robbery / shop-clerk voice C0392–C0394 → street/AAVE C0395 head (heavy "In Spanish:" counts) |
| 130 | 2136–2145 | 132,435 | C0395 tail → C0396 → C0397 → C0398 → female street/AAVE head C0399 |
| 131 | 2146–2155 | 133,435 | Female street/AAVE tail C0399 → shop-clerk robbery voice C0400–C0402 → posh rich NPC C0403 head |
| 132 | 2156–2165 | 134,435 | Posh rich NPC C0403 → street/AAVE C0404 → farm NPC C0405 → homeless/street community C0406–C0407 |
| 133 | 2166–2175 | 135,435 | Homeless/street community C0407 → posh rich/beach NPC C0408 → shop-clerk "bro" C0409 → street/AAVE C0410–C0411 |

## Incidents (all resolved, none outstanding)

- **Wave 129:** no incidents. All 10 files passed the full structure check; spot-checks aligned. All 10 handoffs arrived before loading.
- **Wave 130:** no incidents. Chunks 2136 and 2139 handoffs arrived late and were folded into the wave record afterwards. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 131:** no incidents. Chunks 2146, 2148 and 2154 handoffs arrived late and were folded into the wave record afterwards. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 132:** no incidents. All 10 files were complete and verified on disk before loading; all 10 handoffs arrived and their notes are folded into the wave record.
- **Wave 133:** no incidents. All 10 files were complete and verified on disk before loading; the chunk 2169 handoff arrived after loading and its notes were folded into the wave record afterwards.

## Conventions settled / reinforced in this period

- **Shop-clerk robbery voice (C0392–C0394, C0400–C0402, C0409):** clerk begging / police lines intentionally "tôi/cậu", confrontation "tao/mày" (chunks 2127–2133, 2149–2153, 2170, 2171); "Snapmatic" kept app name (chunks 2129, 2130, 2145, 2150); "Pester" kept app name (chunks 2145, 2147, 2151); "911" → "{number}" (chunks 2128, 2149, 2151, 2153, 2170); "safe" → "két" per chunk 2131 (chunks 2154, 2171); "register" → "ngăn kéo tiền" per the "Till"/"Cash Drawer" precedent (chunk 2170); "getaway driver" → "tài xế tẩu thoát" (chunk 2170); "JoySystem" kept game-console name (chunk 2170); "ATM" kept (chunks 2148, 2170); "get laid" → "được địt" crude side (chunks 2149, 2111).
- **Posh rich NPC (C0403, C0408, waves 131–133):** same character type as "Big Mama" C0381/C0385 — "tôi/cậu" throughout, keeping the posh tone even when swearing ("Suck my penis!" → "Bú cu tôi đi!", chunk 2155 C0403_7E59164E; "Lick my balls!" → "Liếm dái tôi đi!", chunk 2154 C0403_0126DFDD); "habibi" / "habibti" kept (chunks 2154, 2155, 2156, 2157, 2169); "UAE" kept (chunk 2154); "Alhamdulillah" kept (chunk 2168); "Mashallah" / "Inshallah" kept (chunk 2169); "Pegassi" kept car brand (chunk 2169); "Seashark" kept tour name (chunk 2168); "Leonida" kept (chunk 2156); "Pompadours" kept name (chunk 2156); "boss" → "sếp" (chunks 2154, 2156); "get some work done" → "phẫu thuật thẩm mỹ" surgery side per chunk 2155 (chunks 2154, 2156); "father" → "bố" (chunk 2168); "beautiful" → "người đẹp" when used as an address (chunk 2168); "Period, bro!" → "Chốt, bro!" (chunk 2168); "bench" → "đẩy tạ" per chunk 2144 (chunk 2168); "the Vault" → "Kho tiền" per P0 (chunk 2167); "VC" kept (chunk 2168).
- **Street / AAVE (C0395–C0399, C0404, C0410–C0411):** "In Spanish:" cues rendered "Nói tiếng Tây Ban Nha:" + translated content throughout — heaviest counts so far: chunk 2133: 27 cues; chunk 2134: 51 cues; chunk 2135: 48 cues; chunk 2136: 39 cues; chunk 2138: 30 cues; chunk 2139: 23 cues; chunk 2137: 24 cues; chunk 2160: 1 cue; chunk 2167: 0 cues in C0408. "smoke" (conflict) → "gây sự" (chunks 2134, 2135, 2137, 2140, 2141, 2145) vs drug side "hút thuốc" vs shoot side "bắn chết" (chunk 2138 "smoke a bitch" C0396_973614C8; chunk 2140 "catch smoke" → "ăn đạn" C0397_55C8E132); "pop" → shoot side (chunks 2133, 2134, 2135); "pop off" → shoot side (chunk 2043; chunk 2136 read as things blowing up C0395_E84619DE); "trippin'" many-way split ("phê" default / "làm quá lên" / panicking "tripped out" chunk 2144); "fuck on" → "cút đi" read as a "fuck off" variant (chunks 2133, 2134, 2135, 2136, 2171, 2172, 2173) vs sexual side when context is explicit (chunk 2008); "crash out" → "làm liều" (chunks 2142, 2143, 2144) vs car-crash "đâm xe" vs sleep "đi ngủ"; "get in that grid" → "vào cuộc" (chunks 2142, 2143, 2144); "free lick" → "vụ cướp dễ ăn" held (chunk 2142); "hit a lick" → "cướp được (một) vụ" (chunk 2144); "hitting licks" → "đi cướp vụ" (chunk 2144); "them people" → "bọn cớm" police side per chunk 2069 (chunks 2142, 2143); "jitterbug(s)" kept loanword (chunks 2142, 2143); "shitterbug" n/a; "chile" → "cưng" per chunks 2072/2073 (chunks 2145, 2147); "literally" kept as Gen-Z loanword per chunk 1926 (chunks 2149–2153 throughout C0400–C0402); "it's giving" → "Trông đúng kiểu..." Gen-Z reading (chunks 2145, 2152); "shawty" → "cưng" (chunk 2143) vs "cô em" (chunk 2144) vs "con nhỏ" (chunk 2141) — still inconsistent; "bum bitch" → "con đĩ vô gia cư" throughout C0407 (chunks 2165, 2166, 2167); "stuck on stupid" → "dính lấy cái ngu" (chunks 2165, 2167); "mob" → "đi lượn" (chunk 2163) vs "kéo nhau đi"/"xử" by context (chunk 2164); "get in that wind" / "in that wind" → "chuồn" per chunk 2045 (chunks 2163, 2164); "get back" → "trả thù" per chunk 2142 (chunk 2163); "fried" → "toang" passive per chunks 2001/2062/2142 (chunk 2164); "slaw" → "thằng ngáo" (chunk 2164) vs "chậm chạp" (chunk 2162 "Slaw as fuck." read as a variant of "slow") — still inconsistent; "fuck you up" → "đánh mày tơi tả" per chunk 2104 (chunks 2164, 2173); "get fucked up" → "ăn đòn" per chunk 2104 (chunks 2162, 2170); "hole" → "mồm" (chunks 2162, 2174); "tweaker" → "thằng nghiện" (chunk 2162) vs "thằng ngáo" per chunk 1957 (chunks 2160, 2174) — still split; "tweakin'" → "ngáo" per chunk 1957 (chunk 2174); "boy" → "nhóc" person side (chunks 2141, 2142, 2173) vs "cún" dog side (chunks 2175 C0411_4DBA4E3E "Growl at 'em, boy!") — by context; "get down" now eight-way (nằm xuống majority / quẩy / high-place "xuống khỏi đó" / come-here "xuống đây" / fight senses / "cúi xuống" / literal kneeling / quẩy party side; chunk 2126 come-here C0391_B397ACB3; chunk 2130 come-here C0393_636475E4; chunk 2154 high-place C0402_EB2EB01F; chunk 2170 come-here C0409_84B3979A; chunk 2174 default C0410_E7644F3F).
- **Farm NPC (C0405, wave 132):** "These crops ain't for sale" — "crops" read as farm crops (chunk 2160 C0405_03AA050C); "packin'" → "mang súng" (chunks 2158, 2161); "pussy" → "đồ hèn" coward per P0 vs "lồn" body side (chunk 2160 C0405_0848BA76 "Never seen a pussy so big.").
- **Homeless / street community (C0406–C0407, waves 132–133):** "twelve" → "cớm" (chunk 2164); "molly" kept loanword (chunk 2164); "shawty" → "cưng" (chunk 2164); "kin" → "họ hàng" (chunk 2164); "what you on" → "đang phê cái gì" drug side per chunk 1804 (chunk 2164); "about a dollar" → only caring about money (chunk 2164 C0406_DDBBEADB, C0406_FB8427DA); "zoomer" kept (chunk 2165); "HVAC school" → "trường dạy điều hòa" (chunk 2165); "pillhead" → "thằng nghiện thuốc" (chunks 2165, 2166); "chicken butt" → "mông gà" kept the kids' joke image (chunk 2165); "offender registry" → "danh sách tội phạm" (chunk 2165); "cuzzo" kept (chunk 2163); "fammo" kept (chunk 2163); "bumping ya' gums" → "lải nhải" (chunk 2163); "cleaned that boy's clock" → "đánh thằng nhóc đó tơi tả" (chunk 2163); "raise hell" → "làm ầm lên"/"làm loạn" (chunk 2163); "dog" → "con chó" when talking about a real dog (chunk 2163).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default (chunks 2158, 2159, 2160, 2161, 2162, 2166, 2167, 2171, 2172, 2174, 2175); crude sense "lồn" only where the sentence is clearly sexual / body-part (chunk 2160 C0405_0848BA76; chunk 2166 C0407_96302F7B read as coward "thằng hèn" — same chunk also has body-side rows; chunk 2169 C0408_FBC1A18D "Fuck the pussy you slithered out of!"); real-cat reading ("Here, pussy, pussy, pussy!" chunk 2087) still the only animal case.
- **"cooked"** — active "đỉnh" vs passive "toang" per chunks 2001/2062 vs chunk 2128's deliberate literal "nấu chín" (C0392_9573917F, joking store context) vs chunk 2129 passive "toang" C0392_EDA33737 — still split.
- **"parole"** → "việc tại ngoại" (chunk 2003) vs "án treo" (chunks 2005, 2006) vs "tại ngoại" (chunk 2136 C0395_D5CD01A9) — still inconsistent.
- **"I got you" / "I got it" / "gotcha"** — reassure vs understand vs caught — still by context ("I got it" → "Tao hiểu rồi" understand side chunk 2172 C0410_36CB5662 vs "Tao lo được vụ này" reassure side chunk 2175 C0411_8169BEB1 per chunk 2141).
- **"you got it"** — concession vs reassurance vs agreement vs understand vs attention vs encouragement — still by context (chunk 2140 concession C0397_59CC1508; chunk 2148 read as robbery side "Mày lấy hết rồi đấy, bro." C0400_3DF7E3D7 / "Đi đi! Mày có hết rồi!" C0400_59F2CCA1).
- **"on God"** → translated "thề với Chúa" (majority, chunks 2062/2063/2075; chunk 2143 C0398_6E84910E) vs kept loanword — still inconsistent.
- **"sugar baby" / "sugar daddy" / "sugar mama"** — kept loanword (chunks 2110, 2111, 2147 C0399_F2525375, 2155 C0403_7FE36CE9) — now consistent.
- **"RydeMe" / "Snapmatic" / "Pester"** — kept app names throughout — now consistent.
- **Slots kept correctly this period:** "911" → "{number}" (chunks 2128, 2149, 2151, 2153, 2170); "2004" → "{number}" (chunk 2170 C0409_2B3FA15D); "275" → "{number}" (chunk 2168 C0408_67E2C14C); "sixteen centimeters" / "hundred-dollar bills" kept as words because the skeleton has no slot (chunks 2154, 2155).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** Two more crude-side rows this period: chunk 2166 C0407_8F9215CB "Yeah, okay, go fuck yourself, ma'am!" → "Ừ, được rồi, đi mà tự đụ đi, thưa bà!" and C0407_D424ADDE "I'm done. Fuck yourself, bum bitch." → "Tao xong rồi. Tự đụ đi, con đĩ vô gia cư." — both rendered crude per chunk 2139 (C0396_E6D412FD), noted as pending the user's decision. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"let this shit go"** — split within wave 132 itself: chunk 2157 read as letting go "Buông vụ này ra" (C0404_10F051B6) vs chunk 2158 read as shooting "nổ súng" (C0404_40993863, C0404_5B84CC3B) — needs a decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"ASAP"** — translated "ngay lập tức" (chunk 2153 C0402_9F79EA14; chunk 2113; chunk 2047) vs kept loanword (chunk 2046; chunk 2079 C0375_A7934762) — still inconsistent.
- **"get laid"** — crude "được địt" (chunk 2149 C0400_AAFABFCA/C0400_B92DB2E7; chunk 2111 C0387_0091EE30) vs soft readings elsewhere — unresolved.
- **"lowkey"** — many-way split (kept / "thật ra" / "kín đáo" / "ngầm" / "hơi" / "thầm" chunk 2151 C0401_8B781FDF; chunk 2150 "hơi" C0401_5487015D; chunk 2152 kept; chunk 2169 kept C0409_1BBBA89B; chunk 2170 kept C0409_65210B83) — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword (chunks 2078, 2099, 2113, 2147 C0399_EBA26C66, 2168 C0408_A7EE1531) vs "Vice City" — still inconsistent.
- **"daddy"** — "bố" (majority, chunks 2156 C0403_B7F2027C, 2166) vs kept loanword as flirtatious address — still by context.
- **"you got me"** — caught vs concession vs challenge — still by context.
- **"trippin'"** — many-way split ("phê" default / "nổi điên" / alarm / bother / don't-worry / don't-care / panicking / agitated "làm quá lên") — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent.
- **"bike"** — "xe đạp" (majority) vs "mô-tô" / "xe máy" (minority) — still inconsistent.
- **"body"** — corpse vs living person — by context; "bodies" corpse vs manpower — by context (chunk 2175 corpse side C0411_6C68F997).
- **"bail"** — "bảo lãnh" vs "chuồn" vs "cứu ra khỏi vụ này" — still inconsistent.
- **"good looks"** — thanks vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" — by context (chunks 2128, 2129 both "chuồn").
- **"FYI"** — kept vs translated — still inconsistent.
- **"Madone!"** — kept — still undecided.
- **"mistress"** — "cô chủ" — still undecided.
- **"That's Negative."** — "phủ định" (majority) vs "Không phải." — still inconsistent.
- **"DOA"** — kept vs translated — still undecided.
- **"PIT"** — kept (waves 53–85) — still undecided.
- **"call it"** — many-way split (end-it side dominant; chunk 2126 end-it "Tao quyết rồi" C0391_8F6E6030; chunk 2125 end-it "Kết thúc đi" C0391_4D3180D8) — still by context.
- **"officer down" / "casualty"** — dead-vs-hurt ambiguity ("cảnh sát gục rồi" deliberately covers both).
- **"US Army"** — "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" — still inconsistent.
- **"ma'am"** — "thưa bà" vs "thưa cô" vs "cô ạ" — still inconsistent.
- **"move out"** — "rút lui" vs "di chuyển thôi" — still inconsistent.
- **"shocker"** — device vs name — still undecided ("súng điện" majority side).
- **"stun gun"** — "súng chích điện" (majority) vs "súng điện" — still inconsistent.
- **"jerkoff"** — "thằng thủ dâm" vs "thằng quay tay" — still inconsistent.
- **"lib" / "libs" / "libtard"** — renderings vary.
- **"Fire"** — blaze vs gunfire — still by context (chunk 2140 read gunfire C0397_2B0B7743).
- **"M7"** — unknown (kept).
- **"take a shot"** — three-way (shoot / drink / try / fight) — still by context.
- **"Skid mark"** — "Vệt phanh" vs "vết ố" — still split.
- **"Clown Town"** — translated vs place name — still inconsistent.
- **"Evil Eye"** — "Mắt Quỷ" vs loanword — still inconsistent.
- **"white trash" vs "trailer trash"** — handling split.
- **"vibe"** — kept vs translated — still by context.
- **"bag(s)"** — money vs drug sense vs literal — still by context (chunk 2129 read literal C0392_DB19D505).
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — "thao túng" (chunks 1896, 1972, 1973) vs kept — still by context.
- **"Tsou"** — kept as-is (chunks 1717, 1718) — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent ("ra tay" / "kiếm chác" / "đang hành động" / "chơi tới đi" / "chơi tới bến" / "lục túi mày" robbery side chunk 2135 C0395_AF40220F; "run it back" → "làm lại từ đầu" chunk 2150 C0401_5CA44D6F) — still inconsistent.
- **"bump"** — drug sense vs collision sense vs fight sense — by context.
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
- **"fuck with"** — hang-out / like-side readings vs the mess-with default "dây với" — by context; dislike reading "không ưa" added in chunk 1950; chunk 2128's C0392_6B2B176C flagged as possibly the dislike reading.
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
- **Source artifacts preserved as-is:** source typos read as intended ("know" read as "knew", chunk 2141 C0397_98FE1AE2; "up this" missing verb, chunk 2143 C0398_8567F95B; "Go they on!" broken, chunk 2142 C0398_263E5DF8; "live" read as "leave", chunk 2145 C0399_3EF3604A; "Fuck those motherfuckers go?" missing "where did", chunk 2136 C0395_DAE5567C; "I could have to arrested" broken, chunk 2155 C0403_492557AD; "Didn't I just forget your stupid face?" read as a dismissal, chunk 2161 C0405_42F40211; "Who the fuck are you thinking I'm gonna talk to you?" broken, chunk 2158 C0404_5D5E5C84; "What I need to spell it out for you?" missing "What,", chunk 2129 C0393_314F7422; "right fucking!" missing "now", chunk 2132 C0394_72115A17; "You're are dismissed." broken, chunk 2156 C0403_ED2064D1; "Shit, lemme our niggas..." missing "get", chunk 2146 C0399_B3B2B900; "How the... bitch if you don't get down!" truncated, chunk 2146 C0399_8E13F4D9; "Get... yeah, bitch, what now?" truncated, chunk 2146 C0399_A50E7E13; "Hell on outta here." truncated, chunk 2174 C0410_E1546C3C; "Who... the fuck you doing in here?" broken, chunk 2174 C0411_26ECBC85; "What the... if my phone broke..." truncated, chunk 2166 C0407_D30A6B92; "Fuck you after here?" broken, chunk 2162 C0405_FCC14AF7; "broker" read as a typo of "broke" (poorer), chunk 2165 C0407_066BAC3C).

## Next

- Wave 134 (chunks 2176–2185, C0411→) is translating now.
- Next milestone: **140,000** (wave 138).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
