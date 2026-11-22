# Phase 3 — P3 Milestone Report: 320,000 Unique Strings

**Date:** 2026-11-22 (after wave 318 loaded)
**Tier:** P3 (remaining dialogue, category `dialogue`, Core packs)
**Cumulative:** P3 unique **320,435 / 357,142 (89.7%)**; P3 remaining **36,707**
**All tiers combined:** P0 39,003 + P1 45,380 + P2 1,919 + P3 320,435 = **406,737 unique strings** translated
**DB rows (origin `pipeline_muse`, status `machine`):** 529,571 = distinct source_ids (no duplicates)
**Waves in this milestone period (314–318):** 5,000 strings, 0 quarantined in total

## Period totals

- Language cues: **0** in the whole period (314, 315, 316, 317, 318 ×0). One Spanish fragment kept without a cue — 4016 6D0DFAC7 "Go home, vieja! ¡Dios!" (no "In Spanish:" cue in source, so not counted).
- Slots: **1** (316: 3996 3EEFDA25 "Don't even think about calling 911." → "gọi {number}", skeleton-forced slot on a non-number; 314, 315, 317, 318 ×0)
- `~n~~m~`: **0** in the whole period
- `~tone~`: **0** in the whole period
- `~rp~`: **0** in the whole period
- "go fuck yourself": **0 new exact** in the whole period. Related variants: **1 bare variant, softened** (314: 3980 177C6618 "Mm... How about fuck yourself?" → "Ừm... đi mà tự sướng đi thì sao?", per the wave-256/304 precedent); **1 "fucked yourself" variant, softened** (316: 3996 3F429107 "Do you even know how hard you just fucked yourself?" → "Mày có biết mày vừa tự hại mình thảm hại cỡ nào không?" — flag if the crude "tự đụ mình" is wanted; not the exact pending string); **1 "go fuck a gator" variant, crude literal** (317: 4012 63E070C9 "Oh go fuck a gator, lady." → "Ồ, đi mà địt cá sấu đi, bà chị."); **1 "go fucking cry" variant, crude** (318: 4018 72C63411 "Oh go fucking cry about it." → "đi mà khóc mẹ nó về chuyện đó đi."). Two bare "fuck me" exclamations, crude literal (316: 4005 52D7637B "Okay, fuck me then," → "Được rồi, địt mẹ tao đi,"; 4002 4D0C0061 "Fuck me, that was... ugh..." → "Địt mẹ, cái đó... ugh..."). All pending the user's bulk decision.
- "nigga": **0** in the whole period (314, 315, 316, 317, 318 ×0).

## Waves covered

| Wave | Chunks | P3 unique after | Content |
|------|--------|----------------|---------|
| 314 | 3976–3985 | 316,435 | Story S0867 ×1,000, mixed ambient crew/heist barks in the S0849 mold — robbery/change-up lines, cops lines, car/driving lines, motel/apartment downtime lines, one-liner taunts/banter |
| 315 | 3986–3995 | 317,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, boat lines, motel/downtime lines, taunts/banter |
| 316 | 3996–4005 | 318,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, boat/dock lines, dogs lines, pool/motel downtime lines, taunts/banter |
| 317 | 4006–4015 | 319,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, boat lines, golf thread (4008, 4013 — "back nine"/"first nine"), motel/apartment downtime lines, taunts/banter |
| 318 | 4016–4025 | 320,435 | Story S0867 ×1,000, same mold — robbery/change-up lines, cops lines, car/driving lines, golf thread (4018, 4019 — "two for the first nine holes", "first half of the course"), motel/apartment downtime lines, taunts/banter |

## Incidents

