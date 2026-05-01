---
title: "Getting started with Claude in Slack"
title_slug: "getting-started-with-claude-in-slack"
source_url: "https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack"
last_updated_iso: "2026-03-16T21:05:58Z"
article_id: "12487295"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Getting started with Claude in Slack

_Last updated: 2026-03-16T21:05:58Z_

You can now integrate Claude and Slack, giving you two ways to use them together: add Claude directly to your Slack workspace, or enable the Slack connector for your Claude apps.

## What is Claude in Slack?

> The Claude app is available to users on paid Slack plans. Slack admins must approve the Claude app before individual users can access it.

It’s how we’ve brought Claude’s capabilities directly to Slack, bringing AI assistance into your team’s workspace. This integration allows you to work with Claude without leaving Slack through three convenient surfaces:

**Direct message with Claude**: Start a private conversation with @Claude.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755143775/0ac74968f16b0c304ad05c1501c3/8f870a90-c622-449d-9eba-0a2edf5d63f1?expires=1776784500&signature=6b59c35c77ae2453c4faaef22e8b49ed17f73d49135f2d7f688a88f239ec19fb&req=dSciE8h6noZYXPMW1HO4zb2WBQMEHoBy5mlLMjhGEMHnTsf%2B%2BytyhdS2jgfa%0AKw5%2FEVauakBxh%2BpSfIM%3D%0A)

**AI assistant panel**: Click the Claude icon in Slack's AI assistant header to open a panel on the right side of your Slack window, allowing you to access Claude from anywhere in the Slack app.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755144720/47781e38d6f97597aa494e0aeb2d/38f88d2c-aa96-4d35-8a02-7ad6b23f8699?expires=1776784500&signature=5bddc21aee7a4bdfdbf8deb468b7939ca4646cb1aa6d0217089da1dc4933052a&req=dSciE8h6mYZdWfMW1HO4zUifwjfeH6ehPUSeDntyEuV7y5et3bvuJurac7yQ%0AGhpoROo%2BAwUotq35lSc%3D%0A)

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755145556/3155c34bba5a64e0ab7b760e78c2/5c54e519-3c0d-4ffa-a555-0b9d9660ea53?expires=1776784500&signature=f98a026e1720147a9b379773ae6ce4e05de0bfd8e62e61abd8aa1199c9d59ec5&req=dSciE8h6mIRaX%2FMW1HO4zXrVXd57%2BIvGBGejWRiWDiKctfMBkgAR8%2BoQZWYT%0AXGFe4EKZl9aEBilAlxc%3D%0A)

**Thread participation**: Mention @Claude in any thread to get Claude's help with the conversation.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755146282/dd7e489f38bd786346478a9b286e/c3e07137-64e6-470c-9f3f-1db2632a784e?expires=1776784500&signature=7252815b8053eb20c4d98e62aaa5d330b60007f7359933034009dd5968087172&req=dSciE8h6m4NXW%2FMW1HO4za6vkdbjCgEidk%2ByK9LXwIKtPqfdRVUZE2sNgv2O%0AMhYg%2FXBBh72cDH6VxF8%3D%0A)

All surfaces provide the same capabilities that you have enabled in Claude, including web search and connections to your integrated tools, allowing you to seamlessly integrate AI assistance into your existing workflow.

