---
title: "Set organization preferences"
title_slug: "set-organization-preferences"
source_url: "https://support.claude.com/en/articles/14546867-set-organization-preferences"
last_updated_iso: "2026-04-15T17:36:58Z"
article_id: "17017652"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Admin management"
---

# Set organization preferences

_Last updated: 2026-04-15T17:36:58Z_

Organization preferences let Admins and above on Team and Enterprise plans set custom instructions that Claude follows in every conversation across your organization. Use them to apply communication standards, formatting requirements, compliance guidance, or domain-specific context that should show up everywhere your team works with Claude.

> Organization preferences are available to Admins, Owners, and Primary Owners on Team and Enterprise plans.

## How organization and user preferences interact

Claude supports two levels of preference instructions. Understanding how they interact helps admins and the people on your team get the most out of both.

When both are set, organization preferences take precedence. If an individual preference directly contradicts an organization preference, Claude favors the organization-level instruction. For example, if an organization preference says “Always respond in formal English” but an individual preference says “use a casual tone,” Claude responds formally.

Individual preferences still apply for anything the organization preferences don’t address.

> **Note: **Preference prioritization relies on prompt-level instructions. In rare edge cases involving directly contradictory instructions, behavior may vary. Test your preferences to confirm they produce the results you expect.

## Set up organization preferences

You need at least an Admin role to configure organization preferences.

1. Go to **[Organization settings > Organization and access](http://claude.ai/admin-settings/organization)**.
2. Find the **Organization preferences** section.
3. Enter your instructions in the text area. The maximum length is 3,000 characters.
4. Click “Save.”
5. Changes may take up to an hour to take effect across Claude products.

To remove preferences entirely, clear the text area and click “Save.”

---

## Best practices

**Keep instructions concise and clear. **Organization preferences are included in every message sent by everyone in your organization, so shorter instructions help keep conversations efficient. Aim for direct, specific guidance rather than lengthy explanations.

**Be specific about what you want. **Instead of vague instructions like “be professional,” give concrete direction such as “Respond in formal English. Don’t use contractions, slang, or emojis.”

**Focus on consistent behaviors. **Organization preferences work best for instructions that should apply uniformly across every conversation—response formatting standards, tone requirements, or organization-wide context.

**Avoid conflicting instructions. **If your organization preferences contradict each other, Claude may not follow either one reliably. Review your preferences as a whole to make sure they’re consistent.

**Don’t try to override safety behaviors. **Organization preferences can’t disable Claude’s built-in safety guidelines or content policies. Instructions that conflict with Claude’s core training won’t be followed.

**Test your preferences. **After saving, start a new conversation to verify Claude is following your instructions. Try a few different types of questions to confirm the preferences work across a range of topics.

**Review and update regularly. **As your organization’s needs change, revisit your preferences to make sure they’re still relevant. Removing outdated instructions keeps Claude’s responses focused.

---

## Example preferences

**Team identity. **“Address the team as the Acme Platform team. When users ask about ‘our product,’ they mean Acme Cloud.”

**Communication standards. **“Respond in formal English. Use active voice. Avoid contractions and emojis.”

**Response formatting. **“Prefer concise responses under 300 words. Use bullet points for lists with three or more items.”

**Domain context. **“Our team works in healthcare claims processing. When users mention ‘claims,’ they’re referring to insurance claims, not legal claims.”

**Referral guidance. **“When users ask about HR policies, direct them to [hr@acme.com](mailto:hr@acme.com) rather than giving specific policy advice.”

**Data handling reminders. **“Don’t include customer names, account numbers, or other personally identifiable information in responses or generated artifacts.”

## Related Articles
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [SSO login](https://support.claude.com/en/articles/14503613-sso-login)
- [Organization preferences in Claude for Government](https://support.claude.com/en/articles/14503675-organization-preferences-in-claude-for-government)
- [MCP: Web Search](https://support.claude.com/en/articles/14503775-mcp-web-search)
