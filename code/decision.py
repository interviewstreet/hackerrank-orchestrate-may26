def should_escalate(req_type, score):
    if req_type in ["fraud", "billing", "account"]:
        return True
    if score < 0.2:
        return True
    return False
