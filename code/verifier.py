"""Post-LLM citation verification: every claim should map to a chunk."""
from __future__ import annotations

import re

from schemas import ChunkDoc, LLMOutput

_SENT = re.compile(r"(?<=[.!?])\s+")
_WORD = re.compile(r"[a-z0-9][a-z0-9'-]*")
_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "for", "from",
    "has", "have", "if", "in", "into", "is", "it", "its", "of", "on", "or",
    "that", "the", "their", "this", "to", "was", "were", "with", "you",
    "your",
}


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENT.split(text.strip()) if s.strip()]


def _ngrams(s: str, n: int = 5) -> set[str]:
    toks = re.findall(r"\w+", s.lower())
    return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}


def _content_tokens(s: str) -> set[str]:
    return {
        t for t in _WORD.findall(s.lower())
        if len(t) > 2 and t not in _STOPWORDS
    }


def _sentence_supported(sentence: str, corpus_ngrams: set[str],
                        corpus_tokens: set[str]) -> bool:
    sg = _ngrams(sentence, n=5)
    if sg and sg & corpus_ngrams:
        return True

    sent_tokens = _content_tokens(sentence)
    if len(sent_tokens) <= 2:
        return True
    overlap = sent_tokens & corpus_tokens
    if len(overlap) >= 4:
        return True
    return len(overlap) / max(len(sent_tokens), 1) >= 0.45


def verify(out: LLMOutput, retrieved: list[ChunkDoc]) -> LLMOutput:
    if out.status != "replied":
        return out
    if not retrieved:
        return out
    retrieved_ids = {c.chunk_id for c in retrieved}
    out.citations = [cid for cid in out.citations if cid in retrieved_ids]
    cited_ids = set(out.citations)
    cited_chunks = [c for c in retrieved if c.chunk_id in cited_ids] or retrieved
    corpus_ngrams: set[str] = set()
    corpus_tokens: set[str] = set()
    for c in cited_chunks:
        corpus_ngrams |= _ngrams(c.text, n=5)
        corpus_tokens |= _content_tokens(c.text)

    sents = _sentences(out.response)
    if not sents:
        return out
    kept: list[str] = []
    for s in sents:
        if _sentence_supported(s, corpus_ngrams, corpus_tokens):
            kept.append(s)
    if not kept:
        out.status = "escalated"
        out.response = "Escalate to a human."
        out.justification = (out.justification + " | verifier: no sentence "
                             "supported by retrieved corpus").strip()
        return out
    if len(kept) < len(sents):
        out.response = " ".join(kept)
    return out
