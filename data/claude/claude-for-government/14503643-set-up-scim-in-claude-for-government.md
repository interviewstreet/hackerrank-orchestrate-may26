---
title: "Set up SCIM in Claude for Government"
title_slug: "set-up-scim-in-claude-for-government"
source_url: "https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government"
last_updated_iso: "2026-04-10T18:39:16Z"
article_id: "16970822"
breadcrumbs:
  - "Claude for Government"
---

# Set up SCIM in Claude for Government

_Last updated: 2026-04-10T18:39:16Z_

System for Cross-domain Identity Management (SCIM) lets your identity provider automatically manage user accounts in Claude for Government. With SCIM, your IdP controls who has access, what role they hold, and what seat tier they're assigned—without manual intervention in the Claude admin console.

For SCIM setup on Claude Enterprise, see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

## How SCIM differs for Claude for Government

Claude for Government uses a first-party SCIM implementation hosted within the FedRAMP-authorized environment. The commercial Claude Enterprise plan uses a different SCIM backend.

## Prerequisites

Before setting up SCIM, you must complete:

1. **SSO configuration** — Complete the steps outlined in the SSO setup guide.
2. **Domain verification** — Your login domain must be verified (this is completed during SSO setup).
3. **IdP admin access **— Permission to configure a SCIM integration in your identity provider.

## How provisioning works with and without SCIM

Without SCIM, Claude for Government uses just-in-time (JIT) provisioning: any user who authenticates through SSO is automatically assigned a seat, as long as licenses are available. You control who can authenticate by managing membership in the SAML application within your IdP.

With SCIM, login and provisioning are separate. Your IdP tells Anthropic who should have access and at what role/tier. SSO is used only for authentication. This gives you fine-grained control over roles, seat tiers, and offboarding.

#### Step 1: Generate a SCIM API key

1. Navigate to claude.fedstart.com/admin-settings/identity.
2. In the SCIM section, generate a new API key.
3. Copy the key — you'll need it when configuring your IdP.

> **Important**: Store this key securely. It cannot be retrieved after you leave the page.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040196/c3b045028c4c2edef9172b6fb424/9a71258e-ae73-41e3-83a2-d24a240ac0ae?expires=1776784500&signature=eeb7fda4a644fbcd2b51e0acc5400f548fb5fd046734a4bd9eea544574a0467c&req=diIiEMl6nYBWX%2FMW1HO4zSrRmqoYYTIRyIvvU1hav7M4BRovGoXDjnz1Wavc%0ApummdZ4I4uWT2Irl5sY%3D%0A)

#### Step 2: Configure SCIM in your Identity Provider

1. In your IdP (e.g., Entra ID, Okta), create or open a SCIM provisioning integration.
2. Enter the following values:
  1. SCIM endpoint URL: **[https://claude.fedstart.com/v1/scim/v2](https://claude.fedstart.com/v1/scim/v2)**
  2. API key / Bearer token: The key generated in Step 1
3. Configure the user attributes your IdP will sync (typically name and email).
4. Assign users and groups to the SCIM integration within your IdP.

#### Step 3: Verify sync status

After enabling the integration in your IdP:

1. Return to the identity settings page at claude.fedstart.com/admin-settings/identity.
2. Check the SCIM sync status indicator to confirm users are syncing.

> **Warning**: When you fully enable SCIM provisioning, any users who were **not** synced via SCIM will be removed from the organization. Confirm that all expected users appear in the sync before proceeding.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256040198/da9188b8b968d5f900cc08e9ceb2/3814ab37-c3fa-4256-8d16-49c1e1b4c654?expires=1776784500&signature=89bbf60fe84342ebe6ba136f38391cbef22189aa33ee2065c16400014ffa4598&req=diIiEMl6nYBWUfMW1HO4zeLvPV5oQkj%2FoWupW8zJgMrgwx4UbRvwjtIZRljk%0AgSdy%2Fsy8TShPn7tBUBM%3D%0A)

#### Step 4: Map groups to roles and seat tiers

SCIM provisioning uses IdP groups to assign roles and seat tiers within Claude for Government.

1. On the identity settings page, open the role mappings table.
2. For each IdP group, assign:
  1. Role — The user's role within the organization (e.g., Member, Owner).
  2. Seat tier — The license tier, if your organization has purchased multiple tiers.
3. Save your mappings.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2256056441/f7eb09bba549e9861fc81b961cc7/2760fa5b-87bb-491f-9354-ca3cd2bc4475?expires=1776784500&signature=54016c2890b6a9487a0a69642aa6b35c71a324aafdf57aa61f458cbf4444117d&req=diIiEMl7m4VbWPMW1HO4zaWhvnUlukMeh340B79BYGaktc6z6CGD7Kk1%2Bjt5%0AqW5KT04GYk5SesJ1xtY%3D%0A)

If you manage multiple organizations under a single parent (see below), each organization maintains its own role and seat tier mappings. Switch between organizations using the organization selector in the bottom-left corner of the page.

#### Parent organizations (multi-org setups)

Every Claude for Government organization belongs to a **parent organization**. For most customers, this is transparent—a parent is created automatically during provisioning and contains a single child organization.

Parent organizations become relevant when multiple organizations share a login domain. Common scenarios include:

- **Regional offices** that purchase Claude for Government independently but share an email domain.
- **Sub-departments** within an agency that require data separation (e.g., preventing cross-org sharing of chats or projects).

In a multi-org setup:

- Identity settings (IdP configuration and SCIM) are managed at the **parent organization** level.
- Role and seat tier mappings are configured **per child organization**, allowing different groups to map to different orgs.
- Any Owner or Primary Owner in a child organization can manage IdP settings. Restrict these roles to centralized IT staff.

> **Note:** Anthropic support will work with you during provisioning to configure parent/child organization relationships. Contact your account representative or **[Anthropic support](https://claude.fedstart.com/support)** if you need to set up a multi-org structure.

## Related Articles
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
- [How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
