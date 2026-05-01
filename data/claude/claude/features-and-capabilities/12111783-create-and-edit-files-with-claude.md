---
title: "Create and edit files with Claude"
title_slug: "create-and-edit-files-with-claude"
source_url: "https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude"
last_updated_iso: "2026-04-14T19:09:14Z"
article_id: "13415749"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Create and edit files with Claude

_Last updated: 2026-04-14T19:09:14Z_

Claude can execute code to create and work with files directly in your conversations. Prompt Claude using natural language to generate Excel spreadsheets, PowerPoint presentations, Word documents, and PDF files that you can download and use immediately.

> Code execution and file creation is available to all Claude users (Free, Pro, Max, Team, and Enterprise) on the web, Claude Desktop, and Claude Mobile.

These capabilities make it easy to produce professional documents by simply chatting with Claude. You can create financial models in Excel with working formulas, perform advanced analyses on uploaded data, produce reports with charts and visualizations, and generate presentations from your documents—all without specialized software skills.

---

## Availability

**Free, Pro, and Max plans:**

- Code execution and file creation is enabled by default
- Network access is enabled, allowing Claude to install packages from approved sources

**Team plan:**

- Code execution and file creation is enabled by default for Team plan organizations
- Organization owners can disable it in organization settings
- Network access is disabled by default; owners can enable it in organization settings

**Enterprise plan:**

- Code execution and file creation is enabled by default for new Enterprise plan organizations
- Organization owners can disable it in organization settings
- Network access is disabled by default; owners can enable it in organization settings
- Owners can configure network access controls, including domain whitelisting

---

## How to get started

#### Enabling on web and desktop

**Enterprise plans: **This capability is enabled by default at the organization level with **Allow network egress** toggled off for new Enterprise organizations. Owners can adjust this in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)** using the **Code execution and file creation** toggle.

**Team plans: **This capability is enabled by default at the organization level with **Allow network egress** toggled on with access to package managers only. An organization owner can manually disable this for the organization in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)** if needed.

**Free, Pro, and Max plans: **Enable file creation from **[Settings > Capabilities](http://claude.ai/settings/capabilities)** by toggling **Code execution and file creation** on.

To give Claude access to external data sources, toggle **Allow network egress** on:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2054774005/25bcfffba6c249cd128d6c3f6d52/CleanShot+2026-02-11+at+16_34_47%402x.png?expires=1776784500&signature=683cdfb759648c21bf7a568aca112adba319848d92c9480e1bcd3cdf0d60fc86&req=diAiEs55mYFfXPMW1HO4zYFJxAtCBJ3LPQVowIiib2maDYQ622cbO3cmrRkM%0A8Za69wxaTM8SO0g5dnE%3D%0A)

#### Enabling on Claude Mobile

To enable or disable this feature on Claude for iOS or Android, tap your initials or name in the left sidebar to open Settings. Select "Capabilities" and toggle **Code execution and file creation** on or off.

---

## Configuring network access (Team and Enterprise plans)

Team and Enterprise organization owners can control network access settings in **[Organization settings > Capabilities](http://claude.ai/admin-settings/capabilities)**. After enabling code execution and file creation, choose from the following options to configure network access for your team:

- **Allow network egress toggled off:** Claude operates with pre-installed packages only, with no internet access. This provides maximum security for sensitive environments.
- **Allow network egress to package managers only (default):** Claude can access approved package managers (npm, PyPI, GitHub, etc.) to install necessary software packages. This balances functionality with security, but some advanced features may be limited.
- **Allow network egress to package managers and specific domains:** Claude can access package managers plus additional domains you specify. Add domains individually to whitelist specific resources your organization needs:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945362/ad72504d5429960f369b8b91b43c/86f06c0e-6eaa-4574-a4cb-2c38b273613a?expires=1776784500&signature=6b77e31798f7bba61c0aee37dcbeb6f61193ab548e30dd2520c10b706fc0a27e&req=dScvH8B6mIJZW%2FMW1HO4zXJcCWtEnS1OpMW6Iph6YZdJAsfdQ7RLqxv0P09k%0AhxJKCuS%2FcBAL2eceoDk%3D%0A)

**All domains:** Claude has full internet access except for domains on Anthropic's legal blocklist. While this provides maximum flexibility for file creation and analysis tasks, it’s also the riskiest option. Please review the **[security considerations below](#h_0ee9d698a1)** before enabling “All domains”:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1789945361/e3188cb8edb9ca7c303615da6378/f1c99a7d-5956-48d5-9ec7-b7ae6c8c3d28?expires=1776784500&signature=9d3a9e2d64d3f9715fbb241edcc9540097b331c5693899baae26823bb83683d6&req=dScvH8B6mIJZWPMW1HO4zdnsdxKV5junqgKIA6CM1tpKDRgw%2Bx6Jfiwzj5M2%0AvX8Rs%2FGtUoBgZSX9VUc%3D%0A)

---

