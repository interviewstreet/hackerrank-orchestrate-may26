"""
responder.py — Support ticket responder using rotating Gemini API keys.

Responsible for:
  - Building grounded prompts from retrieved documents
  - Calling Gemini 2.0 Flash to generate replies
  - Hallucination checks
"""

import re
from dataclasses import dataclass, field
from typing import Optional
from agent.classifier import Classification
from agent.safety import SafetyDecision
from corpus import loader
from corpus.loader import Document
from utils.live_scraper import scrape_url
from utils.model_provider import call_llm

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_MODEL_NAME = "gemini-2.5-flash"

# ---------------------------------------------------------------------------
# Output data model
# ---------------------------------------------------------------------------

@dataclass
class AgentResponse:
    action: str
    response: str
    explanation: str = ""
    sources: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

_CORPUS_NOT_FOUND = (
    "I don't have enough information in our support documentation to answer this. "
    "Please contact our support team directly."
)

_MIN_OVERLAP_WORDS = 2  # More lenient for summarized responses

# Regex patterns for PII detection
_EMAIL_PATTERN = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
_PHONE_PATTERN = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"


def _find_perfect_link_heuristically(ticket_text: str, doc: Document) -> str:
    """Identify the best external link using deterministic keyword scoring."""
    # Use pre-indexed links if available, otherwise fallback to regex
    links = getattr(doc, "links", [])
    if not links:
        links = re.findall(r"https?://[^\s\)\>]+", doc.content)
    
    # Filter out the document's own URL (and variants)
    doc_base = doc.url.split('?')[0].split('#')[0].rstrip('/')
    other_links = []
    for url in links:
        url_base = url.split('?')[0].split('#')[0].rstrip('/')
        if url_base != doc_base:
            other_links.append(url)
    
    if not other_links:
        return doc.url

    # Scoring: overlap between ticket keywords and the URL path/slug
    keywords = set(re.findall(r"[a-z0-9]{3,}", ticket_text.lower()))
    best_link = other_links[0]
    max_score = -1

    for link in other_links:
        score = 0
        link_lower = link.lower()
        # Bonus for high-value technical domains
        if any(d in link_lower for d in ["aws.amazon.com", "claude.ai", "help.hackerrank.com", "visa.com"]):
            score += 2
        
        # Keyword matching in the URL slug
        for kw in keywords:
            if kw in link_lower:
                score += 1
        
        if score > max_score:
            max_score = score
            best_link = link

    return best_link


def _get_top_score(query: str, docs: list[Document]) -> float:
    """Helper to check the relative quality of search results (using word overlap)."""
    if not docs: return 0.0
    query_words = set(re.findall(r"[a-z0-9]+", query.lower()))
    doc_words = set(re.findall(r"[a-z0-9]+", docs[0].content.lower() + " " + docs[0].title.lower()))
    return len(query_words & doc_words)


