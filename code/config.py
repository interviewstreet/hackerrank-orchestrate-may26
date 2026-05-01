"""
config.py — Central configuration. All constants in one place.

WHY ONE FILE: Change a threshold here → affects all modules instantly.
No hunting across files.
"""

import os
from pathlib import Path

# ── Paths ─────────────────────────────────────────────────────────────────────
CODE_DIR   = Path(__file__).parent.resolve()
REPO_ROOT  = CODE_DIR.parent.resolve()

from dotenv import load_dotenv

# ── Load Secrets ──────────────────────────────────────────────────────────────
load_dotenv(REPO_ROOT / ".env", override=False)
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
DATA_DIR   = REPO_ROOT / "data"
TICKETS_DIR = REPO_ROOT / "support_tickets"

INPUT_CSV  = TICKETS_DIR / "support_tickets.csv"
SAMPLE_CSV = TICKETS_DIR / "sample_support_tickets.csv"
OUTPUT_CSV = TICKETS_DIR / "output.csv"

LOG_DIR    = Path.home() / "hackerrank_orchestrate"
LOG_FILE   = LOG_DIR / "log.txt"

# ── BM25 retrieval ────────────────────────────────────────────────────────────
TOP_K_DOCS = 5           # how many docs to retrieve per query
MIN_BM25_SCORE = 1.0     # below this → escalate (no relevant docs found)
CHUNK_SIZE_WORDS = 250   # words per corpus chunk
CHUNK_OVERLAP_WORDS = 30 # overlap between chunks

# ── Companies ─────────────────────────────────────────────────────────────────
COMPANIES = ["hackerrank", "claude", "visa"]

# Keywords to identify which company a ticket belongs to
COMPANY_KEYWORDS: dict[str, list[str]] = {
    "hackerrank": [
        "hackerrank", "hacker rank", "assessment", "test platform",
        "coding test", "candidate", "recruiter", "interview platform",
        "resume builder", "skillup", "hackerrank for work", "test score",
        "test variant", "question library", "inactivity", "virtual lobby",
    ],
    "claude": [
        "claude", "anthropic", "claude.ai", "claude api", "claude code",
        "claude desktop", "bedrock", "aws bedrock", "claude lti",
        "claude model", "claude conversation", "ai assistant", "claude team",
    ],
    "visa": [
        "visa", "visa card", "credit card", "debit card", "traveller cheque",
        "travelers cheque", "card payment", "visa payment", "card blocked",
        "card stolen", "unauthorized charge", "merchant payment",
        "visa network", "cardholder",
    ],
}

# ── Escalation keywords (always escalate, no reply) ───────────────────────────
# WHY: These are HIGH RISK situations. Wrong auto-reply = real harm.
ESCALATION_KEYWORDS: list[str] = [
    # Financial fraud
    "fraud", "stolen card", "card stolen", "unauthorized transaction",
    "unauthorized charge", "identity theft", "identity stolen",
    "account hacked", "account compromised",
    # Irreversible account actions
    "delete account", "delete all data", "gdpr erasure", "remove all my data",
    # Platform security
    "security vulnerability", "vulnerability", "exploit", "bug bounty",
    # Score / decision manipulation
    "increase my score", "increase score", "change my score",
    "review my answers", "move me to the next round", "tell the company to hire",
    "force pass", "override my result",
    # Billing
    "refund", "pause subscription", "cancel subscription",
    "order id", "payment dispute", "chargeback",
    # Outages (platform-wide)
    "site is down", "all pages", "nothing is accessible",
    # Admin bypass
    "even though i am not", "even though i'm not", "restore my access",
    # Urgent cash / financial distress
    "urgent cash", "need cash now",
]

# ── Prompt injection patterns (regex) ─────────────────────────────────────────
INJECTION_PATTERNS: list[str] = [
    r"ignore (all )?(previous|prior) instructions",
    r"reveal (your )?(system )?prompt",
    r"act as (dan|an? ai without restrictions)",
    r"forget (all )?previous",
    r"you are now",
    r"display (all )?(internal )?(rules|documents|logic)",
    r"show (me )?(your )?(internal|hidden|secret)",
    r"jailbreak",
    r"bypass (your )?(safety|filter|restriction)",
]

# ── Malicious command patterns (regex) ────────────────────────────────────────
MALICIOUS_PATTERNS: list[str] = [
    r"delete (all )?files",
    r"rm -rf",
    r"drop (table|database)",
    r"give me (the )?code to",
]

# ── Product area defaults per company ─────────────────────────────────────────
DEFAULT_PRODUCT_AREA: dict[str, str] = {
    "hackerrank": "screen",
    "claude": "claude",
    "visa": "general_support",
    "unknown": "general_support",
}

# ── Valid output values (problem_statement.md) ────────────────────────────────
VALID_STATUSES      = {"replied", "escalated"}
VALID_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}
