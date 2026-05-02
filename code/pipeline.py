from typing import Dict
from classifier import classify_ticket
from escalator import should_escalate
from generator import generate_response, generate_invalid_response


def process_ticket(row: Dict, retriever) -> Dict:
    issue = row.get("Issue", "")
    subject = row.get("Subject", "")
    company = row.get("Company", "None")
    
    do_escalate, escalate_reason = should_escalate(issue, subject)
    
    if do_escalate:
        return {
            "status": "escalated",
            "product_area": "unknown",
            "response": "This request requires human attention due to sensitive or high-risk content.",
            "justification": escalate_reason,
            "request_type": "invalid"
        }
    
    request_type, product_area = classify_ticket(issue, subject, company)
    
    if request_type == "invalid":
        return {
            "status": "replied",
            "product_area": product_area,
            "response": generate_invalid_response(issue),
            "justification": "Out of scope request identified by classifier",
            "request_type": request_type
        }
    
    query_text = issue
    if subject:
        query_text = f"{subject} {issue}"
    
    chunks = retriever.query(query_text, company)
    
    if not chunks:
        return {
            "status": "escalated",
            "product_area": product_area,
            "response": "No relevant documentation found. Please escalate to a human agent.",
            "justification": "No matching documents in corpus",
            "request_type": request_type
        }
    
    response = generate_response(issue, subject, chunks, company, request_type)
    
    return {
        "status": "replied",
        "product_area": product_area,
        "response": response,
        "justification": f"Retrieved {len(chunks)} relevant documents from corpus",
        "request_type": request_type
    }