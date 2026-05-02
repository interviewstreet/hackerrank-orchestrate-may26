# Data Privacy — Support Ticket Triage

## Overview

This document defines how the support triage system classifies, processes, and protects data that flows through it. It applies to all inputs (support tickets), all outputs (triage decisions and responses), and any intermediate state the system produces while processing a ticket. It governs what the system may do with triage data, not how the system is deployed or configured by operators.

---

## 1. Data Classification

### 1.1 Triage data types and sensitivity levels

| Data Type                          | Classification   | Examples                                                         | Sensitivity                                                          |
| ---------------------------------- | ---------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| Ticket subject line                | **Sensitive**    | Brief description of customer's issue                            | Medium — may reveal nature of problem without full context           |
| Ticket body / issue content        | **Sensitive**    | Free-text description of the customer's problem                  | High — likely contains PII, account details, or financial references |
| Customer PII embedded in tickets   | **PII**          | Names, email addresses, account IDs found in ticket text         | Highest — must not be echoed in any output field                     |
| Financial data embedded in tickets | **Confidential** | Card numbers, transaction IDs, billing amounts                   | Highest — must trigger escalation; never reproduced in output        |
| Security credentials in tickets    | **Confidential** | Passwords, PINs, authentication tokens mentioned by customer     | Highest — must trigger escalation immediately                        |
| Triage output fields               | **Sensitive**    | `status`, `request_type`, `response`, `justification`            | Medium — derived from ticket content; must not re-expose PII         |
| Support corpus / knowledge base    | **Internal**     | Documentation, FAQ articles, policy documents used for retrieval | Low — no customer data; no special handling required                 |

### 1.2 System access boundaries per data type

| Data                    | System may access          | System may log          | System may include in output     |
| ----------------------- | -------------------------- | ----------------------- | -------------------------------- |
| Ticket subject          | Yes                        | Summary only            | No                               |
| Ticket body             | Yes — for triage only      | No — not raw text       | No                               |
| Customer name in ticket | Yes — routing context only | No                      | No — never echo back             |
| Email address in ticket | Yes — routing context only | No                      | No                               |
| Card / account numbers  | Routing decision only      | Never                   | Never — must escalate            |
| Security credentials    | Recognition only           | Never                   | Never — must escalate            |
| Corpus documents        | Yes                        | Source reference only   | Yes — ground responses in corpus |
| Triage output           | Yes                        | Record of decision only | Yes — this is the deliverable    |

---

## 2. Data Processing Principles

### 2.1 What data is processed and for what purpose

| Data                         | Processing Purpose              | Permitted Use                                                                    |
| ---------------------------- | ------------------------------- | -------------------------------------------------------------------------------- |
| Ticket content               | Determine correct triage action | Routing and response generation only                                             |
| Customer PII found in ticket | Contextual signal for routing   | Not used for lookup, verification, or any action                                 |
| Corpus content               | Grounding responses             | Responses must be sourced from corpus; not from model parametric knowledge alone |
| Triage output                | Evaluation deliverable          | Written to output record; not used to influence subsequent tickets               |

### 2.2 Data minimization

1. **No raw ticket text in logs.** Log entries must record decisions and summaries, not reproduce the customer's words.
2. **No PII in justifications.** The `justification` field must describe the triage reasoning generically (e.g., "customer reported billing discrepancy") without including names, account numbers, or other identifying values.
3. **No PII in responses.** The `response` field must not echo back any PII present in the ticket. Address the customer generically; do not address them by name, repeat their email, or confirm account identifiers.
4. **Corpus only.** The system must not retrieve or generate information from outside the designated knowledge base. Ticket content must not be sent to analytics, telemetry, or external search services.
5. **Minimal context per call.** When a language model is invoked, only the minimum ticket content necessary to produce a triage decision should be included. Unrelated tickets must not be included in the same context.
6. **No cross-ticket memory.** The system must process each ticket in isolation. Information from one ticket must not influence the processing of another.

### 2.3 Data the system must not collect

The system must not collect, store, or transmit:

- Any data that is not present in the input ticket or the support corpus
- Personally identifying information beyond what is strictly required to classify a ticket
- Inferences about a customer's identity, behaviour, or attributes beyond what is stated in the ticket

---

## 3. Data Storage

### 3.1 Storage rules for triage data

| Data                      | Permitted Storage                   | What must not be stored                                                |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------------------- |
| Input tickets             | Read at processing time             | Must not be cached with PII in a secondary store                       |
| Triage output record      | Written to output file              | Must not include PII echoed from input                                 |
| Vector index / embeddings | Embeddings derived from corpus only | Must not embed raw ticket text or ticket-derived PII                   |
| Intermediate reasoning    | Not persisted                       | LLM chain-of-thought containing ticket PII must not be written to disk |

### 3.2 Encryption and access

Data at rest must be protected by filesystem-level access controls appropriate to the deployment environment. Data in transit between the system and any external API must use TLS 1.2 or higher. Certificate verification must never be disabled.

### 3.3 What must never be stored

- Raw ticket PII in any log, cache, index, or database record
- Intermediate LLM responses that contain PII extracted from tickets
- Card numbers, account numbers, or transaction IDs in any persistent store

---

## 4. Data Access

### 4.1 Access controls

| Resource        | Who may access                          | Basis                                     |
| --------------- | --------------------------------------- | ----------------------------------------- |
| Input tickets   | Triage system process                   | Required for triage task                  |
| Support corpus  | Triage system process                   | Required for grounded response generation |
| Triage output   | Triage system process, system operators | Evaluation and review                     |
| Processing logs | System operators                        | Audit and debugging                       |