- **Wave 314:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check. Chunk 3978's agent self-caught a duplicated id (item 24 first misread as 12B5ECCD, duplicating item 25) — corrected to 12B52573 before merging; the final file was verified on disk.
- **Wave 315:** 9/10 handoffs arrived before loading — chunk 3988's handoff never arrived; its file was verified on disk (100 items, ids in order, keys exactly {id, vi}, 0 adjacent dups) and loaded with the wave. The 3988 handoff arrived late afterwards and matched the on-disk verification exactly.
- **Wave 316:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check. Chunk 3998 alone produced 129 loader rows (many shared en_norm).
- **Wave 317:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check. Chunk 4015 alone produced 127 loader rows (many shared en_norm).
- **Wave 318:** 10/10 handoffs arrived before loading. All 10 files passed the full structure check. Chunk 4018's halves split 53/47 (miscounted cut point), final file independently verified 100 items in order. Chunk 4024's agent self-caught a duplicated id (80F23162) in the part-2 draft, corrected before merging. Chunk 4025's first merge attempt split 48/52, rewrote both halves with the correct 50/50 split and re-verified 100 items in order.
- No loader errors, no quarantines, no duplicate rows in the whole period (muse rows == distinct source_ids after every wave).

## Conventions settled / reinforced in this period

### Period-wide

