---
title: "Claude Code model configuration"
title_slug: "claude-code-model-configuration"
source_url: "https://support.claude.com/en/articles/11940350-claude-code-model-configuration"
last_updated_iso: "2026-04-16T13:34:11Z"
article_id: "13159341"
breadcrumbs:
  - "Claude Code"
---

# Claude Code model configuration

_Last updated: 2026-04-16T13:34:11Z_

This guide shows you three ways to change which Claude model you're using with Claude Code: the quick `/model` command for instant changes, the `--model` flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

## Easiest method: Use /model command

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

1. Start Claude Code: `claude`
2. Type `/model` and choose your desired model from the interactive menu.
3. Your model change takes effect immediately.

> **Note:** You can check your current model anytime by running `/status` in Claude Code.

## Supported models

- Opus 4.7, `claude-opus-4-7`
- Sonnet 4.6, `claude-sonnet-4-6`
- Opus 4.6, `claude-opus-4-6`
- Opus 4.5, `claude-opus-4-5-20251101`
- Haiku 4.5, `claude-haiku-4-5-20251001`
- Sonnet 4.5, `claude-sonnet-4-5-20250929`

> **⚠️ Model access:** When using a Pro plan with Claude Code, you will only be able to use Opus models after **[enabling and purchasing extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans#h_8d1a703b92)**.

## Change model for current session only

Use the `--model` flag when starting Claude Code.

1. Start a fresh Terminal session.
2. Enter the following commands (depending on the model you’d like to use for that session):
  - **For Opus 4.7:** `claude --model claude-opus-4-7`
  - **For Sonnet 4.6: **`claude --model claude-sonnet-4-6`
  - **For Opus 4.6: **`claude --model claude-opus-4-6`
  - **For Opus 4.5: **`claude --model claude-opus-4-5-20251101`
  - **For Haiku 4.5: **`claude --model** **claude-haiku-4-5-20251001`
  - **For Sonnet 4.5:** `claude --model claude-sonnet-4-5-20250929`

## Change default model for all future sessions

**Step 1)** Check your shell type by running: `echo $SHELL`

- `/bin/zsh` → You're using zsh (macOS default)
- `/bin/bash` → You're using bash (Linux default)

**Step 2)** Add model setting to your shell config:

#### For ZSH users (macOS)

- Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.zshrc`
- Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.zshrc`
- Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.zshrc`
- Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc`
- Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.zshrc`
- Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.zshrc`

#### For BASH users (Linux)

- Opus 4.7: `echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.bashrc`
- Sonnet 4.6: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.bashrc`
- Opus 4.6: `echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.bashrc`
- Opus 4.5: `echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.bashrc`
- Haiku 4.5: `echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.bashrc`
- Sonnet 4.5: `echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.bashrc`

**Step 3)** Apply the changes:

- For ZSH: `source ~/.zshrc`
- For BASH: `source ~/.bashrc`

**Step 4)** Close Terminal completely, then reopen it.

**Step 5)** Start Claude Code in a fresh Terminal session: `claude`.

Now your chosen model will be the default for all future Claude Code sessions.

## Related Articles
- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)
- [How large is the Claude API’s context window?](https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window)
- [Using Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-using-claude-in-microsoft-foundry)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
- [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
