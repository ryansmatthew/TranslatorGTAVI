# Phase 3 — P3 15,000 Milestone Report

**Ngày:** 2026-11-21
**Tiến độ P3:** 15.435 / 357.142 câu duy nhất (4,3%)
**Còn lại P3:** 341.707 câu duy nhất
**Tổng translations (origin `pipeline_muse`, status `machine`):** 174.638 rows = 174.638 distinct source_ids (không trùng lặp)

## Tiến độ theo wave

| Wave | Chunks | P3 unique sau wave | Ghi chú |
|------|--------|-------------------|---------|
| 1 | 846–855 | 3.435 | C0000 police radio |
| 2 | 856–865 | 4.435 | C0000→C0001 |
| 3 | 866–875 | 5.435 | C0001 police radio |
| 4 | 876–885 | 6.435 | C0001→C0002 AAVE street |
| 5 | 886–895 | 7.435 | C0002→C0003 police radio |
| 6 | 896–905 | 8.435 | C0003→C0004 |
| 7 | 906–915 | 9.435 | C0004→C0005 |
| 8 | 916–925 | 10.435 | C0005→C0006 civilian |
| 9 | 926–935 | 11.435 | C0006→C0009 influencer/rich |
| 10 | 936–945 | 12.435 | C0009→C0012 Spanglish |
| 11 | 946–955 | 13.435 | C0012→C0014 beach/gym/influencer |
| 12 | 956–965 | 14.435 | C0014→C0017 rich/AAVE/bar staff |
| 13 | 966–975 | 15.435 | C0017→C0019 |

## Nội dung waves 11–13 (từ báo cáo 10.000)

- **Wave 11 (946–955):** dân thường bãi biển C0012, gym-bro C0013 ("whip" → "xe", "the pump" → "bơm cơ", "gains" → tăng cơ, "pre-workout" giữ nguyên), influencer/rich C0014.
- **Wave 12 (956–965):** NPC giàu/môi giới C0015 ("tax bracket" → "đẳng cấp thuế", "resy" → "đặt bàn", "mil" → triệu đô), thoại đường phố AAVE C0016 ("throw hands" → "đánh nhau", "murk" → "giết", "strapped" → "có súng"), nhân viên quán/bar C0017.
- **Wave 13 (966–975):** nhân viên quán/bar C0017, rồi C0018 giọng Ý-Mỹ ("Madone!", "Paisan", "puttan" → "con đĩ", "Capiche?" giữ nguyên, "Nona" giữ nguyên), C0019 NPC giàu/chảnh và phẫu thuật thẩm mỹ ("BBL" giữ nguyên, "lipo" → "hút mỡ", "chemical peel" → "lột da hóa học", "face lift" → "căng da mặt", "nillionaire" → "triệu phú không đồng").

## Sự cố

Không có sự cố nào trong waves 11–13. Mọi file output đều qua kiểm tra cấu trúc (đủ 100 mục, id đúng thứ tự, key chỉ `{id, vi}`, 0 trùng kề) trước khi nạp; loader báo 0 quarantined ở mọi chunk.

## Quy ước đã chốt (waves 11–13)

- Lệnh K9 tiếng Đức: "Fass!" → "Cắn!", "Fuss!" giữ nguyên (theo chunks 890/900).
- "5-0" → `{number} {number}` hoặc `{number}-{number}` tùy skeleton (tiếng lóng chỉ cảnh sát).
- "call it" → "kết thúc vụ này"; "stack" → "cọc tiền" = 1.000 đô.
- "do numbers" → "câu view" (theo chunk 954; từng có "làm mưa làm gió" ở chunk 928).
- "crashing out" → "sắp nổi điên"; "dip" → "chuồn" (trừ nghĩa đi bơi ở bãi biển).
- "mil" → triệu đô ("drop ten mil easy").
- "Kitty Litter" đọc là tên thuốc (theo tiền lệ P2) — xem mục chưa thống nhất dưới đây.

## Chưa thống nhất / cần xem lại sau (tất cả các row vẫn là status `machine`)

- **"Go fuck yourself!" — ba cách dịch:** "Đi mà tự sướng đi!" (chunks 932, 943, 968 — dịch nhẹ, đi ngược quy tắc không làm nhẹ) vs "đi mà tự đụ đi" (chunk 969 — nghĩa thô trực tiếp) vs "Đi mà tự sướng đi!" được chunk 968 chủ động chọn theo tiền lệ 932/943. Cần một quyết định thống nhất.
- **"VC":** dịch thành "Vice City" (chunks 948/949/964/966) vs giữ nguyên loanword "VC" (chunks 940, 965 "VC cops"). Vẫn chưa thống nhất.
- **"I got you":** bắt giữ vs trấn an/giúp đỡ — đọc theo ngữ cảnh từng chunk (trấn an ở chunks 966/971, bắt giữ ở chunk 968). Mơ hồ cố hữu của câu bark ngắn.
- **"trippin'":** "phê" (chunks 903/904/906/907/961/967) vs "nổi điên" (chunk 948, nghĩa giận dữ). Chưa thống nhất theo nghĩa.
- **"Kitty Litter":** tên thuốc (chunks 831/837/841/956) vs nghĩa đen "cát vệ sinh cho mèo" (chunk 831 C0898_3F5156E9). Vẫn chưa thống nhất.
- **"fuck with":** theo nghĩa — "đụng tới" (đe dọa), "thích" (AAVE), "đùa giỡn" (chunk 948). Quy tắc theo nghĩa đã giữ ổn định, chỉ cần lưu ý khi rà soát.
- **"bike":** "xe đạp" (đa số, kể cả ngữ cảnh tập thể dục) vs "mô-tô" (chunks 874/889/890). Vẫn chia hai phía.
- **"body":** xác chết (đa số) vs người sống/cơ thể (chunks 860/873/922). Mơ hồ theo ngữ cảnh.
- **"bail":** "bảo lãnh" (chunk 947) vs "chuồn" (chunk 936).
- **"good looks":** "Cảm ơn nhé" (chunk 948, nghĩa cảm ơn) vs "Nhìn ngon đấy" (chunk 949, nghĩa khen ngoại hình).
- **"dip":** "chuồn" (chunk 962) vs "đi bơi" (chunk 965, nghĩa bãi biển).
- **"Madone!":** giữ nguyên loanword tiếng Ý (chunks 968/970/971/973/974) — đa số giữ, chưa có ý kiến dịch hẳn thành "Trời ơi!".
- **"mistress":** "cô chủ" (chunks 948/951/971/973) — chủ nhân (BDSM) hay chủ chó hay cách gọi mỉa mai, vẫn mơ hồ.
- **"piece":** súng (tiền lệ P3) vs xe/vật khác — đọc theo ngữ cảnh từng chunk.
- **"24/7":** `{number}/{number}` theo skeleton (chunk 947, đọc là cửa hàng 24/7).

## Tiếp theo

- Wave 14 (chunks 976–985, C0019 trở đi) đang dịch.
- Mốc tiếp theo: 20.000 (wave 18).
- Sau khi P3 hoàn tất: báo cáo cuối P3, rồi sang Phase 4 (OCR prototype).
