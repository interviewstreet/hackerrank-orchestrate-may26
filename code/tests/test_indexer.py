"""Tests for code/indexer.py — Iter 2 (Corpus Indexer).

PRD references: FR-020, FR-024, NFR-001.
Architecture references: section 3.5, section 8.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest

from indexer import build_index


FIXTURE_ROOT = Path(__file__).resolve().parent / "fixtures" / "mini_corpus"


def _copy_corpus(dst: Path) -> Path:
    """Copy the fixture mini-corpus into a tmp_path-rooted ``data/`` tree."""
    target = dst / "data"
    shutil.copytree(FIXTURE_ROOT, target)
    return target


def test_build_index_creates_artifacts(tmp_path: Path) -> None:
    corpus = _copy_corpus(tmp_path)
    out_dir = tmp_path / "index"
    manifest = build_index(corpus, out_dir, force=True)

    assert (out_dir / "chunks.parquet").exists()
    assert (out_dir / "faiss.index").exists()
    assert (out_dir / "bm25.pkl").exists()
    assert (out_dir / "manifest.json").exists()
    assert manifest["chunk_count"] >= 1
    assert manifest["embedding_model"] == "BAAI/bge-small-en-v1.5"


def test_build_index_deterministic_chunk_ids(tmp_path: Path) -> None:
    corpus = _copy_corpus(tmp_path)
    out_dir_a = tmp_path / "idx_a"
    out_dir_b = tmp_path / "idx_b"
    build_index(corpus, out_dir_a, force=True)
    build_index(corpus, out_dir_b, force=True)

    import pyarrow.parquet as pq

    chunks_a = pq.read_table(out_dir_a / "chunks.parquet").to_pandas()
    chunks_b = pq.read_table(out_dir_b / "chunks.parquet").to_pandas()

    assert list(chunks_a["chunk_id"]) == list(chunks_b["chunk_id"])
    assert list(chunks_a["text"]) == list(chunks_b["text"])
    assert list(chunks_a["file_path"]) == list(chunks_b["file_path"])


def test_build_index_skips_empty_files(tmp_path: Path) -> None:
    corpus = _copy_corpus(tmp_path)
    # Add a truly-empty file (no frontmatter, no body)
    (corpus / "hackerrank" / "truly-empty.md").write_text("", encoding="utf-8")

    out_dir = tmp_path / "index"
    manifest = build_index(corpus, out_dir, force=True)

    import pyarrow.parquet as pq

    chunks = pq.read_table(out_dir / "chunks.parquet").to_pandas()

    file_paths = set(chunks["file_path"].tolist())
    # Neither the frontmatter-only empty doc nor the truly-empty file should
    # have produced any chunks.
    for fp in file_paths:
        assert "empty-doc.md" not in fp
        assert "truly-empty.md" not in fp
    # The four content-bearing files should each contribute at least 1 chunk.
    assert manifest["chunk_count"] >= 4


def test_build_index_manifest_sha256_per_file(tmp_path: Path) -> None:
    corpus = _copy_corpus(tmp_path)
    out_dir = tmp_path / "index"
    build_index(corpus, out_dir, force=True)

    manifest = json.loads((out_dir / "manifest.json").read_text(encoding="utf-8"))

    corpus_files = manifest["corpus_files"]
    assert isinstance(corpus_files, dict)
    # Keys must be sorted lexicographically (determinism).
    keys = list(corpus_files.keys())
    assert keys == sorted(keys)
    # Every value is a 64-char lowercase hex SHA-256.
    for path, digest in corpus_files.items():
        assert isinstance(digest, str)
        assert len(digest) == 64
        assert all(c in "0123456789abcdef" for c in digest)
        # The path should be a string that ends in .md
        assert path.endswith(".md")


def test_build_index_rebuild_on_corpus_change(tmp_path: Path) -> None:
    corpus = _copy_corpus(tmp_path)
    out_dir = tmp_path / "index"
    manifest_a = build_index(corpus, out_dir, force=True)

    import pyarrow.parquet as pq

    chunks_a = pq.read_table(out_dir / "chunks.parquet").to_pandas()
    text_a = " ".join(chunks_a["text"].tolist())
    assert "DEFINITELYNOVELTOKEN" not in text_a

    # Mutate one file: insert a unique sentinel that must appear post-rebuild.
    target = corpus / "visa" / "visa-cancel-card.md"
    body = target.read_text(encoding="utf-8")
    body = body.rstrip() + "\n\nDEFINITELYNOVELTOKEN appears in this revision.\n"
    target.write_text(body, encoding="utf-8")

    # Call without force — auto-rebuild logic should detect the SHA mismatch.
    manifest_b = build_index(corpus, out_dir, force=False)

    chunks_b = pq.read_table(out_dir / "chunks.parquet").to_pandas()
    text_b = " ".join(chunks_b["text"].tolist())
    assert "DEFINITELYNOVELTOKEN" in text_b
    # Manifests must differ on the mutated file's SHA.
    rel = "visa/visa-cancel-card.md"
    assert manifest_a["corpus_files"][rel] != manifest_b["corpus_files"][rel]
