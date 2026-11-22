"""Benchmark PaddleOCR configurations on the gold dataset (TDD 7.3).

Compares the configs in src/ocr/config.py on benchmarks/datasets/ocr_gold/v1
and reports, per screen layer and overall:
  - CER / WER vs ground truth (per line, joined with spaces)
  - match-usable rate: fraction of ground-truth lines whose normalised
    text is reproduced EXACTLY by some OCR line. This is a Phase 4 proxy
    for the TDD metric ("fraction of OCR lines the Matching Engine matches
    High") — Phase 5 refines it with the fuzzy tiers; exact match is the
    strictest High path, so this number is a lower bound.
  - latency p50 / p95 per crop (ms), per config and per layer
  - mean bbox IoU for text-matched line pairs
  - peak RSS (VRAM is n/a on a CPU-only machine — re-measure on the
    RTX 3060; the report says so explicitly)

Usage:
  .venv/bin/python benchmarks/bench_ocr.py [--configs baseline,upscale2]
      [--limit N] [--out benchmarks/reports/bench_ocr_YYYY-MM-DD.json]
"""
from __future__ import annotations

import argparse
import json
import logging
import resource
import statistics
import sys
import time
from difflib import SequenceMatcher
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from common.normalize import normalize  # noqa: E402
from ocr import CONFIGS, OcrAdapter  # noqa: E402
from ocr.paddle_engine import PaddleOcrEngine  # noqa: E402

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")
log = logging.getLogger("bench_ocr")


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1,
                           prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def cer(ref: str, hyp: str) -> float:
    if not ref:
        return 0.0 if not hyp else 1.0
    return levenshtein(ref, hyp) / max(len(ref), 1)


def wer(ref: str, hyp: str) -> float:
    rw, hw = ref.split(), hyp.split()
    if not rw:
        return 0.0 if not hw else 1.0
    return levenshtein(rw, hw) / max(len(rw), 1)


def iou(b1: list[float], b2: list[float]) -> float:
    x0 = max(b1[0], b2[0]); y0 = max(b1[1], b2[1])
    x1 = min(b1[2], b2[2]); y1 = min(b1[3], b2[3])
    inter = max(0.0, x1 - x0) * max(0.0, y1 - y0)
    a1 = (b1[2] - b1[0]) * (b1[3] - b1[1])
    a2 = (b2[2] - b2[0]) * (b2[3] - b2[1])
    return inter / max(a1 + a2 - inter, 1e-9)


