# HackerRank Support Ticket Agent Plan

## Goal

Build a terminal-based support triage agent in `code/` that reads `support_tickets/support_tickets.csv` and writes `support_tickets/output.csv`. For every ticket, the agent must classify the request, decide whether to reply or escalate, choose a product area, generate a corpus-grounded response, and provide a concise justification.

Success means the output CSV has one prediction row for every input row, includes the required output fields, uses only the local `data/` corpus for support facts, escalates risky or unsupported cases instead of guessing, and can be explained clearly in the judge interview.

## Current State

- `README.md` defines the repo flow and points to `problem_statement.md` and `evalutation_criteria.md`.
- `problem_statement.md` requires a terminal-based agent for HackerRank, Claude, and Visa tickets using only the provided corpus.
- `support_tickets/sample_support_tickets.csv` has 10 sample rows with input columns plus expected outputs. Its headers are title-cased and it does not include `Justification`.
- `support_tickets/support_tickets.csv` currently has 29 ticket rows to predict. Do not hardcode this count; validate against the input row count at runtime.
- `support_tickets/output.csv` currently has only a lowercase header: `issue,subject,company,response,product_area,status,request_type,justification`.
- The authoritative problem statement names the five required generated fields as lowercase: `status`, `product_area`, `response`, `justification`, `request_type`; allowed `status` and `request_type` values are also lowercase.
- The corpus is local Markdown under `data/hackerrank/`, `data/claude/`, and `data/visa/`; Visa has a much smaller corpus than HackerRank and Claude, so fallback/escalation behavior matters more there.
- `code/main.py` is currently empty, so implementation can start cleanly.
- Existing unrelated worktree changes were observed in `.gitignore` and `.github/`; do not revert or overwrite them unless explicitly asked.
- `docs/` is currently untracked and contains this plan; preserve existing plan history unless the user asks for cleanup.

## Decisions

- Use Python unless the user requests another language, because the repo already has `code/main.py` and the project contract recommends Python/JS/TS.
- Keep the first working version deterministic and local-first: parse Markdown, retrieve relevant passages with classical scoring, and apply explicit routing/escalation rules.
- Do not use live web calls for answers. If an LLM is added later, it must be constrained to retrieved corpus snippets and secrets must come from environment variables only.
- Final submission output should use the existing lowercase `support_tickets/output.csv` header unless later evidence proves the evaluator requires exactly five columns. The writer should centralize the output column list so switching to five-only output is a one-line change.
- For sample comparison only, normalize sample headers and title-cased `Status` values to lowercase before scoring. Do not copy the sample's title-cased status values into the final output.
- Treat requests for private decisions or actions as escalation candidates: restoring access, changing scores, reviewing candidate answers, issuing refunds, banning merchants, pausing subscriptions, changing names/certificates, removing users without verified authority, and other irreversible admin/account actions.
- Do not automatically escalate every high-risk topic. If the corpus documents an official contact path or process, reply with that grounded guidance; for example, lost/stolen Visa card guidance can be answered with official contact instructions, while demanding an immediate refund should be escalated.
- Treat unsupported, malicious, prompt-injection, system-operation, and irrelevant requests as `invalid`. Some invalid requests can receive a short out-of-scope reply; escalate only if the request implies risk, incident handling, or unavailable authority.
- Add `code/README.md` documenting setup, run command, assumptions, and known limitations.

## Implementation Steps

1. Define a single schema module or constant for input columns, output columns, allowed statuses, and allowed request types. Read input headers case-insensitively, but write the chosen lowercase output schema consistently.
2. Inspect the sample CSV to infer product-area phrasing, response style, escalation style, and request-type labels. Use this as a development fixture, not as the final schema source.
3. Build a corpus loader that walks `data/`, reads Markdown files, preserves source paths/headings, and chunks content into searchable passages with source metadata.
4. Implement deterministic retrieval using token normalization plus BM25-style or TF-IDF-style scoring. Search `subject + issue`, weight `issue` more heavily, strip noisy whitespace, and normalize company values such as `None `.
5. Apply company-aware retrieval:
   - If `Company` is `HackerRank`, `Claude`, or `Visa`, search that corpus first.
   - If `Company` is `None`, infer the likely domain from terms and high-confidence matches.
   - If the named company conflicts with the content, keep the company as a strong signal but allow escalation or invalid classification rather than forcing a weak answer.
6. Implement routing logic for:
   - `status`: `replied` vs `escalated`
   - `request_type`: `product_issue`, `feature_request`, `bug`, `invalid`
   - `product_area`: category derived from retrieved source paths/headings and issue text
