---
title: "Work across Excel, PowerPoint, and Word"
title_slug: "work-across-excel-powerpoint-and-word"
source_url: "https://support.claude.com/en/articles/13892150-work-across-excel-powerpoint-and-word"
last_updated_iso: "2026-04-10T15:41:50Z"
article_id: "16135822"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Work across Excel, PowerPoint, and Word

_Last updated: 2026-04-10T15:41:50Z_

Claude can now work across apps to coordinate between the Excel, PowerPoint, and Word add-ins. Instead of switching between apps and providing context each time, Claude can read from one app and make changes in another. For example, you can ask Claude to analyze data in an Excel workbook, then create a presentation in PowerPoint using those results, without copying and pasting between apps.

## Requirements

- A paid Claude plan (Pro, Max, Team, or Enterprise)
- The Claude for Excel add-in installed from the Microsoft Marketplace
- The Claude for PowerPoint add-in installed from the Microsoft Marketplace
- The Claude for Word add-in installed from the Microsoft Marketplace

---

## Let Claude work across apps

#### 1. Install the add-ins

Get[ **Claude for Excel**](https://marketplace.microsoft.com/en-us/product/saas/wa200009404?tab=overview), **[Claude for PowerPoint](https://marketplace.microsoft.com/en-us/product/office/WA200010001?tab=Overview)**,** **and** Claude for Word **from the Microsoft Marketplace. Open each app and activate the add-in at least once before using the cross-app features.

#### 2. Toggle the setting on

> **Note:** If you're a member of a Team or Enterprise plan, an organization owner needs to go to **[Organization settings > Office agents](https://claude.ai/admin-settings/office-agents)** and toggle the **Let Claude work across apps** setting on before you can enable this capability individually.

Go to **Settings **in each of Claude for Excel and Powerpoint and toggle **Let Claude work across files** on:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152216540/23e9f22eca1109ec09f2c6138191/2ef697a8-3a60-4193-bbd7-639ed91b20e9?expires=1776784500&signature=d47e9bc3f5aa114c60c2c122849cb3945a0fd4d0bbf70d90f9a559267b31d877&req=diEiFMt%2Fm4RbWfMW1HO4ze%2BVW3LyWApaQEr1GSm7Lk2y3I5tbzZXoXAvujFB%0Awn1O8x%2F%2B6IWYLQDau8Y%3D%0A)

> **Note:** This setting is default on for Pro and Max plans and default off for Team and Enterprise plans.

You'll see connected file indicators when Excel, PowerPoint, or Word files are linked to your session:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152215013/db0cfd2aa4034975480d82218aad/8f11dc16-2173-4b34-a05a-e31a53b58cc2?expires=1776784500&signature=b72a14c15e5700beacad6983bac54aadc4b7e5ea304595656684d825d1dc8513&req=diEiFMt%2FmIFeWvMW1HO4zZtV0Wux09ZkGgi4PNaz7vV86iEBWzHa5uKQ2lCi%0AJ7jS5ntDUJLO2rEM7Zw%3D%0A)

##

---

## How it works

When you describe a task that involves multiple files or apps, Claude coordinates behind the scenes:

- Claude uses the Excel and PowerPoint add-ins to read from and write to open files.
- Context transfers between apps automatically, so you don't need to copy and paste information manually.

You stay in one place while Claude does the switching.

## What you can do

#### Read and write across open files

Claude can read data from an open Excel workbook, PowerPoint presentation, or Word document, and make changes to them directly. For example:

- Pull numbers from an Excel model into a PowerPoint slide or a Word memo.
- Update a chart in PowerPoint with the latest figures from Excel.
- Read content from a presentation and use it to populate a spreadsheet.
- Summarize a Word document into PowerPoint slides.
- Draft a Word memo using data from an Excel workbook.

#### Pass context between apps

When Claude works across multiple files in Excel, PowerPoint, and Word, it carries relevant context forward. If you've been building a financial model in Excel and ask Claude to create a summary deck or draft an investment memo, Claude already understands the model's structure and key outputs, so you don't need to re-explain.

---

## Skills work across apps too

Skills you've enabled in your Claude settings apply when Claude is working in Excel, PowerPoint, or Word during a cross-app task. If you have a Skill that enforces your team's modeling conventions in Excel and another that matches your slide template in PowerPoint, Claude uses each one in the right app as it moves through the workflow.

For more on how Skills work, see **[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).**

---

## Data handling

Inputs and outputs are automatically deleted from Anthropic's backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** The Claude for Excel, Claude for PowerPoint, and Claude for Word add-ins do not inherit custom data retention settings your organization may have set, and activity is not currently included in Enterprise audit logs, the Compliance API, or data exports. Chat history is not saved between sessions.

#### For admins who want to manage access

Team and Enterprise organization owners can control whether team members can access this capability:

1. Go to **[Organization settings > Office agents](https://claude.ai/admin-settings/office-agents)**
2. Toggle **Let Claude work across apps** on or off.

Admins can also manage member access to the Claude for Excel, PowerPoint, and Word add-ins through the **[Microsoft 365 Admin Center](https://admin.microsoft.com)**.

---

## Current limitations

- Claude can only read from and write to files that are currently open in Excel, PowerPoint, or Word.
- Claude cannot create, open, close, or switch files directly from the add-ins—the files and add-ins must be open with the feature turned on.
- Chat history for cross-app sessions is not saved between sessions.

---

## Troubleshooting

#### Claude doesn't see my open file

Make sure the add-in is activated in the app (**Tools > Add-ins** on Mac or **Home > Add-ins** on Windows) and that working across apps is turned on in Claude Desktop settings.

#### Changes aren't appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its current action, then check the target file. You may need to ask Claude to refresh or re-read the file.

## Related Articles
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
