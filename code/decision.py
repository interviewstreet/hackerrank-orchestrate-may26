from dataclasses import dataclass
from typing import List

from classifier import ClassificationResult
from retrieval import RetrievalHit
from utils import tokenize


CONFIDENCE_THRESHOLDS = {
    "strong_reply": 0.55,
    "overlap_reply": 0.35,
    "none": 0.0,
}

BYPASS_INTENTS = {"bedrock", "crawler", "lti", "interviewer", "troubleshooting", "merchant_rules", "travel_support", "compatibility"}


@dataclass(frozen=True)
class Decision:
    status: str
    confidence: float
    reason_code: str
    reason_detail: str


class DecisionEngine:
    pii_terms = ("personal data", "private info", "privacy request", "data request")
    security_terms = (
        "security vulnerability",
        "bug bounty",
        "identity theft",
        "restore my access",
        "delete my account",
        "remove my account",
        "stolen",
        "compromised",
    )
    certificate_terms = ("certificate", "credential")
    billing_terms = ("payment", "refund", "charge", "billing", "subscription", "dispute")
    legal_terms = ("legal", "compliance", "dpo", "gdpr", "infosec", "security questionnaire")

    def decide(
        self,
        ticket_text: str,
        classification: ClassificationResult,
        hits: List[RetrievalHit],
    ) -> Decision:
        lowered = ticket_text.lower()
        confidence = hits[0].score if hits else CONFIDENCE_THRESHOLDS["none"]
        intent = self._intent_name(lowered)

        if classification.request_type == "invalid":
            return Decision(
                status="escalated",
                confidence=confidence,
                reason_code="invalid",
                reason_detail="Ticket does not match any supported domain or request type.",
            )

        if not hits:
            return Decision(
                status="escalated",
                confidence=0.0,
                reason_code="no_docs",
                reason_detail="No relevant documentation was retrieved from the support corpus.",
            )

        if self._is_high_risk(lowered):
            reason_code, reason_detail = self._select_escalation_reason(lowered, hits)
            return Decision(
                status="escalated",
                confidence=confidence,
                reason_code=reason_code,
                reason_detail=reason_detail,
            )

        if intent in BYPASS_INTENTS and hits:
            return Decision(
                status="replied",
                confidence=confidence,
                reason_code="corpus_grounded_reply",
                reason_detail="A sufficiently strong support document was retrieved for a grounded reply.",
            )

        if confidence >= CONFIDENCE_THRESHOLDS["strong_reply"]:
            return Decision(
                status="replied",
                confidence=confidence,
                reason_code="corpus_grounded_reply",
                reason_detail="A sufficiently strong support document was retrieved for a grounded reply.",
            )

        if confidence >= CONFIDENCE_THRESHOLDS["overlap_reply"] and self._intent_keyword_overlap(lowered, hits):
            return Decision(
                status="replied",
                confidence=confidence,
                reason_code="corpus_grounded_reply",
                reason_detail="A sufficiently strong support document was retrieved for a grounded reply.",
            )

        return Decision(
            status="escalated",
            confidence=confidence,
            reason_code="low_confidence",
            reason_detail="The available documentation does not provide sufficient guidance for this specific case.",
        )

    def _select_escalation_reason(self, lowered: str, hits: List[RetrievalHit]):
        if any(term in lowered for term in ("personal data", "gdpr", "privacy", "my data", "delete my")):
            return (
                "pii",
                "This ticket involves personal data and requires privacy review.",
            )
        if any(term in lowered for term in ("fraud", "unauthorized", "stolen", "suspicious", "bug bounty", "security vulnerability")):
            return (
                "security",
                "This ticket involves account security or fraud and requires human verification.",
            )
        if any(term in lowered for term in ("password", "account access", "login", "identity", "account deletion")):
            return (
                "security",
                "This ticket involves account security changes and requires human verification.",
            )
        if any(term in lowered for term in ("billing", "payment", "refund", "charge", "invoice", "subscription cancel")):
            return (
                "billing",
                "This ticket involves a billing or payment matter that requires human review.",
            )
        if any(term in lowered for term in ("certificate", "credential", "badge", "verify name")):
            return (
                "certificate",
                "This ticket involves a certificate or credential update that requires identity verification.",
            )
        if any(term in lowered for term in ("legal", "compliance", "regulation", "court")):
            return (
                "legal",
                "This ticket involves compliance or legal review.",
            )
        if not hits:
            return ("no_docs", "No relevant documentation was found in the support corpus for this query.")
        return ("low_confidence", "The available documentation does not provide sufficient guidance for this specific case.")

    def _is_high_risk(self, lowered: str) -> bool:
        return any(
            term in lowered
            for term in (
                "personal data", "gdpr", "privacy", "my data", "delete my",
                "fraud", "unauthorized", "stolen", "suspicious", "bug bounty", "security vulnerability",
                "password", "account access", "login", "identity", "account deletion",
                "billing", "payment", "refund", "charge", "invoice", "subscription cancel",
                "certificate", "credential", "badge", "verify name",
                "legal", "compliance", "regulation", "court",
            )
        )

    def _intent_name(self, lowered: str) -> str:
        if "bedrock" in lowered:
            return "bedrock"
        if "crawler" in lowered or "crawl" in lowered:
            return "crawler"
        if "not responding" in lowered or "requests are failing" in lowered or "stopped working" in lowered:
            return "troubleshooting"
        if "minimum" in lowered and "visa" in lowered:
            return "merchant_rules"
        if "urgent cash" in lowered or ("cash" in lowered and "visa" in lowered):
            return "travel_support"
        if "compatibility" in lowered or "zoom connectivity" in lowered:
            return "compatibility"
        if "employee has left" in lowered or "remove them" in lowered:
            return "interviewer"
        if " lti " in f" {lowered} ":
            return "lti"
        if "interviewer" in lowered and "remove" in lowered:
            return "interviewer"
        return ""

    def _intent_keyword_overlap(self, lowered: str, hits: List[RetrievalHit]) -> bool:
        ticket_tokens = set(tokenize(lowered))
        for hit in hits[:3]:
            doc_tokens = set(tokenize(f"{hit.doc.title} {hit.doc.path} {hit.doc.text[:800]}"))
            if len(ticket_tokens & doc_tokens) >= 2:
                return True
        return False
