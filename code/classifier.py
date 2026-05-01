import re
from typing import Optional, List, Dict, Tuple


def infer_company(issue: str, subject: str = "") -> Optional[str]:
    text = (issue + " " + subject).lower()

    hackerrank_keywords = [
        "hackerrank", "test", "assessment", "recruiter", "candidate",
        "coding challenge", "hired", "interview", "score", "report"
    ]
    claude_keywords = [
        "claude", "bedrock", "anthropic", "api", "model", "prompt",
        "tokens", "inference", "deployment"
    ]
    visa_keywords = [
        "visa", "payment", "transaction", "card", "merchant", "dispute",
        "chargeback", "settlement", "processor"
    ]

    hackerrank_score = sum(1 for kw in hackerrank_keywords if kw in text)
    claude_score = sum(1 for kw in claude_keywords if kw in text)
    visa_score = sum(1 for kw in visa_keywords if kw in text)

    max_score = max(hackerrank_score, claude_score, visa_score)
    if max_score == 0:
        return None

    if hackerrank_score == max_score:
        return "HackerRank"
    elif claude_score == max_score:
        return "Claude"
    else:
        return "Visa"


def classify_request_type(issue: str) -> str:
    issue_lower = issue.lower()

    invalid_patterns = [
        r"hate|racism|discrimination",
        r"spam|scam|phishing",
        r"harassment|abuse|violence",
        r"adult|explicit|nsfw"
    ]
    if any(re.search(pattern, issue_lower) for pattern in invalid_patterns):
        return "invalid"

    feature_patterns = [
        r"can you add|could you implement|would like to have|feature request",
        r"it would be great if|we need|please add|feature",
        r"enhancement|improvement|new feature|add.*support",
        r"dark mode"
    ]
    if any(re.search(pattern, issue_lower) for pattern in feature_patterns):
        return "feature_request"

    bug_patterns = [
        r"bug|broken|crash|error|fail|not working",
        r"doesn't work|not able to|unable to",
        r"problem with|issue with|stopped working"
    ]
    if any(re.search(pattern, issue_lower) for pattern in bug_patterns):
        return "bug"

    return "product_issue"


def should_escalate(issue: str, request_type: str, docs: List[Dict]) -> Tuple[bool, str]:
    issue_lower = issue.lower()

    if request_type == "invalid":
        return True, "Content violation or invalid request"

    sensitive_patterns = [
        r"access denied|permission denied|restore.*access",
        r"suspended|banned|locked|disabled account",
        r"billing|payment|invoice|refund|charge",
        r"fraud|dispute|chargeback",
        r"password|reset|two.?factor|authentication",
        r"personal.*info|ssn|tax id|credit card"
    ]
    if any(re.search(pattern, issue_lower) for pattern in sensitive_patterns):
        return True, "Sensitive or permission-related issue requires human review"

    if not docs or (len(docs) == 1 and docs[0].get("score", 0) < 0.3):
        return True, "No relevant documentation found in corpus"

    multi_topic_indicators = issue.count("?") > 2 or issue.count(";") > 1
    if multi_topic_indicators:
        return True, "Multiple unrelated topics detected"

    if request_type in ["feature_request", "bug"]:
        high_relevance_docs = [d for d in docs if d.get("score", 0) > 0.6]
        if not high_relevance_docs:
            return True, f"Cannot resolve {request_type} with available documentation"

    return False, ""
