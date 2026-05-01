---
title: "Proctor Mode Enable Proctor Mode Proctor Mode compatibility How Proctor Mode works"
title_slug: "proctor-mode-enable-proctor-mode-proctor-mode-compatibility-how-proctor-mode-works"
source_url: "https://support.hackerrank.com/articles/5663779659-proctor-mode"
article_slug: "5663779659-proctor-mode"
last_updated_exact: "Apr 22, 2026, 10:12 AM"
last_updated_relative: "Last updated 4 days ago"
breadcrumbs:
  - "Screen"
  - "Test Integrity"
---

# Proctor Mode Enable Proctor Mode Proctor Mode compatibility How Proctor Mode works

_Last updated: Apr 22, 2026, 10:12 AM (Last updated 4 days ago)_

This feature is part of the AI Add-on. For more information, see [📄 HackerRank AI Add-on](/articles/5847651809).

Proctor Mode is an AI-powered feature that simulates live human proctoring to help ensure test integrity without the complexity of manual oversight. It monitors candidate behavior during remote technical assessments and provides detailed post-test reports to support fair, data-driven hiring decisions.

While traditional human proctoring offers strong integrity controls, it is difficult to scale. Proctor Mode delivers a scalable alternative by replicating human-like supervision across large candidate pools.

With Proctor Mode, you can:

- Set clear expectations upfront by showing candidates the test rules and guidelines before they begin.

- Monitor for violations during the test, including behaviors such as tab switching, use of unauthorized tools, face detection anomalies, object detection in the webcam feed, or conversation patterns in the code editor, and intervene when necessary.

- Review a smart, human-like test report that highlights integrity issues through a clear summary and an in-depth session replay with labeled screenshots and flagged events.

# Enable Proctor Mode

To use Proctor Mode in tests, you must enable it at both the **Company** level and the **Test** level.

To enable Proctor Mode:

## Step 1: Enable Proctor Mode in Company Settings

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to **Settings \> Test Settings**.

