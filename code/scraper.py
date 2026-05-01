"""
scraper.py — Corpus preparation utility.

Since the repo's data/ directory ships pre-populated (you clone the repo and
data is already there), this file provides helper utilities to:
  1. Verify the corpus is present and non-empty.
  2. Show corpus statistics.
  3. (Optional) Supplement corpus by scraping additional pages if data/ is sparse.

Usage:
    python scraper.py --verify        # Check corpus health
    python scraper.py --stats         # Show chunk statistics
    python scraper.py --enrich        # Attempt to fetch additional pages

NOTE: The agent is designed to work ONLY with local corpus files.
      The --enrich option only fetches official support documentation URLs
      listed in the problem statement (not arbitrary web content).
"""

from __future__ import annotations

import os
import re
import sys
import time
import argparse
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"

# ─── Allowed supplement URLs (official support docs only) ─────────────────────

SUPPLEMENT_SOURCES = {
    "hackerrank": [
        "https://support.hackerrank.com/hc/en-us",
    ],
    "claude": [
        "https://support.claude.ai/hc/en-us",
        "https://support.claude.com/en/",
    ],
    "visa": [
        "https://www.visa.co.in/support.html",
    ],
}


def verify_corpus(data_dir: Path = DATA_DIR) -> bool:
    """Check that corpus exists and has content."""
    print(f"\n🔍 Verifying corpus at: {data_dir}")
    ok = True
    for domain in ["hackerrank", "claude", "visa"]:
        domain_dir = data_dir / domain
        if not domain_dir.exists():
            print(f"  ❌ Missing: {domain_dir}")
            ok = False
            continue
        files = list(domain_dir.rglob("*"))
        text_files = [f for f in files if f.is_file() and f.suffix in {".txt", ".md", ".html", ".json"}]
        total_chars = sum(f.stat().st_size for f in text_files)
        print(f"  ✅ {domain}: {len(text_files)} files, ~{total_chars/1024:.1f}KB")
    return ok


def corpus_stats(data_dir: Path = DATA_DIR):
    """Print detailed statistics about the corpus."""
    sys.path.insert(0, str(Path(__file__).parent))
    from retriever import load_corpus

    print(f"\n📊 Corpus Statistics")
    print(f"   Data dir: {data_dir}")
    chunks = load_corpus(data_dir)

    by_domain: dict[str, list] = {}
    for c in chunks:
        by_domain.setdefault(c.domain, []).append(c)

    total_chars = sum(len(c.text) for c in chunks)
    print(f"\n   Total chunks : {len(chunks)}")
    print(f"   Total chars  : {total_chars:,}")

    for domain, domain_chunks in sorted(by_domain.items()):
        chars = sum(len(c.text) for c in domain_chunks)
        files = len({c.filename for c in domain_chunks})
        print(f"\n   [{domain}]")
        print(f"     Chunks : {len(domain_chunks)}")
        print(f"     Files  : {files}")
        print(f"     Chars  : {chars:,}")
        # show sample sources
        sources = list({c.source for c in domain_chunks})[:3]
        for s in sources:
            print(f"     Sample : {s}")


def _try_fetch(url: str) -> str:
    """Attempt to fetch a URL. Returns empty string on failure."""
    try:
        import urllib.request
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "SupportTriageAgent/1.0 (hackathon research tool)"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"    ⚠️  Could not fetch {url}: {e}")
        return ""


def enrich_corpus(data_dir: Path = DATA_DIR):
    """
    Optionally fetch additional support pages to supplement the local corpus.
    Only fetches from the three official support sites listed in the problem statement.
    """
    print("\n🌐 Enriching corpus from official support sites...")
    print("   (This only fetches from whitelisted support documentation URLs)")

    for domain, urls in SUPPLEMENT_SOURCES.items():
        domain_dir = data_dir / domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        for url in urls:
            print(f"\n   Fetching: {url}")
            html = _try_fetch(url)
            if not html:
                continue
            # Strip tags
            text = re.sub(r"<[^>]+>", " ", html)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) < 100:
                print(f"    ⚠️  Too little text extracted ({len(text)} chars)")
                continue
            # Save
            safe_name = re.sub(r"[^\w]", "_", url.split("//")[-1])[:80]
            out_path = domain_dir / f"_enriched_{safe_name}.txt"
            out_path.write_text(text, encoding="utf-8")
            print(f"    ✅ Saved {len(text):,} chars → {out_path.name}")
            time.sleep(1)  # polite delay

    print("\n✅ Enrichment complete.")


