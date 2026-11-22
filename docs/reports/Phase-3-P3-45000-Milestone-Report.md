# Báo cáo cột mốc P3 — 45.000 chuỗi duy nhất

**Ngày:** 21/11/2026
**Tiến độ:** P3 **45.435 / 357.142** chuỗi duy nhất (12,7%). Còn lại **311.707** chuỗi.
**Tổng DB:** 219.476 bản dịch `pipeline_muse` = 219.476 `source_id` riêng biệt, không trùng lặp. Tất cả trạng thái `machine`.
**Waves:** 43 wave đã xong (chunks 846–1275). Wave 43 (chunks 1266–1275) nạp sạch 1.000/1.000, 0 bị cách ly.

## Nội dung đã dịch (waves 39–43)

- **Wave 39** (chunks 1226–1235): C0101–C0105 — Karen bảo thủ, realtor C0102, du khách Midwest C0103, Spanglish/Balsero C0104, valley girl C0105.
- **Wave 40** (chunks 1236–1245): C0105–C0109 — valley girl C0105, party C0106, Spanglish C0107, Gen Z C0108, AAVE C0109.
- **Wave 41** (chunks 1246–1255): C0109–C0112 — AAVE C0109/C0111, đầm lầy/redneck C0110, frat boy C0112.
- **Wave 42** (chunks 1256–1265): C0112–C0115 — frat-bro C0112, bro/bóng rổ C0113, nhân viên cửa hàng/tài xế RydeMe C0114, cửa hàng thời trang xa xỉ C0115.
- **Wave 43** (chunks 1266–1275): C0115–C0119 — cửa hàng xa xỉ C0115, nhân viên bị cướp C0116, phụ nữ lớn tuổi/cougar/trailer park C0117, Spanglish/Cuba C0118, NPC tán tỉnh/tiệc tùng C0119.

## Sự cố (đã xử lý, không còn tồn đọng)

- Không có sự cố nghiêm trọng ở waves 39–43. Lỗi duy nhất: chunk 1262 (wave 42) bản nháp thiếu 1 mục ở idx 70 (C0114_C42B564D), agent tự chèn lại và kiểm tra 100/100 trước khi nạp.
- Không có chunk nào bị lỗi giới hạn token đầu ra (lore P2 đã hết; dialogue ngắn nên không gặp).

## Ghi chú chất lượng (tất cả đang ở trạng thái `machine`, rà soát sau)

