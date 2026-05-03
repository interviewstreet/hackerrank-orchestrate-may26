"""
Reasoning: LLM response generation via OpenRouter.

Uses OpenRouter (OpenAI-compatible API) with gpt-oss-120b:free model.
Falls back to Anthropic Claude if OpenRouter is unavailable.
Falls back to extractive local-doc response if no LLM is available.

KEY FIX vs ARIA: The _fallback_response logic now respects the original
safety/escalation decision instead of blindly overwriting the status.
"""

import os
import json
import re
from typing import List, Dict, Optional

# ---------------------------------------------------------------------------
# Import LLM clients (graceful if missing)
# ---------------------------------------------------------------------------
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    import anthropic
except ImportError:
    anthropic = None


class Reasoner:
    """
    Calls LLM API with grounded context.
    Priority: OpenRouter (gpt-oss-120b:free) → Claude → Extractive Fallback.
    """

    def __init__(self, openrouter_key: Optional[str] = None, anthropic_key: Optional[str] = None):
        self.openrouter_client = None
        self.anthropic_client = None
        self.provider = None

        # --- Try OpenRouter first ---
        openrouter_key = openrouter_key or os.environ.get('OPENROUTER_API_KEY')
        if openrouter_key and OpenAI:
            try:
                self.openrouter_client = OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=openrouter_key,
                    default_headers={"Authorization": f"Bearer {openrouter_key}"}
                )
                self.provider = "openrouter"
                self.model = os.environ.get("MODEL_NAME", "openai/gpt-oss-120b:free")
                return
            except Exception as e:
                print(f"[Reasoning] OpenRouter init failed: {e}")

        # --- Fallback to Claude ---
        anthropic_key = anthropic_key or os.environ.get('ANTHROPIC_API_KEY')
        if anthropic_key and anthropic:
            try:
                self.anthropic_client = anthropic.Anthropic(api_key=anthropic_key)
                self.provider = "claude"
                self.model = "claude-3-5-sonnet-20241022"
                return
            except Exception as e:
                print(f"[Reasoning] Claude init failed: {e}")

        self.provider = None

    def generate_response(
        self,
        issue: str,
        subject: str,
        company: str,
        product_area: str,
        request_type: str,
        context_str: str,
        escalation_reason: Optional[str] = None
    ) -> Dict:
        """
        Generate a grounded response using the LLM.
        
        Args:
            context_str: Pre-formatted context string from hybrid engine.
            escalation_reason: If set, return escalation template immediately.
        
        Returns:
            Dict with keys: status, response, justification, confidence
        """
        # If pre-marked for escalation, skip LLM entirely
        if escalation_reason:
            return generate_escalation_response(escalation_reason)

        prompt = self._build_prompt(issue, subject, company, product_area, request_type, context_str)
        has_context = bool(context_str and context_str != "No relevant documentation found.")

        if self.provider == "openrouter" and self.openrouter_client:
            result = self._call_openrouter(prompt)
        elif self.provider == "claude" and self.anthropic_client:
            result = self._call_claude(prompt)
        else:
            return {
                'status': 'escalated',
                'response': 'No LLM provider available. Please escalate to human support.',
                'justification': 'OpenRouter and Claude both unavailable — using safe escalation.',
                'confidence': 0.0,
            }

        if result.get('status') == 'escalated' and has_context:
            extractive = generate_extractive_response(
                context_str,
                product_area,
                'LLM escalated despite available corpus context',
            )
            if extractive.get('status') == 'replied':
                return extractive

        return result

    def _build_prompt(self, issue, subject, company, product_area, request_type, context_str) -> str:
        """Build the grounded LLM prompt with strict JSON output format."""
        return f"""You are a Senior Support Triage Engineer for {company}. Your goal is to provide a grounded, safe, and professional response using ONLY the provided documentation.

STRICT OPERATIONAL RULES:
1. GROUNDING: Use ONLY information from the CONTEXT SECTIONS. If the answer isn't there, you MUST escalate.
2. CITATIONS: In your justification, you MUST mention the specific source section or document title used.
3. CONCISENESS: Answer the issue directly. No preamble. No conversational filler.
4. SCOPE: If the documentation provides a CLEAR POLICY or CONTACT STEP for an issue (e.g., "Email support@company.com for refunds"), you should provide that info and set status="replied". 
5. HUMAN HANDOFF: If the user asks for an action only a human can do (e.g., "Refund me now"), but the doc tells them what to do, set status="replied" and give them the instructions. ONLY set status="escalated" if the docs are missing or if the issue is high-risk/unanswered.
6. VERBATIM: Copy all links, emails, and phone numbers EXACTLY as they appear in the source.

CONTEXT SECTIONS:
{context_str}

TICKET DATA:
- Subject: {subject}
- Issue: {issue}
- Product Area: {product_area}
- Request Type: {request_type}

Respond with ONLY a raw JSON object (no markdown, no extra text):
{{
    "status": "replied" or "escalated",
    "response": "the user-facing answer",
    "justification": "decision logic citing specific source sections",
    "confidence": 0.95
}}"""

    def _call_openrouter(self, prompt: str) -> Dict:
        """Call OpenRouter API and parse structured JSON response."""
        try:
            message = self.openrouter_client.chat.completions.create(
                model=self.model,
                max_tokens=600,
                messages=[{"role": "user", "content": prompt}]
            )
            response_text = message.choices[0].message.content
            return self._parse_json_response(response_text)
        except Exception as e:
            raise RuntimeError(f"OpenRouter error: {str(e)}")

    def _call_claude(self, prompt: str) -> Dict:
        """Call Claude API and parse structured JSON response."""
        try:
            message = self.anthropic_client.messages.create(
                model=self.model,
                max_tokens=600,
                messages=[{"role": "user", "content": prompt}]
            )
            response_text = message.content[0].text
            return self._parse_json_response(response_text)
        except Exception as e:
            raise RuntimeError(f"Claude error: {str(e)}")

    def _parse_json_response(self, text: str) -> Dict:
        """Parse LLM response as JSON with multiple fallback strategies."""
        # Strategy 1: Direct parse
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Strategy 2: Strip markdown fences
        cleaned = re.sub(r'^```(?:json)?\s*', '', text.strip(), flags=re.MULTILINE)
        cleaned = re.sub(r'\s*```\s*$', '', cleaned.strip(), flags=re.MULTILINE)
        try:
            return json.loads(cleaned)
        except json.JSONDecodeError:
            pass

        # Strategy 3: Extract first JSON object
        json_match = re.search(r'\{.*\}', text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group())
            except json.JSONDecodeError:
                pass

        # Strategy 4: Give up, return escalation
        return {
            'status': 'escalated',
            'response': 'Could not parse LLM response. Please escalate to human support.',
            'justification': f'LLM returned unparseable response: {text[:100]}...',
            'confidence': 0.0,
        }


