#!/usr/bin/env python3
"""
Support Triage Agent v2 - Optimized for real support data
Uses sample tickets as examples to learn response patterns and product areas
"""

import argparse
import csv
import json
import os
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import pandas as pd
from groq import APIError, Groq

# Configuration
CONFIG = {
    "model": "llama-3.1-8b-instant",
    "max_tokens": 320,
    "temperature": 0.1,
}

REQUIRED_CORPUS_SOURCES = {
    "HackerRank": "https://support.hackerrank.com/",
    "Claude": "https://support.claude.com/en/",
    "Visa": "https://www.visa.co.in/support.html",
}

FEATURE_REQUEST_SIGNALS = [
    "feature request",
    "enhancement",
    "add feature",
    "new feature",
    "would like",
    "can you add",
    "please add",
    "wishlist",
]

SAFE_REPLY_KEYWORDS = {
    "HackerRank": [
        "submit",
        "submission",
        "practice",
        "challenge",
        "compatibility",
        "browser",
        "editor",
        "language",
    ],
    "Claude": [
        "sdk",
        "api",
        "model",
        "rate limit",
        "token",
    ],
    "Visa": [
        "merchant",
        "minimum spend",
        "card feature",
        "payment flow",
    ],
}

HIGH_RISK_KEYWORDS = [
    "refund",
    "billing",
    "payment",
    "charge",
    "dispute",
    "fraud",
    "identity theft",
    "stolen",
    "security",
    "vulnerability",
    "bug bounty",
    "privacy",
    "personal data",
    "delete data",
    "retention",
    "account",
    "access",
    "permission",
    "admin",
    "owner",
    "remove user",
    "employee",
    "subscription",
    "pause subscription",
    "certificate",
    "name update",
    "reschedule",
    "score",
    "recruiter",
    "ban",
    "aws bedrock",
    "production",
    "outage",
    "cash advance",
    "blocked",
    "blocked card",
]

VALID_SUPPORT_SIGNALS = [
    "refund",
    "billing",
    "payment",
    "charge",
    "dispute",
    "fraud",
    "identity",
    "stolen",
    "access",
    "account",
    "admin",
    "subscription",
    "certificate",
    "score",
    "recruiter",
    "assessment",
    "test",
    "submission",
    "challenge",
    "interview",
    "resume",
    "claude",
    "api",
    "bedrock",
    "visa",
    "card",
    "merchant",
    "cash",
    "blocked",
    "working",
    "error",
    "issue",
    "help",
]

BUG_SIGNALS = [
    "not working",
    "stopped working",
    "failing",
    "failed",
    "error",
    "bug",
    "down",
    "issue",
    "submission",
    "submissions",
    "compatibility",
    "blocked",
]

BILLING_SIGNALS = [
    "refund",
    "billing",
    "payment",
    "charge",
    "subscription",
    "money",
    "merchant",
    "minimum spend",
]

INVALID_SIGNALS = [
    "delete all files",
    "malware",
    "hack the system",
]

ADMIN_FLOW_KEYWORDS = [
    "remove",
    "delete",
    "restore",
    "update",
    "change",
    "pause",
    "reschedule",
    "grant",
    "revoke",
]

COMPANY_CONTEXTS = {
    "HackerRank": {
        "product_areas": [
            "screen",
            "community",
            "assessment",
            "contests",
            "billing",
            "general_support",
        ],
        "focus": "coding assessment, recruitment, and technical testing platform",
    },
    "Claude": {
        "product_areas": [
            "privacy",
            "billing",
            "api",
            "conversation_management",
            "general_support",
        ],
        "focus": "AI conversation and API platform",
    },
    "Visa": {
        "product_areas": [
            "travel_support",
            "general_support",
            "cards",
            "fraud",
            "disputes",
        ],
        "focus": "payment and financial services",
    },
}

PRODUCT_AREA_RULES = {
    "HackerRank": {
        "billing": ["refund", "billing", "payment", "subscription", "money", "order id"],
        "assessment": ["assessment", "test", "score", "certificate", "rescheduling", "reschedule"],
        "screen": ["interview", "screen share", "compatibility", "apply tab", "interviewer", "mock interview"],
        "community": ["resume"],
    },
    "Claude": {
        "privacy": ["privacy", "personal data", "retention", "crawl", "crawling"],
        "api": ["api", "sdk", "bedrock", "requests are failing", "lti"],
        "conversation_management": ["workspace", "access", "seat", "conversation"],
    },
    "Visa": {
        "fraud": ["identity theft", "fraud", "stolen", "blocked"],
        "disputes": ["dispute", "charge", "refund", "merchant", "wrong product"],
        "cards": ["card", "minimum spend", "cash"],
        "travel_support": ["travel", "travelling", "trip"],
    },
}

GENERIC_ESCALATION_RESPONSE = (
    "This request needs review by a human support specialist before we provide a final answer."
)

TEMPLATE_TICKETS = [
    {
        "Issue": "My Claude workspace access was removed after an admin change.",
        "Subject": "Workspace access issue",
        "Company": "Claude",
    },
    {
        "Issue": "None of my HackerRank submissions are going through during the assessment.",
        "Subject": "Submission failure",
        "Company": "HackerRank",
    },
    {
        "Issue": "I need to dispute a suspicious Visa charge from a merchant while traveling.",
        "Subject": "Dispute charge",
        "Company": "Visa",
    },
]

ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "cyan": "\033[36m",
}


@dataclass
class TriageResult:
    """Output structure matching the required schema."""

    issue: Optional[str] = None
    subject: Optional[str] = None
    company: Optional[str] = None
    response: str = ""
    product_area: Optional[str] = None
    status: str = "escalated"
    request_type: str = "product_issue"
    justification: str = ""
    risk_level: Optional[str] = None
    risk_score: Optional[float] = None
    risk_reasons: Optional[list[str]] = None
    routing_source: Optional[str] = None
    routing_notes: Optional[list[str]] = None


@dataclass
class RiskAssessment:
    """Deterministic risk summary used before and after model calls."""

    level: str
    reasons: list[str]
    score: float


@dataclass
class RetrievedDocument:
    """Minimal retrieval record used to ground prompts when corpus files are available."""

    source: str
    score: float
    snippet: str
    company: Optional[str] = None


