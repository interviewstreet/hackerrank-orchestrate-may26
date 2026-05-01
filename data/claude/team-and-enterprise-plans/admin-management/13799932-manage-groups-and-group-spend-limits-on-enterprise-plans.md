---
title: "Manage groups and group spend limits on Enterprise plans"
title_slug: "manage-groups-and-group-spend-limits-on-enterprise-plans"
source_url: "https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans"
last_updated_iso: "2026-04-09T14:28:23Z"
article_id: "15986258"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Admin management"
---

# Manage groups and group spend limits on Enterprise plans

_Last updated: 2026-04-09T14:28:23Z_

Groups and group spend limits are available for Enterprise plan organizations. Owners and Primary Owners can manage groups in **[Organization settings > Groups](http://claude.ai/admin-settings/groups)** and group spend limits in[ **Organization settings > Usage**](https://claude.ai/admin-settings/usage).

## What are groups?

Groups let you organize members into logical collections — by team, department, or any other grouping that fits your organization. Once groups are set up, you can:

- **Set spend limits for groups**, so all members of a group share a per-user spend limit.
- **Control member access through group memberships and custom roles**, so their capabilities and permissions are determined entirely by the groups they belong to. For additional details, see **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

Groups can be created manually or synced automatically from your identity provider via SCIM. Each organization can have up to 100 groups.

In addition to spend limits, Enterprise admins can use groups to control plugin access in Cowork. Each plugin in your organization's marketplace can have group-level overrides that determine whether it's available, pre-installed, required, or hidden for members of a specific group. For details, see **[Manage Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

---

## Create a group

1. Navigate to **[Organization settings > Groups](http://claude.ai/admin-settings/groups)**.
2. Click the "Add group" button.
3. Enter a name for the group in the **Create a group** modal.
4. Select which custom roles to assign to this group (optional).
5. Search for and add members to the group.
6. Click "Add group” and your group will appear in the list..

> **Note:** If SCIM directory sync is enabled, you’ll see a “SCIM Sync” button next to "Add group." Clicking this will manually refresh groups from your identity provider.

## Edit a group

Click any group in the list to open its edit form. You can change the name, update custom role assignments, and add or remove members.

> **Note:** Groups synced from your identity provider via SCIM can't be renamed or deleted in Claude, and their members are managed in your identity provider.

## Delete a group

Click the menu button to the right of any group and select "Delete." Deleting a group doesn't affect the custom roles that were assigned to it and doesn't remove any members from your organization.

---

## SCIM group sync

If your organization uses SCIM directory sync, groups from your identity provider are automatically synced to Claude. SCIM groups appear with a sync indicator in the groups list.

SCIM groups support custom role assignments and spend limits the same way as manually created groups.

To manually trigger a sync, click “SCIM Sync."

---

## Control member access with custom roles

You can control individual members' feature access entirely through groups and custom roles. When a member's role is set to **Custom roles**, they have no default capabilities or permissions beyond chat—their access is determined entirely by the custom roles assigned to their groups. This is different from the User, Admin, or Owner roles, which include built-in permissions.

#### Set a member's role to Custom roles

1. Navigate to[ **Organization settings > Organization**](https://claude.ai/admin-settings/organization).
2. Find the member and click their role dropdown.
3. Select "Custom roles."

Only Owners and Primary Owners can change member roles. You can also assign “Custom roles” at scale by mapping an IdP group using[ **group mappings**](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning).

#### Recommended setup

1. Create custom roles with the desired permissions in **[Organization settings > Custom roles](http://claude.ai/admin-settings/roles)**. For details, see Manage custom roles on Enterprise plans.
2. Create groups in **[Organization settings > Groups](http://claude.ai/admin-settings/groups)** (or sync them from your identity provider).
3. Assign custom roles to groups.
4. Add members to the appropriate groups.
  1. **Note:** If a member set to Custom roles isn't in any groups, or their groups have no custom roles assigned, they have no permissions and can't access any features beyond chat.
5. Set each member's organization role to **Custom roles**.
6. Enable any features at the organization level that you want to control per-group.

The member's effective permissions are now determined by their group memberships and the custom roles assigned to those groups.

> **Important: **Always complete steps 1–5 before enabling features at the organization level (step 6). If you enable a feature before changing members' roles to Custom roles and assigning appropriate custom roles, there's a brief window where some members could access the feature through their previous role. For a detailed walkthrough, see **[Set up role-based entitlements on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-entitlements-on-enterprise-plans)**.

#### Inviting new members

When inviting a new member, Owners and Primary Owners can select "Custom roles" as the role. The new member's access is determined by their group memberships after they join.

---

## Group spend limits

Group spend limits let you control spending across your organization by assigning per-user monthly spend limits to groups. Instead of setting spend limits for each member individually, you can set a limit on a group and have it apply to every member of that group.

Group spend limits work alongside individual spend limits. If a member has an individual spend limit set, their individual limit takes precedence over any group limit.

## Set a group spend limit

1. Navigate to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)**.
2. Select the “By group” tab.
3. Find the group and click the menu button to the right, then “Edit limit”
4. Select “Unlimited,” or “Set dollar amount” and enter a dollar amount for the spend limit.
5. Click "Set limit."

The spend limit applies to all members of the group. Members who also have an individual spend limit set are governed by their individual limit instead.

## How spend limits are resolved

When determining a member's effective spend limit, the system evaluates in this order:

1. **Individual limit**—if the member has an individual spend limit set, that limit applies regardless of group membership.
2. **Group limit**—if the member has no individual limit, the system checks their group memberships. If the member belongs to multiple groups with spend limits, the lowest (most restrictive) limit applies.
  1. This lets you set a broad spend limit on a larger group and then create subgroups with lower limits for teams that need tighter budget controls.
3. **No limit**—if the member has no individual limit and belongs to no groups with spend limits, no spend limit is applied.

## Related Articles
- [Manage extra usage for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-extra-usage-for-team-and-seat-based-enterprise-plans)
- [Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)
- [Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)
- [Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
- [How SCIM sync works for Enterprise organizations](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)
