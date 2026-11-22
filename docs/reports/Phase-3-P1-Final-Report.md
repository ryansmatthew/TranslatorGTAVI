# Phase 3 — Báo cáo cuối P1 (2026-11-21)

## Kết quả cuối cùng

- **P1 unique đã dịch: 45.380 / 45.380 (100%)** — không còn chuỗi nào chưa dịch.
- Tổng số hàng bản dịch trong DB (origin `pipeline_muse`, status `machine`): **144.219 hàng = 144.219 source_id riêng biệt** (không trùng lặp, kiểm chứng sau mỗi wave).
- P0 + P1 cộng lại: **84.383 chuỗi unique** đã dịch (P0 39.003 + P1 45.380).
- Toàn bộ P1 chạy trong 44 wave (chunks 391–825): wave 1–43 mỗi wave 1.000 chuỗi, wave 44 cuối 401 chuỗi (chunks 821–824 mỗi chunk 100, chunk 825 chỉ 1 chuỗi: S1177_EA093AD7 "Five-Star Service...").
- **Quarantined: 0 mục tồn đọng.** Chỉ có 1 sự cố nạp trong toàn bộ P1 — wave 23 chunk 612 (2 mục bị tráo vị trí) — đã sửa và nạp lại đầy đủ trước khi tiếp tục.

## Nội dung P1

P1 = mạng xã hội trong game + item + description + tutorial:

- C0653–C0722: item/description/tutorial (Core).
- C0726: bình luận mạng xã hội.
- C0898: description/tutorial (phần lớn nhất, waves 3–13).
- C0902–C0907: item/description (hoạt động hẹn hò, đạn dược, tên màu/vải, quần áo).
- C0908–C0912: đồ ăn/uống/thuốc, kiểu tóc/hình xăm/trang điểm/nails/piercing.
- C0914–C0924: đồ ăn, phụ tùng xe, mô tả xe, độ xe/livery/mâm.
- C0925–C0927: mô tả vũ khí, skin súng, phụ kiện súng.
- C0930–C0953: nhãn mục tiêu nhiệm vụ, bình luận livestream (Camilo trunk-challenge).
- C0958–C1090: mô tả nhiệm vụ ngắn, tutorial, cài đặt (camera, deadzone, minimap, HUD, âm thanh).
- C1092: bình luận mạng xã hội trong game (phần lớn nhất, waves 25–39).
- C1095–C1113: item/description/tutorial.
- S0039–S1226 (Story): quảng cáo, bài hát, độc thoại minigame M0004/M0005, nhãn câu hỏi, barks, mô tả nhiệm vụ, bản tin Weazel News / Megamundo, PSA châm biếm, hội thoại gia đình S1087.
- S0615/S0616: thẻ sưu tầm (Tên – Màu) và mẫu vật động vật (Loài + hạng chất lượng).
- S0622–S0629: sổ tay, áp phích, thẻ, trang phục, thành tích, thử thách.
- S0822–S1226: lời bài hát, quảng cáo, bản tin dài (Weazel News, Megamundo tiếng Tây Ban Nha, talk-show BBL).

## Mốc đã báo cáo

5.000 (wave 4) · 10.000 (wave 9) · 15.000 (wave 14) · 20.000 (wave 19) · 25.000 (wave 24) · 30.000 (wave 29) · 35.000 (wave 34) · 40.000 (wave 39) · **45.380 hoàn thành (wave 44)**.

## Sự cố đã xử lý trong P1

- **Wave 4, chunk 426**: 1 mục bị tráo bản dịch (tutorial bãi bắn ↔ "Pollo Diablo") — sửa trước khi nạp.
- **Wave 23, chunk 612**: 2 mục bị tráo vị trí ("Vapid Oblivion 1" ↔ "Boxed Snorkel") — phát hiện lúc nạp (2 quarantined), sửa file, nạp lại đúng 2 hàng.
- **Wave 26, chunk 645**: bản nháp bỏ sót 1 mục (idx 47 "COLIN!!!") làm lệch cả khối sau — agent tự phát hiện, sửa file, kiểm tra trên đĩa trước khi nạp.
- **Wave 43, chunk 811**: bản nháp lệch id từ vị trí 17–28 (bỏ sót S0616_F8095E97 "Juvenile Green Iguana") — agent tự phát hiện và sửa, kiểm tra điểm trên đĩa (idx 14–31 khớp) trước khi nạp.

## Ghi chú chất lượng tích lũy (để rà soát sau, tất cả vẫn status `machine`)

### Chưa thống nhất — cần quyết định trước khi rà soát

