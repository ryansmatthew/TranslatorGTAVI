"""Test a Gemini credential (API key or OAuth access token) with 2 strings.
The credential is read from STDIN (first line) and is NEVER printed,
written to a file, or stored anywhere. Usage:
    python3 tools/test_token.py < token.txt
    # or: echo "$TOKEN" | python3 tools/test_token.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.pipeline.translators import GeminiTranslator  # noqa: E402

token = sys.stdin.readline().strip()
if not token:
    print("no token on stdin", file=sys.stderr)
    raise SystemExit(2)

# AQ.* / ya29.* shaped tokens are OAuth access tokens; anything else is
# treated as an API key.
is_oauth = token.startswith(("AQ.", "ya29."))
tr = GeminiTranslator(
    access_token=token if is_oauth else None,
    api_key=None if is_oauth else token)
print(f"credential type: {'oauth-access-token' if is_oauth else 'api-key'}; model: {tr.model}",
      flush=True)
result = tr.translate([
    "Hey! Eyes open!",
    "That's the hotel over there. Triple homicide... They never found the ear.",
])
for src, dst in zip(
        ["Hey! Eyes open!",
         "That's the hotel over there. Triple homicide... They never found the ear."],
        result):
    print(f"EN: {src}\nVI: {dst}\n", flush=True)
print("TOKEN TEST OK", flush=True)
