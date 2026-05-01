---
title: "Classification banner in Claude for Government"
title_slug: "classification-banner-in-claude-for-government"
source_url: "https://support.claude.com/en/articles/14503804-classification-banner-in-claude-for-government"
last_updated_iso: "2026-04-10T00:06:15Z"
article_id: "16971117"
breadcrumbs:
  - "Claude for Government"
---

# Classification banner in Claude for Government

_Last updated: 2026-04-10T00:06:15Z_

The classification banner displays a persistent marking at the top of every page for every user in your organization. Use it to communicate the classification level of data approved for your Claude for Government environment or any custom handling instruction your agency requires.

## When to use a classification banner

Set a classification banner whenever your agency's policy requires a persistent, page-level reminder of what data is and isn't appropriate to enter into Claude. The banner is visible on every screen, so users never lose sight of the environment's classification ceiling—even deep in a long conversation.

## Common configurations

- **CUI environments** — remind users that Controlled Unclassified Information is permitted but classified data is not
- **UNCLASSIFIED environments** — make the boundary explicit for users who also work in classified systems
- **Custom handling caveats** — agency-specific instructions beyond standard markings (e.g., "ITAR — No export-controlled technical data")

> **Note:** The banner is a visual reminder, not an enforcement control. It does not inspect or filter what users type. Pair it with Organization Preferences if you want Claude to apply handling guidance in conversations.

## Configure the classification banner

You must be the Primary Owner to configure the banner.

1. Navigate to **[claude.fedstart.com/admin-settings/organization](https://claude.fedstart.com/admin-settings/organization)**
2. Scroll to the **Classification banner** section
3. Fill in the banner fields:
  - Banner text — the marking that appears on the banner
  - Background color — the banner's fill color
  - Text color — the marking text color
  - Link URL (optional) — if provided, the banner text becomes a clickable link. You can point it at your agency's classification policy page or handling guide.
4. Click "Save." The banner appears for all users in your organization.

You can update the banner at any time by returning to the same settings page.

## Related Articles
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
- [Organization preferences in Claude for Government](https://support.claude.com/en/articles/14503675-organization-preferences-in-claude-for-government)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
