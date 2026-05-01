---
title: "Setting Up SCIM Provisioning with Okta"
title_slug: "setting-up-scim-provisioning-with-okta"
source_url: "https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta"
article_slug: "3939437783-setting-up-scim-provisioning-with-okta"
last_updated_exact: "Mar 25, 2026, 2:39 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Setting Up SCIM Provisioning with Okta

_Last updated: Mar 25, 2026, 2:39 PM (Last updated 1 month ago)_

## Overview

HackerRank enables you to set up provisioning through your SSO by configuring the SCIM protocol.

As an identity provider, Okta enables you to provide SSO access to the cloud, on-premise, and mobile applications. Once you sign into Okta, you can launch your web applications without re-entering your credentials.

This article guides you on how to configure SCIM provisioning with Okta.

## Features

The following provisioning features are supported:

- **Push new Users**

  - New users created through Okta and assigned to HackerRank for Work are created within the application.

<!-- -->

- **Push Profile Updates**

  - Updates made to a user’s profile within Okta will update the user’s profile in HackerRank for Work.

<!-- -->

- **Import New Users**

  - Users created within HackerRank for Work can be downloaded and turned into a User object in Okta.

<!-- -->

- **Import Profile Updates**

  - Updates on a provisioned user’s profile within HackRank for Work can be downloaded and synced in Okta.

<!-- -->

- **Push Groups**

  - Groups are provisioned as Teams and members within those groups are mapped into the team on HackerRank for Work.

  - Only **Add** Users to Group is supported.

<!-- -->

- **Silent Provisioning**

  - Users are silently provisioned through Okta, which indicates that new users will not receive Welcome or Activation emails.

**Note:**  HackerRank accepts only the user's email address. In the setup, the user defines the SAML assertion with the necessary data. HackerRank SSO fails if it receives anything other than an email address.

## Prerequisites

- Your organization has an Enterprise plan with HackerRank.

- [Configure SSO using SAML](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-HackerRank.html) before setting up the provisioning with HackerRank for Work

## Configuring SCIM Provisioning with Okta

The process of configuring SCIM Provisioning with Okta includes the following:

