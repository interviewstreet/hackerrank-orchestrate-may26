---
title: "Enabling and using web search"
title_slug: "enabling-and-using-web-search"
source_url: "https://support.claude.com/en/articles/10684626-enabling-and-using-web-search"
last_updated_iso: "2026-04-16T13:32:05Z"
article_id: "11419273"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Enabling and using web search

_Last updated: 2026-04-16T13:32:05Z_

You can have Claude search the internet to provide you with up-to-date information and insights when using the following models:

- Opus 4.7
- Sonnet 4.6
- Opus 4.6
- Opus 4.5
- Haiku 4.5
- Sonnet 4.5

Web search expands Claude's knowledge with real-time data, helping you make better-informed decisions with current information.

> **To access this feature on a Team or Enterprise plan account:**
>
> An Owner or Primary Owner must first enable web search for the entire workspace. This can be found in **[Admin settings > Capabilities](https://claude.ai/admin-settings/capabilities)**:
>
> ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2032032614/ad907328c4d9a26ee4bd9ca27a52/CleanShot+2026-02-05+at+09_01_42%402x.png?expires=1776784500&signature=40f79f8ca7c263bb84014f69837eda1da6dd171f16a8e14079a81cdc5785e235&req=diAkFMl9n4deXfMW1HO4zetvxbS9EMpVUJIbgsqS2%2BMhDlPSPl4V%2FiO0f%2BVh%0AOfmtO4CG5IAi7Tsb90E%3D%0A)
>
> Once this is enabled at the workspace level, any member of the organization can switch it on while starting a chat by clicking the “+” button in the lower left corner of the chat window and selecting “Web search." Users can toggle this off for chats that don’t require web search capabilities.

## How to enable web search in a chat

1. Click on the slider icon in your chat input interface.
2. Locate **Web search** in the dropdown.
3. Switch the toggle on.

You can disable the feature at any time by following the same steps and turning the toggle off.

## How web search works

When you ask about topics that benefit from current information, Claude invokes a search tool to inform and ground its generated responses with content from the live web. Every response includes citations, so you can easily verify sources yourself.

#### During a search

When Claude searches the web:

1. You'll see an indicator that Claude is searching the web.
2. Claude processes multiple sources to find relevant content.
3. Claude provides a conversational response that includes:
  - Direct citations to sources
  - Source links for further reading
  - Relevant quotes when appropriate

#### Web fetch and direct links

When “Web search” is toggled on, Claude can also retrieve content directly from web pages when provided with specific URLs. This feature, called web fetch, allows Claude to access and analyze the full content of articles, blog posts, and other web pages you want to discuss.

> **Important note for free Claude accounts:** When you provide Claude with a direct link to a long article or document and ask it to analyze or summarize the contents, the entire article is retrieved into Claude's context window. This can consume a significant portion of your usage capacity, especially for lengthy content. For example, asking Claude to summarize a 10,000-word article will use substantially more of your context window than a regular web search query.

## Image results

When web search is enabled, Claude can also search for and display images directly in your conversation. You don't need to enable a separate setting — image results are part of web search.

For example, you might ask Claude to:

- Show you what a recipe looks like before you start cooking
- Find photos of a product you're considering
- Help identify a plant, insect, or object by searching for visual matches
- Compare what similar items look like side by side

Claude selects images from web search results, powered by Bing, and displays them alongside its text response. Each image includes a source link so you can visit the original page for more details.

Image search is powered by Bing ([https://www.microsoft.com/en-us/privacy/privacystatement](https://www.microsoft.com/en-us/privacy/privacystatement)).

Claude can also display interactive content in search results. For more detailed information, see here: **[Visual and interactive content](https://support.claude.com/en/articles/13641943-visual-responses-and-interactive-widgets)**.

## Managing usage on free Claude accounts

As a free user, you have daily usage limits for Claude. Since web search and fetch both contribute to these limits, here are some tips to make the most of your capacity:

- **Be mindful of direct links:** Before asking Claude to analyze a long article via its URL, consider whether you need the full analysis or just key points.
- **Toggle web search off when not needed:** If you're having a conversation that doesn't require current information, disable web search to conserve your usage.
- **Use web search strategically:** Focus on queries where up-to-date information is essential.

To disable web search and conserve your capacity:

1. Click on the slider icon in the lower left corner of your chat input.
2. Find **Web search** in the dropdown.
3. Toggle it off.

You can re-enable it anytime you need current information.

## Tips for effective use

1. **Ask about recent information**: If you ask questions like "Are there any upcoming meteor showers?" or "What are the latest developments in quantum computing?", Claude will search the web for current data.
2. **Specify in your prompt:**
  - If you want to ensure that Claude uses web search, include "Search the web" or "Use web search" in your prompt to Claude.
  - You can also instruct Claude not to use web search in the prompt.
3. **Request multiple sources**: Claude can gather and synthesize information from various sources to give you a comprehensive view.
4. **Verify important information**: While Claude strives for accuracy:
  - Cross-reference cited sources to understand the full picture.
  - Use authoritative sources for critical decisions.

## Limitations

- Search availability may vary based on connectivity.
- Occasionally, website links may not function.
- Claude may use your location (inferred from your IP address) when responding to a request for localized results.
- Search times may vary based on query complexity.
- Usage of web search and web fetch counts toward your daily limits.

## Support

- For web search questions or support, please visit our **[Online Safety Contacts](https://support.claude.com/en/articles/11174660-online-safety-contacts)** page.
- For content removal requests, please visit our **[Blocking and Removing Content from Claude](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)** page.

## Related Articles
- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)
- [How large is the Claude API’s context window?](https://support.claude.com/en/articles/8606395-how-large-is-the-claude-api-s-context-window)
- [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Using Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-using-claude-in-microsoft-foundry)