3.  In the **Test Integrity** section, turn on **Proctor Mode**.

    ![proctor new.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1753797455742-proctornew.png?Expires=253370764800&Signature=KYvvumEX4nTOEOK7EbIBvhXqjprx7W3~uXlc5~9VuWe~QK0kTGhiY07nToEJ-ByzBflSJmGDMZiZzAt9VZb-z2C-PbrV5~JaUbDd2Mdvm4bBf1j4Lh3m3aBhvNReWDUV5kA0D1YcehGUiNmX8LiRUvZV8F5KCrjpugLbl2-z8I9cV9N1po2WC~GajudBv7mFyv5m9OBYL0Hc1J0jtT9-3HqdgogpE6~D16pUcxTbHbaLt9zyH~jAjvlQm76dtgh4qg0x4LHqij6d9tZQQRnWqduzcqId6Q71WzsDHLL-gl4IO8Qbil79TLAu8LAoONPGa8AG2dEOAg-LvgcQhdRHng__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  In the confirmation dialog box, click **Agree & Enable**. 

5.  Click **Save Changes**.

## Step 2: Enable Proctor Mode at the test level

1.  Go to the **Tests** tab.

2.  Select the test you want to configure.

3.  Go to **Settings \> Test Integrity**.

4.  Turn on the **Proctor Mode** toggle.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1760279073731-image.png?Expires=253370764800&Signature=hTlWAetXhcR~KXneVidb9AqyyLRC8-j~DSpK869QtRm5s4~y-dSxqG0-15F7nB8S7Ne7S6h0z8PIl~sARQSqC7HSx-QoryHwJrDausUXgKkix56H~w1mT0BdDXkUzrXfTx7Ih4egC1JSOT5w3eyyA3NewDwh7inHIzH57AXwqBk1gGBCLVBJsqHgp1up5FhnXmCBQUDDDvOPxbjGdy-Sk5NPMWsXLQW5N0uY~a9DRAfQBsDEKjZ5iDCjjTt4fSBhh8~nUJdW0GY-1146Rqeb6SLxmi0NKu8ERtwInV72ERu4jp4UN9~0kAdzuw0vHiVm7SSGaAbwsMZuOqd0IcdaFQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Save Changes**.

**Note:** When Proctor Mode is enabled, **AI Plagiarism Detection** and **Image Analysis** are enabled by default. You can disable Image Analysis, but HackerRank recommends enabling it for full session integrity.

# Proctor Mode compatibility

Proctor Mode compatibility includes the following:

- **Availability:** Proctor Mode is available only for tests created after the July 2025 release. You cannot enable Proctor Mode for tests created before this release. If you used Proctor Mode during the limited availability phase, those tests continue to support it.

- **Supported question types:** Proctor Mode supports only the following question types: Coding, Approximate, Multiple Choice (MCQ), Database, Sentence Completion, Subjective, File Upload, Code Repo, Code Review, and Projects (excluding DevOps and Data Science).

<!-- -->

- **Locked setting:** After you publish a test and candidates start attempting it, you cannot disable Proctor Mode. To conduct the test without Proctor Mode, clone the original test and invite candidates to the new test.

# How Proctor Mode works

Proctor Mode replicates the stages of live proctoring through automated workflows before, during, and after the test session.

Proctor Mode simulates an ideal proctoring experience by focusing on the following areas:

## Before the test: Set rules and guidelines

Proctor Mode starts with an onboarding flow that prepares candidates and helps prevent integrity issues:

- **System compatibility and permissions:** Candidates must meet technical requirements for network stability, supported operating systems, and supported browsers. The test does not begin until all requirements are met.

- **Consent and test rules:** Candidates review and acknowledge a list of prohibited actions, such as switching tabs or using external tools, and must give consent to proceed.

- **Permissions:** Candidates must grant the following permissions to start the test:

  - **Webcam access:** Allows the system to monitor and record the candidate through the webcam during the test.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759320470404-image.png?Expires=253370764800&Signature=ASZeeYqKTKbLq4fbfW7u4rk2GF~o4wOUJis~SipyAxE8rvMwdSYrayVA-ekgmOWW8Utip5GFRjwU70n5fMy2Tkp6Z2oYWauarU7YjF6jkFSFn4uqj34x7jnbbJ0pMvSIrRD7yogquQc5hPOoNbgamqvYwJNZYQYp-wDbUf~NRAXklKO-C7FnwUU88i41smMUu2Uh5~y5vWpX~zs1caAdkbvbFK68M1P6bkJES8C860MSMhveWwcebRAwLJKQ0lu~sFccOKwpfwgjGw7S6DhJxnJJkgFwccF-nAd-9ui~Ph~d7tp-KjN1kftvuICrO~I13lZXjyGLfuqIouf~CZePag__&Key-Pair-Id=K3NV4LZ47N8M46)

  - **Multiple monitor check**: The system checks for multiple monitors. Candidates can continue only if a single monitor is in use.

    ![prnew1.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fa9fb2a1f-5561-4117-a905-779cb29b3089-1753798134441-prnew1.gif-14904339-900b-435f-8f2c-f46e684fd555?Expires=253370764800&Signature=HGktj4zbYkGWaO9A2nKfxfmm2Zhsy~iutyXr4zegxr24ADqvLVr91dvztvfTRbJb~sGzmBlL7rMnTyYyMEvCliTd6r8jbxNU2A1sHp6VRHiEcjz2VHmQRF~BeuiZu7iELOKH7zd3Fxvdg0cmyeTz-HB7G13hxUzSuL9rHv5cc5kQTp4JRU~x2SQ2CvjEWQt-V5IhvdLbwA9K1R9hiRzpYvZJIn9Iz~B6btER2h6xGi8CC4Nwewh9GYPwZlYXMmpssiRIbElk44KzqzA~3q00KKWz3At8cPCLpXC~OStE03OtIn1iYILt9jGcKyjYZr-VtY5sx-MdzIQbnUOsR3V9wg__&Key-Pair-Id=K3NV4LZ47N8M46)

  - **Screen sharing access:** Allows the system to monitor the candidate’s screen activity during the test and verify that no unauthorized applications or resources are being used.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759320620118-image.png?Expires=253370764800&Signature=Bna3geom6UGcdVWMOiG4~GduYI2T2EbguEXxqG7j47PHZ4lAMVnOTH9hQzR8fQ4BebHMRKJVKo1012o83PBC~wo5AcRlDm-vMDslHJzRyWoxMaJANTt289yxCjYfINY2jz3upKDA6QHekcE239fvYkOwofJ0aqkDiHlrHcFvEsB3WO-Wz5u39dwBa3FDghOim90XzEVnrd6F1PRCMPHKncBbth1nreOtpy1TqAUkv~4clFkPGZOulEPpXZQXDzqj3LYzs4fsTq~3KeXFcAimTxYOtMMQvTNULYr404ppZZkG8NRkK~utwp2AHyeusgngZW6THl6Xf4caTz-fq1gtpQ__&Key-Pair-Id=K3NV4LZ47N8M46)

  - **Full-screen mode:** The test launches in full-screen mode to reduce distractions and reinforce integrity.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759320398229-image.png?Expires=253370764800&Signature=nk0qNhxmRXu~Q8LEVMcGlpYkgwfzVkHLBNl4U6jaSvfiUSad13B7t6aCQkVig1q4ZFabPHJmCNkzIPNAK9FhfQk4na3xOZULKlfGL6MMXwZRng8JKNgg0rw147l973sTjhQLQGaGxAEnnCxee~sCcW1I2dYnIl6evwEYQaQGqNaJZXRuwjuLqEc09yg-yPrUJ8JujeETKTbrk0EIoVZCvXOPyVsU1cqDPWiKGkTqolmyKWMeFAeHaWk7Dnrz-IeNHYiK5iq7nCDQuX96lIOUzqo2ZwO5FG2YjuWoFzWs6HvRewqz1BX9hlqTsgU25EcJIG5f72QlnHNNhVdOj0NNfg__&Key-Pair-Id=K3NV4LZ47N8M46)

