# PRD — HackerRank Orchestrate Multi-Domain Support Triage Agent

## 1. Document Control

| Field    | Value                                                          |
| -------- | -------------------------------------------------------------- |
| Version  | 1.0.0                                                          |
| Status   | Draft — approved for implementation                            |
| Owner    | Submission Team (HackerRank Orchestrate hackathon participant) |
| Author   | Agent 3 (PRD author), Claude Code Opus 4.7                     |
| Date     | 2026-05-01                                                     |
| Deadline | 2026-05-02 11:00 IST (`2026-05-02T11:00:00+05:30`)             |
| Sources  | `AGENTS.md` §6, `problem_statement.md`, `README.md`, `evalutation_criteria.md` |

---

## 2. Background & Opportunity

Support organizations across HackerRank, Anthropic (Claude), and Visa receive thousands of inbound tickets that mix routine FAQs, sensitive billing/fraud cases, ambiguous multi-request bodies, and adversarial or out-of-scope content. Frontline triage today is human-bottlenecked, expensive, and inconsistent.

The opportunity is a **terminal-based, corpus-grounded triage agent** that, for each row in `support_tickets/support_tickets.csv`, produces a deterministic 5-column decision (`status`, `product_area`, `response`, `justification`, `request_type`). The agent must answer the easy cases faithfully from the shipped corpus under `data/{hackerrank,claude,visa}/`, and escalate everything that is high-risk, sensitive, ambiguous, or unsupported — without ever guessing or hallucinating policy.

This PRD defines the product surface that downstream architecture (retrieval index, classifier, response generator, escalation policy, CSV writer) must satisfy in order to be evaluable under `evalutation_criteria.md`.

---

## 3. Goals & Non-Goals

### 3.1 Goals

- G-1: Produce a fully populated `support_tickets/output.csv` for every input row, in a single non-interactive terminal run.
- G-2: Ground every `replied` answer in retrieved snippets from `data/` only; cite or trace the snippet in `justification`.
- G-3: Escalate every ticket the agent cannot answer safely (sensitive, out-of-corpus, malicious, multi-request beyond confident scope, `company=None` with insufficient signal).
- G-4: Be deterministic and reproducible: same input CSV ⇒ byte-identical `output.csv` (modulo timestamps if any).
- G-5: Score competitively across all four evaluation dimensions: Agent Design, AI Judge, Output CSV accuracy, AI Fluency.

### 3.2 Non-Goals

- NG-1: Multi-turn dialogue with the end user (input is a single ticket body; output is a single response).
- NG-2: Live web fetches, model fine-tuning, or use of any knowledge outside `data/`.
- NG-3: Building a UI, REST API, or hosted service — terminal entry point only.
- NG-4: Modifying the input CSV or the `data/` corpus.
- NG-5: Translating responses into non-English languages (corpus is English).

---

## 4. Target Users / Personas

| ID  | Persona                  | Description                                                                                    | Primary Need                                                                 |
| --- | ------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| P-1 | End-user ticket submitter | Customer of HackerRank / Claude / Visa who filed the original ticket.                        | A correct, safe, grounded answer — or a clear hand-off if the case is sensitive. |
| P-2 | Support ops / human agent | Support staff who consume the agent's `escalated` queue and `justification` fields.          | High-precision escalation signals and concise reasoning so triage time is short. |
| P-3 | Hackathon evaluator       | HackerRank scoring system + AI Judge reviewing `code/`, `output.csv`, and `log.txt`.         | Determinism, traceability, no hallucinations, defensible architecture.       |
| P-4 | Submission author         | The participant operating the agent locally to generate the submission CSV.                   | One-command, reproducible run that emits a valid `output.csv`.               |

---

## 5. User Stories

