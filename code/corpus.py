"""Walk data/ tree, chunk markdown into ChunkDoc records."""
from __future__ import annotations

import re
from pathlib import Path

from schemas import ChunkDoc

COMPANY_DIR = {"HackerRank": "hackerrank", "Claude": "claude", "Visa": "visa"}
APPROX_CHARS_PER_TOKEN = 4


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip()
    return text


def _chunk(text: str, target_chars: int, overlap: int) -> list[str]:
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if not text:
        return []
    if len(text) <= target_chars:
        return [text]
    paras = text.split("\n\n")
    chunks: list[str] = []
    buf = ""
    for p in paras:
        if not buf:
            buf = p
        elif len(buf) + 2 + len(p) <= target_chars:
            buf = f"{buf}\n\n{p}"
        else:
            chunks.append(buf)
            tail = buf[-overlap:] if overlap and len(buf) > overlap else ""
            buf = f"{tail}\n\n{p}" if tail else p
    if buf:
        chunks.append(buf)
    return chunks


def load_corpus(
    data_dir: Path,
    chunk_size_tokens: int = 400,
    overlap_chars: int = 80,
) -> list[ChunkDoc]:
    target_chars = chunk_size_tokens * APPROX_CHARS_PER_TOKEN
    out: list[ChunkDoc] = []
    for company, sub in COMPANY_DIR.items():
        root = data_dir / sub
        if not root.exists():
            continue
        for md_path in sorted(root.rglob("*.md")):
            try:
                raw = md_path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            text = _strip_frontmatter(raw)
            rel = md_path.relative_to(data_dir)
            parts = rel.parts
            product_area = parts[1] if len(parts) >= 3 else "general"
            chunks = _chunk(text, target_chars, overlap_chars)
            for i, ch in enumerate(chunks):
                cid = f"{company}:{rel.as_posix()}:{i:03d}"
                out.append(ChunkDoc(
                    chunk_id=cid,
                    company=company,
                    product_area=product_area,
                    text=ch,
                    source_path=str(rel),
                ))
    return out


def build_company_product_areas(chunks: list[ChunkDoc]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for c in chunks:
        out.setdefault(c.company, set()).add(c.product_area)
    return out