- The whole period is a single group, S0867, so the wave-to-wave content barely changes — the period's value is in the accumulated splits, not new groups. No new groups appeared in waves 314–318.
- "I'm done" finished (3987 2997E816, 4004 522EB931, 4015 6BB7106F, 4006 56F03AD5) vs fed-up (3986 25683B57, 3995 3BB802A2, 4000 46BE8D07, 4013 65A51747) vs giving-up (4000 4790A9C4) vs doomed (4004 51B8EFE7) — NOT unified.
- "fuck with" mess-with "dây với" (3989 2C0A6DFD, 3988 2B2CF1FA "Would you fuck with me?", 4021 77E79D7C) vs AAVE "thích" (3998 420ABA0A) vs joking "chỉ đùa" (3989 2C6A73A0, 3994 38AEEBCA, 4003, 4019 754A6C2A) vs teasing (4013 67AADB01, 4020 75F7EE8A) vs don't-like (3983 1F2E9063) — NOT unified.
- "I'm good" I'm-fine (4013 65F21393, 4015 53F9BC55, 4020 760803C2) vs don't-need-it (4007 583A0945, 4022 7AEA4E44) — NOT unified.
- "lady" mocking "bà chị" (3976 0F7B08DF, 3979 1643E3CE, 3993 36AE9D11, 4001 498E3E91, 4005 529BB655, 4012 63E070C9, 4012 64815A47, 4021 7A14B82A, 4022 7B759013, 4023 7EBA295E, 4024 7F194726) vs polite "chị"/"chị ơi" (3976 0E13AC76, 3997 3FBFA18C) vs admiring polite "Chị ơi, lớn lên em muốn được như chị." (4016 6D19F395) vs neutral "bà" (3989 2D7D48AC, 4025 81BBAC9E) — NOT unified.
- "go out" die side (3982 1C9D84EF, 3984 227CF2A6, 4025 832119FA) vs leaving (3982 1CB8C455, 3999 4511472F) vs going-out-socially (4019 745F0080, 4025 8122FF8F) — NOT unified.
- "I'm out" leaving (3992 354646DF, 4001? no — 4017 6FECE267, 4016 6D61D793, 4009 5C09C062) vs out-of-ammo/stuff — NOT unified.
- "bike" → "xe đạp" per brief majority (3985 239AB80A, 3993 37DA895F, 3998 43FD66F1, 4012 6404642C, 4013 661C9902, 4019 7387F095, 4020 7655A03B) — motorcycle "xe máy" side still flagged.
- "chill" adjective kept as loanword (per 3792; recurs in nearly every chunk) vs verb "calm down" translated "bình tĩnh cái đéo lại đi" (3990 30F95765, 4003, 4014 696C05C9, 4021 78DE5ADE) — flagged.
- "take a shot" shooting side (3980 1816FC88) vs drink side (3997 40E0FB82, 3979? no — 3997 3F6CCDAF/40E0FB82) — NOT unified.
- "pool" bi-a game side (4005 538AC5BE) vs swimming "hồ bơi" (3997) — NOT unified.
- "make a withdrawal" bank-robbery euphemism "rút tiền" (4008 5ADBE6C4, 4004 516B8706, 4018) — settled.
- "Hello" phone "A lô." (3987 29905743) vs calling-out "Này?" (3987 28D55A97, 4003 4F8314C5, 4005 526F0EEF) — both sides in use, NOT unified.
- "switch this thing up" car side "đổi cái xe này đi" (4014 680264FA) vs settled "đổi gió" — flagged.
- "get fucked" chase-off "cút mẹ mày đi" (3989 2C6E6EF9) — not "go fuck yourself".
- "Ma"/"mama"/"momma"/"mommy" → "Má" (3990 3043FB17, 4007 58CE0F25, 4008 5A069C17, 4013? no — 4020 75863074) vs "Mẹ" (3969-era) vs kept loanword "mommy" mocking (3986 26B43EB4) — NOT unified.
- "cupcake" → "cưng" (3988 29E9D638); "Big House" kept as a place name (3997 3F4B6F65) — flag if prison slang "nhà tù lớn"; "Jack of Hearts" kept as a name (3997 400320F8) — flag if playing-card side "thằng bồi cơ".
- "no sweat off my tits" split: image dropped (3985 250191C6 "chẳng dính gì tới tao đâu") vs crude image kept (3983 1E4DD325 "Chẳng tốn giọt mồ hôi nào trên vú tao.") — NOT unified.
- Polite-NPC "tôi" pattern continues: fearful begging, polite civilian questions, service/order voices, officer addresses, investigator questions (crew "mày" vs polite "anh"/"tôi" — the investigator-style question is itself split: 3978 124A13E5 crew "mày" vs 4015 6B19ED99 crew "mày" vs 4021 78540EB4 polite "tôi/anh" vs 4023 7DD4930A crew "mày"). Newest evidence: 3979 15EA8D9D + 1635D90D "tôi", 3984 225E4C46 fearful begging "tôi", 3987 27F02A24 polite "anh", 3990 30E359DA + 31457625 polite "tôi"/valet "thưa ông", 4000 474B5FE8 "tôi... thưa cảnh sát", 4001 4A4B3E7D polite "tôi/anh", 4007 5933C924 polite "tôi" to an officer, 4015 6AC6C289 + 6BCBDE14 polite "tôi/anh" service voices, 4018 7290E2C7 polite "tôi... thưa cảnh sát", 4021 78540EB4/7899EEC1/794683AA/79CBAFD0 polite "tôi", 4024 7F7DB3A5 polite "tôi... thưa cảnh sát". Rows left as-is (status `machine`).
- Recurring `$`/`%` loss via placeholder-slot exception continues; skeleton-forced `{number}` slot on "911" (3996 3EEFDA25); many source typos rendered by sense (3976 0E137F4B "We should his the Pay 'n' Spray." typo "his" for "hit"; 3977 10DDDCA1 "though" for "through"; 3987 28CF247B "Haven't see" for "Haven't seen"; 3989 2C7E17B5 "one their spots" for "one of their spots"; 3996 3DC7078C "what's going with that"; 4002 4D0C0061 truncated "Fuck me, that was... ugh..."; 4010 5E920102 garbled "Here's something to make up over"; 4010 5F58B74F "for you time"; 4025 8163EFAD missing final punctuation kept).

## New / deepened splits this period

- **"I'm done" / "I'm good" / "fuck with" / "go out" / "lady"** — all deepened in this period (listed above); each now has 3–5 competing renderings across waves 314–318 alone.
- **"a million fuckin' stars"** literal stars (3995 3CB2D4DA) — flag if GTA wanted-level stars.
- **"on fire"** doing-great side (4003 4E95DED2 "mama" → "má" + "đang cháy rực") vs attractive side (4013 67553BE9 "mày trông ngon quá!") vs temperature — NOT unified.
- **"I'm down"** up-for-it (4010 5FD43B9C, 4005 53A36ED9) vs down/depressed — NOT unified.
- **"I'm out"** leaving vs out-of-ammo/stuff — NOT unified (recurs every wave).
- **"knuckle duster"** → "găng tay đấm bốc" (chunk 3582) — known likely-wrong rendering, should likely be "quả đấm sắt" (carried from earlier milestone).
- **"eff"/"effin'"** → "đệt" renderings keep accumulating — deferred until after the "Go fuck yourself!" decision.

