def classify(text):
    text = text.lower()

    if "hackerrank" in text:
        product = "hackerrank"
    elif "claude" in text:
        product = "claude"
    elif "visa" in text:
        product = "visa"
    else:
        product = "unknown"

    if any(x in text for x in ["payment", "charged", "refund"]):
        req = "billing"
    elif any(x in text for x in ["unauthorized", "fraud", "hacked"]):
        req = "fraud"
    elif any(x in text for x in ["login", "password", "account"]):
        req = "account"
    elif any(x in text for x in ["error", "bug", "issue"]):
        req = "bug"
    else:
        req = "faq"

    return product, req
