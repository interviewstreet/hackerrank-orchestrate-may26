---
title: "Candidate Status in API Results Status ATS state"
title_slug: "candidate-status-in-api-results-status-ats-state"
source_url: "https://support.hackerrank.com/articles/3094540490-candidate-status-in-api-results"
article_slug: "3094540490-candidate-status-in-api-results"
last_updated_exact: "Feb 23, 2026, 12:46 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Settings"
  - "Open API"
---

# Candidate Status in API Results Status ATS state

_Last updated: Feb 23, 2026, 12:46 PM (Last updated 2 months ago)_

When you retrieve candidate data using the HackerRank API, the JSON response includes two integer fields:

- `status`

- `ats_state`

# Status

The `status` field represents the state of the candidate’s test attempt.

## Stable values

The table below lists the stable values and their descriptions.

|           |                                                 |
|-----------|-------------------------------------------------|
| **Value** | **Description**                                 |
| `-1`      | Candidate invited                               |
| `0`       | Candidate session in progress                   |
| `1`       | Candidate completed the test; reports not ready |
| `7`       | Reports ready for consumption                   |

**Note:** You can build downstream logic only on the stable values.

## Transient values

The API may return values such as `2–6` or other negative numbers.

These values represent intermediate processing stages, such as:

- Evaluation

- Integrity checks

- Report generation

Transient values are not part of the API contract and may change without notice. Do not build downstream logic that depends on them.

# ATS state

The `ats_state` field represents the candidate’s stage in the recruitment workflow.

After a candidate completes a test:

- The system updates the state automatically if you configure a cut-off score.

- A recruiter can manually update the state to move the candidate forward in the hiring process.

## ATS state values

The table below lists the `ats_state` values and their corresponding recruitment stages:

|           |                                      |
|-----------|--------------------------------------|
| **Value** | **ATS State**                        |
| `0`       | ATS state not set                    |
| `1`       | Test Completed – Evaluation Required |
| `2`       | Test Completed – Qualified           |
| `3`       | Test Completed – Failed              |
| `4`       | Phone Interview – I                  |
| `5`       | Phone Interview – II                 |
| `6`       | Phone Interview – III                |
| `7`       | Offer Sent                           |
| `8`       | Offer Negotiation                    |
| `9`       | Offer Accepted                       |
| `10`      | Offer Declined                       |
| `11`      | On Hold                              |
| `12`      | Phone Interview – Cleared            |
| `13`      | Phone Interview – Failed             |
| `14`      | Technical Interview – Cleared        |
| `15`      | Technical Interview – Failed         |
| `16`      | HR Interview – Cleared               |
| `17`      | HR Interview – Failed                |
| `18`      | Phone Interview                      |
| `19`      | Technical Interview                  |
| `20`      | HR Interview                         |
| `21`      | Hired                                |
| `22`      | Rejected                             |

\
