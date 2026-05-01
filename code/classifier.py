"""
classifier.py — Rule-based + LLM-assisted ticket classification.

Responsibilities:
1. Detect which domain (hackerrank / claude / visa / unknown) a ticket belongs to
   when company field is missing or ambiguous.
2. Classify request_type: product_issue | feature_request | bug | invalid
3. Detect high-risk / sensitive signals that trigger escalation.
4. Extract the product_area label from the ticket + retrieval context.

Design: pattern matching first (zero-cost, deterministic), LLM second.
"""

from __future__ import annotations

import re
from typing import List, Tuple


# ─── Domain keyword patterns ──────────────────────────────────────────────────

DOMAIN_PATTERNS = {
    "hackerrank": re.compile(
        r"\b(hackerrank|hacker\s*rank|hr\b|coding\s*test|coding\s*challenge|"
        r"assessment|proctoring|plagiarism\s*detect|candidate|recruiter|"
        r"interview\s*kit|codepair|hackos|leaderboard|contest|submission|"
        r"test\s*case|compiler|ide\b|hackerrank\.com)\b",
        re.IGNORECASE,
    ),
    "claude": re.compile(
        r"\b(claude|anthropic|claude\.ai|sonnet|opus|haiku|"
        r"conversation|context\s*window|ai\s*assistant|"
        r"pro\s*plan|team\s*plan|claude\s*api|mcp|projects?\b|"
        r"artifacts?\b|voice\s*mode|memory\b)\b",
        re.IGNORECASE,
    ),
    "visa": re.compile(
        r"\b(visa\b|visa\.com|visa\.co\.in|credit\s*card|debit\s*card|"
        r"transaction|fraud|chargeback|merchant|payment|card\s*number|"
        r"cvv|pin\b|contactless|chip\b|tap\s*to\s*pay|reward\s*points|"
        r"card\s*declined|international\s*transaction|forex|currency|"
        r"atm\b|dispute|unauthorized|lost\s*card|stolen\s*card)\b",
        re.IGNORECASE,
    ),
}

# ─── Request type patterns ────────────────────────────────────────────────────

REQUEST_TYPE_PATTERNS = {
    "bug": re.compile(
        r"\b(bug|broken|error|crash|not\s*working|doesn['\']t\s*work|"
        r"glitch|issue\s*with|failing|failed|exception|500|404|"
        r"incorrect\s*result|wrong\s*output|unexpected\s*behavior|"
        r"regression|stopped\s*working|can['\']t\s*load|freezing|"
        r"infinite\s*loop|timeout)\b",
        re.IGNORECASE,
    ),
    "feature_request": re.compile(
        r"\b(feature\s*request|would\s*love|wish\s*you\s*had|"
        r"please\s*add|can\s*you\s*add|suggestion|enhancement|"
        r"improvement|it\s*would\s*be\s*nice|consider\s*adding|"
        r"in\s*the\s*future|roadmap|support\s*for|allow\s*us\s*to)\b",
        re.IGNORECASE,
    ),
    "product_issue": re.compile(
        r"\b(how\s*do\s*i|can['\']t\s*find|not\s*able\s*to|"
        r"having\s*trouble|help\s*me|where\s*is|confused|question|"
        r"clarif|why\s*is|explain|understand|problem\s*with|"
        r"need\s*help|forgot|reset|account|login|sign\s*in|"
        r"billing|charge|invoice|refund|cancel|subscription)\b",
        re.IGNORECASE,
    ),
}

# ─── Escalation risk signals ──────────────────────────────────────────────────

ESCALATION_PATTERNS = {
    "fraud": re.compile(
        r"\b(fraud|fraudulent|unauthorized|stolen|compromised|"
        r"hacked|identity\s*theft|scam|phishing|chargeback|"
        r"dispute|suspicious\s*transaction|not\s*my\s*transaction)\b",
        re.IGNORECASE,
    ),
    "account_security": re.compile(
        r"\b(can['\']t\s*access|locked\s*out|account\s*suspended|"
        r"banned|hacked\s*account|password\s*reset\s*not\s*working|"
        r"two\s*factor|2fa\s*not\s*working|lost\s*access|"
        r"account\s*deleted|account\s*disabled)\b",
        re.IGNORECASE,
    ),
    "legal_compliance": re.compile(
        r"\b(legal|lawsuit|gdpr|data\s*breach|privacy\s*violation|"
        r"subpoena|court\s*order|law\s*enforcement|regulatory|"
        r"compliance|audit|data\s*deletion\s*request|right\s*to\s*erasure)\b",
        re.IGNORECASE,
    ),
    "billing_dispute": re.compile(
        r"\b(charged\s*twice|double\s*charge|wrong\s*amount|"
        r"refund\s*not\s*received|overcharged|billing\s*error|"
        r"unexpected\s*charge|cancel\s*subscription|"
        r"dispute\s*charge|credit\s*back)\b",
        re.IGNORECASE,
    ),
    "assessment_integrity": re.compile(
        r"\b(cheating|plagiarism|impersonation|unfair|"
        r"false\s*positive|wrongly\s*flagged|appeal|"
        r"proctoring\s*error|camera\s*issue|technical\s*failure\s*during)\b",
        re.IGNORECASE,
    ),
    "harm_threat": re.compile(
        r"\b(threatening|threat|violence|harm|illegal|"
        r"dangerous|weapon|drug|abuse|harass)\b",
        re.IGNORECASE,
    ),
    "data_loss": re.compile(
        r"\b(data\s*loss|lost\s*data|deleted\s*by\s*mistake|"
        r"corrupted|cannot\s*recover|backup)\b",
        re.IGNORECASE,
    ),
}

