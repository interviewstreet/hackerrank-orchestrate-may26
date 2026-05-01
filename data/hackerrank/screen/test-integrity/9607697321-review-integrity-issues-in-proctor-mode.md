---
title: "Review Integrity Issues in Proctor Mode Reporting views in Proctor Mode Workflow for reviewing integrity issues"
title_slug: "review-integrity-issues-in-proctor-mode-reporting-views-in-proctor-mode-workflow-for-reviewing-integrity-issues"
source_url: "https://support.hackerrank.com/articles/9607697321-review-integrity-issues-in-proctor-mode"
article_slug: "9607697321-review-integrity-issues-in-proctor-mode"
last_updated_exact: "Apr 22, 2026, 10:13 AM"
last_updated_relative: "Last updated 4 days ago"
breadcrumbs:
  - "Screen"
  - "Test Integrity"
---

# Review Integrity Issues in Proctor Mode Reporting views in Proctor Mode Workflow for reviewing integrity issues

_Last updated: Apr 22, 2026, 10:13 AM (Last updated 4 days ago)_

Proctor Mode generates Summary Report, Session Replay, and Detailed Report to help you assess candidate behavior and overall test integrity. This article explains how to interpret these reports and review common integrity issues.

# Reporting views in Proctor Mode

Proctor Mode offers three reporting views. Each view provides a different level of visibility into a candidate’s test activity and helps you evaluate potential integrity concerns.

## Summary Report

The **Summary Report** provides a high-level overview of the test session. It includes:

![review proctor mode summary report.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769514218359-reviewproctormodesummaryreport.gif?Expires=253370764800&Signature=LaEn6s7o1m9upcAZobwv7teVnWxb-rB-9EZ5n-ziaF-SNcKvUERWj64NEgMU9pLQvtUFHv4OO3yyw3SGM2tyC7beEn27D3-wFUIiLNvatZROZlcbobqMMtojXjMHBfnq2StE3Ll4rBLP0ZliouKN-W~pKyAzJMV6BvpZW70xIXUFRJupb1lv-UI8LKIJPwVJYapm25QTksePMZMydJYgOaPckZeuhOyOJAe9e8ikZ6~3kKTPyBGA~6-NyGswHSl1RErA5gDb06f~tiqHnXEAqo9aPJkce9cNYsWaiGhW2TGUgxranqvlo5eI-Y4ZzvNBRHc8pTpBCOCXNPWYEreEBg__&Key-Pair-Id=K3NV4LZ47N8M46)

- **Integrity Issues indicator**: Indicates whether Proctor Mode detected any integrity issues during the session and displays the severity level.

- **Integrity Summary**: Lists each reason the system flagged the session. Each suspicious activity appears as a separate bullet.

## Session Replay

Session Replay provides a timeline-based, video-style view of the test session. It includes:

![suspicious activity integrity issues proctor mode.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1765884365440-suspiciousactivityintegrityissuesproctormode.gif?Expires=253370764800&Signature=I5FY-bO2UCxUHhZXTU3iMEAminGIooIhIP2j4ipe-4CCgqHyxUkPS8qxVOM9oMpDGlU50vYFDVez9soTCr83IxlvbpaWCQQNLlqidoIi3xWIeOX6QK3wYyH4coKbSpB5iTmLLs36bkaLF6ZjGEH5O1HzrJyOG8KJBDGbkFD0dzvU9qI2KivRFvw143uzr-XWdWWPdvTpDand~3Sjk1amQyQk2Ph5Ilsz2ThulnElE90U2KaAqSSAtdIgH~kRq9EUmDc4MuAL7GhiAu0VTl6FVgDgTyASe1ibtvemVm6Ip8RBTt4mywvrMgkAe6jyAnVWbfY5DPDYDalGF5dhv6Hdbg__&Key-Pair-Id=K3NV4LZ47N8M46)

- Recording of the candidate’s test session across the full browser screen.

- Lists all critical test events, including integrity events. You can search for events and click any event to jump to the corresponding timestamp in the recording.

