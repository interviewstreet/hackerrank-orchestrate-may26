# Agent Roles and Personas

Four pipeline components process every ticket. Three are LLM agents; one is deterministic code. Each has a single, non-overlapping responsibility. No component is permitted to perform a task that belongs to another.

---

## Gatekeeper

**Type**: Deterministic pipeline code — no LLM call  
**Invoked**: First, before any agent  
**Features owned**: F1 (input validation and truncation)

### Responsibilities

- Validate that all three input fields (`issue`, `subject`, `company`) are present and string-typed.
- Truncate `issue` + `subject` combined to a maximum of 2 000 characters before any downstream processing. **Truncation priority: always preserve at least the first 200 chars of `issue` before allocating the remaining budget to `subject`.** (FM-G2)
- Constrain `company` to `{HackerRank, Claude, Visa, None}`; treat any other value as `None`. **Normalize to title-case before the enum check so `"hackerrank"` and `"VISA"` are accepted correctly.** (FM-G3)
- On a schema error (e.g., unparsable CSV row), emit an `escalated` row and continue to the next ticket.

### Constraints

- Must NOT call any LLM. Input validation is deterministic.
- Read the CSV with `errors='replace'` encoding handling — non-UTF-8 bytes become replacement characters; log when replacement occurs. (FM-G1)
- Passes all valid tickets through to Scout regardless of content — classification of adversarial or off-topic inputs is Scout's responsibility.

---

## Scout

**Type**: LLM agent  
**Model**: `google/gemini-2.0-flash-lite` via OpenRouter  
**Invoked**: Second, after Gatekeeper passes the ticket  
**Features owned**: F1 (company inference, multi-request detection), F2 (domain routing for `company=None`), F5 partial (`request_type`, `product_area`)

### Responsibilities

- Extract individual sub-requests from the ticket. Each sub-request is classified with its own `request_type` and `product_area` and will produce a separate output row.
  - `request_type` valid values: `product_issue` | `feature_request` | `bug` | `invalid`
  - `product_area` is inferred from corpus section names (directory names and heading structure within `data/hackerrank/`, `data/claude/`, `data/visa/`); e.g. `billing`, `account_access`, `screen`, `travel_support`, `privacy`, `general_support`
  - Adversarial or off-topic inputs are classified as `request_type=invalid`
- When `company` is `None`, infer the most likely company from ticket content by matching vocabulary, product names, and context against all three corpora. Output an `inferred_company`.

### Input

```json
{
  "issue": "<ticket body>",
  "subject": "<ticket subject>",
  "company": "<HackerRank|Claude|Visa|None>"
}
```

### Output (structured JSON)

```json
{
  "inferred_company": "<HackerRank|Claude|Visa|None>",
  "sub_requests": [
    {
      "issue_excerpt": "<the specific sub-request text>",
      "request_type": "product_issue|feature_request|bug|invalid",
      "product_area": "<corpus section name>"
    }
  ]
}
```

A single-request ticket produces `sub_requests` with exactly one item. Each item in `sub_requests` drives one Sentinel + Anchor cycle and one output row.

### Constraints

- Output must be valid JSON matching the schema above — no free text.
- `temperature=0` required.
- Must NOT make escalation decisions — that is Sentinel's role.
- Must NOT retrieve from corpus — that is Anchor's role.

---

## Sentinel

**Type**: LLM agent  
**Model**: `anthropic/claude-haiku-4-5` via OpenRouter  
**Invoked**: Third, after Scout  
**Features owned**: F4 (escalation decision engine), F5 partial (`status`, `justification`)

### Responsibilities

- Apply escalation rules to decide `replied` vs `escalated`:
  - **Always escalate** when `request_type` indicates: fraud, unauthorized account access, financial disputes, data loss, security vulnerabilities, service outages.
  - **Always escalate** when the ticket is ambiguous about what action is requested and the corpus cannot provide confident grounding.
  - **Always reply** when `request_type = invalid` (out-of-scope tickets receive an out-of-scope message, never escalation).
  - **Always reply** when the ticket is a clear FAQ with a direct corpus match.
- Produce a `justification` (1–3 sentences) citing the escalation rule applied or the reason the ticket is safe to answer.
- When status is `escalated`, the `justification` explains why human review is required.

### Input

