"""
Product Area Agent
Uses ONLY corpus metadata for product_area classification.
No LLM, no guessing.
"""

from utils.logger import log_agent


def run(chunks: list[dict], domain: str, query: str = "") -> str:
    """
    Returns product_area string from corpus metadata only.
    """
    if not chunks:
        log_agent("product_area", "no chunks → unknown", {})
        return "unknown"

    top_meta = chunks[0].get("metadata", {})
    raw_product_area = str(top_meta.get("product_area", "")).strip()

    if not raw_product_area:
        log_agent("product_area", "missing metadata.product_area → unknown", {})
        return "unknown"

    if raw_product_area.lower().endswith(".md"):
        raw_product_area = raw_product_area[:-3]

    product_area = raw_product_area or "unknown"

    log_agent("product_area", f"→ '{product_area}'", {
        "source_url": top_meta.get("source_url", ""),
        "title": top_meta.get("title", ""),
    })

    return product_area