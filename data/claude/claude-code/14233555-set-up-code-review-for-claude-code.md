---
title: "Set up Code Review for Claude Code"
title_slug: "set-up-code-review-for-claude-code"
source_url: "https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code"
last_updated_iso: "2026-03-25T21:47:21Z"
article_id: "16618815"
breadcrumbs:
  - "Claude Code"
---

# Set up Code Review for Claude Code

_Last updated: 2026-03-25T21:47:21Z_

Code Review analyzes your GitHub pull requests and posts findings as inline comments on the lines of code where it found issues. A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and regressions.

This article covers how to enable Code Review, configure review triggers, customize what gets flagged, and troubleshoot common setup issues.

> **Note: **Code Review is in research preview and available on Team and Enterprise plans. It isn’t available for organizations with zero data retention enabled. Code Review usage is billed separately through extra usage and doesn’t count against your plan’s included usage.

---

## How Code Review works

Once an organization enables Code Review, it can trigger automatically when a pull request opens, on every push, or only when someone manually requests a review. When a review runs, multiple agents analyze the diff and surrounding code in parallel. Each agent looks for a different class of issue, then a verification step checks results against actual code behavior to filter out false positives.

Findings are deduplicated, ranked by severity, and posted as inline comments on the specific lines where issues were found. If no issues are found, Claude posts a short confirmation comment on the PR. Reviews don’t approve or block your PR, so existing review workflows stay intact.

Reviews scale in cost with PR size and complexity, completing in 20 minutes on average.

#### Severity levels

Each finding is tagged with a severity level:

Findings include a collapsible extended reasoning section you can expand to see why Claude flagged the issue and how it verified the problem.

#### What Code Review checks

By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage. You can expand what it checks by adding guidance files to your repository.

---

## Set up Code Review

Owners and Primary Owners of Team and Enterprise plans can enable Code Review once for the organization and select which repositories to include. In addition to an owner role within your Claude organization, you’ll need permission to install GitHub Apps in your GitHub organization.

