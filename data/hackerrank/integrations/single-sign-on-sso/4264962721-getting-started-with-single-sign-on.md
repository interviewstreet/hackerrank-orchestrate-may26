---
title: "Getting Started with Single Sign-On Prerequisites Steps to enable SSO SSO endpoints Updating certificates"
title_slug: "getting-started-with-single-sign-on-prerequisites-steps-to-enable-sso-sso-endpoints-updating-certificates"
source_url: "https://support.hackerrank.com/articles/4264962721-getting-started-with-single-sign-on"
article_slug: "4264962721-getting-started-with-single-sign-on"
last_updated_exact: "Mar 25, 2026, 2:31 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Getting Started with Single Sign-On Prerequisites Steps to enable SSO SSO endpoints Updating certificates

_Last updated: Mar 25, 2026, 2:31 PM (Last updated 1 month ago)_

**Single Sign-On (SSO)** is an authentication process that allows users to access multiple applications with a single set of login credentials. HackerRank for Work supports SSO to provide a seamless login experience and is particularly suited for larger teams. This integration simplifies access management by reducing the need to handle multiple credentials.

# Prerequisites

- You must have **Company Admin** access.

- Your organization has an Enterprise plan with HackerRank.

# Steps to enable SSO

1.  **Access SSO Settings**: Navigate to the top right-hand side of the landing page, click on the down arrow under profile, and select **Settings**, followed by **Single Sign-On**.

![2024-09-04_12-43-58.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046391640-?Expires=253370764800&Signature=rbFiFATLIU74-6m8OPrtnSO7gUElmCXaKZ194H6vtREI05K3p4mImbf93BvUFQSBmSCYtl-CVpPpW-KeB9z00WPXcTHub12zHI~knDYJDSYzc3Ppx96sPQut6YQBCWw3V7TwJWYpApVQ-0CgjwlRxMLTCgTjCFrfw0BUzL-JzThXFZFtPo7ll0LQxMptKNCFj11Umb7P0htr0ODGsAvzkM9oufYJtNzvDHzoE72V9mxwl8FGLtlgElqp86KOREjenzkwDRsb6pAt7jicfV6u6vIa1kgYfUgOYwmlThewYruGyVhLReK6PladQNy5cMxvhXeB4A1Y032h-AbGZ0p3xg__&Key-Pair-Id=K3NV4LZ47N8M46)

2\. **Configure SSO:**

- Copy the **SSO Unique ID** and add it to your Identity Provider (IDP) app (e.g., Okta, OneLogin). 

  1.  Use the IDP app to generate a metadata XML file.

  2.  Click **Upload Metadata** in HRW and upload the XML file. Once uploaded, a metadata URL will be displayed.

3\. **Enable SSO:**

- Test the SSO setup by copying the generated URL and opening it in an incognito browser window. You should be redirected to your IDP sign-in page. Sign in and verify that you are returned to HackerRank.

- Once verified, click **Enable SSO** to enforce SSO for all users in your organization. Going forward, all users will be required to sign in via your IDP's login page.

4\. **Disable SSO (Optional):**

- If needed, you can disable SSO at any time by clicking the **Disable SSO** button, which is highlighted in red.

![2024-09-04_12-34-00.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735004457388-33046957727379-00ff24ff-6911-4f36-9d2f-9ab12ce2ac9b?Expires=253370764800&Signature=hR1P0NKbVj9VG2lZfFgw0a2njq6nCB46P8VTi73QYa7ri6~f1--kjzNLPzX89MV6dP3E4~VH-tdbchUBGXebevu5Zi57SMjcR7--KJ1DczpThl35zVI5s-Q1OaEsOMo~u~IoV8riIX5rr5~FvlmSV4HlG9D2QI2saowp9wFnz1DbwfKEn5nZsXt7REr-OpFRS6mp1Ad~Cu7rhmZx2pcdmxjRnCLW3jmJEqaOJz-qKWU-TIS1wIGcTrPaxvx3qiLqEnzeHguRU04vDR7SYW3WdN6RQ~~mn~A9zhKO86qWXHzxX534YjiyNRFqxY8DXGJzaGcAULWubWH31lF5-o6ajg__&Key-Pair-Id=K3NV4LZ47N8M46)

# SSO endpoints

- Entity ID (Metadata URL):\
  `https://www.hackerrank.com/x/api/v1/sso/saml/[company_unique_id]/metadata`

- ACS/Reply URL:\
  `https://www.hackerrank.com/x/api/v1/sso/saml/[company_unique_id]/acs`

- Sign-on URL:\
  `https://hackerrank.com/work/home`

- Logout URL:\
  `https://www.hackerrank.com/x/api/v1/sso/saml/[company_unique_id]/logout`

For example, if your company's unique ID is `fj0iolfc03n`:

- Metadata URL: `https://www.hackerrank.com/x/api/v1/sso/saml/fj0iolfc03n/metadata`

- ACS URL: `https://www.hackerrank.com/x/api/v1/sso/saml/fj0iolfc03n/acs`

# Updating certificates

Your IdP metadata includes a security certificate. When a certificate expires, upload a new metadata file to the [HackerRank SSO Page](https://www.hackerrank.com/work/settings/sso).

To avoid disruptions, upload a metadata file that includes both the current and the new certificates before the existing one expires. In this case:

- The old certificate remains valid until it expires.

- The new certificate takes effect automatically after you update it in the IdP, and the old certificate expires.

This process ensures that users remain logged in and prevents unexpected login failures.

#### **Note:** 

- HackerRank can only accept a user's email address. The SSO setup requires the user to define the SAML assertion with the correct data. SSO will fail if anything other than the email address is provided.

- New users will not receive the usual welcome email to set a password once SSO is enabled.

- HRW accounts for new users will be automatically activated, and they will be redirected to the SSO login page after entering their email addresses.

- You cannot reset your HackerRank password when SSO is enabled. Instead, manage your password through your identity provider app (IDP).

\
