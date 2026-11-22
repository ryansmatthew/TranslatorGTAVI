"""Generate the Phase 4 OCR gold dataset (v1, synthetic).

TDD 7.3: the benchmark dataset is real Remote Play frames when available,
plus public gameplay video while waiting. No real GTA VI frames exist in
this environment yet, so v1 is SYNTHETIC — rendered from real `en_display`
strings taken from gta6.db (the exact text the game shows, markers already
stripped at import), laid out per screen layer with the TDD-mandated
conditions (subtitle day/night + light/dark background, menu, HUD, phone +
social, notification, description) at both 1080p and 720p, with Remote
Play compression artefacts simulated on the 720p renders (downscale +
JPEG q68 + light blur).

This is a clearly-labelled stand-in, NOT a claim about real Remote Play
frames: the report must say so, and real frames replace/extend v1 on the
user's PC (Phase 7) without changing the benchmark code.

Deterministic (seed fixed) and versioned: regenerating with the same
version reproduces the same images and ground truth.

Layout: benchmarks/datasets/ocr_gold/v1/
  images/<id>.png          rendered frame (the OCR input = the crop)
  ground_truth/<id>.json   {"image", "layer", "resolution", "lines": [{"text", "bbox"}]}
  manifest.json            version, seed, counts, generator
"""
from __future__ import annotations

import argparse
import json
import random
import sqlite3
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

VERSION = "v1"
SEED = 20261122

FONT_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# layer -> (count per resolution, category, min_len, max_len)
LAYERS = {
    "subtitle_day":   ("subtitle",   25, 90, 4),
    "subtitle_night": ("subtitle",   25, 90, 4),
    "menu":           ("ui",          3, 28, 6),
    "hud":            ("ui",          3, 30, 6),
    "phone":          ("dialogue",   12, 55, 6),
    "notification":   ("dialogue",   10, 45, 6),
    "description":    ("description", 60, 150, 6),
}


def sample_texts(db: Path, category: str, lo: int, hi: int, n: int,
                 rng: random.Random) -> list[str]:
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    rows = con.execute(
        "SELECT en_display FROM source_strings "
        "WHERE category=? AND en_display IS NOT NULL AND en_display!='' "
        "AND LENGTH(en_display) BETWEEN ? AND ? "
        "AND en_display NOT LIKE '%http%' AND en_display NOT LIKE '%@%' "
        "ORDER BY RANDOM() LIMIT ?",
        (category, lo, hi, n * 4)).fetchall()
    con.close()
    texts = [r[0] for r in rows]
    rng.shuffle(texts)
    return texts[:n]