# ---------------------------------------------------------------------------
# Extractive Fallback (no LLM needed)
# ---------------------------------------------------------------------------

def generate_extractive_response(context_str: str, product_area: str, fallback_reason: str = "") -> Dict:
    """
    Generate a grounded response directly from retrieved context.
    Used when no LLM is available. Stays safe by only quoting corpus text.
    """
    if not context_str or context_str == "No relevant documentation found.":
        return generate_escalation_response("No relevant support documentation found in corpus.")

    # Extract the most useful content from the context string
    text = _clean_markdown(context_str)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    useful = [s.strip() for s in sentences if len(s.strip()) > 20]

    # Build excerpt from first few useful sentences
    if '1.' in text or '* ' in text:
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        excerpt = " ".join(lines[:5])
    else:
        excerpt = " ".join(useful[:4]) or text[:500].strip()

    if len(excerpt) > 800:
        excerpt = excerpt[:797].rstrip() + "..."

    return {
        'status': 'replied',
        'response': f"{excerpt}",
        'justification': f"Extractive fallback from local corpus ({product_area}). Note: {fallback_reason}.",
        'confidence': 0.5,
    }


def _clean_markdown(text: str) -> str:
    """Remove markdown noise for extractive fallback responses."""
    text = re.sub(r'^---\s+.*?\s+---', ' ', text, flags=re.DOTALL)
    text = re.sub(r'^\s*(title|slug|source url|article slug|last updated).*$', ' ', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL)
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', ' ', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'[#*_`>|-]+', ' ', text)
    text = re.sub(r'--- Section \d+.*?---', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ---------------------------------------------------------------------------
# Template responses
# ---------------------------------------------------------------------------

def generate_escalation_response(reason: str) -> Dict:
    """Generate a safe escalation response template."""
    return {
        'status': 'escalated',
        'response': 'This issue requires human support. A support specialist will follow up with you shortly.',
        'justification': reason,
        'confidence': 1.0,
    }


# ---------------------------------------------------------------------------
# High-level convenience function (used by main.py)
# ---------------------------------------------------------------------------

def generate_grounded_response(
    issue: str,
    subject: str,
    company: str,
    product_area: str,
    request_type: str,
    context_str: str,
    escalation_reason: Optional[str] = None,
    openrouter_key: Optional[str] = None,
    anthropic_key: Optional[str] = None
) -> Dict:
    """
    High-level function to generate a grounded response.
    
    Tries OpenRouter first, falls back to Claude, then extractive.
    
    KEY FIX: The fallback now respects the original escalation_reason
    instead of blindly overwriting the status to 'replied'.
    """
    # If pre-escalated, always return escalation (never let LLM override)
    if escalation_reason:
        return generate_escalation_response(escalation_reason)

    try:
        reasoner = Reasoner(openrouter_key=openrouter_key, anthropic_key=anthropic_key)
        if reasoner.provider:
            return reasoner.generate_response(
                issue=issue,
                subject=subject,
                company=company,
                product_area=product_area,
                request_type=request_type,
                context_str=context_str,
                escalation_reason=escalation_reason
            )
        else:
            # No LLM — use extractive fallback (safe, grounded)
            return generate_extractive_response(context_str, product_area, "No LLM provider available")
    except Exception as e:
        # LLM failed — use extractive fallback (safe, grounded)
        # FIX: Don't blindly escalate — use extractive if we have context
        if context_str and context_str != "No relevant documentation found.":
            return generate_extractive_response(context_str, product_area, str(e))
        return generate_escalation_response(f"LLM failed and no fallback context: {str(e)}")
