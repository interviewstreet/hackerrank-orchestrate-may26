---
title: "Enable and use the Microsoft 365 connector"
title_slug: "enable-and-use-the-microsoft-365-connector"
source_url: "https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector"
last_updated_iso: "2026-04-03T16:16:48Z"
article_id: "14016505"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Enable and use the Microsoft 365 connector

_Last updated: 2026-04-03T16:16:48Z_

This article explains how to connect Claude to Microsoft 365 using our pre-built MCP connector, allowing Claude to search, analyze, and access information across SharePoint, OneDrive, Outlook, and Teams.

> The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

With Microsoft 365 connected, Claude can:

- **Search and analyze documents** across SharePoint sites and OneDrive libraries
- **Access email threads** and analyze communications from Outlook
- **Review meeting information** from Teams Calendar
- **Pull insights** from Teams Chat discussions

> **Important:** The Microsoft 365 connector requires a Microsoft Entra tenant tied to a Microsoft Business plan. Personal Microsoft accounts (such as @outlook.com or @hotmail.com addresses) can't be used to connect. If you're unsure whether you have an Entra tenant, check with your IT administrator.

---

## Enable the Microsoft 365 connector

The Microsoft 365 connector requires a **work Microsoft 365 account** tied to a Microsoft Entra tenant (any Microsoft Business plan). Personal Microsoft accounts—such as @outlook.com, @hotmail.com, or @live.com addresses—can't be used with this connector. If you're not sure whether your account is tied to an Entra tenant, check with your IT administrator.

Before anyone in a Microsoft Entra tenant can use the connector, a Microsoft Entra Global Administrator must complete a one-time consent process to authorize the integration.

#### Before you connect

**For Team and Enterprise plans only:** An organization Owner must first enable the connector for the organization before any team members can connect.

1. Sign in to Claude.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Click the "Add" button at the top of the page.
4. Find "Microsoft 365" and click "Add to your team."

This step isn't required on Free, Pro, or Max plans.

#### Microsoft Entra Global Administrator consent

A Microsoft Entra Global Administrator in your tenant must authorize the connector before anyone else can connect. If you're the Global Administrator, you can do this yourself during the connection steps below. If you're not, ask your Global Administrator to either:

- Connect to Microsoft 365 in their own Claude account first (following the steps below), or
- Complete the manual setup described in "Manual setup in Microsoft Entra ID" below.

#### Connecting to Microsoft 365