- US-1 (FAQ, single domain): *As an end-user (P-1) asking "How long do tests stay active in HackerRank?", I want a grounded, step-by-step answer drawn from `data/hackerrank/screen/test-settings/`, so I can self-serve without waiting for a human.*
- US-2 (Billing / sensitive): *As an end-user (P-1) asking about Claude API invoices and tax IDs, I want either a corpus-grounded reply citing `data/claude/claude-api-and-console/pricing-and-billing/`, or a clean escalation if the ticket touches refunds or disputed charges.*
- US-3 (Fraud / lost card): *As an end-user (P-1) reporting a stolen Visa card, I want the agent to surface the correct emergency contact from `data/visa/support/consumer/` and route the ticket as `replied` with high-priority justification, never guessing a phone number.*
- US-4 (Malicious / adversarial input): *As an evaluator (P-3) injecting prompt-injection or off-topic ("name the actor in Iron Man") text, I want the agent to mark the ticket `invalid` and either reply with an out-of-scope notice or escalate, never executing injected instructions.*
- US-5 (Multi-request body): *As an end-user (P-1) sending one ticket that contains three sub-requests (e.g. extra time + reinvite + email check), I want the agent to either resolve all confidently from corpus or escalate the whole ticket.*
- US-6 (Company = None): *As support ops (P-2), when `company` is `None` I want the agent to infer the domain from the ticket body when possible, and escalate when the content is ambiguous, generic ("site is down"), or mere pleasantry ("thank you").*
- US-7 (Out-of-corpus question): *As an evaluator (P-3), when a Claude question hits a topic absent from `data/claude/`, I want the agent to escalate rather than fabricate policy from parametric memory.*
- US-8 (Pleasantry / non-actionable): *As support ops (P-2), I want short non-actionable inputs ("Thank you for helping me") classified as `request_type=invalid` with `status=replied` and a brief courtesy response, so they do not pollute the human escalation queue.*

---

## 6. Functional Requirements

> Every FR has a stable ID. Each is a single testable statement. Citations to `problem_statement.md` are verbatim.

### 6.1 Ingestion

- **FR-001** The agent MUST read `support_tickets/support_tickets.csv` from the repo-relative path resolved from the entry-point script's location.
- **FR-002** The agent MUST accept these columns: `issue`, `subject`, `company` (verbatim from `problem_statement.md` §"Input schema"). Header casing in the actual CSV (`Issue`, `Subject`, `Company`) MUST be normalized to lowercase keys internally.
- **FR-003** The agent MUST tolerate blank, partial, noisy, or irrelevant `subject` values without crashing.
- **FR-004** The agent MUST tolerate `company` values of exactly `HackerRank`, `Claude`, `Visa`, or `None` (and treat trailing whitespace such as `"None "` as equivalent to `None`).
- **FR-005** The agent MUST treat `company=None` as a signal that the issue may be generic or cross-domain and infer best handling from `issue` content (per `problem_statement.md`).
- **FR-006** The agent MUST process every input row exactly once and never silently drop rows.

### 6.2 Classification

- **FR-010** The agent MUST emit `request_type` ∈ {`product_issue`, `feature_request`, `bug`, `invalid`} for every row.
- **FR-011** `request_type=invalid` MUST be used for non-actionable, off-topic, malicious, or pleasantry inputs (US-4, US-8).
- **FR-012** `request_type=bug` MUST be used when the user reports a defect or outage (e.g. "site is down").
- **FR-013** `request_type=feature_request` MUST be used when the user asks for new capability not present in the corpus.
- **FR-014** `request_type=product_issue` MUST be used for how-to / configuration / account / billing / support questions answerable or escalatable within the product.
- **FR-015** The agent MUST emit `product_area` as a short category string drawn from (or directly mappable to) the directory structure under `data/`. Valid examples sampled from the shipped corpus:
  - `Claude > Claude API and Console > Pricing & Billing` (e.g. `data/claude/claude-api-and-console/pricing-and-billing/`)
  - `Claude > Claude Code` (e.g. `data/claude/claude-code/`)
  - `Claude > Pro and Max Plans` (e.g. `data/claude/pro-and-max-plans/`)
  - `Claude > Privacy and Legal` (e.g. `data/claude/privacy-and-legal/`)
  - `HackerRank > Screen > Test Settings` (e.g. `data/hackerrank/screen/test-settings/`)
  - `HackerRank > Screen > Invite Candidates` (e.g. `data/hackerrank/screen/invite-candidates/`)
  - `HackerRank > Library > Question Types` (e.g. `data/hackerrank/library/question-types/`)
  - `HackerRank > Community` (e.g. `data/hackerrank/hackerrank_community/`)
  - `HackerRank > Interviews` (e.g. `data/hackerrank/interviews/`)
  - `Visa > Consumer > Travel Support` (e.g. `data/visa/support/consumer/travel-support/`)
  - `Visa > Consumer > Traveller's Cheques` (e.g. `data/visa/support/consumer/travelers-cheques.md`)
  - `Visa > Small Business > Fraud Protection` (e.g. `data/visa/support/small-business/fraud-protection.md`)
