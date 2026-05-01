"""
config.py — Central configuration for the HackerRank Support Triage Agent.

All constants, paths, thresholds, and keyword lists live here so that
every other module stays free of magic values.
"""

import os

# ── Paths ──────────────────────────────────────────────────────────────────
# BASE_DIR is .../hackerrank-orchestrate-may26/code
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))

# Go up one level to find data and support_tickets
DATA_DIR     = os.path.normpath(os.path.join(BASE_DIR, "..", "data"))
TICKETS_DIR  = os.path.normpath(os.path.join(BASE_DIR, "..", "support_tickets"))

INPUT_CSV    = os.path.join(TICKETS_DIR, "support_tickets.csv")
OUTPUT_CSV   = os.path.join(TICKETS_DIR, "output.csv")

# ── Embedding model ────────────────────────────────────────────────────────
EMBEDDING_MODEL      = "all-MiniLM-L6-v2"
RANDOM_SEED          = 42                  # determinism

# ── Retrieval ──────────────────────────────────────────────────────────────
TOP_K_DOCS           = 3                   # number of docs retrieved
CONFIDENCE_THRESHOLD = 0.20               # cosine-sim below this → escalate

# ── Output field names ─────────────────────────────────────────────────────
OUTPUT_FIELDS = ["status", "product_area", "response", "justification", "request_type"]

# ─────────────────────────────────────────────────────────────────────────────
# Risk keywords  — any match forces escalation regardless of retrieval score.
# Grouped by risk category for readable justifications.
# ─────────────────────────────────────────────────────────────────────────────
RISK_PATTERNS = {
    "fraud_security": [
        "fraud", "stolen", "unauthorized access", "breach",
        "hacked", "compromised", "security incident", "intrusion",
        "leak", "data breach",
    ],
    "payment_dispute": [
        "refund", "dispute", "chargeback", "double charge",
        "charged twice", "payment issue", "overcharged",
    ],
    "score_manipulation": [
        "increase score", "change score", "modify score",
        "change result", "modify result", "change the results",
        "alter result", "pass the candidate", "make him pass",
        "make her pass", "mark as passed", "change recruitment",
    ],
    "account_permission": [
        "admin access", "grant admin", "give admin",
        "escalate permission", "bypass permission", "override access",
    ],
    "vulnerability": [
        "vulnerability", "exploit", "cve", "zero-day",
        "sql injection", "xss", "remote code execution",
    ],
    "data_privacy": [
        "gdpr", "delete all data", "erase all data",
        "right to be forgotten", "data deletion request",
        "personal data removal",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# Product-area keyword map — used for keyword-based classification.
# Semantic classification (embeddings) breaks ties.
# ─────────────────────────────────────────────────────────────────────────────
PRODUCT_AREA_KEYWORDS = {
    "assessments": [
        "assessment", "test", "quiz", "question", "library",
        "coding challenge", "proctoring", "timer", "submission",
        "score", "result", "language", "code editor", "question bank",
        "loading", "blank screen",
    ],
    "account_management": [
        "login", "log in", "password", "reset", "account", "admin",
        "user", "invite", "team", "2fa", "two-factor", "locked out",
        "credentials", "sign in", "access", "permission",
    ],
    "billing": [
        "billing", "invoice", "charge", "payment", "refund",
        "subscription", "plan", "upgrade", "downgrade", "receipt",
        "duplicate charge", "overcharged", "cancel",
    ],
    "privacy": [
        "gdpr", "data deletion", "personal data", "privacy",
        "right to erasure", "data request", "compliance",
        "erase", "delete data", "data export",
    ],
    "security": [
        "security", "breach", "unauthorized", "fraud", "stolen",
        "hacked", "vulnerability", "exploit", "token", "api key",
        "suspicious", "incident",
    ],
    "technical_issues": [
        "api", "integration", "error", "bug", "crash", "not working",
        "failed", "slow", "performance", "browser", "chrome",
        "firefox", "email", "notification", "webhook", "401", "500",
    ],
    "general": [
        "demo", "pricing", "feature request", "feedback", "contact",
        "how to", "help", "report", "audit", "export",
    ],
}

# ─────────────────────────────────────────────────────────────────────────────
# Request-type keyword map
# ─────────────────────────────────────────────────────────────────────────────
REQUEST_TYPE_KEYWORDS = {
    "bug": [
        "bug", "crash", "error", "broken", "not working", "fails",
        "failure", "freeze", "glitch", "incorrect", "wrong",
        "doesn't work", "does not work", "stopped working",
    ],
    "feature_request": [
        "feature", "request", "would like", "wish", "want a",
        "add support", "can you add", "please add", "enhancement",
        "suggestion", "idea", "new functionality",
    ],
    "invalid": [
        "increase score", "change score", "change result",
        "modify result", "pass candidate", "fraud", "stolen",
        "unauthorized",
    ],
    # product_issue is the catch-all — no keywords needed
}
