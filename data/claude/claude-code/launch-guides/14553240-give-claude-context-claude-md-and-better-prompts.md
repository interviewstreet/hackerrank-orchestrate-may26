---
title: "Give Claude context: CLAUDE.md and better prompts"
title_slug: "give-claude-context-claudemd-and-better-prompts"
source_url: "https://support.claude.com/en/articles/14553240-give-claude-context-claude-md-and-better-prompts"
last_updated_iso: "2026-04-15T01:20:31Z"
article_id: "17024481"
breadcrumbs:
  - "Claude Code"
  - "Launch guides"
---

# Give Claude context: CLAUDE.md and better prompts

_Last updated: 2026-04-15T01:20:31Z_

Claude Code works well out of the box, but it becomes noticeably more effective once it knows your project's conventions and once you adopt a few prompting habits. This guide covers both.

---

## Part 1 — CLAUDE.md: your project's memory

#### What it is

`CLAUDE.md` is a plain markdown file that Claude automatically reads at the start of **every** session in that directory. Think of it as the briefing you would give a capable new teammate on their first morning: how the team does things, what to avoid, and where the important pieces live.

You do not need to reference it in prompts or attach it manually. If the file exists, Claude has already read it.

#### Where it lives

Claude looks in a few places and merges what it finds, from broad to specific:

Most teams only need the project-root file. Commit it to git so the whole team benefits.

#### How it's loaded (and what it costs)

The files at and above your working directory are read at session start and delivered to Claude as a user message immediately after the system prompt (not embedded inside the system prompt itself). Subdirectory `CLAUDE.md` files are loaded on demand later, when Claude reads files in that subdirectory. There is no summarization or truncation, and it is not re-read from disk on each turn. If you edit the file mid-session, the change is picked up the next time you run `/compact` or open it via `/memory`; otherwise it takes effect on your next session.

For Claude for Enterprise customers, the cost picture is better than "loaded on every request" might suggest. Claude Code applies Anthropic's prompt caching to `CLAUDE.md`. The first request in a session pays the full input-token price for the file; subsequent requests within roughly five minutes of each other hit the cache and are billed at the much lower cache-read rate. The cache is content-addressed, so any change to `CLAUDE.md` invalidates it and the next request pays full price again.

In practice this means a sizeable `CLAUDE.md` costs full tokens once per session, plus once after any idle gap long enough for the cache to expire, rather than once per message. It is still worth keeping the file lean for context-window space and signal-to-noise, but you do not need to ration lines purely to control per-message spend. In the Enterprise usage dashboard, the file's footprint will show up almost entirely as cache-read tokens rather than standard input tokens.

#### Getting started: run `/init`

In any project, type `/init`. Claude will explore the codebase and draft a `CLAUDE.md` for you, covering build commands, test commands, a structure overview, and any conventions it detects. Review the draft, remove anything inaccurate, and commit it. This takes about five minutes and pays off permanently.

#### What actually belongs in it

Aim for a file that is short and signal-dense — under roughly 200 lines. Every line is loaded into context on every request, so each one should be worth its cost.

**Worth including:**

- **Commands** — how to build, test, lint, and run locally. Claude will execute these, so accuracy matters.
- **Conventions** — naming, error handling, file layout, and "we use X, not Y" decisions.
- **Architecture in three sentences** — what the major pieces are and how they communicate.
- **Hard constraints** — for example, "never write to the production database from tests," "all API routes need auth middleware," or "do not edit `generated/`."
- **Known gotchas** — the issues every new engineer trips on.

**Not worth including:**

- Full API documentation (Claude can read the code directly).
- Changelogs or history.
- Anything that is already obvious from the file tree.
- Aspirational rules the team does not actually follow.

#### How often to update it

Treat it like a living onboarding doc, not a spec.

- **After `/init`** — review once to clean up the generated draft.
- **When Claude gets something wrong twice** — that is the signal a rule is missing. Add one line to address it.
- **When conventions change** — for example, a new framework, test runner, or set of lint rules.
- **Quarterly skim** — delete anything stale, since outdated instructions are worse than none.

You can also add to it mid-session: open `/memory`  to edit the file directly, or just ask Claude to "remember" a rule and it will append it to the right `CLAUDE.md` for you.

---

## Part 2 — Prompting habits that pay off in Claude Code

These are not generic prompt-engineering tips; they are the habits that matter most specifically when Claude is reading and editing a real codebase.

#### 1. State the outcome, not the steps

Claude can explore the codebase itself. Tell it *what* you want and *why*, and let it figure out *where*.

❌ "Open `userService.ts`, find the `validate` function, add a null check on line 42."

✅ "Users with no email are crashing the validation step. Make it handle that gracefully and add a test."

#### 2. Give it the error, verbatim

Paste the full stack trace rather than summarizing it. The exact filename, line number, and message are what allow Claude to find the right location quickly.

#### 3. Scope big tasks with Plan Mode first

For anything touching more than a couple of files, press **Shift+Tab** twice to cycle into plan mode (the first press enters acceptEdits) and ask:

*"Plan how you'd add rate limiting to the public API. Don't change anything yet."*

Review the plan, adjust it in conversation, then switch modes and say "do step 1." This catches misunderstandings before they turn into a twelve-file diff.

#### 4. Point at files when you already know them

Claude can search the codebase on its own, but if you already know the relevant file, say so — it is faster and uses fewer tokens. Use `@` to reference paths, for example `@src/auth/login.ts`.

#### 5. Say what "done" looks like

Examples include "tests pass," "matches the style of the other handlers," or "no new dependencies." Stating acceptance criteria up front is more efficient than several rounds of revision.

#### 6. One task per conversation; `/clear` between them

Long sessions accumulate noise. When you switch from "fix the login bug" to "refactor the billing module," run `/clear` and start fresh. Your `CLAUDE.md` carries the durable context forward, so the chat history does not need to.

#### 7. Correct it like a colleague, not a search engine

If the first answer is off, you do not need to rephrase the whole request. Simply say what is wrong — for example, *"That changes the public API; keep the signature the same."* Claude will keep everything else and adjust only that point.

---

## Quick reference

## Related Articles
- [Your first day in Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)
- [Claude Code communications kit](https://support.claude.com/en/articles/14555877-claude-code-communications-kit)
