---
title: "Uploading files to Claude"
title_slug: "uploading-files-to-claude"
source_url: "https://support.claude.com/en/articles/8241126-uploading-files-to-claude"
last_updated_iso: "2026-03-16T21:03:38Z"
article_id: "8226569"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Uploading files to Claude

_Last updated: 2026-03-16T21:03:38Z_

This article explains how to upload documents and images to Claude, including supported file types, size limits, and how to get started.

## Supported file types

#### Documents

Claude can work with the following document types:

- PDF
- DOCX
- CSV
- TXT
- HTML
- ODT
- RTF
- EPUB
- JSON
- XLSX*

> **Note:** You must enable **[code execution and file creation](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)** in your account to upload XLSX files.

#### Images

Claude supports the following image formats:

- JPEG
- PNG
- GIF
- WebP

---

## How to upload files

You can upload files to Claude in several ways:

1. Click the "+" button in the lower left corner of the chat box
2. Select "Add files or photos" from the menu.
3. Choose files from your device for upload.
4. Click "Open" to attach the files, or drag and drop the files directly into the chat window.
5. You can also copy images and paste them from your clipboard into Claude.

Files can be uploaded to individual chats or uploaded to a project's **Files** section for persistent reference across conversations.

---

## File limits

#### Chat uploads

- **File size:** 30MB per file
- **Number of files:** Up to 20 files per chat
- **Image dimensions:** Up to 8000x8000 pixels

#### Project files

- **File size:** 30MB per file
- **Number of files:** Unlimited, but total content must fit within Claude's context window
- **Content type:** Text extraction only (except for multimodal PDFs)

> **Note:** Additional token limits may apply based on the length of extracted content.

---

## PDF processing

Claude models can analyze both text and visual elements (like images, charts, and graphics) in PDFs that are under 100 pages. Claude will only process text from PDFs over 1000 pages.

---

## Tips for best results

**For images:** Use images that are 1000x1000 pixels or larger. Avoid small or low-resolution images where possible.

**For PDFs:** When referring to specific pages, use the PDF page numbers as shown in your PDF viewer, not the page numbers printed on the document itself.

**For large documents:** If you're working with larger files, consider dividing them into smaller sections to stay within limits.

**For non-PDF documents:** Claude extracts text only from these files. If they contain embedded images, Claude won't be able to read or interpret them.

## Related Articles
- [Can Claude produce images?](https://support.claude.com/en/articles/9002504-can-claude-produce-images)
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)
