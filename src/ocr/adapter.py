"""OCR adapter — the stable interface between PaddleOCR and the rest of
the system.

TDD v1.3, section 7.2 (OCR Worker interface):

  Input : crop image, region_type, scale_hint, frame_id
  Output: [{ text, bbox (in ORIGINAL frame coordinates), conf, line_id }]
          + ocr_time_ms

The adapter keeps this format fixed so Matching and Renderer never
depend on PaddleOCR internals. Responsibilities:
  - run the pre-processing variants from preprocess.py (7.1),
  - OCR each variant, keep the best by mean line confidence,
  - map bboxes from crop coordinates back to original-frame coordinates
    (accounting for crop offset AND upscale factor),
  - emit one structured log line per crop (frame_id, region, variant
    chosen, lines, mean conf, ms) — every module must have logs.
"""
from __future__ import annotations

import logging
import time

import numpy as np

from . import preprocess
from .paddle_engine import PaddleOcrEngine

log = logging.getLogger(__name__)

# region_type -> upscale factor when the caller gives no scale_hint.
DEFAULT_UPSCALE = {
    "subtitle": 1.0,
    "menu": 1.0,
    "hud": 2.0,
    "phone": 2.0,
    "notification": 2.0,
    "description": 1.0,
}


class OcrAdapter:
    """Stable OCR interface. `engine` may be injected (tests / mocks)."""

    def __init__(self, engine: PaddleOcrEngine | None = None,
                 use_gpu: bool = False,
                 denoise_strength: float = 1.0,
                 use_binarize: bool = True,
                 **engine_kwargs):
        self.engine = engine or PaddleOcrEngine(use_gpu=use_gpu,
                                                **engine_kwargs)
        self.denoise_strength = denoise_strength
        self.use_binarize = use_binarize

    def ocr_crop(self, crop_bgr: np.ndarray, region_type: str,
                 scale_hint: float | None = None,
                 frame_id: int = 0,
                 crop_origin: tuple[int, int] = (0, 0)) -> dict:
        """OCR one tracked-region crop.

        crop_bgr: BGR image of the region (already cropped from the frame).
        region_type: subtitle|menu|hud|phone|notification|description.
        scale_hint: upscale factor override; None = default per region.
        crop_origin: (x, y) of the crop's top-left corner in the frame.
        Returns {"lines": [...], "ocr_time_ms": float, "variant": str}.
        bbox coordinates are in ORIGINAL frame pixels.
        """
        t0 = time.monotonic()
        factor = (scale_hint if scale_hint is not None
                  else DEFAULT_UPSCALE.get(region_type, 1.0))
        variants = preprocess.variants_for(
            crop_bgr, region_type,
            upscale_factor=factor,
            denoise_strength=self.denoise_strength,
            use_binarize=self.use_binarize)
        best_lines: list[dict] = []
        best_conf = -1.0
        best_variant = variants[0][0]
        for name, img in variants:
            try:
                raw = self.engine.ocr(img)
            except Exception:
                log.exception("OCR failed on variant %s (frame %s)",
                              name, frame_id)
                continue
            if not raw:
                continue
            mean_conf = sum(r["conf"] for r in raw) / len(raw)
            if mean_conf > best_conf:
                best_conf = mean_conf
                best_variant = name
                best_lines = raw
        ms = (time.monotonic() - t0) * 1000.0
        lines = []
        ox, oy = crop_origin
        for i, r in enumerate(best_lines):
            pts = np.array(r["bbox"], dtype=float)
            # Undo the upscale, then add the crop offset.
            pts = pts / factor
            pts[:, 0] += ox
            pts[:, 1] += oy
            x0, y0 = pts.min(axis=0)
            x1, y1 = pts.max(axis=0)
            lines.append({
                "text": r["text"],
                "bbox": [round(float(x0), 1), round(float(y0), 1),
                         round(float(x1), 1), round(float(y1), 1)],
                "conf": round(r["conf"], 4),
                "line_id": i,
            })
        log.info("ocr frame=%s region=%s variant=%s lines=%d "
                 "mean_conf=%.3f ms=%.0f",
                 frame_id, region_type, best_variant, len(lines),
                 best_conf if best_conf >= 0 else 0.0, ms)
        return {"lines": lines, "ocr_time_ms": round(ms, 1),
                "variant": best_variant}

    def ocr_frame_region(self, frame_bgr: np.ndarray,
                         bbox: tuple[int, int, int, int],
                         region_type: str, frame_id: int = 0) -> dict:
        """Convenience: crop a region out of a full frame, then OCR it."""
        x0, y0, x1, y1 = bbox
        crop = frame_bgr[y0:y1, x0:x1]
        return self.ocr_crop(crop, region_type, frame_id=frame_id,
                             crop_origin=(x0, y0))
