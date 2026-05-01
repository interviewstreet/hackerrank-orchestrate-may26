# Execution Plan — HackerRank Orchestrate Support Triage Agent

| Field    | Value                                                          |
| -------- | -------------------------------------------------------------- |
| Version  | 1.0.0                                                          |
| Status   | Draft — approved for implementation                            |
| Author   | Agent 5 (Senior SWE), Claude Code Opus 4.7                     |
| Date     | 2026-05-01                                                     |
| Inputs   | `docs/Architecture.md`, `docs/PRD.md`, `docs/ProblemAnalysis.md`, `AGENTS.md` §6, `.env`, `.gitignore` |
| Targets  | All FR-001…FR-065, NFR-001…NFR-010, T-1…T-6, AC-1…AC-12 in PRD |

---

## 1. Strategy Overview

A senior engineer's playbook for delivering a corpus-grounded triage agent under a 24-hour deadline. The strategy has four pillars:

1. **TDD red→green→refactor.** Agent 6 (Test Engineer) writes the failing tests first; Agent 5 (Senior SWE) writes the smallest implementation that turns them green; both agents refactor only once green is locked. No code lands without a failing test that drove it.
2. **Vertical slices, not horizontal layers.** Each iteration ships a thin end-to-end slice (loader → writer first, then retrieval, then reasoning) so we always have a runnable artifact, even if degenerate. This protects against the classic "all infra, no demo" failure mode at the deadline.
3. **Risk-first ordering.** The highest-uncertainty, highest-leverage components ship first: (a) CSV round-trip with correct casing (R-4), (b) deterministic retrieval (R-5, R-10), (c) escalation policy (R-1, R-2, R-3). Reasoner LLM polish lands last because it has the biggest cost-per-iteration.
4. **Determinism is a feature, not a chore.** Every iteration's exit gate includes "two consecutive runs of the relevant unit produce identical output" (NFR-001, AC-12). We do not defer this to M-7 — we bake it into Iter 1.

Time budget anchor: now is **2026-05-01 ~13:00 IST**. Deadline **2026-05-02 11:00 IST** = ~22 working hours. This plan budgets **18 hours of build + 4 hours buffer** so M-7 (full run + submission packaging) has room to recover from a single bad iteration.

---

## 2. Definition of Done

### 2.1 Per-iteration DoD (every iter must satisfy)

- All red tests Agent 6 wrote for the iter are green.
- No regression: full `pytest code/tests/ -q` is green at iter close.
- Smoke import test still passes (`test_smoke.py`).
- No new lint/parse errors (`python -m compileall code/`).
- README + `code/instructions.txt` updated by Agent 7 if the run command or env-var surface changed.
- Per-turn §5.2 entry appended to `~/hackerrank_orchestrate/log.txt`.
- Determinism check where applicable: same input → byte-identical output of that unit (loader, retriever, escalation) across two invocations.

### 2.2 Whole-submission DoD (tied to PRD Acceptance Criteria)

- **AC-1**: `python code/main.py` runs from a clean clone with env vars set, exit code 0.
- **AC-2**: `output.csv` row count == `support_tickets.csv` row count; header `issue,subject,company,status,product_area,response,justification,request_type` exact; row order preserved.
- **AC-3**: every `status` ∈ {Replied, Escalated}; every `request_type` ∈ {product_issue, feature_request, bug, invalid}; every `product_area` lowercase snake_case.
- **AC-4**: every Replied row's `response` traceable to ≥1 file under `data/`; spot-check 10 rows = 0 fabricated facts.
- **AC-5**: every Escalated row's `justification` names T-1…T-6.
- **AC-6**: sensitive billing/fraud rows escalated or grounded in directly relevant corpus file.
- **AC-7**: trivia rows → `request_type=invalid`, replied with out-of-scope OR escalated.
- **AC-8**: outage rows → `request_type=bug`, `status=Escalated`.
- **AC-9**: `code/README.md` documents install + run; `instructions.txt` (Agent 7) at root for evaluator.
- **AC-10**: `log.txt` has `AGREEMENT RECORDED:` for this repo + per-turn §5.2 entries.
- **AC-11**: zero API keys in any committed file.
- **AC-12**: two consecutive runs over same input → identical `output.csv`.

---

## 3. Iteration Roadmap