- **Tiếng Tây Ban Nha**: đa số chunk giữ nguyên văn (code-switching), một số ít dịch sang tiếng Việt (chunks 625/626/638). Bản tin Megamundo (S0902–S0904, S0917–S0918) dịch theo quy ước "Nói tiếng Tây Ban Nha:" rồi dịch nội dung — khác với cách giữ nguyên văn ở các chunk chat.
- **Chữ trong ảnh (Image Text:)**: đa số dịch sang tiếng Việt, một số chunk giữ nguyên tiếng Anh (652/683/700/709).
- **"the Y / Y Hotel"**: ba cách cùng tồn tại — "chỗ Y" (chat S0593), "khách sạn Y" (chunks 736/795), giữ nguyên tên "Y Hotel" (chunks 642/671/676/685/695/780).
- **"Gold" (màu thẻ S0615)**: "Vàng Kim" (chunks 797/799/801–805) vs "Vàng" (chunks 798/800) — trùng với Yellow → "Vàng".
- **"Maroon"**: "Đỏ rượu vang" (797/799/801–805) vs "Đỏ sẫm" (800).
- **"Great Uncle Sam"**: "Ông chú Sam vĩ đại" (797/801/803/805) vs "Bác Sam Vĩ Đại" (799).
- **"Officer Pig"**: "Cảnh sát Pig" (802/803/804) vs giữ nguyên biệt danh (798).
- **"Foxy Ho"**: "Ho gợi cảm" (797) vs giữ nguyên biệt danh (798/800/801/803/804).
- **"They"**: "Họ" (797/802/803) vs giữ nguyên (796).
- **"Swallow"**: họ người (797/798) vs "Chim nhạn" (800).
- **"General Surgeon"**: dịch chức danh (796/799/800) vs giữ nguyên tên (796).
- **"Pristine" (hạng mẫu vật S0616)**: "Hoàn hảo" (806/808/809/810/811) vs "Nguyên vẹn" (807).
- **"Tom"**: gà tây trống (808/809) vs mèo đực (807).
- **"Leonida Cottonmouth"**: "Rắn miệng bông Leonida" (806/809) vs "Rắn Cottonmouth Leonida" (808).
- **"Killdeer"**: "Chim choắt" (807) vs "Chim choi choi Killdeer" (810).
- **"A ... gold piece."**: đồng xu vàng (799/802/804) vs "mảnh vàng" (800).
- **"Extraction"**: "Di tản" (396/498) vs "Rút lui" (395).
- **"bag"**: "túi tiền" (đa số, theo chunk 646/669/717) vs "cái túi" theo nghĩa đen (514/687) — nghĩa tiền vẫn là đa số.
- **"Shotgun"**: "Súng hoa cải" (620/621/645/692/701/703/705/706) vs "Súng săn" (619/622).
- **"SMG"**: "Súng tiểu liên" (619) vs giữ "SMG" (621).
- **"Stock" (phụ tùng)**: "nguyên bản" vs "zin".
- **"Top Fill"**: "đổ trên" vs "nắp đổ trên".

### Mơ hồ dai dẳng — cần ngữ cảnh game để quyết

- **"keys"**: Florida Keys / ma túy "Keys" / chìa khóa xe — gặp khắp nơi (706/709/737/747/756/763/766/774/778/788/789/791).
- **"white boy" / "white girls"**: người da trắng theo nghĩa đen (đa số) vs cocaine slang (quy tắc P0 đã duyệt ở chunk 316; chunks 757/758/770).
- **"Got Coke"**: Coca-Cola vs cocaine (S0217_DC24DC90).
- **"8ball"**: bi-a (750) vs cocaine 3.5g (771, skeleton ép thành "{number} ball").
- **"crabs"**: "rận mu" (697/773) vs cua theo nghĩa đen (736/737/767).
- **"cream pie" / "cake"**: đồ ăn theo nghĩa đen (671/690/695/779) vs nghĩa tục.
- **"kitty litter" / "cat litter"**: "cát mèo" theo nghĩa đen vs ma túy.
- **"hog"**: mô-tô Harley "con xe" (đa số) vs lợn theo nghĩa đen (744) vs tên riêng "Hank the Hog" (757).
- **"wrap"**: bọc xe vs bọc đồ ăn (702/714/741/751/762).
- **"Erises" / "Eris"**: giày/thương hiệu (chunk 777 xác nhận Eris là hãng giày) vs tên khác.
- **"FC"**: giữ nguyên loanword, chưa rõ (741/770).
- **"JOH"**: giữ nguyên loanword, chưa rõ là quán/nhóm (768/776/787/790).
- **"PG"**: giữ nguyên loanword, chưa rõ (747/775/792).
- **"pussy"**: nghĩa thô tục "lồn" (đa số) vs nghĩa hèn nhát "đồ hèn" (703/735/757/767/770/777) — cả hai đều có tiền lệ P0 đã duyệt.
- **"fuck with"**: nghĩa AAVE "thích" (248) vs "đừng đụng vào" vs nghĩa đen đã sửa ở P0 (233, S0142_AF3DBA69).
- **"catch"**: câu cá / gái mại dâm / mồi nhử (S0212, chunk 792).
- **"starfish"**: sao biển theo nghĩa đen (789) vs tiếng lóng tình dục.
- **"perineum sunning"**: "phơi nắng đáy chậu" theo nghĩa đen ở cả hai chunk gặp (792/793).
- **"bird"**: chim theo nghĩa đen (794) vs phụ nữ (tiếng lóng).
- **"VC"**: Vice City vs voice chat (791/794).
- **"Lu"**: biệt danh của Lucia (786/788/795).
- **"snow"**: tuyết vs cocaine (778).
- **"six pack"**: gói 6 lon bia vs nghĩa khác (S0206).
- **"the Y"**: xem mục chưa thống nhất ở trên.

