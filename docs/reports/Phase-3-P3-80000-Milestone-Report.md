# Phase 3 — P3 Milestone Report: 80,000 Unique Strings

**Date:** 2026-11-21 (after wave 78 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **80,435 / 357,142 (22.5%)**; P3 remaining **276,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 262,137 = distinct source_ids (no duplicates)
**Waves in this milestone period (74–78):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 74 | 1576–1585 | 76,435 | Rich/Spanglish female C0215–C0216 → conspiracy/paranoid C0217 → rich snobby C0218 |
| 75 | 1586–1595 | 77,435 | Rich kid C0218 → AAVE female "Big Mama"/OG C0219 → valley girl/Gen Z C0220 → street/redneck C0221 → older Southern religious lady C0222 |
| 76 | 1596–1605 | 78,435 | Older Southern religious lady C0222 → civilian/tourist C0223 → street C0224 → "tough grandma" C0225 |
| 77 | 1606–1615 | 79,435 | "Momma" C0225 tail → gym-bro/street C0226 → street/AAVE C0227 → Chicano/Spanglish C0227–C0228 → street C0228 → club/bouncer C0229 |
| 78 | 1616–1625 | 80,435 | Club/bouncer C0229 → Gen Z/valley girl C0230 → bouncer/street C0231 |

## Incidents (all resolved, none outstanding)

- **Wave 76, chunk 1604:** 1 adjacent duplicate — legitimate ("Come on! Your ass is grass!" / "C'mon! Your ass is grass!" → same vi "Nào! Đít mày sắp thành cỏ rồi đấy!", idx 35/36, verified on disk before loading).
- **Waves 74–78 (all other chunks):** no incidents. All files passed structure check (100 items, ids in order, keys {id, vi}, 0 adjacent dups) plus spot-checks. All 50 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **Older Southern religious lady voice (C0222, chunks 1595–1597):** polite "tôi/anh" throughout ("sweetheart"/"darling"/"honey"/"sugar pie" → "cưng", "God bless you" → "Chúa phù hộ bạn", "my pastor" → "mục sư của tôi", "Leave room for Jesus" → "Chừa chỗ cho Chúa đi"); soft old-lady swearing ("damn" → "chết tiệt", "hells bells" → "trời đất ơi", "heck" → "trời ơi", "gosh-darn" → "chết tiệt", "booty"/"caboose" → "mông", "crapper" → "bồn cầu"); Southern idioms kept as images ("all hat and no cattle" → "chỉ được cái đội mũ cao bồi mà chẳng có bò", "Kiss my grits!" → "Hôn mông tao đi!", "skedaddle" → "chuồn", "Good Samaritan" → "người Samari tốt bụng", "Southern Hospitality" → "lòng hiếu khách miền Nam", "bee in your bonnet" → "cái gì đó ám ảnh", "bones to pick" → "hiềm khích").
- **Conspiracy/paranoid voice (C0217, chunks 1579–1583):** "liberal"/"libs" → "cánh tả"/"bọn cánh tả" (settled precedent); "deep state" → "nhà nước ngầm" (majority, incl. chunks 1579, 1582, 1583) vs "chính phủ ngầm" (chunk 1581) — still inconsistent; "shadow government" → "chính phủ bóng tối"; "reptilian"/"reptiloid" → "người bò sát"/"bọn bò sát"; "Hollow Earth" → "Trái Đất Rỗng" (per P0); "false flag" → "cờ giả"; "crisis actors" → "diễn viên khủng hoảng"; "mainstream media" → "truyền thông dòng chính"; "second amendment" → "Tu chính án số 2"; "flat earth" → "Trái Đất phẳng"; "libtard" kept (per chunk 1475).
- **Rich kid / rich snobby voice (C0218, chunks 1584–1586):** "my father's lawyers" → "luật sư của bố tao"; "my father's car" → "xe của bố tao"; "Deals & Dollars" kept store name; register split: polite/formal rich lines use "tôi/bạn", confrontation/insult/bragging lines use "tao/mày".
- **AAVE "Big Mama"/OG female voice (C0219, chunks 1586–1589):** "chile" kept loanword; "honey"/"baby" → "cưng"; "Big Mama" kept name; "OG" kept; "y'all" kept loanword; "Deuces" → "Tạm biệt"; "wolf tickets" → "mấy lời hù dọa suông"; "don't write a check ya ass can't cash" → "đừng có viết tấm séc mà cái đít mày không trả nổi"; "Shamone!" kept; "SuperCoochie" kept; "fifty dollars" kept as words "năm mươi đô" (no skeleton slot); "fifty eleven times" → "năm mươi mười một lần" keeping the exaggeration; "take me out my character" → "làm tao mất chất"; "anointed" → "được Chúa xức dầu"; "I'm not the one" → "tao không phải đứa để mày đùa đâu"; "activated" → "đang sung".
- **Valley girl / Gen Z voice (C0220, chunks 1589–1591):** "ma'am" → "thưa bà"; "Cross my heart" → "Thề đấy"; "slaps" → "mấy bài nhạc đỉnh vãi" (music sense); "Be so fucking for real" → "Làm ơn nghiêm túc dùm cái đi chết tiệt"; "mixed signals" → "tín hiệu lẫn lộn"; "get in my head" → "chui vào đầu tao"; "Its giving batshit" → "Nó đúng kiểu điên khùng luôn."; "serial killer vibes" → "vibe sát nhân hàng loạt"; "You got this!" → "Mày làm được mà!"; "randos" → "người lạ"; "star-fuckers" → "đồ đu bám người nổi tiếng"; "toxic" kept loanword; "bestie"/"Yass!"/"Ee!"/"Woo!" kept; "King shit" → "Đỉnh vãi".
- **"tough grandma" / "Momma" voice (C0225, chunks 1603–1606):** "Momma" → "Má" ("Momma came to play!" → "Má tới chơi đây!"); "tan that hide" → "lột da"; "speed bump" → "gờ giảm tốc" ("You're gonna be a goddamn speed bump!" → "Mày sẽ thành cái gờ giảm tốc chết tiệt đấy!"); "paint the walls with you" → "sơn tường bằng mày" keeping the image; "your ass is grass" → "đít mày sắp thành cỏ" (per chunk 1589).
- **Club/bouncer voice (C0229–C0231, chunks 1615–1625):** "Class D security guard" → "bảo vệ hạng D"; "guard card" → "thẻ bảo vệ"; "VIP" kept; "pat down" → "khám người"; "rap sheet a mile long" → "tiền án dài cả dặm"; "dispatch" → "trung tâm điều phối"; "unit" → "đơn vị"; "bottle service" → "phục vụ chai"; "bouncer" → "bảo vệ"/"anh bảo vệ"; "what's the tea?" → "có chuyện gì hot?"; "hangry" → "đói cọc"; "bailing you out" → "cứu mày ra khỏi vụ này" (bail-out/rescue side); "Mr. Duval" kept name.
- **Gym-bro voice (C0226, chunks 1606–1608):** "jacked" → "đô con"; "natty" → "tập tự nhiên" (no-steroid sense); "bench press" → "đẩy tạ"; "pythons" → "cơ bắp" (arm muscles); "streaming" → "livestream"; "I have lawyers!" → "Tao có luật sư!" (rich-kid voice).
- **Spanglish / Chicano street (C0227–C0228, chunks 1609–1612):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (×2 chunk 1609, ×11 chunk 1610, ×8 chunk 1611, ×12 chunk 1612, including mid-sentence cues); Spanish kept: vámonos, puto, mija, Qué onda, Oye, veterano, barrio, Guerrero, huevos, Vete ya, Orale, perra, culero, chotas, pendeja, lulu, en la cárcel; "LS" kept ("LS style" → "kiểu LS", "East LS" → "Đông LS"); "Mexica Gods" → "các vị thần Mexica"; "do life" → "ngồi tù chung thân"; "shank" → "đâm"; "get smoked" → "bị bắn hạ"; "good looking out" → "cảm ơn mày đã để ý" (per chunk 1569).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule is now the clear default in street contexts (chunks 1600, 1601, 1602, 1604, 1605, 1609, 1610, 1611, 1613, 1614, 1615, 1617, multiple rows each, including "pussy move" → "nước đi của đồ hèn", "pussy out" → "nhát", "chicken shit pussy" → "đồ hèn cứt gà", "bitch move" → "trò hèn"); crude sense "lồn" only where the sentence is clearly sexual (chunk 1587 "long as you got a pussy, you always sitting on fifty dollars"; chunk 1589 "big, ol' clit staring me right in my face").
- **"fuck with"** → "dây với" (mess-with side) is now the default in street dialogue (chunks 1600, 1603, 1604, 1606, 1608, 1610, 1611, 1612, 1617, 1618, 1622, 1623, 1625); "thích" (like side) only where the sentence clearly means liking.
- **"go fuck yourself"** → crude "Đi mà tự đụ đi" side reinforced again (chunk 1600 C0224_2FFB6689; chunk 1607 "Get fucked, dude!" → "Đi mà tự đụ đi, dude!") — the pending decision with the user is still unanswered.
- **"piece" / "piece of hardware" → "khẩu súng"** reinforced (chunk 1603 "Nice piece of hardware you got there!" → "Khẩu súng ngon đấy mày có kìa!"; chunk 1610 "You and that piece on that Leonida shit, bro..."); **"carryin'" → "mang súng"** reinforced (chunks 1603, 1625); **"strapped" → "mang súng"** (chunk 1618); **"nine" → "khẩu 9 ly"** (chunk 1588).
- **"take a shot"** → "bắn đi" (shoot side, chunk 1602) — vs try side (chunk 1504) and drink side — still by context.
- **"get down"** → "nằm xuống" (majority side, chunks 1603, 1609, 1616, 1617, 1619, 1624, 1625) vs "xuống đi" (high-place side, chunks 1602, 1608, 1613) — still by context, split within single chunks (1613).
- **"you got me"** — caught side reinforced ("mày tóm được tao rồi đấy", chunks 1613, 1617, 1619, 1625) vs reassure side ("Tao lo cho mày", chunks 1602, 1621) vs "nghe rõ chưa?" (understood side, chunk 1618 "you gonna quit it, you got me?") — still by context.
- **"I got this"** → "tao lo vụ này" (reassure side, chunks 1601, 1602, 1608, 1614, 1624) — now settled.
- **"I got yo' ass"** → "Tao tóm được mày rồi đấy" (caught side, chunk 1619) vs reassure side elsewhere — still by context.
- **"queen"** → "chị đại" (chunk 1614 "I'm the queen, me!" → "Tao là chị đại, chính tao đây!") vs "nữ hoàng" in the sarcastic "La di loo here come the fuckin' queen majesty..." (chunk 1613) — still inconsistent.
- **"lowkey"** — kept loanword (chunks 1591, 1609) vs "thật ra" (chunk 1590) vs "kín đáo" (chunk 1609 "I need to stay lowkey" → "tao cần phải kín đáo thôi") vs "ngầm"/"hơi" (earlier chunks) — still inconsistent.
- **"trippin'"** → "phê" (default side, chunks 1599, 1609) vs bother side (chunk 1612 "Stop tripping on me, man!" → "Đừng có làm phiền tao nữa, man!") — still by context.
- **"Kitty Litter"** — drug-name reading again (chunk 1600 "I ain't even had my Kitty Litter today!" → "tao còn chưa phê Kitty Litter hôm nay nữa!") vs literal cat-litter reading (earlier chunks) — still inconsistent.
- **"bitch"/"ho"/"motherfucker" read as car/weapon** — plausible by context but a real ambiguity class ("ho" read as car, chunk 1569; "motherfucker" read as weapon, chunk 1569).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.
- **Police register (stable):** calls to police use polite "tôi" (chunks 1584, 1586, 1588, 1597, 1602, 1612, 1613, 1617, 1621, 1624, 1625); radio/reports use professional "tôi"; orders to suspects use "tao/mày" or direct imperatives.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1600 C0224_2FFB6689, chunk 1607 C0226_1DF4B464. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"VC"** — kept loanword (chunks 1610, 1612) vs "Vice City" — still inconsistent.
- **"the Y" / "Y Hotel"** — "khách sạn Y" (chunk 1577) vs kept as name (chunks 830, 838) — still unresolved.
- **"pigs"** — "cớm" (chunks 1571, 1573) vs "lũ lợn" (chunk 1572) — still inconsistent.
- **"deep state"** — "nhà nước ngầm" (majority) vs "chính phủ ngầm" (chunk 1581) — still inconsistent.
- **"queen"** — "chị đại" (chunks 1569, 1575, 1614) vs "nữ hoàng" (chunk 1613) — still inconsistent.
- **"lowkey"** — kept loanword vs "thật ra" vs "kín đáo" vs "ngầm" vs "hơi" — still inconsistent.
- **"nictitating membrane(s)"** — kept loanword (chunk 1580) vs "màng mắt thứ ba" (chunk 1583) — still inconsistent.
- **"911"** — kept literal as a number where the skeleton has no slot (chunk 1609 "Like it's not even 911it's better than that.") vs `{number}` slot where the skeleton has one (chunks 1586, 1590, 1613, 1620) — follows the skeleton by design.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot (e.g. "fifty dollars" → "năm mươi đô", chunk 1587; "five"/"nines" kept as words, chunk 1622).
- **Source artifacts preserved as-is:** chunk 1596 "is that was passes for a swimsuit in Leonida?" (source typo "is that was"); chunk 1599 "an shitty AI" / "make then more loserish" (source typos); chunk 1621 "Its a liabibility!" (source typo); chunk 1618 "ain't won't be doin' all that talkin'" (source grammar error); chunk 1612 "Hub?" (unresolved token, kept); chunk 1615 "You ain't tailin us we're tailin you fuckin skin you what" (garbled source string, translated literally).

## Next

- Wave 79 (chunks 1626–1635, C0231→C0234) is translating now.
- Next milestone: **85,000** (wave 83).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
