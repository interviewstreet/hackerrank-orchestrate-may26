---
title: "Evaluate Integrity Signals for Flagged Candidates at Scale in Proctor Mode Evaluating Integrity Signals for flagged candidates at scale"
title_slug: "evaluate-integrity-signals-for-flagged-candidates-at-scale-in-proctor-mode-evaluating-integrity-signals-for-flagged-candidates-at-scale"
source_url: "https://support.hackerrank.com/articles/9728791902-interpreting-integrity-signals-at-scale-in-proctor-mode-tests"
article_slug: "9728791902-interpreting-integrity-signals-at-scale-in-proctor-mode-tests"
last_updated_exact: "Jan 28, 2026, 9:43 AM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Screen"
  - "Test Integrity"
---

# Evaluate Integrity Signals for Flagged Candidates at Scale in Proctor Mode Evaluating Integrity Signals for flagged candidates at scale

_Last updated: Jan 28, 2026, 9:43 AM (Last updated 3 months ago)_

Proctor Mode helps test administrators quickly identify potential integrity issues in online assessments. [Proctor mode reports](https://support.hackerrank.com/articles/5663779659-proctor-mode#after-the-test-generate-post-test-integrity-report-26) are easy to review for individual sessions, but become inefficient and challenging when evaluating candidate attempts at scale.

# Evaluating Integrity Signals for flagged candidates at scale

To evaluate Integrity Signal for flagged candidates at scale in Proctor Mode:

## Step 1: Export Proctor Mode data for flagged candidates

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Tests** tab.

3.  Open the test that contains the candidate data.

4.  Go to the **Candidates** sub-tab.

5.  In the left panel, under **Integrity Issues**, select the checkboxes for **High** and **Medium**.

    ![pr1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761737575114-pr1.png?Expires=253370764800&Signature=mPwYKd-jwajvxiqALTLrujkCVMKmzRvUHD5BNmsUu81Buxn2yeXsuhWjcolHKJbn2FNWTTtb2YdkZ-CQ2u3YkDmqpPWaTbMyG6wohP4~OhoA14-M2-n4dVoHb491CzDRK1CmRCL9aAO8LBp91ykobWxEmb32dReChe91X1Lk0ARMBSjkPS70V1ucCE5n2voLQbgQz2VWXDWICNDlayO9zWYksZ76OFRoOQqcNw8wrvPZ4tK455v8FB6fVWiRW2EvXbzexY69j9rie8dlNmhmmiH9lNY42AO8UpOf9TtOCJZqtz6lh2fONm1BRzxmYg2Xtrc7mE5Zsnue9CDoIhcVRQ__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Select the **Select all rows from table** checkbox above the candidate list.

    ![pr2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761737608161-pr2.png?Expires=253370764800&Signature=TEsU7GJSeZiy7Q6oWSHiNuEZdgm8gGO22IgkIXB98Az8TjuLB6oolDk3APJiO4ZK5-kdLRWNxCmsWQOROcX2DnxyRpyjqz7mKe70NaEKTeaNy2gEf84XdYqayCOT-veiIQNv-Xwbb39twaxaC7nY2axDZTltw4QC0KkFwd3euU~i3fTZjrfrc~CW-uHHNncg9t8swIa9C4eX2oWJ8cDtxM7rmUI~ppQ0unOfV-3RVnxM~x8mUHXIN~ZlsgxTIWyPFkkqtj-DkflcNRzt1z~p~4t180hz0gePIiICBuGGf3gssDOULYymahB-NtQRzn8QfLeiOfQqr~8fexUAtoeOCQ__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Click **Export** and select **Excel**.

## Step 2: Apply filters in the spreadsheet

Use the exported file to filter and analyze candidates based on suspicious activities. Apply the following filters:

1.  **Fullscreen Exit Count and Fullscreen Exit Duration:** Indicates how many times a candidate exits the enforced full-screen environment and for how long. The system flags candidates who violate these rules with **High Integrity** issues. There are no known ambiguities in detecting this rule violation.

    - Filter out candidates with **two or more exits**. 

    - If a candidate exited once, check the **Fullscreen Exit Duration**:

      - If the duration is more than 10 seconds, filter out the candidate.

      - If the duration is 10 seconds or less, system does not flag the candidate, but you can review the context to confirm.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761738941216-image.png?Expires=253370764800&Signature=DFmqKmXRe8~hRL8T8fbdFtecz71pM8WPzu87jZJCl-WjsRuLKJ9THoz2QBwqZX~14Ke7hNYh4N5XJhDssedzNK9MDBJWf5D4o~hm1-FQkrGIx1GOyYwaccsT2YnDkikoKwLCpHehI58Tfp0Yps5CXVTwWqryDs1EsF4eZ97vRYoDShyVrEDZJSVKZAPwQmc6-7cU9Z997gA76cMfQs6tDDpyoLvSm0gRRoZEFTgHMqjNqu0DCxFS-tjKws0DuusFoIU-LCpn6BmgwxuPETfi1SluQR9XFxdGlfH~5XGf8l5ibXV7BPMCpRU85aGjWxyVW-cVGk98Gy99qqn795~djw__&Key-Pair-Id=K3NV4LZ47N8M46)

<!-- -->

1.  **Number of Window Exits and Out of Window Duration:** Indicates how many times a candidate navigates away from the active test window and for how long.

    - Filter out candidates with **two or more window exits**.

    - If a candidate exited once, check the **Out of Window Duration**:

      - If the duration is more than 10 seconds, filter out the candidate.

      - If the duration is 10 seconds or less, the system does not flag the candidate, but you can review the context and use discretion.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761737899954-image.png?Expires=253370764800&Signature=ooyVv95lw~QocNAWKfwH6hboHFy9dNMTq34ffoCt-Z2jUlLl30-iw1dXpPbtcLGZ3WKtTHdOnwmPiBNTIh1l1TiVEpq4hrtSFEcf-5Xn~vy8kVLkn-ZeZvUtfqWvWhN9vwgJhk3zp3v90lo5tMjUZextmDG9e2THgV5M5RmMUdgLeIq0XARjwGVdaHLyYPxFJjN~AgGXdY3dR9e2SBRmoVehBJqooe2uCdGOfJIJjBLOTDqj8xBgeM5aW2syP4ufxfgJurs4KtbNTsdrxIfu4VlKPo0Ehi0f5UtUSZ2rrOb5GTpDlx77J1HUES0HCtyyuxc2d1Xnx--Kil-vvnZfww__&Key-Pair-Id=K3NV4LZ47N8M46)

<!-- -->

1.  **Proctor Activity Suspicion Severity and Proctor Activity Suspicion Score:** Indicates suspicious activity detected during webcam monitoring.

    1.  Check the values under the **Proctor Activity Suspicion Severity** column. The system marks this column as **High** or **Medium** when it detects multiple faces, different faces, or no face.

    2.  Check **Proctor Activity Suspicion Score** column to understand the overall confidence of the flag.

        - **Score 10:** High confidence

        - **Score 5:** Medium confidence

    3.  Check the **Proctor Activity Reasons** column to identify the detected anomaly.

        **Severity order:**

        1.  Secondary face

        2.  Multiple faces

        3.  No face

    4.  Filter out candidates with High suspicion severity.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761738542431-image.png?Expires=253370764800&Signature=Lh6Iok8gAy-Y4cexCgQU58Pgqm1IsU7EH7HiGwjn8R~sVndUmXY-ZIl0xHt6aNZo1BECi8FJmU7DUWpyYcU0~RIiGqTfqT3K7oszn0KkqCrYTkDeeVdlLYCdBeVPm6XZLpWsxkvA9sn6FviU~6~XalN~jhrggFYd9kAb6GF3SH35PtAJ6lj0MCTGoAueRUD9HJ~KWrmTsP1QZDOEFnUp27eA-5qq1BK5~iXdzM~FC4o1YUbbRMVa9McYs1EZCj8tXwQDlNf1AY3~Geufbmt8HnUFXmakn~ra-zCBGh2FKGOyv1X1eU5ThgqAvFsCjv3Hmh9kqgd~HzzN~z9IdPYl9Q__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** Ignore multiple-face violation flags if the test takes place in a setting where multiple faces are expected (for example, invigilated university exam halls)

1.  **Integrity Summary:** Review the **Integrity Summary** column for tools detected in the screenshots taken during the test. Common tools include:

    - External websites or reference material

    - AI assistants and cheating tools (for example, ChatGPT, InterviewCoder)

    - Messaging and conferencing tools (for example, Slack, Discord, WhatsApp)

    - Remote desktop tools (for example, AnyDesk, TeamViewer)

    An honest test session shows only the HackerRank interface. If a candidate opens another application or navigates away, the system flags it in the **Integrity Summary**.\
    Use discretion when reviewing flagged tools, and verify by checking screenshots in the **Session Replay** on the attempt report.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1761738403419-image.png?Expires=253370764800&Signature=kVRsyNkyB9YOuCdAj5wIOwiDJuYp~xyfGqcpq~x5JQPBT04g5bUoGe9f73lQlzq5S5SsHmTLye9lrbsRSsN-suelUfDe7ITIn7BEqkR7KOLOt5GwPlwOwHJmvNkFRxkZ05agvXQbO2BONw01fy6WGhpxAuHUN-woXxZ~8MjWcQ56PVJM9ohWv03KbkKQlAQ8Bwn744WIy4wKpOHW23o1xeCfYA2R059NG~kfcZb4ze2q-hiwlpRpgNZ0g~oV1Pil4EdByh4KMdxm5mD8EvKz6c6kpNpPUnoURnvIKnXNsT3TbYKJSB730inPbOrkG4~fRsKxAwO4bk96xGDL7vGlDA__&Key-Pair-Id=K3NV4LZ47N8M46)

<!-- -->

1.  **Attempt Activity Suspicion Severity and** **Attempt Activity Suspicion Score:** Indicates suspicious or unusual code-writing patterns detected by advanced plagiarism models.

    - Filter by **Attempt Activity Suspicion Severity** based on the severity values:

      - **High:** Strong suspicion of plagiarism

      - **Medium:** Suspicious activity with lower model confidence (many customers choose to ignore medium flags).

    - Filter further based on **Attempt Activity Suspicion Score.** The scores here are indicative of the confidence level of the prediction. Higher the score, higher the prediction confidence.

      - Score 8-10 → High confidence

    - Check the **Attempt Activity Reasons** column to identify the suspicious pattern:

      - Large copy-paste events (blocked in Proctor Mode)

      - Suspicious code resets (candidate deletes large portions of code and restarts with a new approach that passes most test cases).

\

\
