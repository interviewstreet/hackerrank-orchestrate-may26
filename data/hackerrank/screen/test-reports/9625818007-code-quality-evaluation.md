---
title: "Code Quality Evaluation Key benefits Evaluation method Enabling code quality evaluation Reviewing candidate results"
title_slug: "code-quality-evaluation-key-benefits-evaluation-method-enabling-code-quality-evaluation-reviewing-candidate-results"
source_url: "https://support.hackerrank.com/articles/9625818007-code-quality-evaluation"
article_slug: "9625818007-code-quality-evaluation"
last_updated_exact: "Dec 1, 2025, 2:13 PM"
last_updated_relative: "Last updated 5 months ago"
breadcrumbs:
  - "Screen"
  - "Test Reports"
---

# Code Quality Evaluation Key benefits Evaluation method Enabling code quality evaluation Reviewing candidate results

_Last updated: Dec 1, 2025, 2:13 PM (Last updated 5 months ago)_

This feature is part of the AI Add-on. For more information, see [📄 Advanced Evaluation](/articles/7098008997).

Code quality evaluation assesses how well the written code adheres to best practices for readability, maintainability, efficiency, and security. This evaluation often takes place through processes such as:

- **Peer reviews**: Developers review each other’s code to ensure compliance with coding standards and identify areas for improvement.

- **Automated tools**: Static analysis tools automatically highlight code smells, formatting issues, or potential errors.

- **Test cases and unit tests**: These validate the functional correctness of the code.

- **Quality metrics**: Metrics include cyclomatic complexity, code coverage, duplication rates, and adherence to coding conventions.

In HackerRank tests, correctness is evaluated through automated test cases and quality assurance checks for functional specifications. Code quality evaluation may also involve highlighting potential issues in specific areas. Adding comments on issues or metrics can enhance assessments by providing insights into maintainability, efficiency, and overall code quality.

# Key benefits

Code quality evaluation highlights how advancements in AI are reshaping the role of engineering. Specifically, it highlights:

- **AI’s problem-solving capabilities:** AI efficiently solves a significant portion of logical and coding problems, prompting hiring teams to evaluate skills beyond accuracy metrics.

- **Need for additional evaluation signals:** As AI enhances problem-solving, hiring teams require extra indicators to differentiate between candidates. This ensures hiring decisions align with the demands of enterprise-level development.

- **Code quality as a differentiator:** For candidates with similar scores, the ability to write clean, maintainable, and high-standard code becomes a decisive factor in assessing competency.

- **Enterprise relevance:** Writing scalable, resilient code is essential for enterprise applications. This reflects a candidate’s readiness to tackle real-world challenges and contribute effectively to organizational goals.

# Evaluation method

HackerRank provides a prompt listing specific rules and issues to the AI model along with the candidate’s code. The AI generates feedback on the code and organizes comments into different categories. Based on this feedback, the system uses a straightforward method to evaluate code quality.

HackerRank uses the time-debt method to create a grading system for code quality. This evaluates how long it takes to fix a mistake compared to how long it took to write the code. If fixing the mistake takes much longer, the code quality is considered poor. This helps quantify the impact of low-quality code and enables consistent grading across different solutions and programming languages.

**Note**: This feature is currently supported only for Coding and React questions.

## Grades based on tech debt

- **Grade A**: Tech debt is low; code quality is good.

- **Grade B**: Tech debt is medium; code quality is average.

- **Grade C**: Tech debt is high; code quality is poor and would require significant fixes.

- **Not Generated:** System does not generate a code quality grade for candidates who score below 50%.

- **Not Available:** Grade is not provided for questions that are not supported for code quality grading.

# Enabling code quality evaluation

Turn on **Advanced Evaluation** to enable code quality evaluation for all tests. For more information, see [Enable Advanced Evaluation](https://support.hackerrank.com/articles/7098008997-advanced-evaluation#enable-advanced-evaluation-6).

# Reviewing candidate results

You can view each candidate’s code quality grade in the **Candidate List**. You can filter candidates by their code quality grade. 

The **Summary Report** also displays the code quality grade in a dedicated **Code Quality** column.

![New Report exp.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1760040826242-NewReportexp.gif?Expires=253370764800&Signature=QihWgb0UTKo0p~NC4~xGBgaot1eC7GpKHgxHog02TKgRyY5sjQJGfRLrXAAzDeM2RVve9BjqfVCQC5r4WmaAB6AYLEEbeHCKbAQomAwgANnZHfo3xyO5GPHOYsDfwjQih~u5dC60b3RYQSsco0TceqaMZnstIdNaevrz6Ezzx3nA30nqZ4DfZ75Qjlwq6-ErhiGD0-ZKRVLdm5skDAWI0uEt26NAB2ME9DD3qZQWoa1owouBctMjPM-cjJ5Zkx1rGccjidWe~FkvJM461cGftO9jfbNwsXLJK-ZWJk9kmnql1UitgSdMyoWOE9-lAhUYDvrryVw9fN8yjvqxYLoC7Q__&Key-Pair-Id=K3NV4LZ47N8M46)

You can evaluate a candidate’s code quality directly in the **Detailed Report**. The report provides a code quality grade alongside the candidate’s score, offering deeper insight into their coding abilities.

## Key components

- **Code quality grade**: A quick indicator of the candidate’s code quality. This requires the question to have a recommended time set.

- **Code comments**: Inline comments in the diff view highlight specific areas for improvement.

If you disagree with a comment, you can choose to ignore it. The grade is automatically updated to reflect this action.

## Reading grade

- **A**: Good quality code; very few issues.

- **B**: Medium quality code; some issues.

- **C**: Poor quality code; significant issues.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1753775152427-image.png?Expires=253370764800&Signature=kUbAz2b8Or660AQrayRlYqUNAX29m3aEEmGpPu5W5tshba2Ohq5ivbmN3ecTbZnDMWYrI3NK4yImAY399wrElovcGwtUCWYNFYS3LkrJM-QQ1PMTY-iC5Nha6CwrmgXweuzy4A2ULeLSTCSo5Z2~~vbdpVz3GEoZ4dBqi2dAPWC92FNKCeWjsWyKqUH3~2O7Jm3JPSxqbs6axe0goJr8JIxZsMUPZgNDMQDGuYuCkLpoTRb44Yax4X3F8dBHE-Pf1GchMZ9LdknxdJtaKN66Z-Tf-LjGpx~~A92SSqXwt-6SFzxze7t7Tuvynm0evvfvXPVCNzXN47Q9wkaEhB8HaQ__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: If a user ignores a violation, the code quality grade is recalculated in real time to reflect the updated assessment.

\