def _check_hallucination(
    reply_text: str,
    retrieved_docs: list[Document],
) -> list[str]:
    """Flag response sentences with low lexical overlap or PII leaks."""
    corpus_words: set[str] = set()
    corpus_raw: str = ""
    for doc in retrieved_docs:
        lower_content = doc.content.lower()
        lower_title = doc.title.lower()
        lower_url = getattr(doc, "url", "").lower()
        corpus_words.update(re.findall(r"[a-z0-9]+", lower_content))
        corpus_words.update(re.findall(r"[a-z0-9]+", lower_title))
        corpus_words.update(re.findall(r"[a-z0-9]+", lower_url))
        corpus_raw += lower_content + " " + lower_title + " " + lower_url

    if not corpus_words:
        return []

    # 1. PII Check: Look for emails/phones in response that are NOT in the corpus
    response_emails = re.findall(_EMAIL_PATTERN, reply_text)
    response_phones = re.findall(_PHONE_PATTERN, reply_text)
    
    # Whitelist of trusted support domains
    trusted_domains = ["hackerrank.com", "anthropic.com", "claude.ai", "visa.com"]
    
    pii_violations = []
    for email in response_emails:
        is_trusted = any(domain in email.lower() for domain in trusted_domains)
        if not is_trusted and email.lower() not in corpus_raw:
            pii_violations.append(f"Unauthorized Email Leak: {email}")
            
    # Find all URLs in the reply text to cross-reference phone matches
    reply_urls = re.findall(r"https?://[^\s\>]+", reply_text)
    
    for phone in response_phones:
        # Ignore phones that are just Article IDs or AWS signatures embedded inside a URL
        is_in_url = any(phone in url for url in reply_urls)
        if is_in_url:
            continue
            
        # Normalize phone for check (rough)
        clean_phone = re.sub(r"\D", "", phone)
        if clean_phone not in re.sub(r"\D", "", corpus_raw):
            pii_violations.append(f"Unauthorized Phone Leak: {phone}")

    # 2. Lexical Overlap Check
    sentences = re.split(r"(?<=[.!?])\s+", reply_text.strip())
    flagged: list[str] = pii_violations

    for sentence in sentences:
        if len(sentence.strip()) < 25: # Slightly stricter limit
            continue
        sentence_words = set(re.findall(r"[a-z0-9]+", sentence.lower()))
        overlap = sentence_words & corpus_words
        if len(overlap) < _MIN_OVERLAP_WORDS:
            flagged.append(f"Low Overlap: {sentence.strip()}")

    return flagged


def _build_context(docs: list[Document]) -> tuple[str, list[str]]:
    """Format retrieved documents into a numbered context block."""
    blocks: list[str] = []
    source_urls: list[str] = []

    for i, doc in enumerate(docs, start=1):
        # Massive window for Azure OpenAI context
        content_snippet = doc.content[:20000]
        if len(doc.content) > 20000:
            content_snippet += "..."

        blocks.append(
            f"=== Support Document {i} ===\n"
            f"Title: {doc.title}\n"
            f"URL: {doc.url}\n"
            f"Content: {content_snippet}"
        )

        if doc.url and doc.url not in source_urls:
            source_urls.append(doc.url)

    return "\n\n".join(blocks), source_urls


