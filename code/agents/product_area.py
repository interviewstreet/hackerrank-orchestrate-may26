"""
Product Area Agent
Reads product_area directly from top retrieved chunk metadata.
Zero LLM cost — fully corpus-grounded.
"""

from utils.logger import log_agent


def run(chunks: list[dict], domain: str) -> str:
    """
    Returns product_area string.
    Falls back to domain if no chunks available.
    """
    if not chunks:
        log_agent("product_area", f"no chunks → fallback to domain '{domain}'", {})
        return domain or "unknown"

    top_meta     = chunks[0].get("metadata", {})
    product_area = top_meta.get("product_area", domain or "unknown")

    log_agent("product_area", f"→ '{product_area}'", {
        "source_url":   top_meta.get("source_url", ""),
        "title":        top_meta.get("title", ""),
    })

    return product_area