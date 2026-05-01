---
title: "Use Skills in Claude"
title_slug: "use-skills-in-claude"
source_url: "https://support.claude.com/en/articles/12512180-use-skills-in-claude"
last_updated_iso: "2026-04-13T15:56:14Z"
article_id: "13961685"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Skills in Claude

_Last updated: 2026-04-13T15:56:14Z_

> Skills are available for users on Free, Pro, Max, Team, and Enterprise plans. This feature requires **[code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)**. Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

Skills extend Claude's capabilities by giving it access to specialized knowledge and workflows. This guide shows you how to enable, discover, and use Skills in Claude.

## Prerequisites

**For Enterprise plans:** Owners must first enable both **Code execution and file creation** and **Skills **in **[Organization settings > Skills](https://claude.ai/admin-settings/skills)**. Owners can also upload skills to provision them organization-wide—these skills automatically appear for all users. Once Skills are enabled at the organization level, individual members can toggle on example skills, access provisioned skills, and upload their own personal skills in **[Customize > Skills](https://claude.ai/customize/skills)**.

**For Team plans:** This feature is enabled by default at the organization level. Once enabled, individual members can toggle on example skills and upload their own in **[Customize > Skills](https://claude.ai/customize/skills)**.

**For Max, Pro, and Free plans:** You can enable example skills and upload your own in **[Customize > Skills](https://claude.ai/customize/skills)**.

---

## How to enable Skills

1. For Team / Enterprise plans: Navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** and ensure that both **Code execution and file creation** and **Skills** are enabled.
2. For individual Free, Pro, and Max plans: Navigate to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** and ensure that **Code execution and file creation** is enabled.
3. Go to **[Customize > Skills](https://claude.ai/customize/skills)**.
4. Toggle individual skills on or off as needed.

## Provision skills organization-wide

Owners of Team and Enterprise organizations can provision skills for all users. These skills appear in your individual Skills list with a team indicator—you can toggle them on or off based on your preferences. For information on provisioning skills for your organization, see **[Provision and manage Skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization#h_4dea113421)**.

## Use Anthropic Skills

Anthropic provides several built-in skills that are available to all users, including:

- Enhanced Excel spreadsheet creation and manipulation
- Professional Word document creation
- PowerPoint presentation generation
- PDF creation and processing

With **Code execution and file creation **on, Claude will automatically use these tools when relevant. You don't need to explicitly invoke them—Claude determines when each skill is needed based on your request.

For example, if you ask Claude to "Create a PowerPoint presentation about Q3 results," Claude will automatically use the PowerPoint skill if the capability is enabled.

## Add and use custom skills

You can also create and upload your own skills to teach Claude your specific workflows:

1. Create a skill following the skill structure (see **[How to create custom Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)** for detailed instructions).
2. Package your skill folder as a ZIP file.
3. Navigate to **[Customize > Skills](https://claude.ai/customize/skills)**.
4. To add custom skills, click the "+" button, then “+ Create skill.”
5. Select "Upload a skill.”
6. Upload a ZIP file containing your skill folder.
7. Your skill will appear in your Skills list and can be toggled on or off.

> **Note:** Custom skills you upload are private to your individual account. If you’re on a Team or Enterprise plan and want to share skills with your organization, see **[Provision skills for your organization](https://support.claude.com/en/articles/13119606-managing-skills-as-an-admin#h_4dea113421)**.

---

## Share a skill

On Team and Enterprise plans, you can share skills you've created with specific colleagues or with your entire organization. Skill sharing works in both chat and Cowork.

> **Note:** Sharing is off by default. An owner must navigate to **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** and enable the **Share with organization** toggle, the **Skill sharing** toggle, or both before the “Share” button appears. If you don't see the option to share, check with your organization owner.

To share a skill:

1. Navigate to[ **Customize > Skills**](https://claude.ai/customize/skills).
2. Open a skill you created.
3. Click "Share."
4. Choose who to share with:
  - **Specific people:** Enter names or emails to share directly. The skill appears in each recipient's skills list, grayed out until they enable it.
  - **Entire organization:** The skill is published to your organization's directory, where anyone can find and install it.
5. Click [placeholder: "Share" / "Done"].

Shared skills are view-only. Recipients can enable and use the skill, but they can't edit the contents. If you update the skill later, recipients automatically get the updated version.

## Use skills shared with you

On Team and Enterprise plans, your skills list in **[Customize > Skills](https://claude.ai/customize/skills)** is organized into three sections:

- **Personal skills:** Skills you've created or uploaded yourself.
- **Shared skills:** Skills colleagues have shared with you directly. These appear grayed out until you enable them.
- **Organization skills:** Skills shared org-wide and skills your owner has provisioned. You install these from the directory rather than enabling them from the list.

#### Enable a skill shared with you directly

1. Find the skill in the **Shared with you** section of your skills list.
2. Toggle it on.

You can toggle the skill off again at any time, or delete it from your list entirely if you don't want it.

#### Install a skill from your organization's directory

1. In Cowork, click **Customize** in the left sidebar, then click [placeholder: the "+" button] to open the directory.
2. Click the **Skills** tab.
3. Find the skill you want and click "Install."

Skills you install from the directory can be toggled off, which removes them from your sidebar. They remain in the directory so you can re-enable them later. For more on browsing the directory, see **[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)**.

---

## Use Skills in Excel and PowerPoint

Skills you've enabled in your Claude settings are also available in the Claude for Excel and Claude for PowerPoint add-ins. Claude applies relevant Skills automatically while you work—you don't need to invoke them separately.

**How triggering works in the add-ins:**

- Type `/` in the sidebar to see available Skills and select one (for example, `/debug` or `/deck-check`).
- Or describe your task naturally—Claude recognizes when a Skill applies and uses it.

Claude adapts skills to the surface it’s in. A research skill may produce a Word document in Cowork, but detailed data breakdowns in Excel.

Some skills may work better on one surface than others. If you let Claude work across apps, Claude can orchestrate another app to apply the skill.

If you build a Skill with a specific Excel or PowerPoint template, Claude for Excel and Powerpoint can load that template exactly into the current open file.

#### Instructions

Each add-in also has an **Instructions** field for persistent preferences — see **[Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-in-excel)** and **[Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-in-powerpoint)** for details.

---

## Manage your Skills

#### View your Skills

All your skills are listed in **[Customize > Skills](https://claude.ai/customize/skills)**. You can see:

- Anthropic skills (created, tested, and maintained by Anthropic)
- Custom skills you've uploaded
- When each skill was enabled or uploaded
- A brief description of what each skill does

#### Enable/disable your Skills

Toggle any skill on or off using the switch next to it. Disabled skills won't be available to Claude.

#### Delete custom Skills

To remove a custom skill you've uploaded:

1. Navigate to **[Customize > Skills](https://claude.ai/customize/skills)**.
2. Find the skill in your Skills list and click on it to view the details.
3. Use the toggle in the upper right corner to disable the skill.
4. To delete the custom skill entirely, click the "..." button next to the toggle, then select "Delete":

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2105391273/8359cbf8be20dce0f1cd3fd40e6f/CleanShot-2B2026-02-25-2Bat-2B15_50_16.png?expires=1776784500&signature=0ff3e73b0d9ed0aa7243fa2caf9958f63ab3f4a01b680834847474b0d6199152&req=diEnE8p3nINYWvMW1HO4zSOgAC0vyuKoH%2BdCnFXB0ujfHJLYTYfTA75mZ0Fm%0AJi8V%0A)
5. Click "Delete" in the confirmation prompt.

If you change your mind, you can add the skill again by re-uploading the file.

---

## Privacy and security details

For Team and Enterprise plans, organization owners can provision skills for all users through organization settings, and individuals can share skills with colleagues or organization-wide if an owner has enabled sharing. On all other plans, each person uploads skills to their own account.

Note that skills may include, or instruct Claude to install, third-party packages and software for Claude to use when completing a task. See **[our guidance on Claude's container environment](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1)** for details on Claude's container environment and **[the API documentation](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool#containers)** for API's container environment.

#### What are the primary risks of using Skills?

The most significant risks are prompt injection, which allows Claude to be manipulated to execute unintended actions, and data exfiltration, caused by malicious package code or prompt-injected data leaks. We’ve implemented several mitigations to these risks. Refer to **[our security considerations for code execution](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_0ee9d698a1)** for more information.

> **Important: **Only install skills only from trusted sources.

When installing a skill from a less-trusted source—including one shared by a colleague—review it before enabling. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

---

## Troubleshooting

#### Skills section not visible

Ensure code execution is enabled in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max) or **[Organization settings > Skills](https://claude.ai/admin-settings/skills)** (Team, Enterprise). Then navigate to **[Customize > Skills](https://claude.ai/customize/skills)** to access your skills. Skills require the code execution environment to function.

#### Claude isn’t using a Skill

- Verify the Skill is toggled on in **[Customize > Skills](https://claude.ai/customize/skills)**.
- Check that the Skill's description field clearly explains when it should be used.
- Ensure the Skill's instructions are clear and well-structured.
- Try being more explicit in your request (e.g., "Use my brand guidelines skill to create a presentation").

#### Upload errors

Common reasons for upload failures:

- ZIP file exceeds size limits
- Skill folder name doesn't match the skill name
- Missing required Skill.md file
- Invalid characters in skill name or description

#### Skills greyed out

If Skills appear greyed out, code execution may be disabled at the organization level (for Team and Enterprise plans) or individually. Check with your organization's Owner (Team, Enterprise) or make sure to enable code execution in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max).

#### Share button not visible

Skill sharing for Team and Enterprise plans is off by default. An organization owner must enable peer-to-peer or peer-to-org sharing before you can share skills. Contact your organization owner if you'd like sharing enabled.

---

## Best practices

**Start simple. **Begin with Anthropic's pre-built Skills to understand how they work before creating custom skills.

**Be specific. **Write clear descriptions when writing custom skills. A specific description tells Claude when to invoke your skill.

**Test your skills. **After uploading a custom skill, test it with a few different prompts to ensure it works as expected.

**Organize by purpose. **Create separate skills for different purposes rather than a single skill that’s meant to do everything.

---

## Learn more about using Skills

Refer to **[Teach Claude your way of working using Skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills)** for more information and video demonstrations.

## Related Articles
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Provision and manage Skills for your organization](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)