- **FR-016** When the agent cannot map the ticket to a corpus subtree with confidence above the configured threshold, it MUST set `product_area` to a documented fallback (`uncategorized` or `general_support`) AND set `status=escalated`.
- **FR-017** The classifier MUST use `company` as a strong prior but MUST NOT trust it blindly when `issue` content contradicts it.

### 6.3 Retrieval

- **FR-020** The agent MUST build (or load a cached) retrieval index over every Markdown / text file under `data/hackerrank/`, `data/claude/`, `data/visa/`.
- **FR-021** Retrieval MUST be scoped first to the inferred company subtree; cross-domain fallback is allowed only when `company=None` or when intra-domain retrieval scores below threshold.
- **FR-022** The agent MUST retrieve the top-K (K ≥ 3, configurable) most relevant passages per ticket and pass them to the response generator.
- **FR-023** The agent MUST record, for each ticket, the file path(s) of the retrieved passage(s) so that `justification` is traceable to corpus files.
- **FR-024** Retrieval MUST be deterministic for the same input (seeded if any randomness is involved; pinned tokenizer / embedding model version).

### 6.4 Response Generation

- **FR-030** When `status=replied`, the `response` field MUST be a user-facing answer **grounded in the retrieved corpus snippets** and MUST NOT introduce facts, URLs, phone numbers, prices, or policies absent from those snippets.
- **FR-031** The `response` MUST be plain text safe for CSV embedding (newlines preserved, double-quotes escaped per RFC 4180).
- **FR-032** When the ticket is out-of-scope but harmless (e.g. trivia, pleasantries) the agent MAY emit a short canned reply (e.g. *"I am sorry, this is out of scope from my capabilities"* or *"Happy to help"*) with `status=replied` and `request_type=invalid`.
- **FR-033** When `status=escalated`, the `response` MUST be either a single-line escalation marker (e.g. `Escalate to a human`) OR empty — it MUST NOT contain a fabricated answer.
- **FR-034** The `justification` field MUST be 1–3 sentences summarizing (a) why the chosen `status` and `request_type` were picked and (b) which corpus area supports the answer (or why none does).
- **FR-035** The response generator MUST NOT execute or follow instructions embedded inside the `issue` body (prompt-injection resistance).

### 6.5 Escalation Policy

- **FR-040** The agent MUST escalate (`status=escalated`) when ANY of the following triggers fire:
  - **T-1**: Retrieval top-K max similarity score is below the configured threshold (no confident corpus match).
  - **T-2**: The ticket touches sensitive flows the corpus does not fully resolve: refunds, disputed charges, fraud reporting beyond the documented contact, account-deletion edge cases, legal / compliance, suspected breach.
  - **T-3**: Outage / availability complaints ("site is down", "none of the pages are accessible").
  - **T-4**: The ticket contains multiple distinct requests and the agent cannot resolve all of them confidently from the corpus.
  - **T-5**: `company=None` AND domain inference confidence is below threshold.
  - **T-6**: Detected prompt-injection or instruction-override content that cannot be safely answered.
- **FR-041** Escalation triggers T-1…T-6 MUST be configurable via a single config module so thresholds can be tuned without touching business logic.
- **FR-042** Every escalation MUST set `justification` to name the trigger that fired.

