# Phase 3 — P3 Milestone Report: 95,000 Unique Strings

**Date:** 2026-11-21 (after wave 93 loaded; report written after wave 97 loaded — the period stays waves 89–93 per the established pattern)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **95,435 / 357,142 (26.7%)**; P3 remaining **261,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 279,014 = distinct source_ids (no duplicates)
**Waves in this milestone period (89–93):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 89 | 1726–1735 | 91,435 | "Skull crusher" gym bro C0268 → scared civilian C0269 → Cellerica/wellness C0270 → rich old lady C0271 → young rich bro C0272 head |
| 90 | 1736–1745 | 92,435 | Young rich bro (stuttering, mini golf) C0272 → old/mama AAVE C0273 → swamp/river folk C0274 → store clerk / Gen-Z street C0275 head |
| 91 | 1746–1755 | 93,435 | Street/Gen-Z C0275 → swamp/river folk C0276 → street C0277 → Cellerica/wellness C0278 → street C0279 head |
| 92 | 1756–1765 | 94,435 | Street/AAVE C0279 → Spanglish street C0280 → hippie/Cellerica C0281 → hippie/wellness C0282 head |
| 93 | 1766–1775 | 95,435 | Hippie/wellness C0282 → "Flizzy Flames" street C0283 → sanitation-worker street C0284 → street/Spanglish C0285 |

## Incidents (all resolved, none outstanding)

