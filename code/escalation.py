"""Pre-LLM and post-LLM rule-based escalation/triage gates."""
from __future__ import annotations

import re
from dataclasses import dataclass

from schemas import LLMOutput, TicketInput

# Compiled in priority order. First match wins.
PRE_RULES: list[tuple[str, re.Pattern[str], str]] = [
    ("prompt_inject",
     re.compile(r"(?is)(ignore\s+(all\s+|previous\s+)?instructions|"
                r"disregard\s+(your|the)\s+(rules|prompt)|"
                r"reveal\s+(your\s+)?system\s+prompt|"
                r"show\s+(me\s+)?(your\s+)?(internal|hidden)\s+(rules|prompt|docs)|"
                r"affiche.*r[eè]gles\s+internes)",
                ),
     "escalated"),
    ("legal_threat",
     re.compile(r"(?i)\b(lawsuit|legal\s+action|attorney|subpoena|sue\s+you)\b"),
     "escalated"),
    ("fraud_or_hack",
     re.compile(r"(?i)\b(fraud|stolen\s+card|unauthorized\s+(charge|access)|"
                r"chargeback|account\s+(was\s+)?(hacked|compromised)|"
                r"identity\s+theft)\b"),
     "escalated"),
    ("pii_dump",
     re.compile(r"(?i)(social\s+security\s*\#?:?\s*\d|"
                r"passport\s+(no|number)\s*[:#]?\s*\w|"
                r"(credit|debit)\s+card\s+(number|no)\s*[:#]?\s*\d)"),
     "escalated"),
    ("score_appeal",
     re.compile(r"(?i)(recruiter\s+rejected|review\s+my\s+answers|"
                r"reconsider\s+my\s+(score|result)|increase\s+my\s+score|"
                r"appeal\s+(the\s+)?(decision|result))"),
     "escalated"),
    ("access_restore_non_admin",
     re.compile(r"(?i)(restore\s+my\s+access).{0,80}(not.*(owner|admin)|"
                r"even\s+though\s+i\s+am\s+not)"),
     "escalated"),
    ("refund_demand",
     re.compile(r"(?i)\b(refund\s+(me\s+)?(asap|now|immediately)|"
                r"i\s+want\s+a\s+refund|give\s+me\s+(my\s+)?refund)\b"),
     "escalated"),
    ("site_outage",
     re.compile(r"(?i)(site\s+is\s+down|none\s+of\s+the\s+pages?|"
                r"entire\s+platform\s+down|all\s+submissions?.{0,30}not\s+working|"
                r"none\s+of\s+the\s+submissions?\s+(across|are)|"
                r"nothing\s+is\s+loading)"),
     "escalated"),
    ("dangerous_system_request",
     re.compile(r"(?i)(delete\s+all\s+files|rm\s+-rf|drop\s+(all\s+)?(table|database)|"
                r"give\s+me\s+the\s+code\s+to\s+(delete|destroy|wipe))"),
     "invalid_reply"),
    ("trivial_pleasantry",
     re.compile(r"^\s*(thanks?(\s+you)?|thank\s+you|hi|hello|hey|ok|okay|"
                r"happy\s+to\s+help|good(\s+morning|\s+evening)?)\s*[!.\s]*$",
                re.IGNORECASE),
     "invalid_reply"),
    ("off_topic_trivia",
     re.compile(r"(?i)(name\s+of\s+the\s+actor|who\s+(is|was)\s+the\s+(president|"
                r"actor|singer)|capital\s+of\s+\w+|"
                r"how\s+(do\s+i\s+)?(cook|bake|make)\s+\w+)"),
     "invalid_reply"),
]


@dataclass
class PreCheck:
    decision: str  # "pass" | "escalated" | "invalid_reply"
    rule: str
    message: str = ""


def pre_check(ticket: TicketInput) -> PreCheck:
    text = f"{ticket.subject}\n{ticket.issue}".strip()
    for name, pat, decision in PRE_RULES:
        if pat.search(text):
            msg = _canned_message(decision, name)
            return PreCheck(decision=decision, rule=name, message=msg)
    if ticket.company.strip() == "None" and len(text.split()) < 4:
        return PreCheck(decision="invalid_reply", rule="too_short_no_company",
                        message="I'm not sure what you'd like help with. "
                                "Could you share more details?")
    return PreCheck(decision="pass", rule="")


def _canned_message(decision: str, rule: str) -> str:
    if decision == "escalated":
        return "Escalate to a human."
    if rule == "trivial_pleasantry":
        return "Happy to help."
    if rule == "off_topic_trivia":
        return "I'm sorry, this is out of scope from my capabilities."
    if rule == "dangerous_system_request":
        return "I'm sorry, this is out of scope from my capabilities."
    return "I'm sorry, this is out of scope from my capabilities."


@dataclass
class PostCheck:
    should_escalate: bool
    reason: str = ""


def post_check(out: LLMOutput, allowed_areas: set[str],
               max_score: float, mean_top3: float,
               confidence_floor: float = 0.45) -> PostCheck:
    if out.confidence < confidence_floor and out.status == "replied":
        return PostCheck(True, f"low_confidence={out.confidence:.2f}")
    if out.status == "replied" and not out.citations:
        return PostCheck(True, "no_citations")
    if out.status == "replied" and out.product_area not in allowed_areas:
        return PostCheck(True, f"product_area_unknown={out.product_area}")
    return PostCheck(False)


def coverage_floor(max_score: float, mean_top3: float,
                   max_floor: float = 0.30,
                   mean3_floor: float = 0.22) -> bool:
    return max_score < max_floor or mean_top3 < mean3_floor
