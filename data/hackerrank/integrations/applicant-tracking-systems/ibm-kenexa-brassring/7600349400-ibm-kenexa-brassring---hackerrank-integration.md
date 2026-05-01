---
title: "IBM Kenexa BrassRing - HackerRank Integration"
title_slug: "ibm-kenexa-brassring-hackerrank-integration"
source_url: "https://support.hackerrank.com/articles/7600349400-ibm-kenexa-brassring---hackerrank-integration"
article_slug: "7600349400-ibm-kenexa-brassring---hackerrank-integration"
last_updated_exact: "Dec 28, 2024, 12:21 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "IBM Kenexa Brassring"
---

# IBM Kenexa BrassRing - HackerRank Integration

_Last updated: Dec 28, 2024, 12:21 AM (Last updated 1 year ago)_

## Overview

HackerRank integrates with IBM Kenexa BrassRing through a standardized **Candidate Export** and **Form Import** XML API. If you have experience with these APIs and are a BrassRing Workbench administrator, you should be able to configure the integration yourself. If you are not familiar with these APIs, it is recommended that you work with IBM Kenexa professional services who can make the changes on your behalf. 

## Key Features for Tests Integration

- Send Test invitations to HackerRank assessments from within BrassRing 

  - Optionally specify Time Accommodation% to extend assessment for certain candidates

- Receive Test Results in a BrassRing form when a candidate completes an assessment.

- Support for Candidates on Multiple Requisitions.

  - If a Candidate applies to multiple requisitions, they only need to take the HackerRank assessment once, the results will be sent to all requisitions that requested the test.

  - If a candidate has taken the test in the past, the historical result will be sent back to BrassRing.

- Preserve HackerRank role-based access and permissions when taking actions in BrassRing

## Key Features for Interviews Integration

- Create Interview link and scheduling link  

- Receive results and report link in BrassRing form when Interview has finished

Please refer to the following articles to set up and use the BrassRing- HackerRank Integration:\
\

- [📄 IBM Kenexa BrassRing - HackerRank Tests Integration](/articles/7795424803)
  \
- [📄 IBM Kenexa BrassRing - Interviews Integration](/articles/7390910463)
  \

Below is a list of features that the Brassring Integration offers:

## **Tests **

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 537.641px"><p><strong>Feature</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 293.359px"><p><strong>Brassring</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Full list of HRW Tests</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><p>Must be added manually </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Invite candidates to a specific test</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Cancel / Reinvite an invite</p></td>
<td data-colspan="1" data-rowspan="1"><p><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span><br />
<br />
Reinvite only. No cancel</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Status update from invite to completion</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Total Candidate Score</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Maximum Score</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Link to the detailed test report</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Question-wise scores</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Candidate Feedback</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Reviewer Comments</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>View Code</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Play Code</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Templates</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><p>Owner default</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Invite sent from</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Reinvite</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Public URL sync</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 537.641px"><p>Update results after editing HR</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 293.359px"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
</tbody>
</table>

## Interviews

**Interviews**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 541.641px"><p><strong>Feature</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 289.359px"><p><strong>Brassring</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 541.641px"><p>Create Interview QuickPad</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 289.359px"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 541.641px"><p>Schedule HackerRank Interview</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 289.359px"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 541.641px"><p>View Result</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 541.641px"><p>View Interviewer Notes</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 541.641px"><p>Link to the detailed report</p></td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
</tr>
</tbody>
</table>

\
