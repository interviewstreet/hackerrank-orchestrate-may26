---
title: "Claude in Chrome admin controls"
title_slug: "claude-in-chrome-admin-controls"
source_url: "https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls"
last_updated_iso: "2026-03-16T21:05:18Z"
article_id: "14843295"
breadcrumbs:
  - "Claude in Chrome"
---

# Claude in Chrome admin controls

_Last updated: 2026-03-16T21:05:18Z_

> Claude in Chrome admin controls are available in beta for Team and Enterprise plans.

This article explains how Team and Enterprise Owners can manage Claude in Chrome for their organization.

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites on behalf of your users. As an Owner, you control whether the extension is available for users to install and which sites they can access.

> **Important:** Before enabling Claude in Chrome for your organization, review **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)** to understand the risks of browser-based AI, including prompt injection attacks.

## Accessing Claude in Chrome settings

To manage Claude in Chrome settings for your organization:

1. Sign in to Claude with your Owner account.
2. Navigate to **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension)**.

## Enabling or disabling the extension

Use the toggle to enable or disable Claude in Chrome for your entire organization.

- **Team plans:** The extension is enabled by default. Disable it if you prefer users not to have access.
- **Enterprise plans:** The extension is disabled by default. Enable it when you're ready for users to access the feature.

> **Note:** When you enable the extension for an Enterprise organization, users are not automatically notified. You may want to communicate availability through your internal channels.

## Configuring site access

Use allowlists and blocklists to control which websites Claude can access when users are working with the extension.

**Allowlist:** Specify which sites Claude is permitted to access by adding them to the allowlist. We recommend starting with a restrictive allowlist, especially during initial rollout.

**Blocklist:** Specify sites Claude should never access, regardless of other settings, by adding them to the blocklist. This adds an extra layer of protection beyond **[Claude's default blocked categories](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely#h_34f8d5ca87)**.

**Recommendation:** Start with a more restrictive allowlist for the security of your organization's data, then expand access over time as you become comfortable with the extension's behavior.

## Managing user access on Claude Desktop

Users with both Claude in Chrome and Claude Desktop installed will now have the option to start a task on the desktop app and let it handle work in the browser without switching windows.

If you want to disable this for members of your organization, you can toggle the extension off entirely, or edit your Enterprise configuration.

**Disable the Chrome extension in organization settings:**

1. Click your initials in the lower left corner, then select “Organization settings.”
2. Navigate to “Connectors.”
3. Find **Claude in Chrome** in the list and click “Configure.”
4. Toggle the connector off.

Alternatively, disable `isLocalDevMcpEnabled` in **[your Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)**.

## Deployment options

Once enabled, users can access Claude in Chrome in two ways:

- **Self-service:** Users install the extension themselves from the **[Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)**.
- **Managed deployment:** Use your existing Chrome management tools (Google Workspace admin console or MDM) to deploy the extension to specific users or groups.

Most Enterprise organizations already have Chrome extension management in place. You can use these existing controls to limit which employees can install the extension during a pilot phase.

## Running a pilot

To test Claude in Chrome with a subset of users before broader rollout:

1. Enable the extension at the organization level.
2. Configure a restrictive allowlist limiting Claude to specific, trusted sites.
3. Use your IT controls to limit which employees can install the extension.
4. Share **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)** with pilot users.
5. Gather feedback and expand access over time.

## Educating your users

We recommend sharing these resources with users before they start using Claude in Chrome:

- **[Getting started with Claude in Chrome](https://support.claude.com/en/articles/12012173-getting-started-with-claude-for-chrome)**: Installation and core capabilities
- **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)**: Risks and best practices
- **[Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-for-chrome-permissions-guide)**: How users control what Claude can access

## Related Articles
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- [Claude in Chrome Troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)
- [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)
- [Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)
