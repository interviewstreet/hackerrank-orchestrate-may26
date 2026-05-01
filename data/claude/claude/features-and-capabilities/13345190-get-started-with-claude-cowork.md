---
title: "Get started with Claude Cowork"
title_slug: "get-started-with-claude-cowork"
source_url: "https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork"
last_updated_iso: "2026-04-15T22:23:32Z"
article_id: "15229827"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Get started with Claude Cowork

_Last updated: 2026-04-15T22:23:32Z_

This article explains how to use **[Claude Cowork](https://claude.com/product/cowork)**, which brings Claude Code's agentic capabilities to Claude Desktop for knowledge work beyond coding.

## Availability

Claude Cowork is available for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**
  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download
- **Claude Desktop for Windows**
  - Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

#### Will my computer support Claude Cowork?

If you haven't installed Claude Desktop yet and want to check if your computer will support Cowork, click the link associated with your system to download a simple program that checks this for you:

- **[macOS](https://claude.ai/api/desktop/darwin/universal/cowork-readiness-check/latest/redirect)**
- **[Windows arm64](https://claude.ai/api/desktop/win32/arm64/cowork-readiness-check/latest/redirect)**
- **[Windows x64](https://claude.ai/api/desktop/win32/x64/cowork-readiness-check/latest/redirect)**

Open the program after downloading to run the Cowork readiness check. If you see "This computer is ready for Cowork," you can move forward.

---

## What is Claude Cowork?

Claude Cowork uses the same agentic architecture that powers Claude Code, now accessible within Claude Desktop and without opening the terminal. Instead of responding to prompts one at a time, Claude can take on complex, multi-step tasks and execute them on your behalf.

With Cowork, you can describe an outcome, step away, and come back to finished work—formatted documents, organized files, synthesized research, and more. With scheduled tasks, Claude can complete work for you automatically, which isn't possible in regular chats outside of Cowork. With the introduction of projects in Cowork, you can organize related tasks into persistent, self-contained workspaces with their own files, links, instructions, and memory, making Cowork more powerful for recurring or long-running work.

**Important:**

- Cowork has unique risks due to its agentic nature and internet access.
- Cowork respects your current network egress permissions.
  - **Important:** Network egress permissions don't apply to the **[web search tool](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)** or MCPs, including Claude in Chrome.* *Team or Enterprise plan owners can turn off web search for Cowork and Chat in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**, or Claude in Chrome via **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension).**
- Cowork stores conversation history locally on your computer, so is not subject to Anthropic's **[data retention timeframe](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**.
- Cowork activity is not captured in Audit Logs, Compliance API, or Data Exports. Do not use Cowork for regulated workloads.
- If you're a Team or Enterprise plan admin, you can **[use OpenTelemetry (OTel) to monitor Claude Cowork activity](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)** across your organization.
  - OpenTelemetry is **not** a replacement for audit logging.
- Please review **[Use Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)** for more information.

For important limitations and considerations for Team and Enterprise organizations using Cowork, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans)**.

#### Key capabilities

- **Direct local file access:** Claude can read from and write to your local files without manual uploads or downloads.
- **Sub-agent coordination:** Claude breaks complex work into smaller tasks and coordinates parallel workstreams to complete them.
- **Professional outputs:** Generate polished deliverables like Excel spreadsheets with working formulas, PowerPoint presentations, and formatted documents.
- **Long-running tasks:** Work on complex tasks for extended periods without conversation timeouts or context limits interrupting your progress.
- **Scheduled tasks:** Create and save tasks that you can have Claude run on-demand, or automatically on a cadence of your choosing.
- **Spreadsheets and presentations:** Cowork can produce spreadsheets and slides that can be further edited with Claude for Excel and Powerpoint.
- **Projects:** Group related tasks into separate workspaces with their own files, context, instructions, and memory. See **[Organize your tasks with projects in Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-cowork).**
- **Mobile access for Pro and Max:** Message Claude from your phone and get results delivered back to the same conversation. Claude works on your desktop using your local files and connectors — you just don't have to be sitting in front of it. See **[Assign tasks to Claude from anywhere in Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork)**.

---

## How Claude Cowork runs your tasks

Cowork runs directly on your computer, giving Claude access to the files you choose to share. Code runs safely in an isolated space, but Claude can make real changes to your files.

When you start a task in Cowork, Claude:

1. Analyzes your request and creates a plan.
2. Breaks complex work into subtasks when needed.
3. Runs code and shell commands in an isolated virtual machine (VM) on your computer.
4. Coordinates multiple workstreams in parallel if appropriate.
5. Delivers finished outputs directly to your file system.

You maintain visibility into what Claude is planning and doing throughout the process so you can steer when it matters, or let Claude run independently.

---

## Get started

#### Requirements

- **Claude Desktop app:** Cowork requires the **[desktop app](https://support.claude.com/en/articles/10065433-installing-claude-desktop)** for macOS or Windows and is not available on web or mobile.
- **Paid Claude subscription:** Cowork is available to paid Claude plans (Pro, Max, Team, Enterprise) only.
- **Active internet connection:** Required throughout the session.

#### Access Claude Cowork

1. Open Claude Desktop.
2. Look for the mode selector that includes "Chat" and the Cowork tab.
3. Click the "Cowork" tab to switch modes to "Tasks".
4. Describe the task you want Claude to complete.
5. Review Claude's approach, then let it run.

> **Note:** The Claude Desktop app must remain open while Claude is working. If you close the app, your session will end.

## What to expect during a task

When Claude is working on a task in Cowork:

- **Progress indicators** show what Claude is doing at each step.
- **Transparency:** Claude surfaces its reasoning and approach so you can follow along.
- **Steering:** You can jump in to course-correct or provide additional direction mid-task.
- **Parallel work:** For complex tasks, Claude may coordinate multiple sub-agents working simultaneously.
- **Deletion protection:** When using Cowork, Claude requires your explicit permission before permanently deleting any files. You will see a permission prompt and will need to select "Allow" before Claude is allowed to perform deletion tasks.

Tasks can run for extended periods depending on complexity. You can monitor progress or step away and return when Claude finishes.

---

## Add global and folder instructions

#### Global instructions

You can give Claude standing instructions that apply to every Cowork session. Use this to specify your preferred tone, output format, or background on your role.

To set global instructions:

1. Navigate to Settings > Cowork within Claude Desktop.
2. Click "Edit" next to **Global instructions**.
3. Type your instructions in the text box and click "Save":

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2180541860/aad5befe38e5d2da4f97040baa29/8c27842d-07d6-4b6f-b513-9ea9fbd002dc?expires=1776783600&signature=2a3802595aa51c315c397c9aac0342c051f61637801dc112ea0818133d2f622f&req=diEvFsx6nIlZWfMW1HO4zah%2FGLfis9998mPglonEgA6pXK2zAyRp5MqvcYzI%0A4rKg%0A)

#### Folder instructions

Folder instructions add project-specific context to Cowork when you select a local folder. Claude can also update these on its own during a session.

---

## Claude Cowork plugins

Plugins customize how Claude works for your role, team, and company in Cowork. Each one bundles skills, connectors, and sub-agents into a single package. For details on finding, installing, and customizing plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

---

## Schedule recurring tasks

You can set up tasks that Claude runs automatically or on demand. To schedule a task, type `/schedule` in any Cowork task. You can also click "Scheduled" in the left sidebar to view, create, and manage your scheduled tasks.

Scheduled tasks only run while your computer is awake and the Claude Desktop app is open.

For more in-depth details, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

---

## Usage limits

Working on tasks with Cowork consumes more of your usage allocation than chatting with Claude. This is because complex, multi-step tasks are compute-intensive and require more tokens to execute.

If you find yourself hitting usage limits frequently when using Cowork, consider:

- Batching related work into single sessions.
- Using standard chat for simpler tasks that don't require file access or extended execution.
- Monitoring your individual usage in **[Settings > Usage](http://claude.ai/settings/usage)**.

See **[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)** for more information.

---

## Example use cases

Cowork is designed for complex, multi-step work that benefits from file access and extended execution time. Here are some examples:

#### File and document management

- **Organize files:** "Organize my Downloads folder by type and date" — Claude can sort hundreds of files into categorized folders.
- **Process receipts:** Drop receipts in a folder and ask Claude to create a formatted expense report.
- **Batch rename:** Rename files with consistent patterns like YYYY-MM-DD formatting.

#### Research and analysis

- **Research synthesis:** Combine information from web searches, articles, papers, and notes into coherent reports or summaries.
- **Transcript analysis:** Extract themes, key points, and action items from meeting notes, interviews, or lecture recordings.
- **Personal knowledge synthesis:** Analyze your notes, journals, or research files to surface patterns, themes, and connections you might have missed.

#### Document creation

- **Spreadsheets with formulas:** Generate Excel files with working VLOOKUP, conditional formatting, and multiple tabs—not just CSVs that need fixing.
- **Presentations:** Create slide decks from rough notes or meeting transcripts.
- **Reports from messy inputs:** Turn voice memos and scattered notes into polished documents.

#### Data and analysis

- **Statistical analysis:** Outlier detection, cross-tabulation, and time-series analysis on your data files.
- **Data visualization:** Generate charts using your data.
- **Data transformation:** Clean, transform, and process datasets.

---

## Permissions and security

Cowork runs with layered protections on your computer:

- **Code execution isolation:** Shell commands and code Claude writes run inside an isolated virtual machine (VM), separate from your main operating system.
- **Controlled file and network access:** Claude can only read and write files in folders you've connected, and network access follows the egress settings you've configured.

> **Important:** Claude has access to the local files you grant it permission to access, and can take real actions on your behalf. Review Claude's planned actions before allowing it to proceed, especially when working with sensitive files.

#### Permissions

Permissions work the same as for chat. You control:

1. Which **[MCPs you connect to Claude](https://claude.ai/settings/connectors)** and how often they ask for permission.
2. **[Claude's internet access](https://claude.ai/settings/capabilities)**

Please carefully assess how much you trust an MCP or website before extending access beyond Claude's default settings.

---

## Current limitations

Some Cowork capabilities are not yet available:

- **Memory in projects only:** Memory is supported within projects but is not retained across standalone Cowork sessions.
- **No chat or artifact sharing:** Sessions cannot be shared with others.
- **Desktop app required:** Cowork runs on your desktop computer via the Claude Desktop app. Pro and Max users can also message Claude from the mobile app while your desktop stays active. See Assign tasks to Claude from anywhere in Cowork for details.
- **Session persistence:** The Claude Desktop app must remain open and your computer must be awake for Claude to work on tasks. If you close the app or your computer goes to sleep, active tasks will stop.

We're iterating on Cowork based on feedback. If you encounter issues or have suggestions, use the feedback button in the app to share feedback with our team.

---

## Troubleshooting

#### I'm seeing "Setting up Claude's workspace" when I start Cowork; what does this mean?

This message is expected and indicates that Cowork is updating to the most recent version to apply any fixes and improvements.

#### Claude stopped working on my task

Ensure the Claude Desktop app was open throughout the entire task. If the app was closed or your computer went to sleep, the session may have ended.

#### I'm hitting usage limits quickly

Cowork consumes more usage than standard chat. Try using standard chat for simpler tasks and reserve Cowork for complex, multi-step work that benefits from file access.

#### Files aren't appearing where expected

Check that you've granted Claude the appropriate file access permissions. Review the output location Claude specified when completing the task.

#### I'm trying to start Cowork on Windows and seeing "VM service not running." What does this mean and how can I fix it?

"VM service not running" indicates that the Claude VM Service (CoworkVMService) isn't available. This can happen if you installed Cowork via the older .exe/Squirrel installer instead of MSIX, or the Windows service is stopped. To fix this, reinstall from **[our download page](https://claude.com/download)**, or start "Claude VM Service" in services.msc / `sc start CoworkVMService` (or `CoworkVMServiceStore` for Microsoft Store installs).

#### I'm trying to start Cowork on Windows and seeing "EXDEV: cross-device link not permitted." What does this mean and how can I fix it?

This happens when the VM image download crosses a drive boundary. The most common cause of this issue is when the path Settings > System > Storage > "Where new content is saved" points at D:\ instead of C:\, which makes Windows symlink the MSIX package folder across drives. This can also be caused by AppData redirected to a network share via a roaming profile. To fix this, set storage back to C:\, uninstall then reinstall Cowork, and update to the latest desktop version (which downloads directly to the final drive).

## Related Articles
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
