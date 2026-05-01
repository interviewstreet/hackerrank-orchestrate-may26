---
title: "Microsoft 365 Connector: Security Guide"
title_slug: "microsoft-365-connector-security-guide"
source_url: "https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide"
last_updated_iso: "2026-04-03T16:20:03Z"
article_id: "14259460"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Microsoft 365 Connector: Security Guide

_Last updated: 2026-04-03T16:20:03Z_

> The Microsoft 365 connector is available on all Claude plans: Free, Pro, Max, Team, and Enterprise.

## What it is

The Microsoft 365 Connector is an **Anthropic-hosted integration** that enables Claude to securely access Microsoft 365 services (Outlook, SharePoint, OneDrive, Teams) through user-delegated permissions. Anthropic has completed Microsoft's publisher verification process, associating our verified Microsoft Partner Network account with this application to confirm our organizational identity.

The connector operates as a **secure proxy**, and your Microsoft 365 documents, emails, and files remain in your tenant. The connector only retrieves data on-demand during active queries and doesn’t cache file content. Credentials are encrypted and managed by Anthropic's backend infrastructure. The MCP server itself doesn’t store or manage these credentials. Microsoft's Azure SDK handles the On-Behalf-Of token exchange and caching on a per-user basis for accessing the Graph API.

## Access restriction

#### Access can be fully restricted

The connector provides **multiple layers of access control** to address your security requirements. For detailed information on administration of the Microsoft 365 Connector see **[Enabling and using the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector)**.

**1. Microsoft Entra tenant requirement**

All people using the connector—regardless of Claude plan—must authenticate with a Microsoft 365 account tied to a Microsoft Entra tenant. Personal Microsoft accounts (@outlook.com, @hotmail.com) can't be used. A Microsoft Entra Global Administrator must complete a one-time consent process before anyone in the tenant can connect.

**2. Organization-level gating (Team and Enterprise plans)**

On Team and Enterprise plans, access to the connector requires a two-step approval process. First, Owners must explicitly enable the Microsoft 365 connector in Claude organization settings by navigating to Organization settings > Connectors > Browse connectors > Add "Microsoft 365." Until this approval is granted, team members have no access.

Second, after the Owner enables the connector, a Microsoft Entra Global Administrator must complete individual authentication and grant consent on behalf of the whole organization before any team members can connect.

**3. Granular permission revocation**

You can selectively disable specific capabilities via Microsoft Entra Admin Center. For example:

Changes take effect immediately for all people in your organization. People can also choose to disable capabilities during a chat by selectively toggling off the connector's tools.

**4. Microsoft conditional access integration**

The connector fully supports your existing Entra (Azure AD) policies:

- **Multi-factor authentication (MFA)**: Enforce MFA for connector access
- **Device compliance**: Require managed/compliant devices
- **IP restrictions**: Limit Microsoft authentication to corporate network or VPN
- **Group-based access**: Restrict to specific security groups

**5. User-level permissions**