## Open questions carried forward

- **"Go fuck yourself!" (pending):** fresh DB recount at 07:16 on 2026-11-22: 178 rows, 106 softened vs 71 crude. New softened-side additions in this period: 3980 177C6618 (bare variant, wave 314), 3996 3F429107 ("fucked yourself" variant, wave 316). New crude-side additions: 4012 63E070C9 ("go fuck a gator", wave 317), 4018 72C63411 ("go fucking cry", wave 318) — neither is the exact string, so they do not change the 178-row count. Option A (recommended): crude "Đi mà tự đụ đi" — follows the no-sanitizing rule. Option B: softened — fix the crude rows. Bulk fix to be applied after P3 finishes.
- **"nigga" (unresolved):** kept as loanword in most waves; 0 in this period. Rows left as-is (status `machine`).
- **Polite-NPC pronoun question (open):** the long consistent "tôi" pattern for fearful/polite/sales lines, real police calls, people requesting police, fearful begging/surrender, polite civilian questions, witness statements, legal declarations, radio self-reports, formal staff voices, PA announcements, Jason's and Lucia's polite self-introductions — vs crew "tao/mày" on cooperate lines. New evidence this period listed above under "Polite-NPC 'tôi' pattern continues". Rows left as-is (status `machine`).
- **Couple-voice question (wave 194) and family-voice extension (wave 246):** Lucia/Jason couple scenes generally use "tao/mày"; mother↔daughter "mẹ/con" vs "tao/mày" — same open question family. "Ma" → "Má" vs "Mẹ" — NOT unified. "mama" → "Mẹ" vs kept loanword vs "Má" — NOT unified. "Mommy" → "Mẹ" vs kept loanword — NOT unified. "momma" → "mẹ" vs kept loanword vs "Má" — NOT unified.
- **"eff"/"eff-you" and "cougar":** deferred until after the "Go fuck yourself!" decision.
- **Standing P3-wide unresolved splits:** the full per-wave lists live in the MEMORY.md wave entries (waves 314–318) — consult them rather than re-deriving. Families include: "I got you"/"I got it"/"You got it" by context; "fuck with" mess-with vs AAVE "thích" vs joking vs teasing vs tampering; "get down" default vs high-place/come-here/arrival/fall-die/party; "I'm out" leaving vs out-of-ammo/money/stuff vs out-of-prison; "I'm done" finished vs fed-up vs doomed vs giving-up; "inside" prison vs elsewhere; "put you down" knock-down vs shooting vs land-the-plane; "take a shot"/"get a shot" shooting vs drink vs attempt vs photo; "Back up!" step-back vs calling-for-backup; "hit" by context; "the Y" kept, unresolved; "lady"/"miss"/"officer" polite vs mocking/casual; "Hello" phone vs calling-out; "Princess" kept vs "công chúa"; "fence" physical vs stolen-goods; "bird" literal vs aircraft; "bike" "xe đạp" vs "xe máy"; "heat" cops-pressing vs pressure/teasing; "cover" yểm trợ vs chỗ nấp vs guarding-the-doors; "pool" hồ bơi vs bi-a; "piece" gun vs girlfriend vs share vs said-my-piece; "good shit" hàng ngon vs praise; "suck" be-bad vs literal; "milking" literal vs dragging-it-out; "call it" end-it vs call someone; "charge" battery vs money vs attack; "eat shit" fail side vs literal insult; "screw you" crude vs softened vs mild-but-crude.
