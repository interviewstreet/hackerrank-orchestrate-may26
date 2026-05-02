def contains_phrase(query, phrases):
    return any(p in query for p in phrases)

def contains_word_pattern(query, patterns):
    words = set(query.split())
    return any(all(w in words for w in group) for group in patterns)


def decide(results, request_type, company, query):
    query = query.lower()

    if not results:
        return "escalated", "No relevant documentation found in support corpus"

    top_result = results[0]
    top_score = results[0]["score"]
    text = top_result["text"].lower()

    # 🔴 Keyword groups
    security_keywords = ["stolen", "fraud", "unauthorized", "hacked", "identity"]
    billing_keywords = ["refund", "charge", "payment", "billing", "money"]

    control_keywords = [
        "increase my score", "change result", "review my answers",
        "move me to next round", "reschedule", "extend",
        "approve", "ban", "restore access"
    ]

    permission_keywords = ["access removed", "lost access", "no permission"]
    compliance_keywords = ["infosec", "compliance", "forms"]
    informational_keywords = ["how long", "what is", "why", "explain"]

    # 🔴 Admin detection
    admin_phrase_patterns = [
        "remove employee", "remove user", "delete user",
        "remove interviewer", "remove from account"
    ]

    admin_word_patterns = [
        ["employee", "remove"],
        ["user", "remove"],
        ["account", "remove"],
        ["employee", "left"]
    ]

    is_admin_action = (
        contains_phrase(query, admin_phrase_patterns) or
        contains_word_pattern(query, admin_word_patterns)
    )

    # 🔴 Subscription detection
    is_subscription = (
        "subscription" in query and any(w in query for w in ["pause", "cancel", "stop"])
    )

    # 🔴 Extra detection
    is_vulnerability = any(k in query for k in ["vulnerability", "security issue", "security bug"])
    is_cash = any(k in query for k in ["cash", "need money", "urgent money"])

    combined_text = query + " " + text

    is_security = any(k in combined_text for k in security_keywords)
    is_billing = any(k in query for k in billing_keywords)
    is_control = any(k in query for k in control_keywords)
    is_permission = any(k in query for k in permission_keywords)
    is_compliance = any(k in query for k in compliance_keywords)
    is_informational = any(k in query for k in informational_keywords)

    # =========================
    # 🔴 HARD ESCALATION
    # =========================

    # Visa strict handling
    if company == "visa" and (is_security or is_billing):
        return "escalated", f"Sensitive financial/security issue (score {top_score:.2f})"

    # Visa financial urgency
    if company == "visa" and is_cash:
        return "escalated", f"Financial assistance request requires support (score {top_score:.2f})"

    # Security vulnerability
    if is_vulnerability:
        return "escalated", f"Security vulnerability requires escalation (score {top_score:.2f})"

    # Subscription control
    if is_subscription:
        return "escalated", f"Subscription control requires support (score {top_score:.2f})"

    # Admin actions
    if is_admin_action:
        return "escalated", f"Admin action requires intervention (score {top_score:.2f})"

    # Permission issues
    if is_permission:
        return "escalated", f"Permission issue requires support (score {top_score:.2f})"

    # Security issues
    if is_security:
        return "escalated", f"Security issue requires support (score {top_score:.2f})"

    # Billing issues
    if is_billing:
        return "escalated", f"Billing issue requires support (score {top_score:.2f})"

    # Compliance issues
    if is_compliance:
        return "escalated", f"Compliance-related request (score {top_score:.2f})"

    # Control requests
    if is_control:
        return "escalated", f"Administrative request (score {top_score:.2f})"

    # =========================
    # ⚠️ INFORMATIONAL
    # =========================

    if is_informational and top_score >= 0.2:
        return "replied", f"Answered using documentation (score {top_score:.2f})"

    # =========================
    # ⚠️ CONFIDENCE
    # =========================

    if top_score < 0.2:
        return "escalated", f"Low confidence (score {top_score:.2f})"

    if request_type == "bug" and top_score < 0.4:
        return "escalated", f"Technical issue unclear (score {top_score:.2f})"

    # =========================
    return "replied", f"Relevant documentation match (score {top_score:.2f})"