---
title: "Best Practices to Maintain Test Integrity"
title_slug: "best-practices-to-maintain-test-integrity"
source_url: "https://support.hackerrank.com/articles/1878974014-best-practices-to-maintain-test-integrity"
article_slug: "1878974014-best-practices-to-maintain-test-integrity"
last_updated_exact: "Mar 4, 2026, 4:43 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Screen"
  - "Best Practice Guides"
---

# Best Practices to Maintain Test Integrity

_Last updated: Mar 4, 2026, 4:43 PM (Last updated 2 months ago)_

This guide provides best practices to maintain test integrity.

## Prevent Question Leak

Before inviting candidates, ensure the test does not contain any leaked questions. If leaked questions are identified:

- Remove or replace them before candidates take the test.

- If leaked questions are discovered after the test, exclude them from scoring and check for plagiarism or copied content in the candidates' submissions.

- Use the Watermarking feature to find out who leaked the questions online.  

Refer to the [📄 Manage Leaked Questions](/articles/8820947031)for more on identifying leaked questions.

## Monitor Candidate Malpractice Activity During the Test

### Copy-Paste Tracking

You can enable the [Copy-Paste](https://support.hackerrank.com/hc/en-us/articles/360011479133-Proctoring-HackerRank-Tests#copypaste-tracking) option to monitor and track the number of times candidates copy or paste content from external sources. 

The **Copy-Paste Frequency** column in the Excel report shows how frequently a candidate has copied or pasted code, helping you detect possible misuse of resources.

### Tab Proctoring

Activate [Tab Proctoring](https://support.hackerrank.com/hc/en-us/articles/360011479133-Proctoring-HackerRank-Tests#tab-proctoring) to monitor if a candidate leaves the test window during the assessment. This feature can track the number of times the candidate left the test screen and the total time spent away from the test screen. 

The Excel reports will capture the **Number of window exists** and **Out of window duration (seconds)** for further analysis. 

## Prevent Impersonation

### Image Proctoring

Enabling [Image Proctoring](https://support.hackerrank.com/articles/7825915809-impersonation-detection#image-proctoring-13) [](https://support.hackerrank.com/articles/7825915809-impersonation-detection#image-proctoring-13) requires candidates to keep their cameras on throughout the test. Images of the candidate are captured at regular intervals until the end of the test. The captured images can help you detect suspicious behavior, such as:

- The presence of other people with the candidate.

- The candidate using a mobile phone or other gadgets.

- The candidate consistently looks away from the screen.

- Long absences from the screen, indicating the candidate has left the room.

**Note:** If continuous image capturing is not required, you can use the [Photo Identification](https://support.hackerrank.com/articles/7825915809-impersonation-detection#photo-identification-3) feature to capture a photo of the candidate before the test begins.

### Image Analysis with AI

The [Image Analysis](https://support.hackerrank.com/hc/en-us/articles/17971376196627-Detect-Suspicious-Activity-Using-Image-Analysis#enabling-image-analysis) feature uses AI to analyze the proctored images to provide more details in the report such as suspicion score, suspicion severity, and reasons behind the suspicion.

The information is captured under **Candidate Attempt Activity** in summary reports on the platform and Excel reports. A set of five images is displayed for each suspicious event, providing a quick preview.

You can decide whether the flagged activity warrants further action, such as rejecting the candidate or requesting clarification. 

### Multiple Monitor Detection

Sometimes, candidates may employ a proxy to complete their assessments by using an additional monitor. You can utilize the [Multiple Monitor Detection](https://support.hackerrank.com/hc/en-us/articles/17793999314963-Multiple-Monitor-Detection) feature to identify these instances and request clarification from the candidates.

## Prevent Sharing of Answers During a Test

### Randomize the test structure 

- **Create sections** with varying difficulty levels: Easy, Medium, and Hard.

  - Example:

    - **Section 1**: Easy

    - **Section 2**: Medium

    - **Section 3**: Hard

  - Including harder sections helps reduce plagiarism.

- **Randomize questions** within sections to vary test questions for each candidate.

  - Use a Question Pool and shuffle questions for each candidate.

  - It is advised to randomize questions especially for MCQ (Multiple Choice Question) and Sentence completion question types to make it harder for candidates to share answers

- **Modifying Questions**

  - Clone and modify questions to prevent candidates from copying answers found online.

  - Change or add new test cases or make minor edits to the problem statements to make answers harder to find. This ensures that copied solutions do not pass newly added test cases.

  - Enable the **hide question title** option so candidates cannot search for answers online using the title. When you use this feature the question titles are displayed like Question 01 or Question 02.

### Timing Considerations

Shorten the login window to enter a test and keep the duration of login close to the recommended time to reduce the risk of question leakage.

**Recommended login window:**

- 15-20 minutes for up to 10,000 candidates

- 30 minutes for over 10,000 candidates

## Detect Plagiarism

[AI Plagiarism Detection](https://support.hackerrank.com/hc/en-us/articles/115005603547-Plagiarism-Detection-Using-MOSS-Measure-of-Software-Similarity) is highly recommended if your organization can utilize AI in the hiring process. 

Over the past year, AI tools like ChatGPT have evolved rapidly with frequent upgrades and enhanced problem-solving capabilities. These tools are increasingly used by software engineering professionals, making AI-assisted code plagiarism a leading cause of plagiarism in coding assessments.

Since the launch of our latest model, we have detected more instances of code plagiarism, as candidates are using AI tools more frequently in tests. The new model is well-equipped to capture these latest forms of code plagiarism using several [indicators](https://support.hackerrank.com/hc/en-us/articles/16146609166483-AI-Plagiarism-Detection#viewing-flagged-plagiarism-attempts), including references to AI tools.

**Note:** The [Standard Plagiarism Model - MOSS,](https://support.hackerrank.com/hc/en-us/articles/115005603547-Plagiarism-Detection-Using-MOSS-Measure-of-Software-Similarity) is available by default in your account if your organization cannot enable the AI plagiarism feature for hiring. Since this model has certain [limitations](https://support.hackerrank.com/hc/en-us/articles/115005603547-Plagiarism-Detection-Using-MOSS-Measure-of-Software-Similarity#plagiarism-indicators-in-reports), we recommend manually reviewing code playback for any flagged attempts.

## Considerations

- Communicate a zero-tolerance policy for plagiarism in the **test instructions**, stating that any copying will lead to disqualification.

- Regularly review and update **tests** to ensure their integrity.

- If concerns about a candidate's test integrity remain, request an explanation of their approach in a [live interview](https://support.hackerrank.com/hc/en-us/articles/115007439768-Key-Interview-Features). During the interview, ask them to modify their submitted code to demonstrate their understanding.

\
