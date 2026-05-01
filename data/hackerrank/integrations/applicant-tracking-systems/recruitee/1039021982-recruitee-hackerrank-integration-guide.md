---
title: "Recruitee - HackerRank Integration Guide Prerequisites Integrating Recruitee with HackerRank"
title_slug: "recruitee-hackerrank-integration-guide-prerequisites-integrating-recruitee-with-hackerrank"
source_url: "https://support.hackerrank.com/articles/1039021982-recruitee-hackerrank-integration-guide"
article_slug: "1039021982-recruitee-hackerrank-integration-guide"
last_updated_exact: "Jan 30, 2026, 12:26 PM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Recruitee"
---

# Recruitee - HackerRank Integration Guide Prerequisites Integrating Recruitee with HackerRank

_Last updated: Jan 30, 2026, 12:26 PM (Last updated 3 months ago)_

HackerRank integrates with Recruitee to let you invite candidates to HackerRank assessments and interviews directly from Recruitee.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have admin access to your HackerRank and Recruitee accounts.

- Your organization has an active Enterprise plan with HackerRank.

# Integrating Recruitee with HackerRank

To integrate Recruitee with HackerRank:

## Step 1: Generate an integration API token in HackerRank

The integration API token allows Recruitee to connect securely with your HackerRank account.

1.  Log in to your HackerRank account using your credentials.

2.  Go to **Settings \> Integrations \> Recruitee \> Connect**, or open the [Recruitee integration](https://www.hackerrank.com/work/settings/integrations/recruitee/configuration) page directly.

3.  In the Configuration tab, click **Generate an API Token.**

    ![Recruitee integration.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769699679380-Recruiteeintegration.png?Expires=253370764800&Signature=lqWGSqz~vXoSL7oFrZtjMe-IwD1raenFF-mNMsfcqhNJH4Bw7c535iJOf~Ffgpni2uuWXYCkw1Im59jui6zJxNQVffh1hFI~tH7lsFJI~B1vvWH4fPcW5Iq6ZEUn9jNyDfwzsD6OH0h6PXvrtE6JAFT6FplJBeRwe6sGxxDhfQbx1iWbsdnlSXZMLQcxKcpz8TljD4tNrD2mamixsiRiKfFEwuvgUWak8ndvdqf12R~w6YUiG5ThamSzdv4~XhIDUfR2g36jMYuAYxQz4sPxbon1giC7zoV~FfGIIWP8JoHrBEZNVe5Xxv4Ak~jr~R7mKfAhndIbO7MShOdsmJ9MOg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Copy and close** to copy your token.

    **Note:** You need this token in Step 2: Add the HackerRank API token in Recruitee.

## Step 2: Add the HackerRank API token in Recruitee

This step authorizes Recruitee to connect with your HackerRank account. 

1.  Log in to your Recruitee account using your credentials.

2.  Go to [Marketplace &gt; Categories &gt; Assessments](https://app.recruitee.com/#/marketplace/categories/assessment).

3.  Select **HackerRank**.

    ![Recruitee 1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769754809473-Recruitee1.png?Expires=253370764800&Signature=NMaQ2KYuyJoOxdIuToK2CqVqpxWPIxGEV9zWsSD2HOhOvspK~IV6pPEJvSOL83XGLfPgBjgWeVgYKRGvGPGsYXB30d8rWDU-GmX2fVWkLdUmtJTmqA99bIqIT9U6s4EXuZ-uXxaEoRbjWc2-eLjb-Qhh-oJzdO9FXUE1RxvULQitw3LfPsYx7e6q4kn4cSXHMDhxHCmAh2VzHovy9DnNM5fvhe9bwEbxtj4hf~t3IqUkzZdnlvBffihcifdFN41RmR8qbx5FexU2oEDnxYygRlXGFNdPg6yfG8k0bztWqQiXlgZkTO1v7fuTFcwAzLkG2YATVeAaJPNOCavKfdxI-Q__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Accept and integrate**.

5.  In the **API Key** field, paste the API token generated in Step 1.

6.  Click **Integrate**.

Your Recruitee account is now integrated with HackerRank.

![Recruitee last but one.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769700303053-Recruiteelastbutone.png?Expires=253370764800&Signature=H4Na1nGR4XbAe7nO-r9RWLZZ7sZw8MPvBaUtzUzBuX2lPwb0afXYSaL5EjiFhtGI2SLGSMO-6rbiUfJ9Uel2iLQhDnniEkN6IK~H8wenLLbrsojXbcfLikmgaaNkV-kXh1d6upUSus79QwPCl5W3-fVHEqcw0mmd4lRnltRuhbLzl8xiSHF7TUJe2NGquXT58J-LJbp4YSGS10H8IrGSzGZwNGOoVI73g-KG9Dy5m83GbKkOrobbBUCG0-tihLraSvl-6LFYjVu6lWDfRf7PRs1OzhxgBsMwcnb7yVYDOCvqPBBDQJJR9x2FZj2jYR-p~HlxRK4VEgsKHa7OWKT5GA__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** Click **Manage** to control role-based access for viewing and sending tests, or to remove the integration.

![Recruitee last.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769700369302-Recruiteelast.png?Expires=253370764800&Signature=rWjMYFAIgoz7bsm8il~PVj6bwJhbG2bTktEX8tnODKWVc-9mQeS8hu0odLyKOeACce1EqwrlGQiuAVuClMkK7Lf7qT6M0USJU2hDNTN8aEK7gbdiIo-FBGFEpwK4ZuGKapJMAMReLCOTgMrUHoeJz3QBIw3hzKF5z9KXC2uZsY2A7JzT7m1qdF2xuN8CcbzPTwrueGfugP3NACrrG7dSpOPlGb0Mhmj-aA1M04YBurxGrtGi3xt7ZJ0w6oBiKZX-nc5UkRj8HhzQI3RrreEvag3CCiPl-K3huWutWAlXvbWcLq0So0mwf1hG2scn9ccDM-AwyMbLJBikqT0FHP1HcQ__&Key-Pair-Id=K3NV4LZ47N8M46)

\
