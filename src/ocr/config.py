"""Benchmark configurations for PaddleOCR tuning (TDD 7.3).

The benchmark does NOT re-choose the engine — it compares PaddleOCR
configurations (upscale on/off, denoise, binarise, detection thresholds)
and picks the one with the highest match-usable rate within the latency
budget of Chapter 11, separately per screen layer. The winning config is
recorded in the benchmark report, not hard-coded here.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OcrConfig:
    name: str
    upscale_factor: float = 1.0   # 1.0 = no upscale (adapter default applies per region when None)
    denoise_strength: float = 1.0
    use_binarize: bool = True
    det_db_thresh: float = 0.3
    det_db_box_thresh: float = 0.6
    det_model: str | None = None  # None = PaddleOCR default (PP-OCRv6 medium for en)
    rec_model: str | None = None
    # 1 thread was FASTER than 4 on this shared-CPU VM (16.9s vs 21.3s per
    # subtitle-band predict — thread thrashing). On the GPU PC this is moot.
    cpu_threads: int = 1


# Configs compared by benchmarks/bench_ocr.py. "baseline" is raw PaddleOCR
# with no pre-processing at all — the lower bound from TDD 7.
CONFIGS: list[OcrConfig] = [
    OcrConfig(name="baseline", upscale_factor=1.0,
              denoise_strength=0.0, use_binarize=False),
    OcrConfig(name="upscale2", upscale_factor=2.0,
              denoise_strength=0.0, use_binarize=False),
    OcrConfig(name="upscale2+denoise", upscale_factor=2.0,
              denoise_strength=1.0, use_binarize=False),
    OcrConfig(name="upscale2+denoise+binarize", upscale_factor=2.0,
              denoise_strength=1.0, use_binarize=True),
    OcrConfig(name="upscale2+binarize", upscale_factor=2.0,
              denoise_strength=0.0, use_binarize=True),
    OcrConfig(name="mobile-upscale2+denoise", upscale_factor=2.0,
              denoise_strength=1.0, use_binarize=False,
              det_model="PP-OCRv5_mobile_det",
              rec_model="PP-OCRv5_mobile_rec"),
]
