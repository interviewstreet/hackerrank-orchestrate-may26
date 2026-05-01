---
title: "Provision and manage Skills for your organization"
title_slug: "provision-and-manage-skills-for-your-organization"
source_url: "https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization"
last_updated_iso: "2026-04-09T02:15:27Z"
article_id: "14902443"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Capabilities"
---

# Provision and manage Skills for your organization

_Last updated: 2026-04-09T02:15:27Z_

This article explains how organization owners can provision skills for all users in their organization. Provisioning skills to your team allows you to distribute approved workflows and capabilities across your entire organization from a central location.

> Organization-wide skill management is available to Team and Enterprise plans.

## Prerequisites

Before you can provision skills for your organization, you must enable two capabilities by toggling them on:

1. **Code execution and file creation** in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**
2. **Skills** in **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**

Skills require code execution to function, so if code execution is disabled, skills will not be available.

---

## Provision skills for your organization

When you upload a skill through organization settings, it automatically becomes available to all users in your organization in **[Customize > Skills](https://claude.ai/customize/skills)**. This means that individual users no longer need to manually upload the same skills.

**To provision a skill:**

1. Navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**.
2. In the **Organization skills** section, click "+ Add."
3. Select a .zip file containing your skill (must include a SKILL.md file).
4. The skill is immediately provisioned to all users in your organization.

Admin-provisioned skills are enabled by default for everyone in your organization, but users can still toggle individual skills off if they choose. This gives organizations consistent, approved workflows across teams while letting individual users customize their experience.

---

## Control skill sharing between members

In addition to provisioning skills top-down, you can let members share skills they've built with each other. Two independent toggles control this:

- **Skill sharing:** Members can share a skill with specific colleagues. Recipients see the skill in the **Shared with you** section of their skills list.
- **Share with organization:** Members can publish a skill to the organization directory, where anyone can find and install it.

Both toggles are off by default. You can enable either or both in **[Organization settings > Skills](http://claude.ai/admin-settings/skills)**.

> **Note:** Shared skills are view-only. Recipients can enable and use a shared skill but can't edit its contents. Group sharing and edit permissions are planned for a future release.

#### How shared skills differ from provisioned skills

> **Important:** There's no approval workflow for org-wide sharing. If you enable **Share with organization**, any member can publish a skill to the directory without review. Consider enabling peer-to-peer sharing only if this is a concern.

#### Monitor sharing activity

Skill sharing events are captured in the audit log and Compliance API as `role_assignment` events. You can see who shared a skill, with whom, and whether it was peer-to-peer or organization-wide.

The audit log doesn't capture the contents of shared skills—only the share event itself. There's no admin dashboard to browse or inspect the contents of skills shared between members.

---

## How members see provisioned and shared skills

Skills appear for each member in **[Customize > Skills](https://claude.ai/customize/skills)**, organized into three sections:

- **Personal skills:** Skills the member has created or uploaded.
- **Shared with you:** Skills colleagues have shared directly with a member. These appear grayed out until enabled.
- **Organization skills:** Skills an owner has provisioned and skills members have shared organization-wide. Members install these from the directory.

Owner-provisioned skills are marked with a visual indicator so members can distinguish them from other skill types. Members can click on any skill to preview its contents and description.

For more on how members browse and install from the directory, see **[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)**.

---

## How users see provisioned skills

Skills provisioned by an organization owner will appear for each user in **[Customize > Skills](https://claude.ai/customize/skills)** alongside Anthropic skills and any skills they've uploaded themselves.

These skills are marked with a visual indicator so users can distinguish them from other skill types. Users can click on any skill to preview its contents and description.

---

## Manage and remove provisioned skills

The **Organization skills** section in **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** displays all skills that have been provisioned for your organization. You can use search and section headings to navigate your provisioned skills.

To remove a skill from your organization, locate it in the **Organization skills** list and select the option to remove it. Once removed, the skill will no longer appear in users' Skills lists in **[Customize > Skills](https://claude.ai/customize/skills).**

> **Note: **Only owners can add or remove organization-wide skills. Individual users cannot delete provisioned skills, though they can toggle them off for their own use.

---

## Best practices

- **Test skills before provisioning: **Upload and test skills on your own account first to verify they work as expected before distributing them organization-wide.
- **Use descriptive names: **Give skills clear names that help users understand their purpose at a glance.
- **Write clear descriptions: **The skill's description helps Claude determine when to use it automatically. Ensure descriptions accurately reflect what the skill does.
- **Consider default status carefully: **Enable skills by default when they're broadly useful to most users. Use disabled by default for specialized skills that only some team members need.
- **Decide on sharing deliberately:** Peer-to-org sharing has no approval step. If you want to review skills before they reach everyone, keep org-wide sharing off and ask members to submit skills to an owner for provisioning instead.

## Related Articles
- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Manage Claude Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)
- [Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)
