import re
from dataclasses import dataclass

VALID_STATUSES = {"replied", "escalated"}
VALID_REQUEST_TYPES = {"product_issue", "feature_request", "bug", "invalid"}

FIELD_PATTERNS = {
    "status": re.compile(r"STATUS\s*[:\-]\s*(\w+)", re.IGNORECASE),
    "product_area": re.compile(r"PRODUCT_AREA\s*[:\-]\s*(.+?)(?:\n|$)", re.IGNORECASE),
    "request_type": re.compile(r"REQUEST_TYPE\s*[:\-]\s*(\w+)", re.IGNORECASE),
    "justification": re.compile(
        r"JUSTIFICATION\s*[:\-]\s*([\s\S]+?)(?:\nRESPONSE\s*[:\-]|\Z)", re.IGNORECASE
    ),
    "response": re.compile(
        r"RESPONSE\s*[:\-]\s*([\s\S]+?)(?:\n[A-Z_]+\s*[:\-]|\Z)", re.IGNORECASE
    ),
}


@dataclass
class TriageResult:
    status: str
    product_area: str
    response: str
    justification: str
    request_type: str
    raw_agent_output: str


def parse_agent_output(raw_text: str) -> TriageResult:
    extracted = {}
    for field, pattern in FIELD_PATTERNS.items():
        match = pattern.search(raw_text)
        extracted[field] = match.group(1).strip() if match else ""

    status = extracted["status"].lower().strip()
    if status not in VALID_STATUSES:
        status = "replied"

    request_type = (
        extracted["request_type"].lower().replace(" ", "_").replace("-", "_").strip()
    )
    if request_type not in VALID_REQUEST_TYPES:
        request_type = "product_issue"

    product_area = (
        extracted["product_area"]
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .strip()
        or "general_support"
    )

    response = extracted["response"].strip() or raw_text.strip()
    justification = extracted["justification"].strip() or "See response."

    return TriageResult(
        status=status,
        product_area=product_area,
        response=response,
        justification=justification,
        request_type=request_type,
        raw_agent_output=raw_text,
    )
