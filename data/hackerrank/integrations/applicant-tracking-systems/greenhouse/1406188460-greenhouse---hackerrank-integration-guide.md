---
title: "Greenhouse - HackerRank Integration Guide Prerequisites Integrating Greenhouse with HackerRank Glossary Frequently Asked Questions (FAQs)"
title_slug: "greenhouse-hackerrank-integration-guide-prerequisites-integrating-greenhouse-with-hackerrank-glossary-frequently-asked-questions-faqs"
source_url: "https://support.hackerrank.com/articles/1406188460-greenhouse---hackerrank-integration-guide"
article_slug: "1406188460-greenhouse---hackerrank-integration-guide"
last_updated_exact: "Feb 16, 2026, 1:06 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Greenhouse"
---

# Greenhouse - HackerRank Integration Guide Prerequisites Integrating Greenhouse with HackerRank Glossary Frequently Asked Questions (FAQs)

_Last updated: Feb 16, 2026, 1:06 PM (Last updated 2 months ago)_

HackerRank integrates with Greenhouse to streamline the candidate screening process for recruiters.\
This guide explains how to integrate Greenhouse with HackerRank for Work, allowing you to send tests, schedule interviews, and view results seamlessly.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have admin access to your HackerRank and Greenhouse accounts.

- Your organization has an active Pro or Enterprise plan with HackerRank.

- Your HackerRank login email address matches the email address associated with your Greenhouse account.

# Integrating Greenhouse with HackerRank

To integrate Greenhouse with HackerRank:

**Step 1: Generate an integration API token in HackerRank**