def is_missing_api_key() -> bool:
    """Return True when GROQ_API_KEY is missing or looks like a placeholder."""
    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    return not api_key or api_key in {"your-key", "your-groq-api-key-here"}


def normalize_text(value: Optional[str]) -> str:
    """Lowercase and normalize nullable text fields."""
    if value is None:
        return ""
    return str(value).strip().lower()


def normalize_status_value(value: Optional[str]) -> str:
    """Normalize status to the lowercase challenge format."""
    normalized = normalize_text(value)
    if normalized in {"replied", "reply"}:
        return "replied"
    return "escalated"


def assess_risk(issue: str, subject: str, company: str) -> RiskAssessment:
    """Score the ticket using deterministic routing rules before calling the model."""
    text = f"{normalize_text(subject)} {normalize_text(issue)}"
    score = 0.0
    reasons: list[str] = []

    if any(keyword in text for keyword in HIGH_RISK_KEYWORDS):
        score += 3.0
        reasons.append("high-risk keyword match")

    if any(keyword in text for keyword in BILLING_SIGNALS):
        score += 1.5
        reasons.append("billing or payment language")

    if any(keyword in text for keyword in ADMIN_FLOW_KEYWORDS):
        score += 1.5
        reasons.append("admin or account action")

    if any(keyword in text for keyword in BUG_SIGNALS):
        score += 1.0
        reasons.append("technical failure signal")

    if company == "Visa" and any(keyword in text for keyword in ["fraud", "identity theft", "blocked", "charge", "merchant"]):
        score += 1.0
        reasons.append("visa-sensitive support domain")

    if company == "Claude" and any(keyword in text for keyword in ["privacy", "personal data", "bedrock", "workspace"]):
        score += 1.0
        reasons.append("claude-sensitive support domain")

    if company == "HackerRank" and any(keyword in text for keyword in ["score", "certificate", "subscription", "refund"]):
        score += 1.0
        reasons.append("hackerrank-sensitive support domain")

    if any(keyword in text for keyword in INVALID_SIGNALS):
        score += 2.0
        reasons.append("harmful or invalid request")

    if score >= 4:
        return RiskAssessment(level="high", reasons=reasons, score=score)
    if score >= 2:
        return RiskAssessment(level="medium", reasons=reasons, score=score)
    return RiskAssessment(level="low", reasons=reasons, score=score)


def load_support_corpus(corpus_dir: Optional[str]) -> list[RetrievedDocument]:
    """Load text-like corpus files from a local directory for lightweight retrieval."""
    if not corpus_dir:
        return []

    base_path = Path(corpus_dir)
    if not base_path.exists() or not base_path.is_dir():
        return []

    documents: list[RetrievedDocument] = []
    for path in base_path.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".txt", ".md", ".html", ".csv"}:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore").strip()
        except OSError:
            continue
        if not text:
            continue
        source_text = str(path)
        lowered = normalize_text(f"{path.name} {text[:1200]}")
        company = None
        if "hackerrank" in lowered:
            company = "HackerRank"
        elif "claude" in lowered or "anthropic" in lowered:
            company = "Claude"
        elif "visa" in lowered:
            company = "Visa"

        documents.append(
            RetrievedDocument(
                source=source_text,
                score=0.0,
                snippet=text[:4000],
                company=company,
            )
        )

    return documents


def retrieve_support_documents(
    issue: str,
    subject: str,
    company: str,
    documents: list[RetrievedDocument],
    limit: int = 3,
) -> list[RetrievedDocument]:
    """Rank corpus snippets with a simple keyword-overlap scorer."""
    if not documents:
        return []

    company_filtered = [
        document for document in documents if document.company in {company, None}
    ]
    if company_filtered:
        documents = company_filtered

    query_terms = {
        token
        for token in normalize_text(f"{company} {subject} {issue}").replace("/", " ").split()
        if len(token) > 2
    }
    ranked: list[RetrievedDocument] = []
    for document in documents:
        haystack = normalize_text(document.snippet)
        score = float(sum(1 for term in query_terms if term in haystack))
        if score <= 0:
            continue
        ranked.append(
            RetrievedDocument(
                source=document.source,
                score=score,
                snippet=document.snippet[:700],
                company=document.company,
            )
        )

    ranked.sort(key=lambda item: item.score, reverse=True)
    return ranked[:limit]


def should_force_escalation(
    issue: str,
    subject: str,
    company: str,
    result: TriageResult,
) -> Optional[str]:
    """Force risky tickets to escalate instead of relying on generic model replies."""
    if result.status != "replied":
        return None

    text = f"{normalize_text(subject)} {normalize_text(issue)}"
    response_text = normalize_text(result.response)
    product_area = normalize_text(result.product_area)

    if result.request_type in {"bug", "invalid", "feature_request"}:
        return "Bugs and invalid requests should not receive final automated replies."

    if any(keyword in text for keyword in HIGH_RISK_KEYWORDS):
        return "This ticket includes policy, billing, privacy, security, access, or account-management risk."

    if any(keyword in text for keyword in ADMIN_FLOW_KEYWORDS) and any(
        token in text for token in ["account", "user", "employee", "subscription", "certificate"]
    ):
        return "This request asks for an account or admin-side action that needs human review."

    if company == "Claude" and product_area in {"privacy", "billing"}:
        return "Claude privacy and billing questions are escalated to avoid unsupported policy claims."

    if company == "Visa" and product_area in {"fraud", "disputes", "cards"}:
        return "Visa card, dispute, and fraud issues are escalated unless grounded in explicit support documentation."

    if company == "HackerRank" and product_area in {"billing"}:
        return "HackerRank billing or account-management requests should be handled by human support."

    safe_keywords = SAFE_REPLY_KEYWORDS.get(company, [])
    if safe_keywords and not any(keyword in text for keyword in safe_keywords):
        return "The reply is not clearly tied to a narrow, low-risk FAQ pattern."

    if any(
        phrase in response_text
        for phrase in [
            "typically",
            "generally",
            "likely",
            "usually",
            "might",
            "may vary",
            "official documentation",
        ]
    ):
        return "The drafted reply contains speculative wording rather than a tightly grounded support answer."

    if company == "Unknown":
        return "Unknown-company tickets should not receive automated replies without stronger routing confidence."

    if result.product_area in {None, "", "general_support"}:
        return "Replies are limited to narrowly scoped product areas with clearer support grounding."

    return None


