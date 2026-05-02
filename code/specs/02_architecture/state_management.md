# State Management

## Architecture: Stateless Batch Processing

The triage agent is a **stateless batch processor**. There are no sessions, no conversation memory, and no persistent state that persists between tickets. Each ticket row is processed in full isolation — outputs from one ticket have zero influence on the processing of any other ticket.

This is an explicit design constraint, not a limitation. Multi-turn conversation handling and cross-ticket memory are out of scope (see `vision_and_scope.md` — Out of Scope).

---

## Request-Scoped State (In-Memory Only)

Within the processing of a single ticket, state flows forward through the pipeline as immutable typed dictionaries. Each stage receives the previous stage's output and produces its own output. Nothing is written to disk mid-ticket.

```
Gatekeeper output  →  Scout input
Scout output       →  Orchestrator (distributes to Sentinel per sub-request)
Sentinel output    →  Anchor input (only on replied)
Anchor output      →  Orchestrator (assembles final row)
```

All intermediate state is held in Python dicts in memory for the duration of that ticket's processing and discarded after the output row is written.

### State schema (per sub-request in flight)

```python
{
    # Assigned by Orchestrator at pipeline entry
    "request_id": str,   # "req_{row}_{subreq}_{epoch_ms}" — used in all log entries

    # From Gatekeeper
    "issue": str,         # validated, truncated to 2000 chars combined with subject
    "subject": str,
    "company": str,       # one of HackerRank | Claude | Visa | None

    # From Scout
    "inferred_company": str,
    "issue_excerpt": str,
    "request_type": str,  # product_issue | feature_request | bug | invalid
    "product_area": str,

    # From Sentinel
    "status": str,        # replied | escalated
    "justification": str,

    # From Anchor (only when status=replied)
    "response": str,
    "source_doc": str,
    "grounded": bool,

    # From Verifier (only when grounded=true)
    "verified": bool,     # false → Orchestrator overrides status to escalated
    "verification_confidence": float,  # 0.0–1.0; below threshold triggers escalation
}
```

---

## Persistent State: Output File

The only persistent write is `support_tickets/output.csv`. It is written row-by-row (or in batch after all tickets) by the Orchestrator. No other persistent state is created.

---

## Persistent State: Qdrant Vector Index (Optional)

If Qdrant is used, the vector index is built once from the support corpus (`data/`) at startup and persisted to a local Qdrant data directory. This index contains **only corpus document embeddings** — never ticket-derived embeddings or PII.

| Index property        | Value                                                              |
| --------------------- | ------------------------------------------------------------------ |
| Source                | `data/hackerrank/`, `data/claude/`, `data/visa/` corpus docs       |
| Metadata per point    | `company` field (for pre-search filtering), `source_doc` path      |
| Ticket content stored | Never — ticket embeddings are computed transiently and discarded   |
| Rebuild policy        | Rebuild on corpus change; do not persist ticket-derived embeddings |

The Qdrant company metadata filter is applied **before** vector similarity computation. This is the primary reason Qdrant was chosen over Chroma: Chroma filters results after retrieval (post-hoc), while Qdrant narrows the search space before any similarity math, preventing cross-domain retrieval contamination.

---

## FAQ Cache (Optional Optimization)

A lightweight in-memory FAQ cache may be maintained **per run** to avoid redundant corpus lookups for repeated identical queries. This cache is:

- Keyed by `(company, product_area, issue_excerpt_hash)`
- Scoped to a single run — it is not persisted to disk
- Never populated with ticket PII — only corpus retrieval results are cached

This is an optimization, not a requirement. The cache must not be persisted between runs.

---

## What Is Explicitly Prohibited

| Prohibited                                        | Reason                                                           |
| ------------------------------------------------- | ---------------------------------------------------------------- |
| Cross-ticket memory of any kind                   | Each ticket must be processed in isolation (data_privacy §2.2.6) |
| Persisting ticket text or embeddings to any store | PII exposure risk (data_privacy §3.1)                            |
| Session state across runs                         | Stateless batch design; no user sessions exist                   |
| Using one ticket's output to influence another's  | Would compromise determinism and privacy isolation               |
| Caching LLM responses keyed on ticket content     | Ticket content is untrusted user input and must not persist      |
