"""
scraper.py — Optional corpus refresh utility.

Crawls the three support sites and saves each article as a .json file
under data/{domain}/. Intended for offline corpus refresh ONLY — do NOT
run this during agent evaluation. The problem statement requires using the
pre-built corpus already present in data/.

Sites:
  - HackerRank: https://support.hackerrank.com/
  - Claude:     https://support.claude.com/en/
  - Visa:       https://www.visa.co.in/support.html

Usage:
    python code/corpus/scraper.py

Output:
    data/hackerrank/article_001.json
    data/claude/article_001.json
    data/visa/article_001.json

    Each JSON: {"title": "...", "url": "...", "content": "..."}
"""

import json
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SITES: list[dict] = [
    {
        "domain": "hackerrank",
        "seed_url": "https://support.hackerrank.com/",
        "allowed_host": "support.hackerrank.com",
    },
    {
        "domain": "claude",
        "seed_url": "https://support.claude.com/en/",
        "allowed_host": "support.claude.com",
    },
    {
        "domain": "visa",
        "seed_url": "https://www.visa.co.in/support.html",
        "allowed_host": "www.visa.co.in",
    },
]

MAX_DEPTH = 2
REQUEST_DELAY = 1.0          # seconds between requests
MIN_CONTENT_LENGTH = 100     # skip pages shorter than this
DATA_DIR = Path("data")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; SupportTriageBot/1.0; "
        "+https://github.com/interviewstreet/hackerrank-orchestrate-may26)"
    )
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _get_page(url: str, session: requests.Session) -> BeautifulSoup | None:
    """Fetch a URL and return a BeautifulSoup object, or None on error.

    Args:
        url:     The page URL to fetch.
        session: An active requests.Session for connection reuse.

    Returns:
        BeautifulSoup parse tree, or None if the request fails.
    """
    try:
        response = session.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as exc:
        print(f"  [WARN] Failed to fetch {url}: {exc}")
        return None


def _extract_links(soup: BeautifulSoup, base_url: str, allowed_host: str) -> list[str]:
    """Extract all same-domain links from a page.

    Args:
        soup:         Parsed page.
        base_url:     The URL of the current page (for resolving relative links).
        allowed_host: Only links whose netloc matches this are returned.

    Returns:
        Deduplicated list of absolute URLs on the same host.
    """
    links: list[str] = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"].strip()
        if href.startswith("#") or href.startswith("mailto:"):
            continue
        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        if parsed.netloc == allowed_host and parsed.scheme in ("http", "https"):
            # Strip fragment
            clean = absolute.split("#")[0].rstrip("/")
            if clean not in links:
                links.append(clean)
    return links


def _extract_article(soup: BeautifulSoup, url: str) -> dict | None:
    """Extract title, url, and content from a parsed page.

    Title:   <h1> tag text, falling back to <title>.
    Content: All <p> tag text joined with newlines, stripped of HTML.

    Args:
        soup: Parsed page.
        url:  Source URL (stored verbatim in the JSON).

    Returns:
        Dict {"title": ..., "url": ..., "content": ...} or None if the
        content is shorter than MIN_CONTENT_LENGTH characters.
    """
    # Title
    h1 = soup.find("h1")
    title = h1.get_text(strip=True) if h1 else ""
    if not title:
        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else url

    # Content — gather all paragraphs
    paragraphs = [p.get_text(separator=" ", strip=True) for p in soup.find_all("p")]
    content = "\n".join(p for p in paragraphs if p)

    if len(content) < MIN_CONTENT_LENGTH:
        return None

    return {"title": title, "url": url, "content": content}


# ---------------------------------------------------------------------------
# Core crawler
# ---------------------------------------------------------------------------


def crawl_site(
    domain: str,
    seed_url: str,
    allowed_host: str,
    out_dir: Path,
    session: requests.Session,
) -> int:
    """Crawl a support site up to MAX_DEPTH and save articles as JSON.

    Uses a breadth-first queue. Each URL is visited at most once.
    A REQUEST_DELAY second pause is inserted between every HTTP request.

    Args:
        domain:       Domain tag used for file naming and logging.
        seed_url:     Starting URL for the crawl.
        allowed_host: Only follow links on this hostname.
        out_dir:      Directory where .json files are written.
        session:      Active requests.Session.

    Returns:
        Number of articles successfully saved.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    visited: set[str] = set()
    # Queue entries: (url, depth)
    queue: list[tuple[str, int]] = [(seed_url.rstrip("/"), 0)]
    saved = 0

    while queue:
        url, depth = queue.pop(0)

        if url in visited:
            continue
        visited.add(url)

        time.sleep(REQUEST_DELAY)
        soup = _get_page(url, session)
        if soup is None:
            continue

        # Try to extract an article from this page
        article = _extract_article(soup, url)
        if article:
            filename = out_dir / f"article_{saved + 1:04d}.json"
            filename.write_text(json.dumps(article, ensure_ascii=False, indent=2), encoding="utf-8")
            saved += 1
            print(f"  Scraped: {url}")

        # Enqueue child links if we haven't hit max depth
        if depth < MAX_DEPTH:
            for link in _extract_links(soup, url, allowed_host):
                if link not in visited:
                    queue.append((link, depth + 1))

    return saved


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Crawl all three support sites and save articles to data/.

    Prints per-URL progress and a final summary table of docs saved
    per domain. Safe to re-run — existing files are overwritten.
    """
    print("=" * 60)
    print("Support Corpus Scraper")
    print("WARNING: Do NOT run this during agent evaluation.")
    print("The pre-built corpus in data/ is the official corpus.")
    print("=" * 60)
    print()

    summary: dict[str, int] = {}

    with requests.Session() as session:
        for site in SITES:
            domain = site["domain"]
            out_dir = DATA_DIR / domain
            print(f"[{domain.upper()}] Crawling {site['seed_url']} ...")
            count = crawl_site(
                domain=domain,
                seed_url=site["seed_url"],
                allowed_host=site["allowed_host"],
                out_dir=out_dir,
                session=session,
            )
            summary[domain] = count
            print(f"[{domain.upper()}] Done — {count} docs saved to {out_dir}/\n")

    print("=" * 60)
    print("Summary")
    print("=" * 60)
    total = 0
    for domain, count in summary.items():
        print(f"  {domain:<15} {count:>4} docs")
        total += count
    print(f"  {'TOTAL':<15} {total:>4} docs")
    print("=" * 60)


if __name__ == "__main__":
    main()
