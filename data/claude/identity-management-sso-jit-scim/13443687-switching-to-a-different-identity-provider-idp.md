---
title: "Switching to a different Identity Provider (IdP)"
title_slug: "switching-to-a-different-identity-provider-idp"
source_url: "https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp"
last_updated_iso: "2026-04-10T23:49:06Z"
article_id: "15396490"
breadcrumbs:
  - "Identity management (SSO, JIT, SCIM)"
---

# Switching to a different Identity Provider (IdP)

_Last updated: 2026-04-10T23:49:06Z_

This guide walks you through the process of migrating your Claude or Console organization from one identity provider to another while preserving user access and avoiding disruption.

> **Note:** This process applies to organizations that already have SSO configured. If you're setting up SSO for the first time, see **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)**.

## Before you begin

- Confirm you have the required role:
  - **For Team or Enterprise plans:** You must be an Owner or Primary Owner.
  - **For Claude Console:** You must be an Admin.
- Notify your users in advance that they will be temporarily signed out during the migration.
- Schedule the switch during a low-disruption period.
- Ensure that the SSO and SCIM email attribute for all users in your new IdP exactly matches what was used with your previous IdP. If these email addresses don't match exactly, users will be provisioned with duplicate accounts.

## Steps to switch your IdP

1. **Disable SCIM pushes from your current IdP** (if applicable): Stop Create/Update events on your current IdP's side to prevent any sync signals from being sent during the migration.
  1. For more information about SCIM, see **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**.
2. **Switch provisioning mode to "Invite only"** (if applicable): Wait approximately one hour after disabling SCIM pushes, then navigate to the "Identity and access" page on **all** connected Claude (claude.ai/admin-settings/organization) or Console (platform.claude.com/settings/identity) organizations. Under **Global SSO Configuration**, set the provisioning mode to "Invite only."
  1. This stops SCIM from automatically managing users—users remain in the organization but are no longer subject to SCIM events.
3. **Delete the SCIM directory** (if applicable): Click "Manage SCIM" > "Delete Directory." When in invite only mode, deleting the directory will not trigger directory sync events, including user deprovisioning.
4. **Reset the SSO connection**: Click "Manage SSO" > "Reset Connection."
  1. **Important:** This will sign out all users. They will be able to **[sign in via email link](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account#h_869b162f56)** until the new IdP is configured for SSO.
5. **Verify the reset**: Refresh the "Identity and access" page and confirm that the button state has changed from "Manage SSO" to "Setup SSO."
6. **Set up your new IdP for SSO and provisioning**: Follow the **[SSO setup steps](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** and **[configure JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)** with group mappings enabled (if needed) to ensure all users are assigned in the new IdP with the correct groups for all your connected Claude and/or Console organizations. If applicable, after setup you can click "Manage SCIM" to verify which users have synced to the directory and confirm they're associated with the correct groups.
7. **Re-enable provisioning** (if applicable): Select "Approve automatically (JIT)" or "Sync with SCIM" to switch the provisioning mode and click "Save Changes" to apply.

## Related Articles
- [Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
