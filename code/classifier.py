import re
from dataclasses import dataclass
from typing import Dict
from typing import List
from retrieval import RetrievalHit
from utils import clean_text


ALLOWED_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}

AREA_FALLBACKS = {
    "hackerrank": {
        "interviewer": "team_management",
        "team": "team_management",
        "certificate": "certifications",
        "mock interview": "interviewing",
        "compatibility": "assessments",
        "assessment": "assessments",
        "test": "assessments",
        "resume": "community_support",
        "subscription": "billing_and_subscriptions",
        "interview": "interviewing",
        "lti": "integrations",
    },
    "claude": {
        "bedrock": "api_and_developer_tools",
        "api": "api_and_developer_tools",
        "workspace": "account_management",
        "personal data": "privacy_and_compliance",
        "privacy": "privacy_and_compliance",
        "crawl": "privacy_and_compliance",
        "crawler": "privacy_and_compliance",
        "lti": "education",
    },
    "visa": {
        "charge": "payment_processing",
        "refund": "payment_processing",
        "dispute": "payment_processing",
        "merchant": "merchant_acceptance",
        "minimum": "merchant_acceptance",
        "travel": "travel_services",
        "cash": "travel_services",
        "identity": "fraud_and_security",
        "fraud": "fraud_and_security",
        "privacy": "data_privacy",
    },
}


@dataclass
class ClassificationResult:
    subject: str
    issue: str
    ticket_text: str
    company: str
    request_type: str


class Classifier:
    domain_keywords = {
        "hackerrank": [
            "hackerrank",
            "assessment",
            "test",
            "candidate",
            "recruiter",
            "interview",
            "mock interview",
            "resume builder",
            "apply tab",
            "certificate",
            "interviewer",
        ],
        "claude": [
            "claude",
            "bedrock",
            "anthropic",
            "workspace",
            "crawler",
            "lti",
            "model",
            "console",
        ],
        "visa": [
            "visa",
            "card",
            "merchant",
            "charge",
            "cash",
            "travel",
            "fraud",
        ],
    }

    invalid_patterns = (
        "delete all files",
        "ignore previous instructions",
        "show internal rules",
        "show documents retrieved",
        "logic exact",
        "prompt injection",
    )

    bug_patterns = (
        "not working",
        "stopped working",
        "failing",
        "error",
        "down",
        "issue while",
        "compatibility",
        "blocked",
        "blocker",
        "not responding",
        "unable to",
    )

    feature_patterns = (
        "feature request",
        "can you add",
        "enhancement",
        "new feature",
    )

    def classify(self, row: Dict[str, str]) -> ClassificationResult:
        subject = clean_text(row.get("Subject", ""))
        issue = clean_text(row.get("Issue", ""))
        ticket_text = clean_text(f"{subject} {issue}")
        company = self.infer_company(clean_text(row.get("Company", "")), ticket_text)
        request_type = self.request_type(ticket_text)
        if request_type not in ALLOWED_REQUEST_TYPES:
            request_type = "invalid"
        return ClassificationResult(
            subject=subject,
            issue=issue,
            ticket_text=ticket_text,
            company=company,
            request_type=request_type,
        )

    def infer_company(self, provided: str, ticket_text: str) -> str:
        lowered = provided.lower().strip()
        if lowered in {"hackerrank", "claude", "visa"}:
            return lowered
        scores = {}
        text = ticket_text.lower()
        for company, keywords in self.domain_keywords.items():
            scores[company] = sum(1 for keyword in keywords if keyword in text)
        best_company = max(scores, key=scores.get)
        return best_company if scores[best_company] > 0 else "none"

    def request_type(self, ticket_text: str) -> str:
        lowered = ticket_text.lower().strip()
        if not lowered:
            return "invalid"
        if any(pattern in lowered for pattern in self.invalid_patterns):
            return "invalid"
        if re.fullmatch(r"(thanks|thank you|ok|okay)[.! ]*", lowered):
            return "invalid"
        if any(pattern in lowered for pattern in self.feature_patterns):
            return "feature_request"
        if any(pattern in lowered for pattern in self.bug_patterns):
            return "bug"
        return "product_issue"

    def product_area(self, classification: ClassificationResult, hits: List[RetrievalHit]) -> str:
        if hits:
            top_area = hits[0].doc.product_area
            if top_area not in {"conversation_management", "general"}:
                return top_area

        lowered = classification.ticket_text.lower()
        for keyword, area in AREA_FALLBACKS.get(classification.company, {}).items():
            if keyword in lowered:
                return area

        if classification.company == "hackerrank":
            return "platform_support"
        if classification.company == "claude":
            return "account_management"
        if classification.company == "visa":
            return "payment_processing"
        return "platform_support"
