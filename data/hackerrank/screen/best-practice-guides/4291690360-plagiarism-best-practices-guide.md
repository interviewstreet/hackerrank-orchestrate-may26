---
title: "Plagiarism Best Practices Guide"
title_slug: "plagiarism-best-practices-guide"
source_url: "https://support.hackerrank.com/articles/4291690360-plagiarism-best-practices-guide"
article_slug: "4291690360-plagiarism-best-practices-guide"
last_updated_exact: "Jul 1, 2025, 2:54 PM"
last_updated_relative: "Last updated 10 months ago"
breadcrumbs:
  - "Screen"
  - "Best Practice Guides"
---

# Plagiarism Best Practices Guide

_Last updated: Jul 1, 2025, 2:54 PM (Last updated 10 months ago)_

This guide has been developed to assist you and your organization in understanding how plagiarism is detected, tracked, and reported upon with the HackerRank for Work Platform. You’ll also find considerations, takeaways, and suggested steps to prepare a HackerRank assessment and follow up on candidate submissions.

## **How does HackerRank flag a candidate for plagiarism?**

Our [plagiarism flag](https://support.hackerrank.com/hc/en-us/articles/16146609166483-AI-Powered-Plagiarism-Detection) is an indicator that there is a similarity between the code written by two or more candidates. The goal is to identify candidate submissions with the likelihood of plagiarism by comparing candidate codes and augmenting this with certain behavioral signals.

In simple terms, we flag candidates by looking at code similarity between candidates’ attempts starting at a 75% match. HackerRank then makes use of certain behavioral signals to improve the precision.

- For context, a 75% match score is considered when the candidate has written at least 10 lines of code. If the candidate has written less than 10 lines of code, we have a higher threshold for a match score of 90% to flag candidates for plagiarism. This is to ensure that we don’t flag candidates for questions that require writing simple code snippets of 10 lines of code or less.

## **Pre-Assessment: Test Creation Best Practices**

1.  Create sections within the test and add questions of all difficulty levels - Easy, Medium & Hard. For example, creating multiple sections varying in difficulty.

    - Including sections harder in nature, will reduce plagiarism. 

      - Section 1 - Easy

        1.  Section 2 - Medium

        2.  Section 3 - Hard

2.  Create a Question Pool within each section and randomize the questions within a section to vary the test from one test-taker to another.

3.  Clone and modify assessment questions. 

    - Many plagiarism cases occur because of questions being leaked, which leads to candidates copy-pasting the solutions available online.

      1.  Cloning and modifying questions by adding alternate test cases, changes to the problem statement, etc., helps in two ways.

          - Candidates who copy and paste the standard answer from the web cannot acquire a high since their code doesn’t pass the newly modified test cases.

            1.  Through modifications to the problem statement along with adding scenarios relevant to your organization, the question will not easily be found on the internet.

4.  Keep the login window short and the test duration closer to the recommended time to avoid question leakage. 

    - For context, some companies with large test expirations times for their assessments have encountered upwards of 50% of their candidates being flagged for plagiarism.

      1.  Recommendations for the test login window (test expiration time) 

          - (Varies from one organization to another)

            1.  15-20 mins - for up to 10K candidates sitting for a test

            2.  30 mins -  10K + candidates sitting for a test

5.  Tab and Copy Paste Proctoring and other Test Integrity Settings

    - Today, Copy Paste tracking is enabled by default for all of your customer tests. This will deter candidates from pasting code into their assessment attempts. 

      - Copy-Paste information (Copy-Paste Frequency) is available in the excel report as well as individual candidate reports ( Reviewer can view the lines of code copy-pasted by the candidate )

      1.  Tab Proctoring will deter candidates from moving out of the test window. Tab proctoring also tracks the number of out of window exits made by the candidate as well as time spent outside the window. Both these details are available in the candidate excel report. Copy-Paste information (Copy-Paste Frequency) is available in the excel report as well as the individual candidate reports ( Reviewer can view the lines of code copy-pasted by the candidate ).

          - For more information about downloading an excel report, check out the [Downloading PDF and Excel Test Reports](https://support.hackerrank.com/hc/en-us/articles/360012776753-Downloading-PDF-and-Excel-Test-Reports) article.

      2.  Use sections while creating tests and **add randomization** by allowing the system to **pick a set of different questions for each candidate**. Since each candidate may get different questions, it is difficult for the candidates to split the test questions among themselves and share answers. Refer here - [Section-based testing (Creating test sections and how to use them)](https://support.hackerrank.com/hc/en-us/articles/360000784408-Section-based-Testing-#creating-test-sections-and-how-to-use-them%C2%A0)

      3.  Enable the **“shuffle questions”** option, which would add another layer of randomization to the ordering of questions as well so that candidates cannot rely on question numbers for getting the answers. Refer here - [Shuffle Questions and Question Points](https://support.hackerrank.com/hc/en-us/articles/115006328628-Modifying-Question-Settings-for-Tests#shuffle-question-and-question-points%C2%A0)

      4.  The **Hide Question Title** lets you disallow candidates from using a question title as a prompt on search engines to find answers to screening questions. While the actual question tiles are hidden from the candidates, they will be replaced with a generic title like Question 01, Question 02, etc. (Learn more in the [ConfiguringTest Integrity Settings](https://support.hackerrank.com/hc/en-us/articles/8915614977939-Configuring-the-Test-Integrity-Settings) support article)

6.  Leaked Questions 

    - Before taking the test LIVE, ensure that none of the test questions are leaked. If any questions have been leaked, it is recommended to remove and replace the leaked question within any test before inviting a candidate.

      - For more information, check out the [Leaked Question Indicator](https://support.hackerrank.com/hc/en-us/articles/360009582313-Leaked-Questions-Indicator) article.

7.  Test Instructions

    - Mention very clearly in the “ test instructions” (under test settings = \> “candidates” section” that there is zero tolerance for plagiarism, and copying will result in disqualification.

## **Post-Assessment: Best Practices**

1.  Shortlisting plagiarized candidates from the excel report.

    - Attempt plagiarism - YES/NO 

      1.  This Yes/No includes “ Inside the Test & Outside the Test” plagiarism results.

          - For more information on downloading Excel Test Reports, access our [Downloading PDF and Excel Test Reports](https://support.hackerrank.com/hc/en-us/articles/360012776753-Downloading-PDF-and-Excel-Test-Reports) article.

2.  Plagiarism Percentage

    - By default, the system will flag a candidate as plagiarized when the match score is greater than 75% if at least 10 lines of code are written by the candidate. If there are \<10 lines of code, we will flag candidates for plagiarism only if the match score is greater than 90%. This is to ensure that we don’t flag candidates for questions that require writing simple code snippets (of \<10 lines).

      1.  We recommend a sliding scale based upon the difficulty level for the questions which are part of your assessment. (This is to keep the number of candidates being flagged as potential plagiarism within reason for easier questions)

          - Easy questions = 90%

            1.  Medium questions = (80-90%)

            2.  Hard Questions = 75%

3.  Copy-paste activity

    - **Copy-Paste Frequency** tracks the number of times a candidate tries to copy-paste the code. An increase in this frequency reveals the elevation of malpractice by the candidate.

      1.  HackerRank recommends leaving the alert message prompt to candidates off.

          - This is to prevent candidates from trying other avenues of cheating aside from copy-paste. For example: Typing the code instead of copy-pasting it.

4.  Tab change activity

    - Out of window duration (in seconds)

      1.  Number of window exits (count)

          - HackerRank has observed that for all plagiarized attempts, the median value for the out of duration window is 65 seconds and the median value for the number of window exits is 1.

          - In turn, any candidates with an out of window duration greater than 65 seconds and the number of window exits is more than a singular exit, could be considered a suspicious attempt.  

**Note:** If you’d like to analyze a specific question, you can also review the question column in an excel report to check if there was a particular question for which the majority of the candidates were flagged for plagiarism. For such questions, chances are high that there is a solution available on the internet, or it may be an easy question. It’s also possible that this particular easy question has only limited solutions. Keep in mind, that there are potentially additional reasons.

## **How do we go about shortlisting plagiarized candidates directly from the platform?**

To effectively identify candidates who potentially have plagiarized and be able to differentiate them from those who honestly entered in code, **a manual review is highly recommended.**

**Review by Hiring Manager**:

- **Review the code playback option to view a candidate’s entry**.

  - Code playback is available under the Detailed Tab within a Candidate Report generated post-assessment/test.

    - This feature helps in playing the recording of the candidate’s code submitted for a given HackerRank Assessment. We capture the code snippet written by the candidate whenever the candidate runs the code and display the playback in the report.

      - For more information on Code Playback [click here](https://support.hackerrank.com/hc/en-us/articles/360042800834-Key-Components-in-Candidate-Report#viewing-the-code-playback-in-the-report).

- **Note the copy-paste indicator** (Has a large amount of code been pasted?)

  - The copy-paste indicator can be found on the Detailed Tab of a candidate report. For more information, refer to the [📄 Plagiarism Detection Using MOSS (Measure of Software Similarity)](/articles/2106056073)
    \

- **Review the time taken by the candidate to attempt the particular question**.

  - Available on the Summary and Timeline Tabs of a candidate report. 

    - Then, view insights for questions to view how long candidates are spending on the question on average.\
      \

      - For more information, check out the [Viewing Question Insights](https://support.hackerrank.com/hc/en-us/articles/360061747174-Viewing-Question-Insights-) article.

## **What other help can you get from HackerRank on this topic:**

- Upon customer request, in selected cases, we can loop in the data teams to perform a complete analysis of the customer tests to see where they stand compared to our global average. 

\
