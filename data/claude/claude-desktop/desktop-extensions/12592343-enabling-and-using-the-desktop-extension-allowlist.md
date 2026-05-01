---
title: "Enabling and using the desktop extension allowlist"
title_slug: "enabling-and-using-the-desktop-extension-allowlist"
source_url: "https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist"
last_updated_iso: "2026-03-16T21:04:20Z"
article_id: "14112186"
breadcrumbs:
  - "Claude Desktop"
  - "Desktop extensions"
---

# Enabling and using the desktop extension allowlist

_Last updated: 2026-03-16T21:04:20Z_

> The desktop extension allowlist is available for Owners and Primary Owners of Team and Enterprise plans.

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

## How to enable the allowlist

> **Important: **If you’ve previously configured Enterprise policy controls at the user-machine level, these will override the in-app allowlist. Ensure both `isDesktopExtensionDirectoryEnabled` and `isDesktopExtensionEnabled` are not set to "false" so the allowlist can populate the available registry. Refer to our **[desktop enterprise configuration documentation](https://support.claude.com/en/articles/12622667-enterprise-configuration)** for more information.

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that **users will be able to access all desktop extensions in the registry until you enable the allowlist. **To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

**To turn on the allowlist:**

1. Open Claude Desktop
2. Click your initials or name in the lower left corner
3. Navigate to Organization settings > Connectors
4. Switch to the "Desktop" tab:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755172/63c92550571842577ad435860ec5/6f5cc4e1-ff7d-48de-863a-c4e6184d4605?expires=1776784500&signature=2ce550ce021c9c01f6ed9e2d108fe3f414c22408c425169e39a2a0f62ffa942c&req=dScvF857mIBYW%2FMW1HO4zQ9pUkwN93Te0ugSQm1MFW%2Bgb05iSoIVwwdP0f1B%0ABU%2Bq%0A)
5. Toggle **Allowlist** on:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781755578/a6bafff5f084dc86ae463703fd3d/6cf0ee18-4e71-4129-98e8-cc08174e3c3a?expires=1776784500&signature=85521d81559f2a062dae2e48d5cf9789fc17991031b6d6a55effb054cfeb69da&req=dScvF857mIRYUfMW1HO4zaj0C3csQaMBTAorLxpdoc9wBiBjIBSCViSUQS1u%0AyLhN%0A)

## What happens after enabling the allowlist?

Once the allowlist is enabled:

- Any existing desktop extension installations will be force-deleted from Claude Desktop clients.
- Users will no longer be able to install new desktop extensions that are not included within the allowlist.
- Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs.

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

> **Important:** The allowlist requires Claude Desktop version 0.13.91 or higher, so users should update the desktop app by clicking “Claude”, then either “Check for updates” or “Restart to update to Claude 0.13.91”:
>
> ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781756960/ad18af50c83d35f2673656c23e00/a7ee450f-0c7d-42d6-a75f-fb1bc088cb52?expires=1776784500&signature=d595488fc3979f06196ec0df500171c9f3654b0a28aac562996b9772f48e0e35&req=dScvF857m4hZWfMW1HO4zYUJpoWtAjbuCEDZ5AdBjIbXm6XWXKFUxMN3Mu1I%0AlucEutu%2B78fXFC0WBRc%3D%0A)

## Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1. Navigate to Organization settings > Connectors and select the “Desktop” tab.
2. Click “Browse extensions” to view the list of available extensions.
3. Select the extension you want to add.
4. Click the “Add to your team” button.
5. The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1776784500&signature=3ea8de8f49e0e8a049f12b7b90531abc2c946d38d05b1548658369cd179a04e7&req=dScvF857nINaWfMW1HO4zTrxCq4u91OQqXridZhfx1ILl71dcjsP%2B5zhHX4a%0APJhAJsIJzHDJxB%2Fv3P0%3D%0A)

## Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Organization settings > Connectors > Desktop.

> **Note:** Ensure the name field in the manifest.json does not overlap with any existing MCPBs. All names for unique MCPBs / desktop extensions must be unique.

1. Click “Add custom extension”
2. This will open a filepicker; select the .mcpb file.
3. The extension will appear under **Custom team extensions**.
4. Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our **[desktop extension developer documentation](https://github.com/anthropics/mcpb)**.

## Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.

## Related Articles
- [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
- [Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)
- [Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)
