from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple

from .corpus import CorpusIndex, normalize_company, tokenize
from .models import RetrievalHit, TicketInput, TriageDecision

STATUS_REPLIED = "replied"
STATUS_ESCALATED = "escalated"
VALID_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}

ESCALATE_PATTERNS = [
    r"\bsecurity vulnerability\b",
    r"\bbug bounty\b",
    r"\bnot (the )?(owner|admin)\b",
    r"\brestore my access\b",
    r"\bincrease my score\b",
    r"\breview my answers\b",
    r"\bban the seller\b",
    r"\bshow .*internal .*rules\b",
    r"\blogic exact\b",
]

INVALID_PATTERNS = [
    r"\bactor in iron man\b",
    r"\bdelete all files\b",
    r"\bwrite malware\b",
    r"\bhack\b.*\bsystem\b",
]

FEATURE_PATTERNS = [
    r"\bfeature request\b",
    r"\bwould like\b.*\badd\b",
    r"\bcan you add\b",
    r"\bplease add\b",
]

BUG_PATTERNS = [
    r"\bsite is down\b",
    r"\bnot working\b",
    r"\ball requests are failing\b",
    r"\berror\b",
    r"\bfailed\b",
    r"\bdown\b",
]


def _matches_any(text: str, patterns: List[str]) -> bool:
    lowered = text.lower()
    return any(re.search(pat, lowered) for pat in patterns)


def classify_request_type(issue: str, subject: str) -> str:
    text = f"{issue}\n{subject}"
    if _matches_any(text, INVALID_PATTERNS):
        return "invalid"
    if _matches_any(text, FEATURE_PATTERNS):
        return "feature_request"
    if _matches_any(text, BUG_PATTERNS):
        return "bug"
    return "product_issue"