| # | Name                                  | Time-box | PRD IDs covered                                      | Agent 6 test deliverables                                  | Exit criteria                                                                                          |
| - | ------------------------------------- | -------- | ---------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 0 | Project scaffolding (THIS TURN)       | 1 h      | NFR-003, NFR-004, NFR-009                            | `test_smoke.py` (already green by virtue of stubs)         | All modules parse; `pytest -q test_smoke.py` green; `.env.example` mirrors `.env` keys.                |
| 1 | Loader + Output Writer round-trip     | 2 h      | FR-001..FR-006, FR-050..FR-055, AC-2, AC-3           | `test_loader.py`, `test_output_writer.py`                  | Sample CSV reads → DTO → writes back round-trip with correct casing. Determinism test green.           |
| 2 | Corpus Indexer + Retriever            | 3 h      | FR-020..FR-024, NFR-001                              | `test_indexer.py`, `test_retriever.py`                     | `code/index/` artifacts produced deterministically; top-K query returns expected file paths on fixture corpus. |
| 3 | Classifier + heuristic priors         | 2 h      | FR-010..FR-017, T-3, T-5, T-6 detection              | `test_classifier_heuristics.py`, `test_classifier_schema.py` | Heuristic regex hits known phrases; LLM tool-use schema validated; structured output parses.            |
| 4 | Reasoner + Grounding Verifier         | 3 h      | FR-030..FR-035, R-1                                  | `test_reasoner.py` (mock LLM), `test_verifier.py`          | Citation list non-empty for replied; verifier rejects fabricated phone numbers / URLs.                  |
| 5 | Escalation Policy decision table      | 2 h      | FR-040..FR-042, T-1..T-6, AC-5..AC-8                 | `test_escalation.py` (parametrized: 6 triggers × 2 fixtures) | First-match-wins ordering correct; chitchat allowance fires before T-1.                                |
| 6 | Wire-up `main.py` + integration test  | 2 h      | FR-060..FR-064, AC-1                                 | `test_pipeline_integration.py` against `sample_support_tickets.csv` | `python code/main.py --limit 5` produces a valid `output.csv` end-to-end.                              |
| 7 | Threshold tuning + full run           | 2 h      | NFR-001, NFR-002, AC-12, SM-3a..3e                   | `test_reproducibility.py`                                  | Sample CSV ≥ 9/10 on `status` + `request_type`; full `support_tickets.csv` run < 10 min; submission packaged. |

**Total: 17 hours of build.** Buffer = ~5 hours against the 22-hour wall clock from now (13:00 IST 2026-05-01) to deadline (11:00 IST 2026-05-02).

---

## 4. Per-Iteration Detail

### 4.1 Iter 0 — Project scaffolding (this turn)

**Goal.** Stand up the directory layout in Architecture §5, create stubs that parse, pin dependencies, lay down pytest scaffolding. **No business logic.**

**Files created (this turn).**

