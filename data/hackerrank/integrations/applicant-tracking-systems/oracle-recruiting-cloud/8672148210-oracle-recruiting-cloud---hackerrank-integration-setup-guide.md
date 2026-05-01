---
title: "Oracle Recruiting Cloud - HackerRank Integration Setup Guide"
title_slug: "oracle-recruiting-cloud-hackerrank-integration-setup-guide"
source_url: "https://support.hackerrank.com/articles/8672148210-oracle-recruiting-cloud---hackerrank-integration-setup-guide"
article_slug: "8672148210-oracle-recruiting-cloud---hackerrank-integration-setup-guide"
last_updated_exact: "Jan 29, 2026, 9:24 PM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Oracle Recruiting Cloud"
---

# Oracle Recruiting Cloud - HackerRank Integration Setup Guide

_Last updated: Jan 29, 2026, 9:24 PM (Last updated 3 months ago)_

## Overview

HackerRank integrates with Oracle Recruiting Cloud (ORC) for Tests and Interviews to facilitate an easy and seamless hiring experience. The purpose of this document is to provide a step-by-step guide for setting up the Oracle Recruiting Cloud (ORC) - HackerRank Integration.

## Key Features

- Send Test invites to candidates from ORC through your Candidate Selection Process.

- View candidate’s Test results in ORC including score and evaluator feedback.

- Have a direct link to a candidate’s Test report from ORC.

- Include Tests in your ORC job application flow - you can choose if candidates take this Inline (while applying to the job) or at the end of the job application.

- Generate HackerRank Interview links for Virtual & Remote Onsite Interviews with candidates.

- View Interview results and scorecard information from interviewers.

- Have a direct link to the candidate’s interview report from ORC.\
  \

We recommend setting up the integration in a sandbox ORC and HackerRank instance before implementing it in your production environment.

### **Prerequisites**

User has Company Administrator access on HackerRank\
Recruiting Administrator role (ORA_PER_RECRUITING_ADMINISTRATOR_JOB) on ORC

## Integration Setup

1.  Log in to HackerRank with an Administrator license.

