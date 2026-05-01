---
title: "Install financial services plugins for Cowork"
title_slug: "install-financial-services-plugins-for-cowork"
source_url: "https://support.claude.com/en/articles/13851150-install-financial-services-plugins-for-cowork"
last_updated_iso: "2026-03-16T21:32:54Z"
article_id: "16062900"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Install financial services plugins for Cowork

_Last updated: 2026-03-16T21:32:54Z_

We offer a set of open-source plugins that extend Cowork with specialized capabilities for financial services workflows, including financial modeling, equity research, investment banking, private equity, and wealth management.

These plugins are available in a **[public GitHub repository](https://github.com/anthropics/financial-services-plugins/tree/main?tab=readme-ov-file#claude-for-financial-services-plugins)** that you can add as a marketplace in Cowork.

## What's included

The repository contains a **core plugin** and several **add-on plugins** that build on it:

- **Financial analysis** (core) — Build comparable company analyses, DCF models, LBO models, and 3-statement financials. This plugin also includes all shared MCP connectors for financial data providers. **Install this first.**
- **Investment banking** — Draft CIMs, teasers, and process letters. Build buyer lists, run merger models, and create strip profiles.
- **Equity research** — Write earnings updates and initiating coverage reports. Track catalysts and screen for new ideas.
- **Private equity** — Source and screen deals, run due diligence checklists, draft IC memos, and monitor portfolio company KPIs.
- **Wealth management** — Prep for client meetings, build financial plans, rebalance portfolios, and identify tax-loss harvesting opportunities.

The repository also includes partner-built plugins from **LSEG** and **S&P Global**, which bring their financial data and analytics directly into Cowork.

## Add the marketplace

1. Open the Claude Desktop app.
2. Look for the mode selector at the top of the app that includes "Chat" and “Cowork.”
3. Click the "Cowork" tab.
4. Click “Customize” on the left sidebar.
5. Click “Browse plugins.”
6. Select “Personal.”
7. Click the “+” button, then select **Add marketplace from GitHub**.
8. Enter the repository URL: **[https://github.com/anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins)**
9. Once added, you'll see the available financial services plugins in your marketplace.

## Install plugins

1. From your plugin marketplace, browse the available financial services plugins.
2. Install the **financial analysis** plugin first—this is the core plugin that provides shared tools and data connectors used by all other plugins.
3. Install any additional plugins based on your workflow needs.

Once installed, plugins activate automatically. Skills are applied when relevant, or you can invoke them manually during your Cowork session by typing "/" or clicking the "+" button.

## Available Skills

After installation, you can use Skills like:

- /comps [company] — Run a comparable company analysis
- /dcf [company] — Build a DCF valuation model
- /earnings [company] [quarter] — Generate a post-earnings update report
- /one-pager [company] — Create a one-page company profile
- /ic-memo [project name] — Draft an investment committee memo
- /source [criteria] — Source deals based on criteria
- /client-review [client] — Prep for a client meeting

## MCP connectors

The financial analysis core plugin includes connectors for third-party financial data providers such as Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and Egnyte.

Access to these connectors may require a separate subscription or API key from the respective provider. Contact your data provider for details.

## Customize plugins for your firm

These plugins are designed as starting points. You can customize them to match your firm's workflows by editing the plugin files directly:

- Add your firm's terminology, processes, and formatting standards to skill files.
- Swap or add MCP connectors to point at your specific data providers.
- Adjust workflow instructions to reflect how your team does analysis.
- Use /ppt-template to teach Claude your firm's branded PowerPoint layouts.

## Good to know

- Plugins are file-based (Markdown and JSON) — no code or infrastructure required to customize.
- These plugins work across both Cowork and Claude Code.
- AI-generated financial analysis should always be reviewed by qualified professionals before being used in decision-making.

## Learn more

See our blog post for more information: **[Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance)**.

## Related Articles
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Manage Claude Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
