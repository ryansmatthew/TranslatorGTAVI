"""Shared normalisation — ONE function for both sides (DB import AND runtime OCR).
TDD v1.3, section 5.3. Version: 1.0
Two different versions of this function on the two sides is the single
most serious bug this system can have, so import and runtime MUST both
import from here. Changing this file requires bumping NORMALIZE_VERSION
and rebuilding match_index.

en_norm:  NFKC, lower-case, curly quotes / long dashes / NBSP unified,
          whitespace collapsed, leading/trailing punctuation stripped.
          Internal punctuation is KEPT (the "norm" level).
en_skel:  from en_norm, punctuation -> space, then dynamic values
          (money, time, numbers, ~N~ placeholders) -> typed slots.
          This is the "skeleton" level used by template matching (5.5).
"""
import re
import unicodedata

NORMALIZE_VERSION = 1

_MONEY_RE = re.compile(r"\$\s?\d[\d,]*(\.\d+)?")
_TIME_RE = re.compile(r"\b\d{1,2}:\d{2}(?::\d{2})?\s?(?:am|pm)?\b", re.I)
_NUMBER_RE = re.compile(r"\b\d[\d,]*(\.\d+)?\b")
_PLACEHOLDER_RE = re.compile(r"~\d+[a-z$]*~")
_PUNCT_EDGE = " \t\n\r\"'.,;:!?()[]{}<>-–—/\\|@#$%^&*_+=~`"

def normalize(text: str) -> str:
    """en_norm — see module docstring."""
    if not text:
        return ""
    t = unicodedata.normalize("NFKC", text)
    t = (t.replace("\u2018", "'").replace("\u2019", "'")
           .replace("\u201c", '"').replace("\u201d", '"')
           .replace("\u2013", "-").replace("\u2014", "-")
           .replace("\u00a0", " "))
    t = t.lower()
    t = re.sub(r"\s+", " ", t).strip()
    t = t.strip(_PUNCT_EDGE)
    t = re.sub(r"\s+", " ", t).strip()
    return t

def skeleton(en_norm: str):
    """Return (en_skel, slots, is_template).

    slots: list of {"name": "money"|"time"|"number"|"slot1", "value": original}
    in order of appearance. is_template is True iff any slot was found.
    """
    slots = []

    def _money(m):
        slots.append({"name": "money", "value": m.group(0)})
        return " {money} "

    def _time(m):
        slots.append({"name": "time", "value": m.group(0)})
        return " {time} "

    def _number(m):
        slots.append({"name": "number", "value": m.group(0)})
        return " {number} "

    def _ph(m):
        slots.append({"name": "slot" + m.group(0)[1:-1], "value": m.group(0)})
        return " {slot} "

    t = en_norm
    t = _MONEY_RE.sub(_money, t)
    t = _TIME_RE.sub(_time, t)
    t = _PLACEHOLDER_RE.sub(_ph, t)
    t = _NUMBER_RE.sub(_number, t)
    # skeleton level: punctuation is "soft" -> space
    t = re.sub(r"[^\w\s{}]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t, slots, len(slots) > 0

def mask_slots_for_translation(text: str):
    """Replace dynamic values with {money}/{time}/{number} tokens so the
    translator copies the SLOT (not a literal value) into the Vietnamese
    translation — TDD 5.5. The runtime substitutes the real OCR value
    into the slot when displaying. Returns (masked_text, slots)."""
    slots = []

    def _money(m):
        slots.append({"name": "money", "value": m.group(0)})
        return "{money}"

    def _time(m):
        slots.append({"name": "time", "value": m.group(0)})
        return "{time}"

    def _number(m):
        slots.append({"name": "number", "value": m.group(0)})
        return "{number}"

    t = _MONEY_RE.sub(_money, text)
    t = _TIME_RE.sub(_time, t)
    t = _NUMBER_RE.sub(_number, t)
    return t, slots


def template_pattern(en_skel: str) -> str:
    """Compile a skeleton into a regex pattern string.

    {money} -> money-ish, {time} -> time-ish, {number} -> digits,
    {slot}  -> any short run. Everything else is literal.
    """
    out = []
    i = 0
    while i < len(en_skel):
        if en_skel.startswith("{money}", i):
            out.append(r"\$\s?\d[\d,]*(?:\.\d+)?")
            i += 7
        elif en_skel.startswith("{time}", i):
            out.append(r"\d{1,2}:\d{2}(?::\d{2})?\s?(?:am|pm)?")
            i += 6
        elif en_skel.startswith("{number}", i):
            out.append(r"\d[\d,]*(?:\.\d+)?")
            i += 8
        elif en_skel.startswith("{slot}", i):
            out.append(r".{1,40}?")
            i += 6
        else:
            out.append(re.escape(en_skel[i]))
            i += 1
    return "^" + "".join(out) + "$"

def len_bucket(en_norm: str) -> int:
    return len(en_norm) // 10

def first_token(en_norm: str) -> str:
    return en_norm.split(" ", 1)[0] if en_norm else ""
