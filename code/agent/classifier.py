"""
classifier.py — Support ticket classification.

Responsible for:
  - Determining the domain: "hackerrank" | "claude" | "visa" | "unknown"
  - Picking a "request_type": "billing", "fraud", "technical_issue", etc.
  - Identifying the "product_area": "screen", "claude_ai", "bedrock", etc.
  - Returning a Classification object with a confidence score.
"""

import json
from dataclasses import dataclass
from utils.model_provider import call_llm

# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class Classification:
    domain: str
    request_type: str
    product_area: str
    confidence: float


# Fallback returned on any error
_FALLBACK = Classification(
    domain="unknown",
    request_type="other",
    product_area="unknown",
    confidence=0.0,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_MODEL_NAME = "gemini-2.0-flash"

_DOMAIN_VALUES = ("hackerrank", "claude", "visa", "unknown")
_REQUEST_TYPE_VALUES = (
    "billing", "fraud", "account_access", "technical_issue", 
    "feature_request", "other"
)

# ---------------------------------------------------------------------------
# System prompt for JSON Mode
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = """
You are a specialized support ticket classifier for HackerRank, Claude (Anthropic), and Visa.

Your goal is to categorize the user's ticket into one of the following domains and request types.

DOMAINS:
- HackerRank: technical recruiting, coding assessments, candidate platform, proctoring.
- Claude: Anthropic's AI assistant, API access, subscriptions, model usage, data privacy, bug bounty.
- Visa: payment cards, transactions, fraud, disputes, card services, ATM, travel.

COMMON PRODUCT AREAS (Use these verified sub-directories as "product_area"):
- HackerRank: screen, interviews, library, integrations, engage, skillup, chakra, settings, community.
- Claude: api_and_console, team_plans, pro_plans, enterprise, bedrock, mobile_apps, chrome_extension, connectors, privacy_legal.
- Visa: consumer, small_business, travel_support, account_security, disputes.

REQUEST TYPE DEFINITIONS (pick exactly one):
- "billing"         : payment issues, refunds, subscription changes, pricing questions
- "fraud"           : reported scams, unauthorized charges, stolen cards, identity theft
- "account_access"  : login issues, password resets, 2FA, account locked, SSO
- "technical_issue" : bugs, errors, site down, feature not working, API integration
- "feature_request" : feedback on how to improve the product
- "other"           : general inquiries or anything else

INSTRUCTIONS:
1. Reply ONLY with valid JSON matching this exact schema — no markdown, no extra text.
2. "confidence" must be a float between 0.0 and 1.0.
3. Choose the MOST SPECIFIC request_type that fits. Use "other" only if truly none of the above fit.
4. "product_area" is a short descriptive string. DO NOT use "unknown", "other", or "general". Be specific (e.g., "ios_app", "api_pricing", "account_recovery"). If the specific area is not clear, use the most relevant top-level category from the list above.

Schema:
{
  "domain": "hackerrank" | "claude" | "visa" | "unknown",
  "request_type": "billing" | "fraud" | "account_access" | "technical_issue" | "feature_request" | "other",
  "product_area": "<short descriptive string>",
  "confidence": 0.95
}
"""

# ---------------------------------------------------------------------------
# Keyword-based heuristics (used to provide hints or overrides)
# ---------------------------------------------------------------------------

_DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "visa": [
        "visa", "card", "transaction", "payment", "chargeback",
        "atm", "debit", "credit card", "dispute", "merchant",
        "stolen card", "lost card", "traveller", "cheque",
        "issuer", "bank", "small-business", "consumer",
    ],
    "hackerrank": [
        "hackerrank", "assessment", "candidate", "test", "coding test",
        "interview", "hiring", "recruiter", "proctoring", "plagiarism",
        "resume builder", "chakra", "screen", "skillup", "engage",
        "library", "ats", "greenhouse", "lever", "workday", "sso",
        "gdpr", "community", "prep kit", "certification",
    ],
    "claude": [
        "claude", "anthropic", "subscription", "claude.ai",
        "claude pro", "claude api", "model", "prompt", "context window",
        "bedrock", "lti", "claude for", "console", "scim", "jit",
        "sso", "identity management", "amazon bedrock", "connectors",
        "claude code", "mobile app", "chrome extension", "aws bedrock",
    ],
}

def _keyword_hint(text: str) -> str:
    """Identify potential domain based on keywords to provide a hint to Gemini."""
    lower_text = text.lower()
    counts = {d: 0 for d in _DOMAIN_KEYWORDS}
    for domain, kws in _DOMAIN_KEYWORDS.items():
        for kw in kws:
            if kw in lower_text:
                counts[domain] += 1
    
    # Return a hint if there is a clear leader
    best = max(counts, key=counts.get)
    if counts[best] > 0:
        return f"Hint: This ticket likely belongs to the '{best}' domain."
    return ""


def _apply_domain_override(text: str, current_domain: str, confidence: float) -> tuple[str, float]:
    """Force domain based on strict keywords if confidence is low."""
    if confidence > 0.8 and current_domain != "unknown":
        return current_domain, confidence

    lower_text = text.lower()
    print(f"[DEBUG] Domain Override Check: '{lower_text}' | Current: {current_domain} ({confidence})")
    if "visa" in lower_text and "hackerrank" not in lower_text and "claude" not in lower_text:
        return "visa", 0.85
    if "hackerrank" in lower_text and "visa" not in lower_text and "claude" not in lower_text:
        return "hackerrank", 0.85
    if "claude" in lower_text or "bedrock" in lower_text or "anthropic" in lower_text:
        if "visa" not in lower_text and "hackerrank" not in lower_text:
            return "claude", 0.9
    
    return current_domain, confidence

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def _classify_with_retry(ticket_text: str) -> Classification:
    hint = _keyword_hint(ticket_text)
    raw_text = call_llm(
        system_prompt=_SYSTEM_PROMPT,
        user_content=f"{hint}\n\n{ticket_text}",
        json_mode=True
    )
    args = json.loads(raw_text)
    confidence = float(args.get("confidence", 0.0))
    confidence = max(0.0, min(1.0, confidence))

    domain = str(args.get("domain", "unknown"))
    if domain not in _DOMAIN_VALUES:
        domain = "unknown"

    request_type = str(args.get("request_type", "other"))
    if request_type not in _REQUEST_TYPE_VALUES:
        request_type = "other"

    product_area = str(args.get("product_area", "general")).lower().strip()
    if not product_area or product_area in ("unknown", "other", "general"):
        # Heuristic fallback if Gemini is too vague
        lower_text = ticket_text.lower()
        if "bedrock" in lower_text:
            product_area = "amazon-bedrock"
        elif "api" in lower_text or "console" in lower_text:
            product_area = "api_and_console"
        elif "subscription" in lower_text or "billing" in lower_text or "plan" in lower_text:
            product_area = "billing_and_plans"
        elif "login" in lower_text or "account" in lower_text or "access" in lower_text:
            product_area = "account_access"
        else:
            product_area = "general_support"

    domain, confidence = _apply_domain_override(ticket_text, domain, confidence)

    return Classification(
        domain=domain,
        request_type=request_type,
        product_area=product_area,
        confidence=confidence,
    )


def classify(ticket_text: str) -> Classification:
    """Classify a support ticket using Gemini."""
    if not ticket_text or not ticket_text.strip():
        return _FALLBACK

    try:
        res = _classify_with_retry(ticket_text)
        return res
    except Exception as exc:  # noqa: BLE001
        print(f"  [Classifier] ERROR after all retries: {exc}")
        return _FALLBACK
