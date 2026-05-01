import os

# ── API ────────────────────────────────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
LLM_MODEL         = "claude-sonnet-4-20250514"
LLM_TEMPERATURE   = 0
LLM_MAX_TOKENS    = 1024

# ── Paths ──────────────────────────────────────────────────────────────────
DATA_DIR      = os.path.join(os.path.dirname(__file__), "..", "data")
LOCAL_STORE_DIR = os.path.join(os.path.dirname(__file__), "..", "local_store")
LOG_FILE      = os.path.join(os.path.dirname(__file__), "..", "logs", "log.txt")
OUTPUT_CSV    = os.path.join(os.path.dirname(__file__), "..", "support_tickets", "output.csv")
INPUT_CSV     = os.path.join(os.path.dirname(__file__), "..", "support_tickets", "support_tickets.csv")
SAMPLE_CSV    = os.path.join(os.path.dirname(__file__), "..", "support_tickets", "sample_support_tickets.csv")

# ── Retrieval ──────────────────────────────────────────────────────────────
EMBED_MODEL         = "all-MiniLM-L6-v2"
CHUNK_SIZE          = 512        # tokens (approx chars / 4)
CHUNK_OVERLAP       = 64
TOP_K               = 5
RETRIEVAL_THRESHOLD = 0.35       # cosine similarity floor

# ── Router ─────────────────────────────────────────────────────────────────
ROUTER_CONFIDENCE_THRESHOLD = 2  # keyword score needed to skip LLM fallback

DOMAIN_KEYWORDS = {
    "visa": [
        "visa", "card", "payment", "transaction", "chargeback", "merchant",
        "debit", "credit", "cvv", "pin", "atm", "contactless", "fraud",
        "dispute", "billing", "checkout", "refund", "settlement", "pan",
        "unauthorized", "bank", "issuer", "acquirer",
    ],
    "hackerrank": [
        "hackerrank", "assessment", "test", "coding challenge", "candidate",
        "interview", "proctoring", "plagiarism", "submission", "hire",
        "screen", "skill", "leaderboard", "contest", "challenge", "recruit",
        "engage", "chakra", "skillup", "library", "question", "score report",
    ],
    "claude": [
        "claude", "anthropic", "api", "prompt", "model", "token", "llm",
        "claude.ai", "subscription", "pro plan", "max plan", "team plan",
        "enterprise", "claude code", "console", "bedrock", "vertex",
        "usage limit", "context window", "artifact", "mcp",
    ],
}

# ── Safety ─────────────────────────────────────────────────────────────────
INJECTION_PATTERNS = [
    r"ignore (previous|prior|all) instructions",
    r"you are now",
    r"disregard your",
    r"pretend (you are|to be)",
    r"forget (everything|your instructions)",
    r"new persona",
    r"act as (an? )?(unrestricted|jailbroken|dan\b)",
    r"(jailbreak|prompt injection|override instructions)",
]

SENSITIVE_KEYWORDS = {
    "visa": [
        "fraud", "unauthorized transaction", "stolen card", "chargeback",
        "dispute", "cvv", "card number", " pan ", "settlement dispute",
        "data breach", "identity theft", "account takeover", "phishing",
    ],
    "claude": [
        "account hacked", "unauthorized access", "data breach", "gdpr",
        "right to erasure", "legal action", "lawsuit", "ip violation",
        "sso failure", "scim", "jit provisioning", "account suspended",
        "copyright", "defamation",
    ],
    "hackerrank": [
        "cheating", "plagiarism", "unfair disqualification", "wrongly flagged",
        "gdpr", "delete my data", "data erasure", "billing dispute",
        "contract", "ats sync failure", "candidate data leak",
        "wrongful termination", "discrimination",
    ],
}

ESCALATION_RESPONSE = (
    "Thank you for reaching out. Your issue requires attention from our "
    "specialist support team. A human agent will review your case and "
    "follow up with you shortly. Please do not re-submit this ticket."
)