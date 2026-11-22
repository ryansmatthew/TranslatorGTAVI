"""Phase 3 — translation validation (TDD ch.6.2).
A batch that fails validation is NEVER written to `translations`.
Checks, in order:
  1. marker integrity: the multiset of markers in vi == markers in en
     (same markers, same order, same count — Appendix A)
  2. slot integrity (template rows): every {money}/{time}/{number}/{slot}
     in the source skeleton appears the same number of times in vi
  3. glossary: do_not_translate terms must appear unchanged in vi;
     mapped terms must use exactly the glossary Vietnamese form
  4. length / emptiness: vi must be non-empty; vi/en length ratio outside
     [0.3, 3.0] is flagged for review (not auto-rejected, except empty)
Returns (ok, [reasons]). `quarantine` in the batch runner stores failures
separately instead of blocking the whole batch.
"""
import json
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from src.common.markers import split_markers  # noqa: E402

_SLOT_RE = re.compile(r"\{(money|time|number|slot\d*)\}")
_PLACEHOLDER_MARKER_RE = re.compile(r"~\d+[a-z$]*~")


def check_markers(en: str, vi: str, en_skel: str = ""):
    """Marker multiset/order must match — with one principled exception
    (found by the Phase 3 sample batch, 2026-11-21): a *placeholder*
    marker such as ~1~ denotes a value slot. The skeleton already counts
    its digit as {number} (e.g. "Hole ~1~" -> "hole {number}"), so the
    stored translation may carry {number} instead of the raw ~1~ marker
    — both mean "the number goes here", and check_slots() separately
    enforces that the slot is present in vi. If the skeleton has no slot
    at all, the placeholder must be preserved raw. All other markers
    (timing ~sl:~, input, blip, format) must match exactly, in order."""
    _, en_mj, _ = split_markers(en)
    _, vi_mj, _ = split_markers(vi)
    en_m = [m["marker"] for m in json.loads(en_mj)]
    vi_m = [m["marker"] for m in json.loads(vi_mj)]
    en_core = [m for m in en_m if not _PLACEHOLDER_MARKER_RE.fullmatch(m)]
    vi_core = [m for m in vi_m if not _PLACEHOLDER_MARKER_RE.fullmatch(m)]
    if en_core != vi_core:
        return [f"marker mismatch: en={en_m} vi={vi_m}"]
    n_ph = len(en_m) - len(en_core)
    vi_ph = len(vi_m) - len(vi_core)
    if n_ph and not _SLOT_RE.search(en_skel or "") and vi_ph != n_ph:
        return [f"placeholder marker lost: en has {n_ph} placeholder marker(s), "
                f"vi has {vi_ph}"]
    return []


def check_slots(en_skel: str, vi: str):
    want = collections_counter(_SLOT_RE.findall(en_skel or ""))
    got = collections_counter(_SLOT_RE.findall(vi or ""))
    if want != got:
        return [f"slot mismatch: want={dict(want)} got={dict(got)}"]
    return []


def collections_counter(items):
    from collections import Counter
    return Counter(items)


def check_glossary(vi: str, glossary):
    """glossary: list of dicts {en_term, vi_term, kind, do_not_translate}."""
    reasons = []
    for g in glossary or []:
        if g.get("do_not_translate"):
            if g["en_term"] not in vi and g["en_term"].lower() not in vi.lower():
                # term may legitimately be absent if the source sentence
                # did not contain it — caller only passes terms present in en
                reasons.append(f"do_not_translate term lost: {g['en_term']}")
        elif g.get("vi_term"):
            # only enforced when the English term is in the source;
            # caller filters glossary to terms present in en
            if g["vi_term"] not in vi:
                reasons.append(f"glossary term not used: {g['en_term']} -> {g['vi_term']}")
    return reasons


def check_length(en: str, vi: str):
    if not vi or not vi.strip():
        return ["empty translation"]
    if not en or not en.strip():
        return []
    ratio = len(vi) / max(1, len(en))
    if ratio < 0.3 or ratio > 3.0:
        return [f"length ratio suspicious: {ratio:.2f} (en={len(en)} vi={len(vi)})"]
    return []


def validate(en: str, en_skel: str, vi: str, glossary=None):
    reasons = []
    reasons += check_markers(en, vi, en_skel)
    reasons += check_slots(en_skel, vi)
    reasons += check_length(en, vi)
    if glossary:
        reasons += check_glossary(vi, glossary)
    # length-ratio is a review flag, not a hard failure; everything else is
    hard = [r for r in reasons if not r.startswith("length ratio")]
    return (len(hard) == 0, reasons)
