"""
ARIA - Safety Gate & Multi-Signal Classifier
Detects prompt injection, malicious intent, and classifies tickets before LLM call.
"""

import re
from typing import Dict, Tuple, Optional


# ─── Prompt Injection & Jailbreak Patterns ────────────────────────────────────
INJECTION_PATTERNS = [
    r"ignore (all )?(previous|above|prior) instructions",
    r"disregard (your )?(system|previous|above)",
    r"you are now",
    r"pretend (you are|to be)",
    r"act as (a |an )?(?!support)",
    r"reveal (your|all|the) (system prompt|instructions|rules|logic|corpus|documents)",
    r"show me (your|all|the) (internal|system|hidden)",
    r"what (are|is) your (internal rules|system prompt|instructions)",
    r"affiche (toutes les|les) règles internes",  # French injection (from ticket)
    r"display (all )?(retrieved|internal) (documents|rules|logic)",
    r"bypass (your|all|the) (rules|filters|safety)",
    r"jailbreak",
    r"DAN mode",
    r"sudo",
    r"override (safety|filter)",
]

# ─── High-Risk / Escalation Keywords ─────────────────────────────────────────
ESCALATION_TRIGGERS = {
    "fraud": ["fraud", "stolen card", "unauthorized transaction", "identity theft", "stolen identity",
              "hacked account", "account compromised", "unauthorized access"],
    "legal": ["lawsuit", "legal action", "i will sue", "attorney", "court order", "file a case"],
    "outage": ["site is down", "not working", "all requests failing", "completely down",
               "none of the pages", "platform down"],
    "security_vuln": ["security vulnerability", "bug bounty", "exploit", "vulnerability found",
                       "security flaw", "CVE", "injection", "XSS", "SQL injection"],
    "billing_dispute": ["refund", "charge dispute", "money back", "overcharged", "double charged"],
    "account_takeover": ["account stolen", "someone else logged in", "account hacked"],
    "data_breach": ["data breach", "data leaked", "personal data exposed"],
}

# ─── Out-of-Scope Patterns ────────────────────────────────────────────────────
OUT_OF_SCOPE_PATTERNS = [
    r"\bactor\b.*\bfilm\b|\bfilm\b.*\bactor\b",
    r"\biron man\b",
    r"thank you",
    r"^thanks",
    r"delete all files",
    r"rm -rf",
    r"system command",
    r"who is the president",
    r"weather (in|today)",
    r"sports score",
    r"recipe for",
    r"tell me a joke",
]

# ─── Malicious Code / System Harm Patterns ───────────────────────────────────
HARMFUL_PATTERNS = [
    r"delete all files",
    r"rm -rf",
    r"format (the )?(hard drive|disk|c:)",
    r"shutdown /",
    r":(){ :|:& };:",   # fork bomb
    r"base64 -d",
    r"wget .* \| bash",
    r"curl .* \| sh",
    r"exec\(",
    r"eval\(",
    r"__import__",
]

# ─── Domain Keywords for Inference ───────────────────────────────────────────
DOMAIN_KEYWORDS = {
    "HackerRank": [
        "hackerrank", "assessment", "test", "candidate", "recruiter", "coding challenge",
        "mock interview", "resume builder", "hackerrank for work", "interviewer",
        "submission", "hiring", "certificate", "invite", "variant", "apply tab",
        "proctored", "zoom", "inactivity", "subscription", "test score"
    ],
    "Claude": [
        "claude", "anthropic", "conversation", "chat", "prompt", "ai assistant",
        "workspace", "team plan", "bedrock", "api key", "claude api", "crawl",
        "robots.txt", "claudebot", "lti", "training data", "privacy", "model",
        "security vulnerability", "bug bounty"
    ],
    "Visa": [
        "visa", "card", "credit card", "debit card", "transaction", "payment",
        "merchant", "refund", "dispute", "chargeback", "atm", "traveller",
        "cheque", "fraud", "stolen card", "lost card", "blocked card",
        "identity theft", "cash", "emergency cash", "minimum spend"
    ],
}

