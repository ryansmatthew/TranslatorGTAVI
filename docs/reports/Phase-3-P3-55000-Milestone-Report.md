# Báo cáo cột mốc P3 — 55.000 chuỗi duy nhất

**Ngày:** 21/11/2026
**Tiến độ:** P3 **55.435 / 357.142** chuỗi duy nhất (15,5%). Còn lại **301.707** chuỗi.
**Tổng DB:** 232.201 bản dịch `pipeline_muse` = 232.201 `source_id` riêng biệt, không trùng lặp. Tất cả trạng thái `machine`.
**Waves:** 53 wave đã xong (chunks 846–1375). Wave 53 (chunks 1366–1375) nạp sạch 1.000/1.000, 0 bị cách ly.

## Nội dung đã dịch (waves 49–53)

- **Wave 49** (chunks 1326–1335): C0138–C0141 — NPC đường phố C0138, AAVE C0139/C0140, NPC đường phố C0141, bark đối chất C0141.
- **Wave 50** (chunks 1336–1345): C0141–C0145 — AAVE/đường phố + diss track C0141, NPC giàu/chanh chua C0142, khách du lịch C0143, AAVE/nữ C0144, Spanglish C0145 đầu.
- **Wave 51** (chunks 1346–1355): C0145–C0148 — Spanglish/Cuba C0145, NPC nữ C0146, AAVE/đường phố + diss track + G. Riverz C0147, Karen/bảo thủ C0148 đầu.
- **Wave 52** (chunks 1356–1365): C0148–C0151 — Karen/bảo thủ/khu ngoại ô C0148, AAVE/đường phố C0149, NPC influencer/guru hustle C0150, NPC giàu/chanh chua xen Spanglish C0151.
- **Wave 53** (chunks 1366–1375): C0151–C0154 — NPC giàu/Spanglish C0151, **cảnh sát/radio cảnh sát C0152–C0154** (truy đuổi, ra lệnh, báo cáo qua radio, trò đùa "furry" xuyên suốt các chunk C0152/C0153).

## Sự cố (đã xử lý, không còn tồn đọng)

- Không có sự cố nghiêm trọng ở waves 49–53. Tất cả 10 handoff của mỗi wave đều về trước khi nạp; không wave nào phải dùng tiền lệ "handoff trễ".
- Không có chunk nào bị lỗi giới hạn token đầu ra (dialogue ngắn nên không gặp).

## Ghi chú chất lượng (tất cả đang ở trạng thái `machine`, rà soát sau)

