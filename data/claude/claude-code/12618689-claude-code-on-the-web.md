---
title: "Claude Code on the web"
title_slug: "claude-code-on-the-web"
source_url: "https://support.claude.com/en/articles/12618689-claude-code-on-the-web"
last_updated_iso: "2026-03-16T20:56:14Z"
article_id: "14157303"
breadcrumbs:
  - "Claude Code"
---

# Claude Code on the web

_Last updated: 2026-03-16T20:56:14Z_

Claude Code on the web runs Claude Code tasks remotely, working with code from your GitHub repositories. This article explains how it works, when to use it instead of running Claude Code in your terminal or IDE, and what workflows it enables.

## What Claude Code on the web provides

Claude Code on the web lets you delegate tasks to Claude that run without your active supervision. In your browser, you select a GitHub repository, describe what you want done, and Claude works on the task in a remote environment. Once Claude Code has started working on a task, you can leave the page completely; Claude will continue its work.  When finished, Claude will automatically create a pull request with changes for you to review.

This feature works with repositories you may not have on your local machine. You can kick off tasks on any GitHub repository you have access to without needing to clone it locally or set up a development environment. This makes it useful for projects you contribute to occasionally or for exploring codebases you're still learning about.

Claude Code for web enables asynchronous development workflows. With Claude Code in your terminal or editor, you typically work synchronously: you make a request, wait for Claude to respond, review the changes, then make another request. Synchronous work like this gives you fine-grained control but requires your attention throughout the process. Claude Code on the web handles this differently: you can assign a larger task, let Claude work independently, and return later to review the completed work.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1786446157/07ec74cd46317f8278083a317841/6448f3ee-c6df-4417-8a13-90d8c2ca3d55?expires=1776784500&signature=a0773cb06e6dc397576c1658e5d1ad4c58b7beb8d61e9e62832b5f3ad69d0105&req=dScvEM16m4BaXvMW1HO4zR8%2BD1WHSplz7XrRA1YwWGs51wvTk9KZ3VuqLLeq%0ALUj94FCfeqe1u%2Fx0OX0%3D%0A)

You can also run multiple tasks in parallel. Since each task runs in its own isolated environment, you can have Claude working on several different issues or repositories simultaneously. Each task proceeds independently and creates its own pull request when complete. More than one task can work on the same repository at the same time.

## How It Works

When you start a task, Claude Code on the web creates an isolated virtual machine for your work. Your GitHub repository is cloned into this environment, which comes pre-configured with common development tools and language ecosystems.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1786446158/c092f1383826cb871493f74169d4/97b7cb98-5da2-438e-a920-e170b8b9790e?expires=1776784500&signature=04f6635f1a734c08f23d1635475fe9d13605745206af866f1d916b7523c385b7&req=dScvEM16m4BaUfMW1HO4zcR0opAzh%2B3F7DtpMiX%2FBYkjA44kWQdXS1LD6t3S%0Alafi97yhXcPpryqmOCU%3D%0A)

Claude prepares the environment by running any setup commands you've defined in your repository's configuration. This includes installing dependencies, setting up databases, or running other initialization steps your project needs. If your task requires network access, maybe to install packages or fetch data, you can configure the level of internet access the environment has.

Once the environment is ready, Claude begins working on your task. Claude reads your code, makes changes, writes tests, and runs commands to verify the work. You can monitor progress and provide guidance through the web interface if needed.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1786446156/83ecf0a5b98eddc9ffc9694c50f7/353589ce-b678-441d-8909-71b45fa2d065?expires=1776784500&signature=8068bb33144b071f6a6c3524352c961dd57e7bb6995bcb2ecec4db183a0e6873&req=dScvEM16m4BaX%2FMW1HO4zVbcQ2WE68DLUQl3YqgIJdaxzNsgtAz88gNeZSvg%0A5%2Fwqpq0DhYp3Dczh9p8%3D%0A)

When Claude completes the task, it pushes the changes to a new branch in your GitHub repository. You receive a notification and can review the changes, then create a pull request directly from the interface. The pull request includes all of Claude's work, ready for your review and any additional changes you want to make.

Each task runs in complete isolation. The virtual machine exists only for that specific task and includes security controls like restricted network access and protected credential handling. Your GitHub authentication is managed through a secure proxy, so credentials never exist directly in the environment where Claude is working.

## When to use Claude Code on the web vs. terminal

Claude Code on the web is a new way of working with Claude Code. Some tasks are well-suited for asynchronous execution on the web, while others will continue to be best run with Claude Code via your terminal or IDE.

#### Use Claude Code on the web for:

- **Well-defined tasks with clear requirements:** When you can describe exactly what needs to be done and don't expect to need to steer Claude mid-task, the web interface lets you start the work and return when it's complete.
- **Background work on bug backlogs:** You can assign Claude multiple issues from your backlog and let them run in parallel. Each task proceeds independently, allowing you to tackle several fixes at once without monitoring each one individually.
- **Repositories you don't have locally:** If you need to make changes to a repository you haven't cloned or don't want to set up on your machine, Claude Code on the web handles the environment setup for you.
- **Tasks you want to queue up:** When you have a list of changes to make but don't want to work on them right now, you can start tasks on the web and review the results later. This lets you batch similar work or delegate tasks during times when you're focused on something else.

#### Use Claude Code in your terminal/IDE for:

- **Tasks needing frequent course correction:** When you're not sure exactly what the right approach is or expect you'll need to redirect Claude based on what you see, working in your terminal gives you immediate feedback. You can adjust direction as Claude works rather than waiting for a complete result.
- **Exploratory work with unclear requirements:** If you're figuring out how to solve a problem or investigating different approaches, the terminal lets you refine your request as you learn. The back-and-forth helps clarify requirements that weren't obvious at the start.
- **Local development with uncommitted changes:** When you're actively developing and have uncommitted work in your local repository, using Claude Code in your terminal keeps everything in one place. You can iterate quickly on changes without needing to commit or push work that isn't ready yet.
- **Tasks requiring immediate feedback:** If you need to see results quickly and want to iterate rapidly, the terminal provides lower latency. You can watch Claude work in real-time and stop or redirect if something goes wrong early in the process.

## Example Use Cases

#### Backend Changes with Test-Driven Development

Let Claude write tests that define the expected behavior, then implement the code to make those tests pass. This works particularly well for backend changes where behavior can be validated through automated testing.

**Example prompt:**

```
Add rate limiting to the /api/search endpoint. <br><br>The rate limiter should: <br>- Allow 100 requests per minute per API key <br>- Return 429 status when limit exceeded <br>- Reset limits after 60 seconds <br>- Track different API keys independently <br><br>Use a TDD approach: write comprehensive tests first, then implement the rate limiting logic to pass them.
```

**When to use this approach:** This works well on the web because the tests give Claude clear validation criteria to work towards. You don't need to monitor Claude's progress since the tests will catch issues and guide iteration toward a working solution. The self-contained nature of the task, where Claude writes tests then makes them pass, doesn't require your input once started.

**What makes this effective:** Claude can iterate on the implementation without your supervision, using test failures to identify and fix problems. The task runs longer than a simple code change, but you can let it complete in the background. When you review the pull request, both the tests and implementation are ready, and you have confidence the solution works because the tests pass.

#### Documentation Updates

Generate or update technical documentation such as README files, API documentation, code comments, or user guides.

**Example prompt:**

```
Update CHANGELOG.md with all changes since the v2.3.0 release:<br>  - Review commits on main branch since that tag. <br>  - Categorize changes into "Added, "Changed, "Fixed", and "Removed" sections. <br>  - Include the commit hash for each entry.
```

**When to use this approach:** Changelog updates are well-suited for the web because Claude can review commit history independently and format entries without guidance. The task is tedious to do manually but straightforward enough that Claude can complete it without questions about which commits to include or how to categorize them.

**What makes this effective:** You can delegate the entire changelog update and review the result when complete. Claude reads through commits, extracts meaningful changes, and follows your existing changelog format.

#### Refactoring with Clear Scope

Restructure code to improve organization or readability when you can define clear boundaries for the change. This includes extracting code, splitting up large files, or organizing module structure.

**Example prompt:**

```
The UserService class in /src/services/user.go has 800 lines long.<br>Split it into three focused services: <br>  - UserAuthService (login/logout/sessions) <br>  - UserProfileService (profile CRUD operations)<br>  - UserPreferencesService (settings/preferences)<br><br>Ensure all tests still pass.
```

**When to use this approach:** Refactoring with clear constraints works well on the web because you can set clear boundaries for Claude to follow. Test suites can provide validation, allowing Claude to verify the refactor didn't break any existing functionality.

**What makes this effective:** The task takes time, but doesn't need your active input once the structure is defined. You can start the refactor and review the organized result later, rather than monitoring Claude as it works through the task. The clear scope means Claude is unlikely to need guidance mid-task.

## Tips for Effective Use

- Consider adding a test suite to your repository so Claude more easily verify that it has successfully completed a task
- Specify success criteria rather than vague goals like "improve" or "fix"
- Define what should change and what should stay the same in your prompt
- Scope tasks with clear boundaries so Claude doesn't need guidance mid-task
- If you're thinking "I'll need to see how this goes first," consider using your terminal instead
- Use "Open in CLI" if you realize mid-task that you need to provide guidance

## Related Articles
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
- [Claude Code communications kit](https://support.claude.com/en/articles/14555877-claude-code-communications-kit)
