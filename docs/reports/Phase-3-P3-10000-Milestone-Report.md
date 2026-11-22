# Phase 3 — P3 10,000-String Milestone Report

**Date:** 2026-11-21
**Tier:** P3 (remaining dialogue) — **10,435 / 357,142 unique strings (2.9%)**
**Remaining:** 346,707 unique strings

## Progress

| Wave | Chunks | P3 unique after | Notes |
|------|--------|-----------------|-------|
| 1 | 846–855 | 3,435 | C0000 police radio |
| 2 | 856–865 | 4,435 | C0000→C0001 radio |
| 3 | 866–875 | 5,435 | C0001 radio — 5,000 milestone |
| 4 | 876–885 | 6,435 | C0001 radio → C0002 street AAVE |
| 5 | 886–895 | 7,435 | C0003 radio |
| 6 | 896–905 | 8,435 | C0003 radio → C0004 street |
| 7 | 906–915 | 9,435 | C0004 street → C0005 radio |
| 8 | 916–925 | **10,435** | C0005 radio → C0006 civilian |

- `translations` total: **163,181 rows**, all origin `pipeline_muse`, status `machine`; muse rows == distinct source_ids (no duplicates).
- Quarantined across all 8 waves: **0**.
- Combined P0+P1+P2+P3: **96,737 unique strings** translated.

## Content so far

Waves 1–8 are all Core dialogue barks, in sequence by pack:

- **C0000–C0001** (waves 1–4): police radio — Dispatch calls, unit codes (214/276/321/391/442/569/615/662/846/913), PIT maneuvers, K9 commands, "set the box", "10-29" codes, DOA reports, breathalyzer ("blow into this"), sobriety tests, heights (5'5" / 5'10").
- **C0002** (wave 4): street AAVE barks — threats, gang talk, "nigga"/"jit"/"bruh"/"homie"/"papi" loanwords.
- **C0003** (waves 5–6): police radio again, plus a transition into C0004 street.
- **C0004** (waves 6–7): street AAVE barks.
- **C0005** (waves 7–8): police radio.
- **C0006** (wave 8): civilian bystanders reacting to the player — calling 911, filming, arguing, complaining, threatening to sue.

## Incidents (all resolved before loading)

- Wave 1, chunks 850/851: self-fixed shifted blocks (omitted item + tail slip), spot-checked aligned before loading.
- Wave 5, chunk 892: draft omitted C0003_5E9AA844 "Cover them!" at idx 15, shifting the rest; agent re-aligned by script, spot-checked idx 13–17 and 95–99 aligned before loading.
- Wave 8, chunk 916: draft had 99 items, missing C0005_AA657A26 "Down there! Down there!" at idx 38; agent re-inserted it, spot-checked idx 36–41 aligned before loading.

## Settled conventions (police radio)

- "Dispatch" → "trung tâm điều phối"; "HQ" → "tổng đài"; "subject" → "đối tượng"; "suspect" → "nghi phạm"; "in custody" → "bị bắt giữ"; "backup" → "chi viện"; "set the box" → "vây xe lại"; "PIT" kept (majority); "NOOSE"/"SWAT"/"K9" kept; "PWC" → "mô-tô nước"; "chopper" → "trực thăng"; "scooter" → "xe tay ga"; "fire rescue" → "đội cứu hỏa"; "EMS"/"EMT" → "cấp cứu"; "bicycle" → "xe đạp"; "motorcycle" → "mô-tô".
- "call it" → "kết thúc vụ này" (chunks 861/869/874/896/903/910) — but "call it in!" → "gọi báo cáo đi!" (chunk 914) is a different sense.
- "fresh bodies" → "người mới" (relief officers, chunks 875/899).
- "blow into this" → breathalyzer reading (chunks 854/879/920).

## Settled conventions (street AAVE)

- Loanwords kept: "nigga", "jit", "bruh", "homie", "papi", "ma".
- "motherfucker" → "thằng chó chết"; "bitch" → "con đĩ"; "piece" → súng; "whip" → xe; "stick" → súng; "smoke" → rắc rối/đánh nhau (or bắn chết in "smoke yo' ass"); "twelve" = cảnh sát; "heat" = cớm (police sense); "fuck with" by sense (thích / đụng tới / chơi cùng); "parley" → "đàm phán"; "trippin'" → "phê" (majority); "tweakin'" → "phê".
- "pussy": coward sense → "đồ hèn" (P0 rule); crude sense → "lồn" (chunk 902 C0004_0CB3E169, chunk 907 C0004_C7DF95FF).

## Unresolved ambiguities (all rows status `machine`, for later review)

- **German K9 commands** — still inconsistent: "Fass!" → "Cắn!", "Heel!" → "Sát chân!", "Stellen!" → "Chặn lại!"/"Đứng yên!", "Aus!" → "Nhả ra!", "Los!" → "Đi!" vs "Fuss!" kept, "Zoek!" kept.
- **"bike"** — xe đạp (chunks 867/886/888/896/898/899, argued from a separate "motorcycle" in the same chunk) vs mô-tô (chunks 874/889/890).
- **Heights** — "{number} {number}" per skeleton (most) vs "cao khoảng {number} foot {number} inch" (chunk 849).
- **"body"** — corpse (most chunks) vs living person (chunks 860/873/906 "We need bodies"); chunk 922 "This is what a body looks like" reads body as physique.
- **"DOA"** — kept as loanword (chunks 849/858/860/886) vs translated (chunk 846).
- **"10-29"** — skeleton varies: "{number}-{number}" vs "{number} {number}" vs "{number} {number} {number}" (chunk 889).
- **"PIT"** — kept (most) vs "húc xoay" (chunks 847/862/868/873/895).
- **"I got you" / "I got 'em"** — arrest ("tóm được mày rồi") vs reassure ("tao lo cho mày") — ambiguous in many chunks.
- **"That's Negative."** — "phủ định" (chunks 850/899/909) vs "Không phải." (chunk 876).
- **"officer down"** — badly hurt vs dead (chunk 913).
- **"runner"** — fugitive (chunks 915/919) vs drug runner (chunk 815).
- **"call it"** vs **"call it in"** — two different senses, both occur.
- **"paws"** — animal paws (K9/furry, chunks 896/918) vs hands — read as paws throughout.
- **Source typos preserved in translation**: "feeling" read as "fleeing" (chunks 875/878); "shorts fired!" → "shots fired" (chunk 887); "I'm arrival." → "đã tới nơi"; "Byh-bye!" (chunk 891); "pleases" (chunk 889).

## Next

- Wave 9 (chunks 926–935) in progress. Next milestones: 15,000, 20,000, … Final P3 report at 357,142/357,142.
