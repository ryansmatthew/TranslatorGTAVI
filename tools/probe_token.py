"""Probe what the supplied Gemini credential can actually call.
Reads the credential from STDIN (first line), never prints it.
Tries, in order:
  1. GET /v1beta/models (Bearer) — is the token valid for Gemini API at all?
  2. POST /v1beta/interactions (Bearer) — the endpoint the user named,
     with a minimal body; prints only the HTTP status + error message.
Prints statuses and short error bodies only — never the token.
"""
import json
import sys

import requests

token = sys.stdin.readline().strip()
if not token:
    print("no token on stdin", file=sys.stderr)
    raise SystemExit(2)
H = {"Authorization": "Bearer " + token}

r = requests.get(
    "https://generativelanguage.googleapis.com/v1beta/models",
    headers=H, timeout=30)
print("GET /v1beta/models ->", r.status_code)
print((r.text or "")[:300])

r = requests.post(
    "https://generativelanguage.googleapis.com/v1beta/interactions",
    headers={**H, "Content-Type": "application/json"}, timeout=30,
    json={"model": "gemini-2.5-flash",
          "input": "Translate to Vietnamese: Hey! Eyes open!"})
print("POST /v1beta/interactions ->", r.status_code)
print((r.text or "")[:500])
