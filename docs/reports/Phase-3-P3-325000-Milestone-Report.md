# Phase 3 — P3 Milestone Report: 325,000 Unique Strings

**Date:** 2026-11-22 (after wave 323 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **325,435 / 357,142 (91.1%)**; P3 remaining **31,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 325,435 = **411,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 534,733 = distinct source_ids (no duplicates)
**Waves in this milestone period (319–323):** 5,000 strings, 0 quarantined in total

## Period totals

- Language cues: **0** in the whole period (319, 320, 321, 322, 323 ×0). Spanish fragments kept without a cue — 4048 B71B8D1A "Hola" (wave 321); 4067 E288A82C "Pero" (wave 323); 4069 E74E20E7 "hola" in "You don't know “hola?”" (wave 323). No "In Spanish:" cue in source for any of them, so none counted.
- Slots: **0** in the whole period (319, 320, 321, 322, 323 ×0)
- `~n~~m~`: **0** in the whole period
- `~tone~`: **0** in the whole period
- `~rp~`: **0** in the whole period
- "go fuck yourself": **1 new plural variant, softened** in the whole period — 4067 E0F5696F "'Kay! Go fuck yourselves!" → "Được rồi! Đi mà tự sướng đi!" (wave 323, per the wave-310 plural-variant precedent, pending the user's bulk decision). Related variants: **1 "go cry" variant** (320: 4037 9DDF432C "Yeah go cry about it someplace."); **1 "go fuck up" variant** (322: 4057 CACBB387 "Dude, go fuck up some other party."); **1 "go cry" variant** (323: 4066 DF982033 "go cry about it" → "đi mà khóc ở chỗ khác đi"). No new exact "go fuck yourself" in the whole period.
- "nigga": **0** in the whole period (319, 320, 321, 322, 323 ×0).

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 319 | 4026–4035 | 321,435 | Story S0867 ×1,000, mixed ambient crew/heist barks in the S0849 mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4027 "hole in one", 4030 "last nine holes", 4032 "You got par?"), motel/downtime lines, taunts/banter |
| 320 | 4036–4045 | 322,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4037 "back half", 4040 "That was par, right?", "a good turn"), strip-club lines (4041 lap dance), motel/downtime lines, taunts/banter |
| 321 | 4046–4055 | 323,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4051 "choke on the last hole", "can't find the hole?"; 4055 "get your head in one of these holes?"), strip-club lines, motel/downtime lines, taunts/banter |
| 322 | 4056–4065 | 324,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4057 "let's see a swing big, shot!"; 4058 "sink those putts!"; 4061 "Two tickets, please. We wanna do all of it."; 4063 "One for the front nine, please."), fishing-trip thread (4059 "chill little fishing trip", "You catching anything?"), pool line (4058 "cocktails by the pool"), motel/downtime lines, taunts/banter |
| 323 | 4066–4075 | 325,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4067 "Just two, thanks. Can we do the whole thing?"; 4075 "Something's up with that ball.", "if a homeless guy steals my ball..."), fishing thread (4071 "Let's go fishing."; 4074 "Are we going fishing again?"), pool line (4074 "And we're in the pool."), motel/downtime lines, taunts/banter |

## Incidents

- **Wave 319:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 320:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 321:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 322:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- **Wave 323:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check.
- No loader errors, no quarantines, no duplicate rows in the whole period (muse rows == distinct source_ids after every wave).

## Conventions settled / reinforced in this period

### Period-wide

