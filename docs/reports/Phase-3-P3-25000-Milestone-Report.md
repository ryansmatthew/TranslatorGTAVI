# P3 — Báo cáo mốc 25.000

Ngày: 2026-11-21. Wave 23 vừa nạp xong (chunks 1066–1075).

## Tiến độ

- **P3 unique: 25.435 / 357.142 (7,1%)** — vượt mốc 25.000.
- Còn lại: 331.707 câu chưa dịch. Waves 19–23 đã nạp sạch 5.000/5.000, 0 quarantined.
- Tổng translations trong DB: 192.044 rows, tất cả origin `pipeline_muse`, status `machine`, muse rows = distinct source_ids (không trùng lặp).
- P0+P1+P2+P3 cộng dồn: 39.003 + 45.380 + 1.919 + 25.435 = **111.737 unique strings** đã dịch.

## Nội dung waves 19–23

- **Wave 19 (chunks 1026–1035):** C0030 tail + C0031 cựu binh, C0032 rich/Spanglish, C0033/C0034 khách du lịch. Sự cố: chunk 1034 hoán đổi id ở idx 90/91, agent tự sửa, kiểm tra khớp trên đĩa trước khi nạp.
- **Wave 20 (chunks 1036–1045):** C0035 dân thường, C0036 police radio (mã đơn vị "439"), C0037 bar-hopping, C0038 khách du lịch. Không có sự cố.
- **Wave 21 (chunks 1046–1055):** C0038 tail + C0039/C0040 police radio (mã đơn vị "713", "414"). Sự cố: chunk 1049 hoán đổi id idx 17/18, agent tự sửa, kiểm tra khớp trên đĩa. Chunk 1053 báo cáo tới muộn (sau khi wave đã nạp) — file đã kiểm tra OK trên đĩa trước khi nạp, ghi chú đã đưa vào MEMORY.
- **Wave 22 (chunks 1056–1065):** C0041 police radio (mã đơn vị "673"), C0042/C0043 dân thường đối chất (Krav Maga, Neighborhood Watch, Spanglish). Không có sự cố.
- **Wave 23 (chunks 1066–1075):** C0044 police radio (mã đơn vị "528"), C0045 thợ săn đầm lầy/redneck, C0046/C0047 đường phố AAVE. Không có sự cố. Chunk 1071 chỉ có file ghi trên đĩa (báo cáo chưa tới) nhưng kiểm tra cấu trúc OK trước khi nạp.

## Quy ước đã chốt trong 5 wave này

