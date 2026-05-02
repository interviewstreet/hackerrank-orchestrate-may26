"""
Gatekeeper — deterministic input validation and normalization.
No LLM calls. Runs before any downstream agent.
"""

import time

MAX_COMBINED_CHARS = 2000
MIN_ISSUE_CHARS = 200
VALID_COMPANIES = {"HackerRank", "Claude", "Visa", "None"}
_COMPANY_NORMALISE = {c.lower(): c for c in VALID_COMPANIES}


class GatekeeperResult:
    __slots__ = ("request_id", "issue", "subject", "company", "error")

    def __init__(self, request_id: str, issue: str, subject: str, company: str, error: str = ""):
        self.request_id = request_id
        self.issue = issue
        self.subject = subject
        self.company = company
        self.error = error

    @property
    def ok(self) -> bool:
        return not self.error


def validate(row: dict, row_index: int, epoch_ms: int | None = None) -> GatekeeperResult:
    """
    Validate and normalise one CSV row. Returns a GatekeeperResult.
    On hard schema errors the result has .error set and the pipeline
    should emit an escalated output row.
    """
    epoch_ms = epoch_ms or int(time.time() * 1000)
    request_id = f"req_{row_index:03d}_1_{epoch_ms}"

    try:
        issue = str(row.get("issue") or row.get("Issue") or "").strip()
        subject = str(row.get("subject") or row.get("Subject") or "").strip()
        raw_company = str(row.get("company") or row.get("Company") or "None").strip()
    except Exception as exc:
        return GatekeeperResult(
            request_id, "", "", "None",
            error=f"schema_violation: {exc}"
        )

    # Normalise company
    company = _COMPANY_NORMALISE.get(raw_company.lower(), "None")

    # Truncate: preserve at least MIN_ISSUE_CHARS of issue
    issue_budget = min(len(issue), max(MIN_ISSUE_CHARS, MAX_COMBINED_CHARS - len(subject)))
    subject_budget = MAX_COMBINED_CHARS - min(len(issue), issue_budget)
    issue = issue[:issue_budget]
    subject = subject[:subject_budget]

    return GatekeeperResult(request_id, issue, subject, company)


def make_error_row(request_id: str, reason: str) -> dict:
    return {
        "status": "escalated",
        "product_area": "general_support",
        "response": "Escalate to a human",
        "justification": f"Input parse error [{request_id}]: {reason}",
        "request_type": "product_issue",
    }