1.  [Generating an API Key from HackerRank](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta#generating-an-api-key-from-hackerrank-18)

2.  [Configuring Provisioning for HackerRank](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta#configuring-provisioning-for-hackerrank-20)

3.  [Importing Users](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta#importing-users-23)

4.  [Provisioning Steps](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta#provisioning-steps-27)

### Generating an API Key from HackerRank

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon on the top right corner of the page.

3.  Click **Settings** and click **Single Sign On** on the left panel.

4.  Click **Generate Key** under SCIM Protocol.

    ![integ_scim1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046459697-?Expires=253370764800&Signature=kvXbQBb2M7OVcTSbxEvQqEmz39~nSBVd8-ViEHPVYErKQxSAYlCp~Z1Ckk5hGQOt0QtsVSqPyWWEhYuIV-CsLszc0fQ6E3~4Tzo4sOnLXjWTKQqG7TZbSf8~HB~nwTRAimTLm6qPYD-dXw9UTPnZTuynHUVEVDUw8B8lRx2kGylCbjPza7UOagIrxHWC0QkQU0Pmd0Vsc~dLYAF57BlO8LZB9H9kL07mpi0t-aWxSkPzOA1yZENuwNuyVfOg~zyPPjIQWuWCrQP8T4cPGL65Kc1cVwNH-WFyvLXtSNQbNb3tJmqiuSFKTB0cxZARzW6GxZjBNkw1UfkJ8KfsEO5oSQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Copy the API Key that is generated.

    ![integ_scim.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046460303-?Expires=253370764800&Signature=uikxIoUpic6WP7pxazTg50HQove13bpG3DTtl08faOhj9xZuVronnrUqXfOdbwqhsT8OZrurtfLem04Scly6dJ9sg0vRjNjLw87CabySAvlNSUiy8yeGbnBCTr153bzRrSVVDIx6SJ9lubT4-WJ6-O882p4C~y4uYwuQUTPU6nYUnFVva~Kwr17FL8OoYx1cLuGlnlcpS1YkskbTQaKHLwYxafgZqzNIHj0lWpkFCjRVNw6xz5k5ehzhbDs7HD~bSzlnE5IyNuXAVXn9UuEk4oEmkY9W3z-aTJS5Btoz4DYtk0yCwoF~XXHpmNMA8McBpCqcl1XcVf2JG3nZLJxdMQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### Configuring Provisioning for HackerRank

1.  Click the **Provisioning** tab in the HackerRank for Work application in Okta.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046460644-?Expires=253370764800&amp;Signature=Lt~NECniytIRz9-su3ehrlvZbUOgOiAc4XgsDID92V-1z69m8JLkd06vfIhPL-vJ8LjGRg25tSk2OJ9tdHg174j~xdUiY57hjylpXGgMv5QvH0yeo0~NjqKZqtV-6hy6yvxeVX8mQqbOg1VmHbwqnp7hZS0fDaUEgHWHhJiibzwW3CIUHphuSNzj5IVCXiGWaCQDS2Jw-CEuWvD39qxqDhfYvYtMJwpotRfU6PyYgDMzyo12o0EyH7l87HsXvzuv1V2phJKHiOOSZXt74YkvCqG7QiZ8J8FcUiQzSZSQE19zVSPNRyszXo3kp-Av9BCrfZqXKf8ZnQfINff8aJznZw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

2.  Click **Configure API Integration**.

    ![image19.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046460987-?Expires=253370764800&Signature=YWBQqLNgzZjNYElp~tWF9Kf3zNtzlC~Yt5dcqfChql1EwZFHHUZpRfU9OXs4fJ5h5S7gJ~kpkb03YutoN5zGsaoGBdoDCGwdTu0Bd54KDzRLtiPJAt6Sf-9zf926qXa1r00forirHUfp893tl6dylLWcd89a~NmSGVHpDX2rRo9MDnSeAQowciB-3xvkWb6UL3tr6l0r1N8qy3-jf06OvlTMVaUESJdTBbbKhDTP1DzudZQbyIzckHLFj9nHyX9kmdHFppMGebb5gti3qz6fNbsa48zV46Yym3EmAmJjdZqwQqZ-Kj~qw~CnHtlrOsWfeIf2GCwHLrUG2kvcIA7n3Q__&Key-Pair-Id=K3NV4LZ47N8M46)

<!-- -->

1.  Select the **Enable API Integration** check box.

    ![image1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046461375-?Expires=253370764800&Signature=HoT5gymVwftzhk08ncMdBKBVC2~oyYbeZx6z9yskdOGru0eEn~CDbxvnNV6e1yxXnvJS5sO3b3kyU8qs~nqyKRUSy54sFuNZK3nu-T5UqfHOz1H8Q1iPieZNN4MUh2H2eKto~TJoD4e2iyvq~XK5ivZSjUz6XJ-33gmZw-PZ6yNbtpGg6ntu7LZAWQadXqxjpSYrKpxWRAWEqlbkgJb~qYd6jyVGUrfBWwysdWBN3ff0n30ZQA-O4iNWUdyqxcp89D9bQonJzhzZCBDy2YT-da3FVcCGCr8ewLKciSvPu6atXsXVRA2vW08ZWQMbD9hN4sVWzyGQm8hVHClDlid7lQ__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Enter the API Token generated from HackerRank for Work in **API Token**.

    ![image8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046461741-?Expires=253370764800&Signature=aWYfgNxH7umlnW~wcxfbygFx3qKf2zuoeqdhbblSZEMn1zFhC8AYtkk1HmZ3QO5s6GT3UbC2F9BrZYGpjaJDbWnfBZ5Efwbu8VxFulipBibn82aaTemXDQELokMdRnMzPqtPYnIpDF9~xCrMVJ8CZXS6xsfJ34kJzjELqpKzjO4WRxyAuoaS4T5z5-5X7iIM519B7fzOA1aDxERXWKtCblOdWvlO-eG10rjieDgku~xvHU1n8oXhY4RmcC1nDCNKs3~w1D5qvTVngKLN-s3Sb2w8CPvj48X~5DqL6xcIVJ9Pb8ohBERRjuT~QxnMTytbZbKcswbHBsBo33yTnRxeYQ__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Test API Credentials** to verify that the token is valid, then click **Save**.

4.  In the **To App** option under the **Provisioning** tab, select the **Create Users** and **Update User Attributes** check boxes.

    ![image7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046462206-?Expires=253370764800&Signature=PmMFSyLJxVMXGyhvw45tC8IIdbHVW3mqNweut~0wW7lwPmYxE5pQD45O-YOXuePQOIWaOdtEXic7XTccZ9X~qYNvmtD9JctOlkUbaV5Z545gfX6dln2t0bnEBnyJ1AF6F5ZS185Yz2nU~auGc~f5ohg-51gDveSsZWCUBlUylLLw7styJsLSrD1lRFGb088ylM-3xVKOsOZxhJsODw3YjFrqNtjCShILDe7AJgFNvgXH2Mnd4MXRnxVXfKh7e2n1LUD2jVJ71l63JmSUWWVk~Ool-NlvYrm3g2rwjrqMU0mdO3Gf5x0isa59BY4NRW0KfT~0GlvPQ9P78ATNKgXYYQ__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Save**. You can now begin provisioning users to HackerRank for Work.

### Importing Users

The Import Users option helps to prevent overwriting existing permissions for users that are already created in HackerRank. This option pulls users back into Okta to keep your directory in sync.

To import users:

1.  Click the **Import** tab in the HackerRank for Work application in Okta.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046462565-?Expires=253370764800&amp;Signature=oyQUNGVnHUGZSUb2hmgS4ENmy2XiBGHjd5pQ2p2jurHMtQwgOuOiVhPlpzGp0mrCD3yoLob~e1EGAUuudAZFAfJT-KyM3iH6IdZXQa5ERSTI1LsT4sDCvO5Jw-sBl2bvXVrtvcc4sRXHPlUljzWhF-cB1HY-X0VaaFv2x0lEaqLgEUEee5g965gG9xut-aB0AC4YigRMciQxGmu8uJ1c2lM2EWmL5JHsB-vDo99AyGnuKMeSz1uDjK256F-5mEljUU2kdT~dTLGcqB98lr5OQCxhOGoSMsAn6NKehCs6SK8~2XeEv4a-xlUmLuWURZad0tQa~l3Z-hdIqUVB-KYtog__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

2.  Click **Import Now** to pull the list of users from HackerRank for Work.

    ![image27.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046463244-?Expires=253370764800&Signature=mJzGvS1sFr8nTvluT9ni2G9mZeKT4LUz8KqtvaYU1bYUiNSQS6Pekm0c8Cw1ivajBgqWNmmOOkDGZaYUFb3X0Kf-GS2WYpOvS2PFbQAeeaFWZF~o7iHhmtpamNYZ7vtNKj1jl-qgucQUvxUDmYy8x2w2~XqPkjjmPS2TDVLNpTTzPhvKoErnCS-LHu0YFA6~O2DaG3frFr4dIxtVEaI9xCvDwcjku6DDk-Kmj-CtBoEPtM9SfMOaryIMsL7-QG-GBxqBP8syTsFLMkOBpbVVN3UCh44ZCkQ7CPqeeknSDgxGj7lhz7tEEuYp3ZL2cStnQjhYTfP8M-Sbv5eFaNdR4A__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select the users to be imported and **Confirm Assignments**.

    ![image23.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046463587-?Expires=253370764800&Signature=CGhNZRmFPrbA84hFnkUO8pxJPoIEDdhtnEsqW8XNO7IKEcyJ2YVgDs7FUzhgvnNYoggfhtnrk1wVnzwYYqAW9pCtlbKT1LsTlOfJDDdT6-kdB5JB69G~mdYSag3exwcuhdNEsqKOLWAiXGy2Io4sPt-lz1F9L13wwYzwnd2YUVnjUdDGycdPv-0KiOoF5CcRsLvxqYzqEMEojcWWPJkAU5dAPsKRCj0uRYiorGoSu5p533lgduU4cWKzr6RdCiaTcan2NOSoSH5ToVkQfM~ZBcy-AGxD5Y~UJxd1fg5zoEw~cYJqXFL7KYAFK8qa6qFCcnvaADIsiOe4PwH-X4WcMQ__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  If users in HackerRank for Work exist in Okta but are not assigned to the HackerRank for Work application, an **EXACT** label is associated with the user. A new user is not created, but the user will be assigned to the application. 

5.  The Confirm Imported User Assignments dialog box appears.

    ![image26.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046464005-?Expires=253370764800&Signature=qn9-2hnf7ne3GDjT7P5aIwq2zjrtGlRkTcjjNMFdMqxp227cOirprLGphkDj7Z6QVN0xhb~IO0tjqFqD-7i9QxCWcW37aQljvLBBw1QuQf4coJ7TSga8x3l7rDW4p47f~eTitDuz3ajR4Youyh-VkuWbrgUmAbEEbV967ivbzuCvhufKfHqAbLjzSftLejjxsHfGz2nYGQleKJB~BbACzpZDeXJK2nubI6RS0YrkdLOXvVungLzc-9cU~RVL4rBQI7LtTXCbxVdf0cWCcgDMfss9ijICc7e9zgnUcVp8PMofjXhnXuYgUjiFdzFCLIilgpO0QzKfV1CCy4fP0MHytQ__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Confirm.**

7.  Now, the user appears in your directory.

    ![image15.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046464402-?Expires=253370764800&Signature=tNqOiF07Ouj0avAjEq6bXLo7esy1MjNEOovsH9syjsycgko0q0jHXimmmyYFCxyndPtHQLhAkZk2UMiQf-8TCv2pCfnLX1DsQMFTScdsBY0wCwLultVyCWT9W~ko7voHEMd2t4tVnZmktVAGy8CMl-X~QWB1WpgSXwmGvx2j0z4chZaNHA3yjJJMJI-iqR-xmMoPdZCridqyjzyR7I61o3KuoNGh0Hzjl6vvZVmVURoXHw4E~uzKskaoNBvuh8kbWxmzxNL24KARQUjrgHRFhs5yfC--sTHsaPhnF~RogRSFbnowkR6hDKGPOgVHRAHm4NfvgnVWtCxqoSyBe-3MsQ__&Key-Pair-Id=K3NV4LZ47N8M46)

8.  You can navigate to the **Assignment** tab to verify the newly imported users.

### Provisioning Steps

Perform these steps to create users in HackerRank for Work:

1.  Click the **Assignments** tab in the HackerRank for Work application in Okta.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046464745-?Expires=253370764800&amp;Signature=ASSV-PoAOT2B~e0iTUkQPimAAh1Sp2yAampPJhaoU2Dbj04CTePzcsp1bK-sTXFKKe3kMUuFj~CW~Fz4mYxF6euOBoACoKZRiJ-5tidSkLLWvI-z5pBzlXvLOmF9jvY-8CTxEaDpSBy7cDiO5kBzqKASKLqeQg4Q~Zfe32qLj5GsPMLlvWhPOdIZ7rpLsNq1h9YZEptd0~bsq0lW3WzmgIpKd6UxFJ6EL96l85X1w0ViOrwzzeupi6mMtzHAwzzin-7BRsWu8M8N3x9bEFyItMBSka2isDhZAolyhWq0I02WZUzFDU-qfRHaxBUYz2i0n7u-u0NpWEuYgfwgobvDTQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

2.  Click **Assign**.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046465120-?Expires=253370764800&amp;Signature=hYx5cTFA6LYN3S2ZGWg4PhUGMgrRrnvp2bwij5NttPxue1OgcYv163BAozvnmTB1J~KKiHEM5HO2-Vo4ImpQsCwpUkEB~k89AouQwEzJXFTqIqWC3IBeRKRX3fIU0M3CFfxb7tkbjbE1W9f42QNXT6oVIxDlRLUIXicbszMFIQc3DoytSsGjiTNQHpatsXvoBZd0Ncj0~ON4DBMcB-eApcZ5sURlWmnVwnYI-oHjvYbFRMSBm97cAy2TmWOeyZwnLl~QrhjgJHdSDm406yufOQpp3GXgN481CnqpqIhtrf4VUwKyEKCRH5~48Y2q-Jd3s4fdKNxON~E4wyXSnLjzxA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

There are two options in this list:

- **Assign to People**

- **Assign to Groups**

#### **Assign to People**

Provision a single user.

1.  Click **Assign** for the user that you want to provision.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046465424-?Expires=253370764800&amp;Signature=V1axw7FE3syuclB9xlXckb6u1tZCzjmGmlwDdD3jzAmt2eRH3emFPwKl60laTsZf~X2GeNrkF3Omzx0f9zI7Dem-KjpG5E1dk0fMaauciSX78OAW-eWlggkAc47AyKU0mkbeFNk1QueSXHHWIpRhln7yJx7NiJ-A1skJ6p5tGBsXGsT1nUeA150Hfb1QEKdODg4BpL2LsXIbO41S0SD5cBYKj5if3OxkZO0df0xa0zs8dQxBF5RFY3TrALk~aIJUcol8bubT6AJomRe8uU425H~-0VstQQXvc6XAB5s3BmhOW1JZS1TNDBdW86pUj9dZB3pc5abA~N36vLTglALQww__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    1.  Enter the required attribute fields for these roles:

        - **Role**

          1.  Recruiter

              1.  Create tests, questions, and interviews.

              2.  Access candidates.

              3.  Send invites

          2.  Developer

              1.  Create tests, questions, and interviews.

              2.  Access candidates.

          3.  Interviewer

              1.  Create and give interviews

        - **Company Admin**: Grant the ability to override and grant more permissions for users in the whole company.

        - **Team Admin**: Grant the ability to override permissions for users within the same team.

          ![image22.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046465773-?Expires=253370764800&Signature=pUZrz4HA6ldMZJFwjK6mLtrQVgg8POAn92KNtiixVLgaG7dOyTEUZU9TDK-n7X3eD~uTG4IEjHPIq6~Xa859FxR1vUamnluumf-mOheO9qvzzecPRRJTLH~MFqAx7Bpsxa0aAQotYF-VCOl~Ho4l31H3uL00gDCm~SQ3WWzJmYOxtGdgDKs8NPnIZP1gaAevzyoqD2fWhp2uNgB5lls4oeZ4MgA0NN1skxo6k0NmhLvW-jbK628J3mHQW4WWxI5TjHSabILjBjrKb~us80Hu28hI93N9YNmgrWOTbnOU3f253GpyLTZdJa8ESFhpeuwKZ5ig7gYEd0S6sDrsNTd43g__&Key-Pair-Id=K3NV4LZ47N8M46)

    2.  Click **Save and Go Back** to view your newly assigned user.

        <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046466110-?Expires=253370764800&amp;Signature=BuZhR6mrmQq6RXJGasDmoxf~GXNcyfQpEdo8R5VrK3BEDJnsBGQZYVJN0GeSHzD2ZU5o1M7Kpfw5niY~YPaIjSk2thl33Bp3LRAfBwF~kDlwsqeuaSvzl069ZWRNUevWyCFR8dWg5o9ppmEMmli-aL-F0QgNk~kOPoBGX0jm6pZa8ZdQ-j9dI0-JbVd6Aazemefb4l4LCVwPrWhpl0WWQ~F~vgXcN3CWiHaucbHiNLMFJ8LMfz3KjBrGR7-uYzDeAzoKR0ksoeXPMpqt-KCQ7Nm73q41CRwN3q2L0qFHb6-XACloZ7RaUMsVQ5xh5MJLaHpNK7QYteS4dSCSgeoBtQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

#### **Assign to Groups**

Provision a group of users.

1.  Click **Assign** for the group that you want to provision.

    ![image25.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046466400-?Expires=253370764800&Signature=fsJCxTb-~6p7RR0-6URiTHZkYLdVplgyfAM6bvD53HQEpS7f5oCf~bAGN7hsfCSobG1zlKZECrTb4oeRs5JFECHZmKxqiCpMazehSK72IreDjLRBLhEhlcKjpP0b0e3VgOvtigL4uXvRDF1DGV1yV3hGijYG7rxVqB0j3DTlZEvjlHVcKhTNUFN8L3fXOW5MQ8nxObyaZ1dmvMZRVUyxpgpNFt3URkS0Uo5FCimdKmLjCiAPof-HhD8BSbA4IlV7LX9gLbA4N~idqZtoqmRAtnOfUac~H4jaCTtIaXv03FftX5iMdVj0azVM0pSdmF2kQN61AlgBT7vfCV96FnX6-g__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Enter the required attribute fields for these roles: (all users within the group will be provisioned with the same value for the attributes).

    - **Role**

      1.  Recruiter

          1.  Create tests, questions, and interviews.

          2.  Access candidates.

          3.  Send invites.

      2.  Developer

          1.  Create tests, questions, and interviews.

          2.  Access candidates.

      3.  Interviewer

          1.  Create and give interviews

    - **Company Admin**: Grant the ability to override and grant more permissions for users in the whole company.

    - **Team Admin**: Grant the ability to override permissions for users within the same team.

      ![image18.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046466749-?Expires=253370764800&Signature=KD1Ou8WCnV9G6BxC6EN81yKiB9YUWSu305SsC97wBDNaA49v9oUeJk7u65oH~P048lwnsQKKUfXJth8~lqL0MsKCj7wdRlDHDWNcQyjCPZAfWpVjgdAsFO2EaMfLItNQv0iszVGDtI-kgC1Gqfb-mMxxh-LwXPWS4Qng~MMKKJRJfbPCzQbwCPtIRDkrITyPJrs5v-4QX1EeoAbbTavmGh9P2tGNnw~QJWL9k3~pUKDyXHLFLrvmIpqze82PIOt5yk01N60etOKNM~1E0kc6WIdERZJoA-x7eb4d8HvoksSnCl76uLpxdb2uNiJVChzPmOKfjJH5O3b8SOrLiIk8YQ__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Save and Go Back**. Your group has been assigned to the application.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046467188-?Expires=253370764800&amp;Signature=pmk47aew-kqZrMUv0E74a2-QecFaN54xyUt2m1JRA0On0duFdptygBiiw1IX35GZHvd3a49p5fNwmaP84PqzMf~TpZMd6qp5Qr7OA096joaDHYz4GxMPEJFtY7MT9g7Zn~TGcxiZTs0FCdnvr8PQ1iV7-kCa351NikSjjy8SLD3zG8yaJ4On1YF-Dvy-gWP7asb~F5Xc7esYFD-jTUQj0xLWFDRtqLexhdLyaO9T3pf8-cHM7OQM6f7k8l9d9WbqPD7iZWY1bZ8Tpk42Nvc0H1otasRRbQ4BmqroEZdjzvay3D9bZYIM6mJdF6Jlia6LeiBnbPRazfsGlDtaxDnRgQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

4.  You can also view the list of users assigned in the **People** tab.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046467826-?Expires=253370764800&amp;Signature=QZLUHoh85vWusIIGZhTI2SBywVOPhErZlVUTzTOcR04vSxtGrNfoDNIH4Qx3Uu7dpP4cGIt40pZtJRmhleAVFE327B3RySRYQAVCASbhQqGSC730c-hUALcSIneAh2VgfnkHG3woW-w2vdnSvD0hmJPbjeJPLSf88-u88ztNMFLBAx3BL7p2l2FoBq7WOeDFTeWyLIPApO1cvZfq1yaFczWfccU85zuys-Hk9kCVI7g~l~RnZOd8SPLAt-BtZY5Te90dPOEjLO27dGb5QzgcNK~wtchxkEMgmO7SW9J-Fomnwxe0Sn1KbOwiClwvEH4WeoU2PyDhA-J1QavPyCdMNA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

## Migrating to New Instance of HackerRank

The HackerRank SCIM application is updated to provide a better experience to Okta users. The summary of changes is:

- A new attribute (Interviewer Role) is added

If you are a current user, you need to add a new instance of HackerRank in your Okta org.

If you already have an existing instance of HackerRank, follow these steps to migrate to a newly updated instance of HackerRank:

1.  Log in to your Okta org as an Admin.

2.  Open the Admin UI.

3.  Click **Add Applications**.

    ![image17.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046468246-?Expires=253370764800&Signature=uMCbEgK1XYSchqmdjCqxvNtZ29TrV~~Ato4ZYNAh0eu0qq603mRfZlexHKHLnKEql41F3ReEG3xWhFTeFVkW5fcShFnbsTs0RzodmmhsXREfhJNPgA9o~X5U6BgrJ96tfnOgf9NoWrtVhCkp~VRympOjviYV~NyKF6nS6f8Iy-I1ODV-uAToewObmzn8mYkXQ8w7s3-3JhPbLOZJHWci-PKJYBgryFb9NCJ4EJkb9UDrbOk0lEYuVGgXN5HkI6t1lxMPEFvQfW~~4W1ITB3YywO-qCLDekCLWbe416WJzN2diUqFjeHaM9jC-FapQ5fAq-EHxpt5t5uJ8Gjsd~aaSQ__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Add a new instance of HackerRank.

    ![image30.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046468602-?Expires=253370764800&Signature=MCeKKRq-rSYhlAuyxX0fvLCIYF7TSd9OYFkBzMipKwo71bI9b61SYjt7LuSwRVL29LpY815SjVqwgKRFhPlMLOZXa1Z5TQNN2ZUKFSVF8mCRXlKjkBPhV0HFn-Ah6nO6qKrdzk-fiUv6lgshZUili3Hmj7HFJmArBh~10ZOvfeZZRLvep~ofsY5kyLgyx7cvWtPr8WjecTyjSOpWzsvmJqQhKKbYFr6boRtt4MtJFwkUgdbQwsG~416aV3o5Js4NsEpIXNPV4kR9~J~fLOzHSJzWjvyPRh8xdEDNiNJ8FMWbSn1fcBtBdIKEhKBLermvggsLgbaox1yx8hHie4I1Tw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Configure the application including Provisioning.

6.  After SCIM Provisioning has been enabled, go to the **Import** tab of your new HackerRank app instance.

    ![image22.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046468915-?Expires=253370764800&Signature=lZpHxolisrPq6cOD6uJrl15FEv-IzX-XGNkpstyoZRGiRxAAp1I~Rk0zdaeiBlfMwR2tteld5xKLzHydTxuSc2nU2aormSYZXuadiQCsMgdZeIAGMcFOGgy9n2txqp4~8-40Dr6S2ddethNPcwCvGT5b~EbQ6WMBfjRe1JUcOcPUDPmqo5SIMYluOuwF3lUzdvEbxShAACurGq~ixw9Jet2Au8evRF~3nJQsq4MeumQjTpuS-UXzP-kXu3sPbwX07VjUtDdSZuM-O~YKDK9eMQEg1-gk6ZIH6byTUqJTO0FqvRAcp4UQdP6DG~c8Juv5od9JMUPacd3jzdqD2zYDOA__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Click **Import Now**.

8.  After the users from HackerRank are downloaded, select the users you want created or linked in Okta.

    ![image24.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735004983939-360055064434-01dd769c-bea3-4dfc-a274-679503f8ca62?Expires=253370764800&Signature=NBnuz2MhekMS7b7O30XpOhQD25Xt~EMqT6P3~6g77M6Be8nzbZzj9Bs0i45QDyOueFnJFlX~Dnt9WUVw29mryP-BZcdkHJtYrL97E7nbKX11FnV-lttxuQ5GeYPb4OoUlSU-9prLYYqsUL98aBbFOdfwa3iBsm05yravTcjCtcpwIm9pZ9GXfZ4o-K2z86kowaEA4fJiD8~q0qutY0~N4hb65g1on8G2J~i29-9weHYaf-KnjyYd-sDctPpuVyysIp29DTgrFsBa78U-jvAJ7IFfBZ6sH-d-Fa4Kx3GdtkF-mRgip2eWpQofWgk6f-OruX2ruLPh8iq2ntWYn6k3Vw__&Key-Pair-Id=K3NV4LZ47N8M46)

9.  Click **Confirm Assignments.** A pop-up appears to confirm with proceeding for the assignment confirmation.

    ![image32.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735004994600-360055943873-f67a248b-add8-48f4-8ae0-9a36ec01445a?Expires=253370764800&Signature=SC4xZClf8eMGZpXzAsyxXEOcfeQRb7nyOU5YtA6~cP20lZbnqHlN36ZVCR1FovGudWojOGLwqhNcyZEbE8TdPXf53S~kbtYC0x4h1ikus7bKbPIRD-eWHbxG8Kh0enFNilZv~eWhuqXAdN65LbAT-UEAM5c61WapPAxh7DcvuUpId87hY9jUSaTule6achLuM4A-OihCDOg412Bc85up4eQFKfk~q6R4pgUnIMLpNfw2-5qaxFZNw6PC8lAQbpVH4zCd6eff~w3qvbNekXnaOsDhQL2fKaHXYflbesZHB9IRFeFx0S1N1gORhilYdVX41ih~uGU333IfxlZM2xPWLg__&Key-Pair-Id=K3NV4LZ47N8M46)

10. Click **Confirm**. 

11. Navigate to the Admin Dashboard.

12. Open your previous HackerRank app instance.

13. Go to the **Provisioning** tab.

14. On the **SETTINGS** section, click the **API** option.

15. Click the **Edit** option and clear the **Enable API Integration** checkbox.

    ![image29.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046470055-?Expires=253370764800&Signature=aLLJrP0od8s-dwKDk6aOw5TqDA72UoF7x7XTYZ2D1m0OD4gp-jszm~9uTA6EXXMvNYMdlqHB8zys05~0~WS1NTdoFQoFOa5ysRRHrOc-BpT-tqBTg3yktTFHBYB-vDNDVaLMKJXKt3ldC1niXk5T1PJ~ZUrGWWiHr2KYUyWHczOFunhq-2kP2IQ8T5g81ICC5BG0eQwSKka~7eep9vkZFXUj3~Z8MTgOfXf4lolg~VJb7EwiUPnpZk3sb~CwJgWr2dyDeWppSWmDc4vtkrKHxHIBuoChYHQSBP02wxW8MhqjiD7AdZHDdSYBcZNfprTbIBuuylGXsuTkVO0roFsobQ__&Key-Pair-Id=K3NV4LZ47N8M46)

16. Click **Save**.

17. You can now deactivate or delete your previous HackerRank app instance and use the new HackerRank app you added.

**Note:**

- If you were using SAML as the sign-on mode for your previous HackerRank app instance, you will need to set up SAML on your new HackerRank app instance in Okta (recommended) or maintain the previous HackerRank app instance to ensure that the SAML functionality continues to work.

- If you were using your previous HackerRank app as a profile master for certain Okta attributes, you must set your new HackerRank app as the profile master for the same attributes. 

### Push Groups

To have access to tests and candidate reports, it is a best practice for users to be part of at least one team.

Follow these steps to assign your users to a team within HackerRank for Work.

**Warning**: Users must be provisioned to the application using Assignments for Push Groups to work. Group names must be unique and have not been created on HackerRank.

1.  Click the **Push Groups** tab in the HackerRank for Work application on Okta.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046470349-?Expires=253370764800&amp;Signature=WCSYKx9a72q1fp3gN3-i26UYgpcLGhgjcL0NzFrgO~mc6V6cxoFE8Aslc4WBueKTfGnfDPnYbA-hMypekkR7c8zz0zJUQuHCSx2k5QOrX~1ZheMxkd6nBjuYyyoNHV-WpQRTknZP9N5ziOnLRz6URbOQeH7-w5gUPsj9edCii~~bjhqlGm1Bboa1R53Qm-BBhkEX5sS7fKwwnpMPCHt-X10kzN6PDwIhEtLRIk0gi-Hwe3Hta0kxUnOs6rGO7Z1BsHCgjApSlzjU6IjyYe6ZVX9svSmti6Je1SjEdcW7fkaUE7XoOYjKWWx-Yp5VuBpav6WcHwpYJczWS0gANR-dhA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

2.  Click **Push Groups**.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046470710-?Expires=253370764800&amp;Signature=FTbNqqeq1bO1syOxBCaTv1mmepmW508TSh4UM1KFTQRkhjKH250f2iHA~n7TB8805bpx2Spnn10xjGal49WaCx6CqyOJqTzB9wM15G~G8ApuZpiuhxx9Aok4qJg~UruPs1Y-JZ4AqEbkhIxU6kUH4zNciADPfx52QqBac8PzBrsV6Dm6mD-Rh0XpugBUENWnvtr-JVfI5DOi4usi9Ce3L25tuDakCW7BjpD1drKYHRvlaI1xOeX5Ytg6ipGTCDpLx8jw3mkfq5Bv8mg-R2MqMFfzM7Wil-Sne04vtzikbrpGhC1KV2MSJrhCCgO~nO26to3NT1s8j0wKvwxCSbcDng__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

3.  Select Find groups **By name**.

    ![image9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046471125-?Expires=253370764800&Signature=FVNnTw3~qkXu5JnWID95OWnqQqbDMWIBUslZ71FxlkI5-Bt0hWkvxkLE4yulSHv2mHJxStWzaS~OFGRoIny6BbuitYGnTFT3Y6i4PM-c3JcHYmMKxLoYK7QF8-UjR3ZDSc4kg6qtj7U~UcREWnDY9DZ8Aza9aSdUI9ESjjTcRf-prSbjotSi9nb10bAmgxIW9U909LIICFQPNFn38ejs3HG5bZbWMuNZt~UZ~WLc2RA6kVgzMXn2x3WKX4BeX6dmx4ryWErknY4vRv3LIX8QlLxf8-rZOeOolIRkYBYiMNZvobNNFsn51WW6PPtZ~HUy4puxxa4-YMlqlAlM9acqQA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Using the search box, find your group

5.  Click **Save**.

6.  On successful group push, **Active** status appears for the group.

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046471471-?Expires=253370764800&amp;Signature=V0xHjKr4j7pMp8VT-8POGMe-EpoPBnn34Cj61I4d6WFepABLjW4kjAqW1Cy9q80TOdqxIWhwOtFLpGo26m6mAR59Q8NkvFBteZLcOVp~1QeNZfTY8jTY80cX8~9mjrLXQ7kiNIIkJsTf8OHLKxl8eXR6mJdemuhdDALBTxCc-gQ435EVrkZerSk523xMJkxT-DrBwPxpb-4by8J54dJHEU-g6rBNPmoTm1I9FZ6WdIU7s1d46lTpN8YjMOMpZL-Bty1QOsO7HHkmeNgAWcuAEBd9K0GBntGn27BFRAC9jpeLayIJq4oU1o2gvULHnehhPvklHH1-lE6eUuTwFErU3w__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

### Common Group - Team Configurations

- All users are in one group.

- If you want HackerRank users to be in one team and have equal access to all tests and candidates, push a single group that all users belong to. For example, *Everyone* or *HackerRank Users*.

- The group will be pushed and only those users assigned through the **Assignments** tab will be added to the team *Everyone*.

- HackerRank users are in teams according to organization recruiting.

- If you want to create Teams in HackerRank that correspond to organizations, divisions, or geo-locations, find the corresponding groups in Okta and push them as Teams in HackerRank.

## User Attributes

There are various attributes that you need to configure when assigning or updating users.

- **Username/Email**: The primary email is used as the username in HackerRank and cannot be updated from Okta. Choosing to update either username or primary email in Okta will not be reflected in the HackerRank for Work application.

- **Given Name**: First name of the user.

- **Family Name**: Last name of the user.

- **Role**

  - Recruiter

    - Create tests, questions, and interviews.

    - Access candidates.

    - Send invites.

  - Developer

    - Create tests, questions, and interviews.

    - Access candidates.

  - Interviewer

    - Create and give interviews.

- **Company Admin**: Ability to override and grant more permissions for users in the whole company. The value must be either *true* or *false*.

- **Team Admin**: Ability to override permissions for users within the same team. The value must be either *true* or *false*.

## De-Provisioning a User

You can deprovision a User by clicking on the `X` icon on the right of the User in each row and then confirming it.

![deprovision.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046471850-?Expires=253370764800&Signature=TtnzgGJz~nTk14nwjLZ-rNJXT5V9~fbZ5Kj2YlbLZALWAdXKKUm-ZjYU-qRh4vWcHnZTevVaCgFfIhN1JchuwLov-BN1q2ah6cbzX2BOjXXJ~fHhXOPm0bAlN0IBA8lXZQk7jz~iGXvlr-VNl7fkGcmWe2ciLkez6oZJBoeKgfqq6pzMRkFDmmtm~V-X0rmbkZ19pgHcLnjHVYtJn2Y6stATjDxf4vtuxnjTuat30koi6qX5NChkqSDArQVe3Em2xzmqb8CKixyXB9YTBI63LERz84djghXejqIFPcxBfbV9jv4pcSKIZVOVMVN35KeDoqR2FmxU8tDzFE~jxl5~4g__&Key-Pair-Id=K3NV4LZ47N8M46)

The resources, such as Tests, Interviews, Questions, and so on, are transferred to the Owner of the Company, and the User will be locked.

## Troubleshooting and Tips

- We suggest keeping Okta as the source of truth.

- This integration is optimized for creating users and teams. The following Okta features are not supported.

  - Teams in HackerRank cannot be synced back to Okta as a Push Group option.

  - Push Now functionality.

  - Delete Group in the target app.

  - Remove members from the group.

\
