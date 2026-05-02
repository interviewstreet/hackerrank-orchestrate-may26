"""Post-LLM citation verification: every claim should map to a chunk."""
from __future__ import annotations

import re

from schemas import ChunkDoc, LLMOutput

_SENT = re.compile(r"(?<=[.!?])\s+")


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in _SENT.split(text.strip()) if s.strip()]


def _ngrams(s: str, n: int = 5) -> set[str]:
    toks = re.findall(r"\w+", s.lower())
    return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}


def verify(out: LLMOutput, retrieved: list[ChunkDoc]) -> LLMOutput:
    if out.status != "replied":
        return out
    if not retrieved:
        return out
    cited_ids = set(out.citations)
    cited_chunks = [c for c in retrieved if c.chunk_id in cited_ids] or retrieved
    corpus_ngrams: set[str] = set()
    for c in cited_chunks:
        corpus_ngrams |= _ngrams(c.text, n=5)

    sents = _sentences(out.response)
    if not sents:
        return out
    kept: list[str] = []
    for s in sents:
        sg = _ngrams(s, n=5)
        if not sg or sg & corpus_ngrams:
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
