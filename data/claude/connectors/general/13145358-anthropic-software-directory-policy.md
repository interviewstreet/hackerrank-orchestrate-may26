---
title: "Anthropic Software Directory Policy"
title_slug: "anthropic-software-directory-policy"
source_url: "https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy"
last_updated_iso: "2026-04-15T01:48:09Z"
article_id: "14939113"
breadcrumbs:
  - "Connectors"
  - "General"
---

# Anthropic Software Directory Policy

_Last updated: 2026-04-15T01:48:09Z_

Anthropic allows users to discover high-quality Model Context Protocol servers, Skill folders, plugins, apps, and other software, containers, or data (“Software”) that work seamlessly within Claude through directories, repositories, surfaces, or similar offerings (collectively, “Directories”). We review submissions to our Directories to ensure they meet our standards for safety, security, and compatibility with Anthropic Services and other Software. We conduct both initial and ongoing reviews of Software, and may require developers to address compliance issues to continue being included in our Directories. All Software must maintain compliance with these requirements, including any future changes, to remain in our Directories.

1. Safety and Security

A. Software must not violate or facilitate violation of our [Usage Policy](https://www.anthropic.com/legal/aup). All Software must comply with our Universal Usage Standards and High-Risk Use Case requirements and with our policy on the [countries and regions Anthropic currently supports](https://www.anthropic.com/supported-countries).

B. Software must not evade or enable users to circumvent Claude's safety guardrails, system instructions, or sandbox environments.

C. Software must prioritize protecting user privacy and the privacy interests of third parties. Developers must take care to responsibly handle personal and other sensitive data, follow privacy best practices, and ensure compliance with applicable laws.

D. Software must only collect data from the user’s context that is necessary to perform their function. Software must not collect extraneous conversation data, even for logging purposes.

E. Software must not infringe on the intellectual property rights of others.

F. Software must not query or extract data from Claude's memory, chat history, conversation summaries, or user-generated or uploaded files.

2. Compatibility

This section applies to Software that provides Claude with tools or capabilities through natural language descriptions, including MCP servers, Skill folders, and similar Software ("Instructional Software").

A. Instructional Software must define each tool or capability through narrow, unambiguous natural language that specifies what it does and when it should be invoked.

B. Instructional Software tool or capability descriptions must precisely match actual functionality, ensuring the Instructional Software is called at correct and appropriate times. Descriptions must not include unexpected functionality or promise undelivered features.

C. Instructional Software tool or capability descriptions must not create confusion or conflict with other Software in our Directories.

D. Instructional Software must not intentionally call or coerce Claude into calling other external software, tools, databases, or resources unless requested and intended by a user. Similarly, Instructional Software tool or capability descriptions must not be written in a way that intentionally leads to other Software extraneously calling them.

E. Instructional Software must not attempt to interfere with Claude calling tools from other software, tools, databases, or resources unless requested and intended by a user.

F. Instructional Software must not direct Claude to dynamically pull behavioral instructions from external sources for Claude to execute.

G. Instructional Software must not contain hidden, obfuscated, or encoded instructions. All behavioral guidance must be human-readable and clearly presented.

3. Developer Requirements

A. Developers of Software that collects user data or connects to a remote service must provide a clear, accessible privacy policy link explaining data collection, usage, and retention. Developers must provide Anthropic with links to all applicable privacy policies and ensure such policies are presented to users as required by law.

B. Developers must provide verified contact information and support channels for users with product or security concerns.

C. Developers must document how their Software works, its intended purpose, and how users can troubleshoot issues.

D. Developers must provide a standard testing account with sample data for Anthropic to verify full Software functionality.

E. Developers must provide at least three working examples of prompts or use cases that demonstrate core functionality.

F. Developers must verify that they own or control any API endpoint, domain, or user interface their Software connects to, as well as any external resources it retrieves or renders. Plugins are an exception, and may connect to any Connector approved in the Software Directory.

G. Developers must maintain their Software and address issues within reasonable timeframes.

H. Developers must agree to our [Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms) and follow design guidelines Anthropic publishes applicable to Software.

4. Unsupported Use Cases

Unless otherwise expressly permitted by us in writing, we do not allow Software with certain capabilities into our Directories. We may revisit these restrictions as our Directories and Anthropic Services evolve.

A. Software that transfers money, cryptocurrency, or other financial assets, or executes financial transactions on behalf of users.

B. Software that uses AI models to generate images, video, or audio content. Design-focused software that uses AI models to create visual aids (such as slides, diagrams, charts, UI mockups, logos, or other design assets) are permitted. These servers may generate images as part of a design workflow, provided the developer does not offer standalone image generation as a primary service.

C. Software that serves [advertisements](https://www.anthropic.com/news/claude-is-a-space-to-think), sponsored content, paid product placements, or exists primarily as an advertising or promotional vehicle.

5. Additional Requirements for Model Context Protocol Servers

A. MCP servers must gracefully handle errors and provide helpful feedback rather than generic error messages.

B. MCP servers must be frugal with their use of tokens. The amount of tokens a given tool call uses should be roughly commensurate with the complexity or impact of the task. When possible, users should be given options to exclude unnecessary text in the response.

C. MCP tool names must not exceed 64 characters.

D. Remote MCP servers that connect to a remote service and require authentication must use secure OAuth 2.0 with certificates from recognized authorities.

E. MCP servers must provide all applicable [annotations](https://modelcontextprotocol.io/specification/2025-11-25/schema#toolannotations) for their tools, in particular *readOnlyHint*, *destructiveHint*, and *title*.

F. Remote MCP servers should support the [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) transport. Servers may support [SSE](https://modelcontextprotocol.io/specification/2024-11-05/basic/transports#http-with-sse) for the time being, but in the future it will be deprecated.

G. Local MCP servers must be built with reasonably current versions of all dependencies, including packages in *node_modules*.

> See prior version of this policy here: [Anthropic MCP Directory Policy](https://support.claude.com/en/articles/11697096-anthropic-mcp-directory-policy).

## Related Articles
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Get started with custom connectors using remote MCP](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms)
- [MCP: Individual connectors](https://support.claude.com/en/articles/14503703-mcp-individual-connectors)
