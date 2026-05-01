---
title: "Plagiarism Detection Using MOSS (Measure of Software Similarity)"
title_slug: "plagiarism-detection-using-moss-measure-of-software-similarity"
source_url: "https://support.hackerrank.com/articles/2106056073-plagiarism-detection-using-moss-%28measure-of-software-similarity%29"
article_slug: "2106056073-plagiarism-detection-using-moss-%28measure-of-software-similarity%29"
last_updated_exact: "Jan 20, 2025, 12:03 PM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Screen"
  - "Test Reports"
---

# Plagiarism Detection Using MOSS (Measure of Software Similarity)

_Last updated: Jan 20, 2025, 12:03 PM (Last updated 1 year ago)_

Plagiarism in the hiring process compromises the integrity of evaluations, making it difficult to assess a candidate’s ability. Plagiarism detection tools help maintain fairness, creating a level playing field that leads to better hiring decisions.

HackerRank employs two primary models to detect plagiarism, specifically in coding questions:

1.  [MOSS (Measure of Software Similarity)](https://theory.stanford.edu/~aiken/moss/): This is enabled by default for all tests. The model compares the candidate code against others in our database. This method is effective in identifying plagiarism from external sources or copied test cases.

2.  [AI Plagiarism Detection:](https://hackerrank-knowledge-base.help.usepylon.com/articles/8000786908-ai-plagiarism-detection) [](https://hackerrank-knowledge-base.help.usepylon.com/articles/8000786908-ai-plagiarism-detection) To detect sophisticated and AI-aided plagiarism attempts, HackerRank leverages an advanced AI-based model. This feature is an option that can be enabled if required. 

This article talks in detail about the MOSS model.  

### Plagiarism Detection Using MOSS

Moss tokenizes candidate code and compares these tokens to detect substantial overlaps. Common strategies to bypass plagiarism detection, such as changing variable names or introducing white spaces, are generally ineffective, as Moss focuses on the overall structure of the code.

Plagiarism detection is conducted for the same question across different candidates and versions of programming languages. The system flags a candidate’s recent submission based on behavioral signals against previous ones, considering overlapping attempt durations.

MOSS plagiarism detection is turned on by default for all HackerRank tests. 

### Verifying Plagiarism in the Candidate Report

To review flagged plagiarism activity:

1.  Go to the **Tests** page and select the relevant test.

2.  Navigate to the **Candidates** tab and select the flagged candidate (indicated by a red triangle).

3.  The **Suspicious Activity** tile in the candidate’s test summary will provide details on plagiarism.

4.  Scroll down to the question flagged for plagiarism and click to view the detailed report. 

5.  The **Attempt Activity** section will display the flagged code. Review it and confirm or dismiss the plagiarism flag.

6.  Click **Yes** or **No** based on the review:

    - Yes retains the plagiarism flag.

    - No removing it.

7.  Use the **View Matches** option to see code similarities, and click **View** in the **Output Diff** column for detailed differences.

### Code Similarity and Output Diff

The Match Percentage shows the degree of similarity between candidates’ code. Use the **View Matches** option to see highlighted differences in the codes, which helps identify potential plagiarism. Based on the percentage, flags are categorized as follows:

- High: ≥ 90%

- Medium: 80%–90%

- Low: \< 80%

### Plagiarism Indicators in Reports

In reports, plagiarism detection is presented as follows:

- **Excel Report**: The **Attempt Plagiarism** column indicates whether plagiarism was detected during a candidate's attempt. The result is displayed as either **Yes** or **No**.

- **PDF Report**: If plagiarism is detected in any candidate's responses, those specific question scores are flagged.

#### Limitations:

This model's limitation is that it cannot determine the exact source of plagiarism. Hence, it is recommended that you review the code playback for the flagged attempt before making a final decision.

#### Related Articles

- For more details, see the [Plagiarism Best Practices Guide](https://hackerrank-knowledge-base.help.usepylon.com/articles/4291690360-plagiarism-best-practices-guide)[.](https://hackerrank-knowledge-base.help.usepylon.com/articles/4291690360-plagiarism-best-practices-guide)

- [Tab Proctoring](https://hackerrank-knowledge-base.help.usepylon.com/articles/1079706165-proctoring-hackerrank-tests#tab-proctoring-18) and [Copy-paste tracking](https://hackerrank-knowledge-base.help.usepylon.com/articles/1079706165-proctoring-hackerrank-tests#copy-paste-tracking-8) can also be used for questions without plagiarism detection capabilities.

- For further guidance, refer to the [Downloading PDF and Test Reports](https://hackerrank-knowledge-base.help.usepylon.com/articles/1786677446-downloading-pdf-and-excel-test-reports) article.

\