- **Wave 89, chunk 1731:** handoff arrived late (after the wave had loaded from the on-disk file, which had passed the full structure check). Post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into the wave-89 MEMORY.md entry.
- **Wave 90, chunk 1742:** handoff arrived late (same pattern). Post-load DB check verified 100/100 rows match the final file — no reload needed.
- **Wave 91, chunks 1748 and 1755:** both handoffs arrived late (same pattern). Post-load DB checks verified 100/100 rows match the final files for both — no reload needed.
- **Wave 92, chunks 1759 and 1763:** both handoffs arrived late (same pattern). Post-load DB checks verified 100/100 rows match the final files for both — no reload needed.
- **Waves 89–93 (all other chunks):** no incidents. All files passed structure check (100 items, ids in order, keys {id, vi}, 0 adjacent dups) plus spot-checks. All other 44 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **Gym-bro "skull crusher" voice (C0268, chunks 1726–1727):** "skull crusher" → "kẻ đập nát sọ" (per chunk 1725); "gains" → "lên cơ"; "pecs" → "cơ ngực", "biceps" → "bắp tay"; "pop off" → "nổi điên"; "tren" kept loanword (steroid trenbolone); "VC" kept in "VC Muscle Monstrosity Pro Cup"; "Deuces" → "Chuồn đây".
- **Rich old lady voice (C0271, chunks 1732–1735):** polite "tôi/cậu" throughout, even threats and insults — no "tao/mày"; "darling"/"dear"/"dearie" → "cưng à"/"cưng ơi"; "young man" → "anh bạn trẻ"; "finishing school" → "trường dạy lễ nghi"; "stolen valor" → "tội mạo danh quân nhân"; "new money" → "tiền mới"; "under par" → "dưới chuẩn" (golf wordplay); "bathing costume" → "đồ bơi".
- **Young rich bro, stuttering (C0272, chunks 1735–1738):** stutter dashes kept as in source ("M-mày", "t-tao", "Ừ-ừ", "f-f-fuck"); "mini golf" kept (the running setting — settling disputes on the mini-golf course); "on God" → "thề với Chúa" (majority side, chunks 1736, 1737); "fuck around and find out" → "đùa với lửa"; "get down" → "xuống khỏi đó" (high-place side, "Get down!" from up there).
- **Swamp/river folk (C0274, C0276, chunks 1740–1743, 1747–1749):** broken English, short and repetitive; "gator" → "cá sấu" (consistent); "Bubba" kept name; "Ma" → "má", "Pa" → "Ba"; "kin" → "người nhà"; "cleanfoot"/"cleanfeet" kept (city-clean people); "mud lady" → "mụ đầm lầy", "mud queen" → "nữ hoàng đầm lầy"; "great blue heron" → "diệc xanh lớn" (species-name rule); police calls keep "tao" for the broken-voice character instead of polite "tôi" (C0274_4A4E99B2, C0276_4A4E99B2, per precedent).
- **Gen-Z street voice (C0275, chunks 1744–1746):** "It's giving X" → "Nó toát lên vẻ X"; "nine" read as 911 ("get nine down here" / "calling nine" → "gọi 911"); "tweakin'" → "ngáo"; "deadass" → "nghiêm túc"; "5-0" → "{number} {number}" per skeleton; "vibe"/"lowkey"/"low-key"/"mood"/"bot"/"Sus"/"Defo"/"twin" kept loanwords.
- **Cellerica/wellness voice (C0270, C0278, C0281–C0282, chunks 1729–1732, 1752–1755, 1762–1767):** "manifest" → "hiện thực hóa" (consistent); "aura" → "hào quang" (consistent); Cellerica ranks kept as names (Whisper, Essentials, PEACH, Lost Cause); "Ten"/"Tens" → "mười điểm"/"hạng Mười" (per chunk 1642); "cleanse" → "thanh lọc"; "grounding"/"re-ground" → "nối đất"/"nối đất lại"; "Namaste" kept; "queen" → "chị đại" (settled side, chunk 1731); register split: polite/scared/begging lines use "tôi", confrontation/insult lines use "tao/mày".
- **Spanglish street (C0280, C0285, chunks 1758–1761, 1775):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content; Spanish kept (Oye, Mami, papi, coño, perico/yayo = cocaine, Dale!, ¡Tu puta madre!); "fuck face" → "thằng mặt địt"; "drugs running a train" → "thuốc đang hành... tơi tả"; "pussy" → "đồ hèn" (coward side, default) vs crude "lồn" (explicit sexual, e.g. C0280_479F733E "Go wash your pussy") vs "con đĩ lồn" (general insult, C0280_02BBF7A2 "pussy bitch").
- **Sanitation worker (C0284, chunks 1771–1773):** "sanitation worker" → "nhân viên vệ sinh"; "dumpster divin'" → "bới thùng rác"; "porto potty" → "bồn cầu di động"; "chemical toilet" → "bồn cầu hóa chất"; "street sweeper" → "xe quét đường"; "roadkill" → "xác bị cán chết"; "sewer gator" → "cá sấu cống"; "Ms. Bitch" → "Cô Đĩ"; "head bitch" → "con đĩ đầu đàn"; "Chat" kept loanword (livestream).
- **"Flizzy Flames" character (C0283, chunks 1768–1770):** nonsense bark sounds kept verbatim ("Bladdow", "Blap", "Brap", "Shakalaka", "brrap", "spladdap", "Hellur skiddur", "Scooty booty"); "Lil' Flizzy the Flame"/"Flizzy Flames"/"Lil' Flizzy" kept names; "thrash" → "quậy banh nóc" / "quậy" (the character's signature verb); "wil' out" → "quậy tưng bừng"; "baby mama"/"baby moms" → "mẹ của con tao"; "wavy or straight" → "đang phê hay tỉnh"; "Gravy!" → "Ngon!"; "cougar-cita" kept (cougar + mamacita wordplay, C0283_55289662).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 1726, 1727, 1736, 1739, 1757, 1758, 1768, 1770, 1772, 1775); crude sense "lồn" only where the sentence is clearly sexual (chunks 1738, 1739, 1740, 1748, 1750, 1751, 1773).
- **"fuck with"** → "dây với" (mess-with side) remains the default in street dialogue (chunks 1726, 1727, 1736, 1737, 1738, 1739, 1740, 1744, 1745, 1746, 1749, 1750, 1751, 1752, 1757, 1759, 1768, 1769, 1771, 1772, 1773, 1775); "thích" (like side) only where the sentence clearly means liking.
- **"I got this" / "I got you"** → "tao lo vụ này" / "tao lo cho mày" (reassure side) — settled (chunks 1727, 1737, 1738, 1739, 1751, 1752, 1758, 1759, 1770, 1772, 1774).
- **"you got it"** → "mày thắng rồi" (concession side) — dominant (chunks 1728, 1738, 1744, 1768, 1774, 1775).
- **"get down"** → "nằm xuống" (majority) vs "xuống khỏi đó" (high-place) vs "xuống đây" (come-here) — still by context.
- **"I'm out" / "bounce" / "dip"** → "chuồn" — settled.
- **"trippin'"** → "phê" (default side) vs don't-care vs agitated — still by context.
- **"on God"** → "thề với Chúa" (majority side, chunks 1736, 1737, 1745).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.
- **Police register (stable):** calls to police use polite "tôi" (chunks 1726, 1727, 1729, 1730, 1737, 1744, 1750, 1751, 1752, 1761); orders to suspects and threats use "tao/mày" or direct imperatives; street police calls spoken to bystanders (not 911 calls) use "tao" (chunk 1756 precedent).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** No new rows flagged in this period. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"Rivers" / "river kin" / "snapper" / "pythie"** — inconsistent across chunks 1740–1743, 1747: "Rivers" kept as a name (chunk 1740) vs "Sông" (chunks 1741, 1747, 1748); "river kin" → "họ sông nước" vs "họ hàng sông" vs "người nhà"; "snapper" → "rùa" vs "rùa cắn"; "pythie" → "trăn" vs "trăn nhỏ".
- **"crystal"** — "đá pha lê" (chunk 1752) vs "tinh thể" (chunks 1754, 1755) — inconsistent.
- **"sister(s) of (the) earth"** — three variants: "chị em của Trái Đất" (chunk 1752), "chị em của đất mẹ" (chunk 1753), "chị em của trái đất" (chunk 1754).
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunk 1764) — inconsistent.
- **"vibes" / "vibrations"** in C0278–C0282 wellness chunks — split between kept loanword, "năng lượng", and "rung động" — by context, unresolved as a class.
- **"cougar-cita"** kept as wordplay (chunk 1768, C0283_55289662) — the "cougar" decision is still deferred.
- **"make moves" / "make a move"** — "kiếm chác" vs "tiếp tục làm việc" vs "ra tay đi" — still inconsistent.
- **"get fucked"** — passive side "đi mà bị địt đi" vs fight side "bị đụ nhừ tử" — by context.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"pigs"** — "cớm" vs "lũ lợn" — still inconsistent.
- **"deep state"** — "nhà nước ngầm" (majority) vs "chính phủ ngầm" — still inconsistent.
- **"lowkey"** — kept loanword vs "thật ra" vs "kín đáo" vs "ngầm" vs "hơi" — still inconsistent.
- **"911"** — `{number}` slot where the skeleton has one vs kept literal where it has none — follows the skeleton by design.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; "5-0" → "{number} {number}".
- **Source artifacts preserved as-is:** stuttering kept as in source (C0272, chunks 1736–1738).

## Next

- Waves 94–97 have already loaded (wave 97 brought P3 to 99,435); wave 98 (chunks 1816–1825, C0299→C0302) is translating now.
- Next milestone: **100,000** (wave 98).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
