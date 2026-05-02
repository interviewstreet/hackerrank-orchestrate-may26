"""
classifier.py — Fast, deterministic, rule-based classification.

WHAT THIS MODULE DOES:
  1. COMPANY DETECTION: Infers whether the ticket is for hackerrank, claude, or visa.
  2. REQUEST TYPE CLASSIFICATION: Classifies the ticket as product_issue, feature_request, bug, or invalid.

WHY NO LLM HERE:
  Company and request_type can be determined with high accuracy using simple keyword rules.
  This saves API calls, reduces latency, and guarantees deterministic behavior.
"""

import re
from loguru import logger

from config import COMPANIES, COMPANY_KEYWORDS


# ── Company Detection ─────────────────────────────────────────────────────────

def detect_company(issue: str, subject: str, company_field: str) -> str:
    """
    Determine the company for the ticket.

    Logic:
    1. If the CSV company field is valid, trust it.
    2. Otherwise, run keyword matching on the combined text.
    3. If still unknown, return 'unknown'.
    """
    field = company_field.strip().lower()
    combined_text = f"{subject} {issue}".lower()

    # 1. Direct field match
    if field in COMPANIES:
        return field

    # 2. Keyword match
    scores: dict[str, int] = {company: 0 for company in COMPANIES}
    for company, keywords in COMPANY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in combined_text:
                scores[company] += 1

    best_match = max(scores, key=lambda c: scores[c])
    if scores[best_match] > 0:
        logger.debug(f"Company inferred via keywords: {best_match}")
        return best_match

    logger.debug("Company unknown. Returning 'unknown'.")
    return "unknown"


# ── Request Type Classification ───────────────────────────────────────────────

_BUG_PATTERNS = [
    r"(not|isn't|aren't|don't|doesn't|can't|cannot)\s+(work|load|open|function|respond|submit|access)",
    r"(is|are)?\s+(down|broken|unavailable|offline|not accessible)",
    r"(error|crash|bug|glitch|freeze|stuck|timeout)",
    r"(all|none|no)\s+(requests|submissions|pages|access)\s+(are\s+)?(working|accessible|failing)",
    r"(stopped|stop)\s+working",
    r"failing",
]

_FEATURE_REQUEST_PATTERNS = [
    r"(would like|want|wish|request|suggest|add|implement|include|support)\s+(a\s+|an\s+|the\s+)?(feature|option|ability|support|dark mode|integration)",
    r"(is it possible|can you add|please add|could you)",
    r"(feature request|enhancement|improvement)",
]

_INVALID_PATTERNS = [
    r"^(hi|hello|hey|thanks?|thank you|good (morning|afternoon|evening))[\s!.,]*$",
    r"(actor|movie|film|sport|celebrity|music|song|tv show)",
    r"what is the (capital|population|meaning|definition)",
    r"(give me|generate|write|create)\s+(code|script|program|essay|poem)",
    r"^(none|nothing|n/a|test|testing)$",
]

def _matches_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def classify_request_type(issue: str, subject: str) -> str:
    """
    Determine request_type using deterministic rules.
    Defaults to 'product_issue' if no specific pattern matches.
    """
    combined_text = f"{subject} {issue}".strip()

    if _matches_any(combined_text, _INVALID_PATTERNS):
        return "invalid"

    if _matches_any(combined_text, _BUG_PATTERNS):
        return "bug"

    if _matches_any(combined_text, _FEATURE_REQUEST_PATTERNS):
        return "feature_request"

    return "product_issue"


# ── Product Area Inference ────────────────────────────────────────────────────

def infer_product_area(issue: str, company: str) -> str:
    """
    Infer the product_area based on company and keywords.
    """
    text = issue.lower()

    if company == "hackerrank":
        if any(k in text for k in ["test", "assessment", "screen", "candidate", "invite"]): return "screen"
        if any(k in text for k in ["interview", "lobby", "whiteboard"]): return "interviews"
        if any(k in text for k in ["resume", "apply", "job", "practice", "skillup"]): return "skillup"
        if any(k in text for k in ["settings", "user", "role", "permission"]): return "settings"
        if any(k in text for k in ["community", "forum", "discuss"]): return "hackerrank_community"
        return "general_support"

    if company == "claude":
        if any(k in text for k in ["api", "console", "bedrock", "key", "token"]): return "claude-api-and-console"
        if any(k in text for k in ["privacy", "data", "delete", "conversation"]): return "privacy-and-legal"
        if any(k in text for k in ["plan", "subscription", "pro", "max", "team", "enterprise"]): return "pro-and-max-plans"
        if any(k in text for k in ["education", "lti", "student", "professor"]): return "claude-for-education"
        if any(k in text for k in ["safety", "harmful", "content", "safeguard"]): return "safeguards"
        if any(k in text for k in ["mobile", "ios", "android", "app"]): return "claude-mobile-apps"
        return "claude"

    if company == "visa":
        if any(k in text for k in ["fraud", "stolen", "unauthorized", "dispute"]): return "fraud_support"
        if any(k in text for k in ["travel", "foreign", "international", "abroad"]): return "travel_support"
        if any(k in text for k in ["merchant", "seller", "business", "minimum"]): return "merchant_support"
        if any(k in text for k in ["cheque", "travelers", "traveller"]): return "travel_support"
        return "general_support"

    return "general_support"
