"""
test_agent.py — pytest test suite for the support triage agent.

Tests cover:
  - Classifier domain and request_type detection (mocked Gemini)
  - Safety gate rules: always-escalate cases and normal-reply cases
  - BM25 retriever relevance ranking on an in-memory index
  - Full single-ticket pipeline smoke test (mocked Gemini)

All Gemini API calls are intercepted with unittest.mock so the suite
runs offline without a valid GEMINI_API_KEY.
"""

import sys
import types
from dataclasses import dataclass
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Ensure the code/ directory is on the path however pytest is invoked
_CODE_DIR = Path(__file__).resolve().parents[1]
if str(_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(_CODE_DIR))

from agent.classifier import Classification
from agent.safety import SafetyDecision, check as safety_check
from corpus.loader import Document, build_index, search

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------


def _make_doc(
    doc_id: str = "d1",
    domain: str = "hackerrank",
    product_area: str = "screen",
    title: str = "Test Article",
    url: str = "https://support.hackerrank.com/article",
    content: str = "This is some support article content about testing.",
) -> Document:
    """Factory for Document test fixtures."""
    return Document(
        doc_id=doc_id,
        domain=domain,
        product_area=product_area,
        title=title,
        url=url,
        content=content,
    )


@pytest.fixture()
def mock_doc() -> Document:
    """A generic HackerRank support document."""
    return _make_doc()


@pytest.fixture()
def visa_doc() -> Document:
    """A Visa support document."""
    return _make_doc(
        doc_id="v1",
        domain="visa",
        product_area="consumer",
        title="Lost or Stolen Card",
        url="https://www.visa.co.in/support/consumer",
        content="Call Visa to report a lost or stolen card immediately.",
    )


@pytest.fixture()
def claude_doc() -> Document:
    """A Claude support document."""
    return _make_doc(
        doc_id="c1",
        domain="claude",
        product_area="pro-and-max-plans",
        title="Cancel Claude Pro Subscription",
        url="https://support.claude.com/en/articles/cancel",
        content="To cancel your Claude Pro subscription go to settings.",
    )


@pytest.fixture()
def small_index():
    """An in-memory BM25 index built from 3 distinct mock documents."""
    docs = [
        _make_doc(
            doc_id="hr1",
            domain="hackerrank",
            product_area="screen",
            title="Inviting Candidates",
            content=(
                "To invite candidates to a coding test on HackerRank, "
                "navigate to the Tests tab and click Invite Candidates."
            ),
        ),
        _make_doc(
            doc_id="cl1",
            domain="claude",
            product_area="claude-mobile-apps",
            title="Installing Claude for iOS",
            content=(
                "You can install the Claude app from the App Store by "
                "searching for Claude by Anthropic."
            ),
        ),
        _make_doc(
            doc_id="vi1",
            domain="visa",
            product_area="consumer",
            title="Reporting a Stolen Visa Card",
            content=(
                "If your Visa card is lost or stolen call 1-800-847-2911 "
                "immediately to block the card."
            ),
        ),
    ]
    return build_index(docs), docs


# ---------------------------------------------------------------------------
# Helpers for Gemini mock construction
# ---------------------------------------------------------------------------


def _make_gemini_response(args: dict):
    """Build a fake Groq response with a JSON string."""
    import json
    message = MagicMock()
    message.content = json.dumps(args)
    
    choice = MagicMock()
    choice.message = message
    
    response = MagicMock()
    response.choices = [choice]
    return response


def _make_text_response(text: str):
    """Build a fake Groq response with plain text."""
    message = MagicMock()
    message.content = text
    
    choice = MagicMock()
    choice.message = message
    
    response = MagicMock()
    response.choices = [choice]
    return response


# ---------------------------------------------------------------------------
# 1. test_classifier_hackerrank_faq
# ---------------------------------------------------------------------------


@patch("agent.classifier._client")
def test_classifier_hackerrank_faq(mock_client):
    """Classifier correctly identifies a HackerRank FAQ ticket."""
    mock_client.chat.completions.create.return_value = _make_gemini_response({
        "domain":       "hackerrank",
        "request_type": "faq",
        "product_area": "screen",
        "confidence":   0.92,
    })

    from agent.classifier import classify

    ticket = "How do I invite candidates to take a coding test on HackerRank?"
    result = classify(ticket)

    assert result.domain == "hackerrank", f"Expected 'hackerrank', got '{result.domain}'"
    assert result.request_type in ("faq", "assessment"), (
        f"Expected faq or assessment, got '{result.request_type}'"
    )
    assert 0.0 <= result.confidence <= 1.0


