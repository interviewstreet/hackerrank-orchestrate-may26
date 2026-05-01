---
title: "Google Sheets add-on"
title_slug: "google-sheets-add-on"
source_url: "https://support.claude.com/en/articles/13162029-google-sheets-add-on"
last_updated_iso: "2026-03-16T21:20:27Z"
article_id: "14967430"
breadcrumbs:
  - "Claude API and Console"
  - "Using the Claude API and Console"
---

# Google Sheets add-on

_Last updated: 2026-03-16T21:20:27Z_

The [Claude for Sheets extension](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) integrates Claude into Google Sheets, allowing you to execute interactions with Claude directly in cells.

## Why use Claude for Sheets?

Claude for Sheets enables prompt engineering at scale by enabling you to test prompts across evaluation suites in parallel. Additionally, it excels at office tasks like survey analysis and online data processing.

Visit our [prompt engineering example sheet](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r__UsRsB7WeySDQA/copy) to see this in action.

## Get started with Claude for Sheets

#### Install Claude for Sheets

Easily enable Claude for Sheets using the following steps:

1. **Get your Claude API key:** If you don't yet have an API key, you can make API keys in the Claude Console.
2. **Install the Claude for Sheets extension:** Find the [Claude for Sheets extension](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) in the add-on marketplace, then click the blue `Install` button and accept the permissions.
  1. Permissions: The Claude for Sheets extension will ask for a variety of permissions needed to function properly. Please be assured that we only process the specific pieces of data that users ask Claude to run on. This data is never used to train our generative models.
  2. Extension permissions include:
    1. **View and manage spreadsheets that this application has been installed in:** Needed to run prompts and return results.
    2. **Connect to an external service:** Needed in order to make calls to Claude API endpoints.
    3. **Allow this application to run when you are not present:** Needed to run cell recalculations without user intervention.
    4. **Display and run third-party web content in prompts and sidebars inside Google applications:** Needed to display the sidebar and post-install prompt.
3. **Connect your API key:** Enter your API key at `Extensions` > `Claude for Sheets™` > `Open sidebar` > `☰` > `Settings` > `API provider`. You may need to wait or refresh for the Claude for Sheets menu to appear.

   ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1885955653/fa55fbc81410f0f9da473a5b6c01/044af20-Screenshot_2024-01-04_at_11_58_21_AM.png?expires=1776784500&signature=93ec66a0eaa085cfdc10cee814e8cbc0cef1e486b4294a82ea75d93a60d93141&req=dSgvE8B7mIdaWvMW1HO4zQWPGDAMQSEBY2KGYHWoVfmRY5MCO%2FLpk%2FPqlP5c%0A3f9V%0A)

> **Important:** You will have to re-enter your API key every time you make a new Google Sheet.

#### Enter your first prompt

There are two main functions you can use to call Claude using Claude for Sheets. For now, let's use `CLAUDE()`.

**Simple prompt**

In any cell, type `=CLAUDE("Claude, in one sentence, what's good about the color blue?")`.

Claude should respond with an answer. You will know the prompt is processing because the cell will say `Loading...`.

**Adding parameters**

Parameter arguments come after the initial prompt, like `=CLAUDE(prompt, model, params...)`.

> **Note:** `model` is always second in the list.

Now type in any cell `=CLAUDE("Hi, Claude!", "claude-haiku-4-5-20251001", "max_tokens", 3)`.

Any API parameter can be set this way. You can even pass in an API key to be used just for this specific cell, like this: `"api_key", "sk-ant-api03-j1W..."`.

## Advanced use

