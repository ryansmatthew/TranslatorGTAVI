# Phase 3 — P3 Milestone Report: 120,000 Unique Strings

**Date:** 2026-11-21 (after wave 118 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **120,435 / 357,142 (33.7%)**; P3 remaining **236,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 120,435 = **206,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 308,325 = distinct source_ids (no duplicates)
**Waves in this milestone period (114–118):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 114 | 1976–1985 | 116,435 | Civilian/shop C0345 → Spanglish/Cuban C0346 → street/AAVE C0347 → C0348 head |
| 115 | 1986–1995 | 117,435 | Street/AAVE C0348 → valley-girl C0349 → civilian NPC C0350 → Spanglish/Cuban C0351 head |
| 116 | 1996–2005 | 118,435 | Gang/Spanglish C0351 → female street/AAVE C0352 → street/AAVE + prison C0353 |
| 117 | 2006–2015 | 119,435 | Street/AAVE + prison C0353 → Haitian Creole C0354 → swamp/rural C0355 → veteran C0356 |
| 118 | 2016–2025 | 120,435 | Veteran/older C0356 → civilian NPC C0357 → street/AAVE C0358 → older/rural + dog C0359 → Southern C0360 head |

## Incidents (all resolved, none outstanding)

- **Wave 114:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 115, chunk 1991:** handoff had not arrived at load time — the file passed the full structure check on disk and was loaded per the established precedent; its handoff arrived late (2026-11-21 ~20:45), the post-load DB check verified **100/100 rows match the final file** (no reload needed), and its notes were folded into the wave record.
- **Wave 116:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 117, chunk 2009:** the agent's handoff mislabeled the cue type as "In Spanish:" and claimed 16 cues, but a disk check before loading verified exactly **15 cue rows, all "In Creole:" in the input and all correctly rendered "Nói tiếng Creole:" in the output** — the data was correct, only the agent's report text was wrong. No reload needed. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 118:** no incidents. All 10 files passed the full structure check; spot-checks aligned. All 10 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **Haitian Creole (C0354, wave 117):** "In Creole:" → "Nói tiếng Creole:" + translated content (chunk 2006: 9, 2007: 13, 2008: 10, 2009: 15); "woes" kept gang side per chunks 1908–1910 (C0354_7486492C); "grid" → "vào cuộc" per chunks 1935–1938 (C0354_80E7F1B0, C0354_B8E35D8A); "tweaker" → "thằng ngáo" (C0354_78E7B632); "zooted" → "phê" (C0354_89E9F783, C0354_95ACF004); "fiends" → "lũ nghiện" (C0354_8107AA66); "smoke that bitch" → "bắn chết con đĩ đó" shoot side (C0354_8C810E31); "pack" → "gói hàng" drug package (C0354_B914F4D6) vs corpse "cái xác" (C0354_3D6028FF) — by context; "skrait" → "ổn" (C0354_BB00F1A1, C0354_BE6FB618); "square" → "thằng đần" per chunk 1984 (C0354_C336D529); "side piece" → "bồ nhí" (C0354_A5F4F52C); "Conch King" kept place name (C0354_38689362, C0354_8EEB8FDA); "fuck on" → "cút đi" (chunks 1931, 1933, 1934) vs sexual side when context is explicit (C0354_A5F4F52C "I gotta go fuck on my side piece." → "Tao phải đi địt con bồ nhí của tao đây."); "free lick" renderings vary ("vụ cướp dễ ăn" chunk 2006 / "món hời dễ ăn" chunk 2007 / "vụ ăn cắp miễn phí" chunk 2008); "hit a lick" → "cướp được (một) vụ" consistent (chunks 2006, 2007); "slide" → "chuồn" (C0354_3F25E2FD, C0354_62C01106, C0354_70D4753E); "it's up" → "tới luôn" fight side per chunks 1908/1910 (C0354_6087DF6E); "be down" → "nhập hội" (C0354_671D4A99); "link" → "gặp" (C0354_5EBAAA98); "No flaggin'." → "Không nói điêu đâu." (C0354_69E58197); "green ass" → "non xanh" inexperienced (C0354_39FBBA4D); "brother them" → "anh em của tao" (C0354_3F67BF8A); "You're cooking now." → "Giờ mày đang đỉnh đấy." active peak side per chunk 1972 (C0354_7E69E105); "it's been up" → "muốn đánh nhau" conflict per chunks 1908/1910 (C0354_8ADB3FCB); "claim a set" → "nhận băng nào" (C0354_92E684DC); "Ole boy" → "thằng đó" (C0354_B8E35D8A); "we skrait" → "Bọn tao ổn rồi." (C0354_DE7CB288); "conch" → "ốc biển" (C0354_DC36D71A); "Derrick" kept (C0354_FBA4FE42); "nat" / "nat nat" kept, meaning unknown (C0354_EF37500F); "Get in that wind." → "Chuồn đi." (C0354_F956D349); "off the porch" → "bước ra ngoài đời" (C0354_EECACE83).
- **"The Beast" / "La Bestia"** — still split: "Quái Thú" (chunks 1961, 1964, 1977, 1978, 1994, 1995, 1997), "Quái Vật" (chunk 1962), literal "con quái thú" (chunk 1980), kept as a proper name (chunk 1963); chunk 1979 read "the beast" as a ritual creature fed blood ("quái thú"), distinct from the gang name — unresolved as a class; "La Bestia" kept (chunks 1961, 1962, 1977, 1997); "La Siete" / "Siete" / "the Seven" kept as gang names (chunks 1978, 1994, 1995, 1996, 1997).
- **Spanglish / Cuban (C0346, C0351, waves 114–116):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (chunk 1994: 30, 1995: 34, 1996: 36, 1997: 41 — the heaviest cue chunks of the period); "M7" kept (C0351_C66C6B50); Spanish kept (carepija, maje, mami, cojones, Oye, gringo, Mierda, ¡Córtame!, mara, ¡A huevo!, cerote, puta, Flaco, Otra vez).
- **Valley-girl (C0349, wave 115):** "literally" kept as Gen-Z loanword per chunk 1926, heaviest in chunks 1989/1990.
- **Civilian NPC register (C0350, C0357, waves 115, 118):** polite lines "tôi/anh", aggressive lines "tao/mày" per chunk 1915 — held consistently; "Pester" kept app name (C0357_4829A4A1); "drop-shipping" kept (C0357_6B1774CF); "swatted" → "gọi SWAT đến nhà" (C0357_B46BBF5A); "bodycam" → "camera đeo người" (C0357_B46BBF5A); "Gen-Z" kept (C0357_B46BBF5A, C0357_D2A3ED91); "the desperation emoji" → "emoji tuyệt vọng" (C0357_D2A3ED91); "Mr. Too Cool" → "Ông Quá Ngầu" (C0357_C023E9A0); "five ongoing federal lawsuits" → "năm vụ kiện liên bang đang thụ lý" (C0357_B46A1CDB, C0357_D9623FA7); "alpha douchebag" / "betas" kept "alpha" / "beta" (C0357_B743D754); "custody case for my dog" → "vụ tranh chấp quyền nuôi con chó của tôi" (C0357_DDFF318C); "unamerican" → "phản Mỹ" (C0357_070F823B); "small business" → "doanh nghiệp nhỏ", "online shop" → "cửa hàng online" (C0357_070F823B, C0357_07807D00, C0357_21A2DA5C); "grind" → "cày cuốc" (C0357_07807D00); "underwater" → "ngập nợ" financial (C0357_26379179).
- **Veteran / soldier / older (C0353, C0356, waves 116–118):** "Gellhorn" kept as place/gang name throughout chunk 2003; "cellie" → "bạn tù"; "commissary" → "căng tin"; "PTSD" kept (C0353_60ABE05F, C0356_0C53F584, C0356_219516A7, C0356_A97D0180); "Alderney" kept place name, GTA IV reference (C0356_2D3C64BA); "get off my six" → "cút khỏi sau lưng tao" six = 6 o'clock, behind (C0356_0E1AC923); "Watch your six." → "Coi chừng hướng sáu giờ của mày." (C0356_7D0AA83D); "hit the silk" → "nhảy dù" (C0356_172B837D); "bogey" kept, enemy-aircraft reading (C0356_645DC324); "kick the tires and light the fires" kept literal, pilot idiom (C0356_6854BA97); "Wheels up" → "cất cánh" (C0356_7B9D28FD, C0356_96F4C8D2); "Climb on down from there!" → "Trèo xuống khỏi đó đi!" high-place (C0356_64BF5109); "meat wagon" → "xe chở xác" (C0356_5A70191A); "Bush league" → "hạng nghiệp dư" (C0356_5ED96E27); "C.O." → "chỉ huy" (C0356_7FADB341); "cajónes" → "gan" per chunk 1919 (C0356_872725C2); "stolen valor" → "giả danh quân nhân" (C0356_BAAB902C); "make your move" → "ra tay" per chunks 1781/1850 (C0356_B7A08B79); "go for the throat" → "nhắm vào cổ họng mà đánh" (C0356_E57F9C70); "tailing me" → "bám theo tao" (C0356_A3A7C8ED, C0356_E5201483); "pump the brakes" → "hãm phanh lại" (C0356_A222D13F); "forty-four confirmed combat kills" → "bốn mươi bốn mạng đã xác nhận trong chiến đấu" (C0356_2FBFF988); "picking up what I'm putting down" → "hiểu ý tao đang nói" (C0356_372707B8); "I've neutered dogs with bigger balls than you." → "balls" literal dog testicles, NOT "gan" per chunk 1919 (C0355_E7A449C5); "boss" / "chief" kept; "Miss Popular" kept (C0356_5360AB5E); "Whiskey Charlie" kept (C0356_70AE022B).
- **Swamp / rural (C0355, C0359, C0360, waves 117–118):** "gator" → "cá sấu" (C0355_BF4729EC); "fan boat" / "airboat" → "thuyền quạt" (C0355_CE3D3917, C0355_2CEC7400); "mooring" → "neo đậu" (C0355_D7131343); "bowline" → "nút thòng lọng" (C0355_ABDE58FC); "girlie" → "cô em" (C0355_ABDE58FC); "lil' lady" → "cô em nhỏ" (C0355_A044453A, C0355_C85FA370); "dip shit" → "thằng ngu" (C0355_BECB6646); "pansy" → "thằng ẻo lả" (C0355_E12CFF66); "Skeeters" → "Muỗi" (C0355_0ED48D3D); "shock collar" → "vòng cổ sốc điện" (C0355_18102BE7); "lil' puppydog" → "con cún con" (C0355_1297EDDE); "meat locker" → "kho thịt" (C0355_29F24C91); "Man down." → "Có người gục rồi." (C0355_3AECD28A); "On me, y'all!" → "Theo tao, bọn mày!" (C0355_3E0A86CD); "numb nuts" → "thằng ngu đần" (C0355_4AFDFC5F); "Latina" kept (C0355_4CEF3423, C0355_6FE13661); "No habla espanol, senora!" kept Spanish (C0355_6CC374EF); "Hasta luego, bub." kept Spanish (C0355_E3F8C3DD); "Martha and Lyle" and "Millport" kept (C0359_5A197C50); "eight bucks" kept as words, no slot in skeleton (C0359_05A09DF6); "lollygagging" → "lề mề" (C0360_0386FDF9); "Don't weak out on me now!" → "Đừng có hèn nhát với tao lúc này!" (C0360_06F12C43); "stomp a mudhole in your ass" → "đạp cho đít mày thành một cái hố bùn" kept idiom image (C0360_168A562A); "You a fighter or a flincher? Prove it!" → "Mày là dân đánh nhau hay dân nhát gan? Chứng minh đi!" (C0360_1918297D); "Shits and fucking giggles?" → "Để cho vui thôi à?" (C0360_1EC56EB2).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 1982, 1998, 1999, 2000, 2001, 2002, 2019, 2020, 2021, 2022, 2023, 2024); crude sense "lồn" only where the sentence is clearly sexual (chunks 2001, 2012, 2013, 2014, 2015); "pussy bitch" → "con đĩ lồn" per P0 (chunk 2000 C0352_73ED7CFD); "pussy move" → "nước đi hèn" per chunk 1972 (C0358_DDB66596); "pussy ass" → "mông hèn" coward (chunk 2005 C0353_EE2893FE); "puss" → "lồn" sexual (chunks 2003, 2005).
- **"daddy"** → "bố" (majority side, chunks 2001, 2016) vs kept loanword as flirtatious address (chunks 1489, 1509, 1781, 1786, 1788, 1834, 1853, 1858, 1881, 1989, 2001, 2002) vs "Bố" when spoken to a dog (chunk 1800) — still by context.
- **"get down"** → still seven ways: "nằm xuống" (majority) vs "xuống khỏi đó" (high-place, chunks 2003, 2006, 2014) vs "xuống đây" (come-here) vs "quẩy" (party) vs "đánh nhau" (fight, chunk 1849) vs "cúi xuống" (chunks 1867, 2005) vs literal kneeling "quỳ xuống bằng bốn chân" (chunk 2024 C0359_7AB67FAC) — still by context.
- **"get fucked"** → "bị địt" (passive side, chunks 1782, 1788, 1798, 1845, 1851, 1865, 1883, 1925, 1959, 1962, 1998, 2023) vs active readings elsewhere — still by context.
- **"I got you" / "you got it"** — caught ("tao tóm được mày rồi", chunks 1970, 2022) vs reassure ("Mày lo được từ đây", chunk 2021 C0358_CD329A15) vs concession ("mày thắng rồi", chunk 1996) vs understand — still by context.
- **"fuck with"** → mess-with "dây với" remains the default (chunks 2006, 2014, 2019, 2022, 2023, 2024, 2025); like side in clear flirting; hang-out / like-side readings in chunks 1834, 1832, 1839, 1873, 1908; dislike reading "không ưa" added in chunk 1950 (C0337_D25729E3) — still by context.
- **"make moves" / "make a move" / "run it"** — "ra tay" (chunks 1781, 1850, 1874, 1906, 1960, 1996, 2015) vs "kiếm chác" / "tiếp tục làm việc" / "chơi tới bến" — still inconsistent; "Run it." → "Đi thôi" retreat side (chunk 1953 C0338_A3EACE5B).
- **"balls"** → "gan" per chunk 1919 (chunks 1960, 1963, 1964, 2019, 2021, 2022) vs literal testicles in the oral-sex / dog lines (chunk 1961 C0340_F276782B; chunk 2013 C0355_E7A449C5) — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines (chunks 1791, 1796, 1798, 1799, 2016, 2018, 2023) vs as a person elsewhere — by context; "Lilith" read as a dog (chunk 1972) vs a person — by context.
- **"literally"** kept as Gen-Z loanword per chunk 1926 (chunks 1969, 1970, 1971, 1989, 1990, 1991, 1992, 2001, 2016, 2020, 2021, 2022) — settled precedent in C0343–C0352.
- **"lowkey"** kept (chunks 2019, 2020, 2021, 2022) vs translated elsewhere — still by context.
- **"whip"** → "xe" (chunks 2020, 2007, 2008) — settled; **"tweakin'" / "tweakers"** → "ngáo" per chunk 1957 (chunks 2021, 2022); **"sucker punch"** → "đấm lén" per chunk 2004 (chunk 2024 C0359_BBA1A83D); **"whiskey dick"** → "bị liệt cu vì rượu" (chunk 2024 C0359_928C52B2); **"cool as a cucumber"** → "bình tĩnh vãi lồn" idiom dropped the cucumber image (chunk 2024 C0359_7F486C26).
- **"parole"** → "việc tại ngoại" (chunk 2003) vs "án treo" (chunks 2005, 2006) — still inconsistent.
- **"crank"** kept meth loanword (chunk 2025 C0359_E7DCC1DF); **"penjamin"** kept (Benjamin/$100 bill, chunk 2021 C0358_BDFB2A4B); **"Martha and Lyle"** kept, identity unknown (chunks 2023, 2024).
- **Slots kept correctly this period:** "911" → "{number}" (chunks 2014, 2021); "like it's 1999" → "như năm {number}" (C0353_4E09BFD1); "Gangster shit 101" → "Gangster nhập môn {number}" (C0353_937245EA); numbers kept as words where the skeleton has no slot ("eight bucks", C0359_05A09DF6; "forty-four confirmed combat kills" spelled out, C0356_2FBFF988).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side rows in this period: chunk 2023 C0359_4B2761E4 "How 'bout go fuck yourself?" → "Thế thì đi mà tự đụ đi?"; chunk 2025 C0359_DB76A4E9 "Fuck yourself, shithead!" → "Đi mà tự đụ đi, đồ cứt!" (both per the chunk-1011 crude precedent). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"lowkey"** — many-way split (kept / "thật ra" / "kín đáo" / "ngầm" / "hơi") — still inconsistent.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address vs "Bố" when spoken to a dog — still by context.
- **"you got it"** — concession ("mày thắng rồi") vs reassure vs agreement vs understand vs attention vs encouragement — still by context.
- **"I got you" / "I got it" / "gotcha"** — reassure vs understand vs caught — still by context.
- **"trippin'"** — many-way split ("phê" default / "nổi điên" / alarm / bother / don't-worry / don't-care / panicking / agitated "làm quá lên") — still by context; "trip" worry side added in chunk 2007.
- **"Kitty Litter"** — drug name vs literal cat litter — still inconsistent.
- **"bike"** — "xe đạp" (majority) vs "mô-tô" / "xe máy" (minority) — still inconsistent.
- **"body"** — corpse ("cái xác", per chunk 1838) vs living person ("thân hình", chunk 1919) — by context; "bodies" corpse vs manpower (chunk 1982) — by context.
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
- **"take a shot"** — three-way (shoot / drink / try / fight) — still by context; "Take your shot, kid!" → "Nổ súng đi, nhóc!" shoot side (chunk 2015 C0356_C6A4458E).
- **"Skid mark"** — "Vệt phanh" vs "vết ố" — still split.
- **"Clown Town"** — translated vs place name — still inconsistent.
- **"Evil Eye"** — "Mắt Quỷ" vs loanword — still inconsistent.
- **"white trash" vs "trailer trash"** — handling split.
- **"vibe"** — kept vs translated — still by context.
- **"bag(s)"** — money vs drug sense — still by context.
- **"rack"** — clothes rack vs $1,000 — still by context.
- **"happy hour"** — translated vs kept — still inconsistent.
- **"Papi Long Dick"** — kept vs translated — still inconsistent.
- **"gaslight"** — "thao túng" (chunks 1896, 1972, 1973) vs kept — still by context.
- **"Tsou"** — kept as-is (chunks 1717, 1718) — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent (see conventions).
- **"bump"** — drug sense vs collision sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent.
- **"pheromones"** — kept loanword (chunks 1848, 1851, 1967) — now consistent.
- **"smoke" (conflict)** — "gây sự" (chunks 1851, 1863, 1901, 1928, 1984) vs drug side "hút thuốc" (chunk 1873) vs shoot side "bắn chết" (chunk 2008) — by context.
- **"go left"** — "toang" (chunk 1862) vs "rẽ sang hướng xấu" (chunk 1863) — still split.
- **"joint"** — a woman (chunks 1863, 1872) vs other readings — by context.
- **"on the gas"** — drug side in chunks 1881 and 1882 — driving alternative noted in both.
- **"pop it off"** — split: shoot side (chunks 1889, 1892), start-it ambiguous (chunk 1888), fight side (chunk 1891) — still by context.
- **"alpha"** — "kèo trên" (chunk 1896) vs "đầu đàn" (chunk 1898) — still split.
- **"Pussycat"** — kept as magazine name (chunk 1922 C0330_3E6829D5) vs "mèo con" per the P0 rule — flagged for review.
- **"the woes"** — gang reading (chunks 1908, 1909, 1910, 2008) vs female reading (chunks 1907, 1955, 1956) — by context.
- **"creampuff"** — literal "đồ bánh kem" (chunk 1912) vs weak-person "thằng bánh bèo" (chunk 1914) — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines vs as a person elsewhere — by context; "Lilith" read as a dog (chunk 1972) vs a person — by context.
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunks 1764, 1795) — still inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797) — minor inconsistency.
- **"fuck with"** — hang-out reading (chunk 1834) and like-side readings (chunks 1832, 1839, 1873, 1908) vs the mess-with default "dây với" — by context; dislike reading "không ưa" added in chunk 1950 (C0337_D25729E3).
- **"fuck on"** — "cút đi" read as a "fuck off" variant (chunks 1931, 1933, 1934, 1958, 2010) vs sexual side when context is explicit (chunk 2008 C0354_A5F4F52C) — by context.
- **"crash on"** — attack side (chunk 1935) vs flirting side (chunk 1911) — by context.
- **"fuck your shit"** — dismissal side (chunk 2025 C0359_EA1F2040) vs sexual side (chunk 1985 C0348_22A3BE7A) — by context.
- **"free lick"** — renderings vary ("vụ cướp dễ ăn" / "món hời dễ ăn" / "vụ ăn cắp miễn phí") — still inconsistent; "hit a lick" → "cướp được (một) vụ" consistent.
- **"parole"** — "việc tại ngoại" vs "án treo" — still inconsistent.
- **"pack"** — corpse vs drug package vs group/bầy — by context.
- **"cooked"** — active "đỉnh" (chunks 1926, 1972, 2008) vs passive "toang" (chunk 2001) — by context.
- **"Bitch move"** — "Nước đi hèn, con đĩ!" (chunk 1972) vs "Con đĩ, biến đi!" dismissal side (chunk 1928) vs "nước đi hèn" (chunk 1992) — by context.
- **"Hundo p."** — kept (chunk 1971) vs "a hundo p" → "một trăm phần trăm" (chunk 1973) — still inconsistent.
- **"cougar"** — see the deferred item above.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("goo" read as "go", chunk 2020; "ag" read as "age", chunk 2020; "Stoop!" read as "Stop!", chunk 2019; "I'll the call the cops!" rendered by sense, chunk 2018; "be a rude" rendered by sense, chunk 2016; double-comma typo dropped, chunk 2024); "I'm dead" read as slang "cười chết/bó tay", not literal death (chunk 2021 C0358_C955ECB3).

## Next

- Wave 119 (chunks 2026–2035, C0360→) is translating now.
- Next milestone: **125,000** (wave 123).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
