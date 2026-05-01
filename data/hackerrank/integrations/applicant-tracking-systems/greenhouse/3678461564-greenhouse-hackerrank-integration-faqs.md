---
title: "Greenhouse-HackerRank Integration FAQs API Token and Access Tests and Interviews Common Troubleshooting"
title_slug: "greenhouse-hackerrank-integration-faqs-api-token-and-access-tests-and-interviews-common-troubleshooting"
source_url: "https://support.hackerrank.com/articles/3678461564-greenhouse-hackerrank-integration-faqs"
article_slug: "3678461564-greenhouse-hackerrank-integration-faqs"
last_updated_exact: "Aug 1, 2025, 2:57 PM"
last_updated_relative: "Last updated 9 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Greenhouse"
---

# Greenhouse-HackerRank Integration FAQs API Token and Access Tests and Interviews Common Troubleshooting

_Last updated: Aug 1, 2025, 2:57 PM (Last updated 9 months ago)_

This article provides FAQs and troubleshooting steps for common issues encountered while enabling and using the integration.

# API Token and Access

**Why can't I view the API keys in my HackerRank for Work account?**

You must log in to **HackerRank for Work** with a **Recruiter-type** **Company Admin** user account to view the API access page and generate the Greenhouse API key.

Refer to the **Prerequisites** section in the <span data-name="page_facing_up" data-type="emoji" contenteditable="false">📄</span> [Greenhouse - HackerRank Integration Configuration Guide.](https://support.hackerrank.com/articles/1406188460)

**How do I reset my Greenhouse API key in HackerRank for Work?**

1.  Log in to **HackerRank for Work** using the company admin user account with the same email address as the Greenhouse user account.

2.  Go to **Settings** \> **API access** \> **Greenhouse**.

3.  Click **Delete** to delete the existing key and click **Generate API key** to create a new key.

4.  Add this API key in Greenhouse to enable the integration.

    Refer to the<span data-name="page_facing_up" data-type="emoji" contenteditable="false">📄</span> [Greenhouse - HackerRank Integration Configuration Guide](https://support.hackerrank.com/articles/1406188460) for detailed integration steps.

**Why am I unable to access or send HackerRank Tests from Greenhouse?**

To use the HackerRank–Greenhouse integration, you must have user accounts with the same email address on both platforms. This is the primary requirement for the integration to work correctly.

For example, if your **HackerRank for Work** account uses the email address `jackpeters@hackerrank.com`, your **Greenhouse** user account must also use `jackpeters@hackerrank.com`.

You must log in to HackerRank for Work with this email address to:

- Generate the API key required to enable the Greenhouse integration

- Create and publish HackerRank Tests used for candidate invites

- Create email invite templates for sending Tests from Greenhouse

Alternatively, you can also use the HackerRank Tests and email templates shared with this user account to invite candidates from Greenhouse.

You must log in to Greenhouse with the same email address to:

- Access HackerRank Tests and invite candidates.

- Generate interview links.

- Log in to HackerRank interview and conduct interviews with Greenhouse candidates.

# Tests and Interviews

**Why do I receive an error when generating a HackerRank interview link in Greenhouse?**

You may receive an error due to one of the following reasons:

- You are not logged in to Greenhouse with the same email address as your **HackerRank for Work** account. Both accounts must use the same email address to generate an interview link and access the interview session.

- The candidate’s profile in Greenhouse does not have a valid email address. Update the candidate’s email and try generating the interview link again.

**Which HackerRank Tests and email templates are available in Greenhouse when inviting candidates?**

All the Tests and email templates owned by the user who generated the Greenhouse API key are available in Greenhouse. You can also access those Tests and templates which are shared with this user account.

For example, if you generate the API key using the `jackpeters@hackerrank.com` account, you must log in to **HackerRank for Work** with the same account to create the required Tests and email templates. Alternatively, you can use any Tests and templates shared with that account.

**Why do I see an error in Greenhouse prompting me to publish the selected HackerRank Test before inviting candidates?**

You see this error because the selected HackerRank Test is in **draft mode**. Greenhouse allows you to invite candidates only to **published** Tests.

To fix this, log in to **HackerRank for Work**, open the Test, and publish it. Once published, you can return to Greenhouse and send the invitation.

Refer to the<span data-name="page_facing_up" data-type="emoji" contenteditable="false">📄</span> [Draft Mode of a Test](https://support.hackerrank.com/articles/2464685918) topic for information about publishing a Test.

**Can the email invite template include name placeholders?**

Yes. While creating an email template in **HackerRank for Work**, you can add the Candidate name and Recruiter name placeholders in an email invite message.

Refer to the<span data-name="page_facing_up" data-type="emoji" contenteditable="false">📄</span> [Creating an Email Template](https://support.hackerrank.com/articles/9684438314) topic for detailed information.

**Who is treated as the Inviting Recruiter if I invite a candidate through Greenhouse?**

Greenhouse sends metadata about the user who initiates the candidate invitation. HackerRank uses this information to identify and record that user as the inviting recruiter.

**Will Greenhouse reflect the updated score if I change it in HackerRank after the result is synced?**

No, Greenhouse does not update the score after the result is synced.

**Where can I find the candidate's completed record in HackerRank for Work?**

To find a candidate’s completed record:

- Log in to **HackerRank for Work**, and in the **Search Candidate** field at the top right, enter the candidate’s email address to view their Test attempts.

- Alternatively, from the **HackerRank for Work** home page, select the relevant Test, go to the **Candidates** tab, and click the candidate’s name to view their full Test performance report.

For more details, see the topics in the [Test Reports](#) section of our knowledge base.

Log in to **HackerRank for Work** and in the **Search Candidate** field available in the top-right corner, enter the candidate's email address to view the candidate's attempts.

Alternatively, from the **HackerRank for Work** home page, select the required Test, and click on the **Candidates** tab to view the candidate's list. Click on a candidate's record to view the complete Test performance report.

Refer to the topics in the [Test Reports](https://support.hackerrank.com/collections/2192436165-test-reports) section of our knowledge base for detailed information.

**Why do I not have permission in HackerRank for Work to grade a Test I was invited to through Greenhouse?**

In **HackerRank for Work**, ensure that your user account belongs to the Test owner's team. Alternatively, you can request the Test owner to share the Test with your account.

**Is the candidate’s submitted file for a File Upload type question available in Greenhouse?**

No. To view the candidate’s submission, log in to **HackerRank for Work** and open the candidate’s detailed Test report.

# Common Troubleshooting

If you encounter issues with the integration, try the following steps:

- **Verify the API key**: Ensure the API key added to your Greenhouse account is valid for your HackerRank for Work account.If you are unsure, you can generate a new Greenhouse API key in the HackerRank account settings page and configure the new key in Greenhouse.

- **Check your user account type**: Confirm that your HackerRank for Work account is an active **Recruiter**-type account with **Company Admin** permissions and belongs to a team. You cannot send Test invites using a **Developer**-type account.

- **Verify candidate email address**: Before sending Test invites from Greenhouse, ensure that the candidate’s profile includes a valid email address.

**Note**:For more information about admin permissions, see [Company Admin Permissions.](https://support.hackerrank.com/articles/9603546665-types-of-user-roles#company-admin-2)

\
