---
title: "Use connectors to extend Claude's capabilities"
title_slug: "use-connectors-to-extend-claudes-capabilities"
source_url: "https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities"
last_updated_iso: "2026-04-15T01:48:48Z"
article_id: "12075123"
breadcrumbs:
  - "Connectors"
  - "General"
---

# Use connectors to extend Claude's capabilities

_Last updated: 2026-04-15T01:48:48Z_

This guide explains how to enable and use connectors with Claude to enhance its capabilities.

> Web connectors are available for all users on Claude, Cowork, Claude Desktop, and Claude Mobile (iOS and Android). Desktop extensions are available to all users on Claude Desktop.

What are connectors?

Connectors let Claude access your apps and services, retrieve your data, and take actions within connected services. Claude inherits each person's permissions from the connected service. If someone can't access a specific file, channel, or record in the source system, the connector can't reach it from Claude either.

For example, you can connect Claude to Linear to create issues, to Slack to send messages, or to Google Drive to search your files. Connectors work across Claude, Claude Desktop, Claude Code, and the API (via the **[MCP Connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)**).

You can find available connectors in the **[Connectors Directory](https://claude.ai/connectors)**, where each connector has a page detailing its use cases, read/write capabilities, and availability. You can also add custom connectors or connect to any service that supports MCP.

Browse available connectors

> You can browse the Connectors Directory on Claude and Claude Desktop. It isn't possible to browse the directory on Claude for iOS or Android at this time.

You can browse the directory from two areas:

**From a chat**

1. Click the "+" button in the lower left corner of your chat, or type "/" to open the menu.
2. Hover over “Connectors.”
3. Select “Manage connectors.”
4. Click the “+” button next to **Connectors**.
5. This opens a **Connectors** modal where you can see available connectors by category or scroll through the complete list.

**From settings**

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.
2. Click the “+” button next to **Connectors**.
3. Browse available connectors by category or scroll through the complete list.

---

Connect a service to Claude

> You can connect Claude to a new service on Claude and Claude Desktop. It isn't possible to add new connectors (custom or from the directory) on Claude for iOS or Android at this time.

To connect a service from the directory:

1. Click on the connector you want to add.
2. Review the connector's description and capabilities.
3. Click “Connect” or “Install” to begin the setup process.
4. Follow the authentication prompts to grant Claude access to your account.
5. Configure any specific settings or permissions as needed.

> **Important:** When connecting to a service, you're granting Claude permission to access and potentially modify data within that service based on your account permissions. Only connect services you trust and need for your workflows.

Connect a service on Team and Enterprise plans

Before members of Team and Enterprise plans can use connectors, an Owner or Primary Owner needs to enable them for the organization. Enabling a connector makes it available to your team, but it doesn't automatically grant anyone access. Each person still needs to authenticate individually before they can use it.

1. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
2. Click “Browse connectors” at the bottom of the page.
3. Select the connector from the list and click “Add to your team.”
4. Individual users can then authenticate with the connector to start using it with Claude.

Once enabled at the org level, individual users follow the same steps described above to connect and authenticate.

## Restrict actions within connected services

Owners on Team and Enterprise plans can limit which actions a connected service can take across your organization. For example, you can allow a connector to read data from a service while preventing it from writing any changes back. This applies org-wide to everyone using the connector—individual users can't override it.

Common use cases:

- Allow Claude to search and summarize email, but prevent it from sending messages.
- Allow Claude to read files in Google Drive, but prevent it from creating or editing documents.
- Allow Claude to view Linear issues, but prevent it from creating new ones or changing status.

To configure action restrictions:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**
2. Select the connector to see **Tool permissions**.
3. The permissions will be categorized by type (for example, read-only tools, write/delete tools)
4. You
5. For each permission category or individual permission, select Always allow, Needs approval, or Blocked.

> **Note:** Action restrictions work alongside source-system permissions. Even when you allow a write action in Claude, a person still needs the underlying permission in the source system to make that change. Restricting actions in Claude never grants more access than the source system permits—it only narrows it.

---

Use connected services

Once you connect to a service on Claude or Claude Desktop, it will be available to use the next time you log in to your account on Claude for iOS or Android.

Once connected, services become available in your conversations:

1. Click the “+”** **button in the lower left of the chat interface (you can also type “/” to open this menu).
2. Hover over “Connectors” to open the menu.
3. Enable the specific services you want Claude to use for that conversation by toggling them on.
4. Claude will now be able to use these services when relevant to your requests.

For example, after connecting Linear, you can ask Claude to "Create a new issue for the login bug" and Claude will use Linear to create the issue in your workspace.

Some connectors are interactive and can render live interfaces—like dashboards, task boards, and design tools—directly within your conversation. Look for the **Interactive** badge in the Connectors Directory to find connectors with this capability.

---

Choose how connectors load in your conversation

When you add many connectors, Claude gives you control over how they load. You can find the **Tool access** setting by clicking the “+” button in the lower left corner of your chat, or typing “/” to open the menu. Hover over “Connectors,” then “Tool access” to choose your preferred mode. For most users, **Auto** (the default) works well. If you have 10 or more connectors active, consider switching to **On demand** to give your conversations more room.

Learn more about tool access modes: **[Manage Claude's tool access](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access)**.

---

Manage your connectors

To manage your connected services:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.
2. View all your connected services in the **Connectors** section.
3. For each service, you can disconnect it, modify connection settings, or review permissions and access levels.

---

Custom connectors

> Custom connectors using remote MCP are available on Claude, Cowork, and Claude Desktop for users on free, Pro, Max, Team, and Enterprise plans. Free users are limited to one custom connector.

In addition to directory connectors, you can add custom connectors:

1. Navigate to **[Customize > Connectors](http://claude.ai/customize/connectors)**.
2. Click the “+” button next to **Connectors**.
3. Select “Add custom connector.”
4. Enter the connector's name and URL.
5. Enter advanced settings (OAuth Client ID and secret) if desired.
6. Click “Add,” then follow the same connection process as directory connectors.

Custom connectors connect to your MCP server from Anthropic's cloud, not from your local device. Your server must be reachable over the public internet. If it's behind a firewall or on a private network, see **[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166)** for network requirements and private network options.

> **Important:** Custom connectors allow you to connect Claude to services that haven't been verified by Anthropic. Only connect to servers from trusted organizations and review authentication permissions carefully.

---

Security and privacy

All data transfers are encrypted. When using connectors, you can only sync content to Claude that you have permission to view in the original source.

When connecting to services from the directory, review what access the service is requesting during the connection process. Disconnect services you no longer need or use.

**For Team and Enterprise plans:**

- Access permissions are enforced at the user level. Users need to authenticate with the third-party service when first using the connector, even after an Owner or Primary Owner enables it.
- Connectors are only available in private projects.
- Chats with synced content can't be shared.

---

Troubleshoot connection issues

If you're having trouble connecting to a service, try these steps:

1. Check that you have a stable internet connection.
2. Verify you have an active account with the service.
3. Review any permissions or account type requirements for the service.
4. If authentication fails, try disconnecting and reconnecting from **[Customize > Connectors](http://claude.ai/customize/connectors)**.

## Custom connector not connecting or timing out?

Custom connectors (remote MCP servers) are reached from Anthropic's cloud infrastructure, not from your local machine. This is true even if you're using Cowork or Claude Desktop, which run locally on your computer. If your MCP server is behind a corporate firewall, on a private network, or not reachable over the public internet, the connection will fail.

To resolve this, you can either allowlist Anthropic's IP ranges in your firewall to create a secure outbound-only connection from your network. For detailed guidance, see the network requirements section in **[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166)**.

## Related Articles
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [When to use desktop and web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
