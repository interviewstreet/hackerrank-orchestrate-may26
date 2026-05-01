---
title: "Set up JIT or SCIM provisioning"
title_slug: "set-up-jit-or-scim-provisioning"
source_url: "https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning"
last_updated_iso: "2026-04-10T23:36:14Z"
article_id: "14920932"
breadcrumbs:
  - "Identity management (SSO, JIT, SCIM)"
---

# Set up JIT or SCIM provisioning

_Last updated: 2026-04-10T23:36:14Z_

> JIT provisioning is available for Team plans, Enterprise plans, and Console organizations. SCIM provisioning is available for Enterprise and Console organizations only.

This guide covers how to configure user provisioning and role assignment for your Claude or Claude Console organization.

**Before you begin:** This guide assumes you have already completed the steps in **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**, including domain verification and SSO configuration with your Identity Provider (IdP), and you have an Admin (Console) or Owner (Claude) role.

---

## Step 1: Choose your provisioning mode

Once SSO is configured, you need to decide how users will be provisioned to your organization. This is controlled by the **Provisioning mode** setting in **[Organization](https://claude.ai/admin-settings/organization)****[ settings > Organization and access](https://claude.ai/admin-settings/organization)**.

#### Provisioning options

**Invite only** is the default. Users are added and removed directly in Claude or Console settings.

**Approve automatically (JIT):** Users assigned to your Anthropic IdP app are automatically provisioned when they first log in. This option is available to all plans.

**Sync with SCIM:** Users are automatically provisioned and deprovisioned based on assignments in your IdP, without requiring them to log in first. SCIM is available for Enterprise plans and Console organizations with their own parent organization or joined to an Enterprise parent organization. SCIM is not available for Team plans or Console organizations joined to a Team plan's parent organization.

#### Provisioning behavior overview

Use this table to help decide which provisioning mode is right for your organization:

Both JIT and SCIM can be combined with **Enable group mappings** to control role or seat tier assignment based on IdP group membership. If you select either of these options for your provisioning mode, **Enable group mappings** will appear within that section:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2176723944/4737810c06ddb3b763b4db87616c/bd6fc71e-7ffb-4d75-8023-15c3f3ecd3b1?expires=1776784500&signature=472337e2bf9e28d5a7bd973c450d07181e2a4d32b6536d9656be85ae2771d70b&req=diEgEM58nohbXfMW1HO4zbyhYEDk5uS88ID2M6EZ%2Fu3fSMn1JNVD02Urs3bg%0A5B3e3MbN6CnaaLKesvs%3D%0A)

#### Available roles and seat tiers

For information on purchasing seats or adjusting your plan's seat allocation, see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

---

## Step 2: Set up SCIM directory sync (if using SCIM)

> **Note:** Skip this step if you're using Invite only or JIT provisioning.

If you chose SCIM as your provisioning mode, you need to establish the connection between your Identity Provider and Anthropic before enabling it.

