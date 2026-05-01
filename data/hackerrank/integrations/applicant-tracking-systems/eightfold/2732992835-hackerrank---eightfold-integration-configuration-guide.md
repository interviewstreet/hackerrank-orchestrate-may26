---
title: "HackerRank - Eightfold Integration Configuration Guide"
title_slug: "hackerrank-eightfold-integration-configuration-guide"
source_url: "https://support.hackerrank.com/articles/2732992835-hackerrank---eightfold-integration-configuration-guide"
article_slug: "2732992835-hackerrank---eightfold-integration-configuration-guide"
last_updated_exact: "Dec 15, 2024, 10:53 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Eightfold"
---

# HackerRank - Eightfold Integration Configuration Guide

_Last updated: Dec 15, 2024, 10:53 AM (Last updated 1 year ago)_

The HackerRank-Eightfold integration allows users to invite candidates to HackerRank tests and interviews directly from the Eightfold platform. After completing the tests or interviews, candidates’ scores and performance data are added to their Eightfold profiles. This article provides a step-by-step guide for configuring the integration.

#### **Prerequisites**

To configure the integration, ensure the following:

- **HackerRank Account**: You must have an Enterprise plan with a Recruiter license.

- **Admin Access**: Only users with Company Admin privileges can generate the API key required for integration.

- **HackerRank Tests**: The tests must be created and published using the same Company Admin credentials for access in Eightfold.

- **Eightfold Access**: You must have access to the Admin Console and App Configuration pages on the Eightfold platform.

## Steps to Configure the HackerRank-Eightfold Integration

### Step 1: Generate an API Key from HackerRank

1.  Log in to **HackerRank for Work** using your Company Admin credentials.

2.  **Go to the Home Page**, and click the drop-down menu next to your user icon in the top-right corner.

3.  Click on **Settings**.

4.  In the left pane, select **Integrations**.

5.  Scroll down, locate the **Eightfold** option, and click on +**Connect**. Alternatively, you can use the search bar to find it.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734240233344-?Expires=253370764800&amp;Signature=OabsC8PxQSFTCOe6mSL~4wH0podydU9oYeosOUhVKlzNzKuFopa01DAa5i3tnuYirDhgtxzbwmArc7a9DENyY92~c11M1i3Mc9H-l3OAAQXUG0R~oJyEsiirSlBBvbwffvEd1SSbcvIkTvscJTiCE66lOvhnL8O7tTKApCbWWtPEjxjgspBl64iLz5A~kGl-MUabrMVY0RheenRXapEshCOCdFa7R-~tVrziMVbK8mlgFJgOor5JZ7naPpt6GiY8KgRyWVrQhYpS5H9mAuU17FD67hb3oj2VSL1i1kyEPReVfSb4kPXQ2BLUDq6~bTJCLwb78ko6~5F0i2WruYyorQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

6.  Click **Generate API Token** to get a unique API key. Securely save this key, as you will need it for integration**.** It cannot be retrieved after closing the pop-up.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734240233866-?Expires=253370764800&amp;Signature=K6o99cCHUz4nXqGzdk3swtJ0FPoUcy~o3uH~CLFDfoHA2hw9K~Z5iCdZSZSGQl9OXZP~2RMzzVAUXdShqNfoV3eXW8k0ulewSUaLdJtIkDnJyyxnumtwgzomog4GX7F3GqVJ~0aIIaNtFMAFxJSlzqxQedtma1rCNMr1~PUtqptV5DPUTaDetEt3SZCoXVYTNPIvKL-1ibxoJBb4Mj6lCyMtXMVFEVOQVwFcti1XJ--9wy7GmcWXTEneiYYLSrf-YQzPEbAu5O8EL15oEuca1VmNgWDDLWVSZkuuxQ0dJ6MBt2M~xEfjyAKfsVGtyd~eu-iaEHjt8sZZlvRciP89TQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Note**: You cannot recover the API key after closing the dialog, so store it in a safe place.

### Step 2: Add the API Key to the Eightfold Platform

1.  Log in to **Eightfold**, and go to the **Admin Console** from the More menu.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734240234277-?Expires=253370764800&amp;Signature=VaGv-ThOosOVJuP36Zcz1MbTTzVoPdQzGeNGr5Zo~TbhChsI090V4DiqBgMNeBBnj5SB43d~ZvZ2TKcdLmcsrHpl2nJea9rl2k6rILvSBBEb-K3C7I13hW0SUXJUe3BbJJQZQfuOhNV0Oys-kQpB1XpB-7AY~N7StzV8aNgNxGFKNqoBquHi-8Ch~JtUUPJy0qRkLz~~UM~zQKrZ8NJ3izDB6HlbvheZsVGghR3ZKklKWMLVqXGNm5i~3uCdAUkvDBSfd6iFymh23iowfKMMAwD-dzUXNm~ad8IYOAcfjFPAsQyxd4RziFzq-8Z1n5~sX3e8KOrx1f1z0Yo1P1bC5w__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

2.  Select **Apps**, and then open the **App Marketplace**.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734240234637-?Expires=253370764800&amp;Signature=LjpakdGm1kZce2NxhNeNx8dyJdYLpXL7C6P1815jgHqU2qAaSSD0AfpwJmnz8o5RjjTjmn4zIT958Wym-Q7hfKYRhQC-sylJYgTJvxj8mhHiTSejXmHwCJwXE4IsVugtNz2ugji0b6FYNxlx8ArAdn91JX3COhsbIS4vXEhrSNKbnXwoMEuAM2CP~xj-uJdZMxcLw7hl3qMOMbA81QMi-mI9XygQnEWD8u2FKFTwp2Am4vu6sdDeMQ0p4tgKA4uqxyAoAbYuzrpCZtIYZksDt5wu2AOywAZXw6O4iTCObUHij-nHzIEQ6rGpES5Kl2inQ51OUI-CI0~SVD~8u21HJA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

3.  Search for **HackerRank - Assessments & Interviews**, and open the app installation page.

4.  Click **Install**.

5.  In the **Configure Settings to Install App** window, enter the **API Key** generated from the HackerRank platform.

6.  Enter the appropriate **Stage** for the app (e.g., **Recruiter Screen**).

7.  Set the **Webhook Authentication Type** to **no_auth** to receive notifications on HackerRank assessments and interviews.

8.  Click **Save Settings & Install**.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734240235092-?Expires=253370764800&amp;Signature=X9JAj5K4LRrBNgH4fjWOoICv2Qoc4XiJQ-E2uk70cBGedT~RZOTuj8DngMmQaBGfkSqdVyzbF5bWlPN~iAr0JdffXDs3~jpL2fl3Db4IzPDzWao6lhvU1jBKASE8ad0jk-uAWcg7Q1tULtaaPt6FQcI-GSwAGZl0ejH3FcAeNj3ieMEDpU2xOG6bb848eLR2aDMtHSeS~43~JO6IjfTn736F4idTYE4qtFmrfFWxTAt7s68-SDIG580rYycDZq4Va2JrUs4mvX7YPLWYlNlPapuLgDiUqy3H7M2z0bvuEWCpqIcXi1Dtb-AYREgdWvd4nt1JCX2ylNmvr5Zw2YMRKg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

9.  To verify, go to **Apps** \> **Installed Apps** to see the **HackerRank - Assessments & Interviews** app listed.

**Tip**: Click the app name to check and update the **Configure Settings** if needed.
