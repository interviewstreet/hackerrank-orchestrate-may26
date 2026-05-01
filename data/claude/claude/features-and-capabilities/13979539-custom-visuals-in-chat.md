---
title: "Custom visuals in chat"
title_slug: "custom-visuals-in-chat"
source_url: "https://support.claude.com/en/articles/13979539-custom-visuals-in-chat"
last_updated_iso: "2026-03-16T20:28:53Z"
article_id: "16262087"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Custom visuals in chat

_Last updated: 2026-03-16T20:28:53Z_

Claude can generate custom diagrams, charts, and interactive visuals directly in your conversation. When a visual would explain something better than text, Claude builds one from scratch—shaped to your specific question, rendered inline as part of the response.

> **Note: **Custom visuals are currently in beta and available to all Claude users on web and desktop.

## How it works

You don’t need to turn anything on. Claude decides when a visual would help based on what you’re asking. You can also ask directly—try phrases like “draw this as a diagram,” “show me how this changes over time,” or “chart this data.”

Once a visual appears, you can interact with it—click buttons, adjust sliders, expand it to full screen—and keep asking follow-up questions. Claude can update or rebuild the visual as the conversation continues.

Here are a few examples of what Claude might generate:

- “Show me how this process works” → Claude shows you by creating a flowchart.
- Upload a CSV and ask “What does the data show?”→ Claude generates an interactive chart.
- “Help me decide between two different options” → Claude outputs a side-by-side comparison.
- “Visualize this system or concept” → Claude builds a diagram alongside its explanation.

## Keep a visual

Custom visuals are ephemeral by default. They live inline as part of Claude's response and aren't saved separately when the conversation moves on. Think of them less like a finished file and more like a whiteboard sketch.

However, if you do want to keep a visual, you have a few options:

- **Copy as image** — grab a static snapshot for notes, slides, or a quick paste.
- **Download** — save the visual as an .svg or .html file.
- **Save as artifact** — convert it into an artifact you can keep, publish, and iterate on over time.

This is the main practical difference from artifacts: artifacts are persistent and shareable from the start, while custom visuals help you think in the moment and only stick around if you choose to keep them. If you want to build something persistent—a tool, an app, a document to share—ask Claude to create an artifact instead. For more information, see **[What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)**

## How are custom visuals built?

Custom visuals aren’t photos or illustrations. Claude builds them using HTML—the same building blocks as web pages—so they’re interactive and specific to your question rather than static images.

---

## Limitations

- Custom visuals are available in chats on Claude web and desktop apps only. They don’t render on Claude for iOS or Claude for Android or in Cowork sessions.
- If you share a chat, the visual renders for the recipient on web and desktop only and they must be logged in to view.
- Visuals aren't saved automatically. To keep one, use one of the options described above.
- This feature is in beta. Visual quality and complexity will vary, and Claude may not always choose to generate a visual when you expect one.

---

## Tips

- **Ask for what you want. **If Claude gives a text output when you’d prefer a visual, try rephrasing—“show me a diagram of how this works” or “chart this for me.”
- **Smarter is better.** Opus performs the best at visualization tasks, so if you’re going for something complex, we’d recommend choosing a more intelligent model.
- **Personalize your visuals.** If you tell Claude “make all my visualizations pink”, Claude will remember.
- **Iterate in the conversation. **You can ask Claude to adjust a visual the same way you’d ask it to revise text—“make the chart show monthly instead of yearly” or “add a third option to the comparison.”

## Related Articles
- [Can Claude produce images?](https://support.claude.com/en/articles/9002504-can-claude-produce-images)
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Visual and interactive content](https://support.claude.com/en/articles/13641943-visual-and-interactive-content)
