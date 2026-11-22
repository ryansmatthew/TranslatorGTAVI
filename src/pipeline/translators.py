"""Phase 3 — translator backends behind one interface (TDD ch.6, ch.12).
Both backends translate a LIST of display strings in one call and return
a list of Vietnamese strings in the same order. Markers are NEVER sent
to the translator as translatable text: the caller (translate_batch.py)
replaces each marker with a numbered placeholder token, translates, then
restores the exact original marker. The validator then proves the
restoration is exact.

Backends:
  * GeminiTranslator — Google Gemini API (default model gemini-2.5-flash).
    Needs GEMINI_API_KEY in the environment. No SDK dependency: plain
    HTTPS via `requests`, so the pipeline runs anywhere Python runs.
    The key is NEVER read from chat, files, or the DB — env var only.
  * LocalTranslator — Helsinki-NLP opus-mt-en-vi via `transformers`
    (optional dependency, lazy import). Small (~300M params), CPU-usable,
    fast, but noticeably weaker than an LLM on slang, jokes, and
    social-media tone. It is the fallback / no-key option, and the
    reference implementation of the interface for a future local LLM
    (e.g. Qwen2.5-7B on the RTX 3060 PC) — swap the model, keep the API.

Which backend is used for P0 is decided at the start of Phase 3 from a
sample batch (see tools/sample_batch.py). The choice is recorded in
db_meta (pipeline_backend) and in every translations row (origin).
"""
import json
import os
import time

import requests

SYSTEM_PROMPT = (
    "You are translating video-game text from American English to Vietnamese "
    "for Vietnamese players. Translate naturally, keep the tone of the original "
    "(casual, funny, rude, or formal as written). Keep proper names, place names "
    "(Vice City, Leonida), hashtags, usernames and emoji exactly as they are. "
    "Do NOT translate, remove, or reorder any token that looks like "
    "<<M0>>, <<M1>>, ... — copy them back exactly, in the same positions. "
    "Do NOT add explanations, quotes, or extra lines. Return ONLY a JSON array "
    "of translated strings, in the same order as the input."
)


class GeminiTranslator:
    name = "gemini"
    origin = "pipeline_api"

    def __init__(self, model="gemini-2.5-flash", api_key=None, access_token=None, timeout=120):
        self.model = model
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        # OAuth access token (e.g. "AQ.Ab8...") — used as a Bearer token
        # instead of an API key. Transient only: never stored in a file,
        # the DB, or memory; pass it in at call time.
        self.access_token = access_token or os.environ.get("GEMINI_ACCESS_TOKEN")
        if not self.api_key and not self.access_token:
            raise RuntimeError(
                "No Gemini credential: set GEMINI_API_KEY or GEMINI_ACCESS_TOKEN. "
                "Create an API key at https://aistudio.google.com/apikey "
                "(never paste the key into chat or commit it).")
        self.timeout = timeout
        self.url = (
            "https://generativelanguage.googleapis.com/v1beta/models/"
            f"{model}:generateContent")

    def translate(self, texts, glossary_note=""):
        prompt = SYSTEM_PROMPT
        if glossary_note:
            prompt += "\nGlossary (use exactly these Vietnamese forms):\n" + glossary_note
        prompt += "\n\nTranslate this JSON array:\n" + json.dumps(texts, ensure_ascii=False)
        last = None
        for attempt in range(3):
            try:
                headers = {}
                params = {}
                if self.access_token:
                    headers["Authorization"] = "Bearer " + self.access_token
                elif self.api_key:
                    params = {"key": self.api_key}
                r = requests.post(
                    self.url, params=params, headers=headers, timeout=self.timeout,
                    json={"contents": [{"parts": [{"text": prompt}]}],
                          "generationConfig": {"temperature": 0.3}})
                r.raise_for_status()
                out = r.json()["candidates"][0]["content"]["parts"][0]["text"]
                start, end = out.find("["), out.rfind("]")
                result = json.loads(out[start:end + 1])
                if len(result) != len(texts):
                    raise ValueError(f"expected {len(texts)} translations, got {len(result)}")
                return result
            except Exception as e:  # noqa: BLE001 - retry transient failures
                last = e
                time.sleep(2 ** attempt * 5)
        raise RuntimeError(f"Gemini translation failed after 3 attempts: {last}")


class LocalTranslator:
    """Helsinki-NLP opus-mt-en-vi. Requires: pip install transformers torch sentencepiece."""
    name = "local-opus-mt"
    origin = "pipeline_local"

    def __init__(self, model="Helsinki-NLP/opus-mt-en-vi"):
        try:
            from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
        except ImportError as e:
            raise RuntimeError(
                "Local backend needs: pip install transformers torch sentencepiece") from e
        self.tok = AutoTokenizer.from_pretrained(model)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model)

    def translate(self, texts, glossary_note=""):
        out = []
        for t in texts:
            ids = self.tok(t, return_tensors="pt", truncation=True, max_length=256)
            gen = self.model.generate(**ids, max_length=256)
            out.append(self.tok.decode(gen[0], skip_special_tokens=True))
        return out


def get_translator(backend, **kw):
    if backend == "gemini":
        return GeminiTranslator(**kw)
    if backend == "local-opus-mt":
        return LocalTranslator(**kw)
    raise ValueError(f"unknown backend: {backend} (expected 'gemini' or 'local-opus-mt')")