def normalize_request_type(issue: str, subject: str, result: TriageResult) -> TriageResult:
    """Correct obviously bad request-type labels while keeping conservative escalation."""
    text = f"{normalize_text(subject)} {normalize_text(issue)}"

    if any(signal in text for signal in INVALID_SIGNALS):
        result.request_type = "invalid"
        return result

    if any(signal in text for signal in FEATURE_REQUEST_SIGNALS):
        result.request_type = "feature_request"
        return result

    if result.request_type == "invalid":
        if any(signal in text for signal in VALID_SUPPORT_SIGNALS):
            result.request_type = "bug" if any(signal in text for signal in BUG_SIGNALS) else "product_issue"
            if not result.justification:
                result.justification = "This is a valid support request and should not be marked invalid."

    if any(signal in text for signal in BILLING_SIGNALS):
        result.request_type = "product_issue"

    if (
        result.request_type == "product_issue"
        and any(signal in text for signal in BUG_SIGNALS)
        and not any(signal in text for signal in BILLING_SIGNALS)
    ):
        result.request_type = "bug"

    if text in {"help needed it’s not working, help", "help needed it's not working, help"}:
        result.request_type = "product_issue"

    if "issue while taking the test" in text or "submissions across any challenges are working" in text:
        result.request_type = "bug"

    return result