- Synchronized timeline showing test activity, webcam images, and screenshots by timestamp.

- Screenshots and webcam images are captured every 15 seconds, with increased frequency around integrity violations to provide contextual evidence.

- Automated analysis of screenshots and webcam images that highlights suspicious activity.

## Detailed Report

The Detailed Report offers an in-depth view of how the candidate performed on each question. You can use this report to investigate a candidate’s performance at a granular level and to review integrity issues, especially when a candidate is flagged for code similarity.

# Workflow for reviewing integrity issues

Follow these steps to evaluate integrity issues in a candidate’s test session.

## Step 1: Check the Integrity Issues indicator

Open the candidate’s **Summary Report** and check the **Integrity Issues** indicator in the upper-right corner.

![image (38).png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769514264013-image%252838%2529.png?Expires=253370764800&Signature=qvCPXfsfJu2M1IUViSUAi4A7SWb-1uN-xpGindfrLhQgzHSS2IGTZq61Rl3kZdR10SR3QIidvIpxDbMn1pHdln-kqkWuTB3RkmVcOEkDA7knqsu-cxCf7QqZBvhKhMQp2rWVqnnK6FLK4WxTNkNXQhvBvB8OadxPOvqxDCDdo65-zbXcGjW7KCQYV3PUcoj-VpAPdpVoXI7a3k2~tUFTLsbA-MotwiJ7hGjuo7oKpfaX~TLEUMDY~DXTZgqNZEfHjKDs~yl16tqaaXNhmOrAEbRyAj4-TfiF4aaELYOYg6-D2ultH1W~8Ng5XR2QQA-GzWbdAq6RWxBNt2oZQcAHSg__&Key-Pair-Id=K3NV4LZ47N8M46)

The indicator shows one of the following values, depending on the severity of the detected issues:

- High

- Medium

- No issues detected

If the report shows **No issues detected**, no further integrity review is required.

If the report shows **High** or **Medium**, continue to the next step.

## Step 2: Review the Integrity Summary

Scroll to the **Integrity Summary** to view the specific reasons the system flagged the session. Each item represents a type of suspicious activity that requires review.

![image (39).png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769514330622-image%252839%2529.png?Expires=253370764800&Signature=S9hk22KHEfjYDzNUi7JR92Ctyhhk~f901lEB4zlwYhQUBRPPlET7dBWCtKm31W414TrMmFPN3~0YeGC6mBga8CBGgF8ku7eiMkaCRJAZDYMMFdjJWT4c9RkRmWc40kyo6~o04folw10AXhoqVqROMKYUeulBmmJ7eb31mDUsz68YLNdIpTfW1JWLuIhGCb2mqazM2drUy3cF9dIoe0hr8aPDZI73T~~iy175N1sLuHPkgAmoBGZGLdV62Ma2ZhbFPlk0ce-UL7X7jXN-6svtqjrKrC-lEGMV1u4ney-L1bBTn-A6Fb5peuB~wGk2UvHLRf1pqZgNdu2~SUpMVaS-2Q__&Key-Pair-Id=K3NV4LZ47N8M46)

Continue to the next step for a detailed review of each activity type.

## Step 3: Review each suspicious activity in detail

The sections below describe common types of suspicious activity and how to evaluate them.

### Tab switch or full-screen exit

Proctor Mode flags the session when the candidate:

- Leaves the test tab for 10 seconds or more (single or cumulative duration)

- Exits full-screen mode for 10 seconds or more (single or cumulative duration)

**How to review**

