"""
Classifier: Detect company domain and classify product areas / request types.

Pure rule-based classification — no LLM, no imports from other modules.
This ensures the classifier works independently regardless of which retrieval
engine is active.
"""

import re
from typing import Optional, List, Any

# ---------------------------------------------------------------------------
# Company Detection Keywords
# ---------------------------------------------------------------------------
COMPANY_KEYWORDS = {
    'hackerrank': [
        'test', 'candidate', 'assessment', 'role', 'screen', 'interview',
        'mock interview', 'hackerrank', 'hackekrank', 'hakerrank', 'hacker rank',
        'hr', 'hiring', 'recruiter', 'question', 'library', 'variant',
        'engage', 'invite', 'certificate', 'resume builder', 'practice',
        'submission', 'interviewer', 'proctoring', 'inactivity',
        'compatibility check', 'skillup',
    ],
    'claude': [
        'claude', 'claud', 'clade', 'api', 'model', 'token', 'context',
        'conversation', 'desktop', 'chat', 'prompt', 'anthropic', 'bedrock',
        'lti', 'team workspace', 'subscription', 'crawl', 'robot',
        'vulnerability', 'bug bounty', 'education', 'workspace', 'connector',
    ],
    'visa': [
        'card', 'payment', 'visa', 'viza', 'credit', 'debit', 'transaction',
        'merchant', 'dispute', 'fraud', 'cheque', 'traveller', 'minimum',
        'spend', 'cash', 'blocked', 'stolen', 'identity theft',
        'viisaa', 'visaa',
    ],
}

# ---------------------------------------------------------------------------
# Product Area Keywords (Domain-Aware)
# ---------------------------------------------------------------------------
DOMAIN_PRODUCT_AREAS = {
    'hackerrank': {
        'test_management': ['test', 'create', 'variant', 'archive', 'clone', 'expiration', 'active', 'timer', 'duration'],
        'candidate_management': ['candidate', 'invite', 'reinvite', 'extra time', 'accommodation', 'reschedule', 'pdp', 'candidate report'],
        'interview_management': ['interview', 'interviewer', 'lobby', 'inactivity', 'zoom', 'compatibility', 'live code', 'whiteboard'],
        'account_management': ['account', 'password', 'login', 'user', 'team', 'delete account', 'remove user', 'remove interviewer', 'sso login', 'disabled', 'inactive', 'daabled'],
        'community_certification': ['certificate', 'certification', 'resume builder', 'practice', 'community', 'apply tab', 'badge'],
        'integrations_security': ['infosec', 'security', 'api', 'integration', 'sso', 'scim', 'webhook', 'greenhouse', 'lever', 'ats'],
        'assessment_integrity': ['score', 'leaked', 'grading', 'plagiarism', 'integrity', 'proctoring', 'cheat', 'flag', 'monitoring'],
        'billing_payment': ['billing', 'pricing', 'subscription', 'plan', 'payment', 'refund', 'order id', 'pause', 'invoice', 'receipt'],
    },
    'claude': {
        'api_usage': ['api', 'key', 'token', 'context window', 'rate limit', 'quota', 'bedrock', 'model', 'latency', 'endpoint'],
        'account_management': ['account', 'password', 'login', 'user', 'team', 'delete account', 'remove user', 'sso login', 'disabled', 'inactive', 'daabled', 'seat', 'workspace'],
        'billing_payment': ['billing', 'pricing', 'subscription', 'plan', 'payment', 'refund', 'invoice', 'receipt', 'pro', 'team'],
        'privacy_data': ['data', 'privacy', 'gdpr', 'export', 'retention', 'crawl', 'robot', 'training', 'opt-out', 'compliance'],
        'conversation_management': ['conversation', 'chat', 'delete', 'rename', 'share', 'history', 'archive conversation'],
        'education': ['lti', 'canvas', 'professor', 'student', 'education', 'college', 'university', 'lms'],
        'security_vulnerability': ['vulnerability', 'bug bounty', 'security report', 'disclosure', 'exploit', 'patch'],
    },
    'visa': {
        'card_management': ['card', 'lost', 'stolen', 'replace', 'pin', 'block', 'travel', 'atm', 'debit', 'credit', 'disabled', 'daabled', 'emergency'],
        'payment_dispute': ['fraud', 'dispute', 'unauthorized', 'chargeback', 'transaction', 'merchant', 'suspicious', 'refund', 'scam'],
    }
}