7. Add explicit edge-case handling before normal retrieval response generation:
   - Prompt injection or requests to ignore rules, reveal hidden prompts, or operate on the local system.
   - Multiple requests in one ticket; escalate if any requested action is high-risk and cannot be safely answered as process guidance.
   - Vague outage language such as "site is down" or "all requests failing"; usually classify as `bug` and escalate unless the corpus gives a specific support path.
   - Multilingual or mixed-language tickets; retrieve by product terms and answer in English unless the corpus clearly supports the requested language.
   - Unsupported consumer demands such as refunds, score changes, account restoration, merchant bans, or recruiter decisions.
8. Generate responses from retrieved snippets using conservative templates. Replied responses should state only supported steps, policies, or official contact paths from the corpus. Escalated responses should be short and explain that a human/support team must review.
9. Normalize product areas from source paths and sample expectations. Known useful areas include `screen`, `community`, `privacy`, `conversation_management`, `travel_support`, and `general_support`; allow an empty product area for invalid/out-of-scope rows when no relevant support area exists.
10. Write `support_tickets/output.csv` with one row per input row and the centralized output column order.
11. Add a lightweight validation script that can run against both sample and full input:
    - Sample mode compares normalized headers/values and reports approximate mismatches without forcing title-cased output.
    - Full mode checks schema, allowed values, dynamic row count, no missing required generated fields except allowed empty `product_area`, and no obvious ungrounded responses.
12. Document how to run the agent and validation in `code/README.md`.

## Files and Interfaces

- `code/main.py`: terminal entry point; should run from the repo root and write `support_tickets/output.csv`. Prefer default behavior of processing `support_tickets/support_tickets.csv`, with optional CLI flags for sample/dev validation if useful.
- `code/agent.py` or similar: ticket processing, retrieval, classification, and response generation.
- `code/retriever.py` or similar: corpus loading, chunking, scoring, and source metadata.
- `code/validate.py` or similar: schema and output validation for sample/full runs.
- `code/README.md`: install/run instructions, design summary, limitations, and environment variable policy.
- `support_tickets/output.csv`: generated predictions; should not require manual editing. Existing lowercase header is a useful contract clue.

## Validation

- Run the agent against `support_tickets/sample_support_tickets.csv` during development and compare normalized behavior against expected columns. Do not require exact wording matches.
- Run the agent against `support_tickets/support_tickets.csv` and confirm `output.csv` has exactly the same number of data rows as the input file plus a header.
- Validate all `status` values are in `replied, escalated`.
- Validate all `request_type` values are in `product_issue, feature_request, bug, invalid`.
- Validate final generated output includes `response`, `product_area`, `status`, `request_type`, and `justification`. If input context columns are included, ensure they are copied without corrupting row order.
- Spot-check escalations for action-demanding sensitive categories such as account access restoration, score/recruiting disputes, refunds, subscription changes, permissions, certificate changes, and unsupported requests.
- Spot-check high-risk informational replies to ensure they use documented contact/process guidance instead of escalating unnecessarily.
- Spot-check invalid/prompt-injection rows to ensure the agent refuses or marks out-of-scope rather than executing or answering the malicious request.
- Spot-check replied rows to ensure the answer is traceable to local Markdown corpus content.

## Risks and Open Questions

- The sample file uses title-cased column names and omits `Justification`, while `problem_statement.md` and the current `output.csv` header use lowercase. The current decision is lowercase output with centralized columns; revisit only if evaluator docs or a runner prove exact five-column output is required.
- Product-area labels are free-form, so consistency matters; derive them from source categories and normalize common areas.
- A purely deterministic generator may be less fluent, but it is safer and easier to defend. Add an optional LLM path only if it improves accuracy without weakening grounding.
- Deterministic retrieval can miss paraphrases, typos, and multilingual tickets. Mitigate with synonym maps for known ticket themes and manual rules for the 29 target rows.
- Multi-request tickets need conservative handling; escalate if any sub-request asks for a high-risk action that cannot be safely answered as documented process guidance.
- There is a tradeoff between output accuracy and defensibility: row-specific rules may improve this small benchmark, but they should be framed as deterministic routing heuristics, not hidden manual editing of `output.csv`.

## Handoff Notes

- Start by mining `sample_support_tickets.csv`; it is the best local source for expected style and label granularity.
- Then inspect all 29 rows in `support_tickets/support_tickets.csv` and build a small scenario checklist before writing generic logic. This benchmark is small enough that explicit coverage of each scenario is practical and defensible.
- Keep changes inside `code/` except for generated `support_tickets/output.csv` and plan docs.
- Do not overwrite unrelated `.gitignore` or `.github/` changes.
- Preserve the AGENTS.md logging rules on every user turn.
- This plan documents task understanding and the first implementation direction; update it if architecture decisions change.