1. Navigate to your Organization and access settings in Claude (**[claude.ai/admin-settings/organization](http://claude.ai/admin-settings/organization)**) or Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identit)**)
2. In the **Global access settings **section, click “Setup SCIM” (or “Manage SCIM”)** **next to **Directory sync (SCIM)**.
3. Follow the WorkOS setup guide to configure SCIM in your Identity Provider. You'll need to copy values from WorkOS into your IdP's Anthropic application.

**‼️ When you reach the IdP Group step, pause to review Steps 3 and 4 of this guide, alongside the other guides.**

For IdP-specific JIT / SCIM setup instructions, see:

- **[Okta SAML](https://workos.com/docs/integrations/okta-saml)** / **[OKTA SCIM](https://workos.com/docs/integrations/okta-scim)**
- **[Entra ID SAML](https://workos.com/docs/integrations/entra-id-saml)** / **[Entra ID SCIM](https://workos.com/docs/integrations/entra-id-scim)**
- **[Google SAML](https://workos.com/docs/integrations/google-saml)** / **[Directory Sync](https://workos.com/docs/integrations/google-directory-sync)**
- **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)** / **[OneLogin SCIM](https://workos.com/docs/integrations/onelogin-scim)**
- **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)** / **[JumpCloud SCIM](https://workos.com/docs/integrations/jumpcloud-scim)**
- See additional IdPs **[here](https://workos.com/docs/integrations)**

Once your IdP is connected, continue to Step 3.

---

## Step 3: Configure provisioning mode and enable group mappings

1. In the **Global access settings** section of your Organization and access settings, find **Provisioning mode**.
2. Select your chosen option from the dropdown:
  1. **Invite only**: New members can only join if manually invited by an existing member. SSO access alone won't add them to your org.
  2. **Approve automatically (JIT)**: Allow people with SSO access to join when they first log in. Each new member uses one of your available seats.
  3. **Sync with SCIM**: Add or remove members automatically as your directory changes. Your org always stays current.
3. If you selected “Approve automatically (JIT)” or “Sync with SCIM,” do NOT click “Save changes” immediately. You must first ensure all users are assigned to your Anthropic application in your IdP.
4. Once you’ve confirmed all users are assigned in your IdP you can either:
  1. Click “Save changes” to complete the set up and trigger the initial provisioning, or
  2. Toggle on **Enable group mappings** and move to Step 4.

> **Important**: Saving before users are properly assigned will result in those users being deprovisioned from the organization.

---

## Step 4: Configure groups in your Identity Provider and map groups to roles and seat types

1. Create groups in your IdP for each role you want to assign. Unless you're on the single-seat Enterprise plan, create groups for each seat type as well.
  1. While there are no longer naming requirements for these groups, we recommend including something in the group name (e.g., `anthropic-claude-` or `anthropic-console-`) to make them easier to identify.
2. Add users to the groups you created, ensuring at least one user (including yourself) is in a group that will be mapped to an Admin (Console) or Owner (Claude) role.
3. Return to your Organization and access settings in Claude or Console, and find **Provisioning mode**.
4. Toggle **Enable group mappings** on (if it’s not already):

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2176704418/12b0291c6e4838629c426eb70b35/dec53ce5-8b57-4864-9239-b4b5fe1feef9?expires=1776784500&signature=20265c433c87bea0b293c937e45b08c93565e8a25116764c9d9cfa64d2777aa1&req=diEgEM5%2BmYVeUfMW1HO4zb2ns7WRJvVuR0JZcR0qIIov%2B5OdC5H85FQuKkMb%0Amjc7%0A)
5. In the **Enable group mappings** section, click “Add” next to each role and select the corresponding group from your IdP in the dropdown.
  1. When using group mappings, you *must* assign all users to a role-based group in order to ensure they’re provisioned an account. Assigning users to seat-tier based groups is optional.
  2. You can map an IdP group to the “Custom roles” role. Members assigned this role have no default permissions—their access is determined entirely by the custom roles assigned to their groups in Claude.
6. **For all plans except single-seat Enterprise:** In the **Assign seat tiers to IdP groups** section (optional), click "Add" next to each seat type and select the corresponding group from your IdP. If a user isn't assigned to a seat type group, they will be assigned to the highest available type by default.
  1. **For single-seat Enterprise:** Seat type mapping does not apply. All provisioned users are automatically assigned an Enterprise seat, provided one is available in your organization.
7. Verify all necessary groups are mapped to the appropriate roles and seat types.
8. Click “Save changes.”
  1. **Note:** Microsoft Entra only pushes SCIM changes every 40 minutes, so there may be a delay before changes appear. You can check which users are synced from your IdP by clicking "Manage SCIM" and viewing the Directory. Those users in the Directory will be provisioned to Claude / Console.

> **Important:** All users who need access must be assigned to the appropriate groups before you save your group mappings configuration. These users should already be assigned to your Anthropic application in your IdP from when you enabled SSO.

---

## Troubleshooting

#### Users assigned correctly and showing in the directory but aren’t being added to the Claude as members?

Verify you have enough seats purchased and available to add members to your org.

1. Check the number of available seats shown in **[Organization](https://claude.ai/admin-settings/organization)****[ settings > Billing](https://claude.ai/admin-settings/billing)** and purchase additional seats if needed (see our guides for **[Team plans](https://support.claude.com/en/articles/12004354-purchasing-and-managing-seats)** and **[Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**).
2. Once you have available seats, go back to the Organization and access page and click “Sync now,” next to **Directory sync (SCIM)**. This will trigger a sync to provision accounts for those users not yet added as members.

#### Users aren't being provisioned with the correct role

1. Verify the user is assigned to the correct group in your IdP.
2. Verify the group is mapped to the correct role in your Organization and access settings.
3. **For JIT:** The user needs to log out and log back in for role changes to take effect.
4. **For SCIM:** Click "Sync Now" to prompt an immediate sync, or wait for the automatic sync cycle.

#### I lost Admin/Owner access after enabling group mappings

This happens when the person configuring group mappings isn't assigned to a group mapped to an Admin or Owner role, causing their permissions to be downgraded to User.

To fix this:

**Option 1: Have another Admin/Owner reinstate your role**

1. Contact another Admin or Owner of your organization.
2. Ask them to navigate to **[Organization settings > Organization](https://claude.ai/admin-settings/organization)** (for Claude) or **[Settings > Members](https://platform.claude.com/settings/members)** (for Console).
3. Have them change your role back to Admin or Owner.

**Option 2: Fix via your Identity Provider**

1. In your IdP, assign yourself to a group with the correct prefix that maps to an Admin or Owner role.
2. **For JIT:** Log out and log back in to regain access.
3. **For SCIM:** Ask another Admin or Owner to click "Sync Now" in the Organization and access settings, or wait for the automatic sync cycle.

## Related Articles
- [Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Switching to a different Identity Provider (IdP)](https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp)
- [How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
