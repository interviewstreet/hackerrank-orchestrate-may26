---
title: "Using Claude Code with your Max plan"
title_slug: "using-claude-code-with-your-max-plan"
source_url: "https://support.claude.com/en/articles/11145838-using-claude-code-with-your-max-plan"
last_updated_iso: "2026-04-21T00:08:52Z"
article_id: "12031902"
breadcrumbs:
  - "Claude Code"
---

# Using Claude Code with your Max plan

_Last updated: 2026-04-21T00:08:52Z_

This article applies to individual consumers using Max plan subscriptions to access Claude Code. If you’re a member of a Team or Enterprise plan organization, see **[Using Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)**.

## What is Claude Code?

Claude Code is a command line tool that gives you access to Claude models directly in your terminal, allowing you to delegate complex coding tasks while maintaining transparency and control. With Max plans, you now have access to both Claude on the web, desktop, and mobile apps and Claude Code in your terminal with one unified subscription.

#### Why use Claude and Claude Code?

Use two powerful AI products in one simple subscription.

- Use Claude for writing, research, analysis, and more — at work and at home.
- Use Claude Code for your terminal-based coding workflows.

---

## How to connect Claude Code to your Max plan

1. **Ensure you have an active Max plan subscription**
  - If you're not already subscribed, upgrade at **[claude.ai/upgrade](https://claude.ai/upgrade)**
2. **Install Claude Code**
  - Visit the **[Claude Code page in our Claude Docs](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)** to download and install Claude Code.
  - Follow the installation instructions for your operating system.
3. **Authenticate with your Claude credentials**
  - When prompted during setup or first use, log in with the same credentials you use for Claude.
  - This will connect your Max plan subscription to Claude Code.
  - If you're already logged in to Claude Code via Claude Console PAYG, run /login from within Claude Code to switch to your subscription plan.

#### Having trouble using your Max plan to access Claude Code?

If you're not seeing the option to authenticate with your preferred account, follow these steps to update Claude Code:

1. Log out of your active session completely using the `/logout` command.
2. Run `claude update`.
3. Restart your terminal completely for the change to take effect.
4. Run `claude` and select the correct account to use Claude Code.

> **Important: **If you have an ANTHROPIC_API_KEY environment variable set on your system, Claude Code will use this API key for authentication instead of your Claude subscription (Max, Team, or Enterprise plans), resulting in API usage charges rather than using your subscription's included usage. See this article for more information: **[Managing API key environment variables in Claude Code](https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code).**

---

## What happens when you hit usage limits

Max plans offer usage limits that are shared across Claude and Claude Code, meaning all activity in both tools counts against the same usage limits. To help you monitor your usage, you will see warning messages about remaining capacity.

When you reach your usage limits, you can select from a few options based on your needs:

#### Max plan users

- If you're on the Max 5x plan, consider upgrading to the Max 20x plan if you consistently hit limits.
- **[Enable extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-max-20x-plans)** to continue using Claude with your Max plan after hitting the included usage limit.
- You will have the flexibility to switch to **[pay-as-you-go usage](https://support.claude.com/en/articles/8114526-how-will-i-be-billed-for-claude-api-use)** with a Claude Console account for intensive coding sprints.
- Wait until your usage limits reset.

For more details on efficient usage, refer to our **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)**.

---

## Claude Code billing

#### Understanding two distinct systems

It's important to recognize these are separate systems:

- **Claude Code:** Presents options for continuing usage through API credits.
- **Claude Console / Claude API:** Contains optional auto-reload settings for API credit management where your terminal is located.

#### Choosing to use API credits

If you want to use API credits through Claude Code:

- Usage will be billed at **[standard API rates](https://claude.com/pricing#api)** (distinct from Max Plan pricing).
- If auto-reload is enabled in your Console account, additional credits will be automatically added when your balance runs low.

#### Staying within your plan

To maintain usage strictly within your Max Plan allocation:

- Decline the API credit option when presented.
- Allow your usage period to reset before continuing to use Claude Code.
- Monitor your remaining allocation using the /status command.

#### Opting out of API credits for Claude Code

If you prefer to prevent the API credit option from appearing entirely:

- Run `claude logout` in your terminal.
- Run `claude login` and authenticate using only your Max plan credentials.
- Avoid adding any Claude Console credentials during the login process.

This ensures Claude Code will only use your plan allocation and you won't be prompted to use API credits when you reach your limits.

#### Managing auto-reload settings

Auto-reload functionality is managed within your Claude Console account, not through Claude Code:

- Review your **[Console Billing settings](https://platform.claude.com/settings/billing)** to check auto-reload status.
- Adjust these settings in the Console if you prefer to avoid automatic credit purchases.
- Remember, auto-reload only applies when you've chosen to use API credits.

#### Summary

- Claude Code maintains strict user control over billing decisions.
- All transitions to API credit usage require explicit user consent.
- Auto-reload is an independent Claude Console feature.
- To maintain your Max plan budget, simply decline API credit options when offered.

## Related Articles
- [How do I pay for my Claude API usage?](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage)
- [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)
- [Manage extra usage for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-extra-usage-for-paid-claude-plans)
