# Phase 3 — Báo cáo cuối P2 (lore) (2026-11-21)

## Kết quả cuối cùng

- **P2 unique đã dịch: 1.919 / 1.919 (100%)** — không còn chuỗi lore nào chưa dịch.
- Tổng số hàng bản dịch trong DB (origin `pipeline_muse`, status `machine`): **146.156 hàng = 146.156 source_id riêng biệt** (không trùng lặp, kiểm chứng sau mỗi wave).
- P0 + P1 + P2 cộng lại: **86.302 chuỗi unique** đã dịch (P0 39.003 + P1 45.380 + P2 1.919).
- P2 chạy trong 2 wave (chunks 826–845): wave 1 = 1.000 chuỗi, wave 2 = 919 chuỗi (chunks 836–844 mỗi chunk 100, chunk 845 chỉ 19 chuỗi: mô tả cài đặt C1090).
- **Quarantined: 0 mục tồn đọng.**

## Nội dung P2

P2 = toàn bộ lore (category `lore`, group "Bài viết / Truyện"):

- C0679: 4 dòng chỉ số game (sát thương vũ khí khi đứng yên...).
- C0680: các câu đố triết học/bí ẩn (10 Sephirot Kabbalah, 7 hành tinh/nguyên tố, Phi 1,618, "Trên sao, dưới vậy", tarot).
- C0898: phần lớn nhất — bài báo châm biếm (Weazel News, Megamundo, WAiNK, Sprunk/Mutandis, Bilgeco, Dodos Rising...), truyện chọn-lựa-của-bạn (gamebook, lật tới trang N), truyện fantasy/western/sci-fi, tóm tắt cốt truyện (Jason/Lucia/Raul/Kordell/Boobie...), thẻ thể thao (STAKS/LOB DUNKS/PBL/AFF), nhật ký tháp canh Kalaga/Switchback, email/thư trong game (Yordanis Castillo Perez — thư trong chai dưới đáy biển), thơ Jun Youbi, hướng dẫn gameplay, nhãn mở khóa.
- C1090: 19 mục mô tả tùy chọn cài đặt (radio khi lên xe, dấu chỉ cửa, HUD, nền phụ đề, la bàn, bản đồ thu nhỏ, Lái tự động...).

## Sự cố đã xử lý trong P2

- **Wave 1, chunks 828 và 833**: agent đầu tiên bị tràn giới hạn token (văn bản lore dài) — không có file output. Chạy lại theo cách chia 2 nửa (1–50 rồi 51–100) và xong cả hai, 0 lỗi validation.
- **Wave 1, chunk 832**: bản nháp gán nhầm id cho mục 34 (C0898_4AA89689 thay vì C0898_4A99D8CC, Hollow Earthers) — agent tự phát hiện và sửa trước khi bàn giao; kiểm tra trên đĩa khớp thứ tự input.
- **Wave 1, chunk 829**: 1 id gõ sai (C0898_254FE12D → C0898_254FE12F) + 8 chỗ lệch marker `~n~` — agent tự phát hiện và sửa, validate lại 0 lỗi.
- **Wave 2, chunk 833**: lúc nối file 4 lần, mỗi lần append thừa một dấu phẩy làm JSON lỗi ở 3 chỗ nối — agent tự phát hiện, xóa dấu phẩy thừa; 5 lỗi marker `~n~~n~` bị gộp thành `~n~` cũng đã khôi phục đủ.
- **Wave 2, chunk 837**: bản nháp lọt một từ tiếng Nga "едва" và một từ "turned" chưa dịch — agent tự phát hiện và sửa.

## Ghi chú chất lượng tích lũy (để rà soát sau, tất cả vẫn status `machine`)

### Quy ước đã ổn định trong P2

- 10 Sephirot (Kabbalah) dịch thống nhất: Kingdom → Vương Quốc, Foundation → Nền Tảng, Wisdom → Trí Tuệ, Understanding → Thấu Hiểu, Mercy → Lòng Từ Bi, Severity → Sự Nghiêm Khắc, Beauty → Vẻ Đẹp, Splendor → Hào Quang, Victory → Chiến Thắng, Crown → Vương Miện.
- "skunk ape" → "vượn hôi" (đối thoại/lore) vs giữ loanword (nhãn UI) — theo quy tắc P0.
- "Mr. Mangrove" → "Ông Mangrove"; "Hollow Earth" → "Trái Đất Rỗng"; "Good Time State" → "Bang Vui Vẻ".
- "Minimap" → "Bản đồ thu nhỏ"; "stick drift" → "trôi cần"; "deadzone" → "Vùng chết".
- "Ratface" → "Mặt Chuột"; "Swallow" giữ nguyên họ người (theo đa số chunks 797/798) — vẫn mâu thuẫn với "Chim nhạn" (chunk 800).
- "Kitty Litter" → "cát mèo" theo nghĩa đen trong đa số chunk, dù nhiều ngữ cảnh gần như chắc là tên ma túy (chunks 831/841) — ngược với chunk 837 ("Kitty Litter" giữ nguyên làm tên ma túy).
- "BODY COUNT" → "SỐ NGƯỜI ĐÃ QUAN HỆ" / "SỐ BẠN TÌNH" (nghĩa số bạn tình, theo nghĩa đoán) — nhất quán ở chunks 831/837/839/840/843.
- "AMERICA'S NEXT TOP HOOKER" — dịch ("GÁI ĐIẾM HÀNG ĐẦU NƯỚC MỸ") ở chunks 830/836/840, giữ nguyên tên ở chunks 828/843 — chưa thống nhất.
- "BACKYARD AMERICAN MANIA" — dịch ("CUỒNG LOẠN SÂN SAU NƯỚC MỸ") ở chunk 830, giữ nguyên tên ở chunks 832/839 — chưa thống nhất.
- "Y Hotel" / "the Y hotel" — giữ nguyên tên (chunks 830/838) vs "khách sạn Y" (chunk 834) — vẫn chưa thống nhất.
- "Extraction" → "di tản" (chunks 829/836, theo đa số) vs "rút lui" (chunk 395).
- "heat" — "độ nóng" (chunks 76/841) vs "mức truy nã" (chunk 843) vs "cắt đuôi cớm" (chat S0593) — chưa thống nhất.
- "bag" → "túi tiền" (nghĩa tiền, đa số).
- "fence" → "tay tiêu thụ"; "chop shop" → "xưởng rã xe"; "Finder's Fee" → "phí tìm đồ".
- "taco dump" → "ị một bãi taco to đùng" (chunks 816/838).
- "P.O." → "cán bộ quản chế".
- Tên loài dịch sang tiếng Việt; tên Latin giữ nguyên (Chaceon fenneri, Menippe Mercenaria).
- Thẻ thể thao: tên đội/cầu thủ và viết tắt thống kê (AVG/HR/RBI/SB/PPG/TCK...) giữ nguyên; nhãn dịch sang tiếng Việt.
- "1st/2nd place" → "Hạng 1/2" (chunk 843 sửa slot thừa).
- Nguồn gõ sai/typo giữ nguyên trong bản dịch: "Hewit"/"Hewitt", "Galetski"/"Galecki", "meteorogical", "ODONALD WEINER", "Marty's head" (linh vật tên "Manty"), "swapmy homini" (có thể là "swampy hominid").

