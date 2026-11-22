# Phase 3 — P3 20,000 Milestone Report

**Ngày:** 2026-11-21
**Tiến độ P3:** 20.435 / 357.142 câu duy nhất (5,7%)
**Còn lại P3:** 336.707 câu duy nhất
**Tổng translations (origin `pipeline_muse`, status `machine`):** 182.844 rows = 182.844 distinct source_ids (không trùng lặp)

## Tiến độ theo wave

| Wave | Chunks | P3 unique sau wave | Ghi chú |
|------|--------|-------------------|---------|
| 14 | 976–985 | 16.435 | C0019→C0021 rich/beach/AAVE |
| 15 | 986–995 | 17.435 | C0021→C0024 AAVE/girlie/gym |
| 16 | 996–1005 | 18.435 | C0024→C0025 gym/club/Spanglish |
| 17 | 1006–1015 | 19.435 | C0026→C0028 C0026/girlie/C0028 |
| 18 | 1016–1025 | 20.435 | C0028→C0030 Spanglish/tech-bro |

(Các wave 1–13 xem báo cáo mốc 15.000: P3 unique 15.435 sau wave 13.)

## Nội dung waves 14–18 (từ báo cáo 15.000)

- **Wave 14 (976–985):** NPC giàu C0019 ("have you had work done" → "dao kéo chưa", "negging" → "chê để tán tỉnh", "paypig" giữ nguyên), thoại bãi biển/thể thao C0020 ("chicken fight" → "chọi gà dưới nước", "white-girl-wasted" → "say như gái da trắng", "swiss cheese you" → "bắn mày thủng lỗ chỗ như phô mai Thụy Sĩ", "one-V-one" → "solo 1v1", "Fore!" giữ nguyên), đường phố AAVE C0021 ("toolie" → súng, "run my fade" → "đánh nhau", "mark" → "con mồi", "unc" → "chú", "ear hustling" → "hóng hớt").
- **Wave 15 (986–995):** AAVE C0021–C0022 ("strap" → súng, "gun show" → "khoe cơ bắp", "rack" → một ngàn đô, "shorting" → "bán khống", "paper-handed" → "tay giấy", "bench" → "đẩy tạ", "octagon" → "lồng bát giác"), giọng nữ/influencer C0023 ("Yas, queen!" → "Đúng rồi, queen!", "My b." → "Lỗi của tao!", "Pina Coladas deep" → "uống hai ly Pina Colada rồi"), gym C0024 ("benched a PR" → "đẩy tạ phá kỷ lục cá nhân", "gorge" → "Đẹp vãi", "peg" → nghĩa strap-on).
- **Wave 16 (996–1005):** gym/club C0024 ("cover" → "phí vào cửa", "leg day" → "ngày tập chân", "bench your squat" → "đẩy tạ nặng hơn mức squat của mày", "traps" → "cơ cầu vai", "PR" → "kỷ lục cá nhân", "small dick energy" → "mùi cu nhỏ", "Sike bitch!" → "Lừa được mày rồi"), Spanglish Cuba C0025 ("In Spanish:" → "Nói tiếng Tây Ban Nha:" + dịch nội dung; tiếng Tây Ban Nha giữ loanword: asere, comemierda, comepinga, coño, dale, oye, mami, papi, mamazota, anormal, pero, exacto, ¡Pinga!, santero, picadillo; "crackhead" → "thằng nghiện đá", "strapped" → "mang súng", "get jumped" → "bị úp sọt", "pad"/"crib" → "nhà", "shanked" → "bị đâm", "machete" → "mã tấu").
- **Wave 17 (1006–1015):** C0026 ("get cut" → "ăn dao", "throwdown" → "đánh nhau", "yeyo" giữ nguyên, "losermobile" → "con xe cùi", "24/7" → "{number} {number}" theo skeleton, "pump" → "bơm cơ", "bump" → "một liều"/"hít một phát" (cocaine), "a ten" → "mười điểm"), NPC nữ giàu/chảnh C0027 ("negging" → "chê để tán tỉnh", "cheugy" → "quê mùa", "queen out" → "làm queen", "daddy" → "bố" trong ngữ cảnh con nhà giàu, "food stamp" → "ăn trợ cấp thực phẩm", "match my freak" → "hợp gu biến thái của tao", "tusi" giữ nguyên), C0028 ("ghost" → "lặn mất", "brokies" → "mấy đứa rách rưới", "wee-woo-wee-woo" → "hú còi", "sleep you" → "đánh mày ngất", "outtie" → "chuồn", "filler" → "tiêm filler").
- **Wave 18 (1016–1025):** C0028, rồi Spanglish Cuba nặng C0029 ("In Spanish:" 8–13 câu/chunk; giữ loanword: dale, asere, mami, mija, comepinga, oye, ven acá, en serio, pordioseros, qué bolá, ciao, tú sabes, En serio, mi amor, pírate, cabrón, cojones, repartero, Bembe; "fuck-you money" → "tiền đếch cần ai", "burner phone" → "điện thoại dùng một lần", "side chicks" → "bồ nhí", "tweakers" → "mấy đứa nghiện đá", "ring you up" → "tính tiền cho mày", "shoplifter" → "tên trộm vặt", "take a shot" → "làm một ly đi"), tech-bro/giàu chảnh C0030 ("Mr. Mangrove" → "Ông Mangrove", "shadow banned" → "cấm sóng ngầm", "permaban" → "cấm vĩnh viễn", "beta blockers" → "thuốc chẹn beta", "take the W" → "nhận lấy chiến thắng", "blocklisted" → "bị cấm", "K hole" → "phê K", "gamified blockchain fintech shopping" giữ thuật ngữ, "restraining order" → "lệnh cấm tiếp cận", "one hit wonder" → "thằng một bài hit", "flop sweat" → "mồ hôi thất bại").

