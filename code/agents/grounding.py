"""
Grounding validator.
Ensures the retrieved chunks are relevant enough to justify calling the LLM.
"""

from config import MIN_SCORE, RETRIEVAL_THRESHOLD
from utils.logger import log_agent


def run(chunks: list[dict], query: str) -> dict | None:
	"""
	Return an escalation dict when retrieved context is too weak.
	Return None when the context is grounded enough to continue.
	"""
	if not chunks:
		log_agent("grounding", "ESCALATE — no retrieved chunks", {})
		return _escalate("G1-no-context", "No retrieval results were available.")

	top_score = float(chunks[0].get("score", 0))
	if top_score < MIN_SCORE:
		log_agent("grounding", "ESCALATE — low confidence retrieval", {"top_score": top_score})
		return _escalate(
			"G2-low-score",
			f"Top retrieval score {top_score:.3f} is below the minimum grounding threshold.",
		)

	if top_score < RETRIEVAL_THRESHOLD:
		log_agent("grounding", "PASS — weak but usable context", {"top_score": top_score})
	else:
		log_agent("grounding", "PASS — grounded context", {"top_score": top_score})

	return None


def _escalate(rule: str, reason: str) -> dict:
	return {
		"status": "escalated",
		"request_type": "invalid",
		"product_area": "unknown",
		"response": "Thank you for reaching out. Your issue requires attention from our specialist support team. A human agent will review your case and follow up with you shortly. Please do not re-submit this ticket.",
		"justification": f"[{rule}] {reason}",
		"rule_triggered": rule,
	}