### Lớp lỗi do skeleton ép slot

- Số trong tiêu đề điều khoản bị nuốt: "3.3.3." → "{number}.{number}." (chunk 842, C0898_E57224C0), "7.2.6." → "{number}.{number}." (chunk 837), "12.2.7." → "{number}.{number}." (chunk 830) — hiển thị sẽ thiếu một số.
- Tách số thập phân: "42.5kg" → "{number} 5kg" (chunk 836), "+3.9kg" → "+{number} 9kg" (chunk 843), "6.2L" → "{number} 2L" (chunk 835).
- "24/7" → "{number}/{number}" (chunk 837).
- "1.7 lbs" → "{number} lbs" (chunk 827); "1.4 Billion?" → "{number} tỉ?" (chunk 824).
- Mất dấu `%` qua skeleton: "3P% | 36.4" → "3P {number}" (chunk 830, C0898_342B5F21) — ngược với tiền lệ khôi phục "{number}%" ở chunk 333.

### Mơ hồ dai dẳng — cần ngữ cảnh game để quyết

- **"kitty litter"**: cát mèo theo nghĩa đen vs ma túy — xem mục quy ước ở trên.
- **"The Cardinals"** (câu đố C0680): Hồng Y giáo chủ / chim hồng y / lá bài — chunk 826 giữ loanword, chunk 827 dịch "Các Hồng Y".
- **"Hands on deck, suit you!"**: chơi chữ deck/suit của bài tây — dịch thoát ở cả hai chunk nhưng khác nhau ("Tay trên boong..." vs "Tay đặt lên bộ bài...").
- **"She is so Phi (ne)"**: chơi chữ Phi/fine — giữ nguyên dạng ngoặc ở cả hai chunk.
- **"The Seasons"**: "Cardinals", "leaves" (lá/lá bài), "homerun" — chưa rõ.
- **"Move up by me"**: "pitch" (cao độ nhạc / giá chào hàng / ném bóng), "ON/ZERO" (trò chơi gì?) — chưa rõ.
- **"1 sole on my face"**: chơi chữ sole/soul (chunk 834).
- **"Nether region"**: "Vùng Hạ Giới" (chơi chữ vùng kín, chunk 834).
- **"li-bear-ty"**: chơi chữ liberty + bear, không giữ được (chunk 834).
- **"BODY COUNT"**: số bạn tình vs số người giết — đọc theo nghĩa bạn tình ở P2 (xem quy ước ở trên).
- **"Delights"**: "Khoái lạc" (chunk 830) vs giữ nguyên tên (chunk 843).
- **"LADIES NIGHT"**: "ĐÊM QUÝ CÔ" (chunk 839) vs giữ nguyên (chunk 843).
- **"The Full Package"**: "Trọn Gói" (chunks 836/843).
- **"Hollow Earth Society of Leonida (Ltd)"**: dịch tên tổ chức (chunk 843) vs giữ nguyên tên tổ chức (tiền lệ "Thrillbilly Mud Club" giữ nguyên).
- **"Monster Man"**: "Người Quái Vật" (chunk 841) vs giữ nguyên tên (tiền lệ khác).
- **"Watcher"**: "Người Canh Gác" (chunk 841) vs giữ nguyên (tiền lệ khác).
- **"Auto Drive" / "closed captions" / "reticle" / "lock-on"**: dịch theo nghĩa mô tả ("Lái tự động", "phụ đề chi tiết", "tâm ngắm", "khóa mục tiêu") ở chunks 844/845 — nếu nên giữ nguyên tên tính năng thì cần sửa hàng loạt.

## Việc còn lại

- **P3 (dialogue còn lại): 354.707 chuỗi unique** — đã duyệt bulk, đang chạy theo waves 1.000, báo cáo mốc mỗi 5.000.
- Sau dịch: Phase 4 OCR prototype, Phase 5 Matching Engine, Phase 6 Overlay + Android TV app, Phase 7 Realtime Integration, Phase 8 Optimization (theo TDD).