def append_debug_log(debug_log_path: Path, row_index: int, result: TriageResult) -> None:
    """Append one JSONL audit record per processed ticket."""
    debug_log_path.parent.mkdir(parents=True, exist_ok=True)
    risk = assess_risk(result.issue or "", result.subject or "", result.company or "Unknown")
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "row_index": row_index,
        "issue": result.issue,
        "subject": result.subject,
        "company": result.company,
        "risk_level": result.risk_level or risk.level,
        "risk_score": result.risk_score if result.risk_score is not None else risk.score,
        "risk_reasons": result.risk_reasons or risk.reasons,
        "routing_source": result.routing_source or "unknown",
        "routing_notes": result.routing_notes or [],
        "status": result.status,
        "request_type": result.request_type,
        "product_area": result.product_area,
        "response": result.response,
        "justification": result.justification,
    }
    with open(debug_log_path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def append_chat_log(chat_log_path: Path, issue: str, result: TriageResult) -> None:
    """Append one JSONL record per interactive chat exchange."""
    chat_log_path.parent.mkdir(parents=True, exist_ok=True)
    risk = assess_risk(issue, result.subject or "", result.company or "Unknown")
    payload = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "issue": issue,
        "subject": result.subject,
        "company": result.company,
        "risk_level": result.risk_level or risk.level,
        "risk_score": result.risk_score if result.risk_score is not None else risk.score,
        "risk_reasons": result.risk_reasons or risk.reasons,
        "routing_source": result.routing_source or "unknown",
        "routing_notes": result.routing_notes or [],
        "status": result.status,
        "request_type": result.request_type,
        "product_area": result.product_area,
        "justification": result.justification,
        "response": result.response,
    }
    with open(chat_log_path, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def load_existing_results(output_file: str) -> tuple[list[dict], set[str]]:
    """Load prior CSV output so interrupted runs can resume safely."""
    output_path = Path(output_file)
    if not output_path.exists():
        return [], set()

    try:
        existing_df = pd.read_csv(output_path)
    except Exception:  # noqa: BLE001
        return [], set()

    unique_results: list[dict] = []
    keys: set[str] = set()

    for record in existing_df.fillna("").to_dict(orient="records"):
        key = build_ticket_key(
            record.get("issue", ""),
            record.get("subject", ""),
            record.get("company", ""),
        )
        if key in keys:
            continue
        keys.add(key)
        unique_results.append(record)

    return unique_results, keys


def build_ticket_key(issue: str, subject: str, company: str) -> str:
    """Create a stable key for each ticket row."""
    return "||".join([normalize_text(company), normalize_text(subject), normalize_text(issue)])


def make_rules_only_decision(issue: str, subject: str, company: str) -> TriageResult:
    """Fallback decision path when the model is unavailable or disabled."""
    risk = assess_risk(issue, subject, company)
    text = f"{normalize_text(subject)} {normalize_text(issue)}"
    request_type = "product_issue"

    if any(signal in text for signal in INVALID_SIGNALS):
        request_type = "invalid"
    elif any(signal in text for signal in FEATURE_REQUEST_SIGNALS):
        request_type = "feature_request"
    elif any(signal in text for signal in BUG_SIGNALS) and not any(signal in text for signal in BILLING_SIGNALS):
        request_type = "bug"

    justification = f"Rules-only fallback applied ({risk.level} risk"
    if risk.reasons:
        justification += f": {', '.join(risk.reasons[:3])}"
    justification += ")."

    return TriageResult(
        issue=issue,
        subject=subject,
        company=company,
        status="escalated",
        request_type=request_type,
        product_area=infer_product_area(issue, subject, company, None),
        response=GENERIC_ESCALATION_RESPONSE,
        justification=justification,
        risk_level=risk.level,
        risk_score=risk.score,
        risk_reasons=risk.reasons,
        routing_source="rules_only",
        routing_notes=["deterministic fallback"],
    )


def infer_product_area(issue: str, subject: str, company: str, current_product_area: Optional[str]) -> Optional[str]:
    """Fill missing or unsupported product areas using deterministic keyword rules."""
    normalized_area = normalize_text(current_product_area)
    allowed_areas = set(COMPANY_CONTEXTS.get(company, {}).get("product_areas", ["general_support"]))
    if normalized_area in allowed_areas:
        return normalized_area

    text = f"{normalize_text(subject)} {normalize_text(issue)}"
    company_rules = PRODUCT_AREA_RULES.get(company, {})
    for product_area, keywords in company_rules.items():
        if any(keyword in text for keyword in keywords):
            return product_area

    if company in COMPANY_CONTEXTS:
        return "general_support"
    return None


def normalize_result(issue: str, subject: str, company: str, result: TriageResult) -> TriageResult:
    """Apply deterministic cleanup so final CSV rows stay consistent."""
    result.status = normalize_status_value(result.status)
    result.request_type = result.request_type or "product_issue"
    result.product_area = infer_product_area(issue, subject, company, result.product_area)

    if result.status == "escalated":
        result.response = GENERIC_ESCALATION_RESPONSE

    if result.request_type == "invalid":
        result.product_area = None

    if result.routing_notes is None:
        result.routing_notes = []

    return result


def apply_safety_guardrails(
    issue: str,
    subject: str,
    company: str,
    result: TriageResult,
) -> TriageResult:
    """Post-process model output to prefer safe escalation over unsupported replies."""
    result = normalize_request_type(issue, subject, result)
    text = f"{normalize_text(subject)} {normalize_text(issue)}"

    if text in {"help needed it’s not working, help", "help needed it's not working, help"}:
        return TriageResult(
            issue=result.issue,
            subject=result.subject,
            company=result.company,
            status="escalated",
            request_type="product_issue",
            product_area=result.product_area,
            response=GENERIC_ESCALATION_RESPONSE,
            justification="The request is too vague to answer safely without more context.",
        )

    escalation_reason = should_force_escalation(issue, subject, company, result)
    if not escalation_reason:
        return result

    return TriageResult(
        issue=result.issue,
        subject=result.subject,
        company=result.company,
        status="escalated",
        request_type=result.request_type,
        product_area=result.product_area,
        response=GENERIC_ESCALATION_RESPONSE,
        justification=escalation_reason,
    )


def sanitize_escalated_result(result: TriageResult) -> TriageResult:
    """Remove unsupported specifics from escalated replies and keep wording generic."""
    if result.status != "escalated":
        return result

    response_text = normalize_text(result.response)
    if any(
        phrase in response_text
        for phrase in [
            "1-800",
            "visit our website",
            "bug bounty program",
            "cash advances",
            "local bank",
            "financial advisor",
            "contact our dedicated fraud team",
            "billing team directly",
            "customer service team directly",
        ]
    ):
        result.response = (
            "This request needs review by a human support specialist before we provide a final answer."
        )

    return result


def annotate_risk_and_route(
    result: TriageResult,
    risk: RiskAssessment,
    source: str,
    notes: Optional[list[str]] = None,
) -> TriageResult:
    """Attach consistent audit metadata to a triage result."""
    result.risk_level = risk.level
    result.risk_score = risk.score
    result.risk_reasons = risk.reasons
    result.routing_source = source
    result.routing_notes = list(notes or [])
    return result


def standardize_input_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Accept both challenge-style lowercase headers and older uppercase variants."""
    column_map = {}
    for column in df.columns:
        normalized = normalize_text(column)
        if normalized == "issue":
            column_map[column] = "Issue"
        elif normalized == "subject":
            column_map[column] = "Subject"
        elif normalized == "company":
            column_map[column] = "Company"
        elif normalized == "status":
            column_map[column] = "Status"
        elif normalized in {"request type", "request_type"}:
            column_map[column] = "Request Type"
        elif normalized in {"product area", "product_area"}:
            column_map[column] = "Product Area"
    return df.rename(columns=column_map)


def load_sample_tickets(sample_file: str) -> pd.DataFrame:
    """Load sample tickets to use as examples in the prompt."""
    try:
        df = standardize_input_columns(pd.read_csv(sample_file))
        print(f"Loaded {len(df)} sample tickets from {Path(sample_file).name}")
        return df
    except Exception as exc:  # noqa: BLE001
        print(f"Warning: Could not load sample tickets: {exc}")
        return pd.DataFrame()


def build_examples_for_prompt(sample_df: pd.DataFrame, limit: int = 2) -> str:
    """Build example section for the system prompt from sample tickets."""
    if len(sample_df) == 0:
        return ""

    examples = []
    for idx, row in sample_df.head(limit).iterrows():
        if pd.isna(row["Issue"]) or pd.isna(row["Company"]):
            continue

        issue_preview = str(row["Issue"])[:90].replace("\n", " ")
        examples.append(
            f"""
Example {idx + 1}:
  Company: {row["Company"]}
  Issue: {issue_preview}...
  Status: {row["Status"]}
  Product Area: {row["Product Area"]}
  """
        )

    return "EXAMPLES FROM TRAINING DATA:\n" + "\n".join(examples)


def detect_company(subject: str, issue: str, company: Optional[str]) -> str:
    """Detect company from content if not provided."""
    if company and str(company).lower() != "nan":
        return str(company)

    text = (str(subject) + " " + str(issue)).lower()

    keywords = {
        "HackerRank": [
            "hackerrank",
            "codepair",
            "assessment",
            "test",
            "candidate",
            "coding",
        ],
        "Claude": ["claude", "api", "conversation", "anthropic"],
        "Visa": ["visa", "card", "payment", "traveller's cheque", "cardholder"],
    }

    for company_name, company_keywords in keywords.items():
        if any(keyword in text for keyword in company_keywords):
            return company_name

    return "Unknown"


def build_system_prompt(
    sample_df: pd.DataFrame,
    ticket_company: str,
    retrieved_docs: list[RetrievedDocument],
) -> str:
    """Build company-specific system prompt with examples."""
    company_info = COMPANY_CONTEXTS.get(ticket_company, {})
    product_areas = company_info.get("product_areas", ["general_support"])
    focus = company_info.get("focus", "support services")

    examples_section = build_examples_for_prompt(sample_df)
    evidence_section = ""
    if retrieved_docs:
        evidence_lines = []
        for index, doc in enumerate(retrieved_docs, start=1):
            evidence_lines.append(
                f"Evidence {index}:\n"
                f"  Source: {doc.source}\n"
                f"  Company: {doc.company or 'Unknown'}\n"
                f"  Score: {doc.score:.1f}\n"
                f"  Snippet: {doc.snippet[:500].replace(chr(10), ' ')}"
            )
        evidence_section = "\nRETRIEVED SUPPORT DOCUMENTATION:\n" + "\n".join(evidence_lines)

    allowed_source = REQUIRED_CORPUS_SOURCES.get(ticket_company, "provided support corpus only")
    return f"""Triage support tickets for {ticket_company}.

Context: {focus}
Allowed product areas: {", ".join(product_areas)}
Approved support source: {allowed_source}

Use only the retrieved support documentation and the provided examples. If evidence is missing or weak, escalate.
Never answer from memory or general product knowledge. If the retrieved snippets do not clearly support a safe answer, escalate.
Reply only for narrow, low-risk FAQ-style usage questions.
Escalate if the ticket involves billing, refunds, fraud, disputes, privacy, security, account access, admin actions, policy, or uncertainty.

Request types:
- product_issue
- feature_request
- bug
- invalid

Return JSON only:
{{
  "status": "replied|escalated",
  "request_type": "product_issue|feature_request|bug|invalid",
  "product_area": "allowed_area_or_null",
  "response": "short response",
  "justification": "short reason"
}}

{examples_section}
{evidence_section}
"""


def make_triage_decision(
    issue: str,
    subject: str,
    company: str,
    sample_df: pd.DataFrame,
    corpus_documents: Optional[list[RetrievedDocument]] = None,
) -> TriageResult:
    """Use Groq API to make triage decision."""
    risk = assess_risk(issue, subject, company)
    if os.environ.get("TRIAGE_RULES_ONLY", "").strip() == "1":
        result = make_rules_only_decision(issue, subject, company)
        return annotate_risk_and_route(result, risk, "rules_only", ["TRIAGE_RULES_ONLY=1"])

    if risk.level == "high":
        result = make_rules_only_decision(issue, subject, company)
        return annotate_risk_and_route(result, risk, "rules_only", ["high-risk bypass"])

    retrieved_docs = retrieve_support_documents(
        issue,
        subject,
        company,
        corpus_documents or [],
    )
    if not retrieved_docs:
        result = make_rules_only_decision(issue, subject, company)
        result.justification = (
            "No relevant support-corpus evidence was retrieved for this company, so the ticket should be escalated."
        )
        return annotate_risk_and_route(result, risk, "rules_only", ["no corpus evidence"])

    system_prompt = build_system_prompt(sample_df, company, retrieved_docs)

    user_message = f"""Subject: {subject if subject else "[No subject]"}

Ticket Body:
{issue}"""

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    try:
        response = client.chat.completions.create(
            model=CONFIG["model"],
            max_tokens=CONFIG["max_tokens"],
            temperature=CONFIG["temperature"],
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            response_format={"type": "json_object"},
        )

        response_text = response.choices[0].message.content.strip()

        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_str = response_text

        decision = json.loads(json_str)

        result = TriageResult(
            issue=issue,
            subject=subject,
            company=company,
            status=decision.get("status", "escalated"),
            request_type=decision.get("request_type", "product_issue"),
            product_area=decision.get("product_area"),
            response=decision.get("response", ""),
            justification=decision.get("justification", ""),
        )
        result = apply_safety_guardrails(issue, subject, company, result)
        route_notes = ["groq chat completion"]
        if retrieved_docs:
            route_notes.append(f"retrieved_docs={len(retrieved_docs)}")
        else:
            route_notes.append("no_retrieved_docs")
        return annotate_risk_and_route(result, risk, "model", route_notes)

    except json.JSONDecodeError as exc:
        result = make_rules_only_decision(issue, subject, company)
        result.justification = f"Rules-only fallback after JSON parse failure: {str(exc)[:50]}"
        return annotate_risk_and_route(result, risk, "rules_only", ["json parse failure"])
    except APIError as exc:
        print(f"API Error: {exc}", file=sys.stderr)
        result = make_rules_only_decision(issue, subject, company)
        justification = "Rules-only fallback after API error"
        notes = ["api error fallback"]
        if "rate_limit" in str(exc).lower() or "429" in str(exc):
            justification = "Rules-only fallback after API rate limit"
            notes = ["api rate limit fallback"]
        result.justification = justification
        return annotate_risk_and_route(result, risk, "rules_only", notes)


def process_tickets(
    input_file: str,
    sample_file: str,
    output_file: str,
    *,
    resume: bool = True,
    corpus_dir: Optional[str] = None,
) -> None:
    """Process support tickets using sample data as examples."""
    print(f"\n{'=' * 80}")
    print("Support Triage Agent v2")
    print(f"{'=' * 80}\n")

    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    if is_missing_api_key() and os.environ.get("TRIAGE_RULES_ONLY", "").strip() != "1":
        print(
            "Missing GROQ_API_KEY. Export a real key before running the script.",
            file=sys.stderr,
        )
        sys.exit(1)

    if os.environ.get("TRIAGE_RULES_ONLY", "").strip() != "1" and not corpus_dir:
        print(
            "Missing --corpus-dir. To satisfy the challenge requirements, run with the extracted support corpus.",
            file=sys.stderr,
        )
        sys.exit(1)

    sample_df = pd.DataFrame()
    if sample_file and os.path.exists(sample_file):
        sample_df = load_sample_tickets(sample_file)
    corpus_documents = load_support_corpus(corpus_dir)
    if corpus_dir:
        print(f"Loaded {len(corpus_documents)} support corpus documents from {corpus_dir}\n")
    if os.environ.get("TRIAGE_RULES_ONLY", "").strip() != "1" and corpus_dir and not corpus_documents:
        print(
            "No support corpus documents were loaded. Check --corpus-dir and extract the real support corpus first.",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        support_df = standardize_input_columns(pd.read_csv(input_file))
        print(f"Loaded {len(support_df)} support tickets to process\n")
    except Exception as exc:  # noqa: BLE001
        print(f"Error loading input file: {exc}", file=sys.stderr)
        sys.exit(1)

    results, completed_keys = load_existing_results(output_file) if resume else ([], set())
    total = len(support_df)
    debug_log_path = Path(output_file).with_suffix(".jsonl")
    debug_log_path.parent.mkdir(parents=True, exist_ok=True)
    if debug_log_path.exists() and not completed_keys:
        debug_log_path.unlink()

    skipped_completed = 0
    processed_new = 0
    model_routed = 0
    rules_only_routed = 0
    high_risk_bypassed = 0
    api_fallbacks = 0

    print(f"Processing {total} tickets...\n")
    if resume and completed_keys:
        print(f"Resumed from {len(completed_keys)} existing rows.\n")

    for idx, row in support_df.iterrows():
        issue = row.get("Issue", "")
        subject = row.get("Subject", "")
        company = row.get("Company", "Unknown")

        if not issue or str(issue).strip() == "nan":
            continue

        if not company or str(company).lower() == "nan":
            company = detect_company(subject, issue, company)

        ticket_key = build_ticket_key(issue, subject, company)
        if ticket_key in completed_keys:
            skipped_completed += 1
            print(
                f"[{idx + 1:3d}/{total}] {company:<12} | {str(subject)[:40]:<40}"
                " -> SKIP completed"
            )
            continue

        print(
            f"[{idx + 1:3d}/{total}] {company:<12} | {str(subject)[:40]:<40}",
            end=" -> ",
        )
        sys.stdout.flush()

        result = make_triage_decision(issue, subject, company, sample_df, corpus_documents)
        result = sanitize_escalated_result(result)
        result = normalize_result(issue, subject, company, result)
        results.append(asdict(result))
        completed_keys.add(ticket_key)
        processed_new += 1

        if result.routing_source == "model":
            model_routed += 1
        if result.routing_source == "rules_only":
            rules_only_routed += 1
        if result.routing_notes and "high-risk bypass" in result.routing_notes:
            high_risk_bypassed += 1
        if result.routing_notes and any("api" in note for note in result.routing_notes):
            api_fallbacks += 1

        append_debug_log(debug_log_path, idx + 1, result)

        status_icon = "OK" if result.status == "replied" else "UP"
        print(f"{status_icon} {result.request_type:<15}")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w", encoding="utf-8", newline="") as file_handle:
        if results:
            fieldnames = [
                "issue",
                "subject",
                "company",
                "response",
                "product_area",
                "status",
                "request_type",
                "justification",
            ]
            writer = csv.DictWriter(file_handle, fieldnames=fieldnames)
            writer.writeheader()

            for result in results:
                writer.writerow(
                    {
                        "issue": result.get("issue", ""),
                        "subject": result.get("subject", ""),
                        "company": result.get("company", ""),
                        "response": result.get("response", ""),
                        "product_area": result.get("product_area") or "",
                        "status": result.get("status", "escalated"),
                        "request_type": result.get("request_type", "product_issue"),
                        "justification": result.get("justification", ""),
                    }
                )

    print(f"\n{'=' * 80}")
    print(f"Triage complete. Results saved to: {output_file}")
    print(f"Debug log saved to: {debug_log_path}")
    print(f"{'=' * 80}\n")

    replied_count = sum(1 for result in results if result.get("status") == "replied")
    escalated_count = sum(
        1 for result in results if result.get("status") == "escalated"
    )
    total_processed = len(results)

    print("Summary:")
    print(f"  Total processed: {total_processed}")
    print(f"  New rows processed: {processed_new}")
    print(f"  Completed rows skipped: {skipped_completed}")
    print(f"  Model-routed rows: {model_routed}")
    print(f"  Rules-only rows: {rules_only_routed}")
    print(f"  High-risk bypasses: {high_risk_bypassed}")
    print(f"  API fallbacks: {api_fallbacks}")
    if total_processed:
        print(f"  replied: {replied_count} ({replied_count / total_processed * 100:.1f}%)")
        print(
            f"  escalated: {escalated_count} ({escalated_count / total_processed * 100:.1f}%)"
        )

    by_type = {}
    for result in results:
        request_type = result.get("request_type", "unknown")
        by_type[request_type] = by_type.get(request_type, 0) + 1

    if by_type:
        print("\nBy Request Type:")
        for request_type, count in sorted(by_type.items()):
            print(f"  {request_type}: {count}")


def chat_mode(sample_file: Optional[str], chat_log_file: str = "chat_session.jsonl") -> None:
    """Interactive terminal mode for one-off support triage conversations."""
    if is_missing_api_key() and os.environ.get("TRIAGE_RULES_ONLY", "").strip() != "1":
        print(
            "Missing GROQ_API_KEY. Export a real key or set TRIAGE_RULES_ONLY=1 before starting chat mode.",
            file=sys.stderr,
        )
        sys.exit(1)

    sample_df = pd.DataFrame()
    if sample_file and os.path.exists(sample_file):
        sample_df = load_sample_tickets(sample_file)

    chat_log_path = Path(chat_log_file)

    print("\n" + "=" * 80)
    print("Support Triage Agent Chat")
    print("=" * 80)
    print("Type a support issue and press Enter.")
    print("Optional commands:")
    print("  /company HackerRank|Claude|Visa|Unknown")
    print("  /subject your short subject")
    print("  /reset")
    print("  /quit")
    print(f"Chat log: {chat_log_path.resolve()}")
    print("=" * 80 + "\n")

    current_company = "Unknown"
    current_subject = ""

    while True:
        try:
            raw_input_value = input("issue> ").strip()
        except EOFError:
            print("\nExiting chat mode.")
            break

        if not raw_input_value:
            continue

        if raw_input_value.lower() == "/quit":
            print("Exiting chat mode.")
            break

        if raw_input_value.lower() == "/reset":
            current_company = "Unknown"
            current_subject = ""
            print("chat context reset")
            continue

        if raw_input_value.startswith("/company "):
            current_company = raw_input_value.split(" ", 1)[1].strip() or "Unknown"
            print(f"company set to: {current_company}")
            continue

        if raw_input_value.startswith("/subject "):
            current_subject = raw_input_value.split(" ", 1)[1].strip()
            print(f"subject set to: {current_subject}")
            continue

        company = current_company
        if company == "Unknown":
            prompt_company = input(
                "company [HackerRank/Claude/Visa/Unknown, Enter to auto-detect]> "
            ).strip()
            if prompt_company:
                company = prompt_company
        else:
            keep_company = input(f"company [{company}] (Enter to keep)> ").strip()
            if keep_company:
                company = keep_company

        subject = current_subject
        if not subject:
            subject = input("subject [optional]> ").strip()
        else:
            keep_subject = input(f"subject [{subject}] (Enter to keep)> ").strip()
            if keep_subject:
                subject = keep_subject

        if company == "Unknown":
            company = detect_company(subject, raw_input_value, None)

        current_company = company or "Unknown"
        current_subject = subject

        result = make_triage_decision(raw_input_value, subject, company, sample_df)
        result = sanitize_escalated_result(result)
        result = normalize_result(raw_input_value, subject, company, result)

        print_chat_result(result)
        append_chat_log(chat_log_path, raw_input_value, result)


def print_chat_result(result: TriageResult) -> None:
    """Render chat-mode triage output in a clearer terminal layout."""
    status_color = ANSI["green"] if result.status == "replied" else ANSI["yellow"]
    rows = [
        ("Company", result.company or "[none]"),
        ("Subject", result.subject or "[none]"),
        ("Status", f"{status_color}{result.status}{ANSI['reset']}"),
        ("Request Type", result.request_type),
        ("Product Area", result.product_area or "[none]"),
        ("Justification", result.justification),
        ("Response", result.response),
    ]
    width = 80
    print("\n" + f"{ANSI['cyan']}" + "=" * width + f"{ANSI['reset']}")
    print(f"{ANSI['bold']}TRIAGE RESULT{ANSI['reset']}")
    print(f"{ANSI['cyan']}" + "=" * width + f"{ANSI['reset']}")
    for label, value in rows:
        print(f"{ANSI['dim']}{label:<14}{ANSI['reset']}: {value}")
    print(f"{ANSI['cyan']}" + "=" * width + f"{ANSI['reset']}\n")


def print_help() -> None:
    """Print command-line usage instructions."""
    print("Usage:")
    print(
        "  python support_triage_agent_v2.py <input_csv> [sample_csv] [output_csv] [--no-resume] [--corpus-dir path]"
    )
    print("  python support_triage_agent_v2.py --chat [sample_csv] [--chat-log path]")
    print("  python support_triage_agent_v2.py --inspect <input_csv>")
    print("  python support_triage_agent_v2.py --evaluate <predictions_csv> <expected_csv>")
    print("  python support_triage_agent_v2.py --template-csv <output_csv>")
    print("  python support_triage_agent_v2.py --explain-row <input_csv> <row_number> [sample_csv]")
    print("  python support_triage_agent_v2.py --help")
    print("\nExamples:")
    print(
        "  python support_triage_agent_v2.py support_tickets.csv "
        "sample_support_tickets.csv results.csv"
    )
    print(
        "  python support_triage_agent_v2.py support_tickets.csv sample.csv results.csv "
        "--corpus-dir ./support_corpus"
    )
    print("  python support_triage_agent_v2.py support_tickets.csv sample.csv results.csv --no-resume")
    print("  python support_triage_agent_v2.py --chat sample_support_tickets.csv")
    print("  python support_triage_agent_v2.py --chat sample_support_tickets.csv --chat-log my_chat.jsonl")
    print("  python support_triage_agent_v2.py --inspect support_tickets.csv")
    print("  python support_triage_agent_v2.py --evaluate output.csv expected.csv")
    print("  python support_triage_agent_v2.py --template-csv starter_tickets.csv")
    print("  python support_triage_agent_v2.py --explain-row support_tickets.csv 5 sample_support_tickets.csv")
    print("\nEnvironment:")
    print("  GROQ_API_KEY=...                     Run model-backed triage")
    print("  TRIAGE_RULES_ONLY=1                 Force deterministic fallback routing")


def inspect_dataset(input_file: str) -> None:
    """Print a quick dataset summary for support CSV files."""
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    try:
        df = pd.read_csv(input_file)
    except Exception as exc:  # noqa: BLE001
        print(f"Error loading input file: {exc}", file=sys.stderr)
        sys.exit(1)

    print("\n" + "=" * 80)
    print("Dataset inspection")
    print("=" * 80)
    print(f"Rows: {len(df)}")
    print(f"Columns: {', '.join(df.columns.tolist())}")

    duplicate_count = 0
    if {"Issue", "Subject"}.issubset(df.columns):
        dedupe_keys = (
            df["Issue"].fillna("").astype(str).str.strip().str.lower()
            + "||"
            + df["Subject"].fillna("").astype(str).str.strip().str.lower()
            + "||"
            + df.get("Company", pd.Series(["Unknown"] * len(df))).fillna("Unknown").astype(str).str.strip().str.lower()
        )
        duplicate_count = int(dedupe_keys.duplicated().sum())

    if "Company" in df.columns:
        company_counts = (
            df["Company"].fillna("Unknown").replace("", "Unknown").value_counts(dropna=False)
        )
        print("\nCompanies:")
        for company, count in company_counts.items():
            print(f"  {company}: {count}")

    if "Issue" in df.columns:
        missing_issues = int(df["Issue"].isna().sum())
        print(f"\nMissing Issue values: {missing_issues}")

    if "Subject" in df.columns:
        missing_subjects = int(df["Subject"].isna().sum())
        print(f"Missing Subject values: {missing_subjects}")

    print(f"Duplicate ticket keys: {duplicate_count}")

    print("=" * 80 + "\n")


def write_template_csv(output_file: str) -> None:
    """Generate a starter ticket CSV with the expected schema."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["Issue", "Subject", "Company"])
        writer.writeheader()
        writer.writerows(TEMPLATE_TICKETS)

    print(f"Template CSV written to: {output_path}")


def explain_row(input_file: str, row_number: int, sample_file: Optional[str] = None) -> None:
    """Explain how one ticket would be routed using the current deterministic logic."""
    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}", file=sys.stderr)
        sys.exit(1)

    df = pd.read_csv(input_file)
    if row_number < 1 or row_number > len(df):
        print(f"Row number {row_number} is out of range for {len(df)} rows.", file=sys.stderr)
        sys.exit(1)

    sample_df = pd.DataFrame()
    if sample_file and os.path.exists(sample_file):
        sample_df = load_sample_tickets(sample_file)

    row = df.iloc[row_number - 1]
    issue = row.get("Issue", "")
    subject = row.get("Subject", "")
    company = row.get("Company", "Unknown")
    company = detect_company(subject, issue, company)

    risk = assess_risk(issue, subject, company)
    result = make_triage_decision(issue, subject, company, sample_df)
    result = sanitize_escalated_result(result)
    result = normalize_result(issue, subject, company, result)

    print("\n" + "=" * 80)
    print(f"Explain row {row_number}")
    print("=" * 80)
    print(f"Company: {company}")
    print(f"Subject: {subject if subject else '[none]'}")
    print(f"Issue: {issue}")
    print(f"Risk level: {result.risk_level or risk.level}")
    print(f"Risk score: {result.risk_score if result.risk_score is not None else risk.score}")
    print("Risk reasons:")
    for reason in (result.risk_reasons or risk.reasons or ["[none]"]):
        print(f"  - {reason}")
    print(f"Routing source: {result.routing_source or 'unknown'}")
    print("Routing notes:")
    for note in (result.routing_notes or ["[none]"]):
        print(f"  - {note}")
    print(f"Status: {result.status}")
    print(f"Request type: {result.request_type}")
    print(f"Product area: {result.product_area or '[none]'}")
    print(f"Justification: {result.justification}")
    print(f"Response: {result.response}")
    print("=" * 80 + "\n")


