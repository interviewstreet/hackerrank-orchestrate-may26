---
title: "Migrate your organization from Team to Enterprise"
title_slug: "migrate-your-organization-from-team-to-enterprise"
source_url: "https://support.claude.com/en/articles/13779868-migrate-your-organization-from-team-to-enterprise"
last_updated_iso: "2026-03-31T22:44:08Z"
article_id: "15935290"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Get started"
---

# Migrate your organization from Team to Enterprise

_Last updated: 2026-03-31T22:44:08Z_

When upgrading from a Team plan to an Enterprise plan, we recommend you keep the same Team organization and follow the upgrade path to change it to Enterprise. This way your data (memberships/roles, conversations and projects) and settings will be preserved. If a you create a brand new Enterprise organization, then you'll need to set up everything from scratch.

## What's retained (same organization upgrade)

- All chat history and conversations
- Projects and shared content
- User memberships and roles

## Migrate from Team to Enterprise

You can migrate from a Team plan to a self-serve Enterprise plan by following these steps:

1. Navigate to **[claude.ai/upgrade](https://claude.ai/upgrade)** and click "Get Enterprise plan."
2. When prompted, choose "Upgrade an existing organization" and select your Team plan organization.
3. Add the number of seats needed for all your team members (Enterprise organizations have a 20 seat minimum).
4. Set a per-user spend limit and a starting usage balance for the whole team.
5. Your payment information will be saved from previous Team plan payments, but you can click the pencil icon to change it if needed.
  1. We only support credit card payments for self-serve Enterprise plans. For more information, see **[Self-serve vs. sales-assisted Enterprise](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan#h_3058c781c5)**.
6. Review your order summary and click "Confirm upgrade."

> **Important:** Migrating an organization from Team to Enterprise via this pathway is not reversible; please ensure that an Enterprise plan is the right fit for your organization before initiating this change.

After upgrading to an Enterprise plan, we recommend reviewing your organization's settings to confirm all desired features and capabilities are enabled. Some features that are turned on by default on Team plans may be turned off by default on Enterprise plans, so it's worth checking that your configuration matches your preferences.

## Seat assignment

During migration, some users may appear as "Unassigned" rather than being automatically mapped to seat tiers. Admins should verify all users have correct seat assignments after the cutover.

For detailed guidance, refer to **[Purchasing and managing seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**.

## SSO and identity setup timeline

- **Domain verification (DNS):** Allow 24–48 hours for DNS changes to propagate globally, though many changes take effect within 10 minutes.
- **SCIM provisioning sync:** Microsoft Entra ID pushes changes approximately every 40 minutes. Okta syncs more frequently.

For detailed setup instructions, refer to **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** and **[Setting up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning).**

> **Note:** Once you turn on SSO, existing users will be forced to log out and log back in.

## Billing and usage configuration

For usage-based Enterprise plans, usage is billed based on actual consumption. For more detailed information, refer to **[How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**

If you had purchased extra usage for your Team plan, any unused credits will roll over and become available on your new usage-based Enterprise plan.

## Provisioning process

On the start date, you'll be provisioned and able to use the new features by the end of the day. After initial setup, Owners and Primary Owners can self-serve additional seats by navigating to **[Organization settings > Organization](https://claude.ai/admin-settings/organization)** and clicking "Manage" under **Total seats**.

## Helpful resources

- **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**
- **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**
- **[Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)**
- **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)**
- **[Enterprise billing information](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**
- **[Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)**

## Related Articles
- [Purchase and manage seats on Team plans](https://support.claude.com/en/articles/12004354-purchase-and-manage-seats-on-team-plans)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)
- [Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