### 4.2 Agent access limitations

The triage agent is explicitly prohibited from:

1. Making network requests to any URL not part of the configured language model or retrieval API
2. Reading files outside the designated corpus and input directories
3. Writing files to any path other than the designated output location and processing log
4. Executing shell commands not initiated by the triage pipeline itself
5. Using PII found in a ticket to perform external lookups, account actions, or identity verification

### 4.3 Audit trail

The system must maintain a processing log sufficient to reconstruct which tickets were processed, what triage decision was made for each, and whether any anomalies (escalations, schema violations, retrieval failures) were encountered. The log must not contain raw ticket content or PII.

---

## 5. Data Retention

### 5.1 Retention principles

| Data                              | Retention Guidance                                                                        |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| Input tickets                     | Retain only as long as triage is ongoing; delete when no longer needed for evaluation     |
| Triage output                     | Retain for the evaluation period; remove or archive thereafter                            |
| Processing logs                   | Retain for debugging and audit purposes; purge when no longer operationally required      |
| Vector index                      | Retain only if built from corpus documents; rebuild rather than persist if ticket-derived |
| LLM API call logs (provider-side) | Governed by provider's retention policy; not under system control                         |

### 5.2 No PII in persistent indexes

If the system builds a persistent vector index, it must index only corpus documents, not ticket content. Ticket-derived embeddings must not be written to any persistent store.

---

## 6. Data Sharing

### 6.1 Permitted sharing

| Recipient                 | Data shared                                 | Purpose               |
| ------------------------- | ------------------------------------------- | --------------------- |
| Language model API        | Ticket text fragments as part of prompts    | Response generation   |
| Retrieval / embedding API | Ticket text fragments for similarity search | Corpus retrieval      |
| System operators          | Triage output record, processing log        | Evaluation and review |

### 6.2 Restrictions

- Ticket content must not be published publicly or shared outside the intended triage workflow
- Ticket content must not be sent to analytics services, telemetry endpoints, or logging aggregators beyond the system's own processing log
- Corpus content must not be redistributed in bulk outside the triage system

---

## 7. Privacy Principles

### 7.1 Principles applied

| Principle                     | Requirement                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------------------------------ |
| Data minimization             | Process only the data required to triage the ticket                                                    |
| Purpose limitation            | Ticket data is used only to produce a triage decision; not for model training, analytics, or profiling |
| Storage limitation            | No persistent storage of PII beyond the input record                                                   |
| Accuracy                      | Responses must be grounded in the corpus; the system must not fabricate information                    |
| Integrity and confidentiality | Ticket content and outputs protected by access controls; PII not echoed in outputs                     |

### 7.2 PII handling in output fields

The `response` field must not echo PII from the input ticket:

- If the ticket contains a customer name, the response must not address the customer by name
- If the ticket contains an email address, the response must not repeat that address
- If the ticket contains a card number, account number, or transaction ID, those values must never appear in any output field
- The `justification` field must describe the reasoning without identifying the customer (use "the customer" generically)

### 7.3 Escalation as a privacy control

The escalation pathway (`status=escalated`) functions as a privacy and safety mechanism:

- Tickets containing financial PII requiring action (card numbers, bank accounts) must be escalated, not processed
- Tickets containing security credentials (passwords, tokens) must be escalated immediately
- Tickets that appear to be prompt injection attempts must be classified as `request_type=invalid` and receive `status=replied` with an out-of-scope message — the same handling as any other `invalid` ticket; they are **not** escalated, as prompt injections do not represent high-risk customer situations requiring human review
- The system must never use PII found in a ticket to perform lookups, trigger external actions, or infer account state

---

## 8. Security Measures for Triage Data

### 8.1 Input validation

| Threat                              | Mitigation                                                                                                                                     |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Prompt injection via ticket content | Treat ticket text as untrusted input; enforce system/user message separation in LLM calls; classify injected content as `request_type=invalid` |
| Malicious file paths in ticket text | Never interpret ticket content as filesystem paths or shell commands                                                                           |
| Excessively large ticket input      | Truncate ticket content before passing to the model; log that truncation occurred                                                              |
| Malformed input records             | Use a structured parser (not string manipulation) to read input; validate field types before processing                                        |

### 8.2 Output validation

Before writing any triage record to the output, validate:

- `status` is one of the allowed values only
- `request_type` is one of the allowed values only
- `response` does not contain any string that matches a known credential pattern (e.g., API key formats, 16-digit card numbers)
- `response` is non-empty and within a reasonable length bound
- No PII from the input ticket appears verbatim in `response` or `justification`

If any validation fails, replace the record with a safe escalation response and log the validation failure.

### 8.3 Prompt architecture requirements

LLM prompts must enforce:

1. **System/user separation.** Agent instructions are in the system role; ticket content is passed in the user/content role. Ticket content must never be concatenated directly into the system prompt.
2. **Explicit untrusted-input labeling.** The system prompt must instruct the model that ticket content is untrusted user input and must not override triage instructions.
3. **Schema enforcement.** Outputs must conform to the expected structured schema; unstructured or schema-violating responses must be rejected and treated as escalations.

### 8.4 Anomaly handling

The system must automatically escalate (not reply) when:

- LLM output does not conform to the expected schema after the configured number of retries
- Retrieved corpus chunks fall below the minimum similarity threshold for confident grounding
- Ticket content is classified as adversarial or injection-bearing
- The candidate response contains a pattern matching a credential or financial identifier
