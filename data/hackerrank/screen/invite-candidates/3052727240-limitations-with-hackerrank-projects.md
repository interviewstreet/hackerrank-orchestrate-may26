---
title: "Limitations With HackerRank Projects"
title_slug: "limitations-with-hackerrank-projects"
source_url: "https://support.hackerrank.com/articles/3052727240-limitations-with-hackerrank-projects"
article_slug: "3052727240-limitations-with-hackerrank-projects"
last_updated_exact: "Oct 22, 2025, 9:18 PM"
last_updated_relative: "Last updated 6 months ago"
breadcrumbs:
  - "Screen"
  - "Invite Candidates"
---

# Limitations With HackerRank Projects

_Last updated: Oct 22, 2025, 9:18 PM (Last updated 6 months ago)_

The project questions on HackerRank use VM-based containers, with specific limitations on the number of workspaces a company can have at any given time. 

**Limitations by Question Type:**

- **Logins per Minute:**  The maximum number of candidates who can log into a test from a company in any given minute.

- **Workspace:** A container assigned to a project question. Each project question uses one independent workspace.

- **Concurrent Workspaces:**  The total number of containers a company can utilize simultaneously.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 22px; width: 35.0494%"><p><strong>Question Type</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 22px; width: 34.2263%"><p><strong>Logins Per Minute </strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 22px; width: 143.963%"><p><strong>Concurrent Workspaces </strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 35.0494%; height: 22px"><p>Front-end</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 34.2263%; height: 22px"><p>500</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 143.963%; height: 22px"><p>10000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 35.0494%; height: 22px"><p>Back-end</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 34.2263%; height: 22px"><p>500</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 143.963%; height: 22px"><p>10000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 35.0494%; height: 22px"><p>Full-stack</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 34.2263%; height: 22px"><p>500</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 143.963%; height: 22px"><p>10000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 35.0494%; height: 22px"><p>Data Science </p></td>
<td data-colspan="1" data-rowspan="1" style="width: 34.2263%; height: 22px"><p>500</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 143.963%; height: 22px"><p>10000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 35.0494%; height: 22px"><p>DevOps </p></td>
<td data-colspan="1" data-rowspan="1" style="width: 34.2263%; height: 22px"><p>500</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 143.963%; height: 22px"><p>10000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><p>MCQ</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p>20000</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><p>Coding</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p>20000</p></td>
</tr>
</tbody>
</table>

**Example**

If a test includes two project questions:

- **Maximum Logins**: 50 candidate logins per minute.

- **Simultaneous Test takers**: Up to 500 candidates. 

- **Concurrent Workspaces**: 1000 concurrent workspaces (each candidate will utilize two workspaces (one for each project question)

## Candidate Experience 

Generally, candidates can log in without any issues. However, if the limits are exceeded, they will experience the following when:

**1. Logins per Minute are at Capacity:** When login capacity is reached, candidates will see a message indicating their login is temporarily throttled. A countdown will replace the "**Try Again**" button, and candidates will be provisioned on servers once it finishes.

![Confirmation Form.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046700429-?Expires=253370764800&Signature=gAI0fmDcO5PJrv0f5Fhv78bbOwRMy9YKgIFWSQCnsNZNHE0~~EfbsMf2p3h0AJqBemuKg9JN88W9WDSgoiJRhrQeGzXJbHRE~p~peIJa4Kz-rhV1OJd5G5n9gNkbZr4JjrejHOK-gvFtS92GHm71j37Yj14ju5ExZz7B44~Bg10o1kWl~jB1H~J7L-ZmaGHdDROTOw1-1CzYml~~CsHNP39xyo6aHhUT4eSFbdbeLRNqREx-1fo6eQEAsBqT8eTn5N2XLfrJjaXSZVpzDrlzs8EH1hGQ~pAYi~1A1vNGDvBZRr~WieHHbrBhPlaKcAqFQCym8vkmwEg-Iwxl97B7nw__&Key-Pair-Id=K3NV4LZ47N8M46)

**2. Concurrent Workspaces are at Capacity:** If the concurrent workspace limit is exceeded, the remaining candidates will see an error message: "Our servers are at capacity. Please try to take this test after some time." As candidates complete their attempts, new candidates will be allowed to log in.

![Servers at capacity.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046700808-?Expires=253370764800&Signature=Gxi18p7-iXxnJWK~06OCeL6hamhgxRilpfENgVrjjjlP-q3YECFphF6fSm5zhuA16N2d3-ilesyJnNpA-xI5kzlmdOG9wi~gzoXY66sAAQjqyDJMkCgswe~cyYY0NS3K00r2KDbsVj6yiyDProKp1ZJD-E7L8LLT~6W4fM2~bDNrUyniTftodOCC3gZZG9D1MCazLB57IJ6zync6IBq8TG0X1VZ3QTgurvC7EkTzEpwRgfwik6SQGnJg3usd~Kr4My9lhkO~5lqifZ8K4FCTroJ1m-MAqh-spu-8I1J2IrQvdAhRAtRoXTBvzH8XYlCQvQGcF9vJoN0m~t5EXC3rAQ__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:**

- Reach out to [support@hackerrank.com](mailto:support@hackerrank.com) if your requirement exceeds the default threshold. Given the limitations, inviting candidates in batches to stagger logins is recommended. Also, the limits remain the same irrespective of the test duration, as the table above mentions.

- For both Project questions and non-project questions, if the requirement is more than 5,000 simultaneous attempts, reach out to [support@hackerrank.com](mailto:support@hackerrank.com).

#### **Related Articles:**

- [Creating a HackerRank Project Question](https://kb.hackerrank.com/articles/1570281449-creating-front-end%2C-back-end-full-stack-and-mobile-questions)

- [Front-end, Back-end, and Full Stack Developer](https://kb.hackerrank.com/articles/1570281449-creating-front-end%2C-back-end-full-stack-and-mobile-questions)

- [Data Science](https://kb.hackerrank.com/articles/5187107609-data-science-questions)

- [Database Engineer](https://kb.hackerrank.com/articles/8826242281-database-engineer-questions)

- [Code Review](https://kb.hackerrank.com/articles/4262355406-code-review-questions)

- [Mobile Development](https://kb.hackerrank.com/articles/1570281449-creating-front-end%2C-back-end-full-stack-and-mobile-questions)

- [Scoring Front end, Back end, and Full-stack Questions](https://kb.hackerrank.com/articles/4110011178-scoring-front-end%2C-back-end-and-full-stack-questions)

- [Manual Scoring of Data Science Questions](https://kb.hackerrank.com/articles/1079079701-manual-scoring-of-data-science-questions-)

- [Auto Scoring of Data Science Questions](https://kb.hackerrank.com/articles/8932030959-automatic-scoring-of-data-science-questions)

- [Taking Front-end, Back-end, Full-Stack Developer assessments](https://candidatesupport.hackerrank.com/hc/en-us/articles/4402921107091-Taking-Front-end-Back-end-Full-stack-developer-assessments)

- [Blog](https://www.hackerrank.com/blog/hackerrank-projects-supports-data-science-skills/)

\
