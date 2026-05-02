import re
from typing import Tuple


def classify_ticket(issue: str, subject: str, company: str) -> Tuple[str, str]:
    text = (issue + " " + (subject or "")).lower()
    
    request_type = classify_request_type(text)
    product_area = classify_product_area(text, company)
    
    return request_type, product_area


def classify_request_type(text: str) -> str:
    bug_patterns = [
        r'\bbroken\b', r'\bnot working\b', r'\bfailing\b', r'\berror\b',
        r'\bbug\b', r'\bcrashing\b', r'\bdowntime\b', r'\bsite down\b',
        r'\bcrash\b', r'\bfail\b', r'\berror\b'
    ]
    
    feature_patterns = [
        r'\badd\b.*\bfeature\b', r'\bwant to\b.*\badd\b', r'\bwould like\b.*\bhave\b',
        r'\bnew feature\b', r'\benhancement\b', r'\brequest.*\badd\b'
    ]
    
    invalid_patterns = [
        r'\btranslate\b', r'\bwhat is\b.*\bname\b', r'\bactor.*\bmovie\b',
        r'\birrelevant\b', r'\bcode to delete.*\bsystem\b', r'\bdelete.*\bfile.*\bsystem\b'
    ]
    
    for pattern in bug_patterns:
        if re.search(pattern, text):
            return "bug"
    
    for pattern in feature_patterns:
        if re.search(pattern, text):
            return "feature_request"
    
    for pattern in invalid_patterns:
        if re.search(pattern, text):
            return "invalid"
    
    return "product_issue"


def classify_product_area(text: str, company: str) -> str:
    area_keywords = {
        "testing": ["test", "assessment", "interview", "mock", "screen"],
        "account_management": ["account", "login", "password", "google login", "delete account"],
        "billing": ["billing", "payment", "refund", "subscription", "price"],
        "workspace_access": ["workspace", "team", "admin", "permission", "seats"],
        "conversation_management": ["conversation", "chat", "delete", "rename", "incognito"],
        "privacy": ["privacy", "data", "delete", "conversation"],
        "stolen_lost_card": ["stolen", "lost", "blocked", "card", "cheques"],
        "dispute": ["dispute", "charge", "merchant", "wrong product"],
        "usage_limits": ["limit", "usage", "rate", "quota", "timeout"],
        "technical_troubleshooting": ["not working", "broken", "error", "issue", "compatibility"]
    }
    
    company_areas = {
        "HackerRank": ["testing", "account_management", "mock_interviews", "screen", "hiring"],
        "Claude": ["workspace_access", "conversation_management", "account_management", "privacy"],
        "Visa": ["stolen_lost_card", "dispute", "billing", "usage_limits"],
        "None": ["technical_troubleshooting", "general"]
    }
    
    scores = {}
    for area, keywords in area_keywords.items():
        scores[area] = sum(1 for kw in keywords if kw in text)
    
    if company in company_areas:
        company_specific = company_areas[company]
        for area in company_specific:
            if scores.get(area, 0) > 0:
                return area
    
    best_area = max(scores.keys(), key=lambda k: scores[k]) if any(scores.values()) else "technical_troubleshooting"
    return best_area if scores[best_area] > 0 else "technical_troubleshooting"