def _bg(w: int, h: int, kind: str, rng: random.Random) -> Image.Image:
    """Simple busy background: vertical gradient + soft blobs."""
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    if kind == "day":
        top, bot = (150, 180, 200), (90, 110, 130)
    elif kind == "night":
        top, bot = (18, 22, 34), (8, 10, 18)
    else:
        top, bot = (40, 44, 52), (20, 22, 30)
    for y in range(h):
        t = y / h
        d.line([(0, y), (w, y)],
               fill=tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    # a few soft darker/lighter blobs to break up flatness
    for _ in range(6):
        x, y = rng.randint(0, w), rng.randint(0, h)
        r = rng.randint(80, 300)
        blob = Image.new("RGB", (r * 2, r * 2), (0, 0, 0))
        bd = ImageDraw.Draw(blob)
        bd.ellipse([0, 0, r * 2, r * 2],
                   fill=(rng.randint(0, 60), rng.randint(0, 60), rng.randint(0, 70)))
        blob = blob.filter(ImageFilter.GaussianBlur(40))
        mask = Image.new("L", (r * 2, r * 2), 0)
        md = ImageDraw.Draw(mask)
        md.ellipse([0, 0, r * 2, r * 2], fill=90)
        img.paste(blob, (x - r, y - r), mask)
    return img


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


def _wrap(draw: ImageDraw.ImageDraw, text: str, font, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render(layer: str, texts: list[str], w: int, h: int,
           rng: random.Random) -> tuple[Image.Image, list[dict]]:
    """Render one gold image. Returns (image, ground-truth lines)."""
    kind = "day" if layer == "subtitle_day" else (
        "night" if layer == "subtitle_night" else "dark")
    img = _bg(w, h, kind, rng)
    d = ImageDraw.Draw(img, "RGBA")
    gt: list[dict] = []
    scale = w / 1920.0

    if layer.startswith("subtitle"):
        fs = int(44 * scale)
        font = _font(fs, bold=True)
        band_h = int(150 * scale)
        y0 = h - band_h - int(40 * scale)
        d.rectangle([0, y0, w, y0 + band_h], fill=(0, 0, 0, 150))
        lines = []
        for t in texts:
            lines += _wrap(d, t, font, int(w * 0.8))
        lh = int(fs * 1.35)
        y = y0 + (band_h - lh * len(lines)) // 2
        for ln in lines:
            tw = d.textlength(ln, font=font)
            x = (w - tw) / 2
            d.text((x + 2, y + 2), ln, font=font, fill=(0, 0, 0, 220))
            d.text((x, y), ln, font=font, fill=(255, 255, 255, 255))
            gt.append({"text": ln, "bbox": [round(x), round(y),
                                             round(x + tw), round(y + fs)]})
            y += lh

    elif layer == "menu":
        fs = int(40 * scale)
        font = _font(fs)
        font_b = _font(fs, bold=True)
        pw, ph = int(620 * scale), int((len(texts) + 2) * fs * 1.5)
        x0, y0 = int(120 * scale), (h - ph) // 2
        d.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(10, 12, 16, 225))
        d.text((x0 + int(30 * scale), y0 + int(18 * scale)), "MENU",
               font=font_b, fill=(255, 210, 60, 255))
        y = y0 + int(80 * scale)
        for i, t in enumerate(texts):
            if i == 1:
                d.rectangle([x0, y, x0 + pw, y + int(fs * 1.3)],
                            fill=(255, 255, 255, 40))
            d.text((x0 + int(30 * scale), y), t, font=font,
                   fill=(255, 255, 255, 255))
            gt.append({"text": t, "bbox": [x0 + int(30 * scale), y,
                                           x0 + int(30 * scale) + int(d.textlength(t, font=font)),
                                           y + fs]})
            y += int(fs * 1.5)

    elif layer == "hud":
        fs = int(30 * scale)
        font = _font(fs, bold=True)
        x, y = int(60 * scale), int(50 * scale)
        for t in texts:
            tw = d.textlength(t, font=font)
            d.text((x + 2, y + 2), t, font=font, fill=(0, 0, 0, 255))
            d.text((x, y), t, font=font, fill=(255, 255, 255, 255))
            gt.append({"text": t, "bbox": [x, y, x + int(tw), y + fs]})
            y += int(fs * 1.5)

    elif layer == "phone":
        fs = int(26 * scale)
        font = _font(fs)
        pw, ph = int(480 * scale), int(800 * scale)
        x0, y0 = w - pw - int(80 * scale), (h - ph) // 2
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=int(36 * scale),
                            fill=(12, 14, 18, 245), outline=(80, 80, 90, 255),
                            width=3)
        y = y0 + int(40 * scale)
        for t in texts:
            lines = _wrap(d, t, font, pw - int(60 * scale))
            for ln in lines:
                d.text((x0 + int(30 * scale), y), ln, font=font,
                       fill=(235, 235, 235, 255))
                gt.append({"text": ln, "bbox": [x0 + int(30 * scale), y,
                                                x0 + int(30 * scale) + int(d.textlength(ln, font=font)),
                                                y + fs]})
                y += int(fs * 1.4)
            y += int(18 * scale)

    elif layer == "notification":
        fs = int(30 * scale)
        font = _font(fs)
        lines = []
        for t in texts:
            lines += _wrap(d, t, font, int(520 * scale))
        bw = int(600 * scale)
        bh = int(len(lines) * fs * 1.4 + 30 * scale)
        x0, y0 = w - bw - int(60 * scale), int(50 * scale)
        d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=int(14 * scale),
                            fill=(0, 0, 0, 180))
        y = y0 + int(15 * scale)
        for ln in lines:
            d.text((x0 + int(20 * scale), y), ln, font=font,
                   fill=(255, 255, 255, 255))
            gt.append({"text": ln, "bbox": [x0 + int(20 * scale), y,
                                            x0 + int(20 * scale) + int(d.textlength(ln, font=font)),
                                            y + fs]})
            y += int(fs * 1.4)

    elif layer == "description":
        fs = int(34 * scale)
        font = _font(fs)
        pw = int(1100 * scale)
        x0 = (w - pw) // 2
        lines = []
        for t in texts:
            lines += _wrap(d, t, font, pw - int(80 * scale))
        bh = int(len(lines) * fs * 1.5 + 60 * scale)
        y0 = (h - bh) // 2
        d.rectangle([x0, y0, x0 + pw, y0 + bh], fill=(0, 0, 0, 190))
        y = y0 + int(30 * scale)
        for ln in lines:
            d.text((x0 + int(40 * scale), y), ln, font=font,
                   fill=(240, 240, 230, 255))
            gt.append({"text": ln, "bbox": [x0 + int(40 * scale), y,
                                            x0 + int(40 * scale) + int(d.textlength(ln, font=font)),
                                            y + fs]})
            y += int(fs * 1.5)

    return img, gt


