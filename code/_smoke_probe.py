"""Tiny smoke probe — verifies the live Anthropic API works for our classifier.

Cost: ~200 input + ~100 output tokens on claude-sonnet-4-5 -> ~$0.0021.

Run: python code/_smoke_probe.py
Requires: ANTHROPIC_API_KEY in .env at repo root.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Ensure code/ is on sys.path so `from preprocessor import ...` resolves.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

if not os.getenv("ANTHROPIC_API_KEY"):
    print("FAIL: ANTHROPIC_API_KEY not in environment after loading .env")
    sys.exit(2)

from classifier import classify  # noqa: E402
from preprocessor import clean  # noqa: E402
from schemas import Ticket  # noqa: E402

ticket = Ticket(
    index=0,
    issue="I cannot cancel a test invite for a candidate. The Cancel button is greyed out.",
    subject="Cannot cancel test invite",
    company="HackerRank",
)

cleaned = clean(ticket)
print(f"[probe] preprocessor OK: injection={cleaned.injection_detected}")

try:
    result = classify(cleaned)
except Exception as exc:
    print(f"FAIL: classifier raised {type(exc).__name__}: {exc}")
    sys.exit(3)

print(f"[probe] classifier OK")
print(f"  request_type        = {result.request_type}")
print(f"  domain              = {result.domain} (conf={result.domain_confidence:.2f})")
print(f"  product_area        = {result.product_area} (conf={result.product_area_confidence:.2f})")
print(f"  is_outage           = {result.is_outage_report}")
print(f"  is_chitchat         = {result.is_chitchat_or_trivia}")
print(f"  is_sensitive        = {result.is_sensitive}")
print(f"  is_authz_violation  = {result.is_authorization_violation}")
print(f"  is_multi_request    = {result.is_multi_request}")
print("[probe] PASS")
