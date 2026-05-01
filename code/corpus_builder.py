"""
ARIA - Corpus Builder
Reads support documentation from the local data/ directory (provided in repo).
Structure: data/hackerrank/, data/claude/, data/visa/ — all .md files recursively.
Falls back to static corpus if data/ is not found.
"""

import os
import re
from pathlib import Path
from typing import List, Dict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


DOMAIN_FOLDERS = {
    "HackerRank": "hackerrank",
    "Claude":     "claude",
    "Visa":       "visa",
}

STATIC_CORPUS = {
    "HackerRank": [
        "To delete your HackerRank account, go to Settings > Delete Account. Google login accounts must first set a password via Forgot Password before deletion.",
        "To remove a user from HackerRank for Work, go to Admin > Users, find the user, click the three dots menu, and select Remove User or Deactivate.",
        "HackerRank does not allow score changes or manual review of completed assessments by support. Scores are final and graded by the platform.",
        "To add time accommodation for a candidate: Go to Tests > Select Test > Candidates tab > Select candidate > More > Add Time Accommodation. Enter percentage in multiples of 5.",
        "To reinvite a candidate to an assessment: Tests tab > Select test > Candidates > Select candidate > Reinvite.",
        "Tests in HackerRank remain active indefinitely unless a start and end time is set. Set expiry in Test Settings > General > Start/End date.",
        "To pause or cancel a HackerRank subscription, contact support or go to Billing settings. Pausing stops new hiring but retains data.",
        "For payment or billing issues, provide your order ID to HackerRank support. Refunds are handled on a case-by-case basis per the refund policy.",
        "Mock interview refunds are subject to HackerRank refund policy. Contact support with your order details.",
        "Test variants allow you to adapt a single test for different candidate profiles. A test must have at least two variants. Variants cannot be deleted if only two exist.",
        "Rescheduling a HackerRank assessment is at the discretion of the hiring company, not HackerRank support. Contact the recruiter or company directly.",
        "HackerRank does not change recruiter decisions or move candidates to next rounds.",
        "Candidate inactivity timeout: Candidates are timed out after a period of inactivity. Contact support to request configuration changes.",
        "For Zoom connectivity issues during proctored tests, ensure Zoom is not blocked by firewall, allow camera and microphone permissions.",
        "HackerRank InfoSec security questionnaires are handled by the security team. Submit through the official vendor security form or contact your account manager.",
        "Certificate name corrections: Contact HackerRank support with proof of correct name such as government ID. Updates may take a few days.",
        "The Apply tab on HackerRank is for job applications. If you cannot see it, ensure you are logged in and have completed your profile.",
        "Submission issues across challenges may indicate a platform outage. Check HackerRank status page or contact support.",
        "To remove an interviewer from the platform: Admin > Interviewers > Select user > three dots menu > Remove.",
        "Resume Builder on HackerRank allows candidates to create resumes. If Resume Builder is down, try clearing cache or contact support.",
    ],
    "Claude": [
        "To delete a Claude conversation: Open the conversation > Click the conversation name at top > Select Delete.",
        "Claude data retention: When you enable training data opt-in, conversation data may be used to improve models. Opt out in Settings > Privacy.",
        "Claude Team workspace access is managed by the workspace admin. If your seat was removed by an IT admin, only an admin can restore access.",
        "Claude API access issues with AWS Bedrock: Ensure your Bedrock service quota is active, your region supports Claude models, and IAM permissions include bedrock:InvokeModel.",
        "If Claude is completely down or all requests are failing, check status.anthropic.com for service status.",
        "To report a security vulnerability in Claude: Submit through Anthropic's responsible disclosure program at anthropic.com/security.",
        "To prevent Claude from crawling your website, add ClaudeBot to your robots.txt: User-agent: ClaudeBot Disallow: /",
        "Claude for Education LTI integration: Claude offers LTI keys for educational institutions. Contact Anthropic education team or visit claude.ai/education.",
        "If you opted in to model training, your data may be used to improve Claude. Visit privacy.claude.com for details on data retention.",
    ],
    "Visa": [
        "To report a lost or stolen Visa card from India: Call Visa India at 000-800-100-1219. From anywhere: Visa Global Customer Assistance Service 24/7 at +1 303 967 1090.",
        "If your Visa card is blocked while traveling: Contact your card-issuing bank first. The bank can unblock or reissue your card.",
        "Lost or stolen Visa Traveller Cheques: Call the issuer immediately. For Citicorp: 1-800-645-6556 or 1-813-623-1709.",
        "To dispute a Visa charge: Contact your card-issuing bank directly. They will initiate a chargeback process. Visa does not directly handle disputes.",
        "Visa does not directly refund cardholders or ban merchants. Dispute resolution goes through your issuing bank via the chargeback process.",
        "If your identity has been stolen: Contact your card-issuing bank immediately. File a police report. Contact credit bureaus to place a fraud alert.",
        "Visa Emergency Cash: Visa Global Customer Assistance Service at +1 303 967 1090 can arrange emergency cash via the Visa Emergency Money Transfer program.",
        "Merchants in the US including US territories like US Virgin Islands may set a minimum transaction of up to 10 dollars for Visa credit card purchases under the Dodd-Frank Act.",
        "For general Visa support in India: Visit www.visa.co.in/support.html or call the Visa India helpline.",
    ],
}