def pct(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    k = (len(s) - 1) * p / 100.0
    f, c = int(k), min(int(k) + 1, len(s) - 1)
    return s[f] + (s[c] - s[f]) * (k - f)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", default=None)
    ap.add_argument("--configs", default=None,
                    help="comma-separated config names (default: all)")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    ds = Path(args.dataset) if args.dataset else (
        ROOT / "benchmarks" / "datasets" / "ocr_gold" / "v1")
    manifest = json.loads((ds / "manifest.json").read_text())
    items = manifest["items"]
    if args.limit:
        items = items[:args.limit]
    wanted = (args.configs.split(",") if args.configs else None)
    configs = [c for c in CONFIGS if wanted is None or c.name in wanted]

    engine = PaddleOcrEngine(use_gpu=False)
    results: dict = {
        "dataset": manifest["version"],
        "synthetic": manifest.get("synthetic", True),
        "date": time.strftime("%Y-%m-%d"),
        "machine": "linux VM, CPU-only (no GPU/VRAM here)",
        "note": "Images are cropped to the ground-truth text region (+24px "
                "margin) before OCR — the real pipeline never OCRs a full "
                "frame (TDD 7.1: crop exactly the tracked region).",
        "configs": {},
    }
    for cfg in configs:
        engine = PaddleOcrEngine(
            use_gpu=False, det_model=cfg.det_model, rec_model=cfg.rec_model,
            det_db_thresh=cfg.det_db_thresh,
            det_db_box_thresh=cfg.det_db_box_thresh,
            cpu_threads=cfg.cpu_threads)
        adapter = OcrAdapter(engine=engine,
                             denoise_strength=cfg.denoise_strength,
                             use_binarize=cfg.use_binarize)
        per_image = []
        for it in items:
            img = cv2.imread(str(ds / "images" / (it["id"] + ".png")))
            gt = json.loads((ds / "ground_truth" / (it["id"] + ".json")).read_text())
            # Crop to the GT text region (+24px margin), like the real
            # Region Detector would crop the tracked region.
            gx0 = max(0, min(g["bbox"][0] for g in gt["lines"]) - 24)
            gy0 = max(0, min(g["bbox"][1] for g in gt["lines"]) - 24)
            gx1 = min(img.shape[1], max(g["bbox"][2] for g in gt["lines"]) + 24)
            gy1 = min(img.shape[0], max(g["bbox"][3] for g in gt["lines"]) + 24)
            crop = img[gy0:gy1, gx0:gx1]
            t0 = time.monotonic()
            out = adapter.ocr_crop(crop, it["layer"],
                                   scale_hint=cfg.upscale_factor,
                                   crop_origin=(gx0, gy0))
            wall_ms = (time.monotonic() - t0) * 1000.0
            ocr_lines = [ln["text"] for ln in out["lines"]]
            ref_text = " ".join(g["text"] for g in gt["lines"])
            hyp_text = " ".join(ocr_lines)
            # match-usable: per GT line, exact normalised match in OCR lines
            ocr_norm = {normalize(t) for t in ocr_lines}
            ocr_joined = normalize(hyp_text)
            matched = sum(
                1 for g in gt["lines"]
                if normalize(g["text"]) in ocr_norm
                or normalize(g["text"]) in ocr_joined)
            # IoU for the best text-similar pair per GT line
            ious = []
            for g in gt["lines"]:
                best, best_r = None, 0.0
                for ln in out["lines"]:
                    r = SequenceMatcher(None, g["text"], ln["text"]).ratio()
                    if r > best_r:
                        best, best_r = ln, r
                if best and best_r > 0.5:
                    ious.append(iou(g["bbox"], best["bbox"]))
            per_image.append({
                "id": it["id"], "layer": it["layer"],
                "resolution": it["resolution"],
                "cer": cer(ref_text, hyp_text),
                "wer": wer(ref_text, hyp_text),
                "match_usable": matched / max(len(gt["lines"]), 1),
                "ms": out["ocr_time_ms"], "wall_ms": round(wall_ms, 1),
                "variant": out["variant"],
                "mean_iou": float(np.mean(ious)) if ious else 0.0,
                "n_ocr_lines": len(ocr_lines),
                "n_gt_lines": len(gt["lines"]),
            })
            log.info("%s %s cer=%.3f wer=%.3f usable=%.2f ms=%.0f",
                     cfg.name, it["id"], per_image[-1]["cer"],
                     per_image[-1]["wer"], per_image[-1]["match_usable"],
                     per_image[-1]["ms"])
        layers: dict[str, dict] = {}
        for layer in sorted({p["layer"] for p in per_image}):
            sub = [p for p in per_image if p["layer"] == layer]
            layers[layer] = {
                "n": len(sub),
                "cer": round(float(np.mean([p["cer"] for p in sub])), 4),
                "wer": round(float(np.mean([p["wer"] for p in sub])), 4),
                "match_usable": round(float(np.mean([p["match_usable"] for p in sub])), 4),
                "p50_ms": round(pct([p["ms"] for p in sub], 50), 1),
                "p95_ms": round(pct([p["ms"] for p in sub], 95), 1),
                "mean_iou": round(float(np.mean([p["mean_iou"] for p in sub])), 3),
            }
        results["configs"][cfg.name] = {
            "n_images": len(per_image),
            "cer": round(float(np.mean([p["cer"] for p in per_image])), 4),
            "wer": round(float(np.mean([p["wer"] for p in per_image])), 4),
            "match_usable": round(float(np.mean([p["match_usable"] for p in per_image])), 4),
            "p50_ms": round(pct([p["ms"] for p in per_image], 50), 1),
            "p95_ms": round(pct([p["ms"] for p in per_image], 95), 1),
            "mean_iou": round(float(np.mean([p["mean_iou"] for p in per_image])), 3),
            "peak_rss_mb": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1),
            "layers": layers,
            "per_image": per_image,
        }
        c = results["configs"][cfg.name]
        print(f"== {cfg.name}: CER={c['cer']} WER={c['wer']} "
              f"usable={c['match_usable']} p50={c['p50_ms']}ms "
              f"p95={c['p95_ms']}ms IoU={c['mean_iou']} "
              f"peakRSS={c['peak_rss_mb']}MB")
    out_path = Path(args.out) if args.out else (
        ROOT / "benchmarks" / "reports" /
        f"bench_ocr_{time.strftime('%Y-%m-%d')}.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print(f"results -> {out_path}")


if __name__ == "__main__":
    main()
