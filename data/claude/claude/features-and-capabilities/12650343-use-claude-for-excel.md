---
title: "Use Claude for Excel"
title_slug: "use-claude-for-excel"
source_url: "https://support.claude.com/en/articles/12650343-use-claude-for-excel"
last_updated_iso: "2026-04-16T13:44:13Z"
article_id: "14205991"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Claude for Excel

_Last updated: 2026-04-16T13:44:13Z_

> Claude for Excel is currently in beta and available to Pro, Max, Team, and Enterprise plans.

Claude for Excel is an add-in that integrates Claude into your Excel workflow. It's designed for professionals who work extensively with spreadsheets, particularly in financial analysis and modeling.

With Claude for Excel, you can:

- Ask questions about your workbook and get answers with cell-level citations
- Update assumptions while preserving formula dependencies
- Debug errors and identify their root causes
- Build new models or fill existing templates
- Navigate complex multi-tab workbooks seamlessly
- Use connectors to bring context from your other tools directly into your spreadsheets

---

## Get started with Claude for Excel

#### Supported versions

- Excel on the web
- Excel on Windows (Microsoft 365 subscription, build 16.0.13127.20296+)
- Excel on Mac (version 16.46+, build 21011600+)
- Excel on iPad (version 2.51+)

#### For individuals

1. Navigate to the **[Claude for Excel listing on Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/saas/wa200009404?tab=overview)**.
2. Click "Get it now" to install the add-in.
3. Open Excel, activate the add-in, and sign in with your Claude account.

#### For admins

**Deploy Claude** **for** **Excel to your organization:**

