# Pipeline Topology

## Execution Model

The pipeline is **strictly sequential**. Each stage receives the previous stage's structured JSON output before executing. No stage runs in parallel with another.

**Why sequential, not parallel**: Sentinel needs Scout's `request_type` to apply escalation rules correctly — e.g., `invalid` tickets are never escalated, `bug` tickets involving data loss always are. If Sentinel ran in parallel with Scout, it would lack this signal and produce noisier decisions. The latency cost of sequencing is negligible given `temperature=0` and small per-ticket payloads.

---

## Stage Diagram

```
support_tickets.csv
        │
        │  row (issue, subject, company)
        ▼
┌───────────────────┐
│    Gatekeeper     │  deterministic code — no LLM
│                   │  • validate schema & truncate input
│                   │  • assign request_id
└───────┬───────────┘
        │
        │ PASS
        ▼
┌───────────────────┐
│      Scout        │  google/gemini-2.5-flash-lite
│                   │  • extract sub_requests (one item per sub-request)
│                   │  • classify request_type + product_area per sub-request
│                   │  • infer company (if None)
└───────┬───────────┘
        │  {inferred_company, sub_requests[]}
        │
        │  (iterate: one cycle per sub_requests item)
        ▼
┌───────────────────┐
│     Sentinel      │  anthropic/claude-haiku-4-5
│                   │  • apply escalation rules
│                   │  • produce status + justification
└───────┬───────────┘
        │
        ├── ESCALATED ──────────────────────────────────────────────────────►  ┐
        │   status=escalated                                                    │
        │   response="Escalate to a human"                                      │
        │   justification=Sentinel justification                                │
        │                                                                       │
        │ REPLIED                                                               │
        ▼                                                                       │
┌───────────────────┐                                                           │
│      Anchor       │  google/gemini-2.5-flash                                  │
│                   │  • retrieve corpus chunks (F3)                            │
│                   │  • grounded=true if top chunk cos_sim ≥ 0.65 (F7)        │
│                   │  • generate grounded response                             │
└───────┬───────────┘                                                           │
        │                                                                       │
        ├── grounded=false ─────────────────────────────────────────────────►  ┤
        │   (override: status → escalated, response → "Escalate to a human")   │
        │                                                                       │
        │ grounded=true                                                         │
        ▼                                                                       │
┌───────────────────┐                                                           │
│     Verifier      │  google/gemini-2.5-flash-lite                             │
│                   │  • re-read: does response actually solve the issue? (F9)  │
│                   │  • produce verified bool + confidence score               │
└───────┬───────────┘                                                           │
        │                                                                       │
        ├── verified=false (confidence < 0.60) ────────────────────────────►   ┤
        │   (override: status → escalated, response → "Escalate to a human")   │
        │                                                                       │
        │ verified=true                                                         │
        ▼                                                                       │
┌───────────────────┐                                                           │
│   Orchestrator    │  deterministic code — no LLM      ◄─────────────────────┘
│   (output stage)  │  • assemble 5-field row per sub-request
│                   │  • write to output.csv (one row per sub-request)
│                   │  • preserve ticket order + sub-request order
└───────────────────┘
```

---

## Data Contract Between Stages

Each stage produces a typed JSON object consumed by the next. The Orchestrator resolves `inferred_company` before passing context to Anchor.

```
Gatekeeper → Scout:
  {request_id, issue, subject, company}  (validated, truncated)

Scout → Orchestrator (per-ticket):
  {inferred_company,
   sub_requests: [{issue_excerpt, request_type, product_area}]}

Orchestrator iterates sub_requests; per sub-request:

  Orchestrator → Sentinel:
    {request_id, issue_excerpt, subject, resolved_company, request_type, product_area}

  Sentinel → Anchor (only on replied):
    {request_id, issue_excerpt, subject, resolved_company, product_area,
     status, justification}

  Anchor → Verifier (only when grounded=true):
    {request_id, issue_excerpt, response, source_doc, grounded}

  Verifier → Orchestrator:
    {verified: bool, verification_confidence: float, verification_reason: str}

Orchestrator (final row per sub-request):
  {status, product_area, response, justification, request_type}
```

---

## Conditional Invocation

Anchor is the most expensive agent per token. It is **skipped** for sub-requests where Sentinel returns `status=escalated`.

For a typical support batch where ~35–40 % of sub-requests escalate, this reduces Anchor spend proportionally.

---

## Why This Topology

