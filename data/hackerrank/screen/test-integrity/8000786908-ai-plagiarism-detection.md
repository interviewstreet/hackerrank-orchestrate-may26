---
title: "AI Plagiarism Detection"
title_slug: "ai-plagiarism-detection"
source_url: "https://support.hackerrank.com/articles/8000786908-ai-plagiarism-detection"
article_slug: "8000786908-ai-plagiarism-detection"
last_updated_exact: "Jan 28, 2026, 9:42 AM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Screen"
  - "Test Integrity"
---

# AI Plagiarism Detection

_Last updated: Jan 28, 2026, 9:42 AM (Last updated 3 months ago)_

Plagiarism in the hiring process compromises the integrity of evaluations, making it difficult to assess a candidate’s abilities accurately. Plagiarism detection tools help maintain fairness, creating a level playing field that leads to better hiring decisions.

## Types of Code Plagiarism

We encounter three types of code plagiarism: 

- Use of AI tools when explicitly prohibited.

- Plagiarism from other external sources like the internet.

- Copying code from someone else who took the same test. 

## Types of Plagiarism Detection Models 

### Standard plagiarism detection

[Standard plagiarism detection](https://support.hackerrank.com/articles/2106056073-plagiarism-detection-using-moss-(measure-of-software-similarity)) is enabled by default for all tests. It uses [Moss](https://theory.stanford.edu/~aiken/moss/) (Measure of Software Similarity) to compare a candidate’s code against others in our database. This method effectively identifies plagiarism from external sources or copied test cases (as mentioned above under types of code plagiarism). However, it may result in false positives, depending on factors such as code length and similarity threshold.

### Advanced AI plagiarism detection

To address all three types of code plagiarism, including AI-aided malpractice, we have developed an advanced Machine Learning (ML) model. This model analyzes multiple factors, such as:

- Code writing patterns

- Time taken to solve the problem

- Copy-paste activity

- Tab-switching behavior

The ML model predicts suspicious behavior and classifies candidate attempts in a test as either "**High**" or "**Medium**." This detection is especially useful for identifying the use of AI tools like ChatGPT when their usage is restricted.

The flagged attempts are highlighted in candidate reports, allowing hiring teams to review the reasons and make informed decisions. Human oversight remains crucial, as the ML model currently has an overall precision of **85%**, meaning flagged sessions are correct **85%** of the time.

**Note**: The AI Plagiarism Detection feature currently supports only Coding questions.

### Limitations

AI plagiarism detection is limited when evaluating questions requiring minimal effort to achieve a full score or when solutions consist of very few lines of code. These scenarios often lack enough data points for accurate detection. However, the system will still flag the response for potential plagiarism if significant external content is copy-pasted.

**Note:** Given that it’s a Machine Learning model, we comply with the audit requirements mentioned in the [](https://support.hackerrank.com/articles/8514725302-summary-of-bias-audit-results-(hackerrank's-image-analysis-system)) [AEDT / NYC AI law](https://support.hackerrank.com/articles/8514725302-summary-of-bias-audit-results-(hackerrank's-image-analysis-system))[.](https://support.hackerrank.com/articles/8514725302-summary-of-bias-audit-results-(hackerrank's-image-analysis-system))  

## Enabling Advanced Plagiarism Detection for a Test

This feature can be enabled from Test Settings. 

**Steps**

- Click on **Settings** within a test and select **Test Integrity** under the **Test Administration** section.  

- Scroll down to **Plagiarism** and turn on the **AI Plagiarism** toggle.

- Click on **Agree & Enable** from the following popup. 

![7c6722ef-474f-4575-86f8-7df538645a7a.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046211204-?Expires=253370764800&Signature=d2dZ-F~HtkYN4R3ATZYqBEHek8ITIvA45yhX0DSw1vUiDSFpJnZHe723RlAWREKs4Zak4mQBHB3RFyW7hKqTAYMk0Oh9gbajPL51sX8fd7yGmjFeQJGEsUFb6zlD56PVqV7qxgbSrrUS7EMmX6Z5PFrO1JfQ7zGvjKS9qIIkb2j4EIyFqEXoIBaTZtZWXS7twt0oDOkVOAlg-qbkIiimtXRv56A1njUrnrnaa7HrdC8XN81LbdF88u99Iw~ke5mZctdsnmfGRGKzzUVegwGjX0UNg3tj2XTcg0VxmesFvA~Qjy~GnOiFOLNAscqB0l3syok1WsZLSeTYM9vecdhb~g__&Key-Pair-Id=K3NV4LZ47N8M46)

## Candidate Consent

When AI plagiarism detection is enabled, candidates must consent before starting the test.

![7bf3e75d-b7ec-434b-9965-65858e62a65e (1) (1).png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046211595-?Expires=253370764800&Signature=aM3R2B293W1nA~RcD46YwWWAiqD2wK37HWBpx1zkhBl~mR4C5M95A4h6eAX86zInUThme1AwHjHXrerlJyTQUKclsphqU8mHwx0LBEVYcOmJJaIJJ8Em9I98o35BL0azeamVa--VQ110cGvnoG8I28865j0eWEf-MGIR4Vru2HtxviZ58Q1twUVFb1PxI6sOChcedWPG9kkqzV28cJegQoKlge936X0tQ-Zj2aHCwoZCFY0hbmJSE2JUimx4jp0WfoguLVzOs0gGr9rovKd4KO7aNHhtCDnzTqmbWciUP0KzwK6FBdthxNbohckO7xptqb5AdRwitQLzX9HllQwgrg__&Key-Pair-Id=K3NV4LZ47N8M46)

## Signals Used for Detection

A non-exhaustive list of factors considered:

- **Copy-Pasting:** Significant portions of code copied from external sources.

- **Coding Patterns:** Structural similarities in code and distinct coding styles.

- **Iterations:** Multiple iterations in the code while tackling layered tasks.

- **Tab-Switching:** Switching away from the active test tab during execution.

## Viewing Flagged Plagiarism Attempts

When a candidate's test attempt is flagged for plagiarism, it is categorized as "**High**" or "**Medium**" based on the confidence level of the model’s prediction. Follow the steps below to view these flagged attempts.

**Steps**

1.  ** **Navigate to the **Candidate List** and choose the candidate whose test attempt has been flagged.

2.  You can view the suspicious activity under the **Performance** tab in the Candidate Summary report.

3.  To review more details on the plagiarism signals, click on the question that has been flagged.

4.  In the question details, the **Keystroke Codeplayer** lets you quickly understand why a candidate was flagged for plagiarism. You can navigate to the relevant portions of their coding journey where potential suspicious activity may have occurred.

![CodeSimilarity.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761737395059-CodeSimilarity.gif?Expires=253370764800&Signature=h~LGe7FRkjEljf64dTPFCnlmeXVlqzNjwq2DfUGI26w28xQ92L1-IkSg88ARVGqFHaW0J~CK7jmzqbqRgT7FrMgSk85o2-OGAjiD1BMrEaFgEYYTpxBy8PgWQx7Qk5P98HNv3lRc~lpHbeZkNoVo8-PzW6w2bZVRtW-AxzD~zJw3KorRSyTdEq6oBlgiMVQb23U-1l1N9tkLH1VbZcD8CO7fiS5HQTVzWt02iaV6wfbJGTNCpSKoReMoNfx3srq-U~PnnvBEpCJvbWiUtSNYBdBigslnUYeoiIPs6EcvEJoseVGCMi84Y4rIQkt8J0naYupgreNBkrnFe4Ff~KG5bA__&Key-Pair-Id=K3NV4LZ47N8M46)

### Understanding the Reasons for Flagging

There are two main categories under which a candidate’s attempt can be flagged:

**Code Similarity:** The candidate’s code is similar to one or more candidates' submissions, indicating potential plagiarism.

**Coding Patterns:** Unusual behavior was detected through the candidate’s keystroke patterns during the test. This may involve:

- Code iterations

- Writing patterns or 

- Tab switch instances

**Sub-Patterns in Coding Behavior**: The following sub-patterns are commonly detected when **coding patterns** raise concerns about the candidate’s behavior:

- **Suspicious Code Resetting:** A large section of previously written code is deleted and replaced, accompanied by irregular typing or cursor movements.

- **External Copy-Paste:** Significant portions of code are copied directly from an external source.

## Continuous Model Improvement

HackerRank’s dedicated ML team continuously improves the plagiarism detection model by learning from emerging patterns of code plagiarism and misclassifications. When a statistically significant improvement is made, new updates to the model are deployed automatically.

## FAQs

**Will coding in an external IDE instead of the HackerRank platform trigger a potential cheating flag?**

If candidates use Projects, which support an offline workflow (coding in their own IDE and pushing the code to the HackerRank platform), no cheating flag is triggered.

However, if candidates solve a standard coding question in an external IDE and copy and paste their code into the HackerRank platform, the system is likely to flag this behavior as suspicious activity.

## Related Articles

- Standard Plagiarism Detection - [](https://support.hackerrank.com/hc/en-us/articles/115005603547-Plagiarism-Detection-Using-MOSS-Measure-of-Software-Similarity) [Moss model](https://support.hackerrank.com/articles/2106056073-plagiarism-detection-using-moss-(measure-of-software-similarity))

- Future of Hiring with AI - [](https://support.hackerrank.com/hc/en-us/articles/31668981495187-The-Next-Generation-of-Hiring-Interview-Features) [Next-gen Hiring Process](https://support.hackerrank.com/articles/5377881818-the-next-generation-of-hiring%3A-interview-features)

- [Plagiarism Best Practices](https://support.hackerrank.com/articles/4291690360-plagiarism-best-practices-guide)[](https://support.hackerrank.com/articles/4291690360-plagiarism-best-practices-guide)

\
