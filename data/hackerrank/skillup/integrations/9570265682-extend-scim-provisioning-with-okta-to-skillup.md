---
title: "Extend SCIM Provisioning with Okta to SkillUp Prerequisites Updating attribute mappings for SkillUp How SCIM provisioning works"
title_slug: "extend-scim-provisioning-with-okta-to-skillup-prerequisites-updating-attribute-mappings-for-skillup-how-scim-provisioning-works"
source_url: "https://support.hackerrank.com/articles/9570265682-extend-scim-provisioning-with-okta-to-skillup"
article_slug: "9570265682-extend-scim-provisioning-with-okta-to-skillup"
last_updated_exact: "Nov 5, 2025, 9:52 PM"
last_updated_relative: "Last updated 6 months ago"
breadcrumbs:
  - "SkillUp"
  - "Integrations"
---

# Extend SCIM Provisioning with Okta to SkillUp Prerequisites Updating attribute mappings for SkillUp How SCIM provisioning works

_Last updated: Nov 5, 2025, 9:52 PM (Last updated 6 months ago)_

SkillUp supports SCIM-based provisioning with Okta to automatically synchronize users, roles, and profile attributes. SkillUp and HackerRank for Work share the same SCIM endpoint and authentication mechanism. 

If you have not configured SCIM provisioning with Okta for HackerRank for Work, follow the [Setting Up SCIM Provisioning with Okta for HackerRank for Work](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta) article first.

If your organization already uses [SCIM provisioning with Okta for HackerRank for Work](https://support.hackerrank.com/articles/3939437783-setting-up-scim-provisioning-with-okta), you can extend the existing integration to include SkillUp users. You only need to update the attribute mappings in Okta to enable provisioning for SkillUp.

This article explains how to extend your HackerRank for Work–Okta integration to manage SkillUp users.

# Prerequisites

Ensure that **SAML-based SSO** is already configured in HackerRank for Work. For more information, see [📄 Configure Single Sign-On (SSO) for SkillUp](/articles/7581923631).

# Updating attribute mappings for SkillUp

To extend your existing HackerRank for Work–Okta integration to manage SkillUp users:

1.  Log in to the **Okta Admin Console**.

2.  Go to **Applications \> HackerRank for Work**.

    ![skillup.1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1762352880856-skillup.1.png?Expires=253370764800&Signature=BtRq6c8bA9V3s92DBv~KupNs05GCILO82XSezijTP6tXemL0~NPBA225T2KH3HUmIwdi9bkS85giV8bBdyw-RtCbOFIN4ZblXUBocjs9ccgQHNjd4KTzbt2M-xgHnU~LgvoNoUuayYHQPIlKM6nOUc-UpJdSqsr2uPDMfAj5ITvKUAJNzKmxz7JsxXaTyh0WQPcg9yiNEq-dff1JYUFJK2Gzk9kI3QL~uSgs1l1AHf2nL9j9bMymtKv7jn6WvCbfyhYvyceXtCkKsWzUeH8zN32Jzre7rWWoIdBs3pQSnJDrmn8Z0A2WgFDDO9eQU0UXzsw94LeIjst8-AYYEfUT3A__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select the **Provisioning** tab.

4.  Update the mappings to include SkillUp-specific attributes.

    ![skillup1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1762352905245-skillup1.png?Expires=253370764800&Signature=F6NeMV7n1Ddf3ppjENQJo0fhn3uuOLumeEBD4BOQYMZulMntrTHTx8-Y~ESFC1I94TiKArHyUkpRED3f-sk04WlOMBKsiO4PzjfIN7GsocH1Mu6uJNlU-uTa6u1tCN2XURp9QMn1Tc7pd08MdCEeE6S74hA626~LVzJ65zVwRpoUqEP0H8lXtb~ymhi4UFhljY5DpcxHi8awKM38SK5KL0eFduwAb0k5i7eCY01HUxhKG9q-qsa-8JC~3vBkC0gevQcpE2Z-smUA6Om~VESm0WftubeH9CNGkLr3Acx0MO4JTAGkEAsW6trdomwKGn5GqXPeNtpC9CXLrFA1D97r-Q__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  **Modify existing attributes:** Mark the following attributes as **Not Required**:

        - `Role`

        - `Company Admin`

        - `Team Admin`

    2.  **Add SkillUp attributes:** Use the following table to add new SkillUp attributes.

        <table style="width:100%;">
        <colgroup>
        <col style="width: 16%" />
        <col style="width: 16%" />
        <col style="width: 16%" />
        <col style="width: 16%" />
        <col style="width: 16%" />
        <col style="width: 16%" />
        </colgroup>
        <tbody>
        <tr>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Display Name</strong></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Variable Name</strong></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Data Type</strong></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Required</strong></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Attribute Type</strong></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1" data-background-color="green" style="background-color: #D1FAE5"><p><strong>Description</strong></p>
        <p><br />
        </p></td>
        </tr>
        <tr>
        <td data-colspan="1" data-rowspan="1"><p>Job Title</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p><code>job_title</code></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>string</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Yes</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Personal</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Maps to the user’s job title in Okta</p></td>
        </tr>
        <tr>
        <td data-colspan="1" data-rowspan="1"><p>Manager Email</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p><code>manager_email</code></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>string</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Conditional</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Personal</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Maps to the manager’s email in Okta</p></td>
        </tr>
        <tr>
        <td data-colspan="1" data-rowspan="1"><p>SkillUp Role</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p><code>skillup_role</code></p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>string (enum)</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Yes</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Group</p>
        <p><br />
        </p></td>
        <td data-colspan="1" data-rowspan="1"><p>Defines the user’s access level in SkillUp</p></td>
        </tr>
        </tbody>
        </table>

Use the namespace `urn:ietf:params:scim:schemas:core:2.0:User` for all new attributes.

## Allowed values for SkillUp role

|                  |              |
|------------------|--------------|
| **Display Name** | **Value**    |
| Individual       | `individual` |
| Manager          | `manager`    |
| Admin            | `admin`      |

**Note:**

- `job_title` and `skillUp_role` are mandatory for all SkillUp users.

- `manager_email` is mandatory for users with the `Individual` role.

- To exclude a user from SkillUp provisioning, leave all SkillUp-specific attributes (`manager_email`, `job_title`, `skillup_role`) blank.

# How SCIM provisioning works

After you update the attribute mappings, Okta automatically provisions SkillUp users using the same SCIM configuration as HackerRank for Work.

- When you assign a user to the HackerRank for Work application in Okta, SkillUp automatically creates or updates their profile based on the assigned SkillUp Role. 

- Attribute updates, such as job title, manager email, or skill-up role, synchronize in real-time.

- When you deprovision a user in Okta, SkillUp automatically deactivates their account.

For more information on supported provisioning actions such as Push New Users, Push Profile Updates, and Import Users, see [📄 Setting Up SCIM Provisioning with Okta](/articles/3939437783).

**Note:**

- Use Okta as the system of record for user data and roles.

- Verify that required attributes ( `email`, `givenName`, `familyName`) are mapped correctly.

- If provisioning fails:

  - Confirm that the API key is valid.

  - Check that attribute names and namespaces match exactly.

  - Ensure that the HRW SCIM integration is active.

\