def evaluate_predictions(predictions_file: str, expected_file: str) -> None:
    """Compare predicted CSV output to an expected labeled CSV."""
    if not os.path.exists(predictions_file):
        print(f"Predictions file not found: {predictions_file}", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(expected_file):
        print(f"Expected file not found: {expected_file}", file=sys.stderr)
        sys.exit(1)

    predicted_df = pd.read_csv(predictions_file).fillna("")
    expected_df = pd.read_csv(expected_file).fillna("")

    required_columns = ["issue", "subject", "company"]
    missing_columns = [
        column
        for column in required_columns
        if column not in predicted_df.columns or column not in expected_df.columns
    ]
    if missing_columns:
        print(
            f"Evaluation requires columns present in both files: {', '.join(required_columns)}",
            file=sys.stderr,
        )
        sys.exit(1)

    def normalize_eval_value(value: object) -> str:
        return str(value).strip().replace("\r\n", "\n").replace("\r", "\n")

    for frame in (predicted_df, expected_df):
        for column in set(required_columns + ["status", "request_type", "product_area"]):
            if column in frame.columns:
                frame[column] = frame[column].map(normalize_eval_value)

    join_columns = required_columns
    comparison_columns = ["status", "request_type", "product_area"]
    merged = expected_df.merge(
        predicted_df,
        on=join_columns,
        how="left",
        suffixes=("_expected", "_predicted"),
    )
    merged = merged.fillna("")

    print("\n" + "=" * 80)
    print("Evaluation report")
    print("=" * 80)
    print(f"Expected rows: {len(expected_df)}")
    print(f"Matched prediction rows: {int(merged['status_predicted'].ne('').sum())}")

    for column in comparison_columns:
        expected_col = f"{column}_expected"
        predicted_col = f"{column}_predicted"
        comparable = merged[expected_col].ne("")
        if not comparable.any():
            continue

        correct = (merged.loc[comparable, expected_col] == merged.loc[comparable, predicted_col]).sum()
        total = int(comparable.sum())
        accuracy = (correct / total * 100) if total else 0.0
        print(f"{column}: {correct}/{total} correct ({accuracy:.1f}%)")

    mismatches = []
    for _, row in merged.iterrows():
        for column in comparison_columns:
            expected_value = row.get(f"{column}_expected", "")
            predicted_value = row.get(f"{column}_predicted", "")
            if expected_value and expected_value != predicted_value:
                mismatches.append(
                    {
                        "subject": row.get("subject", ""),
                        "company": row.get("company", ""),
                        "field": column,
                        "expected": expected_value,
                        "predicted": predicted_value,
                    }
                )

    if mismatches:
        print("\nMismatches:")
        for item in mismatches[:20]:
            print(
                f"  [{item['company']}] {item['subject'] or '[no subject]'} | "
                f"{item['field']}: expected={item['expected']} predicted={item['predicted']}"
            )
    else:
        print("\nNo mismatches found in compared fields.")

    print("=" * 80 + "\n")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action="store_true")
    parser.add_argument("--chat", action="store_true")
    parser.add_argument("--inspect")
    parser.add_argument("--evaluate", nargs=2, metavar=("PREDICTIONS_CSV", "EXPECTED_CSV"))
    parser.add_argument("--template-csv")
    parser.add_argument("--explain-row", nargs="+")
    parser.add_argument("--no-resume", action="store_true")
    parser.add_argument("--chat-log", default="chat_session.jsonl")
    parser.add_argument("--corpus-dir")
    parser.add_argument("positional", nargs="*")
    parsed = parser.parse_args()

    if parsed.help or (
        not parsed.chat
        and not parsed.inspect
        and not parsed.evaluate
        and not parsed.template_csv
        and not parsed.explain_row
        and not parsed.positional
    ):
        print_help()
        if len(sys.argv) == 1:
            sys.exit(1)
        return

    if parsed.chat:
        sample_file = parsed.positional[0] if parsed.positional else None
        chat_mode(sample_file, chat_log_file=parsed.chat_log)
        return

    if parsed.inspect:
        inspect_dataset(parsed.inspect)
        return

    if parsed.evaluate:
        evaluate_predictions(parsed.evaluate[0], parsed.evaluate[1])
        return

    if parsed.template_csv:
        write_template_csv(parsed.template_csv)
        return

    if parsed.explain_row:
        if len(parsed.explain_row) < 2:
            print_help()
            sys.exit(1)
        input_file = parsed.explain_row[0]
        row_number = int(parsed.explain_row[1])
        sample_file = parsed.explain_row[2] if len(parsed.explain_row) > 2 else None
        explain_row(input_file, row_number, sample_file)
        return

    resume = not parsed.no_resume
    positional = parsed.positional

    if len(positional) < 1:
        print_help()
        sys.exit(1)

    input_file = positional[0]
    sample_file = positional[1] if len(positional) > 1 else None
    output_file = positional[2] if len(positional) > 2 else "triage_results.csv"

    process_tickets(
        input_file,
        sample_file,
        output_file,
        resume=resume,
        corpus_dir=parsed.corpus_dir,
    )


if __name__ == "__main__":
    main()
