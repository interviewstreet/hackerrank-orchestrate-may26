---
title: "Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning"
title_slug: "important-considerations-before-enabling-single-sign-on-sso-and-jitscim-provisioning"
source_url: "https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning"
last_updated_iso: "2026-04-10T23:30:07Z"
article_id: "10859428"
breadcrumbs:
  - "Identity management (SSO, JIT, SCIM)"
---

# Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning

_Last updated: 2026-04-10T23:30:07Z_

Before setting up SSO for your Claude or Claude Console organization, review this guide to understand key concepts, plan your approach, and complete any prerequisite steps.

## Understanding parent organizations

Our single sign-on feature uses the concept of a "parent organization." This is an entity that stores SSO settings that can be shared across multiple Claude or Console organizations. Your plan type determines whether or not you have a parent organization by default:

#### Key things to know

- **Domain verification is required before you can configure SSO.** Domains are verified at the parent organization level—once verified, other parent organizations cannot claim the same domain.
- **Multiple organizations can be linked to the same parent organization** to share domain verification and SSO configuration. This is useful if you have both Claude (Team/Enterprise plans) and Console organizations.
- **Each parent organization can only be linked to one Identity Provider. **This means that every organization linked to a single parent organization must be managed through the same IdP.
- **Enabling group mappings** allows you to control which users are provisioned to which organizations under your parent, and with which roles. See **[Configure groups and assign users in your IdP](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning#h_0178209cfa)** for details.
- **Parent organizations manage identity and access only**—specifically, domain verification, SSO configuration, and user provisioning. Billing, invoicing, and usage tracking are handled at the individual organization level and aren't affected by parent organization relationships.

#### What this means for you

You will need to check the parent organization dynamic depending on your plan:

- **If you have a Team or Enterprise plan:** You can proceed directly to the **[Setting up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)** guide. Your parent organization is already in place (or will be created when you enable SSO for Team plans).
- **If you have a Claude Console organization and an existing Team or Enterprise plan:** Your Console organization may already be linked to your Team or Enterprise parent organization. Check if you can access **[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**. If so, this indicates that the org is linked to the parent organization and SSO is already configured. If not, an Owner on your Team or Enterprise plan can initiate a merge to link your Console organization (see **[Merge organizations](#h_3bad8701c8)** below) to their parent organization and the existing SSO configuration.
- **If you have a Claude Console organization without a Team or Enterprise plan:** **[Contact our Sales team](https://claude.com/contact-sales)** to request a parent organization for your Console account. Once we create your parent organization, you will see the Identity settings page in Claude Console and can proceed with SSO setup.

---

## Merge organizations

Team or Enterprise organizations can invite other orgs to join an existing parent organization and share SSO configuration.

> **Important:** The **Merge Organizations** option is only available on Claude (claude.ai). Console organizations cannot initiate a merge—they must be invited by a Team or Enterprise organization.

#### Requirements for merging

- The Team or Enterprise organization initiating the proposal must have verified domains in their parent organization.
- All members in the organization being invited must have email addresses matching those verified domains.
- An Admin (Console) or Owner (Claude) for the invited organization needs to approve the merge.

#### To initiate a merge proposal

1. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.
2. Click "Invite" under **Merge Organizations**.
3. Select the organization you want to invite and click "Next."
4. Review the member count and click "Invite."
5. The merge proposal will be sent to the invited organization's Admins/Owners, with the email subject “*Parent Organization Update: New Member Organization Proposed*,” and must be approved within 14 days.

> **Note:** If the person initiating the merge is also an Admin/Owner in the invited organization, only one approval is required.

#### To approve a merge proposal

An organization Owner or Primary Owner needs to go to **[claude.ai/settings/join-proposal](https://claude.ai/settings/join-proposal)** to accept the merge.

Once a Console organization is merged, it will gain access to the **[Identity and access page](http://platform.claude.com/settings/identity)**, in the Organization settings, to configure SSO and provisioning settings.

---

## Global access settings

You'll find settings you can use to configure SSO in the **Global access settings** section. This is where you configure the primary SSO connection and policies that apply across multiple joined Claude or Console organizations. While some settings in this section apply to all Claude and Console organizations that have joined the parent organization, those with a "This org only" label apply only to the specific organization you're currently viewing. This allows you to enable organization-specific features like group mappings.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2136628437/d6bd859fe6590fb3d9075e4ecd82/image.png?expires=1776784500&signature=5246db6b8c3c63c8df107711e0e0da1c3aefb7ab275eb4c195168fd2f07dfa6a&req=diEkEM98lYVcXvMW1HO4zbFPn2EuI2YvZ%2FwOXT%2BR2c0lD%2Brnb4SDZGM4Imlr%0AkHwKPdsn3BDRX%2FJkwXM%3D%0A)

---

## Restrict new organization creation

Once your organization's domains are verified, owners will see a **Restrict organization creation** toggle under **Security** on the Organization and access page. Toggle this on to prevent users from creating new Claude or Console organizations—including personal accounts—using any of your verified domains.

---

## Provisioning options

Once SSO is configured, you can choose how users are provisioned to your organization.

> ***Note:** Only Enterprise plan organizations can enable SCIM provisioning; if a Console organization is merged with a Team plan’s parent org, it will not have access to SCIM provisioning.

For detailed information on how each provisioning method works, see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)**.

---

## What happens to existing users when SSO is enabled

After enabling SSO for your organization, there are two distinct scenarios to consider for users who have individual accounts associated with your verified company domain:

#### Users with existing free/Pro/Team/Max accounts who ARE added to your SSO application

These users will maintain access to their existing free/Pro/Team/Max accounts. They will have the ability to toggle between the Team or Enterprise plan account and their previous accounts by clicking the profile icon with their initials in the bottom left corner.

#### Users with existing free/Pro/Team/Max accounts who are NOT added to your SSO application

- **If "Require SSO for Claude" is NOT enabled:** These users can still access their existing accounts using the "Continue with email" option.
- **If "Require SSO for Claude" IS enabled:** These users will be unable to access their existing free/Pro/Team/Max accounts. Please note that these accounts are not deleted, but will be inaccessible as users are unable to log in via SSO.

---

## How to view existing Claude / Console accounts associated with your verified domain

To view or download information about your verified domains and their usage across Claude organizations:

1. Navigate to the Organization and access section in Claude (**[claude.ai/admin-settings/organization](https://claude.ai/admin-settings/organization)**) or the Identity and access section in Console (**[platform.claude.com/settings/identity](http://platform.claude.com/settings/identity)**).
2. Click “Domain memberships” in the **Domains **section.
3. Review the information or download details in CSV or JSON format.

---

## Recommended steps before implementing SSO

#### Communicate clearly with your team

- Notify all employees about the upcoming migration to SSO.
- Provide a clear timeline for when the change will occur.
- Advise employees who won't be added to the SSO application to save or **[export their conversation history](https://support.claude.com/en/articles/9450526-how-can-i-export-my-claude-data)** if SSO will be enforced.

#### Plan for a smooth transition

- Schedule the SSO implementation during a time that minimizes disruption.
- Ensure your IT team is prepared to support employees with the transition.
- Have a clear process in place for granting access to authorized users.
- If possible, implement both SSO and provisioning features at the same time.

Taking time to test, communicate, and plan before enabling domain capture and SSO will help ensure a successful transition and positive experience for your organization.

---

## Next steps

Once you've reviewed these considerations and completed any necessary prerequisite steps (such as merging organizations), proceed to **[Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)** for detailed implementation instructions.

## Related Articles
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Switching to a different Identity Provider (IdP)](https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp)
- [SSO login](https://support.claude.com/en/articles/14503613-sso-login)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