`CLAUDEMESSAGES` is a function that allows you to specifically use the [Messages API](https://platform.claude.com/docs/en/api/messages). This enables you to send a series of `User:` and `Assistant:` messages to Claude.

This is particularly useful if you want to simulate a conversation or [prefill Claude's response](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prefill-claudes-response).

Try writing this in a cell:

```
=CLAUDEMESSAGES("User: In one sentence, what is good about the color blue?<br>Assistant: The color blue is great because")
```

> **Newlines**
>
> Each subsequent conversation turn (`User:` or `Assistant:`) must be preceded by a single newline. To enter newlines in a cell, use the following key combinations:
>
> - **Mac:** Cmd + Enter
> - **Windows:** Alt + Enter

**Example multiturn CLAUDEMESSAGES() call with system prompt**

To use a system prompt, set it as you'd set other optional function parameters. (You must first set a model name.)

```
=CLAUDEMESSAGES("User: What's your favorite flower? Answer in &lt;answer&gt; tags.<br>Assistant: &lt;answer&gt;", "claude-haiku-4-5-20251001", "system", "You are a cow who loves to moo in response to any and all user queries.")
```

## Optional function parameters

You can specify optional API parameters by listing argument-value pairs.

You can set multiple parameters. Simply list them one after another, with each argument and value pair separated by commas.

> **Note:** The first two parameters must always be the prompt and the model. You cannot set an optional parameter without also setting the model.

The argument-value parameters you might care about most are:

#### Example: Setting parameters

Ex. Set `system` prompt, `max_tokens`, and `temperature`:

```
=CLAUDE("Hi, Claude!", "claude-haiku-4-5-20251001", "system", "Repeat exactly what the user says.", "max_tokens", 100, "temperature", 0.1)
```

Ex. Set `temperature`, `max_tokens`, and `stop_sequences`:

```
=CLAUDE("In one sentence, what is good about the color blue? Output your answer in &lt;answer&gt; tags.","claude-opus-4-5-20251101","temperature", 0.2,"max_tokens", 50,"stop_sequences", "\[""&lt;/answer&gt;""\]")
```

Ex. Set `api_key`:

```
=CLAUDE("Hi, Claude!", "claude-haiku-4-5-20251001","api_key", "sk-ant-api03-j1W...")
```

## Claude for Sheets usage examples

#### Prompt engineering interactive tutorial

Our in-depth [prompt engineering interactive tutorial](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing) utilizes Claude for Sheets.

Check it out to learn or brush up on prompt engineering techniques.

> **Note:** Just as with any instance of Claude for Sheets, you will need an API key to interact with the tutorial.

#### Prompt engineering workflow

Our [Claude for Sheets prompting examples workbench](https://docs.google.com/spreadsheets/d/1sUrBWO0u1-ZuQ8m5gt3-1N5PLR6r%5F%5FUsRsB7WeySDQA/copy) is a Claude-powered spreadsheet that houses example prompts and prompt engineering structures.

#### Claude for Sheets workbook template

Make a copy of our [Claude for Sheets workbook template](https://docs.google.com/spreadsheets/d/1UwFS-ZQWvRqa6GkbL4sy0ITHK2AhXKe-jpMLzS0kTgk/copy) to get started with your own Claude for Sheets work!

## Troubleshooting

#### NAME? Error: Unknown function: 'claude'

1. Ensure that you have enabled the extension for use in the current sheet
  1. Go to *Extensions > Add-ons > Manage add-ons*
  2. Click on the triple dot menu at the top right corner of the Claude for Sheets extension and make sure "Use in this document" is checked

     ![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1885994017/0576e3f7d37c8223e5fb4743ad92/9cce371-Screenshot_2023-10-03_at_7_17_39_PM.png?expires=1776784500&signature=65dd13211afbe5bc21417f83b2cbd64521123e0eba361e9e0c737d41430764c9&req=dSgvE8B3mYFeXvMW1HO4zftja8M28UEcpoA36c5sCs9yzMymTbX2mhzwmYPj%0Ax0gR%0A)
2. Refresh the page

#### #ERROR!, ⚠ DEFERRED ⚠ or ⚠ THROTTLED ⚠

You can manually recalculate `#ERROR!`, `⚠ DEFERRED ⚠`, or `⚠ THROTTLED ⚠` cells by selecting from the recalculate options within the Claude for Sheets extension menu.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/1885996645/cc87f17bd5fa2e8facfdbfc09154/f729ba9-Screenshot_2024-02-01_at_8_30_31_PM.png?expires=1776784500&signature=991595bdf6b56c660bb02b476e6f28ab82c2f78735d702a75b038a46261dfb3c&req=dSgvE8B3m4dbXPMW1HO4zSC1mgL6f6uThyBIJxp2kExZNqOCgh1klDtEaBOB%0Amy8anJMe51fpwRil5Uo%3D%0A)

#### Can't enter API key

1. Wait 20 seconds, then check again
2. Refresh the page and wait 20 seconds again
3. Uninstall and reinstall the extension

## Further information

For more information regarding this extension, see the [Claude for Sheets Google Workspace Marketplace](https://workspace.google.com/marketplace/app/claude%5Ffor%5Fsheets/909417792257) overview page.

## Related Articles
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Using Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-using-claude-in-microsoft-foundry)
- [Configure a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents)
- [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