2.  Navigate to Settings\>Integrations\>[Oracle Recruiting Cloud.](https://www.hackerrank.com/work/settings/api/oraclerecruitingcloud)

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047172238-?Expires=253370764800&amp;Signature=emINztonYjv8nKiAHopJycGBjAPxCMbyIFH344CWTx2XhkNvIF49CeGoDX8BNmqONi2yoTqHpcGTdlnwboDBa6rVJbgYQmGgFEATWpzGbJgeF67MPYZUanAjilbXWSEJewGnyvVdS-LZ05oVbBtaj0NsrupIRg-aofkGRdaeKDWeQaGDgUrgtF2WItOZHMge6YxNID~pBlXeYRDy4YN5VD09uvr2MbUxFfHTjw-5phqxbBbj~A-RD9ayHYgK3jlsWvFuyS56rYMoAg03QhDKF6lVfGPTV-CCj2ukCoHRzr~OaztY4sp~V4qKCLnUHFhcGTRZRBdPFZWmCHAZMRERWA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

3.  Download the Integration ZIP file in Step 1 of the page.

    ![ZIP_file_screenshot.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047172680-?Expires=253370764800&Signature=Nm4fBnB50QLCH3-t7GjRvu5qivzfhMp6BGf4CxNw6Hk44tB30hFhmJm-UeI6txQ76N17egtj7l84GWXjSgUa-ROCvZk~wr6UdNLt3025oYovMGwqvSKoVxNABUp86RgJZRwANc9ayKTQ8EIYfSpPn8VwPu9uKGFN7Xa2138WFxhWpRo~M9LPtfpw9bDB55dQvh7WpRNGVF6q~qeMTejH4AKTurRqWsqUqj3xmXle5Fvz2SgGR8scsPGI6tyranLDEHDjzt5J7P6G8Kogzq6~6GHiu1skzZ-FIw2ABsXrlcqETJPj4fXfXwuYRokv1tK1wDYaOqtyiyQ3iz4MuWI~Tw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  The HackerRank Integration configuration file contains information on the integration entered by HackerRank while building the integration. This includes API Tokens, Endpoints, and so on that are used by the ORC to identify the integration partner. When you upload this .ZIP file to ORC (2 steps later), the integration triggers will be stored in your ORC instance.

5.  Log in to ORC with a Recruiting Administrator Role (or higher).

6.  Import the HackerRank Integration Configuration ZIP file.

7.  Based on the instructions from the ORC team, here are guidelines from the ORC team to help you import the file into your ORC instance:

    - Partner Enablement: Partner enablement consists of contacting the partner to obtain the implementation project .zip file and import it into Oracle HCM Cloud.

    - You must have the Application Implementation Administrator role (ORA_ASM_APPLICATION_IMPLEMENTATION_ADMIN_ABSTRACT) and Recruiting Administrator (ORA_PER_RECRUITING_ADMINISTRATOR_JOB) are required to import the file provided by the partner.

    - In the Setup and Maintenance work area, click the Tasks icon and select the Manage Configuration Packages task.

    - In the Manage Configuration Packages page, in the Search Results section, click Upload.\
      Select the implementation project .zip file provided by the partner.

    - Click Get Details to verify that the selected file is correct. If needed, click Update to select a different file and click on **Submit**.

    - When the warning message appears, click Yes. The upload process starts. Once the upload is done, the status changes to Completed successfully. Click the Refresh icon to update the status.

    - Once the upload is done, you must import setup data.

    - Select the row where Upload - Completed Successfully appears and click the Import Setup Data button.

    - If needed, click the Refresh icon to update the status.

    - Once the import is done, the status changes to Completed successfully.

    - The partner is now provisioned. If you go to the Recruiting Category Enablement task and Recruiting Category Provisioning and Configuration task, you can see that the status of the partner is set to Provisioned. 

    - **For any questions related to the above guidelines from the ORC team, please contact the ORC team directly.**

8.  Create an API User for HackerRank on ORC.

    - Here are guidelines from the ORC team to help you create an API User in your ORC instance:

    - **Provide User Account Credentials:** The Administrator provides the user account credentials to the partner for data synchronization. The partner uses this user account for authentication with HCM when updating the data.

    - A separate account is required for the testing environment and the production environment.

    - The following privileges are required:

      - **For ASM:** Use REST Service–Candidate Assessments

    - For any questions related to the above guidelines from the ORC team, please contact the ORC team directly.

    - Once this is done, you will have an API User Name and Password. Store this safely.

    - **Optional**:

      - We also support the addition of IP allowlisting for an extra layer of security. This ensures that only requests coming from HackerRank’s servers make it through to your ORC instance.

      - If your API User Name and Password are compromised, this logic will block requests generated from servers outside HackerRank.

      - Include the below IPs to the allowlist:

        - `100.25.76.193`

        - `3.233.184.164`

9.  Copy and store your ORC Base URL:

    - Your ORC Base URL is the domain of your company’s ORC instance. \\

    - We require this to be able to post data back to your ORC instance. We use this in addition to the API Users previously generated.

    - The API User Name and Password tells ORC that we’re a trusted partner trying to post data to your ORC instance.

    - Here’s how the ORC Base URL would look like: [https://www.yourcompany.oraclecloud.com](https://www.yourcompany.oraclecloud.com)

    - Here’s a sample URL: [https://eyte-dev12.fa.us2.oraclecloud.com/](https://eyte-dev12.fa.us2.oraclecloud.com/)

10. Generate OAuth Tokens from HackerRank:

    - For this integration, HackerRank uses OAuth 2.0 to authenticate incoming API requests.

    - For each customer, we have 3 unique tokens that need to be entered in ORC. Once we validate these 3 tokens, we generate a temporary access token that is used by ORC until it expires.

    - Once it expires, ORC has to send us the 3 tokens again for us to validate. This way any token compromised can’t be used for a time longer than 1000 seconds (16 mins 40 secs).

    - Click on Generate OAuth Tokens. You will get 3 tokens: Reference Key, Client ID, and Client Secret.

      ![Generate_OAuth_Tokens.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047173548-?Expires=253370764800&Signature=jcoGByIVkKDoOyi1D2gXhmvjK3Zu8lAQU0~m5qkQNOS8x1Fh1ZqodGOa8pyuiCf42N4c17qmHfhqTwEOfqoSVVgyFfuTxOlTRTa-MbQko9hFVBllwx7YktYs~iB2zY2dnMsbFMmimlDKcb4jgMMgQ1AJo0Z0FA8WJXzV-pfmhryARrPuLmrEx6Kc1YPbzgrGXflCURMiJX1CJhCm2GUR8GOICFotWjJ1WyPuzWxeJ7CPEAT7y3RWmSwpbETKg6omxI4V79mTZJXE7pCNj98IHkAD9pvNrSHUr0uNzGmLQvuIDQzwh9et7A7nVaO1OfXGP3cg2ajm~XTE-IGvjULfMA__&Key-Pair-Id=K3NV4LZ47N8M46)

      **Note:** The **Client ID** and **Client Secret** are separate values. They look very similar but are not interchangeable and usually differ by only a few characters.

    - Copy each token and store it safely. Once you close the modal, your tokens will be encrypted and you will not be able to see them again.

      ![Copy_OAuth_tokens.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047174083-?Expires=253370764800&Signature=N0dcWqi3rvoWeaEj9nv7n6n84Poknn~7UKTKaeWOX4J0r9RP3PBVS7~zBpBZy2KfsIb~kAGBvPNNdKxnKHs3XWplk7jSZLkjbaja01wmHVkUKX6r6W2ZEoZKB6hLCbTtDZtQ3X6lzFiOGv-zqh7fJsjyM6K0ZbWc-R0oVV33f4yMBTHUECvdifk2WKlX3SYqABAEgmPhnc6U~BFgdxpVduTh1xkuXyew5xFfc0AqKOaGDOW6xPCJeDpxZyCqLHgQODWHaQG6TkR7dx~2~G-BQc7q~Bh4FKPS6z9jdMcJMgrn1xcc1Mi7ZCPnLNJP08kEgVZp9Z3UnENR6C34UN8LPg__&Key-Pair-Id=K3NV4LZ47N8M46)

    - If you misplace the token and cannot find it to be entered in ORC, you can come back and regenerate tokens from HackerRank. One thing to remember is that if your integration is active with any old tokens, it will stop working if you delete these tokens from HackerRank.

11. Find the **HackerRank Integration Provisioning** page in ORC:

    - In ORC, you need to enter all the OAuth tokens and activate the integration.

    - You need to get to the HackerRank Integration setup page. Follow these steps to get there:

    - **Go to Setup and Maintenance.**

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047174619-?Expires=253370764800&amp;Signature=IY6gnYcYabzyGafN5mdW8E127bNsHXpUfwNGzPcrIHdbOVQh221U94wlPI9F~luyI8F-zyfwepG3TEI0KBik2nNpx1h3quvWcIP5aK8Oni2fPSaObHkKNlj~6p5yCAOG7Irf073S8TbuNnZ0T4QRpGfGYHAdVAxkWxF3tFZE~XCQdflrJbF2T~kWc8Ir~WMAxupZ8ntp2FiYEQ6XZ5W0Y7A4yG0Fc68hLUghEHCHnyChFtB6cqvj4YSz7niyj1~tOmHoTR17jvzOZXkTa3GhJhVkFmO2Z8KwjXZBdQOfMwgzEHL1TJ~jkBUz5TpSfcYriItFeVdCLJN6Q4m1SvqOZw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - Click Recruiting and Candidate Experience.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047175228-?Expires=253370764800&amp;Signature=Vb5-ebe1-5W-jeDp2E7WZHBJP0VEr0ghsYMQ0JSdMaH47fjqaK3rcVMX9MX0jjbiDkuFjeY-FT6BYV5QTCIz5Ao3ZdOtC5M1OXA-BC~O-wha2HS3T9sAUbtbpSUuYDFzakEoc-08RCuQ8LGthsEplup-0RwmHVReAOp78R~g3zkeBIUwuvmBijMYxeofmU7TsjEAvRbZs4IxHXx0cVGPRu~j7VJu~ua0Ej5DY2~6AoaO4kMU~94-wdAEq9gWb8rROXkYKbB8Yxb-XeB~2Dqkuaq~8BSEjNaJz3E7JP-XHXYu7fKAZOjsMZh~LHcKDoiMnexP0nXQcCxBrJnM5g5Cag__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - Click on Recruiting and Candidate Experience Management then go to RecruitingCategory Provisioning and Configuration.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047175652-?Expires=253370764800&amp;Signature=PEQJyDAgCE4UVqXThqids75WPRwKfiLkVbvWAJooeDO2W0p56gBmhCmAnQx5XQZV2r1VthQ1FmNUlUDHcmH9H9RsR7zutfM7XdraL-hJWA~HQfut3UHmR5g9-oCaiP9l8aWwAtd~YhUhlA2KDHgZ1dKBpiGjgP1U-V2MZS3LeXxrQXcL~S6~NLOjRaJP6PsDSfZgMLid2Sj-YpZFa~195DIyULYBuFdjlzS84GvapY1UN9tDToSd4wzARJIt8z4JY1mGwL6kqD9TCButriKW4SnxvN-qgMjuUFCQELmFPwsi4~T9qRpJd5eEykIt6aGYb~hRTMlbQPScdqHVIqJ5xQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - In the Integration Categories under Assessment Partners, you should see HackerRank. Click on the Edit (pencil) icon placed at the right end.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047176142-?Expires=253370764800&amp;Signature=kzq3qWG-B3epLu4l5fAHG5rKeB9K3vjZqB-E223uzYcU8ulG1lbmJtmxVHixQgv0XdEWWWE0jNe-rPKgwEaIWz~hUoaAYnhJledEL8A60HdX2EmDyTJxTXEt6ruy7n~q62SyT4JS6HzQ59JHGICOq1Pcg5xQevSItpfjxLkEK5t9Fla81N~nfLfBCTSMQg1scRSLnEIDkpZK8n64vES57aDfa-2ESHNjnSf3eEUv1dLlCLIL2hyM3etg420WVHywocgmlPMSEH5Xm5wslBAOukuPBwWgo6DYAov6UTL~xpp5nz5eGDdDpavbmTQBr3dHeowd9guhwg74BJ0l9b49-w__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - You will land on the HackerRank Integration page.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047176513-?Expires=253370764800&amp;Signature=n7H5MgPeDs1hDQDnpphtuJN88g9JXH6hsA7HvTvOmd-mLtvuYWrBKf0P5bdUaiz16FmiqQY3G3T07xhuv6dyyKDcPWdjVJQM8A7kiVFfalwqhCw1LpWUTjgm8G5otYmqFqbleVaIw9EvuAzGY-nK2paP1A2sZczOYUrh5qs-7yzbGbbzlBVrJfRr-mvy31-FakujbNWE-QveRBcwFtvSw0G~CYuJryQoWHQG8nKro~uX1lKXSJc8FDQEEaEdArcm38sEw3hRCl7G5zfzX8enZS-XuUOEmlHoOY4vhwDEVwAjsQ6jj6d5zYZ3p16RIki9ccPMCThbo9cB6qCDb3ZRQQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

12. Enter Integration Details in ORC:

    - Once you get to the Integration Provisioning page, enter the 3 tokens generated from HackerRank: Reference Key, Client ID, and Client Secret.

    - At this point, you will also be able to set up the Validity and Validity Period:

      - **Share Results Across Job Applications** - If this is checked, we will use candidates’ test results across job applications if they were invited for the same test.

      - For example: If a candidate takes a test for Req A and then applies to Req B where you have the same test set up, we will not ask the candidate to take the test again. Instead, we will use their results from the previous attempt (for Req A).

      - **Validity Period in Days** - For the Validity logic of sharing test results across requisitions, this defines the number of days a test result is valid.

      - For example: If this is set as 30 days, and the candidate applies to Req B 40 days after taking the test. Then we will ask the candidate to take the test again.

      - We typically see our customers use a 6-month (180-day) validity logic. Meaning that they consider that a candidate may improve their skills in a 6-month period to make it worth their time to take the test again. 

13. Assign User Account in ORC:

    - On the integration page, click on + Assign User Account. This will trigger a modal that will ask you for information on the user.

    - This is the API User to which all HackerRank Tests and interviews will be tied.\
      In the modal, enter the User Name as ORC_HACKERRANK_USER (Use all caps and no spaces).

    - You can use any description. We recommend “User with all Tests and Interviews”. Then click OK.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047176876-?Expires=253370764800&amp;Signature=PI~3qaxDKKu9LfOr38o01lH1DtoKrhf5P21PjmbR11fJF62xHFfY0GhcIiL3m~T4QtUZAti-8a~86RBZnMnzzppao5uTGaiGJ6DLbdeZtzxRabsX0qVyyrzIYfmjA7FBI0FeLA43jHtQh63CisR6wdV3pRO7mgzOrBB8k7tc7uavJanKObgTeFdxs66q655s73t3QZsgiNhn6hEPMPqAqnXtnyUdjTXs6m6XYFuEqtd667kC-INEXoYyXRk3aiEDdpHUdm9PWiCayENoj7ffjSw1DYhUKnZ4G9ZdFBG34wD5KJLSyc0zW8p9z6pw7ENxPdYQyLv2jO1HaMVGyK1r6A__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - Once you click on OK, ORC sends us this User Name and initiates the first API call made from ORC to HackerRank.

    - At this stage, ORC asks HackerRank for a list of all tests and interviews accessible to your company. We respond with 5 Interviews and up to 494 of your most recent Tests. (That makes it a total of 499 since ORC does not accept more than 499 packages for an integration).\
      If you are able to see the list of tests shown in Screening Packages, then the integration was successful.

    - If you are unable to see the tests or if ORC returns an invalid User Name error, check if you entered the “ORC_HACKERRANK_USER” as is without spaces or quotes.

    - This is an example of what you will see if this step was successful:

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047177194-?Expires=253370764800&amp;Signature=Vttsp3OGA7vZaZ~HxJhq3hjqclcgysyw53LavKECANAVYMEImPKUCv3kTVT06jE~Rqp6ii-1I86YNfnh7rX-GFz~9a6XB9WOJ2U1d7Wja2joFvKVBYAA6puPKBno4gCpAY5T5wqIzZKzvaPAaQDgfcGN1VTpEeKtlVIsFcAHVnP1Es~Iw6Azjuju4ZlDf0kNjBU9tYaAA1EuYz7TqbP52q86hvnV6pyToNmV~wcgR37Bk8qSLEMYes5yMSnwD-RhwgSC-5C3yrkCO7At~KioSIBi3E-6KY0rKSSqwgKnF8mUdrWYbg2tshKFfmepuGsCzDu01ifsa-K~T9ndn-yzrA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    - Once you see this, one final step on this page is to click on the **Activate** button at the top next to **Save**. Now, your Oracle configuration is completed.

14. Assign Additional User Accounts in Oracle Recruiting:

    - HackerRank supports adding more than one user account on Oracle. In the previous step, you added "ORC_HACKERRANK_USER" which is a user account that pulls in all the available HackerRank tests from your HackerRank account.

    - HackerRank, now, supports adding individual users as user accounts on Oracle Recruiting. You can follow the same steps in Oracle by clicking on **+Assign User Account** and entering the users' email IDs.

      ![ORC_Adding_UA.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047177606-?Expires=253370764800&Signature=U98iSxvpNGIXXInXlup~pzLzsP2dmxyjyxZDMw1fJmZ7G6k2wM7NQnTqOvndCZFUir1dpisfShXCV2Y6malzZVA0Z9rEVuFoQT8ak-EASaSSIY7vsvAWAxjVQFgmbVA-0C3w0pO6m10LNUa1003r9s1hwfhoKzkZgx6yt5pufDDVzGpu-79vfVi~R1kk7K6V-vPCumaKnizBQQ5T5wi8cI1k-2dWNcyA6-cZsFcLa8sKIuLl6sYrEDjg026NqIPyFBdCll6pswLDzDWe1q0acE9DVLFG84Vcr4rXXIebjl4c3ZVSWGfWwF0TFPv5eJUN75zKvM~nLHmwZM~2dWqzGA__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Note that these email IDs need to match with a valid HackerRank license.

    - By adding individual accounts, only the tests that the provided email ID has access to will be pulled into Oracle. Thus making it easier for users to select a test that is most relevant to them and avoiding scrolling through a list of tests for roles and regions that they are not a part of.\
      This feature supports recruiters across teams and geographies to use the HackerRank - Oracle Recruiting integration effectively.

    - All the added user accounts will show up on the integration settings page in HackerRank.

      ![USER_Accounts.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047178028-?Expires=253370764800&Signature=lkhC1YUFvCEQ3afI5BM~nMeRQCJSD5MNYiMVe4DBIbMkY1ly8tKeoUnmB7XfYZ8gePnHxdSNSHaGsKA7xKt8TCm4fyzObHjMt4hnDA45nb6EuhZKIVYBGnnEry3xPQhm9XDdb4Zds~dCPF511rX0uWGCZus-3WyyPgo~0CuuibH3IQbVRt~F6kUTD-yDudyKs66tyVHAQC7BcNCN5JjAVXSVyDecRGe5gnKsvVI2xLRq6sFQQagySHAwbD-mu5pb8tirhaYpdUJSyzHq-ucTdd7EUHPkvFajhbdKpkGMjoaDKonwC4F09jYAf6DkNe-8OVIHmW9ZXJIQkrFXukQotA__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Note that if you want to delete these additional user accounts, you could do so from the integration settings page in HackerRank.

      ![DELETE_UA.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047178739-?Expires=253370764800&Signature=iROkbhfQVN~RQb2womDpR3~HQNU0F1OMOafnh5Wry8cO3FiS1Qsbj4xueoEWJKEgE681cEifRQTjPRy~VJJ3X4oCwZXhVMb2pZDa7QsaeMzhYYfxneWecv81od1DbkkYSikVwdsUtcnKdPyvel0Wz2bDVhfGyuizDRA7-W1q0a1622qs1F8iWl-C1-EqpWgj0Eawim~TLCjAXhYWcp6UbyicYgEr6SMha1H4WML9hhousPernoH-0Q8I~AK772-J4pxJQbsylwI89dwCcr8KdcMYzjIy99c9wLUXtdi811HQ096OApLWKOnqdw2YpMSqmqbKM~WsVQ54tUTV8EyVSQ__&Key-Pair-Id=K3NV4LZ47N8M46)

15. Enter API User Details and ORC Base URL in HackerRank:

    - Open HackerRank ORC Integration Settings Page.

    - On the page, in Step 5. a. Enter the User Name and Password you previously generated from ORC.

    - On the page, in Step 5. b. Enter the ORC Base URL.

      ![Final_Step.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047179616-?Expires=253370764800&Signature=BUxy8aZTZ5GXb9TaW7tRBv-XaA0Gnqq6lqCwcSdl5RK42NeqbsLk85kCHU80k1CMzCnjzPPXYSCdjNgMQKnTYZ4nKJu-4wamSYp1zlh7U~PM9UjlIDbPg0I2L1Wc4voISAOD6XV8F670DuYFjhos0OFyywgiQ202TskB95XDO~aeEt8jr4stpo8V39AmvPq1pICTjWfqkP0v-SXtzJKDWLNWaqBamQ1KU1RDs2cKmqbblaHYauMKz09A0k0WeWihP2QXoPrLO8ImLH6cmzdb~JQ2jyxWRmIAr~fvaKqRYbM1dkcdwBfIPgv-PiUPRWLoudupJc3EQJiutJM7vLK5JQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Make sure you press Test and Save. This will validate the credentials you entered. If the credentials are correct, you will see a success message on the screen and your details will be saved.

Now, your integration is successful and activated. You and users in your organization will be able to use HackerRank from within ORC.\
\
