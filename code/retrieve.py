"""BM25 retrieval over corpus chunks."""

from __future__ import annotations

from collections import defaultdict

from rank_bm25 import BM25Okapi

from corpus import Chunk, _tokenize


class CorpusIndex:
    def __init__(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks
        tokenized = [_tokenize(c.lexical_text) for c in chunks]
        self._bm25 = BM25Okapi(tokenized)

    def query(self, q: str, top_k: int) -> list[tuple[Chunk, float]]:
        q_tokens = _tokenize(q)
        if not q_tokens:
            return [(c, 0.0) for c in self.chunks[:top_k]]
        scores = self._bm25.get_scores(q_tokens)
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
        out: list[tuple[Chunk, float]] = []
        for idx, score in ranked[:top_k]:
            out.append((self.chunks[idx], float(score)))
        return out


def build_company_indexes(all_chunks: list[Chunk]) -> dict[str | None, CorpusIndex]:
    by_company: dict[str, list[Chunk]] = defaultdict(list)
    for c in all_chunks:
        by_company[c.company].append(c)
    indexes: dict[str | None, CorpusIndex] = {None: CorpusIndex(all_chunks)}
    for company, cs in by_company.items():
        indexes[company] = CorpusIndex(cs)
    return indexes
