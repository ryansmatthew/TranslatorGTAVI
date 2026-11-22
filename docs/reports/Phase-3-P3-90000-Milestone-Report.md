# Phase 3 — P3 Milestone Report: 90,000 Unique Strings

**Date:** 2026-11-21 (after wave 88 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **90,435 / 357,142 (25.3%)**; P3 remaining **266,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 273,531 = distinct source_ids (no duplicates)
**Waves in this milestone period (84–88):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 84 | 1676–1685 | 86,435 | Street/AAVE C0250 → rich/snobby tourists C0251 → street C0252 → tourists + rich old ladies C0253 |
| 85 | 1686–1695 | 87,435 | Tourists/civilians C0253 → civilians/tourists/streamers C0254 → snobby females C0255 → rich/snobby beach females C0256 → narcissistic beauty NPC C0257 head |
| 86 | 1696–1705 | 88,435 | Narcissistic photographer/beauty NPC C0257 → sassy/ballroom C0258 → rich/snobby C0259 → rich/snobby female C0260 → Spanglish tourist C0261 head |
| 87 | 1706–1715 | 89,435 | Spanglish tourist C0261 → Spanglish/immigrant tourist C0262 → street/AAVE C0263 → Cellerica/wellness + rich/snobby female C0264 |
| 88 | 1716–1725 | 90,435 | Rich/Cellerica female C0264 → rich/foreign tourist C0265 → street/AAVE C0266 → bro street C0267 → "skull crusher" muscle-bro C0268 head |

## Incidents (all resolved, none outstanding)

- **Wave 88, chunks 1720 and 1725:** both handoffs arrived late (after the wave had loaded from the on-disk files, which had passed the full structure check). Post-load DB checks verified 100/100 rows match the final files for both — no reload needed. Notes folded into the wave-88 MEMORY.md entry.
- **Waves 84–88 (all other chunks):** no incidents. All files passed structure check (100 items, ids in order, keys {id, vi}, 0 adjacent dups) plus spot-checks. All other 48 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **Spanglish tourist voice (C0261–C0262, chunks 1695–1710):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (16 items chunk 1705, 34 chunk 1706, 42 chunk 1709, 49 chunk 1708, 34 chunk 1710, incl. mid-sentence cues C0261_065BA9CF, C0261_308B3725, C0261_30FA0028, C0261_636D22FE, C0261_959708F0, C0261_A57DA9B9, C0261_AC9ADE1B, C0261_D605B0B3, C0261_DB189B61, C0261_F73A41EC, C0261_FB85306E); Spanish kept: Oye, ¡Oye!, Orale, Mira mija, Bueno, güey, si, No gracias, vato, gringo, "No me jodas." kept verbatim (C0262_4ACABECC); "pussy" → "đồ hèn" coward sense per P0, vs clearly sexual "Tao tới đây để địt lồn!" (C0261_3D293C88); "fuck with" → "dây với" (mess-with side); "fuck you up" → "đụ mày nhừ tử" (fight side); "sugar daddy" kept loanword (chunks 1708, 1709, 1710); "greencard" → "thẻ xanh"; "a ten" → "mười điểm" (per chunk 1642); "ghetto" → "quê mùa" (C0262_1B1B45BE); "queen" → "chị đại" (C0261_6230FFAD, C0262_5299A83B); "coca" kept (cocaine); register "tao/mày", police calls in polite "tôi" (C0261_9B6ACF77, C0262_240811FC).
- **"In Portuguese:" cues** — first appear in chunks 1692/1693 (wave 85), rendered "Nói tiếng Bồ Đào Nha:" + translated content per the "In Spanish:" precedent.
- **Street/AAVE confrontation voice (C0263, C0266–C0267, chunks 1710–1725):** "pussy" → "đồ hèn" coward sense per P0 (chunks 1711, 1712, 1719, 1720, 1722, 1723, 1725); "fuck with" → "dây với" (mess-with side); "trippin'" → "phê" (default side, chunks 1711, 1712, 1720) vs "đéo bận tâm" (don't-care side, chunks 1711 "She trippin'." vs 1712 "I ain't trippin' off you..." — split within chunk 1712) vs "làm quá lên" (agitated side, chunk 1711 C0263_6307123F); "smoke" → "đánh nhau" ("Move around unless you want smoke."); "it's up" → "tới luôn rồi"; "run a fade" → "đánh tay đôi"; "woofin'" → "sủa"; "on that type of time" → "sẵn sàng gây sự"; "switch" kept (auto-switch for a gun); "whip" → "xe"; "strapped" → "có súng", "the strap" → "khẩu súng"; "piece" → "khẩu súng"; "homie"/"yo"/"moe"/"my G"/"dog"/"bruh"/"Slim"/"nigga" kept loanwords; "ma" → "má" (chunk 1682 precedent); "love" → "cưng" ("Take care, love."); "bump" → "hít một liều" (drug sense, chunks 1710, 1717); "make moves" → "kiếm chác" (chunk 1720) vs "tiếp tục làm việc" (chunk 1721 C0266_C4E19848) — inconsistent; "bitch out" → "hèn nhát bỏ chạy" (chunk 1721 C0266_E69D7185); "puss out" → "nhát gan bỏ chạy" (chunk 1724); "roll out" → "chuồn" (chunk 1723); "let's bounce" → "chuồn thôi"; "get down" → "nằm xuống" (majority side, chunks 1712, 1719, 1721) vs "xuống khỏi đó" (high-place side, chunk 1712 "Get your goofy ass down from there!") vs "xuống đây" (come-here side, chunk 1724 C0267_FAD502AC 911 call); "you got it" → concession side ("mày thắng rồi", chunks 1711 C0263_5CBA3DC1, 1712 C0263_CD9C9CF7, C0263_DB430374) vs reassure side ("Tao lo vụ này", chunk 1710 C0263_1816F67C "I got you") — still by context; "I got this" → "tao lo vụ này" (reassure side, settled); "daddy" → "bố" (majority side, chunk 1712 C0263_936C7D61).
- **Rich/snobby + Cellerica/wellness voice (C0255–C0260, C0264, chunks 1686–1716):** "manifest" → "hiện thực hóa" (chunks 1713, 1714, 1715, 1716); Cellerica ranks/energies kept as names: Pillar, Lost Cause, PEACH, Cloud; "Cellerica"/"Cecilia"/"Manifestick"/"Bellville" kept; "she-tox" kept (detox/she wordplay); "de-stress cleanse" → "liệu trình thanh lọc giảm stress của Cellerica"; "jungle juice"/"kale smoothies" kept drink names; "hot yoga" → "hot yoga"; "pathological" → "bệnh hoạn"; "power couple" → "cặp đôi quyền lực"; "attorney(s)" → "luật sư"; "NDA"/"PR" kept; "designer" → "đồ hiệu"; "on a budget" → "xài đồ rẻ tiền"; "speed dial" → "quay số nhanh"; "cheekbones" → "gò má" (cosmetic-surgery reading, C0260_092E972F); "get down" → "nằm xuống" (majority side, chunks 1713, 1714); "grandma" → "bà cụ" (chunk 1684) vs "bà già" (chunk 1685) — inconsistent; "ma" → "má" (chunk 1682) vs kept loanword (chunks 1683, 1684) — inconsistent; "sugar baby" kept loanword (chunks 1691) vs "em cưng" (chunk 1659) — still inconsistent; "Go manifuck yourself!" → "Đi mà tự hiện thực hóa mình đi!" (chunk 1713 C0264_16CCA2C5, Cellerica wordplay kept — may need review if the "Go fuck yourself!" decision goes crude).
- **Rich/foreign tourist voice (C0265, chunks 1716–1719):** "Tsou" kept (unresolved — may be a name or an exclamation, chunks 1717, 1718); "pussy" → "đồ hèn" coward sense per P0; "fuck you up" → "đụ mày nhừ tử" (fight side, C0265_59284732); "get off me" → "xuống khỏi người tao"; "bump" → "hít một liều" (C0265_5089B78C); "ass sucker" → "đồ bú đít"; "assface" → "mặt đít"; "crack whore" → "con điếm nghiện crack"; "cocaine" kept; "America" → "nước Mỹ"; "limited edition" → "bản giới hạn"; "came off the lot" → "vừa mới ra khỏi hãng" (new car); "bad look" → "trông tệ vãi lồn"; "elite"/"peasant" → "giới tinh hoa"/"nông dân"; "net worth" → "tài sản"; "go full America" → "chơi kiểu Mỹ" (C0265_ED2BB166); police calls in polite "tôi" (C0265_3381DD7F, C0265_C8F1692B).
- **"Skull crusher" muscle-bro voice (C0268 head, chunk 1725):** "skull crusher" → "kẻ đập nát sọ" / "máy đập nát sọ"; "traps" → "cơ bắp" ("You see these fuckin' traps?"); "flex" → "khoe cơ bắp"; "bangin' bod" → "thân hình bốc lửa"; "Vinny" kept name; "pussy" → "đồ hèn" coward sense per P0; "fuck with" → "dây với" (mess-with side); "fuck you up" → "đụ mày nhừ tử" (fight side).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 1696, 1706, 1707, 1708, 1711, 1712, 1717, 1718, 1719, 1720, 1722, 1723, 1725); crude sense "lồn" only where the sentence is clearly sexual (chunk 1706 C0261_3D293C88, chunk 1707 C0261_D821680E "I'm here to get pussy...").
- **"fuck with"** → "dây với" (mess-with side) remains the default in street dialogue (chunks 1696, 1697, 1706, 1708, 1711, 1719, 1720, 1722, 1723, 1724, 1725); "thích" (like side) only where the sentence clearly means liking.
- **"go fuck yourself"** → crude "Đi mà tự đụ đi" side reinforced again (chunk 1706 "Go fuck yourself, asshole!" → "Đi mà tự đụ đi, thằng khốn!", chunk 1710 C0262_FDC938F5, chunk 1708 C0261_E0C2EE6D "They can go fuck themselves." → "Bọn nó cứ tự địt mình đi.") — the pending decision with the user is still unanswered.
- **"I got this"** → "tao lo vụ này" (reassure side, chunks 1696, 1711, 1714, 1719, 1723) — settled.
- **"trippin'"** → "phê" (default side) vs don't-care vs agitated "làm quá lên" — still by context.
- **"queen"** → "chị đại" (chunks 1697, 1698, 1699, 1706, 1709) — settled side.
- **"daddy"** → "bố" (majority side, chunks 1699, 1705, 1712) — "What's up, daddy?" → "Có gì không, bố?"
- **"911"** — `{number}` slot where the skeleton has one (chunks 1714 C0264_8E817959, 1723 C0267_9DFD08CA, 1724 C0267_FAD502AC) vs kept literal where it has none (chunk 1609) — follows the skeleton by design.
- **"bitch"/"motherfucker" read as car/weapon** — plausible by context but a real ambiguity class (earlier waves).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.
- **Police register (stable):** calls to police use polite "tôi" (chunks 1696, 1697, 1698, 1700, 1701, 1702, 1705, 1706, 1708, 1711, 1712, 1714, 1715, 1716, 1717, 1718, 1720, 1724); orders to suspects use "tao/mày" or direct imperatives.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1706 "Go fuck yourself, asshole!" (C0261, incl. the Spanish-cue version C0261_039D998C from wave 86), chunk 1708 C0261_E0C2EE6D, chunk 1710 C0262_FDC938F5. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"Tsou"** — kept as-is in chunks 1717/1718, unresolved: may be a name, an exclamation, or a foreign word (C0265_67D4BCEE, C0265_78CCC561, C0265_CAA85E33, C0265_D94879D3, C0265_DED523A2).
- **"make moves"** — "kiếm chác" (chunk 1720) vs "tiếp tục làm việc" (chunk 1721) — inconsistent.
- **"grandma"** — "bà cụ" (chunk 1684) vs "bà già" (chunk 1685) — inconsistent.
- **"ma"** — "má" (chunk 1682) vs kept loanword (chunks 1683, 1684) — inconsistent.
- **"sugar baby"** — "em cưng" (chunk 1659) vs kept loanword (chunks 1661, 1691) — inconsistent.
- **"get down"** — "nằm xuống" (majority) vs "xuống khỏi đó" (high-place) vs "xuống đây" (come-here) — still by context.
- **"you got it"** — concession side ("mày thắng rồi") vs reassure side ("Tao lo vụ này") — still by context.
- **"trippin'"** — "phê" (default) vs don't-care vs agitated — still by context.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" (chunk 1577) vs kept as name (chunks 830, 838) — still unresolved.
- **"pigs"** — "cớm" vs "lũ lợn" — still inconsistent.
- **"deep state"** — "nhà nước ngầm" (majority) vs "chính phủ ngầm" (chunk 1581) — still inconsistent.
- **"lowkey"** — kept loanword vs "thật ra" vs "kín đáo" vs "ngầm" vs "hơi" — still inconsistent.
- **"911"** — `{number}` slot where the skeleton has one vs kept literal where it has none — follows the skeleton by design.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot (e.g. "ten million" → "mười triệu", chunk 1719; "twenty-four hours" kept in word form, chunk 1711).
- **Source artifacts preserved as-is:** chunk 1707 "No fucking way! What is it now?s" (extra "s", C0261_930862B8); chunk 1706 "Fuck are you doing?" (missing "the", C0261_4C99C3FC); chunk 1723 "You're bring weird, bro" ("bring" for "being", C0267_7379D66C); chunk 1723 "can't put the toothpaste back in the that tube" (extra "the", C0267_9942BEAD); chunk 1722 "let's got!" ("got" for "go", C0267_3AF3ABFC).

## Next

- Wave 89 (chunks 1726–1735, C0268→C0272) is translating now.
- Next milestone: **95,000** (wave 93).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
