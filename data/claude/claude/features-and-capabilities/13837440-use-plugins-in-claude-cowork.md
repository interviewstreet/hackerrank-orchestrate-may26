---
title: "Use plugins in Claude Cowork"
title_slug: "use-plugins-in-claude-cowork"
source_url: "https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork"
last_updated_iso: "2026-04-09T14:02:42Z"
article_id: "16045566"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use plugins in Claude Cowork

_Last updated: 2026-04-09T14:02:42Z_

> Plugins are available to all Claude Cowork users on paid plans (Pro, Max, Team, Enterprise).

Plugins customize how Claude works for your role, team, and company in Cowork. Each plugin bundles together skills, connectors, and sub-agents into a single package—so instead of setting up each piece individually, you get a ready-to-go setup from the first conversation.

Claude also connects to services like Google Drive, Gmail, Slack, DocuSign, and many more. Plugins can bundle the right connectors for a given workflow so you don't have to set them up individually.

> **Note:** Connectors in Cowork reach external services through Anthropic's cloud, not through your local network. Even though Cowork runs on your computer, a custom connector must point to a server that's reachable over the public internet from Anthropic's IP ranges. If your organization's MCP servers are behind a firewall or on a private network, see **[Network requirements for custom connectors](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp#h_b66e88c454)**.

---

## Browse available plugins

Cowork includes a growing library of plugins for common knowledge work—including sales, finance, legal, marketing, HR, engineering, design, operations, data analysis, and more. Each one comes pre-configured with the skills and connectors relevant to that function.

We also provide **Plugin Create**, a plugin that helps you build custom plugins from scratch.

For the full collection of Anthropic-built plugins, visit **[GitHub](https://github.com/anthropics/knowledge-work-plugins)**.

> **Note:** Plugins may include local MCP servers that run on your computer with the same permissions as any other program you run. Only install plugins from sources you trust. If your organization is on an Enterprise plan, your admin may have restricted which plugins you can install, or disabled local MCP servers entirely.

---

## Install a plugin

1. Open the Claude Desktop app and switch to the “Cowork” tab.
2. Click the “Customize” menu in the left sidebar, which brings together your plugins, skills, and connectors in one place.
3. Click “Browse plugins” to open a modal where you can view all the available options.
4. Click “Install” on your selected plugin.
5. You can also upload a custom plugin file if you've built one yourself or received one from a colleague.

Plugins you add yourself are saved locally to your machine.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2100409211/fc01614dde1a616fa31ffaa9cb04/47bacf5b-a810-45b5-a468-9769f1a58ef8?expires=1776784500&signature=78f65ecd3686b9cb436a0337cb148f1e1a74dec22c4672171228fdb6f3215abc&req=diEnFs1%2BlINeWPMW1HO4zZF3LRPaO%2FFQxakFVfq5WwyLr2xlPcLNKZFaiFwz%0A5l81w%2BnHxxwhmXLB2nc%3D%0A)

---

## Use Skills

Each plugin you install adds Skills you can use while working in Cowork. Type "/" or click the "+" button to see available Skills from your installed plugins.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2157396844/4a790e10f5b88df770783df1d7e9/image.png?expires=1776784500&signature=36a7542bc0ee454c16781955d7f66051596071f476c2b808fb76ec24625d7d31&req=diEiEcp3m4lbXfMW1HO4zf4NC%2FD7i0SRmKUxugP2BQs30jcsjchjHGosCRc9%0AGF2kAvcAPXYqRg7zwgA%3D%0A)

---

## Customize a plugin

After installing a plugin, you can tailor it to better fit your workflow:

1. While viewing an installed plugin, click “Customize” in the upper right corner.
2. This opens a new Cowork task with a prompt asking Claude to customize the plugin you chose.
3. Click “Let's go” to start working with Claude to adjust the plugin's Skills and connectors to match how you work.

---

## Build your own plugin

Want to create something from scratch? Cowork includes **Plugin Create**, a built-in plugin that walks you through the process. You can also start from any of the Anthropic-built templates and modify them.

For details on plugin structure and formatting, see the **[Plugins reference](https://code.claude.com/docs/en/plugins-reference)** in our Claude Code docs.

---

## Organization-managed plugins

If you're on a Team or Enterprise plan, an owner can distribute plugins across your organization through plugin marketplaces. These work the same as any other plugin, with a couple of differences:

- You can't edit organization-managed plugins. This keeps shared tooling consistent across your team.
- Some plugins may be auto-installed or required for you. You can uninstall auto-installed plugins if you don't need them, but required plugins can't be removed.
- Available organization plugins show up when you browse the plugin catalog, and you can install them yourself.

On Enterprise plans, your admin may customize which plugins are available to your group. This means the plugins you see in the catalog may differ from what colleagues in other groups see.

For guidance on setting up and managing plugins organization-wide, see **[Manage Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-cowork-plugins-for-your-organization)**.

## Related Articles
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Manage Claude Cowork plugins for your organization](https://support.claude.com/en/articles/13837433-manage-claude-cowork-plugins-for-your-organization)
- [Install financial services plugins for Cowork](https://support.claude.com/en/articles/13851150-install-financial-services-plugins-for-cowork)
- [Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)
