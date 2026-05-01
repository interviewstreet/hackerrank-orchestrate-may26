---
title: "Automated Security Reviews in Claude Code"
title_slug: "automated-security-reviews-in-claude-code"
source_url: "https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code"
last_updated_iso: "2026-03-16T20:48:20Z"
article_id: "13147827"
breadcrumbs:
  - "Claude Code"
---

# Automated Security Reviews in Claude Code

_Last updated: 2026-03-16T20:48:20Z_

Claude Code now includes automated security review features to help you identify and fix vulnerabilities in your code. This guide explains how to use the /security-review command and GitHub Actions to improve your code security.

> **Note:** While automated security reviews help identify many common vulnerabilities, they should complement, not replace, your existing security practices and manual code reviews.

## Overview

Automated security reviews in Claude Code help developers catch vulnerabilities before they reach production. These features check for common security issues including SQL injection risks, cross-site scripting (XSS) vulnerabilities, authentication flaws, insecure data handling, and dependency vulnerabilities.

You can use security reviews in two ways: through the /security-review command for on-demand checks in your terminal, or through GitHub Actions for automatic review of pull requests.

## Availability

These features are available for all Claude Code users, including:

- Users on individual paid plans (Pro or Max).
- Individual users or enterprises with pay-as-you-go API Console accounts.

## Using the /security-review command

The /security-review command lets you run security analysis directly from your terminal before committing code.

#### Running a Security Review

To check your code for vulnerabilities:

1. Open Claude Code in your project directory.
2. Run /security-review in the terminal.
3. Claude will analyze your codebase and identify potential security concerns.
4. Review the detailed explanations provided for each issue found.

#### Implementing Fixes

After Claude identifies vulnerabilities, you can ask it to implement fixes directly. This keeps security reviews integrated into your development workflow, allowing you to address issues when they're easiest to resolve.

#### Customizing the Command

You can customize the /security-review command for your specific needs. See the[ security review documentation](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command) for configuration options.

## Setting up GitHub Actions for automated PR reviews

After installing and configuring the GitHub action, it will automatically review every pull request for security vulnerabilities when it's opened.

#### Installation

To set up automated security reviews for your repository:

1. Navigate to your repository's GitHub Actions settings
2. Follow the[ step-by-step installation guide](https://github.com/anthropics/claude-code-security-review) in our documentation
3. Configure the action according to your team's security requirements

#### How It Works

Once configured, the GitHub action:

- Triggers automatically when new pull requests are opened.
- Reviews code changes for security vulnerabilities.
- Applies customizable filtering rules to reduce false positives.
- Posts inline comments on the PR with identified concerns and recommended fixes.

This creates a consistent security review process across your entire team, ensuring code is checked for vulnerabilities before merging.

#### Customization Options

You can customize the GitHub action to match your team's security policies, including setting specific rules for your codebase and adjusting sensitivity levels for different vulnerability types.

## What security issues can be detected?

Both the /security-review command and GitHub action check for common vulnerability patterns:

- **SQL injection risks**: Identifies potential database query vulnerabilities.
- **Cross-site scripting (XSS)**:  Detects client-side script injection vulnerabilities.
- **Authentication and authorization flaws**: Finds issues with access control.
- **Insecure data handling**: Identifies problems with data validation and sanitization.
- **Dependency vulnerabilities**: Checks for known issues in third-party packages.

## Getting Started

To start using automated security reviews:

- **For the /security-review command**: Update Claude Code to the latest version (run), then run `/security-review` in your project directory.
  - Claude Code automatically keeps itself up to date to ensure you have the latest features and security fixes, but you can also run `claude update` to update manually.
- **For the GitHub actions**: Visit our[ documentation](https://github.com/anthropics/claude-code-security-review) for installation and configuration instructions.

## Best Practices

For optimal results, we recommend running /security-review before committing significant changes and configuring the GitHub action for all repositories containing production code. Consider adjusting the filtering rules based on your team's specific security requirements and codebase characteristics.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
- [Claude Security](https://support.claude.com/en/articles/14661296-claude-security)
