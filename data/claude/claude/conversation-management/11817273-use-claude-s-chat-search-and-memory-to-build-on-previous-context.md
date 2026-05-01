---
title: "Use Claude’s chat search and memory to build on previous context"
title_slug: "use-claudes-chat-search-and-memory-to-build-on-previous-context"
source_url: "https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context"
last_updated_iso: "2026-03-16T21:29:12Z"
article_id: "12946743"
breadcrumbs:
  - "Claude"
  - "Conversation management"
---

# Use Claude’s chat search and memory to build on previous context

_Last updated: 2026-03-16T21:29:12Z_

You can now prompt Claude to search through your previous conversations to find and reference relevant information in new chats. Additionally, Claude can remember context from previous chats, creating continuity across your conversations. This article introduces Claude’s chat search and memory capabilities and explains how they work, what Claude can and can’t remember, and how you can toggle the features on/off.

---

## Search past chats with Claude

> Searching past chats is available to users on paid plans (Pro, Max, Team, and Enterprise plans) on the web, Claude Desktop, and Claude Mobile apps.

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

## What Claude can search

You can prompt Claude to search conversations within these boundaries:

- All chats outside of projects.
- Individual project conversations (searches are limited to within each specific project).

## Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

- "What did we discuss about [topic]?"
- "Can you find our conversation about [subject]?"
- "Let's continue where we left off with [project]."

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

## Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and find the **Preferences** section. Switch the toggle next to “Search and reference chats” off:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1776784500&signature=5e1835678c7954f43bda07755f03e57b8e9c5358e526f8902209d518e32868ac&req=dScmH859nYlXUPMW1HO4zRzXEFk3KzXHJG68qZhl7834MA6w%2FsaCH5SUqVXk%0A8%2Bc7FRqKLhgDRvUJD30%3D%0A)

## Can I exclude a specific past chat from searches?

> Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans). See **[Using incognito chats](https://support.claude.com/en/articles/12260368-using-incognito-chats)** for more information.

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1776784500&signature=e3a3b05d533804f4cb83a19f34095cda284482842966d2adbdc7d14d50d2fba1&req=dScmH859nYlWWvMW1HO4za54v6VrNIK%2BXDpzhlKsgjOq4bhqEVsMpCCVTw5t%0ATZ%2B18s6AZqqiyFXwCbg%3D%0A)

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

> **Important: **If you’re using an Enterprise or Team plan account, incognito chats are included in standard data exports and follow your organization's data retention policies.

---

## What is Claude's memory?

> Memory from chat history is available for all Claude users (free, Pro, Max, Team, and Enterprise plans) on the web, Claude Desktop, and Claude Mobile.

Claude can now generate memory based on your chat history. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

## How does Claude’s memory work?

In addition to searching past chats, enabling Claude’s memory feature adds several capabilities.

#### Memory summary

Claude will automatically summarize your conversations and create a synthesis of key insights across your chat history (not including chats in projects). This synthesis is updated every 24 hours and provides context for every new standalone conversation.

#### Project memory and summary

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

## Enable Claude’s memory

> **Note:** Members of Enterprise plans can only enable this feature individually when it’s enabled by an Owner for their organization. See [Controls for Enterprise plan Owners](#h_f7d6b307e2)** **for more information.

You can toggle Claude’s memory on by navigating to [Settings > Capabilities](http://claude.ai/settings/capabilities):

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1776784500&signature=c745fd8bdfc7a2ce5e1fc4f124696dbb4a2f04b651bfe12418ce0da28f8c3593&req=dScmH859nYlWW%2FMW1HO4zTD5P8fhf%2BBABq9N9dRTKYdyjyie9PzM9CHbm8L5%0AsYgK6EnJdT2S9uu4eH4%3D%0A)

If you want to disable Claude’s memory, click the toggle to see two options:

- **Pause memory:** Claude keeps its existing memory but won’t use memory or make new memories. Conversations with Claude while memory is paused will not be summarized into its memory should you turn the feature back on.
- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click “Reset memory,” this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

> **Important: **All memory will be retained and exportable by admins in accordance with existing enterprise chat data retention policies.

## What does Claude remember?

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

- Your role, projects, and professional context
- Communication preferences and working style
- Technical preferences and coding style
- Project details and ongoing work

## What Claude doesn't remember

#### Incognito chats

> Incognito chats are available to all Claude users (free, Pro, Max, Team, and Enterprise plans).

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

---

## Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

- Deleted conversations are removed from memory synthesis.
- Claude’s memory is updated within 24 hours when conversations are created, modified, or deleted.
- All memory data is included in data exports.
- Enterprise data retention policies apply to all memory-related data, including incognito chats.

---

## User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

#### View and manage your memory summary

See exactly what Claude remembers about you by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and clicking “View and edit memory.” The **Manage memory** modal displays everything Claude remembers about you. In addition to asking Claude to edit the existing summary, you can also tell Claude what you want it to remember. To add custom instructions to Claude’s memory, click the pencil icon in the lower left corner of the summary.

You can also update your memory summary directly from your chats. Simply tell Claude what you'd like it to remember, and it will update your memory summary without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation, so you don’t need to wait for the daily synthesis to run.

#### Past chat citations

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

#### Toggle search past chats and memory on/off

You maintain control over Claude’s ability to search past chats and use memory – you can always disable these features and enable them again when needed in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**.

#### Importing your memory from other AI tools

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

---

## Controls for Enterprise plan owners

Enterprise plan Owners and Primary Owners have specific controls for managing memory features across their organization.

#### Organization-level memory controls

The organization-wide **Generate memory from chat history** toggle is enabled by default. When enabled, individual users can manage their own memory settings. Owners can disable the memory summary feature for their entire organization by navigating to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. When disabled by an Owner, it immediately deletes all existing memory synthesis data for all users, and individual users cannot modify or access the memory synthesis setting.

> **Important:** Disabling Claude's memory at the organization level will automatically and permanently delete all memory data for all users in your organization.

#### Data handling and compliance

- **Chat summaries** are stored alongside conversation data and follow your organization's existing data retention policies. When a conversation is deleted, its summary is also deleted.
- **Memory synthesis** is stored with encryption at rest and is tied to underlying conversations. As conversations expire or are deleted according to your retention settings, the synthesis updates accordingly.
- **Incognito chats** don't contribute to memory and aren't visible in users' chat histories, but they remain available to Owners through data export features and are subject to your existing data retention policies (retained for at least 30 days for safety purposes).

#### Audit logging and data exports

- **Audit logging:** The system logs when org-level memory toggles are enabled or disabled by Owners. Standard conversation access logging applies to memory synthesis. Individual user memory edits are not logged.
- **Data exports:** Memory synthesis and chat summaries are included in standard conversation history exports. Incognito chats are included in organizational data exports. All exported chat summaries remain tied to their source conversations.

#### Team plan limitations

Team plans do not have organization-level controls for memory features. Individual Team plan members manage their own memory settings directly.

## Related Articles
- [Import and export your memory from Claude](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude)
- [Using incognito chats](https://support.claude.com/en/articles/12260368-using-incognito-chats)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
