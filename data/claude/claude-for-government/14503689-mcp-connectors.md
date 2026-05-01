---
title: "MCP connectors"
title_slug: "mcp-connectors"
source_url: "https://support.claude.com/en/articles/14503689-mcp-connectors"
last_updated_iso: "2026-04-10T00:09:26Z"
article_id: "16970910"
breadcrumbs:
  - "Claude for Government"
---

# MCP connectors

_Last updated: 2026-04-10T00:09:26Z_

MCP connectors let Claude connect to your organization’s tools, data sources, and services. Claude can search your documents, read your email, or call external APIs on your behalf, all without leaving the chat.

For general questions about connectors in Claude, see **[Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)**.

## How MCP connectors differ in Claude for Government

**Claude for Government runs the first FedRAMP High authorized MCP implementation. **The MCP framework, the infrastructure that registers, authenticates, and executes Anthropic-provided connectors, operates entirely within the Claude for Government authorized boundary. Because the authorization covers MCP as a feature, new Anthropic-provided and customer-provided connectors can be added without additional FedRAMP audits of Claude for Government itself, as long as the connectors meet your agency's data-handling requirements.

**The connector catalog is curated.** Only connectors approved for the government environment appear in the Admin Settings directory, so some commercial Claude connectors are not available.

> **Important:** Some connectors call external APIs that transmit data outside the FedRAMP boundary. Each connector's catalog description states what data flows where. Your organization is responsible for evaluating whether that data flow is appropriate for your workloads, data classification levels, and applicable regulatory requirements.

## Browse available connectors

Organizations can also register their own MCP servers for internal systems, custom tools, or approved third-party services. See **[Custom Connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)**.

## Enable a connector for your organization

Connectors are enabled org-wide from Admin Settings. Once enabled, individual users in your organization can connect their own accounts.

> **Note**: You must be an Owner or Primary Owner to enable connectors. Members can connect their accounts to connectors that are already enabled but cannot add new ones to the catalog.

1. Navigate to **claude.fedstart.com/admin-settings/connectors** (or use your organization’s custom Claude for Government domain).
2. Click "Browse connectors" to view the catalog.
3. Select a connector and review its description, paying particular attention to what data leaves the boundary, if any.
4. Click "Add to your organization."
5. Some connectors require an organization-level authentication step (for example, the Microsoft 365 connector requires tenant-admin consent in Microsoft Entra). Follow the on-screen instructions.

## Connect your account to a connector

After your org admin enables a connector, it appears in your personal settings.

1. Navigate to **claude.fedstart.com/settings/connectors**
2. Click "Connect" next to the connector.
3. Complete the authentication flow—typically a one-time OAuth consent screen.
4. The connector is now active in your chats. Claude will use it automatically when relevant, or you can reference it directly ("search my SharePoint for…").

---

## Security and privacy

#### How authentication works

Connectors use delegated, per-user OAuth wherever possible. When you connect a tool, Claude inherits your permissions in that tool and can only see and do what you can already see and do. There are no service accounts with elevated access.

#### Where your credentials are stored

OAuth tokens are encrypted at rest and stored entirely within the Claude for Government FedRAMP High boundary. Tokens are scoped to the individual user who authenticated and are never shared between users. Anthropic does not receive standing access to your connected tenants.

#### What stays inside the boundary

The MCPservice, token storage, and all connector-execution audit logging stay inside the FedRAMP High authorized environment. Each tool invocation follows the path:

User → Claude (in boundary) → MCP service(in boundary) → connected service

Whether the **connected service** sits inside or outside the boundary depends on the connector. The catalog description for each connector states this explicitly. For example, the Microsoft 365 connector calls Microsoft Graph within your tenant; the Web Search connector calls a third-party search API outside the boundary under a zero-data-retention agreement.

> **Important:** Adding a connector does not change Claude for Government's FedRAMP authorization, but your agency's own ATO process may require you to evaluate the specific data-handling characteristics of each connector before enabling it.

---

## Frequently asked questions

#### Does enabling a connector give Anthropic access to our data?

No. Connectors use per-user delegated OAuth. Data flows between the in-boundary MCP proxy and the connected service using the individual user's credentials. Anthropic does not receive standing access to your tenant.

#### If we add a new connector, do we need to update our ATO?

Adding a connector does not change Claude for Government's FedRAMP authorization—MCP was authorized as a feature. Whether your agency's own ATO requires an update depends on the data the connector handles and your internal authorization process.

#### Can we restrict which users in our org can use a connector?

Connectors are enabled at the organization level. Once enabled, any user in the org can connect their individual account. Per-user or per-group connector gating is not currently available.

#### Can Claude take write actions—send emails, create files—through connectors?

It depends on the connector: admins should review all connector permissions before adding them. Custom connectors can expose write tools if your MCP server implements them; see the security guidance in Custom Connectors before enabling write scopes.

## Related Articles
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
- [MCP: Web Search](https://support.claude.com/en/articles/14503775-mcp-web-search)
