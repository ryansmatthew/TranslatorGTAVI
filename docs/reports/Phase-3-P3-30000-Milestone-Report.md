# P3 — Báo cáo mốc 30.000

Ngày: 2026-11-21. Wave 28 vừa nạp xong (chunks 1116–1125).

## Tiến độ

- **P3 unique: 30.435 / 357.142 (8,5%)** — vượt mốc 30.000.
- Còn lại: 326.707 câu chưa dịch. Waves 24–28 đã nạp sạch 5.000/5.000, 0 quarantined.
- Tổng translations trong DB: 199.747 rows, tất cả origin `pipeline_muse`, status `machine`, muse rows = distinct source_ids (không trùng lặp).
- P0+P1+P2+P3 cộng dồn: 39.003 + 45.380 + 1.919 + 30.435 = **116.737 unique strings** đã dịch.

## Nội dung waves 24–28

- **Wave 24 (chunks 1076–1085):** C0047/C0048 AAVE, C0049/C0050 đối chất đường phố, C0051 dân đảo/beach. Không có sự cố. Chunk 1083 báo cáo tới muộn (sau khi wave đã nạp) — file đã kiểm tra OK trên đĩa trước khi nạp, ghi chú đã đưa vào MEMORY.
- **Wave 25 (chunks 1086–1095):** C0051 dân đảo/beach, C0052/C0053 dân thường đối chất, C0054 thuyết âm mưu/MyWays. Không có sự cố.
- **Wave 26 (chunks 1096–1105):** C0054 tail + C0055 AAVE, C0056 bà già Cuba Spanglish, C0057 redneck/mud park. Không có sự cố.
- **Wave 27 (chunks 1106–1115):** C0058 redneck/mud park, C0059 dân thường, C0060 AAVE, C0061 tail. Không có sự cố.
- **Wave 28 (chunks 1116–1125):** C0061/C0062 dân thường đối chất, C0063 redneck livestream/quay phim, C0064/C0065 AAVE. Sự cố duy nhất: chunk 1122 bản nháp thiếu C0063_D2536339 ở idx 26 làm lệch khối — agent tự phát hiện, chèn lại và sửa vi của C0063_D2FE8058, kiểm tra khớp trên đĩa trước khi nạp (0 trùng kề).

## Quy ước đã chốt trong 5 wave này