class CorpusChunk:
    def __init__(self, text: str, source: str, domain: str, filepath: str = ""):
        self.text = text
        self.source = source
        self.domain = domain
        self.filepath = filepath


class CorpusBuilder:
    def __init__(self):
        self.chunks: List[CorpusChunk] = []
        self.vectorizer = None
        self.tfidf_matrix = None

    def _clean_text(self, text: str) -> str:
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)
        text = re.sub(r'<[^>]+>', '', text)
        text = re.sub(r'^[-_*]{3,}$', '', text, flags=re.MULTILINE)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    def _chunk_markdown(self, text: str, min_len: int = 80, max_len: int = 1200) -> List[str]:
        sections = re.split(r'\n(?=#{1,3} )', text)
        chunks = []
        for section in sections:
            section = self._clean_text(section)
            if not section or len(section) < min_len:
                continue
            if len(section) <= max_len:
                chunks.append(section)
            else:
                paras = re.split(r'\n\n+', section)
                current = ""
                for para in paras:
                    para = para.strip()
                    if not para:
                        continue
                    if len(current) + len(para) < max_len:
                        current = (current + "\n\n" + para).strip()
                    else:
                        if len(current) >= min_len:
                            chunks.append(current)
                        current = para
                if len(current) >= min_len:
                    chunks.append(current)
        return chunks

    def _find_data_dir(self, script_dir: Path):
        candidates = [
            script_dir / "data",
            script_dir.parent / "data",
            Path("data"),
            Path("../data"),
        ]
        for c in candidates:
            resolved = c.resolve()
            if resolved.exists() and resolved.is_dir():
                return resolved
        return None

    def load_from_data_dir(self, data_dir: Path, verbose: bool = True) -> int:
        loaded = 0
        for domain, folder_name in DOMAIN_FOLDERS.items():
            domain_path = data_dir / folder_name
            if not domain_path.exists():
                if verbose:
                    print(f"  [CORPUS] Warning: {domain_path} not found, skipping")
                continue
            md_files = list(domain_path.rglob("*.md"))
            if verbose:
                print(f"  [CORPUS] {domain}: {len(md_files)} .md files in {domain_path.name}/")
            for md_file in md_files:
                try:
                    text = md_file.read_text(encoding="utf-8", errors="ignore")
                    chunks = self._chunk_markdown(text)
                    for chunk in chunks:
                        self.chunks.append(CorpusChunk(
                            text=chunk,
                            source=str(md_file.relative_to(data_dir)),
                            domain=domain,
                            filepath=str(md_file),
                        ))
                    loaded += len(chunks)
                except Exception as e:
                    if verbose:
                        print(f"  [CORPUS] Could not read {md_file}: {e}")
        return loaded

    def load_static_fallback(self):
        for domain, docs in STATIC_CORPUS.items():
            for doc in docs:
                self.chunks.append(CorpusChunk(
                    text=doc, source="static_fallback", domain=domain
                ))

    def build_corpus(self, verbose: bool = True):
        script_dir = Path(__file__).parent.resolve()
        data_dir = self._find_data_dir(script_dir)

        if data_dir:
            if verbose:
                print(f"  [CORPUS] Found data directory: {data_dir}")
            n = self.load_from_data_dir(data_dir, verbose=verbose)
            if verbose:
                print(f"  [CORPUS] Loaded {n} chunks from local corpus")

        # Always add static fallback as extra signal
        self.load_static_fallback()

        if verbose:
            print(f"  [CORPUS] Total chunks in index: {len(self.chunks)}")

        self._build_index()

    def _build_index(self):
        texts = [c.text for c in self.chunks]
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            max_features=12000,
            stop_words="english",
            sublinear_tf=True,
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def retrieve(self, query: str, domain: str = None, top_k: int = 6) -> List[Dict]:
        if self.vectorizer is None:
            return []
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix)[0]

        boosted = []
        for i, score in enumerate(scores):
            chunk = self.chunks[i]
            boost = 1.6 if (domain and chunk.domain == domain) else 1.0
            boosted.append((i, float(score) * boost))

        boosted.sort(key=lambda x: x[1], reverse=True)

        results = []
        seen = set()
        for idx, score in boosted:
            key = self.chunks[idx].text[:120]
            if key in seen:
                continue
            seen.add(key)
            results.append({
                "text": self.chunks[idx].text,
                "domain": self.chunks[idx].domain,
                "score": score,
                "source": self.chunks[idx].source,
            })
            if len(results) >= top_k:
                break
        return results

    def get_confidence(self, retrieved: List[Dict]) -> float:
        if not retrieved:
            return 0.0
        return retrieved[0]["score"]
