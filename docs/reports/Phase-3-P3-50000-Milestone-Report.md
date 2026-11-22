# Báo cáo cột mốc P3 — 50.000 chuỗi duy nhất

**Ngày:** 21/11/2026
**Tiến độ:** P3 **50.435 / 357.142** chuỗi duy nhất (14,1%). Còn lại **306.707** chuỗi.
**Tổng DB:** 225.941 bản dịch `pipeline_muse` = 225.941 `source_id` riêng biệt, không trùng lặp. Tất cả trạng thái `machine`.
**Waves:** 48 wave đã xong (chunks 846–1325). Wave 48 (chunks 1316–1325) nạp sạch 1.000/1.000, 0 bị cách ly.

## Nội dung đã dịch (waves 44–48)

- **Wave 44** (chunks 1276–1285): C0119–C0123 — NPC tiệc tùng/tán tỉnh C0119, AAVE C0120/C0121, NPC đường phố C0121, phụ nữ giàu C0122, nhân viên quán/shop C0123.
- **Wave 45** (chunks 1286–1295): C0123–C0126 — nhân viên quán/shop C0123, NPC giàu/hustle-mindset C0124, Spanglish/Cuba C0125, Gen Z/streamer + NPC đường phố C0126.
- **Wave 46** (chunks 1296–1305): C0126–C0130 — NPC đường phố C0126, AAVE/nữ C0127, NPC đường phố C0128, alpha/beta bro C0129, C0130.
- **Wave 47** (chunks 1306–1315): C0130–C0134 — NPC sợ hãi/xin tha C0130, bark đối chất C0131, NPC thuyết âm mưu/yêu nước C0132, NPC giàu/khoe tiền C0133, C0134.
- **Wave 48** (chunks 1316–1325): C0134–C0138 — NPC đối chất C0134, bark đường phố C0135, NPC khách sạn/đường phố C0136, Gen Z/valley girl C0137, C0138.

## Sự cố (đã xử lý, không còn tồn đọng)

- Không có sự cố nghiêm trọng ở waves 44–48. Ba wave dùng tiền lệ "handoff trễ": chunk 1298 (wave 46), chunk 1312 (wave 47) và chunk 1319 (wave 48) chưa có handoff khi 9 chunk còn lại đã xong, nhưng file đầu ra đã có trên đĩa và qua kiểm tra cấu trúc (100/100, id đúng thứ tự, 0 trùng kề) + spot-check (idx 0/49/99 khớp), nên wave được nạp theo tiền lệ; ghi chú chi tiết được bổ sung sau khi handoff tới.
- Không có chunk nào bị lỗi giới hạn token đầu ra (dialogue ngắn nên không gặp).

## Ghi chú chất lượng (tất cả đang ở trạng thái `machine`, rà soát sau)

