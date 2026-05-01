---
title: "Claude Code power user tips"
title_slug: "claude-code-power-user-tips"
source_url: "https://support.claude.com/en/articles/14554000-claude-code-power-user-tips"
last_updated_iso: "2026-04-15T01:12:53Z"
article_id: "17025313"
breadcrumbs:
  - "Claude Code"
  - "Launch guides"
---

# Claude Code power user tips

_Last updated: 2026-04-15T01:12:53Z_

This article collects workflow tips from the Claude Code team at Anthropic. These practices cover parallel execution, planning, automation, verification, and customization—the patterns the team uses every day to ship code faster. Everyone’s setup is different, so experiment to see what works for you.

> **Important:** The single most impactful tip in this guide is **verification**—giving Claude a way to check its own output. If you only adopt one practice, make it that one. See the **[Verification](#h_7dd53c5c29)** section below.

> **Before you start: scope of this guide**
>
> These are power-user patterns collected from individual engineers on the Claude Code team. As a result:
>
> - Most commands shown here ship with Claude Code: /color and /btw are **built-in commands**, and /simplify and /loop are **bundled skills** that ship with the CLI. See the **[commands reference](https://code.claude.com/docs/en/commands)** and **[skills](https://code.claude.com/docs/en/skills)**. You can build your own skills by adding a SKILL.md file under .claude/skills/<name>/.
> - The iMessage plugin ships in the official claude-plugins-official marketplace. Community plugins (for example the “ralph-wiggum” plugin) are not reviewed or sanctioned by Anthropic — check with your administrator before installing third-party plugins in a managed environment.
> - Some capabilities—auto mode, sandboxing, remote control, scheduled cloud jobs, voice—are **off by default** and may be disabled by your organization's policy. If a command or flag here returns "not available," your admin has likely not enabled it for your workspace.
>
> Everything else in this guide works on a stock Claude Code install. When in doubt, run `/help` to see what is actually available in your session.

## Contents

---

## Working in parallel

#### Run multiple sessions at once

The biggest productivity unlock is running 3–5 Claude sessions in parallel, each in its own git worktree. Claude Code has native worktree support built in.

- From the CLI, run `claude --worktree` (or `claude --worktree my_worktree`) to start a session in an isolated worktree. Add `--tmux` to launch in its own Tmux session.
- From the Desktop app, open the Code tab and check the worktree checkbox.
- For non-git VCS (Mercurial, Perforce, SVN), define `WorktreeCreate` and `WorktreeRemove` hooks in your `settings.json` to get the same isolation.

To stay oriented across many sessions, name your worktrees, set up shell aliases (`za`, `zb`, `zc`) to jump between them, color-code your terminal tabs, and enable terminal notifications so you know when any Claude needs your attention. Many engineers keep a dedicated “analysis” worktree just for reading logs and running queries.

#### Subagents with worktree isolation

Subagents can also run in isolated worktrees, which is especially powerful for large batched changes. Add `isolation: worktree` to your agent’s frontmatter:

```
# .claude/agents/worktree-worker.md<br>---<br>name: worktree-worker<br>model: haiku<br>isolation: worktree<br>---
```

Then prompt naturally: *“Migrate all sync IO to async. Batch the changes and launch 10 parallel agents with worktree isolation. Each agent should test its changes end to end, then put up a PR.”*

#### /batch for large migrations

The `/batch` command interviews you about a migration, then fans the work out to as many worktree agents as needed — dozens, hundreds, or more. Each agent works in isolation, tests its own changes, and creates a PR independently.

```
&gt; /batch migrate src/ from Solid to React
```

---

## Planning before building

#### Start complex tasks in plan mode

Press **Shift+Tab** to cycle into plan mode. Pour your effort into the plan so Claude can one-shot the implementation. The typical flow is: enter plan mode → refine the plan → switch to auto-accept edits → Claude executes.

A few patterns from the team:

- Have one Claude write a plan, then spin up a second Claude to review it as a staff engineer.
- The moment something goes sideways, switch back to plan mode and re-plan rather than course-correcting mid-stream.
- After plan mode, Claude **automatically names your session** based on what you’re working on—you can also set a name upfront with `claude --name "auth-refactor"`.

#### Use Opus with thinking for everything

Claude Code team’s reasoning: *“It’s the best coding model I’ve ever used, and even though it’s bigger & slower than Sonnet, since you have to steer it less and it’s better at tool use, it is almost always faster than using a smaller model in the end.”*

**The math:** less steering + better tool use = faster overall results, even with a larger model.

#### Effort level

Run /effort to choose your effort level. The available levels are **low** (fewer tokens, faster), **medium**, **high** (more tokens, more intelligence), **max**, and **auto** (Claude chooses per request). The default is **high** on Team, Enterprise, and direct API access, and **medium** on other plans. The Claude Code team uses high for everything; switch to /effort max for hard debugging or architecture decisions where you want Claude to reason for as long as it needs. Max burns through usage limits faster, so activate it per session.

---

## Prompting effectively

Don’t accept the first solution—push Claude to do better. A few prompts that work well:

- **“Grill me on these changes and don’t make a PR until I pass your test.”** Forces Claude to validate your understanding before shipping.
- **“Prove to me this works.”** Have Claude diff behavior between `main` and your feature branch.
- **“Knowing everything you know now, scrap this and implement the elegant solution.”** Useful after a mediocre first attempt.

Write detailed specs to reduce ambiguity before handing work off. The more specific you are, the better the output.

#### /btw for side questions

While Claude is actively working, use `/btw` to ask a quick question without interrupting it. It’s single-turn with no tool calls, but has full context of the conversation.

```
&gt; /btw what does the retry logic do?
```

---

## Learning with Claude

Claude Code isn’t just for writing code—it’s a powerful learning tool when you configure it to explain and teach.

- **Enable “Explanatory” or “Learning” output style** in `/config` to have Claude explain the *why* behind changes.
- **Generate visual HTML presentations** explaining unfamiliar code.
- **Ask for ASCII diagrams** of new protocols and codebases.
- **Build a spaced-repetition skill:** explain your understanding, Claude asks follow-ups to fill gaps.

---

## CLAUDE.md and memory

#### Invest in your CLAUDE.md

Share a single `CLAUDE.md` file at your repo root, checked into git, with the whole team contributing. The key practice: **anytime Claude does something incorrectly, add it to CLAUDE.md** so it knows not to repeat the mistake.

After every correction, end with: *“Update your CLAUDE.md so you don’t make that mistake again.”* Claude is very good at writing rules for itself.

#### @claude in Code Reviews

Install the GitHub Action with `/install-github-app`, then tag `@claude` in PR comments to add learnings to `CLAUDE.md` as part of the review:

```
nit: use a string literal, not ts enum  @claude add to CLAUDE.md to never use enums, always prefer literal unions
```

This is “Compounding Engineering”—each correction makes every future session better.

#### Auto-memory

Run `/memory` to configure Claude Code’s built-in memory system.

**Auto-memory** automatically saves preferences, corrections, and patterns between sessions. Memories are written to ~/.claude/projects/<project>/memory/ (one directory per git repo root). This is separate from your user-level ~/.claude/CLAUDE.md and project-level ./CLAUDE.md files, which you maintain by hand.

The naming maps to how REM sleep consolidates short-term memory into long-term storage.

#### Advanced: Notes directory

One engineer on the team tells Claude to maintain a notes directory for every task and project, updated after every PR — then points `CLAUDE.md` at it.

---

## Verification — the #1 Tip

Giving Claude a way to verify its work will markedly improve the quality of the final result. If Claude can close the feedback loop on its own, it will iterate until the output is right.

Verification looks different per domain—bash commands, test suites, simulators, browser testing—but the principle is the same. Invest in domain-specific verification.

#### The Chrome extension

For frontend work, install the Claude Code Chrome extension. Think of it like any other engineer: if you ask someone to build a website but don’t let them use a browser, will it look good? Probably not. With a browser, they’ll iterate until it does.

The team uses the Chrome extension every time they work on web code. Download it for Chrome or Edge at **[code.claude.com/docs/en/chrome](https://code.claude.com/docs/en/chrome)**.

#### Desktop app for web servers

The Claude Desktop app bundles the ability to **automatically start and test web servers** in a built-in browser. You can set up something similar in CLI or VS Code using the Chrome extension, or just use the Desktop app directly.

#### /simplify for Code Quality

Append `/simplify` to any prompt after making changes. It runs parallel agents that review changed code for reuse, quality, efficiency, and `CLAUDE.md` compliance—all in one pass.

```
&gt; hey claude make this code change then run /simplify
```

---

## Commands, skills, and subagents

#### Skills for repeated workflows

If you do something more than once a day, turn it into a skill. Skills are checked into `.claude/skills/<name>/SKILL.md` and shared with the team (the legacy `.claude/commands/` path still works, but skills are the recommended approach). A few ideas:

- A `/techdebt` command that runs at the end of every session to find duplicated code.
- A command that syncs 7 days of Slack, GDrive, Asana, and GitHub into one context dump.
- Analytics-engineer agents that write dbt models, review code, and test in dev.

Slash commands can include **inline Bash** to pre-compute info (like `git status`) without extra model calls.

#### Subagents for PR workflows

Think of subagents as automations for your most common PR workflows. Drop `.md` files into `.claude/agents/`:

```
.claude/agents/   build-validator.md   code-architect.md   code-simplifier.md   verify-app.md
```

Each agent can have a custom name, color, tool set, allowed/disallowed tools, permission mode, and model. Set the **default agent for your main conversation** by adding `"agent"` to `settings.json` or using `claude --agent <name>`. Run `/agents` to get started.

#### --agent for custom system prompts

Custom agents are a powerful primitive that often gets overlooked. Define a new agent in `.claude/agents`, then run `claude --agent=<name>`. Example of a read-only agent:

```
# .claude/agents/ReadOnly.md --- name: ReadOnly description: Read-only agent restricted to the Read tool only color: blue tools: Read ---  You are a read-only agent that cannot edit files or run bash.
```

#### Leveraging subagents at runtime

- **Append “use subagents”** to any request where you want Claude to throw more compute at the problem.
- **Offload individual tasks to subagents** to keep your main agent’s context window clean and focused.
- **Route permission requests to Opus via a hook** — let it scan for attacks and auto-approve the safe ones.

#### Code review agents

When a PR opens, Claude can dispatch a team of agents that each focus on a different concern — logic errors, security issues, performance regressions — and post inline comments. The Anthropic team built this for themselves first; code output per engineer increased significantly and reviews were the bottleneck.

---

## Hooks

Hooks let you deterministically run logic at points in the agent lifecycle. Ask Claude to add a hook to get started.

#### Common hook patterns

Example `PostToolUse` hook for auto-formatting:

```
"PostToolUse": [<br>  {<br>    "matcher": "Write|Edit",<br>    "hooks": [{ "type": "command", "command": "bun run format || true" }]<br>  }<br>]
```

---

## Permissions and safety

#### Pre-approve common commands

Run `/permissions` to pre-allow common safe commands and check them into your team’s `.claude/settings.json`. This is the **recommended alternative** to skipping permissions entirely — you get fewer prompts while keeping an auditable allowlist. **Full wildcard syntax is supported**—try `"Bash(bun run *)"` or `"Edit(/docs/**)"`.

Claude Code’s permission system layers prompt-injection detection, static analysis, sandboxing, and human oversight. A small set of safe commands is pre-approved out of the box; everything you add via `/permissions` is additive to that baseline.

#### Auto mode

Auto mode lets Claude make permission decisions on your behalf. Classifiers evaluate each action before it runs — safe operations get auto-approved, risky ones still get flagged. Enable it with `claude --enable-auto-mode`; once enabled, **Shift+Tab** cycles `default → acceptEdits → plan → auto` during a session. Without that flag, the cycle is `default → acceptEdits → plan`.

#### Sandboxing

Run `/sandbox` to opt into Claude Code’s open-source sandbox runtime. It runs on your machine and supports both **file and network isolation**, improving safety while reducing permission prompts. Three modes are available:

- Sandbox BashTool, with auto-allow
- Sandbox BashTool, with regular permissions
- No sandbox

#### Long-running tasks

For very long-running tasks, ensure Claude can work uninterrupted. Recommended approaches:

- Prompt Claude to verify with a background agent when done.
- Use an agent `Stop` hook for deterministic checks (preferred for auditable workflows).
- Use the “ralph-wiggum” community plugin.

For sandboxed environments, use `--permission-mode=dontAsk` or `--dangerously-skip-permissions` to avoid blocks.

---

## Scheduled and recurring tasks

#### /loop for local recurring tasks

`/loop` schedules a recurring task locally for up to 3 days at a time. A few examples the Claude Code team runs:

```
/loop 5m /babysit         # auto-address review, rebase, shepherd PRs /loop 30m /slack-feedback # auto put up PRs for Slack feedback /loop 1h /pr-pruner       # close out stale PRs
```

#### /schedule for Cloud Jobs

Unlike `/loop`, scheduled jobs run in the **cloud** — they keep working even when your laptop is closed.

```
&gt; /schedule a daily job that looks at all PRs shipped since   yesterday and updates our docs based on the changes. Use   the Slack MCP to message #docs-update with the changes
```

> **Note:** Experiment with turning your most common workflows into a skill + a loop. It’s powerful.

---

## Mobile and remote control

#### Work from your phone

Claude Code has a **mobile app**—download the Claude app for iOS/Android and tap the Code tab. An **iMessage plugin** is also available (`/plugin install imessage@claude-plugins-official`) to send tasks from any Apple device.

#### Teleport sessions between devices

Move sessions back and forth between mobile, web, desktop, and terminal:

- `claude --teleport` (or `/teleport` from inside a session) continues a cloud session on your machine.
- `/remote-control` lets you control a local session from your phone or the web.
- `claude remote-control` lets you spawn a new local session from the mobile app. *Availability: Pro, Max, Team, and Enterprise plans on CLI v2.1.51+.*

You can also enable **“Enable Remote Control for all sessions”** in `/config`.

#### Claude Cowork Dispatch

Dispatch is a secure remote control for the Claude Desktop app. It can use your MCPs, browser, and computer with your permission—useful for catching up on Slack and emails, managing files, and doing things on your laptop when you’re away from it.

---

## Tool integrations (MCP)

Connect Claude to your existing tools so it can search Slack, run BigQuery, grab Sentry logs, and more. Add MCP servers via claude mcp add or the "mcpServers" block in settings.json — see **[code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)** for configuration.

#### Data and analytics

Ask Claude to use the `bq` CLI to pull and analyze metrics on the fly—keep a BigQuery skill checked into your codebase. The Claude Code team's take: “Personally, I haven’t written a line of SQL in 6+ months.” This works for any database that has a CLI, MCP, or API.

#### Bug fixing

Enable the Slack MCP, paste a bug thread into Claude, and just say **“fix”**—zero context switching. Or say **“go fix the failing CI tests”** without micromanaging how. Point Claude at **docker logs** to troubleshoot distributed systems—it’s surprisingly capable at this.

#### Plugins

Plugins bundle LSPs (available for every major language), MCPs, skills, agents, and custom hooks. Install from the official Anthropic plugin marketplace, or stand up an internal marketplace for your organization—then check the marketplace reference into `settings.json` so it’s auto-added for every developer. Run `/plugin` to get started.

---

## Customizing your environment

#### Terminal setup

Run `/config` to set light/dark mode and /terminal-setup to enable **Shift+Enter** for newlines in IDE terminals, Warp, or Alacritty (Apple Terminal is not supported by `/terminal-setup`). For Vim keybindings, open `/config` → Editor mode. The team recommends **Ghostty** for synchronized rendering and 24-bit color.

#### Status line, color, and keybindings

- `/statusline` generates a custom status line based on your `.bashrc`/`.zshrc`—show model, directory, remaining context, cost, or anything else.
- `/color` changes the prompt input color—useful when you have 3–5 sessions open and need to tell them apart at a glance.
- `/keybindings` remaps any key. Settings live-reload and are stored in `~/.claude/keybindings.json`.

#### Voice input

Voice mode is available to all users, including Claude Code Desktop and Cowork. Most of the Claude Code team's coding is done by speaking—you speak roughly 3× faster than you type, and your prompts get more detailed as a result.

- **CLI:** run `/voice` then hold the space bar
- **Desktop:** press the voice button (microphone icon)
- **iOS:** enable dictation in your system settings
- **macOS native:** hit fn×2 for system dictation in any terminal

#### Web sessions

Beyond the terminal, run additional sessions on [claude.ai/code](https://claude.ai/code). Use the `&` command to background a session, or the `--teleport` flag to switch contexts between local and web.

#### Output styles

Run `/config` and set an output style. **Explanatory** has Claude explain frameworks and patterns as it works (great for new codebases). **Learning** has Claude coach you through changes. You can also create **custom** styles to adjust Claude’s voice.

#### Spinner verbs

It’s the little things that make Claude Code feel personal. Ask Claude to customize your spinner verbs to add to or replace the default list. Check the `settings.json` into source control to share verbs with your team.

#### Customize everything

Claude Code is built to work great out of the box, but when you do customize, **check `settings.json` into git** so your team benefits too. Configuration is supported per-codebase, per-subfolder, per-user, or via enterprise-wide policies.

**By the numbers:** dozens of settings and environment variables—see the **[settings reference](https://code.claude.com/docs/en/settings)**. Use the `"env"` field in `settings.json` to avoid wrapper scripts.

---

## SDK and multi-repo work

#### --bare for Faster SDK Startup

By default, `claude -p` (and the TypeScript/Python SDKs) searches for local `CLAUDE.md` files, settings, and MCPs. For non-interactive usage, you usually want to specify these explicitly via `--system-prompt`, `--mcp-config`, `--settings`, etc. Add `--bare` for roughly 10× faster startup:

```
claude -p "summarize this codebase" \<br>    --output-format=stream-json \<br>    --verbose \<br>    --bare
```

> **Note:** This was a design oversight when the SDK was first built. In a future version, the default will flip to `--bare`. For now, opt in with the flag.

#### --add-dir for multi-repo work

When working across repositories, use `--add-dir` (or `/add-dir`) to give Claude access and permissions to additional folders. Or add `"additionalDirectories"` to your team’s `settings.json` to always include them.

#### Forking a session

To branch off an existing session, run `/branch` from inside it, or `claude --resume <session-id> --fork-session` from the CLI.

#### Setup scripts for cloud environments

In Claude Code on web and desktop, add a **setup script** that runs before each new cloud session—install dependencies, configure settings, set environment variables. The script is skipped on resume.

---

## Appendix: Quick reference

---

## Appendix: Related articles

Claude Code ships frequently. Verify version-specific details against **[code.claude.com/docs](https://code.claude.com/docs)** before distributing internally.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)
- [Claude Code communications kit](https://support.claude.com/en/articles/14555877-claude-code-communications-kit)
