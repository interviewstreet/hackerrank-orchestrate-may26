---
title: "Enforce network-level access control with Tenant Restrictions"
title_slug: "enforce-network-level-access-control-with-tenant-restrictions"
source_url: "https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions"
last_updated_iso: "2026-03-16T21:07:23Z"
article_id: "15020592"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Security and compliance"
---

# Enforce network-level access control with Tenant Restrictions

_Last updated: 2026-03-16T21:07:23Z_

> Tenant Restrictions are available for members of Enterprise plans and Console organizations.

Tenant Restrictions enable IT administrators on Enterprise plans to enforce network-level access control for Claude. This feature ensures that users on corporate networks can only access approved organizational accounts, preventing unauthorized use of personal accounts.

## How it works

When enabled, your network proxy injects an HTTP header into requests to Claude. Anthropic validates this header and blocks access from any organization not in the allowed list.

**Supported authentication methods:**

- Web access ([claude.ai](http://claude.ai))
- Desktop / App Access
- API key authentication
- OAuth token authentication

## Header format

```
anthropic-allowed-org-ids: &lt;org-uuid-1&gt;,&lt;org-uuid-2&gt;,...
```

- Comma-delimited list of organization UUIDs
- No spaces between values

**Example:**

```
anthropic-allowed-org-ids: 550e8400-e29b-41d4-a716-446655440000,6ba7b810-<br>9dad-11d1-80b4-00c04fd430c8
```

## Configuration steps

#### 1. Find your organization UUID

Members of Enterprise plans can find this in two different places:

1. Navigate to **[Settings > Account](https://claude.ai/settings/account)** and find **Organization ID**.
2. Navigate to **[Organization settings > Organization](https://claude.ai/admin-settings/organization)** and scroll down to the bottom of the page to locate **Organization ID**.

Members of Console organizations can find this in **[Settings > Organization](https://platform.claude.com/settings/organization)**.

#### 2. Configure your network proxy

Configure your proxy to inject the header for Claude traffic:

```
Rule: Claude Tenant Restriction<br>Application: claude.ai, api.anthropic.com, claude.com, anthropic.com<br>Action: Inject Header<br>Header Name: anthropic-allowed-org-ids<br>Header Value: <br>TLS Inspection: Required
```

#### 3. Test your configuration

From restricted network, test with your org's API key:

```
curl https://api.anthropic.com/v1/messages \<br>  -H "x-api-key: $CLAUDE_API_KEY" \<br>  -H "anthropic-version: 2023-06-01" \<br>  -H "content-type: application/json" \<br>  -d '{"model":"claude-sonnet-4-6","max_tokens":1024,"messages":<br> [{"role":"user","content":"Hello"}]}'
```

## Error response

When access is blocked, users receive the following error:

```
{<br>  "type": "error",<br>  "error": {<br>    "type": "permission_error",<br>    "message": "Access restricted by network policy. Contact IT Administrator.",<br>    "error_code": "tenant_restriction_violation"<br>  }<br>}
```

## Supported proxy platforms

- Zscaler ZIA (Cloud App Control policies)
- Palo Alto Prisma Access (SaaS App Management)
- Cato Networks (Tenant Restriction policy)
- Netskope (Header Insertion rules)
- Generic HTTPS proxies with header injection capability

## Use cases

## Security benefits

- **Data Loss Prevention:** Block personal account usage from corporate networks.
- **Compliance:** Enforce data residency and access policies.
- **Shadow IT Control:** Prevent unauthorized Claude usage.
- **Audit Trail:** Complete visibility into access attempts.

## Backward compatibility

- No impact to networks without tenant restrictions configured.
- Standard authentication continues for unmanaged networks.
- Existing API key authentication remains unchanged.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Microsoft 365 Connector: Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
- [Restrict access to Claude with IP allowlisting](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
