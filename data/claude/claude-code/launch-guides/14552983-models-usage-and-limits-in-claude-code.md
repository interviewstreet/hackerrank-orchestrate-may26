---
title: "Models, usage, and limits in Claude Code"
title_slug: "models-usage-and-limits-in-claude-code"
source_url: "https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code"
last_updated_iso: "2026-04-15T01:05:49Z"
article_id: "17024198"
breadcrumbs:
  - "Claude Code"
  - "Launch guides"
---

# Models, usage, and limits in Claude Code

_Last updated: 2026-04-15T01:05:49Z_

This guide explains which model you are using, how usage is metered, and how to keep long sessions within their context and usage limits.

---

## How usage is metered

How you signed in determines how usage is metered. Everything else about Claude Code behaves the same way regardless.

If you signed in with an Enterprise seat, you generally do not need to think about tokens until you reach a limit. If you are using an API key, the **`/cost`** command shows your running spend for the current session.

---

## Choosing a model

Run **`/model`** at any time to see which models are available to your account and to switch between them. As a rough guide:

- **Sonnet** is the default and is the right choice for the large majority of coding work. It is fast, capable, and cost-efficient.
- **Opus** offers deeper reasoning for harder problems such as large cross-cutting refactors, difficult debugging, or architectural decisions. It uses meaningfully more of your quota, so switch to it when you need it rather than leaving it on by default.
- **Haiku** is the fastest and cheapest option, well suited to quick lookups, simple edits, or high-volume scripted runs.

You can change models mid-session without losing your conversation. A common pattern is to plan with Opus and execute with Sonnet.

> **Note:** Exact model names, versions, and availability change over time. The `/model` command is always the source of truth for your account.

---

## What actually consumes tokens

Every turn sends three things to the model:

1. **The conversation so far** — every previous message in this session.
2. **Project context** — your `CLAUDE.md` and any files Claude has read.
3. **Your new prompt.**

Of these, the first item grows the fastest. A long debugging session in which Claude has read twenty files and produced fifteen diffs is carrying all of that on every subsequent message. This is where both cost and context limits originate.

---

## Managing the context window

The **context window** is the maximum amount of text the model can consider at once. Claude Code shows a live indicator of how full it is. When it fills up, Claude can no longer see the oldest parts of the conversation clearly and quality drops.

Two commands keep it under control:

- **`/clear`** wipes the conversation and starts fresh. Your `CLAUDE.md` and project files remain available; only the chat history is removed. Use this whenever you switch tasks, as it is the single most effective lever for both quality and cost.
- **`/compact`** summarizes the conversation so far into a short recap, freeing up space while preserving the essential context. Use this when you are mid-task and need to keep going. Claude Code also auto-compacts when you get close to the limit, so you will rarely hit a hard wall.

**Rule of thumb:** use `/clear` when starting a new task, and `/compact` when continuing a long one.

---

## Five habits that stretch your usage furthest

Almost every "I burned through my limit by lunchtime" report traces back to one of these five.

#### 1. Clear between tasks

Every previous message is resent on every turn, so a session that has wandered through three unrelated problems pays for all three on each new message.

**In practice:** you just finished debugging a login redirect and now want to write a database migration. Run `/clear` first. A simple test: if your next prompt would make perfect sense in a brand-new terminal, clear before sending it. Your `CLAUDE.md` and project files stay put; only the chat history goes.

**One warning:** `/clear` cannot be undone. If you might still need something from the history, copy it out first or run `/compact` instead, which preserves a summary rather than wiping everything.

#### 2. Match the model to the job

Opus costs several times more per turn than Sonnet, and Sonnet more than Haiku. Spending Opus on routine work is the fastest way to drain a daily limit.

**Reasonable defaults:** Sonnet for most coding (features, tests, known bugs, refactors); Opus when you're genuinely stuck or the change is wide (hard debugging, cross-cutting refactors, architecture calls); Haiku for quick mechanical work (renames, log lines, regex explanations, boilerplate).

#### 3. Point at files instead of pasting them

Anything you paste sits in context, in full, for the rest of the session. Referencing a file by path lets Claude read selectively and focus on the part you care about.

**In practice:** instead of pasting `auth.ts`, write look at the `validateToken` function in `src/auth.ts` — mentioning the path lets Claude open and read selectively. (Note that the @ prefix injects the entire file plus its `CLAUDE.md` tree into context, so use a bare path when you are trying to *save* tokens.) For logs and stack traces, trim to the relevant 20 or 30 lines before pasting. For anything large (lockfiles, build logs, data dumps), put it on disk and reference the path.

#### 4. Keep **CLAUDE.md** lean

This file is prepended to *every* turn. Prompt caching means turns after the first are billed at the much cheaper cache-read rate, so the dollar cost is lower than the raw line count suggests, but it still occupies context-window space on every message.

**The rule: two strikes, keep it tight.** Only add a note the second time you have to correct Claude on the same thing (first-time issues are usually one-offs). Keep the file under roughly 200 lines; if something new needs to go in and there's no room, something old has to come out.

**When to update it:** right after a session where you had to correct Claude twice on the same thing. That's when the fix is fresh and takes a minute to write down. Every few weeks, read the whole file and delete anything that is no longer true or whose purpose you can't remember. Stale notes are worse than missing notes because they actively misdirect Claude.

#### 5. Ask for a plan before big changes

A plan costs a few hundred tokens. A wrong 400-line diff that you revert and regenerate costs thousands, twice, plus the turns spent explaining what went wrong. **In practice:** for anything touching more than two or three files, switch to Plan Mode or just ask: "Before changing anything, list the files you'll touch and what you'll do in each." Read the list, correct it in plain English ("skip `legacy/`, and don't touch the tests yet"), then let it execute.

**Pro tip: plan with Opus, execute with Sonnet.** The highest-value use of Opus is writing the plan itself, where deeper reasoning actually pays off. Once a good plan exists, execution is mostly mechanical and Sonnet handles it at a fraction of the cost. This pattern is built in as `/model opusplan`, which uses Opus while planning and Sonnet for execution. Switching models doesn't clear the conversation, so Sonnet still sees everything Opus produced.

---

## What to do when you reach a limit

- **Enterprise seat users:** the message tells you when your window resets. In the meantime you can switch to a lighter model with `/model`, or, if your organization allows it, temporarily fall back to an API key.
- **API key users:** there is no usage cap, but check `/cost` and your Console or cloud-provider dashboard if spend is a concern. Unexpectedly high numbers almost always trace back to very long sessions that were never cleared.
- **Context window full** (which is different from a usage limit): run `/compact` to keep going, or `/clear` if the older history is no longer needed.

---

## Quick reference

## Related Articles
- [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Manage extra usage for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-extra-usage-for-paid-claude-plans)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