## Sự cố

- **Wave 17, chunk 1012:** bản nháp ban đầu thiếu 1 mục — C0027_9945F6E1 "Eww. Gross!" ở idx 11. Agent tự phát hiện và chèn lại đúng vị trí; kiểm tra trên đĩa idx 9–13 trước khi nạp xác nhận khớp ("Eww. Gross!" → "Ghê. Kinh tởm!" đúng idx 11). Nạp sạch, 0 quarantined.
- **Wave 16, chunk 1001:** báo cáo (handoff) của agent tới muộn, sau khi wave đã được kiểm tra trực tiếp trên đĩa và nạp xong. File đã xác minh: 100 mục, id đúng thứ tự, 0 trùng kề. Ghi chú của chunk đã bổ sung vào memory sau đó. Không ảnh hưởng dữ liệu.
- Các wave 14–18 còn lại: mọi file output đều qua kiểm tra cấu trúc (đủ 100 mục, id đúng thứ tự, key chỉ `{id, vi}`, 0 trùng kề) trước khi nạp; loader báo 0 quarantined ở mọi chunk.

## Quy ước đã chốt (waves 14–18)

- "In Spanish:" → "Nói tiếng Tây Ban Nha:" + dịch nội dung; từ tiếng Tây Ban Nha giữ loanword để giữ code-switching (tiền lệ P0, áp dụng đều qua C0025/C0029).
- "bump" → "một liều"/"hít một phát" (cocaine) — ổn định qua chunks 1007/1009/1010/1011/1023.
- "sleep you" → "đánh mày ngất" (chunks 993/995/1014).
- "I got this" → "Tao lo vụ này" (tiền lệ chunk 979, áp dụng đều).
- "cover" → "phí vào cửa" (club/bar, chunks 996/999/1000); "PR" → "kỷ lục cá nhân" (gym); "leg day" → "ngày tập chân"/"tập chân"; "bench" → "đẩy tạ".
- "Mr. Mangrove" → "Ông Mangrove" (theo quyết định đã chốt ở P0).
- "fuck with" theo nghĩa — "đụng tới"/"gây sự" (đe dọa), "chơi với" (AAVE like-sense, lời mời), "thích" (AAVE). Quy tắc theo nghĩa giữ ổn định.
- "pussy" theo nghĩa — "đồ hèn" (hèn nhát, mặc định theo quy tắc P0) vs "lồn" (nghĩa tục, khi ngữ cảnh rõ ràng: chunks 989, 1005, 1018, 1021, 1022, 1024, 1025).
- "piece" = súng (tiền lệ P3, chunks 1023/1025) vs "Muốn ăn đòn không?" cho "You want a piece of this?" (chunk 982, nghĩa đánh nhau) — theo ngữ cảnh.
- "daddy" → "bố" trong ngữ cảnh con nhà giàu được chiều (chunks 1012/1013/1023) vs giữ nguyên loanword khi mơ hồ sugar daddy/bố ruột (chunks 1010/1022/1025) — chưa thống nhất hẳn.
- "24/7" → slot theo skeleton (chunk 947 "{number}/{number}", chunk 1008 "{number} {number}").
- "shorty" → "em gái" + giữ chơi chữ "lùn" (chunk 1008).
- "swing" → "cú vung gậy" (golf, chunks 989/1005) vs "cú đánh" (đánh nhau, chunk 1010) — theo ngữ cảnh.

