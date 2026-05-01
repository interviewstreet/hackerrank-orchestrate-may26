---
title: "Retrieval augmented generation (RAG) for projects"
title_slug: "retrieval-augmented-generation-rag-for-projects"
source_url: "https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects"
last_updated_iso: "2026-03-16T21:03:43Z"
article_id: "12444697"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Retrieval augmented generation (RAG) for projects

_Last updated: 2026-03-16T21:03:43Z_

> RAG for projects is available for all Claude plans (free, Pro, Max, Team, and Enterprise).

Projects can now handle much more content without running into limits, giving Claude better context to help you. As you add more files and information to your projects, Claude automatically switches to a faster mode (powered by RAG) that keeps response times quick while maintaining quality responses.

## What is RAG for projects?

RAG or retrieval augmented generation is a technology that allows your projects to store and access significantly more knowledge than before. When your project knowledge approaches the context window limit, Claude will automatically enable RAG mode to expand your project's capacity by up to 10x while maintaining quality responses.

Previously, projects had a knowledge capacity limit based on the **[context window](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)**. Once you reached this threshold, it wasn't possible to add more content. With RAG, you can continue adding knowledge beyond these limits while maintaining full functionality.

## How RAG works

When RAG is enabled for your project, Claude uses a **project knowledge search tool** to retrieve relevant information from your uploaded documents. Instead of loading all project content into memory at once, Claude intelligently searches and retrieves only the most relevant information needed to answer your questions.

This approach allows for:

- **Enhanced capacity**: Store up to 10x more content in your projects.
- **Maintained quality**: Response accuracy remains consistent with in-context processing.
- **Faster responses**: Optimized retrieval keeps response times quick.
- **Seamless transition**: Automatic activation when needed, no setup required.

## When RAG activates

RAG automatically activates when your project approaches or exceeds the context window limits. You'll see a visual indicator showing that your project is RAG-enabled.

If your project knowledge later drops below the context window threshold, Claude can automatically convert back to context-based processing.

## Using projects with RAG

Working with RAG-enabled projects feels similar to working with regular projects. You can:

- Upload documents, images, and other files as usual
- Ask questions about your project knowledge
- Reference specific documents or information
- Add and remove content at any time

The main difference is that you'll see Claude using a **project knowledge search tool** when it needs to find relevant information from your uploaded content.

## Best practices for RAG projects

To get the most out of your RAG-enabled projects:

#### Upload comprehensive content

Add all relevant documents and files to your project upfront. The more context Claude has access to, the better it can assist you.

#### Use clear, descriptive filenames

Well-named files help Claude understand and retrieve the right information more effectively.

#### Organize related content together

Group related documents in the same project to enable Claude to draw connections between different sources.

#### Reference specific documents

When asking questions, you can reference specific documents by name to help Claude focus its search.

---

## Frequently asked questions

#### Will having RAG enabled on my project affect response quality?

No. RAG maintains consistent response quality as in-context processing while enabling larger project capacity.

#### Do I need to do anything to enable RAG?

No, RAG activates automatically when needed. No setup or configuration is required.

#### Can I control when RAG is used?

RAG activation is handled automatically based on the size of your project knowledge. When possible, projects will use in-context processing for optimal performance.

#### Will my existing projects work with RAG?

Yes. All existing projects will automatically benefit from RAG when the project knowledge exceeds context limits.

#### Does RAG work with all Claude tools?

Yes. RAG works with all Claude features, including web search, extended thinking, and Research.

## Related Articles
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- [Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
