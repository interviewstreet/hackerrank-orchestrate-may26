"""
classifier.py — Two-stage classification pipeline.

Stage 1: Request-type  →  bug | feature_request | invalid | product_issue
Stage 2: Product-area  →  assessments | account_management | billing |
                           privacy | security | technical_issues | general

Each stage uses a hybrid approach:
  1. Keyword scan  — fast O(n) pattern match on lowercased text.
  2. Semantic tie-break — cosine similarity vs. pre-built label embeddings,
     used only when the keyword vote is ambiguous or returns no winner.

This keeps the classifier deterministic and explainable without needing
an LLM call for every ticket.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

from config import (
    PRODUCT_AREA_KEYWORDS,
    RISK_PATTERNS,
    REQUEST_TYPE_KEYWORDS,
)
from utils import clean_text, log

if TYPE_CHECKING:
    from retriever import Retriever


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _keyword_votes(text: str, keyword_map: dict[str, list[str]]) -> Counter:
    """
    Return a vote counter keyed by category.
    Each keyword match in `text` adds one vote to its category.
    Longer keywords score more (len/10 bonus) so "unauthorized access" beats
    "access" in isolation.
    """
    votes: Counter = Counter()
    for category, keywords in keyword_map.items():
        for kw in keywords:
            if kw in text:
                votes[category] += 1 + len(kw) // 10
    return votes


# ─────────────────────────────────────────────────────────────────────────────
# Risk Detection
# ─────────────────────────────────────────────────────────────────────────────

class RiskDetector:
    """
    Scans ticket text for high-risk patterns.
    Returns (is_high_risk: bool, risk_category: str | None).
    """

    def detect(self, text: str) -> tuple[bool, str | None]:
        lowered = clean_text(text)
        for category, patterns in RISK_PATTERNS.items():
            for pattern in patterns:
                if pattern in lowered:
                    log.warn(f"Risk detected — category={category!r}, trigger={pattern!r}")
                    return True, category
        return False, None


# ─────────────────────────────────────────────────────────────────────────────
# Request-Type Classifier
# ─────────────────────────────────────────────────────────────────────────────

class RequestTypeClassifier:
    """
    Classifies a ticket into one of four request types.

    Decision order (stops at first match):
      1. Invalid signals  → invalid
      2. Bug signals      → bug
      3. Feature signals  → feature_request
      4. Fallback         → product_issue
    """

    def classify(self, text: str) -> str:
        lowered = clean_text(text)
        votes = _keyword_votes(lowered, REQUEST_TYPE_KEYWORDS)

        if not votes:
            return "product_issue"   # default catch-all

        # "invalid" always wins if it has any votes (policy violation)
        if votes.get("invalid", 0) > 0:
            return "invalid"

        winner = votes.most_common(1)[0][0]
        return winner if winner != "product_issue" else "product_issue"


# ─────────────────────────────────────────────────────────────────────────────
# Product-Area Classifier
# ─────────────────────────────────────────────────────────────────────────────

class ProductAreaClassifier:
    """
    Two-stage product-area classifier.

    Stage 1 — keyword voting:
      Build a vote counter; if one area dominates, return it immediately.

    Stage 2 — semantic similarity (via Retriever embeddings):
      When the keyword vote is a tie or yields zero, compare the ticket
      embedding against pre-computed label-description embeddings and pick
      the closest area.
    """

    # Human-readable descriptions used as semantic label anchors
    _LABEL_DESCRIPTIONS: dict[str, str] = {
        "assessments":          "coding test quiz assessment question timer score result",
        "account_management":   "login password account admin user 2fa locked out access",
        "billing":              "billing invoice charge payment refund subscription plan",
        "privacy":              "gdpr data deletion personal data privacy compliance erasure",
        "security":             "security breach unauthorized fraud stolen hacked vulnerability",
        "technical_issues":     "api integration error bug crash performance browser",
        "general":              "general query feature request demo pricing help",
    }

    def __init__(self) -> None:
        self._label_embeddings: dict[str, any] | None = None

    def _ensure_label_embeddings(self, retriever: "Retriever") -> None:
        """Lazily build label embeddings using the retriever's encoder."""
        if self._label_embeddings is not None:
            return
        self._label_embeddings = {
            area: retriever.encode(desc)
            for area, desc in self._LABEL_DESCRIPTIONS.items()
        }

    def classify(self, text: str, retriever: "Retriever | None" = None) -> str:
        lowered = clean_text(text)
        votes = _keyword_votes(lowered, PRODUCT_AREA_KEYWORDS)

        if votes:
            top_two = votes.most_common(2)
            winner_score  = top_two[0][1]
            runner_score  = top_two[1][1] if len(top_two) > 1 else 0

            # Clear winner: top score is strictly more than runner-up → fast path
            if winner_score > runner_score:
                return top_two[0][0]

        # Tie or no votes → semantic fallback
        if retriever is not None:
            self._ensure_label_embeddings(retriever)
            ticket_emb = retriever.encode(lowered)
            best_area, best_sim = "general", -1.0
            for area, label_emb in self._label_embeddings.items():
                sim = float(retriever.cosine_similarity(ticket_emb, label_emb))
                if sim > best_sim:
                    best_sim, best_area = sim, area
            log.info(f"Semantic product-area → {best_area} (sim={best_sim:.3f})")
            return best_area

        # Pure keyword tie — return the leader anyway
        if votes:
            return votes.most_common(1)[0][0]

        return "general"


# ─────────────────────────────────────────────────────────────────────────────
# Multi-intent Detection
# ─────────────────────────────────────────────────────────────────────────────

def detect_multi_intent(text: str) -> list[str]:
    """
    Lightweight multi-intent detection.

    Checks if the ticket touches several product areas simultaneously.
    Returns a list of areas (>1 means multi-intent).
    Used by the decision engine to flag potentially complex tickets.
    """
    lowered = clean_text(text)
    votes = _keyword_votes(lowered, PRODUCT_AREA_KEYWORDS)

    # Collect all areas with at least 1 vote
    areas = [area for area, count in votes.items() if count > 0]
    return areas if areas else ["general"]
