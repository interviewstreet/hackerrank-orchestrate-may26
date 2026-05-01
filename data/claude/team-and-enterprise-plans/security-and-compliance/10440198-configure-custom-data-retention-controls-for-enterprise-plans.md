---
title: "Configure custom data retention controls for Enterprise plans"
title_slug: "configure-custom-data-retention-controls-for-enterprise-plans"
source_url: "https://support.claude.com/en/articles/10440198-configure-custom-data-retention-controls-for-enterprise-plans"
last_updated_iso: "2026-03-16T20:33:05Z"
article_id: "11075786"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Security and compliance"
---

# Configure custom data retention controls for Enterprise plans

_Last updated: 2026-03-16T20:33:05Z_

> This feature is available to Enterprise plan customers. To set custom retention periods for your organization, you must have either a Primary Owner or Owner role.

*This article is about our commercial products such as Claude for Work and the Anthropic API. For our consumer products such as Claude Free, Pro, Max and when accounts from those plans use Claude Code, see **[here](https://privacy.claude.com/en/collections/10663362-consumers)**. *

Custom data retention controls allow organizations to manage how long Claude stores conversation and project data. This article explains how to set up and manage data retention periods for your organization.

## How data retention works

Data retention is based on the last observed activity:

- **For chats:** Retention period starts from the time of the last message in the conversation.
- **For projects:** Retention period starts from the time the project was last updated (this includes chat creation or project knowledge base modifications).
  - Note that your custom data retention periods set for projects will supersede your custom retention periods for any chats.

The minimum retention period is 30 days, and each month is counted as 30 days. For example, a three-month retention period equals 90 days.

## What gets deleted

When data reaches the end of its retention period:

- **For chats:** All chats (including chats within projects) and any artifacts within those chats will be deleted.
- **For projects:** All projects will be deleted, including any chats and artifacts within those projects.

## Important considerations

- Deletion occurs at midnight UTC on the scheduled day.
- By default, data is retained indefinitely unless a custom retention period is set.
- When you modify retention settings, any data that falls outside the new retention period will be deleted immediately upon saving.
- Data past its retention period will be permanently deleted and cannot be recovered.

## Setting up data retention

## To set custom retention periods:

1. Log in to your Owner Enterprise plan account.
2. Navigate to **[Organization settings > Data and Privacy](https://claude.ai/admin-settings/data-privacy-controls)**.
3. Set your desired retention period (minimum 30 days).
4. Save your changes.

## Example retention calculation

If a conversation’s last message is at 3PM UTC on March 1 with a 30-day retention period, the deletion will occur at midnight UTC on March 31.

## Monitoring retention-related activities

All retention-related actions and changes are automatically tracked in **[audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)**. You can access these logs to monitor changes to retention settings and data deletion events.

## Related Articles
- [Can you delete data that I sent via Team and Enterprise plans?](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans)
- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- [Using incognito chats](https://support.claude.com/en/articles/12260368-using-incognito-chats)
- [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
- [Claude Enterprise Analytics API: Access engagement and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data)