The integration [API token](https://support.hackerrank.com/articles/1406188460-greenhouse---hackerrank-integration-guide#glossary-11) allows Greenhouse to connect securely with your HackerRank account.

1.  Log in to your HackerRank account using your credentials.

2.  Go to **Settings \> Integrations \> Greenhouse \> Connect,** or open the [Greenhouse integration](https://www.hackerrank.com/work/settings/integrations/greenhouse/configuration) page directly.

3.  In the **Configuration** tab, click **Generate an API Token.**

![1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1762499532770-1.png?Expires=253370764800&Signature=jqHqJMslNYmpUoKaZADH~l23RBq0MAXz0KsCl0VyHvcFjRfEbZGrSg9Rz4V49XYw2lpwUNpguflamXdcHnesW6M-TShhyFBqlIXwOChHDubJstBA6eZeoGeumWEABslpmCBiQBQQAgivB03OJivU~08KoZ6HcTpSrm25Ix529WoISL--A~8kBmZCCnHTPzS9kjZVvaY8KSSSUQCCMX3uxURBr4US8dwDULKH1~lWhlomZ618LNnGlDmQmVs5iG-GhH9hUy-ORPRSpec0T930-TPc4Tp-u9SSepJm7GoyVRm9FU65bCHqugO21texBnWokW3t8gZPnC9Oaayq561wwg__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Click **Copy and close** to copy your token.

**Note:** You need this token in Step 2: Add the integration API token in Greenhouse and Step 6: Create a ticket in Greenhouse Support.

**Step 2: Add the HackerRank API token in Greenhouse**

This step authorizes Greenhouse to connect with your HackerRank account.

1.  Log in to your Greenhouse account using your credentials.

2.  Go to **Integrations \> HackerRank**, or open the [HackerRank Integration](https://app.greenhouse.io/partners?partner_type=integration&partner_id=45) page directly.

    ![2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Febe30ed1-6dcf-4b0c-ac3d-6d6bda894aa1-1762499579416-2.png-5e064202-7d70-4e27-b58d-85c7f86ef6c1?Expires=253370764800&Signature=mZ7SNvYFYeWlpyu420v8XOT-eVjoAUbJfqlElgwEECtBeHjF~u~7tV9equ60vrr8dj0vMHfCWcxw-zp-3yeobF1lthKPwOvwsXpcGFlKzUhMitKxJQC2-T61~O2UN4DGUaFrdgOZX1ikcoS4Rxyz6P6625U9zu8TAVWaNCEOnORpXweGJPoMS07EI4AVPHsYJIyNkPiWpl0Bcmr3gUjORpIE0NjB9M~ynmgbD3CsTPwwLH0Ie6e-nF5YO9ngktMJbXhjkufk3eia-kviMk9FcmeEnlRoMsdbksO4ywgI34691F5jzR-QRd1X8qvD5BY7HY-M4SMJPvyH~sTo1geJHQ__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Connect**.

4.  In the **API Key** field, paste the API token generated in Step 1.

    ![3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F70adee1f-1563-4c44-91ef-5c1e9c70061c-1762499682796-3.png-8e62d846-f329-4460-9b60-29af408ba4c2?Expires=253370764800&Signature=CeVzs8OcyzDIOQg0ze5iw76NQfF1vmW81horL9L9pEeTu5wbhvmzCY2FXlydw03iJRKJG~wI8z8SalYKe6LbxUfglm1MiRaYM7aamFNNZaLvQ-c4gjnHmatpVApv6SThMaD5dAysR9MZR1dCZ-rKr4Adw9Zs9P23sH5B1Os9QKuRp5ulhpxxK18Do4XCe25keya3izVJe1OrfS551U197IHqtSDAMKUAqEAaWz9-Lhx8PVFeLex5hHSWurb9Tv~HuNzND6AveW3hedUjDnYtgn0zC5jS4acKaPBZnn75Gv~iL7-CLASHqUUnJJz6VzrD7gbQBbpDqAFNY-Zt9OaVAw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Save**.

**Step 3: Create a Harvest API in Greenhouse**

The [Harvest API](https://support.hackerrank.com/articles/1406188460-greenhouse---hackerrank-integration-guide#glossary-11) allows Greenhouse to securely share candidate and job information with HackerRank. It also allows automatic syncing of test results and interview information.

1.  Go to **Configure \> Dev Center \> API Credential Management,** or open the [API Credential Management](https://app.greenhouse.io/configure/dev_center/credentials) page directly.

    ![6.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Feefcb0b4-1a44-4f74-a42a-53b1ccbe4653-1762499735124-6.png-bd2fc004-8cf8-49dc-b240-948e56123288?Expires=253370764800&Signature=u3kimmw3R2QVQclMemm0fu9SzssUzjRH4A~a7tOidxqHTpl~mBv77Mi3zB2CmgUH2F~2pIDGvAC7Gjxt4dHVl~zWUSwgKzaU41dKzd71D3RmCBagPMvfU~k2fwY6~Hi~L4gKNk3xpRCF20aBRHAMJNbOv11tqd64yNY3ZDvNVA6ACoE9XMuNGYcZXL--HNBhugWom3R-hAEHispYr5EwYdihZyz2odvlvB6O9lu~0Z5Pp2nz6WRQFrm-26hcMj7DaqUh0aAoh3qjzLfUbJeEkSjAQus5BCL4N1-CjO2lnEn-UGeY45kJRFHsw803PqGPvFKqBTakXrMAKaI4k3tYZA__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Click **Create new API credentials**.

3.  In the **Create new credential** dialog box, set the following options:

    ![7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F35da600d-ccfa-4660-abc1-278c303d746c-1762499825540-7.png-a6cf8061-3137-4e09-8788-6ce13e9db997?Expires=253370764800&Signature=U7LITthL7K6P65GlEZdvZjOEidcR-ndlXISt1vw91KjD2ySeSD6A42yx4-y5AheZZeMDc9ufyvuOVTa576GGJ1vnVwBtyVRUOgzlU~S0C0ACHBaVL5cyw0HT~CtCr2MHmbmEZ-KdxazmBZXUQdEDxb61I~J4aPS4A5uDoCNrtKGAAiEht1M-yy8M9yT2nxCG-6ZVoGBply1kqn6Kv1EGP4Tk4havZby4MD6mx-I4k-gfHUb1RSSYBgL7EDk978zg9EqLt42vESax2k~KqqwmZxdNNx9o4mvbBKDDVR7eU-~SQ-5PyL9femHpZlnoGDCEYrEXBFMImk7VQul6mc9UtQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Select **Harvest** as the API Type.

    - Select **HackerRank** as the Partner.

    - Enter a description.

4.  Click **Create**[.](http://Create.Click)

5.  Click **Copy** to copy the API key to your clipboard.

    ![9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fea08dc92-cc1a-4653-a979-bc41f81ab5b4-1762499909784-9.png-a1758e4b-665e-4619-a8a4-699f762899a6?Expires=253370764800&Signature=heBBjvQ6FpyXsqq4IeDSON9~ve4oifqGPe2YRXFbLmhhPEg8IEzK3eThKOcES9eLaRf07xsn6InXTvsK-iMjOPkXxqdKX-c4cf1U~fgG7WKcm5xYV1Ms0rFEwKiaUmaluHdo57JfBh3qJbmR3MHB57pCdv-QItpHdHiCvTecQKgQOYRUCUrbzRRCKy9dwY6EgPE3jOtj4wPAx1zTkZku3AFhADF6Ak8wv4qeGxXG1aJrSN17MeLCR0TndOsYj7mxmvSoJEUxi-huFE9w-myF3a04ITU3Kznfek74Exq-aWr1gIbpSASUQulv3RA-hvyRqXR0PDBwTA4SDxK7NTGh3Q__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** You need this token in Step 5: Add the Harvest API key in HackerRank.

6.  Click **I have stored the API key** to confirm that you have saved it securely.

7.  In the **Manage permissions** section, select the required permissions listed below for the HackerRank Integration.

    ![8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fb7aa915d-f4f0-4841-ae5f-81a5fde7ff84-1762499978729-8.png-c7bbd53a-416f-482f-85d2-1e010181bdd8?Expires=253370764800&Signature=B2r8QLfuHs7HTOUbdy6mZuPWhpvidEbfKvivl2uD1YhycOXDjF5y7AXDpg-edZi~dH-7vyx-8Hka54jHviGJu4NKPNW4Nufk1Ai1YsDQ08tQEIJHMB-ME1b~0BhLpnTSPCt0UHBTwYE4tgPopOENmvXbzYO0QNvyxaaQzS-I3GUaJJRB6z0HtRVW9jsoQaGa2rifaw-Y6iiGdR4qWmmpbSz0kwqxGKmph-mo0nbPfL23IGspRsEoEtkmK4uhanwZ23YtH9geQTCWCYjgLTjqm9iBJrdwOkfm8SSrHaeoWoQs7aPTqJMhZA46wq5ERLSYinbldeOUD4TNX98VpN4JnA__&Key-Pair-Id=K3NV4LZ47N8M46)![screencapture-app-greenhouse-io-configure-dev-center-credentials-permissions-2025-11-06-15_26_21.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F8d5cce9e-9be1-49f4-8c38-d1a0ae2d0bca-1762502920226-screencapture-app-greenhouse-io-configure-dev-center-credentials-permissions-2025-11-06-15_26_21.png-45caae91-0b87-44ea-8290-ac0de9909301?Expires=253370764800&Signature=pWWOQC2ZhGN~C6sLHcSj4h82tMz2SZy5r~9FxE62FSF6cnjDBPOlcb4qikykW8fsPSBT9Dxpt6bJoxx1fmqaynz8TZOUXA5OYsJgbnWGLmIv7JOPF1sPJQGLbtxsPeNFl4~oirfVU5g1~XwDT8DBwtO5H9gDIU1skBvIUiKsmxbeb4Ttd~G-rCl-qbp3WZ9T3b5U0yh-3GnWlhL1DLjt898qy1I-JbOmdCZZaweSwNZhNHLTl9ZnwLrnx5d7qc24tP62ktWYP0Cz20bpjsYE8wR7RBtsJk21Ccin6lQrE7KmX6WP1Z0F~NCvJ6viT2sUTaND42EKK8H5WxexLP1heQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    - **Applications**

      - `Get: Retrieve Application`: Retrieves a specific application when need. For example, to validate application details or support features that use application data.

      - `Get: List Applications`: Lists or filters applications by job or status to support configuration.

    - **Candidates**

      - `Get: Retrieve Candidate`: Retrieve a candidate’s current data, including custom fields, before you add or update information. This prevents overwriting existing data.

      - `Get: List Candidates`: Verify the API key when you connect Greenhouse. The system sends a minimal request (for example, one result) to confirm the key works. It does not retrieve candidate data for normal operations.

      - `Patch: Edit Candidate`: Updates candidate profiles with HackerRank data such as test results, integrity signals, interview feedback. The system stores this data in custom fields or activity.

      - `Post: Add Candidate`: Create a new candidate in Greenhouse when you create a candidate in HackerRank. This ensures the candidate appears in Greenhouse and can receive notes, attachments, and tags.

      - `Post: Add Note`: Add notes to the candidate’s activity feed in Greenhouse. For example, test name, score, report link, PDF link, and score update messages.

      - `Post: Add Attachment`: Attach the candidate’s resume to their Greenhouse profile when you create the candidate from HackerRank.

    - **Custom fields**

      - `Get: Get Custom Fields`: Retrieve existing custom field definitions and current values on candidates or jobs. This allows the integration to append new data, such as integrity signals or feedback, without overwriting existing values.

      - `Patch: Update Custom Field`:\
        Update HackerRank data to your custom fields. For example, store test results, integrity signals, and interview feedback.

      - `Post: Create Custom Field`:\
        Create a new custom field in Greenhouse if a required field for HackerRank data does not exist. This ensures the integration stores results and feedback correctly.

    - **Departments**

      - `Get: Retrieve Department`:\
        Retrieves department information associated with jobs or applications.

    - **Jobs**

      - `Get: List Jobs`: Retrieve job information when you configure or use the integration. For example, validate or filter by job.

    - **Tags**

      - `Get: List Candidate Tags`: Retrieve existing tag names in Greenhouse. This ensures the integration adds only missing HackerRank tags, such as test status tags.

      - `Get: List Tags Applied to Candidate`: Retrieve the tags currently applied to a candidate. This helps keep status in sync and prevents duplicate tags.

      - `Post: Add New Candidate Tag`: Create new tag names in Greenhouse, such as HackerRank test status tags, if they do not already exist.

      - `Put: Add Candidate Tag`: Apply the appropriate tag to a candidate after the candidate is created or updated from HackerRank.

      - `Delete: Remove Tag from Candidate/Reove Candidate Tags`: Remove or update tags on a candidate when the status or workflow changes. This ensures tags remain accurate.

    - **Users**

      - `Get: Retrieve User`: Verify that the On-Behalf-Of user ID is valid when you connect your Greenhouse account. This ensures the integration attributes actions to the correct user.

      - `Get: List Users`: Retrieve user information during setup or support to validate or identify the user acting on behalf of the integration.

8.  Click **Save**.

**Step 4: Get the admin user ID in Greenhouse**

The [Admin User ID](https://support.hackerrank.com/articles/1406188460-greenhouse---hackerrank-integration-guide#glossary-11) identifies the Greenhouse user who owns the integration.

1.  Go to **Configure \> Users,** or open the [Users](https://app.greenhouse.io/account/users?status=active) page directly.

2.  Click **Export to Excel**.

    ![10.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fa2c35710-09db-4cda-8d64-b2c99778c3a1-1762500109623-10.png-4f370bd0-1e77-4b08-bcc8-c5fafe004b4b?Expires=253370764800&Signature=uZQlxc5dxnCyJPvaBetm6u-0IgFs5siMgrb7CmY7XvRiWBSVKiOOdhcTkhQOcVOLyq2vhgru~DPtICqSxrwzVApTrDmxGMFz3euXHS2I8qWITMI2bYTkK-Gr2Rs0Y3o3tJgV9BaeARbW49oxOcvIrjNdvciW2bJUH6vJTbWadyLpnbtMr-DL8c~IAi0oTIohyWTkx-Np7uEA3FPbyWmYbQEt5N3dc84QzR7w34eFZIyfaq8MT~oHJGNjCuZF~Hnv-YAQKM2Gd8LFX2ZNAnHeqh45BMXAa~eRRAGvDcECroMraHhqv2B5zmlZxEtwMeNInQUIySap3APx7P5ffUEhDg__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Open the downloaded file and locate your user ID in the **User ID** column.

**Step 5: Add the Harvest API key and admin user ID in HackerRank**

This step completes the data link between HackerRank and Greenhouse.

1.  In the HackerRank account, go to **Settings \> Integrations \> Greenhouse \> Connect,** or open the [Greenhouse integration](https://www.hackerrank.com/work/settings/integrations/greenhouse/configuration) page directly.

2.  In the **Configuration** tab:

    ![4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F493af6b6-1075-4c50-9993-d96a73c036eb-c0f4b6b7-54bd-43b6-9ec3-2cfd4ddf812d-1762500185786-4.png-0088a265-e3b8-4d6b-ad1e-9ab7b95a842b-2560ffd6-59c2-4c5d-aa17-3feb27639f5f?Expires=253370764800&Signature=VhV5epzzLUZdsaXKTdkn853GON6X9StivpmaVxEU4DCUnt-w-706O6gC9QfkX1OPgwY9Nri9NADmmVUFFG~XJ6~IRDBIuZ5pZnWMxZU-ZiHtMF~kkCiG~xdpxLCOGl8HH5aq~vMHSzthidmIZ~jMOD0NWG97XelDzpVrRkU5YcqFjCmmts60zjDNguUMty8iIvPsunnPtQxSXzdHpb-K9SXtba8RoVfOudVFeOcHpNXcei6aUY1KHyyDODaGcM9T~w8ST6bW0dw9OOADpfBhhLgqvfRhWvTZ3Za2M9BpxJYqq5LivihkbnFK6TQ-nPIn7rWpem77VJKIX9ljwtdUJA__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Paste the Harvest API key from Step 3 into the **Greenhouse Harvest API Token** field.

    2.  Enter the user ID from Step 4 into the **Greenhouse User ID** field.

3.  Click **Test and Save**.

When the configuration is saved successfully, the system displays the message **ATS Settings** **updated**.

![11.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Ffc3d23a2-2671-4227-868f-fe2b3521935d-814eff63-ae22-4a79-a6eb-f10e58561060-1762500224011-11.png-cc7b33aa-382d-4330-8a41-ce7ba9e97db5-e912ebc1-6661-488e-b3b0-b45378bbdcf5?Expires=253370764800&Signature=oe77v9TgyHixGNeQUPNoUOY~hH3BY3x5yH97a~SyG3PzZ7KP0boVOProJl~x-eWDeAbT87kceAf-SsXGgSoWlpEzjIEp6cWR4sNenRBFN7JO2E~KVizy6UUKyR6qlKH7oXR-9tt17zErr3nJn11ulNOFDNvR2PEHD1oWTO-tYQpVULpp7F3V2ybStcqyOJL8aJu1Lp5jcVpD6rsA2u5l1v80sOao0fL4IV0uhn4RiCe1k5uwOMYsnhQAOXxD9Qi8KudqdyrePk8x~HdPLpU-GRvu-kYQDQyOWiaCcna~WXKXXptlczd-nSOVCWvQ3ep~gLDW2ZUsLWv8Red9LKyAxw__&Key-Pair-Id=K3NV4LZ47N8M46)

**Step 6: Create a ticket in Greenhouse Support**

The Greenhouse Support team manually verifies and activates your integration.

1.  Go to the [Greenhouse Support](https://support.greenhouse.io/hc/en-us) page.

2.  Click the chatbot icon.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fcb99356f-fa3c-45c1-84be-f2c213b83049-2e045035-1d0d-4f69-a0c8-727889580bb6-1762534850344-image.png-834d4ebc-6489-4074-89f5-367df6ff1567-36f4c28e-f368-40a8-92c9-c26b8d7184fc?Expires=253370764800&Signature=Xe5TQpEE3tjKXbPj9T9hccVZbEGSD8isXR7KSMVrXJceLphG8fQSfgfQ~0SNxiwy~3JRcGLPRE0A0yjuqOoxA5M-eISBwHaEZaqvwDz2x2l8vzqxhF8-tIozpm5UxEL0WLaYxENbllmlFNVi-Cufo7DR7uR0S6AwYKMp-6NOug9NoIqVitEjAIHnxdYRadKeswDvhJredDoy2iPKYWR8RH2C6DhNbxH7EIiSx8nyqYnw6fpAxPPp9w6rSKx0kx0nv8hEjL1HLXX5eoclEH-fd7ReiZA5tqI9JwUr8Mb4yBf2C57qTMS-dMb1AmkzUlOhzx3l3sJ2nxVY3znJuzS60g__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select **Ticket**. 

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fdc37a554-1ce8-4780-9a21-a1fd197f1e03-8c9002dd-58ad-4bb5-b590-4e315d40dcb0-1762534919007-image.png-45783a88-eb4e-4bf0-828e-f05062abb157-00538116-dfb1-43ae-83ec-55026fd0cf40?Expires=253370764800&Signature=I3zOcWZj6~ihMWtb0UCTT2gwx8mBClOCjkOSGUI6xWvz5T7-bx8UwPogc~Bw-6w6OhLYRYZRgmc5bFh1cdnPrIlWySWp2q5guMHtMr3FxIe9Nz3Y-Bdllw8fU9-2kCc5gyVM0R4BhuiQ5UNIccV~WwqUnTC8fEO1wUHxxKnidjJHX5CsLP9A9GAAAviP~QyD7QAXl~T7d99CGv5iYmxPRViQvSWHdixWMVnfewxhb25ReRKfsx546WLhf~KDsG-EPQndiSzptYo9cK0QZ-5ii4u9gQZ32NDmUfoSF~Wq3l~U-LV5NZV3ML4jVWlJFwy7jX77s1v~Kal-U2jflj6gVw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **I'm a customer (I use Greenhouse at work). **

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fae2a2f94-4f94-498b-a84c-4a76bf60abf7-762ee5bf-28ff-44ff-8344-412082be0e4b-1762534936908-image.png-5441a813-372b-4884-a35b-23ec42924813-42b14d5a-536d-4beb-a714-ff41f3408bb6?Expires=253370764800&Signature=EybNzTOMkbbFxHu88SzSHzdlCm6Z~c-ikCmYZ~aeiyv-UnQzGoFzI~7xcZfzm9w0OBHh0t0kVrx9~ZuJ~h9uPkrkBFW0XoaeIbmGLKPbdlUXhqSrz-pB~i0ysBn7upe5sj0BhDMN3AWOdm633Rev8fpHYuiI0ShcrP8oNRKcUE1M3VOmEnGRwDgx84kNNwYyKB2i~uOVk7KXoGYV5mOxdnB3lqHAaijvnllU07PWWyfYyrdyGo9sS1iS-~1hUEskvoNKpSqNWVGihADgcpJwn1bRB~sthRDDBSXyFmUruwUYl5qg64g4HOhf6l1DBZWBZzTxt0rVgnCbrUcyMpT8LQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Enter your **Full Name** and **Email**, and select **Product question** for **Request Type**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F506800b0-173a-4184-b6cc-413c84624afb-eb1beb26-bccd-4db9-a942-baec5ed291ca-1762534495319-image.png-112c9c54-6f60-46d2-8374-8af3d69e2e17-8a4c660e-5d27-46d4-b461-3b05c2d49942?Expires=253370764800&Signature=aO30VmMnbdUsouATDEv64AMlxjB2CWBtLxDTlO-nep~-9pFEu~K3cjuWe63CYwS9HueQxOoFlpaxbhLx46IDb6lWeZ~yHgJvobknVheTAEEKJuHUfVxSrqDSHuJNfqKShofX5fEEthQq~wqzjJZTm4Ad1Rd5mcsEMlt-dSAUSPBxF5U06z3Wp~AMYjYRy3to9J18WOWWCyYXrr-QL0QUwvg0OIeIo79XHnnlW~mhtOnt0zUoSxmv3CM~U6aM7ti~FA6Ntc3WWTot1~jOyxnkTMBww4ir~DlAK1aNpffLtxlWpzu2Y~V7h8i-BAv0HJOSlhoeQoHmT-qpOCQAgQ88cQ__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Send**. 

7.  Create a ticket:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fb7ab0695-b518-43d0-a977-45c92610840b-a389bd8f-70bb-4dad-acab-20b6010960cd-1762532836137-image.png-c6a570a9-b55e-4006-a619-1de9a6a47c46-9bff2b45-38a0-47cd-a31a-9a26d5c4da32?Expires=253370764800&Signature=srZYWDe2IUKKz-23xGTxmsnmO~56ddcGcFk~8eiOfRq3denEmsDpnVn15~~rW8e0u4LI8OErjWbET6Zw7u5ZCEUNx7xeWEIACkN24p47nUVjRNPfHpiiH9QO7YGq35KgStbYs3Zc0bIOyW2iZ~qMxtgActB~8mNXHSTLmQ1-G9ycVo-AjWB6abraWWl~Qly1Dfruvo7kmDWxAtJuz43lTQHMZedwb3LYQR8v0CY3z50DkCP9SF~ZCknHcxc51uG9v275XbHKpq9QuDDXtMdAhP97hmOl7Bq-B2EFLqYSvYaxlu4WICEgBk4rkY9Zmt4bXk0mKbpwxePtBzItS8XEDg__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select **Partner Integrations** under **Request topic**.

    2.  Enter `GreenHouse HackerRank Integration API` as **Subject line**.

    3.  Enter `Request to securely send the HackerRank Greenhouse API key for the Greenhouse – HackerRank integration.`** **as **Summary of your request**. 

    4.  Click **Send**.

8.  Click **Submit** to send the ticket.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F40b304bc-422e-4d18-bb0d-7749a4c01078-6222ecca-bf91-4a87-9314-ce363f587f0a-1762534977079-image.png-4e13ed22-60ec-4f3b-94e1-b95515561f87-6d9527d1-8432-4653-a1ea-5d7b014081d4?Expires=253370764800&Signature=Zs5rVaCzgxVhbTt2iPxMPc4q146B3g30nQY0ioZDECrHbR0MhOrbg4a5vi8QmuK9mAbCc-j7EWw8RxRXWvpLMyVc-Uxv0cYTyA66pueunuUgGZDaWyI~WzJP3J1~H3WhKdiqNs098nps9NtewwDKRYM7zvuWk42PJ4zpmKR6ckWdsDcT5c2MhZM5RRSWfnPQRwpcnKDcItxBJ1DqIS7QL9l0nVaWPUVH7mgzqrzpOdQqQ4N3BuatcSHqNMjo~i~0SGmTdGehrWCoi03yjqDRc47UC7obSKEVqE91q~hCKih70eVPh~YCTRrbxzp6m-zBeX9vrzvsNBvpzhL~nHmigA__&Key-Pair-Id=K3NV4LZ47N8M46)

Once you submit the ticket, Greenhouse Support contacts you with the next steps to complete the integration. You receive a link to securely submit the API token created in Step 1.

**Note:** If you did not save the API token from Step 1, you can retrieve it from your Greenhouse account. You do not need to generate a new token or change any existing integration settings.

To retrieve the API token:

1.  Go to **Integrations \> HackerRank**, or open the [HackerRank Integration](https://app.greenhouse.io/partners?partner_type=integration&partner_id=45) page directly in your Greenhouse account.

    ![derer.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Ffbb146f9-3803-439b-9329-d39c688824a2-a842045c-b1c1-4b0f-b14f-96b73c6bfbda-1764695327555-derer.png-9f40208b-daff-4be1-abe4-daf97fdae9ac-726cfa9c-714e-407e-897c-4a2080557c65?Expires=253370764800&Signature=fhag1XAqwgz18JXJe6zHzM6NoRLr09ERvF66YBJn5NNKDrrNaNJ04-OihFgv-8oArNCjC-tMnewmLSVeQ28g-bKjj6bKHkelh243wxpLfgW-RrCRrnMQIGXUoDrYcBBdUfgX0uTGNiguBpkDxk4tR5EcGiL~fgrC37wEG7di-gKeYcbFbo7naUgWGvyH6UU6y1WyYHZSXN2~-SmDIshCfkggzmix60cPDX0hyIxhxWA0HICCSTiUWsoFy9XwsvZazyIAzsGpVkpJz-w~iyY6FyMURRA7V58fHK8IzGEZy30S-KHBom9UFHVmaT2AeIXmrz5cep2PX7PqoVhd-CxQQg__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Click **Edit**.

3.  Copy the API token in the **API Key** field.

After you receive confirmation that the token is saved, the Greenhouse-HackerRank integration is complete. This process is usually completed within 24 hours.

**Step 7 (Optional): Add a user to the Greenhouse - HackerRank Integration**

After you complete the Greenhouse-HackerRank integration, you can let other users integrate Greenhouse with HackerRank using the same API key.

To add a user:

1.  Log in to your Greenhouse account using your credentials.

2.  Go to **Integrations \> HackerRank**, or open the [HackerRank Integration](https://app.greenhouse.io/partners?partner_type=integration&partner_id=45) page directly.

3.  Click **Edit** and copy the existing **API Key**.

    ![5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2Fe52b117f-c818-4ac7-9ce8-9d3ef06cc509-1762500306383-5.png-d9f21ee7-b133-478e-a1dd-356262069669?Expires=253370764800&Signature=UFPQMDwBr70B4ezNbPFQlZSo1Tk0aRXbo6diYrSA7c-NAOnzcDG02xd1gtY3birN4~UgzycooWAgOeWIx3PQX99cCX7BCSlVWVqoTSY3pKlGovhqybuV9BTMXFFRQvsLC4ymwYtMyTyLqPdSgSv97Yqlar1uPqGiSZvc4-nZ-I7r35XLk4f-2fk~0xqYySiwOkL6KTHgZT7MiRjFJKY1knFD1hlmMRw9vs-p7i1woWaT0LZPDSMO36hmYUQpd6Oq~L51KRB5748tj0Cx3NLlomx1Yy-eHsobP-bIVAHTVJNqMdSYJVHfhbf6OFWAj32vsg5DAzwGRrZlbANuIhrEgA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Share the copied API key with the user you want to add.

5.  Ask the user to follow Step 2: Add the HackerRank API token in Greenhouse to add the API key to their Greenhouse account.

# Glossary

- **Harvest API:** Greenhouse’s data-sharing interface that connects partner applications such as HackerRank.

- **Admin User ID:** A unique identifier for your Greenhouse admin account that specifies who creates the integration connection.

- **API Token:** A secure key that allows Greenhouse to recognize and authenticate HackerRank’s connection request.

# Frequently Asked Questions (FAQs)

**Why is the Greenhouse Integration page not showing in my HackerRank account?**

You do not have admin access to your HackerRank account. Only admins can access the integration settings page.

**Why don’t I see the ATS Settings updated message after I click Test and Save?**

Verify that you entered the correct Greenhouse User ID and Harvest API Token in HackerRank.

**Why am I the only user who can’t send tests through Greenhouse?**

 Check the following:

- Your HackerRank and Greenhouse login email addresses match.

- You have a Recruiter or Company Admin access in HackerRank.

- You have **Send Test** permissions in HackerRank.

- The test you are trying to send is active (not expired or deleted).

\
