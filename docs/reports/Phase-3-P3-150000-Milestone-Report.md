# Phase 3 — P3 Milestone Report: 150,000 Unique Strings

**Date:** 2026-11-21 (after wave 148 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **150,435 / 357,142 (42.1%)**; P3 remaining **206,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 150,435 = **236,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 341,972 = distinct source_ids (no duplicates)
**Waves in this milestone period (144–148):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 144 | 2276–2285 | 146,435 | Police tail C0449 → street/AAVE C0450 → Cellerica voice C0451–C0452 → police C0452–C0453 |
| 145 | 2286–2295 | 147,435 | Police C0453 → street C0454 → police C0455–C0456, incl. sobriety-test lines |
| 146 | 2296–2305 | 148,435 | Police C0456–C0457 → paranoid conspiracy NPC C0458 → street/AAVE C0459–C0460 |
| 147 | 2306–2315 | 149,435 | Street/AAVE C0460 → Spanglish C0461 → street/AAVE C0462–C0463 |
| 148 | 2316–2325 | 150,435 | Street/AAVE C0463 → fisherman/dock NPC C0464 → flamboyant nude realtor NPC C0465 → fashionista C0466 → Canadian tourist NPC C0467 |

## Incidents (all resolved, none outstanding)

- **Wave 144:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 145:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 146:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 147:** no incidents. Chunks 2308, 2309 and 2310 were loaded from disk-verified files before their handoffs arrived (late-handoff precedent); all three handoffs arrived afterwards and their notes were folded into the wave record. Chunk 2307's first merge came out 52/48 and the agent fixed it to 50/50 by script before the final re-verification. Chunk 2308's first merge was 46/54, also fixed before merging. All 10 files passed the full structure check; spot-checks idx 0/49/99 aligned.
- **Wave 148:** no incidents. Chunk 2325's file was verified on disk before its handoff arrived. Chunk 2324's part-2 last 2 items were swapped and the agent fixed the order before merging. All 10 files passed the full structure check; spot-checks idx 0/49/99 aligned.

## Conventions settled / reinforced in this period

- **Street / AAVE barks (C0460–C0463, waves 147–148):** "tao/mày" throughout, crude register kept ("bitch" → "con đĩ", "fuck" → "địt mẹ"/"đéo", "motherfucker" → "thằng chó chết"); "tweakin'"/"tweaker" → "ngáo"/"ngáo đá" (chunks 2307, 2311); "free licks" → "vụ cướp dễ ăn" (chunks 2307, 2308); "trippin'" → "phê" default (chunks 2307, 2312); "fuck you up" → "địt mày tơi tả" (chunks 2311, 2312, 2313); "fuck with" → "dây với" mess-with default (chunks 2306, 2312, 2313); "throw hands" → "đấm nhau" (chunks 2313, 2315); "square up" → "đánh tay đôi" (chunk 2315); "dip" → "chuồn" (chunk 2315); "jit" kept loanword (chunk 2315); "big mama" → "Mama Lớn" per chunks 2088/2105/2108 (chunk 2315); "joint" drug side → "điếu cần" (chunk 2315); "what ... on?" drug side → "đang phê cái gì" (chunks 2313, 2315); "smoke" = gây sự unless shooting context, then bắn (chunk 2314); "get down" default "nằm xuống" (chunk 2321) vs high-place "xuống khỏi đó" vs come-here "xuống đây" vs party "quẩy" (chunk 2308 C0461_02724150, C0461_11021292 — new reading); "you got it" concession side → "mày thắng rồi" (chunks 2315, 2322, 2323) vs attention side vs understand side — by context; "I got you" caught side vs reassure side — by context; "pussy" coward side → "đồ hèn" throughout (chunks 2306–2315); "shawty" → "em gái", "lil bro" → "thằng em", "lil mama" → "em gái" (chunks 2306, 2315); "bike" → "xe đạp" majority (chunks 2306, 2308); "body" → "cái xác" corpse side (chunk 2306); "slide" → "chuồn" (chunk 2306); "Sanchez"/"Trav" kept as names (chunk 2306); "short bus" → "xe buýt đặc biệt" (chunk 2307); "strapped" → "súng sẵn sàng" (chunk 2307); "up a creek" → "lâm vào thế bí" (chunk 2307); "take it there" → "làm tới luôn" (chunks 2307, 2323); "off a bean" → "phê thuốc" (chunk 2307); "It's up for ya ass!" → "Tới lượt mày rồi đấy!" (chunk 2307); "get jumped" → "bị hội đồng" (chunk 2314); "mark" → "thằng con mồi" (chunk 2313); "tap that" → "chịch con đó" (chunk 2313); "stand on business" → "sẵn sàng xử lý vụ này" (chunk 2313); "stripes" → "uy tín" (chunk 2313); "That's twin" → "anh em sinh đôi của tao" (chunk 2313).
- **Spanglish / Cuban voice (C0461, wave 147):** "In Spanish:" cues rendered "Nói tiếng Tây Ban Nha:" + translated content — chunk 2311: 10 cues; chunk 2312: 7 cues; chunk 2309: 6 cues; chunk 2308: 5 cues; chunk 2310: 3 cues. "Oye"/"Ay"/"mami"/"bro"/"bruh" kept; "coked out" → "phê coke" (chunk 2311); "OD" kept (chunk 2311); "parlay" → "cược xiên" (chunk 2311); "Little Cuba" kept (chunk 2311); "tostones"/"empanada" kept (chunk 2312); "Cuban royalty" → "Hoàng tộc Cuba" (chunk 2312 C0461_FAB9BB0A) vs "hoàng gia Cuba" (chunk 2310 C0461_6B0FE5E2, C0461_96C8BAC8) — **split, flagged for review**; "trap house" → "nhà trap" (chunk 2309); "pack" → "gói hàng" drug side (chunk 2309); "hit the bag" → "đấm bao cát" (chunk 2309); "got popped" → "bị bắn chết" (chunk 2309); "bodies" → "xác" corpse side (chunk 2309); "two piece" → "combo hai cú đấm" (chunk 2309); "buck fifty soaking wet" → "150 pound cả khi ướt sũng" literal (chunk 2309); "tax" → "thuế đường phố" (chunk 2310); "Reuben" kept (chunk 2310); "Craziest Block In Leonida" kept as a name (chunk 2310).
- **Fisherman / dock NPC (C0464, wave 148):** NOT street/AAVE — a fishing/beach voice: victims begging, threats, fishing wordplay. Species names translated: "snapper" → "cá hồng", "porgy" → "cá tráp", "barracuda" → "cá nhồng" (chunk 2317); fishing metaphors kept: "angler" → "cần thủ", "on the hook" → "mắc câu", "put a hook in it" → "móc câu vào mồm mày", "catch of the day" → "mẻ câu của ngày hôm nay" (chunks 2316, 2317); "take you out on the boat" → đưa ra thuyền, not a date or a kill (chunk 2317); "ma'am" → "thưa bà" majority (chunks 2316, 2318); "bucko" → "nhóc con" (chunk 2318); "off the hook" → "thoát rồi đấy" (chunk 2318); "vibe" kept loanword (chunk 2318); "cock" → "cặc" (chunk 2318). Fearful/polite lines use "tôi" (chunks 2316, 2317, 2318) — see the open question below.
- **Flamboyant realtor NPC (C0465, wave 148):** a panicked, stuttering, apparently nude real-estate broker obsessed with "networking" ("free all your parts", "my penis has been out", "Clothes were getting in the way of my business deals"). "open house" → "buổi xem nhà" (chunks 2319, 2321), with the pun kept once: "biến cái sọ của mày thành nhà mẫu mở cửa cho xem!" (chunk 2320 C0465_A076E605); "closer" → "dân chốt sale" (chunk 2320); "walkthrough" → "buổi xem nhà" (chunk 2321); "listing" kept (chunk 2321); "realtor's rage" → "cơn thịnh nộ của một môi giới bất động sản" (chunk 2321); "blackball" → "tẩy chay" (chunk 2319); "crack" kept (chunk 2319); "close this deal" → "chốt vụ này" (chunk 2319); "get by" → "qua đây" (chunk 2319); "piece" → súng ("Sold it for crack", chunk 2321 C0465_B6FB6023); "ride" → xe (chunk 2321); "gooch" → "háng" (chunk 2320); "did a line" → "hít một đường" cocaine side (chunk 2320); "Get the fuck down from there!" → "Cút mẹ xuống khỏi đó đi!" high-place side (chunk 2320); "alpha energy" kept "alpha" (chunk 2321). Sales/polite lines use "tôi" + "anh/cô", threats/swearing use "tao/mày" (chunks 2319, 2320, 2321) — see the open question below.
- **Fashionista / fashion week (C0466, wave 148):** "fit check" → "kiểm tra đồ" (chunks 2323, 2324); "whip" → "xe" (chunks 2323, 2324); "drip" kept loanword (chunk 2322) vs "Chất." (chunk 2323) — still split; "bussin'" → "phê lắm" (chunk 2323); "Gutter & Blood" kept (chunk 2323); "Val-de-Grâce" kept (chunk 2323); "Klose" kept as a brand (chunk 2322); "Jack of Hearts" kept as a place (chunk 2322); "Matic" kept as an app (chunks 2322, 2323); "Leonida"/"Liberty City" kept; "pool" → "hồ bơi" pool-party precedent (chunk 2322); "swear to God" → "thề với Chúa" (chunk 2323); "room at Y" kept "Y" (chunk 2323 C0466_AC1C4B0A — "the Y" still unresolved); "Fuck you got on" → "mày đang mặc cái đéo gì" (chunk 2323).
- **Canadian tourist NPC (C0467, wave 148):** "bud"/"buddy"/"eh"/"hoser"/"toque"/"Jesus Murphy" kept; "Canadians" → "người Canada" (chunk 2325); "eff"/"effin'"/"eff you" → "đệt" per the pending-decision precedent (chunks 2324, 2325 — "un-effable" → "không-đệt-được"); "moose" → "nai sừng tấm" (chunk 2324); "back bacon" → "thịt xông khói Canada" (chunk 2324); "five-point buck" → "hươu đực năm nhánh" (chunk 2324); "bum"/"arses" → "mông" (chunk 2324); "stones" → "gan" (chunk 2324); "jackoff" → "thằng thủ dâm" (chunk 2324); "johnson" → "cặc" (chunk 2324); "Get a room!" → "Kiếm phòng mà làm đi!" (chunk 2324); "hang a Larry" → "rẽ trái", "ten clicks" → "mười cây" (chunk 2325); "paws" → "tay" hands side (chunk 2325 C0467_9033C0DC); "mess with me" → "dây với tao" (chunk 2325); "daddy"/"mommy"/"sugar boy" kept as flirtatious address (chunk 2325).
- **"pussy"** → coward sense "đồ hèn" remains the clear default (chunks 2306–2315, 2324); crude sense "lồn" only where the sentence is clearly sexual / body-part — still by context.
- **"get down"** — now a nine-way split: "nằm xuống" default / "xuống khỏi đó" high-place / "xuống đây" come-here / "quẩy" party side (chunk 2308) / "chơi" / "đánh nhau" / "xuống xe" / "đi xuống" / "làm tới" — still by context, flagged per row.
- **Slots kept correctly this period:** "100" → "{number}" (chunk 2312 C0461_EB46C8BE); "911" → "{number}" (chunk 2325 C0467_70A9DE7B).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" — DECISION STILL PENDING with the user.** New crude-side rows this period: chunk 2311 C0461_D324D618 "Oye! Go fuck yourself..." → "Oye! Đi mà tự đụ đi..."; chunk 2322 C0466_562F090E "Go fuck yourself, bruh!" → "Đi mà tự đụ đi, bruh!". Related variants this period: chunk 2317 C0464_381149D8 "Screw yourself!" → softened "Đi mà tự sướng đi!" vs chunk 2317 C0464_865DC247 "Suck yourself!" → crude "Tự bú đi!" — the same family split inside one chunk. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"tao/mày" vs "tôi" for polite NPC lines — NEW open question this period.** The brief said "tao/mày throughout" for the street barks, but C0464–C0466 are not street voices: agents used "tôi" for fearful/polite lines (chunk 2316 C0463_EF726D5B, C0464_00A8568C, C0464_2B17127B; chunk 2317 C0464_70FEC798; chunk 2318 C0464_B388C6B5), for sales/polite realtor lines in "tôi" + "anh/cô" (chunk 2319), for calling the police (chunk 2321 C0465_F6D68AC0; chunk 2322 C0466_422D0BCA) and for polite begging (chunk 2322 C0466_73E01613). This matches the settled police/service-call precedent (radio self-reports and polite questions in "tôi"), but whether the whole C0464–C0466 run should be unified to "tao/mày" or keep the split is undecided — flagged for review, not changed.
- **"networking" three-way split (chunk 2319):** verb → "giao lưu" (majority) vs noun "network" → "mạng lưới" (C0465_0D9924A1) vs "you'll network like crazy" → "kết nối điên cuồng" (C0465_128CD678) — still inconsistent.
- **"Cuban royalty" split:** "hoàng gia Cuba" (chunk 2310) vs "Hoàng tộc Cuba" (chunk 2312 C0461_FAB9BB0A) — still inconsistent.
- **"drip" split:** kept loanword (chunk 2322) vs "Chất." (chunk 2323) — still inconsistent.
- **"set the box" split:** "Chặn nó lại!" (chunks 2212, 2262, 2274, 2285-era 2287/2288) vs "lập vòng vây" (chunk 2258, chunk 2296 C0456_8CEAF731) vs "Lập vòng vây đi!" (chunk 2275 C0449_92F13772, chunk 2298 C0457_7208DCDA); "boxed in" → "Giữ nó bị chặn lại!" (chunk 2264).
- **"paws" split:** "chân" furry/K9 side vs "tay" hands side (chunks 2222, 2240, 2287, 2296, 2325 C0467_9033C0DC) — by context, flagged per row.
- **"officer down"** → "cảnh sát gục rồi" settled vs chunk 2243's one-off "cảnh sát bị đánh nặng rồi" (C0438_A5A8E389).
- **"sleeper agent" three-way split in C0441:** "đặc vụ ngủ" (2249, 2252) vs "đặc vụ ngủ đông" (2251) vs "đặc vụ ngủ quên" (2250).
- **"pig(s)" police-insult split:** "lũ cớm" (chunk 2259) vs "đồ lợn" (chunk 2252 C0441_C16919C7) vs literal pig readings elsewhere.
- **"smelled pussy" split:** coward "mùi hèn" (chunk 2138; chunk 2253 C0442_344B8D80) vs body side "mùi lồn" (chunk 2188; chunk 2253 C0442_39ED4D5B).
- **"let this shit go" split:** letting-go (chunk 2157; chunk 2279) vs shooting (chunk 2158).
- **"I got you" / "you got it" / "you got me"** — still by context (caught / reassure / understand / concession / attention / win-lose sides all attested this period).
- **"trippin'"** — many-way split ("phê" default / "làm quá lên" / panicking) — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent as a class.
- **"bike"** — "xe đạp" majority vs "mô-tô" minority — still inconsistent.
- **"body"** — corpse vs living person — by context.
- **"call it"** — end-it dominant — still by context.
- **"ASAP" / "pronto"** — translated vs kept — still inconsistent.
- **"VC"** — expanded vs kept — still inconsistent.
- **"daddy"** — "bố" majority vs kept loanword as flirtatious address (chunk 2325 C0467_A105F96A) — still by context.
- **"mommy"** — kept loanword (chunk 2325 C0467_A19C7318) vs "mẹ" — still by context.
- **"lowkey"** — many-way split — still by context.
- **"vibe"** — kept vs translated — still by context.
- **"the Y" / "Y Hotel"** — kept vs "khách sạn Y" — still unresolved (chunk 2323 "room at Y").
- **"eff" / "eff-you"** — "đệt" renderings continue (chunks 2324, 2325) — deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — still deferred behind the pending "Go fuck yourself!" decision.
- **"$"-loss and "%"-loss via the placeholder-slot exception** continue; skeleton decimal splits continue; skeleton-forced slots on non-numbers continue ("911" → "{number}", chunk 2325).
- **Source artifacts preserved as-is this period:** broken "You known around here?" (chunk 2307 C0460_9210197B); truncated "You ain't violating my probation under." (chunk 2307 C0460_95068F53); "closed you're fucking eyes" ("closed your", chunk 2309 C0461_4505F541); "somone" → "someone" (chunk 2315 C0463_B0DAA0DF); "harrass" (chunk 2319 C0465_252E0D45); "oufit's" → "outfit's" (chunk 2323 C0466_905D5A96); "come back me up" ("come back and back me up", chunk 2323 C0466_91F2BAA3); "scivey" unknown, maybe "scurvy" (chunk 2325 C0467_802C2650); truncated "Are you fucking... Why?" and "Don't fucking... do not!" kept dangling (chunk 2320 C0465_662BE34B, C0465_7BFA648C).

## Next

- Wave 149 (chunks 2326–2335) is being spawned now.
- Next milestone: **155,000** (wave 153).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