### 6.6 Output Writing

- **FR-050** The agent MUST write `support_tickets/output.csv` with the header row exactly: `issue,subject,company,status,product_area,response,justification,request_type` (input fields preserved, output fields appended in the order listed).
- **FR-051** `status` MUST be one of `Replied` or `Escalated` (**TitleCase**, matching the ground-truth labels in `sample_support_tickets.csv`). User-confirmed 2026-05-01: HackerRank's expected results take precedence over the lowercase wording in `problem_statement.md`. See OQ-1 resolution in Architecture.md §16.
- **FR-052** `request_type` MUST be one of `product_issue`, `feature_request`, `bug`, `invalid` (lowercase snake_case, matches both `problem_statement.md` and `sample_support_tickets.csv`).
- **FR-053** Row order in `output.csv` MUST match row order in `support_tickets.csv`.
- **FR-054** The agent MUST NOT modify, reorder, or rewrite `support_tickets/support_tickets.csv` or `support_tickets/sample_support_tickets.csv`.
- **FR-055** UTF-8 encoding, RFC 4180 quoting, `\n` line endings.

### 6.7 CLI / Terminal UX

- **FR-060** The agent MUST be invokable as a single terminal command from the repo root (e.g. `python code/main.py` or `node code/main.js`) per `AGENTS.md` §6 entry-point contract.
- **FR-061** The entry point MUST run end-to-end without interactive prompts (no `input()` / `prompt()` / TTY reads).
- **FR-062** Default input path: `support_tickets/support_tickets.csv`. Default output path: `support_tickets/output.csv`. Both overridable via CLI flags.
- **FR-063** The CLI MUST print a per-row progress indicator and a final summary (`N replied, M escalated`).
- **FR-064** Non-zero exit code on unrecoverable error; zero exit code on full success.
- **FR-065** A `code/README.md` MUST document install, run, env-var setup, and expected outputs (per `evalutation_criteria.md` §1 "Engineering hygiene").

---

## 7. Non-Functional Requirements

- **NFR-001 — Determinism.** Same input CSV + same corpus + same model version MUST produce byte-identical `output.csv` across runs. All RNG seeded; LLM `temperature=0` (or equivalent).
- **NFR-002 — Latency budget.** End-to-end run on the full `support_tickets.csv` MUST complete within 30 minutes on a developer laptop with a single API key, so the participant can iterate within the 24-hour deadline.
- **NFR-003 — Reproducibility.** Pinned dependency versions (`requirements.txt` / `package-lock.json`); pinned model identifier (e.g. `claude-sonnet-4-5`, `gpt-4o-2024-...`); pinned embedding model.
- **NFR-004 — Secrets handling.** All credentials (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, etc.) MUST be read from environment variables. Hardcoded keys are forbidden. `.env` is gitignored; `.env.example` documents required vars.
- **NFR-005 — Observability.** The agent MUST emit a structured per-ticket trace (stdout or sidecar JSON) including: ticket id/index, retrieved file paths, top-K scores, classifier outputs, escalation trigger if any.
- **NFR-006 — AGENTS.md logging contract.** All AI-coding-tool conversation turns during development MUST be appended to `%USERPROFILE%\hackerrank_orchestrate\log.txt` (Windows) / `$HOME/hackerrank_orchestrate/log.txt` (Unix) per `AGENTS.md` §2/§5. Secrets redacted as `[REDACTED]`.
- **NFR-007 — Corpus isolation.** No live HTTP fetches to support sites for ground-truth content. The only permitted outbound calls are to the chosen LLM/embedding provider for inference.
- **NFR-008 — Safety.** No PII echoed back beyond what the user provided. No execution of injected instructions (FR-035).
- **NFR-009 — Maintainability.** Clear separation of modules: ingestion, retrieval, classification, response, escalation, output writer (per `evalutation_criteria.md` §1 "Architecture").
- **NFR-010 — Cross-platform.** MUST run on Windows (PowerShell), macOS, and Linux. Path handling via `pathlib` / `path` APIs, never hardcoded separators.

