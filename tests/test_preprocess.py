"""Unit tests for src/ocr/preprocess.py (no PaddleOCR needed)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ocr import preprocess


def _img(h=60, w=120):
    rng = np.random.default_rng(0)
    return rng.integers(0, 255, (h, w, 3), dtype=np.uint8)


def test_upscale_keeps_aspect_and_scales():
    img = _img()
    out = preprocess.upscale(img, 2.0)
    assert out.shape == (120, 240, 3)
    assert preprocess.upscale(img, 1.0).shape == img.shape


def test_denoise_strength_zero_is_identity():
    img = _img()
    assert np.array_equal(preprocess.denoise(img, 0.0), img)
    assert preprocess.denoise(img, 1.0).shape == img.shape


def test_enhance_contrast_shape():
    assert preprocess.enhance_contrast(_img()).shape == (60, 120, 3)


def test_binarize_is_black_and_white():
    bw = preprocess.binarize(_img())
    assert bw.shape == (60, 120, 3)
    assert set(np.unique(bw)).issubset({0, 255})


def test_variants_small_text_upscales_and_binarizes():
    img = _img()
    variants = preprocess.variants_for(img, "phone", upscale_factor=2.0,
                                       denoise_strength=1.0, use_binarize=True)
    names = [n for n, _ in variants]
    assert names == ["base", "binarized"]
    assert variants[0][1].shape == (120, 240, 3)


def test_variants_apply_passed_upscale_factor():
    img = _img()
    variants = preprocess.variants_for(img, "subtitle", upscale_factor=2.0,
                                       denoise_strength=0.0, use_binarize=False)
    assert [n for n, _ in variants] == ["base"]
    # The passed factor is applied as-is (adapter divides bboxes by the
    # same factor); a region-based override here used to break IoU.
    assert variants[0][1].shape == (120, 240, 3)
