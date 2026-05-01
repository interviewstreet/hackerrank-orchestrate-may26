import re
import unicodedata
from pathlib import Path
from typing import Dict, List


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "my",
    "of",
    "on",
    "or",
    "the",
    "to",
    "us",
    "we",
    "with",
    "you",
    "your",
}


def workspace_root() -> Path:
    return Path(__file__).resolve().parent.parent


def clean_text(value: str) -> str:
    text = unicodedata.normalize("NFKC", str(value or ""))
    replacements = {
        "\ufeff": " ",
        "â€™": "'",
        "â€˜": "'",
        "â€œ": '"',
        "â€": '"',
        "â€“": "-",
        "â€”": "-",
        "Â": " ",
        "Ã©": "e",
        "Ã¨": "e",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def markdown_to_text(raw: str) -> str:
    text = raw
    text = re.sub(r"^---.*?---", " ", text, flags=re.DOTALL)
    text = re.sub(r"(?im)^(title|title_slug|source_url|final_url|article_id|article_slug|description|last_updated.*|last_modified|breadcrumbs):.*$", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`{1,3}.*?`{1,3}", " ", text, flags=re.DOTALL)
    text = re.sub(r"(?m)^\s*[-*]\s+", "", text)
    text = re.sub(r"[#>|_]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return clean_text(text)


def tokenize(text: str) -> List[str]:
    return [
        token
        for token in re.findall(r"[a-z0-9]+", clean_text(text).lower())
        if token not in STOPWORDS and len(token) > 1
    ]


def sentence_candidates(text: str) -> List[str]:
    sentences = re.split(r"(?<=[.!?])\s+", clean_text(text))
    results = []
    for sentence in sentences:
        lowered = sentence.lower()
        if len(sentence) < 25:
            continue
        if lowered.startswith(("title", "source url", "last updated", "breadcrumbs")):
            continue
        if "last modified" in lowered or "last updated" in lowered:
            continue
        if any(term in lowered for term in ("the magic of travel", "discover the magic", "offers and perks")):
            continue
        if "http" in lowered:
            continue
        results.append(sentence.strip())
    return results


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def resolve_log_path(log_path: Path, root: Path) -> Path:
    candidate = log_path if log_path.is_absolute() else (root / log_path)
    resolved_root = root.resolve()
    resolved_log = candidate.resolve()
    assert str(resolved_log).startswith(str(resolved_root))
    assert "hackerrank_orchestrate" not in str(resolved_log).lower() or str(resolved_log).startswith(str(resolved_root))
    return resolved_log


def append_run_log(log_path: Path, text: str) -> None:
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(text)
        if not text.endswith("\n"):
            handle.write("\n")


def build_ticket_id(row: Dict[str, str], row_index: int) -> str:
    subject = clean_text(row.get("Subject", ""))
    if subject:
        return subject
    return f"row-{row_index}"
