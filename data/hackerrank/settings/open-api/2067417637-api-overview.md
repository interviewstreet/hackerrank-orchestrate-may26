---
title: "API Overview"
title_slug: "api-overview"
source_url: "https://support.hackerrank.com/articles/2067417637-api-overview"
article_slug: "2067417637-api-overview"
last_updated_exact: "Nov 22, 2025, 1:33 AM"
last_updated_relative: "Last updated 5 months ago"
breadcrumbs:
  - "Settings"
  - "Open API"
---

# API Overview

_Last updated: Nov 22, 2025, 1:33 AM (Last updated 5 months ago)_

HackerRank offers robust APIs to automate test administration and result retrieval. Seamlessly integrate these APIs with your HR systems or create custom dashboards to streamline workflows. Additionally, explore our pre-built integrations with leading Applicant Tracking Systems (ATS). Refer to our [📄 Integrations Overview](/articles/1847021717)article for more details.

## Generating my API Token

Each enterprise user with a **HackerRank for Work** account can use our APIs to generate a personal access token. These APIs help automate repetitive tasks, such as administering tests and fetching results.

**Note**: This token is not intended to support ATS integrations. To obtain API keys for integrations with ATS platforms like Breezy, Lever, Greenhouse, or Jobvite, refer to the **ATS Integration** section in our knowledge base.

#### Steps to Generate an Access Token

- Click the **arrow** next to the user icon in the top-right corner of the **Home** page and then click on **Settings**.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735207710006-1735207351793-1735206765435-image.png-f458ef41-fe8a-4059-bd42-df7821ab3c5a-59f0a144-3e46-4134-9e3c-b39e3a88ec8e?Expires=253370764800&Signature=i8qJdkA9aH3IoMZ-5e5mCosx7JPT~Hnma6NDTnfEF04I-SbFY9oXzJriCaWIfLMLEhuFYNMz6gyd10NXS8-jJpUfIDl5D-k9EplxI9aMPEIQe43zemSyzi~LHSw1PxW6MdaV71p5E5-F8bDufewagvryvYh-6mqZr0TF2EQJBQqtIQWEnUNkvQl8qyQm-YeV4YYJcnN28K89VBgFQ3ObcdEnzsM956SAOdrvp9HDEn2nAFt0WT07DeJ9fVkwDWdOl-4~RKle9~3a0P-6sqwubPeUaaU1LhXNJh0XvGFd09Iu2aeQYjnBcAVORh1qLoMvSEip3BrGSFtWTpN1Y9cVNA__&Key-Pair-Id=K3NV4LZ47N8M46)

- On the **API** page, click **New Token**.

- In the **New Token** dialog box:

  - Enter a label for the token.

  - Click **Generate Token**.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735207697884-1735207352303-1735206943076-image.png-50e74835-dd94-4722-9f91-d3fd3bbe5ca7-f9e213ef-d114-4aae-af2d-ab1eed22877f?Expires=253370764800&Signature=mTlwRbCphb-9gh4RIcRthgYQg9Gj-ASAOUnZb6htO-89vIaviYfFKyEPMjcSujJtOwNI0cv9QxDBVQCw1Z2xmqtDpzAzYzuehCzwyij39j4c~X0PYxleogcOOU8Vp9Ah-t32dbw6K4qt4bui3nBlLbvPq0y6W-Bq0yzC5PMzDz~fVMOIuVWH2iXSR5-XqnIEfMypZynKqOnf606PoNjT1RdJq4zYm9Zbk3o4~4hZPke4He7xcX9QBDnv3dUTNRsohWHxRqTmZQTLHmbh-hW3dBBBPARtYve2mMTZDmEjsFXNJbEkRuTgnAoxj-0mhrXVERmUPTOz9ifc9K2nw-txMg__&Key-Pair-Id=K3NV4LZ47N8M46)

- The newly generated token will be displayed. You can use the options provided to copy, edit, or delete it.

**Tip**: Refer to our detailed [API Documentation](https://www.hackerrank.com/work/apidocs#!/Introduction/options_intro_api) for more information about API usage and capabilities.

## Rate limits

HackerRank recommends sending up to 10 API requests per second. If you exceed this rate, the API returns a 429 (Too Many Requests) error. Monitor these errors and retry failed requests when necessary.

If you need to send more than 10 API requests per second, contact [support@hackerrank.com](mailto:support@hackerrank.com).

## Available APIs

Here's an overview of our APIs and their capabilities:

|  |  |
|----|----|
| **API Name** | **Notes on Use Cases** |
| [Test API](https://www.hackerrank.com/work/apidocs#!/Tests/options_tests) | Most popular with our existing customers. The calls in this API allow you to perform repetitive tasks about the Tests module - like inviting candidates for a test, fetching candidate status, including detailed reports, viewing details about tests and the contained questions, etc. |
| [Interviews API](https://www.hackerrank.com/work/apidocs#!/Interviews/get_x_api_v3_interviews_limit_limit_offset_offset) | Allow such actions as creating a new QuickPad, scheduling an interview, viewing all interviews, fetching reports, etc. |
| [Users API](https://www.hackerrank.com/work/apidocs#!/Users/options_users) | Users endpoint is useful for creating new users programmatically, such as when integrating HackerRank with other systems or applications. |
| [Teams API](https://www.hackerrank.com/work/apidocs#!/Teams/options_teams) | Teams endpoint allows you to create new teams automatically, which is helpful when organizing coding competitions or collaborative projects on HackerRank. |
| [User Membership API](https://www.hackerrank.com/work/apidocs#!/UserMembership/get_x_api_v3_teams_team_id_users_limit_limit_offset_offset) | This endpoint helps you get a list of team members, which is handy when creating tools to manage teams or connecting HackerRank with other services. |
| [Test Candidates API](https://www.hackerrank.com/work/apidocs#!/TestCandidate/options_candidates) | Similar to Tests API, this endpoint provides a flexible and efficient way to access candidate data, with options to limit and offset results for easy pagination and customization. |
| [Questions API](https://www.hackerrank.com/work/apidocs#!/Questions/options_questions) | With this powerful resource, you can tap into a vast repository of questions and challenges to drive your organization's growth, improvement, and innovation. |

\