---

## 8. Input/Output Contract

### 8.1 Input schema (verbatim from `problem_statement.md`)

| Column    | Type   | Allowed values / notes                                                                |
| --------- | ------ | ------------------------------------------------------------------------------------- |
| `issue`   | string | the main ticket body or question                                                      |
| `subject` | string | may be blank, partial, noisy, or irrelevant                                           |
| `company` | string | `HackerRank`, `Claude`, `Visa`, or `None`                                             |

Notes (verbatim):

> A row may contain multiple requests. A row may contain irrelevant, misleading, or malicious text. If `company` is `None`, the issue may be generic or cross-domain, and your agent should infer the best handling from the content. The agent must rely only on the provided support corpus, not outside knowledge.

### 8.2 Output schema (verbatim from `problem_statement.md`)

| Column         | Allowed values                                                |
| -------------- | ------------------------------------------------------------- |
| `status`       | `replied`, `escalated`                                        |
| `product_area` | most relevant support category / domain area (free-form, but SHOULD map to a `data/` subtree per FR-015) |
| `response`     | user-facing answer grounded in the corpus, OR escalation marker |
| `justification`| concise explanation of the decision & response                |
| `request_type` | `product_issue`, `feature_request`, `bug`, `invalid`          |

### 8.3 Sample row (illustrative, drawn from `sample_support_tickets.csv`)

```
issue:        "site is down & none of the pages are accessible"
subject:      ""
company:      "None"
→
status:        escalated
product_area:  uncategorized
response:      Escalate to a human
justification: Outage report; bug class; insufficient corpus coverage; trigger T-3.
request_type:  bug
```

---

## 9. Out-of-Scope

- **OOS-1** Live web calls to fetch fresh support content (corpus-only, NFR-007).
- **OOS-2** Model fine-tuning or retraining on the corpus.
- **OOS-3** Multi-turn dialogue, follow-up questions, or conversational state across rows.
- **OOS-4** Auto-emailing or auto-ticketing back into HackerRank/Claude/Visa systems.
- **OOS-5** Hosted UI, REST API, webhook, or daemon mode.
- **OOS-6** Translation, transliteration, or multilingual support.
- **OOS-7** PII redaction beyond what the corpus already requires.
- **OOS-8** Modifying the input CSV, the corpus, or `AGENTS.md`.

---

## 10. Success Metrics

Mapped 1:1 to `evalutation_criteria.md`:

| ID    | Dimension                  | Metric                                                                                                  | Target                                                  |
| ----- | -------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| SM-1  | §1 Agent Design            | Reviewer can identify discrete modules for retrieval, reasoning, routing, output; deterministic config. | All five modules present; pinned deps; runnable README. |
| SM-2  | §2 AI Judge                | Author can articulate trade-offs and failure modes per module on demand.                                | 30-min interview without unanswered design questions.   |
| SM-3a | §3 Output CSV — `status`        | Replied vs escalated correct.                                                                       | ≥ 90% on sample set.                                    |
| SM-3b | §3 Output CSV — `product_area`  | Matches a real corpus subtree per FR-015.                                                           | ≥ 85% on sample set.                                    |
| SM-3c | §3 Output CSV — `response`      | Faithful, grounded, non-hallucinated.                                                               | 0 fabricated facts on spot-check sample.                |
| SM-3d | §3 Output CSV — `justification` | Concise, traceable to a corpus file path.                                                           | 100% rows reference a trigger or a file.                |
| SM-3e | §3 Output CSV — `request_type`  | Correct of {product_issue, feature_request, bug, invalid}.                                          | ≥ 90% on sample set.                                    |
| SM-4  | §4 AI Fluency              | `log.txt` shows scoped prompts, critique, verification, author-driven decisions.                        | Per-turn entries present, redacted, append-only.        |

---

## 11. Constraints & Assumptions

