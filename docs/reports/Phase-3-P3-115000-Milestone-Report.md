# Phase 3 — P3 Milestone Report: 115,000 Unique Strings

**Date:** 2026-11-21 (after wave 113 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **115,435 / 357,142 (32.3%)**; P3 remaining **241,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 115,435 = **201,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 302,652 = distinct source_ids (no duplicates)
**Waves in this milestone period (109–113):** 5,000 strings, 0 quarantined in total

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 109 | 1926–1935 | 111,435 | Beach valley-girl C0331 → Spanglish/Cuban C0332 → street/AAVE C0333 → C0334 head |
| 110 | 1936–1945 | 112,435 | Street/AAVE C0334 → C0335 → C0336 |
| 111 | 1946–1955 | 113,435 | C0336 tail → C0337 → C0338 → C0339 head (Haitian Creole) |
| 112 | 1956–1965 | 114,435 | Haitian Creole C0339 → street/AAVE C0340 → Spanglish/Cuban C0341 → combat barks C0342 head |
| 113 | 1966–1975 | 115,435 | Swamp/river C0342 → valley-girl/rich-girl C0343 → alt/queer C0344 → civilian NPC C0345 head |

## Incidents (all resolved, none outstanding)

- **Wave 109:** no incidents. All 10 files passed the full structure check; spot-checks aligned. Chunk 1928's output file was malformed mid-write at the first disk check (agent still writing in two halves) and chunk 1935's file did not exist at that check; both completed and verified before loading.
- **Wave 110:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 111:** no incidents. All 10 files passed the full structure check; spot-checks aligned.
- **Wave 112, chunk 1957:** output file did not exist at the first disk check — its agent was still running (confirmed via subagent list, last activity 2 s earlier); its handoff arrived 2026-11-21 ~20:36 and the final file passed the full structure check before loading. All other chunks' handoffs arrived before loading.
- **Wave 113, chunk 1969:** handoff arrived late (2026-11-21 ~20:38) — the file had passed the full structure check on disk before loading, per the established precedent. All other chunks' handoffs arrived before loading.

## Conventions settled / reinforced in this period

- **"The Beast" / "La Bestia"** — three-way split, unresolved as a class: "Quái Thú" (chunks 1935, 1961, 1964), "Quái Vật" (chunk 1962 C0341_35BE2D2F "I'm the fucking Beast!"), kept as a proper name (chunk 1963, C0341_650A66E6, C0341_6ED88235, C0341_92D3389B); "La Bestia" kept (chunks 1961, 1962).
- **"grid" / "get in that grid"** → "vào cuộc" settled (chunks 1935–1938); "woo woo woo" kept as meaningless chant (chunk 1938); "stupid head" → "thằng đầu ngu" (chunks 1943, 1944).
- **"flag"** — many-way split by context: red-flag reading (chunk 1936 C0334_31E733D2), "nói điêu" / cap variant (chunk 1936), gang "phất cờ" (chunk 1937), "khoe khoang" (chunk 1938), "giơ cờ" gang (chunk 1939) — still by context.
- **"crash on"** → attack side (chunk 1935) vs flirting side (chunk 1911) — by context; "fuck on" → "cút đi" read as a "fuck off" variant (chunks 1931, 1933, 1934, 1958).
- **"the woes"** → gang reading (chunks 1908, 1909, 1910) vs female reading "mấy em" (chunks 1907, 1955, 1956) — still by context.
- **"creampuff"** → literal "đồ bánh kem" (chunk 1912) vs weak-person "thằng bánh bèo" (chunk 1914) — by context.
- **"Pussycat"** kept as magazine name (chunk 1922 C0330_3E6829D5) vs "mèo con" per the P0 rule — flagged for review.
- **"flawg"** kept, unknown meaning (chunks 1935 C0334_21C4EE2D, 1936 C0334_5889E315).
- **Haitian Creole (C0339, waves 111–112):** "In Creole:" → "Nói tiếng Creole:" + translated content, per the "In Spanish:" precedent (chunks 1954: 17, 1955: 26, 1956: 34, 1957: 34, 1958: 9); "cheri doudou" kept (C0339_75953A43); "cheri" kept (chunk 1957); "Manmzel" kept (chunk 1957 per chunk 1954); "free lick" → "miếng mồi ngon" per chunk 1938 (C0339_7EA6A56F); "what you on" → "đang phê cái đéo gì" per chunk 1804 (C0339_79F3CE8A, C0339_82AADF87); "lock in" → "tập trung vào" per chunk 1909 (C0339_71E6F0C8); "crashing out" → "làm liều" per chunk 1907 (C0339_AE53D6EC); "on sight" → "gặp mặt là xử luôn" per chunk 1807 (C0339_9CF70E2F); "spin on" → "quay xe lại xử" per chunk 1937 (C0339_8FBD6932, C0339_B5EA3C9E, C0339_BE4EE195); "woes" → "mấy em" female per chunk 1907 (C0339_870231C9, C0339_8A2DBB1D); "tweaker" → "ngáo đá" (C0339_98E43934); "dickride" → "bú cu" crude (C0339_9E619E91); "buss a U-ey" → "quay đầu xe lại" (C0339_A49DB7EF); "walk 'em down" → "tiến tới xử bọn nó" (C0339_AAD0A32E); "Zaks" kept as place name (C0339_A978EBC6); "plug" → "mối" (C0339_C5B1565C); "racks" → "cọc tiền" per chunk 1935 (C0339_E63291E3); "skrait" → "ổn" per chunks 1908/1910 (C0339_F72F34C1); "I'm not the one" → "tao không phải đứa để mày dây vào đâu" per chunk 1952 (C0339_BE03E1AE); "sliding" → "chuồn" per chunk 1935 (C0339_D4A7E39F); "let that bitch sing" → "để khẩu đó hát" gun side per chunk 1935 (C0339_CF445E5A); "Put that bitch down." → "Hạ khẩu súng đó xuống." gun side per chunk 1935 (C0339_714F65A6).
- **Spanglish / Cuban (C0340–C0341, wave 112):** "In Spanish:" → "Nói tiếng Tây Ban Nha:" + translated content (chunks 1961: 5, 1962: 23, 1963: 12, 1964: 19); Spanish kept (mami, jit, barrio, puta, puto, vamanos, cerote, caraepija, Oye, ¡Nambe chele!, baboso, Maje, ¡A la gran Puta!, ¡Púchica!, ¡Vamos, vamos!, Vaya pues, El maje, A la gran puta); "La Bestia" kept; "Hector" kept (C0341_4ADDF6B6); "La Perle" kept (C0340_FB9B5F52); "BuckMe" kept app name per chunk 1904 (C0340_FE76CCAF); "Youngin" kept (C0340_F121E89B); "the Seven" kept as gang name (C0341_B7B3A140); "M7" kept per precedent (C0341_CC94E32F); "fish scale" kept as cocaine loanword (C0340_65547AA7); "strap" → "súng" (C0340_614BC08C); "lock it down" → "khóa chặt" per chunk 1855 (C0340_67CD4094); "dip" → "chuồn" (C0341_A657D58D, C0341_DF89CBB3); "whip" → "xe" (C0341_AFAB26B1); "fucked up" → "toang" (C0341_E083167F); "OD" kept loanword (C0341_CAA19B01); "put her to sleep" → kill reading (C0341_46EBF1A5); "he cut that with some weird shit" → drug-cutting reading (C0341_3C1759EC); "Mami no ingles?" translated to Vietnamese (C0340_ECF8753C — flagged: Spanish sentence translated rather than kept whole).
- **Swamp / river Florida (C0342, wave 113):** dog voice in several lines (C0342_381C7519, C0342_42AD76E3, C0342_5168A799, C0342_5859D698); "gators" → "cá sấu" (C0342_74D784E3); "dock" → "cập bến" (C0342_6CE52798); "pick you off" → "bắn tỉa" (C0342_6BD14E9E); "nosejob" → "mũi sửa" (C0342_5A4A36DD); "gumption" → "gan" (C0342_67CC2832); "Swamp's got its eyes on you..." → "Đầm lầy đang để mắt tới mày đấy..." (C0342_C365BC10); "I got eyes on you, and so does the drone." → "Tao đang để mắt tới mày, và con drone cũng thế." (C0342_C8067F41); "piece" → "khẩu súng" per chunk 1936 (C0342_8416875C); "pheromones" kept per chunks 1848/1851 (C0342_8B807499); "Mary-Lynn" kept (C0342_9145B244); "brother" → "anh bạn" per chunk 1965 (C0342_9D20C5E8); "lady" → "cô em" per chunk 1963 (C0342_B3C45805, C0342_BF67BA48); "boy" → "nhóc" per chunk 1965 (C0342_C33A5DFE); "sweetheart" → "cưng" (C0342_85A5D857); "Big man!" → "Ông lớn!" (C0342_943794D2); "body" → "cái xác" per chunk 1838 (C0342_F3E172A6); "salty" → "cay cú" (C0342_FF6E7E5C); "lock down" → "phong tỏa" literal area-lockdown (C0342_E2F99A83, NOT "khóa chặt" — by context); "lock it in" → "tập trung vào" per chunk 1909 (C0342_EAF9759B); "make your ass 2-D" → "làm cho cái mông mày thành {number}-D" (C0343_164A5BE9); "ranger" → "kiểm lâm", "invasive species" literal (C0342_0C9A67D7).
- **Valley-girl / rich-girl (C0343, wave 113):** "literally" kept Gen-Z loanword — heaviest "literally" chunk so far (chunk 1969: "literal murder on sight", "literal sand... literal eyeballs", "literal pile of literal shit... literal diamonds", "Literally fine", "literal actual problem"); "Literally" kept per chunk 1926 (chunk 1970); "Babe" / "girl" / "dude" kept; "Oh my God" → "Ôi trời ơi"; "vibe" kept (C0343_2317A87D); "lowkey" kept (C0343_72C26C5C); "ATV" kept (C0343_55C3D85F); "Bok, bok, bok!" kept chicken sound (C0343_4BA79FB0); "psycho lemur" → "vượn cáo điên khùng" (C0343_5BD2296E); "dog filters" → "filter chó" (C0343_73BA64F8); "fiancé" → "hôn phu" (C0343_57D0A201, C0343_ACEE0FE0); "homophobe" → "người kỳ thị đồng tính" (C0343_73187AE6); "contact" → "kính áp tròng" (C0343_3B005111); "training wheels" → "bánh xe tập đi" (C0343_3391ACB3); "hungover as balls" → "nôn nao vãi lồn" (C0343_4B267A89); "pickle pussy" → "lồn dưa chua" explicit crude (C0343_7E231D90); "mom-ass pedo van" → "xe van ấu dâm kiểu mẹ bỉm" (C0343_8078EA49); "fucking me! You're fucking everyone right now!" → "chơi tao/chơi tất cả" deceived side (C0343_5BB41776); "girl's girl" → "kiểu con gái bênh con gái" (C0343_E8A38265); "dick punch" → "thằng đấm cu" (C0343_EB06E990); "reciept" kept source typo, "hóa đơn" (C0343_F0669B6C); "making eyes" → "liếc mắt đưa tình" (C0343_F25BA9FD); "eat your fucking eyes like grapes" → "ăn đôi mắt chết tiệt của mày như ăn nho" (C0343_F6BA9AA2); "provider" → "người lo liệu" (C0343_1D0F7406); "exposure-therapy away my shark thing" → "liệu pháp tiếp xúc để hết sợ cá mập" (C0343_9D343631); "coconut rum" → "rượu rum dừa" (C0343_AF63C059); "crash it" → "đâm nó" car-crash side (C0343_C92FAB3D); "gritty" → "đầy cát" beach side (C0343_D1B72D61); "deposit" → "tiền đặt cọc" (C0343_8F858397).
- **Alt / queer (C0344, wave 113):** "Lilith" kept — read as a dog in chunk 1972 ("Sic 'em, girl!", "Attack, Lilith! Go for the throat!", "Calm down, Lilith! Be a good girl!") vs "Lillith" variant kept in chunk 1971 (spelling as in source); "gaslighting" → "thao túng" per chunk 1896 (C0344_32966A3C, C0344_3EADC751); "femme"/"masc" kept (C0344_379A332E, C0344_38232B36, C0344_7DF35ECF, C0344_A0789F41); "cishet" kept (C0344_0D22DB91); "incel"/"loser" kept (C0344_211B36A5); "deuces" kept (C0344_0F85DEA2); "Hundo p." kept (C0344_020542DC) vs "a hundo p" → "một trăm phần trăm" (C0344_CC8ED2D0) — still inconsistent; "safe word" → "từ an toàn" per chunk 1885 (C0344_1895BE42); "tap in" → "tham gia" per chunk 1965 (C0344_1BBCC735); "lowkey" kept (C0344_1D8C204D); "chode" kept (C0344_12CEB8CE); "kickball" kept (C0344_186F0B34); "hon" kept (C0344_3092BE43); "bounce" → "chuồn" (C0344_3126F473); "pube" → "lông mu" (C0344_0145EF21); "your body, your choice" → "Cơ thể của mày, lựa chọn của mày" (C0344_1646AFB2); "masc joy" kept "masc" (C0344_165744CE); "go for the throat" → "nhắm vào cổ họng mà đánh" per chunk 1945 (C0344_525F8961); "Sic 'em, girl!" → "Cắn bọn nó đi, cưng!" dog command per chunk 1940 (C0344_680C8B19); "get down" → "nằm xuống" majority (C0344_580F8FCB); "pussy" → "hèn" coward (C0344_5203B740, C0344_65F5F0D2) vs explicit-sexual "lồn" where clearly sexual (C0344_88465A5D, C0344_90C0EA49, C0344_A6BDBCA4) — by context; "I'm out" → "chuồn" (C0344_3DF987F7, C0344_58A0169B); "I'm cooking" → "đang đỉnh" per "cooked" → "đỉnh" chunk 1926 (C0344_71CC2672); "get topped" → "bị đè" sexual (C0344_4498FFCD); "goo-goo eyes" → "ánh mắt đắm đuối" (C0344_46CE011A); "Allyship, so tight." → "Tình đồng minh, chặt vãi." (C0344_4A6312D9); "bisexual freak out" → "lên cơn lưỡng tính" (C0344_5E1FCB52); "muscle mommy" kept (C0344_61032321); "kiki" → "tám chuyện" queer slang (C0344_6E66EE00 "Can't kiki, dog, getting swole."); "fuck me." → "địt mẹ." exclamation, not invitation (C0344_6FCBB505); "Bitch move, bitch!" → "Nước đi hèn, con đĩ!" (C0344_702DC75A, vs chunk 1928 "Con đĩ, biến đi!" dismissal side — still by context); "all sizzle no steak" → "chỉ được cái mẽ ngoài chứ chẳng có gì" (C0344_771880C6); "Back it up, slugger." → "Lùi lại, đồ đấm bốc." (C0344_7B5CA9A9); "locked in" → "tập trung" per chunk 1909 (C0344_87FFDF48); "Daddy's got you" → "Bố lo cho mày" reassure, "daddy" → "bố" majority (C0344_997F4C0E); "lipstick femme" kept "femme" (C0344_8680C8ED); "beta" kept (C0344_9A3B38BC); "Sagittarius" → "Nhân Mã" (C0344_9B1C2F81, pet dog); "fur baby" → "thú cưng" (C0344_A7A23513); "piece" → "khẩu súng" (C0344_B3BE178A); "fit" → "bộ đồ", "It's giving X" → "đúng kiểu X luôn" per chunk 1945 (C0344_BE2BF995); "Bet." → "Chốt." (C0344_D1E9C78F); "slit" → "lồn" (C0344_D3437F2D); "wet" → "ướt át" sexual (C0344_CE3B2408); "menstrual cup" → "cốc nguyệt san" (C0344_B10BB612); "@BabyGay99" kept (C0344_CDEDF0E0); "matches" → dating-app matches (C0344_9B64DF12); "demi-sexual" kept (C0344_EC7D7EFB "my dog is demi-sexual"); "queer" kept (C0344_F7838CB1); "lock in" → "tập trung vào" per chunk 1909 (C0344_F7C38029); "double dipping" → "chấm hai lần" literal (C0344_FAD8F781); "barking up the right tree" kept dog image + wordplay (C0344_F0A819D5); "Eat a butt!" → "Ăn đít đi!" (C0344_FD3599B5); "Fielding error!" → "Lỗi bắt bóng!" baseball (C0344_D5DDA04C); "the thing me and Lilith here have in common... we're both dogs." → "cả hai đứa tao đều là chó." dog-park literal (C0344_E31AA538); "Babe I got this, I lift." → "Cưng ơi, tao lo vụ này, tao tập gym mà." (C0344_E95A35CD); "Drag 'em! Start cookin'!" → "Kéo bọn nó ra! Bắt đầu nấu đi!" (C0344_05111D53, ballroom-drag alternative noted); "take a shot" → drink side "làm một ly đi" (C0344_23AAEB94); "shit-housery" → "trò nhảm cứt" (C0344_25714853); "read this chode" kept literal (C0344_12CEB8CE, ballroom "read" alternative noted).
- **Civilian NPC (C0345, wave 113):** register split per chunk 1915 — polite/annoyed NPC lines "tôi/anh", "tao/mày" only in clearly aggressive/intimate lines (chunks 1974, 1975); crude kept ("sack of shit" → "bao cứt khổng lồ", "shit" → "cứt", "fuck you" → "địt mẹ bọn nó", "asshole" → "thằng khốn"); "get off on this shit" → "sướng vì cái trò này" sexual arousal, "totally flaccid" → "xìu hẳn" (C0345_2E34492D); "sit on my face" → "ngồi lên mặt anh" literal (C0345_2EA92395); "pube" → "sợi lông mu" (C0345_5B9061DB); "go with the flow" → "xuôi theo dòng đời" (C0345_435542DF); "shit in their sundae" → "ỉa vào kem" literal (C0345_49147652); "bone to pick" → "có chuyện với tôi" (C0345_4C35F144); "good look" → "trông ngon đấy" (C0345_639F1F10); "bad fucking time" → "một phen khó chịu chết tiệt" (C0345_652B0F0E); "back to the grind" → "quay lại làm việc" (C0345_6624AE12); "ramblin' on outta here" → "đang lẩm bẩm rời khỏi đây" (C0345_6863701A); "be a chicken" → "làm con gà" coward (C0345_71AAA7EE); "sneak a peek" → "lén nhìn" (C0345_72A71B3C); "wrapped up in all this" → "dính vào tất cả chuyện này" (C0345_7ACEFCE0); "those dudes ain't chill" → "mấy gã đó không dễ chịu đâu" (C0345_7C92C0D1); "y'all" kept; "Whoa" kept; "Mm, mm-hmm" → "Mm, ừm-hừm"; "Welp" → "Chà"; "mess with me" → "dây với tôi" mess-with default (C0345_15232EA4); "go to town on it" → "thoải mái mà quậy nó đi" (C0345_1E2FD6DD); "I'm shit with faces" → "tôi dở nhớ mặt lắm" (C0345_12031B98); "Triggers a little sticky" → "Cò hơi dính một chút" gun side (C0345_0453F74D); "can't reward someone for being a dick" → "không thể thưởng cho kẻ khốn nạn được" (C0345_139755FD); "You tryin' to get the cops called on your ass, 'cause I'll do it..." → threat to call police (C0345_6C1E7022).
- **"pussy"** → coward sense "đồ hèn" per the P0 rule remains the clear default in street contexts (chunks 1959, 1960, 1961, 1962, 1963, 1972, 1974); crude sense "lồn" only where the sentence is clearly sexual (chunks 1959, 1970, 1973); "pussies" → "lũ lồn" explicit (chunk 1959 C0340_6B024984) vs "lũ hèn" (chunk 1962 C0341_2831CFEA) — by context; "pussy bitch" → "con đĩ lồn" per P0 (chunk 1962 C0341_27B24E08); "pussy ass" → "mông hèn" coward (chunks 1961, 1958); "pussy move" → "nước đi hèn hạ" (chunk 1968 C0343_001436DC).
- **"daddy"** → "bố" (majority side, chunks 1973, 1974) vs kept loanword as flirtatious address (chunks 1489, 1509, 1781, 1786, 1788, 1834, 1853, 1858, 1881) vs "Bố" when spoken to a dog (chunk 1800) — still by context.
- **"get down"** → still six ways: "nằm xuống" (majority) vs "xuống khỏi đó" (high-place, chunks 1966, 1968) vs "xuống đây" (come-here) vs "quẩy" (party) vs "đánh nhau" (fight, chunk 1849) vs "cúi xuống" (chunk 1867) — still by context.
- **"get fucked"** → "bị địt" (passive side, chunks 1782, 1788, 1798, 1845, 1851, 1865, 1883, 1925) vs active readings elsewhere — still by context; "get fucked" → "đi mà bị địt đi" passive (chunk 1959 C0340_6D33A08F).
- **"I got you" / "you got it"** — caught ("tao tóm được mày rồi", chunk 1970 C0343_C0FB097A) vs reassure vs understand ("mày hiểu rồi", chunk 1959 C0340_A40941DD) vs encouragement ("Mày làm được mà", chunk 1959 C0340_8F5707C4) — still by context.
- **"fuck with"** → mess-with "dây với" remains the default; like side in clear flirting; hang-out / like-side readings in chunks 1834, 1832, 1839, 1873, 1908 — still by context; dislike reading "không ưa" added in chunk 1950 (C0337_D25729E3).
- **"make moves" / "make a move" / "run it"** — "ra tay" (chunks 1781, 1850, 1874, 1906, 1960) vs "kiếm chác" / "tiếp tục làm việc" / "chơi tới bến" vs plan side "Tao còn vụ phải làm" (chunk 1959 C0340_719AF409) — still inconsistent; "Run it." → "Chơi đi." (chunk 1957 C0339_C0C2F1E0).
- **"balls"** → "gan" per chunk 1919 (chunks 1960, 1963, 1964) vs literal testicles in the oral-sex line (chunk 1961 C0340_F276782B) — by context.
- **"white boy"** → "thằng da trắng" person side (chunks 1959, 1966) — vs cocaine slang in the fixed P0 row S0705_0BC3777F.
- **Slots kept correctly this period:** "50 racks cash" → "{number} cọc tiền mặt" (C0339_E63291E3); "make your ass 2-D" → "làm cho cái mông mày thành {number}-D" (C0343_164A5BE9); "911" → "{number}" (C0344_8D762A0E); numbers kept as words where the skeleton has no slot.
- **"bitch" → "con đĩ"; "motherfucker" → "thằng chó chết"; "fuck you" → "địt mẹ mày"; "fuck off" → "cút đi"; "asshole" → "thằng khốn"; "shit" → "cứt"** — crude register kept throughout, no sanitizing.

## Quality notes for later review (all rows status `machine`)

- **"Go fuck yourself!" three-way split — DECISION STILL PENDING with the user.** New crude-side row in this period: chunk 1948 C0337_6CE2F30F "Go fuck yourself, pussy!" → "Đi mà tự đụ đi, đồ hèn!" (crude side per chunk 1011). The pending decision (options A crude / B softened) was presented to the user on 2026-11-21 and is still unanswered. Do NOT ask about "eff"/"eff-you" or "cougar" until after this decision.
- **"eff" / "fuggin'"** — chunk 1802 rendered 4 "eff" items as "đệt"; chunk 1809 C0297_0B7C5F80 "Oh eff you!" → "Ôi, đệt mày đi!"; chunk 1811 rendered 3 "fuggin'" items as "chết tiệt"; chunk 1869 C0314_BFC04472 "Eff off!" → "Đệt, cút đi!" — still deferred behind the pending "Go fuck yourself!" decision.
- **"cougar"** — "máy bay bà già" (chunks 1269/1272, 1823, 1826 C0302_F85267FE) vs "con báo già" (chunk 1271) vs "Con cọp già" (chunk 1270) — decision still deferred.
- **"the Y" / "Y Hotel"** — "khách sạn Y" vs kept as name — still unresolved.
- **"VC"** — kept loanword vs "Vice City" — still inconsistent.
- **"on God"** — translated "thề với Chúa" (majority) vs kept loanword — still inconsistent.
- **"lowkey"** — many-way split (kept / "thật ra" / "kín đáo" / "ngầm" / "hơi") — still inconsistent.
- **"daddy"** — "bố" (majority) vs kept loanword as flirtatious address vs "Bố" when spoken to a dog — still by context.
- **"you got it"** — concession ("mày thắng rồi") vs reassure vs agreement vs understand vs attention vs encouragement — still by context.
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
- **"gaslight"** — "thao túng" (chunks 1896, 1972, 1973) vs kept — still by context.
- **"Tsou"** — kept as-is (chunks 1717, 1718) — unresolved.
- **"make moves" / "make a move" / "run it"** — renderings inconsistent (see conventions).
- **"bump"** — drug sense vs collision sense — by context.
- **"girlie"** — "cô em" / "cưng" vs kept loanword — still inconsistent.
- **"pheromones"** — kept loanword (chunks 1848, 1851, 1967) — now consistent.
- **"smoke" (conflict)** — "gây sự" (chunks 1851, 1863, 1901) vs drug side "hút thuốc" (chunk 1873) — by context.
- **"go left"** — "toang" (chunk 1862) vs "rẽ sang hướng xấu" (chunk 1863) — still split.
- **"joint"** — a woman (chunks 1863, 1872) vs other readings — by context.
- **"on the gas"** — drug side in chunks 1881 and 1882 — driving alternative noted in both.
- **"pop it off"** — split: shoot side (chunks 1889, 1892), start-it ambiguous (chunk 1888), fight side (chunk 1891) — still by context.
- **"alpha"** — "kèo trên" (chunk 1896) vs "đầu đàn" (chunk 1898) — still split.
- **"Pussycat"** — kept as magazine name (chunk 1922 C0330_3E6829D5) vs "mèo con" per the P0 rule — flagged for review.
- **"the woes"** — gang reading (chunks 1908, 1909, 1910) vs female reading (chunks 1907, 1955, 1956) — by context.
- **"creampuff"** — literal "đồ bánh kem" (chunk 1912) vs weak-person "thằng bánh bèo" (chunk 1914) — by context.
- **"boy" read as a dog** in guard-dog/K9 command lines (chunks 1791, 1796, 1798, 1799) vs as a person elsewhere — by context; "Lilith" read as a dog (chunk 1972) vs a person — by context.
- **"succubus"** — kept loanword (chunk 1763) vs "nữ quỷ" (chunks 1764, 1795) — still inconsistent.
- **"pocket pussy"** — "lồn giả bỏ túi" (chunk 1799) vs "lồn bỏ túi" (chunk 1797) — minor inconsistency.
- **Slot-forced awkwardness** continues: "$"-loss via the placeholder-slot exception; skeleton decimal splits; numbers kept as words where the skeleton has no slot.
- **Source artifacts preserved as-is:** source typos read as intended ("In Spines:" read as "In Spanish:", chunk 1884; "past time" read as "pastime", chunk 1924; "keeping it tall" read as "keeping it real" variant, chunk 1908; "reciept" kept as a typo, chunk 1971).

## Next

- Wave 114 (chunks 1976–1985, C0345→) is translating now.
- Next milestone: **120,000** (wave 118).
- P3 completion target: **357,142 / 357,142 (100%)**, then a final P3 report. The 12,066-row `review` tier is never auto-translated.
