"""Marker parser — the single module for import / translation / validation / display.
TDD v1.3, Appendix A. Version: 1.0

Marker forms found in all_rows.tsv (examples from the dump):
  ~sl:0:2.41~            subtitle timing — never shown as text
  ~INPUT_AIM~            button prompt — shown as a button icon, not text
  ~n~                    newline, ~b~ bold, ~s~ / ~o~ style, ~case_lower~ / ~case_end~
  ~BLIP_EMOJI_FIRE~      in-game emoji/blip — shown as icon
  ~1~, ~2~               numbered placeholders -> template slots
  ~case_lower~s~case_end~  case directive wrapping a literal

Rules:
  * en_display = en with markers removed, except ~n~ -> newline,
    and ~<digit>~ placeholders kept verbatim (they become template slots).
  * markers = JSON list of {marker, start, end, kind} in original order.
  * Unknown ~...~ tokens are NOT silently dropped: they are recorded
    with kind='unknown' and removed from en_display, and the importer
    counts them so they can be reviewed.
  * No marker is ever translated or reordered.
"""
import json
import re

MARKER_RE = re.compile(r"~[^~\n]{1,300}~")
MARKERS_VERSION = 2
# v2: limit raised 80 -> 300 chars. v1 swallowed visible text in 2 rows
# whose ~INPUT_...~ prompt is 112 chars long
# ('Slowly rotate ~INPUT_MINIGAME_FISHING_RIGHT_AXIS_X,...~ to attract fish...').

def _kind(token: str) -> str:
    inner = token[1:-1]
    if inner.startswith("sl:") or inner.startswith("lr:"):
        return "timing"
    if inner.startswith("INPUT_") or inner.startswith("INPUTGROUP_") or inner.startswith("ACTION_"):
        return "input"
    if inner.startswith("BLIP_") or inner.startswith("LIP_EMOJI"):
        return "blip"
    if inner.startswith("COLOR_") or inner.startswith("HUD_COLOUR"):
        return "format"
    if inner in ("n", "b", "s", "o", "u", "t", "m", "e", "d", "f", "rp", "tone", "c", "a"):
        return "format"
    if inner in ("case_lower", "case_end", "case_upper"):
        return "case"
    if re.fullmatch(r"\d+", inner):
        return "placeholder"
    if re.fullmatch(r"\d+[a-z$]+", inner):
        # ~1b~, ~1$~, ~2b~, ~1T~, ~1ew~, ~1et~, ~1es~ — numbered placeholder with a suffix
        return "placeholder"
    if inner == "$":
        return "placeholder"
    return "unknown"

def split_markers(en: str):
    """Return (en_display, markers_json, unknown_count)."""
    if not en:
        return "", "[]", 0
    markers = []
    out = []
    last = 0
    unknown = 0
    for m in MARKER_RE.finditer(en):
        token = m.group(0)
        kind = _kind(token)
        if kind == "unknown":
            unknown += 1
        markers.append({"marker": token, "start": m.start(), "end": m.end(), "kind": kind})
        out.append(en[last:m.start()])
        if token == "~n~":
            out.append("\n")
        elif kind == "placeholder":
            # keep the placeholder in the display text; template code
            # turns it into a slot later
            out.append(token)
        # all other markers: emit nothing (button icon / bold / emoji /
        # timing are not readable text for OCR matching)
        last = m.end()
    out.append(en[last:])
    display = "".join(out)
    # collapse the whitespace left behind by removed markers, but keep
    # real newlines from ~n~
    display = re.sub(r"[ \t\r\f\v]+", " ", display)
    display = re.sub(r"\n\s+", "\n", display)
    display = re.sub(r"\s+\n", "\n", display)
    display = display.strip()
    return display, json.dumps(markers, ensure_ascii=False), unknown
