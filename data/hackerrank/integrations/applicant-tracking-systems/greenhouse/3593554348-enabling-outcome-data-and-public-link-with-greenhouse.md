---
title: "Enabling Outcome Data and Public Link with Greenhouse"
title_slug: "enabling-outcome-data-and-public-link-with-greenhouse"
source_url: "https://support.hackerrank.com/articles/3593554348-enabling-outcome-data-and-public-link-with-greenhouse"
article_slug: "3593554348-enabling-outcome-data-and-public-link-with-greenhouse"
last_updated_exact: "Dec 28, 2024, 5:01 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Greenhouse"
---

# Enabling Outcome Data and Public Link with Greenhouse

_Last updated: Dec 28, 2024, 5:01 AM (Last updated 1 year ago)_

## Overview

A HackerRank Public Link helps you assess a candidate's skills before they even enter your ATS system. With this feature, any candidates with the link can take the test without having to be invited. If you are a Greenhouse user then after taking an assessment from a public link, a candidate profile will be automatically created within your Greenhouse account. 

You can map your test to a particular job on Greenhouse and obtain detailed candidate test reports for that job role whenever a candidate attempts the test on HackerRank.

What’s more, with HackerRank’s **Test Health Dashboard,** you can now get a full view of your complete conversion funnel, right from the initial invite and engagement through **who finally received an offer.**

## Importance of Outcome Data

A high score on a test does not always mean a hire. This is where the data through the test invite to offer (outcome data) come in handy. If you knew what scores were given to the candidates who made it through, it might throw extra light on the difficulty level of the test.

Outcome Data also helps you understand how efficient your hiring funnel is and the ratio of the candidates you invite for a test to candidates that you hire.

![THD_Updated.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047207846-?Expires=253370764800&Signature=LWnI5P6BRjtIw3o4LD9BvhJAuEelIZN~JiACxZacRclE4bZV0sFPl4Q0wXzoklPEyThntGHdtMdagNEVEAfTJwnql4Ovlxz2H7tm1fLQwEUx0PwQvBbP77Xz0H7l5C2BVnL~dSb6Eb0ZxRa2rE3wO9XVsjhtKVcaR2ReF3tDrD9KQYbwAE5gbTnRIT9gnbUQ0jiRe8eZ1x-PckvANNqVQuYGozhTBWmlpAKe9ZzzuSV4wdFG~I0wyBGsZmi-VVh0ECcLO6Wg0cUTj8uWOTI1-Qm2tOSPmtXBdSal-YI9euliQvPlnqNHFBRrnOTt7oFVRbS5iAy0EHP368mwlg9FiQ__&Key-Pair-Id=K3NV4LZ47N8M46)

When Outcome Data is not enabled for your account, the candidate performance funnel in your test health dashboard looks like the below image.

![Candidate_Performance_Funnel.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047208227-?Expires=253370764800&Signature=dXS12I0Qg5ko79eiHZNsaKWXGy2t2DccOy3xA-vrMU-7phauJSCKX51fKWw3ekTqPWdfsWm24WK6EzhcIPs53Ti-gtpGjlawRoWEyYk-oSgoyWAPHH5qK8alqIW7RbHa~T0IR1S43N2GGJcpXhjwEdMKbAJ-8TXKsxnLAM1u1sKyGE1-6yWTtT9mi1DV-QJqtVVyQwoLpXUi93uszYYOD8DG7Rulj-umuwVgaV-A1UCHUiy4lnDcfKeDjpGlgHkyXe97y23Z~DnB1aH6QHSUHFE4oyE93oW2is0MuCERkWJhjbc1ttEmFW9vCPqrELlqbzTvztGmrsxcbU1HaX9xsA__&Key-Pair-Id=K3NV4LZ47N8M46)

If you are a Greenhouse customer, you can unlock the offered stage by providing HackerRank with your outcome data through an automated connection to your ATS.

## Enabling Outcome Data and Public Link for Greenhouse 

**Prerequisites**

- An Active Integration with Greenhouse - or you can set it up from here:[📄 Greenhouse - HackerRank Integration](/articles/2646010908)
  \

