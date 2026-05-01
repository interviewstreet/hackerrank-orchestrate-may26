---
title: "Manage Claude’s tool access"
title_slug: "manage-claudes-tool-access"
source_url: "https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access"
last_updated_iso: "2026-03-16T21:33:28Z"
article_id: "15860163"
breadcrumbs:
  - "Connectors"
  - "General"
---

# Manage Claude’s tool access

_Last updated: 2026-03-16T21:33:28Z_

When you connect many services to Claude, you can control how those connectors are loaded into your conversations. This helps Claude work more accurately and efficiently, especially if you've added 10 or more connectors.

> Tool access modes are available for all users on Claude, Cowork, Claude Desktop, and Claude Mobile (iOS and Android).

## Why tool access matters

Each connector takes up space in a conversation. With a small number of connected services, this is rarely noticeable. But as your connector library grows, the combined overhead can limit how much room is left for your actual work: documents, code, and conversation history.

To address this, Claude supports three tool access modes that control when and how your connectors are loaded.

---

## Tool access modes

You can manage Claude’s access to your connectors per conversation using the **Tool access** setting in your chat.

Choose from three options:

- **Auto** *(default)*: Claude decides dynamically which connectors to load based on what you're working on. This is the best starting point for most users.
- **Always available**: All your connectors are loaded at the start of every conversation. Claude can use any of them immediately, without any extra steps.
  - Best for: Fewer than 10 connectors you use constantly.
  - Trade-off: Uses more conversation space upfront.
- **On demand:** Connectors aren't loaded until Claude searches for the right one based on your request. Claude finds the most relevant connectors and loads only those.
  - Best for: Large connector libraries (10 or more), or when you're running into conversation length issues.
  - Trade-off: Claude may take an extra step to find the right connector before using it.

---

## Which mode should I use?

---

## How to change your tool access setting

You can set your tool access mode per conversation by following these steps:

1. Open a chat with Claude.
2. Click the “+”** **button in the lower left corner of your chat, or type "/" to open the menu.
3. Mouse over “Connectors,” then “Tool access.”
4. Select your preferred mode from the three options.

Your selection only applies to that conversation. You can change it at any time.

---

## Frequently asked questions

#### Will “On demand” mode miss the connectors I need?

Claude searches for the most relevant connectors based on your request, so it works well for most tasks. For connectors that need to be available every time, use “Always available” or set that connector's access individually.

#### Why does Claude sometimes add an extra message to use a connector?

In “On demand” mode, Claude searches for the right tool before using it. This search step adds one interaction, but keeps your conversation from hitting length limits when you have many tools connected.

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Getting started with Claude in Slack](https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack)
- [Troubleshoot Claude error messages](https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
- [Claude Enterprise Analytics API: Access engagement and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data)