| Design choice                                          | Rationale                                                                                           |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Sequential (not parallel)                              | Sentinel's escalation rules require Scout's classification as input                                 |
| Gatekeeper before all LLMs                             | Input validation and truncation must occur before any LLM token is spent                            |
| Anchor conditional on Sentinel                         | Avoids generation cost for escalated sub-requests; corpus grounding is never needed for escalations |
| Hardcoded escalation message (`"Escalate to a human"`) | Escalation response must be deterministic — Anchor's generated text is never used for escalations   |
| `grounded=false` override                              | Ensures a ticket Anchor cannot answer is never replied to; converts silently to escalated           |
| Single OpenRouter provider                             | One API key, one billing balance; model swap is a one-line config change                            |

---

## Architectural Decisions

### Language: Python

Python was chosen over Node.js because this project is centered around retrieval, classification, and safety logic — areas where Python has a stronger and more mature ecosystem (sentence-transformers, Qdrant client, scientific computing libraries). It also enables faster prototyping and iteration, which is critical in a time-constrained hackathon. The pipeline is a batch processor; Node's async I/O advantages don't apply.

### Retrieval Strategy: RAG

Four retrieval approaches were considered:

| Approach                                     | Reason rejected                                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Fine-tuning                                  | Expensive to update; corpus changes require full retraining                                     |
| Full-context prompting (paste all documents) | Slow, expensive, hits context-window limits; no targeted retrieval                              |
| Keyword search (BM25, regex)                 | Doesn't understand semantic meaning; fails on paraphrase and synonyms                           |
| **RAG (chosen)**                             | Retrieves only relevant chunks; grounding is observable and auditable; scales to corpus updates |

RAG is also the only approach that produces a traceable `source_doc` citation per response — which is required for the `justification` field and anti-hallucination enforcement.

### Vector Store: Qdrant over Chroma

Every retrieval query must be scoped to a specific company corpus. Qdrant applies the `company` metadata filter **before** computing vector similarity — it narrows the candidate set first, then runs cosine math only on matching documents. Chroma applies filters after or during retrieval, meaning it computes similarity against the full index and discards wrong-domain results afterward. For this task:

- Qdrant prevents cross-domain contamination at the retrieval level, not as a post-hoc guardrail
- Qdrant is faster because the pre-filter reduces the similarity computation space
- Qdrant's filter semantics are more predictable and correct for this use case

### No Agent Framework

Each agent is a plain Python function that calls its own designated model — there is no coordination problem, no shared memory, and no tool use between agents. Using a framework (LangChain, LlamaIndex, CrewAI) would add:

- Hidden prompt templates that inflate token costs unpredictably
- Abstraction layers that obscure model selection and error paths
- Framework-specific failure modes that complicate debugging

Plain Python gives full control over model selection, cost optimization (Anchor is conditionally skipped for escalations), and deterministic sequential execution. The pipeline is intentionally simple — a framework would be complexity for its own sake.

---

## Model Provider Abstraction (Local Model Readiness)

All LLM calls are routed through a thin `ModelClient` abstraction rather than calling OpenRouter directly. This design decision future-proofs the pipeline for local model deployment (e.g. Ollama, vLLM, llama.cpp) without changing any pipeline logic.

### Interface contract

```python
class ModelClient:
    def complete(
        self,
        model: str,        # logical model name (resolved by client to actual endpoint)
        messages: list,    # OpenAI-compatible messages array
        temperature: float,
        response_format: dict | None,  # JSON schema for structured output
    ) -> dict:             # parsed response dict
        ...
```

### Supported backends

| Backend        | When to use                                           | Config key           |
| -------------- | ----------------------------------------------------- | -------------------- |
| `openrouter`   | Default — cloud APIs via OpenRouter                   | `OPENROUTER_API_KEY` |
| `local_ollama` | Privacy-sensitive deployments; no data leaves machine | `OLLAMA_BASE_URL`    |
| `local_vllm`   | High-throughput local GPU deployment                  | `VLLM_BASE_URL`      |

The active backend is selected by the `MODEL_BACKEND` environment variable. All three backends accept the same `ModelClient.complete()` call signature. Switching from cloud to local requires only an env var change — no pipeline code changes.

### Why this matters for security

Routing ticket content through a cloud API means customer PII is transmitted to a third-party provider. For deployments where this is unacceptable (e.g. regulated industries, internal enterprise use), swapping to a local backend eliminates external data transmission entirely. The `ModelClient` abstraction makes this swap zero-code-change.

### Local model selection guidance

When using a local backend, choose models with strong instruction-following for structured JSON output:

| Pipeline role | Minimum recommended local model  |
| ------------- | -------------------------------- |
| Scout         | `gemma2:9b` or `llama3.1:8b`     |
| Sentinel      | `llama3.1:8b` (safety-tuned)     |
| Anchor        | `llama3.1:70b` or `mistral-nemo` |
| Verifier      | `gemma2:9b` or `llama3.1:8b`     |

Local models may require looser JSON parsing (output may not be clean JSON) — implement a best-effort JSON extraction fallback in `ModelClient.complete()` for local backends.