![tab switch (1)1.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769543249287-tabswitch%25281%25291.gif?Expires=253370764800&Signature=uocb~g-6Yp3TAwsnr7BgxrYvFtJZQJwZMAk5Vd6Q5OLIvKOLvAj2kAJQj5D350w4XXiSlnGA~uFaGiQI~YwlcHubEJavr~NkVwBDO2KlpP0US0bKi8pbFbYyVX-BM9t39O--oGc2gf9wAGst1To2EaOxIR1s8FL5Ycx0UXdO7IaPzlSy2ut0zAs-lf0tsNJezDDbV98YwPfZ1ydxDSH6X5ExSpSll6V0jioVbkMxzsfwShEfjg9xZJEN5KAHcwcTrTRvs1xrPThRw~y2obx-OybDKpGfZOX0Pk4VtA30zydbvb4MlTQpl16gphQivFgGSMTrGTO2peVG8Uku6RMufQ__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Candidate switched tabs** or **Candidate exited full-screen mode** to view flagged time ranges and the duration for each instance.

4.  Select a flagged time range to open the **Session Replay**.

5.  Review the screenshots captured during the flagged time range to understand what the candidate was doing while away from the test tab.

6.  Watch the test-taking tab recording to observe the candidate’s activity immediately after returning to the test.

**Tip:** Look for sudden, high-quality code written after the candidate returns to the test. This pattern may indicate the use of external references.

### Webcam-related integrity issues

If **Image Analysis** is enabled, Proctor Mode captures webcam images every 15 seconds and analyzes them using an automated model. The system flags unusual activity, such as:

- The candidate’s face missing for an extended period

- Multiple faces visible

- Secondary faces detected

**How to review**

![webcam no face detection integrity.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769515481982-webcamnofacedetectionintegrity.gif?Expires=253370764800&Signature=Rtsndt7bn5gReHYrql0740nJMHxXZg~GLpNvSPkbrUjJ1sgFOKnWs4zWeikQWFGIG7G-EQpr5~gocPLgNJqlCpq78FYaHy~y7mAYQG22r3a0mY~GDGWUC90P3KVW1g3QbEX9p-zNpgip4DpoXtsotRcWBkm44XvzX9O7JMKLMJY3DsT2X2QZ9Mb75GbkWoaqVeqCVAtHNISaJbevsSqHKO9tI2w8GlPcvV2t8JSp-rqLhPB8JU9VCZn2NA94cFcpcwFBFwQ6X6VWTprNrPzBunO2GPC4mu1WcbKYTo11-5tgzBwE6KWuGDM7ZItPHq56PieDfvWlNHPcwJxuM6WYJw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Detected in webcam images** to view the flagged images and the timestamp of each occurrence.

4.  Select a flagged image to open it in full size.

5.  Verify that the images match the flagged integrity issue.

To review the candidate’s activity in detail, open **Session replay**.

### Screenshot analysis issues

Proctor Mode takes screenshots every 15 seconds and analyzes them using an automated model. The system flags any screenshot that appears to show unauthorized tools or applications.

**How to review**

![screenshot detection integrity.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769514820640-screenshotdetectionintegrity.gif?Expires=253370764800&Signature=DDd1H2P3KhK3wrDoB8TkQOkj91iwZCSZK5MNH3gnfX0ZQrPAe7U58~sldqO-ayOLveoLwtuHj8LiqVy5T6vzOFxEIwr6RCr6M0hmpNrrVZChMN78Ooag11y84m55ETemPsuul1f37J0ns2NTuYezUqgVMxEy1Sg1QqTFRTy~8gpYFE17Hlrx5egEVHhUNmFi88f9S8xNzyGKBWcXNReJNbQRvaldGgNgSRa32oqQm7rWbEkq736VrV5QgZyO1G-z2LRp3HmNYYTivqe0cWBtXuEPa3EH6~yCP3DNaHnpYNniO9-LICMuxxqzfNb3epvlfN~~gdC20CZ7Lg~WkrSGMw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Detected in screenshots** to view the flagged screenshots

    along with the following information:

    - The detected application or tool

    - The timestamp of the activity.

4.  Select a flagged screenshot to open it in full size.

5.  Verify whether the screenshot shows an unauthorized tool or application.

To review the candidate’s activity in detail, open **Session replay**.

### Object detection in webcam feed

Proctor Mode detects and flags mobile phones and tablets in the candidate’s webcam feed during an assessment.

**How to review**

![Object Detection in Webcam Feed (AI Add-on).gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776332514643-ObjectDetectioninWebcamFeed%2528AIAdd-on%2529.gif?Expires=253370764800&Signature=rxYMBMgh41P0yYUnwA5t5VItHGDSHxN0BI1KdvDvUqaH0WUPvYL9A4uEmO8JkGS6erZ4ZlKeZYCYi-e6Pf082B5dyx5MqZmuS6o1ATH2aBX9e6RqAHUvlZ~3d8s-HcflOJwfuW-Nw~Y1Cdp4Dl4Q0nnW~R8VRPry~v9DpbSL70SBGrBCb5nnzgqRavUQyQuCTWaBuGcfdL2pCWgQcoiDlaKkvmotZcpTyiQvpC7KrU-86yovxUfP0Nvpz5BbQzzn-z9I3rrluXYGMLLFojUgsphi9iLUZhPCTIDxWryxO5hXPcd72Wke-UilgfaT7LL3Y4hYYvNxtPZAvyvGeRiqkA__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Detected in webcam images** to view flagged images and timestamps.

4.  Select a flagged image to open it in full size.

5.  Verify whether a mobile phone or tablet is visible in the image.

To review the activity in detail, open **Session Replay**.

### Conversation detection in the code editor

Proctor Mode detects patterns where candidates type and delete content in the editor. This behavior may indicate external communication. The system flags such activity for review as potential external assistance.

**How to review**

![Deleted Code Analysis (AI Add-on) (1).gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776332069723-DeletedCodeAnalysis%2528AIAdd-on%2529%25281%2529.gif?Expires=253370764800&Signature=WG1Q3VKBk8-ADRL0Us0511UjWRhzMsduMgdIJvg8Pf5b5W7EE82oAvf3-52VihyT~UNGr4GHp-6yZrkaG87PFlfzV5Birab3ZQ1Mw2PyLcE4LIale5XiFdmgslYYr2j7a5zSIDbKj8eAkkYWzqUd-n3qFxZD0cpRmKhmas9Fl71vSWGG6Q~KbnU0KPcasvUkYcG3VKVqyCKnKYv~KeHIHhbULZ6y00QJBMxFuvLU-jf0q8fnyMJYwiIxio2ZPSajES~CGDOHZPX8-FX2zp4VtRQXIP9Edl3YjNh45PEYKrNTC8HPodPPCRCgWZzU2ZeCtciyN~ahfZemBfjb9L8OhA__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Detected conversation in code editor** to view the flagged time ranges and the duration for each instance.

4.  Select a flagged time range to open the **Session Replay**.

5.  Review the candidate’s typing activity during the flagged duration to identify potential external communication.

### High code similarity

HackerRank reviews the code submitted by the candidate to detect high similarity with another candidate’s submission. Proctor Mode flags a question when the candidate’s submission is highly similar to one or more other candidates’ solutions, indicating potential plagiarism.

**How to review**

![code similarity integrity.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769542222960-codesimilarityintegrity.gif?Expires=253370764800&Signature=H5Zbm8TXIXJni4tNUYJuJvtSjoeEtNp-~2zNgT2YfUsgLEpv6S5CLO88ndhB~Into4KSfiNOZ~x1qob~jlyUhBSSAiDX7VJplAc7kQgKdfmpUIMBYm0ikklHZPXEAnmjwo-OV115SmiJ8OOEsWezIu8RvHMzs0KCoJtf2qOU0vnA01cs0udeQdus3YbTYnwmn3HsbQZHqz-YodFyaqgSIzt3NGkCRbgIPsU~Wk0PAZhJHoXZFfuHNpwufcQOVaZWQzZZiSNiww4Rduxh6ktIRQ9IXtmjFRv4~lk1fbYwM2qJBIMQMLzzzsu624jrE3AWgurQpN8Ih9VgTLR69jDV3A__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open the **Summary Report** for the candidate.

2.  Go to **Integrity Summary**.

3.  Expand **Detected code similarity with other submissions** to view the affected question and the similarity percentage.

4.  Select the flagged item to open the side-by-side code comparison.

5.  Compare the submissions to determine whether the similarity is legitimate or suspicious.

6.  (Optional) Click **Go to Detailed Report** to review additional context.

\

\
