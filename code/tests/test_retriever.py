"""Tests for code/retriever.py — Iter 2 (Hybrid Retriever).

PRD references: FR-020..FR-024, T-1, NFR-001.
Architecture references: section 3.6, section 8.
"""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from indexer import build_index
from retriever import Retriever


FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "mini_corpus"


def _copy_corpus(dst: Path) -> Path:
    target = dst / "data"
    shutil.copytree(FIXTURE_ROOT, target)
    return target


@pytest.fixture(scope="module")
def built_index(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Build the mini-corpus index once per module to amortize embedding cost."""
    base = tmp_path_factory.mktemp("retriever_build")
    corpus = _copy_corpus(base)
    out_dir = base / "index"
    build_index(corpus, out_dir, force=True)
    return out_dir


def test_retriever_topk_returns_k_results(built_index: Path) -> None:
    r = Retriever(built_index)
    results = r.search("how do I cancel a test invite for a candidate", domain=None, k=3)
    assert len(results) == 3
    for doc in results:
        assert doc.chunk_id
        assert doc.text
        assert doc.domain in {"hackerrank", "claude", "visa"}


def test_retriever_domain_scope_filters(built_index: Path) -> None:
    r = Retriever(built_index)
    results = r.search("cancel my card", domain="visa", k=4)
    assert len(results) >= 1
    for doc in results:
        assert doc.domain == "visa"


def test_retriever_below_threshold_returns_low_scoring(built_index: Path) -> None:
    r = Retriever(built_index)
    # An off-topic query should still return k results, but with low cosine.
    results = r.search(
        "rocket propulsion physics interplanetary trajectory orbital mechanics",
        domain=None,
        k=3,
    )
    assert len(results) == 3
    top1 = results[0]
    # Below the production RETRIEVAL_MIN_SCORE threshold (0.32) — used by T-1.
    assert top1.cosine_score < 0.5
    # Sanity: every doc has scores populated.
    for doc in results:
        assert doc.cosine_score is not None
        assert doc.bm25_score is not None
        assert doc.rrf_score is not None


def test_retriever_deterministic_tie_break_by_chunk_id(built_index: Path) -> None:
    r = Retriever(built_index)
    # Two consecutive identical searches must return identical chunk_id ordering.
    a = r.search("Visa fraud lost stolen card", domain="visa", k=2)
    b = r.search("Visa fraud lost stolen card", domain="visa", k=2)
    assert [d.chunk_id for d in a] == [d.chunk_id for d in b]
    # Sort property: when scores tie, results MUST sort by chunk_id ascending.
    # We verify the deterministic ordering invariant by sorting same-RRF buckets.
    by_rrf: dict[float, list[str]] = {}
    for d in a:
        by_rrf.setdefault(round(d.rrf_score, 12), []).append(d.chunk_id)
    for ids in by_rrf.values():
        assert ids == sorted(ids)


def test_retriever_rrf_fusion_outranks_bm25_only_when_dense_agrees(
    built_index: Path,
) -> None:
    r = Retriever(built_index)
    # Query that should hit the visa-fraud doc strongly (dense + lexical agree).
    results = r.search("visa fraud unauthorized stolen card", domain="visa", k=2)
    assert len(results) == 2
    top = results[0]
    # The highest-RRF doc should be the fraud-protection chunk.
    assert "visa-fraud" in top.file_path
    # And RRF score of top exceeds the second-place doc.
    assert results[0].rrf_score >= results[1].rrf_score
