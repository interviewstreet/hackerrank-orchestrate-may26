---
title: "What are Skills?"
title_slug: "what-are-skills"
source_url: "https://support.claude.com/en/articles/12512176-what-are-skills"
last_updated_iso: "2026-03-31T20:36:50Z"
article_id: "13961678"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# What are Skills?

_Last updated: 2026-03-31T20:36:50Z_

Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

> Skills are available for users on Free, Pro, Max, Team, and Enterprise plans. This feature requires **[code execution to be enabled](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)**. Skills are also available in beta for Claude Code users and for all API users using the code execution tool.

---

## How do Skills work?

Skills improve Claude’s consistency, speed, and performance on many tasks. Skills work through progressive disclosure—Claude determines which Skills are relevant and loads the information it needs to complete that task, helping to prevent context window overload.

When you ask Claude to complete a task, it reviews available Skills, loads relevant ones, and applies their instructions.

---

## Types of Skills

#### Anthropic Skills

These are Skills created and maintained by Anthropic, such as enhanced document creation for Excel, Word, PowerPoint, and PDF files. Anthropic Skills are available to all users and Claude invokes them automatically when relevant.

#### Custom Skills

These are Skills you or your organization create for specialized workflows and domain-specific tasks. Here are some potential workflows you could enable using custom Skills:

- Apply brand style guidelines to documents and presentations.
- Generate communications following company email templates.
- Structure meeting notes with company-specific formats.
- Create tasks in company tools (JIRA, Asana, Linear) following team conventions.
- Execute company-specific data analysis workflows.
- Automate personal workflows and customize Claude to match your work style.

#### Organization provisioned skills

For Team and Enterprise plans, organization Owners can provision skills for all users. Skills provisioned in this way appear automatically in every team member's Skills list and can be set as enabled or disabled by default. This allows organizations to:

- Distribute approved workflows consistently across all employees
- Ensure teams use standardized procedures and best practices
- Deploy new capabilities without requiring individual uploads

Learn more about provisioning skills in **[Provision and manage Skills for your organization](https://support.claude.com/en/articles/13119606-managing-skills-as-an-admin)**.

#### Partner skills

The Skills Directory features professionally-built skills from partners like Notion, Figma, Atlassian, and others. These skills are designed to work seamlessly with their respective MCP connectors, enabling powerful integrated workflows.

---

## Key benefits

**Improvement in Claude’s performance of specific tasks**: Skills provide specialized capabilities for tasks like document creation, data analysis, and domain-specific work that requires supplementing Claude's general knowledge.

**Organizational knowledge capture**: Package your company's workflows, best practices, and institutional knowledge for Claude to use consistently across your team.

**Easy customization**: Anyone can create Skills by writing instructions in Markdown—no coding required for simple Skills, though you can attach executable scripts to custom Skills for more advanced functionality.

**Centralized management for organizations:** Team and Enterprise plan Owners can provision skills organization-wide, ensuring consistent workflows across teams without requiring individual setup from each user.

---

## Agent Skills open standard

The Agent Skills specification is published as an open standard at **[agentskills.io](https://agentskills.io)**. This means skills you create aren't locked to Claude—the same skill format works across AI platforms and tools that adopt the standard. A reference Python SDK is also available for developers implementing skills support in their own platforms.

---

## Skills compared to other Claude capabilities

#### Skills vs. projects

**[Projects](https://support.claude.com/en/articles/9517075-what-are-projects)** provide static background knowledge that's always loaded when you start chats within them. Skills provide specialized procedures that activate dynamically when needed and work everywhere across Claude.

#### Skills vs. MCP (Model Context Protocol)

MCP connects Claude to external services and data sources. Skills provide procedural knowledge—instructions for how to complete specific tasks or workflows. You can use both together: MCP connections give Claude access to tools, while Skills teach Claude how to use those tools effectively.

#### Skills vs. custom instructions

**[Custom instructions](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)** apply broadly to all your conversations. Skills are task-specific and only load when relevant, making them better for specialized workflows.

---

## Learn more about Skills

To discover available Skills, check out the directory by clicking "Customize" in your account and navigating to "Skills." You can click "+" then "Browse skills" to open the directory. For more information, see **[Browse skills, connectors, and plugins in one directory](https://support.claude.com/en/articles/14328846-browse-skills-connectors-and-plugins-in-one-directory)**.

For more details about how Skills work, see **[Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)** in our Claude Docs.

## Related Articles
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
