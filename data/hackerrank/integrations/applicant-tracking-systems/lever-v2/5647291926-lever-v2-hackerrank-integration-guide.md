---
title: "Lever V2 - HackerRank Integration Guide Prerequisites Integrating Lever V2 for HackerRank tests Integrating Lever V2 for HackerRank interviews"
title_slug: "lever-v2-hackerrank-integration-guide-prerequisites-integrating-lever-v2-for-hackerrank-tests-integrating-lever-v2-for-hackerrank-interviews"
source_url: "https://support.hackerrank.com/articles/5647291926-lever-v2-hackerrank-integration-guide"
article_slug: "5647291926-lever-v2-hackerrank-integration-guide"
last_updated_exact: "Mar 12, 2026, 3:22 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Lever V2"
---

# Lever V2 - HackerRank Integration Guide Prerequisites Integrating Lever V2 for HackerRank tests Integrating Lever V2 for HackerRank interviews

_Last updated: Mar 12, 2026, 3:22 PM (Last updated 1 month ago)_

HackerRank integrates with Lever V2 to allow you to manage tests and interviews directly within your existing recruitment workflow.

With this integration, you can:

- Create and schedule HackerRank Tests and Interviews directly in Lever.

- Sync statuses, feedback, and scorecards automatically between Lever and HackerRank.

- Cancel or update tests and interviews in Lever and see those changes instantly reflected in HackerRank.

**Note:** This version replaces the [📄 Lever HackerRank Integration](/articles/1538275190)and removes the need for manual webhook configurations or redirect-based setup.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have admin access to your HackerRank for Work account.

- You have admin access to your Lever account.

- Your HackerRank login email address matches the email address associated with your Lever account.

- Your organization has an active Enterprise plan with HackerRank.

# Integrating Lever V2 for HackerRank tests

To integrate Lever V2 with HackerRank for tests:

## Step 1: Generate an API token in HackerRank

The integration API token allows Lever to connect securely with your HackerRank account.

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Click your profile icon in the upper-right corner and select **Settings**.

3.  Go to **Integrations \> Lever V2.**

4.  Click **Connect**.

