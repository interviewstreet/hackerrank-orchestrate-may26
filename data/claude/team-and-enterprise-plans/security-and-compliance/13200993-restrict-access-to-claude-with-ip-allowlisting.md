---
title: "Restrict access to Claude with IP allowlisting"
title_slug: "restrict-access-to-claude-with-ip-allowlisting"
source_url: "https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting"
last_updated_iso: "2026-03-16T21:23:50Z"
article_id: "15023830"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Security and compliance"
---

# Restrict access to Claude with IP allowlisting

_Last updated: 2026-03-16T21:23:50Z_

> IP allowlisting is available for Enterprise plans only.

IP allowlisting enables Enterprise plan administrators to control which IP addresses can access Claude through their organization. This feature ensures that requests can only be made from approved network locations, providing an additional layer of security.

When enabled, we validate the source IP address of every authenticated request against your organization's configured allowlist. Requests from IP addresses not added to the allowlist will be blocked.

IP allowlisting supports CIDR ranges. For example: `10.0.0.0/8, 2001:db8::/32`.

## How to configure IP allowlisting

If your Enterprise organization is interested in enabling an IP allowlist, please compile a list of all necessary CIDR ranges for your organization, including office locations, VPN exit points, and any other approved access points. Omitting required CIDR ranges could result in users getting locked out of Claude. Then, reach out to your Anthropic Contact or our [Sales team](https://claude.com/contact-sales) to share your list of CIDR ranges. They can add these to your account’s allowlist to enable the feature.

When a request originates from an IP address that’s not in your allowlist, access is denied. Users should contact their IT administrator if they believe they're being blocked in error.

## Related Articles
- [Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)
- [Enforce network-level access control with Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)
- [Claude Enterprise Analytics API: Access engagement and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
