---
title: "Claude Code: Common developer use cases"
title_slug: "claude-code-common-developer-use-cases"
source_url: "https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases"
last_updated_iso: "2026-04-15T00:05:38Z"
article_id: "17024784"
breadcrumbs:
  - "Claude Code"
  - "Launch guides"
---

# Claude Code: Common developer use cases

_Last updated: 2026-04-15T00:05:38Z_

Claude Code is a command-line agent that runs in your terminal, reads your repository, edits files, executes commands, and requests confirmation before performing potentially destructive actions. It is designed to assist at every stage of the software development lifecycle—from exploring an unfamiliar codebase to shipping and maintaining production code.

The table below summarizes where Claude Code fits across the development lifecycle. The remainder of this article walks through the ten tasks developers most frequently use it for, with a sample prompt and expected result for each.

## How to use this guide

Each use case below includes when to use it, an example prompt, and the expected result. No configuration is required for any of them except §9 (issue-tracker integration), which requires a one-time MCP connector setup.

Use cases are ordered roughly by how early most developers encounter them. Select the one that matches your current task.

---

## Use cases

#### 1. Fix a failing test

**When to use this:** A test is failing and the cause is not immediately obvious. Use this to have Claude Code locate the root cause and propose a fix without you needing to identify the source file first.

**Example prompt:**

```
&gt; the tests in tests/auth.test.ts are failing, can you figure out why and fix them
```

**Expected result:** Claude Code reads the test file, traces the code path through the modules under test, identifies the mismatch, and proposes an edit. After you approve the change, it re-runs the test suite to confirm the fix.

#### 2. Understand unfamiliar code

**When to use this:** You need to understand how a module, function, or subsystem works before making changes—for example, when inheriting code or reviewing an unfamiliar area.

**Example prompt:**

```
&gt; walk me through how the payment retry logic works
```

**Expected result:** Claude Code locates the relevant files, reads the implementation, and explains the control flow in plain language: entry points, decision branches, edge cases, and how the code connects to the rest of the system. Ask follow-up questions (e.g., “where does X get set”) to drill deeper.

## 3. Find where something happens

**When to use this:** You know a behavior exists in the codebase but cannot locate it via filename or simple text search.

**Example prompt:**

```
&gt; where do we validate email addresses in this codebase? I want to add a new rule
```

**Expected result:** Claude Code searches the repository, opens candidate files, and returns file paths and line numbers with enough surrounding context to identify the correct match. If multiple locations exist, it indicates which one is the source of truth.

#### 4. Triage an error or stack trace

**When to use this:** You have a runtime error, stack trace, or log output and need to map it back to the responsible code.

**Example prompt:**

```
&lt;table class="prompt"&gt; &lt;colgroup&gt; &lt;col style="width: 100%" /&gt; &lt;/colgroup&gt;<br>&lt;tbody&gt; &lt;tr class="odd"&gt; &lt;td&gt;&amp;gt; getting this in production:&lt;br /&gt;<br>TypeError: Cannot read properties of undefined (reading 'sessionId')&lt;br /&gt;    <br>at validateSession (src/auth/session.ts:47)&lt;br /&gt;     at middleware<br>(src/auth/middleware.ts:12)&lt;br /&gt; what's going on?&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt;<br>&lt;/table&gt;
```

**Expected result:** Claude Code reads the files referenced in the trace, explains what is undefined and why, and proposes a fix. For errors without a clean stack trace, paste any available log output and Claude Code will reconstruct the failure from context.

#### 5. Refactor with a plan

**When to use this:** A change spans multiple files and you want to review the full scope before any edits are made.

**Prerequisite:** Press **Shift+Tab** until the mode indicator shows “plan."

**Example prompt:**

```
&gt; refactor the auth module to use the new session store instead of SessionCache
```

**Expected result:** Claude Code analyzes the code and produces a numbered plan listing every file it will modify and the change in each. You can approve the plan as-is or amend it (e.g., “don’t touch the logout route”). No files are edited until you approve.

