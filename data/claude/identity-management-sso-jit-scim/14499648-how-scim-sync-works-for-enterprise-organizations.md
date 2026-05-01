---
title: "How SCIM sync works for Enterprise organizations"
title_slug: "how-scim-sync-works-for-enterprise-organizations"
source_url: "https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations"
last_updated_iso: "2026-04-09T15:02:01Z"
article_id: "16965230"
breadcrumbs:
  - "Identity management (SSO, JIT, SCIM)"
---

# How SCIM sync works for Enterprise organizations

_Last updated: 2026-04-09T15:02:01Z_

SCIM provisioning keeps your Enterprise organization's membership and groups in sync with your identity provider. This article covers what gets synced, how syncs are triggered, and what to watch for when resyncing.

> Available on the Enterprise plan. For setup instructions, see **Set up JIT or SCIM provisioning**.

## What gets synced

When you connect your identity provider (IdP) to your Enterprise organization through the WorkOS integration, two things sync from your IdP:

- **Members** from your SCIM directory
- **SCIM groups** that you've pushed from your IdP to WorkOS

Group membership in your organization determines which capabilities members with custom roles can access, along with group spend limits.

## Automatic syncing

Your Enterprise organization receives changes from your IdP automatically whenever your IdP pushes member or group updates (adds, removes, or edits) to WorkOS.

Behind the scenes, your organization polls WorkOS for update events every minute and processes them in a queue. This method is eventually consistent — syncs typically complete within minutes, but can take several hours during periods of high system traffic.

## Manual syncing

Some actions trigger a manual sync immediately, and you can also run one on demand.

#### Actions that trigger a manual sync

- **Changing the provisioning mode to SCIM.** Any member not in your IdP directory is removed, and any member in your IdP directory is added. You'll need to wait for this initial resync before configuring group mappings.
- **Enabling Advanced Group Mappings.** The full list of members and groups updates. New and existing members' roles and seat tiers are enforced by the group mapping and can't be overridden manually. After saving a new mapping, click

**Sync now** to recompute roles and seat tiers for existing members.

- **Using the Check for updates button** at **Organization settings > Groups**.
- **Using the Sync now button** at **Organization settings > Identity and access > Manage SCIM**.

> **Note: **When you update seat provisioning or seat roles through group mappings, existing members aren't resynced automatically. Trigger a manual sync to apply the changes.
>
> When you disable group mappings, you regain the ability to manually assign member roles and seat tiers. Existing members keep their current roles. New members are assigned the User role—change their role to "Custom Roles" if you want to enable custom role permissions.

## How to manually trigger a sync

You can trigger a manual sync from two places in your admin settings.

**From the Groups page**

1. Go to **Organization settings > Groups**.
2. Click **Check for updates**.
3. Select whether to sync members, groups, or both.

**From the Manage SCIM page**

1. Go to **Organization settings > Identity and access > Manage SCIM**.
2. Click **Sync now**.
3. Select whether to sync members, groups, or both.

> **Note: **If you trigger a manual sync while background changes are processing, your organization takes the most recent change for each member or group. If multiple changes are queued for the same member or group, you may need to resync again to make sure everything applies correctly.

## Member sync vs. group sync

When you trigger a manual sync, you can choose to sync members, groups, or both. Here's what each does:

- **Member sync** updates your organization's record of which members are mapped to seats, seat tiers, and seat roles (Custom Roles, User, Admin, Owner). This can affect members' login access to Claude.
- **Group sync** updates your organization's record of which SCIM groups exist and who belongs to them. Group membership determines which capabilities members with custom roles can use, along with group spend limits.

## How long manual syncs take

Manual syncs rescan WorkOS for the full list of members and groups to establish an up-to-date baseline. Expect roughly one minute per 100 members in your organization—so a 1,000-member organization takes about 10 minutes to fully resync.

## Verifying your sync status

To check whether your organization's membership and groups are current, you have two options:

- **Export your member list.** Go to **Organization settings > Members** and click **Export CSV** to download the current view of your membership.
- **View the WorkOS integration's record.** Go to **Organization settings > Identity and access > Manage SCIM** to see what WorkOS currently holds for your organization.

## Risks to watch for when resyncing

Before you trigger a manual resync, keep these in mind:

- **Changing the provisioning mode to SCIM removes members not in your IdP directory.** Confirm that all existing members are in your IdP directory before changing provisioning mode.
- **Updating a member's email creates a new member record.** The member with the old email is removed, and a new member with the new email is created.
- **Resyncing cascades to child organizations.** If you have multiple organizations with SCIM provisioning under the same **parent organization**, resyncing one triggers resyncing in the others. This includes sandbox organizations sharing the same parent.
- **Incomplete group mappings remove members from the organization.** When enabling group mapping for SCIM, finish assigning all groups before saving. Any member not included in a role group mapping is removed from the organization. If you enable seat tier mapping, any member not in a seat tier group mapping is also removed.

## Related Articles
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Migrate your organization from Team to Enterprise](https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise)
- [Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
