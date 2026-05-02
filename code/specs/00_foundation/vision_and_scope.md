# Vision and Scope

## Project Vision

Build a terminal-based, multi-domain support triage agent that processes customer support tickets for HackerRank, Claude, and Visa by retrieving grounded answers exclusively from the provided support corpus, classifying each ticket, and deciding whether to reply directly or escalate to a human — with zero hallucination, zero fabricated policies, and semantically stable, reproducible output (same routing and classification decisions across runs; exact string identity is not guaranteed due to LLM non-determinism).

---

## Problem Statement

### What problem does this solve?

Support teams at HackerRank, Claude (Anthropic), and Visa receive high volumes of tickets spanning billing, bugs, account access, fraud, product usage, and out-of-scope requests. Manually triaging, classifying, and responding to each ticket is slow, error-prone, and inconsistent. Incorrect responses — especially in high-risk domains like fraud, billing, or account deletion — cause serious harm.

### Why does it matter?

- **Scale**: Production support queues exceed what human agents can handle without automation.
- **Accuracy**: Support agents hallucinate policies or give outdated information; the agent must be grounded in authoritative documentation.
- **Safety**: Some tickets (fraud, account compromise, billing disputes) must never receive automated responses — they require human escalation.
- **Noise elimination**: Adversarial or obviously illegitimate inputs (prompt injections, gibberish, off-topic requests) must be classified as `invalid` by Scout and resolved with an out-of-scope reply — never left untracked.
- **Consistency**: Every identical ticket should receive the same quality classification and response regardless of human agent variability.

### The core tension the agent must navigate

Reply with a helpful, corpus-grounded answer when confident. Escalate to a human immediately when the ticket is high-risk, ambiguous, out-of-scope, or unsupported by the corpus. Never guess when unsure.

---

## Target Users

### Primary users (consumers of agent output)

| User                    | Need                                                                 |
| ----------------------- | -------------------------------------------------------------------- |
| Support operations team | Automated, consistent first-pass triage of ticket queues             |
| Human escalation agents | Clear escalation justification so they know exactly what to handle   |
| Hackathon evaluator     | A runnable CLI that produces `output.csv` from `support_tickets.csv` |

### Indirect users

| User                                         | Need                                                                   |
| -------------------------------------------- | ---------------------------------------------------------------------- |
| End customers (HackerRank/Claude/Visa users) | Accurate, helpful support responses grounded in official documentation |
| Engineering teams                            | Reproducible runs with pinned dependencies and seeded sampling         |

### What users are NOT served by this project

- Internal HR or IT helpdesk tickets
- Sales or marketing inquiries
- Live chat or real-time support (this is batch processing)

---

## Key Objectives

1. **Grounded response generation**: Every agent reply must be traceable to a specific document in `data/`. The agent must never produce information that cannot be attributed to the corpus.

2. **Accurate triage classification**: The agent must correctly classify each ticket across all five output fields (`status`, `product_area`, `response`, `justification`, `request_type`).

3. **Safe escalation logic**: High-risk tickets (fraud, billing disputes, account compromise, bugs causing data loss, or any ticket where the corpus provides insufficient grounding) must be escalated, never guessed at.

4. **Multi-domain routing**: The agent must correctly handle tickets tagged to HackerRank, Claude, Visa, or `None` (ambiguous/cross-domain), routing retrieval to the correct sub-corpus.

5. **Semantically stable, reproducible execution**: Given the same input CSV, the agent must produce semantically equivalent decisions in `output.csv` across runs — the same ticket must not resolve as `replied` in one run and `escalated` in another, and the substantive meaning of any generated response must remain consistent. LLM sampling must use `temperature=0` and all dependencies must be pinned. Correctness is measured by semantic content — routing decisions, classification labels, and response meaning — not by byte-for-byte string identity.

---

## Core Features

### F1 — Input parsing

- Read `support_tickets/support_tickets.csv` with fields: `issue`, `subject`, `company`
- Handle blank, noisy, or irrelevant `subject` fields gracefully
- Handle multi-request tickets (a single `issue` may contain more than one question); Scout extracts each sub-request individually, and each sub-request produces a separate output row in `output.csv`
- Pass all inputs through the classification pipeline; adversarial or off-topic inputs are classified as `request_type=invalid` by Scout and receive an out-of-scope reply