- The Microsoft 365 Connector uses **[delegated permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#delegated-permissions)**.
- Users can only access Microsoft 365 data **they already have permission** for
- SharePoint search requires Sites.Read.All permission. Site-specific permissioning (using *.Selected permissions) is not supported because the underlying search is tenant-wide.
- Users cannot bypass SharePoint sharing settings or folder permissions
- Users cannot access other users' private files or emails
- Delegated permissions inherently respect Microsoft 365 data loss prevention (DLP) policies

**6. Token management**

- Refresh tokens expire after 90 days of inactivity by default, requiring re-authentication. This can be customized in Microsoft Entra ID using a token lifetime policy.
- Access tokens typically expire within 60-90 minutes per Microsoft Entra ID defaults and are automatically refreshed
- Admins or users can revoke access anytime via Microsoft Entra ID
- The Microsoft 365 Connector never sees or stores passwords

## Security architecture summary

#### Authentication flow

- **OAuth 2.0 On-Behalf-Of (OBO):** Industry-standard delegated authentication
- **PKCE protection**: Public client uses Proof Key for Code Exchange to prevent authorization code interception
- **Two-stage token exchange**: User authenticates to obtain access token for MCP server, then MCP server exchanges it for Graph API access using OBO flow with confidential client credentials. In this flow, not even the user or their Claude client has access to the OBO tokens. Only the MCP server can access and use tokens with access to the user’s data via the Microsoft Graph API.
- **No credential storage**: Users never share Microsoft passwords with Anthropic
- **Encrypted token storage**: Access and refresh tokens are encrypted while cached by the Claude backend

#### Data flow

- Documents and other content are retrieved **only during active queries**
- **Tool call results **from the connector that are **part of stored chats are retained**
- **The user who requested the Claude chat** can see the tool call results and Claude’s response incorporating the data
- **Other users shared on the chat** can only see Claude’s response incorporating the result of the tool call
- Each request creates a fresh data flow which is cleaned up after the response is returned

#### Multi-tenant isolation

- Microsoft Entra tenants are **cryptographically separated** from each other using a common-scoped multi-tenant configuration
- Multi-tenant isolation is cryptographically enforced through digitally signed access tokens that bind each user to their organization’s tenant

## Available capabilities

#### Current features (read-only access)

The connector provides **read-only** access to:

## Permissions list

**Basic permissions**

- [User.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#userread) - Sign in and read user profile (basic requirement)

**Mail permissions**

- [Mail.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#mailread) - Read user mail (required for email tools/resources)
- [Mail.ReadBasic](https://learn.microsoft.com/en-us/graph/permissions-reference#mailreadbasic) - Read user mail metadata (alternative for limited functionality)
- [Mail.Read.Shared](https://learn.microsoft.com/en-us/graph/permissions-reference#mailreadshared) - Read user and shared mail
- [MailboxFolder.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#mail-permissions) - Read a user's mailbox folders
- [MailboxItem.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#mail-permissions) - Read a user's mailbox items

**Calendar permissions**

- [Calendars.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#calendarsread) - Read user calendars and events
- [Calendars.Read.Shared](https://learn.microsoft.com/en-us/graph/permissions-reference#calendarsreadshared) - Read calendars user can access, including shared

**User directory**

- [User.ReadBasic.All](https://learn.microsoft.com/en-us/graph/permissions-reference#userreadbasicall) - Read basic profiles of all users (for meeting availability)

**Chat permissions**

- [Chat.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#chatread) - Read user chat messages
- [Chat.ReadBasic](https://learn.microsoft.com/en-us/graph/permissions-reference#chatreadbasic) - Read user chat metadata (alternative for limited functionality)
- [ChatMember.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#chatmemberread) - Read the members of chats
- [ChatMessage.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#chatmessageread) - Read user chat messages (more specific than Chat.Read)

**Channel permissions**

- [Channel.ReadBasic.All](https://learn.microsoft.com/en-us/graph/permissions-reference#channelreadbasicall) - Read the names and descriptions of channels
- [ChannelMessage.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#channelmessagereadall) - Read channel messages

**Meeting permissions**

- [OnlineMeetings.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#onlinemeetingsread) - Read online meetings
- [OnlineMeetingTranscript.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#onlinemeetingtranscriptreadall) - Read meeting transcripts
- [OnlineMeetingAiInsight.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#onlinemeetingaiinsightread) - Read all AI Insights for online meetings
- [OnlineMeetingArtifact.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#onlinemeetingartifactreadall) - Read user's online meeting artifacts
- [OnlineMeetingRecording.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#onlinemeetingrecordingreadall) - Read all recordings of online meetings

**Files permissions**

- [Files.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#filesread) - Read user files
- [Files.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#filesreadall) - Read all files user can access

**Sites permissions**

- [Sites.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesreadall) - Read items in all site collections
- [Sites.Selected](https://learn.microsoft.com/en-us/graph/permissions-reference#sitesselected) – Manages application access at the site collection level, providing access to a specific site collection

## Current limitations

- **No write capabilities**: Cannot send emails, schedule meetings, create/modify documents, or post Teams messages.
- **User-level access only**: Access with service principal authentication is not supported.

## Frequently asked questions

#### Can we test with a small pilot group before enterprise-wide rollout?

Yes. The recommended approach is to use app assignment to restrict who can use the connector:

- Enable the connector (Team and Enterprise Owners enable it in organization settings; individual plan users can connect directly).
- Microsoft Entra Admin completes pre-consent setup
- Use Microsoft Entra Enterprise App assignment to restrict access to specific users or groups (e.g., assign only "IT Security Test Group" to the app).
- Expand groups progressively for gradual deployment

#### How do we ensure no data leakage occurs between our organization and others in the multi-tenant environment?

Multi-tenant isolation ensures complete separation:

- Server uses the common tenant configuration to accept tokens from any Microsoft Entra ID tenant
- Each user's token contains their organization's tenant ID (tid claim) which is validated
- Graph API tokens obtained through OBO are automatically scoped to the user and their tenant
- Cross-tenant token access is prevented cryptographically by the design of Microsoft Graph’s OAuth 2.0 implementation.

#### What happens if someone tries to connect with a personal Microsoft account?

The connector requires a Microsoft Entra tenant tied to a Microsoft Business plan. Personal Microsoft accounts (@outlook.com, @hotmail.com) can't be used to authenticate. People attempting to connect with a personal account will receive an authentication error.

#### Do you have audit logging for compliance?

Yes. All Graph API calls made by the connector are logged in your organization's Microsoft 365 audit log, which you can access through the M365 Compliance Center. These logs show the timestamp, user, operation performed, and resource accessed, with retention periods matching your Microsoft 365 audit policy. Additionally, Anthropic logs authentication and tool execution events.

#### Can we revoke access if we discover unauthorized usage?

There are multiple revocation methods:

- **Individual:** Users disconnect via **Customize > Connectors**
- **Admin-level**: On Team and Enterprise plans, Owners disable the connector in Claude organization settings (all team members affected).
- **Permission-level**: Revoke specific permissions in Microsoft Entra Admin Center
- **Tenant-level**: Revoke all permissions in Microsoft Entra Admin Center

#### What certifications does Anthropic have?

Anthropic has the following certifications:

- **SOC 2 Type II** (annual audit)
- **ISO 27001** certified
- **GDPR compliant** (DPA available)
- **Microsoft publisher-verified** application

## Additional resources

- Claude Help Center: **[Enabling and using the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector)**
- **[Overview of Microsoft Graph permissions: Delegated permissions](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#delegated-permissions)**

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Enable and use the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-enable-and-use-the-microsoft-365-connector)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
