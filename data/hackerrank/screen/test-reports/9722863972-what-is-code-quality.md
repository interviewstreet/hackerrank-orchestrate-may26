---
title: "What is Code Quality"
title_slug: "what-is-code-quality"
source_url: "https://support.hackerrank.com/articles/9722863972-what-is-code-quality"
article_slug: "9722863972-what-is-code-quality"
last_updated_exact: "Aug 13, 2025, 6:48 PM"
last_updated_relative: "Last updated 8 months ago"
breadcrumbs:
  - "Screen"
  - "Test Reports"
---

# What is Code Quality

_Last updated: Aug 13, 2025, 6:48 PM (Last updated 8 months ago)_

Code Quality is an approximation of the usefulness and maintainability of the code in the long term. Code Quality provides insights to the hiring managers about the coding practices and style of the candidate. This enables the hiring managers to make better hiring decisions that are not just based on the accuracy of the code written by the candidate.

* ***Note**: Currently, we do not provide an overall rating or score for the code quality. Also, we do not evaluate the time complexity of the candidate's code submission. Only the issues in the code are highlighted and described.

The key attributes used to evaluate the code quality of the candidate are as follows:

- **Duplications**: The more the number of duplicate blocks of code, the worse is the quality of the code.

- **Documentation**: A large number of irrelevant comments in the code adversely impacts the code quality.

- **Issues**: The number of issues with the following three levels of severity:

  - Blocker: The blocker issues have operational or security risks. These issues might make the whole application unstable in production.\
    *Examples*: Calling a garbage collector, not closing a socket, and so on.

  - Critical: The critical issues have operational or security risks. These issues might lead to unexpected behavior in production without impacting the integrity of the whole application.\
    *Examples*: NullPointerException, badly caught exceptions, lack of unit tests, and so on.

  - Major: These issues might have a substantial impact on productivity.\
    Examples: Too complex methods, package cycles, and so on.

- **Maintainability**: When candidates use code that is easy to implement in the short run instead of applying the best overall solution, it might require extra development work in the long run. This is referred to as long-term technical debt. The more this debt, the worse is the code quality.

- **Security**: Code quality is also determined by the security vulnerabilities present in the code. Many security vulnerabilities involve coding errors that allow attackers easy access to the system. The more vulnerable the system, the poorer the code quality.

Refer to the [View code quality in a report](https://hackerrank-knowledge-base.help.usepylon.com/articles/5965153034-view-code-quality-in-a-report) topic to understand the steps involved to enable this option.