- **"get down" ba phía vẫn chưa thống nhất:** "nằm xuống" (đa số, dùng khi không có ngữ cảnh xe/chỗ cao) vs "xuống khỏi đó" (khi ngữ cảnh là xe/vật/chỗ cao, ví dụ chunk 1260, 1261, 1262, 1265) vs "quẩy" (ít dùng ở P3) — cộng thêm nghĩa "lifestyle" ("get down like that" → "chơi kiểu đó", chunk 1240) và "xuống khỏi đó" theo phía xuống khỏi xe ("off the car" → "xuống khỏi xe đi", chunk 1275). Các chunk mới tiếp tục chọn theo ngữ cảnh từng câu.
- **"In Spanish:" vs "In Creole:":** chunk 1245 (wave 40) dịch nhầm 4 cue "In Spanish:" thành "Nói tiếng Creole:" — lỗi thật, cần sửa ở đợt rà soát. Ngược lại, các cue "In Creole:" thật trong C0109/C0111 (chunks 1246/1247/1252/1253) được dịch đúng "Nói tiếng Creole:". Waves 42–43 không còn cue "In Spanish:"/Creole bị nhầm.
- **"cougar":** ba cách dịch trong wave 43 — "máy bay bà già" (chunks 1269, 1272) vs "con báo già" (chunk 1271, "this cougar's got a cub to meet up with" → "con báo già này có một thằng nhóc để gặp") vs "con cọp già" (chunk 1270, "cougar's on the prowl" → "Con cọp già này đang đi săn mồi đây") — chưa thống nhất.
- **"man meat":** "trai đẹp" (chunk 1271, "How you doin' man meat?") vs "mấy thằng trai trẻ ngon nghẻ" (chunk 1271, "young man meat") — chưa thống nhất.
- **"hot flash" / "menopause":** "cơn bốc hỏa" / "mãn kinh" đã thống nhất xuyên suốt C0117 ("Don't fuck with menopause, bitch!" → "Đừng có đùa với thời kỳ mãn kinh, con đĩ!", chunk 1270).
- **"trailer trash" / "trailer park":** "rác rưởi khu nhà di động" / "khu nhà di động" (chunk 1269); "trailer" → "nhà di động" — đã thống nhất trong wave 43.
- **"on God":** dịch "thề với Chúa" (chunk 1273, theo phía chunk 1243) vs giữ loanword (chunk 1274, "You better answer me, on God" → "Mày tốt nhất nên trả lời tao, on God"; chunk 1245 giữ loanword) — vẫn chưa thống nhất.
- **"get fucked up":** phía "bị xử/đánh" đã thống nhất trong wave 42 ("You 'bout to get fucked up!" → "Mày sắp bị xử đẹp đấy!", chunk 1261, theo tiền lệ chunk 1197) vs nghĩa "phê thuốc" — phân biệt theo ngữ cảnh.
- **"I'm outtie" → "tao chuồn đây"** (chunk 1256, theo tiền lệ chunk 1254); **"bounce"/"dip"/"slide" → "chuồn"** (chunk 1268); **"I'm out" → "tao chuồn đây"** (C0114) vs **"tôi chuồn đây"** (C0115, giọng lịch sự) — phân biệt theo giọng nhân vật.
- **Giọng "tôi" lịch sự:** các câu gọi cảnh sát/phục vụ trong C0115/C0116 (ví dụ C0115_F1641297, C0116_23759C75, C0115_9FDE6ED5, C0116_58D2D531, C0117_10E4063E) dịch bằng "tôi" thay vì "tao/mày" — có chủ đích, theo ngữ cảnh. Ngoại lệ: câu gọi cảnh sát C0117_C0D4757B giữ giọng "tao/mày" chửi thề vì nhân vật đang chửi; câu C0116_D7AEB067 dùng giọng trung lập không đại từ.
- **Spanglish giữ nguyên:** "puta", "mami", "Adios", "Pa la pinga", "Coño", "Jesucristo", "Oye", "Bueno", "vamos", "nada", "pito", "comemierda", "anormal", "socio", "De pinga!", "abuelita", "mi amorcito" giữ loanword tiếng Tây Ban Nha; "In Spanish:" → "Nói tiếng Tây Ban Nha:" + nội dung dịch (11 mục/chunk ở C0118).
- **"fuck with":** nghĩa "đụng tới" (mess with) đã thống nhất xuyên suốt waves 42–43 ("Don't fuck with my bros" → "Đừng có đụng tới mấy thằng bro của tao"; "You wanna fuck with my homies? Fuck with me." → "Mày muốn đụng tới mấy thằng anh em của tao à? Đụng tới tao này.").
- **"pussy":** nghĩa hèn nhát ("đồ hèn") là mặc định theo quy tắc P0 (C0112_D23F926A, C0113_3E0EDD77, C0118_4761592D, C0118_5FF115AD); nghĩa tục ("lồn") chỉ dùng khi ngữ cảnh rõ là tình dục (C0117_76BF3DD3, "You can eat my pussy on a hot summer's day!"). Cả hai nghĩa đều xuất hiện trong cùng wave — quyết định theo ngữ cảnh từng câu.
- **"call it":** phía kết thúc vụ ("tao dừng đây", chunk 1258, theo tiền lệ 1228/1240) vs "đoán" (chunk 1073) vs "dừng ở đây" (chunk 1273, "call it quits") — phân biệt theo ngữ cảnh.
- **"No-Cap Captain":** dịch theo nghĩa "Đội trưởng Không-Nói-Dóc" (chunk 1268) — nếu nên giữ nguyên tên thì cần sửa ở đợt rà soát.
- **"You're telling me"** trong cue "In Spanish:" (chunk 1272, C0118_0B53D604) được dịch theo nghĩa đen ("Mày nói với tao đấy à.") thay vì thành ngữ đồng tình ("mày nói đúng đấy") — cần xem lại.
- **Lỗi gốc được giữ/dịch theo ý định:** "lighting" thay vì "lightning" (chunk 1261, giữ nghĩa đen "bị sét đánh"); "I though were you" (chunk 1259); "iIne" thay vì "Fine!" (chunk 1263); "your" thay vì "you're" (chunk 1270, C0117_567D11FB); "awayfrom" viết dính (chunk 1266, C0116_1E6C2D56); "injured reserved" thay vì "injured reserve" (chunk 1259); "What you you want" thừa "you" (chunk 1272) — giữ dạng lặp như gốc.
- **"911" → "{number}"** xuyên suốt (chunks 1256, 1265, 1266, 1270, 1274); **"100%" → "{number}%"** giữ dấu % theo tiền lệ chunk 333 (chunk 1257).
- **"VC":** giữ loanword xuyên suốt (Vice City vs voice chat vẫn chưa chốt).
- **"FYI":** dịch "cho mày biết" (chunk 1209) vs giữ loanword (đa số) — chưa thống nhất.

## Bước tiếp theo

- Wave 44 (chunks 1276–1285, C0119 trở đi) đang dịch.
- Cột mốc tiếp theo: **50.000** (dự kiến wave 48).
- Hoàn thành P3 khi đạt 357.142/357.142; sau đó là báo cáo tổng kết P3 và Phase 4 (OCR prototype).
