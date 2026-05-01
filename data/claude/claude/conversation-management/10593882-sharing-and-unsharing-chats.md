---
title: "Sharing and Unsharing Chats"
title_slug: "sharing-and-unsharing-chats"
source_url: "https://support.claude.com/en/articles/10593882-sharing-and-unsharing-chats"
last_updated_iso: "2026-03-16T21:21:48Z"
article_id: "11293454"
breadcrumbs:
  - "Claude"
  - "Conversation management"
---

# Sharing and Unsharing Chats

_Last updated: 2026-03-16T21:21:48Z_

Learn how to create shareable links to your chats with Claude. While chats are always private by default, you can easily create snapshots of your conversations to share via direct link. This guide walks you through the process of sharing and unsharing chats.

## Sharing Chats

To share a chat:

1. Click the "Share" button in the upper right corner of your chat.
2. Click the "Share" button in the pop out to create a shareable link.

Once a chat has been shared, anyone with the link can view the chat snapshot. The chat snapshot includes all messages that were sent prior to sharing the chat, including any artifacts. All messages sent after sharing a chat will remain private by default. However, if you unshare the chat and share it again, the snapshot will be updated to include any new messages.

> **Note:** Users on Team and Enterprise plans can only share chats with other members of the same organization, not publicly. Read more here: [Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing).

#### Sharing Chats with Files or MCP Integrations

When sharing chats that include uploaded files or MCP (Model Context Protocol) integrations, it's important to understand what information is included in the shared snapshot.

**Attached files:** If you share a chat that contains an attached file, the file itself is not included in the shared snapshot and remains private. Only the conversation and Claude's responses will be visible to anyone with the link.

**MCP tool calls:** When sharing chats that use MCP integrations, the raw data retrieved from MCP tool calls remains hidden in the shared snapshot. Only the final chat output and conversation will be visible to viewers. The underlying tool call data stays private.

This ensures that sensitive information from your files and connected tools is protected, even when you share a chat snapshot.

## Unsharing Chats

To unshare a chat:

1. Navigate to the "Share" menu.
2. Click the visibility dropdown.
3. Change the chat from "Public" to "Private" to disable the direct link.

## Managing Shared Chats

Users on free, Pro, or Max plans can review a log of shared chats by navigating to [Settings > Privacy](https://claude.ai/settings/data-privacy-controls). Find the **Privacy settings** section and click “Manage” next to **Shared chats:**

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1776784500&signature=1ebf7545a166815c9ee0370e566a87c4b76a189035bd305f7876a3d154026e82&req=dSklF894lIheWvMW1HO4zWn5EDUaakFuc9cNIYuX0GHQuOKCEMn5cYZW87A4%0AsITGyOIayBkNpuPOBEQ%3D%0A)

This will open a **Shared chats** modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1776784500&signature=0f5a3376f00a61696876fc6deed51708f4004b18c7841b4946753db9a9fea752&req=dSYlEst6noleWfMW1HO4ze44dyFmnBY7guvTv9woD7a%2FPCCgiW5ZPuc%2BYrWp%0AahPSGxtaOFY9tbk0M0E%3D%0A)

If you don’t have any shared chat snapshots, the **Shared chats** modal will show “No shared content found”:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1776784500&signature=517b0783640c132bab7a6a536b41b9fda542de41392408a625a069a6f2f2c023&req=dSYlEst6nolfUfMW1HO4zdaFksNziY20DeZsm0Gz1HsuFrgCj%2ByrxPVD%2FvaU%0ASzew%2BSSVQcB0l27fRoQ%3D%0A)

## Related Articles
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)
- [Publishing and sharing artifacts](https://support.claude.com/en/articles/9547008-publishing-and-sharing-artifacts)
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Custom visuals in chat](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat)
