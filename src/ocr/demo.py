"""Standalone OCR demo: run the adapter on one image and print lines.

Usage (from the project root, venv active):
  python -m src.ocr.demo benchmarks/datasets/ocr_gold/v1/images/subtitle_night_00_1080p.png --region subtitle
  python -m src.ocr.demo <image> --region phone --gpu   (on the user's RTX 3060 PC)

No DB, no matching — just OCR, per the "each module runs standalone" rule.
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

import cv2

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ocr import OcrAdapter  # noqa: E402

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(name)s %(message)s")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("image")
    ap.add_argument("--region", default="subtitle",
                    choices=["subtitle", "menu", "hud", "phone",
                             "notification", "description"])
    ap.add_argument("--gpu", action="store_true")
    ap.add_argument("--no-binarize", action="store_true")
    args = ap.parse_args()
    img = cv2.imread(args.image)
    if img is None:
        raise SystemExit(f"cannot read image: {args.image}")
    adapter = OcrAdapter(use_gpu=args.gpu, use_binarize=not args.no_binarize)
    out = adapter.ocr_crop(img, args.region, frame_id=0)
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