- `.env.example` — mirrors `.env` keys with placeholder values.
- `code/main.py` (replaces empty 0-byte file) — argparse CLI scaffold; calls into `agent.run()`.
- `code/agent.py` — Agent orchestrator stub.
- `code/loader.py` — `load_tickets(path) -> list[Ticket]` stub.
- `code/preprocessor.py` — `clean(ticket) -> CleanedTicket` stub.
- `code/indexer.py` — `build_index(corpus_root, out_dir)` stub + `__main__` entrypoint.
- `code/retriever.py` — `Retriever.search(query, domain, k)` stub.
- `code/classifier.py` — `classify(cleaned_ticket) -> ClassificationResult` stub.
- `code/reasoner.py` — `reason(cleaned_ticket, retrieved_docs) -> ReasoningResult` stub.
- `code/verifier.py` — `verify_grounding(response, retrieved_docs) -> bool` stub.
- `code/escalation.py` — `decide(classification, retrieval, reasoning) -> EscalationDecision` stub.
- `code/output_writer.py` — `write_output(rows, path)` stub.
- `code/schemas.py` — Pydantic DTOs from Architecture §4 (concrete; not stubs since they're data classes).
- `code/config.py` — `load_config()` stub for env vars + YAML.
- `code/tracer.py` — `Tracer` class stub.
- `code/prompts/system.md`, `code/prompts/classify.md`, `code/prompts/reason.md` — placeholder.
- `code/requirements.txt` — pinned per Architecture §8.
- `code/config.yaml` — defaults.
- `code/README.md` — install + run.
- `code/tests/__init__.py`, `code/tests/conftest.py`, `code/tests/test_smoke.py`.
- `code/pytest.ini` — testpaths, addopts.

**Failing tests.** Iter 0 has only the smoke test which is intentionally passing (it just imports each module to catch syntax errors). The first failing tests appear in Iter 1.

**Exit gate.**

- `python -c "import ast; ..."` parses every stub.
- `pytest code/tests/test_smoke.py -q` green.
- `.env.example` keys match `.env` keys (verified by Agent 1 on next session).

---

### 4.2 Iter 1 — Loader + Output Writer (round-trip CSV)

**Goal.** Read `support_tickets/sample_support_tickets.csv` into `Ticket` DTOs, write `OutputRow` DTOs back out with correct casing/encoding. Round-trip the **input columns unchanged** so AC-2 (row order, header) is satisfied even before we have intelligence.

**PRD/Architecture refs.** FR-001..FR-006, FR-050..FR-055, AC-2, AC-3. Architecture §3.3, §3.10.

**Failing tests Agent 6 writes first** (red phase):

- `code/tests/test_loader.py`
  - `test_load_tickets_normalizes_titlecase_headers` — input file has `Issue,Subject,Company`; loader emits `Ticket` with lowercase attrs.
  - `test_load_tickets_strips_company_trailing_whitespace` — `"None "` → `"None"`.
  - `test_load_tickets_blank_subject_ok` — empty subject string preserved.
  - `test_load_tickets_preserves_row_order` — index matches input order.
  - `test_load_tickets_unknown_company_marks_inference` — `requires_inference=True` when company outside enum.
  - `test_load_tickets_utf8_with_bom` — BOM handled.
- `code/tests/test_output_writer.py`
  - `test_write_output_header_lowercase_8_columns` — exact `issue,subject,company,status,product_area,response,justification,request_type`.
  - `test_write_output_status_titlecase` — `Replied` / `Escalated`.
  - `test_write_output_request_type_lowercase_snakecase`.
  - `test_write_output_product_area_lowercase_snakecase`.
  - `test_write_output_rfc4180_quoting_for_embedded_quotes`.
  - `test_write_output_lf_lineendings_on_windows` — bytes contain no `\r`.
  - `test_write_output_round_trip_byte_identical` — write twice, hashes match (NFR-001 spot test).
  - `test_write_output_invalid_enum_falls_back_to_escalated_invalid` — defense-in-depth.

**Implementation steps Agent 5 takes (green phase).**

1. `loader.py`: `csv.DictReader` with `utf-8-sig` to absorb BOM; lowercase `fieldnames` mapping; `Ticket` constructor; `requires_inference` set when `company` not in enum.
2. `output_writer.py`: `csv.writer(file, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)`; write header explicitly; per-row `_normalize_status`, `_normalize_request_type`, `_normalize_product_area` enum-coercion guards; strip `\r` from values.
3. `schemas.py` finalized for `Ticket` and `OutputRow`.

**Refactor opportunities.** Move enum lists to `code/config.yaml` once Iter 3 needs them too.

**Exit gate.** All loader + writer tests green. Determinism test green. AC-2 + AC-3 partially satisfied (header + casing). Round-trip pipeline degenerate-but-runnable.

---

### 4.3 Iter 2 — Corpus Indexer + Retriever

**Goal.** Offline build of hybrid (dense + BM25) retrieval index over `data/`. Deterministic top-K query against domain-scoped subset.

**PRD/Architecture refs.** FR-020..FR-024, NFR-001. Architecture §3.5, §3.6, §8.

**Failing tests.**

- `code/tests/test_indexer.py`
  - `test_build_index_creates_artifacts` — `chunks.parquet`, `faiss.index`, `bm25.pkl`, `manifest.json` exist.
  - `test_build_index_deterministic_chunk_ids` — same input → same chunk IDs.
  - `test_build_index_skips_empty_files`.
  - `test_build_index_manifest_sha256_per_file`.
  - `test_build_index_rebuild_on_corpus_change` — mutate one file → rebuild triggered.
- `code/tests/test_retriever.py`
  - `test_retriever_topk_returns_k_results` against tiny synthetic corpus fixture.
  - `test_retriever_domain_scope_filters` — `domain="visa"` excludes Claude/HackerRank chunks.
  - `test_retriever_below_threshold_returns_low_scoring` — for downstream T-1.
  - `test_retriever_deterministic_tie_break_by_chunk_id`.
  - `test_retriever_rrf_fusion_outranks_bm25_only_when_dense_agrees`.

**Implementation steps.**

1. `indexer.py`: walk sorted `Path("data").rglob("*.md")`; parse frontmatter; markdown header split + recursive char split; embed via `bge-small-en-v1.5`; build FAISS `IndexFlatIP` over normalized vectors; build `BM25Okapi`; persist + manifest.
2. `retriever.py`: load artifacts; embed query; FAISS top-30 + BM25 top-30 → RRF fusion → top-K; tie-break by `chunk_id`.
3. Guard in `main.py`: auto-rebuild if `manifest.json` SHA fingerprint mismatches `data/`.

**Refactor opportunities.** Pull the chunker into a sub-module if reasonable.

**Exit gate.** Indexer artifacts deterministic across two builds (compare hashes). Retriever passes all unit tests. Smoke run on real corpus completes < 5 min.

---

### 4.4 Iter 3 — Classifier (request_type, domain, product_area)

**Goal.** Single LLM call returns structured JSON via Anthropic tool-use; heuristic priors run first and provide hard signals for outage/chitchat/injection.

**PRD/Architecture refs.** FR-010..FR-017, T-3 (outage), T-5 (low confidence), T-6 (injection). Architecture §3.4, §3.7.

**Failing tests.**

- `code/tests/test_classifier_heuristics.py`
  - `test_outage_regex_hits_site_is_down`, `..._resume_builder_is_down`, `..._claude_stopped_working`, `..._pas_accessible`.
  - `test_chitchat_regex_thank_you`, `..._happy_to_help_pleasantry`.
  - `test_injection_regex_french_jailbreak`, `..._english_show_internal_rules`, `..._delete_all_files_codegen`.
  - `test_short_body_with_no_question_word_is_chitchat`.
- `code/tests/test_classifier_schema.py` (uses mock Anthropic client)
  - `test_classify_emits_valid_pydantic_classificationresult`.
  - `test_classify_retries_once_on_parse_failure_then_escalates`.
  - `test_classify_heuristic_outage_overrides_llm_when_more_conservative`.

**Implementation steps.**

1. `preprocessor.py`: regex sanitize + injection detection (sets `injection_detected`).
2. `classifier.py`: heuristic prior dict → tool-use call to `claude-sonnet-4-5` with mandatory tool schema → pydantic validation → retry-once → return `ClassificationResult`. Mock the Anthropic client in tests.
3. `code/prompts/classify.md` finalized.

**Exit gate.** Heuristic tests green; schema tests green using mock; on a 5-row sample CSV smoke run, all 5 produce valid `ClassificationResult`.

---

### 4.5 Iter 4 — Reasoner + Grounding Verifier

**Goal.** Generate grounded response with citations; verify post-hoc that numeric/URL/$/phone tokens appear in retrieved chunks.

**PRD/Architecture refs.** FR-030..FR-035, R-1. Architecture §3.8.

**Failing tests.**

- `code/tests/test_reasoner.py` (mock Anthropic)
  - `test_reasoner_returns_response_when_chunks_sufficient`.
  - `test_reasoner_can_answer_false_when_no_relevant_chunks`.
  - `test_reasoner_does_not_echo_system_prompt`.
  - `test_reasoner_emits_citations_subset_of_data_paths`.
  - `test_reasoner_retries_once_on_pydantic_failure`.
- `code/tests/test_verifier.py`
  - `test_verifier_passes_when_all_phone_numbers_in_corpus`.
  - `test_verifier_fails_when_response_invents_phone`.
  - `test_verifier_fails_when_response_invents_url`.
  - `test_verifier_fails_when_response_invents_dollar_amount`.
  - `test_verifier_ignores_generic_numbers_like_dates`.

**Implementation steps.**

1. `reasoner.py`: prompt assembly with delimited ticket + delimited chunks → tool-use → pydantic → retry-once.
2. `verifier.py`: regex-extract phones / URLs / $ amounts / explicit numerics; substring-check union of retrieved chunk text.
3. `code/prompts/reason.md` finalized.

**Exit gate.** Replied rows in 5-row smoke pass verifier; injected fake phone in test fixture is rejected.

---

### 4.6 Iter 5 — Escalation Policy decision table

**Goal.** Pure-Python deterministic decision function. No LLM. All thresholds from `config.yaml`.

**PRD/Architecture refs.** FR-040..FR-042, T-1..T-6, AC-5..AC-8. Architecture §3.9, §9.

**Failing tests** (parametrized — 6 triggers × at least 2 fixtures each, plus chitchat allowance + happy path):

- `code/tests/test_escalation.py`
  - `test_t6_injection_detected_escalates_invalid` (×2 fixtures).
  - `test_t3_outage_escalates_bug` (×2).
  - `test_t2_sensitive_keyword_escalates_keeps_classifier_request_type` (×2 — fraud, vulnerability).
  - `test_t2_authorization_violation_escalates` (×2 — refund-demand, score-override).
  - `test_t4_multi_request_below_threshold_escalates` (×2).
  - `test_t5_low_confidence_company_none_escalates` (×2).
  - `test_t1_weak_retrieval_escalates` (×2 — empty retrieval, low cosine).
  - `test_chitchat_replies_invalid_with_canned` (×2 — "thank you", trivia).
  - `test_happy_path_replied` (×1).
  - `test_first_match_wins_ordering_t6_before_t3_before_t1` — order matters.

**Implementation steps.**

1. `escalation.py`: implement decision table from Architecture §3.9 verbatim. All thresholds via config injection so M-7 can tune without edits.
2. Sensitive-keyword + authorization-violation regex lists in `config.yaml`.

**Exit gate.** All parametrized cases green. AC-5..AC-8 fully satisfied at unit level.

---

### 4.7 Iter 6 — Wire-up in `main.py` + integration test

**Goal.** End-to-end run on `support_tickets/sample_support_tickets.csv` produces a syntactically valid `output.csv`. Quality tuning happens in Iter 7; this iter just connects the pipes.

**PRD/Architecture refs.** FR-060..FR-064, AC-1. Architecture §3.1, §6.

**Failing tests.**

- `code/tests/test_pipeline_integration.py`
  - `test_main_run_on_5_row_fixture_produces_valid_output_csv` — fixture CSV with mocked LLM returning canned JSON; assert 5 rows out, header correct, casing correct.
  - `test_main_run_per_row_exception_marks_escalated` — inject exception in classifier on row 3; row 3 emerges Escalated/invalid with `pipeline error` justification; rows 1,2,4,5 unaffected.
  - `test_main_run_writes_partial_csv_on_main_crash` — kill mid-run; `output.partial.csv` exists.
  - `test_main_run_emits_progress_summary_to_stdout`.

**Implementation steps.**

1. `main.py`: argparse, dotenv, seed RNG, build/load index, iterate tickets with try/except per row, call agent.process_ticket, emit summary.
2. `agent.py`: `process_ticket(ticket) -> OutputRow` orchestrator that chains preproc → classifier → retriever (skipped on chitchat) → reasoner (skipped on chitchat or T-1) → escalation → output_row.
3. `tracer.py` writes JSONL line per ticket.

**Exit gate.** End-to-end run on 5-row fixture green (mocked LLM). README updated by Agent 7. AC-1 satisfied at integration level.

---

### 4.8 Iter 7 — Threshold tuning + full run + packaging

**Goal.** Tune `RETRIEVAL_MIN_SCORE`, `CLASSIFICATION_MIN_CONFIDENCE` against `sample_support_tickets.csv` until SM-3a + SM-3e ≥ 9/10. Run full `support_tickets.csv`. Package submission.

**PRD/Architecture refs.** NFR-001, NFR-002, AC-12, SM-3a..3e. Architecture §11, §13.3.

**Failing tests.**

- `code/tests/test_reproducibility.py` — full pipeline twice on 5-row fixture → byte-equal output. Skipped without ANTHROPIC_API_KEY.
- `code/tests/test_sample_csv_accuracy.py` — labeled-sample comparison; assert ≥ 9/10 status, ≥ 9/10 request_type.

**Implementation steps.**

1. Run full pipeline on `sample_support_tickets.csv`; diff against labels; log mismatches.
2. Adjust `config.yaml` thresholds; re-run; iterate up to 3 times.
3. Run full `support_tickets.csv` → final `output.csv`.
4. Manual spot-check of 10 random Replied rows for hallucinations (SM-3c).
5. Agent 7 updates `instructions.txt`; zip `code/` excluding `.venv/`, `__pycache__/`, `code/index/` per AGENTS.md §6 — final `data/index/` and `code/index/` are excluded by .gitignore but submission zip rule confirms.

**Exit gate.** All AC-1..AC-12 satisfied. Submission packaged. Final §5.2 log entry posted.

---

## 5. Test Strategy Cross-Reference

Mirrors Architecture §13. Agent 6 owns `docs/testexecution.md` (companion document) which itemizes each test file, its red-phase assertions, and the order in which Agent 6 writes them.

| Architecture §13 layer        | Test file(s)                                                    | Owner agent | Iteration |
| ----------------------------- | --------------------------------------------------------------- | ----------- | --------- |
| Loader                        | `test_loader.py`                                                | Agent 6     | 1         |
| Preprocessor                  | `test_preprocessor.py`                                          | Agent 6     | 3         |
| Classifier heuristics         | `test_classifier_heuristics.py`                                 | Agent 6     | 3         |
| Classifier schema (mock LLM)  | `test_classifier_schema.py`                                     | Agent 6     | 3         |
| Indexer                       | `test_indexer.py`                                               | Agent 6     | 2         |
| Retriever                     | `test_retriever.py`                                             | Agent 6     | 2         |
| Reasoner (mock LLM)           | `test_reasoner.py`                                              | Agent 6     | 4         |
| Verifier                      | `test_verifier.py`                                              | Agent 6     | 4         |
| Escalation (parametrized)     | `test_escalation.py`                                            | Agent 6     | 5         |
| Output writer                 | `test_output_writer.py`                                         | Agent 6     | 1         |
| Pipeline integration          | `test_pipeline_integration.py`                                  | Agent 6     | 6         |
| Reproducibility               | `test_reproducibility.py`                                       | Agent 6     | 7         |
| Sample CSV accuracy           | `test_sample_csv_accuracy.py`                                   | Agent 6     | 7         |
| Smoke (import-only)           | `test_smoke.py`                                                 | Agent 5     | 0         |

Agent 6's `testexecution.md` will own per-test assertion text; this plan only owns *which* tests exist and *which iter* they belong to.

---

## 6. Collaboration Protocol

- **Agent 1 (Verifier).** Re-runs verification when (a) PRD/Architecture/.env changes, (b) directory layout changes (e.g. if `support_issues/` ever appears, Agent 1 catches it). Agent 1 is consulted at start of every iter to confirm no drift.
- **Agent 2 (PRD)/Agent 3 (PRD author)/Agent 4 (Architect).** Re-spawned ONLY when Agent 5 or Agent 6 discovers a constraint that contradicts ProblemAnalysis/PRD/Architecture (e.g. corpus reveals a `product_area` value not in the enum, or sample CSV adds a column). Discoveries are reported up — Agent 5 does not silently amend the spec.
- **Agent 6 (Test Engineer).** Owns RED phase — writes failing tests *before* Agent 5 enters GREEN phase. Each iter has a clear handoff: Agent 6 finishes test commit → Agent 5 begins implementation. They share the same branch (`development`).
- **Agent 7 (Docs/Run-instructions).** Updates `instructions.txt` (root, for evaluator) and refreshes `code/README.md` at the end of every iter that changes the run command, env-var surface, or CLI flags. Agent 7 runs *after* Agent 5's GREEN phase, *before* the §5.2 log entry that closes the iter.
- **Logging.** Every agent appends their own §5.2 entry; sub-agents include `parent_agent=` and pass the log path through.
- **Sub-agent rule.** If Agent 5 spawns a Task sub-agent (e.g. for a focused refactor), the sub-agent inherits the same iteration ID, writes its own log entries, and returns control to Agent 5 before iter close.

---

## 7. Risk Register & Mitigation

Top 5 risks for the build phase (see PRD §12 for the master register).

| # | PRD ref | Risk                                             | Mitigation in this plan                                                                                                |
| - | ------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| 1 | R-1     | Hallucinated facts in `response`                | Iter 4 ships `verifier.py` as a hard gate. Iter 5 escalation table also fires T-1 on `grounding_failed`.               |
| 2 | R-5     | LLM non-determinism breaks AC-12                 | `temperature=0`, pinned `claude-sonnet-4-5`, seeded RNG, pinned deps. Iter 7 `test_reproducibility.py` enforces.        |
| 3 | R-2     | Over-escalation tanks SM-3a                      | Iter 5 chitchat allowance rule fires *before* T-1. Iter 7 threshold tuning loop on `sample_support_tickets.csv`.        |
| 4 | R-4     | CSV casing drift (sample-vs-spec divergence)    | Iter 1 explicit casing tests + writer-side enum coercion guard. OQ-1/OQ-2 already resolved in Architecture §16.         |
| 5 | R-9     | Multi-request rows answered partially            | T-4 trigger in Iter 5; classifier sets `is_multi_request` heuristic. Whole-ticket escalation, not partial reply.        |

---

## 8. Rollback / Recovery

Per-iteration rollback strategy (we do not commit-then-rollback in git here; we use **module-level isolation** + `--limit N` to keep the blast radius small).

- **If an iter's tests later break.** Each iter touches a distinct module set; revert that iter's module to its pre-iter HEAD via `git checkout <prev-commit> -- code/<file>` and re-run the suite.
- **If retriever returns garbage on real corpus.** Fall back to BM25-only mode (`config.yaml: retrieval.mode=bm25`). Architecture supports this naturally.
- **If LLM API quota exhausts.** Fall back to a smaller mocked-response mode that still emits valid (but degenerate) `output.csv` — every row escalated with `justification="trigger T-1: LLM unavailable"`. This protects AC-1, AC-2, AC-3 even at worst case.
- **If a green test set later breaks.** Re-run `pytest -q` per iter on a per-module basis; bisect by iter number; the iter roadmap above is the bisection map.
- **If clock pressure forces skipping an iter.** Iter priority for completion: 1 > 5 > 6 > 7 > 2 > 3 > 4. (Loader/writer + escalation + wire-up + run beats fancier reasoning.) Even with only Iter 1, 5, 6, 7 done we can ship a "always-escalate" submission that passes AC-1, AC-2, AC-3, AC-5.

---

## 9. Submission Checklist

Per AGENTS.md §6 + PRD §13.

- [ ] `support_tickets/output.csv` exists, 8 columns, lowercase header, 57 rows.
- [ ] Every row casing: `Replied`/`Escalated`, lowercase `request_type`, lowercase snake_case `product_area`.
- [ ] `code/` zipped excluding `.venv/`, `__pycache__/`, `code/index/`, `code/runs/`, `data/index/`, `data/embeddings/`, `*.pyc`.
- [ ] `instructions.txt` at repo root (Agent 7) with `python code/main.py` command + env var setup.
- [ ] `code/README.md` install + run.
- [ ] `~/hackerrank_orchestrate/log.txt` captured + `AGREEMENT RECORDED:` line present.
- [ ] No API keys in any committed file (`grep -r 'sk-ant-' code/` returns nothing).
- [ ] Two consecutive runs of `python code/main.py --input support_tickets/sample_support_tickets.csv --limit 5` produce identical output bytes.
- [ ] HackerRank Community Platform submission link followed; final ZIP uploaded.

---

## 10. Time Budget vs Deadline

Anchor: now ≈ **2026-05-01 13:00 IST**. Deadline: **2026-05-02 11:00 IST** (= 22 h).

| Iter | Cumulative wall-clock from now | Local time at iter end (IST) | Remaining buffer |
| ---- | ------------------------------ | ----------------------------- | ----------------- |
| 0    | +1 h                           | 14:00 (May 1)                 | 21 h              |
| 1    | +3 h                           | 16:00 (May 1)                 | 19 h              |
| 2    | +6 h                           | 19:00 (May 1)                 | 16 h              |
| 3    | +8 h                           | 21:00 (May 1)                 | 14 h              |
| 4    | +11 h                          | 00:00 (May 2)                 | 11 h              |
| 5    | +13 h                          | 02:00 (May 2)                 | 9 h               |
| 6    | +15 h                          | 04:00 (May 2)                 | 7 h               |
| 7    | +17 h                          | 06:00 (May 2)                 | 5 h               |

Buffer of ~5 hours absorbs one bad iter or one full-run tuning cycle. If at any point fewer than 2 hours remain, AGENTS.md §4.3 mandates suspending feature work and packaging immediately (Iter 7's degenerate fallback in §8 above).

---

*This plan is the buildable contract. Agent 6 next writes `docs/testexecution.md` enumerating the failing tests for Iter 1; Agent 5 then opens Iter 1 GREEN phase. Agent 1 verifies no drift before Iter 1 starts.*
