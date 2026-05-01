---
title: "Set up the Claude LTI in Canvas by Instructure"
title_slug: "set-up-the-claude-lti-in-canvas-by-instructure"
source_url: "https://support.claude.com/en/articles/11725453-set-up-the-claude-lti-in-canvas-by-instructure"
last_updated_iso: "2026-03-16T21:04:03Z"
article_id: "12811565"
breadcrumbs:
  - "Claude for Education"
---

# Set up the Claude LTI in Canvas by Instructure

_Last updated: 2026-03-16T21:04:03Z_

This article provides information on how to enable the Claude LTI integration in Canvas LMS. These steps are intended for Claude for Education administrators and Learning Management Systems (LMS) administrators.

## Creating Claude LTI Developer Key in Canvas

1. In Canvas, sign in as an administrator and navigate to **Admin -> Developer Keys**.
2. Click "+ Developer Key" then "+ LTI Key."
3. Enter the following:
  1. **Key Name:** Claude LTI
  2. **Description:** Enter a short description for the Canva LTI 1.3 app
  3. **Redirect URIs:** [https://claude.ai/lti/launch](https://claude.ai/lti/launch)
  4. **Title: **Claude LTI
  5. **Target Link URI:** [https://claude.ai/lti/launch](https://claude.ai/lti/launch)
  6. **OpenID Connect Initiation Url:** [https://claude.ai/api/lti/login](https://claude.ai/api/lti/login)
  7. **JWK method:** [https://claude.ai/api/lti/keys](https://claude.ai/api/lti/keys)
4. Under **Additional Settings**, toggle Privacy Level to **Public**.
5. Under **Placements**, we recommend removing the defaults and adding "Course Navigation" and "Assignment Edit" as the options.
6. Click "Save."
7. Toggle the state to **On**.

## Installing Claude LTI as an App

1. In Canvas, go to Admin -> Settings -> Apps.
2. Click "View App Configurations" then select "+ App."
3. Select **Configuration Type** “By Client ID.”
4. Input the Client ID generated for your developer key (from Step 6 under Creating Claude LTI Developer Key in Canvas).
5. Click "Install" and refresh the course page.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1611422430/c8e0875feac1f2c7cb033be74fc9/AD_4nXfLU_bui3EXcCjQ0qm70HD97neqjGayKeDer_t76utlci8gZSUjYRhw6ZSOlDdqSEcwXBzd_shAh7pQEJ-8OoE0O21DM5coOgxmO_WD5hlwiuwtS2iYXcTavhIRyQT5zKFWvfn3NA?expires=1776784500&signature=879b7989745213c6ab9551051108e1dd37b00ca1bca3be52a0606c0f10ded78b&req=dSYmF818n4VcWfMW1HO4zTEDZe0Zk%2FeEEv2ojHLMylYQTqljc62hB3hBc2Ji%0AAYGO9A0Di4c3nmwickE%3D%0A)

## Turn on the Claude LTI Integration in Claude for Education organization settings

1. In Claude for Education, sign in as an administrator.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Find **Canvas** and click "Enable."
4. In the settings modal that pops up, input the required information to enable the integration
  1. **Canvas Domain**
  2. **Client ID** (found in Canvas Admin -> Developer Keys)
  3. **Deployment ID** (found in Canvas Admin -> Settings -> Apps -> View App Configurations -> Claude LTI Settings Button -> Deployment ID)
5. Click "Save Changes." The integration should now show as enabled.

## Questions

If you have any questions about your Claude for Education plan account or the Claude LTI, we encourage you to contact your university’s administrator(s).

## Related Articles
- [Getting Started with Claude for Education at Your University (for Owners/Admins)](https://support.claude.com/en/articles/11139094-getting-started-with-claude-for-education-at-your-university-for-owners-admins)
- [FAQs on Using Claude for Education at Your University](https://support.claude.com/en/articles/11139144-faqs-on-using-claude-for-education-at-your-university)
- [Logging in to your Claude account](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)
- [Enforce network-level access control with Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