# ─── Product Area Mapping ─────────────────────────────────────────────────────
PRODUCT_AREA_MAP = {
    "HackerRank": {
        "test": "assessments",
        "assessment": "assessments",
        "candidate": "assessments",
        "score": "assessments",
        "certificate": "assessments",
        "submission": "platform",
        "apply": "platform",
        "resume": "platform",
        "interview": "interviews",
        "zoom": "interviews",
        "inactivity": "interviews",
        "billing": "billing",
        "payment": "billing",
        "refund": "billing",
        "subscription": "billing",
        "user": "account_management",
        "admin": "account_management",
        "remove": "account_management",
        "employee": "account_management",
        "account": "account_management",
        "delete": "account_management",
        "infosec": "security",
        "security": "security",
        "down": "platform_status",
        "not working": "platform_status",
        "variants": "test_management",
        "variant": "test_management",
        "invite": "assessments",
    },
    "Claude": {
        "conversation": "privacy",
        "delete": "privacy",
        "data": "privacy",
        "training": "privacy",
        "crawl": "web_crawling",
        "robots": "web_crawling",
        "workspace": "team_access",
        "seat": "team_access",
        "access": "team_access",
        "bedrock": "api_integration",
        "api": "api_integration",
        "lti": "education",
        "professor": "education",
        "student": "education",
        "vulnerability": "security",
        "bug bounty": "security",
        "down": "service_status",
        "failing": "service_status",
    },
    "Visa": {
        "lost": "card_services",
        "stolen": "card_services",
        "blocked": "card_services",
        "card": "card_services",
        "dispute": "disputes",
        "chargeback": "disputes",
        "refund": "disputes",
        "fraud": "fraud_security",
        "identity": "fraud_security",
        "cash": "emergency_services",
        "emergency": "emergency_services",
        "traveller": "travel_support",
        "cheque": "travel_support",
        "minimum": "merchant_policies",
        "spend": "merchant_policies",
    },
}


class SafetyGate:
    """Pre-flight safety and validity checker."""

    def check_injection(self, text: str) -> Tuple[bool, str]:
        """Returns (is_injected, reason)"""
        text_lower = text.lower()
        for pattern in INJECTION_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return True, f"Prompt injection attempt detected: '{pattern}'"
        return False, ""

    def check_harmful(self, text: str) -> Tuple[bool, str]:
        """Returns (is_harmful, reason)"""
        text_lower = text.lower()
        for pattern in HARMFUL_PATTERNS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return True, f"Potentially harmful command detected"
        return False, ""

    def check_out_of_scope(self, text: str) -> Tuple[bool, str]:
        """Returns (is_oos, reason)"""
        text_lower = text.lower().strip()
        # Purely gratitude/social messages (very short only)
        if len(text.split()) <= 8:
            greetings = ["thank you", "thanks", "good morning", "good evening", "ok", "okay", "bye", "goodbye"]
            if any(text_lower.startswith(g) for g in greetings):
                return True, "Social/gratitude message, no actionable support issue"
        for pattern in OUT_OF_SCOPE_PATTERNS:
            # Skip "thank you" pattern for longer messages (could be part of a real request)
            if "thank you" in pattern and len(text.split()) > 8:
                continue
            if re.search(pattern, text_lower, re.IGNORECASE):
                return True, f"Out of scope: matched pattern '{pattern}'"
        return False, ""

    def get_escalation_signals(self, text: str) -> Dict[str, bool]:
        """Return dict of escalation signal categories triggered."""
        text_lower = text.lower()
        signals = {}
        for category, keywords in ESCALATION_TRIGGERS.items():
            for kw in keywords:
                if kw in text_lower:
                    signals[category] = True
                    break
        return signals