```json
{
  "issue": "<ticket body>",
  "subject": "<ticket subject>",
  "company": "<resolved company>",
  "request_type": "<Scout output>",
  "product_area": "<Scout output>"
}
```

### Output (structured JSON)

```json
{
  "status": "replied|escalated",
  "justification": "<1-3 sentences>"
}
```

### Constraints

- Output must be valid JSON matching the schema above — no free text.
- `temperature=0` required.
- Must NOT generate the user-facing `response` field — that is Anchor's role.
- Escalation message text is hardcoded by Orchestrator; Sentinel never writes the escalation response body.
- Must NOT perform retrieval — that is Anchor's role.
- `justification` must name the **specific escalation trigger** and quote the ticket text that triggered it (e.g. `"Ticket mentions 'I didn't authorize this charge' — fraud escalation rule applied"`). Generic justifications like "Ticket escalated due to policy" are not acceptable. (FM-SE2)

---

## Anchor

**Type**: LLM agent  
**Model**: `google/gemini-2.5-flash` via OpenRouter  
**Invoked**: Fourth, **only when Sentinel returns `status=replied`**  
**Features owned**: F3 (retrieval), F7 (anti-hallucination), F5 partial (`response`)

### Responsibilities

- Retrieve the top-k most relevant corpus chunks from `data/<resolved_company>/` using the ticket's `product_area` and `issue` as the query.
- For `inferred_company=None` (no confident company inference), retrieve from all three corpora and select best-matching chunks by relevance score.
- Generate a grounded user-facing `response` using **only** the retrieved corpus chunks. No parametric model knowledge may be used to answer the ticket.
- Supplement the `justification` with the source document cited (e.g. "Source: `data/hackerrank/billing.md`").
- Set `grounded=false` in output if the top retrieved corpus chunk has cosine similarity < **0.65** — this signals the Orchestrator to override `replied → escalated`.

### Input

```json
{
  "issue": "<ticket body>",
  "subject": "<ticket subject>",
  "resolved_company": "<HackerRank|Claude|Visa>",
  "product_area": "<Scout output>",
  "corpus_chunks": ["<chunk 1>", "<chunk 2>", "..."]
}
```

### Output (structured JSON)

```json
{
  "response": "<user-facing reply grounded in corpus>",
  "source_doc": "data/<company>/<filename>.md",
  "grounded": true
}
```

### Prompt engineering — company-aware persona

Anchor's system prompt is built dynamically at call time by `_build_system_prompt(resolved_company)`. It has three layers:

**1. Company-specific role (persona)**

| Company | Role injected at top of system prompt |
| --- | --- |
| `HackerRank` | "You are a friendly HackerRank support specialist. You help developers, recruiters, and hiring teams with technical assessments, coding challenges, interviews, and the HackerRank hiring platform." |
| `Claude` | "You are a friendly Anthropic support specialist. You help users with Claude AI products — including Claude.ai, billing, account management, the Claude API, Claude Code, and enterprise plans." |
| `Visa` | "You are a friendly Visa support specialist. You help cardholders, small business owners, and travelers with Visa payment products, card benefits, and financial services." |
| `None` | "You are a friendly support specialist for HackerRank, Claude (Anthropic), and Visa products." |

This anchors the model's voice and vocabulary to the correct brand before any corpus context is injected.

**2. Retrieved corpus context**

The top-k chunks from Qdrant (already pre-filtered by company) are appended verbatim to the user message, separated by `---` dividers. Each chunk is prefixed with its `source_doc` path so the model can cite it in `source_doc` output.

**3. Tone and style constraints** (enforced in system prompt)

- Open by acknowledging the customer's issue before providing the solution.
- Write in plain, everyday language — no jargon, acronyms, or corporate-speak.
- Respond in 2–4 short paragraphs; use bullet points only when listing 3 or more steps.
- Never open with hollow affirmations ("Certainly!", "Of course!", "Great question!").
- Close with a short, one-sentence offer to help further.

**Why this structure matters**

Without a branded persona, the model defaults to a generic assistant voice that sounds impersonal and inconsistent across companies. The role definition sets the right vocabulary and brand tone before the corpus context is read, so the model interprets the chunks as a support agent for that company rather than as a neutral summarizer.

### Constraints

