---
title: "Use interactive connectors in Claude"
title_slug: "use-interactive-connectors-in-claude"
source_url: "https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude"
last_updated_iso: "2026-03-25T18:44:35Z"
article_id: "15411962"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Use interactive connectors in Claude

_Last updated: 2026-03-25T18:44:35Z_

> Interactive connectors are available for all users on Claude, Cowork, Claude Desktop, and Claude for iOS/Android.

## What are interactive connectors?

Some connectors can now display live, interactive apps directly within your Claude conversations. Instead of returning text-only responses, these connectors render interfaces—like analytics dashboards, task boards, or design tools—that you can interact with without leaving the chat.

For example, you might ask Claude about your project status, and instead of just describing it, Claude opens your Asana board right in the conversation. You can check off tasks, update statuses, and keep chatting with Claude—all in one place.

Claude can also generate its own custom visuals—diagrams, charts, and simple interactive elements built from scratch for your question. When a connected service offers an interactive interface that handles your request, like an MCP app, Claude will use it. Custom visuals fill the gaps when no connector interface fits what you’re asking for.

For more on Claude-generated visuals, see **[Custom visuals in chat](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat)**.

---

## How interactive connectors appear

Interactive connectors display in two ways:

**Inline cards** are compact components embedded directly in the conversation. They're ideal for quick summaries, confirmations, and single actions—like a status update or a message draft ready to send.

**Fullscreen view** provides an immersive interface for complex interactions like data visualizations, document editing, or detailed project views. The conversation input remains available so you can continue talking to Claude while interacting with the connector.

## Interact with connectors

You can interact directly with elements inside the connector:

- Filter, sort, or drill into data
- Toggle settings, check boxes, or make selections
- Confirm and execute actions (mark complete, send, save)
- Expand and collapse content sections

If you need to ask Claude to modify something, refine a result, or navigate to a different context, type in the conversation input—Claude can interpret your request and update the interface accordingly.

## Which connectors are interactive?

In the **[Connectors Directory](https://claude.ai/directory)**, connectors with this capability are marked with an "Interactive” badge. Current interactive connectors include:

- **Amplitude** — View and interact with analytics dashboards
- **Asana** — Manage tasks and project boards
- **Box** — Work with documents and files
- **Canva** — Create and edit designs
- **Clay** — Manage contacts and outreach
- **Figma** — Review and annotate designs
- **Hex** — Explore data and notebooks
- **Slack** — Draft and send messages

We’re adding support for more interactive connectors over time.

## Get started with interactive connectors

1. Navigate to the **[Connectors Directory](https://claude.ai/directory)**.
2. Look for connectors marked with the "Interactive" badge.
3. Connect and authenticate with the connector.
4. Start a conversation with Claude and ask about something the connector handles—the interactive elements will appear automatically when relevant.

> **Note:** Interactive connectors are default on when you have the relevant connector enabled. No additional setup is needed.

## Considerations for Team and Enterprise plans

#### Can Team and Enterprise owners control interactive connectors separately from standard connectors?

Yes. Team and Enterprise owners can disable the specific tool calls that render interactive connectors within **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. This does not disable the connector itself — text-based tool functionality continues to work normally.

---

## Permissions and security

#### How are interactive connectors secured?

Interactive connectors run in sandboxed iframes with strict Content Security Policies. All communication between the interface and Claude uses auditable JSON-RPC messaging. Servers must predeclare which external domains they need, and the host can review HTML content before rendering.

#### Do interactive connectors require additional permissions beyond the connector itself?

No. Interactive connectors use the same permissions you granted when connecting the tool. They don't request additional access to your data.

#### Can interactive connectors make purchases or financial transactions?

No. Purchases through third-party interactive connectors are not supported.

---

## Troubleshooting

#### The interface isn't appearing

- Check that the connector is connected and enabled for your current conversation.
- Try starting a new conversation and asking Claude a question that the connector handles.

#### The connector isn't responding to interactions

- Check your internet connection.
- Try refreshing the page or restarting Claude Desktop.
- If the issue persists, disconnect and reconnect the connector in **[Settings > Connectors](https://claude.ai/settings/connectors)**.

#### I want to disable interactive connectors

- **Team and Enterprise users:** Ask your organization owner to disable the relevant tool calls in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
- **Individual users:** You can disable specific connector tools via the "Search and tools" menu in your conversation.

---

## I'm a developer. Where can I learn about building MCP Apps?

MCP Apps is the open-source extension to the Model Context Protocol that powers interactive apps. If you are building your own interactive connector, note that it must meet additional design, security, and testing requirements. See the **[Remote MCP Server Submission Guide](https://support.claude.com/en/articles/12922490)** for details.

## Related Articles
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [When to use desktop and web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)