# ─── Product area taxonomy ────────────────────────────────────────────────────

PRODUCT_AREAS = {
    "hackerrank": {
        "assessment": re.compile(r"\b(assessment|test|proctoring|camera|plagiarism|candidate|timer)\b", re.I),
        "billing": re.compile(r"\b(billing|invoice|charge|payment|subscription|plan|upgrade)\b", re.I),
        "account": re.compile(r"\b(account|login|password|email|profile|sign\s*in|sso|saml)\b", re.I),
        "developer": re.compile(r"\b(api|sdk|integration|webhook|token|oauth)\b", re.I),
        "ide_compiler": re.compile(r"\b(ide|compiler|code\s*editor|run\s*code|language|submission)\b", re.I),
        "leaderboard_contest": re.compile(r"\b(leaderboard|contest|hackos|rank|score|rating)\b", re.I),
        "recruiter": re.compile(r"\b(recruiter|candidate\s*management|invite|invitation|report|result)\b", re.I),
        "general": re.compile(r".*", re.I),
    },
    "claude": {
        "billing_plans": re.compile(r"\b(billing|charge|plan|pro|team|enterprise|subscription|payment|invoice)\b", re.I),
        "account_access": re.compile(r"\b(account|login|password|sign\s*in|email|verify|2fa)\b", re.I),
        "api_developers": re.compile(r"\b(api|sdk|token|rate\s*limit|model|anthropic|developer)\b", re.I),
        "privacy_data": re.compile(r"\b(privacy|data|delete|gdpr|erasure|export)\b", re.I),
        "features_usage": re.compile(r"\b(context|memory|project|artifact|voice|image|upload|attachment|search)\b", re.I),
        "safety_policy": re.compile(r"\b(safety|policy|content|moderation|refuse|block|restricted)\b", re.I),
        "general": re.compile(r".*", re.I),
    },
    "visa": {
        "fraud_disputes": re.compile(r"\b(fraud|unauthorized|dispute|chargeback|stolen|compromised)\b", re.I),
        "card_services": re.compile(r"\b(card|lost|stolen|replace|new\s*card|damaged|block|freeze)\b", re.I),
        "transactions": re.compile(r"\b(transaction|payment|declined|failed|pending|charge|refund)\b", re.I),
        "rewards_benefits": re.compile(r"\b(reward|points|cashback|benefit|offer|redeem)\b", re.I),
        "international": re.compile(r"\b(international|forex|currency|travel|abroad|foreign)\b", re.I),
        "merchant": re.compile(r"\b(merchant|business|pos|terminal|acquiring|acceptance)\b", re.I),
        "general": re.compile(r".*", re.I),
    },
}


# ─── Helpers ──────────────────────────────────────────────────────────────────

def detect_domain(issue: str, subject: str, company: str) -> str:
    """
    Return the most likely domain. If company is provided and not 'None',
    trust it. Otherwise use pattern matching on issue + subject text.
    """
    if company and company.strip().lower() not in ("none", "", "null"):
        c = company.strip().lower()
        if "hackerrank" in c:
            return "hackerrank"
        if "claude" in c:
            return "claude"
        if "visa" in c:
            return "visa"

    text = f"{subject} {issue}"
    scores: dict[str, int] = {d: 0 for d in DOMAIN_PATTERNS}
    for domain, pattern in DOMAIN_PATTERNS.items():
        scores[domain] = len(pattern.findall(text))

    best = max(scores, key=lambda d: scores[d])
    if scores[best] > 0:
        return best
    return "unknown"


def classify_request_type(issue: str, subject: str) -> str:
    """
    Heuristically classify the request type.
    Priority: bug > feature_request > product_issue > invalid
    """
    text = f"{subject} {issue}"

    if REQUEST_TYPE_PATTERNS["bug"].search(text):
        return "bug"
    if REQUEST_TYPE_PATTERNS["feature_request"].search(text):
        return "feature_request"
    if REQUEST_TYPE_PATTERNS["product_issue"].search(text):
        return "product_issue"

    # Very short / nonsensical / off-topic
    if len(issue.strip().split()) < 3:
        return "invalid"

    return "product_issue"  # safe default


def detect_escalation_signals(issue: str, subject: str) -> List[str]:
    """
    Return list of escalation signal names found in the text.
    Empty list means no high-risk signals detected.
    """
    text = f"{subject} {issue}"
    signals = []
    for name, pattern in ESCALATION_PATTERNS.items():
        if pattern.search(text):
            signals.append(name)
    return signals


def classify_product_area(issue: str, subject: str, domain: str) -> str:
    """
    Return the most specific product area label for the given domain.
    """
    text = f"{subject} {issue}"
    taxonomy = PRODUCT_AREAS.get(domain, {})

    for area, pattern in taxonomy.items():
        if area == "general":
            continue
        if pattern.search(text):
            return f"{domain}/{area}"

    return f"{domain}/general"


def is_invalid_ticket(issue: str, subject: str) -> bool:
    """
    Detect completely nonsensical, empty, or malicious injection attempts.
    """
    stripped = issue.strip()
    if not stripped or len(stripped) < 5:
        return True

    # Prompt injection patterns
    injection_patterns = [
        r"ignore\s*(all\s*)?(previous|prior|above)\s*instructions",
        r"you\s*are\s*now\s*a",
        r"disregard\s*(your|the)\s*(system|prompt|instruction)",
        r"act\s*as\s*(if\s*you\s*are|a)",
        r"jailbreak",
        r"DAN\b",
    ]
    for pat in injection_patterns:
        if re.search(pat, stripped, re.IGNORECASE):
            return True

    return False