## During the test: Monitor in real time

Proctor Mode uses AI to monitor candidate behavior and flag suspicious actions in real time.

- **Full-screen enforcement and tab monitoring:** Attempts to exit full-screen mode or switch browser tabs are automatically flagged and logged.

  ![pr2.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1753798883688-pr2.gif?Expires=253370764800&Signature=OWaqzEOH0uTg14jdHHUjQiaCGlotGoUOYC29NHoA8ZMzBYB8xmXrGIDBb7xblrRNsx2-sJ56ssRN0SZl~mV579PX3veeh02IdMrd0s~09wkGEdr5nbHPjfPzsjE6hyUZ2h06klqb4fxcZLpOSYBOyundJ7MfcDn6gdOZNgGe4aCmLqbJbs9NgLnBmVW2w3dyYetrdN7JlPGHbW8-Xp8~f38FefrrP~GTkLrSeYzPKZhsU7EzLMthZjwpmbgzT0TYF6ze~ASoACIZ9Y9IEgl5GMRLLtgDCCKj6JfvSncZO80BFp5o-iQfuakd8ww9Mmr-4KV7TvBYH-eoeUv0cYXQGQ__&Key-Pair-Id=K3NV4LZ47N8M46)

- **Webcam monitoring:** AI continuously monitors candidate presence. If the candidate is not visible or multiple faces are detected, a warning appears and the event is recorded.

  ![pr3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1753798923367-pr3.png?Expires=253370764800&Signature=lO0K-pPOKs07sVeGoU~~YsdorR-t4U2bEvUMPLB0r-7k~rlV348S2oF7Cv-9Uq65Sx1VmjItjz-gfYeq9FXGmYpm4DD~-Rdk4UHahfzWgwW8QXdsnsQngYVCcc2yzQE0S0lo-C7jedbo6EDBaB~eD7om6vzaIwBctGd2e7iCPW9AjPfDK~Zkn8GBWp6xBKL2gkNnbLKvcfXiB1kQYy0J3u~nLSmYhYgV404KJsVZdg2KHTFAv3g2IrxVLWqpDtXzxNl07OTIZAx7SeMc3IpPFQzJ65BfZPDypxrdw8R2ieZ8KkW2HhqqEX6RIMB24nw13NqpGJrnlcJd~KTWZIzEjA__&Key-Pair-Id=K3NV4LZ47N8M46)

