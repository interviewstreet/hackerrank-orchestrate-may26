---
title: "Use dictation in Office agents"
title_slug: "use-dictation-in-office-agents"
source_url: "https://support.claude.com/en/articles/14479591-use-dictation-in-office-agents"
last_updated_iso: "2026-04-07T23:40:44Z"
article_id: "16936768"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use dictation in Office agents

_Last updated: 2026-04-07T23:40:44Z_

Dictation lets you speak your prompts instead of typing them when using Office agents. Click the microphone icon in the chat input, speak, and your words appear in the composer as you talk.

Dictation is available for organizations that sign in with Claude directly. It isn't available when Office agents is configured with third-party authentication such as a gateway, Vertex AI, or Bedrock. See below for more information.

## How it works

When you click the microphone, Office agents streams your audio to Anthropic's transcription service, the same infrastructure that powers dictation in the Claude apps. The transcribed text appears in the composer in real time. Click the microphone again to stop, or press Enter to stop and send in one step.

Nothing is transcribed on your device, and your audio isn’t sent to any third-party service. Audio is processed entirely on Anthropic’s infrastructure and isn’t retained; only the resulting text remains in your composer.

## Use dictation

- Click the microphone icon on the right side of the chat input. The placeholder changes to *Listening...* and the button turns blue.
- Speak your prompt. Your words appear in the composer as you talk.
- Click the microphone again to stop, or press Enter to stop and send in one step.
- To choose a different microphone, hover over the microphone icon and click the arrow that appears.

## Why dictation isn't available with third-party authentication

In third-party environments, Office agents do not send prompts to Anthropic directly. Spoken audio is effectively a prompt, so dictation isn’t offered there. If you need voice input in a third-party environment, use the dictation feature built into your operating system or Office application instead.

## Related Articles
- [How do I view and sign your Data Processing Addendum (DPA)?](https://support.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa)
- [Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)
- [Using dictation on Claude Mobile](https://support.claude.com/en/articles/10065434-using-dictation-on-claude-mobile)
- [Logging in to your Claude account](https://support.claude.com/en/articles/13189465-logging-in-to-your-claude-account)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