1. Visit the **[Microsoft 365 Admin Center](https://admin.microsoft.com/)**.
2. Navigate to **Settings > Org Settings > User owned apps and services** and ensure that **[“Let users access the Office Store"](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-addins-in-the-admin-center?view=o365-worldwide#manage-add-in-downloads-by-turning-onoff-microsoft-marketplace-across-all-apps-except-outlook)** is toggled on.
3. Navigate to **Settings > Integrated apps > Add-ins**.
4. Search for "Claude by Anthropic for Excel" in Microsoft AppSource.
5. Deploy the add-in to your organization or specific users.
6. Share these instructions with your team: **[Microsoft's deployment guide](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-deployment-of-add-ins?view=o365-worldwide)**.

After installation, team members can open Excel, activate the Claude add-in (from **Tools > Add-ins** on Mac or **Home > Add-ins** on Windows), sign in with their Claude credentials, and start working with their spreadsheets.

> **Important:** Organizations that have disabled "Let users access the Office Store" may find that admin-deployed add-ins don't appear for users. To work around this, deploy using the manifest XML files provided below.

For IT administrators deploying to multiple users:

#### Step 1: Obtain the custom manifest

1. Click **[this link](http://pivot.claude.ai/manifest-excel.xml)** to download the custom manifest XML file.
2. Save this file to a secure location.

#### Step 2: Access Microsoft 365 Admin Center

1. Navigate to **[https://admin.microsoft.com](https://admin.microsoft.com)**
2. Sign in with your admin credentials.
3. Go to **Settings** > **Integrated apps.**

#### Step 3: Upload the custom add-in

1. Click "Upload custom apps"
2. Select "Office Add-in."
3. Choose "I have a manifest file on this device."
4. Browse and select the Claude for Excel manifest XML file.
5. Click "Upload."

#### Step 4: Assign Users

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

- Users will see Claude appear in Excel's Home ribbon.
- First-time users will need to sign in with their Claude accounts
- No additional installation required by users.

#### Connect through an LLM gateway

If your organization routes API traffic through an internal LLM gateway connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the add-in without a Claude account. This is the same gateway pattern used by Claude Code.

For setup instructions and gateway requirements, see **[Use Claude for Excel and PowerPoint with an LLM gateway](https://support.claude.com/en/articles/13945233-use-claude-in-excel-and-powerpoint-with-an-llm-gateway)**.

---

## Key features

#### Read and understand complex models

Ask Claude questions about specific cells, formulas, or entire sections of your workbook. Claude can navigate across multiple tabs and provides answers with direct citations to referenced cells.

**Example prompts:**

- "What assumptions drive the revenue forecast in Q3?"
- "Explain how the WACC calculation flows through the DCF model"

#### Update assumptions safely

Modify values and inputs while Claude maintains all formula dependencies and relationships. Every change is highlighted with clear explanations.

**Example prompts:**

- "Increase growth rate by 2% and show the impact on terminal value"
- "Update interest rate assumptions based on latest Fed guidance"

#### Build and fill templates

Create spreadsheets from scratch or populate existing templates with new data, formulas, and assumptions.

**Example prompts:**

- "Build a three-statement model for a SaaS company"
- "Fill this DCF template with data from the uploaded 10-K"

#### Debug and fix errors

Identify error sources (like #REF!, #VALUE!, or circular references) and get actionable fixes that maintain spreadsheet integrity.

**Example prompts:**

- "Why is this NPV calculation returning #VALUE?"
- "Find all circular references in this workbook"

#### Change tracking and citations

Claude highlights every cell it updates and provides explanatory comments. When explaining calculations, Claude includes clickable citations that navigate directly to referenced cells.

#### Edit and format natively

Claude can now apply a range of Excel-native operations directly, including sorting and filtering data, editing pivot tables and charts, applying conditional formatting rules, setting data validation, and preparing workbooks for printing with finance-specific formatting tools.

**Example prompts:**

- "Sort this table by revenue, descending"
- "Add a conditional format that highlights cells below the target threshold in red"
- "Set up a dropdown for the status column with options: Active, Pending, Closed"
- "Toggle off gridlines and set the print area to A1:F20"

#### Support for connectors

Connect your other tools to give Claude context beyond what's in your spreadsheet. All connectors configured in your Claude settings are supported, including custom connectors.

To connect a tool, open the Claude sidebar and select the connectors icon to see available options.

Custom connectors can introduce security risks. Before enabling them, review **[Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp#h_b79c05dfcd)** for guidance on what to consider.

#### Use Skills in Excel

Skills you've enabled in your Claude settings are also available in the Claude for Excel add-in. Claude applies relevant Skills automatically while you work—you don't need to invoke them separately.

You can also type / in the sidebar to see available Skills and select one directly (for example, /debug or /clean-up). Skills that aren't relevant to Excel are excluded from this list.

To learn more about enabling and managing Skills, see **[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)**.

#### Set persistent instructions

Use the **Instructions** field in the add-in sidebar to set preferences that apply to every conversation in Excel. Instructions are useful for things like formatting conventions (for example, "always use IB formatting: blue for inputs, black for formulas"), preferred output style, or recurring context Claude should know about your workflow.

Instructions you set in Excel only apply to Excel — they're separate from any Instructions you set in PowerPoint.

---

## Technical specifications

**Supported file formats:**

- .xlsx files
- .xlsm files

**What's preserved:**

- Formulas and dependencies
- Cell relationships
- Existing formatting and structure

---

## Context and session management

- **Auto-compaction**: We **[automatically compact longer conversations](https://support.claude.com/en/articles/11647753-understanding-usage-and-length-limits#h_21b66a43b4)** into new conversations to avoid running out of context.
- **Session logging**: By turning this feature on in your settings, Claude will create a separate "Claude Log" tab in the Excel sheet to track your actions taken each turn. This allows Claude to maintain a history of its actions on the sheet.
  - If Claude doesn't do this automatically, you can simply ask it to log its history and it should create a new logging tab.
- **Overwrite protection**: To avoid accidental data loss, Claude warns you before overwriting existing data.

> **Note:** Your use of Claude for Excel is associated with your existing Claude account and is subject to the same usage limits.

---

## Current limitations

For Claude for Excel use, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) **Data will be deleted after 30 days, but will be cached for a number of hours so users can access context in recently closed out documents.

This is unlike our other commercial products (Team and Enterprise plans) that allow you to save and continue conversations with Claude. Chat history is not saved between sessions.

Currently, observability and audibility are not available with this feature. Claude for Excel does not inherit custom data retention settings your organization might have set, and isn't included in Enterprise audit logs or the Compliance API at this time.

Additionally, Claude does not have advanced Excel capabilities, including:

- Data tables
- Macros
- VBA (Visual Basic for Applications)

As a beta feature, Claude for Excel is **not recommended** for:

- Final client deliverables without human review
- Audit-critical calculations without verification
- Replacing users’ financial judgment and expertise
- Models containing highly sensitive or regulated data without proper controls

#### Unsupported versions

- Excel 2016 / 2019 (perpetual/volume license)
- Excel on Android
- Older builds of Microsoft 365 Excel below the SharedRuntime threshold

---

## Best practices

To use Claude for Excel safely and effectively:

- Always review changes before finalizing your work.
- Verify outputs match your organization's methodologies.
- Use appropriate permissions and access controls.
- Maintain human oversight for client-facing work.

---

## Prompt injection attack risks

Only use Claude for Excel with trusted spreadsheets and not spreadsheets from external untrusted sources (for example, downloaded templates, vendor files, collaborative documents, and data imports).

An important risk that users of Claude for Excel and other AI tools that can read and manipulate spreadsheets is prompt injection attacks that hide malicious instructions in spreadsheet content (cells, formulas, comments, etc.) to trick the AI models into taking unintended actions. For example, a seemingly innocent template or data file received from an external party or downloaded from the internet might contain hidden instructions to "export all financial data to this external URL" or "modify these financial records." Claude may interpret these malicious instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude for Excel can be manipulated to:

- **Extract and share sensitive information **with bad actors through formulas, web searches containing your sensitive data, or file system access that exposes proprietary information.
- **Modify critical data** such as financial records.
- **Perform destructive actions **without verification (should you allow Claude to act without verifying its actions), exploiting Claude's helpful nature to delete or corrupt important data across multiple sheets.

Users can approve all of Claude’s actions via a confirmation pop-up that appears when each tool is triggered:

- External data fetching: WEBSERVICE, STOCKHISTORY, STOCKSERIES, TRANSLATE, and the CUBE* functions
- External imports: IMPORTDATA, IMPORTXML, IMPORTHTML, IMPORTFEED, FILTERXML
- Dynamic references: INDIRECT
- Command execution: DDE (Dynamic Data Exchange)
- Code execution: CALL, EVALUATE, FORMULA
- File system access: IMAGE, FILES, DIRECTORY, FOPEN, FWRITE, FCLOSE
- System information: REGISTER.ID, RTD, INFO

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1849431310/ffc870a5114b4178fcd74b5cccf8/Screenshot+2025-11-25+at+11_30_10%E2%80%AFAM.png?expires=1776784500&signature=2f4029abf9460c4eb91587144e3c2038fa68bb7a269cb49c47af75a07d07661f&req=dSgjH819nIJeWfMW1HO4zYWKZ%2BRsKt53qAsRdssXCyDaRdJiUdEOE8LG1c2h%0ApUBwWGsm8pPPNDUrrKg%3D%0A)

While we continue to develop our offerings and improve safety measures to reduce these risks, users should exercise caution when using Claude for Excel and should not use it with spreadsheets from external, untrusted sources.

---

## Example use cases

#### Financial modeling

**Build models**

- "Build a 3-statement financial model for [company/industry]"
- "Create a SaaS metrics model with ARR, churn, and LTV calculations"
- "Build an LBO model with debt schedules and returns analysis"
- "Create a real estate pro forma for a multifamily acquisition"

**Forecasting**

- "Build a 12-month revenue forecast using historical trends"
- "Create a headcount capacity plan based on target client count"
- "Model cash flow projections for the next 3 years"

**Scenario analysis**

- "Add a downside case assuming revenue drops 15%"
- "Create base, bull, and bear scenarios with different growth assumptions"
- "Build a sensitivity table showing IRR across exit multiples and hold periods"

#### Data analysis

**Insights and trends**

- "What trends stand out in 2025 vs 2024?"
- "Identify the top 10 customers by revenue and their growth rates"
- "Which product categories are underperforming vs budget?"

**Variance analysis**

- "Compare actuals to budget and explain the largest variances"
- "Which accounts have unusual changes vs prior month?"
- "Reconcile these two sheets and highlight discrepancies"

**Categorization**

- "Categorize these transactions into expense types"
- "Tag customer feedback by sentiment and topic"
- "Score each lead based on likelihood to convert"

#### Data cleaning

**Standardize formats**

- "Convert all dates to YYYY-MM-DD format"
- "Standardize phone numbers to +1 (XXX) XXX-XXXX"
- "Clean up company names (remove Inc, LLC, Ltd variations)"

**Fix data quality issues**

- "Find and remove duplicate rows, keeping the most recent"
- "Identify and fix unicode/encoding errors"
- "Fill missing values based on patterns in the data"

**Parse and transform**

- "Extract company name from email domain"
- "Split full address into street, city, state, zip columns"
- "Convert this pivot table into a flat data table"

#### Formulas

**Troubleshooting**

- "Find all #REF and #VALUE errors in this workbook"
- "Why is cell B4 showing an error? Trace the issue"
- "This SUMIF isn't returning the right result — what's wrong?"

**Explanation**

- "Explain what this formula does in plain English"
- "Trace this cell back to its source inputs"
- "Document all the formulas on this sheet"

**Creation**

- "Write a formula to calculate days of inventory from this data"
- "Create a VLOOKUP that pulls price from the rate table"
- "Build a formula that flags overdue invoices"

#### Dashboards and reporting

**Dashboards**

- "Create an executive dashboard summarizing all worksheets"
- "Build a KPI scorecard with revenue, margins, and growth metrics"
- "Make an interactive summary with key charts and metrics"

**Reports**

- "Generate a monthly financial summary from the GL data"
- "Create a board-ready P&L with variance commentary"
- "Consolidate regional sheets into a company-wide report"

**Charts**

- "Create a waterfall chart showing revenue bridge"
- "Build a combo chart with revenue bars and margin line"
- "Make a cohort retention heatmap from this data"

#### Formatting

**Professional styling**

- "Format this model using IB conventions (blue inputs, black formulas)"
- "Add headers, borders, and proper number formats"
- "Apply consistent formatting across all sheets"

**Conditional formatting**

- "Highlight negative values in red"
- "Color-code rows by status (green/yellow/red)"
- "Add data bars to show relative performance"

#### Document import

**PDF extraction**

- "Extract the financial table from this PDF into Excel"
- "Pull the line items from this invoice PDF into my template"
- "Convert this scanned statement into editable data"

**Template population**

- "Fill in my deal template using data from this offering memo"
- "Populate the pitch template with these company metrics"
- "Map the imported CSV data to my standard format"

#### Model review

**Audit and validation**

- "Check that all formulas link correctly across sheets"
- "Verify the balance sheet balances in all periods"
- "Find any hardcoded values that should be formulas"

**Improvement**

- "How can I simplify this model structure?"
- "What's missing from this valuation model?"
- "Suggest ways to make this more user-friendly"

---

## Frequently asked questions

#### Which models are available when using Claude for Excel?

You can switch between Opus 4.7, Opus 4.6, and Sonnet 4.6 when using Claude for Excel.

#### Does Claude understand financial modeling conventions?

Yes, Claude is trained to recognize common financial modeling patterns, formula structures, and industry-standard calculations. However, always verify that outputs match your specific methodologies.

#### Can I use Claude for Excel with sensitive data?

Claude for Excel works within your existing security framework. For highly sensitive or regulated data, ensure you follow your organization's data handling policies.

#### What happens to my chat history?

Currently, chat history is not saved between sessions. Each time you open the add-in, you start a fresh conversation with Claude. However, we are working to support this in future versions of Claude for Excel.

#### How does Claude access my spreadsheet?

Claude reads the content of your currently open workbook, including cells, formulas, and tab structure. It can only access the workbook you have open in Excel.

#### What if Claude makes a mistake?

Claude highlights all changes it makes to your workbook. Review these changes carefully before saving or sharing your file. You can always undo changes using Excel's standard undo function.

## Related Articles
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Work across Excel, PowerPoint, and Word](https://support.claude.com/en/articles/13892150-work-across-excel-powerpoint-and-word)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