## Chưa thống nhất / cần xem lại sau (tất cả các row vẫn là status `machine`)

- **"Go fuck yourself!" — vẫn ba cách dịch:** "Đi mà tự sướng đi!" (chunks 932, 943, 968, 1004 — dịch nhẹ) vs "đi mà tự đụ đi" (chunk 969 — thô trực tiếp) vs "Đi mà tự đụ đi, con đĩ!" (chunk 1011 — thô trực tiếp, agent chủ động chọn theo quy tắc không làm nhẹ). Cần một quyết định thống nhất.
- **"VC":** dịch thành "Vice City" (chunks 948/949/964/966) vs giữ nguyên loanword "VC" (chunks 940, 965, 990 "VC three", 1016 "VC girlies"). Vẫn chưa thống nhất.
- **"I got you":** bắt giữ ("Tao tóm được mày rồi!" — chunks 997, 1022, 1023) vs trấn an/giúp đỡ ("tao lo cho mày" — chunks 966/971/991/998/999/1000/1009) — đọc theo ngữ cảnh từng chunk. Mơ hồ cố hữu của câu bark ngắn.
- **"trippin'":** "phê" (chunks 903/904/906/907/961/967/1017) vs "nổi điên" (chunk 948, nghĩa giận dữ). Chưa thống nhất theo nghĩa.
- **"Kitty Litter":** tên thuốc (chunks 831/837/841/956) vs nghĩa đen "cát vệ sinh cho mèo" (chunk 831 C0898_3F5156E9). Vẫn chưa thống nhất.
- **"bike":** "xe đạp" (đa số, kể cả ngữ cảnh tập thể dục) vs "mô-tô" (chunks 874/889/890). Vẫn chia hai phía.
- **"body":** xác chết (đa số) vs người sống/cơ thể (chunks 860/873/922). Mơ hồ theo ngữ cảnh.
- **"bail":** "bảo lãnh" (chunk 947) vs "chuồn" (chunk 936).
- **"good looks":** "Cảm ơn nhé" (chunk 948, nghĩa cảm ơn) vs "Nhìn ngon đấy" (chunk 949, nghĩa khen ngoại hình).
- **"dip":** "chuồn" (chunk 962) vs "đi bơi" (chunk 965, nghĩa bãi biển).
- **"daddy":** "bố" vs giữ nguyên loanword — mơ hồ bố ruột / sugar daddy / người tình lớn tuổi (chunks 1010/1012/1013/1022/1023/1025).
- **"fucked up":** "bị đánh cho nhừ tử" (chunk 1007) vs "phê" (chunks 903/904) vs "hỏng" (chunk 997). Theo ngữ cảnh, chưa thống nhất.
- **"get down":** "nằm xuống" (tránh đạn, chunks 994/1004) vs "quẩy" (nhảy, chunk 993) vs "xuống đi" (xuống khỏi sân khấu, chunk 993). Theo ngữ cảnh.
- **"FYI":** giữ nguyên loanword (chunks 936, 1010, 1013) vs dịch (chunk 204). Vẫn chưa thống nhất.
- **"Madone!":** giữ nguyên loanword tiếng Ý (chunks 968/970/971/973/974) — đa số giữ.
- **"mistress":** "cô chủ" (chunks 948/951/971/973) — chủ nhân (BDSM) hay chủ chó hay cách gọi mỉa mai, vẫn mơ hồ.
- **"24/7":** `{number}/{number}` (chunk 947) vs `{number} {number}` (chunks 1008, 947) — skeleton khác nhau theo từng câu gốc, không phải lỗi dịch.

## Tiếp theo

- Wave 19 (chunks 1026–1035, C0030 trở đi) đang dịch.
- Mốc tiếp theo: 25.000 (wave 23).
- Sau khi P3 hoàn tất: báo cáo cuối P3, rồi sang Phase 4 (OCR prototype).
