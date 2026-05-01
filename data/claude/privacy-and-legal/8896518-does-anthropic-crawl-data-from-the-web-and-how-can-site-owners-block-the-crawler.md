---
title: "Does Anthropic crawl data from the web, and how can site owners block the crawler?"
title_slug: "does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler"
source_url: "https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler"
last_updated_iso: "2026-04-07T21:18:35Z"
article_id: "9027581"
breadcrumbs:
  - "Privacy and legal"
---

# Does Anthropic crawl data from the web, and how can site owners block the crawler?

_Last updated: 2026-04-07T21:18:35Z_

As per industry standard, Anthropic uses a variety of robots to gather data from the public web for model development, to search the web, and to retrieve web content at users’ direction.  Anthropic uses different robots to enable website owner transparency and choice.  Below is information on the three robots that Anthropic uses and how to set your site preferences to enable those you want to access your content and limit those you don’t.

As part of our mission to build safe and reliable frontier systems and advance the field of responsible AI development, we’re sharing the principles by which we collect data as well as instructions on how to opt out of our crawling going forward:

- Our collection of data should be *transparent*. Anthropic uses the Bots described above to access web content.
- Our crawling should *not* *be* *intrusive or disruptive*. We aim for minimal disruption by being thoughtful about how quickly we crawl the same domains and respecting Crawl-delay where appropriate.
- Anthropic’s Bots *respect “do not crawl”* signals by honoring industry standard directives in robots.txt.
- Anthropic’s Bots *respect anti-circumvention technologies *(e.g., we will not attempt to bypass CAPTCHAs for the sites we crawl.)

To limit crawling activity, we support the non-standard Crawl-delay extension to robots.txt. An example of this might be:

User-agent: ClaudeBot

Crawl-delay: 1

To block a Bot from your entire website, add this to the robots.txt file in your top-level directory. Please do this for every subdomain that you wish to opt out from. An example of this is:

User-agent: ClaudeBot

Disallow: /

Opting out of being crawled by Anthropic Bots requires modifying the robots.txt file in the manner above. Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file. If a crawler has a source IP address on **[this list](https://claude.com/crawling/bots.json)**, it indicates that the crawler is coming from Anthropic.

You can learn more about our data handling practices and commitments at our **[Help Center](https://support.claude.com/en/collections/4078534-privacy-and-legal)**. If you have further questions, or believe that our Bots may be malfunctioning, please reach out to [claudebot@anthropic.com](mailto:claudebot@anthropic.com). Please reach out from an email that includes the domain you are contacting us about, as it is otherwise difficult to verify reports.

> You can be notified of substantial changes to this article by clicking here and completing the form:
>
> Subscribe to updates

## Related Articles
- [Reporting, Blocking, and Removing Content from Claude](https://support.claude.com/en/articles/7996906-reporting-blocking-and-removing-content-from-claude)
- [How to get support](https://support.claude.com/en/articles/9015913-how-to-get-support)
- [Does Anthropic Act as a Data Processor or Controller?](https://support.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller)
- [Reporting, Blocking, and Removing Content from Claude](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)
- [Claude in Chrome Permissions Guide](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide)
