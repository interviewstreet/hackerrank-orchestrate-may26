"""Pure-Python escalation policy decision table.

Evaluates triggers T-1..T-6 in order; first match wins. No LLM calls. All
thresholds are caller-injected so they can be tuned via config.yaml.

PRD references: FR-040..FR-042, T-1..T-6, AC-5..AC-8.
Architecture references: section 3.9, section 9.
"""

from __future__ import annotations

import re

from prompts.canned_responses import CHITCHAT_REPLY, OUT_OF_SCOPE_REPLY
from schemas import (
    CleanedTicket,
    ClassificationResult,
    EscalationDecision,
    ReasoningResult,
    RetrievedDoc,
)

DEFAULT_RETRIEVAL_MIN_SCORE = 0.32
DEFAULT_DOMAIN_MIN_CONFIDENCE = 0.6


def decide(
    *,
    cleaned: CleanedTicket,
    classification: ClassificationResult,
    retrieval: list[RetrievedDoc],
    reasoning: ReasoningResult | None,
    grounding_failed: bool = False,
    retrieval_min_score: float = DEFAULT_RETRIEVAL_MIN_SCORE,
    domain_min_confidence: float = DEFAULT_DOMAIN_MIN_CONFIDENCE,
) -> EscalationDecision:
    """Return an EscalationDecision per Architecture §3.9 first-match-wins.

    Order:
      T-6 injection         -> Escalated, invalid
      T-3 outage            -> Escalated, bug
      T-2 sensitive         -> Escalated, keep classifier request_type
      T-2 authz violation   -> Escalated, keep classifier request_type
      T-4 multi_request     -> Escalated, keep classifier request_type
      T-5 domain=none low conf + weak retrieval -> Escalated, keep request_type
      T-1 weak retrieval / can_answer=False / grounding_failed -> Escalated
      Chitchat allowance    -> Replied, invalid (canned)
      Happy path            -> Replied, reasoner output
    """
    request_type = classification.request_type
    product_area = classification.product_area
    top1_score = retrieval[0].cosine_score if retrieval else 0.0

    # T-6 injection — short-circuit before any other trigger.
    if cleaned.injection_detected:
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-6"],
            final_request_type="invalid",
            final_response="",
            final_justification="trigger T-6: prompt injection detected; escalated for human review.",
            final_product_area=product_area or "uncategorized",
        )

    # T-3 outage report — always escalate as bug.
    if classification.is_outage_report:
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-3"],
            final_request_type="bug",
            final_response="",
            final_justification="trigger T-3: outage / service-down report; escalated for engineering follow-up.",
            final_product_area=product_area or "uncategorized",
        )

    # T-2 sensitive (fraud / dispute / vulnerability / etc.).
    if classification.is_sensitive:
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-2"],
            final_request_type=request_type,
            final_response="",
            final_justification="trigger T-2: sensitive topic (security / billing dispute / vulnerability); escalated for specialist handling.",
            final_product_area=product_area or "uncategorized",
        )

    # T-2 authorization violation.
    if classification.is_authorization_violation:
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-2"],
            final_request_type=request_type,
            final_response="",
            final_justification="trigger T-2: request requires authorization beyond what self-service can grant; escalated for human approval.",
            final_product_area=product_area or "uncategorized",
        )

    # T-4 multi-request with weak coverage.
    if classification.is_multi_request and top1_score < retrieval_min_score:
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-4"],
            final_request_type=request_type,
            final_response="",
            final_justification="trigger T-4: ticket bundles multiple distinct asks and at least one is not covered by the corpus; escalated for human triage.",
            final_product_area=product_area or "uncategorized",
        )

    # T-5 unknown domain with low confidence and weak retrieval.
    if (
        classification.domain == "none"
        and classification.domain_confidence < domain_min_confidence
        and top1_score < retrieval_min_score
    ):
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-5"],
            final_request_type=request_type,
            final_response="",
            final_justification="trigger T-5: domain inference confidence too low and corpus retrieval is weak; escalated for human triage.",
            final_product_area=product_area or "uncategorized",
        )

    # Chitchat allowance — reply with canned out-of-scope text.
    # Must fire BEFORE T-1 because chitchat tickets intentionally have empty
    # retrieval (the pipeline skips it) and would otherwise trip "weak retrieval".
    if classification.is_chitchat_or_trivia:
        return EscalationDecision(
            status="Replied",
            triggers_fired=[],
            final_request_type="invalid",
            final_response=OUT_OF_SCOPE_REPLY,
            final_justification="non-support / chitchat content; replied with out-of-scope acknowledgement.",
            final_product_area=product_area or "uncategorized",
        )

    # T-1 weak retrieval / can-not-answer / grounding-failed.
    can_answer = bool(reasoning and reasoning.can_answer_from_corpus)
    weak_retrieval = top1_score < retrieval_min_score
    if weak_retrieval or not can_answer or grounding_failed:
        cause: list[str] = []
        if weak_retrieval:
            cause.append("retrieval below confidence threshold")
        if not can_answer:
            cause.append("reasoner declined to answer from corpus")
        if grounding_failed:
            cause.append("grounding verifier rejected response")
        return EscalationDecision(
            status="Escalated",
            triggers_fired=["T-1"],
            final_request_type=request_type,
            final_response="",
            final_justification=f"trigger T-1: {'; '.join(cause)}.",
            final_product_area=product_area or "uncategorized",
        )

    # Happy path — corpus-grounded reply from reasoner.
    assert reasoning is not None  # implied by can_answer check above
    return EscalationDecision(
        status="Replied",
        triggers_fired=[],
        final_request_type=request_type,
        final_response=reasoning.response,
        final_justification=reasoning.justification or "Answer drawn from support corpus.",
        final_product_area=product_area or "uncategorized",
    )


# ---------------------------------------------------------------------------
# Optional regex helpers (kept for Iter 5 testing — currently unused at runtime
# because the LLM classifier already populates is_sensitive / is_authz_violation
# based on the system-prompt criteria).
# ---------------------------------------------------------------------------

_SENSITIVE_RE = re.compile(
    r"(?i)\b("
    r"identity\s+theft|stolen\s+card|fraud(?:ulent)?|disput(?:e|ed)\s+(?:charge|transaction)"
    r"|chargeback|subpoena|breach|vulnerability|bug\s+bounty|self[- ]?harm|suicide"
    r")\b"
)

_AUTHZ_RE = re.compile(
    r"(?i)("
    r"(restore|grant)\s+(my\s+)?access"
    r"|(increase|change|update)\s+my\s+score"
    r"|delete\s+(this|that|other)\s+(user|account)"
    r"|make\s+.{0,20}refund"
    r"|ban\s+(the\s+|this\s+)?(seller|user)"
    r")"
)


def regex_sensitive(text: str) -> bool:
    """Defense-in-depth check the LLM may already have flagged."""
    return bool(_SENSITIVE_RE.search(text or ""))


def regex_authz_violation(text: str) -> bool:
    return bool(_AUTHZ_RE.search(text or ""))