- The whole period is a single group, S0867, so the wave-to-wave content barely changes — the period's value is in the accumulated splits, not new groups. No new groups appeared in waves 319–323.
- "I'm good" I'm-fine (4026 846C673F, 4028 887A90C9, 4029 8B072BD0, 4036 9A1867BA, 4037 9CE1DF9D, 4041 A6232566, 4055 C745274D, 4057 CAF2E069, 4064 DBDD7622, 4068 E4674ECD) vs don't-need-it (4042 A8F51BE7, 4045 B083F5C3, 4075 F49753B5 "I'm good on this") — NOT unified.
- "I'm done" finished (4030 8CE790D6, 4031 8F1CA31F, 4034 96D953B3, 4037 9BE0D40B, 4041 A716B8DD, 4045 AF803195, 4047 B3F5FEBC, 4053 C266731F, 4059 CED61971, 4060 D2580536, 4063 D8ECD8FE, 4068 E3940D37, 4075 F42182D0) vs fed-up vs doomed (4051 BE30683D) vs done-with-you (4030 8C1672D7, 4037 9D429A19, 4039 A28CD393, 4065 DD601A6B) — NOT unified.
- "I'm down" up-for-it (4030, 4031 8EF962A0, 4040, 4042 A9899D72, 4045 AFB1700B, 4046 B0D6D973, 4052 BF2BA676, 4053 "I'm down for whatever", 4054 C430B308, 4059 CFD7BB02/D09CCFC9, 4064 DBA969AB, 4065 DCFFA12F, 4072 EE337791) vs knocked-down (4042 A9B71F2E) vs down/depressed — NOT unified.
- "I'm out" leaving (4057 CBC06A15, 4061 D51DB282, 4067 E0E370D4/E0EAB6B4) vs out-of-ammo (4050 B9E5DB74) — NOT unified.
- "fuck with" mess-with "dây với" (4035, 4039 A0D9E2BD, 4073 EEDC5F4D, 4075 F4DE3116) vs AAVE "thích" (4037 9DDAA0EF) vs joking "chỉ đùa/trêu" (4069 E71439D6, 4072 EC8DE680/EDC6FE51) vs tampering vs teasing/messing vs don't-like — NOT unified.
- "go out" die side (4050 BAB00AD2, 4052 BF0D7B8D, 4057 CBD312E2) vs going-out-socially (4054 C4774B92, 4056 C9178F77, 4057 CB5C4E88, 4059 D05983D2, 4062 D5893E84/D7402BC8, 4073 F0656426/F0577358) vs died + high (4048 B71114BA "went out high as balls") vs leaving (4060 D1EBC48C) — NOT unified.
- "lady" mocking "bà chị" (4026, 4032, 4033, 4034, 4038 9EC06F46, 4040 A4BFC1BB, 4043 AA60C959, 4045 AF8288A0, 4049 B8753EED, 4052 BEF9886A, 4054 C5D7D1B5, 4056 C8BA9309, 4061 D305BA1D, 4065 DD1692C3, 4066 E00B7BA0, 4067 E31B5384, 4068 E338BF7E/E4E16CDF, 4070 E8B3B11E, 4075 F5C2F5FC) vs polite "chị" (4032 90BF8137, 4067 E2F62C0F, 4068 E56DC3E8) — NOT unified.
- "take it out" kill side (4061 D35BC62A "Great! A tank! Take it out!") vs remove-it side (4057 CA2CC5AD) vs vent-anger side (4039 A2EB2921 "take that out on him", 4069 "take it out on me" → "trút lên tao") — NOT unified.
- "take a shot" shooting side (4051 BC525D45, 4059 CF3E4C2A "My boy's a good shot") vs drink side vs attempt side — NOT unified.
- "put you down" knock-down "hạ mày" (4048 B692E012) vs shooting side — NOT unified.
- "call it" end-it side (4052 BF9C0BFC, 4053, 4065 DCF76682 "I'm calling it") vs call someone — NOT unified.
- "eat shit" literal insult "Ăn cứt đi" (4055, 4067 E1CB8FBB) vs fail side "ngã sấp mặt" — NOT unified.
- "bike" → "xe đạp" per brief majority (4026, 4037 9CCC6D20, 4040, 4046 B2053BB4 "Kill that bike!", 4054 C3ABBAE6 "Bike's down!", 4070 E7EEA4E2) — motorcycle "xe máy" side still flagged.
- "chill" verb "calm down" translated (4036 9AF4DA13/9B97DB65, 4038 9EB8FF53, 4043 AC6C61E6, 4051 BD084494, 4057 CAA2C7A8, 4060 D18D9CAA, 4067 E0D9951A/E0E9CB59, 4069 E5F6D2FB/E653DA0C, 4074 F128972B/F252A644) vs kept as loanword "Chill đi" (4041 A7AB5AB4, 4050 BAEE2377, 4053, 4058, 4059, 4063 D9E95EC5, 4065, 4070 E7FEB8B4/E87A5357, 4071 EA2D62D3, 4072 EC4BE803/EC88E8D4/EDDDC6AB, 4073 EF75D7D2, 4075 F5A2662F) — NOT unified.
- "pool" swimming "hồ bơi" (4038 9E74CB09/9FCCD310, 4058, 4068 E56CAE89, 4074) vs bi-a (4005, 4060 "Rack 'em up!") — NOT unified.
- "on the clock" "đang trong giờ làm" (4044) vs "đang chạy đua với thời gian" — NOT unified.
- "on E" fuel-gauge side "sắp hết xăng" (4063 D901EF8C) vs ecstasy side — NOT unified.
- "chemistry" kept loanword vs translated "ăn ý" (4061 D4ABCCB4) — NOT unified.
- "screw you" mild-but-crude "cút mẹ mày đi" (4043 AB8E53E5) vs crude "Địt mẹ mày" — NOT unified.
- "change things up" → "đổi gió" (4042 A9CC7891) vs car side "đổi con xe" (4027) vs "switch it out" car side "đổi con khác đi" (4069 E5E7B672) — NOT unified.
- "the Y" / "the Y Hotel" kept (4059 CFAAB514, 4061 D403DED8, 4066 E07D2E64) — unresolved.
- "Leonida's finest" → "Tinh hoa của Leonida" (4053 C184A33D, per the S0088 "Capri's finest" flag).
- "BBL" kept as acronym (4062 D6003D4D, 4068 E4D6DAFA) — spelled-out side still flagged.
- "take the L" loss side "Nhận lấy thất bại này đi" (4071 EB62793F, per wave-204 "hold this L") — settled as loss.
- "I got it" have-it side (4071 EA2D62D3, 4074 F13E5BDA) vs understood side (4070 E939F640, 4074 F1D97F4E) — NOT unified.
- "inside" prison side (4075 F46C84B7) vs indoors — NOT unified.
- "get down" default "nằm xuống" (4044, 4058 CD39960F, 4066, 4071 EAF83D2C "Stay fucking down!") vs high-place/come-here/arrival/fall-die/party — NOT unified.
- Investigator-style question voice split continues: crew "mày" (4027 862DAA67, 4033 93EC17D5, 4040 A52E3A59, 4048 B54CDA8E/B73FF73D/B756DEAA, 4055 C7077E03, 4056 C88C0118/C9208193, 4064 DAF32538, 4075 F4257FAE/F59E5A8E) vs polite "tôi/anh" city-worker (4031 8F638BC2, 4038 9E11291D, 4039 A148609C, 4045 AF33D3FC/AF636D18, 4053 C170738B, 4059 CF3ABC4D, 4069 E6E48960/E72762E1, 4074 F36D89BA) — NOT unified.
- Near-identical pair translated slightly differently: 4071 E9B6E988 "Okay, I'll look for my own." vs E9D9AB48 "Okay, I'll find my own."
- Source typos rendered by sense (4044 "Chil,l", 4038 "Oksy", 4064 DA1D38E3 "don't'", DAEE976E "Don;t", 4058 CE399B8A "embarassing", 4057 CAABA158 "you friends", 4062 D57AAA01 "say some").

