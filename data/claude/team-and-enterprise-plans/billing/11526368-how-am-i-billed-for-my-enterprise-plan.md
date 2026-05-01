---
title: "How am I billed for my Enterprise plan?"
title_slug: "how-am-i-billed-for-my-enterprise-plan"
source_url: "https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan"
last_updated_iso: "2026-04-07T18:55:44Z"
article_id: "12525220"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Billing"
---

# How am I billed for my Enterprise plan?

_Last updated: 2026-04-07T18:55:44Z_

Enterprise plan billing has two parts: a fixed seat fee and separate usage charges. The seat fee covers platform access. Usage is billed on top of that, based on what your team actually consumes.

How billing works depends on whether your organization is on a self-serve or sales-assisted Enterprise plan, and whether you're using the current single Enterprise seat or a legacy seat type. The sections below are organized by plan type—make sure you're reading the section that matches your setup. If you're unsure which plan type you're on, check with the person who set up your Enterprise account or contact your Anthropic account manager. Price and plans are subject to change at Anthropic's discretion.

> **Important: **The main sections of this article describe the current Enterprise seat billing model, which applies to all new Enterprise plans (excluding HIPAA-ready plans).
>
> - If your organization was provisioned before the transition to the single Enterprise seat and you see **Chat** and **Chat + Claude Code** seat types in **[Organization settings > Organization](https://claude.ai/admin-settings/organization)**, skip to the **[Chat and Chat + Claude Code seats section](#h_f6aa4f4dd2)**.
>   - **[HIPAA-ready Enterprise organizations](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)** are an exception: they are provisioned with separate Chat and Chat + Claude Code seat types and are not eligible for the single Enterprise seat billing model.
> - If your organization is on a seat-based plan with **Standard** and **Premium** seats, skip to the **[seat-based plans section](#h_3b87de90bd)**.
> - Chat-only seats and Standard/Premium seats are no longer available for new contracts—both legacy plan types are transitioning to the single Enterprise seat at their next renewal.

---

## Seat fees

All usage-based Enterprise plans (self-serve and sales-assisted) use the same seat pricing: **priced per user per month and billed annually**.

The seat fee gives each person access to Claude on web, desktop, and mobile, plus Claude Code and Cowork, but doesn't include any usage. Every token your team consumes is billed separately at standard API rates.

You're charged for the number of seats on your plan at the start of your annual billing cycle. If you add seats during your term, you're charged the prorated amount immediately for the remainder of the year.

**Example:** Your annual plan starts January 1 with 50 seats. You are charged upfront for the seats. On April 1, you add 10 seats. You'll be charged immediately for the remaining months.

> **Note:** Seats cannot be removed mid-term on self-serve Enterprise plans. For step-by-step instructions on purchasing, adding, and managing seats, see **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

---

## Usage billing

On usage-based Enterprise plans, usage is charged separately from your seat fee and is based on actual token consumption at standard API rates. For current per-model pricing, see our **[API pricing page](https://www.anthropic.com/pricing#api)**.

How and when you're billed for usage depends on your plan type:

#### Self-serve Enterprise

Usage is purchased **upfront in credits**. Your credits draw down as your team uses Claude and Claude Code. When your credits run out, usage stops until an Owner or Primary Owner purchases more. Self-serve Enterprise plans are billed in USD only. If your organization needs to pay in another currency, **[contact our Sales team](https://claude.com/contact-sales)** to set up a sales-assisted plan.

- After setup, Owners and Primary Owners can purchase additional credits at any time from **[Organization](https://claude.ai/admin-settings/organization)****[ settings > Usage](https://claude.ai/admin-settings/usage)**.
- All credits are shared across your organization — any team member can draw from the same pool.

#### Sales-assisted Enterprise

Usage is **billed monthly in arrears** based on your organization's actual consumption during each billing period. You'll receive a monthly invoice reflecting usage for that period. Speak with your account manager for questions about your usage invoices.

---

## How usage works across your team

Enterprise seats don't come with an individual token allowance. All usage across your organization is billed together at API rates, regardless of who consumed it.

What this looks like in practice depends on your plan type:

#### Self-serve Enterprise

Everyone's usage draws from the same credit balance. One person's heavy usage depletes credits faster for everyone, so monitoring and spend limits matter here. When the balance hits zero, usage stops for the whole organization until an Owner purchases more.

#### Sales-assisted Enterprise

There's no balance to deplete. Everyone's usage is metered and added to the same monthly invoice. One person's heavy usage doesn't block anyone else — it just increases what shows up on the bill. If you want a ceiling, set spend limits.

---

## Spend controls

Owners and Primary Owners can set spending caps to manage your organization's consumption. This applies to both self-serve and sales-assisted plans.

To configure spend controls, sign in as an Owner or Primary Owner and navigate to **[Organization](https://claude.ai/admin-settings/organization)****[ settings > Usage](https://claude.ai/admin-settings/usage)**.

You can set caps at two levels:

- **Organization level:** Maximum spend for all usage across your organization.
- **Individual level:** Maximum spend for a specific user.

These limits work hierarchically — a user cannot exceed their individual limit or the organization limit, whichever is lower.

On **self-serve plans**, spend caps work alongside your credit balance. If a user hits their individual cap or the organization cap, their usage will stop even if credits remain. Owners can adjust caps at any time.

On **sales-assisted plans**, spend caps prevent usage from continuing past the cap threshold. If a cap is reached, usage stops until the next billing period begins or an owner raises the limit.

**Owners can set limits to "unlimited,"** but consumption will still be billed. You cannot disable billing for usage — usage-based pricing is a core part of the Enterprise plan.

---

## Monitoring usage and spend

You can track your organization's usage and spending in a few places:

- **Organization** **settings > Usage:** View month-to-date spending for each member, current spend cap status, and credit balance (self-serve plans).
- **Monthly invoices:** Detailed usage per user for the billing period (sales-assisted plans).
- **Spend limit notifications:** Alerts when users or your organization approach configured spending thresholds.

---

## What happens when usage stops

If usage stops on your Enterprise plan, here's how to resume:

- **Self-serve plans:** If credits run out or a spend cap is reached, an Owner or Primary Owner can purchase additional credits or raise the spend cap from **[Organization](https://claude.ai/admin-settings/organization)****[ settings > Usage](https://claude.ai/admin-settings/usage)**.
- **Sales-assisted plans:** If a spend cap is reached, an Owner or Primary Owner can raise the cap, or usage will resume at the start of the next billing period. Contact your account manager with questions.

---

## Chat and Chat + Claude Code seats

> **Important:** Chat and Chat + Claude Code are legacy seat types that are no longer available for new Enterprise contracts. This section only applies to organizations that were provisioned with these seat types before the transition to the single Enterprise seat. If you recently signed a new Enterprise contract, the main sections of this article apply to you—your plan uses the single Enterprise seat.

Some existing usage-based Enterprise organizations currently have two seat types with different pricing. If you see **Chat** and **Chat + Claude Code** seats in **[Organization settings > Organization](https://claude.ai/admin-settings/organization)**, this section applies to you.

Seat fees are billed annually. Usage billing works the same way as described in the **[Usage billing section](#h_540cbc3861)** above: separately from seat fees, at API rates, and in arrears on sales-assisted plans.

#### Transition to the single Enterprise seat

> **Note:** **[HIPAA-ready organizations](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans)** are provisioned with separate Chat and Chat + Claude Code seat types and are not eligible for the unified seat type.

At your next contract renewal, your plan will automatically transition to the single Enterprise seat model. When that happens, all users — regardless of their current seat type — will move to the **Enterprise seat**. This seat includes Claude Code, Cowork, Chat and more.

If you have questions about your upcoming renewal, reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)**.

---

## Seat-based plans

> **Important:** Standard and Premium are legacy seat types that are no longer available for new Enterprise contracts. This section only applies to organizations that were provisioned with these seat types before the transition to usage-based billing. If you recently signed a new Enterprise contract, the main sections of this article apply to you.

Some Enterprise organizations are on older seat-based plans with **Standard** and **Premium** seats. These plans charge a flat monthly fee per seat that includes a usage allowance, which is a different model than the usage-based billing described above.

If you see "Standard" and "Premium" seats in **[Organization settings > Organization](https://claude.ai/admin-settings/organization)**, this section applies to you.

On seat-based plans, extra usage is available to allow team members to continue working after reaching their seat’s included limits. See **[Manage extra usage for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans)** for details on how extra usage works and how it's billed on your plan.

#### Transitioning to usage-based Enterprise

At your next contract renewal, your plan will transition to the usage-based single Enterprise seat model described in this article. If you'd like to migrate before your renewal, reach out to your Anthropic Contact or **[our Sales team](https://claude.com/contact-sales)**.

## Related Articles
- [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Manage extra usage for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-extra-usage-for-team-and-seat-based-enterprise-plans)
- [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
- [Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)
