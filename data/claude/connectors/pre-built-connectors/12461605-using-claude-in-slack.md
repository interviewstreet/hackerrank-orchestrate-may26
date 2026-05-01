---
title: "Using Claude in Slack"
title_slug: "using-claude-in-slack"
source_url: "https://support.claude.com/en/articles/12461605-using-claude-in-slack"
last_updated_iso: "2026-03-16T21:03:21Z"
article_id: "13892183"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Using Claude in Slack

_Last updated: 2026-03-16T21:03:21Z_

Claude in Slack gives you AI assistance right where your team collaborates. This article covers how to interact with Claude in Slack, which features are available, and tips for getting the most out of the integration.

## Send a direct message to Claude

1. Search for "@Claude" anywhere in Slack.
2. Click on Claude, then the "Chat" tab at the top to open a direct message.
3. You'll see a welcome message with suggested prompts.
4. Type your question or request and press Enter.

## Use the AI assistant panel

1. Click the Claude icon in the AI assistant header (if available in your workspace).
2. The Claude panel will open on the right side of your Slack window.
3. Type your message and press Enter.
4. Claude will respond in the panel.
5. When you close the AI assistant panel, the conversation moves to your history.
6. Access previous conversations by clicking the clock icon.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1755150661/a1a13c73bda421f6ee906650cfc9/22907223-e523-4a93-a6d2-3199a8368991?expires=1776784500&signature=3bf42d8fc4982bb1412d944aef0058357b77b87dbf36be8c9321c4c01d05cbfe&req=dSciE8h7nYdZWPMW1HO4zXK25RdJ4DUbVfOC%2FRy97LVgJNY%2Fw%2F%2FBXLFM5SCj%0AGSoGEgj1wLNuTsqYfh4%3D%0A)

## Mention @Claude in a thread or channel

1. Mention @Claude in any thread or channel where you want Claude's help.
2. Claude will draft a response based on the recent conversation context.
3. You'll see the draft privately first.
4. Review, edit, or regenerate the response before deciding to share it.
5. Click "Post to thread" to share Claude's response with your team.

This gives you control to review what Claude shares before it becomes visible to others.

#### What context from the thread or channel is included when using @Claude?

When mentioned in a channel, Claude will have access to the last 20 messages in that channel, including any files shared within those messages. When using @Claude in a thread, it will have access to the last 50 messages in that thread.

## Forward a thread directly to Claude

You can also select “Forward message…” on a message within any Slack thread to send it directly to Claude. When shared in this way, Claude will have access to the last 100 messages in the thread.

## Route coding tasks to Claude Code (beta)

> **Note:** This feature is currently available in beta as a research preview for Team and Enterprise plan users who have access to Claude Code on the web.

You can delegate coding tasks to Claude Code directly from Slack. When you mention @Claude for a coding-related request, Claude automatically detects the coding intent and spins up a Claude Code session on the web using context from your Slack conversation.

#### How it works

1. Mention @Claude in a channel or thread with a coding task.
2. Claude reviews your message to determine if it's a coding request.
3. If it is, Claude gathers context from recent messages and creates a new Claude Code session.
4. Claude posts status updates back to your Slack thread as the session progresses.
5. Once complete, Claude provides a link to the full session where you can review changes and open a pull request.

You can also manually tell Claude to handle a request as a coding task if it isn't automatically detected.

#### Use cases for Claude Code in Slack

- **Bug investigation and fixes**: Ask Claude to investigate and fix bugs as soon as they're reported in Slack.
- **Quick code reviews and modifications**: Have Claude implement small features or refactor code based on team feedback.
- **Collaborative debugging**: When team discussion provides crucial context—like error reproductions or user reports—Claude uses that information to inform its debugging approach.

#### Requirements

To use Claude Code in Slack:

- The Claude app must be installed in your Slack workspace via the [Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4).
- A Claude Owner or Primary Owner must enable Claude Code on the web by navigating to [Admin settings > Claude Code](http://claude.ai/admin-settings/claude-code).
- You must have access to Claude Code on the web.

Claude automatically chooses which repository to run the task on based on the repositories you've authenticated to Claude Code on the web.

---

## Features and capabilities

#### Available features

Claude in Slack supports many of the capabilities offered by the Claude web app, including:

- **Web search**: Get up-to-date information from the internet.
- **Integrations**: Access connected services like Google Docs, Gmail, and Google Calendar.
- **File uploads**: Attach files directly in your Slack conversation for Claude to analyze.
- **Document analysis**: Upload PDFs, text files, images, and more.

#### How integrations work

If you've connected integrations in Claude (like Google Workspace), they work in Slack too:

1. Share a Google Doc link in your message to Claude.
2. Claude will automatically access and analyze the document based on your permissions.
3. You can reference emails from Gmail or events from Google Calendar the same way.

You cannot manage or connect new integrations from within Slack—set these up in your Claude settings first.

#### Feature limitations

The following features are not available when using Claude in Slack:

- Research
- Extended thinking
- Creating new integration connections (you can only use integrations you’ve already connected in your Claude settings)

---

## Using integrations across multiple Slack workspaces

If you use Claude across more than one Slack workspace, it's important to understand that your integrations (like the Slack connector) are tied to your **Claude account**, not to a specific Slack workspace.  
  
**To avoid unexpected results:**

- Disconnect the Slack connector from your Claude account before using Claude in a different workspace (**Settings > Connectors > Slack > Disconnect**), then reconnect it when needed.
- If you regularly use Claude in simultaneous workspaces, consider using separate Claude accounts, each configured for its respective workspace.

---

## Common use cases

#### Code assistance

Share code snippets with Claude to get implementation suggestions, or help debugging errors, optimizing functions, and understanding legacy code. For more complex coding tasks, Claude can automatically route your request to Claude Code on the web (see **[Route coding tasks to Claude Code](#h_adda66b697)**).

#### Content creation

Transform team discussions into formalized documentation, draft emails and proposals in your direct message with Claude, then share the results in relevant Slack channels.

#### Document analysis

Upload files directly to Claude for data analysis, key point extraction/summarization, and translation. Supported file types include: PDF, TXT, DOC, DOCX, images (PNG, JPG), CSV, and more. For more information, see **[Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)**.

#### Meeting preparation

Before joining a call, ask Claude to summarize key topics from shared documents, analyze relevant files, review meeting agendas, and prepare talking points.

#### Onboarding support

Granting new team members access to channel history and shared documents in Slack helps them ramp up faster.

#### Quick research

Get instant answers during team discussions. Ask Claude about industry trends, technical concepts, or company information while staying in your conversation.

---

## Best practices

#### Optimize your workflow

- **Keep Claude DMs organized**: Use them for draft work before sharing in channels.
- **Leverage context**: Claude maintains conversation context within each session.
- **Use clear prompts**: Be specific about what you need to get the best results.
- **Request web search**: Add "search the web" to your prompt when you need current information.

#### Managing conversations

- Each Claude DM maintains full chat history.
- In the AI assistant panel, conversations move to history when you close the panel.
- Start fresh conversations when switching topics for better results.

#### File handling

- Upload files directly in your Slack message to Claude.
- Claude processes files using the same system as the Claude web app.
- You can upload multiple files in a single message.

## Message editing and deletion

- **Editing messages**: Claude won't see edits to previous messages.
- **Deleting messages**: Deleted messages remain in Claude's context but are removed from the Slack interface.
- **Threading**: Threading is disabled in Claude DMs to maintain conversation flow.

## Channel restrictions

Claude works in direct messages and threads where you explicitly mention @Claude. You control when Claude participates in conversations and can review all responses before sharing them with your team.

---

## Troubleshooting

#### "Usage limit reached"

This message appears when you've hit your Claude account usage limits. Try again later or consider **[upgrading your Claude plan](https://claude.ai/upgrade)**.

#### "I'm unable to generate a response at this time"

This generic error message can appear for various reasons:

- API failures or temporary service issues
- Empty responses from Claude
- Network connectivity problems

Try sending your message again. If the problem persists, you can **[contact our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)**.

#### "I don't have access to our previous conversation history"

This message appears when you try to continue a conversation in Slack that has already been deleted from Claude. This can happen if:

- You disconnected your Claude in Slack app.
- Your organization’s retention policy deleted the conversation.
- You manually deleted the conversation from the Claude web app.

Start a new conversation to continue.

## Related Articles
- [Getting started with Claude in Slack](https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack)
- [Using Claude in Xcode](https://support.claude.com/en/articles/12293051-using-claude-in-xcode)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Claude Code champion kit](https://support.claude.com/en/articles/14555399-claude-code-champion-kit)
