#!/usr/bin/env python3
"""
Demo script: Run the agent on sample tickets WITHOUT API calls.
Shows what the agent would output by simulating responses based on retrieved docs.
"""

import csv
from pathlib import Path
from corpus_index import CorpusIndex


def simulate_agent_response(corpus, issue, subject, company):
    """Simulate agent response using corpus retrieval (no API calls)."""
    # Infer company from text if not provided
    if not company:
        from main import SupportTicketAgent
        agent_temp = object.__new__(SupportTicketAgent)
        company = agent_temp.infer_company(issue, subject) or "Unknown"
    
    # Classify request type
    from main import SupportTicketAgent
    agent_temp = object.__new__(SupportTicketAgent)
    request_type = agent_temp.classify_request_type(issue)
    
    # Retrieve relevant docs
    docs = corpus.retrieve(issue, company=company, limit=5)
    
    # Apply escalation logic
    should_escalate, reason = apply_escalation_rules(issue, request_type, docs)
    
    if should_escalate:
        return {
            "Status": "escalated",
            "Product Area": company,
            "Response": "",
            "Justification": reason,
            "Request Type": request_type
        }
    else:
        # Generate simulated response from docs
        if docs:
            product_area = f"{company}/{docs[0].get('category', 'General')}"
            justification = f"Found {len(docs)} relevant documents. Top match: {docs[0]['source']}"
            response = f"Based on our documentation in the {docs[0]['category']} section: [See: {docs[0]['source']}]"
        else:
            product_area = company
            justification = "Insufficient documentation available"
            response = "I don't have enough information to answer this question."
        
        return {
            "Status": "replied",
            "Product Area": product_area,
            "Response": response[:200],  # Truncate for demo
            "Justification": justification,
            "Request Type": request_type
        }


def apply_escalation_rules(issue, request_type, docs):
    """Apply escalation logic."""
    issue_lower = issue.lower()
    
    if request_type == "invalid":
        return True, "Content violation or invalid request"
    
    sensitive_patterns = [
        "access denied", "permission denied", "restore", "access",
        "billing", "payment", "invoice", "fraud", "chargeback",
        "password", "two factor", "personal info", "ssn", "credit card"
    ]
    
    if any(pattern in issue_lower for pattern in sensitive_patterns):
        return True, "Sensitive or permission-related issue requires human review"
    
    if not docs or (len(docs) == 1 and docs[0].get("score", 0) < 0.3):
        return True, "No relevant documentation found in corpus"
    
    return False, ""


def main():
    """Run demo on sample tickets."""
    print("HackerRank Orchestrate - Demo Run (No API Calls)\n")
    print("This demonstrates the agent working on sample tickets")
    print("using only corpus retrieval and pattern matching.\n")
    
    # Load corpus
    print("→ Loading corpus...")
    corpus = CorpusIndex("../data")
    print(f"✓ Loaded {len(corpus.documents)} documents\n")
    
    # Process sample tickets
    sample_file = Path("../support_tickets/sample_support_tickets.csv")
    output_file = Path("../support_tickets/demo_output.csv")
    
    print(f"→ Processing tickets from {sample_file.name}...")
    
    tickets = []
    with open(sample_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        tickets = list(reader)
    
    print(f"✓ Read {len(tickets)} sample tickets\n")
    
    # Generate predictions
    predictions = []
    for i, ticket in enumerate(tickets, 1):
        issue = ticket.get("Issue", "")
        subject = ticket.get("Subject", "")
        company = ticket.get("Company")
        
        pred = simulate_agent_response(corpus, issue, subject, company)
        predictions.append(pred)
        
        print(f"{i}. {subject[:40]:40} → {pred['Status']:10} ({pred['Request Type']})")
    
    # Write output
    print(f"\n→ Writing predictions to {output_file.name}...")
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Status", "Product Area", "Response", "Justification", "Request Type"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(predictions)
    
    print(f"✓ Demo output written to {output_file.name}")
    print(f"\n✓ Demo complete!")
    print(f"\nTo run the full agent with API calls:")
    print(f"  1. export ANTHROPIC_API_KEY='sk-ant-...'")
    print(f"  2. python3 main.py")


if __name__ == "__main__":
    main()
