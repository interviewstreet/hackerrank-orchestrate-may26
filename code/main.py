from pathlib import Path
import csv
import math
import re
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = REPO_ROOT / "data"
INPUT_FILE = REPO_ROOT / "support_tickets" / "support_tickets.csv"
OUTPUT_FILE = REPO_ROOT / "support_tickets" / "output.csv"

STOPWORDS = {
    "the", "and", "or", "to", "a", "an", "of", "in", "on", "for", "with", "is", "are", "was",
    "be", "have", "has", "it", "this", "that", "as", "at", "by", "from", "your", "you", "i",
    "we", "our", "can", "will", "do", "does", "did", "not", "also", "please", "help", "need",
    "issue", "ticket", "support", "help", "my", "me", "us", "may", "should", "would", "could",
}

ESCALATION_KEYWORDS = {
    "identity stolen", "stolen", "fraud", "unauthorised", "unauthorized", "hacked", "hack", "account takeover",
    "charge dispute", "dispute", "refund asap", "refund", "payment issue", "order id", "merchant", "wrong product",
    "ban the seller", "urgent cash", "blocked", "blocked card", "charge", "security vulnerability", "legal",
    "removed my seat", "access lost", "account access", "lost access", "locked",
}

INVALID_PATTERNS = {
    "give me the code", "delete all files", "name of the actor", "not in scope", "please build", "please code",
}

def normalize_text(text):
    if not text:
        return []
    tokens = re.findall(r"\w+", text.lower())
    return [token for token in tokens if token not in STOPWORDS]


def read_markdown_documents():
    docs = []
    for ecosystem_dir in DATA_ROOT.iterdir():
        if not ecosystem_dir.is_dir():
            continue
        for md_file in ecosystem_dir.rglob("*.md"):
            try:
                text = md_file.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            title = ""
            for line in text.splitlines():
                cleaned = line.strip()
                if cleaned.startswith("#"):
                    title = cleaned.lstrip("# ").strip()
                    break
            label = title or md_file.stem
            tokens = normalize_text(title + " " + text)
            if not tokens:
                continue
            docs.append({
                "path": md_file.relative_to(REPO_ROOT).as_posix(),
                "ecosystem": ecosystem_dir.name.lower(),
                "title": label,
                "content": text,
                "tokens": tokens,
                "tf": Counter(tokens),
            })
    return docs


def build_idf(documents):
    df = Counter()
    for doc in documents:
        df.update(set(doc["tokens"]))
    total = len(documents)
    return {term: math.log((total + 1) / (1 + count)) + 1 for term, count in df.items()}


def vector_norm(counter, idf):
    return math.sqrt(sum((count * idf.get(term, 1)) ** 2 for term, count in counter.items()))


def score_query(query_tokens, doc, idf):
    query_tf = Counter(query_tokens)
    dot = 0.0
    for term, qcount in query_tf.items():
        dot += qcount * doc["tf"].get(term, 0) * idf.get(term, 1)
    norm_query = vector_norm(query_tf, idf)
    norm_doc = vector_norm(doc["tf"], idf)
    if norm_query == 0 or norm_doc == 0:
        return 0.0
    return dot / (norm_query * norm_doc)


def select_top_docs(query, documents, idf, limit=3):
    tokens = normalize_text(query)
    scored = []
    for doc in documents:
        if doc["ecosystem"] not in query.lower() and False:
            pass
        score = score_query(tokens, doc, idf)
        scored.append((score, doc))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [doc for score, doc in scored[:limit] if score > 0]


def classify_request_type(text):
    q = text.lower()
    if any(pattern in q for pattern in INVALID_PATTERNS):
        return "invalid"
    if any(term in q for term in ["bug", "error", "not working", "failed", "issue", "unable to", "problem", "can't", "cannot"]):
        if any(term in q for term in ["feature", "request", "would like", "please add", "can you add"]):
            return "feature_request"
        return "bug"
    if any(term in q for term in ["request", "would like", "could you", "can you", "please add", "need a way"]):
        return "feature_request"
    if any(term in q for term in ["how to", "how do i", "how can i", "what is", "where", "when", "why", "help"]):
        return "product_issue"
    return "product_issue"


def classify_product_area(ecosystem, text, top_doc):
    q = text.lower()
    if ecosystem == "hackerrank":
        if any(word in q for word in ["interview", "hr lobby", "interviewer", "interviewers"]):
            return "Interviews"
        if any(word in q for word in ["candidate", "assessment", "test", "score", "certificate", "grading", "submit", "submissions", "proctor"]):
            return "Assessments"
        if any(word in q for word in ["community", "profile", "practice", "discussion", "forum"]):
            return "Community"
        if any(word in q for word in ["billing", "payment", "subscription", "refund", "invoice", "order id"]):
            return "Billing"
        if any(word in q for word in ["login", "sign in", "password", "account", "profile", "admin", "access", "seat"]):
            return "Account"
        if any(word in q for word in ["api", "integration", "webhook", "postman"]):
            return "API"
        if "certificate" in q or "certification" in q:
            return "Certification"
    elif ecosystem == "claude":
        if any(word in q for word in ["api", "rest api", "sdk", "endpoint", "model"]):
            return "API"
        if any(word in q for word in ["workspace", "sign in", "login", "account", "profile", "seat", "admin"]):
            return "Account"
        if any(word in q for word in ["billing", "subscription", "payment", "pricing", "invoice"]):
            return "Billing"
        if any(word in q for word in ["workbench", "desktop", "chrome", "mobile", "web"]):
            return "Workbench"
        if any(word in q for word in ["enterprise", "team", "organization", "org", "admin"]):
            return "Enterprise"
        return "Claude.ai"
    elif ecosystem == "visa":
        if any(word in q for word in ["fraud", "stolen", "security", "identity theft", "phishing", "blocked"]):
            return "Security"
        if any(word in q for word in ["travel", "visa traveler", "traveler", "trip", "hotel"]):
            return "Travel"
        if any(word in q for word in ["offer", "cashback", "promotion", "reward"]):
            return "Offers"
        if any(word in q for word in ["payment", "charge", "refund", "order", "merchant"]):
            return "Payments"
        if any(word in q for word in ["card", "credit card", "debit card", "blocked", "account"]):
            return "Cards"
        return "Other"
    inferred = infer_area_from_doc_path(ecosystem, top_doc)
    return inferred or "Other"