Once a Global Administrator has granted consent (or if you're the Global Administrator and will be granting consent during this process):

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.
2. Find "Microsoft 365" in the list and click "Connect."
3. Authenticate with your Microsoft 365 credentials.
4. If you're the Global Administrator and this is the first time the connector is being authorized for your tenant, review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

After the Global Administrator has granted consent, other people in the same Entra tenant can connect by repeating steps 1–3 above. They won't see the consent prompt — they'll just authenticate and start using the connector.

> **Note:** Once you've connected Microsoft 365 to your Claude account, you can also use it on Claude for iOS or Android.

#### Restricting access (optional)

**Restrict which people can use the connector:** Navigate to the M365 MCP Server for Claude enterprise application in the Entra admin center (**[https://entra.microsoft.com](https://entra.microsoft.com)**), go to Properties and set "Assignment required?" to Yes, then add the specific users or groups under the Users and groups section—only those assigned will be able to authenticate and use the connector. Repeat this same process for the M365 MCP Client for Claude enterprise application to ensure both components are restricted to the same set of authorized people.

**Restrict which permissions the connector can use:** See the "Permission categories" and "Selectively revoking permissions" sections below.

#### Manual setup in Microsoft Entra ID

If your Microsoft Entra Global Administrator doesn't have a Claude account, or if you need to troubleshoot the app install and permissions setup, you can add the connector apps and grant admin consent directly in Microsoft Entra ID.

This process adds two service principals to your tenant. Each principal establishes a service-level identity for one of the two M365 MCP for Claude app registrations, allowing them to access and interact with your organization's data and resources via the Microsoft Graph API.

**1) Add the service principals**

Using **[Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)**, add both required service principals:

M365 MCP Client for Claude

POST [https://graph.microsoft.com/v1.0/servicePrincipals](https://graph.microsoft.com/v1.0/servicePrincipals)

{"appId":"08ad6f98-a4f8-4635-bb8d-f1a3044760f0"}

M365 MCP Server for Claude

POST [https://graph.microsoft.com/v1.0/servicePrincipals](https://graph.microsoft.com/v1.0/servicePrincipals)

{"appId":"07c030f6-5743-41b7-ba00-0a6e85f37c17"}

**2) Grant admin consent**

Construct and visit the following URLs in your browser, replacing {your-tenant-id} with your organization's tenant ID:

M365 MCP Client for Claude

`[https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0](https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0)`

M365 MCP Server for Claude

`[https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17](https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17)`

When you visit each URL, you'll be prompted to consent to the delegated permissions required by the integration on behalf of your organization.

**3) Complete setup in Claude**

After the Microsoft Entra admin completes the consent process:

- **For Team and Enterprise plans:** An organization Owner needs to enable the connector in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**, then members can connect individually through **Customize > Connectors**.
- **For Free, Pro, and Max plans:** Navigate to **Customize > Connectors**, find "Microsoft 365," and click "Connect."

---

## How to use the Microsoft 365 connector

Ask Claude a question that requires accessing your Microsoft 365 data. Claude will automatically detect which tools it needs and retrieve the relevant information.

#### Example queries

- "Find the Q4 strategic planning document in SharePoint."
- "Summarize email conversations about the product launch."
- "What discussions happened in the Teams channel about the marketing campaign?"
- "Review meeting notes from last week's leadership sync."

Claude will provide a response based on information retrieved from your Microsoft 365 environment, including relevant context and citations when applicable.

## SharePoint and OneDrive document access

- Search documents across SharePoint sites and libraries to locate project specifications, strategic plans, and other business documents.
- Access files stored in your OneDrive and have Claude analyze content without manually uploading.
- Consolidate information from distributed file locations and analyze trends across multiple documents.

## Outlook email analysis

- Search email threads and conversations to track project status, client feedback, and team alignment.
- Access message content and metadata, filtering by date, sender, subject, and other criteria.
- Analyze communication patterns and find specific information from past correspondences.

## Outlook Calendar meeting analysis and summarization

- Review meeting summaries, attendee information, and content to prepare for upcoming meetings or understand discussions you missed.
- Analyze scheduling patterns and track project decisions.

## Teams chat capabilities

- Access Teams chat messages and channel discussions where you're a participant.
- Review team collaboration patterns and find decisions made across conversations.  
  ​

---

## Which permissions does the Microsoft 365 Connector require?

When you connect the Microsoft 365 integration, you'll be asked to grant several permissions that allow Claude to access your Microsoft 365 data on your behalf.

**Important to understand:**

- All permissions are **delegated permissions**, which means Claude acts on behalf of your Microsoft 365 account and can only access data you already have permission to view in Microsoft 365.
- Claude can only access Microsoft 365 data for the account you've connected.
- Claude can’t access anything beyond your existing permissions.
- These permissions enable read-only access—Claude can’t modify, delete, or create content in your Microsoft 365 tenant.

## Permission categories

During authentication, the Microsoft 365 connector requests the following permissions:

**Basic access**

- **User.Read**: Sign in and read your user profile
- **openid: Sign in with your organizational account**
- **offline_access: Maintain access to data you have given it access to**
- **email: View your email address**
- **profile: View your basic profile information**

**Email (Outlook)**

- **Mail.Read**: Read your email messages
- **Mail.ReadBasic**: Read email metadata (sender, subject, date)
- **Mail.Read.Shared**: Read emails in mailboxes you have access to
- **MailboxFolder.Read**: Read your mailbox folder structure
- **MailboxItem.Read**: Read items in your mailbox

**Calendar**

- **Calendars.Read**: Read your calendar events
- **Calendars.Read.Shared**: Read calendars shared with you

**Teams Chat**

- **Chat.Read**: Read your Teams chat messages
- **Chat.ReadBasic**: Read Teams chat metadata
- **ChatMember.Read**: Read information about chat participants
- **ChatMessage.Read**: Read your Teams chat messages

**Teams Channels**

- **Channel.ReadBasic.All**: Read channel names and descriptions
- **ChannelMessage.Read.All**: Read channel messages

**Meetings**

- **OnlineMeetings.Read**: Read your online meetings
- **OnlineMeetingTranscript.Read.All**: Read meeting transcripts
- **OnlineMeetingAiInsight.Read**: Read AI-generated meeting insights
- **OnlineMeetingArtifact.Read.All**: Read meeting recordings and artifacts
- **OnlineMeetingRecording.Read.All**: Read meeting recordings

**Files (OneDrive and SharePoint)**

- **Files.Read**: Read your files
- **Files.Read.All**: Read all files you can access
- **Sites.Read.All**: Read items in SharePoint sites

**User Directory**

- **User.ReadBasic.All**: Read basic profile information for all users in your organization (used for finding meeting availability)

## Why are these permissions needed?

These permissions allow Claude to do the following when prompted:

- Search your emails, documents, and calendar to answer your questions.
- Access meeting information and Teams discussions.
- Find and analyze content across your Microsoft 365 environment.
- Provide accurate, contextual responses based on your work data.

Additionally, the Microsoft 365 Connector searches SharePoint across the entire tenant using the permissions of the user. Site-specific search restriction is unsupported.

You can revoke these permissions at any time by disconnecting the connector in **[Customize > Connectors](https://claude.ai/customize/connectors)**. Team and Enterprise plan Owners can also remove the connector for their organization in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

## Selectively revoking permissions

To limit which types of resources the connector can access, you can selectively revoke permissions from the default set of authorized scopes. This requires Microsoft Entra admin access.

1. As a Microsoft Entra Admin, go to: entra.admin.com
2. Select “Enterprise Applications.”
3. Next to the search box, remove the application type filter.
4. Search for and click "M365 MCP Server for Claude."
5. Go to Permissions.
6. Under the Admin consent tab and in the Microsoft Graph list of permissions, select the permission you would like to revoke and click the breadcrumbs button (“...”).
7. Select “Revoke permission,” and confirm with the “Yes, revoke” button.
8. Claude will now be unable to access resources via that API. Attempts to access a resource with a revoked permission will show a "Failed to call tool <name of tool>".
9. As a convenience, users can also individually toggle off which tools the connector will use in the Microsoft 365 connector settings to prevent Claude from trying to access a tool for which the permission is revoked.

To restore a revoked permission, follow the steps to grant admin consent described in the manual setup section above. This will revert the permissions to the default state.

## Privacy and security

- **Permission inheritance:** Claude mirrors your existing Microsoft 365 permissions.
- **On-demand access:** Claude only accesses your data when you explicitly ask questions requiring it.
- **Revocable access:** You can disconnect the integration at any time through **[Settings > Connectors](https://claude.ai/settings/integrations)**.

Read more here: **[Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)**.  
​

---

## Troubleshooting

#### Authentication is failing. What should I check?

1. **Verify your credentials:** Ensure you're using the correct Microsoft 365 account. Personal Microsoft accounts (like @outlook.com) aren't supported—you need an account tied to a Microsoft Entra tenant.
2. **Check subscription status:** Confirm your Microsoft 365 license is active.
3. **Check admin consent:** If you aren't a Microsoft Entra Global Administrator, confirm that your admin has granted tenant-wide consent for the connector. Without this, you'll receive an error during authentication.
4. **Review organizational policies:** Your IT team may need to approve third-party app access.
5. **Try a different browser:** Some browsers may block authentication popups.
6. **Disable browser extensions:** Ad blockers or privacy extensions may interfere.
7. **Clear cookies and cache:** Try a fresh browser session.

#### Claude says it can't find documents I know exist

Check the following:

1. **Permissions:** Verify you have access to the document in Microsoft 365 directly.
2. **Location:** Ensure the document is in SharePoint or OneDrive, not local storage.
3. **Indexing delay:** Recently uploaded documents may take time to become searchable.
4. **Specific location:** Try specifying the exact SharePoint site or library name.
5. **File name:** Try searching by exact file name or unique keywords from the document.

#### Search results are incomplete or irrelevant

Tips to improve your search queries:

- Be more specific about what you're looking for.
- Specify locations (site names, date ranges, document types).
- Use exact phrases for better matching.
- Try breaking up complex queries into simpler, more focused questions.
- Verify spelling of names, projects, or terms.  
  ​

---

## Frequently asked questions

#### Can Claude modify my Microsoft 365 data?

No. The current Microsoft 365 integration provides **read-only access**. Claude can search and analyze your data but cannot:

- Create, edit, or delete documents
- Send emails or calendar invites
- Modify SharePoint sites or OneDrive files
- Change Teams settings or permissions

#### Can I use the Microsoft 365 Connector with Enterprise Search?

Yes, the Microsoft 365 Connector works well with **[Enterprise Search](https://support.claude.com/en/articles/12489464-using-enterprise-search)**. When enabled:

1. Enterprise Search can query Microsoft 365 alongside other connected tools.
2. You get unified search across Slack, Google Workspace, Microsoft 365, and more.
3. Enterprise Search's optimized prompts help Claude search more effectively.

#### Can Claude search archived emails?

Yes, Claude can search all emails you have access to in Outlook, including archived messages, as long as they're accessible through your account.

#### Does Claude search shared drives and team sites?

Yes, Claude can search any SharePoint sites and shared drives you have permission to access, including team sites, communication sites, SharePoint document libraries, and shared OneDrive folders.

#### Can Claude access private Teams channels?

Claude can only access Teams content that you have permission to view in Microsoft 365. If you're a member of a private channel, Claude can search for that content. If you're not a member, Claude can’t access it.

#### How do I ask Claude to search specific locations?

Be specific in your queries:

- **For specific SharePoint sites:** "Search the Engineering team site in SharePoint for architecture documents."
- **For specific date ranges:** "Find emails from the last week about the Q4 budget."
- **For specific senders or topics:** "Show me Teams discussions with Sarah about the product roadmap."
- **For specific file types:** "Find PowerPoint presentations in SharePoint about sales strategy."

#### Can Claude summarize long email threads?

Yes. Try something like: "Summarize the email thread about the vendor selection process." Claude will read the thread and provide a concise summary with key points and decisions.

#### What happens if a Microsoft 365 user tries to connect before a MicrosoftEntra Global Admininstrator grants tenant-wide permission?

You'll receive an error message indicating that an administrator must grant app permissions before you can use the connector. The connection attempt will fail until a Microsoft Entra Global Administrator approves the necessary permissions. If you're on an individual Claude plan, ask your Microsoft Entra admin to complete the consent process. If you're on a Team or Enterprise plan, your Claude Owner and Microsoft Entra admin both need to complete their respective setup steps.

## Related Articles
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
