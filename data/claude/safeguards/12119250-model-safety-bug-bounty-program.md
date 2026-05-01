---
title: "Model Safety Bug Bounty Program"
title_slug: "model-safety-bug-bounty-program"
source_url: "https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program"
last_updated_iso: "2026-03-16T20:49:23Z"
article_id: "13426208"
breadcrumbs:
  - "Safeguards"
---

# Model Safety Bug Bounty Program

_Last updated: 2026-03-16T20:49:23Z_

## Purpose

We believe external testing is crucial for building a safe AI ecosystem. As model capabilities advance, the consequences of jailbreaks could become increasingly significant. This ongoing Program builds on our successful previous bug bounty initiatives with several key objectives:

1. Identify universal jailbreaks in our deployed systems with ASL-3 protections
2. Provide continuous assessment of our safeguards' effectiveness
3. Test our monitoring systems' ability to detect vulnerabilities
4. Incentivize the user of one central legitimate channel for reporting publicly available jailbreaks

## Program Overview

Our Model Safety Bug Bounty Program is run through HackerOne. Through this Program, we are interested in finding universal jailbreaks that surpass our [Constitutional Classifiers](https://www.anthropic.com/news/constitutional-classifiers) system. We also occasionally run targeted programs within our overall Program to test the robustness of classifiers we hope to launch in the future.

A universal jailbreak is a generalized technique that reliably elicits policy-violating responses from a language model, regardless of the input prompt. Unlike narrow jailbreaks, which depend on the specifics of a particular question or context, universal jailbreaks work across a wide range of prompts and scenarios.

This is an ongoing Program. Once accepted to the Program on HackerOne, participants can submit jailbreak reports at any time through this Program. **To help with your red-teaming efforts, we provide access to a free model alias that reflects the model and classifiers live on our latest, most advanced model**.** Your use of this free model alias must be limited to performing authorized red-teaming activities.**

## Program Scope

This Program is primarily interested in discovering jailbreaks that are **universal**, in that they can reveal harmful information across a wide range of queries, and **detailed**, in that they reveal highly specific harmful information related to biological threats.

To emphasize, we are interested in jailbreaks that extract information that answers a set of **harmful biological questions that we share with accepted participants in the Program.**

We will pay **up to $35,000 per novel, universal jailbreak identified.** We are only interested in jailbreaks that reveal substantial amounts of harmful information based on our sole criteria and discretion. We award bounties using a sliding scale based on an internal grading rubric which determines how detailed and accurate responses are.

This program is scoped to jailbreaks on our Constitutional Classifiers. For technical vulnerabilities that potentially exist on our Information Systems such as misconfigurations, CSRFs or cross site request forgeries, privilege escalation attacks, SQL Injection, XSS, and directory traversal attacks, please refer to our [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy) and submit your report [here](https://hackerone.com/297a385f-b3bd-4ecd-9466-7d9ad55371ce/embedded_submissions/new).

## How to Apply

You can apply to join our Program [here](https://docs.google.com/forms/d/e/1FAIpQLSf3IuyunFH1Rbz_9Bpt2kGBfwSW5QQ1TBkeAzNZrtCP-hRvNA/viewform). We review applications on a rolling basis. If accepted, you will receive an invite via HackerOne. IIf you do not already have a HackerOne account, please create one before applying to the Program so we can invite you directly on the platform. You must use your @wearehackerone.com email alias to create a [Claude Console account](https://platform.claude.com).

## Disclosure Guidelines & Confidentiality Obligations

All Program participants are required to sign a non-disclosure agreement to protect Program confidentiality as a condition for joining. **You may publicly disclose:**

- The existence of Anthropic's Model Safety Bug Bounty Program.
- Your participation as a selected participant in the Program.

**You may not disclose without express permission:**

- Any jailbreaks/vulnerabilities (even resolved ones) outside of the Program without express consent from Anthropic.
- The testing question set.
- Details about the classifiers and safety mitigations.
- Information about the models being tested.
- Identity of other participants.
- Any other information related to the Program, except as expressly permitted above.

## Anthropic’s Use of Data from the Program

Participant agrees that all data submitted to Anthropic, including its products and services, in connection with this Program may be used, stored, shared, and/or published by Anthropic indefinitely in furtherance of its safety research, model development, and related purposes without further obligation to Participant.

## Related Articles
- [Reporting, Blocking, and Removing Content from Claude](https://support.claude.com/en/articles/7996906-reporting-blocking-and-removing-content-from-claude)
- [What is the External Researcher Access Program?](https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program)
- [Reporting, Blocking, and Removing Content from Claude](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)
- [Anthropic's AI for Science Program](https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program)
- [Public Vulnerability Reporting](https://support.claude.com/en/articles/11427875-public-vulnerability-reporting)
