---
title: "Purchase and manage seats on Team plans"
title_slug: "purchase-and-manage-seats-on-team-plans"
source_url: "https://support.claude.com/en/articles/12004354-purchase-and-manage-seats-on-team-plans"
last_updated_iso: "2026-03-16T20:37:43Z"
article_id: "13254584"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Admin management"
---

# Purchase and manage seats on Team plans

_Last updated: 2026-03-16T20:37:43Z_

Seat management allows Team plan owners to control their organization's seat allocation, assign users to different seat types, and manage billing. For pricing and billing details, see **[How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)**

> **Permissions note:** Only Owners and Primary Owners can purchase seats and access **[Organization settings > Billing](https://claude.ai/admin-settings/billing)**. Admins and above can reassign seat types for members in **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.

For information on adding and removing members from your organization, see **[Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

---

## Understanding seat types

Team plans offer two seat types:

Organizations can mix and match seat types based on team needs. Assign Premium seats to power users who need more capacity, while keeping other team members on Standard seats.

Your plan has a total seat allocation (e.g., 30 Standard seats and 10 Premium seats). Within that allocation, you can assign and reassign users to different seat types as needed.

---

## Purchasing new seats

> **Important:** If you want to upgrade an existing member from Standard to Premium, you don't need to purchase a new seat. Use the seat tier reassignment in **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)** instead — see **[Upgrading a Standard seat to Premium](#h_e7a7f4f396)** below.

Follow these steps to add seats to your plan's total allocation:

1. Log in with your Owner or Primary Owner account.
2. Navigate to **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.
3. Click "Manage" under "Total seats."
4. In the "Seat breakdown" modal, click "Add or change seats."
5. Click the "**+**" next to the seat type you want to add (Standard or Premium).
6. Click "Next" to review your purchase details and confirm the billing impact.
7. Check the confirmation box before continuing.
8. Click "Confirm & purchase" to complete the transaction.

> **Note:** You can also purchase seats while adding a new member. If you don't have an available seat of the selected type, you'll be prompted to purchase one.

---

## Reducing your seat allocation

You can reduce the total number of seats on your Team plan:

1. Log in with your Owner or Primary Owner account.
2. Navigate to **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.
3. If needed, remove members or reassign them to free up the seats you want to eliminate.
4. Click “Manage” under **Total seats**.
5. Click “Add or change seats” in the **Seat breakdown** modal.
6. Click the "**-**" next to the seat type you want to reduce.
7. Click “Next” to review the changes.
8. Check the confirmation box and click "Confirm & purchase" to complete the change.

---

## Assigning and reassigning seat types

You can move users between Standard and Premium seats within your existing allocation.

To reassign a user's seat type:

1. Go to **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.
2. Find the member you want to reassign.
3. Click the dropdown under **Seat Tier**.
4. Select Standard or Premium.

Members moved from Premium to Standard will have lower usage limits, and vice versa.

## Upgrading a Standard seat to Premium

Upgrading a member from Standard to Premium is a reassignment, not a new purchase. You don't need to buy an additional seat unless your Premium allocation is already full.

1. Go to **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.

2. Find the member assigned to a Standard seat you want to upgrade.

3. Click the dropdown under **Seat Tier**.

4. Select "Premium."

If you have no available Premium seats, you'll be prompted to purchase one at this point.

The upgrade is prorated based on your billing cycle, and you'll be charged the price difference immediately.

#### What if I don't have an available seat?

If you try to reassign a user to Premium but don't have any available Premium seats, you'll then be prompted to purchase an additional Premium seat.

## Using "unassigned" to swap users between seat types

The unassigned option allows you to temporarily remove a user from a seat without removing them from your organization. This is useful when you need to swap people between seat types within your existing allocation.

**Example:** You have five Premium seats, all assigned. You want to move User A (currently on Premium) to Standard, and move User B (currently on Standard) to Premium—without purchasing an additional seat.

1. Go to **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.
2. Find User A and change their seat tier to "Unassigned." This frees up one Premium seat.
3. Find User B and change their seat tier to "Premium." They now occupy the available Premium seat.
4. Find User A and change their seat tier to "Standard."

> **Note:** Unassigned users remain members of your organization but cannot use Claude until they're assigned to a seat.

## Seat assignment with JIT or SCIM provisioning

**[Users provisioned via JIT or SCIM](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning-to-manage-user-assignments-on-team-or-enterprise-plans)** are automatically assigned to the highest-available seat type when they're added. Admins and above can manually reassign seat types afterward in **[Organization](https://claude.ai/admin-settings/billing)[ settings > Organization](https://claude.ai/admin-settings/organization)**.

You can also enable group mappings with JIT or SCIM to provision users directly to a specific seat type.

---

## Understanding billing

- **New seats** are prorated based on your billing cycle and charged immediately.
- **Seat type upgrades** (Standard → Premium) are prorated and charged immediately for the price difference.
- **Removing members** does not trigger an immediate credit or refund. The seat becomes available to assign to another member. To reduce your bill, you'll need to reduce your plan's total seat allocation.

For detailed billing calculations and examples, see **[How is my Team plan bill calculated?](https://support.claude.com/en/articles/9267289-how-is-my-team-plan-bill-calculated)**

## Related Articles
- [What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Manage extra usage for Team and seat-based Enterprise plans](https://support.claude.com/en/articles/12005970-manage-extra-usage-for-team-and-seat-based-enterprise-plans)
- [Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)
- [Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)
