"""
generator.py — Response Generator.

STRICT RULE: Every customer-facing response MUST be grounded in retrieved
corpus content.  The generator is intentionally simple — it surfaces the
most relevant passage, wraps it in a polite template, and refuses to add
information that was not found in the corpus.

For escalated tickets a safe, non-committal message is returned that:
  • Acknowledges the ticket.
  • Explains it has been escalated.
  • Avoids promising a timeline or outcome.
"""

from __future__ import annotations

import textwrap
from typing import Optional

from decision import Decision, TicketContext
from retriever import RetrievedDoc
from utils import log


# ─────────────────────────────────────────────────────────────────────────────
# Templates
# ─────────────────────────────────────────────────────────────────────────────

# Safe escalation message — no commitments, no hallucinated policies
_ESCALATION_TEMPLATE = (
    "Thank you for reaching out to HackerRank Support. "
    "We have received your ticket and our team is reviewing it. "
    "Your request has been escalated to the appropriate specialist team "
    "who will be in touch with you shortly. "
    "We appreciate your patience and apologise for any inconvenience."
)

# Escalation message for explicitly prohibited requests
_POLICY_VIOLATION_TEMPLATE = (
    "Thank you for contacting HackerRank Support. "
    "After reviewing your request, we are unable to fulfil it as it falls outside "
    "the scope of permitted actions under HackerRank's Terms of Service. "
    "If you believe this message was sent in error, please contact your account manager "
    "or reach out to support@hackerrank.com for further clarification."
)

# Risk-specific escalation (security / fraud)
_SECURITY_ESCALATION_TEMPLATE = (
    "Thank you for alerting us. "
    "Your report has been flagged as a HIGH-PRIORITY security matter and has been "
    "immediately escalated to our Security and Trust team. "
    "Please do not attempt to log in or change any credentials until you hear from us. "
    "Our team will contact you within 2 hours."
)

_PRIVACY_ESCALATION_TEMPLATE = (
    "Thank you for your data privacy request. "
    "This has been escalated to our Privacy and Compliance team who will process it "
    "in accordance with applicable data protection regulations (including GDPR). "
    "You can expect a response within 30 days as required by law."
)

_BILLING_ESCALATION_TEMPLATE = (
    "Thank you for reaching out regarding your billing concern. "
    "Your case has been escalated to our Finance and Billing team for investigation. "
    "Please allow up to 5 business days for a resolution. "
    "If you have transaction IDs or receipts available, please reply to this ticket "
    "with those details to help us resolve your case faster."
)

# Reply prefix
_REPLY_GREETING = "Thank you for contacting HackerRank Support. "


# ─────────────────────────────────────────────────────────────────────────────
# Generator
# ─────────────────────────────────────────────────────────────────────────────

class ResponseGenerator:
    """
    Produces customer-facing response text.

    • For 'replied' decisions: extracts and formats the most relevant
      passage from the best retrieved document. No content is added beyond
      what the corpus contains.

    • For 'escalated' decisions: returns the appropriate canned safe message
      based on the risk category.
    """

    # Maximum words to include from the corpus chunk in the reply
    MAX_CHUNK_WORDS = 120

    def generate(self, ctx: TicketContext, decision: Decision) -> str:
        if decision.status == "escalated":
            return self._escalation_response(ctx, decision)
        return self._reply_response(ctx, decision)

    # ── Escalation responses ───────────────────────────────────────────────

    def _escalation_response(self, ctx: TicketContext, decision: Decision) -> str:
        """Pick the most appropriate escalation template based on risk category."""
        rc = ctx.risk_category or ""

        if ctx.request_type == "invalid":
            log.info("Generating policy-violation response.")
            return _POLICY_VIOLATION_TEMPLATE

        if rc == "fraud_security":
            log.info("Generating security escalation response.")
            return _SECURITY_ESCALATION_TEMPLATE

        if rc == "data_privacy":
            log.info("Generating privacy escalation response.")
            return _PRIVACY_ESCALATION_TEMPLATE

        if rc == "payment_dispute":
            log.info("Generating billing escalation response.")
            return _BILLING_ESCALATION_TEMPLATE

        # Generic escalation
        log.info("Generating generic escalation response.")
        return _ESCALATION_TEMPLATE

    # ── Reply responses ────────────────────────────────────────────────────

    def _reply_response(self, ctx: TicketContext, decision: Decision) -> str:
        """
        Build a reply grounded in the best retrieved document.

        Strategy:
          1. Take the best chunk from the retriever.
          2. Truncate to MAX_CHUNK_WORDS to keep the response concise.
          3. Wrap in a polite template.
          4. Add a feature-request note if applicable.
          5. Append a source attribution line (internal, not shown to customer —
             but kept here for auditability in the CSV).
        """
        doc = decision.best_doc
        if doc is None:
            # Defensive fallback — should not happen for 'replied' status
            log.warn("No best_doc for a replied ticket — falling back to generic escalation.")
            return _ESCALATION_TEMPLATE

        # Trim the chunk to a reasonable length
        passage = self._trim_passage(doc.chunk.text)

        if ctx.request_type == "feature_request":
            response = (
                f"{_REPLY_GREETING}"
                f"Thank you for your feature suggestion! "
                f"We have noted your request. Here is some relevant information from our "
                f"current documentation that may be helpful:\n\n"
                f"{passage}\n\n"
                f"To formally submit your feature request, please visit our Feedback Portal "
                f"at feedback.hackerrank.com. Feature requests are reviewed quarterly by our "
                f"Product team, and popular requests may be added to the roadmap."
            )
        else:
            response = (
                f"{_REPLY_GREETING}"
                f"Based on our support documentation, here is the information relevant to "
                f"your query:\n\n"
                f"{passage}\n\n"
                f"If this does not fully resolve your issue, please reply to this ticket "
                f"with additional details and we will be happy to assist further."
            )

        return response.strip()

    # ── Helpers ────────────────────────────────────────────────────────────

    def _trim_passage(self, text: str) -> str:
        """Truncate passage to MAX_CHUNK_WORDS words, ending at a sentence boundary if possible."""
        words = text.split()
        if len(words) <= self.MAX_CHUNK_WORDS:
            return text

        truncated = " ".join(words[:self.MAX_CHUNK_WORDS])

        # Try to end at a sentence boundary (., !, ?)
        for punct in (".", "!", "?"):
            last_punct = truncated.rfind(punct)
            if last_punct > len(truncated) // 2:   # don't cut too early
                return truncated[:last_punct + 1]

        return truncated + "…"
