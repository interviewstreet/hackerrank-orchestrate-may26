---
title: "Test Cases in Coding and Approximate Solution Questions"
title_slug: "test-cases-in-coding-and-approximate-solution-questions"
source_url: "https://support.hackerrank.com/articles/3245197419-test-cases-in-coding-questions"
article_slug: "3245197419-test-cases-in-coding-questions"
last_updated_exact: "Sep 18, 2025, 5:43 PM"
last_updated_relative: "Last updated 7 months ago"
breadcrumbs:
  - "Library"
  - "Additional Resources"
  - "Programming Questions"
---

# Test Cases in Coding and Approximate Solution Questions

_Last updated: Sep 18, 2025, 5:43 PM (Last updated 7 months ago)_

Test cases are crucial to assessing a candidate's code. They consist of specific inputs and expected outputs that verify the code’s correctness and functionality. By covering various scenarios, including edge cases and typical use cases, test cases help ensure the code behaves as intended.

When a candidate compiles their code, each test case checks the code's execution status and results. The score is based on how many test cases the code passes successfully.

## Types of Test Cases in Coding Questions

### Sample Test Cases

Sample test cases are visible to candidates. They display the input and expected output values, allowing candidates to validate and debug their code. Marking test cases as sample test cases during creation enables candidates to view execution results and download them if needed.

![2024-11-22_15-59-03.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734993690916-35754831206675-a805cd47-f511-4bc3-ae62-1ecb560c5546?Expires=253370764800&Signature=DbyhawDkQPMhSsYyJe6S2GART7bSen96BDuawviapKnnOR29r217JbMh8fXp9K5V5UtOwwoq1gvf18i77640vLD0ANFQlIyDzkaPAQAd9R-QvZcUWDknntljneVHab0E~RzwH4b1d2XGBQ7akuwGARbXIaqcbZilLv9anlDub3~FMgcIM7D3bhNFQ2~KhzoIRNgPolrkuqLnV0ebp5bUhybw~tX3-~yg9MZja42qyqFytXx2mw3sLDck9TpOgEITdqpwhe6fbyLgQ7KB9EUWlMsNqxgFLrYXqZ7NaekD-lE-DS1ZnbgpqfJgri7qOwonH9AyHBVWM192Kv~lhHd~KA__&Key-Pair-Id=K3NV4LZ47N8M46)

**Example Use Case:** For a problem requiring the identification of the first non-repeated character in a string:

- The sample test case helps candidates understand the expected solution approach.

- Candidates see the input, expected output, and their code’s execution results.

#### **Importance of Sample Test Cases**

Sample test cases enhance the clarity of problem statements by illustrating specific examples. Providing 2–3 sample test cases helps candidates grasp the problem requirements effectively. We recommend including 8–15 test cases per coding question to ensure a comprehensive evaluation. These test cases should:

- Cover varied scenarios and complexities.

- Avoid redundancy by testing distinct concepts.

### Hidden Test Cases

Hidden test cases evaluate candidates on diverse edge cases without revealing input or expected output. Not marking test cases as a sample test case will hide the test cases from the candidates and will be indicated by a lock icon. These cases:

- Challenge candidates to write robust code capable of handling edge scenarios.

- Display only the candidate's output and debug messages during execution.

![2024-11-22_15-58-35.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734993701188-35754799473555-8d1bb706-e480-45dd-a575-20cc8544d697?Expires=253370764800&Signature=FVpDDpr8vvYYFRy3kj0bLSIAHbU-Im7L~ELckxDWfL2eB8IgReOKzlIZWsEmW7hEJT5bX7NYoD9LRNeUjznFa~fS-xXEtoOHWbpY2re7cYm6QY1bWsjPvYscW89RQ-q703~YcDnp5ceA9ejQ~w3Z5TMRoZSZrq1YgkidsqGO~a0XmHCmA1PEZdG2aszJalISJyCOYdGIgAYCyTl3sFQMapYCkvzOkpJQLciHb-Oan5p-KptGQCYUQoTHFad-O6XuD-VNm57Ys7JqTvFArWMnsL8Z5GBhdPxkJ81uwdtH8NWO~h3bmKZhXUusJ8nLc515EGBEXh0bqCxHA2Zca9yW4w__&Key-Pair-Id=K3NV4LZ47N8M46)

**Example Use Case:** For the same problem of identifying the first non-repeated character:

- Hidden test cases validate the solution’s correctness under corner conditions, such as empty or long strings.

**Tip**: You can disable the output visibility for hidden test cases via the Questions tab in the test settings. However, enabling output is recommended for an improved debugging experience.

## Creating a New Test Case

1\. When creating a new coding question or editing an existing one, you will need to follow the steps for creating a new question and eventually come to step 4, which is adding the **Testcases.**

