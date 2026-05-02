"""Centralized constants and configuration. Locked at startup."""
from __future__ import annotations

import os
import random
from pathlib import Path

import numpy as np

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

REPO_ROOT = Path(__file__).resolve().parent.parent
CODE_DIR = Path(__file__).resolve().parent
DATA_DIR = REPO_ROOT / "data"
TICKETS_DIR = REPO_ROOT / "support_tickets"
INPUT_CSV = TICKETS_DIR / "support_tickets.csv"
SAMPLE_CSV = TICKETS_DIR / "sample_support_tickets.csv"
OUTPUT_CSV = TICKETS_DIR / "output.csv"
CACHE_DIR = CODE_DIR / ".cache"


def load_env_files() -> None:
    """Load optional local env files without overriding exported variables."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    for path in (
        REPO_ROOT / ".env",
        REPO_ROOT / ".env.local",
        CODE_DIR / ".env",
        CODE_DIR / ".env.local",
    ):
        if path.exists():
            load_dotenv(path, override=False)


load_env_files()

OUTPUT_HEADER = [
    "issue", "subject", "company", "response",
    "product_area", "status", "request_type", "justification",
]

STATUS_VALUES = ("replied", "escalated")
REQUEST_TYPE_VALUES = ("product_issue", "feature_request", "bug", "invalid")
COMPANIES = ("HackerRank", "Claude", "Visa", "None")

PRODUCT_AREA_SEED = {
    "HackerRank": ["screen", "community", "interview", "library",
                   "integrations", "settings", "general"],
    "Claude":     ["privacy", "conversation_management", "billing",
                   "api", "teams", "claude_code", "general"],
    "Visa":       ["general_support", "travel_support", "business_support",
                   "card_services", "fraud", "payments"],
    "None":       ["general_support", "general"],
}

CHUNK_SIZE_TOKENS = 400
CHUNK_OVERLAP_CHARS = 80
RETRIEVE_TOP_K = 8
COVERAGE_MAX_FLOOR = 0.30
COVERAGE_MEAN3_FLOOR = 0.22
TFIDF_COVERAGE_MAX_FLOOR = 0.11
TFIDF_COVERAGE_MEAN3_FLOOR = 0.08
LLM_CONFIDENCE_FLOOR = 0.45

ANTHROPIC_MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-4-6")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "auto")  # anthropic | openai | auto
EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
