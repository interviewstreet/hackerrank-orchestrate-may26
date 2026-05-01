"""Load markdown support articles into retrievable chunks."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-zA-Z0-9]+", text.lower())


def _split_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    raw = raw.lstrip("\ufeff")
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm if isinstance(fm, dict) else {}, parts[2].strip()


def _product_hint_from_path(company: str, rel: Path) -> str:
    parts = rel.parts
    if not parts:
        return "general"
    # data/<company>/<segment>/...
    if len(parts) >= 2:
        seg = parts[1]
        return seg.replace(" ", "_").replace("-", "_").lower()
    return parts[0].lower()


def _chunk_body(body: str, max_chars: int = 2200) -> list[str]:
    body = body.strip()
    if len(body) <= max_chars:
        return [body]
    chunks: list[str] = []
    paras = re.split(r"\n\n+", body)
    buf = ""
    for p in paras:
        if len(buf) + len(p) + 2 <= max_chars:
            buf = f"{buf}\n\n{p}".strip() if buf else p
        else:
            if buf:
                chunks.append(buf)
            if len(p) <= max_chars:
                buf = p
            else:
                for i in range(0, len(p), max_chars):
                    chunks.append(p[i : i + max_chars])
                buf = ""
    if buf:
        chunks.append(buf)
    return chunks


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    company: str
    path: str
    title: str
    product_hint: str
    breadcrumbs: str
    text: str

    @property
    def lexical_text(self) -> str:
        return " ".join(
            [
                self.company,
                self.title,
                self.product_hint,
                self.breadcrumbs,
                self.text,
            ]
        )


def load_chunks(data_root: Path | None = None) -> list[Chunk]:
    root = data_root or (_repo_root() / "data")
    chunks: list[Chunk] = []
    for company in ("hackerrank", "claude", "visa"):
        base = root / company
        if not base.is_dir():
            continue
        for path in sorted(base.rglob("*.md")):
            rel = path.relative_to(base)
            raw = path.read_text(encoding="utf-8", errors="replace")
            fm, body = _split_frontmatter(raw)
            title = str(fm.get("title") or path.stem).strip()
            crumbs = fm.get("breadcrumbs")
            if isinstance(crumbs, list):
                breadcrumb_str = " > ".join(str(c) for c in crumbs)
            else:
                breadcrumb_str = ""
            hint = _product_hint_from_path(company, rel)
            for idx, piece in enumerate(_chunk_body(body)):
                cid = f"{company}:{rel.as_posix()}#{idx}"
                chunks.append(
                    Chunk(
                        chunk_id=cid,
                        company=company,
                        path=str(rel.as_posix()),
                        title=title,
                        product_hint=hint,
                        breadcrumbs=breadcrumb_str,
                        text=piece,
                    )
                )
    return chunks
