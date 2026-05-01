---
title: "Use Claude for PowerPoint"
title_slug: "use-claude-for-powerpoint"
source_url: "https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint"
last_updated_iso: "2026-04-16T13:46:28Z"
article_id: "15504285"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Claude for PowerPoint

_Last updated: 2026-04-16T13:46:28Z_

> Claude for PowerPoint is currently a beta in research preview and available to Pro, Max, Team, and Enterprise plans.

Claude for PowerPoint is an add-in that integrates Claude into your PowerPoint workflow. It's designed for professionals who build presentations, particularly those who spend significant time creating and refining slide decks.

With Claude for PowerPoint, you can:

- Build new slides using your existing client or corporate templates
- Make pinpoint edits to specific slides without regenerating entire decks
- Generate full deck structures from natural language descriptions
- Convert bullets into professional diagrams and native PowerPoint charts
- Use connectors to bring context from your other tools directly into your slides
- Iterate on feedback quickly while preserving formatting and template compliance

---

## Get started with Claude for PowerPoint

#### Supported versions

- PowerPoint on the web
- PowerPoint on Windows (Microsoft 365 subscription, build 16.0.13127.20296+)
- PowerPoint on Mac (version 16.46+)

#### For individuals

1. Navigate to the **[Claude for PowerPoint listing on Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/office/WA200010001?tab=Overview)**.
2. Click "Get it now" to install the add-in.
3. Open PowerPoint, activate the add-in, and sign in with your Claude account.

#### For admins

**Deploy Claude for PowerPoint to your organization:**