## New / deepened splits this period

- **"I'm good" / "I'm done" / "I'm down" / "I'm out" / "go out"** — all deepened in this period (listed above); each now has 3–4 competing renderings across waves 319–323 alone.
- **"fuck with"** — the joking "trêu/chỉ đùa" side appears in this period (4069 E71439D6, 4072 EC8DE680/EDC6FE51) alongside the established mess-with and AAVE "thích" sides.
- **"chill"** — the split widened: verb "calm down" translated in 9 chunks vs loanword kept in 12 chunks across waves 319–323.
- **"on E"** — new split: fuel-gauge "sắp hết xăng" (4063 D901EF8C) vs ecstasy side.
- **"take the L"** — settled as loss side in this period (4071 EB62793F).
- **"knuckle duster"** → "găng tay đấm bốc" (chunk 3582) — known likely-wrong rendering, should likely be "quả đấm sắt" (carried from earlier milestone).
- **"eff"/"effin'"** → "đệt" renderings keep accumulating — deferred until after the "Go fuck yourself!" decision.

## Open questions carried forward

- **"Go fuck yourself!" (pending):** fresh DB recount at 07:16 on 2026-11-22: 178 rows, 106 softened vs 71 crude. New softened-side addition in this period: 4067 E0F5696F (plural variant, wave 323). New crude-side additions: none in this period. Option A (recommended): crude "Đi mà tự đụ đi" — follows the no-sanitizing rule. Option B: softened — fix the crude rows. Bulk fix to be applied after P3 finishes.
- **"nigga" (unresolved):** kept as loanword in most waves; 0 in this period. Rows left as-is (status `machine`).
- **Polite-NPC pronoun question (open):** the long consistent "tôi" pattern for fearful/polite/sales lines, real police calls, people requesting police, fearful begging/surrender, polite civilian questions, witness statements, legal declarations, radio self-reports, formal staff voices, PA announcements, Jason's and Lucia's polite self-introductions — vs crew "tao/mày" on cooperate lines. New evidence this period listed above under "Investigator-style question voice split continues". Rows left as-is (status `machine`).
- **Couple-voice question (wave 194) and family-voice extension (wave 246):** Lucia/Jason couple scenes generally use "tao/mày"; mother↔daughter "mẹ/con" vs "tao/mày" — same open question family. "Ma" → "Má" vs "Mẹ" — NOT unified. "mama" → "Mẹ" vs kept loanword vs "Má" — NOT unified. "Mommy" → "Mẹ" vs kept loanword — NOT unified. "momma" → "mẹ" vs kept loanword vs "Má" — NOT unified.
- **"eff"/"eff-you" and "cougar":** deferred until after the "Go fuck yourself!" decision.
- **Standing P3-wide unresolved splits:** the full per-wave lists live in the MEMORY.md wave entries (waves 319–323) — consult them rather than re-deriving. Families include: "I got you"/"I got it"/"You got it" by context; "fuck with" mess-with vs AAVE "thích" vs joking vs teasing vs tampering; "get down" default vs high-place/come-here/arrival/fall-die/party; "I'm out" leaving vs out-of-ammo/money/stuff vs out-of-prison; "I'm done" finished vs fed-up vs doomed vs giving-up; "inside" prison vs elsewhere; "put you down" knock-down vs shooting vs land-the-plane; "take a shot"/"get a shot" shooting vs drink vs attempt vs photo; "Back up!" step-back vs calling-for-backup; "hit" by context; "the Y" kept, unresolved; "lady"/"miss"/"officer" polite vs mocking/casual; "Hello" phone vs calling-out; "Princess" kept vs "công chúa"; "fence" physical vs stolen-goods; "bird" literal vs aircraft; "bike" "xe đạp" vs "xe máy"; "heat" cops-pressing vs pressure/teasing; "cover" yểm trợ vs chỗ nấp vs guarding-the-doors; "pool" hồ bơi vs bi-a; "piece" gun vs girlfriend vs share vs said-my-piece; "good shit" hàng ngon vs praise; "suck" be-bad vs literal; "milking" literal vs dragging-it-out; "call it" end-it vs call someone; "charge" battery vs money vs attack; "eat shit" fail side vs literal insult; "screw you" crude vs softened vs mild-but-crude.
