# Phase 3 — P3 Milestone Report: 125,000 Unique Strings

**Date:** 2026-11-21 (after wave 123 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **125,435 / 357,142 (35.1%)**; P3 remaining **231,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 125,435 = **211,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 313,964 = distinct source_ids (no duplicates)
**Waves in this milestone period (119–123):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 119 | 2026–2035 | 121,435 | Southern "good ol' boy" C0360 → spiritual/swamp witch C0361 → street/AAVE C0362 → Southern C0363 head |
| 120 | 2036–2045 | 122,435 | Southern C0363 tail → street/AAVE C0364 → street/AAVE female C0365 head |
| 121 | 2046–2055 | 123,435 | Street/AAVE C0365 → C0366 → La Siete/Mara gang C0367 → Cuban/Spanglish C0368 head |
| 122 | 2056–2065 | 124,435 | Cuban/Spanglish C0368 → swamp/Southern C0369 → street/AAVE C0370 → C0371 head |
| 123 | 2066–2075 | 125,435 | Street/AAVE C0371 → C0372 → Southern/AAVE female C0373 → street/AAVE C0374 head |

## Incidents (all resolved, none outstanding)

- **Wave 119:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 120:** no incidents. All 10 files passed the full structure check; spot-checks aligned. Chunk 2045 was loaded from a disk-verified file before its handoff arrived; the late handoff's notes were folded into the wave record.
- **Wave 121:** no incidents. All 10 files passed the full structure check; spot-checks aligned. All 10 handoffs arrived before loading.
- **Wave 122, chunk 2062:** the first part-2 draft was missing C0370_4D59125E, shifting everything after it by one — the agent caught it in the cross-check, rewrote part 2 completely and re-verified by script before merging; the full structure check (100 items, ids in order, 0 adjacent dups) passed before loading. All other chunks clean.
- **Wave 123:** no incidents. All 10 files passed the full structure check; spot-checks aligned. All 10 handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **La Siete / La Mara gang (C0367, wave 121):** the heaviest "In Spanish:" period of the whole run — chunk 2050: 42 cues, chunk 2051: 44, chunk 2052: 50, chunk 2053: 33 (C0367: 24, C0368: 9), chunk 2054: 26, chunk 2055: 28, plus chunk 2049: 2 and chunk 2056 (C0368): 34, chunk 2057: 27. All rendered "Nói tiếng Tây Ban Nha:" + translated content. "The Beast" → "Quái Thú" (chunks 2050, 2051, 2052, 2053, per chunks 1961/1964); "La Siete" / "the Seven" / "Siete" kept gang names; "La Mara" kept; "Mara" kept; "M7" kept; "M fucking 7" forced into the "{number}" slot by the skeleton (chunks 2052, 2053); Spanish kept (caraepija, Cerote, Puta, Jueputa, ¡Mierda!, papi, mami, perro, Oye, Vamos, Calma, gringo, pupusas, El Salvador, clica, Semejante cerota, Jaina); "gangbanging" → "xử hội đồng" gang-attack side (C0367_1C7C3082); "hood" → "khu phố"; "homeboy" kept vs "thằng anh em" (chunk 2052); "Daddy" kept loanword as intimate address (C0367_AA109564); "getting jumped" → "bị úp sọt" (C0367_9461E37A); "Talk shit, get hit." → "Nói láo, ăn đòn." (C0367_C3312242); "Blood for the Seven." → "Máu vì Seven." (C0367_23BD11F4); "Mara fee" → "phí Mara" (C0367_398A3FF1); "green card" → "thẻ xanh" (C0367_1A26F40F); "no papers" → "không giấy tờ" (C0367_CCE60856); "My way or the highway." → "Theo cách của tao hoặc cút đi." (C0367_D72472BE); "The Beast" gang-name reading vs the ritual-creature reading (chunk 1979) — still by context.
- **Cuban / Spanglish street (C0368, waves 121–122):** "Comepinga" kept (C0368_488D2847, C0368_4B42E4DA); "balsero" kept (C0368_987B78C6, C0368_F89A07C8); "mis hermanos" kept (C0368_45633398); "Chichi" kept (dog name, C0368_91DBA4B7, C0368_9772369E, C0368_D9348439, C0368_ED3BDD1D); "PeekHole" kept app name per chunk 2048 (C0368_EA985D73); "el jefe" kept (C0368_8A4B70CA); "puta" kept (C0368_91FAF789); "Oye" / "Dale" / "gringo" kept; "Dayron" kept name (C0368_A4972646); "Ocean Beach" kept place name (C0368_9F83F6EF); "fresh meat" → "thịt tươi" (C0368_89218310); "Angstipan" kept made-up drug name (C0368_6FE37B36); "NINE1NINE" kept place name (C0368_32C01487); "Mojito" kept (C0368_1C8F9820); "getty" → "tụ tập" (C0368_336F90E2); "meet the maker" → "gặp ông trời" (C0368_33B057D3); "¡Vete means get out, bro!" → "Vete có nghĩa là cút đi, bro!" (C0368_313E4D02); "FYI" kept (C0368_6754CB44).
- **Swamp / Southern (C0369, wave 122):** tour, bingo, gator hunting, zombie deer/CWD — "gators" → "lũ cá sấu" (C0369_0FE288EC, C0369_17479033, C0369_41CBD957); "chum" → "mồi cá" (C0369_0FE288EC); "zombie deer" → "hươu thây ma" (C0369_31E9D4F8); "CWD" kept (C0369_34AD83C4); "clown car" → "xe hề" (C0369_10C490A5); "packin'" → "mang hàng" gun side (C0369_12F6DB72); "sticky fingers" → "tay máy" (C0369_160F1396); "minced" → "ẻo lả" effeminate side (C0369_21B18FF8); "read the room" → "biết đọc tình hình" (C0369_240BC1CA); "Run the tags!" → "Kiểm tra biển số đi!" (C0369_26805E88); "live one" → "đứa còn sống" (C0369_28DAD595); "Mama's got 'em." → "Mama tóm được bọn nó rồi." (C0369_2CFDBEAD); "Sic 'em, boy!" → "Thả chúng ra, cún!" — "boy" read as the dog (C0369_382196CF); "Nobody under two hundred and fifty." → "Không ai dưới hai trăm năm mươi cân." — read as weight, number kept spelled out because the skeleton has no slot (C0369_3952A806); "top down" → sexual side (C0369_44322388); "possums getting to it" → mating side (C0369_4AE582F1); "sashay them hips" → "lắc hông" (C0369_4E130D32); "Put a fork in this one." → "Xong việc với thằng này rồi." (C0369_94C61DBA); "I bet you look good ass naked on an airboat." → "Tao cá là mày trần truồng trên thuyền quạt trông ngon lắm đấy." (C0369_97284FF2); "On your Ps and Qs, okay?" → "Cẩn thận vào đấy, được chưa?" (C0369_9B3D0833); "I will gut you!" → "Tao sẽ mổ bụng mày!" (C0369_A6D019F6); "Simon says 'Hurry up before I feed you to something'" kept (C0369_A145E829); "My beer's getting warm hunting this fucker..." → "Bia của tao đang ấm dần lên vì đi săn thằng khốn này..." (C0369_B4604705); "That's how I'm cut." → "Tao là kiểu người như thế đấy." (C0369_C4B6382A); "You know what a turkey vulture is? One over there got his eye on you..." → "Mày biết kền kền gà tây là gì không? Một con ở đằng kia đang để mắt tới mày đấy..." (C0369_CF59C1CA); "mama" kept (C0369_5822440E, C0369_937DFBFF); "BuckMe" kept app name (C0369_585B6E66); "white trash" → "lũ da trắng rác rưởi" (C0369_DBC87045); "pussy" → "đồ hèn" coward per P0 (C0369_F7AED7E4, C0369_7BEE14CA); "sweatpea" → "cưng à" (C0369_FD7E579D); "shoot you there" → driving/shuttling side (C0369_F09087F7); "pitch a fit" → "nổi điên" (C0369_F2CB9904); "Mush!" → "Đi nào!" sled-dog command (C0369_2134BDC1).
- **Street / AAVE (C0370–C0372, waves 122–123):** "crash-out" / "crash out" → "làm liều" per chunk 1907 (chunks 2062, 2063, 2065, 2069); "free lick" → "vụ cướp dễ ăn" per chunk 2006 (chunks 2062, 2065); "hit a lick" / "hitting licks" → "cướp (được) một vụ" / "đi cướp vụ" (chunks 2063, 2065); "grid" → "vào cuộc" per chunks 1935–1938 (chunks 2064, 2066); "what you on" → "đang phê cái đéo gì" per chunk 1804 (chunks 2062, 2063, 2064, 2068, 2069, 2070); "tweakin'" → "ngáo" per chunk 1957 (chunk 2063); "scary ass" → "nhát chết" per chunk 2042 (chunks 2063, 2064); "on God" → "thề với Chúa" majority side (chunks 2062, 2063, 2075); "jit" → "thằng nhóc" (chunks 2062, 2065) vs kept (chunk 2063 area); "flawg" kept (chunks 2062, 2042); "jitterbug" kept nickname (chunks 2062, 2069); "thang" → "khẩu súng" per chunk 2062 (chunks 2067, 2069); "strapped" → "mang súng" (chunks 2062, 2067); "press charges" → "tố cáo" (chunks 2062, 2070); "chopping it up" → "tám chuyện" per chunk 2062 (chunks 2062, 2069); "Lock in" → "tập trung vào" per chunk 1909 (chunk 2062); "skrait" → "ổn" per chunk 2044 (chunk 2061); "played" → "nhàm" per chunk 2009 (chunks 2061, 2062); "hustle" → "làm ăn" (chunk 2070); "on my grind" → "đang cày cuốc" / "Tao đang cày đây" (chunks 2069, 2070); "wolfin'" → "hù dọa" (chunk 2070) vs "nói khoác" (chunk 2068) — by context; "sliding" → "kéo tới" arriving side (chunks 2063, 2070) vs "chuồn" leaving side (chunks 2040, 2045, 2069) — by context; "it's up" → "tới luôn" fight side per chunks 1908/1910 (chunk 2063); "catching a charge" → "dính án" (chunk 2063); "spin the block" → "lượn vòng quanh khu phố" (chunk 2064); "run my fade" → "đánh một trận cho ra trò" (chunk 2064); "drill shit" → "xử lý bọn nó" (chunk 2064); "get in that wind" → "chuồn" per chunk 2045 (chunks 2062, 2064, 2069); "stand ten toes down" → "đứng vững" per chunk 2061 (chunk 2074); "paper" → money (chunks 2068, 2069); "paper chase" → "kiếm tiền" (chunk 2069); "twelve" → "cớm" per chunk 2042 (chunk 2069); "them people" → "bọn cớm" police side (chunk 2069); "back up" → "chi viện" (chunk 2069); "straightenin'" → "dằn mặt" (chunk 2069); "going off" → "nổi điên" per chunk 2046 (chunk 2069); "I got yo' ass" → "tao tóm được mày rồi" caught (chunk 2069); "off the porch" → "khỏi hiên nhà" / "rời khỏi hiên nhà" per chunk 2062 (chunks 2062, 2068); "4's up!" → "{number} lên!" — "4"/"4s" gang signal per chunks 1934/1951–1954 (chunk 2063 C0370_6D1A1A0E); "911?" → "{number}?" (chunk 2068 C0372_1C22968A); "pool stick" → "gậy bi-a" — "pool" billiards side, unlike the pool-party "hồ bơi" convention (chunk 2068 C0372_2F753F4B); "kirk" → "nổi điên" (chunks 2065, 2046–2048); "Dappa" kept, unknown meaning (chunk 2065 C0371_43CBEDF7); "Null nie" kept, unknown meaning — 6 occurrences so far (chunks 2068 ×2, 2069 ×3, 2070 ×1; possibly German "null nie" = "never ever"); "wet wet" kept literal, unknown (chunk 2074 C0373_EACE2736).
- **Southern / "granny" (C0373, wave 123):** "plumb" (Southern intensifier) rendered by sense — "plumb crazy" → "điên thật" (chunk 2071) / "điên hẳn" (chunk 2072) / "điên hẳn rồi" (chunk 2073) / "điên hết cả" (chunk 2074); "plumb ugly" → "xấu hoắc"; "Bless yo' heart" → "Thương mày quá" sarcastic Southern side (chunks 2071, 2074) vs "Chúa phù hộ cho mày" (chunk 2072); "chile" kept loanword as address (chunk 2071) vs "cưng" (chunks 2072, 2073); "granny" → "bà" (chunks 2072, 2073); "home trainin'" → "phép tắc ở nhà" (chunk 2071) / "dạy dỗ ở nhà" (chunk 2072); "uppity" → "làm cao" (chunk 2071); "ghetto gutta bitch" → "con đĩ ghetto cống rãnh" (chunks 2071, 2072); "Gellhorn" kept place name (chunks 2071, 2072); "freaky frog" → "con ếch quái dị" literal (chunks 2071, 2072, 2073, 2074); "Yessum." → "Dạ vâng ạ." (chunk 2072); "Mr. Handsome..." → "Ngài Đẹp Trai..." (chunk 2072); "chitlins" → "lòng lợn" (chunk 2073); "bobbled headed fool" → "thằng ngu đầu to như búp bê lắc đầu" (chunk 2073); "shake ass at the Jack of Hearts" → "lắc mông ở Jack of Hearts" (chunk 2073); "You got it. You the boss." → "Được rồi, mày đúng. Mày là sếp." concession per chunk 2038 (chunk 2073); "You got me nah!" → "Mày bắt được tao rồi, không!" caught (chunk 2073); "send ya to state" → "tống mày vào tù bang" (chunk 2074); "paws" → "tay" (chunk 2074); "city gutter rat" → "con chuột cống thành phố" (chunk 2074); "chip on yo' shoulder" → "cái cục tức trên vai" (chunk 2074); "hankerin' for a beatin'" → "thèm ăn đòn" (chunk 2074); "Driips" / "RON Oil" kept names (chunk 2074); "white girl" read as cocaine slang because of "clean nose" (chunk 2071 C0372_FCB6E1AA — same drug reading as S0705 "white boy"); "You look so poor you can't even pay attention!" → kept the "pay attention" wordplay (chunk 2071 C0373_21100A5E).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 2056, 2061, 2062, 2065, 2069); crude sense "lồn" only where the sentence is clearly sexual (chunks 2057, 2075); "pussy bitch" → "con đĩ lồn" per P0 (chunk 2075); "pussy-ass ho" → "con đĩ hèn" coward (chunk 2065); "pussy-ass nigga" → "thằng nigga hèn nhát" (chunk 2048); "pussies" → "thằng hèn" coward (chunk 2056).
- **"daddy"** → "bố" (majority side, chunks 2069, 2070) vs kept loanword as flirtatious address (chunk 2052 C0367_AA109564) vs "Bố" when spoken to a dog (chunk 1800) — still by context.
- **"get down"** → now eight ways: "nằm xuống" (majority) vs "xuống khỏi đó" (high-place) vs "xuống đây" (come-here) vs "quẩy" (party, chunk 2068 C0372_444E98F9) vs "đánh nhau" (fight) vs "cúi xuống" vs literal kneeling (chunk 2024) vs "quẩy" party side in chunk 2043 — still by context.
- **"get fucked"** → "bị địt" (passive side, chunks 1782, 1788, 1798, 1845, 1851, 1865, 1883, 1925, 1959, 1962, 1998, 2023, 2065) vs active readings elsewhere — still by context.
- **"I got you" / "you got it"** — caught ("tao tóm được mày rồi", chunks 2069, 2073) vs reassure ("Tao lo được vụ này", chunk 2066 C0371_836DF4F4) vs concession ("mày thắng rồi", chunks 2071, 2073) vs understand — still by context.
- **"fuck with"** → mess-with "dây với" remains the default (chunks 2066, 2067, 2074, 2075); like side in clear flirting; hang-out / like-side readings in chunks 1834, 1832, 1839, 1873, 1908; dislike reading "không ưa" added in chunk 1950 (C0337_D25729E3) — still by context.
- **"make moves" / "make a move" / "run it"** — "ra tay" (chunks 1781, 1850, 1874, 1906, 1960, 1996, 2015) vs "kiếm chác" (chunk 2069 C0372_9B012439) vs "đang hành động" (chunk 2070 C0372_D653630D) vs "tiếp tục làm việc" / "chơi tới bến" — still inconsistent.
- **"boy" read as a dog** in guard-dog/K9 command lines and dog-owner lines (chunks 1791, 1796, 1798, 1799, 2016, 2018, 2023, 2058) vs as a person elsewhere (chunks 2059, 2060, 2061) — by context.
- **"literally"** kept as Gen-Z loanword per chunk 1926 (chunks 1969, 1970, 1971, 1989, 1990, 1991, 1992, 2001, 2016, 2020, 2021, 2022; chunk 2054 C0368_2E2A6A83) — settled precedent in C0343–C0368.
- **"Martha and Lyle"** kept, identity unknown (chunks 2023, 2024, 2027, 2029, 2032, 2066, 2070, 2071).
- **"Prison Pocket"** kept nickname (chunks 2074, 2075).
- **Slots kept correctly this period:** "911" → "{number}" (chunks 2068, 2028); "M fucking 7" → "M địt mẹ {number}" (chunks 2052, 2053); "4's up!" → "{number} lên!" (chunk 2063); numbers kept as words where the skeleton has no slot ("two hundred and fifty" as weight, C0369_3952A806).
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** No new rows in this period. The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"Null nie"** — kept as-is in all 6 occurrences so far (chunks 2068, 2069, 2070); meaning unknown (possibly German "null nie" = "never ever", a character's slang insult) — unresolved.
- **"Dappa"** — kept as-is (chunk 2065 C0371_43CBEDF7 "Dappa as fuck!") — meaning unknown, unresolved.
- **"wet wet"** — kept literal (chunk 2074 C0373_EACE2736 "A'ight wet wet!") — meaning unknown, unresolved.
- **"chile"** — kept loanword as address (chunk 2071) vs "cưng" (chunks 2072, 2073) — still inconsistent.
- **"bless yo' heart"** — "Thương mày quá" sarcastic (chunks 2071, 2074) vs "Chúa phù hộ cho mày" (chunk 2072) — still inconsistent.
- **"plumb crazy"** — four renderings ("điên thật" / "điên hẳn" / "điên hẳn rồi" / "điên hết cả") — still inconsistent.
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
- **"good looks"** — thanks ("cảm ơn nhé", chunk 2074 C0374_15A99BB9) vs looks — still inconsistent.
- **"dip"** — "chuồn" vs "đi bơi" (river context, chunk 1911) — by context.
- **"FYI"** — kept (chunk 2055 C0368_6754CB44) vs translated — still inconsistent.
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
- **"bless your heart"** — sarcastic renderings vary (see "bless yo' heart" above).
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
- **"fuck on"** — "cút đi" read as a "fuck off" variant (chunks 1931, 1933, 1934, 1958, 2010, 2074) vs sexual side when context is explicit (chunk 2008 C0354_A5F4F52C) — by context.
- **"crash on"** — attack side (chunks 1935, 2044) vs flirting side (chunk 1911) — by context.
- **"fuck your shit"** — dismissal side (chunk 2025 C0359_EA1F2040) vs sexual side (chunk 1985 C0348_22A3BE7A) — by context.
- **"free lick"** — renderings vary ("vụ cướp dễ ăn" / "món hời dễ ăn" / "vụ ăn cắp miễn phí") — still inconsistent; "hit a lick" → "cướp được (một) vụ" consistent.
- **"parole"** — "việc tại ngoại" vs "án treo" — still inconsistent.
- **"pack"** — corpse vs drug package vs group/bầy — by context.
- **"cooked"** — active "đỉnh" (chunks 1926, 1972, 2008) vs passive "toang" (chunk 2001) — by context.
- **"Bitch move"** — "Nước đi hèn, con đĩ!" (chunk 1972) vs "Con đĩ, biến đi!" dismissal side (chunk 1928) vs "nước đi hèn" (chunk 1992) — by context.
- **"Hundo p."** — kept (chunk 1971) vs "a hundo p" → "một trăm phần trăm" (chunk 1973) — still inconsistent.
- **"cougar"** — see the deferred item above.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("goo" read as "go", chunk 2020; "ag" read as "age", chunk 2020; "Stoop!" read as "Stop!", chunk 2019; "I'll the call the cops!" rendered by sense, chunk 2018; "be a rude" rendered by sense, chunk 2016; double-comma typo dropped, chunk 2024; "worf" read as "worth", chunk 2067; "Can't right no" read as "can't right now", chunk 2067; "no you see" read as "now you see", chunk 2066; "for I make ya" read as "before I make you", chunk 2066; "accordian" read as "accordion", chunk 2066; "ain't ain't" double negative rendered by sense, chunk 2070); "I'm dead" read as slang "cười chết/bó tay", not literal death (chunk 2021 C0358_C955ECB3).

## Next

- Wave 124 (chunks 2076–2085, C0374→) is translating now.
- Next milestone: **130,000** (wave 128).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