### Lớp lỗi do skeleton ép slot

- Số trong từ lóng/leetspeak bị ép thành `{number}`: "Waiting 4 u" → "Đang chờ {number} mày" (741), "247 hot dog" → "{number} hot dog" (759), "pray 4 you" → "cầu nguyện {number} mày" (759), "sorry 4 ur loss" → "chia buồn {number} mất mát" (767), "bonded 4 life" → "{number}" (779), "family 5 eva" → "{number}" (777), ":3" → "{number}" (776), "John 3:16" → "John {time}" (759), "@big$shmoney$33" → "@big$shmoney{money}" (741), "smoke up an 8-ball" → "hút một {number} ball" (771).
- Mất dấu `$` qua ngoại lệ placeholder-slot: "Retry (~1$~)", "Pay (~1$~)", "Wager (~1$~)", "Sell All Collectible Cards For ~1$~" → "({number})" — gặp khắp P1.
- Tách số thập phân: "9.6kg" → "{number} 6kg", "2.7kg" → "{number} 7kg" (506/511/515).
- Mất dấu `%`: đã khôi phục theo tiền lệ chunk 333 ("{number}%") ở nhiều chunk; 3 hàng P0 đã sửa trong đợt rà soát chất lượng P0.
- "Sprinting (10,000m)" → "Chạy nước rút ({number} 000m)" (chunk 813) — skeleton tách số.

### Quy ước đã ổn định trong P1

- "pool" → "hồ bơi" (bơi lội/hồ bơi) vs "bi-a" (bàn bi-a/giải đấu) — phân biệt theo ngữ cảnh.
- "fence" → "tiêu thụ"/"tay tiêu thụ" (đồ trộm cắp) vs "hàng rào" theo nghĩa đen khi là hàng rào thật (747/758).
- "chop shop" → "xưởng rã xe".
- "trunk challenge" → "Thử thách cốp xe".
- "Griffin range" → "Bãi tập bắn Griffin".
- "Hollow Earth" → "Trái Đất Rỗng".
- "Mud Club" giữ nguyên tên.
- "Good Time State" → "Bang Vui Vẻ".
- "skunk ape" → "vượn hôi" (đối thoại/xã hội) vs giữ loanword (nhãn UI).
- "Mr. Mangrove" → "Ông Mangrove" (theo quy tắc P0 đã duyệt).
- "Minimap" → "Bản đồ thu nhỏ".
- "Sponsored" → "Được tài trợ".
- "Image Text:" → "Chữ trong ảnh:".
- "nm" → "Không có gì".
- "heat" → "cớm truy nã" (chat) — vẫn mâu thuẫn với "độ nóng" ở chunk 76/787.
- "In Spanish:" / "In Italian:" / "In Creole:" → "Nói tiếng Tây Ban Nha:" / "Nói tiếng Ý:" ... rồi dịch nội dung (bản tin Megamundo, talk-show BBL).
- "bag" → "túi tiền" (nghĩa tiền, đa số).
- "plug" → "mối" (người bán ma túy).
- Tên loài dịch sang tiếng Việt (quy ước P0); "Sylvilagus palustris" giữ Latin ở chunk 766 là ngoại lệ.
- Biệt danh/chơi chữ giữ loanword: KKKlash, Illuminaughty, Vaccerine, Immigrantasma, Wokester, Snowbunny, Flamer, The Ratster, ExeKKKutioner, MonaLi$a, Diddler, Karkinos, Gloriana.
- Tootsie uwu-speak dịch thành tiếng Việt dễ thương bình thường; Furry uwu-speak giữ nguyên ("Uwu. Rawr xD. Or hewwo.").
- Nguồn gõ sai/typo giữ nguyên trong bản dịch: "YEILD", "~LIP_EMOJI_FIRE~" thiếu B, "fjks6.,", "Visting", "Galetski"/"Galecki" (hai chính tả khác nhau cho cùng một cảnh sát, chunk 821).

## Việc còn lại

- **P2 (lore, 1.937 dòng) và P3 (dialogue còn lại, 465.455 dòng) chưa được duyệt** — cần hỏi người dùng trước khi dịch tiếp.
- Sau dịch: Phase 4 OCR prototype, Phase 5 Matching Engine, Phase 6 Overlay + Android TV app, Phase 7 Realtime Integration, Phase 8 Optimization (theo TDD).