- Company Administrator access for HackerRank - you need to be able to see [the ATS integrations page](https://www.hackerrank.com/work/settings/api)

- Administrator access for Greenhouse - you need to have access to [the API Settings tab](https://app.greenhouse.io/configure/dev_center/credentials)

**Steps**

#### Inside Greenhouse

- Open the **Settings** tab and go to **API Credential Management.**

  ![API_Credential_Management.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047208557-?Expires=253370764800&Signature=MfkEvAgtwF0MqpQdk0Y~~tlESLk82xxyekv6fdUOE7-STJFoF7zJYlUGFefVLj0vn9N8TImYx5gVU5ZxG9gNdgppq6MssGv0FJSPGBWtQ20k2p7tT1hIiBQQ~rZzvpjy9mBg4SoUWegHtoWfw5iz9lizCQxj~gj7-mtWdg98--E-nHjbgsMkiJjGV60T6sgnd97iOv3zgs5L1uBeQ2hLc~qjekAyEerSQtaMDIKf8CWPoTGavzTUnIHmZz30usEBadnzhAyDsfChpHukq4ubq8U9a~RMyqBKz92pBCO1WmqFcyIn3Na4JvqNWEWacKS-Jc92x48TK2Zi3gXNYeE-Rg__&Key-Pair-Id=K3NV4LZ47N8M46)

  \

- Click **Create a New API Key.**

  ![Create_New_API_Key.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047208950-?Expires=253370764800&Signature=qO6pp-YoifGKsMvUytjxzjj34A0MAz8kok6tKGb5grESZbtXa9JSI2Fa32E0RAjIfcE17Dejf31wp~Lr1Gd5PscXwAdImVtBQ8e53fc4DktC7BwJbJfJq4HGs4jyONPfdhXjaAPhJbVwjBV0GuhRZ4sRsrfaa6Y9RwpavEVGrDk7Zgky7DnRX1YFgxBlIR2e28nYMnhMzWGERORzkJJyiZ0j94z33jBIFST1VlsaW2rIGV3bw86-2jGJOVGsSKT6y8GmsGM1ciezsSAV2XR-vHouBUJgrBDqVwW5oNsi1C0DHGk4k28b7IJ2qPTuQiIfo92bYtNRKu-LFGq4nbqfKA__&Key-Pair-Id=K3NV4LZ47N8M46)

  \

- Enter key name, choose Harvest Key, and create the key.

  ![Create_New_Credentials.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047209289-?Expires=253370764800&Signature=F5baogiUnXrRS2brsHBAgLYwtXq7n61F19io2VTM8hVx4~wbSt6mY2A~Kx0iXq7NlkDayrgahMwPjg19RrffN5mnIrBJfR7jYxfIVLXb3YlKYnVOWmHoibSaZfScNYBjaf3B8FLcxaAq1rwxHvBk~rn8QP38ty9MdvuqsVJoIiQcwRHl3kQtECY3JfJP5KE2EtkMdVm-fMdBxN9pKPWKg-q0KlJcwxP4rzHpNetP4riE-gos7HKG7RgkQ4e56wMSCdbf7MO1Vtlg5Sxp4Z8kDg0XK1pRKKeoXHyEUC2E3zkJwFAl1G7-BD9K0NqrDbd9XIz3eKuoZ2HmXjo0qrvuKQ__&Key-Pair-Id=K3NV4LZ47N8M46)

  \

- For Outcome Data, choose the following permissions:\
  Under “Applications”\
  GET: Retrieve Application\
  GET: List Applications\
  \

- For Public Link, choose the following permissions:

  Under “Candidates”\
  POST: Add Attachment\
  POST: Add Note\
  \
  Under “Departments”\
  GET: Retrieve Department

  \
  Under “Jobs”\
  GET: List Jobs\
  \
  Under “Tags” - *all permissions*\
  POST: Add New Candidate Tags\
  DELETE: Remove Tag from Candidate\
  GET: List Tags Applied to Candidate\
  GET: List Candidate Tags\
  PUT: Add a Candidate Tag\
  DELETE: Remove Candidate Tags

         Under “Users”\
         GET: List Users

- Don’t forget to click Update to save the permissions.

  ![Permissions.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047209686-?Expires=253370764800&Signature=IYz-KeUxtYnQxw1Io0JCA1wkd9PRXnEnMLgwW-NNpAhopRwqrHPdOLGEfned7-anAkL9S7lEsudkBIrzVhZWp~CQFjhPK4QOOXm6uyXsl4eSR9XQVrDWLl23UKO6n1eYNCQdBKbtAwlwj0FLPzKrmU0hq5t8DFfjpJCxL1Qww6bgqlCLYmaEnzk0KaeSQ7pk4k7TvGiUGz4-~eaELjm~xvldbuWddVNvIKx6ly9cWnDv8GoBbMhxG3-FfOW9yPs2il1PSeIjmZamr196pX0TKXLJeq8UoRJp-Oj3jPh42w-Y7JQ2EoDfI2fyYIC13rNWzC3q7eABpFjx6KFEJ57hTA__&Key-Pair-Id=K3NV4LZ47N8M46)

  \

#### Inside HackerRank

- Go to **HackerRank ATS Settings** page for Greenhouse Settings\>ATS Integrations\>Greenhouse

- In the Greenhouse API Key step, enter the Harvest API token you created on Greenhouse, and click **Save**.

  ![Greenhouse_API_KEy.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047210113-?Expires=253370764800&Signature=qCHAwAXRlFlUV~QCaeUuglvL7vHivAgLfS9g-z7GKXuSN-b3vAyv5y6rZQVKTP6U1MZNx5Syc1k4l9Hv9gRue2CC7KVjVRYKwDeOnR2OMkCiWaibnq7bsuOhCHQ5OfEjNo~LwY4auAhyk~VFwd6EJ8GIQ2nxWOvsBsCSWvqDlrspAPQJyqTQL3DcyETmLePszcR6sp53pC2vXl-O-0Li9qaUQ-H9SUVJDkvH~QMJdlqGKxjBibRCTGePk96PBn8QzfOVkaeMd69ZdftmJe0j4fkxCLen7Uqoq3d~9TOql~SF0HIF5cFZ4Utfl5o-bjFzPXvrgMMG2PssF7gIasDHUA__&Key-Pair-Id=K3NV4LZ47N8M46)

#### For Outcome Data

- In the **Candidate benchmarking and test outcome** section, select **Sync Outcome Data**.

- Once done, it will verify the permissions for the key and if everything goes well, you will see the green check box.

  ![Candidate_Benchmarking.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047210480-?Expires=253370764800&Signature=HczMH85X02nR1HQPVs0VsW5ldsMrdwGFoN1-dMREaMeSEnyRQ79jK~~GVf3qQ2-YjqPqdt2zqJLSnGAuHANqn0XMsVuXavsWvmsa9tee1386JKYRnf8Rn6J~MhmKuoHKnD6SG7DIhQdTO1-sWvDPt6RIYfhL5xl6KpxnZELUFj6lwrocyYnX0Z-EqhuFkwI~NCCa~tqvcq93h7sYKmZl2DsJ-PUx6aA02Zlo5M7SacSLUuavhIs3kRL3Ira4EMv6iZF1XRV1KJXyaizQKo5jIrU4uZpIb0osIQ13lPI-~fV6JT79VL0Qi4NYkILgluWVz5GYpMXwFimGQSlOlx1uTA__&Key-Pair-Id=K3NV4LZ47N8M46)

- In case your key is missing permissions, you will see an error message. In this case, go back to Greenhouse and enable proper permissions for Outcome Data then come back and click “Try Again”

  ![Candidate_Benchmarking_Try_Again.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047210779-?Expires=253370764800&Signature=EBWc4tzFTIufZWnj2eyX6wzEU73E1xO6LbL28qHpaMbyqpK9iDAu4gkOQBT-tpuEyYcbdBnWa9VRsfHReeSEJyzkMqu9JvdOegvyMjRxrAfiWRWasGRUzLiP-3h6gyKjXK2kaJDALQz1oI4VeL~z~I7UjOu9XESdGjovIvbZjDRN5fKgncZ51z9bWcjXkqcnDDbyQqa1e1MqzBRGi67B-f1knXiL5nrrALjpXJdieCP545apdDyvGWIKgNV4XmJEqSXUfJcU0gxGKsA2qaD5-b9nA3v9HgDAkkWT3M2or~vZa10oY38RCsvxAzIRcc5cYAQc7Y5MK1R~S~o3gL59fw__&Key-Pair-Id=K3NV4LZ47N8M46)

#### For Public Link

- You can enable Public Link access and generate a public link for each test from the Test Settings for that test.

- Refer to the[📄 Modifying Test Access Settings](/articles/8915306379)article to create a public test URL in case your test does not have one.

Note: If you do not see any errors after enabling “Sync Outcome Data”, you will see the outcome data in the Test Health Dashboards for all your tests within 24-48 hours. Data refreshes once a day.

## Frequently Asked Questions

1.  **I have entered a Harvest API Token. Why can I still not see the Outcome Data?**\
    If all your permissions are correct, then you will see Outcome Data in Test Health Dashboard in the next 24 - 48 hours.\
    If you are getting an error, please ensure that you have enabled the correct permissions for your Greenhouse Harvest API Key. You can find this in Step 5 of the “Inside Greenhouse” section of this document.\
    \

2.  **All my permissions are correct and my Test Health Dashboard is blank.**\
    The Test Health Dashboard is a current indicator of your Test Performance. Hence, it only shows data for the last 90 days. If your test has had no activity in the last 90 days, you will not be able to see insights into your Test Health.\
    \

3.  **Where can I see Outcome Data on a company level?**\
    Today, we are using the Outcome Data as an indicator of your Test performance. Hence, it is available inside your Test Health Dashboard.\
    We are working to provide you with more insights using this information. Please reach out to your HackerRank representative for requests or feedback on how you would like to see this Outcome Data.\
    \

4.  **How can I enable Public Link for a test?**\
    This document ensures that you enable the connection for successfully pushing candidate information inside Greenhouse.\
    You can enable Public Link for specific tests from “Test Settings” by following this document:[📄 Modifying Test Access Settings](/articles/8915306379)
    \

\
\
\
\
