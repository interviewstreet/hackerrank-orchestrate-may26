---
title: "Let Claude use your computer in Cowork"
title_slug: "let-claude-use-your-computer-in-cowork"
source_url: "https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork"
last_updated_iso: "2026-04-01T21:25:54Z"
article_id: "16481744"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Let Claude use your computer in Cowork

_Last updated: 2026-04-01T21:25:54Z_

Claude can now use your computer to complete tasks in Cowork and Claude Code (refer to our **[Claude Code Docs](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer)** for more information about this). When Claude doesn't have a connector or tool for what you need, it navigates your screen directly—clicking, typing, and opening apps just like you would. It can work in your browser, open files, and run your dev tools automatically, with no setup required.

> Computer use is in research preview for Pro and Max plans. It’s available in Cowork and Claude Code in the Claude Desktop application for both macOS and Windows. This early research preview comes with risks—review **[Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)** before using this capability.

---

## How computer use works with Cowork

In Cowork, Claude uses the most precise tool first. When you assign a task, Claude follows this order:

1. **Connectors. **If a connector is available—like Gmail, Google Drive, or Slack—Claude uses it. This is the fastest and most reliable path.
2. **Browser. **When there isn’t a connector for the tool you need, Claude can navigate the Chrome browser to work on your task using Claude in Chrome.
3. **Screen interaction. **Claude uses computer use to interact directly with your screen: clicking, typing, and navigating your desktop apps.

Claude prioritizes the fastest method. For example, pulling messages through your Slack connection takes seconds, but navigating Slack through your screen takes much longer and is more error-prone.

---

## What you can do

Computer use lets Claude work with the apps and files on your machine. For example:

- Pull together a competitive analysis using local files and connected tools, then compile it into a formatted report.
- Open your phone simulator, interact with the app you developed, and find UX issues.
- Fill in a spreadsheet with data from multiple sources, format it, and save it to a shared folder.
- Navigate apps that don’t have connectors—like an internal dashboard or a specialized tool your team uses.

If your work involves a physical machine, Claude keeps working while you step away. Your computer just needs to be on.

---

## Permissions and access

Claude asks for your permission before accessing each application. You’ll see a prompt and must approve before Claude can interact with that app. Some apps are off-limits by default.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2193297849/243cf7bd2386d92a253c2cec7d32/46cb6fcb-c0ee-4d1c-9974-9c1c1058c81c?expires=1776784500&signature=c0327f7cc11881077fc78429d68756de089f441e35d4819a50cedf446111b898&req=diEuFct3molbUPMW1HO4za8%2BSXqFSySZOFMEfKzd96oZf4En9ZwvX5K2NroT%0A4QZinY7jb1l8dN8VdZI%3D%0A)

Claude is trained to avoid risky operations—like transferring funds, modifying or deleting files, or handling sensitive data—and to flag signs of prompt injection. However, these safeguards aren't perfect, and Claude may occasionally act outside these boundaries.

---

## Safeguarding personal data

When Claude uses computer use, Claude takes screenshots of your computer to understand how to navigate the screen and the apps to which you’ve given permission. This means Claude can see any information visible on your screen or those apps, including personal data, sensitive documents, or private information belonging to you or others.

Be mindful of what's visible when using Claude, especially on apps containing confidential information. Close files or apps with sensitive information before using computer use.

#### Claude is trained to avoid

- Engaging in stock trading or investment transactions
- Inputting sensitive data
- Gathering or scraping facial images

These guardrails are part of how Claude is trained and instructed, but they aren't absolute. Don't rely on them as a substitute for blocking access to sensitive apps.

#### Recommendations

- Do not give computer use permission access to sensitive apps (such as banking, healthcare, government).
- Start with simple tasks like research or organizing rather than complex multi-step workflows.
- Make sure your prompts are specific and carefully tailored to avoid Claude doing things you didn't intend.

#### What to avoid

We strongly advise against using computer use to manage or take actions on sensitive information including but not limited to:

- Managing financial accounts or investments
- Handling legal documents or contracts
- Processing medical or health information
- Interacting with apps containing personal information of others

#### Memory

Cowork has memory, which means Claude can learn how you work and retain context across sessions. Sensitive data—like passwords, financial details, or health information—is excluded from memory. You can view, edit, and delete what Claude remembers at any time.

---

## Safety

Computer use runs outside the virtual machine that Cowork normally uses for working on your files and running commands. This means Claude is interacting with your actual desktop and apps, rather than an isolated sandbox. We’ve built safeguards for this:

- **Per-app permissions. **Claude asks before accessing each application, and some sensitive apps (investment and trading platforms, cryptocurrency) are blocked by default.
- **App blocklist.** Prevent Claude from accessing certain apps by adding them to a blocklist. Any requests from Claude to use blocked applications will be automatically denied.
- **Action review.** Our system scans for signs of prompt injection when Claude uses your computer, and Claude will ask permission before accessing new applications. You can stop Claude at any point. But this capability is still early, and attacks are constantly evolving—stay cautious.

That said, computer use is a new capability, and the threats it guards against are constantly evolving. Claude makes mistakes, and no safeguards are perfect. Start with apps you trust and monitor Claude’s work—especially early on. Note that actions taken in one app can impact other apps. For example, clicking a link in your email app might open it in Chrome, even if you haven’t explicitly granted Claude permission to use Chrome (we can prevent Claude from seeing the Chrome window but can’t stop the link from opening). We don't recommend for use on apps with sensitive data relating to your healthcare, finances, or other personal records.

For detailed safety guidance, see **[Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely)**.

---

## Current limitations

This is a research preview. Keep the following in mind:

- Your desktop must be active. Your computer needs to be awake and the Claude Desktop app needs to be open for computer use to work.
- Complex tasks sometimes need a second try. Computer use works well for many tasks, but may struggle with complex multi-step workflows.
- Screen interaction is slower than connectors. When Claude works through your screen instead of a direct integration, tasks take longer. Where possible, connect the tools you use most.
- Available on Pro and Max plans only. Team and Enterprise plans don’t have access to computer use at this time.

---

## Get started with computer use

To start using computer use:

1. Make sure you have the latest version of Claude Desktop. Download or update at claude.com/download.
2. Open the desktop app and go to **Settings > General** (under **Desktop app**).
3. Find the **Computer use** toggle and turn it on:

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2193911341/630e6df3b08b27d1c7b4f1ca6a1f/image.png?expires=1776784500&signature=e1be11a0f5fc3e1ef0707800c90e984b466ccb30a2180b1b781aa16d10463f91&req=diEuFcB%2FnIJbWPMW1HO4zR8GrkJ7TU41jdPXX%2BaSOrF%2FBh3IGdxZNxkz0A86%0ABwsf%0A)
4. Open Cowork or Claude Code in the desktop app and start a session.
5. Ask Claude to do something that involves an app on your computer. Claude will ask for permission to access the app before proceeding.

We’re sharing this early because it’s the kind of capability that gets better with real usage. If something doesn’t work as expected, use the in-app feedback button or reach out to [usersafety@anthropic.com](mailto:usersafety@anthropic.com).

## Related Articles
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