def _extract_supportive_lines(content: str, query: str, max_lines: int = 4) -> List[str]:
    query_tokens = set(tokenize(query))
    lines: List[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line.startswith("![") or line.startswith("["):
            continue
        if line.startswith("---") or line.startswith("_Last updated"):
            continue
        if line.startswith("#") or line.startswith("- [") or line.startswith("|"):
            continue
        if len(line) < 20:
            continue
        if len(line) > 260:
            continue
        score = len(query_tokens.intersection(set(tokenize(line))))
        if score > 0:
            lines.append(line)
        if len(lines) >= max_lines:
            break
    if lines:
        return lines

    fallback: List[str] = []
    for raw in content.splitlines():
        line = raw.strip()
        if (
            line
            and len(line) >= 30
            and len(line) <= 260
            and not line.startswith("#")
            and not line.startswith("- [")
            and not line.startswith("|")
        ):
            fallback.append(line)
        if len(fallback) >= max_lines:
            break
    return fallback


def _confidence(hits: List[RetrievalHit]) -> float:
    if not hits:
        return 0.0
    top = hits[0].score
    second = hits[1].score if len(hits) > 1 else 0.0
    return top / (top + second + 1.0)


def _should_escalate(ticket: TicketInput, request_type: str, conf: float, hits: List[RetrievalHit]) -> Tuple[bool, str]:
    text = f"{ticket.issue}\n{ticket.subject}"
    if _matches_any(text, ESCALATE_PATTERNS):
        return True, "high_risk_or_permission_sensitive"
    if request_type == "invalid":
        # Invalid requests can still be replied to with out-of-scope guidance.
        return False, "out_of_scope"
    if request_type == "bug" and conf < 0.33:
        return True, "bug_low_grounding"
    if conf < 0.27 or not hits:
        return True, "low_retrieval_confidence"
    return False, "safe_to_reply"


def _build_escalation_response(reason: str) -> str:
    if reason == "high_risk_or_permission_sensitive":
        return (
            "I cannot safely complete this request directly. "
            "I am escalating this ticket to a human support specialist for secure verification and handling."
        )
    if reason == "bug_low_grounding":
        return (
            "I could not find enough grounded troubleshooting guidance in the provided support corpus. "
            "I am escalating this to human support for investigation."
        )
    if reason == "low_retrieval_confidence":
        return (
            "I do not have enough high-confidence, corpus-backed guidance to answer safely. "
            "This ticket is being escalated to a human agent."
        )
    return "This request is outside the support scope. Please contact the relevant support team for further help."


def _build_reply_response(ticket: TicketInput, hits: List[RetrievalHit]) -> str:
    top = hits[0].doc
    query = f"{ticket.issue} {ticket.subject}"
    lines = _extract_supportive_lines(top.content, query, max_lines=4)
    if not lines:
        if top.source_url:
            return f"Please refer to: {top.source_url}"
        return "I found a relevant support article and recommend following the documented steps there."

    sentence = " ".join(lines[:3]).strip()
    if len(sentence) > 550:
        sentence = sentence[:550].rsplit(" ", 1)[0] + "..."
    if top.source_url:
        return f"{sentence}\n\nSource: {top.source_url}"
    return sentence


def triage_ticket(ticket: TicketInput, index: CorpusIndex) -> TriageDecision:
    request_type = classify_request_type(ticket.issue, ticket.subject)
    query = f"{ticket.issue}\n{ticket.subject}\n{ticket.company}"
    hits = index.search(query=query, company=ticket.company, top_k=3)
    conf = _confidence(hits)
    escalate, reason = _should_escalate(ticket, request_type, conf, hits)

    product_area = "general_support"
    if hits:
        product_area = hits[0].doc.product_area or "general_support"

    if escalate:
        return TriageDecision(
            status=STATUS_ESCALATED,
            product_area=product_area,
            response=_build_escalation_response(reason),
            justification=f"Escalated due to {reason}; retrieval_confidence={conf:.2f}.",
            request_type=request_type if request_type in VALID_REQUEST_TYPES else "invalid",
        )

    if request_type == "invalid":
        return TriageDecision(
            status=STATUS_REPLIED,
            product_area=product_area,
            response="This request appears outside the supported HackerRank/Claude/Visa support scope.",
            justification=f"Replied as out-of-scope invalid request; retrieval_confidence={conf:.2f}.",
            request_type="invalid",
        )

    return TriageDecision(
        status=STATUS_REPLIED,
        product_area=product_area,
        response=_build_reply_response(ticket, hits),
        justification=f"Replied using corpus document '{hits[0].doc.doc_id}' with retrieval_confidence={conf:.2f}.",
        request_type=request_type if request_type in VALID_REQUEST_TYPES else "product_issue",
    )


def _get_case_insensitive(row: Dict[str, str], key: str) -> str:
    if key in row:
        return row.get(key, "") or ""
    lower_map = {k.lower(): v for k, v in row.items()}
    return lower_map.get(key.lower(), "") or ""


def run_batch(input_csv: str, output_csv: str, index: CorpusIndex) -> None:
    tickets: List[TicketInput] = []
    with open(input_csv, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            issue = _get_case_insensitive(row, "Issue").strip()
            subject = _get_case_insensitive(row, "Subject").strip()
            company = normalize_company(_get_case_insensitive(row, "Company"))
            tickets.append(TicketInput(issue=issue, subject=subject, company=company))

    out_path = Path(output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "issue",
                "subject",
                "company",
                "response",
                "product_area",
                "status",
                "request_type",
                "justification",
            ],
        )
        writer.writeheader()
        for ticket in tickets:
            decision = triage_ticket(ticket, index)
            writer.writerow(
                {
                    "issue": ticket.issue,
                    "subject": ticket.subject,
                    "company": ticket.company,
                    "response": decision.response,
                    "product_area": decision.product_area,
                    "status": decision.status,
                    "request_type": decision.request_type,
                    "justification": decision.justification,
                }
            )
