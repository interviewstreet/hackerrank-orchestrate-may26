---
title: "Managing API key environment variables in Claude Code"
title_slug: "managing-api-key-environment-variables-in-claude-code"
source_url: "https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code"
last_updated_iso: "2026-03-16T21:22:36Z"
article_id: "13676744"
breadcrumbs:
  - "Claude Code"
---

# Managing API key environment variables in Claude Code

_Last updated: 2026-03-16T21:22:36Z_

## Understanding authentication priority in Claude Code

When using Claude Code, it's important to understand how authentication methods are prioritized to avoid unexpected API charges and ensure you're using your intended account.

## How authentication works

- Claude Code prioritizes environment variable API keys over authenticated subscriptions.
- This is intentional behavior designed to give you flexibility in choosing your authentication method.
- When an API key is set as an environment variable, you'll be charged via API pay-as-you-go rates using the API account associated with that key.
- This happens even if you're logged into Claude Code with a claude.ai subscription or a different Console account.

## Best practices

**To use Claude Code with your Claude subscription:** Keep the ANTHROPIC_API_KEY environment variable unset.

- This prevents unexpected API charges and ensures you're using your subscription's included usage.
- If you need to use a specific API key occasionally, set it temporarily only when needed.
- Run /status in Claude Code periodically to verify your current authentication method.

## Authentication conflict warnings

Claude Code will notify you when there's a conflict between your authenticated subscription and an environment variable API key:

1. During initial setup, if an API key is detected in your environment variables, Claude Code will ask you to confirm which authentication method you want to use.
2. After successful login, you'll see a notification if both credentials are active, alerting you to the potential for unexpected API charges.

## Checking your current configuration

To verify if an API key is set as an environment variable, run /status in Claude Code. This will show you which authentication method is currently active.

To check your environment variable directly, run one of these commands in a terminal (outside of Claude Code):

macOS/Linux:

```
echo $ANTHROPIC_API_KEY
```

Windows CMD:

```
echo %ANTHROPIC_API_KEY%
```

Windows PowerShell:

```
echo $env:ANTHROPIC_API_KEY
```

## Setting an API key temporarily

If you need to use an API key for the current terminal session only:

macOS/Linux:

```
export ANTHROPIC_API_KEY='your-api-key-here'
```

Windows CMD:

```
set ANTHROPIC_API_KEY=your-api-key-here
```

Windows PowerShell:

```
$env:ANTHROPIC_API_KEY="your-api-key-here"
```

## Setting an API key environment variable permanently

macOS/Linux:

```
For zsh (default on macOS):<br>bash<br># Add to shell config file<br>echo 'export ANTHROPIC_API_KEY="your-api-key-here"' &gt;&gt; ~/.zshrc<br><br># Apply changes<br>source ~/.zshrc<br>For bash:<br>bash<br># Add to shell config file<br>echo 'export ANTHROPIC_API_KEY="your-api-key-here"' &gt;&gt; ~/.bash_profile<br><br># Apply changes<br>source ~/.bash_profile
```

Windows:

1. Open System Properties → Advanced → Environment Variables
2. Under "User variables", click "New"
3. Variable name: ANTHROPIC_API_KEY
4. Variable value: your-api-key-here
5. Click OK and restart your terminal

## Removing an API key environment variable

macOS/Linux (temporary):

```
unset ANTHROPIC_API_KEY
```

macOS (permanent):

```
# Remove from config file<br>sed -i '' '/ANTHROPIC_API_KEY/d' ~/.zshrc<br>source ~/.zshrc
```

Linux (permanent)

```
sed -i '/ANTHROPIC_API_KEY/d' ~/.zshrc
```

Windows CMD:

```
set ANTHROPIC_API_KEY=
```

Windows PowerShell:

```
Remove-Item Env:ANTHROPIC_API_KEY
```

Windows (permanent): Delete the variable from System Environment Variables settings.

## Common issues to avoid

- Setting environment variables in shell configuration files and forgetting about them.
- Not restarting your terminal after changing environment variables.
- Assuming you're using your subscription when an API key is configured in your environment.

If you have any questions, please [contact our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support).

## Related Articles
- [Using Claude Code with your Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-max-plan)
- [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Your first day in Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code)
- [Troubleshoot Claude Code installation and authentication](https://support.claude.com/en/articles/14552646-troubleshoot-claude-code-installation-and-authentication)
