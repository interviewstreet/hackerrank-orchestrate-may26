---
title: "Organization preferences in Claude for Government"
title_slug: "organization-preferences-in-claude-for-government"
source_url: "https://support.claude.com/en/articles/14503675-organization-preferences-in-claude-for-government"
last_updated_iso: "2026-04-09T23:39:29Z"
article_id: "16970877"
breadcrumbs:
  - "Claude for Government"
---

# Organization preferences in Claude for Government

_Last updated: 2026-04-09T23:39:29Z_

Organization preferences allow administrators to define custom instructions that Claude follows in every conversation for all users in the organization. Use this to set compliance guidance, communication standards, formatting requirements, or domain-specific context.

## How organization and user preferences interact

Claude supports two levels of preference instructions. Understanding how they interact helps administrators and users get the most out of both.

When both are set, organization preferences take precedence. If a user preference directly contradicts an organization preference, Claude will strongly favor the organization-level instruction. For example, if an organization preference says "Always respond in formal English" but a user preference says "Use casual tone," Claude will respond formally.

Individual user preferences still apply for anything not addressed by the organization preferences.

> **Note**: Preference prioritization relies on prompt-level instructions. In rare edge cases involving directly contradictory instructions, behavior may vary. Test your preferences to confirm they produce the expected results.

## Set up organization preferences

To configure organization preferences, you must have an Owner or Admin role for your organization.

1. Click the gear icon in the lower left corner and select "Organization settings."
2. Select **Organization**.
3. Locate the **Organization preferences** section.
4. Enter your instructions in the text area. You can include guidance such as compliance rules, formatting requirements, communication standards, or domain-specific context. The maximum length is 3,000 characters.
5. Click "Save." Your preferences take effect immediately for all users in the organization.

To remove preferences entirely, clear the text area and click "Save."

---

## Best practices

**Keep instructions concise and clear.** Organization preferences are included in every message sent by every user in your organization, so shorter instructions help keep conversations efficient. Aim for direct, specific guidance rather than lengthy explanations.

**Be specific about what you want**. Instead of vague instructions like "be professional," provide concrete direction such as "Respond in formal English. Do not use contractions, slang, or emojis."

**Focus on consistent behaviors**. Organization preferences work best for instructions that should apply uniformly across all conversations, such as compliance requirements, response formatting standards, or classification handling rules.

**Avoid conflicting instructions.** If your organization preferences contradict each other, Claude may not follow either one reliably. Review your preferences as a whole to ensure they are consistent.

**Do not attempt to override safety behaviors.** Organization preferences cannot disable Claude's built-in safety guidelines or content policies. Instructions that conflict with Claude's core training will not be followed.

**Test your preferences.** After saving, start a new conversation to verify Claude is following your instructions as expected. Try a few different types of questions to make sure the preferences work well across a range of topics.

**Review and update regularly.** As your organization's needs change, revisit your preferences to ensure they remain relevant and accurate. Removing outdated instructions keeps Claude's responses focused.

---

## Example preferences

**Compliance and classification guidance** — "Treat all responses as CUI. Do not include controlled unclassified information in web search queries or file names."

**Communication standards** — "Always respond in formal English. Use active voice."

**Domain-specific context** — "Users are federal agency employees. When they reference 'the system,' they mean our grants management platform."

**Response formatting** — "Prefer concise responses under 300 words. Use bullet points for lists with three or more items."

**Referral guidance** — "When users ask about HR policies, direct them to [hr@example.com](mailto:hr@example.com) rather than providing specific policy advice."

## Related Articles
- [Understanding Claude's Personalization Features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Classification banner in Claude for Government](https://support.claude.com/en/articles/14503804-classification-banner-in-claude-for-government)
- [Set organization preferences](https://support.claude.com/en/articles/14546867-set-organization-preferences)
