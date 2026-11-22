"""Pre-processing for PaddleOCR on Remote Play frames.

TDD v1.3, section 7.1. Mandatory steps before PaddleOCR:
  1. Crop exactly the tracked region (never OCR the full screen),
     upscale 2x for small-text regions (phone, HUD), keep aspect ratio.
  2. Local contrast boost; try both the original and a binarised
     version for subtitle regions with a semi-transparent background,
     pick the result by OCR confidence.
  3. Light compression-noise removal for the Remote Play source
     (default pre-processing, since Remote Play is the main source);
     the filter strength is tuned in the Phase 4 benchmark (7.3).

This module is pure image processing — no PaddleOCR dependency, so it
is unit-testable on its own. All functions take/return BGR numpy arrays
(OpenCV convention) unless noted.
"""
from __future__ import annotations

import cv2
import numpy as np


def upscale(img: np.ndarray, factor: float = 2.0) -> np.ndarray:
    """Upscale keeping aspect ratio (INTER_CUBIC for text)."""
    if factor == 1.0:
        return img
    h, w = img.shape[:2]
    return cv2.resize(img, (int(w * factor), int(h * factor)),
                      interpolation=cv2.INTER_CUBIC)


def denoise(img: np.ndarray, strength: float = 1.0) -> np.ndarray:
    """Light compression-noise removal.

    Bilateral filter: smooths flat areas (video-compression blocking)
    while keeping text edges. strength 0 disables, 1.0 is the default.
    """
    if strength <= 0:
        return img
    d = 5
    sigma_color = 35.0 * strength
    sigma_space = 35.0 * strength
    return cv2.bilateralFilter(img, d, sigma_color, sigma_space)


def enhance_contrast(img: np.ndarray) -> np.ndarray:
    """Local contrast boost via CLAHE on the L channel (LAB space)."""
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2BGR)


def binarize(img: np.ndarray) -> np.ndarray:
    """Adaptive-threshold binarisation (for semi-transparent subtitle bands).

    Returns a 3-channel BGR image (black text on white) so the OCR
    engine sees the same format as the other variants.
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bw = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 10)
    return cv2.cvtColor(bw, cv2.COLOR_GRAY2BGR)


# Regions whose text is small enough that 2x upscale is mandatory (7.1).
SMALL_TEXT_REGIONS = {"phone", "hud", "notification"}


def variants_for(img: np.ndarray, region_type: str,
                 upscale_factor: float = 2.0,
                 denoise_strength: float = 1.0,
                 use_binarize: bool = True) -> list[tuple[str, np.ndarray]]:
    """Build the candidate pre-processed variants for one crop.

    Returns a list of (variant_name, image). The caller OCRs each
    variant and keeps the best by mean OCR confidence (7.1).
    Order matters: the first variant is the default if confidences tie.
    The passed upscale_factor is applied as-is — the caller (adapter)
    resolves the per-region default; this function must not second-guess
    it, or the adapter's bbox un-scaling (which divides by the same
    factor) breaks.
    """
    base = upscale(img, upscale_factor)
    if denoise_strength > 0:
        base = denoise(base, denoise_strength)
    base = enhance_contrast(base)
    variants = [("base", base)]
    if use_binarize:
        variants.append(("binarized", binarize(base)))
    return variants
