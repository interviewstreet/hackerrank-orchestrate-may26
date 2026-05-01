---
title: "InterviewPlanner-HackerRank Integration FAQs"
title_slug: "interviewplanner-hackerrank-integration-faqs"
source_url: "https://support.hackerrank.com/articles/7401637722-interviewplanner-hackerrank-integration-faqs-"
article_slug: "7401637722-interviewplanner-hackerrank-integration-faqs-"
last_updated_exact: "Jan 23, 2025, 3:32 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Scheduling"
---

# InterviewPlanner-HackerRank Integration FAQs

_Last updated: Jan 23, 2025, 3:32 AM (Last updated 1 year ago)_

HackerRank Interview integrates with InterviewPlanner to enable a seamless and efficient candidate screening process for recruiters.

This article provides useful troubleshooting tips for some common issues encountered while enabling and using the integration.

## API Token and Access

### I am unable to view the API keys in my HackerRank for Work account.

You must log in to HackerRank for Work with a **Recruiter-type** **Company Admin** user account to view the API access page and generate the InterviewPlanner API key.

Refer to the **Prerequisites** section in the[📄 Using HackerRank Interviews in InterviewPlanner](/articles/3675175160) topic.

### Seems like the InterviewPlanner API key is not valid for my HackerRank for Work account. How can I reset the API key?

- Log in to HackerRank for Work using the company admin user account which has the same email address as the InterviewPlanner user account.

- Navigate to **Settings** -\> **API access** -\> **InterviewPlanner**.

- Click **Delete** to delete the existing key and click **Generate API key** to create a new key.

- Add this API key in InterviewPlanner to enable the integration.

Refer to the[📄 Configuring InterviewPlanner - HackerRank Integration](/articles/1300810624)topic for detailed integration steps.

## Interviews

### Why do I receive an error message while trying to generate an interview link in InterviewPlanner?

- Ensure that you have logged in to InterviewPlanner using the same email address as your HackerRank *for* Work user account. This is required for generating the HackerRank interview link and logging in to an interview session.

- The candidate's profile may not have a valid email address. Update the candidate's email address and try generating the interview link again.

### Who is treated as the Inviting Recruiter if I invite a candidate through InterviewPlanner?

InterviewPlanner sends us metadata about the recruiter who initiated the action to invite a candidate. That information is used to determine the inviting recruiter.

### Other Troubleshooting Tips

What are the other troubleshooting tips for any issues encountered with the integration?

- Verify whether the API key added to your InterviewPlanner account is valid for your HackerRank for Work account. If you are unsure, you can generate a new InterviewPlanner API key in the HackerRank account settings page and configure the new key in InterviewPlanner.

- Ensure that your HackerRank for Work user account is an activated **Recruiter** type account with **Company Admin** permissions. This user account must belong to any team. You cannot send invites using a Developer type user account.

- While sending invites from InterviewPlanner, ensure that the candidate profile has a valid email address.

**Note**:  For more information about admin permissions and user activation, refer to the articles, [Company Admin Permissions](https://support.hackerrank.com/articles/9603546665-types-of-user-roles#company-admin-2), and[📄 Activating a Team Member](/articles/4529668655)

\

\