## How does disabling network access address security concerns with code execution and file creation?

**Short answer:** Disabling network access prevents data from leaving Claude's sandboxed environment - even if something goes wrong.

#### How it works

When Claude executes code or creates files, it operates within an isolated, sandboxed container. This means the work happens in a controlled environment separate from your systems. However, if network access is enabled, there's a potential risk: through prompt injection or other attacks, Claude could theoretically be tricked into sending data to external servers.

Disabling network access eliminates this risk entirely. Your team still gets Claude's full code execution and file creation capabilities -  building Excel models, creating presentations, analyzing data - but with the assurance that nothing can be transmitted outside the sandbox.

#### A phased approach to network access

Claude is most powerful with network access enabled - it can install new packages and dependencies, pull in real-time data, and interact with web services. For organizations comfortable with that risk profile, enabling access to vetted, trusted domains unlocks the full potential of code execution and file creation.

For those taking a more cautious approach, we recommend starting with network access disabled and adjusting as your team builds confidence:

1. **Start with network access off.** This is the most secure configuration. Claude can execute code and create files, but cannot communicate externally.
2. **Enable package managers.** Unlocks pip, npm, and other package managers to install dependencies - significantly expands what Claude can build.
3. **Expand network access as needed.** Add specific domains to an allowlist based on business requirements, maintaining visibility into what's permitted.

This approach gives you defense in depth - even if there were vulnerabilities in the sandbox or a successful prompt injection, disabled network access acts as a final barrier preventing data from leaving Anthropic's infrastructure.

> **Note:** If MCP (Model Context Protocol) integrations are enabled, network communication remains possible through those connections regardless of the network egress setting. Organizations should evaluate MCP configurations separately.

---

## Using code execution and file creation

When enabled, simply describe what you need in your message. For example, you might say "Create an Excel spreadsheet to track monthly expenses" or "Convert this document into a PowerPoint presentation." Claude will generate the file, which you can then download directly from the conversation.

Start with simple tasks to familiarize yourself with Claude's capabilities, then progress to more complex workflows. Be specific in your requests—describe the structure, content, and formatting you want. You may need to review and refine Claude's outputs to meet your exact requirements.

#### Supported file types

Claude can create Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization.

The maximum file size is 30MB per file for both uploads and downloads.

---

## Key capabilities

#### Direct file creation and editing

Claude creates Excel spreadsheets (.xlsx), PowerPoint presentations (.pptx), Word documents (.docx), and PDF files. You can download the files Claude creates or save them directly to Google Drive.

The maximum file size is 30MB per file for both uploads and downloads. For PDFs larger than 30MB, Claude can process them through its computing environment without loading them into the context window.

#### Advanced data analysis

Claude can perform sophisticated data analysis and data science work, including:

- Creating Python scripts for data analysis
- Generating data visualizations as image files (PNG)
- Processing CSV, TSV, and other data files
- Building machine learning models

#### Project files integration

Files in your projects are now accessible through Claude's computing environment while remaining in context. This enables seamless reference and workflow integration across your project files.

#### Extended context window

The context window has been expanded to support more complex multi-step workflows, particularly for conversations that use code execution and file creation extensively.

#### Language support

Claude provides full support for multiple languages in both the user interface and generated files, with proper formatting and regional standards.

---

## Security and network access

#### How it works

Code execution and file creation gives Claude a sandboxed computing environment. Claude’s internet access will vary based on your network egress settings.

**Network access allows Claude to:**

- Download and install packages from approved package managers (npm, PyPI, etc.)
- Access resources needed for file creation and analysis

---

## Security considerations

It is possible for a bad actor to inconspicuously add instructions via external files or websites that trick Claude into:

1. Downloading and running untrusted code in the sandbox environment for malicious purposes
2. Reading sensitive data from a connected knowledge source (for example, Remote MCP, projects) and using the sandbox environment to make an external network request to leak the data

This means Claude can be tricked into sending information from its context (for example, prompts, projects, data via MCP, Google integrations) to malicious third parties. To mitigate these risks, we recommend you monitor Claude while using the feature and stop it if you see it using or accessing data unexpectedly. You can report issues to us using the thumbs down function directly in Claude.

