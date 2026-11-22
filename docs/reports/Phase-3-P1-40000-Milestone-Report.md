# P1 — Báo cáo mốc 40.000 chuỗi (2026-11-21)

## Tổng quan

- **P1 unique đã dịch: 40.979 / 45.380 (~90%)** — còn lại 4.401 chuỗi.
- Tổng số hàng bản dịch trong DB (origin `pipeline_muse`, status `machine`): **138.641 hàng = 138.641 source_id riêng biệt** (không trùng lặp).
- Wave 39 (chunks 771–780) nạp sạch: 1.000/1.000, **0 quarantined**.
- Toàn bộ P1 từ wave 1 đến wave 39: 39.000/39.000 nạp sạch, không có mục nào bị kẹt lại.

## Nội dung wave 36–39

- Wave 36–38: toàn bộ là bình luận mạng xã hội trong game (C1092).
- Wave 39 (chunks 771–779): C1092 xã hội; chunk 780 bắt đầu chuyển sang C1095–C1112 item/description/tutorial (18 mục cuối, gồm hướng dẫn bấm nút `~INPUT_ENTER~`).
- Wave 40 (chunks 781–790) đang dịch: C1112 item/description/tutorial + các nhóm Story S0056–S0593 (description/dialogue).

## Ghi chú chất lượng tích lũy (để rà soát sau, tất cả vẫn status `machine`)

- **Tiếng Tây Ban Nha**: đa số chunk giữ nguyên văn (code-switching), một số ít dịch sang tiếng Việt (chunks 625/626/638). Chưa thống nhất.
- **Chữ trong ảnh (Image Text:)**: đa số dịch sang tiếng Việt, gồm cả các khối chiêm tinh (LEO, TAURUS, CAPRICORN) và quảng cáo; một số chunk giữ nguyên tiếng Anh (652/683/700/709). Chưa thống nhất.
- **"pussy"**: hai nghĩa vẫn cùng tồn tại — nghĩa thô tục "lồn" (đa số) và nghĩa hèn nhát "đồ hèn" (chunks 703/735/757/767/770, theo tiền lệ P0 đã duyệt).
- **"bag"**: nghĩa tiền "túi tiền" là đa số (theo chunk 646/669/717); một số trường hợp rõ ràng không phải nghĩa tiền (chunk 764 "put the dick jokes in the bag" = cất đi).
- **"keys"**: mơ hồ dai dẳng — Florida Keys / ma túy "Keys" / chìa khóa xe (chunks 706/709/737/747/756/763/766/774).
- **"white boy" / "white girls"**: đa số đọc theo nghĩa đen (người da trắng), nhưng một số mục có thể là cocaine slang theo quy tắc P0 đã duyệt ở chunk 316 (chunks 757/758/770).
- **"wrap"**: mơ hồ — bọc xe hay bọc đồ ăn (chunks 702/714/741/751/762).
- **"hog"**: nghĩa mô-tô Harley "con xe" là đa số, nhưng có trường hợp đọc theo nghĩa đen là lợn (chunk 744) và trường hợp là tên riêng "Hank the Hog" (chunk 757).
- **"crabs"**: "rận mu" (theo chunk 697) vs cua theo nghĩa đen — chunk 767 dịch "CRAB FESTIVAL" là "Lễ Hội Cua" (đúng, là lễ hội cua thật).
- **"the Y / Y Hotel"**: vẫn chưa có đáp án thống nhất — "khách sạn Y" (chunk 736), giữ nguyên tên "Y Hotel" (chunks 642/671/676/685/695/780), hashtag #yhotel giữ nguyên.
- **"Erises" / "Eris"**: giữ nguyên loanword, chưa rõ là giày, thương hiệu hay thứ khác (chunks 740/745/758/760/766/768/772/777).
- **"FC"**: giữ nguyên loanword, chưa rõ là nhóm, câu lạc bộ hay nghĩa khác (chunks 741/770).
- **"8ball"**: chunk 750 dịch "bi số 8" (bi-a); chunk 771 lưu ý "smoke up an 8-ball" gần như chắc chắn là ma túy đá (3.5g cocaine) nhưng skeleton ép thành slot "{number} ball".
- **Slot-forced**: số trong từ lóng/leetspeak bị ép thành `{number}` — "Waiting 4 u" → "Đang chờ {number} mày" (741), "247 hot dog" → "{number} hot dog" (759), "pray 4 you" → "cầu nguyện {number} mày" (759), "sorry 4 ur loss" → "chia buồn {number} mất mát" (767). Theo skeleton, để rà soát sau.
- **Mất dấu %**: đã giữ dấu % theo tiền lệ chunk 333 ("{number}%") ở nhiều chunk (743/745/748/760/764); không còn mục mất % mới trong wave 36–39.
- **Lỗi gõ / typo nguồn được giữ nguyên trong bản dịch**: `~LIP_EMOJI_FIRE~` thiếu chữ B (chunk 758), "YEILD" (chunk 744), "fjks6.," gõ bừa bàn phím (chunk 760).
- **Chơi chữ bị mất trong bản dịch**: "HUGH JOHNSON CORE" (chunk 760), "Sir Cumference" (chunk 750), "cum/come" (chunk 761), "shore/sure" (chunk 779), "cumundrum" (chunk 766), "holesome" (chunk 753).
- **Tên loài Latin giữ nguyên**: "Sylvilagus palustris" (chunk 766) — trái với quy ước P0 là dịch tên loài ("thỏ đầm lầy").
- **"swimmin with the fishes"** dịch theo nghĩa đen "đi bơi với cá" (chunk 765) dù là thành ngữ mafia (bị giết, xác chìm xuống nước).

## Việc còn lại

- Wave 40–43 (4 wave đầy đủ 1.000) + wave 44 cuối (~401 chuỗi) → hoàn thành P1 (45.380).
- Báo cáo cuối P1 khi hoàn thành.
- Sau P1: P2 (lore, 1.937 dòng) và P3 (dialogue còn lại, 465.455 dòng) **chưa được duyệt** — cần hỏi người dùng.
