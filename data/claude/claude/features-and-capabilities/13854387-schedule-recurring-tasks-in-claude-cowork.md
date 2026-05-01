---
title: "Schedule recurring tasks in Claude Cowork"
title_slug: "schedule-recurring-tasks-in-claude-cowork"
source_url: "https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork"
last_updated_iso: "2026-04-09T22:39:21Z"
article_id: "16067064"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Schedule recurring tasks in Claude Cowork

_Last updated: 2026-04-09T22:39:21Z_

Scheduled tasks allow you to delegate work to Claude Cowork by creating tasks that run automatically on a recurring basis, or on demand. Instead of starting each task from scratch, you describe it once and Claude handles it on your schedule—delivering finished outputs like reports, briefings, and summaries every time.

> Scheduled tasks are available in Cowork on Claude Desktop for all paid plans (Pro, Max, Team, Enterprise).

## What scheduled tasks can do

Scheduled tasks have access to the same capabilities as regular Cowork tasks, including connected tools, skills, and installed plugins. Common uses include:

- **Daily briefings:** Summarize Slack messages, emails, or calendar events from the past 24 hours.
- **Weekly reports:** Compile data from Google Drive, spreadsheets, or connected tools into a formatted summary.
- **Recurring research:** Track topics, competitors, or industry news on a regular cadence.
- **File organization:** Periodically sort, clean up, or process files in a designated folder.
- **Team updates:** Generate status updates or standup summaries from project management tools.

## How scheduled tasks work

When you create a scheduled task, Claude saves your prompt as the task's instructions and runs them at the cadence you choose. Tasks can search Slack, query files, run web research, generate reports, and more—using any connectors and plugins you've set up in Cowork.

Each scheduled task runs as its own Cowork session. You can review the results when they're ready, just like any other task.

> **Important:** Scheduled tasks only run while your computer is awake and the Claude Desktop app is open. If your computer is asleep or the app is closed when a task is scheduled to run, Cowork will skip the task, then run it automatically once your computer wakes up or you open the desktop app again. When Cowork re-runs a skipped task, you will see a notification letting you know. Skipped runs also appear in the task’s history.

For Team and Enterprise organizations, admins control Cowork access through the admin toggle. For more details, see **[Cowork for Team and Enterprise plans](https://support.claude.com/en/articles/13455879)**.

---

## Create a scheduled task

There are two ways to create a scheduled task:

#### From any task using the /schedule Skill

1. Open Cowork and click “+ New task” in the upper left corner to start a new task.
2. Enter your prompt in the chat input, then click "Let's go" to start the task.
3. Alternatively, open an existing task.
4. Type "/schedule" in the chat input.
5. This launches a Skill to create a scheduled task that can be run on demand or automatically on an interval.
6. Add any other required details about the task you’re trying to create in the chat input and send the message.
7. Claude may ask you questions with **[multiple choice responses](https://support.claude.com/en/articles/13641943-visual-and-interactive-content#h_6bd6fbd2c3)** before creating the scheduled task.
8. Once Claude has all the necessary information, it will output the name of the task it’s creating, the schedule it will follow, and what the task actually does.
9. You can explicitly confirm you want to schedule the task when prompted by Claude by clicking “Schedule":

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2104085399/4dda7e6f76026fd827db0b9323a9/f20635bf-15e7-4978-a213-5b9f67e9fb9a?expires=1776784500&signature=5eb4770e592f2294784cdc6f55c4fe9c0a2ec130fa2f82e7f23bf3ee1306aada&req=diEnEsl2mIJWUPMW1HO4zeLJCUPj9%2B6CPx%2FSrZI7l8z58lKX%2BMZQGIm6MlJy%0ANqU%2F%0A)
10. Claude will create and schedule your task, and it will be added to the “Scheduled tasks” page.

#### From the “Scheduled tasks” page

1. Click “Scheduled” in the left sidebar.
2. Click “+ New task” in the upper right.
3. In the **Create scheduled task** modal, enter the following information:
  1. Task name
  2. Description of the task
  3. The prompt describing what your task does.
    1. **Note:** Type "/" to include plugins and Skills.
  4. How frequently the task will run (hourly, daily, weekly, on weekdays, or manually)
  5. The model you want to use [optional]
  6. Which folder Claude should work in [optional]
4. Click “Save” to add a new task to the **Scheduled tasks** page.

## Manage your scheduled tasks

To view and manage all your scheduled tasks, click “Scheduled” in the left sidebar. From here you can:

- View all the scheduled tasks you’ve created
- Review upcoming and past runs
- Click into individual tasks to manually edit the instructions or cadence
- Pause a scheduled task
- Resume a paused task
- Delete a scheduled task
- Run a task on demand

## Related Articles
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Assign tasks from anywhere in Claude Cowork](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