1. Go to **[Organization settings > Claude Code](http://claude.ai/admin-settings/claude-code)** and find the **Code Review** section.
2. Click “Configure” to begin the GitHub App installation flow.
3. Follow the prompts to install the Claude GitHub App to your GitHub organization. The app requests read and write permissions for contents, issues, and pull requests.
4. Choose which repositories to enable for Code Review. If you don’t see a repository, confirm you gave the Claude GitHub App access to it during installation.
5. Set a review trigger for each repository using the **Review Behavior** dropdown (see the next section for details on each option).

To verify setup, open a test PR. If you chose an automatic trigger, a check run named **Claude Code Review** should appear within a few minutes. If you chose Manual, comment “@claude review” on the PR to start the first review.

---

## Choose a review trigger

After setup, the **Code Review** section shows your repositories in a table. For each repository, choose when reviews run:

- **Once after PR creation: **The review runs once when a PR is opened or marked ready for review.
- **After every push: **The review runs on every push to the PR branch, catching new issues as the PR evolves. Claude auto-resolves threads when you fix previously flagged issues. This runs the most reviews and costs the most.
- **Manual: **Reviews start only when someone comments “@claude review” on a PR. Useful for high-traffic repos where you want to select which PRs get reviewed.

The repositories table also shows the average cost per review for each repo based on recent activity.

---

## Manually trigger reviews

Comment “@claude review” on a pull request to start a review and opt that PR into push-triggered reviews going forward. This works regardless of the repository’s configured trigger.

For the comment to trigger a review:

- Post it as a top-level PR comment, not an inline comment on a diff line.
- Put “@claude review” at the start of the comment.
- You must have owner, member, or collaborator access to the repository.
- The PR must be open and not a draft.

If a review is already running, the request is queued until the in-progress review completes.

---

## Customize reviews

Code Review reads two files from your repository to guide what it flags. Both are additive on top of the default correctness checks.

#### CLAUDE.md

Code Review reads your repository’s CLAUDE.md files and treats newly introduced violations as nit-level findings. If your PR changes code in a way that makes a CLAUDE.md statement outdated, Claude flags that the docs need updating too.

Claude reads CLAUDE.md files at every level of your directory hierarchy, so rules in a subdirectory’s CLAUDE.md apply only to files under that path.

#### REVIEW.md

Add a REVIEW.md file to your repository root for review-specific rules. Use it to encode:

- Company or team style guidelines
- Language- or framework-specific conventions not covered by linters
- Things Claude should always flag (for example, “any new API route must have an integration test”)
- Things Claude should skip (for example, “don’t comment on generated code”)

Claude auto-discovers REVIEW.md at the repository root. No configuration is needed.

---

## Pricing and usage

Code Review is billed based on token usage. Each review averages $15–25 in cost, scaling with PR size, codebase complexity, and how many issues require verification.

Code Review usage is billed separately through extra usage and doesn’t count against your plan’s included usage. The review trigger you choose affects total cost:

- **Once after PR creation** runs once per PR.
- **After every push** runs on each push, multiplying cost by the number of pushes.
- **Manual** incurs no cost until someone comments “@claude review.” After that comment, additional pushes to the PR trigger reviews automatically.

Costs appear on your Anthropic bill regardless of whether your organization uses AWS Bedrock or Google Vertex AI for other Claude Code features.

To set a monthly spend cap, go to **[Organization settings > Usage](https://claude.ai/admin-settings/usage)** and configure the limit for the Claude Code Review service.

Monitor spend via the weekly cost chart in the analytics dashboard or the per-repo average cost column in admin settings.

#### View usage

Go to the **[Code Review analytics dashboard](https://claude.ai/analytics/code-review)** to see activity across your organization. The dashboard shows:

- **PRs reviewed: **Daily count of pull requests reviewed over the selected time range.
- **Cost weekly: **Weekly spend on Code Review.
- **Feedback: **Count of review comments that were auto-resolved because someone addressed the issue.
- **Repository breakdown: **Per-repo counts of PRs reviewed and comments resolved.

---

## Troubleshooting

#### Repositories don’t appear after installing the GitHub App

If you’ve installed the Claude GitHub App but your repositories don’t appear in the admin panel:

1. Confirm the Claude GitHub App has access to the repositories you expect. Go to your GitHub organization’s settings, find the Claude GitHub App under **Installed GitHub Apps**, and check whether it has access to all repositories or only selected ones.
2. If your organization uses GitHub Enterprise Cloud with Enterprise Managed Users (EMU), make sure the Claude GitHub OAuth App is authorized at the enterprise level. EMU enterprises can restrict which OAuth apps are approved, and the Claude app must be explicitly allowed.
3. Try disconnecting and reconnecting the GitHub integration. Go to **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)**, remove the repository configuration, and run through setup again.
4. If the issue persists, **[contact our Support team](https://support.claude.com/en/articles/9015913-how-to-get-support)** with your organization name and GitHub organization name so we can investigate.

#### Code Review doesn’t start on a new PR

If no check run appears after opening a PR:

- Confirm the repository is listed and enabled in your admin settings.
- Check the review trigger setting. If it’s set to Manual, you’ll need to comment “@claude review” on the PR to start a review.
- Make sure the PR isn’t a draft. Code Review doesn’t run on draft PRs.
- Verify the Claude GitHub App still has access to the repository in your GitHub organization’s settings.

#### GitHub Enterprise Cloud with IP restrictions

If your GitHub Enterprise Cloud organization restricts access by IP address, the Claude GitHub App may be unable to access your repositories. To fix this, **[enable IP allow list inheritance for installed GitHub Apps](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#allowing-access-by-github-apps)** in your GitHub enterprise settings. The Claude GitHub App registers its IP ranges, so enabling this setting allows access without manual configuration. To **[add the ranges to your allow list manually](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization#adding-an-allowed-ip-address)** instead, or to configure other firewalls, see the **[Anthropic API IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)**.

#### GitHub Enterprise Server (self-hosted)

Code Review currently requires repositories hosted on **[github.com](http://github.com)**, so self-hosted GitHub Enterprise Server isn’t supported yet.

---

## Related resources

- **[Plugins](https://code.claude.com/docs/en/discover-plugins)** — Browse the plugin marketplace, including a code-review plugin for running on-demand reviews locally before pushing.
- **[GitHub Actions](https://code.claude.com/docs/en/github-actions)** — Run Claude in your own GitHub Actions workflows for custom automation beyond Code Review.
- **[GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd)** — Self-hosted Claude integration for GitLab pipelines.

## Related Articles
- [Automated Security Reviews in Claude Code](https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code)
- [Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Claude Code on the web](https://support.claude.com/en/articles/12618689-claude-code-on-the-web)
- [Claude Code: Common developer use cases](https://support.claude.com/en/articles/14553517-claude-code-common-developer-use-cases)
