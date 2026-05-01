---
title: "Get started with custom connectors using remote MCP"
title_slug: "get-started-with-custom-connectors-using-remote-mcp"
source_url: "https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp"
last_updated_iso: "2026-04-02T19:24:29Z"
article_id: "12073865"
breadcrumbs:
  - "Connectors"
  - "Custom Connectors"
---

# Get started with custom connectors using remote MCP

_Last updated: 2026-04-02T19:24:29Z_

> Custom connectors using remote MCP are available on Claude, Cowork, and Claude Desktop for users on Free, Pro, Max, Team, and Enterprise plans. Free users are limited to one custom connector. This feature is currently in beta.

## What are custom connectors?

Custom connectors let you connect Claude directly to the tools and data sources that matter most to your workflows. This enables Claude to operate within your favorite software and draw insights from the complete context of your external tools.

You can:

- Connect Claude to existing remote MCP servers.
- Build your own remote MCP servers to connect with any tool.

> **⚠️ Security and Privacy with Custom Connectors (beta)**
>
> Be aware that custom connectors allow you to connect Claude to services that have not been verified by Anthropic, and allow Claude to access and take action in these services. For more guidance, review the **[Security and privacy considerations](#h_9088ccdf4d)** section below.

## What are remote MCP servers?

The Model Context Protocol (MCP) is an open standard, created by Anthropic, for AI applications to connect to tools and data.

Previously, **[MCP servers only ran locally](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)** (i.e. on a user's laptop). Now, developers can build and host remote MCP servers that communicate with AI apps over the internet.

Remote MCP servers give models access to internet-hosted tools and data, transforming Claude into an informed teammate that can independently handle complex, multi-step projects tailored to your needs.

---

## Network requirements

When you add a custom connector, Claude connects to your remote MCP server from Anthropic's cloud infrastructure, rather than from your local device. This is true across every Claude client, including claude.ai, Claude Desktop, Cowork, and the mobile apps.

This means your MCP server must be reachable over the public internet from Anthropic's IP ranges. Servers hosted on a private corporate network, behind a VPN, or blocked by a firewall won't connect, even if you can reach them from your own machine.

#### If your server is on a private network

You’ll need to allowlist Anthropic's IP addresses in your firewall so inbound connections from Claude can reach your server. See **[Anthropic IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)** for the current ranges.

#### Why this applies to Cowork and Claude Desktop

Even though Cowork and Claude Desktop run on your computer, remote connectors are configured and brokered through your Claude account. The connection to your MCP server originates from Anthropic's servers, not from your machine's network interface. Local MCP servers configured in Claude Desktop via `claude_desktop_config.json` are a separate mechanism and do use your local network, but those aren't available in Cowork or claude.ai.

---

## Add a custom connector

> **Note:*** *While anyone can build and host connectors using remote MCP, only Owners can add them to Team and Enterprise plans. Once a connector has been added to a Team or Enterprise organization, users individually connect to and enable that connector. This ensures that Claude can only access tools and data that the individual user has access to.

#### For Team and Enterprise plans

**Preliminary steps for owners:**

Before members of Team and Enterprise plans can configure custom connectors, an  Owner or Primary Owner needs to follow these initial steps to add a custom connector to your organization:

1. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
2. Click the "Add" button.
3. Hover over “Custom,” then select “Web.”
4. Add your connector's remote MCP server URL.
5. Optionally, click “Advanced settings” to specify an OAuth Client ID and OAuth Client Secret for your server.
6. Finish configuring your connector by clicking "Add."

**Steps for members after connector is configured:**

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**
2. Find the custom connector your Owner added in the list (it will have a "Custom" label).
3. Click "Connect" to authenticate and start using the connector with Claude.

#### For Pro and Max plans

If you are using an individual Pro or Max plan, follow these steps to add a custom connector:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**
2. Click "+" then “Add custom connector.”
3. Add your connector's remote MCP server URL.
4. Optionally, click “Advanced settings” to specify an OAuth Client ID and OAuth Client Secret for your server.
5. Finish configuring your connector by clicking "Add."

#### Enabling connectors after configuration

You can enable connectors for individual conversations via the “+” button on the lower left of your chat interface, then "Connectors." You'll see your configured connectors with toggles allowing you to enable/disable them per conversation.

---

## Remove custom connectors

You can remove a custom connector by following these steps:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**
  1. Team and Enterprise Owners can do this on their organization's behalf in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**
2. Locate the "Connectors" section.
3. Click "Remove" or select the three dots next to the connector you'd like to remove.
4. Follow the prompts to remove.

If you're hoping to edit a custom connector, you'll need to remove it first, then re-add it using the updated details.

---

## Build custom connectors

To learn about building connectors to use with Claude, see **[Building custom connectors via remote MCP servers](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)**.

---

## Security and privacy considerations

Custom connectors allow you to connect Claude to arbitrary services that have not been verified by Anthropic. When you connect Claude to external services, you're granting it the ability to access and potentially modify data within those services based on your permissions. It’s important to make sure you’re only connecting to remote MCP servers that you trust and that you’re aware of Claude’s interactions with web connectors.

#### Security and permissions

When you add a custom connector to Claude, you'll typically go through an OAuth authentication process to securely sign in to the application and grant specific permissions. This allows Claude to interact with the application on your behalf, without Claude ever seeing your actual password. You can revoke these permissions at any time by disconnecting the connector in Claude's settings or the third-party service's security settings.

Remote MCP servers act as intermediaries between Claude and external applications. You should:

- **Only connect to trusted servers:** Only connect Claude to servers built and hosted by organizations and applications you trust.
- **Review requested permissions carefully:** During auth, review what permissions the MCP server is requesting to the application. Limit these scopes when possible and deny access if requested permissions seem unnecessary.
- **Be aware of prompt injections:** Malicious MCP servers may include hidden instructions that try to make Claude perform unintended actions. Claude has built-in protections that attempt to block these attacks, but it's important to pay attention to tool inputs & outputs and connect only to trusted servers.
- **Monitor changes in tool behavior:** Server developers may update tool behavior unexpectedly, leading to unintended or malicious behavior.

#### Reporting malicious MCP servers

If you become aware of a malicious MCP server, please report it to our **[vulnerability disclosure program](https://hackerone.com/anthropic-vdp/)**, and choose [`https://github.com/modelcontextprotocol`](https://github.com/modelcontextprotocol) as the Asset.

#### Taking actions with tools

Remote MCP servers give Claude tools it can invoke during your conversation. The developer of an MCP server can define what these tools do, including:

- Reading data from connected applications.
- Creating, modifying, or deleting data in connected applications.
- Taking actions on behalf of the user.

Claude can only access resources that you've given the server permission to access, but you should:

- Be aware of any actions Claude is taking and that they have no destructive or unintended effects.
- Review Claude's tool approval requests carefully and only click "Allow always" when using a server and tool that you trust to run unsupervised.
- Using the "Search and tools" menu, disable any tools that aren't relevant to the current conversation or that you don't want Claude to be able to invoke.

#### Interactive connectors

Some connectors can display interactive interfaces directly within your Claude conversations. Instead of only returning text-based responses, these connectors can open live, interactive apps — like dashboards, task boards, or design tools — right in the chat.

Interactive connectors appear in two ways:

- **Inline cards:** Compact components embedded in the conversation, showing summaries, confirmations, or quick actions.
- **Fullscreen view:** Immersive interfaces for complex interactions like data visualizations or document editing. The conversation composer remains available so you can continue chatting with Claude.

You can interact with these connectors directly — filtering data, checking off tasks, adjusting settings — without leaving the conversation. Any actions you take within the interface use the same permissions you granted when connecting the tool.

**Admin controls:** Team and Enterprise plan owners can disable specific tool calls that render interactive connectors within **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

#### Using Claude with Research

> **Note: ****[Advanced Research](https://claude.com/blog/integrations)** is not currently able to invoke tools from local MCP servers.

Research allows Claude to deeply investigate queries by searching through hundreds of internal and external sources. During the research process, Claude can invoke tools from your connectors automatically without further approval.

When using Research with custom connectors:

- Disable any tools that can take write actions in external applications.
- Review Claude’s approval request carefully and be aware of which tools you’re granting Claude permission to invoke.
- Be mindful of the impact of Claude sending a large number of requests to your connectors.

See **[Using Research on Claude](https://support.claude.com/en/articles/11088861-using-research-on-claude)** for more information about this feature.

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [When to use desktop and web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
