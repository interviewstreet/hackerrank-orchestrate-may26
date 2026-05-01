---
title: "Just-in-Time (JIT) Provisioning for HackerRank SSO"
title_slug: "just-in-time-jit-provisioning-for-hackerrank-sso"
source_url: "https://support.hackerrank.com/articles/8000473667--setting-up-hackerrank-sso-with-just-in-time-"
article_slug: "8000473667--setting-up-hackerrank-sso-with-just-in-time-"
last_updated_exact: "Mar 25, 2026, 2:37 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Just-in-Time (JIT) Provisioning for HackerRank SSO

_Last updated: Mar 25, 2026, 2:37 PM (Last updated 1 month ago)_

Just-in-Time (JIT) provisioning allows organizations that use Single Sign-On (SSO) to automatically create and manage user accounts in HackerRank. This feature removes the need to manually preconfigure accounts. When JIT provisioning is enabled, users who sign in with SSO for the first time will automatically have a HackerRank account created and ensures secure access management and a smooth onboarding experience. JIT provisioning does not trigger for non-SSO logins.

## Key benefits

JIT provisioning for HackerRank SSO provides the following benefits:

- **Automated account creation:** Users are granted immediate access to HackerRank upon authenticating via SSO, eliminating the need for IT administrators to manually create user accounts.

- **Improved security and compliance:** User access is managed by the organization’s Identity Provider (IdP), ensuring compliance with access control policies.

- **Seamless user experience:** Employees can use their existing corporate credentials to log in without requiring additional usernames and passwords.

## How JIT provisioning works

The following steps describe how JIT provisioning functions in HackerRank:

1.  **User initiates login:** The user navigates to HackerRank and selects the SSO login option.

    **Note:** JIT provisioning runs only during SSO login. If users log in without SSO, HackerRank does not create user accounts automatically.

2.  **Identity verification:** The login request is redirected to the organization’s Identity Provider (IdP), where the user enters their corporate credentials.

3.  **SSO authentication:** After successful verification, the IdP sends a SAML assertion with user attributes to HackerRank.

4.  **Automatic account creation:** If JIT provisioning is enabled and the user does not already have an account, HackerRank creates one automatically using the attributes provided by the IdP.

5.  **Access granted:** The user is logged in to HackerRank and can begin using the platform immediately.

## Prerequisites

- Your organization has an Enterprise plan with HackerRank.

- You must have an active HackerRank for Work account with Company admin access.

- You must [configure SSO using SAML](https://saml-doc.okta.com/SAML_Docs/How-to-Configure-SAML-2.0-for-HackerRank.html) before you use JIT provisioning.

## Enabling JIT provisioning in HackerRank

To enable JIT provisioning:

1.  Log in to HackerRank using a Company Admin account.

2.  Go to the **Settings \>** **Single Sign On**.

3.  In the **Just-in-Time provisioning** section, enter the email domain(s) that should be routed through SSO. For example, [hackerrank.com](http://hackerrank.com).

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1749119636434-image.png?Expires=253370764800&Signature=VgIERAE~IkI4n1KxOxO~nbqRC6MZ-m0cOXZRi46k1ESb-RzXAaJjBmzGoQ-h-CLQn9PgLt5ofAqXXk3fnBDp1FjxeuPQO6~F-d23fYCQHtKQVIvBBG7L6ETLNjXF6rnn5gxPJ-WGhmpHnIwU0l7B9PrXnjXbVJxyFTaUldBEe5~VC81haR-rRQ7bKq0uAFGl~yQaoOCDa~53~gNW-iRft~7zl6lICuN8HXFbRX5OodAjGeGaCNhW-G31J5CgzUmP4~suDfzoqTSc9FBwGeCDDj6YDFnih7YdlxNkzSZLDZ16hMXBGgnCY8qIPKRVb7U0cqfoaY-aIfmanwUVfKT8YA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select a default **role** and **team** (optional) for new users.

5.  Click **Save & Enable**

**Note:** Ensure that your IdP sends the following attributes in the SAML assertion:

- `email`

- `first_name`

- `last_name`

## User attributes for JIT provisioning

For JIT provisioning to work correctly, the IdP must include the following user attributes in the SAML response:

- **Email:** The user’s work email address. This must be unique for each user.

- **First name:** The user’s first name

- **Last name:** The user’s last name

- **Groups** *(optional):* Details such as user roles or departments. Used for organizing or assigning roles.

## Configuring JIT provisioning with common IdPs

The following sections describe how to configure JIT provisioning for commonly used IdPs.

### AWS IAM Identity Center (AWS SSO)

To configure:

1.  Log in to the [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/).

2.  Create or configure a SAML 2.0 application for HackerRank, and set up the service provider (SP) details.

3.  Map user attributes as follows:

    - `email` → Email

    - `givenName` → First Name

    - `surname` → Last Name

4.  Enable JIT provisioning in HackerRank and verify that AWS IAM Identity Center is sending the correct attributes.

### Microsoft Entra ID (Azure AD)

To configure:

1.  Log in to the [Azure Portal](https://portal.azure.com).

2.  Go to the **Azure Active Directory**.

3.  Create a new **Enterprise Application** and select **Non-Gallery Application**.

4.  Configure SSO using the SAML protocol.

5.  Map user attributes as follows:

    - `user.mail` → Email

    - `user.givenname` → First Name

    - `user.surname` → Last Name

    - `user.groups` (optional) → Groups

6.  Enable JIT provisioning in HackerRank and verify that Azure AD is sending the correct attributes.

### Google Cloud Identity/Google Workspace

To configure:

1.  Log in to the [Google Admin](https://admin.google.com/) console.

2.  Go to **Apps \> SAML Apps** and add HackerRank as a new SAML application.

3.  Configure SSO URLs and the service provider entity ID.

4.  Map user attributes as follows:

    - Basic Information \> Primary Email → Email

    - Basic Information \> First Name → First Name

    - Basic Information \> Last Name → Last Name

5.  Enable JIT provisioning in HackerRank and verify successful sign-in using the mapped attributes.

## Troubleshoot JIT provisioning issues

If users experience problems with JIT provisioning, try the following troubleshooting steps:

- **User Not Created?**\
  Ensure that the IdP is correctly configured to send the required attributes.

- **Incorrect Role Assignments?**\
  Confirm that the IdP is sending the correct group or role information.

- **Login Failure?**\
  Review the SAML assertion logs in your IdP to verify that the authentication was successful.

If you need further assistance, contact us at [support@hackerrank.com](mailto:support@hackerrank.com).

\
