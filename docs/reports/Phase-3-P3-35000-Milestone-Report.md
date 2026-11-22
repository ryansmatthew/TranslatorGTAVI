# P3 — Báo cáo mốc 35.000

Ngày: 2026-11-21. Wave 33 vừa nạp xong (chunks 1166–1175).

## Tiến độ

- **P3 unique: 35.435 / 357.142 (9,9%)** — vượt mốc 35.000.
- Còn lại: 321.707 câu chưa dịch. Waves 29–33 đã nạp sạch 5.000/5.000, 0 quarantined.
- Tổng translations trong DB: 206.826 rows, tất cả origin `pipeline_muse`, status `machine`, muse rows = distinct source_ids (không trùng lặp).
- P0+P1+P2+P3 cộng dồn: 39.003 + 45.380 + 1.919 + 35.435 = **121.737 unique strings** đã dịch.

## Nội dung waves 29–33

- **Wave 29 (chunks 1126–1135):** C0065/C0066 AAVE đối chất, C0067 Spanglish/Cuba (20 mục "In Spanish:" chỉ riêng chunk 1132), C0068 nhân viên cửa hàng AAVE, C0069 tail. Không có sự cố. Chunk 1126 và 1129 không gửi báo cáo về — file đã kiểm tra OK trên đĩa trước khi nạp, ghi chú đưa vào MEMORY sau khi báo cáo tới muộn.
- **Wave 30 (chunks 1136–1145):** C0069/C0070 Spanglish, C0071 dân nghiện (dealer, fix, crank, uppers), C0072 Karen/chính trị. Không có sự cố. Chunk 1142 báo cáo tới muộn — file đã kiểm tra OK trước khi nạp.
- **Wave 31 (chunks 1146–1155):** C0073 dân thường sợ hãi/xin tha, C0074 dân "điên"/ảo giác (phê thuốc, "candy lady", "bear-maced"), C0075 chủ nuôi hổ, C0076 đối chất. Không có sự cố.
- **Wave 32 (chunks 1156–1165):** C0076 tail, C0077 nhân viên cửa hàng, C0078 khách du lịch (Ranter, "self-care day", "two-star hotel with no AC"), C0079/C0080 nhân viên cửa hàng (giọng lịch sự "tôi/cậu" xen "tao/mày"), C0081 cãi vã. Không có sự cố. Chunk 1160 không gửi báo cáo về — file đã kiểm tra OK trên đĩa trước khi nạp, ghi chú chưa có (handoff không tới).
- **Wave 33 (chunks 1166–1175):** C0081 tail, C0082 AAVE/redneck rapper (mixtape, "stilo", "Twelve", "on set"), C0083 dân thường/influencer ("views", "followers"), C0084 nhân viên cửa hàng/bà già ("Ol' Boogerwolf", "mama"/"granny"), C0085 influencer. Không có sự cố. Chunk 1174 bản nháp thiếu idx 20 (C0084_6AA9AA28 "Why? Just why?") — agent tự phát hiện, chèn lại, kiểm tra 100/100 trước khi nạp.

## Quy ước đã chốt trong 5 wave này

