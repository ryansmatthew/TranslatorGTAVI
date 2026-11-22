# TranslatorGTAVI — Real-time Vietnamese Translation for GTA VI (PS5)

A real-time Vietnamese translation system for GTA VI on PS5. The game is
English-only, so the system OCRs the English text the PS5 shows via
PS Remote Play, matches it against a pre-translated database, and draws the
Vietnamese translation as an overlay on the Android TV the game is played on.

**The game is never modified.** The TV receives HDMI directly from the PS5;
the PC only opens PS Remote Play in parallel for OCR and sends overlay data
to the TV app over the local network.

## Status

- **Phase 1 — Architecture:** done. Technical Design Document v1.3 (25 pages,
  Vietnamese) — see `docs/` note below.
- **Phase 2 — Translation DB:** done. 579,495 rows imported from the
  `psviethoa/gta6-text-en` text dump (Xbox Build 1.0.2.1); 461,633 unique
  English strings; SQLite (WAL) + FTS5; markers split; 9,233 templates.
  Exact/normalized lookup: 100% hit on a 10,000-query sample, p95 2.0 ms.
- **Phase 3 — Offline translation:** done. **443,444 unique strings**
  translated (P0 39,003 + P1 45,380 + P2 1,919 + P3 357,142), 567,918 DB rows,
  0 quarantined. All translations are status `machine` (human review pending).
- **Phase 4 — OCR prototype:** in progress. PaddleOCR (PP-OCR, English model)
  + adapter, synthetic gold dataset v1, benchmark harness. See `src/ocr/`.
- **Phase 5 — Matching Engine**, **Phase 6 — Overlay + Android TV app**,
  **Phase 7 — Realtime Integration**, **Phase 8 — Optimization:** planned.

## How it works

```
PS5 ──HDMI──▶ TV (gameplay, untouched)
 │
 └── PS Remote Play ──▶ PC: capture → change detection → PaddleOCR
                        → matching (exact → normalized → FTS5 → fuzzy,
                          context re-rank) → translation DB (SQLite)
                        ──WebSocket/LAN──▶ Android TV overlay app
```

- **No AI/VLM fallback, ever.** Unmatched or low-confidence text keeps its
  original English and is logged to `unmatched_log`. Guiding principle:
  *thà không dịch còn hơn dịch sai* — a wrong display is the worst error.
- **PaddleOCR is the only OCR engine** (English model; the game is
  English-only). OCR runs on crops of tracked regions, never the full frame.
- **Android TV app** (API 26+, minSdk 26) draws the overlay with
  `SYSTEM_ALERT_WINDOW` / `TYPE_APPLICATION_OVERLAY`, transparent,
  `FLAG_NOT_FOCUSABLE | FLAG_NOT_TOUCHABLE`.

## Repository layout

```
src/
  common/     normalize.py, markers.py — SHARED by DB import, translation
              pipeline and runtime. Changing them requires bumping
              NORMALIZE_VERSION and rebuilding match_index.
  db/         schema.sql, import_tsv.py — Phase 2 import
  pipeline/   translate_batch.py, validate.py, translators.py — Phase 3
  ocr/        adapter.py, paddle_engine.py, preprocess.py, config.py — Phase 4
  matching/   Phase 5 (planned)
tools/        load_muse_translations.py, bench_phase2.py,
              apply_p0_quality_fixes.py, probe/test_token.py (diagnostics)
tests/        pytest unit tests (OCR pre-processing + adapter)
benchmarks/
  bench_ocr.py, datasets/ocr_gold/ — Phase 4 benchmark harness + gold dataset
docs/
  reports/    Phase 2 import report, Phase 3 final + milestone reports
```

## Setup

```bash
# Translation DB (Phase 2) — needs the text dump (not in this repo)
python3 src/db/import_tsv.py --tsv <all_rows.tsv> --db data/gta6.db

# OCR environment (Phase 4)
python3 -m venv .venv
.venv/bin/pip install -r requirements-ocr.txt
.venv/bin/python -m pytest tests/ -q
.venv/bin/python -m src.ocr.demo <image.png> --region subtitle
```

On the Windows PC with an RTX 3060, install the GPU build of PaddlePaddle
instead of the CPU one (see `requirements-ocr.txt`) and pass `use_gpu=True`.

## What is NOT in this repo (and why)

- **`data/gta6.db` (455 MB) and `data/muse_batches/` (172 MB):** the built
  database and the per-chunk translation outputs are too large for git
  (GitHub blocks files over 100 MB). The DB is rebuildable: import the text
  dump with `src/db/import_tsv.py`, then load the translation batches with
  `tools/load_muse_translations.py`. The DB and batches will be shared as a
  release asset / separate download, not as git objects.
- **Gold dataset images** (`benchmarks/datasets/ocr_gold/*/images/`): PNG
  renders are build artifacts. The generator
  (`benchmarks/datasets/ocr_gold/generate_gold.py`) plus the ground-truth
  JSONs in the repo reproduce them deterministically (seed fixed).
- **The TDD PDF** (`gta-vi-realtime-vietnamese-translation-tdd.pdf`): kept
  in the project workspace; it is the design authority for all phases.
- **API keys / tokens:** never committed. `src/pipeline/translators.py`
  reads `GEMINI_API_KEY` from the environment; diagnostic tools read
  credentials from stdin and never print or store them.

## Decisions (locked)

- SQLite (WAL) + FTS5 prototype; PostgreSQL only if multiple machines or
  translators are needed (ADR-1).
- RapidFuzz only on context-filtered candidates (ADR-2).
- Chapter 14 gates: wrong-display rate ≤ 1%; ~0.5 s subtitle latency is a
  Phase 7 *measurement target*, not a commitment.
- Offline translation priority: UI, subtitle, in-game social media, item,
  description, tutorial, lore, remaining dialogue.
