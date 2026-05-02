"""Hybrid (dense + BM25) retriever.

Loads index artifacts produced by indexer.py and serves top-K queries.

PRD references: FR-020..FR-024, T-1.
Architecture references: section 3.6, section 8.
"""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Optional

import numpy as np

from indexer import EMBEDDING_DIM, EMBEDDING_MODEL_ID, _tokenize
from schemas import RetrievedDoc

RRF_K = 60
DENSE_TOPN = 30
LEXICAL_TOPN = 30
ALLOWED_DOMAINS = {"hackerrank", "claude", "visa"}


class Retriever:
    """Loads cached index artifacts and answers top-K retrieval queries."""

    def __init__(self, index_dir: Path) -> None:
        import faiss
        import pyarrow.parquet as pq

        index_dir = Path(index_dir)
        if not index_dir.exists():
            raise FileNotFoundError(f"Index dir does not exist: {index_dir}")

        # chunks.parquet — load as a plain DataFrame.
        self.chunks = pq.read_table(index_dir / "chunks.parquet").to_pandas()
        # FAISS index.
        self.faiss = faiss.read_index(str(index_dir / "faiss.index"))
        if self.faiss.d != EMBEDDING_DIM:
            raise RuntimeError(
                f"FAISS index dim {self.faiss.d} != expected {EMBEDDING_DIM}"
            )
        # BM25 pickle (may be None on empty corpus).
        with (index_dir / "bm25.pkl").open("rb") as f:
            payload = pickle.load(f)
        self.bm25 = payload.get("bm25") if isinstance(payload, dict) else payload

        # Lazy embed model — created on first .search() call.
        self._embed_model = None

        # Domain-mask cache: maps domain -> np.ndarray of int row indices
        # (positions in self.chunks) for that domain.
        self._domain_indices: dict[str, np.ndarray] = {}
        domains = self.chunks["domain"].to_numpy()
        for d in ALLOWED_DOMAINS:
            self._domain_indices[d] = np.where(domains == d)[0]
        self._all_indices = np.arange(len(self.chunks))

    # ---------- internals --------------------------------------------------

    def _embed_query(self, query: str) -> np.ndarray:
        if self._embed_model is None:
            import torch
            from sentence_transformers import SentenceTransformer

            try:
                torch.use_deterministic_algorithms(True)
            except Exception:
                pass
            torch.manual_seed(0)
            torch.set_num_threads(1)
            self._embed_model = SentenceTransformer(EMBEDDING_MODEL_ID)

        vec = self._embed_model.encode(
            [query],
            normalize_embeddings=True,
            show_progress_bar=False,
            convert_to_numpy=True,
        )
        return np.asarray(vec, dtype=np.float32)

    def _candidate_indices(self, domain: Optional[str]) -> np.ndarray:
        if domain is not None and domain in ALLOWED_DOMAINS:
            return self._domain_indices[domain]
        return self._all_indices

    def _dense_search(
        self, qvec: np.ndarray, candidates: np.ndarray, top_n: int
    ) -> list[tuple[int, float]]:
        """Return [(row_index, cosine_score)] sorted by score desc, then row_index."""
        if candidates.size == 0:
            return []
        # Compute scores over candidates only by gathering vectors.
        # FAISS IndexFlatIP exposes reconstruct_n; we reconstruct all then mask.
        # This is fine for ~5000 chunks but if scaled up, switch to IDSelector.
        all_vecs = self.faiss.reconstruct_n(0, self.faiss.ntotal)
        cand_vecs = all_vecs[candidates]  # (M, D)
        sims = cand_vecs @ qvec[0]  # (M,)
        # Take top_n
        n = min(top_n, sims.shape[0])
        if n == 0:
            return []
        # argpartition for top-n then sort
        part_idx = np.argpartition(-sims, n - 1)[:n]
        part_idx = part_idx[np.argsort(-sims[part_idx], kind="stable")]
        return [(int(candidates[i]), float(sims[i])) for i in part_idx]

    def _bm25_search(
        self,
        query_tokens: list[str],
        candidates: np.ndarray,
        top_n: int,
    ) -> list[tuple[int, float]]:
        if self.bm25 is None or candidates.size == 0:
            return []
        # rank_bm25 scores all docs; we then mask.
        scores = self.bm25.get_scores(query_tokens)
        scores = np.asarray(scores, dtype=np.float64)
        cand_scores = scores[candidates]
        n = min(top_n, cand_scores.shape[0])
        if n == 0:
            return []
        part_idx = np.argpartition(-cand_scores, n - 1)[:n]
        part_idx = part_idx[np.argsort(-cand_scores[part_idx], kind="stable")]
        return [(int(candidates[i]), float(cand_scores[i])) for i in part_idx]

    # ---------- public -----------------------------------------------------

    def search(
        self,
        query: str,
        domain: str | None,
        k: int,
    ) -> list[RetrievedDoc]:
        """Embed the query, run hybrid RRF retrieval, return top-K docs."""
        if k <= 0:
            return []

        candidates = self._candidate_indices(domain)
        if candidates.size == 0:
            return []

        qvec = self._embed_query(query)
        qtok = _tokenize(query)

        dense = self._dense_search(qvec, candidates, DENSE_TOPN)
        lex = self._bm25_search(qtok, candidates, LEXICAL_TOPN)

        cosine_by_idx: dict[int, float] = {idx: score for idx, score in dense}
        bm25_by_idx: dict[int, float] = {idx: score for idx, score in lex}

        # RRF fusion across dense + lexical rankings.
        rrf_by_idx: dict[int, float] = {}
        for rank, (idx, _score) in enumerate(dense, start=1):
            rrf_by_idx[idx] = rrf_by_idx.get(idx, 0.0) + 1.0 / (RRF_K + rank)
        for rank, (idx, _score) in enumerate(lex, start=1):
            rrf_by_idx[idx] = rrf_by_idx.get(idx, 0.0) + 1.0 / (RRF_K + rank)

        if not rrf_by_idx:
            return []

        # Build (chunk_id, idx, rrf) and sort: rrf desc, chunk_id asc.
        chunk_ids = self.chunks["chunk_id"].to_numpy()
        triples = [
            (chunk_ids[idx], idx, rrf) for idx, rrf in rrf_by_idx.items()
        ]
        triples.sort(key=lambda t: (-t[2], t[0]))
        triples = triples[:k]

        out: list[RetrievedDoc] = []
        for chunk_id, idx, rrf in triples:
            row = self.chunks.iloc[idx]
            cosine = cosine_by_idx.get(idx, 0.0)
            bm25 = bm25_by_idx.get(idx, 0.0)
            breadcrumbs_raw = row["breadcrumbs"]
            if breadcrumbs_raw is None:
                breadcrumbs = []
            else:
                breadcrumbs = [str(b) for b in list(breadcrumbs_raw)]
            out.append(
                RetrievedDoc(
                    chunk_id=str(chunk_id),
                    file_path=str(row["file_path"]),
                    domain=str(row["domain"]),
                    breadcrumbs=breadcrumbs,
                    title=str(row["title"]) if row["title"] is not None else "",
                    text=str(row["text"]),
                    cosine_score=float(cosine),
                    bm25_score=float(bm25),
                    rrf_score=float(rrf),
                )
            )
        return out
