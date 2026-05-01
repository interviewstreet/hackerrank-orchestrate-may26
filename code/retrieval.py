import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence

from utils import clean_text, markdown_to_text, tokenize


AREA_MAP = {
    "hackerrank/interviews": "interviewing",
    "hackerrank/screen": "assessments",
    "hackerrank/settings": "team_management",
    "hackerrank/integrations": "integrations",
    "hackerrank/skillup": "learning_and_development",
    "hackerrank/chakra": "ai_interviewing",
    "hackerrank/hackerrank_community/subscriptions-payments-and-billing": "billing_and_subscriptions",
    "hackerrank/hackerrank_community/certifications": "certifications",
    "hackerrank/hackerrank_community": "community_support",
    "hackerrank/general-help": "platform_support",
    "hackerrank/uncategorized": "platform_support",
    "claude/privacy-and-legal": "privacy_and_compliance",
    "claude/claude/account-management": "account_management",
    "claude/claude/troubleshooting": "service_availability",
    "claude/claude-api-and-console": "api_and_developer_tools",
    "claude/amazon-bedrock": "api_and_developer_tools",
    "claude/claude-for-education": "education",
    "claude/team-and-enterprise-plans/security-and-compliance": "privacy_and_compliance",
    "visa/support/consumer/travel-support": "travel_services",
    "visa/support/consumer": "consumer_support",
    "visa/support/small-business/fraud-protection": "fraud_and_security",
    "visa/support/small-business/dispute-resolution": "payment_processing",
    "visa/support/small-business/regulations-fees": "merchant_acceptance",
    "visa/support/small-business": "merchant_acceptance",
}

INTENT_ROUTING = {
    "crawler": ["claude/privacy-and-legal/8896518"],
    "crawl": ["claude/privacy-and-legal/8896518"],
    "bedrock": ["claude/amazon-bedrock"],
    "not responding": ["claude/claude/troubleshooting"],
    "requests are failing": ["claude/claude/troubleshooting"],
    "stopped working": ["claude/claude/troubleshooting"],
    "urgent cash": ["visa/support/consumer/travel-support"],
    "minimum spend": ["visa/support/consumer/visa-rules"],
    "employee has left": ["hackerrank/settings/teams-management"],
    "remove them": ["hackerrank/settings/teams-management"],
    "certificate": [
        "hackerrank/hackerrank_community/certifications",
        "hackerrank/skillup/getting-started",
    ],
    "interviewer": ["hackerrank/settings/teams-management"],
    "personal data": [
        "claude/team-and-enterprise-plans/security-and-compliance/9267387",
        "claude/privacy-and-legal",
    ],
    "privacy": ["claude/privacy-and-legal"],
    "compatibility": [
        "hackerrank/interviews/getting-started/6271433412",
        "hackerrank/uncategorized/5897755717",
    ],
    "reschedule": ["hackerrank/interviews/manage-interviews/2342466364"],
}


@dataclass(frozen=True)
class SupportDoc:
    company: str
    path: str
    title: str
    text: str
    product_area: str


@dataclass(frozen=True)
class RetrievalHit:
    doc: SupportDoc
    score: float


