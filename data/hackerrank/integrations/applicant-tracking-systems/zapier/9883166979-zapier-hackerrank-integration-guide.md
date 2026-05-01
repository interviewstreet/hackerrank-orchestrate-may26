---
title: "Zapier - HackerRank Integration Guide Prerequisites Integrating Zapier with HackerRank"
title_slug: "zapier-hackerrank-integration-guide-prerequisites-integrating-zapier-with-hackerrank"
source_url: "https://support.hackerrank.com/articles/9883166979-zapier-hackerrank-integration-guide"
article_slug: "9883166979-zapier-hackerrank-integration-guide"
last_updated_exact: "Jan 30, 2026, 12:26 PM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Zapier"
---

# Zapier - HackerRank Integration Guide Prerequisites Integrating Zapier with HackerRank

_Last updated: Jan 30, 2026, 12:26 PM (Last updated 3 months ago)_

The Zapier-HackerRank integration lets you connect HackerRank with Zapier to automate workflows between HackerRank and other applications. 

This integration enables non-technical users to create no-code automations that sync HackerRank events, such as assessments and interviews, with third-party tools such as Airtable.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have admin access to your HackerRank and Zapier accounts.

- Your organization has an active Enterprise plan with HackerRank.

# Integrating Zapier with HackerRank

To integrate Zapier with HackerRank:

## Step 1: Generate an integration API token in HackerRank

The integration [](https://support.hackerrank.com/articles/1406188460-greenhouse---hackerrank-integration-guide#glossary-11) API token allows Zapier to connect securely with your HackerRank account.

1.  Log in to your HackerRank account using your credentials.

2.  Go to **Settings \> Integrations \> Zapier \> Connect,** or open the [Zapier integration](https://www.hackerrank.com/work/settings/integrations/zapier/configuration) page directly.

3.  In the **Configuration** tab, click **Generate an API Token.**

    ![1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769057081494-1.png?Expires=253370764800&Signature=Rn-yBW-ANMykkkEmXc1CEbn7G~aQfx9Cxj~6Vve3g0UhxaDEuU-wKsGJwh9XCgJXH7pZ6762taOPWiX8TzdbroGrUDdhm69cOsv5J46MSdtdnstDGKBghcgpchrQ6bRlMS71nespKrgcEuZhQG2GaDdsXN2c90wtthJMGSGBbLorxoikrE5dLh~s4rwtXYxHtPLDqDcVrpjG4QROGImmHgz-PespLvf5p2PY4XbC1ovqjtxo3BKUqbodl0L4hWNRrDfQqfm7xBPRDySL6RAcJS6TA8oHmLfP~uLSbpYxErivJqyC-V1U5nsU739MAgwOS14Q7Yg~B5-imUeCLt-Avw__&Key-Pair-Id=K3NV4LZ47N8M46)

<!-- -->

1.  Click **Copy and close** to copy your token.

**Note:** You need this token to complete Step 2.

## Step 2: Add the HackerRank API token in Zapier

This step authorizes Zapier to connect with your HackerRank account.

1.  Log in to your Zapier account using your credentials.

2.  Select **App Connections** from the left pane.

3.  Click **+ Add Connection**.

    ![2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769057106427-2.png?Expires=253370764800&Signature=Bqd2ULJ~3rKUr4V-sxGWPpYek4KJBU5NC456gT3S7A6Kpg5I4UF1KmHWz3osiMP~Geo2oYTZNXKlzMmbU70HhRcRajQYhkGZpnjZwBzCFa6j0loVK-wpwM3PPWrvuC05v0pxh-vSVIG787JMf7pv0SXDK-xYJmkvuB2ASPznq8WEawjJftJWega44UnOqtVoA58fq2nP9GPADvGPvx6Jfoum30BM5kmwVBLXbfcumDuwC2r3q7-BgyXyb6usEMqH5OJpF924GwI59FXcrj60ePuau4mrR50Hq18nWqw02xjYbRO8gsnsJeJRefDHvsLzOs7KuNpCLuC~pCAWeS~g-w__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  In the **Add new connection** dialog, search for **HackerRank**, and then select it.

    ![3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769057127083-3.png?Expires=253370764800&Signature=Kitt12qkZ~gGZiGMbMq1WLUgfZHT00LA0aEtoHiFtn0FboE336SA3mLPmTKDkqYOCr57QFpDIo-R23~djrC3J1ztiyFPH3WPvXU~t1zf9A4p7GRFvM7lbCrGdEoaDgB2iN~vEUzAvS3fvx4695vn7jbmGphyOilxG9UtSpIkl6J6CZkwNZ86g7gfrxRmNSKUBVUpM8EItqA2grVI2i3Mo8uWzV4fi7WUcAjPPIoM3RI-ZQJ0~omHY7W0V56-Oi7V5iDgaHGdfAx605Ykz2-36T4XvZ6uC9bA8k7AKHaGWNSaFn-WO1ekUZVa6asfOVT7YWvX38UxDCDxzHaZdNOXSw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Add Connection**.

6.  In the **Connect an Account** window:

    ![4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769057135350-4.png?Expires=253370764800&Signature=KCaBFU4vMBqDAMaGYjzMg5nKuo0fMyMPi6KxH7H~wALDs3EfwjcHJ1g-Wl5VWzV2cKFmZJrowTo1lOeAY3~M1b2uGtWwGsslIpYeWd42FxWk2rjqGEwaQw2ZtmJ0aCX2EH50Az5eJ5WSaigIP4xpRNNZG~JCRgPPrIi1ROyMvh1deIMS-c9SA7sRmq9jaJWg9c0IcMFXpjWnAaJE6dCjX44VSqI6~6nmcmNDcgTsc0auyJhv32-1Xhx4zciBa-cLU7Vho8bBitptKz83UXk1k1HFv7Kwnrub0O0bGczDvhAY5Xj8Dh9Zjf45uXLwtP59iuINbuUGDHp00qF99eYNnw__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Paste the HackerRank API token from Step 1 into the **HackerRank API Token** field.

    2.  Enter the email address associated with your HackerRank account into the **User Email** field.

7.  Click **Yes. Continue to HackerRank**.

Your Zapier account is now integrated with HackerRank.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769057297274-image.png?Expires=253370764800&Signature=NZXiA3kJ7aOPbbEz3Cj9gMGggkj4EibvmVOsItPGmm5IG4t7zZ8HAvL5e7USBIwxuSlnLrrU77YLVQMWGWBfZ03oU3OzOAYbRrgd7BdpnDcNADiRfPM4JOEyRPwAQUDXYbfIo0MzDPTQl96dYTxjjEW18zkJS8xhQsJXqY15Sk1Q2uJGMy93JCU5uUWe1VkYlUutIsbVp~~4fSCtJN92XqrvCa39Pq468C8lVbYIOPuY8PY-dNX3muQndvDYWef7r9GYq5uw5sVLznEJ122xy-anJM4M1~hyoKTs6KclPPUA2DrG51g4UmDWr6datz~GgpXXlp7lnagasGw3UkUIbQ__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** After you integrate HackerRank with Zapier, refer to the following user guides to create workflows for HackerRank assessments and interviews:

- [📄 Zapier - HackerRank Integration Test User Guide](/articles/7100809601)
  \
- [📄 Zapier - HackerRank Integration Interview User Guide](/articles/5179178131)
  \

\
\

\