- "Fuck with" → "đụng tới" (mess with) xuyên suốt; chỉ ngoại lệ khi nghĩa là thích (AAVE like-sense, chunk 1078 "I don't fuck with nobodies" → "tao không chơi với mấy đứa vô danh đâu").
- "Pussy" theo nghĩa từng câu: hèn nhát → "đồ hèn" (quy tắc P0, đa số) vs thô tục → "lồn" ("Lick my pussy, pusslicker!" chunk 1108, "I thought I smelled pussy" chunk 1107, "pussy lips" chunk 1069).
- "Get down" ba phía vẫn tiếp tục: nằm xuống (tránh đạn, "Stay the fuck down!" → "Nằm mẹ xuống!") / xuống khỏi xe, vật, chỗ cao ("get down from there", "get down off my car" → "xuống khỏi xe") / "Get down here!" → "Xuống đây ngay!".
- "Take a shot" ba phía: bắn ("nã một phát đi", chunk 1084; "bắn một phát", chunk 1091) / quay phim ("Quay một phát đi", chunk 1083) / uống một ly (chưa gặp lại từ wave 24).
- "Call it" theo nghĩa: kết thúc vụ này ("I'm callin' it" → "tao kết thúc vụ này đây") vs chốt/quyết định ("Okay, I'm calling it. We gotta go!" → "tao chốt đây", chunk 1086) vs đoán ("can't call it" → "đoán", chunk 1073).
- "I got you" theo ngữ cảnh: bắt giữ → "Tao tóm được mày rồi!"; trấn an/giúp đỡ → "tao lo cho mày"; "I got you covered!" → "Tao yểm trợ mày!"; "I got your back!" → "Tao ở sau lưng mày!".
- "You got it" → "mày thắng rồi" (nhượng bộ) — chốt từ chunk 1072, dùng xuyên suốt waves 24–28.
- "Dog walk you/'em" → "dắt mày/bọn nó đi như dắt chó" (làm nhục/thống trị).
- "Sleep you" → "đánh mày ngất xỉu" (theo tiền lệ chunk 995/1080).
- "Piece" → "súng" ("'cause you got a piece?", "Nice piece." → "Súng ngon đấy.").
- "PO" → "cán bộ quản chế" (parole officer, theo tiền lệ P0).
- "Nut up" → "cứng lên" / "Cứng cỏi lên đi".
- "Trippin'" → "phê" (đa số) vs "Đừng có lo" ("Don't even trip", chunk 1125) vs "làm quá/cư xử kỳ quặc" (chưa chốt).
- "On" = phê thuốc ("what you on right now?" → "mày đang phê cái gì đấy").
- "Blew me" → "làm tao thất vọng rồi" (chunk 1097 — vs nghĩa tình dục "blow me", chưa chốt).
- "Skid mark" → "Vệt phanh" (chunk 1089) vs "vết ố" (chunk 1090, nghĩa quần lót) — chưa thống nhất.
- "Buff out" → "đánh bóng" (sửa vết xước xe).
- "Ice" → "xử vụ này" (giết / xử lý vụ việc, mơ hồ — chunk 1083).
- "Go fuck yourself!" → "Đi mà tự đụ đi!" (phía thô trực tiếp, tiền lệ chunk 1011) — phía làm nhẹ "Đi mà tự sướng đi!" vẫn còn ở các chunk cũ, chưa thống nhất.
- "Daddy" → "bố" (đa số, "I'm done like my daddy" chunk 1115) vs giữ loanword (chunk 1022) — chưa thống nhất.
- "White trash" → "đồ da trắng rác rưởi" (chunk 1115); "hickville" → "cái xó nhà quê"; "trailer trash" giữ loanword.
- "Deep state" → "nhà nước ngầm" (chốt); "MyWays"/"My Way" giữ nguyên; "shill" → "tay sai"; "reptilian" → "bò sát"/"thằn lằn"; "shapeshifter" → "biến hình"; "burner" → "điện thoại dùng một lần"; "sovereign citizen" → "công dân có chủ quyền".
- "Nine-one-one" → "911" (dạng số, skeleton không có slot — tiền lệ chunk 1093).
- C0051 dân đảo: "dude"/"buddy" → "anh bạn"/"bạn ơi", "bro"/"y'all"/"amigo"/"Comprende?"/"Adios"/"Hasta never."/"vaminos" giữ loanword, "vibe" giữ ("vibe tốt"), "Mahalo" giữ, "cabesa" giữ (đầu, tiếng Tây Ban Nha), "make like a tree and head out" → "chuồn đây" (chơi chữ tree/leaf mất), "skate"/"outski" → "chuồn".
- C0056 bà già Cuba: "In Spanish:" → "Nói tiếng Tây Ban Nha:" + dịch nội dung (kể cả cue kép trong một mục); từ Tây Ban Nha giữ loanword (Dale, Oye, Ay, Comunistas, chancla, Dinero, Gordito, Manolito, pipo, pero, "Ni pinga", culicagaos); "Second Amendment" → "Tu chính án số 2"; "Clown Town" → "Thị trấn Hề" (vs giữ tên địa danh, chưa chốt); "Sargent Panther" giữ nguyên; "Holly Mother" đọc là lỗi gõ của "Holy Mother" → "Đức Mẹ ơi".
- C0063 livestream: "go live" → "livestream", "followers" → "người theo dõi", "tag me" → "tag tao vào", "@Redneck_CEO_22" giữ nguyên, "FuckUpVille" giữ nguyên ("Population: you!" → "Dân số: mày!"), "open-carry-challenge" giữ nguyên cụm tiếng Anh, "redneck balls" → "hai hòn dái nhà quê", "do numbers" → "hút view".
- C0064/C0065 AAVE: "nigga"/"bruh"/"bro"/"yo"/"y'all"/"homie"/"twin"/"shawty"/"Boo" giữ loanword, "mark" → "con mồi", "warrants" → "đang bị truy nã", "one more strike" → "một lần cảnh cáo nữa", "get jumped" → "bị úp sọt", "catch a charge" → "dính thêm một tội nữa", "on my momma" → "thề với má tao", "gas" → "cỏ" (cần sa, chunk 1124), "holding" → "đang có hàng" (ma túy, chunk 1125), "your ass is grass" → "mông mày sẽ thành cỏ" (giữ hình ảnh gốc).
- "VC" giữ loanword (chưa chốt, vẫn chưa dịch thành "Vice City").
- "$" mất qua placeholder-slot exception vẫn tiếp diễn khắp các wave; skeleton decimal splits vẫn tiếp diễn.

## Việc còn lại

- P3 còn 326.707 câu (91,5%). Wave 29 (chunks 1126–1135, C0065→C0069) đang dịch.
- Mốc tiếp theo: 35.000 (wave 33).
- Sau P3: toàn bộ DB có thể dịch (P0+P1+P2+P3) sẽ xong; tier `review` 12.066 dòng không bao giờ dịch tự động.