5.  In the **Configuration** tab, click **Generate an API token**.

    ![lever v2 api generation.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F30246bb1-dcd6-4a33-b361-e28620d08d86-1773300139776-leverv2apigeneration.png-365a168b-806a-453c-8a52-10deb285ddd6?Expires=253370764800&Signature=lbF~BZgsnPJ73q1WO1lHhBgSwsbbjec4X4Pld0-1O3ExmDR61kXJUiZCzBbeEUM7Zi~jQEAhTn02BXeJQZXXafITtlNddjp6MXq188yy3NCBjv6iwdRBixSI3CZlvqqsRablUnsd9UeHlH4DfH7bnUBOYTP7VBrHixi2IjyGCEWEu~V8x-moHxPu0f9E3pgXD3giGUPHoEj6Pxc6bpljKgcjJw~d49cXUZF6GN6kRgXqGbFKHt3WZYrQJIdUhzcyO2cs86KjwjObJEvpRobgJUlePAJoVvOsnWY9--8W0jfnN4lsstYJRg9C5p4Ex5OocKvJvUNG-VcjU6YdcTsokw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Copy and close** to copy your token.

    **Note:** You need this token in Step 2: Add the HackerRank API token in Lever.

## Step 2: Add the HackerRank API token in Lever

This step authorizes Lever to connect with your HackerRank account.

1.  Log in to your Lever account using your credentials.

2.  Click your profile icon in the upper-right corner and select **Settings**.

3.  Go to **Integrations and API \> Partner Integrations**.

4.  Turn on the **HackerRank Test** toggle under the **Assessments** section.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F02d02e4e-ae1a-4008-b8eb-30183d82f51e-1773300404810-image.png-79c0aabb-c681-4403-a1a9-205726ba6798?Expires=253370764800&Signature=NRaoNAWLP-WtiZrq4eUWvC~XZD0suNdeHxtyBCdxbzQ1I-9Dc4dwzQrKnUyuQoiE4N~3UzU8hGxyBHKMjVpv12CfLnKliR6E0hgaMr5ZgeDC2akFPtGFOWcZjS4qJ~KqfjXvevPVjkIX6bDrHTwyUSL0812kiRbC3~qK5UE~ZFqOfumYt~biS62JqwQqKfcb1ocGhuBEl26tJtcnEldWS190MWGpnIpuOIDh19lXWsG3I71rSFYoL-4Mla1UBra9BRoKsKOLK7gikW7LzPClv6DBWcENC7hRyjXXNjwr4ATI~PezaYFdFLwyxnmzlN5Pe18JGdwWpRrH4rr5zA0kGg__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Paste the HackerRank API token into the **Access token** field.

6.  Click **Verify Connection**. Lever displays the status as **Verified** after the connection succeeds.

Your Lever account is now integrated with HackerRank to schedule tests.

# Integrating Lever V2 for HackerRank interviews

To integrate Lever V2 with HackerRank for interviews:

## Step 1: Generate an API key in Lever

The API key allows HackerRank to connect securely with your Lever account.

1.  Log in to your Lever account using your credentials.

2.  Click your profile icon in the upper-right corner and select **Settings**.

3.  Go to **Integrations and API \> API Credentials**.

4.  In the **Lever API credentials** section, click **Generate New Key**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fe37cbdbb-ac5d-414a-881a-aba0caa93aa7-1773300533063-image.png-687aa40f-f137-492d-9fd4-c2b62aff1eae?Expires=253370764800&Signature=fAwtSeXazj7vAgicm7rQ1cfKShfdkwO0lKWUMRs~oxjXLX5TqMGTy4cW9N46DyWXEIfeXUExudZBux7kDDWeFPshhmSK9S7Thw1SaApg7WxCIu6fmndFRzS-4Sl91EXCvjcBORRwHlazTAULJzI6c5wD0sTdp4i1LM8X8SA~oGxxKmHqKcN45RtF-77HgoB1SXnOz~3i5-Ww3ciQrrv5aNxJX43dvlcesNnI5HyLGG2tfZdQkBtWPLxXNgIba8io2eoYpL-igSojF9BGKX03uYHUOtwJLbHzdeCZlMdK1EmeIug0jpqO9nXWFpgJFiJEbl7DZQf-9Fk8RMJErDlJkw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Select the required permission listed below under **Permissions**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fa5d5e83e-7421-4ebe-928b-6f6e5926c0f6-1773300596965-image.png-580cc5b3-b4cf-487b-8f9f-a357bd8404ae?Expires=253370764800&Signature=M8Rf8qCV20jiBGs2Kr13LyD9FuM1yBg5BRHgwQZ9542HFdyfGR1pbOeJ2~EuzhTCUPb6WI1lgu0MuE3k0OLlOhhUiBzLwNuwTiFAvOn~ZC4-Tt2aH7IiliQC5Y6XukoieWnG9VzAQ6vkke1NCYFpQCr9FUR87yH~3T1613jo~rnfqHwDltMhGKlIGxyFbTtM05lM~hUL-tQv2sE7DdEk3k0APG9faINmp4OlKlebEDi1pLANykYtDS5UT8kXzKCfnY-8p-68DNdIqwIuIgrkdncDYhKTi-ho8sLf-XMMvKVYVOfWL6u9I4rZQoBljFdgIRJLfWjUwP-t32WZmhjD2Q__&Key-Pair-Id=K3NV4LZ47N8M46)![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F5ea97828-55c8-4faf-bdf9-83241378333d-1773300585141-image.png-a08b7565-3d51-4010-b007-584b35a9ccf0?Expires=253370764800&Signature=pBu69PKeYETR6kmM9QCkEJtyTWDP~kftMgFx3ZzYK5809JMX9T83goeN0J5VjT1y~7YVjtyfbkqLTPPB~CHiuvXrR-44M8wC0imCQDDunj~ssnvofyIgT1taRhYS4678qKM7rCmqug5XBc-fSEihNThKjw9zHEogsOrsefSjHvVEMcID-mWvoRraND-RFYedYuFzmletZ-2Lm4qvcIRb9SnQ8R3RutbJUZ61ybSUlcfyoq8jVDZH55haOhVg3AP5kODOU87WqKc0JlW8llXKpeHBH4MWwaD0-10BBvbpEly1uVFUAeQn~aeGMte7mHZPxYCyMne4~w8bzVhuhnrErw__&Key-Pair-Id=K3NV4LZ47N8M46)

    - **Read endpoints:**

      - **find an opportunity interview:** Retrieve interview details to sync interview status and updates.

      - **find an opportunity:** Retrieve candidate opportunity details for interview creation and feedback mapping.

      - **find all webhooks:** Retrieve existing webhooks to verify configuration.

      - **find all feedback templates:** Retrieve available feedback templates.

      - **find a feedback template:** Retrieve a specific feedback template for accurate feedback mapping.

    - **Write endpoints:**

      - **update an opportunity feedback form:** Update candidate feedback forms after interview feedback is given.

      - **update a feedback template:** Update an existing feedback template when required.

      - **remove opportunity contact links:** Remove interview links when an interview is deleted.

      - **delete a webhook:** Delete an existing webhook during integration updates or cleanup.

      - **create an opportunity feedback form:** Create and attach an interview feedback form to a candidate opportunity.

      - **create a feedback template:** Create a structured interviewer feedback template.

      - **add opportunity links:** Add interview and report links to a candidate opportunity.

      - **add a webhook:** Create a webhook to enable real-time updates between Lever and HackerRank.

