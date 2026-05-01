---
title: "Deploying enterprise-grade MCP servers with desktop extensions"
title_slug: "deploying-enterprise-grade-mcp-servers-with-desktop-extensions"
source_url: "https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions"
last_updated_iso: "2026-03-16T20:59:16Z"
article_id: "14286075"
breadcrumbs:
  - "Claude Desktop"
  - "Desktop extensions"
---

# Deploying enterprise-grade MCP servers with desktop extensions

_Last updated: 2026-03-16T20:59:16Z_

Desktop extensions are installable packages that run Model Context Protocol (MCP) servers locally on your machine. They provide Claude Desktop with secure access to your local resources, internal systems, and personal tools without the complexity of remote infrastructure.

With desktop extensions, you can deploy enterprise-grade MCP implementations with fine-grained admin controls. This article explains why desktop extensions are valuable for organizations and how to use them effectively.

## Why use desktop extensions?

#### Seamless authentication

Desktop extensions operate within your corporate network boundaries, using the user’s existing authenticated context without requiring additional firewall rules or VPN configurations. They leverage existing SSO and browser sessions automatically with no token management required – credentials stay securely on user devices.

#### Access internal resources

Desktop extensions connect to internal wikis, JIRA, Confluence, and other systems behind your firewall. They can query private databases and APIs without VPN configuration, connect to on-premises systems like SAP, Oracle, and custom applications, and access internal resources without exposing them on public infrastructure.

#### Read and manipulate local resources

Desktop extensions provide access to local resources that remote connectors cannot reach. This includes direct filesystem access for code editing and Git operations, integration with locally installed tools like Docker, IDEs, and databases, control over desktop applications via local APIs, and hardware integration for specialized workflows.

#### Instant deployment with minimal infrastructure overhead

One-click installation through Claude Desktop comes with no dependencies to manage. The built-in [Node.js](http://node.js) runtime is included, there’s no cloud infrastructure to provision, and updates are distributed directly through the extension marketplace.

#### Enterprise-grade controls

Organization owners can upload custom extensions to their organization and control which desktop extensions their users have access to through the desktop extension allowlist. To learn more about managing desktop extensions in your organization, see Enabling and using the desktop extension allowlist.

## Enterprise use cases

**Multiple enterprises are building desktop extensions to serve a variety of use cases:**

- As secure proxies to internal MCP servers, giving them complete control over access, authentication, and audit logs while maintaining their zero-trust architecture.
- To give Claude access to internal documentation and knowledge bases.
- To connect to development tools and databases securely, and maintain complete control over authentication, authorization, and audit logging.

Desktop extensions eliminate the traditional tradeoff between security and usability—providing Claude with powerful capabilities while maintaining your enterprise security posture.

## Related Articles
- [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
- [Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)