**Reference:** **[Permissions](https://code.claude.com/docs/en/permissions)**

#### 6. Write tests for existing code

**When to use this:** A source file lacks coverage, or you need additional edge-case tests that match your project’s existing test conventions.

**Example prompt:**

```
&gt; add tests for @src/billing/invoice.ts — cover the edge cases around partial refunds. match the style of the existing tests in tests/billing/
```

**Expected result:** Claude Code reads both the source file and the reference test directory, generates a new test file in the existing style, and runs it to confirm the tests pass. If obvious coverage gaps remain, it flags them and asks whether to address them.

#### 7. Review a pull request

**When to use this:** You need to review or summarize a PR, particularly in an area of the codebase you do not know well.

**Prerequisite:** GitHub CLI authenticated (run `gh auth login` once).

**Example prompt:**

```
&gt; /pr https://github.com/example/api/pull/4471<br>&gt; is the error handling solid?
```

**Expected result:** Claude Code fetches the diff, review comments, and CI status, then reads the changed files in their full repository context. It can produce a focused review, draft review comments, verify a specific concern, or summarize the PR.

#### 8. Onboard to a new repository

**When to use this:** You are working in a repository for the first time and need a structured overview of its architecture, build commands, and conventions.

**Example prompt:**

```
&lt;table class="prompt"&gt; &lt;colgroup&gt; &lt;col style="width: 100%" /&gt; &lt;/colgroup&gt;<br>&lt;tbody&gt; &lt;tr class="odd"&gt; &lt;td&gt;&amp;gt; /init&lt;br /&gt; &amp;gt; give me a tour of this<br>codebase — where's the entry point, how is it structured, what should I<br>read first&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;
```

**Expected result:** `/init` scans the project and writes a `CLAUDE.md` file summarizing build commands, architecture, and conventions. The follow-up tour prompt produces a guided walkthrough of the project structure. Project context remains loaded for the rest of the session.

**Reference:** **[Memory and CLAUDE.md](https://code.claude.com/docs/en/memory)**

#### 9. Work an issue end to end

**When to use this:** You want to read a ticket, implement the fix, and validate it in a single conversation without switching tools.

**Prerequisite:** Issue tracker connected via MCP (one-time `.mcp.json` configuration).

**Example prompt:**

```
&lt;table class="prompt"&gt; &lt;colgroup&gt; &lt;col style="width: 100%" /&gt; &lt;/colgroup&gt;<br>&lt;tbody&gt; &lt;tr class="odd"&gt; &lt;td&gt;&amp;gt; what's the top-priority issue assigned<br>to me?&lt;br /&gt; &amp;gt; go ahead and fix it&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;
```

**Expected result:** Claude Code queries the issue tracker, reads the ticket, locates the relevant code, proposes a fix, and runs the tests. The session ends with a reviewable diff and the context needed to close the ticket.

**Reference:** **[MCP](https://code.claude.com/docs/en/mcp)**

#### 10. Turn a recurring task into a Skill

**When to use this:** You repeat the same multi-step prompt regularly (pre-commit checks, standup summaries, PR descriptions, release notes) and want to make it reusable for the whole team.

**Example prompt:**

```
&gt; make me a /ship skill that runs the tests, runs the linter, looks at git diff, and drafts a conventional-commit message — then shows me the message without committing
```

**Expected result:** Claude Code writes a `SKILL.md` file to `.claude/skills/ship/`. The `/ship` command is available immediately, with no restart required, and is shared with anyone who clones the repository. (The legacy `.claude/commands/` path is still supported, but skills are the recommended form.)

**Reference:** **[Skills](https://code.claude.com/docs/en/skills)**

## Appendix: Quick reference

## Appendix: Resource directory

For details on `/init`, @-references, permission modes, skills, MCP, and hooks, see **[code.claude.com/docs](https://code.claude.com/docs)**. Claude Code ships frequently—verify version-specific details against **[code.claude.com/docs](https://code.claude.com/docs)** before distributing internally.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips)
- [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)
- [Claude Code communications kit](https://support.claude.com/en/articles/14555877-claude-code-communications-kit)