def compress_720(img: Image.Image) -> Image.Image:
    """Simulate Remote Play 720p: downscale, JPEG q68, light blur."""
    small = img.resize((1280, 720), Image.LANCZOS)
    buf = io.BytesIO()
    small.save(buf, format="JPEG", quality=68)
    out = Image.open(io.BytesIO(buf.getvalue())).convert("RGB")
    return out.filter(ImageFilter.GaussianBlur(0.6))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[3]
    db = Path(args.db) if args.db else root / "data" / "gta6.db"
    out = Path(args.out) if args.out else (
        root / "benchmarks" / "datasets" / "ocr_gold" / VERSION)
    (out / "images").mkdir(parents=True, exist_ok=True)
    (out / "ground_truth").mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    manifest: dict = {"version": VERSION, "seed": args.seed,
                      "synthetic": True,
                      "source": "en_display strings from gta6.db, rendered with Liberation Sans",
                      "note": "SYNTHETIC stand-in for real Remote Play frames (none available yet). "
                              "Replace/extend with real frames on the user PC; benchmark code unchanged.",
                      "items": []}
    idx = 0
    for layer, (cat, lo, hi, n) in LAYERS.items():
        texts = sample_texts(db, cat, lo, hi, n, rng)
        # subtitle renders 2 lines per image from 2 texts; others one text each
        groups = [texts[i:i + 2] for i in range(0, len(texts), 2)] \
            if layer.startswith("subtitle") else [[t] for t in texts]
        for gi, group in enumerate(groups):
            for res, (w, h) in (("1080p", (1920, 1080)), ("720p", (1280, 720))):
                img, gt = render(layer, group, w, h, rng)
                if res == "720p":
                    img = compress_720(img)
                    # bboxes scale 1920->1280 for the 720p render: render() already
                    # drew at 1280, so gt is already in 720p coords. OK.
                name = f"{layer}_{gi:02d}_{res}"
                img.save(out / "images" / f"{name}.png")
                (out / "ground_truth" / f"{name}.json").write_text(
                    json.dumps({"image": f"{name}.png", "layer": layer,
                                "resolution": res, "lines": gt},
                               ensure_ascii=False, indent=1), encoding="utf-8")
                manifest["items"].append(
                    {"id": name, "layer": layer, "resolution": res,
                     "n_lines": len(gt)})
                idx += 1
    manifest["total_images"] = idx
    (out / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"gold {VERSION}: {idx} images -> {out}")
    from collections import Counter
    print(Counter((i["layer"], i["resolution"]) for i in manifest["items"]))


if __name__ == "__main__":
    main()
