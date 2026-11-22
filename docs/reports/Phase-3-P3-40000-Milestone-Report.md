# Báo cáo cột mốc P3 — 40.000 chuỗi duy nhất

**Ngày:** 21/11/2026
**Tiến độ:** P3 **40.435 / 357.142** chuỗi duy nhất (11,3%). Còn lại **316.707** chuỗi.
**Tổng DB:** 213.075 bản dịch `pipeline_muse` = 213.075 `source_id` riêng biệt, không trùng lặp. Tất cả trạng thái `machine`.
**Waves:** 38 wave đã xong (chunks 846–1225). Wave 38 (chunks 1216–1225) nạp sạch 1.000/1.000, 0 bị cách ly.

## Nội dung đã dịch (waves 34–38)

- **Wave 34** (chunks 1176–1185): C0085–C0088 — influencer/sugar daddy, dân thường, AAVE roast, bar/say rượu.
- **Wave 35** (chunks 1186–1195): C0088–C0091 — bar/say rượu, trailer-park, Spanglish C0090, nữ giàu có chanh chua C0091.
- **Wave 36** (chunks 1196–1205): C0091–C0094 — nữ giàu có, AAVE C0092, Spanglish C0093, gym rat/influencer C0094.
- **Wave 37** (chunks 1206–1215): C0094–C0098 — gym/wellness, valley girl C0095, "Papi Long Dick" C0096, nữ AAVE C0097, sneakerhead C0098.
- **Wave 38** (chunks 1216–1225): C0098–C0101 — sneakerhead/fit C0098, AAVE C0099, dân giàu/thượng lưu C0100, Karen bảo thủ/chính trị C0101.

## Sự cố (đã xử lý, không còn tồn đọng)

- Không có sự cố nghiêm trọng ở waves 34–38. Lỗi duy nhất: chunk 1190 (wave 35) bản nháp hoán đổi id ở idx 3/4, agent tự sửa trước khi nạp.
- Không có chunk nào bị lỗi giới hạn token đầu ra (lore P2 đã hết; dialogue ngắn nên không gặp).

## Ghi chú chất lượng (tất cả đang ở trạng thái `machine`, rà soát sau)

- **"get down" ba phía vẫn chưa thống nhất:** "nằm xuống" (đa số, dùng khi không có ngữ cảnh xe/chỗ cao) vs "xuống khỏi đó" (khi ngữ cảnh là xe/nắp ca-pô/chỗ cao, ví dụ chunk 1204, 1218, 1220) vs "quẩy" (ít dùng ở P3). Các chunk mới tiếp tục chọn theo ngữ cảnh từng câu.
- **"Papi Long Dick":** giữ nguyên tên ở hầu hết các chunk (1210, 1211, 1212), nhưng chunk 1209 dịch thành "Papi Cu Dài" — lệch duy nhất, cần thống nhất sau (khuyến nghị giữ nguyên tên).
- **"VC":** giữ loanword xuyên suốt (Vice City vs voice chat vẫn chưa chốt).
- **"liberal" / "libtard" / "libs":** "liberal" → "cánh tả" (đa số, chunk 1224/1225), "libtard" giữ loanword ở chunk 1225 nhưng dịch "thằng tự do ngu" ở chunk 1224 — chưa thống nhất; "libs" → "bọn lib" (chunk 1223).
- **"FYI":** dịch "cho mày biết" (chunk 1209) vs giữ loanword (đa số trước đây) — chưa thống nhất.
- **"pussy":** nghĩa hèn nhát ("đồ hèn") là mặc định theo quy tắc P0; nghĩa tục ("lồn") chỉ dùng khi ngữ cảnh rõ ràng là tình dục (ví dụ C0096_85092AE1). Cả hai nghĩa đều xuất hiện trong cùng một chunk ở wave 37 — quyết định theo ngữ cảnh từng câu.
- **"trippin'" / "on one" / "off it":** mặc định đọc "đang phê" theo tiền lệ P3; nghĩa "ảo tưởng/bận tâm" chỉ dùng khi ngữ cảnh rõ (ví dụ "We ain't tripping on you" → "không để ý tới mày").
- **"body count":** đọc là số bạn tình theo tiền lệ P2/P3 (chunks 1210–1212); nghĩa số người đã giết chỉ dùng khi ngữ cảnh rõ là bạo lực.
- **Giọng "tôi" lịch sự:** các câu gọi cảnh sát/phục vụ (ví dụ C0097_DAC5F52C, C0100_43F08145, C0101_A85D3C8E) dịch bằng "tôi" thay vì "tao/mày" — quyết định theo ngữ cảnh, có chủ đích.
- **"deep state":** dịch "nhà nước ngầm" (chunk 1225) vs giữ loanword (chunk 1224) — chưa thống nhất.
- **Số giữ nguyên chữ:** khi skeleton không có slot, số viết bằng chữ được giữ nguyên ("six patrol cars" → "sáu xe tuần tra", "four-hundred subscribers" → "bốn trăm người theo dõi", "Four-percent brain" → "não bốn phần trăm").

## Bước tiếp theo

- Wave 39 (chunks 1226–1235, C0101 trở đi) đang dịch.
- Cột mốc tiếp theo: **45.000** (dự kiến wave 43).
- Hoàn thành P3 khi đạt 357.142/357.142; sau đó là báo cáo tổng kết P3 và Phase 4 (OCR prototype).
