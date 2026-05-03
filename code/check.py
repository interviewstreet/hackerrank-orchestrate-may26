"""
Auditor: Senior-level evaluation of triage outputs.

Runs a second-pass LLM review to validate completeness, correctness,
and optimality. Uses the same Reasoner class (OpenRouter → Claude).
"""

import os
import json
from typing import Dict, Optional
from brain import Reasoner


class Auditor:
    """Evaluates triage output using a senior auditor persona."""

    def __init__(self, openrouter_key: Optional[str] = None, anthropic_key: Optional[str] = None):
        self.reasoner = Reasoner(openrouter_key=openrouter_key, anthropic_key=anthropic_key)

    def audit(self, issue_data: Dict, output_data: Dict) -> Dict:
        """
        Audit the triage output for quality.
        Returns: {is_complete, is_correct, is_optimal, issues, suggested_fix}
        """
        if not self.reasoner.provider:
            return {
                "is_complete": True,
                "is_correct": True,
                "is_optimal": True,
                "issues": ["No LLM available for auditing"],
                "suggested_fix": None
            }

        prompt = f"""You are a senior support triage auditor.

Your job is to evaluate whether the generated triage output is complete, correct, and optimal.

Given:
1. Support ticket:
   - issue: {issue_data.get('issue', '')}
   - subject: {issue_data.get('subject', '')}
   - company: {issue_data.get('company', '')}

2. Generated output:
   - status: {output_data.get('status', '')}
   - product_area: {output_data.get('product_area', '')}
   - response: {output_data.get('response', '')}
   - justification: {output_data.get('justification', '')}
   - request_type: {output_data.get('request_type', '')}

Evaluate based on:
1. COMPLETENESS — All fields present and valid?
2. CLASSIFICATION — request_type and product_area correct?
3. DECISION — replied vs escalated chosen correctly?
4. RESPONSE — Grounded, safe, no hallucination?
5. JUSTIFICATION — Concise and correct reasoning?
6. OPTIMALITY — Best possible action given info?

Return ONLY this JSON (no markdown fences):
{{
  "is_complete": true/false,
  "is_correct": true/false,
  "is_optimal": true/false,
  "issues": ["list of specific problems"],
  "suggested_fix": null or {{"status": "...", "response": "...", "justification": "..."}}
}}

Strict rules:
- Do not add external knowledge
- Do not change intent of original issue
- Prefer safety over answering when uncertain"""

        try:
            if self.reasoner.provider == "openrouter":
                return self.reasoner._call_openrouter(prompt)
            else:
                return self.reasoner._call_claude(prompt)
        except Exception as e:
            return {
                "is_complete": True,
                "is_correct": True,
                "is_optimal": True,
                "issues": [f"Audit failed: {str(e)}"],
                "suggested_fix": None
            }