> **Note:** Team and Enterprise plan users with access to Claude Code on the web can also route coding tasks directly to Claude Code by mentioning @Claude. See [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack#h_adda66b697) for details on this beta feature.

---

## Enabling and installing Claude in Slack

#### For Slack admins

1. Go to the [Claude app in the Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4).
2. Click "Add to Slack" on the Claude app page.
3. Review and approve the app for your organization.
4. Choose whether to deploy org-wide or to specific workspaces.

**To install across all workspaces:**

1. Navigate to your Slack management workspace at: [https://app.slack.com/manage/<INSERT_SLACK_ID>/workspaces/all](https://app.slack.com/manage/<INSERT_SLACK_ID>/workspaces/all)
  - Find your enterprise's Slack ID using the appropriate lookup method
2. Navigate to **Integrations → Installed apps → Add to more workspaces**.
3. Toggle through all relevant workspaces where you'd like to enable Claude.

#### For individual users

Once your Slack admin has approved Claude (or if you're on a personal Slack plan):

1. Find Claude in your apps list (search for "Claude" if it's not immediately visible), or go to the Slack App Marketplace.
2. Click "Connect Account” to be prompted to connect your Claude account:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755147280/abac53f0415690817c630a420091/98c15ecd-761c-4e0d-aeae-1c52d38e52c8?expires=1776784500&signature=662131c5087e1e7f1fb9b8615256ed52585e923db28a5faa3d4ddc4ed1934fd3&req=dSciE8h6moNXWfMW1HO4zRIwikq7TSRj%2Fy7g3WAjXh6ZBgXKGyHYMt8mN3nO%0AREP%2B%0A)
3. In the window that opens, select which organization you would like to connect with Claude for Slack.
4. Click “Authorize” to allow Claude in Slack to access your Claude chat account:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755147985/57be4bd15a4720466d9114ef9e0d/5944ab3f-20b9-43f7-b475-127b98a3eef4?expires=1776784500&signature=4ba0dd7d3028bcc8950b0d1ee102c938eacd97783c8cf835d4eeda20775a4b57&req=dSciE8h6mohXXPMW1HO4zcpXRZM8GgmRFQ%2BRWX0w%2Fe4orCYn5qdU3BcHuJ5C%0AaDjS%0A)
5. You should see a confirmation message upon successful connection:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755148657/71571a264d97c7a145c399b3e653/f0d32375-bf8f-47d5-89e3-c165eb3a1d41?expires=1776784500&signature=1b68628612b45659148663af6d0d16e78b63a96205c49bb1fc857d99eb80fb78&req=dSciE8h6lYdaXvMW1HO4zZ9S5TcefJVuXLLzhWuBjzNae63UTFHmDwuxmwif%0AAHBJ%0A)
6. After successful authentication, return to Slack.
7. Click “+ New Chat” to start a conversation with Claude, or @mention Claude in any Slack conversation to access its capabilities.

> **Tip**: Add Claude to your Slack header for quick access by clicking the three dots "..." at the top right and selecting "Add this app to header."

**Enabling Claude Code in Slack (beta)**

Team and Enterprise plan users can route coding tasks from Slack to Claude Code on the web. To enable this capability:

1. A Claude Owner or Primary Owner must enable Claude Code on the web by navigating to **[Organization settings > Claude Code](http://claude.ai/admin-settings/claude-code)**.
2. Individual users must have access to Claude Code on the web.

Once enabled, mentioning @Claude for coding tasks will automatically create a Claude Code session. Learn more about **[using Claude Code in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack#h_adda66b697)**.

---

## What is the Slack connector?

> The Slack connector is available for all paid plans (Pro, Max, Team, and Enterprise).

Enabling the Slack connector allows Claude to search within your Slack workspace’s channels, direct messages, and shared files to pull relevant context into your conversations. Note that members of Team and Enterprise plan organizations will not see the option to enable the Slack connector individually until it’s enabled by an Owner.

> **Important:** You must install Claude in Slack before enabling and using the Slack connector.

## Enabling the Slack connector

#### Team and Enterprise owners

1. Log in to your Owner or Primary Owner account and click your initials in the lower left corner.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Under “Connectors,” click the "Enable" button next to the Slack connector.
4. Users can then authenticate in their individual connector settings to begin using Slack in Claude.

#### Individual Pro, Max, Team, and Enterprise users

1. Log in to your Claude account and click your initials in the lower left corner.
2. Navigate to **[Settings > Connectors](http://claude.ai/settings/connectors)**.
3. Find the Slack connector and click “Connect.”
4. Click "Connect" to authenticate with the connector and start using Slack in Claude.

---

## Managing your Claude in Slack connections

#### Viewing Claude app connection status

1. Click on the Claude app in your Slack sidebar.
2. Go to the "Home" tab.
3. You'll see your connection status, including your connected account email and organization name.

#### Disconnecting the Claude app

To disconnect your Claude account from Slack:

1. Go to the Claude Home tab in Slack.
2. Under **Disconnect Claude Account**, click the red "Disconnect" button.
3. Confirm the disconnection.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755149744/97a579fedf87deb5e5b6abf48963/4cab9f61-9f98-40c4-969a-f590716dfb38?expires=1776784500&signature=6d5e36a40a0da97e23aa79ed923f386f78a7361599e3feadfb4dc8d75ef6a7ac&req=dSciE8h6lIZbXfMW1HO4zdIAspNMZrWVQgg7UiXQlE00RiyqBu6k8uoivuXk%0A8DW2NTgaSNKv6e3CbhA%3D%0A)

Disconnecting will:

- Remove the connection between your Claude account and Slack workspace.
- Delete all past Claude conversations in Slack from Claude (within 30 days).
- Preserve conversations in Slack, but Claude won't have awareness of them if you reconnect

#### Disconnecting the Slack connector

You can also disconnect the Slack connector from your Claude settings (or you can enable/disable the connector for an individual chat):

1. Go to[ ](https://claude.ai/settings/integrations)claude.ai/settings/connectors
2. Find **Slack** in your list of Connectors.
3. Click the menu (...) and select "Disconnect."

---

## Privacy and data

#### Data storage

Your Slack conversations with Claude remain separate from your Claude history, keeping work organized across platforms.

#### Data visibility

- Conversations initiated in Slack are not visible in [your Claude chat history](http://claude.ai/recents).
- Conversations initiated in the Claude web app are not accessible in Slack.
- Each platform maintains separate conversation histories.

#### Data deletion

- Conversations are automatically deleted from Claude within 30 days if you disconnect the integration or uninstall the app.
- Your conversations in Slack follow your organization's Slack retention policies.

---

## Frequently asked questions

#### I’m trying to add Claude in Slack but it’s not working – help!

If you are using a company Slack instance and are not assigned to an Admin role, a Slack Admin must approve the Claude app on behalf of your organization before you’re able to download it. If you try to skip this step and install Claude in Slack, you’ll see a **Request to install **prompt where you can send a message to your Slack Admin. Work with them to approve the app and make it available for your team.

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
