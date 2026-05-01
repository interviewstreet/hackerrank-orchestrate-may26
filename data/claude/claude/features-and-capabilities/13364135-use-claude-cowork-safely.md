---
title: "Use Claude Cowork safely"
title_slug: "use-claude-cowork-safely"
source_url: "https://support.claude.com/en/articles/13364135-use-claude-cowork-safely"
last_updated_iso: "2026-04-09T02:23:10Z"
article_id: "15263286"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Claude Cowork safely

_Last updated: 2026-04-09T02:23:10Z_

Cowork lets Claude work on your computer with access to your files, browser, connected services, and apps. That capability comes with risks worth understanding. This article covers what we've built to keep you safe, what you should watch for, and how to protect yourself when using Cowork.

## Availability

Claude Cowork is available for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**
  - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download
- **Claude Desktop for Windows**
  - Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

---

## Understanding the risks

**[Claude Cowork](https://claude.com/product/cowork)** has unique risks due to its agentic nature and internet access.

**To minimize risks:**

- Avoid granting access to local files with sensitive information, like financial documents.
- When using the Claude in Chrome extension, limit access to trusted sites.
- If you chose to extend Claude’s default internet access settings, be careful to only extend internet access to sites you trust.
- Monitor Claude for suspicious actions that may indicate prompt injection.
- Ensure you’re using trusted MCPs (as always).
- Be especially cautious with computer use—Claude is interacting with your actual desktop and apps outside the virtual machine. For details on how computer use works and how to manage permissions, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-computer-use-safety)**.

> **Important:** Cowork has access to Claude in Chrome; we strongly advise against using Claude in Chrome to manage or take actions involving sensitive information. See **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely#h_044f6a88a7)** for more information about the potential risks.

Cowork activity is not captured in audit logs, Compliance API, or data exports. Do not use Cowork for regulated workloads. For more information, see Cowork for Team and Enterprise plans.

## Our safety measures

We've implemented multiple layers of protection:

- **Model training:** We use reinforcement learning to train Claude to recognize and refuse malicious instructions—even when they appear authoritative or urgent.
- **Content classifiers:** We scan all untrusted content entering Claude's context and flag potential injections before they can affect behavior.
- **Deletion protection:** Cowork requires your explicit permission before permanently deleting any files. You'll see a permission prompt and must select "Allow" before Claude can perform deletion tasks.
- **Computer use safeguards:** When Claude uses your computer, it asks for your permission before accessing each application. For full details, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-computer-use-safety)**.

> **Important:** While we've enacted these safety measures to reduce risks, the chances of an attack are still non-zero. Always exercise caution when using Cowork.

---

## Protect yourself from malicious attackers

**1. Be selective about file access**

You control which local files Claude can access. Since Claude can read, write, and permanently delete these files, be cautious about granting access to sensitive information like financial documents, credentials, or personal records. Consider creating a dedicated working folder for Claude rather than granting broad access, and keep backups of important files.

**2. Monitor tasks, not just commands**

Cowork executes code and commands on your behalf. While we surface what Claude is doing, you shouldn't expect to validate every individual command—instead, watch for unexpected patterns: Is Claude accessing files or websites you didn't mention? Is the task scope creeping beyond what you asked for? If something feels off, stop the task immediately.

**3. Be cautious with scheduled tasks**

Scheduled tasks run automatically, which means Claude may be working without you actively watching. Because you can't monitor these tasks in real time, take extra care when setting them up:

- **Start simple.** Begin with low-risk tasks like generating summaries or compiling information before automating anything more complex.
- **Avoid sensitive data and consequential actions.** Don't schedule tasks that access sensitive files, send messages on your behalf, make purchases, or take other actions that are difficult to undo.
- **Review outputs after each run.** Check the results of scheduled tasks regularly to make sure Claude is performing as expected. You can review past runs from the "Scheduled" page in the left sidebar.
- **Pause tasks you're not actively using.** If you no longer need a scheduled task, pause or delete it rather than leaving it running in the background.

Scheduled tasks only run while your computer is awake and the Claude Desktop app is open. For more on setting up and managing scheduled tasks, see **[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork)**.

**4. Be cautious with computer use**

When Claude uses your computer, it works outside the virtual machine—interacting directly with your apps, browser, and desktop. This is powerful, but carries additional risk. Keep the following in mind:

- Start with lower-stakes tasks and build trust gradually, like you would with a new colleague.
- Block sensitive apps (healthcare portals, banking, dating apps) so Claude doesn't encounter information you'd rather keep private.
- Be aware that Claude takes screenshots to understand your screen.
- Monitor Claude's actions. Although it can only use apps that you’ve given it permission to use, if it clicks a link in one app that link will open, even if you haven’t given Claude permission to access that app.

For more information, see **[Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-computer-use-safety)**.

**5. Limit browser and web access to trusted sources**

If you're using the Claude in Chrome extension with Cowork, limit access to sites you trust. Web content is a primary vector for prompt injection attacks—malicious instructions can be hidden in websites, emails, or documents that Claude accesses. Claude's default network access is intentionally restricted; only extend it to sites you trust.

> **Important:** Network egress permissions don't apply to the **[web search tool](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search)** or MCPs, including Claude in Chrome.* *Team or Enterprise plan owners can turn off web search for Cowork and Chat in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**, or Claude in Chrome via **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension).**

**6. Be especially cautious with unfamiliar MCPs and plugins**

Desktop extensions (MCPs) and plugins expand what Claude can do, but each one introduces new ways for attacks to reach Claude. Plugins bundle together skills, connectors, and sub-agents into a single package, which means installing one can significantly expand Claude's scope of action.

Local MCP servers bundled with plugins and desktop extensions run on your computer with the same permissions as any other program you run. Stick to verified extensions from the Claude Desktop directory, and carefully evaluate the permissions any extension or plugin requests before installing.

For more on plugins, see **[Use plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)**.

**7. Be mindful of cross-app data sharing**

When using the Claude for Excel and Claude for PowerPoint add-ins with Cowork, Claude can read, edit, and pass context between these applications. For example, Claude might analyze data in Excel and move a chart into a presentation—without you explicitly directing that transfer. Be aware that data from one application may flow into another during a Cowork session, and avoid working with sensitive information in these add-ins while Cowork is active.

**8. Be aware of mobile access to your desktop**

When you message Claude from your phone, Claude works on your desktop computer using whatever file access, connectors, and plugins you've already granted. This means your phone effectively becomes a remote control for your desktop's resources.

If your organization manages your computer, be aware that this extends access to a personal mobile device. Review what access you've granted Claude in Cowork, and consider whether that level of access is appropriate when reachable from your phone.

**9. Report suspicious behavior immediately**

If Claude suddenly starts discussing unrelated topics, attempts to access unexpected resources, or requests sensitive information unprompted, stop the task and report it to [usersafety@anthropic.com](mailto:usersafety@anthropic.com) or use the in-app feedback button. Your reports help us improve our defenses.

---

## Your responsibility

You remain responsible for all actions taken by Claude performed on your behalf. This includes:

- Any content published or messages sent
- Purchases or financial transactions
- Data accessed or modified
- Actions taken by scheduled tasks running on your behalf
- Actions taken through computer use on your desktop and in your apps
- Respecting third-party website terms of service, including any restrictions on automated access

For more information about using AI agents safely, please review our **[Acceptable Use Policy for Agents](https://support.claude.com/en/articles/12005017-using-agents-according-to-our-usage-policy)**.

## Related Articles
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
