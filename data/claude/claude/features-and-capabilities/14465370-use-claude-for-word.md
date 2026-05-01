---
title: "Use Claude for Word"
title_slug: "use-claude-for-word"
source_url: "https://support.claude.com/en/articles/14465370-use-claude-for-word"
last_updated_iso: "2026-04-17T15:24:21Z"
article_id: "16914654"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Claude for Word

_Last updated: 2026-04-17T15:24:21Z_

Claude for Word is an add-in that integrates Claude into your Word workflow. It’s designed for professionals who work extensively with documents, particularly in legal review, financial memo drafting, and iterative editing.

> Claude for Word is currently in beta and available to Pro, Max, Team, and Enterprise plans.

With Claude for Word, you can:

- Ask questions about your document and get answers with clickable section citations.
- Edit selected text while preserving surrounding styles, numbering, and formatting.
- Use tracked changes mode so every edit lands as a revision you can accept or reject in Word’s native review pane.
- Have Claude work through comment threads, editing the anchored text and replying with what it changed.
- Fill templates with drafted content that inherits your document’s heading and paragraph styles.
- Find every provision touching a theme with semantic navigation, not just keyword search.

---

## Get started with Claude for Word

#### Supported versions

- Word on the web
- Word on Windows (Microsoft 365 subscription, Version 2205 / Build 15202.10000 or later)
- Word on Mac (version 16.61 / Build 22040100 or later)

#### For individuals

