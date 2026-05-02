# Human-in-the-Loop: Protocols for Intervention and Handoff Triggers

## Overview

The pipeline is designed to handle the majority of support tickets autonomously. However, certain ticket types must **never** receive an automated response — they require human judgment. This document defines exactly when the pipeline hands off to a human, what information is provided in that handoff, and what the human agent receives.

---

## 1. Handoff Triggers

The pipeline produces `status=escalated` — and therefore hands off to a human — under the following conditions. All are evaluated by Sentinel before any response is generated.

### 1.1 Always-Escalate Ticket Types

These ticket types are escalated regardless of corpus coverage. No amount of relevant documentation makes automated reply appropriate:

| Trigger                                  | Examples                                                               |
| ---------------------------------------- | ---------------------------------------------------------------------- |
| Fraud / unauthorized charges             | "Someone made purchases I didn't authorize on my Visa card"            |
| Account compromise / unauthorized access | "Someone logged into my HackerRank account without my permission"      |
| Security credentials exposed             | Customer pastes a password, PIN, or auth token in the ticket body      |
| Data loss                                | "My test results were deleted", "My submission was lost"               |
| Service outage (no ETA known)            | "The entire site is down", "I can't access anything"                   |
| Ambiguous or contradictory request       | Ticket intent cannot be determined with confidence from ticket content |

### 1.2 Corpus-Triggered Escalation

These escalations occur when Sentinel or Anchor determines the corpus cannot support a confident grounded reply:

| Trigger                                             | Who detects               | Behavior                                     |
| --------------------------------------------------- | ------------------------- | -------------------------------------------- |
| No relevant corpus documentation                    | Sentinel (inference)      | `status=escalated` before Anchor is called   |
| Top retrieved chunk cosine similarity < 0.65        | Anchor (`grounded=false`) | Orchestrator overrides `replied → escalated` |
| LLM API failure after retries on Sentinel or Anchor | Orchestrator              | Safe-default to `status=escalated`           |

---

## 2. Handoff Package

When a ticket is escalated, the human agent receives the following in `output.csv`:

| Field           | Value for escalated tickets                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `status`        | `escalated`                                                                                                                      |
| `response`      | `"Escalate to a human"` (hardcoded — never LLM-generated)                                                                        |
| `justification` | 1–3 sentences from Sentinel explaining why escalation is required, citing the specific trigger (fraud, no corpus coverage, etc.) |
| `product_area`  | The most specific category identified by Scout                                                                                   |
| `request_type`  | Scout's classification (`product_issue`, `bug`, `feature_request`)                                                               |

The `justification` field is the primary signal for the human agent — it tells them exactly why this ticket was escalated, so they can prioritize and handle it appropriately.

---

## 3. What Human Agents Must NOT Rely On

- The `response` field for escalated tickets contains only the hardcoded string — it does not contain any corpus excerpts, diagnostic information, or draft answers. Human agents receive a blank-slate escalation, not a "draft for review."
- The pipeline does not pass through full ticket text in the output. Human agents must retrieve the original ticket from the source system using the ticket identifier.

---

## 4. Escalation Is Not a Fallback for Pipeline Failures

When the pipeline escalates due to API errors or timeouts (see `exception_handling.md`), the `justification` will note the pipeline failure:

```
justification: "Pipeline error: Sentinel API unavailable after retry. Escalated by default for safety."
```

This is distinct from a content-driven escalation. Human agents should be aware that some escalations represent genuine high-risk tickets, while others may be retryable if the API issue was transient.

---

## 5. Invalid Tickets Are NOT Escalated

Tickets classified as `request_type=invalid` (out-of-scope, adversarial, gibberish, prompt injection) receive `status=replied` with a polite out-of-scope message. They are **not** escalated to human agents. The rationale: human agents should not spend time reviewing off-topic requests or prompt injection attempts — the automated out-of-scope reply is the correct and complete resolution.

This is a firm rule. See `constitution.md` §7.3 and `guardrails.md` for full alignment.

---

## 6. No Live Handoff in This Version

This is a batch processing system — the "handoff" is the `output.csv` record. There is no real-time notification to human agents, no ticket management system integration, and no live chat handoff. Human agents review escalated rows in `output.csv` via their existing workflow.

Future versions may integrate with ticketing systems (Zendesk, Freshdesk) to create escalation tickets automatically — this is an out-of-scope item for v1.
