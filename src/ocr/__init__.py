"""OCR module: PaddleOCR adapter + pre-processing (TDD Ch. 7)."""
from .adapter import OcrAdapter
from .config import CONFIGS, OcrConfig
from .paddle_engine import PaddleOcrEngine

__all__ = ["OcrAdapter", "OcrConfig", "CONFIGS", "PaddleOcrEngine"]