2\. In the **Testcases** section, you can **Upload Solutions** and **Add test cases** one by one or in [bulk by uploading a Zip File.](https://support.hackerrank.com/articles/5773853281-how-do-i-upload-all-test-cases-at-once)  

![2024-11-11_12-06-30.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734993712790-35286833883027-550271cf-c7e5-4b0a-94e7-fe5a53e94455?Expires=253370764800&Signature=Te38~Vn0bLtpmjGRw8DBEWUq7NGlDPR1IGJD3YQJsssdEH0YlZIatKbfiG1-dXzI3CCyQCyhqp1RzjAdIavw2RgL9SmtQPXIjCbdUlYe6wAI7UIVT5aSzxG1zey04ETzMJQnoPK2KlVH-x6TMc7YQ1rbyZdzpw1Rt5puQVP8CNK73tG1-QTUGFpIdI7sD4WIRKTZHq4k7ZQHZutW23uomiKVgTIfxXRGZLU1nfTkwskBlEd9eh9Udm7rCxziLXc-ueDHQfTGVDdR2zFI2OuTTLRUE3RT~K6nbe0bwDPUIIGBGUiqon93UjArPanpacSGeVY9RKO53IuYy3rNFb7lXQ__&Key-Pair-Id=K3NV4LZ47N8M46)

3\. While adding a test case, enter the mandatory details such as name, difficulty, score, input, and output. 

4\. Select **Mark as a sample test case** only if you want to identify a test case as a sample type. You can add the required number of sample test cases to a question and choose not to assign scores for them.

5\. Similarly, you can add the required number of hidden test cases to the question (uncheck "**Mark as a sample test case**"). Hidden test cases should contain edge case scenarios to validate the candidates' code solution. When the candidate compiles the code, the hidden test cases will be executed to show the status and help the candidate to know if their code returned the expected results. 

![Adding a Test Case.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734993743714-32891410894995-4c270c72-4f4c-44b6-89d7-562766d05ddf?Expires=253370764800&Signature=IByAukJr5ko1XzVwPoxa0EyO7TkxDddCiFaz2ypmjngkNXIcH-U1SUcC66LDbMOpqIrmLhB6v2dYrVvtG5Xcr2tZNVwH4A2UlZswwBx1MzzsB7dTGX78ZXukmZdH3KDmxVmwQ7Gfu6eHzg2fQb10mUtnwe6G1dPqPPw4mhIDxSvCSuQNeU0dlFvll1s1zljZ3AIuycknTvOM5Nf2U3ns5Vqp1Q4aDAK2QcK7Z9kTeYSs4G9xUdIxDPT82fce8JxHL6HqW0w-6eBRYwfE~mYC2ApJLphjyFWlRixZUM4b--qTF4x5rWNA5A--NQwuF2YTRP7BTLkCmaKNxOhGw~7omw__&Key-Pair-Id=K3NV4LZ47N8M46)

6\. To avoid EOF issues, we recommend all test cases that require a multi-value input to define the input in the format suggested below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 483.466px"><p><em>number of lines (ex. 4)</em><br />
<em>value of line 1 (ex. 100)</em><br />
<em>value of line 2 (ex. 500)</em><br />
<em>value of line 3 (ex. 40)</em><br />
<em>value of line 4 (ex. 200)</em></p></td>
</tr>
</tbody>
</table>

7\. Leverage our code stub generator to manage the input parsing for candidates. The test case input format for our code stubs is as below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 507.188px"><p><strong>5 separate input parameters e.g. foobar(a, b, c, d, e) - separate parameters by newline:</strong><br />
2<br />
3<br />
4<br />
5<br />
6</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 508.097px"><p><strong>Int / String Array - the size of the array followed by the list of values in the array</strong><br />
3<br />
100<br />
200<br />
300</p></td>
</tr>
</tbody>
</table>

The following image illustrates the candidate's view of the test case execution status for the compiled code in the test. Note that the candidate can only view the sample test case's input and expected output values. Only the test execution results are displayed for the hidden test cases.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734993784529-32888779353235-fd06bfca-1f97-475d-b8d4-9529e056ebb2?Expires=253370764800&amp;Signature=FgQ5ZOFyZlV6B1jv8MUuOkFAA8ExnU6S5mfTDelI0LxO92mh-E3CWzVplifnuXU~A0L5mxR8SOCWcsx152Bi9w5--DXs9vYiu~6BgCIn7lTZH5jgdpWq0hpBFB3REpZssyZuduLYS~5fmAAj1lk00h2-OS8PxVI6v0RnGn5TnRmYiKHt~Riy6DL6CT8tZHTJRBhoMvHXeDX62d8wvIRzMO7Eq2rtt-Ilx-s-dZ5u0Kz8fJrlpcps6hFqEVNxHh5NPowK0ZZqFQovZV7PbdCxy92f0uBqmndcLzrfda80a0IEvFY~OdJ3wnmz4sRbMAQaNiQCN4m2kR4JYiayfSV12g__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Refer to[📄 Viewing a Candidate's Detailed Test report](/articles/8263794320)to know how the test cases show up in a test report. 

### Scoring Test Cases

Assign varying scores to test cases based on difficulty, ensuring a fair distinction between candidates' skill levels:

- Assign more points to complex test cases.

- Sample test cases can be assigned zero points if desired.

- The sum of all test case scores constitutes the total question score.

If the candidate solution does not complete within the test case time limit, the test case fails, and the candidate receives no points. Timeouts usually occur in more challenging test cases with unoptimized solutions. For more information about language-specific time limits, see [📄 Execution Environment](/articles/6693750503).

### Best Practices for Test Cases

#### Syncing with Code Stubs

Ensure input and output structures align with the code stubs to maintain language consistency:

- For arrays, read the size (`n`) first, followed by `n` elements.

- For linked lists, input includes the number of elements and their respective values.

#### **Key Recommendations:**

- Diversify test case complexity and sizes.

- Avoid duplicating test objectives across multiple test cases.

\
