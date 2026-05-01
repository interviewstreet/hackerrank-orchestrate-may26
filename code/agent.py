#!/usr/bin/env python3
import logging
from pathlib import Path
from typing import Optional, List, Dict

from retriever import Retriever
import classifier


# Logging setup (append-only shared log)
LOG_DIR = Path.home() / "hackerrank_orchestrate"
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "log.txt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filemode="a",
)
logger = logging.getLogger(__name__)


class SupportTicketAgent:
    """High-level agent that composes classifier + retriever to triage tickets."""

    def __init__(self, corpus_path: str = "../data"):
        logger.info("Initializing Retriever...")
        self.retriever = Retriever(corpus_path)
        logger.info(f"Corpus loaded: {self.retriever.document_count} documents indexed")

    def process_ticket(self, issue: str, subject: str = "", company: Optional[str] = None) -> Dict:
        # Infer company if not provided
        if not company:
            company = classifier.infer_company(issue, subject)

        # Classify request type
        request_type = classifier.classify_request_type(issue)

        # Retrieve relevant docs
        docs = self.retriever.retrieve(issue, company=company, limit=5)

        # Decide escalation
        should_escalate, escalation_reason = classifier.should_escalate(issue, request_type, docs)

        if should_escalate:
            return {
                "status": "escalated",
                "product_area": company or "Unknown",
                "response": "",
                "justification": escalation_reason,
                "request_type": request_type,
            }

        # Extractive response generation (simple, deterministic)
        if not docs:
            return {
                "status": "escalated",
                "product_area": company or "Unknown",
                "response": "",
                "justification": "No relevant documentation available",
                "request_type": request_type,
            }

        best_doc = docs[0]
        best_content = best_doc.get("content", "")

        # Simple extractive: pick up to two sentences that match query tokens
        import re

        issue_terms = [t for t in re.findall(r"[a-z0-9]+", issue.lower()) if len(t) > 2]
        sentences = re.split(r"(?<=[.!?])\s+", best_content)
        relevant_sentences = []
        for s in sentences:
            if any(term in s.lower() for term in issue_terms):
                relevant_sentences.append(s.strip())
            if len(relevant_sentences) >= 2:
                break

        if not relevant_sentences:
            relevant_sentences = [s.strip() for s in sentences[:2] if s.strip()]

        response = " ".join(relevant_sentences[:2])
        if response and not response.endswith((".", "?", "!")):
            response += "."

        justification = (
            f"Grounded in {best_doc.get('source', 'corpus')} with {len(docs)} retrieved documents; "
            f"top similarity score {best_doc.get('score', 0):.2f}"
        )

        product_area = company or "Unknown"
        if docs and "category" in best_doc:
            product_area = f"{company}/{best_doc.get('category')}"

        return {
            "status": "replied",
            "product_area": product_area,
            "response": response,
            "justification": justification,
            "request_type": request_type,
        }

    def process_csv(self, input_file: str, output_file: str):
        import csv

        tickets = []
        with open(input_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                tickets.append(row)

        logger.info(f"Processing {len(tickets)} tickets from {input_file}")

        predictions = []
        for ticket in tickets:
            issue = ticket.get("Issue", "")
            subject = ticket.get("Subject", "")
            company = ticket.get("Company")
            pred = self.process_ticket(issue, subject, company)
            pred["issue"] = issue
            pred["subject"] = subject
            pred["company"] = company or ""
            predictions.append(pred)

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["issue", "subject", "company", "response", "product_area", "status", "request_type", "justification"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in predictions:
                writer.writerow({
                    "issue": p["issue"],
                    "subject": p["subject"],
                    "company": p["company"],
                    "response": p["response"],
                    "product_area": p["product_area"],
                    "status": p["status"],
                    "request_type": p["request_type"],
                    "justification": p["justification"],
                })

        logger.info(f"Predictions written to {output_file}")
        print(f"✓ Processed {len(predictions)} tickets")
        print(f"✓ Output written to {output_file}")
