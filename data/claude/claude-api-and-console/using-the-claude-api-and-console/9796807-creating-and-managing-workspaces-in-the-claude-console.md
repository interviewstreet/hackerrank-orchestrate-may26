---
title: "Creating and managing Workspaces in the Claude Console"
title_slug: "creating-and-managing-workspaces-in-the-claude-console"
source_url: "https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console"
last_updated_iso: "2026-03-16T21:19:36Z"
article_id: "10177277"
breadcrumbs:
  - "Claude API and Console"
  - "Using the Claude API and Console"
---

# Creating and managing Workspaces in the Claude Console

_Last updated: 2026-03-16T21:19:36Z_

This guide will walk you through the process of creating, editing, and managing Workspaces in your Claude Console organization.

## What are Workspaces?

Workspaces are collaborative spaces within Console organizations where teams can separate API resources by use case.

## How to create a new Workspace

> **Note:** Only Organization Admins can create new Workspaces.

1. Log in to your [Claude Console account](https://platform.claude.com/login).
2. Navigate to the **Workspaces** section by clicking on "Settings" in the top level menu and selecting “Workspaces” from the left side bar ([Settings > Workspaces](https://platform.claude.com/settings/workspaces)).
3. Click the "Add Workspace" button near the top right of the page.
4. In the modal that appears, enter a name for your new Workspace, and select a color assignment. This color assignment will be used to help visually identify your workspace in the Claude Console.
5. Click "Create" to finalize the new Workspace.

Your new Workspace will now appear in the list of Workspaces.

> **Note:** You are limited to 100 workspaces per organization.

## Editing Workspace Settings

1. From the **Workspaces** list, click on the ellipsis next to the Workspace you want to edit.
2. Select “Edit details."
3. You can modify the following settings:
  - Workspace Name
  - Color
4. After making your changes, click "Save" to apply them.

> **Note:** The default Workspace is not editable and cannot be removed.

## Adding members to a Workspace

> **Note:** You must add members to your Console organization by following [these instructions](https://support.claude.com/en/articles/13443764-inviting-members-to-the-claude-console) before you can add them to a Workspace.

1. Navigate to the desired Workspace's details page by clicking on it from the Workspaces list.
2. Click on the “Members” tab.
3. Click on “Add to Workspace” near the top right of the page.
4. Choose the individual you’d like to add from the list of your organization’s members.
5. Assign a Workspace role for this member.
6. Confirm your selections by clicking “Add to Workspace."

> **Note:** Organization Admins are automatically added as Workspace Admin to every Workspace. Organization Billing role holders are automatically granted ability to see cost, usage, and limit values for all Workspaces, but can be upgraded to the Organization Admin role.

## Deleting members from a Workspace

Click the trash can icon next to the member to remove them from your Workspace.

> **Note:** Organization members with Admin and Billing roles are automatically granted permissions on all Workspaces and cannot be removed from Workspaces.

## Managing API Keys in a Workspace

1. Navigate to the desired Workspace's details page by clicking on it from the **Workspaces** list.
2. Click on the "API Keys" tab.
3. To create a new API key for this Workspace:
  - Click "Create Key"
  - Give the key a descriptive name
  - Click "Create Key"
4. To revoke an existing API key:
  - Find the key in the list
  - Click the ellipsis next to it
  - Select "Disable API Key" or “Delete API Key”
    - **Note:** Deleting an API key is a permanent action and cannot be undone.
  - Confirm the action

> **Note:** API keys are tied to the Workspace they're created in and cannot be moved between Workspaces.

## Setting Workspace Rate Limits

1. Navigate to the desired Workspace's details page by clicking on it from the **Workspaces** list.
2. Click on the "Limits" tab.
3. Set a limit for each model tier and limit type by clicking on the pencil icon next to each option.
4. Workspace Spend Limits can be reset to the organization rate limit by clicking the “Refresh” icon next to the rate limit you previously set for the Workspace.

> **Note:** Anthropic always evaluates all applicable limiters -- at the Workspace and Organization level -- for every request. In other words, if the Workspace limits are unset, Organization limits still apply.

## Setting Workspace Spend Limits or Notifications

1. Navigate to the desired Workspace's details page by clicking on it from the **Workspaces** list.
2. Click on the "Limits" tab.
3. Choose one of the following:
  - Select “Change Limit” to set a specific spend limit for this Workspace.
    - **Note:** You can only set a spend limit that is lower than your organization’s limit. If unset, your spend limit defaults to the organization’s limit.
  - Select “Add notification” to set up an email notification when the Workspace spend reaches a specific amount.

##

## Viewing Workspace Usage and Costs

1. Navigate to the [Usage or Cost Reports](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console).
2. Choose to view by an individual Workspace, or by “All Workspaces”.

## Archiving a Workspace

If you no longer need a Workspace but want to retain its historical data:

1. Navigate to the **Workspaces** page.
2. Click the ellipsis next to the Workspace you would like to archive.
3. Confirm that you want to archive the Workspace.

> **Note:** Archiving a Workspace will archive all API keys in the Workspace. This action cannot be undone.

## Managing the Default Workspace

Every organization has a default Workspace that cannot be renamed, archived, or deleted. To view API keys associated with the default Workspace:

1. Navigate to the **Workspaces** list.
2. Click on "Default" in the list.

> **Note:** You can view your default Workspace’s limits from the [Limits settings](https://platform.claude.com/settings/limits).

## Related Articles
- [Cost and Usage Reporting in the Claude Console](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console)
- [Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)
- [Sharing Prompts in the Claude Console](https://support.claude.com/en/articles/10722177-sharing-prompts-in-the-claude-console)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Inviting members to the Claude Console](https://support.claude.com/en/articles/13443764-inviting-members-to-the-claude-console)
