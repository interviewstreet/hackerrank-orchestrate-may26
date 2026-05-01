---
title: "Best Practices for Email Delivery and Bounce Management Understanding email bounces Best practices to improve email deliverability"
title_slug: "best-practices-for-email-delivery-and-bounce-management-understanding-email-bounces-best-practices-to-improve-email-deliverability"
source_url: "https://support.hackerrank.com/articles/1258426835-best-practices-for-email-delivery-and-bounce-management"
article_slug: "1258426835-best-practices-for-email-delivery-and-bounce-management"
last_updated_exact: "Feb 19, 2026, 3:31 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Screen"
  - "Best Practice Guides"
---

# Best Practices for Email Delivery and Bounce Management Understanding email bounces Best practices to improve email deliverability

_Last updated: Feb 19, 2026, 3:31 PM (Last updated 2 months ago)_

Reliable email delivery is essential for effective candidate communication and uninterrupted hiring workflows. This guide outlines the differences between soft and hard bounces and provides best practices to improve email deliverability.

# Understanding email bounces

An email bounce occurs when a message fails to reach the recipient. Bounces are categorized as either soft or hard depending on whether the failure is temporary or permanent.

## Soft bounces

A soft bounce indicates a temporary failure to deliver an email. The message might be delivered successfully if retried. However, delivery is not guaranteed, especially if a spam filter caused the failure.

Common causes of soft bounces include:

- **Mailbox full**: The recipient’s inbox is full and cannot accept new messages.

- **Server busy**: The recipient’s email server is temporarily unavailable.

- **Message too large**: The email exceeds the server’s size limits.

- **Spam filter**: The email was temporarily blocked by a spam filter.

- **Temporary server error**: A transient issue occurred on the recipient’s server.

## Hard bounces

A hard bounce indicates a permanent failure to deliver an email. The message cannot be delivered and will not be retried.

Common causes of hard bounces include:

- **Invalid recipient**: The email address is incorrect or no longer exists.

- **Invalid domain**: The domain part of the email address is invalid.

- **Blocked**: The email was blocked by the recipient’s server due to security settings or blacklist rules.

- **Inactive address**: The email address was previously valid but is no longer active.

- **Mailbox not found**: The email address does not exist on the server.

- **Invalid sender**: The sender address is not recognized or is rejected by the recipient’s server.

**Note**: Quarantined emails are not categorized as bounces.

# Best practices to improve email deliverability

Follow these best practices to improve email deliverability:

## Allowlist HackerRank domains and IP addresses

Request your IT or security team to allowlist the following HackerRank domain and IP addresses:

- **Domains**:

  - [hackerrank.com](http://hackerrank.com)

  - [hackerrankforwork.com](http://hackerrankforwork.com)

  - [pm-bounces.hackerrankforwork.com](http://pm-bounces.hackerrankforwork.com) 

- **IP Addresses**: Contact the HackerRank Support team to obtain the current list of IP addresses used for outgoing emails.

## Encourage candidates to provide a personal email address

Ask candidates to provide a personal email address (such as Gmail, Outlook) for receiving their HackerRank invitation. Personal email providers offer better delivery rates and fewer bulk-email restrictions.

## Encourage candidates to allowlist HackerRank

Ask candidates to add HackerRank emails to their safe sender list. You can include the following message in your communications:

> *Check your spam or junk folder if you do not receive the HackerRank invitation. We recommend adding* [no-reply@hackerrank.com](mailto:no-reply@hackerrank.com) *to your contacts to ensure future messages are delivered.*

## Avoid spam triggers in custom messages

Format your message carefully to enhance deliverability and minimize the risk of triggering spam filters. Follow these guidelines when drafting or customizing emails.

|  |  |  |  |
|----|----|----|----|
| **Guideline** | **What to Avoid** | **Why It Matters** | **Recommended Practice** |
| **Emphasis formatting** | All-uppercase phrases (for example, IMPORTANT, DISCLAIMER) | All caps can resemble phishing or scam messages. | Use bold, italic, or underline for emphasis instead of all caps. |
| **Urgency language** | Repeated use of terms such as Important | Excessive urgency may appear manipulative or spam-like. | Use urgency once per message. Choose neutral alternatives when possible. |
| **Employment and fee-related wording** | Phrases such as offer of employment and pay fees for application | These phrases resemble scam language if not properly contextualized. | Retain for legal clarity, but review tone and surrounding content. |
| **Spam-triggering phrases** | Language such as Click now, Free access, or overly promotional wording | Common in marketing spam; may reduce trust or trigger spam filters. | Use clear, factual language. Focus on value without exaggeration. |
| **Punctuation and formatting** | Multiple exclamation marks (for example, Apply now!!!), excessive links or images | These patterns are often flagged as spam by mail servers. | Use standard punctuation. Limit images and links to essential content. |
| **Tone and style** | Aggressive, exaggerated, or overly casual language | Reduces professional credibility and increases the risk of being filtered. | Maintain a professional, informative tone throughout the message. |

**Note**: For assistance, contact [support@hackerrank.com](mailto:support@hackerrank.com).

\
