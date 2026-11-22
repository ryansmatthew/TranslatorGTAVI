# Phase 3 — P3 Milestone Report: 100,000 Unique Strings

**Date:** 2026-11-21 (after wave 98 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **100,435 / 357,142 (28.1%)**; P3 remaining **256,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 284,607 = distinct source_ids (no duplicates)
**Waves in this milestone period (94–98):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 94 | 1776–1785 | 96,435 | Street/Spanglish C0285 tail → annoyed tourist/beach NPC C0286 → street/Spanglish C0287 → rich/snobby tourist C0288 → foreign tourist C0289 head |
| 95 | 1786–1795 | 97,435 | Foreign tourist/Spanglish + diva/snob beach C0289 → annoyed ordinary NPC C0290 → street/Spanglish C0291 → nerd/socially-awkward NPC C0292 head |
| 96 | 1796–1805 | 98,435 | Nerd NPC C0292 → beach/nerd NPC C0293 → worried ordinary NPC + shy Gen-Z female C0294 → street/AAVE C0295 → street C0296 head |
| 97 | 1806–1815 | 99,435 | Street/AAVE C0296 → suburban mom/conspiracy C0297 → grumpy old beach man / Jewish NY old man C0298 → old lady C0299 head |
| 98 | 1816–1825 | 100,435 | Old lady C0299 → female influencer / ghost guns C0300 → snob/aristocratic rich C0301 → Spanglish/santera C0302 |

## Incidents (all resolved, none outstanding)

- **Wave 94, chunk 1779:** first draft swapped the ids at idx 9/10 (C0286_F795C5FE ↔ C0286_F7DCE378) — agent self-detected via its structure check, fixed, re-checked 100/100 in order before handoff.
- **Wave 94, chunks 1780 and 1783:** handoffs never arrived before loading (1780's handoff arrived 2026-11-21 ~19:57, after the wave had loaded). Both files had passed the full structure check on disk and were loaded per the established precedent; post-load DB checks verified 100/100 rows match the final files for both — no reload needed. Notes folded into the wave-94 MEMORY.md entry.
- **Wave 95, chunks 1790 and 1793:** handoffs never arrived before loading (1790's handoff arrived 2026-11-21 ~19:57, after the wave had loaded). Same pattern: files verified on disk, loaded per precedent, post-load DB checks verified 100/100 rows match the final files for both — no reload needed. Notes folded into the wave-95 MEMORY.md entry.
- **Wave 96:** no incidents. All 10 handoffs arrived before loading.
- **Wave 97:** no incidents. All 10 handoffs arrived before loading.
- **Wave 98, chunk 1820:** first draft swapped the pair at idx 71/72 (C0301_1E6FD4F1 "She's my queen..." ↔ C0301_1ECEE07A "Walk away. Do it!") — agent self-fixed, disk check idx 70–73 confirmed alignment before loading.
- **Wave 98, chunks 1821 and 1825:** handoffs never arrived; files verified on disk and loaded per the established precedent; post-load DB checks verified 100/100 rows match the final files for both — no reload needed.

## Conventions settled / reinforced in this period

- **Rich/snobby tourist voice (C0288, chunks 1783–1785):** polite "tôi/cậu" throughout per chunks 1733/1734, even swearing; "Cribcrash" kept name; "spring for collision" → "mua bảo hiểm va chạm"; "attourney" (source typo) → "luật sư"; "get down here" → "xuống đây" (come-here side); police calls in polite "tôi".
- **Foreign tourist / Spanglish diva (C0289, chunks 1786–1788):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (30 items chunk 1786, 38 chunk 1787, 34 chunk 1788); Spanish kept (Oye, papi, mami, cabrón, chica, tia, gracias, adios, ¡Tu puta madre!); "daddy" kept loanword as flirtatious address (C0289_111F6B6B, per chunks 1489/1509); "sugar babies" kept; "queen" → "chị đại" (settled side, C0289_D905EFFC); "get fucked" → "đi mà bị địt đi" (passive side); "pussy" → "lồn" (explicit sexual) vs "đồ hèn" (coward) vs "con đĩ lồn" (general insult, C0289_5B5BAAB9 "Pussy bitch!").
- **Annoyed ordinary NPC (C0290, chunks 1789–1794):** register split — polite "tôi/cậu" in complaint/police-call lines vs "tao/mày" in confrontation/insult lines; "Leonida" kept name; "Leonidans" → "dân Leonida" (chunk 1790, C0290_69972445, C0290_9B5388B9); "San Fierro" kept name; "get down" → "nằm xuống" (majority side, C0290_5FAC1AF8); "daddy" → "bố" (majority side, C0290_A2D4782D); "decoy phones" → "điện thoại mồi"; "gun nut" → "thằng cuồng súng"; "aneurism" → "phình động mạch não"; "sick thrills" → "cảm giác mạnh bệnh hoạn".
- **Nerd / socially-awkward NPC (C0292, chunks 1795–1797):** polite "tôi/cậu" throughout per the wellness/snob precedent, except direct threats using "tao/mày"; "fap lair" → "hang quay tay"; "goon cave" kept loanword; "pocket pussy" → "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797) — minor inconsistency, see quality notes; "succubus" → "nữ quỷ" (chunk 1795) vs kept loanword (chunk 1763) — still inconsistent; "boy" read as a dog in guard-dog/K9 command lines (chunks 1796, 1798, 1799: "Now, boy! Attack!" → "Nào, cún! Tấn công!", "Heel boy! Heel!" → "Sát chân, cún! Sát chân!"); "Daddy" → "Bố" when spoken to a dog (C0293_ECEAE8DA).
- **Street/AAVE (C0295–C0296, chunks 1803–1808):** "fuck with" → "dây với" (mess-with side); "trippin'" → "phê" (default) vs don't-worry ("don't even trip" → "đừng lo", C0296_ACFFED97) vs don't-care ("trippin' off", C0296_A954F55E); "heat" → "súng" (C0296_D3D6C9D0); "paper" → "tiền"; "panic room" → "phòng trú ẩn"; "drivers ed" → "học lái xe" (per chunk 1802); "bike" → "xe đạp" (majority side, C0295_D52734D7); "get down" → "xuống khỏi đó" (high-place side, C0295_6607FE02).
- **Suburban mom / conspiracy (C0297, chunks 1809–1811):** polite "tôi/cậu" throughout; "soccer mom" → "bà mẹ bóng đá"; "momfluencer"/"mommy blogger" kept loanwords; "mommy blog"/"mommyblog" → "blog mẹ bỉm"; "deep state" → "nhà nước ngầm" (majority side); "heck around and find out" → "Đùa với lửa đi rồi biết!" (per the "fuck around and find out" precedent); "Snowball" kept name; "cut of your jib" → "cái tướng của cậu" ("globalist jib" → "cái tướng của bọn toàn cầu hóa"); "Self Defense for Menopausal Patriots" → "Tự vệ cho các bà yêu nước mãn kinh"; "brain control fillings" → "trám răng điều khiển não".
- **Grumpy old men (C0298, chunks 1811–1814):** register split — chunk 1812 polite "tôi/cậu" per the rich/tourist precedent vs chunks 1811/1813 "tao/mày"; Yiddish flavor kept: "schmuck"/"putz" → "đồ ngốc"/"thằng ngốc", "kvetching" → "càu nhàu", "schmutz" → "bẩn", "Feh" → "Hừ", "Oy" → "Này"/"Ôi", "tuchus" → "đít", "fakakta" → "chết tiệt", "bupkis" → "chẳng có cái gì cả", "kibbitzing" → "lắm mồm", "robo-schlomo" kept; "fuggin'" → "chết tiệt" (chunks 1811, 1812, 1813 — see quality notes); "jalopy" → "xe cà tàng"; "old fart" → "ông già xì hơi"; "go down on my wife" → "bú lồn vợ tôi" (crude kept); "shake icicles from our dicks" → "giũ băng khỏi cu" (image kept); the 911 call uses polite "tôi" (C0298_7CAA71D8); 1 slot kept: "'72" → "{number}" (C0298_98BF15D4).
- **Old lady (C0299, chunks 1814–1817):** polite "tôi/cậu" throughout per the rich-old-lady precedent (chunks 1733/1734), even the swearing lines; only direct-insult lines break to "tao/mày" (C0299_656612A6, C0299_8E78C0D0, C0299_D4503F28); "tripping balls" → "phê vãi cả ra"; "yeyo" kept loanword; "plug" → "mối" (dealer); "buzz"/"high" → "cơn phê"; "DMT" kept; "Sands of Time" kept name; "strip bunco" → "bunco cởi đồ"; "pool" → "hồ bơi" in swimming contexts; "soul mate" → "tri kỷ"; "skidaddle" → "chuồn"; "mary jane" kept loanword; "scissor" → "cọ xát" (female-female sex reading, C0299_E1113E7E); "three-way" → "cuộc ba người".
- **Female influencer / ghost guns (C0300, chunks 1817–1820):** "ghost gun" → "súng ma"; "3D printed gun" → "súng in 3D"; "resting bitch face" → "mặt đĩ đơ"; "buccal fat" → "mỡ má"; "work done" (cosmetic surgery) → "làm lại"; "implants" → "đồ độn"; "neg me" → "dìm hàng tao"; "get down" → "quẩy" in "how a real bitch gets down" (C0300_9CDBC572); "on God" → "thề với Chúa" (majority side); "what the fuck you're on" → "mày đang phê cái đéo gì" (per chunk 1804); "get jumped in" → "bị đánh nhập hội" (gang initiation); "ACAB" kept loanword; "Snapmatic" kept name; "dox" kept; "intrusive thought" → "suy nghĩ xâm nhập".
- **Snob / aristocratic rich (C0301, chunks 1820–1823):** polite "tôi/cậu" throughout per the rich/tourist precedent, even the swearing lines; "Beatrice" kept name (dog); "San Fierro" kept name; "VC" kept loanword; "queen" → "chị đại" (settled side, C0301_1E6FD4F1); "label whore" → "đồ mê đồ hiệu"; "breeder" → "đồ đẻ con"; "beard" → "bình phong"; "peach" → "quả đào ngon"; "plebian" → "đồ dân đen"; "non-fungible tokens" → "token không thể thay thế"; "six feet" kept in words (no slot in skeleton, per chunk 1736); "effective altruists" → "bọn tôi theo chủ nghĩa vị tha hiệu quả"; "bag of slop" → "bao cám lợn" (image kept); 1 slot kept: "911" → "{number}" (C0301_D782226A).
- **Spanglish / santera (C0302, chunks 1823–1825):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (26 items chunk 1823); Spanish kept (Oye, cojones, comunista, chancla, santero, Ay, Psst, mi gente); "saints" → "các vị thánh"; "hex" → "yểm bùa"; "curse" → "nguyền rủa"; "take a shot" → "nốc một ly" (drink side, C0302_366BBCA0); "cougar" → "máy bay bà già" (C0302_1D9D9D88, per chunks 1269/1272 — decision still pending); "bike" → "xe đạp" (majority side, C0302_3CF80844); source typos read as intended ("Lifes's tough" → "Đời khổ lắm.", "Unaccceptable!" → "Không thể chấp nhận được!", stray "T" kept in C0302_6106AF01).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts; crude sense "lồn" only where the sentence is clearly sexual (chunks 1787, 1824 C0302_3F681788); "pussy bitch" → "con đĩ lồn" (general insult).
- **"fuck with"** → "dây với" (mess-with side) remains the default in street dialogue; "thích" (like side) only where the sentence clearly means liking.
- **"I got this" / "I got you"** → "tao lo vụ này" / "tao lo cho mày" (reassure side) — settled.
- **"you got it"** → "mày thắng rồi" (concession side) — dominant.
- **"get down"** → "nằm xuống" (majority) vs "xuống khỏi đó" (high-place) vs "xuống đây" (come-here) vs "quẩy" (party) — still by context.
- **"I'm out" / "bounce" / "dip"** → "chuồn" — settled.
- **"trippin'"** → "phê" (default) vs don't-worry vs don't-care vs agitated — still by context.
- **"on God"** → "thề với Chúa" (majority side, chunks 1736, 1737, 1745, 1818, 1819).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.
- **Police register (stable):** calls to police use polite "tôi"; orders to suspects and threats use "tao/mày" or direct imperatives; street police calls spoken to bystanders (not 911 calls) use "tao" (chunk 1756 precedent, chunks 1807, 1817).

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side row in this period: chunk 1776 C0286_18E2458E "fuck yourself" → "tự địt mình đi" (wave 94). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802's 4 "eff" items rendered "đệt"; chunks 1811–1813 render "fuggin'" as "chết tiệt" (C0298_05910317, C0298_0C443103, C0298_0FD018DA, plus chunk 1812's "fuggin'" items). Both wait on the pending "Go fuck yourself!" decision; if it goes a different way, these items may need review.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823 C0302_1D9D9D88) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunks 1764, 1795 C0292_142C698A) — inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797 C0293_11779C0D) — minor inconsistency.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"take a shot"** — three-way: drink side (chunk 1824 C0302_366BBCA0) vs fight side (chunk 1792 C0291_09982375) vs shoot/try — still by context.
- **"get down"** — four ways now ("nằm xuống" / "xuống khỏi đó" / "xuống đây" / "quẩy") — still by context.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"911"** — `{number}` slot where the skeleton has one vs kept literal where it has none — follows the skeleton by design.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot (e.g. "six feet" kept in words, chunks 1736, 1820).
- **Source artifacts preserved as-is:** source typos read as intended (chunk 1824: "Lifes's", "Unaccceptable!", stray "T"); "attourney" (misspelling of "attorney") translated as "luật sư" (chunk 1783).

## Next

- Wave 99 (chunks 1826–1835, C0302→C0305) is translating now.
- Next milestone: **105,000** (wave 103).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
