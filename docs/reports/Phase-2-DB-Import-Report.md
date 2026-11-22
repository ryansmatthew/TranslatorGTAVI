# Phase 2 — Translation Database: Import Report

**Date:** 2026-11-21
**TDD:** v1.3 (approved by user 2026-11-21: ADR-1 SQLite+FTS5, ADR-2 RapidFuzz on filtered candidates, Chapter 14 gates)
**Status:** ✅ Phase 2 gate passed

## What was built

Project: `gta-vi-vi-translator/` in this goal's workspace
- `src/db/schema.sql` — TDD ch. 4.4–4.5
- `src/db/import_tsv.py` — importer (re-runnable, fresh rebuild)
- `src/common/markers.py` (v2) + `src/common/normalize.py` (v1) — shared modules, used by both import and runtime
- `data/gta6.db` — 350 MB, SQLite WAL + FTS5
- `data/import_report.json` — machine-readable import report
- `tools/bench_phase2.py` + `tools/bench_phase2_report.json` — Phase 2 gate benchmark

## Import result — IMPORT OK

| Check | Result |
|---|---|
| Source file | `all_rows.tsv`, 69 MB, sha256 `39a002c0…2e2a55` |
| Rows imported | **579,495 / 579,495** (0 lost) |
| match_index rows | 579,495 |
| match_fts rows | 579,495 |
| Unique non-empty English | 461,633 |
| Empty `en` | 4,421 |
| `en` checksum (id+en, file order) | matches source ✅ `0ce1b510…434a` |
| Bad marker JSON | 0 |
| Rows with markers | 43,399 |
| Unknown markers left | 5 instances (flagged in DB, all non-visible tokens) |
| Templates detected | 9,233 |
| Import time | ~116 s |

### Tiers (TDD 4.3)

| Tier | Rows | Contents |
|---|---|---|
| P0 | 50,157 | UI 27,179 + Subtitle 22,978 |
| P1 | 49,880 | Social media 18,150 + Item 15,980 + Description 14,893 + Tutorial 857 |
| P2 | 1,937 | Lore |
| P3 | 465,455 | Remaining dialogue |
| review | 12,066 | Blank category — imported, never auto-translated |

## Benchmark — 10,000 sampled queries (TDD ch. 14, Phase 2 gate)

| Query | Hit rate | p50 | p95 | p99 | Max |
|---|---|---|---|---|---|
| Exact / normalized (`match_index.en_norm`, indexed) | 100% | 0.012 ms | 2.0 ms | 6.3 ms | 16.9 ms |
| FTS5 (`match_fts`, first 3 tokens, n=1,976) | 100% | 0.073 ms | 0.49 ms | — | 1.06 ms |

p95 is inflated by cold-cache first queries (~30 ms); warm lookups are ~0.01 ms. No p95 budget was fixed in the TDD — these numbers are recorded as the measured baseline.

## Deviations from TDD v1.3 (documented in code)

1. **`source_strings.id` is TEXT, not INTEGER.** TDD 4.4 prints `id INTEGER PRIMARY KEY`, but real TSV ids are text (`C0000_B381007C`). All FKs referencing it are TEXT too.
2. **FTS5 is standalone, not external-content.** The TDD's `content='match_index'` form corrupted on bulk DELETE/rebuild in this environment (`database disk image is malformed`). Standalone FTS5 (`source_id UNINDEXED, en_norm`) is populated from `match_index` by the importer and is fully rebuildable from it.
3. **Marker parser v2:** limit raised 80 → 300 chars after finding 2 fishing-prompt rows whose 112-char `~INPUT_…~` marker was swallowing visible text in v1. Those rows are now correct, e.g. `Slowly rotate to attract fish then press when you feel a bite`.

## Known limitations

- Full-table scans (`COUNT(*)` on `match_index`, `PRAGMA integrity_check`) are slow on cold disk in this VM (>15 s); indexed lookups and FTS5 counts are fast. Integrity is proven instead by the import-time `en` checksum round-trip + FTS row count.
- DB is 350 MB (source + display + norm + skeleton + FTS copies of the same text, per TDD design).
- `translations` table is empty — that is Phase 3 (offline translation pipeline), not started yet.

## Next step

Phase 3 — Offline Translation Pipeline (P0 first: UI, then Subtitle). The API-vs-local-model choice for P0 is deferred to the start of Phase 3, per the user's decision.
