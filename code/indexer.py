"""Offline corpus indexer.

Builds a hybrid retrieval index over ``data/{hackerrank,claude,visa}/``.
Persists chunks.parquet, faiss.index, bm25.pkl, manifest.json.

PRD references: FR-020, FR-024, NFR-001.
Architecture references: section 3.5, section 8.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import pickle
import random
import re
import sys
from pathlib import Path
from typing import Iterable

import numpy as np

# Determinism paranoia (NFR-001 / Architecture §8).
random.seed(0)
np.random.seed(0)
os.environ.setdefault("PYTHONHASHSEED", "0")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


# ---------- public API -----------------------------------------------------

EMBEDDING_MODEL_ID = "BAAI/bge-small-en-v1.5"
EMBEDDING_DIM = 384
CHUNK_SIZE = 600
CHUNK_OVERLAP = 80
MIN_CHUNK_CHARS = 30
DOMAINS = ("hackerrank", "claude", "visa")

# Top-level table-of-contents files we always skip (Architecture §3.5).
SKIP_TOPLEVEL_INDEX = {
    Path("hackerrank") / "index.md",
    Path("claude") / "index.md",
    Path("visa") / "index.md",
}

# Deterministic word tokenizer for BM25.
_WORD_RE = re.compile(r"[A-Za-z0-9]+")


def _tokenize(text: str) -> list[str]:
    return _WORD_RE.findall(text.lower())


def _sha256_of_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def _infer_domain(rel_path: Path) -> str:
    parts = rel_path.parts
    if not parts:
        raise ValueError(f"Empty rel path: {rel_path!r}")
    domain = parts[0]
    if domain not in DOMAINS:
        raise ValueError(
            f"Unknown domain {domain!r} for path {rel_path!r}; "
            f"expected one of {DOMAINS}"
        )
    return domain


def _walk_corpus(corpus_root: Path) -> list[Path]:
    """Sorted .md files in corpus_root, with the three top-level index.md skipped."""
    files = sorted(corpus_root.rglob("*.md"))
    out: list[Path] = []
    for p in files:
        rel = p.relative_to(corpus_root)
        if rel in SKIP_TOPLEVEL_INDEX:
            continue
        out.append(p)
    return out


def _parse_frontmatter(path: Path) -> tuple[dict, str]:
    """Return (metadata_dict, body_text)."""
    import frontmatter  # python-frontmatter package

    with path.open("r", encoding="utf-8") as f:
        post = frontmatter.load(f)
    meta = dict(post.metadata) if post.metadata else {}
    body = post.content or ""
    return meta, body


def _chunk_body(body: str) -> list[tuple[str, int, int]]:
    """Markdown-header split + recursive char split.

    Returns list of (chunk_text, char_start, char_end) where char_* are
    offsets into the original *body* string. Offsets are computed
    deterministically by walking through the body sequentially.
    """
    # Defensive: avoid the heavy splitter on trivially-empty bodies.
    if not body or not body.strip():
        return []

    from langchain_text_splitters import (
        MarkdownHeaderTextSplitter,
        RecursiveCharacterTextSplitter,
    )

    headers_to_split_on = [
        ("#", "h1"),
        ("##", "h2"),
        ("###", "h3"),
    ]
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False,
    )
    try:
        header_docs = md_splitter.split_text(body)
    except Exception:
        # Some bodies have no headers — fall back to single block.
        header_docs = []

    if not header_docs:
        # No headers found: treat the whole body as one block.
        blocks = [body]
    else:
        blocks = [d.page_content for d in header_docs]

    char_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )

    chunks: list[str] = []
    for block in blocks:
        sub = char_splitter.split_text(block)
        if sub:
            chunks.extend(sub)
        elif block.strip():
            chunks.append(block)

    # Compute char_start/char_end. The MarkdownHeaderTextSplitter
    # normalizes whitespace, which makes a literal body.find(chunk) fail in
    # general. We therefore compute offsets in two passes:
    #   1. Try exact substring search anchored at a moving cursor.
    #   2. Fall back to a deterministic synthetic offset based on the chunk's
    #      position in the sequential output: char_start = sum(prior chunk
    #      lens) - (i * CHUNK_OVERLAP), char_end = char_start + len(chunk).
    # The synthetic offsets are deterministic across runs (pure functions of
    # the splitter output) so chunk_id stability is preserved.
    out: list[tuple[str, int, int]] = []
    cursor = 0
    synth_cursor = 0
    for chunk in chunks:
        if not chunk or len(chunk) < MIN_CHUNK_CHARS:
            continue
        idx = body.find(chunk, cursor)
        if idx < 0:
            idx = body.find(chunk)
        if idx >= 0:
            char_start = idx
            char_end = idx + len(chunk)
            cursor = max(char_start + max(1, len(chunk) - CHUNK_OVERLAP), cursor + 1)
        else:
            # Synthetic deterministic offset: monotonic, derived from
            # accumulated chunk length minus overlap.
            char_start = synth_cursor
            char_end = synth_cursor + len(chunk)
        out.append((chunk, char_start, char_end))
        synth_cursor += max(1, len(chunk) - CHUNK_OVERLAP)
    return out


def _chunk_id(file_rel_posix: str, char_start: int, char_end: int) -> str:
    raw = f"{file_rel_posix}|{char_start}|{char_end}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def _manifest_corpus_files(corpus_root: Path, files: Iterable[Path]) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in files:
        rel = p.relative_to(corpus_root).as_posix()
        out[rel] = _sha256_of_path(p)
    return dict(sorted(out.items()))


def _existing_manifest(out_dir: Path) -> dict | None:
    manifest_path = out_dir / "manifest.json"
    if not manifest_path.exists():
        return None
    try:
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return None


def _build_corpus_records(
    corpus_root: Path, files: list[Path]
) -> list[dict]:
    """Walk + chunk every file. No embedding here — pure CPU work."""
    records: list[dict] = []
    for p in files:
        rel = p.relative_to(corpus_root)
        rel_posix = rel.as_posix()
        try:
            meta, body = _parse_frontmatter(p)
        except Exception as exc:  # malformed YAML — skip with warning
            print(f"[indexer] WARN failed to parse {rel_posix}: {exc}", file=sys.stderr)
            continue
        if not body or not body.strip():
            continue
        domain = _infer_domain(rel)
        title = str(meta.get("title", "")) if meta else ""
        breadcrumbs_raw = meta.get("breadcrumbs") if meta else None
        if isinstance(breadcrumbs_raw, list):
            breadcrumbs = [str(b) for b in breadcrumbs_raw]
        else:
            # Derive from path parts as fallback.
            breadcrumbs = [seg for seg in rel.parts[:-1]]

        for text, char_start, char_end in _chunk_body(body):
            cid = _chunk_id(rel_posix, char_start, char_end)
            records.append(
                {
                    "chunk_id": cid,
                    "file_path": rel_posix,
                    "domain": domain,
                    "breadcrumbs": breadcrumbs,
                    "title": title,
                    "text": text,
                    "char_start": char_start,
                    "char_end": char_end,
                }
            )
    # Sort by chunk_id lexicographically for deterministic row order.
    records.sort(key=lambda r: r["chunk_id"])
    return records


def _embed_texts(texts: list[str]) -> np.ndarray:
    """Embed with bge-small-en-v1.5; deterministic CPU inference."""
    import torch
    from sentence_transformers import SentenceTransformer

    try:
        torch.use_deterministic_algorithms(True)
    except Exception:
        # Some torch builds raise if certain ops aren't deterministic; we
        # still set the flag where we can.
        pass
    torch.manual_seed(0)
    torch.set_num_threads(1)

    model = SentenceTransformer(EMBEDDING_MODEL_ID)
    embeds = model.encode(
        texts,
        batch_size=64,
        normalize_embeddings=True,
        show_progress_bar=False,
        convert_to_numpy=True,
    )
    arr = np.asarray(embeds, dtype=np.float32)
    if arr.ndim != 2 or arr.shape[1] != EMBEDDING_DIM:
        raise RuntimeError(
            f"Embedding shape {arr.shape} != expected (N, {EMBEDDING_DIM})"
        )
    return arr


def _persist(
    out_dir: Path,
    records: list[dict],
    embeds: np.ndarray,
    corpus_files: dict[str, str],
) -> dict:
    import faiss
    import pyarrow as pa
    import pyarrow.parquet as pq
    from rank_bm25 import BM25Okapi

    out_dir.mkdir(parents=True, exist_ok=True)

    # chunks.parquet — column-major arrays in record order (already sorted).
    table = pa.table(
        {
            "chunk_id": [r["chunk_id"] for r in records],
            "file_path": [r["file_path"] for r in records],
            "domain": [r["domain"] for r in records],
            "breadcrumbs": [r["breadcrumbs"] for r in records],
            "title": [r["title"] for r in records],
            "text": [r["text"] for r in records],
            "char_start": [r["char_start"] for r in records],
            "char_end": [r["char_end"] for r in records],
        }
    )
    pq.write_table(table, out_dir / "chunks.parquet")

    # faiss.index — IndexFlatIP over normalized vectors.
    index = faiss.IndexFlatIP(EMBEDDING_DIM)
    if len(records) > 0:
        index.add(embeds)
    faiss.write_index(index, str(out_dir / "faiss.index"))

    # bm25.pkl — pickled BM25Okapi over deterministic-tokenized corpus.
    tokenized = [_tokenize(r["text"]) for r in records]
    if not tokenized:
        # BM25Okapi crashes on empty corpus; persist a sentinel.
        bm25 = None
    else:
        bm25 = BM25Okapi(tokenized)
    with (out_dir / "bm25.pkl").open("wb") as f:
        pickle.dump({"bm25": bm25, "tokenized_lengths": [len(t) for t in tokenized]}, f)

    manifest = {
        "corpus_files": corpus_files,
        "embedding_model": EMBEDDING_MODEL_ID,
        "chunk_count": len(records),
        "build_timestamp": _dt.datetime.now(_dt.timezone.utc).isoformat(),
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8"
    )
    return manifest


def build_index(corpus_root: Path, out_dir: Path, force: bool = False) -> dict:
    """Walk corpus, chunk, embed, persist artifacts. Idempotent.

    If the existing manifest matches the current corpus SHA fingerprint and
    embedding model, the build is skipped (returns the existing manifest).
    Pass ``force=True`` to bypass the cache.

    Returns the manifest dict.
    """
    corpus_root = Path(corpus_root)
    out_dir = Path(out_dir)

    files = _walk_corpus(corpus_root)
    corpus_files = _manifest_corpus_files(corpus_root, files)

    existing = _existing_manifest(out_dir) if not force else None
    if (
        existing is not None
        and existing.get("embedding_model") == EMBEDDING_MODEL_ID
        and existing.get("corpus_files") == corpus_files
    ):
        return existing

    records = _build_corpus_records(corpus_root, files)
    if records:
        embeds = _embed_texts([r["text"] for r in records])
    else:
        embeds = np.zeros((0, EMBEDDING_DIM), dtype=np.float32)

    return _persist(out_dir, records, embeds, corpus_files)


# ---------- CLI ------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="python code/indexer.py",
        description="Build the hybrid retrieval index over data/.",
    )
    repo_root = Path(__file__).resolve().parent.parent
    parser.add_argument(
        "--rebuild",
        action="store_true",
        help="Force rebuild even if manifest matches.",
    )
    parser.add_argument(
        "--corpus-root",
        type=Path,
        default=repo_root / "data",
        help="Root directory of the corpus (default: <repo>/data).",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=repo_root / "code" / "index",
        help="Output directory for index artifacts (default: <repo>/code/index).",
    )
    args = parser.parse_args()

    print(
        f"[indexer] corpus_root={args.corpus_root} "
        f"out_dir={args.out_dir} rebuild={args.rebuild}"
    )
    manifest = build_index(args.corpus_root, args.out_dir, force=args.rebuild)
    print(
        f"[indexer] done: {manifest['chunk_count']} chunks across "
        f"{len(manifest['corpus_files'])} files; model={manifest['embedding_model']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
