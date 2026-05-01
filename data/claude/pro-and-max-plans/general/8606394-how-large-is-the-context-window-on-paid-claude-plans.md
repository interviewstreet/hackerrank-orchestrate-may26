---
title: "How large is the context window on paid Claude plans?"
title_slug: "how-large-is-the-context-window-on-paid-claude-plans"
source_url: "https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans"
last_updated_iso: "2026-04-16T13:28:07Z"
article_id: "8670598"
breadcrumbs:
  - "Pro and Max plans"
  - "General"
---

# How large is the context window on paid Claude plans?

_Last updated: 2026-04-16T13:28:07Z_

Claude’s context window size is 200K, meaning it can ingest 200K+ tokens (about 500 pages of text or more) when using a paid Claude plan.

When using Claude Code with a Pro, Max, Team, or Enterprise plan, Opus 4.7 supports a 1M token context window. Pro users need to enable extra usage to access Opus 4.7 in Claude Code. Sonnet 4.6 also supports a 1M context window for all paid Claude plans on Claude Code, but extra usage must be enabled to access it (except for usage-based Enterprise plans).

> **Note: **Users on Enterprise plans have access to a 500K context window when using specific models. See **[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)** for more information.

## Automatic context management

For users on paid plans with code execution enabled, Claude automatically manages your conversation context. When your conversation approaches the context window limit, Claude summarizes earlier messages to make room for new content. This does not count towards your usage limit, and allows conversations to continue indefinitely in most cases.

Your full chat history is preserved so Claude can reference it, even after earlier portions have been summarized. You may occasionally notice Claude "organizing its thoughts" during long conversations—this is the automatic context management at work.

> **Note:** Code execution must be enabled for automatic context management to work. In rare edge cases (such as very large first messages or system errors), you may still encounter context window limits.

## Maximizing your context window

While context is managed automatically for most conversations, you can still optimize how you use your available context space:

- **Utilize projects effectively:** Projects use retrieval-augmented generation (RAG), which allows Claude to work with larger amounts of information by only loading relevant content into the context window.
- **Keep project instructions concise:** Claude performs best when you use project instructions for general context around your project, key guidelines, and Claude's role.
- **Manage tools and connectors:** These features are token-intensive, so being mindful of how many you have active helps maximize your available context.

## Related Articles
- [How large is the Claude API’s context window?](https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window)
- [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