6.  Enter a name in the **Key name** field under the **Confidential data access** section.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fda175f6f-74c1-4e4c-b916-9b2d59d3fe9b-1773300637411-image.png-752a80b1-566d-44cd-8bb4-634c19fb1119?Expires=253370764800&Signature=IDHbIfWpNACdNwefsCBOGETFAvDz2PxI~t13yX29LOI-nEJlwvDKrVHI6hEnB5f9~efyRHnZY9vjF7mU0A7pFryGyMnriiR0xasNEz2Ik8S9tOgPHDFfh4eMLyWAxrbLQDTmWgVn6pMAltpVs0Sk1cD7rUHXM9cWhiVmQgSk-JvR8TcOdJ9e3LifxSnSm9zcof6YOuUlF5QFL2kM-MqHzyuMUdBwFfgJ-0RcSj7kWW6a3s5BNnAiDcEcRo341CeGxhO1D7nehQg~CcIiTpjkWSJmT0LC795YNwYq1Xk5gmh0MEItzdHYFJJiTFlczEWRGpVSV9MQYvk~53gqRo8oJw__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Click **Generate Key**.

8.  Click **Copy Key** and store it securely. 

    **Note:** You need this token in Step 2: Add the Lever API Key in HackerRank.

## Step 2: Add the Lever API key in HackerRank

This step authorizes HackerRank to connect with your Lever account.

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Click your profile icon in the upper-right corner and select **Settings**.

3.  Go to **Integrations \> Lever V2.**

4.  In the **Configuration** tab, paste the Lever API key into the **Lever API Key** field.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F2e6c837f-ace1-4921-87d5-57475c868f18-1773300813053-image.png-974900c2-e2bf-4e28-9ad3-74e20390001d?Expires=253370764800&Signature=sPVF5YzC836y1-g2XahCH0MHzXlJHkKEpbpAmGPYHmvKilgWUblhj7XydhxcDWykNSUm2KNYNnoFwI-zt3uRw9iIZ1XUvN7NZDKe859rB2d~T0XVkdzMqF-jmj8XQWn8BfhsJmNbAq25BRVWnAxTs6d-HFrqzJBqvppGCWFT7pH6KVkiHwAx7INhcLjOkd0VW7Orj9Fp0IKGr~k-skDzhh9iNSJ0HjfbSHxrPzWXgeZ-KMWa6am3l-ee4ZxwId4G9fKrdsh4UWRPO0n9hnKsnVypH8cz6ehyaFExBDjWWFbm37DewZfpDsbGiwKqUplZsnCOlrjBKevJrlkCjQdvqQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Save**. A success message appears.

Your Lever account is now integrated with HackerRank to schedule HackerRank interviews.

**Note:** After you integrate HackerRank with Zapier, refer to the following user guides to create HackerRank assessments and interviews:

- [📄 Lever V2 - HackerRank Integration Test User Guide](/articles/6548604920)
  \
- [📄 Lever V2 - HackerRank Integration Interview User Guide](/articles/5269579148)
  \

\