- **Object detection in webcam feed**: Detects and flags mobile phones and tablets in the candidate’s webcam feed. It captures images with the detected objects and adds them to the report for review.

- **Multiple monitor detection:** The platform continuously verifies that only one monitor remains connected. It flags any new monitor connections made during the test.

  ![prnew2.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1753798782242-prnew2.gif?Expires=253370764800&Signature=LVPhdKxx8W7R1SN3XaQX9-0S0Bv4Pp5eFuNQF3yHX7QwrbQ0Awid9E2WUSXp01sDjwU7zkENYrCSKTIEBqof4LcwCRLQXwxqbic2Hu4Q0fel6W14TtqXxRUXmnMVEZx1bKD1-gUxddMA8U9UBcm-SltTh-bHhBHwBp~gNIrDlh9IP~qVl0AZk68rCMpAs4cK7MKiJ2wkXqsym1LWDFAlAM2HP6HKMMepNR92SzS~PHySFQYpqucpCNiJu1DYaD7BNzE7fhpdoCDxfeQ9WZh2wbsNj-YFzYDjGfh-VdSY59jEZ4fKDrlVzlkt8t8YQyW15ucc-Wz50uXDEN5hbtJh5Q__&Key-Pair-Id=K3NV4LZ47N8M46)

- **Session screenshots:** Screenshots of the candidate’s system are captured periodically to detect unauthorized software or external resources.

- **Conversation detection in the code editor**: Detects patterns where candidates type and delete content in the editor that may indicate external communication. Such activity is flagged for review as potential external assistance.

- **Copy-paste restrictions:** Copy-paste functionality is disabled to prevent pasting content from external sources into the editor.

## After the test: Generate post-test integrity report

Proctor Mode generates summary and detailed reports that help you assess candidate behavior and overall test integrity.

### Summary report

The summary report offers a concise overview of the session, including:

- Indication of whether integrity issues occurred

- Integrity summary

### Integrity results

Proctor Mode assigns a final integrity result of **High** or **Medium** based on the severity of detected issues.

**Tests without candidate personal information**

When a test does not capture candidate personal information (such as webcam images), Proctor Mode evaluates integrity in the following three areas:

- **Proctor Mode rules**: Check whether a candidate violates Proctor Mode rules. For example, exiting full-screen mode, switching tabs, or leaving the test window.

- **Screenshots**: Reviews periodic screen captures for suspicious activity during the candidate session.

- **Code Similarity:** Compares the code submitted by a candidate with the code submitted by other candidates.

The **Integrity Summary** provides a consolidated view of all detected integrity signals for a candidate. It lets you preview issues and drill down into supporting evidence within the same section.

![test without webcam.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769513919844-testwithoutwebcam.gif?Expires=253370764800&Signature=JtXP9vwIhowgyaP3mS66VtQOmglq65glTR04mkGO7~iSDWnwANU89uGWDFPzRL-OY6U~PnnockjDyiYh0Y~z9Uzrlkg2l42oguuxp5lruqeWctweQoyzjb1rhUbBWuehNxMJRBLzf5ZY-uFxj-5duQdCrumoVnVpGLxXLwpmKCji2yXQkKMlvFi4FNBB3RXM7nIeBcLF69B4qF5Yors3CIcaffhfwsKghH2FhjaekRD8hUPupWj5a1e3WU-IpaGCUVj9P7~TtUWAm5YDNV3b7041F-smJSGUni~kL1qHvMMLz0XEQ2Fc2ZRS62nhGQ6YNGJzfs37ZoLFlhuNsqYKhw__&Key-Pair-Id=K3NV4LZ47N8M46)

The **Session Replay** provides a timeline-based, video-style view of the test session. It includes the following features:

