---
title: "API Safeguards Tools"
title_slug: "api-safeguards-tools"
source_url: "https://support.claude.com/en/articles/9199617-api-safeguards-tools"
last_updated_iso: "2026-03-16T21:13:38Z"
article_id: "9379409"
breadcrumbs:
  - "Safeguards"
---

# API Safeguards Tools

_Last updated: 2026-03-16T21:13:38Z_

Whether you are just starting the process of setting up safeguards for your API deployment of Claude, or your deployment is already running, here are some strategies to consider when building your own AI safety program. These suggestions are designed to help you comply with our [Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Usage Policy](https://www.anthropic.com/legal/aup), which prohibit certain uses of Claude. Failure to comply with the [Terms](https://www.anthropic.com/legal/commercial-terms) and  [Usage Policy](https://www.anthropic.com/legal/aup) may result in suspension or termination of your access to the services.

**Basic Safeguards**

- Store IDs linked with each API call, so if you need to pinpoint specific violative content you have the ability to find it in your systems.
- Consider assigning IDs to users, which can help you track specific individuals who are violating Anthropic’s AUP, allowing for more targeted action in cases of misuse.
  - The choice to [pass IDs to Anthropic through the API](https://docs.anthropic.com/claude/reference/messages_post#:~:text=models%20for%20details.-,metadata,object,-An%20object%20describing) is up to you. But, if provided, we can more precisely pinpoint violations. To help protect end-users' privacy, any IDs passed should be cryptographically hashed.
- Consider requiring customer to sign-up for an account on your platform before utilizing Claude
- Ensure your customers understand permitted uses
- Warn, throttle, or suspend users who repeatedly violate Anthropic’s [Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Usage Policy](https://www.anthropic.com/legal/aup)

**Intermediate Safeguards**

- Create customization frameworks that restrict end-user interactions with Claude to a limited set of prompts or only allow Claude to review a specific knowledge corpus that you already have, which will decrease the ability of users to engage in violative behavior.
- Enable additional safety filters - free real-time moderation tooling built by Anthropic for helping detect potentially harmful prompts and managing real-time actions to reduce harm
  - For more information about how to enable our additional safety filters, please reach out to [usersafety@anthropic.com](mailto:usersafety@anthropic.com).
- *For Bedrock Customers:*
  - Activate your private S3 bucket in order to store prompts and completions for your own evaluation

**Advanced Safeguards**

- [Use Claude for your content moderation](https://docs.anthropic.com/claude/docs/content-moderation)
- Run a moderation API against all end-user prompts before they are sent to Claude to ensure they are not harmful

**Comprehensive Safeguards**

- Set up an internal human review system to flag prompts that are marked by Claude (being used for content moderation) or a moderation API as harmful so you can intervene to restrict or remove users with high violation rates.

## Related Articles
- [Our Approach to User Safety](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety)
- [Safeguards warnings and appeals](https://support.claude.com/en/articles/8241253-safeguards-warnings-and-appeals)
- [Responsible Use of Anthropic's Models: Guidelines for Organizations Serving Minors](https://support.claude.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors)
- [Report a Concern: Australian DIS Standard compliance](https://support.claude.com/en/articles/12335811-report-a-concern-australian-dis-standard-compliance)
- [Real-time cyber safeguards on Claude](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)