- **"get down" vẫn ba phía:** "nằm xuống" (đa số, dùng khi không có ngữ cảnh xe/chỗ cao) vs "xuống khỏi đó" (khi ngữ cảnh là xe/vật/chỗ cao, ví dụ chunk 1299, 1302, 1310, 1317) vs "quẩy" (chunk 1277 "getting down" → "làm tình" theo nghĩa tình dục đồng thuận; chunk 1335 "how we get down in rebel-fuckin-country" → "quẩy") — cộng thêm nghĩa "cúi xuống" và "xuống khỏi xe" ("off the car" → "xuống khỏi xe đi", chunk 1288). Các chunk mới tiếp tục chọn theo ngữ cảnh từng câu.
- **"on God":** dịch "thề với Chúa" (đa số, theo phía chunk 1243 — chunks 1279, 1280, 1281, 1297, 1300, 1313, 1318, 1323) vs giữ loanword (chunks 1245, 1274) — vẫn chưa thống nhất.
- **"lowkey":** ba phía trong waves 44–48 — "ngầm" (chunk 1266) vs "thật ra" (chunk 1267) vs "hơi" (chunk 1330, "lowkey rude" → "hơi thô lỗ") — chưa thống nhất.
- **"trippin'":** "phê" là phía mặc định P3 (chunks 1290, 1299, 1301, 1314) vs "nổi điên/bận tâm" khi ngữ cảnh là khó chịu (chunks 1289, 1317, 1324, 1334 "trippin' off you" → "chẳng thèm để ý tới mày") vs "đừng lo" trong "Don't even trip" (chunks 1247, 1290) — phân biệt theo ngữ cảnh, chưa thống nhất tuyệt đối.
- **"fuck with":** nghĩa "đụng tới" (mess with) đã thống nhất xuyên suốt waves 44–48 ("Don't fuck with my bros" → "Đừng có đụng tới mấy thằng bro của tao"); nghĩa "thích/chơi cùng" chỉ dùng khi ngữ cảnh rõ ("you can fuck with us if you're in our tax bracket" → "chơi với", chunk 1314; "only I'm allowed to fuck with my friends like that" → "đùa giỡn với bạn tao", chunk 1315).
- **"pussy":** nghĩa hèn nhát ("đồ hèn") là mặc định theo quy tắc P0 (hầu hết các chunk); nghĩa tục ("lồn") chỉ dùng khi ngữ cảnh rõ là tình dục (C0124_634EC1E5, "act like that pussy worth somethin'" → "cư xử như thể cái lồn của mày đáng giá gì đó", chunk 1289). Cả hai nghĩa đều xuất hiện trong cùng wave — quyết định theo ngữ cảnh từng câu.
- **"go fuck yourself!":** ba phía — thô trực tiếp "đi mà tự đụ đi" (đa số, chunks 1291, 1295, 1296) vs mềm "Đi mà tự sướng đi!" (chunks 932, 943, 968, 1004) vs trung lập — chưa thống nhất.
- **"call it":** phía kết thúc vụ ("tao dừng đây", "tao quyết định", chunks 1258, 1273, 1313, 1328) vs "đoán" (chunk 1073) vs "chốt" (chunk 1086) — phân biệt theo ngữ cảnh.
- **"I got you":** phía trấn an ("tao lo cho mày", chunks 1294, 1306, 1309, 1321) vs phía bắt được ("tao tóm được mày rồi", chunk 1329, "I got you now") vs nhượng bộ ("mày thắng rồi", chunk 1072) — phân biệt theo ngữ cảnh.
- **"get fucked up":** phía "bị xử/đánh" đã thống nhất trong waves 44–48 ("You got fucked up!" → "Mày bị xử rồi!", chunk 1287; "Almost got fucked up..." → "Suýt nữa thì bị xử rồi...", chunk 1300) vs nghĩa "phê thuốc" — phân biệt theo ngữ cảnh.
- **"get off":** "xuống khỏi người tao đi" (đa số, khi có người/vật) vs "xuống khỏi đó đi" (khi không rõ vật) vs "cút đi" (khi không có ngữ cảnh xe/vật, ví dụ chunk 1297 C0127_209724E6) — phân biệt theo ngữ cảnh.
- **Giọng "tôi" lịch sự:** các câu gọi cảnh sát/phục vụ dịch bằng "tôi" thay vì "tao/mày" — có chủ đích, theo ngữ cảnh (C0124, C0126_EBB63767, C0132_9BD81B7A, C0134_4C4CA1D5, C0138_28AFDB1B, C0138_EAAEEC6B, C0139_AB6D497D, C0140_A2D45398). Ngoại lệ: câu gọi cảnh sát giữ giọng "tao/mày" chửi thề khi nhân vật đang dọa dẫm/thách thức (C0125_9D6F5BC8, C0125_AA2C3B25, C0130_B524F1D0, C0132_97EBCE40, C0135_71F320E6, C0138_828A2D21, C0139_58E3535F).
- **"liberal" / "deep state" / "sheep":** "cánh tả" đã thống nhất xuyên suốt waves 47–48 ("liberal media" → "truyền thông cánh tả", "liberal elites" → "tinh hoa cánh tả"); "deep state"/"deepstate" → "nhà nước ngầm" (theo tiền lệ chunk 1225); "sheep" → "lũ cừu" (chửi chính trị, chunks 1304, 1312).
- **"It's giving..." → "Nó toát lên vẻ..."** đã thống nhất xuyên suốt (chunks 1287, 1299, 1323, 1324, 1325); **"serving X"** dịch theo cùng phía ("serving deranged axe murderer" → "đang toát lên vẻ kẻ sát nhân cầm rìu điên loạn", chunk 1332).
- **"In Spanish:" → "Nói tiếng Tây Ban Nha:" + nội dung dịch** xuyên suốt (chunks 1286, 1287, 1291, 1292, 1293, 1320, 1321, 1322); tiếng Tây Ban Nha giữ nguyên: "Oye", "Coño", "Dios mio", "Si", "Dale", "Adiós", "Hola", "Lo siento", "Por favor", "pupusas", "Pipo", "punto".
- **"cougar":** ba cách dịch từ wave 43 vẫn chưa thống nhất — "máy bay bà già" (chunks 1269, 1272) vs "con báo già" (chunk 1271) vs "con cọp già" (chunk 1270).
- **"VC":** giữ loanword xuyên suốt (Vice City vs voice chat vẫn chưa chốt).
- **"FYI":** giữ loanword (đa số) vs dịch "cho mày biết" (chunk 1209) — chưa thống nhất.
- **"gaslight":** giữ loanword (chunk 1243) vs dịch "thao túng" (chunk 1244) — chưa thống nhất.
- **"daddy":** dịch "bố" (đa số P3, ví dụ "My daddy is a prosecutor" → "Bố tao là công tố viên", chunk 1332) vs giữ loanword (chunk 1333, "my daddy is buying me a new Gallivanter") — chưa thống nhất.
- **"Sagittarius" → "Nhân Mã"** (chunk 1331) vs **"Scorpio" giữ nguyên** (chunks 1299, 1325, 1331) — cung hoàng đạo dịch/giữ không thống nhất.
- **"911" → "{number}"** xuyên suốt; **"1-800-Got-Hands" → "{number}-{number}-Got-Hands"** (chunk 1325); **"431,512" follower → "{number}"** (chunk 1333); **"Civility 101" → "Phép lịch sự {number}"** (chunk 1333).
- **Lỗi gốc được giữ/dịch theo ý định:** "you to psycho" (chunk 1287); "aal" thay vì "all" (chunks 1294, 1328); "Okaywho" viết dính (chunk 1294); "I need You need to back up" thừa "need" (chunk 1294); "being a prison" thay vì "being in prison" (chunk 1294); "Bitchm" thiếu dấu phẩy (chunk 1309); "Wel,l" lỗi gõ (chunk 1311); "first off all" thiếu "of" (chunk 1326); "Noot" thay vì "Not", "Hold onm" thay vì "Hold on" (chunk 1318); "like me like" lặp từ (chunk 1318); "what're, you" thừa dấu phẩy (chunk 1305) — giữ dạng dở dang như gốc.

## Bước tiếp theo

- Wave 49 (chunks 1326–1335, C0138 trở đi) đang dịch.
- Cột mốc tiếp theo: **55.000** (dự kiến wave 53).
- Hoàn thành P3 khi đạt 357.142/357.142; sau đó là báo cáo tổng kết P3 và Phase 4 (OCR prototype).
