# Resilience Protocol: Reactive Routing, Retries, & Recovery

Each pipeline stage has a defined failure mode and a recovery action. The guiding rule: **when in doubt, escalate — never guess or skip**.

---

## Stage-Level Failures

### Gatekeeper failures

| Failure                                      | Behavior                                                                                                                 |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Missing `issue` field (empty string or null) | Treat as `invalid` — pass directly to Scout with `issue=""`                                                              |
| CSV parse error on row                       | Log error to stderr, write a `escalated` row with `justification="Input parse error on this row."`, continue to next row |
| Encoding error in ticket text                | Decode with `errors='replace'`, continue                                                                                 |

Gatekeeper must **never crash the pipeline**. A bad row produces an escalated output and processing continues.

---

### Scout failures

| Failure                          | Behavior                                                                                                                                                                                            |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API timeout or 5xx error         | Retry once with 2-second backoff. On second failure, skip Scout and proceed with defaults: `request_type=product_issue`, `product_area=general_support`, `inferred_company=<input company or None>` |
| Malformed JSON response          | Retry once. On second failure, use defaults above. Log to stderr.                                                                                                                                   |
| Rate limit (429)                 | Wait for `Retry-After` header duration (or 60s if absent), then retry once. On failure, use defaults.                                                                                               |
| `request_type` not in valid enum | Default to `product_issue`. Log to stderr.                                                                                                                                                          |
| `product_area` not recognized    | Keep as-is — Anchor will use it as a freeform search query.                                                                                                                                         |

Scout failures are **non-fatal**. Defaults ensure the pipeline continues. However, a Scout failure degrades Sentinel's escalation accuracy — log clearly.

---

### Sentinel failures

| Failure                                | Behavior                                                                                                       |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| API timeout or 5xx error               | Retry once with 2-second backoff. On second failure, **escalate the ticket** — never skip Sentinel's judgment. |
| Malformed JSON response                | Retry once. On second failure, escalate.                                                                       |
| Rate limit (429)                       | Wait, retry once. On failure, escalate.                                                                        |
| `status` not in `{replied, escalated}` | Default to `escalated`. Log to stderr.                                                                         |

Sentinel failures **default to escalated**, not replied. This is the safe direction: a ticket that wasn't properly assessed should always go to a human.

---

### Anchor failures

| Failure                                                          | Behavior                                                                                                               |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| API timeout or 5xx error                                         | Retry once with 2-second backoff. On second failure, treat as `grounded=false` → override to `escalated`.              |
| Malformed JSON response                                          | Retry once. On second failure, treat as `grounded=false`.                                                              |
| Rate limit (429)                                                 | Wait, retry once. On failure, treat as `grounded=false`.                                                               |
| Empty corpus retrieval (no chunks with cosine similarity ≥ 0.65) | Set `grounded=false` immediately — do not call Anchor. Orchestrator writes escalated row with `"Escalate to a human"`. |
| `grounded=false` in Anchor output                                | Orchestrator overrides `status → escalated`, writes hardcoded escalation message.                                      |

Anchor failures **never produce a replied row with fabricated content**. The only outcomes are a grounded reply or an escalation.

---

### Verifier failures

| Failure                                       | Behavior                                                                                                           |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| API timeout or 5xx error                      | Retry once with 2-second backoff. On second failure, treat as `verified=false` → escalate.                         |
| Malformed JSON response                       | Retry once. On second failure, treat as `verified=false`.                                                          |
| Rate limit (429)                              | Wait, retry once. On failure, treat as `verified=false`.                                                           |
| `verified=false` (confidence < 0.60)          | Orchestrator overrides `status → escalated`; Anchor's response is discarded; hardcoded escalation message written. |
| `verification_confidence` missing from output | Default to `verified=false` — treat as escalation. Never assume verification passed if the signal is absent.       |

Verifier failures default to `verified=false` (escalation), matching the safety-first principle: an unverified response is never returned to the user.

---

## Cross-Cutting Concerns

### API key not set

