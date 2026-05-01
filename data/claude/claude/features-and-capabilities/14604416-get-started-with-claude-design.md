---
title: "Get started with Claude Design"
title_slug: "get-started-with-claude-design"
source_url: "https://support.claude.com/en/articles/14604416-get-started-with-claude-design"
last_updated_iso: "2026-04-17T15:07:03Z"
article_id: "17088437"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Get started with Claude Design

_Last updated: 2026-04-17T15:07:03Z_

Claude Design by Anthropic Labs lets you create designs, interactive prototypes, presentations, and more by having a conversation with Claude. This guide walks you through creating your first project, iterating on designs, and getting the most out of the tool.

> Claude Design by Anthropic Labs is now available in research preview to Pro, Max, Team, and Enterprise plans. This capability is default off for Enterprise plans.

This guide assumes your organization’s design system has already been set up, so everything you create will automatically use your brand’s colors, typography, and component patterns. If you’re a design lead who needs to set up or modify the design system itself, see **[Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)**.

---

## How Claude Design works

Claude Design has two main areas: a chat interface on the left and a canvas on the right. You describe what you want in the chat, and Claude generates a working design on the canvas. From there, you iterate—refining through conversation and inline comments until it’s right.

The typical flow is:

1. Create a project and add any relevant context (screenshots, a codebase).
2. Describe what you want to build.
3. Review what Claude generates on the canvas.
4. Iterate using chat messages and inline comments.
5. Export or share when you’re happy with the result.

---

## Create a new project

When you create a project, it automatically inherits your organization’s design system. You don’t need to upload brand assets or configure anything—your brand colors, fonts, and components are already in place.

#### Add context to your project

The more context you give Claude, the better your output will be. You can attach reference material at any point during a project.

- **Screenshots, images, or existing assets: **Upload screenshots of existing designs, competitor products, wireframes, or visual inspiration. You can also attach an existing slide deck or document with a design style you want to replicate. Useful for “make it look like this” requests.
- **Codebases and existing design files: **Link a code repository so Claude understands your existing components, architecture, and styling patterns. This makes prototypes more production-ready from the start. Import also supports multiple ways to upload existing product design work.

#### Write effective prompts

You don’t need to be a designer to get great results. Be specific about what you’re building, who it’s for, and what matters most.

A good prompt includes the **goal** (what you’re building), the **layout** (how things should be arranged), the **content** (what information to display), and the **audience** (who will use it). Claude will also ask clarifying questions if it needs more information.

Here are some examples of prompts that work well:

- “Create a dashboard showing monthly revenue with filters for region and product line.”
- “Design a mobile app onboarding flow with 4 screens that walks users through our core features.”
- “Build a landing page for our new API product with a hero section, code examples, and pricing.”
- “Create a form for collecting customer feedback with conditional questions based on category.”
- “Design an internal tool for our ops team to review and approve content submissions.”

---

## Iterate on your design

The first generation is a starting point. The real value comes from iterating.

#### Using chat

Chat is best for broad changes that affect the overall design:

- “Make the color scheme darker and more minimal.”
- “Rearrange the dashboard so metrics are in the top row and the chart is below.”
- “Add a settings panel on the right side.”
- “Show me 2–3 alternative layouts for this page.”

You can also ask Claude to explain its design decisions, suggest improvements, or review the design for accessibility.

#### Using inline comments

Inline comments let you click directly on a specific part of the canvas and request a targeted change. This is faster than describing the location in chat.

Examples of good inline comments:

- “Make this button padding larger.”
- “Change this to a dropdown instead of radio buttons.”
- “Use the primary brand color here.”
- “Make this section collapsible.”

> **Note: **If your comments aren’t being picked up, paste the feedback directly into the chat instead. This is a known workaround for an intermittent issue where comments can disappear before Claude reads them.

#### When to use chat vs. comments

Use **comments** for targeted, component-level changes (“fix this button,” “adjust this spacing”). Use **chat** for structural changes, new sections, aesthetic shifts, or anything that requires explanation or context.

## Manage versions and revisions

If you want to explore a different direction without losing your current work, tell Claude: “Save what we have and try a completely different approach.” Claude will save your current project and confirm where it’s saved, so you can reference earlier iterations in the conversation easily.

## Export and share

Once your design is ready, you can share it with colleagues or export it for use elsewhere. The right format depends on your use case—whether you’re getting stakeholder feedback, handing off to engineering, or presenting to a group.

Use the “Export” button in the upper right corner when viewing your project to choose from the following export formats.

- Download as .zip
- Export as PDF
- Export as PPTX
- Send to Canva
- Export as standalone HTML
- Handoff to Claude Code
  - Send to local coding agent
  - Send to Claude Code Web

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2287510952/553a03eec5cea7b9eff53b473552/6dc33363-38b1-444e-96bb-f8218b588173?expires=1776783600&signature=9174139372fdf5fc66441c12de9687206146101aa4285b3289abba56b3db83c9&req=diIvEcx%2FnYhaW%2FMW1HO4zQFD7ipdk25ynfz9ljnuyXSZ4tPkD6Pt0nIqbavu%0AdI4qjc%2B%2F6vs3Ywf1whc%3D%0A)

You can also share projects within your organization using a shareable link. Sharing options include view-only, comment, and edit access.

---

## Subscription usage and pricing

See here for more details: **[Claude Design subscription usage and pricing](https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing)**.

---

## Tips for best results

- **Start simple, then layer in complexity. **Begin with the core layout and content, then add interactions, edge cases, and polish. Claude responds well to incremental requests.
- **Be specific in your feedback. **“This doesn’t look right” is hard to act on. “Tighten the spacing between form fields to 8px” gives Claude exactly what it needs.
- **Reference your design system. **If you know a component exists in your brand’s system, mention it by name: “Use the Primary Button component” or “Apply the Card layout pattern.”
- **Think about responsiveness early. **Mention whether your design needs to work on mobile, tablet, and desktop, or just one of those.
- **Ask for variations. **If you’re unsure about a direction, ask Claude to show you 2–3 options. Comparing alternatives is much faster than guessing.
- **Ask Claude for feedback. **Claude can review your design for accessibility, contrast ratios, information hierarchy, and general usability. Treat it as a design collaborator, not just a generator.

---

## Known limitations

Claude Design is available as an experimental preview from Anthropic Labs. A few things to be aware of:

- **Comment persistence: **Inline comments occasionally disappear before Claude reads them. To work around this, paste the comment text into the chat.
- **Save errors in compact view: **The compact layout mode can trigger save errors. If this happens, switch to full view and retry.
- **Large codebases: **Linking very large repositories may cause lag or browser issues. Link specific subdirectories rather than entire monorepos.
- **Chat errors: **If you hit a “chat upstream error,” try starting a new chat tab within the same project.

## Related Articles
- [Get started with Claude](https://support.claude.com/en/articles/8114491-get-started-with-claude)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Your first day in Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code)
- [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)
- [Claude Design admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans)
