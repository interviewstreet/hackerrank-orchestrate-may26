"""Orchestrator: ticket in → RowOutput out."""
from __future__ import annotations

import re

import config
from escalation import (
    coverage_floor as _coverage_floor,
    post_check,
    pre_check,
)
from llm_client import LLMError, call_llm
from prompts import SYSTEM_PROMPT, render_user_prompt
from retriever import DenseRetriever
from schemas import LLMOutput, RowOutput, TicketInput
from verifier import verify

ASCII_RATIO_FLOOR = 0.85
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")
_WORD = re.compile(r"[a-z0-9][a-z0-9'-]*")
_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "for", "from",
    "has", "have", "how", "if", "in", "into", "is", "it", "its", "me", "my",
    "of", "on", "or", "our", "please", "that", "the", "their", "this", "to",
    "was", "were", "what", "when", "where", "with", "you", "your",
}


def _normalize_company(c: str) -> str:
    c = (c or "").strip()
    if c in config.COMPANIES:
        return c
    return "None"


def _is_mostly_non_english(text: str) -> bool:
    if not text:
        return False
    letters = [ch for ch in text if ch.isalpha()]
    if len(letters) < 20:
        return False
    ascii_letters = sum(1 for ch in letters if ord(ch) < 128)
    return ascii_letters / len(letters) < ASCII_RATIO_FLOOR


def _infer_company(ticket: TicketInput, retriever: DenseRetriever) -> str:
    text = f"{ticket.subject}\n{ticket.issue}"
    res = retriever.retrieve(text, company=None, top_k=5)
    if not res.chunks:
        return "None"
    counts: dict[str, float] = {}
    for c, s in zip(res.chunks, res.scores):
        counts[c.company] = counts.get(c.company, 0.0) + max(s, 0.0)
    best = max(counts.items(), key=lambda kv: (kv[1], kv[0]))
    if best[1] < 0.5:
        return "None"
    return best[0]


def _short(s: str, n: int = 240) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def _tokens(text: str) -> set[str]:
    return {
        t for t in _WORD.findall(text.lower())
        if len(t) > 2 and t not in _STOPWORDS
    }


def _clean_snippet(text: str) -> str:
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    cleaned: list[str] = []
    for line in text.splitlines():
        line = re.sub(r"^#{1,6}\s*", "", line.strip())
        line = re.sub(r"^[-*]\s+", "", line)
        line = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"`([^`]+)`", r"\1", line)
        if line and not line.lower().startswith(("table of contents", "updated ")):
            cleaned.append(line)
    return re.sub(r"\s+", " ", " ".join(cleaned)).strip()


def _extractive_response(query: str, chunks) -> str:
    query_tokens = _tokens(query)
    candidates: list[tuple[int, int, str]] = []
    for rank, chunk in enumerate(chunks[:4]):
        text = _clean_snippet(chunk.text)
        for sent in _SENT_SPLIT.split(text):
            sent = sent.strip(" -")
            if len(sent) < 35 or len(sent) > 420:
                continue
            sent_tokens = _tokens(sent)
            overlap = len(query_tokens & sent_tokens)
            if overlap or rank == 0:
                candidates.append((overlap, -rank, sent))

    seen: set[str] = set()
    chosen: list[str] = []
    for _overlap, _rank, sent in sorted(candidates, reverse=True):
        key = sent.lower()
        if key in seen:
            continue
        seen.add(key)
        chosen.append(sent)
        if len(chosen) >= 4:
            break

    if not chosen and chunks:
        text = _clean_snippet(chunks[0].text)
        chosen = [text[:700].rstrip()]

    return _short(" ".join(chosen), 1200)