1. Navigate to the **[Claude for Word listing on Microsoft Marketplace](https://marketplace.microsoft.com/en-us/product/office/WA200010453?tab=Overview)**.
2. Click “Get it now” to install the add-in.
3. Open Word, activate the add-in, and sign in with your Claude account.

#### For admins

**Deploy Claude for Word to your organization:**

1. Visit the **Microsoft 365 Admin Center**.
2. Navigate to **Settings > Org Settings > User owned apps and services** and ensure that **“Let users access the Office Store”** is toggled on.
3. Navigate to **Settings > Integrated apps > Add-ins**.
4. Search for “Claude by Anthropic for Word” in Microsoft AppSource.
5. Deploy the add-in to your organization or specific people.
6. Share these instructions with your team: **Microsoft’s deployment guide**.

After installation, team members can open Word, activate the Claude add-in (from Tools > Add-ins on Mac or Home > Add-ins on Windows), sign in with their Claude credentials, and start working with their documents.

> **Important:** Organizations that have disabled “Let users access the Office Store” may find that admin-deployed add-ins don’t appear for people. To work around this, deploy using the manifest XML files provided below.

For IT administrators deploying to multiple people:

**Step 1: Obtain the custom manifest**

1. Click **[this link](https://pivot.claude.ai/manifest-word.xml)** to download the custom manifest XML file.
2. Save this file to a secure location.

**Step 2: Access Microsoft 365 Admin Center**

1. Navigate to **https://admin.microsoft.com**
2. Sign in with your admin credentials.
3. Go to **Settings > Integrated apps**.

**Step 3: Upload the custom add-in**

1. Click “Upload custom apps.”
2. Select “Office Add-in.”
3. Choose “I have a manifest file on this device.”
4. Browse and select the Claude for Word manifest XML file.
5. Click “Upload.”

**Step 4: Assign people**

Choose your deployment scope:

- **Entire organization: **All people get access
- **Specific users: **Enter individual email addresses
- **Specific groups: **Select security groups or distribution lists
- **Just yourself: **For admin testing only

**Step 5: Deploy**

1. Review deployment settings.
2. Click “Deploy.”
3. The add-in will be available within minutes (may take up to 24 hours for full organization rollout).

**Step 6: Access**

- People will see Claude appear in Word’s Home ribbon.
- First-time people will need to sign in with their Claude accounts.
- No additional installation required.

#### Connect through an LLM gateway

If your organization routes API traffic through an internal LLM gateway connected to Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the add-in without a Claude account. This is the same gateway pattern used by Claude Code.

For setup instructions and gateway requirements, see **[Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-and-powerpoint-with-third-party-platforms)**.

---

## Key features

#### Read and understand documents

Ask Claude questions about specific sections, clauses, or defined terms in your document. Claude provides answers with clickable citations that navigate directly to the referenced section in your document.

**Example prompts:**

- “What’s the liability cap and is it mutual?”
- “Summarize the key commercial terms in this agreement”
- “What assumptions drive the revenue forecast in section 3?”

#### Edit selected text

Select a passage and tell Claude what to change. Claude edits only the selection while preserving surrounding styles, numbering, and formatting. New text inherits the paragraph style, font, and numbering of the surrounding content.

**Example prompts:**

- “Tighten this paragraph and drop the passive voice”
- “Rewrite this clause to make the indemnification mutual”
- “Simplify this section for a non-technical audience”

#### Track changes mode

When you enter suggested edits mode, Claude’s edits land as tracked revisions. The original text is visible as a deletion and the new text as an insertion, all reviewable in Word’s native review pane. This gives you a clear audit trail of what Claude changed, so you can accept or reject each revision individually.

**Example prompts:**

- “Rewrite §4.2 to cap damages at 12 months of fees, and make it mutual”
- “Draft a mutual indemnification clause after §8”

#### Comment-driven editing

Claude reads comment threads in your document, understands what text each thread is anchored to, and can work through them one by one. For each comment, Claude edits the anchored passage and replies to the thread with a note explaining what it did.

**Example prompts:**

- “Work through my open comments”
- “Address the comment on the liability section”

#### Summarize counterparty redlines

When a counterparty returns a document with tracked changes, Claude can read and summarize what they changed. Ask Claude to group changes by severity or flag the ones worth pushing back on.

**Example prompts:**

- “Summarize what the other side changed and flag anything that’s worth discussing”
- “Which of these redlines are dealbreakers?”

#### Fill templates

Draft sections in your document’s heading and paragraph styles. Claude uses your template’s formatting when generating content, so new headings, bullets, and table entries match what’s already there. Tables populate in place without reflowing layout or changing column widths.

**Example prompts:**

- “Draft the Key Risks section with four risks in the template’s style”
- “Populate the summary table with revenue, gross margin, and net retention for the last three years”

#### Semantic navigation

Find every provision or passage in your document that touches a specific theme. Claude returns thematic matches, not just keyword hits, and each result navigates to the relevant location on click.

**Example prompts:**

- “Find every provision touching data retention”
- “Where does this agreement address termination?”

## Work across Word, Excel, and PowerPoint

Claude for Word shares context with Claude for Excel and Claude for PowerPoint, so Claude can work across your open documents in a single conversation. For example, you can ask Claude to pull numbers from an Excel model into a Word memo, or summarize a Word document into PowerPoint slides, without copying and pasting between apps.

For setup instructions, see **[Work across Excel, PowerPoint, and Word](https://support.claude.com/en/articles/13892150-work-across-excel-and-powerpoint)**.

---

## Context and session management

- **Auto-compaction: **We automatically compact longer conversations into new conversations to avoid running out of context.
- **Overwrite protection: **To avoid accidental data loss, Claude warns you before overwriting existing content.

> **Note:** Your use of Claude for Word is associated with your existing Claude account and is subject to the same usage limits.

---

## Current limitations

For Claude for Word use, we automatically delete inputs and outputs on our backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization’s data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** Data will be deleted after 30 days, but will be cached for a number of hours so users can access context in recently closed out documents.

This is unlike our other commercial products (Team and Enterprise plans) that allow you to save and continue conversations with Claude. Chat history isn’t saved between sessions.

Currently, observability and audibility are not available with this feature. Claude for Word doesn’t inherit custom data retention settings your organization might have set, and isn’t included in Enterprise audit logs or the Compliance API at this time.

As a beta feature, Claude for Word is **not recommended** for:

- Final client deliverables or counterparty sends without human review
- Litigation filings or audit-critical documents without verification
- Replacing legal or financial judgment
- Documents containing highly sensitive or privileged data without proper controls

#### Unsupported versions

- Word 2016 / 2019 (perpetual/volume licensed)
- Word on iPad
- Word on Android
- Microsoft 365 Word builds older than Version 2205 (Windows) or 16.61 (Mac)

---

## Best practices

To use Claude for Word safely and effectively:

- Always review tracked changes before accepting them.
- Verify that outputs match your firm’s playbook and standard positions.
- Use appropriate permissions and access controls.
- Maintain human oversight for client-facing work.

---

## Prompt injection attack risks

Only use Claude for Word with trusted documents and not documents from external untrusted sources (for example, downloaded templates, counterparty files, or collaborative documents shared via email).

An important risk for people using Claude for Word and other AI tools that can read and edit documents is prompt injection attacks that hide malicious instructions in document content (text, comments, tracked changes, headers, footers) to trick AI models into taking unintended actions. For example, a seemingly routine contract received from an external party might contain hidden instructions to modify terms or exfiltrate data. Claude may interpret these instructions as legitimate requests from you.

Our testing has identified edge scenarios where Claude for Word can be manipulated to:

- **Extract and share sensitive information **with bad actors through web searches containing your sensitive data or file system access that exposes proprietary information.
- **Modify critical content **such as contract terms or financial figures.
- **Perform destructive actions **without verification (should you allow Claude to act without verifying its actions), exploiting Claude’s helpful nature to delete or alter important content.

While we continue to develop our offerings and improve safety measures to reduce these risks, you should exercise caution when using Claude for Word and should not use it with documents from external, untrusted sources.

---

## Example use cases

#### Legal contract review

- “Summarize the key commercial terms: parties, term, governing law, and anything off-market”
- “Flag provisions that deviate from standard market position, ranked by severity”
- “Make the indemnification mutual and insert our standard fallback language”
- “Work through all five reviewer comments as tracked changes”
- “What did the counterparty change, and which revisions are dealbreakers?”

#### Finance memo drafting

- “Draft the Investment Thesis section with three points, pulling the numbers from the uploaded 10-K”
- “Populate the summary table with revenue, gross margin, and FCF for the last three years”
- “Too generic on point two. Use the customer count from the deck”
- “Address the partner’s comment on the Risks section”

#### Document QA and consistency

- “Flag inconsistent defined terms and broken cross-references”
- “Check the numbering scheme for gaps”
- “Proofread for spelling, grammar, and punctuation”
- “Is the same party referred to by different names anywhere in this document?”

#### General document editing

- “Tighten section 4 and drop the passive voice”
- “Rewrite this for a non-technical audience”
- “Add a fourth risk addressing customer concentration”
- “Define this term and use it consistently throughout”

---

## Frequently asked questions

#### Which models are available when using Claude for Word?

You can switch between Opus 4.7, Opus 4.6, and Sonnet 4.6 when using Claude for Word.

#### Does Claude understand legal and financial document conventions?

Claude recognizes common document patterns including multi-level legal numbering, defined terms, cross-references, and standard contract structures. However, always verify that outputs match your specific requirements and your firm’s standard positions.

#### Can I use Claude for Word with sensitive data?

Claude for Word works within your existing security framework. For highly sensitive or regulated data, ensure you follow your organization’s data handling policies.

#### What happens to my chat history?

Currently, chat history isn’t saved between sessions. Each time you open the add-in, you start a fresh conversation with Claude.

#### How does Claude access my document?

Claude reads the content of your currently open document, including text, comments, tracked changes, footnotes, tables, and bookmarks. It can only access the document you have open in Word.

#### What if Claude makes a mistake?

In tracked changes mode, you can review every edit before accepting it. You can always undo changes using Word’s standard undo function (Ctrl+Z / Cmd+Z).

#### Does Claude support .doc files?

Claude for Word supports .docx files. If you’re working with a legacy .doc file, save it as .docx first.

## Related Articles
- [Using Claude in Slack](https://support.claude.com/en/articles/12461605-using-claude-in-slack)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Work across Excel, PowerPoint, and Word](https://support.claude.com/en/articles/13892150-work-across-excel-powerpoint-and-word)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