### F2 — Multi-domain corpus router

- Map `company` field to the correct corpus sub-directory:
  - `HackerRank` → `data/hackerrank/`
  - `Claude` → `data/claude/`
  - `Visa` → `data/visa/`
  - `None` → search all three corpora; select best match by relevance score
- Each corpus has an `index.md` file listing available documentation

### F3 — Retrieval pipeline

- Retrieve the most relevant support documentation from the routed corpus
- Retrieval must be grounded: no knowledge outside `data/` may be used to answer tickets
- Retrieval strategy must support both keyword-dense and semantically paraphrased queries
- Return top-k relevant chunks with source attribution

### F4 — Escalation decision engine

- Apply escalation rules before generating any response
- **Always escalate** when:
  - Ticket involves fraud, unauthorized account access, or contested/unauthorized financial charges (billing disputes where the customer is challenging a charge)
  - Ticket involves data loss, security vulnerabilities, or service outages
  - The corpus contains no relevant documentation for the ticket
  - The ticket is ambiguous about what action is requested
  - Confidence in corpus relevance falls below the numeric threshold (cosine similarity of the top retrieved chunk < **0.65**)
- **May reply** when:
  - The ticket concerns a financial product procedure (e.g., lost/stolen card replacement, traveller's cheque redemption) **and** the corpus contains specific authoritative documentation for that procedure — the response must be entirely grounded in that corpus content with no invented steps
- **Always reply** when:
  - The ticket is a clear FAQ with a direct corpus match
  - The ticket is `invalid` (out-of-scope, irrelevant, or social/non-support)
- `status` values: `replied` (agent answered) | `escalated` (routed to human)
- Escalated responses use the hardcoded text `"Escalate to a human"`; do not generate free-text for escalations

### F5 — Structured output generation

For each ticket, produce exactly five fields:

- `status`: `replied` | `escalated`
- `product_area`: the most specific applicable support category, inferred from corpus section names (e.g., `screen`, `privacy`, `travel_support`, `general_support`); set to `general_support` when no specific category can be determined
- `response`: user-facing text grounded in retrieved corpus chunks; for escalations the hardcoded text `"Escalate to a human"`
- `justification`: 1-3 sentences explaining the routing decision and response rationale, citing corpus source where applicable
- `request_type`: `product_issue` | `feature_request` | `bug` | `invalid`

### F6 — Output writing

- Write all results to `support_tickets/output.csv`
- Columns in order: `status`, `product_area`, `response`, `justification`, `request_type`
- One row per sub-request; multi-request tickets (identified by Scout) produce one row per sub-request; single-request tickets produce one row; input row order and sub-request order within a ticket are preserved

### F7 — Anti-hallucination enforcement

- The agent must not produce any claim, policy, step, or instruction not found in the corpus
- If the corpus does not cover a topic, the agent must escalate or state the topic is out of scope — it must not synthesize from parametric model knowledge
- Responses must attribute their source (which document/section) in the `justification` field

### F8 — CLI entry point

- The agent is invoked from the terminal with a documented command (see `code/README.md`)
- No GUI, no web server, no interactive prompts during processing
- Exit code `0` on success; non-zero on failure with a descriptive error message to stderr

### F9 — Post-generation response verification

- After Anchor generates a corpus-grounded response, a Verifier stage independently re-reads the original ticket sub-request and the proposed response, and asks: "Does this response actually address what the customer asked?"
- The Verifier produces a `verified` boolean and a `verification_confidence` score (0.0–1.0)
- If `verified=false` (confidence below threshold **0.60**), the response is discarded and the ticket is escalated — it is safer to escalate than to return a technically grounded but practically unhelpful answer
- This layer catches cases where Anchor retrieved a corpus chunk that is topically adjacent but does not solve the specific user problem

---

## Agent Architecture

The pipeline is composed of four components — one non-LLM gate and three specialized LLM agents — executed in a fixed sequential order. All three LLM agents are accessed through a single OpenRouter API key using the OpenAI-compatible SDK.

### Pipeline Overview

```
ticket_row (issue, subject, company)
      │
      ▼
 [Gatekeeper] ── validate schema & truncate input; assign request_id
      │
      ▼
   [Scout] ─────── classify: request_type, product_area, inferred_company
      │             extract sub_requests (one item per sub-request)
      │
      │  (one Sentinel + Anchor + Verifier cycle per sub-request)
      ▼
 [Sentinel] ──────────────────── decide: replied vs escalated
      │                                    │
      │ escalated                          │ replied
      ▼                                    ▼
 write "Escalate to a human"          [Anchor] → retrieve corpus (cos_sim ≥ 0.65)
      │                                    │        + generate response
      │                               grounded=false → override to escalated
      │                                    │ grounded=true
      │                                    ▼
      │                             [Verifier] → does response solve the issue?
      │                                    │      (confidence ≥ 0.60)
      │                               verified=false → override to escalated
      │                                    │ verified=true
      └──────────────► [Orchestrator] → assemble 5-field row per sub-request → output.csv
```

### Component Definitions

#### Gatekeeper — pipeline code, no LLM

**Purpose**: Execute F1 (input parsing and validation) before any LLM token is spent.

| Responsibility                                          | Feature           |
| ------------------------------------------------------- | ----------------- |
| Truncate input to max 2 000 chars                       | F1 / data_privacy |
| Validate schema (issue, subject, company fields)        | F1                |
| Constrain company to `{HackerRank, Claude, Visa, None}` | F1                |

**Implementation**: Deterministic code. No LLM call. Validates and truncates the ticket before any downstream processing. On a schema error (e.g., CSV parse failure), emits an `escalated` row and continues to the next ticket.

**Why no LLM**: Input validation and truncation must happen before any LLM token is spent to prevent context-window abuse and ensure clean inputs for downstream agents.

---

#### Scout — `google/gemini-2.5-flash-lite` via OpenRouter

**Purpose**: Fast, cheap first-pass classification. Handles F1 (company inference), F2 (domain routing for `company=None`), and produces the `request_type` and `product_area` fields.

| Responsibility                                                               | Feature | Output field                                |
| ---------------------------------------------------------------------------- | ------- | ------------------------------------------- |
| Classify `request_type` per sub-request                                      | F5      | `sub_requests[].request_type`               |
| Classify `product_area` per sub-request (inferred from corpus section names) | F5      | `sub_requests[].product_area`               |
| Infer company from ticket content when `company=None`                        | F2      | `inferred_company`                          |
| Extract individual sub-requests from multi-request tickets                   | F1      | `sub_requests[]` (one item per sub-request) |

**Input**: `{issue, subject, company}` + a system prompt instructing the model to extract sub-requests and infer `product_area` from corpus section names.

**Output** (structured JSON): `{inferred_company, sub_requests: [{issue_excerpt, request_type, product_area}]}`
A single-request ticket produces `sub_requests` with exactly one item.

**Why this model**: Gemini Flash Lite's 1 M-token context can hold an entire ticket batch; it outperforms similarly-priced models on extraction and structured classification tasks; cost is minimal ($0.10 / 1M in, $0.40 / 1M out — optimised at hackathon scale).

**Risk**: Preview model — no announced GA date. Acceptable for hackathon; monitor for shutdown before production use.

---

#### Sentinel — `anthropic/claude-haiku-4-5` via OpenRouter

**Purpose**: Safety-critical escalation judgment. Applies F4 (escalation rules) using Scout's classification as additional signal. Produces `status` and `justification`.

| Responsibility                                                                 | Feature | Output field    |
| ------------------------------------------------------------------------------ | ------- | --------------- |
| Apply escalation rules (fraud, billing, account compromise, outage, data loss) | F4      | `status`        |
| Escalate when corpus cannot ground a response                                  | F4 / F7 | `status`        |
| Produce escalation justification citing ticket risk                            | F5      | `justification` |
| Confirm `invalid` tickets receive `replied` + out-of-scope message             | F4      | `status`        |

**Input**: `{issue, subject, company, request_type, product_area}` — Scout's output feeds into Sentinel's context.

**Output** (structured JSON): `{status: replied|escalated, justification}`

**Why this model**: Anthropic's safety training maps directly to fraud and escalation judgment — the highest-stakes decisions in the pipeline. Stable GA model with no deprecation risk. Running Sentinel through OpenRouter keeps billing consolidated.

**Why sequential (not parallel with Scout)**: Sentinel needs `request_type` to apply escalation rules correctly (e.g., `invalid` tickets skip escalation; `bug` tickets involving data loss always escalate). Parallel execution would require Sentinel to re-classify, duplicating Scout's work and degrading accuracy.

---

#### Anchor — `google/gemini-2.5-flash` via OpenRouter

**Purpose**: Retrieval-augmented response generation. Handles F3 (corpus retrieval), F7 (anti-hallucination), and generates the `response` field. **Only called when Sentinel returns `replied`.**

| Responsibility                                   | Feature | Output field                 |
| ------------------------------------------------ | ------- | ---------------------------- |
| Retrieve top-k relevant corpus chunks            | F3      | (internal)                   |
| Generate grounded user-facing reply              | F5, F7  | `response`                   |
| Cite source document in justification            | F7      | `justification` (supplement) |
| Signal `grounded=false` when corpus has no match | F7      | triggers escalation          |

**Input**: `{issue, subject, inferred_company, product_area}` + retrieved corpus chunks from the routed `data/<company>/` directory.

**Output** (structured JSON): `{response, source_doc, grounded: bool}`

If `grounded=false`, the Orchestrator overrides Sentinel's `replied` with `escalated` and emits the hardcoded escalation message — no fabricated response is ever written.

**Why this model**: Near-Pro reasoning at Flash price. 1 M context holds the full support corpus in a single call. Strong instruction-following for "only use provided docs" constraints. Always set `thinkingBudget: 0` (or equivalent) to prevent runaway thinking-token costs.

**Risk**: Preview model. Same mitigation as Scout.

---

#### Orchestrator — `agent.py` pipeline code, no LLM

**Purpose**: Thin coordinator. No LLM calls. Drives the sequential pipeline, assembles the final 5-field row, and writes `output.csv`.

| Responsibility                                                           | Feature |
| ------------------------------------------------------------------------ | ------- |
| Drive Gatekeeper → Scout → Sentinel → Anchor sequence                    | F8      |
| Pass structured outputs between agents                                   | F8      |
| Assemble `{status, product_area, response, justification, request_type}` | F5, F6  |
| Write `support_tickets/output.csv` in input row order                    | F6      |
| CLI entry point, exit codes                                              | F8      |

---

### Feature-to-Component Coverage Map

| Feature                 | Component(s)                                                                              |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| F1 — Input parsing      | Gatekeeper (validation, truncation, request_id), Scout (company inference, multi-request) |
| F2 — Domain router      | Scout (infer company), Orchestrator (map to `data/<company>/`)                            |
| F3 — Retrieval pipeline | Anchor                                                                                    |
| F4 — Escalation engine  | Sentinel                                                                                  |
| F5 — Structured output  | Scout (request_type, product_area), Sentinel (status, justification), Anchor (response)   |
| F6 — Output writing     | Orchestrator                                                                              |
| F7 — Anti-hallucination | Anchor (grounding constraint + `grounded` flag), Orchestrator (override on false)         |
| F8 — CLI entry point    | Orchestrator                                                                              |
| F9 — Post-gen verify    | Verifier (`verified` + `verification_confidence`), Orchestrator (override on false)       |

---

### Provider Strategy

All LLM agents run through **OpenRouter** (`https://openrouter.ai/api/v1`) using the OpenAI-compatible SDK, via the `ModelClient` abstraction. One API key, one billing balance. Switching any model — or switching to a local backend — is a one-line config change.

| Agent    | Model                          | Input cost | Output cost | Role                          |
| -------- | ------------------------------ | ---------- | ----------- | ----------------------------- |
| Scout    | `google/gemini-2.5-flash-lite` | $0.10 / 1M | $0.40 / 1M  | Classification                |
| Sentinel | `anthropic/claude-haiku-4-5`   | $1.00 / 1M | $5.00 / 1M  | Escalation judgment           |
| Anchor   | `google/gemini-2.5-flash`      | $0.15 / 1M | $0.60 / 1M  | RAG + response generation     |
| Verifier | `google/gemini-2.5-flash-lite` | $0.10 / 1M | $0.40 / 1M  | Post-generation quality check |

Anchor and Verifier are **conditionally invoked** — escalated tickets skip both. For a 30-ticket batch where ~40 % escalate, this significantly reduces spend on the two most downstream stages.

---

## Out of Scope

The following are explicitly excluded from this project:

- **Live/real-time chat interface**: The agent processes a batch CSV; it does not respond to live users
- **Web scraping or live API calls to support portals**: The agent uses only the local `data/` corpus
- **Training or fine-tuning models**: The agent uses pre-trained LLMs via API; no model training occurs
- **Ticket management system integration**: No Zendesk, Salesforce, Freshdesk, or CRM integration
- **Multi-turn conversation handling**: Each ticket row is processed independently with no conversation memory
- **Image or attachment processing**: Only text fields are processed
- **Automatic corpus updates**: The corpus in `data/` is static for this submission
- **User authentication or access control**: The agent runs locally with no login system
- **Performance SLA monitoring or dashboards**: This is a batch tool, not a production service

---

## Technical Constraints

| Constraint    | Requirement                                                                                                                                                                                |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Language      | Python                                                                                                                                                                                     |
| Execution     | Terminal-based CLI; must run with a single command documented in `code/README.md`                                                                                                          |
| Corpus        | ONLY `data/hackerrank/`, `data/claude/`, `data/visa/` — no external knowledge                                                                                                              |
| Secrets       | All API keys via environment variables; `.env` file (gitignored); no hardcoded keys                                                                                                        |
| Dependencies  | All pinned in `requirements.txt` with exact versions                                                                                                                                       |
| Determinism   | LLM sampling must use `temperature=0`; classification and routing decisions must be semantically stable across runs — exact string identity not guaranteed                                 |
| Output path   | Results always written to `support_tickets/output.csv`                                                                                                                                     |
| Entry point   | `code/agent.py`                                                                                                                                                                            |
| Model backend | All LLM calls routed through a `ModelClient` abstraction; default backend is OpenRouter; local backends (Ollama, vLLM) supported via `MODEL_BACKEND` env var without pipeline code changes |

---

## Dependencies

### Required external services

| Service                                             | Purpose                                | Configuration                                     |
| --------------------------------------------------- | -------------------------------------- | ------------------------------------------------- |
| OpenRouter API                                      | Single gateway to all three LLM agents | `OPENROUTER_API_KEY` env var                      |
| Embedding model (optional, via OpenRouter or local) | Semantic retrieval over corpus         | Same API key or local sentence-transformers model |

### Required local data

| Path                                         | Description                                               |
| -------------------------------------------- | --------------------------------------------------------- |
| `data/hackerrank/`                           | HackerRank support corpus (index + article files)         |
| `data/claude/`                               | Claude (Anthropic) support corpus (index + article files) |
| `data/visa/`                                 | Visa support corpus (index + article files)               |
| `support_tickets/support_tickets.csv`        | Input tickets to process                                  |
| `support_tickets/sample_support_tickets.csv` | Labeled examples for behavior reference                   |
| `.env`                                       | API keys and configuration (never committed)              |

### Optional dependencies (if chosen)

| Dependency | Purpose                                                                                                                                                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Qdrant     | Persistent vector index for corpus retrieval. Chosen over Chroma because metadata filtering (by company) runs **before** vector similarity computation, preventing cross-domain contamination and improving retrieval accuracy at no extra latency cost. |

---

## Assumptions

1. The `data/` corpus is authoritative and complete for answering all non-escalation tickets.
2. The `sample_support_tickets.csv` file is representative of the distribution and difficulty of `support_tickets.csv`.
3. The evaluator runs the agent in a clean environment with only the dependencies listed in `requirements.txt`.
4. "Escalate to a human" in this context means returning a predefined static escalation message (not a live handoff).
5. The `company=None` case should be resolved by the agent through content-based inference, not defaulted to any single domain.
