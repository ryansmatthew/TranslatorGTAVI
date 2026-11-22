# Phase 3 — P3 Milestone Report: 110,000 Unique Strings

**Date:** 2026-11-21 (after wave 108 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **110,435 / 357,142 (30.9%)**; P3 remaining **246,707**
**DB rows (origin `pipeline_muse`, status `machine`):** 296,805 = distinct source_ids (no duplicates)
**Waves in this milestone period (104–108):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 104 | 1876–1885 | 106,435 | Spanglish/Cuban C0316 tail → C0317 → C0318 → C0319 head |
| 105 | 1886–1895 | 107,435 | Spanglish/Cuban C0319 → C0320 → C0321 → C0322 head |
| 106 | 1896–1905 | 108,435 | Spanglish/Cuban C0322 → C0323 → C0324, first heavy Haitian Creole packs (C0323) |
| 107 | 1906–1915 | 109,435 | Street/AAVE C0324 → C0325 → swamp/river C0326 → Gen-Z/valley-girl C0327 head |
| 108 | 1916–1925 | 110,435 | Valley-girl/rich-girl C0327 → rich/snob C0328 → paranoid C0329 → high-fashion snob C0330 → beach rich-girl C0331 head |

## Incidents (all resolved, none outstanding)

- **Wave 104:** no incidents. All 10 files passed the full structure check; spot-checks aligned. Chunk 1884 read "In Spines:" as a typo of "In Spanish:" (C0319_310E1548).
- **Wave 105, chunk 1886:** handoff arrived late (2026-11-21 ~20:20, after loading). The file had passed the full structure check on disk and was loaded per the established precedent; post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into the wave-105 MEMORY.md entry.
- **Wave 105, chunk 1891:** the agent's first file-write was corrupted at 1 item; the agent rewrote the whole file via script and re-verified 100/100 before finishing (its agent also had one failed exec during its own verification; final file verified independently).
- **Wave 106, chunk 1898:** agent had one failed exec during its own verification; final file verified independently. Chunk 1899's handoff arrived late (2026-11-21 ~20:22, after loading); post-load DB check verified 100/100 rows match the final file — no reload needed. Notes folded into the wave-106 MEMORY.md entry.
- **Wave 106, chunk 1905:** translated in two halves 50+50, merged by script, temp part deleted, final file independently re-verified 100/100.
- **Wave 107:** no incidents. All 10 handoffs arrived before loading. Chunks 1906 and 1915 were translated in two halves 50+50, merged by script, temp parts deleted, final files independently re-verified.
- **Wave 108:** no incidents. All 10 handoffs arrived before loading. Chunks 1918, 1922, 1924 and 1925 were translated in two halves 50+50, merged by script, temp parts deleted, final files independently re-verified.

## Conventions settled / reinforced in this period

- **Spanglish / Cuban (C0316–C0325, waves 104–107):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content, heaviest cue chunks so far (chunks 1896: 58, 1897: 61, 1899: 59); Spanish kept (Mala mia, La mía, la chancla, Oye, Oe, asere, mami, ¿Qué pasó?, comepinga, penco, permiso, Papo, chama, mija, compadre, Dale, si, BBL); "Pipo" kept name (C0322_E297A1D8); "GPS" kept; "totaled" → "bị đâm nát" (C0322_EA69219E); "shrimp legs" → "chân tôm" (C0322_ED836AC7); "papers" → "giấy tờ" (immigration sense, C0322_E0799980); "on one" → "phê thuốc" per "on the gas" (C0323_067F4CA1); "smoke" → "hút cỏ" (drug side, C0323_00757B00); "what you on" → "đang phê cái đéo gì" (per chunk 1804, chunks 1907, 1908, 1909, 1910); "crash" → "làm liều" (chunks 1907, 1910) vs "đập nhau" (fight side, chunk 1909); "hitting licks" → "đi cướp" (C0325_3E8E073E); "lick" → "vụ cướp" (chunk 1908); "bread" → "tiền"; "whip" → "xe"; "bean" kept drug loanword (chunks 1907, 1910); "oxy" kept (C0325_3AC311D2); "the woes" kept gang reading (chunks 1908, 1909, 1910) vs "mấy em" female reading (chunk 1907 C0325_1CAB28B4) — still by context; "the 4s" kept gang name (chunks 1908, 1909, 1910); "4s up" → "giơ 4 lên" (gang sign, C0325_192D955C); "on God" → "Thề với Chúa" (chunk 1908); "island time" → "giờ đảo" (C0325_4B2659E2); "family dem" → "gia đình tao" (C0325_4C044940); "do time" / "do a bid" → "ngồi tù" (chunks 1908, 1910); "punch the clock" → "đi làm đúng giờ" (C0325_4E8C014D); "politic" → "tán gẫu" (C0325_4E963C3A); "pop yo shit" → "khoác lác" (C0325_4EAE5B86); "it's up" → "tới lượt/tới số" (fight side, chunks 1908, 1910); "a buck fifty" → "150 pao" (weight, C0325_D05BCE81); "Stand on that shit." → "Cứ giữ vững lời mày đi." (C0325_F81C6F94).
- **Haitian Creole (C0323, wave 106):** "In Creole:" → "Nói tiếng Creole:" + translated content, per the "In Spanish:" precedent (chunks 1900: 12, 1901: 20, 1902: 17, 1903: 10, 1899: 5); "Imbesil!" → "Đồ đần!" (C0323_3B500827); "skress" → "stress" (Creole reading, C0324_0D18BA9D, guess).
- **"fuck with"** → mess-with "dây với" remains the default; like side in clear flirting ("I fuck wit' ya" → "Tao thích mày đấy", C0325_68986C30); joking side ("fuckin' with you" → "đùa mày thôi", C0329_A270C630); sexual side ("fuck with" → "địt bằng", C0323_36BA121E); hang-out / like-side readings in chunks 1834, 1832, 1839, 1873 — still by context.
- **"I got you" / "I got it" / "I got this" / "gotcha"** — reassure ("tao lo cho mày" / "tao lo vụ này") vs understand ("tao hiểu rồi") vs caught ("tao tóm được mày rồi") — still by context. "you got it" → concession ("mày thắng rồi", dominant in this period, chunks 1904, 1905, 1907, 1910) vs attention ("mày có rồi đấy", C0326_0FB48266, per chunk 1882) vs agreement.
- **"pop it off"** — split across waves 105–106: shoot side (chunks 1889, 1892), start-it ambiguous (chunk 1888), fight side (chunk 1891) — still by context.
- **Swamp / river Florida (C0326, wave 107):** "Gator bait" → "Mồi cá sấu" (C0326_1440BF4A); "gator" → "cá sấu" (C0326_840D3771); "wild hog" → "lợn rừng" (C0326_87C11C65); "dock" → "đậu thuyền" (per chunk 1881, C0326_14EF5E0C); "ride" → "xe"; "taillights" → "đèn hậu" (C0326_269585E4); "call shotgun" → "xí ghế phụ" (C0326_47B92220); "dip" → "đi bơi" (swim sense in river context, C0326_405281AB — NOT the "chuồn" side); "creampuff" → "đồ bánh kem" literal (C0326_5D5099E0) vs "thằng bánh bèo" weak-person sense (C0326_E4285D91) — still by context; "crocodile leather sheets" → "ga giường da cá sấu" (C0326_6FCBF7A4); "dog down" → "chó gục rồi" (C0326_55CDFD5E, K9-person alternative noted).
- **Valley-girl / rich-girl (C0327, waves 107–108):** "ghosting" kept; "Pester" kept app name (per "Ranter", chunks 1915, 1916); "vibe" kept; "situationship" kept; "threeway" kept; "negging" kept; "pick-me girl" kept; "followers" kept; "amigo" / "m'kay" kept; "fiancé" → "vị hôn phu"; "sisterhood" → "tình chị em"; "sick fuck" → "thằng biến thái bệnh hoạn"; "Poetic justice" → "Quả báo xứng đáng"; "chivalry" → "hiệp sĩ"; "fuckboy" / "incel" / "loser" / "manifest" kept loanwords; "high value man" → "người đàn ông giá trị cao" (C0327_77C360E2) / "high value woman" → "phụ nữ giá trị cao" (chunk 1917); "hookup pottery class" → "lớp gốm kiếm tình một đêm" (C0327_279A23D0); "I'm a catch" → "tao là hàng ngon" (C0327_290362E8); "appear available" → "trông như mình đang độc thân" (C0327_3382A599); "ratchet" → "rẻ rách" (C0327_3B9F458F); "chemically castrated" → "thiến hóa học" (C0327_442BBFA0); "out of my purview" → "không phải chuyện của tao" (C0327_4CE7D511); "sick ride. Not!" → "xe xịn đấy. Đùa thôi!" (C0327_6EA55293); "pinging the cops" → "báo cảnh sát" (C0327_772F7655); "logging the fuck off" → "đăng xuất mẹ luôn" (C0327_78B397CF); "swipe left" → "quẹt trái" (C0327_7BEBFFEA); "tentacle porn addiction" → "chứng nghiện phim khiêu dâm xúc tu" (C0327_7E24F091); "skid mark" → "Vết ố" (stain side, C0327_6CFDA296, vs "Vệt phanh" brake reading — unresolved); police-call lines kept neutral, no pronoun (C0327_623AAD21, C0327_AADBCA21, per chunk 1915).
- **Rich / snob NPC (C0328, wave 108):** register split per chunks 1341/1343 — insults/confrontations "tao/mày", polite/calm lines "tôi/anh" (C0328_5BA4C9C7, C0328_95DFC2D9 police call, C0328_9EDBF87E, C0328_AC9CC98A, C0328_ADE1582B; chunk 1917 C0328_43A49D30, C0328_29ECB21B); "clubs" → "gậy golf" (C0328_53ADC8EB); "laser lipolysis" → "hút mỡ bằng laser" (C0328_899BED06); "Rockford Hills" kept; "Med-Spa" kept; "gated community" → "khu dân cư có cổng bảo vệ" (C0328_BA99842E); "loser" → "thằng thua cuộc" (C0328_97C20464, C0328_C3656357); "talking shit" → "nói láo" (C0328_B83E1581); "stress lines" → "nếp nhăn vì stress" (C0328_D4BFE0DF); "tax bracket" → "đẳng cấp thuế" (C0328_D59CB565); "Doggy Med-Spa" kept (C0328_D8BAB6AF); "middle class" → "tầm thường" (snob reading, C0328_179C42BD); "cat fight" → "trận cào cấu" (C0327_EC72A873); "Work, girl." → "Quẩy đi, cô em." (C0327_FC7AE85F); "dating pool" → "bể hẹn hò" (C0327_FF1000F1); "lady-balls" → "cái gan đàn bà" (C0327_E25C3383).
- **Paranoid / repetitive NPC (C0329, wave 108):** teeth-obsession thread kept ("teeth" → "răng", C0329_2EE2C625, C0329_39D44C7E, C0329_5C89DCEF); "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (chunks 1920: 2, 1921: 4); Spanish kept (papi, mami, ¡Cállate!, idiota, ¡Ayyy mira!, Al Carajo, gracias, En serio, Coño, Problemas, Comemierda); "cops" → "cớm" (C0329_552BF909, C0329_7C3B14E9); "Lick my shit!" → "Liếm cứt tao đi!"; "Screw you!" → "Địt mẹ mày!"; "get to me" → "chọc tức tao" (C0329_711660F9); "eat glass" → "ăn thủy tinh" literal image (C0329_711660F9); "fish person" → "con người cá" (C0329_737FF34B); "Suck it up!" → "Chịu đựng đi!" (endure side, C0329_72A70BAE); "piece of ass" → "em ngon" (C0329_2F7DA312); "pancake" → "đè bẹp" (C0329_9C2B5366, Rodrigo's legs — two linked lines, C0329_9C2B5366 + C0329_D2254A98); "snapping" → "sắp nổ tung" (mental-breakdown sense, C0329_B5E2B37A); "body" → "thân hình" (living-body flirting sense, C0329_1686A9E5, vs corpse "cái xác" per chunk 1838 — still by context); "balls" → "gan" (C0329_04FA0F6E); "Pop a wheelie!" → "Bốc đầu xe đi!" (C0329_E5340540); police-call C0329_9B0768C2 polite "tôi/bọn tôi" per precedent.
- **High-fashion snob (C0330, wave 108):** "queen" → "chị đại" (settled side, C0329_F71D60C6) vs "nữ hoàng" literal in "women are treated like queens" (C0330_26DC97D1) — still by context; "I'm calling it" → "Tao quyết định rồi" (end-it, C0330_1474CDED); "Couture Criminali" kept brand; "Sessanta Nove" kept collection; "Leonidans" → "dân Leonida" (C0330_35988410); "Liberty City" kept; "Edith" kept (her dog); "Holland" → "Hà Lan" (C0330_06ABCC1B); "fish out of water" → "cá mắc cạn" (C0330_0D6451DA); "salt in the gash" → "muối xát vào vết thương" (C0330_2A000D42); "dime a dozen" → "đầy rẫy ra đấy" (C0330_450990C2); "fierce" → "dữ dằn" (C0330_19545768); "indubitably" → "không còn nghi ngờ gì nữa" (C0330_19E0DC0A); "allyship" → "sự ủng hộ của đồng minh" (C0330_3CA85331); "hall monitor" → "sao đỏ" (per chunk 109, C0330_723333E2); "peanut gallery" → "đám khán giả rẻ tiền" (C0330_50F8929D); "sangfroid" → "sự điềm tĩnh" (C0330_648D7F22); "out to lunch" → "mất trí" (C0330_5FACC67A); "Au Natural Perfume" kept product (C0330_70A9B27D); "Cimicino" kept (C0330_9F153054); "drag queens" / "twinks" / "followers" kept loanwords; "get read to filth" → "bị chửi tơi bời" (C0330_90A2612F); "bon mot" → "câu châm biếm chết người" (C0330_83CB0043); "phallic psychosis" → "loạn thần dương vật" (C0330_B80A4817); "homoerotic jockeying" → "tranh giành đầy mùi đồng tính" (C0330_ADDCA1A6); "wear the pants" → "người nắm quyền" (C0330_DD3FC98B); "vasectomy" → "thắt ống dẫn tinh" (C0330_ECC1A3F3); "smooth operator" → "tay chơi lão luyện" (C0330_ED5A1571); "Pussycat" kept as magazine name (C0330_3E6829D5, vs P0 "mèo con" rule — flagged for review); "past time" read as "pastime" typo (C0330_F62859B6); register: chunk 1923 "tao/mày" per chunk 1915, chunk 1924 "tôi/cậu" for the snob voice with only outburst lines in "tao/mày" — still by voice, not settled; police-call C0330_849E4F84 kept neutral, no pronoun; slot: "1997" → "năm {number}" (C0330_C7915EF5).
- **Beach rich-girl (C0331 head, chunk 1925):** "Black don't crack" → "Da đen có nhăn bao giờ đâu" (proverb, C0330_FD0C8C6A); "This look is giving 'leper colony'" → "Cái vẻ này đúng kiểu 'trại phong' luôn" (per "It's giving" chunk 1323, C0330_FD5BBBDF); "VAIN" kept (C0330_FFF5758C); "Snapmatic" kept (C0331_28C507F5); "literally" kept Gen-Z loanword (C0331_40627B1D, C0331_4B7778A2); "clout chasers" → "hám fame" (per chunk 1332, C0331_414D6E6D); "my b" → "lỗi của tao" (per chunk 1316, C0331_47711DD8); "get fucked" → "bị địt" (passive side, per chunks 1782/1845, C0331_3254752C); "crashin' out" → "làm liều" (per chunk 1907, C0331_2BDC43CF); "creep" → "biến thái" (C0331_23A500BF); "fuckin' up" → "đánh nhừ tử" (attack side, NOT sexual, C0331_28C507F5 lion/zebra); "this little shit" → "cái chỗ cứt nhỏ này" (place reading, C0331_3A8E20C7).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 1899, 1900, 1902, 1913, 1921); crude sense "lồn" only where the sentence is clearly sexual (chunks 1888, 1890, 1891, 1905, 1925); "pussy" → "lồn" explicit in chunk 1905 C0324_8521BC9B; "pussies" → "lũ lồn" explicit (chunk 1880) vs "lũ hèn" (chunk 1893) — by context.
- **"daddy"** → "bố" (majority side, chunks 1899, 1900) vs kept loanword as flirtatious address (chunks 1489, 1509, 1781, 1786, 1788, 1834, 1853, 1858, 1881) vs "Bố" when spoken to a dog (chunk 1800) — still by context.
- **"get down"** → now six ways: "nằm xuống" (majority) vs "xuống khỏi đó" (high-place, chunk 1919 C0328_F0B3B5AE) vs "xuống đây" (come-here) vs "quẩy" (party) vs "đánh nhau" (fight, chunk 1849) vs "cúi xuống" (chunk 1867) — still by context.
- **"get fucked"** → "bị địt" (passive side, chunks 1782, 1788, 1798, 1845, 1851, 1865, 1883, 1925) vs active readings elsewhere — still by context.
- **"on the gas"** → drug side in chunks 1881 ("phê thuốc", C0318_4A9D17B3) and 1882 ("phê cỏ", C0318_9151B18A) — driving alternative noted in both.
- **"make moves" / "make a move" / "run it"** — "ra tay" (chunks 1781, 1850, 1874, 1906) vs "kiếm chác" / "tiếp tục làm việc" / "chơi tới bến" (chunks 1827, 1896, 1897, 1898) — still inconsistent.
- **"alpha"** → "kèo trên" (chunk 1896 C0322_46201CEF) vs "đầu đàn" (chunk 1898 C0322_BE99548C) — still split.
- **Slots kept correctly this period:** "in '95" → "năm {number}" (chunks 1884, 1886); "100 percent." → "{number} phần trăm." (C0323_848F0B93); "On the way, 4." → "Đang tới, {number}." (C0323_764A89AE); "My 4..." → "Của tao {number}..." (C0323_29C358F4, truncated source); "1997" → "năm {number}" (C0330_C7915EF5); numbers kept as words where the skeleton has no slot ("21st century", chunk 1897).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 1846 C0308_27950089 and C0308_3B1B62D1 (recorded in the 105,000 report), chunk 1888 C0320_2C39F2D7 "you fuck yourself" → "mày tự đụ đi" (crude side per chunk 1846). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"lowkey"** — many-way split (kept / "thật ra" / "kín đáo" / "ngầm" / "hơi") — still inconsistent.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address vs "Bố" when spoken to a dog — still by context.
- **"you got it"** — concession ("mày thắng rồi") vs reassure vs agreement vs understand vs attention — still by context.
- **"I got you" / "I got it" / "gotcha"** — reassure vs understand vs caught — still by context.
- **"trippin'"** — many-way split ("phê" default / "nổi điên" / alarm / bother / don't-worry / don't-care / panicking / agitated "làm quá lên") — still by context.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent.
- **"bike"** — "xe đạp" (majority) vs "mô-tô" / "xe máy" (minority) — still inconsistent.
- **"body"** — corpse ("cái xác", per chunk 1838) vs living person ("thân hình", chunk 1919) — by context.
- **"bail"** — "bảo lãnh" vs "chuồn" vs "cứu ra khỏi vụ này" — still inconsistent.
- **"good looks"** — thanks vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" (river context, chunk 1911) — by context.
- **"FYI"** — kept vs translated — still inconsistent.
- **"Madone!"** — kept — still undecided.
- **"mistress"** — "cô chủ" — still undecided.
- **"That's Negative."** — "phủ định" (majority) vs "Không phải." — still inconsistent.
- **"DOA"** — kept vs translated — still undecided.
- **"PIT"** — kept (waves 53–85) — still undecided.
- **"call it"** — many-way split (end-it side dominant) — still by context.
- **"officer down" / "casualty"** — dead-vs-hurt ambiguity ("cảnh sát gục rồi" deliberately covers both).
- **"get laid"** — crude vs soft — unresolved.
- **"US Army"** — "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" — still inconsistent.
- **"ma'am"** — "thưa bà" vs "thưa cô" vs "cô ạ" — still inconsistent.
- **"move out"** — "rút lui" vs "di chuyển thôi" — still inconsistent.
- **"shocker"** — device vs name — still undecided.
- **"stun gun"** — "súng chích điện" (majority) vs "súng điện" — still inconsistent.
- **"jerkoff"** — "thằng thủ dâm" vs "thằng quay tay" — still inconsistent.
- **"bless your heart"** — sarcastic renderings vary.
- **"lib" / "libs" / "libtard"** — renderings vary.
- **"deep state"** — "nhà nước ngầm" (majority) vs "chính phủ ngầm" — still inconsistent.
- **"Fire"** — blaze vs gunfire — still by context.
- **"M7"** — unknown (kept).
- **"take a shot"** — three-way (shoot / drink / try / fight) — still by context.
- **"Skid mark"** — "Vệt phanh" vs "vết ố" — still split.
- **"Clown Town"** — translated vs place name — still inconsistent.
- **"Evil Eye"** — "Mắt Quỷ" vs loanword — still inconsistent.
- **"white trash" vs "trailer trash"** — handling split.
- **"vibe"** — kept vs translated — still by context.
- **"bag(s)"** — money vs drug sense — still by context.
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — kept vs "thao túng" (chunk 1896 per chunk 1244) — still by context.
- **"Tsou"** — kept as-is (chunks 1717, 1718) — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent (see conventions).
- **"bump"** — drug sense vs collision sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent.
- **"pheromones"** — kept loanword (chunk 1848) vs "pheromone" (chunk 1851) — minor inconsistency.
- **"smoke" (conflict)** — "gây sự" (chunks 1851, 1863, 1901) vs drug side "hút thuốc" (chunk 1873) — by context.
- **"go left"** — "toang" (chunk 1862) vs "rẽ sang hướng xấu" (chunk 1863) — still split.
- **"joint"** — a woman (chunks 1863, 1872) vs other readings — by context.
- **"on the gas"** — drug side in chunks 1881 and 1882 — driving alternative noted in both.
- **"pop it off"** — split: shoot side (chunks 1889, 1892), start-it ambiguous (chunk 1888), fight side (chunk 1891) — still by context.
- **"alpha"** — "kèo trên" (chunk 1896) vs "đầu đàn" (chunk 1898) — still split.
- **"Pussycat"** — kept as magazine name (chunk 1922 C0330_3E6829D5) vs "mèo con" per the P0 rule — flagged for review.
- **"the woes"** — gang reading (chunks 1908, 1909, 1910) vs female reading (chunk 1907) — by context.
- **"creampuff"** — literal "đồ bánh kem" (chunk 1912) vs weak-person "thằng bánh bèo" (chunk 1914) — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines (chunks 1791, 1796, 1798, 1799) vs as a person elsewhere — by context.
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunks 1764, 1795) — still inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797) — minor inconsistency.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("In Spines:" read as "In Spanish:", chunk 1884; "past time" read as "pastime", chunk 1924; "keeping it tall" read as "keeping it real" variant, chunk 1908).

## Next

- Wave 109 (chunks 1926–1935, C0331→) is translating now.
- Next milestone: **115,000** (wave 113).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