- **C-1** Corpus is fixed at `data/{hackerrank,claude,visa}/`; no additions, deletions, or edits.
- **C-2** Agent is terminal-based and runs locally on the participant's machine (per `problem_statement.md` "Requirements").
- **C-3** Secrets loaded only from env vars (per `AGENTS.md` §6.6 + `evalutation_criteria.md` §1).
- **C-4** AGENTS.md logging contract (§2/§5) applies to every conversation turn during development.
- **C-5** Submission deadline: **2026-05-02 11:00 IST**. Results: 2026-05-15 12:00 IST.
- **C-6** Recommended language: Python, JavaScript, or TypeScript (per `AGENTS.md` §1).
- **C-7** Entry point lives in `code/` (per `AGENTS.md` §6.1).
- **A-1** `output.csv` *header* uses the spec's lowercase column names (`issue,subject,company,status,product_area,response,justification,request_type` — FR-050). `output.csv` *value* casing matches the sample CSV ground-truth labels: `status` is **TitleCase** (`Replied`/`Escalated`), `request_type` and `product_area` are lowercase snake_case (FR-051, FR-052). User-confirmed 2026-05-01.
- **A-2** A single LLM provider key (Anthropic or OpenAI) is sufficient to meet latency budget NFR-002.
- **A-3** The participant has read network access at run time **only** for the chosen LLM/embedding provider.

---

## 12. Risks & Mitigations

| ID   | Risk                                                                            | Likelihood | Impact | Mitigation                                                                                                |
| ---- | ------------------------------------------------------------------------------- | ---------- | ------ | --------------------------------------------------------------------------------------------------------- |
| R-1  | Hallucinated policies / invented phone numbers or prices.                      | High       | High   | FR-030 grounding rule; FR-035 prompt-injection resistance; reviewer spot-check (SM-3c).                   |
| R-2  | Over-escalation (everything gets `escalated`) tanks `status` accuracy.         | Medium     | High   | Thresholds (FR-041) tuned against `sample_support_tickets.csv` before final run.                          |
| R-3  | Under-escalation on sensitive billing/fraud tickets.                            | Medium     | High   | Hard-coded sensitive-topic triggers in T-2/T-3 even when corpus retrieval succeeds.                       |
| R-4  | Inconsistent column casing between sample CSV and `problem_statement.md` spec. | High       | Med    | FR-002 normalization; output CSV always uses lowercase per FR-050.                                        |
| R-5  | Non-determinism from LLM `temperature>0` or unseeded sampling.                  | Medium     | Med    | NFR-001 mandates `temperature=0` and seeded RNG.                                                          |
| R-6  | Long run time on full `support_tickets.csv` blows latency budget.               | Medium     | Med    | Cache embeddings to disk; batch retrieval; allow `--limit N` for dev.                                     |
| R-7  | Secrets accidentally committed.                                                 | Low        | High   | `.env` gitignored; pre-commit hook OR explicit code review checklist; no key strings in source.           |
| R-8  | AGENTS.md log not appended (evaluator penalizes AI Fluency).                    | Medium     | Med    | NFR-006; per-turn logging treated as a blocking step before any tool call.                                |
| R-9  | Multi-request rows (US-5) get a partial answer.                                 | Medium     | Med    | T-4 escalation when not all sub-requests can be confidently answered.                                     |
| R-10 | Corpus drift between dev and eval (none expected, but worth checking).          | Low        | Low    | Compute and log a SHA-256 manifest of `data/` at run start.                                               |

---

## 13. Acceptance Criteria

The submission is accepted when ALL of the following hold:

