# AI Judge Interview Criteria

## Overview

After submission, participants defend their approach in a live AI judge interview. This document prepares you to answer the evaluator's likely questions with confidence. Each section maps to a decision in the architecture and the reasoning behind it.

---

## 1. Core Design Questions

### "Why Python over Node.js or other languages?"

**Answer**: This project is centered around retrieval, classification, and safety logic — areas where Python has a stronger and more mature ecosystem (sentence-transformers, Qdrant client, LangChain, tiktoken, pandas). It also enables faster prototyping and iteration, which is critical in a 24-hour hackathon. The pipeline is a batch processor, not a web server — Node's async I/O strengths don't apply here.

### "Why RAG instead of fine-tuning, keyword search, or full-context prompting?"

**Answer**: Four alternatives exist; RAG is the best balance for this task:

| Approach               | Problem                                                                          |
| ---------------------- | -------------------------------------------------------------------------------- |
| Fine-tuning            | Expensive to update; requires retraining when corpus changes                     |
| Full-context prompting | Pasting all documents is slow, expensive, and hits context-window limits         |
| Keyword search         | Doesn't understand meaning; fails on paraphrases and synonyms                    |
| **RAG (chosen)**       | Retrieves only relevant chunks; grounding is traceable; scales to corpus updates |

RAG also makes grounding **auditable** — each response has a `source_doc` citation that can be verified.

### "Why Qdrant over Chroma or FAISS?"

**Answer**: Every query must be scoped to a specific company (HackerRank, Claude, or Visa). Qdrant applies metadata filters (`company` field) **before** vector similarity computation, narrowing the search space before any cosine math runs. Chroma filters results post-hoc (after or during similarity search), which means it still computes similarity against the full index and then discards wrong-domain results. For this task, pre-filter accuracy and the correctness guarantee of never retrieving cross-domain content is more important than raw indexing speed. Qdrant gives both better accuracy and faster query execution.

### "Why no agent framework (LangChain, LlamaIndex, CrewAI, etc.)?"

**Answer**: The pipeline has exactly four stages in a fixed sequence — no coordination problem that a framework solves. Each agent is a function that calls its own model. Using a framework would add:

- Abstraction overhead with no benefit
- Unpredictable token usage (hidden prompt templates)
- Less control over model selection and cost per stage
- Framework-specific failure modes that are harder to debug

Plain Python gives full control over model selection, cost optimization (Anchor is conditionally skipped), and deterministic execution. The pipeline is simple enough that a framework would be complexity for its own sake.

---

## 2. Safety and Escalation Questions

### "How do you prevent hallucinations?"

**Answer**: Three independent layers:

1. **Anchor retrieves first, generates second** — the prompt explicitly contains only the retrieved corpus chunks and instructs the model to use only that content
2. **`grounded=false` override** — if the top retrieved chunk falls below cosine similarity 0.65, Anchor sets `grounded=false` and the Orchestrator overrides the ticket to `escalated`; no ungrounded reply is ever written
3. **Sentinel guards before Anchor runs** — Sentinel's escalation rules prevent Anchor from being called on high-risk tickets where even a correct-but-guessed answer would be dangerous

### "How do you handle prompt injection?"

**Answer**: Two layers:

1. **System/user message separation** — ticket content is always passed in the `user` role, never concatenated into the `system` prompt. The model receives instruction from the system prompt and cannot confuse ticket content with instructions.
2. **Scout classification** — injected content (`"Ignore previous instructions..."`) is classified as `request_type=invalid` and receives an out-of-scope reply. The pipeline behavior is unchanged regardless of injection content.

### "What happens if an LLM API call fails?"

**Answer**: Each stage has a defined failure behavior (see `exception_handling.md`). The key principle: failures default toward the safe direction:

- Scout failure → use classification defaults; continue pipeline
- Sentinel failure → escalate the ticket (never default to replied)
- Anchor failure → treat as `grounded=false` → escalate

No unhandled exception can cause a ticket to be silently dropped or produce a fabricated reply.

---

## 3. Architecture Questions

### "Why is the pipeline sequential rather than parallel?"

**Answer**: Sentinel needs Scout's `request_type` to apply escalation rules correctly. For example: `request_type=invalid` tickets always receive `replied` (never escalated), and `bug` tickets involving data loss always escalate. If Sentinel ran in parallel with Scout, it would lack this classification signal and produce noisier decisions. The latency cost of sequencing is negligible at `temperature=0` with small per-ticket payloads.

### "How do you handle `company=None` tickets?"

**Answer**: Scout infers the company from ticket content by matching vocabulary, product names, and context against all three corpus sub-directories. The `inferred_company` is then used to scope retrieval. If inference produces `None` (no confident match), Anchor queries all three corpora and selects the best-matching chunks by relevance score.

### "Why one OpenRouter API key instead of direct Anthropic/Google APIs?"

**Answer**: One API key, one billing balance, one SDK. Switching any model is a one-line config change. OpenRouter supports both Anthropic and Google models through the OpenAI-compatible SDK, eliminating per-provider SDK dependencies. For a 24-hour hackathon, this simplifies setup and debugging.

---

## 4. Known Limitations

Be prepared to acknowledge these honestly — the evaluator will ask:

| Limitation                                           | Honest answer                                                                                  |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| No cross-run sender memory                           | Accepted constraint for v1 batch scope; FI-1 in `guardrails.md` outlines the future approach   |
| Preview models (Gemini Flash Lite, Gemini 2.5 Flash) | Acceptable for hackathon; would pin to GA models for production use                            |
| Static corpus                                        | Corpus updates require a manual rebuild of the Qdrant index; no live refresh                   |
| No output validation against human labels            | Benchmark targets are projections; actual accuracy depends on ground-truth comparison          |
| Single retry per stage                               | Network reliability is not the primary failure mode for this use case; one retry is sufficient |

---

## 5. What Was Deprioritized and Why

| Deprioritized feature           | Reason                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------ |
| Web server / API interface      | Evaluator needs a CLI tool; web server adds complexity with no evaluation benefit          |
| Multi-turn conversation memory  | Each ticket is independent; conversation history adds state management complexity          |
| Ticket management integration   | No Zendesk/Freshdesk integration; out of scope for hackathon                               |
| Fine-tuned classification model | RAG with structured prompting achieves equivalent accuracy at zero training cost           |
| Custom embedding model          | Pre-trained sentence-transformers achieve sufficient retrieval quality for the corpus size |