# ---------------------------------------------------------------------------
# 2. test_classifier_visa_fraud
# ---------------------------------------------------------------------------


@patch("agent.classifier._client")
def test_classifier_visa_fraud(mock_client):
    """Classifier identifies Visa fraud tickets correctly."""
    mock_client.chat.completions.create.return_value = _make_gemini_response({
        "domain":       "visa",
        "request_type": "fraud",
        "product_area": "transaction",
        "confidence":   0.97,
    })

    from agent.classifier import classify

    ticket = "There is an unauthorized transaction on my Visa card I did not make"
    result = classify(ticket)

    assert result.domain == "visa", f"Expected 'visa', got '{result.domain}'"
    assert result.request_type == "fraud", (
        f"Expected 'fraud', got '{result.request_type}'"
    )
    assert result.confidence >= 0.5


# ---------------------------------------------------------------------------
# 3. test_safety_visa_fraud_always_escalates
# ---------------------------------------------------------------------------


def test_safety_visa_fraud_always_escalates(visa_doc):
    """Rule 1: Visa fraud always escalates regardless of retrieved docs."""
    classification = Classification(
        domain="visa",
        request_type="fraud",
        product_area="transaction",
        confidence=0.95,
    )
    decision = safety_check("unauthorized charge on my card", classification, [visa_doc])

    assert decision.should_escalate is True
    assert "fraud" in decision.reason.lower()


# ---------------------------------------------------------------------------
# 4. test_safety_no_docs_escalates
# ---------------------------------------------------------------------------


def test_safety_no_docs_escalates():
    """Rule 6: No retrieved docs → always escalate (no grounded answer)."""
    classification = Classification(
        domain="hackerrank",
        request_type="faq",
        product_area="screen",
        confidence=0.85,
    )
    decision = safety_check("How do I create a test?", classification, retrieved_docs=[])

    assert decision.should_escalate is True
    assert "documentation" in decision.reason.lower()


# ---------------------------------------------------------------------------
# 5. test_safety_faq_does_not_escalate
# ---------------------------------------------------------------------------


def test_safety_faq_does_not_escalate(mock_doc):
    """Normal FAQ with docs and high confidence should NOT escalate."""
    classification = Classification(
        domain="hackerrank",
        request_type="faq",
        product_area="assessments",
        confidence=0.9,
    )
    decision = safety_check("how do I create a test", classification, [mock_doc])

    assert decision.should_escalate is False
    assert decision.reason == ""


# ---------------------------------------------------------------------------
# 6. test_retriever_returns_relevant_docs
# ---------------------------------------------------------------------------


def test_retriever_returns_relevant_docs(small_index):
    """BM25 retriever returns the most relevant doc first for a targeted query."""
    index, docs = small_index

    # Query clearly targeting the HackerRank "invite candidates" doc
    results = search("invite candidates coding test HackerRank", index, top_k=3)

    assert len(results) > 0, "Expected at least one result"
    top_doc = results[0]
    assert top_doc.doc_id == "hr1", (
        f"Expected 'hr1' as top result, got '{top_doc.doc_id}' ({top_doc.title})"
    )

    # Domain-scoped search should restrict results
    visa_results = search("stolen card visa block", index, domain="visa", top_k=3)
    assert all(d.domain == "visa" for d in visa_results), (
        "Domain-scoped search returned non-visa docs"
    )


def test_retriever_domain_scoping(small_index):
    """Domain filter restricts results to the requested domain only."""
    index, _ = small_index

    claude_results = search("install app", index, domain="claude", top_k=5)
    for doc in claude_results:
        assert doc.domain == "claude", (
            f"Domain filter leak: expected 'claude', got '{doc.domain}'"
        )


def test_retriever_empty_query(small_index):
    """Empty query returns an empty result list without crashing."""
    index, _ = small_index
    results = search("", index)
    assert results == []


# ---------------------------------------------------------------------------
# 7. test_full_pipeline_smoke
# ---------------------------------------------------------------------------


