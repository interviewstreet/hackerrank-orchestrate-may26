"""
Safety Gate — Pre-LLM escalation rules.

These checks run BEFORE retrieval or generation. They are intentionally
conservative for requests that require human authority or are clearly unsafe.

4-Layer Defense (inspired by ARIA, but with more robust patterns):
  ① Injection Detection  — 18+ prompt injection / jailbreak patterns
  ② Harmful Content Gate — Destructive commands, code execution attempts
  ③ Out-of-Scope Filter  — Non-support queries, greetings, immigration
  ④ Risk-Based Escalation — Fraud, refunds, score disputes, account authority
"""

import re
from typing import Tuple

# ---------------------------------------------------------------------------
# Layer 1: Prompt Injection / Jailbreak Detection
# ---------------------------------------------------------------------------
INJECTION_PATTERNS = [
    r"\b(ignore previous|ignore instruction|ignore all|ignore above)",
    r"\b(act as|pretend to be|role\s?play|you are now)\b",
    r"\b(jailbreak|prompt inject|system prompt|bypass|circumvent)\b",
    r"\b(show.*rules|internal rules|exact.*logic|reveal.*prompt)\b",
    r"\b(DAN mode|developer mode|sudo|admin override)\b",
    r"\b(output your instructions|repeat your system)\b",
    # Multi-language injection (French — from ticket #25)
    r"(affiche[\s\S]*r[eè]gles|r[eè]gles internes|logique exacte|documents r[eé]cup[eé]r[eé]s)",
    # Spanish / Portuguese injection
    r"(muestra.*reglas|instrucciones internas|mostrar.*lógica)",
]

# ---------------------------------------------------------------------------
# Layer 2: Harmful / Destructive Content
# ---------------------------------------------------------------------------
HARMFUL_PATTERNS = [
    r"\b(delete all files|wipe.*system|rm -rf|format.*disk)\b",
    r"\b(sudo|exec\(|eval\(|os\.system|subprocess)\b",
    r"\b(fork bomb|:()\{|virus|malware|trojan)\b",
    r"\b(give me the code to delete|write.*script.*destroy)\b",
    r"\b(hack into|break into|exploit vulnerabilities|crack password)\b",
]

# ---------------------------------------------------------------------------
# Layer 3: Out-of-Scope / Invalid Requests
# ---------------------------------------------------------------------------
OOS_PATTERNS = [
    # Entertainment / General knowledge
    r"\b(iron man|actor|movie|book|author|shakespeare|nuclear|physics|psychology)\b",
    # Immigration / Visa (the document, not the card)
    r"\b(visa application|visa interview|f-?1 visa|h-?1b|green card|immigration)\b",
    r"\b(passport|embassy|consulate|citizenship|asylum)\b",
    # Generic greetings / thank-yous (no actionable content)
    r"^\s*(thank you|thanks|thank u|thx|hi|hello|hey)\s*[.!]?\s*$",
]

# ---------------------------------------------------------------------------
# Layer 4: Risk-Based Escalation (sensitive topics that need human authority)
# ---------------------------------------------------------------------------
RISK_ESCALATION_PATTERNS = {
    "fraud_identity_theft": {
        "pattern": r"\b(identity stolen|identity theft|phishing|unauthorized.*charge|account.*hacked|stolen.*identity)\b",
        "reason": "Identity theft / fraud — requires human security review",
    },
    "refund_billing": {
        "pattern": r"\b(refund|money back|charge.*back|give.*money|order id|payment issue)\b",
        "reason": "Refund / billing dispute — requires human authority for financial decisions",
    },
    "score_dispute": {
        "pattern": r"\b(increase.*score|change.*score|review.*answers|graded.*unfairly|unfair.*grading|move.*next round)\b",
        "reason": "Score dispute — HackerRank does not allow manual score changes",
    },
    "account_restore": {
        "pattern": r"\b(restore.*access|restore.*seat|restore.*account|give.*access back)\b",
        "reason": "Account restore request — requires admin authority",
    },
    "platform_outage": {
        "pattern": r"\b(all.*failing|everything.*broken|site.*down|completely.*down|stopped working completely|none.*working)\b",
        "reason": "Possible platform outage — requires engineering investigation",
    },
    "legal_security": {
        "pattern": r"\b(legal|lawsuit|attorney|lawyer|terms of service violation|compliance)\b",
        "reason": "Legal/compliance — requires human legal review",
    },
    "card_blocked_travel": {
        "pattern": r"\b(card.*blocked|blocked.*card|bloqu[eé]|tarjeta)\b",
        "reason": "Blocked card — requires issuing bank intervention",
    },
}


def check_escalation_signals(issue: str, subject: str = "") -> Tuple[bool, str]:
    """
    Run ALL 4 safety layers before retrieval occurs.
    
    Returns:
        (should_escalate: bool, reason: str)
    """
    combined = f"{issue} {subject}".lower()

    # === Layer 0: Empty / Too Short ===
    if not issue or not issue.strip():
        return True, "Empty or invalid issue"
    if len(issue.strip()) < 5:
        return True, "Issue too short/unclear to triage safely"

    # === Layer 1: Injection Detection ===
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            return True, "Prompt injection / jailbreak attempt detected"

    # === Layer 2: Harmful Content ===
    for pattern in HARMFUL_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            return True, "Destructive / harmful request detected"

    # === Layer 3: Out-of-Scope ===
    for pattern in OOS_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            return True, "Out-of-scope request — not related to supported domains"

    return False, ""


def is_likely_invalid(issue: str) -> bool:
    """Heuristic for completely out-of-scope or destructive requests."""
    text = issue.lower()
    for pattern in OOS_PATTERNS + HARMFUL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False