- **AC-1** Running the documented entry point from a clean clone with required env vars set produces `support_tickets/output.csv` exit code 0.
- **AC-2** `output.csv` row count equals `support_tickets.csv` row count; header matches FR-050; row order preserved.
- **AC-3** Every row's `status` ∈ {`Replied`, `Escalated`} (TitleCase); every row's `request_type` ∈ {`product_issue`, `feature_request`, `bug`, `invalid`} (lowercase).
- **AC-4** Every `Replied` row's `response` can be traced to at least one file under `data/`; spot-check on 10 random `Replied` rows finds zero hallucinated facts.
- **AC-5** Every `Escalated` row's `justification` names one of triggers T-1…T-6.
- **AC-6** Every triggering scenario in §11.R-3 (sensitive billing/fraud) is escalated or grounded in a directly relevant corpus file (no parametric guessing).
- **AC-7** Out-of-scope trivia rows (e.g. "What is the name of the actor in Iron Man?") are marked `request_type=invalid` with either an explicit out-of-scope reply or escalation.
- **AC-8** Outage/availability complaints (e.g. "site is down") are `request_type=bug`, `status=Escalated`.
- **AC-9** `code/README.md` exists and documents install + run.
- **AC-10** `log.txt` at the AGENTS.md path exists, has the `AGREEMENT RECORDED:` line for this repo root, and contains §5.2 per-turn entries.
- **AC-11** No API keys present in any committed file.
- **AC-12** Two consecutive runs over the same input produce identical `output.csv` (NFR-001).

---

## 14. Milestones (24-hour timeline)

Anchor: now = 2026-05-01 (any IST hour). Deadline: **2026-05-02 11:00 IST**.

| Milestone | T-offset (from start) | Deliverable                                                                          |
| --------- | --------------------- | ------------------------------------------------------------------------------------ |
| M-0       | T+0h                  | AGENTS.md onboarding complete; agreement recorded; PRD + ProblemAnalysis on disk.    |
| M-1       | T+2h                  | Repo skeleton: `code/main.py`, `code/agent.py`, `code/retriever.py`, `code/classifier.py`, `code/escalation.py`, `code/output_writer.py`, `code/README.md`. |
| M-2       | T+5h                  | Corpus indexed (embeddings or BM25) for all three domains; index cached on disk.     |
| M-3       | T+9h                  | Classifier (`request_type`, `product_area`) producing valid outputs on sample CSV.   |
| M-4       | T+13h                 | Response generator with grounding + prompt-injection guard; passes US-1, US-2, US-3. |
| M-5       | T+16h                 | Escalation policy with all six triggers wired; passes US-4, US-5, US-6, US-7, US-8.  |
| M-6       | T+19h                 | Full dry-run on `sample_support_tickets.csv`; tune thresholds; meet SM-3a/3e ≥ 90%.  |
| M-7       | T+21h                 | Full run on `support_tickets.csv`; produce final `output.csv`; AC-1…AC-12 verified.  |
| M-8       | T+22h                 | Zip `code/`; collect `log.txt`; submit on HackerRank Community Platform.             |
| M-9       | T+24h (deadline)      | Buffer / final sanity check / submission confirmed.                                  |

If fewer than 2 hours remain at any point, suspend feature work and execute M-7 → M-8 immediately (per `AGENTS.md` §4.3).

---

## 15. Glossary

- **Corpus** — the union of Markdown / text files under `data/hackerrank/`, `data/claude/`, and `data/visa/`. The only ground-truth source of fact.
- **Domain** — one of HackerRank, Claude, or Visa. Selected from `company` field, or inferred from `issue` when `company=None`.
- **Product area** — the corpus subtree most relevant to a ticket; the value emitted in the `product_area` output column. See FR-015 for examples.
- **Escalation** — emitting `status=escalated` and not answering, because the ticket is sensitive, unsupported, ambiguous, malicious, or out-of-corpus.
- **Grounded answer** — a `response` whose substantive claims are all supported by retrieved corpus passages.
- **Trigger T-1…T-6** — the six escalation conditions defined in FR-040.
- **Entry point** — the terminal-invokable script under `code/` (e.g. `code/main.py`) that reads the input CSV and writes `output.csv`.
- **AGENTS.md log** — the append-only conversation log at `~/hackerrank_orchestrate/log.txt`, maintained per `AGENTS.md` §2 and §5.
- **AI Judge** — the post-submission 30-minute camera-on interview that scores depth of understanding and trade-off awareness (per `evalutation_criteria.md` §2).
