---
title: "Claude Security"
title_slug: "claude-security"
source_url: "https://support.claude.com/en/articles/14661296-claude-security"
last_updated_iso: "2026-04-16T23:58:49Z"
article_id: "17192643"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Claude Security

_Last updated: 2026-04-16T23:58:49Z_

Claude Security is a capability built into **[Claude](https://claude.ai)** that scans codebases for security vulnerabilities and suggests targeted patches for human review. It helps teams find and fix issues that traditional methods often miss.

> Claude Security is now in research preview.

Claude Security lets you:

1. **Scan your code in parallel** — Claude Security understands context, traces data flows across files, and identifies complex, multi-component vulnerability patterns that traditional scanners might not detect.
2. **Validate findings** — Every finding goes through multi-stage verification, with Claude challenging its own results before surfacing them. The result: more real issues reported and fewer false positives.
3. **Review and patch** — Pivot directly from a finding into a Claude Code session to review the proposed fix. Resolve vulnerabilities quickly instead of growing a backlog.

To get started, see the **getting started guide**.

## Finding types

Each finding falls into one of the categories below.

#### Categories

## Severities

Severity is assigned per finding based on exploitability in your codebase, not the category itself—so the same category can land at different severities in different repos.

## Finding structure

Every scan finding includes the following fields:

## Frequently asked questions

- **Model selection** — Access to Mythos is limited to a small set of approved customers.
- **Scan length** — Scan time varies based on the repository and the agent's actions.
- **Severity configuration** — Severity isn't configurable today.
- **Non-GitHub repositories** — Only repositories hosted on GitHub can be scanned today.
- **Scan determinism** — Scans are non-deterministic, so a real issue may not surface in every scan. New findings are marked "new" in the console.

## Scope of use

You may only use Claude Security to scan code that your company owns and to which your company holds all necessary rights to scan. You may not use Claude Security to scan code owned by or licensed from third parties, including but not limited to open source projects or repositories other than those included in your company's codebase(s).

## Related Articles
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Using Claude in Chrome Safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)
- [Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
