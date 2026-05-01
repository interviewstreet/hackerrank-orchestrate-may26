---
title: "Using the GitHub Integration"
title_slug: "using-the-github-integration"
source_url: "https://support.claude.com/en/articles/10167454-using-the-github-integration"
last_updated_iso: "2026-04-15T01:58:38Z"
article_id: "10707782"
breadcrumbs:
  - "Connectors"
  - "Pre-Built Connectors"
---

# Using the GitHub Integration

_Last updated: 2026-04-15T01:58:38Z_

> For more information on enabling GitHub within your account, see **[Connect a service to Claude](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities#h_c228562ecd)**.

Connect your GitHub repositories directly to Claude to provide comprehensive context for your software development tasks. You can easily add repositories by selecting them from a list, helping Claude better understand and assist with your codebase.

How to add GitHub repositories

> **Note:*** *If you're currently unauthenticated with GitHub, you'll be redirected to GitHub to authenticate before you can use this integration.

## Chats

- Click the "+" button on the lower left corner of the chat interface.
- Select "Add from GitHub" from the drop-down.
- Use the file browser to select specific files and folders.
- When you send your message, Claude will access and process the content to inform its response.

## Projects

- Click the "+" button in the upper right corner of your project knowledge section.
- Select "GitHub" from the drop-down.
- Search through your accessible repositories, or paste a repository URL.
- Use the file browser to select specific files and folders.
- Your selected content will be added to the project knowledge for Claude to access and process.
- You can use the "Sync" icon to ensure you're working with the most up-to-date version of your codebase.
- You can use the "Configure files" icon to modify which files and folders Claude analyzes.

Connecting to private repositories

If Claude cannot access a repository after you enter a valid URL, it most likely means you're attempting to connect Claude to a private repository:

Follow the link to our GitHub App, where you can grant access to repos if you're a GitHub administrator, or send a request to your GitHub organization's administrators.

- **Grant access yourself if you can**: You can choose between letting Claude access all repos or specific ones.
- **Request access if you don't have the necessary permissions**: The administrators of your GitHub organization will receive an email notification about your request. Once they approve the request, you'll be able to sync and access the repository in Claude.

Best Practices

1. **Start small**: Begin by selecting a small subset of your codebase to analyze. This will help you get familiar with how Claude interprets and discusses your code.
2. **Iterate and refine**: If Claude's initial response doesn't fully address your question, don't hesitate to ask follow-up questions or request clarification.
3. **Combine with human expertise**: Use Claude's insights as a starting point for further investigation and discussion with your team. Please review Claude's work.
4. **Thoughtful file selection**: When using "Configure files", be strategic about your selections. Include key files and directories that are central to your current task or project, but avoid selecting unnecessary files to keep within token limits and maintain focus.
5. **Regular updates**: Remember to refresh your project's GitHub sync periodically to ensure Claude is working with the most up-to-date version of your codebase and especially before starting a new analysis or when you know there have been significant changes to your repo.

Frequently Asked Questions

**Q: What information is retrieved from GitHub?**

A: Only files (names and contents) in a repo on a specific branch are synced. We do not retrieve commit history, PRs, or other metadata.

**Q: What happens if my repository is updated after adding it to a project?**

A: You can click "Sync now" to fetch the latest changes from your repository. This will update all previously selected files and folders.

**Q: Can I add multiple repositories to a single project or chat?**

A: Yes, you can add multiple repositories to provide Claude with comprehensive context for your development tasks. The repositories must fit within Claude's context window.

**Q: What happens if I lose access to a repository?**

A: If you lose access to a repository, you won't be able to view its contents in projects where it was previously added. The repository preview will be removed, though the conversation history will be maintained.

Browse all available connectors in the [Connectors Directory](https://claude.ai/directory).

## Related Articles
- [Automated Security Reviews in Claude Code](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)
- [Manage Claude Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Security](https://support.claude.com/en/articles/14661296-claude-security)
