---
title: "Use Google Workspace connectors"
title_slug: "use-google-workspace-connectors"
source_url: "https://support.claude.com/en/articles/10166901-use-google-workspace-connectors"
last_updated_iso: "2026-04-15T01:59:27Z"
article_id: "10707090"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Use Google Workspace connectors

_Last updated: 2026-04-15T01:59:27Z_

Connect your Gmail, Google Calendar, and Google Drive to Claude so you can search emails, manage your calendar, work with documents, and save files—all without leaving the conversation.

> Google Workspace connectors (Gmail, Google Calendar, and Google Drive) are available for all users on Claude and Claude Desktop.

For Team and Enterprise plans, an Owner or Primary Owner must enable these connectors at the organization level before individual users can authenticate. For setup instructions, read **[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities#h_17dd443beb)**.

What you can do

## Gmail

- **Search and read emails** using natural language queries
- **Draft emails** with proper formatting and context — Claude creates drafts in your Gmail account, but cannot send emails on your behalf
- **Access email metadata**, including attachment metadata (not attachment content)
- **Manage email organization** with labels and threads
- **List saved drafts** in your Gmail account

## Google Calendar

- **View events and calendars**, including shared calendars you have access to
- **Create, update, and delete events** with full customization
- **Find mutual availability** across attendees
- **Manage attendee lists** and respond to invitations (accept, decline, or tentative)
- **Set up recurring meetings**

## Google Drive

- **Search and retrieve Google Docs** from your Drive
- **Add Google Docs directly to chats and projects** by pasting URLs or selecting from recent documents
- **View file permissions** and **list recent changes** to your Drive
- **Save Claude-generated files** directly to your Drive (requires **[code execution and file creation](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)** to be enabled)

> **Note:** Claude extracts text content only from Google Drive files. Images embedded in documents are not processed.

---

How to use the connectors

Ask Claude a question that requires access to your Gmail, Calendar, or Drive. Claude automatically detects which tools it needs and uses them to respond. Each action Claude takes on your behalf requires your explicit approval.

Claude's response includes citations indicating which emails, calendar events, or documents were used as sources, with links to the originals when available. You can ask follow-up questions to dig deeper into any source.

## Add Google Drive files to chats

1. Click the plus sign in the chat interface.
2. Select "Add from Google Drive."
3. Search through your recently accessed documents or paste the document's URL.
4. When you send your message, Claude accesses and processes the document to inform its response.

You can add multiple files to a single chat to give Claude comprehensive context. The files must fit within the conversation's context window.

## Add Google Drive files to projects

The Google Drive connector is only available when adding to **Files** in private projects. This option will be disabled for shared projects.

1. Open your project and find the **Files** section.
2. Click the "+" button to add files.
3. Select "Drive."
4. Search through your recently accessed documents or paste the document's URL.
5. Your document is added to your project knowledge for Claude to access when chatting in that project.

Google Docs added to chats and projects sync directly from Google Drive, so you're always working with the latest version.

## Managing individual connectors

You can enable or disable specific connectors from below the chat interface:

1. Click the plus sign in the chat interface.
2. Hover over "Connectors."
3. Toggle individual connectors on or off.

---

Google Drive Cataloging (Enterprise)

> Google Drive Cataloging is only available for Enterprise plans.

Enterprise users can enable Google Drive Cataloging to index their Drive content with RAG (Retrieval Augmented Generation). When enabled, Claude indexes your Google Drive documents to provide more accurate, contextual responses with direct citations to relevant sources — and reduces token usage by pulling only relevant content into your context.

If cataloging is turned off, Claude uses the Google APIs to search through your Drive data directly.

## Supported file types for cataloging

Google Docs (text extraction only, up to 10MB).

## Enable Google Drive Cataloging

**For admins:**

1. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.
2. Locate **Google Drive cataloging** under **Data sources**.
3. Toggle this on and follow the instructions to authenticate.

**For individual users** (after an admin enables the feature):

1. Click the plus sign in the chat interface.
2. Toggle **Drive search** on.

If this is your first time using this feature, you'll be redirected to Google to authenticate.

## How cataloging works

Once enabled, Claude indexes your Google Docs and uses that index during conversations to provide relevant context and citations. Claude periodically re-indexes documents that have changed and de-indexes documents that have been deleted. It may take several hours for Claude to recognize updates or deletions.

## Cataloging data retention

- Indexed data for a deleted file is removed within one hour of the file being deleted.
- When an admin turns off cataloging, all indexed data for the organization is deleted within six hours.

---

Privacy and data handling

- You must authenticate directly with your Google account before using these connectors.
- On Team and Enterprise plans, an Owner or Primary Owner must enable connectors at the account level before individual users can authenticate.
- Claude can only access the Gmail, Calendar, and Drive data for the Google account you've connected.
- Claude only accesses your data when you explicitly ask a question or request an action requiring this information, and retrieves the minimum information needed.
- Claude mirrors your existing permissions — you cannot access information you don't already have access to in Google Workspace.
- Data retrieved while using connectors is stored on Anthropic servers, protected by Anthropic's security infrastructure (see our **[Trust Center](https://trust.anthropic.com/controls#organizational-security)** for details). This data is retained with its associated chat, so you can delete any retrieved data by deleting the chat.
- We do not train our models on your Gmail or Calendar connector data, ensuring your private information remains private.
  - **Note**: If you are using our consumer products (e.g. Claude Free, Pro, and Max ( when using Claude Code with those accounts) and you have chosen to allow us to use your chats and coding sessions for model training, then any content you copy/paste from your Gmail or Calendar or Claude's responses which include specific information from these connectors may be used to improve our models. For more information, refer to **[Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)**
- Each user's Google Drive Cataloging index is private — no other users can access it, even within the same organization. Each index is unique to a user/organization pair, and fully respects your underlying access controls and permissions.
- Data is encrypted at rest and in transit.

## A note on Gmail permissions

During authentication, Google's OAuth screen mentions email sending permissions. Claude only reads emails and creates drafts with your explicit approval. The send function is not enabled — all emails must be sent manually through your Gmail account.

---

Current limitations

- Attachment content is not directly accessible through Gmail (metadata only).
- Claude cannot see images embedded in documents, emails, or presentations.
- Some advanced Gmail filters may not be supported.
- Complex queries may require multiple API calls.
- Rate limits apply per Google's API quotas.
- Performance may vary for large mailboxes.

---

Troubleshooting

## Reconnecting your Google account

If you see the error "*Please try again. You may need to reconnect with your Google Drive account," *follow these steps:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.
2. Find your Google connector and click on it to view the details.
3. Click the "Disconnect" button.
4. Click "Disconnect" in the confirmation message.
5. The next time you use a Google Workspace feature in your chat, you'll be redirected to Google to re-authenticate.

If you're still having trouble, disconnect from your Google account settings at[ **myaccount.google.com/connections**](https://myaccount.google.com/connections). Search for the Claude connection, click into the settings, and choose "Delete all connections."

## Google Workspace admin configuration

If your organization uses Google Workspace and the connectors aren't working (you may see the message *"Access blocked: your institution's admin needs to review Claude for Google Drive"*), your Google Workspace admin may need to allow Claude as a trusted application:

1. Go to **[admin.google.com](https://admin.google.com)**
2. Navigate to **Security > Access and data control > API controls > Manage third-party app access**.
3. Click "Add app," then select "OAuth App Name."
4. Search for "Claude" and set it as "Trusted."
5. Wait approximately 15 minutes for Google's policy to propagate, then try connecting again.

---

Frequently asked questions

## What happens if I update a Google Doc after adding it to a chat?

The document continues to sync with the most up-to-date version in Google Drive.

## Can I add multiple files to a single chat?

Yes. You can add multiple Google Drive files to provide Claude with comprehensive context. The documents must fit within the conversation's context window.

## What happens if I lose access to a document?

You won't be able to view its contents in conversations where it was previously added. The document preview is removed, but the conversation history is maintained.

## Does Claude have access to images, comments, or suggestions in Google Docs?

No. Claude extracts the main text content only and cannot see images, comments, or suggestions.

## Can Claude send emails on my behalf?

No. Claude can create email drafts, but all emails must be sent manually through your Gmail account.

## Can I opt out of using these connectors?

On Team and Enterprise plans, Owners and Primary Owners can disable Google Workspace connectors for their organization in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. Individual users can also disable specific tools from the chat interface.

## Who has access to my Google Drive Cataloging index?

Only you. Your index includes only documents you have access to, and no one else can access it—even members of the same organization. If you disconnect your Google account from Claude, your index is deleted.

Browse all available connectors in the [Connectors Directory](https://claude.ai/directory).

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack)
- [Enable and use the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector)
- [Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