- "Fuck with" → "đụng tới" (mess with) xuyên suốt; chỉ ngoại lệ khi nghĩa là thích (AAVE like-sense).
- "Pussy" theo nghĩa từng câu: hèn nhát → "đồ hèn" (quy tắc P0, đa số) vs thô tục → "lồn" ("Lick my stale puss!" chunk 1150, "I bet your pussy stink!" chunk 1136, "Pussy on the rag" chunk 1166 → "đồ hèn tới tháng").
- "Get down" ba phía vẫn tiếp tục: nằm xuống (đa số, "Get down!" → "Nằm xuống!") / xuống khỏi xe, vật, chỗ cao ("get down from that car", "Get down 'fore you fall and break your damn neck" → "xuống khỏi đó") / "Get down here!" → "Xuống đây ngay!" (gọi cảnh sát tới).
- "Call it" → "kết thúc vụ này đây" (chốt từ P3) vs "chốt" ("Okay, I'm calling it. We gotta go!") vs "dừng ở đây" (chunks 1116/1145).
- "I got you" theo ngữ cảnh: bắt giữ → "Tao tóm được mày rồi!"; trấn an/giúp đỡ → "tao lo cho mày"; "I got your back!" → "Tao ở sau lưng mày!".
- "You got it" → "mày thắng rồi" (nhượng bộ) — chốt từ chunk 1072; "Sure, you got it." vẫn mơ hồ (đồng ý / mày hiểu rồi, chunk 1174).
- "You got me" → "mày thắng tao rồi" (nhượng bộ) — chốt từ chunk 1072; ngoại lệ "You got me" → "Mày có tao đây" (chunk 1138).
- "Piece" → "súng"; "dealer"/"plug" → "mối"; "fix" → "liều thuốc"; "crank" → "đá"; "uppers" → "thuốc kích thích"; "hit" (drug) → "hơi"; "on dust" → "phê bụi".
- "Go fuck yourself!" → "Đi mà tự đụ đi!" (phía thô trực tiếp, tiền lệ chunk 1011) — phía làm nhẹ "Đi mà tự sướng đi!" vẫn còn ở các chunk cũ, chưa thống nhất.
- "Daddy" → "bố" (đa số, "Daddy's hoppin' in!" chunk 1153, "Hey, daddy, let a grown woman change ya life." chunk 1175) vs giữ loanword (chunk 1022) — chưa thống nhất.
- "Candy lady" → "chị bán kẹo thân thiện trong khu phố" (giữ lớp vỏ bọc euphemism, ma túy — chunks 1150/1162).
- "Gun show" → "khoe cơ bắp" (tiền lệ P0); "candy" = ma túy theo tiếng lóng.
- C0078 khách du lịch: "Ranter" giữ nguyên (app mạng xã hội trong game), "self-care day" → "ngày "chăm sóc bản thân"" (giữ ngoặc kép mỉa mai), "ma'am" → "cô ạ" (phía "thưa cô", chưa thống nhất), "rental" → "xe thuê", "doesn't even phase me" → "chẳng ảnh hưởng gì tới tao đâu" (gốc sai chính tả phase/faze, dịch theo ý định).
- C0079/C0080 nhân viên cửa hàng: giọng lịch sự dùng "tôi/cậu" cho câu phục vụ, chuyển sang "tao/mày" ở câu sợ hãi/chửi bới; "sweetheart"/"sweetie"/"hun" → "cưng"/"cưng à", "shoplifter" → "tên trộm vặt", "trespasser" → "kẻ xâm nhập", "safe in the back" → "cái két ở đằng sau".
- C0082 AAVE: "whip"/"ride" → "xe", "Twelve" → "Cớm"/"mấy thằng cớm", "five-oh" → "5-0", "Deuces" → "Chuồn đây"/"Tạm biệt", "strapped" → "có súng", "ratchet" → "rẻ tiền", "run the fade"/"toe to toe" → "đấu tay đôi", "built different" → "sinh ra đã khác biệt", "keep it G real" → "sống thật chất G", "G"/"GOAT"/"mixtape"/"rapper"/"fo'sho" giữ loanword, "stilo" → "phong cách", "drip" → "đồ" ("copped your drip out the garbage" → "mua đồ ở thùng rác"), "cold as fuck" → "nằm lạnh ngắt rồi" (chết), "dome" → "đầu", "bags" → "túi tiền" (kiếm tiền) vs "túi hàng" (ma túy, chunk 1167 — chưa thống nhất), "Snapmatic"/"Angstipan" giữ nguyên, "24/7" → "{number} {number}" (cửa hàng tiện lợi 24/7).
- C0083 influencer: "views" → "lượt xem", "followers" → "người theo dõi", "you got this" → "Mày lo được mà" (động viên) vs "tao lo vụ này" (trấn an) — theo ngữ cảnh.
- C0084 bà già/nhân viên: "mama" → "má", "granny" → "bà", "Ol' Boogerwolf" giữ nguyên tên/biệt danh, "You're a day late and a dollar short" → "Mày tới muộn một ngày và thiếu một đô rồi" (giữ thành ngữ), "Throw them under the jail!" → "Tống bọn nó vào tù đi!".
- "Nine-one-one" → "911" (dạng số, skeleton không có slot — tiền lệ chunk 1093).
- "VC" giữ loanword (chưa chốt, vẫn chưa dịch thành "Vice City").
- "Trippin'" → "phê" (đa số) vs báo động cứ kêu ("Dang alarm, always tripping..." chunk 1163) — theo ngữ cảnh.
- "$" mất qua placeholder-slot exception vẫn tiếp diễn khắp các wave; skeleton decimal splits vẫn tiếp diễn.

## Việc còn lại

- P3 còn 321.707 câu (90,1%). Wave 34 (chunks 1176–1185, C0085→C0088) đang dịch.
- Mốc tiếp theo: 40.000 (wave 38).
- Sau P3: toàn bộ DB có thể dịch (P0+P1+P2+P3) sẽ xong; tier `review` 12.066 dòng không bao giờ dịch tự động.
