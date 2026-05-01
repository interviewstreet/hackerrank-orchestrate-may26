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

CHUNK_SIZE          = 300      
CHUNK_OVERLAP       = 50

TOP_K               = 3       

RETRIEVAL_THRESHOLD = 0.35     # base threshold
LOW_CONF_THRESHOLD  = 0.25     # for fallback trigger
MIN_SCORE           = 0.15     # filter weak chunks

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
    # --- Instruction override ---
    r"ignore (previous|prior|all) instructions",
    r"disregard (all|any|previous) (instructions|rules)",
    r"forget (everything|all|your instructions)",
    r"override (all|previous) (instructions|rules)",
    r"bypass (all|any) (restrictions|filters|rules)",
    r"do not follow (the )?above instructions",

    # --- Role / persona hijack ---
    r"you are now",
    r"pretend (you are|to be)",
    r"act as (an? )?(unrestricted|jailbroken|dan\b|developer|system)",
    r"assume the role of",
    r"switch to (developer|admin|root) mode",
    r"enter (debug|developer) mode",
    r"simulate (a )?(different|new) persona",
    r"new persona",
    r"you are no longer",
    r"from now on you are",

    # --- Jailbreak / known attacks ---
    r"(jailbreak|prompt injection|override instructions)",
    r"\bDAN\b",
    r"do anything now",
    r"unfiltered response",
    r"no restrictions",
    r"without following policies",

    # --- System prompt / hidden info extraction ---
    r"reveal (your|the) (system prompt|hidden instructions)",
    r"show (me )?(your )?(prompt|instructions)",
    r"what are your (rules|instructions|policies)",
    r"print (your )?(system prompt|hidden prompt)",
    r"dump (your )?(prompt|configuration)",
    r"expose (your )?(prompt|rules)",

    # --- Data exfiltration / secrets ---
    r"(api[_-]?key|secret key|access token|private key)",
    r"show (me )?(all )?(tokens|keys|credentials)",
    r"leak (data|information|secrets)",
    r"extract (hidden|private) data",
    r"retrieve (internal|private) information",

    # --- Tool / system manipulation ---
    r"execute (shell|system|command)",
    r"run (this|the following) command",
    r"open (a )?(shell|terminal)",
    r"access (filesystem|database|internal system)",
    r"modify (system|instructions|rules)",

    # --- Obfuscation / trick patterns ---
    r"```.*ignore.*```",  # code block injection
    r"<\s*script\s*>",    # HTML/script injection attempt
    r"base64",
    r"encoded (instructions|message)",
    r"decode (this|the following)",
]

SENSITIVE_KEYWORDS = {
    "visa": {
        "high_risk": [
            "fraud", "fraudulent", "unauthorized", "unauthorised",
            "stolen card", "lost card", "card stolen",
            "unauthorized transaction", "unknown transaction",
            "someone used my card", "card hacked",
            "identity theft", "phishing", "scam",
            "data breach", "account takeover",
            "chargeback", "dispute transaction",
            "card details leaked", "cvv", "card number", "pan",
        ],
        "medium_risk": [
            "billing issue", "double charge", "duplicate charge",
            "refund not received", "payment failed",
            "transaction failed", "incorrect charge",
        ],
    },

    "claude": {
        "high_risk": [
            "account hacked", "unauthorized access",
            "data breach", "privacy violation",
            "gdpr", "right to erasure", "delete my data permanently",
            "legal action", "lawsuit", "court case",
            "ip violation", "copyright", "defamation",
            "account suspended wrongly", "security issue",
        ],
        "medium_risk": [
            "api not working", "model error", "rate limit",
            "billing issue", "subscription issue",
            "sso failure", "scim issue", "jit provisioning",
            "login issue", "access issue",
        ],
    },

    "hackerrank": {
        "high_risk": [
            "cheating", "plagiarism", "copied code",
            "unfair disqualification", "wrongly flagged",
            "data leak", "candidate data leak",
            "gdpr", "delete my data", "data erasure",
            "discrimination", "bias", "wrongful termination",
            "legal complaint", "contract violation",
        ],
        "medium_risk": [
            "test not loading", "assessment issue",
            "submission failed", "compiler error",
            "question bug", "incorrect result",
            "billing issue", "payment problem",
            "ats sync failure", "integration issue",
        ],
    },
}
ESCALATION_RESPONSE = (
    "Thank you for reaching out. Your issue requires attention from our "
    "specialist support team. A human agent will review your case and "
    "follow up with you shortly. Please do not re-submit this ticket."
)