def _build_system_prompt(domain: str) -> str:
    """Build the system instruction that constrains the model to the corpus."""
    domain_label = domain.title() if domain != "unknown" else "the product"
    return (
        f"You are a professional, expert Senior Support Engineer for {domain_label}.\n\n"
        "CONTEXT:\n"
        "Below are support documents. These ARE the source of truth.\n\n"
        "STRICT INSTRUCTIONS:\n"
        "1. Address ONLY the customer's core problem. If they ask for a refund, provide the policy and contact info ONLY. Do NOT include 'how-to' guides for unrelated features.\n"
        "2. If a document mentions a contact email (e.g., help@hackerrank.com), you MUST include it.\n"
        "3. Do NOT use [[NO_ANSWER]] if any document mentions the customer's topic, even if the instructions are brief.\n"
        "4. Copy all links and emails VERBATIM from the source.\n"
        "5. Be concise and professional. Avoid extra filler or 'related tips'.\n"
        "6. Mention the source URL or Document Title when providing steps.\n"
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def _generate_reply_with_retry(
    ticket_text: str,
    classification: Classification,
    retrieved_docs: list[Document],
) -> str:
    context, _ = _build_context(retrieved_docs)
    system_prompt = _build_system_prompt(classification.domain)
    user_content = (
        f"Customer ticket:\n{ticket_text}\n\n"
        f"Support documents:\n{context}\n\n"
        "Provide a helpful, concise response based strictly on the above documents."
    )

    # DEBUG: See what we are sending to the AI
    print(f"--- DEBUG PROMPT for {classification.domain} ---\n{user_content}\n--- END DEBUG ---")

    reply = call_llm(
        system_prompt=system_prompt,
        user_content=user_content,
        json_mode=False
    )
    
    if "[[NO_ANSWER]]" in reply:
        return _CORPUS_NOT_FOUND
    return reply


def generate_reply(
    ticket_text: str,
    classification: Classification,
    retrieved_docs: Optional[list[Document]],
    index: dict,
) -> AgentResponse:
    """Generate a corpus-grounded reply using multi-provider cascade."""
    
    # SMART PRUNING: Isolate high-priority docs or cap context for batch stability.
    priority_docs = [d for d in retrieved_docs if getattr(d, "score", 0) >= 99999.0]
    if priority_docs:
        print(f"  [responder] Priority docs detected. Pruning context to {len(priority_docs)} source(s).")
        retrieved_docs = priority_docs
    elif len(retrieved_docs) > 10:
        retrieved_docs = retrieved_docs[:10]

    # Stage 1: Identify domain and perform Targeted Search (if docs not provided)
    if not retrieved_docs:
        # If domain is 'unknown', we go straight to Global Search
        target_domain = classification.domain if classification.domain != "unknown" else None
        
        # Use high top_k to leverage Azure's large context window
        retrieved_docs = loader.search(
            ticket_text, 
            index, 
            domain=target_domain, 
            top_k=15 if target_domain else 10
        )

        # If targeted search returned poor results, try global
        if target_domain and (not retrieved_docs or _get_top_score(ticket_text, retrieved_docs) < 3.0):
            print(f"[responder] Targeted search in '{target_domain}' was poor. Falling back to Global Search.")
            global_docs = loader.search(ticket_text, index, domain=None, top_k=12)
            retrieved_docs = global_docs
    
    if not retrieved_docs:
        return AgentResponse(action="reply", response=_CORPUS_NOT_FOUND, sources=[])

    # Stage 3: Live Document Refresh & Link Following
    # Protect priority docs: if a doc is already a perfect match (99999), don't risk hijacking it with links.
    for i, doc in enumerate(retrieved_docs[:2]):
        if getattr(doc, "score", 0) >= 99999.0:
            print(f"  [responder] Doc '{doc.title}' is priority-locked. Skipping link-following.")
            continue

        target_url = _find_perfect_link_heuristically(ticket_text, doc)
        if target_url:
            print(f"  [Live] Following link: {target_url}")
            fresh_content = scrape_url(target_url)
            if fresh_content:
                # APPEND fresh content, never overwrite the original policy grounding!
                doc.content = f"{doc.content}\n\n--- FRESH DATA FROM {target_url} ---\n{fresh_content}"
                # Update URL so the responder knows the final source
                doc.url = target_url

    _, source_urls = _build_context(retrieved_docs)

    try:
        reply_text = _generate_reply_with_retry(ticket_text, classification, retrieved_docs)
        
        explanation = (
            f"Classified as {classification.product_area} for {classification.domain}. "
            f"Grounded in {len(retrieved_docs)} priority source(s)."
        )

        # Internal check for empty/nonsensical replies
        if len(reply_text) < 10:
            return AgentResponse(action="reply", response=_CORPUS_NOT_FOUND, explanation="Retrieved docs were insufficient for grounding.", sources=source_urls)

        flagged = _check_hallucination(reply_text, retrieved_docs)
        if flagged:
            print(f"[responder] HALLUCINATION/PII WARNING: {len(flagged)} violation(s) flagged.")
            for f in flagged:
                print(f"  - {f}")
            # If PII leak is detected, we fallback to a safe message
            if any("Leak" in f for f in flagged):
                return AgentResponse(action="reply", response=_CORPUS_NOT_FOUND, explanation="Hallucination/PII detected during grounding check.", sources=source_urls)

        return AgentResponse(action="reply", response=reply_text, explanation=explanation, sources=source_urls)

    except Exception as exc:  # noqa: BLE001
        print(f"[responder] ERROR after retries: {exc}")
        return AgentResponse(action="reply", response=_CORPUS_NOT_FOUND, explanation=f"LLM Error: {str(exc)}", sources=source_urls)


def generate_escalation(
    ticket_text: str,  # noqa: ARG001
    safety_decision: SafetyDecision,
) -> AgentResponse:
    """Build a professional escalation notice WITHOUT calling the API."""
    message = (
        "Thank you for reaching out. Your request has been escalated to our "
        f"specialized support team because: {safety_decision.reason}. "
        "A human agent will contact you shortly."
    )
    return AgentResponse(action="escalate", response=message, sources=[])