- `temperature=0` required.
- `thinkingBudget: 0` (or equivalent) — Gemini thinking tokens are unbilled only when disabled; leaving it on can 2–3× output costs unexpectedly.
- Must NOT fabricate any policy, step, or fact not present in the retrieved corpus chunks.
- Must NOT make routing or escalation decisions.
- If `grounded=false`, Orchestrator ignores `response` and writes the hardcoded escalation message instead.
- Do NOT include document headings, file paths, section numbers, or any corpus structure markers (e.g. `## Section 3`, `data/hackerrank/screen.md`) in the `response` body. Write only clean, user-facing prose. (FM-A2)

### Retrieval implementation note

Corpus retrieval is performed via Qdrant with a mandatory `company` metadata pre-filter applied before vector similarity computation. This prevents cross-domain contamination at the retrieval level. Chroma was considered but rejected because it applies filters post-hoc (after computing similarity against the full index), which would allow wrong-domain chunks to rank highly before being discarded. With Qdrant, the search space is narrowed to the correct company corpus before any cosine math runs.

---

## Verifier

**Type**: LLM agent  
**Model**: `google/gemini-2.0-flash-lite` via OpenRouter  
**Invoked**: Fifth, **only when Anchor returns `grounded=true`**  
**Features owned**: F9 (post-generation verification)

### Responsibilities

- Re-read the original `issue_excerpt` and Anchor's `response` side-by-side and answer: "Does this response actually address what the customer asked?"
- Produce a `verified` boolean and a `verification_confidence` score (0.0–1.0)
- If `verified=false` or `verification_confidence < 0.60`, the Orchestrator discards the response and overrides `status → escalated`

This stage is the semantic quality gate. It catches cases where Anchor retrieved a corpus chunk that is topically related but does not actually solve the customer's specific problem — for example, retrieving a general "how to reset password" article in response to a specific "I reset my password but my old sessions are still active" question.

### What the Verifier checks

| Check | Description |
| --- | --- |
| Issue coverage | Does the response address all parts of the sub-request? |
| Actionability | Does the response give the customer something they can actually do? |
| Accuracy fit | Does the response make sense in context of the specific issue, not just the topic? |

### What the Verifier does NOT do

- Does not re-classify the ticket (Scout's job)
- Does not make escalation policy decisions (Sentinel's job)
- Does not retrieve additional corpus content
- Does not rewrite or improve the response — it either approves or rejects

### Input

```json
{
  "request_id": "<req_007_1_...>",
  "issue_excerpt": "<the specific sub-request text>",
  "response": "<Anchor's proposed response>",
  "source_doc": "data/<company>/<filename>.md"
}
```

### Output (structured JSON)

```json
{
  "verified": true,
  "verification_confidence": 0.85,
  "verification_reason": "Response directly addresses the password reset question with step-by-step instructions matching the issue."
}
```

### Constraints

- `temperature=0` required.
- Output must be valid JSON — if malformed after one retry, default to `verified=false`.
- Must NOT rewrite, modify, or supplement the response.
- Must NOT escalate independently — it signals `verified=false` and the Orchestrator takes the escalation action.
- Threshold is **0.60** — confidence below this escalates. The threshold is deliberately conservative: a response that only "probably" helps is not good enough.

---

## Orchestrator

**Type**: Deterministic pipeline code — no LLM call  
**Invoked**: Wraps the entire pipeline  
**Features owned**: F6 (output writing), F8 (CLI entry point), pipeline coordination

### Responsibilities

- Parse `support_tickets/support_tickets.csv` row by row.
- Drive the sequential pipeline: Gatekeeper → Scout → Sentinel → (conditional) Anchor.
- Pass structured JSON outputs between pipeline stages.
- Resolve `company`: use Scout's `inferred_company` when input `company=None`.
- On `status=escalated` (from Sentinel) or `grounded=false` (from Anchor), write `"Escalate to a human"` to `response`.
- Assemble the final 5-field row: `{status, product_area, response, justification, request_type}` for each sub-request.
- Write all rows to `support_tickets/output.csv`; multi-request tickets produce multiple consecutive rows, preserving input ticket order and sub-request order within each ticket.
- Exit `0` on success; non-zero with stderr message on failure.

### Constraints

- Must NOT call any LLM directly.
- Must preserve input row order in output.
- Must write one output row per sub-request; multi-request tickets produce multiple consecutive rows in `output.csv`.
