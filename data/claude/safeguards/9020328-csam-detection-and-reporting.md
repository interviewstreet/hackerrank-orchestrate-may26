---
title: "CSAM Detection and Reporting"
title_slug: "csam-detection-and-reporting"
source_url: "https://support.claude.com/en/articles/9020328-csam-detection-and-reporting"
last_updated_iso: "2026-03-16T21:13:10Z"
article_id: "9175078"
breadcrumbs:
  - "Safeguards"
---

# CSAM Detection and Reporting

_Last updated: 2026-03-16T21:13:10Z_

Anthropic strictly prohibits Child Sexual Abuse Material (CSAM) on our services. We are committed to combatting CSAM distribution across our products and will report flagged media and related information to the National Center for Missing and Exploited Children (NCMEC).

As just one example of how we are combatting CSAM distribution: on our first-party services, we use a hash-matching tool to detect and report known CSAM that is included in a user or organization’s inputs. This tool provides access to NCMEC’s database of known CSAM hash values. When an image is sent in an input to our services, we will calculate a perceptual hash of the image. This hash will be automatically compared against the database. In the case of a match, we will notify and provide NCMEC information about the input and the related Account.

As part of Anthropic’s safety process, we will also send a notice to the user or organization any time we report CSAM to NCMEC. If you receive a notification from us about CSAM detection and believe we’ve made an error, please email [usersafety@anthropic.com](mailto:usersafety@anthropic.com).

## Related Articles
- [Our Approach to User Safety](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety)
- [I’m planning to launch a product using the Claude API. What steps should I take to ensure I’m not violating Anthropic’s Usage Policy?](https://support.claude.com/en/articles/8241216-i-m-planning-to-launch-a-product-using-the-claude-api-what-steps-should-i-take-to-ensure-i-m-not-violating-anthropic-s-usage-policy)
- [Law Enforcement Requests](https://support.claude.com/en/articles/9035075-law-enforcement-requests)
- [API Safeguards Tools](https://support.claude.com/en/articles/9199617-api-safeguards-tools)
- [Reporting, Blocking, and Removing Content from Claude](https://support.claude.com/en/articles/10684638-reporting-blocking-and-removing-content-from-claude)
