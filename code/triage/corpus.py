from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from .models import CorpusDoc, RetrievalHit

TOKEN_RE = re.compile(r"[a-z0-9]+")
STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "how",
    "i",
    "in",
    "is",
    "it",
    "me",
    "my",
    "of",
    "on",
    "or",
    "please",
    "that",
    "the",
    "to",
    "we",
    "with",
    "you",
    "your",
}


def normalize_company(raw: str) -> str:
    name = (raw or "").strip().lower()
    if name in {"hackerrank", "claude", "visa"}:
        return name
    return "none"


def tokenize(text: str) -> List[str]:
    if not text:
        return []
    tokens = [t for t in TOKEN_RE.findall(text.lower()) if t and t not in STOP_WORDS]
    return tokens


def _parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 5 :]
    meta: Dict[str, str] = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def _first_heading(body: str) -> str:
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _extract_product_area(company: str, rel_parts: List[str], meta: Dict[str, str]) -> str:
    crumbs = meta.get("breadcrumbs", "")
    if crumbs:
        # basic YAML list lines are flattened by the parser; path-based fallback remains primary.
        pass

    if company == "hackerrank":
        return rel_parts[1] if len(rel_parts) > 1 else "general-help"
    if company == "claude":
        return rel_parts[1] if len(rel_parts) > 1 else "claude"
    if company == "visa":
        if "fraud" in "-".join(rel_parts):
            return "fraud-protection"
        if "dispute" in "-".join(rel_parts):
            return "dispute-resolution"
        if len(rel_parts) > 2 and rel_parts[1] == "support":
            return rel_parts[2]
        return rel_parts[1] if len(rel_parts) > 1 else "general_support"
    return "general_support"


def load_corpus(data_dir: str) -> List[CorpusDoc]:
    root = Path(data_dir)
    docs: List[CorpusDoc] = []
    for path in root.rglob("*.md"):
        rel = path.relative_to(root).as_posix()
        rel_parts = rel.split("/")
        if not rel_parts:
            continue
        company = normalize_company(rel_parts[0])
        if company == "none":
            continue
        raw_text = path.read_text(encoding="utf-8", errors="ignore")
        meta, body = _parse_frontmatter(raw_text)
        title = meta.get("title") or _first_heading(body) or path.stem.replace("-", " ")
        source_url = meta.get("source_url", "")
        product_area = _extract_product_area(company, rel_parts, meta)
        content = f"{title}\n{body}".strip()
        tokens = tokenize(content)
        token_freq = dict(Counter(tokens))

        docs.append(
            CorpusDoc(
                doc_id=rel,
                company=company,
                product_area=product_area,
                title=title,
                source_url=source_url,
                path=str(path.as_posix()),
                content=content,
                tokens=tokens,
                token_freq=token_freq,
            )
        )
    return docs


class CorpusIndex:
    def __init__(self, docs: Iterable[CorpusDoc]):
        self.docs: List[CorpusDoc] = list(docs)
        self.df: Dict[str, int] = defaultdict(int)
        self.idf: Dict[str, float] = {}
        self._build()

    def _build(self) -> None:
        n_docs = len(self.docs)
        for doc in self.docs:
            seen = set(doc.tokens)
            for tok in seen:
                self.df[tok] += 1
        for tok, freq in self.df.items():
            self.idf[tok] = math.log((1 + n_docs) / (1 + freq)) + 1.0

    def search(self, query: str, company: str, top_k: int = 3) -> List[RetrievalHit]:
        company_norm = normalize_company(company)
        query_tokens = tokenize(query)
        if not query_tokens:
            return []

        q_freq = Counter(query_tokens)
        candidates = self.docs
        if company_norm != "none":
            candidates = [d for d in self.docs if d.company == company_norm]

        hits: List[RetrievalHit] = []
        for doc in candidates:
            score = 0.0
            for tok, qf in q_freq.items():
                tf = doc.token_freq.get(tok, 0)
                if tf == 0:
                    continue
                score += (1 + math.log(tf)) * (1 + math.log(qf)) * self.idf.get(tok, 1.0)

            # Favor focused support pages over global indexes and release notes.
            rel_path = doc.doc_id.lower()
            if rel_path.endswith("/index.md") or rel_path == "index.md":
                score *= 0.25
            if "release-notes" in rel_path:
                score *= 0.4

            # Small metadata boost for query tokens in title/path.
            title_path_tokens = tokenize(f"{doc.title} {doc.doc_id}")
            title_hits = sum(1 for tok in query_tokens if tok in title_path_tokens)
            score += title_hits * 0.5

            if score > 0:
                hits.append(RetrievalHit(doc=doc, score=score))
        hits.sort(key=lambda h: h.score, reverse=True)
        return hits[:top_k]
