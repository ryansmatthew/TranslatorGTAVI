# Báo cáo cuối P0 — Dịch toàn bộ UI + Subtitle sang tiếng Việt

Ngày: 2026-11-21. Trạng thái: **HOÀN TẤT 100%**.

## Kết quả tổng

- P0 unique (en_norm): **39.003 / 39.003 (100%)**, còn lại 0.
- Tổng dòng `translations` trong DB: **92.717**, tất cả origin `pipeline_muse`, status `machine`.
- Distinct source_id = 92.717 = tổng dòng → **không có dòng trùng lặp** (lỗi trùng ở wave 1 đã sửa từ lâu, không tái diễn).
- Tổng số chunk: 390 file (chunks 01–390), mỗi chunk 100 mục, trừ chunk cuối 390 có 73 mục.
- Số mục bị cách ly (quarantined) trong toàn bộ quá trình: **7 mục, tất cả đã sửa xong, không còn mục nào tồn đọng**.

## Các mục từng bị cách ly (đã sửa hết)

| # | Chunk | source_id | Vấn đề | Cách sửa |
|---|-------|-----------|--------|----------|
| 1 | 116 | C0898_7BB56DC7 | "Brian's 1922" thiếu slot `{number}` | Sửa thành "{number} của Brian", load lại |
| 2–7 | 151 | 6 mục từ item 27 trở đi | File bị lệch: agent bỏ sót "Most Sold Species" làm mọi bản dịch sau đó trượt 1 vị trí | Xóa 118 dòng đã load sai, load lại từ file đã sửa, kiểm tra từng mục |

Sự cố chunk 151 là sự cố nghiêm trọng duy nhất trong toàn bộ quá trình (67 bản dịch load sai + 6 bị cách ly). Đã sửa triệt để: xóa đúng 118 dòng sai, load lại, kiểm tra từng mục đúng.

## Chất lượng — các nhóm cần rà soát (tất cả vẫn status `machine`, sửa được sau)

Chi tiết đầy đủ có trong `P0-Quality-Review-Checklist-DRAFT.md` (7 mục, kèm số liệu DB và source_id). Tóm tắt:

1. **"pussy" — 3 cách dịch (205 dòng)**: thô "lồn" 178 dòng (đúng register chủ đạo); "hèn" 16 dòng — phần lớn đúng nghĩa hèn nhát, không phải làm nhẹ; đọc thành mèo chỉ có 2 lỗi thật: S0840_8B70AAA0, S0840_DE38CAED. "pussycat" → "mèo con" là đúng, đừng sửa.
2. **"fuck with"**: chỉ 1 lỗi rõ — S0142_AF3DBA69 ("địt với đủ thể loại nhạc" → phải là "thích"); còn lại là 2 nghĩa hợp lệ (thích / đừng đụng vào).
3. **"skunk ape"**: 14 dòng giữ loanword (chủ yếu nhãn UI) vs 8 dòng "vượn hôi" trong hội thoại S0424 — cần quy tắc UI vs dialogue.
4. **"Mr. Mangrove"**: "Ông" (5) vs "Ngài" (10) trong cùng cảnh S0424 — chọn một là sửa hàng loạt được.
5. **"Minimap"**: C0898 "bản đồ nhỏ" (7) vs C1090 "Bản đồ thu nhỏ" (4) — chia theo pack, sửa theo pack.
6. **Mất dấu %**: chỉ còn 3 dòng (C0898_3A87E3C0, C0898_556FBED7, S0261_4A2B90B6) — sửa thành "{number}%" như chunk 333.
7. **"white boy"**: S0705_0BC3777F là tiếng lóng chỉ cocaine, bản dịch hiện đọc thành người — 1 dòng cần sửa. (S1192_6BB6B5C8 và S1153_2805F659, S1134_BA641AA6 cũng mơ hồ tương tự.)
8. **Làm nhẹ câu chửi** (ghi nhận rải rác, không chặn): chunk 161 "motherfucking" → "chết tiệt"; chunk 204 "Put your dick away" → "Cất cái của quý đi"; chunk 238 "jerk-off"/"brain fartin'"; chunk 262 "fucktards"; chunk 286 "ass whoopin'"; chunk 292 "Pussy" → "Đồ hèn", "douchebag" → "đồ khốn"; chunk 319 "he's a bitch" → "đồ hèn"; chunk 326 "motherfucker" → "thằng điên". Ngược lại, đa số chunk giữ đúng độ thô theo quy tắc.
9. **Đại từ xưng hô suy đoán**: các chuỗi hội thoại dài (S0567 điện thoại, S0842 bar, S0878 club, S1016–S1088 Jason/Lucia, S1189/S1192 bình luận đua xe) dùng tao/mày, tôi/cậu, anh/em theo suy đoán vì từng câu đứng riêng không rõ người nói/người nghe.
10. **Nhãn UI không ngữ cảnh**: tên cửa hàng, vai trò, perk, tên đường đua... dịch theo cảm giác (ví dụ "Heat" → "Độ nóng" ở chunk 76 nhưng giữ nguyên làm tên đội ở chunk 308).
11. **Các quy ước đã thống nhất xuyên suốt**: tên loài dịch sang tiếng Việt; âm thanh trong `[...]` dịch; "fence" = tiêu thụ đồ trộm cắp; "Master" = Chính; "Lockbox" = hộp khóa; "Pool" = bi-a (trừ khi là hồ bơi thật); "In Spanish:" → "Nói tiếng Tây Ban Nha:..."; tên riêng Lucia/Jason/Vice City/Leonida không dịch; tháng/ngày giờ theo quy ước (AM → SA, PM → CH, WED → T4...).
12. **Sự cố marker đã tự sửa trước khi load**: chunk 295 bỏ mất marker `~sl:~` ở 99/100 mục, agent tự sửa bằng script, kiểm tra 0 lỗi marker trước khi load; chunks 328, 332 tự sửa khối bị lệch, kiểm tra khớp trên đĩa trước khi load. Đây là 2 sự cố suýt xảy ra ngoài chunk 151, đều được chặn trước khi vào DB.

## Quy trình đã chạy

- 40 wave, mỗi wave 1.000 chuỗi (wave cuối 473), mỗi wave 10 subagent dịch song song, mỗi file kiểm tra trên đĩa trước khi load (đủ 100 mục, id đúng thứ tự, vi không rỗng, key đúng {id, vi}, kiểm tra trùng kề để bắt khối bị lệch).
- Mọi chuỗi đều qua validator (marker/slot) trước khi ghi DB; chuỗi lỗi vào quarantine, không ghi.
- Tiến độ commit theo wave, có thể resume; milestone báo cáo ở 5.000, 10.000, 15.000, 20.000, 25.000, 30.000, 35.000.

## Việc tiếp theo (chưa duyệt)

- Chốt 7 mục trong checklist chất lượng (đã gửi user ngày 2026-11-21), chạy lại số liệu sau P0 rồi mới áp dụng sửa.
- P1 (social/item/description/tutorial, 49.880 unique), P2 (lore, 1.937), P3 (dialogue còn lại, 465.455) **chưa được duyệt dịch bulk** — cần user quyết định.
- Sau đó: Phase 4 OCR prototype, Phase 5 Matching Engine, Phase 6 Overlay + Android TV app, Phase 7 Realtime Integration, Phase 8 Optimization.
