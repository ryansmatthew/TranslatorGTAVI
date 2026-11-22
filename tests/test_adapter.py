"""Unit tests for src/ocr/adapter.py with a fake engine (no PaddleOCR)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ocr.adapter import OcrAdapter


class FakeEngine:
    """Returns one fixed line; bbox in the (upscaled) variant coords."""

    def __init__(self, lines):
        self.lines = lines

    def ocr(self, img):
        return self.lines


def _img():
    return np.zeros((100, 200, 3), dtype=np.uint8)


def test_bbox_mapped_back_to_frame_coords():
    # Engine "sees" the 2x-upscaled variant: bbox (20,10)-(100,30) in
    # variant coords == (10,5)-(50,15) in crop coords; crop sits at
    # (1000, 500) in the frame.
    eng = FakeEngine([{"bbox": [[20, 10], [100, 10], [100, 30], [20, 30]],
                       "text": "Hello", "conf": 0.9}])
    ad = OcrAdapter(engine=eng, denoise_strength=0.0, use_binarize=False)
    out = ad.ocr_crop(_img(), "phone", frame_id=7, crop_origin=(1000, 500))
    assert len(out["lines"]) == 1
    ln = out["lines"][0]
    assert ln["text"] == "Hello"
    assert ln["bbox"] == [1010.0, 505.0, 1050.0, 515.0]
    assert ln["line_id"] == 0
    assert out["ocr_time_ms"] >= 0


def test_best_variant_by_confidence():
    class TwoVariantEngine:
        def __init__(self):
            self.calls = 0

        def ocr(self, img):
            self.calls += 1
            # First call (base) is weak, second (binarized) is strong.
            conf = 0.5 if self.calls == 1 else 0.95
            return [{"bbox": [[0, 0], [10, 0], [10, 10], [0, 10]],
                     "text": "Hi", "conf": conf}]

    eng = TwoVariantEngine()
    ad = OcrAdapter(engine=eng, denoise_strength=0.0, use_binarize=True)
    out = ad.ocr_crop(_img(), "subtitle")
    assert out["variant"] == "binarized"
    assert out["lines"][0]["conf"] == 0.95


def test_no_text_returns_empty_lines():
    ad = OcrAdapter(engine=FakeEngine([]), denoise_strength=0.0,
                    use_binarize=False)
    out = ad.ocr_crop(_img(), "menu")
    assert out["lines"] == []
    assert out["variant"] == "base"


def test_engine_failure_does_not_crash():
    class Boom:
        def ocr(self, img):
            raise RuntimeError("boom")

    ad = OcrAdapter(engine=Boom(), denoise_strength=0.0, use_binarize=False)
    out = ad.ocr_crop(_img(), "hud")
    assert out["lines"] == []