class TicketClassifier:
    """Multi-signal classifier for domain, urgency, intent, product area."""

    def __init__(self):
        self.safety = SafetyGate()

    def infer_domain(self, issue: str, subject: str, declared_company: str) -> str:
        """Infer the best domain from content if company is None or ambiguous."""
        if declared_company and declared_company.strip().lower() not in ["none", "", "nan"]:
            return declared_company.strip()

        combined = (issue + " " + (subject or "")).lower()
        scores = {domain: 0 for domain in DOMAIN_KEYWORDS}
        for domain, keywords in DOMAIN_KEYWORDS.items():
            for kw in keywords:
                if kw in combined:
                    scores[domain] += 1

        best = max(scores, key=scores.get)
        if scores[best] == 0:
            return "None"
        return best

    def classify_product_area(self, issue: str, subject: str, domain: str) -> str:
        """Classify which product area the ticket belongs to."""
        combined = (issue + " " + (subject or "")).lower()
        if domain in PRODUCT_AREA_MAP:
            area_map = PRODUCT_AREA_MAP[domain]
            scores = {}
            for keyword, area in area_map.items():
                if keyword in combined:
                    scores[area] = scores.get(area, 0) + 1
            if scores:
                return max(scores, key=scores.get)
        return "general_support"

    def classify_request_type(self, issue: str, subject: str, escalation_signals: Dict) -> str:
        """Classify request type: product_issue, feature_request, bug, invalid."""
        combined = (issue + " " + (subject or "")).lower()

        # Invalid: no real support request
        if re.search(r"(thank you|thanks|hello|hi there|good morning|who is|what is the name)", combined, re.IGNORECASE):
            if len(issue.split()) < 15:
                return "invalid"

        # Bug: platform/service not working
        bug_signals = ["not working", "down", "broken", "error", "crash", "failing", "bug",
                       "glitch", "issue with", "stopped working", "can't access", "unable to"]
        if any(s in combined for s in bug_signals):
            return "bug"

        # Feature request
        feature_signals = ["would like", "request", "can you add", "feature", "suggestion",
                           "would be great", "please add", "i wish", "could you implement"]
        if any(s in combined for s in feature_signals):
            return "feature_request"

        return "product_issue"

    def assess_urgency(self, issue: str, escalation_signals: Dict) -> str:
        """Return urgency level: low, medium, high, critical."""
        combined = issue.lower()
        if any(k in combined for k in ["urgent", "asap", "immediately", "emergency", "critical", "stolen", "fraud"]):
            return "critical"
        if escalation_signals:
            return "high"
        if any(k in combined for k in ["soon", "quickly", "today", "not working"]):
            return "medium"
        return "low"

    def should_escalate(self, issue: str, escalation_signals: Dict,
                        is_injection: bool, is_harmful: bool,
                        confidence: float, domain: str) -> Tuple[bool, str]:
        """
        Decision logic: should this ticket be escalated or replied to?
        Returns (should_escalate, reason)
        """
        # Always escalate injection/harm
        if is_injection:
            return True, "Security: prompt injection detected — escalating for manual review"
        if is_harmful:
            return True, "Security: potentially harmful request — escalating for manual review"

        # Escalate outages (platform-wide)
        if "outage" in escalation_signals:
            return True, "Platform outage reported — requires engineering/ops team"

        # Escalate fraud/identity theft
        if "fraud" in escalation_signals or "account_takeover" in escalation_signals or "data_breach" in escalation_signals:
            return True, "High-risk security/fraud issue — requires specialist team"

        # Escalate identity theft
        issue_lower_check = issue.lower()
        if "identity" in issue_lower_check and ("stolen" in issue_lower_check or "theft" in issue_lower_check):
            return True, "Identity theft report — requires fraud/security specialist team"

        # Escalate legal threats
        if "legal" in escalation_signals:
            return True, "Legal threat detected — requires legal/compliance team"

        # Security vulnerability reports get escalated to security team
        if "security_vuln" in escalation_signals:
            # Special case: we can still provide guidance + escalate
            return True, "Security vulnerability report — escalating to security team per responsible disclosure"

        # Low confidence = insufficient corpus coverage
        if confidence < 0.05:
            return True, f"Insufficient corpus coverage (confidence: {confidence:.3f}) — escalating to human agent"

        # Requests that are inherently not actionable by support
        impossible_requests = [
            "change my score", "increase my score", "tell the company",
            "force the recruiter", "ban the seller", "make visa refund",
            "restore my access even though i am not",
        ]
        issue_lower = issue.lower()
        for req in impossible_requests:
            if req in issue_lower:
                return True, f"Request cannot be actioned by support (policy limitation): '{req}'"

        return False, ""

    def full_classify(self, issue: str, subject: str, company: str) -> Dict:
        """Run full classification pipeline on a ticket."""
        # Safety checks
        is_injected, inject_reason = self.safety.check_injection(issue + " " + (subject or ""))
        is_harmful, harm_reason = self.safety.check_harmful(issue)
        is_oos, oos_reason = self.safety.check_out_of_scope(issue)

        # Domain inference
        domain = self.infer_domain(issue, subject, company)

        # Escalation signals
        escalation_signals = self.safety.get_escalation_signals(issue)

        # Product area
        product_area = self.classify_product_area(issue, subject, domain)

        # Request type
        request_type = self.classify_request_type(issue, subject, escalation_signals)
        if is_oos or is_injected or is_harmful:
            request_type = "invalid"

        # Urgency
        urgency = self.assess_urgency(issue, escalation_signals)

        return {
            "domain": domain,
            "product_area": product_area,
            "request_type": request_type,
            "urgency": urgency,
            "escalation_signals": escalation_signals,
            "is_injected": is_injected,
            "inject_reason": inject_reason,
            "is_harmful": is_harmful,
            "harm_reason": harm_reason,
            "is_oos": is_oos,
            "oos_reason": oos_reason,
        }