def infer_area_from_doc_path(ecosystem, doc):
    if not doc:
        return "Other"
    path = doc["path"].lower()
    if ecosystem == "hackerrank":
        if "interviews" in path:
            return "Interviews"
        if "community" in path:
            return "Community"
        if "billing" in path or "payment" in path:
            return "Billing"
        if "account" in path or "settings" in path or "sso" in path:
            return "Account"
        if "api" in path or "integration" in path:
            return "API"
        if "certificate" in path:
            return "Certification"
        return "Assessments"
    if ecosystem == "claude":
        if "api" in path or "console" in path:
            return "API"
        if "billing" in path or "pricing" in path:
            return "Billing"
        if "account" in path or "identity" in path or "workspace" in path or "admin" in path:
            return "Account"
        if "workbench" in path or "desktop" in path or "chrome" in path or "mobile" in path:
            return "Workbench"
        if "enterprise" in path or "team" in path or "org" in path:
            return "Enterprise"
        return "Claude.ai"
    if ecosystem == "visa":
        if "security" in path or "fraud" in path:
            return "Security"
        if "travel" in path:
            return "Travel"
        if "offer" in path or "rewards" in path:
            return "Offers"
        if "payment" in path or "charge" in path or "merchant" in path:
            return "Payments"
        if "card" in path:
            return "Cards"
        return "Other"
    return "Other"


def should_escalate(text, top_doc, score):
    q = text.lower()
    if any(keyword in q for keyword in ESCALATION_KEYWORDS):
        return True
    if any(pattern in q for pattern in INVALID_PATTERNS):
        return True
    if top_doc is None or score < 0.05:
        return True
    return False


def build_response(ecosystem, text, top_doc, product_area, escalate):
    if escalate:
        return "This issue has been escalated to our support team for further review. They will be in touch shortly."
    if top_doc:
        return (
            f"I found a relevant article in the {ecosystem.title()} help center: {top_doc['title']}. "
            f"You can review it here: {top_doc['path']}. If you have additional questions, feel free to ask."
        )
    return (
        f"I could not find a specific article for this issue right now. "
        f"Please contact the support team for {ecosystem.title()} if you need further assistance."
    )


def build_justification(request_type, product_area, top_doc, escalate):
    if escalate:
        return "Escalated due to high-risk content or insufficient matched documentation."
    note = "Matched topic using local corpus and ticket text."
    if top_doc:
        return f"{note} Top article: {top_doc['path']}"
    return note


def read_tickets(input_file):
    tickets = []
    with input_file.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            tickets.append({
                "issue": row.get("Issue", "") or "",
                "subject": row.get("Subject", "") or "",
                "company": (row.get("Company", "") or "").strip(),
            })
    return tickets


def write_output(rows):
    fieldnames = ["status", "product_area", "response", "justification", "request_type"]
    with OUTPUT_FILE.open("w", newline='', encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def canonical_ecosystem(company):
    name = company.strip().lower()
    if "hackerrank" in name:
        return "hackerrank"
    if "claude" in name:
        return "claude"
    if "visa" in name:
        return "visa"
    return "hackerrank"


def main():
    documents = read_markdown_documents()
    if not documents:
        raise RuntimeError("No documents found in the corpus.")
    idf = build_idf(documents)
    tickets = read_tickets(INPUT_FILE)
    output_rows = []

    for ticket in tickets:
        text = " ".join([ticket["issue"], ticket["subject"], ticket["company"]]).strip()
        ecosystem = canonical_ecosystem(ticket["company"] or text)
        matched_docs = [doc for doc in documents if doc["ecosystem"] == ecosystem]
        query_text = ticket["issue"] + " " + ticket["subject"]
        top_docs = select_top_docs(query_text, matched_docs, idf, limit=3)
        top_doc = top_docs[0] if top_docs else None
        top_score = score_query(normalize_text(query_text), top_doc, idf) if top_doc else 0.0

        request_type = classify_request_type(query_text)
        product_area = classify_product_area(ecosystem, query_text, top_doc)
        escalate = should_escalate(query_text, top_doc, top_score)
        status = "escalated" if escalate else "replied"
        response = build_response(ecosystem, query_text, top_doc, product_area, escalate)
        justification = build_justification(request_type, product_area, top_doc, escalate)

        output_rows.append({
            "status": status,
            "product_area": product_area,
            "response": response,
            "justification": justification,
            "request_type": request_type,
        })

    write_output(output_rows)
    print(f"Wrote {len(output_rows)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
