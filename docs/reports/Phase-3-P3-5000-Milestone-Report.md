# Phase 3 — Báo cáo mốc 5.000 chuỗi P3 (2026-11-21)

## Tiến độ

- **P3 unique đã dịch: 5.435 / 357.142 (1,5%)** — vượt mốc 5.000.
- Tổng số hàng bản dịch trong DB (origin `pipeline_muse`, status `machine`): **152.952 hàng = 152.952 source_id riêng biệt** (không trùng lặp).
- P0 + P1 + P2 + P3 cộng lại: **91.737 chuỗi unique** đã dịch.
- P3 còn lại: 351.707 chuỗi unique.

## Nội dung 3 wave đầu (chunks 846–875)

Toàn bộ là thoại radio cảnh sát / barks truy đuổi (Core C0000 → C0001): lệnh bắt giữ, báo cáo hiện trường, gọi chi viện, mô tả nghi phạm (chiều cao, chủng tộc, trang phục), mã radio 10-29/10-19/10-97/10-33, mã đơn vị 257/321/391/442/615/662/846/913.

## Sự cố đã xử lý

- **Wave 1, chunk 850**: bản nháp bỏ sót C0000_37380262 ("All good, just keep it put away!") ở vị trí 10, làm toàn bộ id từ vị trí 10 đến 98 bị lệch một bậc — agent tự phát hiện, gán lại id bằng script, đối chiếu từng mục, kiểm tra trên đĩa khớp thứ tự input trước khi nạp.
- **Wave 1, chunk 851**: bản nháp bị trượt 3 mục ở cuối chunk (thiếu C0000_52C8360C "Okay, I got 'em!" và gán sai vi cho C0000_52CC3675 / C0000_52CF8794 / C0000_52EBBF24) — validator bắt được lỗi slot ở C0000_52EBBF24, agent đối chiếu lại với file input, chèn mục thiếu, sửa cả 3 cặp id–vi, kiểm tra trên đĩa khớp trước khi nạp.
- Không có mục nào bị quarantine trong 3 wave đầu (0 lỗi validation ở loader).

## Quy ước đã ổn định trong P3

- "Dispatch" → **"trung tâm điều phối"** (đa số từ wave 2 trở đi; wave 1 còn "Tổng đài" ở chunk 846 và "trung tâm" ở chunks 850/851).
- "subject" → "đối tượng", "suspect" → "nghi phạm", "in custody" → "bị bắt giữ", "backup" → "chi viện".
- "set the box" / "box them in" → **"vây xe lại"** (chiến thuật vây xe của cảnh sát); "PIT" giữ nguyên loanword trong đa số chunk, một số chunk dịch "húc xoay" (chunks 847/862/868/873).
- "NOOSE" giữ nguyên tên đơn vị; "K9" giữ nguyên; "SWAT" giữ nguyên; "PWC" → "mô-tô nước".
- "HQ" → "tổng đài" (chunks 865/869).
- "fuck with" → "chọc" theo nghĩa AAVE (chunk 849).
- "tased"/"shock" → "chích điện".
- "Hispanic" giữ loanword ("nữ gốc Hispanic"); "Caucasian male" → "nam da trắng".
- "furry" giữ loanword.
- "call it" → "kết thúc vụ này" (chunks 861/869/874).
- "I'm arrival." — lỗi ngữ pháp của gốc, đọc là "đã tới nơi" (chunks 847/850/851/864/873).
- "10-19" thường nghĩa là quay về đồn (giữ dạng mã số qua slot).
- Lệnh cho chó K9 bằng tiếng Đức giữ nguyên hoặc dịch: "Fass!" → "Cắn!" (chunks 871/872), "Zoek!" giữ nguyên (chunk 869), "Heel, heel!" → "Sát chân, sát chân!" (chunk 874), "Bite!" → "Cắn!" (chunk 873).

## Ghi chú chất lượng tích lũy (để rà soát sau, tất cả vẫn status `machine`)

- **"DOA"**: dịch hẳn "có một người chết" (chunk 846) vs giữ nguyên loanword (chunks 849/858/860) — chưa thống nhất.
- **"10-29"**: "{number}-{number}" (chunks 857/858/859/860/862) vs "{number} {number}" (chunks 862/864) vs "{number} {number} {number}" (chunk 866, C0001_283DB6FA/C0001_3166C94C) — skeleton của từng chuỗi khác nhau, hiển thị sẽ khác nhau.
- **Chiều cao**: "5'10\"" → "{number}'{number}\"" (chunks 860/875) vs "cao khoảng {number} foot {number} inch" (chunk 849) — chưa thống nhất.
- **"bike"**: mô-tô (chunk 874, theo tiền lệ P0 "Bikes" = mô-tô) vs xe đạp (chunk 867, vì chunk đó dùng riêng "motorbike") — chưa thống nhất.
- **"body"**: xác chết (chunks 858/869/871) vs người còn sống (chunks 860/873) — đọc theo ngữ cảnh từng câu, không chắc.
- **"PIT"**: giữ nguyên loanword (đa số) vs "húc xoay" (chunks 847/862/868/873) — chưa thống nhất.
- **"Dispatch"**: "Tổng đài" (chunk 846) vs "trung tâm điều phối" (đa số) vs "trung tâm" (chunks 850/851) — chưa thống nhất.
- **"clear air!"**: "dọn đường bay!" (chunk 865, giả định dọn không phận cho trực thăng) — có thể là "giữ sóng trống" (clear the airwaves).
- **"Give this a blow for me."**: đọc là thổi máy đo nồng độ cồn (chunk 854) — có thể là nghĩa tục "blow job".
- **"I got you, move!"**: "Tao tóm được mày rồi, đi đi!" (chunk 871) — có thể là "Tao yểm trợ mày, di chuyển đi!" nếu người nói là đồng đội.
- **"Take her out!"**: "Hạ cô ta đi!" (chunk 862) — giữ nghĩa mơ hồ giữa bắt giữ và bắn hạ.
- **"Light him up!"**: "Bắn hạ nó đi!" (chunk 867) — lệnh nổ súng, đọc theo ngữ cảnh.
- **"I'm back up!"**: "Tao đứng dậy được rồi!" (chunk 864) — có thể là "tao có chi viện rồi".
- **"fucked up some spring breaker"**: "xử đẹp một thằng đi nghỉ xuân" (chunk 869) — đọc là đánh đập; có thể là quan hệ tình dục.
- **"kitty"**: "lấy con mèo đi" (chunk 869, C0001_55B528F2) — có thể là mèo thật hoặc tiếng lóng khác.
- **"feeling the scene"**: đọc là lỗi gõ của "fleeing" (chunk 875, C0001_BA58FD14) — không chắc.
- **"fresh bodies"**: "đưa thêm người mới ra đây" (chunk 875) — đọc là cảnh sát mới tới thay ca.
- **"piece"**: "khẩu súng" theo tiếng lóng (chunk 875, C0001_C03E4121).

## Việc còn lại

- P3 còn 351.707 chuỗi unique — tiếp tục waves 1.000, báo cáo mốc mỗi 5.000, báo cáo cuối khi xong.
- Sau dịch: Phase 4 OCR prototype, Phase 5 Matching Engine, Phase 6 Overlay + Android TV app, Phase 7 Realtime Integration, Phase 8 Optimization (theo TDD).