class RetrievalEngine:
    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir
        self.docs = self._load_docs()

    def search(self, ticket_text: str, company: str, top_k: int = 5) -> List[RetrievalHit]:
        candidates = self._company_candidates(company)
        routed_candidates = self._intent_candidates(ticket_text, company, candidates)
        if routed_candidates:
            candidates = routed_candidates

        query_tokens = tokenize(ticket_text)
        if not query_tokens:
            return []

        hits: List[RetrievalHit] = []
        for doc in candidates:
            score = self._score_doc(query_tokens, ticket_text, doc)
            if score >= 0.12:
                hits.append(RetrievalHit(doc=doc, score=score))

        hits.sort(key=lambda hit: hit.score, reverse=True)
        return hits[:top_k]

    def _company_candidates(self, company: str) -> List[SupportDoc]:
        if company == "none":
            return self.docs
        return [doc for doc in self.docs if doc.company == company]

    def _intent_candidates(
        self,
        ticket_text: str,
        company: str,
        candidates: Sequence[SupportDoc],
    ) -> List[SupportDoc]:
        lowered = ticket_text.lower()
        routes: List[str] = []
        if re.search(r"\blti\b", lowered):
            routes = ["hackerrank/integrations", "hackerrank/skillup"] if company in {"hackerrank", "none", "", None} else ["claude/claude-for-education"]
            return [doc for doc in candidates if any(route in doc.path.lower() for route in routes)]
        for intent, prefixes in INTENT_ROUTING.items():
            if intent in lowered:
                routes.extend(prefixes)
        if not routes:
            return []

        matched = [
            doc
            for doc in candidates
            if any(route in doc.path.lower() for route in routes)
        ]
        return matched

    def _load_docs(self) -> List[SupportDoc]:
        docs: List[SupportDoc] = []
        for path in sorted(self.data_dir.rglob("*.md")):
            raw = path.read_text(encoding="utf-8", errors="ignore")
            plain_text = markdown_to_text(raw)
            if not plain_text:
                continue
            relative = path.relative_to(self.data_dir).as_posix()
            company = relative.split("/", 1)[0].lower()
            docs.append(
                SupportDoc(
                    company=company,
                    path=relative,
                    title=self._extract_title(raw, path.stem),
                    text=plain_text,
                    product_area=self._product_area(relative),
                )
            )
        return docs

    def _extract_title(self, raw: str, stem: str) -> str:
        for line in raw.splitlines():
            stripped = line.strip()
            if stripped.startswith("# "):
                return clean_text(stripped[2:])
        return clean_text(stem.replace("-", " "))

    def _product_area(self, relative_path: str) -> str:
        lowered = relative_path.lower()
        for prefix, area in sorted(AREA_MAP.items(), key=lambda item: len(item[0]), reverse=True):
            if lowered.startswith(prefix):
                return area
        if lowered.startswith("hackerrank/"):
            return "platform_support"
        if lowered.startswith("claude/"):
            return "account_management"
        if lowered.startswith("visa/"):
            return "consumer_support"
        return "platform_support"

    def _score_doc(self, query_tokens: List[str], ticket_text: str, doc: SupportDoc) -> float:
        path_tokens = tokenize(doc.path.replace("/", " "))
        title_tokens = tokenize(doc.title)
        body_tokens = tokenize(doc.text)

        path_overlap = self._overlap_score(query_tokens, path_tokens)
        title_overlap = self._overlap_score(query_tokens, title_tokens)
        body_overlap = self._overlap_score(query_tokens, body_tokens[:400])
        phrase_boost = self._phrase_boost(ticket_text.lower(), doc)

        score = (0.35 * title_overlap) + (0.25 * path_overlap) + (0.30 * body_overlap) + phrase_boost
        return round(min(score, 1.0), 3)

    def _overlap_score(self, left: Sequence[str], right: Sequence[str]) -> float:
        if not left or not right:
            return 0.0
        left_counts = Counter(left)
        right_counts = Counter(right)
        overlap = sum(min(left_counts[token], right_counts[token]) for token in left_counts)
        return overlap / max(len(set(left)), 1)

    def _phrase_boost(self, ticket_text: str, doc: SupportDoc) -> float:
        combined = f"{doc.title} {doc.path} {doc.text}".lower()
        boosts = 0.0
        phrases = [
            "bedrock",
            "crawler",
            "robots.txt",
            "privacy center",
            "team members",
            "compatibility",
            "status page",
            "reschedule",
            "certificate",
            "subscription",
            "refund",
        ]
        for phrase in phrases:
            if phrase in ticket_text and phrase in combined:
                boosts += 0.08
        return min(boosts, 0.24)
