"""
live_scraper.py — Utility to fetch and clean text from support URLs in real-time.
"""

import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; SupportTriageBot/1.0; +https://github.com/HarshavardhanVemali/hackerrank-orchestrate-may26)"
}

def scrape_url(url: str) -> str:
    """Fetch a URL and return a clean text representation of the page content.
    
    Args:
        url: The absolute URL to scrape.
        
    Returns:
        String containing the cleaned text content, or an empty string on failure.
    """
    if not url or not url.startswith("http"):
        return ""
    
    # Fast path: skip binary extensions
    if any(url.lower().endswith(ext) for ext in [".dmg", ".exe", ".zip", ".png", ".jpg", ".jpeg", ".pdf", ".gz", ".tar"]):
        return ""

    try:
        # Use a short timeout to prevent hanging the whole pipeline
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        
        # Check content type - skip if not HTML
        content_type = response.headers.get("Content-Type", "").lower()
        if "html" not in content_type:
            return ""

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for script_or_style in soup(["script", "style", "nav", "footer", "header"]):
            script_or_style.decompose()

        # Extract text from common article containers
        # Try to find the main content area first
        article = soup.find("article") or soup.find("main") or soup.find("div", class_=re.compile(r"content|article|body", re.I))
        
        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            # Fallback to body text
            text = soup.body.get_text(separator="\n", strip=True) if soup.body else ""

        # Basic cleanup: collapse multiple newlines
        text = re.sub(r"\n\s*\n", "\n\n", text)
        return text.strip()

    except Exception as e:
        print(f"  [DEBUG] Live scraping failed for {url}: {e}")
        return ""