class Classifier:
    """Rule-based classifier for company, product area, and request type."""

    @staticmethod
    def detect_company(issue: str, subject: str = "", company_hint: Optional[str] = None) -> str:
        """
        Detect which domain this ticket belongs to.
        Returns: 'hackerrank', 'claude', 'visa', or 'unknown'
        """
        if company_hint:
            hint_lower = company_hint.strip().lower()
            for domain in COMPANY_KEYWORDS:
                if domain in hint_lower:
                    return domain
            # Handle "None" string
            if hint_lower in ('none', ''):
                pass  # Fall through to inference
            else:
                return hint_lower if hint_lower in COMPANY_KEYWORDS else 'unknown'

        combined = f"{issue} {subject}".lower()

        # Score each domain by keyword hits
        scores = {}
        for domain, keywords in COMPANY_KEYWORDS.items():
            scores[domain] = sum(1 for kw in keywords if kw in combined)

        best = max(scores, key=scores.get)
        return best if scores[best] > 0 else 'unknown'

    @staticmethod
    def classify_product_area(
        issue: str,
        subject: str = "",
        company: str = 'unknown',
        retrieved_chunks: Optional[List[Any]] = None
    ) -> str:
        """
        Classify the product area for this ticket with domain-awareness.
        """
        combined = f"{issue} {subject}".lower()
        company_key = company.lower() if company.lower() in DOMAIN_PRODUCT_AREAS else None
        
        # Get areas for this domain, or all areas if domain is unknown
        if company_key:
            active_areas = DOMAIN_PRODUCT_AREAS[company_key]
        else:
            # Flatten all areas for fallback
            active_areas = {}
            for dom_areas in DOMAIN_PRODUCT_AREAS.values():
                active_areas.update(dom_areas)

        scores = {area: 0 for area in active_areas}
        for area, keywords in active_areas.items():
            scores[area] = sum(1 for kw in keywords if kw in combined)

        # Boost scores from retrieved chunks
        if retrieved_chunks:
            for chunk in retrieved_chunks:
                chunk_text = ""
                if hasattr(chunk, 'heading') and hasattr(chunk, 'content'):
                    chunk_text = f"{chunk.heading} {chunk.content}".lower()
                elif hasattr(chunk, 'page_content'):
                    chunk_text = chunk.page_content.lower()
                elif isinstance(chunk, dict):
                    chunk_text = str(chunk.get('text', '')).lower()

                if chunk_text:
                    for area, keywords in active_areas.items():
                        if any(kw in chunk_text for kw in keywords):
                            scores[area] += 0.5

        if not scores:
            return 'general'

        best = max(scores, key=scores.get)
        if scores[best] > 0:
            return best

        # Fallback by company
        fallbacks = {
            'hackerrank': 'test_management',
            'claude': 'api_usage',
            'visa': 'card_management',
        }
        return fallbacks.get(company_key, 'general')

    @staticmethod
    def classify_request_type(issue: str, subject: str = "") -> str:
        """
        Classify the request type.
        Returns: 'product_issue', 'feature_request', 'bug', 'invalid'
        """
        combined = f"{issue} {subject}".lower()

        # Feature request signals
        if any(w in combined for w in ['can we', 'can you add', 'we need', 'feature request', 'please add', 'would like']):
            return 'feature_request'

        # Bug signals
        if any(w in combined for w in ['broken', 'error', 'not working', 'bug', 'crash', 'failing', 'down']):
            return 'bug'

        # Invalid signals
        if any(w in combined for w in ['ignore', 'jailbreak', 'actor', 'movie', 'delete all files']):
            return 'invalid'

        return 'product_issue'


# ---------------------------------------------------------------------------
# Convenience functions (backward compatible with existing main.py imports)
# ---------------------------------------------------------------------------

def detect_company(issue: str, subject: str = "", company_hint: Optional[str] = None) -> str:
    return Classifier.detect_company(issue, subject, company_hint)

def classify_product_area(issue: str, subject: str = "", company: str = 'unknown', retrieved_chunks=None) -> str:
    return Classifier.classify_product_area(issue, subject, company, retrieved_chunks)

def classify_request_type(issue: str, subject: str = "") -> str:
    return Classifier.classify_request_type(issue, subject)
