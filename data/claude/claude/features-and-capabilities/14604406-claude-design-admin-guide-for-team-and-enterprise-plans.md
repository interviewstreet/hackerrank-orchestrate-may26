---
title: "Claude Design admin guide for Team and Enterprise plans"
title_slug: "claude-design-admin-guide-for-team-and-enterprise-plans"
source_url: "https://support.claude.com/en/articles/14604406-claude-design-admin-guide-for-team-and-enterprise-plans"
last_updated_iso: "2026-04-17T20:55:22Z"
article_id: "17088422"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Claude Design admin guide for Team and Enterprise plans

_Last updated: 2026-04-17T20:55:22Z_

Claude Design by Anthropic Labs lets your team create on-brand designs, prototypes, presentations, and interactive microsites through conversation with Claude.

> Claude Design by Anthropic Labs is available in research preview to Pro, Max, Team, and Enterprise plans. This capability is default off for Enterprise plans.

Claude Design works best when a **design system** is set up for your organization first. This ensures every project your team creates stays true to your brand, typography, color palette, and component patterns. This guide walks you through enabling Claude Design, setting up the right foundation, and rolling it out to your team.

## Enable Claude Design for your organization

Claude Design is available via a toggle in organization settings, and can be **[controlled using custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

Before you enable broad access, read through the rollout approach below. Turning on Claude Design without a design system in place means your team will get functional but generic output.

Team and Enterprise plan admins can enable this organization-wide by following these steps:

1. Go to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.
2. Find the **Claude Design** toggle under **Anthropic Labs** and switch it on.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2289240025/8a528b6cccc3ea1001c25953cb14/image.png?expires=1776783600&signature=214c04aae01c7e471fc9ca2827ce050d7cf1b6cebe854d33795e40c7021d5dd3&req=diIvH8t6nYFdXPMW1HO4zahp0uQPEeUjDIPtKBLQ9H8otgYAk7vUXV21x0dZ%0ACzrqb%2B3EWbAJUs6IpEs%3D%0A)

##

---

## The design system: why it comes first

The single most important thing you can do before rolling out Claude Design is have an experienced designer set up your organization’s design system. Once in place, every project your team creates automatically reflects your brand.

This means your rollout has a natural sequence: design system setup first, then broader access.

#### Who should set up the design system

For best results, we recommend pulling in designers across both brand and product design. Together they can ensure the design system covers both brand identity and product UI patterns.

#### What they’ll do

1. Create your organization in Claude Design (see **[Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)**).
2. Complete the onboarding flow.
3. Upload brand assets (codebases, slide decks, or other design references).
4. Validate that Claude generates designs consistent with your brand.

Access to design system setup is controlled separately from general Claude Design access via custom roles, as described above. This lets you grant design system editing permissions to your trusted designers while giving broader feature access to the rest of your team.

---

## Recommended rollout phases

A phased rollout lets you validate your design system and build internal expertise before broad adoption. You can control access to Claude Design in accordance with each rollout phase using **[custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**.

#### Phase 1: Design system setup

- **Who: **2–4 trusted designers and design leads across brand and product design.
- **Goal: **Create and validate your organization’s design system.
- **Checkpoint: **Review generated output for brand consistency before proceeding.

#### Phase 2: Design team onboarding

- **Who: **Full design team.
- **Goal: **Build familiarity with Claude Design; stress-test the design system across real projects.
- **Checkpoint: **Gather feedback on design quality and refine the design system if needed.

#### Phase 3: Product and UX onboarding

- **Who: **Product managers, UX researchers, and adjacent functions.
- **Goal: **Enable faster prototyping and design collaboration beyond the design team.
- **Checkpoint: **Observe usage throughout the organization and gather feedback on usability.

#### Phase 4: Broader organization

- **Who: **Entire organization or specific departments.
- **Goal: **Make design creation available widely while maintaining brand consistency.
- **Checkpoint: **Observe usage throughout the organization and gather feedback on usability.

#### Rollout tips

- Announce each phase clearly so people know when their turn is coming.
- Consider running a short training session or office hours during early phases.
- Establish a feedback channel for design system improvements.
- Share examples of creative uses of Claude Design internally to help foster creativity.

---

## What your team can do with Claude Design

Once set up, your team can use Claude Design to:

- **Create prototypes and mockups: **Describe a UI and get a working interactive prototype.
- **Build presentations and slide decks: **Generate on-brand decks through conversation, presentable as HTML, PDF, and PPTX.
- **Design microsites and landing pages: **Create polished single-page sites.
- **Iterate with inline comments: **Annotate designs directly on the canvas and ask Claude to implement changes.
- **Hand off to engineering: **Export design intent for use with Claude Code or your existing development workflow.

We have more tutorials available here:

- **[Using Claude Design for prototypes and UX](http://claude.com/resources/tutorials/using-claude-design-for-prototypes-and-ux)**
- **[Using Claude Design for presentations and slide decks](http://claude.com/resources/tutorials/using-claude-design-for-presentations-and-slide-decks)**

---

## Monitor usage

Claude Design is an Anthropic Labs release that doesn’t support audit logs or usage tracking yet.

We recommend tracking adoption qualitatively during your rollout—check in with each group as they onboard, collect feedback, and sample a few projects periodically to assess design system compliance.

## Data handling and privacy

When your team uses Claude Design, they may upload design assets, brand guidelines, screenshots, and other materials. Understanding how these are handled is important for organizations with data governance requirements.

- Uploaded assets are stored persistently, and fall under the same **[data retention and deletion policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** as other Anthropic enterprise products.
- Claude Design doesn’t currently support data residency requirements.

---

## Third-party platform availability

Claude Design is currently available only through the web interface at claude.ai/design.

If your organization requires Claude Design through your existing cloud provider agreements, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.

---

## Subscription usage and pricing

See here for more details: **[Claude Design subscription usage and pricing](https://support.claude.com/en/articles/14667344-claude-design-subscription-usage-and-pricing)**.

---

## Frequently asked questions

#### Do all team members need to upload brand assets?

No. Once a designer sets up your organization’s design system, all projects created within that organization automatically use it. Team members just start creating.

#### Can we have multiple design systems for different brands or sub-teams?

Yes. Organizations can have multiple design systems.

#### What happens if someone starts using Claude Design before the design system is set up?

They’ll get functional designs, but the designs won’t reflect your brand. We strongly recommend completing design system setup first for the best team experience.

#### Can I restrict Claude Design to specific departments?

Yes. Use the RBAC controls to grant access to specific groups or departments rather than enabling it org-wide.

#### How many users can we onboard at once?

There are no strict limits, but we recommend the phased approach outlined above to ensure quality and successful adoption across your organization.

#### Can we export or archive generated designs?

Claude Design currently supports export to HTML bundles, PPTX, PDF, and hand-off to Claude Code. Additional export options will be added over time. Reach out to your sales contact if there’s a specific format or destination you need.

## Related Articles
- [Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)
- [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
