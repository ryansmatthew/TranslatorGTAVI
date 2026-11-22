# OCR module — PaddleOCR adapter (Phase 4, TDD Ch. 7)

PaddleOCR (PP-OCR, English model) is the only OCR engine. The adapter keeps
a stable interface so Matching/Renderer never depend on PaddleOCR internals.

## Layout

- `preprocess.py` — upscale 2x (small-text regions), denoise, CLAHE contrast,
  adaptive binarisation; builds the candidate variants (7.1).
- `paddle_engine.py` — thin PaddleOCR wrapper, owns the dependency.
- `adapter.py` — stable interface (7.2): `ocr_crop(crop, region_type,
  scale_hint, frame_id, crop_origin)` → `{"lines": [{text, bbox (frame
  coords), conf, line_id}], "ocr_time_ms", "variant"}`. OCRs each variant,
  keeps the best by mean confidence, maps bboxes back to frame coords.
- `config.py` — benchmark configurations compared in Phase 4 (7.3).
- `demo.py` — standalone run on one image (no DB, no matching).

## Install

```bash
python -m venv .venv
.venv/bin/pip install -r requirements-ocr.txt
```

First run downloads the English det/rec models (~15 MB) into `~/.paddleocr`.

On the user's PC (Windows, RTX 3060) install the GPU build of PaddlePaddle
instead of the CPU one and pass `use_gpu=True` (demo: `--gpu`). The
benchmark numbers in this repo were measured CPU-only in a Linux VM — GPU
latency/VRAM must be re-measured on the RTX 3060 before any latency claim.

## Tests

```bash
.venv/bin/python -m pytest tests/test_preprocess.py tests/test_adapter.py -q
```

## Benchmark

```bash
.venv/bin/python benchmarks/bench_ocr.py
```

Runs every config in `config.py` over `benchmarks/datasets/ocr_gold/v1`
and writes `benchmarks/reports/bench_ocr_<date>.json`. The gold dataset is
**synthetic v1** (rendered from real `en_display` strings, see
`benchmarks/datasets/ocr_gold/generate_gold.py`) — a stand-in until real
Remote Play frames exist. Real frames replace/extend v1 without changing
the benchmark code.