- Police radio: "Dispatch" → "trung tâm điều phối", "perp"/"suspect" → "nghi phạm", "pinned" → "bị ghìm", "cruiser" → "xe tuần tra", "stun gun"/"shocker" → "súng điện", "shock" → "chích điện", "cuffs"/"bracelets" → "còng"/"còng tay", "squad car" → "xe tuần tra", "body" = xác chết ("drop the body" → "bỏ cái xác xuống"), "PIT" giữ nguyên (đa số), "VCPD"/"SWAT"/"EMS" giữ nguyên, "Sarge" → "Sếp", "ma'am" → "thưa bà", "machete" → "mã tấu", "call it" → "kết thúc vụ này", "stand down" → "lui lại", "move out" → "rút lui", "ETA" giữ nguyên, "casualty" → "thương vong".
- "I got you" theo ngữ cảnh: bắt giữ → "Tao tóm được mày rồi!"; trấn an/giúp đỡ → "Tao lo cho mày"; "I got you covered!" → "Tao yểm trợ mày!"; "I got your back!" → "Tao ở sau lưng mày!" (ủng hộ, khác với bắt giữ).
- "I gotcha" → "tao lo vụ này" (trấn an).
- "Get down" ba phía vẫn tiếp tục: nằm xuống (tránh đạn) / xuống khỏi xe, vật / "Get down here!" → "Xuống đây ngay!".
- "Bike": xe đạp (đa số) vs xe máy/mô-tô (ngữ cảnh truy đuổi, chunk 1054/1066).
- "Paws" → "chân" (K9/furry), "furry"/"furrymobile" → "xe furry", "furball" → "cục lông".
- C0045 thợ săn: "apex predator" → "thú săn mồi đỉnh cao"/"kẻ săn mồi đỉnh cao", "huntsman" → "thợ săn", "wild hog" → "lợn rừng", "survivalist" → "dân sinh tồn", "dirt nap" → "ngủ với đất" (chết), "9 iron" → "gậy sắt số {number}".
- C0046/C0047 AAVE: "bro"/"yo"/"bruh"/"fam"/"homies"/"big dawg"/"slim" giữ loanword, "trippin'" → "phê", "whip" → "xe", "strapped" → "có súng", "jump you" → "úp sọt", "ass whooping" → "trận đòn", "on papers" → "đang bị quản chế", "the laws" → "cớm", "bounce"/"dip" → "chuồn", "clout" giữ nguyên, "snitch" → "thằng mách lẻo", "holla at you" → "hú mày sau", "big dog" → "đại ca" (mỉa mai), "5-0" → "{number} {number}", "call 5-0" → slot, "square up" → "đấu tay đôi", "get fucked up"/"ass whooped" → "bị đánh nhừ tử", "I'm him" → "Tao là số một đây".
- "Who's your daddy?" → "Bố mày là ai?" (theo tiền lệ chunk 1012/1013, "daddy" → "bố").
- "US Army" → "Lục quân Hoa Kỳ" vs "Quân đội Mỹ" (chưa thống nhất).
- "Ma'am" → "thưa bà" vs "thưa cô" (chưa thống nhất).
- "Lib" giữ loanword (chunk 1061) vs "libs" → "bọn cánh tả" (chunk 1055) — chưa thống nhất.
- "Fire" = đội cứu hỏa vs tiếng súng — vẫn mơ hồ (chunk 1059 "Fire's here." → "Đội cứu hỏa tới rồi." vs chunk 1053 "Fire leaving scene" → "Có tiếng súng rời khỏi hiện trường").
- "M7" giữ nguyên (không rõ là băng đảng, đơn vị hay vũ khí — chunk 1058/1060).
- "Deescalate" giữ nguyên tên chó cảnh sát (chơi chữ, chunk 1060).
- "That's Negative." → "phủ định" (đa số) vs "Không phải." (chunk 876).
- "Officer down" → "cảnh sát gục rồi"/"cảnh sát bị hạ" — chết hay bị thương vẫn mơ hồ.
- "Casualty" → "thương vong" — chết hay bị thương vẫn mơ hồ.
- "Eff"/"eff-you" ba phía (thô trực tiếp "địt mẹ mày" / nhẹ "đệt" / làm nhẹ "khốn kiếp") — chưa thống nhất.
- "Go fuck yourself!" ba phía (làm nhẹ "Đi mà tự sướng đi!" / thô "đi mà tự đụ đi") — chưa thống nhất.
- "VC" → "Vice City" vs giữ loanword — chưa thống nhất.
- "Bitch" → "con đĩ" vs "đồ hèn" — theo nghĩa từng câu (chunks 1074/1075 ghi chú cả hai phía).
- "Pussy" theo nghĩa: thô tục ("môi lồn", chunk 1069) vs hèn nhát ("đồ hèn", quy tắc P0).
- "$" mất qua placeholder-slot exception vẫn tiếp diễn khắp các wave; skeleton decimal splits ("6.2L" → "{number} 2L") vẫn tiếp diễn.
- "Move out" → "rút lui" vs "di chuyển thôi" — chưa thống nhất.
- "Jerkoff" → "thằng thủ dâm" vs "thằng quay tay" — chưa thống nhất.
- "Bless your heart" — các cách dịch mỉa mai khác nhau — chưa thống nhất.

## Việc còn lại

- P3 còn 331.707 câu (92,9%). Wave 24 (chunks 1076–1085, C0047→C0049) đang dịch.
- Mốc tiếp theo: 30.000 (wave 28).
- Sau P3: toàn bộ DB có thể dịch (P0+P1+P2+P3) sẽ xong; tier `review` 12.066 dòng không bao giờ dịch tự động.
