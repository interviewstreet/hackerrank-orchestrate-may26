---
title: "Troubleshoot Claude error messages"
title_slug: "troubleshoot-claude-error-messages"
source_url: "https://support.claude.com/en/articles/12466728-troubleshoot-claude-error-messages"
last_updated_iso: "2026-03-16T20:32:12Z"
article_id: "13898432"
breadcrumbs:
  - "Claude"
  - "Troubleshooting"
---

# Troubleshoot Claude error messages

_Last updated: 2026-03-16T20:32:12Z_

This article explains common error messages and warnings you may encounter when using Claude and provides guidance on how to address them.

## Usage limit warnings and errors

Usage limit warnings appear when you're approaching your plan’s limit within a five-hour session: *“Approaching 5-hour limit.”*

If you hit your plan’s limit after the warning appears, you’ll see a blocking error message letting you know when you can use Claude again: *“5-hour limit reached - resets [time].”*

Looking for ways to maximize your Claude usage? Refer to **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)**.

#### Extra usage

Paid Claude users with extra usage enabled in Usage settings will see a slightly different usage limit error:* “5-hour limit resets [time] - continuing with extra usage.”* Note that this will only appear for members with access to extra usage.

Refer to these articles for more information about this feature depending on your plan:

- **[Extra usage for paid Claude Plans](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans)**
- **[Extra usage for Team and Enterprise plans](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-enterprise-plans)**

## Length limit errors

You may encounter a length limit error when your message to Claude exceeds the maximum input length allowed: "Your message will exceed the length limit for this chat. Try attaching fewer or smaller files or starting a new conversation." This error indicates that your message is too long and needs to be shortened before sending it to Claude.

For users on paid plans with code execution enabled, Claude automatically manages long conversations by summarizing earlier messages when context limits are approached. This means most users will rarely encounter length limit errors during normal use. Your full chat history is preserved so Claude can reference it even after summarization. In rare cases where you still encounter this error (such as when sending a very large first message), you can:

- Break your content into smaller chunks and process them separately
- Summarize or extract key sections before sending to Claude
- Use Claude to first identify the most relevant portions of your content
- Start a new conversation

## Login errors

If you see a generic error message when attempting to log in to your Claude account (e.g, "There was an error logging you in"), try the following troubleshooting steps:

- Ensure you’re not using a VPN when accessing Claude.
- Disable any browser extensions that you currently have active.
- Clear your browser’s cache and cookies.

If you're still seeing an error, check **[our status page](http://status.claude.com)** for active incidents.

## Capacity constraints

Capacity issues occur when Claude’s infrastructure experiences high demand system-wide. When capacity is constrained, you may see this message when chatting with Claude: *"Due to unexpected capacity constraints, Claude is unable to respond to your message. Please try again soon."*

> **Important:** Capacity constraints are not outages. The system is functioning normally but managing high demand across all users. These issues are temporary and typically resolve as demand patterns shift throughout the day. If you encounter this message, try again in a few minutes.

Capacity issues will not appear on our status page because they represent normal load management rather than technical problems.

## Service incidents and outages

Service incidents are disruptions where Claude is unavailable or significantly degraded for all or most users. These represent actual technical problems with our systems. To check for confirmed incidents, visit status.claude.com, where you'll find real-time updates on scope, impact, and resolution progress for any active incidents.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1753796247/e6a8c6ef8653b229c5758e881242/c2fc6fc0-d163-4119-93e0-394104d86bc9?expires=1776784500&signature=afbc53bfcae14e864c631c45fdc6995b563a2bf827c21269d1b3404f6b4aec0f&req=dSciFc53m4NbXvMW1HO4za4BUakk2rbB7y68oYp%2BYg%2FiwPbXbx7xAcXI97AM%0AoxD5weTxF51K1eC%2F2sA%3D%0A)

## Related Articles
- [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [Manage extra usage for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-extra-usage-for-paid-claude-plans)
- [Claude Design subscription usage and pricing](https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing)
