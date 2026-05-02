# Benchmarks

## Overview

These benchmarks define quantitative performance targets for the triage pipeline. They are evaluated against the 30-ticket `support_tickets/support_tickets.csv` dataset using the labeled `sample_support_tickets.csv` as a reference distribution.

---

## 1. Classification Accuracy

Measured by comparing pipeline output against ground-truth labels.

| Metric                     | Target | Notes                                                                             |
| -------------------------- | ------ | --------------------------------------------------------------------------------- |
| `status` accuracy          | ≥ 90%  | Correct `replied` / `escalated` decision across all 30 tickets                    |
| `request_type` accuracy    | ≥ 85%  | Correct classification among `product_issue`, `feature_request`, `bug`, `invalid` |
| `product_area` match       | ≥ 80%  | Semantic match or exact match against expected category                           |
| Company inference accuracy | ≥ 80%  | For `company=None` tickets, correct domain inferred from content                  |

Accuracy is measured as: `(correct rows) / (total rows)` × 100. Multi-request tickets contribute one accuracy point per sub-request row.

---

## 2. Hallucination Rate (Hard Constraints)

These are pass/fail — any failure disqualifies the submission.

| Metric                            | Target         | Measurement                                           |
| --------------------------------- | -------------- | ----------------------------------------------------- |
| Fabricated policy statements      | 0 / 30 tickets | Manual review: claim not found in any corpus file     |
| Fabricated procedural steps       | 0 / 30 tickets | Manual review: step not present in any corpus file    |
| Ungrounded responses (no source)  | 0 / 30 tickets | Escalated instead of replied when corpus has no match |
| Parametric knowledge in responses | 0 / 30 tickets | All claims attributable to `data/` corpus files       |

---

## 3. Escalation Precision and Recall

Escalation decisions are the highest-stakes part of the pipeline. Both false positives (unnecessary escalations) and false negatives (missed escalations on dangerous tickets) matter.

| Metric                                              | Target | Notes                                                                      |
| --------------------------------------------------- | ------ | -------------------------------------------------------------------------- |
| Escalation recall (dangerous tickets caught)        | 100%   | Zero fraud / account-compromise / data-loss tickets that receive `replied` |
| Escalation precision (no unnecessary escalations)   | ≥ 80%  | Clear FAQ tickets should receive `replied`, not escalation                 |
| Invalid ticket handled as `replied` (not escalated) | 100%   | All `request_type=invalid` tickets produce `status=replied`                |

---

## 4. Retrieval Quality

Measured on the `replied` tickets where Anchor is invoked.

| Metric                           | Target | Notes                                                            |
| -------------------------------- | ------ | ---------------------------------------------------------------- |
| Corpus hit rate (cos_sim ≥ 0.65) | ≥ 85%  | Proportion of replied tickets where top chunk clears threshold   |
| Cross-domain contamination       | 0%     | No response cites a document from the wrong company corpus       |
| Source attribution present       | 100%   | Every `justification` on a `replied` ticket cites a `data/` file |

---

## 5. Processing Performance

| Metric                     | Target       | Measurement                                                  |
| -------------------------- | ------------ | ------------------------------------------------------------ |
| Total runtime (30 tickets) | < 5 minutes  | Wall clock time from invocation to `output.csv` written      |
| Per-ticket average time    | < 10 seconds | Including retrieval, Sentinel, and (conditional) Anchor call |
| Peak memory usage          | < 4 GB RAM   | Measured with `psutil` or system monitor                     |
| Output file write time     | < 1 second   | After last ticket processed                                  |

---

## 6. Reliability

| Metric               | Target                   | Notes                                                                          |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------ |
| Run completion rate  | 100%                     | All 30 tickets produce an output row; no silently skipped rows                 |
| Unhandled exceptions | 0 per run                | All failures caught and converted to escalated rows                            |
| Semantic stability   | 100% routing consistency | Same `status` and `request_type` across two consecutive runs on the same input |

---

## 7. Benchmark Evaluation Method

### Automated checks (fast)

Run after every execution:

1. CSV column presence and enum validation (`status`, `request_type` values)
2. Row count matches expected (input rows + multi-request expansion)
3. Source attribution presence check in `justification` fields
4. Credential/PII pattern scan in `response` and `justification`

### Manual review (pre-submission)

Spot-check a minimum of 5 `replied` tickets:

1. Read each `response` against the cited `source_doc`
2. Verify every factual claim has a corresponding sentence in the corpus file
3. Confirm no PII from the ticket appears in `response` or `justification`

### Reference comparison

Compare `output.csv` against `sample_support_tickets.csv` labels on overlapping tickets to estimate ground-truth accuracy before submission.