On startup, Orchestrator checks that `OPENROUTER_API_KEY` (or equivalent) is set. If missing:

```
ERROR: OPENROUTER_API_KEY environment variable not set.
Set it in .env and re-run: cp .env.example .env && nano .env
```

Exit code: `1`. No output.csv is written.

---

### Qdrant index not built (FM-SYS3)

On startup, before processing any ticket, Orchestrator verifies the Qdrant collection exists and contains at least one point for each company corpus. If the index is empty or missing:

```
ERROR: Qdrant index not found or empty for company=<name>.
Build the index first: python code/build_index.py
```

Exit code: `1`. No output.csv is written. This check must run before the first ticket is processed — not discovered mid-run.

---

### Output file write failure

If `support_tickets/output.csv` cannot be opened for writing (permissions, disk full):

```
ERROR: Cannot write to support_tickets/output.csv: <os error>
```

Exit code: `1`. Processing stops — partial output is not written.

---

### Full pipeline failure rate

If more than 50 % of tickets in a single run fail at the Sentinel or Anchor stage (indicating a systemic API issue), the Orchestrator logs a warning to stderr after processing completes:

```
WARNING: X of Y tickets were escalated due to pipeline failures. Check API status.
```

This does not change the exit code — output.csv is still written with the best available results.

---

## Retry Policy Summary

| Stage    | Max retries | Backoff | Failure default                    |
| -------- | ----------- | ------- | ---------------------------------- |
| Scout    | 1           | 2s      | Use classification defaults        |
| Sentinel | 1           | 2s      | Escalate ticket                    |
| Anchor   | 1           | 2s      | Treat as grounded=false → escalate |

Retries are applied per-ticket, not globally. A per-ticket retry does not delay processing of other tickets (sequential model — retries add at most a few seconds per affected ticket).

---

## Logging

All errors and warnings are written to **stderr only**. `stdout` is reserved for progress output (e.g. `Processing ticket 3/30...`).

### Request ID

Every sub-request in the pipeline is assigned a **request ID** at the moment it enters processing. The ID is used consistently across all log entries for that sub-request, enabling full trace reconstruction from a single ID.

**Format**: `req_{row_index}_{subreq_index}_{epoch_ms}`  
**Example**: `req_007_1_1746200134521`

- `row_index` — 1-based row number in `support_tickets.csv`
- `subreq_index` — 1-based index within the ticket's sub-requests (always `1` for single-request tickets)
- `epoch_ms` — millisecond Unix timestamp at ticket entry time (makes IDs globally unique across runs)

The request ID is:

- Included in every log entry for that sub-request
- Written to `justification` for escalated rows that were caused by pipeline errors (enables human agents to correlate the output row with the processing log)
- Never includes PII from the ticket

### Log entry format

```
[{request_id}] {stage}: {event} → {action}
```

**Fields**:

- `request_id` — as defined above
- `stage` — `Gatekeeper` / `Scout` / `Sentinel` / `Anchor` / `Verifier` / `Orchestrator`
- `event` — error type: `api_error({status})` / `timeout` / `json_parse_error` / `rate_limit` / `schema_violation` / `grounded=false` / `verified=false`
- `action` — `retry 1` / `success` / `escalated` / `default`

**Examples**:

```
[req_007_1_1746200134521] Sentinel: api_error(503) → retry 1 → success
[req_012_1_1746200141803] Anchor: timeout → retry 1 → timeout → grounded=false → escalated
[req_019_1_1746200158001] Scout: json_parse_error → retry 1 → success
[req_023_2_1746200164310] Verifier: verified=false → escalated (low confidence: 0.41)
[req_027_1_1746200172900] Gatekeeper: schema_violation (missing issue field) → escalated
```

### Structured progress output (stdout)

Progress output to stdout uses the request ID for traceability:

```
[req_007_1_...] Processing ticket 7/30 (sub-request 1/1) — company=HackerRank
[req_012_1_...] Processing ticket 12/30 (sub-request 1/2) — company=Visa
[req_012_2_...] Processing ticket 12/30 (sub-request 2/2) — company=Visa
```
