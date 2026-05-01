---
title: "Real-time cyber safeguards on Claude"
title_slug: "real-time-cyber-safeguards-on-claude"
source_url: "https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude"
last_updated_iso: "2026-04-16T13:24:56Z"
article_id: "17089111"
breadcrumbs:
  - "Safeguards"
---

# Real-time cyber safeguards on Claude

_Last updated: 2026-04-16T13:24:56Z_

As part of our ongoing safety commitments, we are rolling out new real-time cyber safeguards on our most capable Claude models. These safeguards are designed to automatically detect and block requests that may indicate prohibited or high-risk cybersecurity usage based on our Usage Policy.

We continuously evaluate our models against emerging threats and evolve our defenses accordingly. After extensive capability and safety testing, we believe a stronger, real-time layer of cyber defense is now warranted on our most capable models.

This work is ongoing. We'll continue to test, refine, and evolve safeguards over time.

## How this works

Our cyber safeguards currently block two categories of activities:

- **Prohibited use:** Cybersecurity activities that are almost always used maliciously and have little to no legitimate defensive application such as mass data exfiltration or ransomware code development. These are blocked by default and not subject to adjustment via self-serve application through the Cyber Verification Program.
- **High Risk Dual use:** Cybersecurity activities that have legitimate defensive applications, such as vulnerability exploitation or offensive security tooling development. These are blocked by default, but defensive users can apply for adjustment for legitimate use cases through the Cyber Verification Program described below.

## Cyber Verification Program

Many cybersecurity practitioners do legitimate work that overlaps with the dual use category above. The Cyber Verification Program (CVP) is a free application-based program that is designed to enable professionals to continue working on legitimate dual use tasks safely while minimizing interruption.

If your use case has a legitimate defensive purpose and is being affected by these safeguards, we encourage you to apply for the CVP. See **How to apply** below for the right path based on how you access Claude.

Organizations on Zero Data Retention (ZDR) are not currently eligible to participate in the CVP. If you have a Sales Managed ZDR account, please contact your Anthropic Sales Representative for more information.

## How to apply

How you apply depends on how you access Claude. Once you submit your application, we aim to send an email notification with our review decision within 2 business days.

Cyber Use Case Form

**Are you a platform owner?** If you use Claude to power products or services available to your customers and want to learn whether your platform is eligible to participate in the Cyber Verification Program, please **[fill out this Platform CVP Interest Form](https://claude.com/form/platform-cvp-interest)**.

## Appeals

We expect to occasionally decline eligible applications incorrectly, and approved users may still experience blocks on legitimate work. We’re actively working to reduce both.

If you’re encountering one of these issues, we recommend checking the following:

**Are you signed in to the right organization?** CVP approval is tied to a specific organization ID. If you're hitting blocks on a different organization—for example, your personal workspace instead of your team's organization—the approval doesn't carry over. Compare the organization ID where you're seeing blocks against the one on your approval email.

**Is the activity actually dual use?** CVP approval only lifts blocks on dual use activities. Prohibited use activities (e.g., mass data exfiltration, ransomware code development) remain blocked regardless of CVP status.

If you've checked both and still believe something is wrong, you can **[submit a report or appeal form](https://claude.com/form/cyber-block-false-positive-report-cvp-rejection-appeal)**. Your feedback helps us refine these safeguards.

## Related Articles
- [API Safeguards Tools](https://support.claude.com/en/articles/9199617-api-safeguards-tools)
- [Model Safety Bug Bounty Program](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program)
- [Getting started with Claude for Nonprofits](https://support.claude.com/en/articles/12893767-getting-started-with-claude-for-nonprofits)
- [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
