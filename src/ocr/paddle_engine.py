"""PaddleOCR engine wrapper (thin).

TDD v1.3, section 7: PaddleOCR (PP-OCR, English model) is the only OCR
engine. This wrapper owns the PaddleOCR dependency and nothing else:
it takes a BGR numpy image and returns raw detection+recognition
results. All policy (pre-processing variants, best-variant selection,
coordinate mapping, logging) lives in adapter.py, so a future PP-OCR
upgrade only touches this file.

Pinned API: paddleocr 3.x (3.7.0 here) + paddlepaddle 3.3.1.
Notes on the 3.x API (verified 2026-11-22):
  - Constructor takes `device="cpu"` / `"gpu:0"` (no `use_gpu` arg),
    `text_det_thresh` / `text_det_box_thresh`,
    `text_recognition_batch_size`, and model names
    (`text_detection_model_name`, `text_recognition_model_name`)
    or `..._model_dir`. Defaults: PP-OCRv6 medium det/rec for lang=en.
  - `ocr()` is deprecated; use `predict()`. It returns a list of
    OCRResult; `result.json["res"]` holds `rec_texts`, `rec_scores`,
    `rec_polys` (4-point polygons) and `rec_boxes`.
  - CPU gotcha: Paddle 3.3 + MKLDNN crashes the detection predictor
    (`ConvertPirAttribute2RuntimeAttribute not support ... DoubleAttribute`).
    Always pass `enable_mkldnn=False` on CPU.
  - The default pipeline includes document preprocessing and textline
    orientation models — useless for game screenshots, so both are
    disabled here (faster init and inference).

Model download: PaddleOCR downloads models on first use into
`~/.paddlex/official_models`. On the user's PC this happens once.
"""
from __future__ import annotations

import logging
import time

import numpy as np

log = logging.getLogger(__name__)


class PaddleOcrEngine:
    """Thin wrapper around paddleocr.PaddleOCR (English only)."""

    def __init__(self, use_gpu: bool = False,
                 det_model: str | None = None,
                 rec_model: str | None = None,
                 det_db_thresh: float = 0.3,
                 det_db_box_thresh: float = 0.6,
                 rec_batch_num: int = 6,
                 cpu_threads: int = 4):
        self.use_gpu = use_gpu
        self.det_model = det_model
        self.rec_model = rec_model
        self.det_db_thresh = det_db_thresh
        self.det_db_box_thresh = det_db_box_thresh
        self.rec_batch_num = rec_batch_num
        self.cpu_threads = cpu_threads
        self._ocr = None

    def _ensure(self):
        if self._ocr is None:
            from paddleocr import PaddleOCR
            kwargs: dict = {
                "lang": "en",
                "device": "gpu:0" if self.use_gpu else "cpu",
                "enable_mkldnn": False,
                "cpu_threads": self.cpu_threads,
                "text_det_thresh": self.det_db_thresh,
                "text_det_box_thresh": self.det_db_box_thresh,
                "text_recognition_batch_size": self.rec_batch_num,
                # Game screenshots are not documents: skip doc
                # preprocessing and textline-orientation models.
                "use_doc_orientation_classify": False,
                "use_doc_unwarping": False,
                "use_textline_orientation": False,
            }
            if self.det_model:
                key = ("text_detection_model_dir" if "/" in self.det_model
                       else "text_detection_model_name")
                kwargs[key] = self.det_model
            if self.rec_model:
                key = ("text_recognition_model_dir" if "/" in self.rec_model
                       else "text_recognition_model_name")
                kwargs[key] = self.rec_model
            t0 = time.monotonic()
            self._ocr = PaddleOCR(**kwargs)
            log.info("PaddleOCR initialised in %.1fs (use_gpu=%s)",
                     time.monotonic() - t0, self.use_gpu)

    def ocr(self, img_bgr: np.ndarray) -> list[dict]:
        """OCR one BGR image.

        Returns a list of {"bbox": [[x, y], ...] (4 points, image coords),
        "text": str, "conf": float}. Empty list when nothing is found.
        Raises on engine failure — the caller decides retry/fallback.
        """
        self._ensure()
        predict = getattr(self._ocr, "predict", None) or self._ocr.ocr
        results = predict(img_bgr)
        lines: list[dict] = []
        if not results:
            return lines
        res = results[0].json["res"]
        for poly, text, conf in zip(res.get("rec_polys", []),
                                    res.get("rec_texts", []),
                                    res.get("rec_scores", [])):
            lines.append({
                "bbox": [[float(x), float(y)] for x, y in poly],
                "text": text,
                "conf": float(conf),
            })
        return lines