![sr.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1776633958417-sr.gif?Expires=253370764800&Signature=LTue3GINZwddp0tJBwgSDzGByNaIiRKr4Ojic4q9eYrFTYWJy7pshLFG29cHTopn2gATAYANZ2rg8I7~htQXVAEa8lT8jlmM2AuVK3A~PpRbUL2eueQgljoGHb2rU-iFRJ9jzfO3oHI-hxbVgu1bJTaQMEukk8q0MQHR-ipa0rz9S0o8q2XF4lQrIIzvzl0EUpx5DcM73gj~jTdocfvyAUVpB~PK6nsyUbxZ0c6AaqDg3zwYL6V5Z1r~~HcY1-jGFx-zoehuQNbu6IhnfQPbpdU9rpTeZe3e8eb07Sz1dJTs0snosmu8ZzJYOfxilfnCJnvj5qFpO6QhFRrp2tpEcw__&Key-Pair-Id=K3NV4LZ47N8M46)

- Recording of the candidate’s test session across the full browser screen

- Lists all critical test events, including integrity events. You can search for events and click any event to jump to the corresponding timestamp in the recording.

- Displays a synchronized timeline with test activity and screenshots by timestamp.

- Analyzes screenshots automatically and highlights suspicious activity.

**Tests with candidate personal information**

When a test includes candidate personal information (such as webcam images), Proctor Mode evaluates the same three areas as **tests without candidate personal information** and also analyzes webcam images for potential violations, such as the candidate’s face missing for an extended period, multiple faces visible, or secondary faces detected.

The **Integrity Summary** provides a consolidated view of all detected integrity signals for a candidate, including issues detected in webcam analysis. It lets you preview issues and drill down into supporting evidence within the same section.

![test with webcam.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769513895832-testwithwebcam.gif?Expires=253370764800&Signature=g3q2F4hY1hCPs3AsFh3hhnjbgMtYKQ2ZR3iY~IggdmOUEXZFQdIW3XMGuf1iIPQQy4eg5e25Lgr6oomfWvZQVRzeqokkpOvqG3hX5oMsL3pogSr76Li-BdgMFk7U3dH4h7ZJX~fGH0VB5EkCm5v-7~FYC2OGNkvHmBaPY3LRX1HkkqmyI0UQCcNZHzTdFiyfA9dOh8vj0f0Dzz5qtB7avvbzNGn2DqT5tmk1AUtCOXnyQTZJRw~uzM7N~T8~olWqjPGk4LLTmrr1kSOX~Oaq97L1ewPEt0aP7JK4SDax00Bi7G7s8jS5-oModdwbjfJk~bJqBHYEF8QlGC0bhxbiHw__&Key-Pair-Id=K3NV4LZ47N8M46)

The **Session Replay** for these tests includes all the features available for **tests without candidate personal information**, along with the following additional capabilities:

- Captures webcam images every five seconds.

- Captures screenshots every 15 seconds and increases frequency around integrity violations to provide contextual evidence.

- Displays a synchronized timeline with webcam images.

**Note:**

- Proctor Mode uses **Screenshot Analysis** to examine captured images.

- For more information on how to review integrity issues in Proctor Mode, see [📄 Review Integrity Issues in Proctor Mode](/articles/9607697321).

### Screenshot analysis

The system prompts candidates to share their entire screen. The platform captures screenshots every 15 seconds. When the system detects suspicious activity such as window switching or exiting full-screen mode, it reduces the capture interval to five seconds.

The system uses a model to analyze screenshots and detect unauthorized tools, including:

- Tutorial websites, answer-sharing platforms, or GitHub repositories hosting leaked solutions.

- External AI coding assistants, such as third-party AI tools or copilots, not integrated within HackerRank’s IDE.

- Specialized browser extensions or invisible overlay applications that assist in answering coding questions.

- Collaboration tools, such as video conferencing, messaging, or remote desktop applications.

- Question-leaking tools, such as screen recorders or screenshot applications running in the background.

The system classifies each screenshot as **suspicious** or **not suspicious** and provides an explanation for any detected issues or tools. All suspicious screenshots appear highlighted in the Session Replay and on the candidate’s attempt timeline.