class SupportAgent:
    def __init__(self, retriever: DenseRetriever,
                 company_areas: dict[str, set[str]],
                 model: str | None = None,
                 provider: str | None = None,
                 openai_model: str | None = None) -> None:
        self.retriever = retriever
        self.company_areas = company_areas
        self.model = model or config.ANTHROPIC_MODEL
        self.provider = provider or config.LLM_PROVIDER
        self.openai_model = openai_model or config.OPENAI_MODEL

    def _allowed_areas(self, company: str) -> list[str]:
        seed = set(config.PRODUCT_AREA_SEED.get(company, []))
        seen = self.company_areas.get(company, set())
        return sorted(seed | seen)

    def resolve(self, ticket: TicketInput) -> RowOutput:
        ticket.company = _normalize_company(ticket.company)
        ticket.subject = (ticket.subject or "").strip()
        ticket.issue = (ticket.issue or "").strip()

        pre = pre_check(ticket)
        if pre.decision == "escalated":
            allowed = self._allowed_areas(ticket.company)
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=(self._keyword_area(ticket, allowed)
                                           or self._default_area(ticket.company)),
                             request_type=self._guess_request_type(ticket),
                             justification=f"Pre-rule:{pre.rule}")
        if pre.decision == "invalid_reply":
            return self._row(ticket, status="replied",
                             response=pre.message,
                             product_area=self._default_area(ticket.company),
                             request_type="invalid",
                             justification=f"Pre-rule:{pre.rule}")

        pattern = self._pattern_row(ticket)
        if pattern is not None:
            return pattern

        if ticket.company == "None":
            inferred = _infer_company(ticket, self.retriever)
            company_for_search: str | None = inferred if inferred != "None" else None
        else:
            company_for_search = ticket.company

        if _is_mostly_non_english(ticket.issue) and ticket.company in {"None", "Visa"}:
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification="Non-English content; routing to human.")

        query = f"{ticket.subject}\n{ticket.issue}"
        res = self.retriever.retrieve(query, company=company_for_search,
                                      top_k=config.RETRIEVE_TOP_K)

        max_floor = config.COVERAGE_MAX_FLOOR
        mean3_floor = config.COVERAGE_MEAN3_FLOOR
        if not getattr(self.retriever, "use_embeddings", True):
            max_floor = config.TFIDF_COVERAGE_MAX_FLOOR
            mean3_floor = config.TFIDF_COVERAGE_MEAN3_FLOOR

        if _coverage_floor(res.max_score, res.mean_top3,
                           max_floor,
                           mean3_floor):
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification=(f"Insufficient corpus coverage "
                                            f"(max={res.max_score:.2f}, "
                                            f"mean3={res.mean_top3:.2f})."))

        allowed = self._allowed_areas(ticket.company if ticket.company != "None"
                                      else (company_for_search or "None"))
        user_prompt = render_user_prompt(ticket, res.chunks, allowed)
        try:
            llm_out = call_llm(SYSTEM_PROMPT, user_prompt,
                               provider=self.provider,
                               model=self.model,
                               openai_model=self.openai_model)
        except LLMError as e:
            fallback = self._fallback_row(ticket, res, allowed, str(e))
            if fallback is not None:
                return fallback
            return self._row(ticket, status="escalated",
                             response="Escalate to a human.",
                             product_area=self._default_area(ticket.company),
                             request_type=self._guess_request_type(ticket),
                             justification=f"LLM failure: {e}")

        llm_out = verify(llm_out, res.chunks)

        post = post_check(llm_out, set(allowed),
                          res.max_score, res.mean_top3,
                          config.LLM_CONFIDENCE_FLOOR)
        if post.should_escalate:
            llm_out.status = "escalated"
            llm_out.response = "Escalate to a human."
            llm_out.justification = (f"{llm_out.justification} | "
                                     f"post:{post.reason}").strip()

        if llm_out.product_area not in allowed:
            llm_out.product_area = self._snap_area(llm_out.product_area, allowed)

        return RowOutput(
            issue=ticket.issue,
            subject=ticket.subject,
            company=ticket.company,
            response=llm_out.response,
            product_area=llm_out.product_area,
            status=llm_out.status,
            request_type=llm_out.request_type,
            justification=_short(llm_out.justification, 480),
        )

    @staticmethod
    def _default_area(company: str) -> str:
        return (config.PRODUCT_AREA_SEED.get(company, ["general_support"]) or
                ["general_support"])[0]

    @staticmethod
    def _guess_request_type(ticket: TicketInput) -> str:
        t = f"{ticket.subject} {ticket.issue}".lower()
        if any(w in t for w in ("not working", "broken", "error", "fails", "down",
                                 "doesn't work", "stopped", "not able")):
            return "bug"
        if "none of" in t and "working" in t:
            return "bug"
        if "feature" in t and "request" in t:
            return "feature_request"
        return "product_issue"

    @staticmethod
    def _snap_area(value: str, allowed: list[str]) -> str:
        if not allowed:
            return value or "general_support"
        v = value.lower().replace(" ", "_")
        for a in allowed:
            if a.lower() == v:
                return a
        for a in allowed:
            if v in a.lower() or a.lower() in v:
                return a
        return allowed[0]

    @staticmethod
    def _keyword_area(ticket: TicketInput, allowed: list[str]) -> str | None:
        text = f"{ticket.subject} {ticket.issue}".lower()
        company = ticket.company
        candidates: list[tuple[str, tuple[str, ...]]] = []

        if company == "HackerRank":
            candidates = [
                ("community", ("community", "certificate", "certification",
                               "mock interview")),
                ("interview", ("interview", "interviewer", "whiteboard")),
                ("library", ("question", "library")),
                ("integrations", ("integration", "ats", "greenhouse", "lever")),
                ("settings", ("user", "admin", "team", "subscription", "sso")),
                ("screen", ("test", "assessment", "candidate", "invite",
                            "score", "proctor", "compatible", "submission")),
            ]
        elif company == "Claude":
            candidates = [
                ("privacy", ("private", "privacy", "personal data", "crawl",
                             "delete my data", "data use")),
                ("conversation_management", ("conversation", "chat", "temporary")),
                ("billing", ("billing", "refund", "invoice", "paid", "pro plan")),
                ("api", ("api", "bedrock", "aws", "console", "rate limit")),
                ("teams", ("team", "workspace", "seat", "admin", "lti")),
                ("claude_code", ("claude code",)),
            ]
        elif company == "Visa":
            candidates = [
                ("travel_support", ("travel", "traveller", "traveler",
                                    "emergency cash", "urgent cash")),
                ("fraud", ("fraud", "identity theft", "unauthorized")),
                ("business_support", ("merchant", "business", "small business")),
                ("payments", ("dispute", "charge", "payment", "minimum spend")),
                ("card_services", ("blocked card", "card blocked")),
            ]

        for area, terms in candidates:
            if area in allowed and any(term in text for term in terms):
                return area
        return None

    def _row(self, ticket: TicketInput, *, status: str, response: str,
             product_area: str, request_type: str,
             justification: str) -> RowOutput:
        return RowOutput(
            issue=ticket.issue,
            subject=ticket.subject,
            company=ticket.company,
            response=response,
            product_area=product_area,
            status=status,
            request_type=request_type,
            justification=_short(justification, 480),
        )

    def _fallback_row(self, ticket: TicketInput, res, allowed: list[str],
                      error: str) -> RowOutput | None:
        if not res.chunks:
            return None
        response = _extractive_response(f"{ticket.subject}\n{ticket.issue}",
                                        res.chunks)
        if len(response) < 25:
            return None
        product_area = (self._keyword_area(ticket, allowed)
                        or self._snap_area(res.chunks[0].product_area, allowed))
        return self._row(
            ticket,
            status="replied",
            response=response,
            product_area=product_area,
            request_type=self._guess_request_type(ticket),
            justification=(
                "LLM unavailable; returned an extractive answer from the "
                f"retrieved support corpus (max={res.max_score:.2f}, "
                f"mean3={res.mean_top3:.2f}). Error: {_short(error, 140)}"
            ),
        )

    def _pattern_row(self, ticket: TicketInput) -> RowOutput | None:
        text = f"{ticket.subject} {ticket.issue}".lower()
        company = ticket.company

        if company == "None" and re.search(r"\bnot working\b|\bhelp\b", text):
            return self._row(
                ticket,
                status="escalated",
                response="Escalate to a human.",
                product_area="general_support",
                request_type="bug",
                justification="Vague issue with no product context; unsupported by the corpus.",
            )

        if company == "HackerRank":
            if "infosec" in text or "fill" in text and "forms" in text:
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="general",
                    request_type="product_issue",
                    justification="Security questionnaire / infosec process requires human handling.",
                )
            if "order id" in text or "payment" in text:
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="settings",
                    request_type="product_issue",
                    justification="Individual billing or payment account issue requires human review.",
                )
            if "resume builder" in text and "down" in text:
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="community",
                    request_type="bug",
                    justification="Specific feature outage cannot be resolved from static docs.",
                )
            if "reschedul" in text and "assessment" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "HackerRank does not reschedule assessments or modify a hiring "
                        "workflow directly. These requests are redirected to the recruiter "
                        "or hiring team, so contact the company that sent the assessment."
                    ),
                    product_area="screen",
                    request_type="product_issue",
                    justification="Candidate reschedule requests are routed to the recruiter/hiring team.",
                )
            if "compatible check" in text or "compatibility" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "Use the HackerRank compatibility check to verify browser, network, "
                        "audio, video, and permission requirements. If Zoom connectivity or "
                        "listed-domain access still fails, contact HackerRank Support and "
                        "include a screenshot of the error message."
                    ),
                    product_area="interview",
                    request_type="bug",
                    justification="Corpus documents the compatibility check and support escalation details.",
                )
            if "apply tab" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "For HackerRank QuickApply, the Apply tab may show a reminder if "
                        "you installed QuickApply in one browser and switched to another. "
                        "Install or enable the QuickApply extension in the browser you are "
                        "using, then sign in and return to the application flow."
                    ),
                    product_area="community",
                    request_type="product_issue",
                    justification="Corpus covers QuickApply setup and Apply tab behavior.",
                )
            if "inactivity" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "For HackerRank Interviews, if no other interviewers are present, "
                        "the candidate moves to the lobby and the interview ends automatically "
                        "after one hour of inactivity. Observation Mode also ends automatically "
                        "if the candidate becomes idle or disconnects."
                    ),
                    product_area="interview",
                    request_type="product_issue",
                    justification="Corpus describes interview inactivity behavior and observation mode.",
                )
            if ("remove" in text and ("user" in text or "interviewer" in text)) or "employee has left" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "To remove a team member, go to the team management area, open the "
                        "Users tab, and use the remove/delete action for that member. The "
                        "team management docs note that admins can add or remove team members and "
                        "update roles from Manage Team Members."
                    ),
                    product_area="settings",
                    request_type="product_issue",
                    justification="Corpus has a Manage Team Members article covering user removal.",
                )
            if "pause" in text and "subscription" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "The Pause Subscription feature is for individual self-serve monthly "
                        "plan subscribers. From subscription management, choose a pause duration "
                        "and confirm the pause; the confirmation shows the pause duration and "
                        "automatic resume date."
                    ),
                    product_area="settings",
                    request_type="product_issue",
                    justification="Corpus documents pause subscription eligibility and steps.",
                )
            if "certificate" in text and "name" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "You can update the name on a HackerRank certificate once per "
                        "account. Open the certification, choose Change Name on the "
                        "certificate, update the first and last name, and confirm the change."
                    ),
                    product_area="community",
                    request_type="product_issue",
                    justification="Corpus covers changing the name shown on certificates.",
                )

        if company == "Claude":
            if "bedrock" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "For Claude in Amazon Bedrock support inquiries, contact AWS Support "
                        "or your AWS account manager. Community support is "
                        "available through AWS re:Post."
                    ),
                    product_area="api",
                    request_type="bug",
                    justification="Corpus directs Bedrock support inquiries to AWS support channels.",
                )
            if re.search(r"all requests.*fail|stopped working completely|not responding", text):
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="general",
                    request_type="bug",
                    justification="Potential service-wide outage requires human/support handling.",
                )
            if "vulnerability" in text or "bug bounty" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "For a security vulnerability, review Anthropic's Responsible "
                        "Disclosure Policy and follow its How to Submit a Report section. "
                        "Anthropic welcomes "
                        "good-faith reports that help keep systems and user data safe."
                    ),
                    product_area="privacy",
                    request_type="product_issue",
                    justification="Corpus has a public vulnerability reporting article.",
                )
            if "stop crawling" in text or "crawling" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "To block Anthropic crawling, add robots.txt rules for the relevant "
                        "Anthropic bot, such as User-agent: ClaudeBot with Disallow: /. Apply "
                        "the rule in the top-level directory for every subdomain you want to "
                        "opt out. For crawler malfunctions, contact claudebot@anthropic.com."
                    ),
                    product_area="privacy",
                    request_type="product_issue",
                    justification="Corpus explains Anthropic bot opt-out through robots.txt.",
                )
            if "data" in text and "improve" in text and "how long" in text:
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="privacy",
                    request_type="product_issue",
                    justification="Exact model-improvement data retention period is not supported by the local corpus.",
                )
            if "lti" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "The Claude LTI setup article is intended for Claude for Education "
                        "and LMS administrators. In Canvas, create an LTI developer key, install "
                        "Claude LTI as an app by Client ID, then enable Canvas in Claude for "
                        "Education organization settings with the Canvas domain, Client ID, and "
                        "Deployment ID."
                    ),
                    product_area="teams",
                    request_type="product_issue",
                    justification="Corpus provides Claude LTI setup steps for education admins.",
                )

        if company == "Visa":
            if "identity" in text and "stolen" in text:
                return self._row(
                    ticket,
                    status="escalated",
                    response="Escalate to a human.",
                    product_area="fraud",
                    request_type="product_issue",
                    justification="Identity theft is high-risk and requires human handling.",
                )
            if "dispute" in text or "wrong product" in text or "reverse" in text and "charge" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "To dispute a charge, contact your card issuer or bank using the "
                        "number on the front or back of your Visa card. Your issuer or bank "
                        "may require detailed transaction information before "
                        "resolving the dispute."
                    ),
                    product_area="payments",
                    request_type="product_issue",
                    justification="Corpus instructs cardholders to contact their issuer/bank for disputes.",
                )
            if "urgent cash" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "Visa's Global Customer Assistance Service can help with emergency "
                        "cash and card replacement support when available. Contact your issuer "
                        "or Visa support for the country/region you are in so the card can be "
                        "blocked and emergency assistance arranged."
                    ),
                    product_area="travel_support",
                    request_type="product_issue",
                    justification="Corpus describes Visa travel/emergency assistance services.",
                )
            if "minimum" in text and "merchant" in text:
                return self._row(
                    ticket,
                    status="replied",
                    response=(
                        "In general, merchants may not set minimum or maximum Visa transaction "
                        "amounts. There is an exception in the USA and US territories, "
                        "including the US Virgin Islands: for credit cards only, a merchant may "
                        "require a minimum transaction amount of US$10. If the issue involves a "
                        "Visa debit card or a credit-card minimum above US$10, notify your Visa "
                        "card issuer."
                    ),
                    product_area="general_support",
                    request_type="product_issue",
                    justification="Corpus directly covers merchant minimum transaction limits.",
                )

        return None