In line with our **[safe and trustworthy agents framework](https://www.anthropic.com/news/our-framework-for-developing-safe-and-trustworthy-agents)**, we have applied the following mitigations:

- Given you full control of the feature. You can turn it on or off at any time.
- Designed Claude to give you user-friendly summaries of its actions so you can see what it is doing. You can stop Claude's actions at any time and we recommend monitoring Claude's work while using the feature.
- Given you the ability to review and audit actions taken by Claude within the sandbox environment.
- Disabled public sharing of conversations that include any file artifacts from the code execution and file creation feature for free, Pro, and Max users.
- Limited the duration of tasks that can be completed by Claude and the length of time you can use a single sandbox container to avoid loops of malicious activity.
- Implemented sandbox isolation such that no sandbox environments are ever shared between users.
- Intentionally limited the network, container, and storage resources.
- Implemented a prompt injection classifier to detect malicious prompt manipulation and stop execution if detected.

We have performed red-teaming and security testing on this feature. We have a continuous process for ongoing security testing and red-teaming. We encourage organizations to evaluate these protections against their specific security requirements when deciding whether to enable this feature.

#### For Team and Enterprise owners

Team and Enterprise owners have full control over this feature, including:

- Enabling or disabling the feature organization-wide
- Controlling network access settings
- Configuring domain whitelisting to allow access only to specific approved domains

> **Note:** Claude can only be tricked into leaking data it has access to in a conversation via an individual user's prompt, project, or activated connections.

---

## Approved network domains

When network access is enabled, Claude can access the following approved domains:

- **Anthropic Services (Explicit):** [api.anthropic.com](http://api.anthropic.com/), [statsig.anthropic.com](http://statsig.anthropic.com/)
- ​**GitHub:** [github.com](http://github.com/)
- **NPM:** [registry.npmjs.org](http://registry.npmjs.org/), [npmjs.com](http://npmjs.com/), [npmjs.org](http://npmjs.org/)
- ​**Python:** [pypi.org](http://pypi.org/), [files.pythonhosted.org](http://files.pythonhosted.org/), [pythonhosted.org](http://pythonhosted.org/)
- **Rust:** [crates.io](https://crates.io), [index.crates.io](https://index.crates.io), [static.crates.io](https://static.crates.io)
- **Ubuntu:** [archive.ubuntu.com](https://archive.ubuntu.com), [security.ubuntu.com](https://security.ubuntu.com)
- **Yarn:** [yarnpkg.com](http://yarnpkg.com/), [registry.yarnpkg.com](http://registry.yarnpkg.com/)

---

## Common workflows

> **Note: **Refer to **[Create and edit files with Claude to eliminate hours of busy work](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work)**[ ](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work)for use cases and demo videos, and **[Financial Analysis Workflows with Claude](https://support.claude.com/en/articles/12220298-financial-analysis-workflows-with-claude)** for guidelines specific to Claude for Financial Services customers.

#### Build a financial model in Excel

Generate spreadsheets with working formulas and calculations by describing your needs. Try:

```
Create a monthly budget tracker with income, expenses categories, and <br>automatic calculations for savings.
```

Claude will produce an Excel file with proper formulas, formatting, and even charts to visualize your data.

#### Generate a professional report

Combine data analysis with document creation by providing your information and requirements. Try:

```
Create a quarterly sales report using this CSV data, including trend <br>analysis and recommendations.
```

Claude will analyze your data and produce a formatted Word document or PDF with charts, insights, and professional formatting.

#### Convert between file formats

Change any document from one format to another while preserving or enhancing the content. Try:

```
Convert this Word document to a presentation.
```

or

```
Explain this Excel spreadsheet in a Word report with commentary.
```

Claude can even support workflows requiring multiple file format conversions. For instance, you could upload a CSV file and prompt Claude to create a financial model, write a memo summarizing it, and generate a PowerPoint to share the results.

#### Extract and analyze PDF data

Upload a PDF containing tables or forms and ask Claude to extract the information. Try:

```
Extract all the data from this PDF into an Excel spreadsheet and create a <br>summary chart.
```

Claude will pull the data, organize it in spreadsheet format, and add visualizations for quick insights.

#### Perform Complex Analyses

Upload a CSV with data and ask Claude to build a machine learning model to predict a particular outcome. Have Claude output a report summarizing what it did and the results. Claude will use python to train a model on your data, and provide an explanation of what it did, including the quality of the model, and the results.

---

## Frequently asked questions

#### How does file creation work?

We have given Claude a private computing environment directly in claude.ai. This allows Claude to write and run code (for example Python or Javascript). It uses common code packages to create documents, spreadsheets, and slides. Users can also have Claude use its computing environment for other things like data analysis, debugging code snippets, and fun tasks like gif-creation.

#### How do Claude’s file creation capabilities impact usage limits?

Use of this capability draws from the same usage limits offered by your plan. Note that creating files will use more of your limit compared to normal chats with Claude.

#### Can Claude work with more than one file at a time?

Claude can handle multiple files in a single chat, allowing you to create comprehensive multi-file reports and analyses. Files remain available for download throughout your conversation.

#### Is file creation supported on Claude for iOS or Android?

File creation is supported on Claude for iOS and Android. Note that when you tap "Download" on Claude Mobile, the file will open in either the system preview or a separate app (for example, the Word app for .docx files).

#### Do artifacts work with file creation?

Yes you are still able to create artifacts (e.g., HTML or react apps, markdown documents, mermaid diagrams, SVGs) with file creation on. Claude now uses the computing environment to create artifacts so the user experience may look slightly different than users are used to. Please report any issues or feedback using the thumbs up/down functionality when chatting with Claude.

## Related Articles
- [Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)
- [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
