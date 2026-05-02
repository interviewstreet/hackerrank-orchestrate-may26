# Input/Output Validation Policies

## Input Guardrails

- All ticket fields (`issue`, `subject`, `company`) are validated for presence and type before processing begins.
- Input length is capped to prevent context-window abuse; oversized tickets are truncated and flagged in `justification`.
- Adversarial or off-topic inputs are not pre-filtered; they pass through the full pipeline and are classified as `request_type=invalid` by Scout.
- The `company` field is constrained to the known domain set (`HackerRank`, `Claude`, `Visa`, `None`); unknown values are treated as `None`.

## Output Guardrails

- Every generated `response` must be attributable to a corpus chunk; if attribution fails, the ticket is escalated rather than replied to.
- The escalation message is hardcoded — no free-text LLM generation is used for escalated tickets.
- The escalation response is the hardcoded string `"Escalate to a human"` — no LLM generation for escalated tickets.
- `status` may only be one of the two defined values: `replied` or `escalated`. Any other value is a pipeline error.

---

## Current Limitations

### No persistent sender identity or cross-session tracking

The agent processes each CSV row independently with no memory of prior sessions or prior tickets from the same sender. This means:

- A sender who submits repeated adversarial tickets receives `replied` (out-of-scope) or `escalated` per-ticket but is **not blocked** from submitting again.
- There is no rate limiting at the sender or IP level.
- Abuse patterns that span multiple submissions (gradual social engineering across tickets) are invisible to the current pipeline.
- Invalid ticket outcomes are recorded in `output.csv` for the current run only; there is no persistent abuse log that survives across runs.

This is an accepted constraint for the v1 batch-processing scope.

---

## Future Improvements

### FI-1 — Persistent sender reputation and blocking

Track senders (by email, user ID, or a hash of identifying fields) across runs in a lightweight store (e.g. a local SQLite database or append-only JSONL file). After a configurable number of confirmed `invalid` or escalated tickets within a rolling time window, flag the sender as blocked.

Blocked senders receive the same out-of-scope reply (no signal that they are blocked) but are short-circuited before any LLM processing to eliminate compute cost.

Unblocking must be a manual human action; the system must never auto-unblock.

### FI-2 — Rate limiting per sender

Enforce a per-sender ticket submission rate (e.g. max N tickets per hour, M tickets per day). Tickets that exceed the rate limit receive a "please try again later" variant of the redirection message. Rate-limit counters reset on a sliding window, not a fixed clock boundary.

Rate limiting applies independently of and before Scout classification.

### FI-3 — Abuse signal feedback loop

Expose a lightweight operator interface (a CLI flag or admin CSV) that allows human agents to mark escalated tickets as confirmed abuse. These labels feed back into Scout's context or a pattern list, tightening classification over time without requiring full model retraining.

### FI-4 — Cross-run invalid/abuse audit log

Write all `invalid` and adversarial-classified ticket events to a persistent, append-only audit log (separate from `output.csv`) that survives across runs. Each entry records the timestamp, a hashed sender identifier, the classification reason, and a truncated (non-PII) excerpt of the flagged input. This log enables retrospective analysis of abuse trends and supports FI-1 and FI-3.

---

## Placement in Pipeline

```
[FI-2 Rate Limiter] → [FI-1 Sender Block Check] → Gatekeeper (F1 validation) → Scout/Sentinel/Anchor normal pipeline
```

Both FI-1 and FI-2 run before the Gatekeeper so that confirmed-bad and rate-exceeded senders never reach any LLM call.
