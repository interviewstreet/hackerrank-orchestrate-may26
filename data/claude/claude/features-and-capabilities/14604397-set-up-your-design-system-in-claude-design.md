---
title: "Set up your design system in Claude Design"
title_slug: "set-up-your-design-system-in-claude-design"
source_url: "https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design"
last_updated_iso: "2026-04-17T15:07:56Z"
article_id: "17088410"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Set up your design system in Claude Design

_Last updated: 2026-04-17T15:07:56Z_

Creating a design system allows Claude Design to produce outputs that fit your specifications. It extracts reusable components, colors, typography, and patterns from the assets you provide—codebases, slide decks, or other design references—and uses them as the foundation for every project created within your account.

> Claude Design by Anthropic Labs is now available in research preview to Pro, Max, Team, and Enterprise plans. This capability is default off for Enterprise plans.

This guide is for the designer or brand owner who will set up the design system. You only need to do this once; after setup, all team members’ projects automatically use it (for Team and Enterprise plans).

## Prerequisites

- Permissions granted by your organization admin for design system setup.
- At least one of the following as source material:
  - A codebase with your design system or component library
  - A slide deck or document that reflects your visual identity
  - Brand guideline assets (logos, color palettes, typography specs)

---

## Step 1: Create or switch to your organization

To set up your organization’s design system:

1. Open **[Claude Design](http://claude.ai/design)**.
2. In the lower-left corner of the project picker, click the current organization name.
3. Select your organization, or create a new one.
4. You’ll be redirected to the onboarding flow. Complete it.

## Step 2: Upload your brand and product assets

During onboarding (or afterward from your organization settings), upload the assets that define your brand and product. Claude will analyze them and extract a reusable design system.

**What to upload:**

- **Codebases: **If your design system lives in code (for example, a React component library), you can link or upload the repository. Claude will read the components and styles.
- **Prototypes:** Screenshots, web flows, and existing design files.
- **Slide decks or documents: **Even a well-designed PowerPoint or PDF that reflects your brand can work. Claude extracts colors, layout patterns, and typographic choices.
- **Individual assets: **Logos, color palette files, typography specimens.

You only need one source to get started, but providing multiple gives Claude more to work with.

## Step 3: Review the generated design system

After uploading, Claude generates a design system (UI kit) for your organization. This typically includes:

- **Color palette: **Primary, secondary, and accent colors extracted from your assets.
- **Typography: **Font families, sizes, and weights.
- **Components: **Buttons, cards, navigation elements, and other reusable UI patterns.
- **Layout patterns: **Spacing, grid systems, and page structures.

To validate your design system, create a test project and see if the output matches your brand expectations. Try prompts like:

- “Create a landing page for [your product].”
- “Design a dashboard showing [relevant metrics].”
- “Make a presentation about [a topic your team commonly presents on].”

## Step 4: Make it available to your team

Once you’re satisfied with the design system quality, make sure the “Published” toggle is switched on. After publishing, any projects created from the Claude Design homescreen while in your organization will use your design system instead of the default.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2287527007/b1c46cb8dba4cd7e8bbea85fb0c3/2819c6cf-9ce1-4df5-84c8-feae0164bf2e?expires=1776784500&signature=2f5ea886b5d55f892e26defd9acaac5875214a7db1f50586db51f8064a003794&req=diIvEcx8moFfXvMW1HO4zWNHGPSMBj8SIQKNMXlu0T%2Fn3khCc%2Bz5h8pwl%2FRt%0ARvgFSWg5yJZKDLXkBac%3D%0A)

---

## Tips for best results

- **Include real examples, not just specs. **A finished landing page or marketing site tells Claude more about your brand’s feel than a color palette alone.
- **Iterate. **If the first extraction doesn’t capture your brand well, try uploading additional or different assets.

## Updating your design system

Brands evolve. When your design system changes, you can update it within Claude Design. From your Claude Design organization settings, click the “Open” button next to the design system you want to edit. Click the “Remix” button in the upper right corner to open the chat interface on the left side of the window. From here, you can work with Claude to change your design system.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Design admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans)
- [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
