def classify(text):
    t = text.lower()

    # 🔴 Billing / money issues
    if any(k in t for k in ["bill", "charge", "payment", "refund", "money"]):
        return "product_issue", "billing"

    # 🔐 Account / login issues (refined)
    elif any(k in t for k in ["login", "password", "sign in"]):
        return "product_issue", "account"

    elif "access" in t:
        return "product_issue", "account"

    # ⚙️ Technical bugs
    elif any(k in t for k in ["error", "bug", "not working", "failed", "issue", "problem", "down", "failing"]):
        return "bug", "technical"

    # 💡 Feature requests
    elif any(k in t for k in ["feature", "request", "add", "improve"]):
        return "feature_request", "general"

    # 🚨 Security / fraud
    elif any(k in t for k in ["stolen", "fraud", "unauthorized", "hacked"]):
        return "product_issue", "security"

    # ❌ Truly invalid
    elif any(k in t for k in ["delete all files", "give me code to hack"]):
        return "invalid", "other"

    # ✅ Default
    else:
        return "product_issue", "general"