1. Visit the **[Microsoft 365 Admin Center](https://admin.microsoft.com/)**.
2. Navigate to **Settings > Org Settings > User owned apps and services** and ensure that **[“Let users access the Office Store"](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center?view=o365-worldwide#manage-add-in-downloads-by-turning-onoff-microsoft-marketplace-across-all-apps-except-outlook)** is toggled on.
3. Navigate to **Settings > Integrated apps > Add-ins**.
4. Search for "Claude by Anthropic in PowerPoint" in Microsoft AppSource.
5. Deploy the add-in to your organization or specific users.
6. Share these instructions with your team: **[Microsoft's deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide)**.

After installation, team members can open PowerPoint, activate the Claude add-in (from **Tools > Add-ins** on Mac or **Home > Add-ins** on Windows), sign in with their Claude credentials, and start working with their presentations.

> **Important:** Organizations that have disabled "Let users access the Office Store" may find that admin-deployed add-ins don't appear for users. To work around this, deploy using the manifest XML files provided below.

For IT administrators deploying to multiple users:

#### Step 1: Obtain the custom manifest

1. Click **[this link](https://pivot.claude.ai/manifest-powerpoint.xml)** to download the custom manifest XML file.
2. Save this file to a secure location.

#### Step 2: Access Microsoft 365 Admin Center

1. Navigate to **[https://admin.microsoft.com](https://admin.microsoft.com)**
2. Sign in with your admin credentials.
3. Go to **Settings** > **Integrated apps.**

#### Step 3: Upload the custom add-in

1. Click "Upload custom apps"
2. Select "Office Add-in."
3. Choose "I have a manifest file on this device."
4. Browse and select the Claude for PowerPoint manifest XML file.
5. Click "Upload."

#### Step 4: Assign users

Choose your deployment scope:

- **Entire organization**: All users get access
- **Specific users**: Enter individual email addresses
- **Specific groups**: Select security groups or distribution lists
- **Just yourself**: For admin testing only

#### Step 5: Deploy

1. Review deployment settings.
2. Click "Deploy."
3. Add-in will be available within minutes (may take up to 24 hours for full organization rollout).

#### Step 6: User access

- Users will see Claude appear in PowerPoint's Home ribbon.
- First-time users will need to sign in with their Claude accounts
- No additional installation required by users.

#### Connect through an LLM gateway

If your organization routes API traffic through an internal LLM gateway connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the add-in without a Claude account. This is the same gateway pattern used by Claude Code.

For setup instructions and gateway requirements, see **[Use Claude for Excel and PowerPoint with an LLM gateway](https://support.claude.com/en/articles/13945233-use-claude-in-excel-and-powerpoint-with-an-llm-gateway)**.

---

## Key features

#### Build from templates

Start with a client or corporate template already loaded. Describe what you need, and Claude generates slides using the correct layouts, fonts, and colors from the slide master. Claude reads your deck's template and respects its formatting rules.

**Example prompts:**

- "Create a market sizing section—3 slides covering TAM, SAM, SOM with supporting visuals"
- "Add an executive summary slide using the one-column content layout"

#### Edit existing slides

Select a slide and tell Claude what to change. Claude makes edits while preserving your formatting and surrounding context.

**Example prompts:**

- "Simplify the text on this slide"
- "Add a chart showing the quarterly trend"
- "Restructure the storyline across slides 4-7"

#### Generate full decks

Open a blank deck and describe your goal. Claude builds a draft with logical structure and professional defaults, then you can refine from there.

**Example prompts:**

- "Create a 10-slide deck walking through our market entry hypotheses"
- "Build an internal project update presentation with timeline and next steps"

#### Create native charts and diagrams

Convert bullet points into professional visuals—diagrams, process flows, or editable native PowerPoint charts. Claude produces visuals you can edit directly, not static images.

**Example prompts:**

- "Turn these bullets into a process flow diagram"
- "Create a bar chart comparing Q1-Q4 performance"

#### Template awareness

Claude reads the slide master, layouts, fonts, and color scheme in your deck and uses them when generating or editing slides. It aims to maintain template compliance without introducing off-brand elements.

#### Support for connectors

Connect your other tools to give Claude context beyond what's in your deck. With connectors enabled, Claude can draw on information from your connected tools when generating or refining content.

To connect a tool, open the Claude sidebar and select the connectors icon to see available options.

Custom connectors can introduce security risks. Before enabling them, review **[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp#h_b79c05dfcd)** for guidance on what to consider.

#### Use Skills in PowerPoint

Skills you've enabled in your Claude settings are also available in the Claude for PowerPoint add-in. Claude applies relevant Skills automatically while you work—you don't need to invoke them separately.

You can also type `/` in the sidebar to see available Skills and select one directly (for example, `/deck-check`). Skills that aren't relevant to PowerPoint are excluded from this list.

To learn more about enabling and managing Skills, see **[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)**.

#### Set persistent instructions

Use the **Instructions** field in the add-in sidebar to set preferences that apply to every conversation in PowerPoint. Instructions are useful for things like brand guidelines (for example, "always use one-line bullets" or "use the blue accent color for highlights"), preferred slide structure, or recurring context Claude should know about your workflow.

Instructions you set in PowerPoint only apply to PowerPoint — they're separate from any Instructions you set in Excel.

---

## Context and session management

- **Auto-compaction**: We **[automatically compact longer conversations](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits#h_21b66a43b4)** into new conversations to avoid running out of context.
- **Overwrite protection**: To avoid accidental data loss, Claude warns you before overwriting existing data.

> **Note:** Your use of Claude for PowerPoint is associated with your existing Claude account and is subject to the same usage limits.

---

## Current limitations

For Claude for Powerpoint use, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) **Data will be deleted after 30 days, but will be cached for a number of hours so users can access context in recently closed out documents.

This is unlike our other commercial products (Team and Enterprise plans) that allow you to save and continue conversations with Claude. Chat history is not saved between sessions.

Currently, observability and audibility are not available with this feature. Claude for PowerPoint does not inherit custom data retention settings your organization might have set, and isn't included in Enterprise audit logs or the Compliance API at this time.

As a beta feature, Claude for PowerPoint is **not recommended** for:

- Final client deliverables without human review
- Presentations containing highly sensitive or regulated data without proper controls
- Replacing your judgment on design and narrative flow

#### Unsupported versions

- PowerPoint 2016 / 2019 (perpetual/volume license)
- PowerPoint on iPad
- PowerPoint on Android
- Older builds of Microsoft 365 PowerPoint below the SharedRuntime threshold

---

## Best practices

To use Claude for PowerPoint safely and effectively:

- Always review changes before finalizing your work
- Start with your template already applied before asking Claude to generate content.
- Be specific about what you want changed—Claude can target individual slides or elements.
- Verify that outputs match your organization's brand guidelines.

---

## Prompt injection attack risks

Only use Claude for PowerPoint with trusted files and not files from external untrusted sources (for example, downloaded templates, vendor files, collaborative documents, and data imports).

An important risk that users of Claude for PowerPoint and other AI tools that can read and manipulate files is prompt injection attacks that hide malicious instructions in file content to trick the AI models into taking unintended actions. For example, a seemingly innocent template or data file received from an external party or downloaded from the internet might contain hidden instructions to "export all financial data to this external URL" or "modify these financial records." Claude may interpret these malicious instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude for PowerPoint can be manipulated to:

- **Extract and share sensitive information **with bad actors through web searches containing your sensitive data or file system access that exposes proprietary information.
- **Modify critical data** such as financial records.
- **Perform destructive actions **without verification (should you allow Claude to act without verifying its actions), exploiting Claude's helpful nature to delete or corrupt important data across multiple slides.

While we continue to develop our offerings and improve safety measures to reduce these risks, users should exercise caution when using Claude for PowerPoint and should not use it with files from external, untrusted sources.

---

## Example use cases

#### Consulting deliverables

- "Build a market sizing section with TAM, SAM, SOM slides"
- "Create a competitive landscape slide comparing 4 players"
- “Summarize these survey results”

#### Iterative refinement

- "Simplify the text on slide 3—it's too dense"
- "Combine slides 5 and 6 into a single summary"
- "Make the recommendations section more visual"

#### Data visualization

- "Convert these bullet points into a process flow"
- "Create a bar chart from this data table"
- "Add a pie chart showing market share breakdown"

#### Deck restructuring

- "Reorder slides to lead with recommendations first"
- "Add transition slides between each major section"
- "Create an agenda slide that reflects the current structure"

---

## Frequently asked questions

#### Which models are available when using Claude for PowerPoint?

You can switch between Opus 4.7, Opus 4.6, and Sonnet 4.6 when using Claude for PowerPoint.

#### Does Claude understand my template?

Yes. Claude reads the slide master, layouts, fonts, and color scheme in your deck and uses them when generating or editing slides. It aims to maintain template compliance, though you should always review output for complex templates.

#### Can I use Claude for PowerPoint with sensitive data?

Claude for PowerPoint works within your existing security framework. For highly sensitive or regulated data, ensure you follow your organization's data handling policies.

#### What happens to my chat history?

Currently, chat history is not saved between sessions. Each time you open the add-in, you start a fresh conversation with Claude.

#### How does Claude access my presentation?

Claude reads the content of your currently open presentation, including slides, text, shapes, and slide master information. It can only access the presentation you have open in PowerPoint.

#### What if Claude makes a mistake?

Review Claude's changes carefully before saving or sharing your file. You can always undo changes using PowerPoint's standard undo function (Ctrl+Z / Cmd+Z).

## Related Articles
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Work across Excel, PowerPoint, and Word](https://support.claude.com/en/articles/13892150-work-across-excel-powerpoint-and-word)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
