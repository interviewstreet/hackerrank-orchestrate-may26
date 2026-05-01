---
title: "Model availability in Claude for Government"
title_slug: "model-availability-in-claude-for-government"
source_url: "https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government"
last_updated_iso: "2026-04-10T00:02:35Z"
article_id: "16971091"
breadcrumbs:
  - "Claude for Government"
---

# Model availability in Claude for Government

_Last updated: 2026-04-10T00:02:35Z_

Claude is a family of state-of-the-art large language models developed by Anthropic. This guide introduces the models available for customers using Claude for Government. For the most up to date information about the model’s general capabilities, please visit our **[Model Overview page](https://platform.claude.com/docs/en/about-claude/models/overview)**.

## How model availability differs in Claude for Government

Claude for Government routes all inference through Google Cloud Vertex AI's FedRAMP High authorized environment rather than Anthropic's commercial endpoints. This is what keeps model traffic inside the authorization boundary.

#### New models arrive shortly after commercial launch

New models are typically available in Claude for Government the same day or within one to two days of their commercial release. The gating factor is Vertex availability—once a model is serving on Vertex, Anthropic completes the Claude for Government and the models become available to users.

> **Note:** There is **no separate FedRAMP audit per model**. Vertex's authorization is infrastructure-level, not per-model. Once the Claude for Government environment is authorized, new models inherit that authorization automatically. Your agency does not need to re-engage Anthropic's FedRAMP process when a new model ships.

#### Opus access is gated by seat tier

Unlike Enterprise, Claude for Government restricts Opus-class models to certain seat tiers. Lite seats—the default tier in the federal agency offer—have full access to Sonnet and Haiku but not Opus.

## Seat types and model access

**Lite seats** are the tier included in the federal agency offer and are designed for agency-wide deployment at minimal per-seat cost. Lite seats have full access to Sonnet-class models and Haiku models. Lite seats have capped usage per 5-hour window.

**Standard seats** provide access to all available models, including Claude Opus, with full-capacity rate limits. Standard seats are best for power users whose work benefits from Opus-class reasoning, such as complex analysis, advanced coding, and long-horizon research.

## How admins manage model access

**Seat tier assignment.** Admins can assign seat tiers to users via SCIM group mappings in **Organization settings > Identity**. Create groups in your identity provider for each tier (e.g., `claude-standard-users` and `claude-lite-users`), push them via SCIM, and map each group to a seat tier in Claude for Government. Users inherit the seat tier of their group.

**Default model selection.** Admins can set the organization's default model in Admin Settings. New conversations will start on this model unless the user selects a different one.

**Changing a user's seat tier.** Move the user between groups in your identity provider; the change syncs to Claude for Government on the next SCIM cycle.

## When new models arrive

Agencies don't take any action to receive new models—they show up in the model picker once enabled. Anthropic announces availability through your public sector account contact and in release notes.

If your agency policy requires advance notice or opt-in before new models reach users, contact your Anthropic public sector representative to discuss configuration options.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Public Sector FAQs](https://support.claude.com/en/articles/13756069-public-sector-faqs)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