- **Cảnh sát C0152–C0154 (wave 53) — quy tắc xưng hô mới:** radio/báo cáo với trung tâm dùng giọng "tôi" chuyên nghiệp ("Trung tâm, tôi đang tới."); quát nghi phạm dùng "tao/mày" hoặc mệnh lệnh trực tiếp; câu lịch sự với dân thường dùng "tôi/anh/bà". Câu gọi cảnh sát giữ "tôi" khi lịch sự, giữ "tao" khi nhân vật đang dọa dẫm/thách thức (C0149_BE9AB76D, C0150_0DCBDE00 là hai phía).
- **"Dispatch" → "trung tâm điều phối"** đã thống nhất xuyên suốt các chunk cảnh sát (tiền lệ P0).
- **"PIT" giữ nguyên** — chưa thống nhất với phía "húc xoay" (chunk 1367 "Đang áp sát nghi phạm để húc PIT ngay!", chunk 1370 "cú PIT không hiệu quả", chunk 1373 "PIT thất bại"); cần một quyết định thống nhất sau.
- **"officer down"** — ba cách: "cảnh sát bị hạ" (chunk 1368), "cảnh sát gục rồi" (chunks 1369, 1372, 1373), "có cảnh sát gục rồi" (chunk 1372) — chết hay bị thương vẫn chưa chốt; "gục" được dùng để bao cả hai nghĩa.
- **"That's Negative." / "negative"** — phía đa số "phủ định" (chunk 1371) vs "Không phải." (chunk 876, chunk 1374 "It's a negative" → "Không phải"); "negative mindset" → "tư duy tiêu cực" là nghĩa khác, không phải phủ định radio (chunk 1374).
- **"furry"** — giữ loanword xuyên suốt, kể cả trong các chunk cảnh sát ("Paw above your furry little head!" → "Giơ chân lên khỏi cái đầu lông lá nhỏ của mày!", chunk 1368; "Got you, you furry little bitch!" → "Tóm được mày rồi, con đĩ furry nhỏ!", chunk 1371; "furry vehicle" → "xe phủ lông" vs "xe furry", chunks 1373/1374 — hai phía).
- **"Shocker"** — đọc là súng chích điện (taser), cùng nhóm với "stun gun" → "súng điện" (chunks 1369, 1371, 1374, 1375); nếu là tên người/biệt danh thì cần sửa.
- **"get down" vẫn ba phía:** "nằm xuống" (đa số, dùng khi không có ngữ cảnh xe/chỗ cao — chunks 1356, 1362, 1367, 1369, 1375) vs "xuống khỏi đó" (khi ngữ cảnh là xe/vật/chỗ cao) vs "quẩy" (nghĩa tiệc tùng/làm tình, chunk 1335) — phân biệt theo ngữ cảnh từng câu.
- **"on God":** dịch "thề với Chúa" (đa số, chunks 1352) vs giữ loanword (chunks 1245, 1274) — vẫn chưa thống nhất.
- **"lowkey":** "ngầm" (chunks 1266, 1332, 1352, 1358) vs "thật ra" (chunk 1267) vs "hơi" (chunk 1330, "lowkey rude" → "hơi thô lỗ") — chưa thống nhất.
- **"trippin'":** "phê" là phía mặc định P3 (chunks 1354, 1358, 1359) vs "nổi điên/bận tâm" khi ngữ cảnh là khó chịu (chunks 1317, 1335, 1358 "trippin' off you" → "chẳng thèm để ý tới mày") vs "đừng lo" trong "Don't even trip" (chunks 1247, 1290, 1359) — phân biệt theo ngữ cảnh, chưa thống nhất tuyệt đối.
- **"fuck with":** nghĩa "đụng tới" (mess with) đã thống nhất xuyên suốt ("Don't fuck with my bros" → "Đừng có đụng tới mấy thằng bro của tao"); nghĩa "thích/chơi cùng" chỉ dùng khi ngữ cảnh rõ ("Fuck with me!" → "Chơi với tao này!", chunk 1340; "we don't fuck with strangers" → "bọn tao không chơi với người lạ đâu", chunk 1353; "had to come fuck with ya boy again" → "tới chơi với thằng bạn tao", chunk 1358).
- **"pussy":** nghĩa hèn nhát ("đồ hèn") là mặc định theo quy tắc P0 (hầu hết các chunk); nghĩa tục ("lồn") chỉ dùng khi ngữ cảnh rõ là tình dục (C0148_CBC5D673, "pure white Christian pussy" → "cái lồn da trắng Cơ đốc thuần khiết", chunk 1357; C0144_EFA7B3F2, chunk 1345). Cả hai nghĩa đều xuất hiện trong cùng wave — quyết định theo ngữ cảnh từng câu.
- **"go fuck yourself!":** ba phía — thô trực tiếp "đi mà tự đụ đi" (đa số, chunks 1347, 1350, 1366 "literally fuck yourself" → "tự địt mình đi") vs mềm "Đi mà tự sướng đi!" (chunks 932, 943, 968, 1004) vs trung lập — **đang chờ quyết định của người dùng** (đã trình bày, chưa trả lời).
- **"call it":** phía kết thúc vụ ("tao dừng đây", "tao quyết định", chunks 1258, 1273, 1313, 1328, 1354 "dừng vụ này ở đây") vs "đoán" (chunk 1073) vs "chốt" (chunk 1086) — phân biệt theo ngữ cảnh.
- **"I got you":** phía trấn an ("tao lo cho mày", chunks 1358, 1359, 1360) vs phía bắt được ("tao tóm được mày rồi" / "Tóm được mày rồi", chunks 1329, 1371, 1373, 1375) vs nhượng bộ ("mày thắng rồi", chunk 1072; "I'll let you have that" → "tôi sẽ nhường anh vụ này", chunk 1375) — phân biệt theo ngữ cảnh.
- **"get fucked up":** phía "bị xử/đánh" đã thống nhất ("You got fucked up!" → "Mày bị xử rồi!") vs nghĩa "phê thuốc" — phân biệt theo ngữ cảnh.
- **"get off":** "xuống khỏi người tao đi" (đa số, khi có người/vật) vs "xuống khỏi đó đi" (khi không rõ vật) vs "cút đi" (khi không có ngữ cảnh xe/vật, chunks 1351, 1360, 1361) — phân biệt theo ngữ cảnh.
- **"liberal" / "deep state" / "libtard":** "liberal" → "cánh tả" đã thống nhất xuyên suốt; "deep state" → "nhà nước ngầm" (tiền lệ chunk 1225); "libtard" giữ nguyên loanword (chunks 1356, 1357); "libs" → "bọn cánh tả" (chunk 1356) vs "lũ lib" (chunk 1357) — chưa thống nhất.
- **"In Spanish:" → "Nói tiếng Tây Ban Nha:" + nội dung dịch** xuyên suốt (chunks 1346–1350, 1364–1367, 1369, 1370); tiếng Tây Ban Nha giữ nguyên: "Coño", "chamo", "mi pana", "panita", "marica", "careverga", "¡Oye!", "Mira", "¿Hola?", "Cálmate", "Muchas gracias", "adiós", "¡Por favor!", "¿Qué?", "Si, si...", "¿Sabés qué?", "'Mor", "mami", "jueputa", "hijueputa", "bombon", "perico", "cocodrilo".
- **"AudaCity" giữ nguyên tên** (chunks 1365, 1366 — chơi chữ với "audacity").
- **"Motivation Mechanics" giữ nguyên tên khóa học/series** (chunks 1361–1364, "Motivation Mechanics 104" → "Cơ Chế Động Lực {number}").
- **Số không có slot giữ dạng chữ:** "ten million" → "mười triệu", "five-thousand dollar" → "năm nghìn đô", "forty-two percent" → "bốn mươi hai phần trăm" (chunk 1361); "two seconds" → "hai giây", "fifty thousand dollar" → "năm mươi nghìn đô" (chunk 1363).
- **"871" / "284" / "367" → "{number}"** xuyên suốt các chunk cảnh sát (số hiệu đơn vị radio); "911" → "{number}" xuyên suốt; "556" → "{number}" trong "Duke 556" (chunk 1357).
- **"cougar":** ba cách dịch vẫn chưa thống nhất — "máy bay bà già" (chunks 1269, 1272) vs "con báo già" (chunk 1271) vs "con cọp già" (chunk 1270).
- **"VC":** giữ loanword xuyên suốt (Vice City vs voice chat vẫn chưa chốt; "I'm the king of VC!" → "Tao là vua của VC đấy!", chunk 1363).
- **"FYI":** giữ loanword (đa số) vs dịch "cho mày biết" (chunk 1209) — chưa thống nhất.
- **"gaslight":** giữ loanword (chunks 1243, 1333) vs dịch "thao túng" (chunks 1244, 1332) — chưa thống nhất.
- **"daddy":** dịch "bố" (đa số P3) vs giữ loanword (chunk 1333, "my daddy is buying me a new Gallivanter") — chưa thống nhất.
- **"Sagittarius" → "Nhân Mã"** (chunk 1331) vs **"Scorpio" giữ nguyên** (chunks 1299, 1325, 1331) — cung hoàng đạo dịch/giữ không thống nhất.
- **"woe" → "cưng"** (tiền lệ chunk 1345, dùng lại ở chunk 1360 "How you been, woe?" → "Mày dạo này thế nào, cưng?").
- **"the ick" → "cái ick"** (tiền lệ chunk 1323, dùng lại ở chunk 1363); **"E-fucking-nough" → "Đủ mẹ rồi đấy"** (tiền lệ chunk 1322, dùng lại ở chunk 1363).
- **"collisionable" giữ nguyên** — từ bịa của guru, không dịch (chunk 1363).
- **Lỗi gốc được giữ/dịch theo ý định:** "Krav Magra" (sai chính tả của Krav Maga) và "Muy Thai" (sai chính tả của Muay Thai) giữ nguyên như gốc (chunks 1338, 1341); "what's gonna on" (chunk 1359); "beven" đọc là lỗi gõ của "been" (chunk 1360); "greven" đọc là biến thể của "grieving" (chunk 1360); "Hol' up, what's that/" giữ dạng dở dang như gốc (chunk 1359).

## Bước tiếp theo

- Wave 54 (chunks 1376–1385, C0154 trở đi) đang dịch.
- Cột mốc tiếp theo: **60.000** (dự kiến wave 58).
- Hoàn thành P3 khi đạt 357.142/357.142; sau đó là báo cáo tổng kết P3 và Phase 4 (OCR prototype).