def create_placeholder_corpus(data_dir: Path = DATA_DIR):
    """
    Create minimal placeholder corpus files for testing when data/ is empty.
    THIS IS ONLY FOR TESTING — the real corpus comes from the repo.
    """
    print("\n⚠️  Creating minimal placeholder corpus for testing...")

    placeholders = {
        "hackerrank": """
HackerRank Support Documentation

Account & Login
To reset your password, click 'Forgot Password' on the login page.
If your account is suspended, contact support@hackerrank.com.
SSO issues: ensure your SAML configuration is correctly set up.

Assessments
Candidates cannot pause or restart a timed assessment.
Proctoring uses webcam and screen monitoring.
If a candidate is flagged for plagiarism, the recruiter is notified.

Billing
HackerRank offers Starter, Professional, and Enterprise plans.
To cancel your subscription, go to Billing Settings.
Refunds are processed within 5-7 business days.

IDE & Compiler
Supported languages include Python, Java, C++, JavaScript, and more.
If the IDE crashes, try refreshing or using a different browser.
""",
        "claude": """
Claude Help Center

Plans & Billing
Claude Free plan includes limited messages per day.
Claude Pro costs $20/month and includes more messages and Claude 3 Opus access.
Claude Team plan costs $25/user/month with a 5-user minimum.
To cancel, go to Settings > Billing > Cancel Plan.

Account
Create a Claude account at claude.ai with email or Google sign-in.
To delete your account, go to Settings > Privacy > Delete Account.

Features
Claude supports file uploads, image analysis, and code generation.
Projects allow organizing conversations by topic.
Memory feature lets Claude remember preferences across conversations.

API
The Claude API is available at api.anthropic.com.
API keys can be generated in the Anthropic Console.
Rate limits vary by tier.

Safety & Privacy
Claude is designed to be safe, helpful, and honest.
Conversation data may be used to improve Claude unless you opt out.
""",
        "visa": """
Visa Consumer Support

Card Services
To report a lost or stolen card, call the number on the back of your card immediately.
Visa Zero Liability Policy protects against unauthorized transactions.
Card replacement typically takes 3-5 business days.

Fraud & Disputes
To dispute a transaction, contact your card issuing bank.
Unauthorized transactions should be reported immediately.
Visa's dispute resolution typically takes 30-45 days.

Transactions
Card declined? Check if the card is active and has sufficient funds.
International transactions may require notifying your bank.
Visa cards are accepted at 100+ million merchant locations.

Rewards
Visa rewards programs vary by card issuer.
Contact your bank for specific rewards redemption information.
""",
    }

    for domain, content in placeholders.items():
        domain_dir = data_dir / domain
        domain_dir.mkdir(parents=True, exist_ok=True)
        out_file = domain_dir / "placeholder_docs.txt"
        if not out_file.exists():
            out_file.write_text(content.strip(), encoding="utf-8")
            print(f"  Created: {out_file}")
    print("  Done. Replace with real corpus from the repo.")


def main():
    parser = argparse.ArgumentParser(description="Corpus management utility")
    parser.add_argument("--verify", action="store_true", help="Verify corpus health")
    parser.add_argument("--stats", action="store_true", help="Show corpus statistics")
    parser.add_argument("--enrich", action="store_true", help="Fetch additional support pages")
    parser.add_argument("--placeholder", action="store_true", help="Create placeholder corpus for testing")
    parser.add_argument("--data-dir", type=Path, default=DATA_DIR, help="Corpus directory")
    args = parser.parse_args()

    if args.verify:
        ok = verify_corpus(args.data_dir)
        sys.exit(0 if ok else 1)
    elif args.stats:
        corpus_stats(args.data_dir)
    elif args.enrich:
        enrich_corpus(args.data_dir)
    elif args.placeholder:
        create_placeholder_corpus(args.data_dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