@patch("agent.classifier._client")
@patch("agent.responder._client")
def test_full_pipeline_smoke(mock_responder_client, mock_classifier_client, mock_doc):
    """Full pipeline produces a valid AgentResponse for a normal FAQ ticket."""
    # Mock classifier Groq call
    mock_classifier_client.chat.completions.create.return_value = _make_gemini_response({
        "domain":       "hackerrank",
        "request_type": "faq",
        "product_area": "screen",
        "confidence":   0.88,
    })

    # Mock responder Groq call (plain text response)
    mock_responder_client.chat.completions.create.return_value = _make_text_response(
        "To invite candidates, go to the Tests tab and click Invite."
    )

    # Run pipeline
    from agent.classifier import classify
    from agent.responder import generate_escalation, generate_reply
    from corpus.loader import build_index

    ticket = "How do I invite candidates to a HackerRank coding test?"

    # Build tiny index with the mock_doc fixture
    index = build_index([mock_doc])

    # a. Classify
    classification = classify(ticket)
    assert classification.domain == "hackerrank"

    # b. Retrieve
    retrieved = search(ticket, index, domain=classification.domain, top_k=3)

    # c. Safety
    decision = safety_check(ticket, classification, retrieved)

    # d. Respond
    if decision.should_escalate:
        response = generate_escalation(ticket, decision)
    else:
        response = generate_reply(ticket, classification, retrieved)

    # Assertions on the output shape
    assert response.action in ("reply", "escalate"), (
        f"Unexpected action: '{response.action}'"
    )
    assert isinstance(response.response, str) and len(response.response) > 0, (
        "response.response must be a non-empty string"
    )
    assert isinstance(response.sources, list), "sources must be a list"


# ---------------------------------------------------------------------------
# Additional safety rule coverage
# ---------------------------------------------------------------------------


def test_safety_billing_dispute_escalates(mock_doc):
    """Rule 2: Visa domain + dispute keyword in text escalates.

    The rule fires on domain=visa + billing keyword regardless of classifier
    request_type, so the test uses domain=visa to match the implemented rule.
    """
    clf = Classification("visa", "product_issue", "transactions", 0.88)
    decision = safety_check("I want to dispute this charge on my Visa card", clf, [mock_doc])
    assert decision.should_escalate is True
    assert "billing" in decision.reason.lower()


def test_safety_account_hacked_escalates(mock_doc):
    """Rule 3: account_access + 'hacked' keyword escalates."""
    clf = Classification("claude", "account_access", "account-management", 0.85)
    decision = safety_check("My account was hacked, I cannot login", clf, [mock_doc])
    assert decision.should_escalate is True
    assert "compromise" in decision.reason.lower()


def test_safety_legal_language_escalates(mock_doc):
    """Rule 5: Legal trigger word anywhere in ticket escalates."""
    clf = Classification("hackerrank", "other", "general", 0.75)
    decision = safety_check("I am considering a lawsuit against your company", clf, [mock_doc])
    assert decision.should_escalate is True
    assert "legal" in decision.reason.lower()


def test_safety_low_confidence_escalates(mock_doc):
    """Rule 7: Confidence < 0.4 escalates regardless of topic."""
    clf = Classification("hackerrank", "faq", "general", 0.35)
    decision = safety_check("Something is not working", clf, [mock_doc])
    assert decision.should_escalate is True
    assert "confidence" in decision.reason.lower()


# ---------------------------------------------------------------------------
# Classifier fallback behaviour
# ---------------------------------------------------------------------------


@patch("agent.classifier._client")
def test_classifier_returns_fallback_on_api_error(mock_client):
    """Classifier returns the fallback Classification when Groq raises."""
    mock_client.chat.completions.create.side_effect = Exception("API unavailable")

    from agent.classifier import classify, _FALLBACK

    result = classify("some ticket text")

    assert result.domain == _FALLBACK.domain
    assert result.request_type == _FALLBACK.request_type
    assert result.confidence == 0.0


@patch("agent.classifier._client")
def test_classifier_empty_input_returns_fallback(mock_client):
    """Empty ticket text returns fallback without calling the model."""
    from agent.classifier import classify, _FALLBACK

    result = classify("")

    mock_client.chat.completions.create.assert_not_called()
    assert result.domain == _FALLBACK.domain


# ---------------------------------------------------------------------------
# Responder escalation (no Gemini call)
# ---------------------------------------------------------------------------


def test_generate_escalation_no_api_call():
    """generate_escalation() never calls Gemini and embeds the reason."""
    from agent.responder import generate_escalation
    from agent.safety import SafetyDecision

    sd = SafetyDecision(True, "Fraud reports must be handled by a human agent immediately")

    with patch("agent.responder._client") as mock_client:
        response = generate_escalation("stolen card", sd)
        mock_client.chat.completions.create.assert_not_called()

    assert response.action == "escalate"
    assert "Fraud reports" in response.response
    assert response.sources == []
