---
title: "Using the Blackbaud Connector in Claude"
title_slug: "using-the-blackbaud-connector-in-claude"
source_url: "https://support.claude.com/en/articles/12923221-using-the-blackbaud-connector-in-claude"
last_updated_iso: "2026-03-16T20:59:01Z"
article_id: "14637538"
breadcrumbs:
  - "Claude for Nonprofits"
---

# Using the Blackbaud Connector in Claude

_Last updated: 2026-03-16T20:59:01Z_

The Blackbaud Connector provides Claude with secure access to Raiser’s Edge NXT fundraising data, enabling nonprofit professionals to retrieve donor records, gifts, events, and generate communications using natural language. This article explains how to set up and use the Blackbaud Connector for your fundraising workflows.

The Blackbaud Connector relies upon Claude’s ability to use remote connectors.

## What This Integration Provides

#### Capabilities

The Blackbaud Connector enables Claude to access and interact with your fundraising data from Raiser’s Edge NXT.

- **Constituent Profile Retrieval:** Access detailed donor profiles including contact information, affiliations, and giving history. Claude can retrieve comprehensive constituent data on demand.
- **Constituent Search:** Search for donors by name or partial name across your Raiser’s Edge NXT database, making it easy to find specific individuals in your records.
- **Event Discovery:** Search for fundraising events by name or keyword and retrieve event details including dates, locations, funds raised, and participant information.
- **Gift Record Access:** View specific gift records including donation amounts, dates, donors, and associated campaigns to understand giving patterns.
- **Communication Generation:** Draft personalized thank-you notes, outreach emails, and other donor communications using data from your records.
- **Real-Time Data Access:** The connector fetches information on-demand from Raiser’s Edge NXT, ensuring the data Claude provides is current at the moment you ask.

#### How Claude Uses Blackbaud Data

Claude applies your Blackbaud fundraising data to support nonprofit workflows.

- Donor Research: Retrieves constituent profiles and giving histories to help you understand donor relationships and prepare for meetings or outreach.
- Gift Analysis: Pulls donation records to identify giving patterns, track campaign performance, and recognize major donors.
- Event Planning Support: Searches event records to review past fundraising activities, compare results, and inform future event strategies.
- Personalized Communications: Uses donor data to draft customized thank-you letters, appeals, and follow-up messages that reference specific gifts and engagement history.
- Quick Data Lookups: Enables rapid answers to questions about constituents, events, or gifts without requiring you to open Raiser’s Edge NXT directly.

## Setting Up the Blackbaud Connector

#### For Blackbaud Marketplace Admins

Your Marketplace admin needs to connect the Claude for Blackbaud application:

1. Navigate to the [Claude for Blackbaud app](https://app.blackbaud.com/marketplace) in the Blackbaud Marketplace.
2. Connect it to your Blackbaud environment.
3. Approve scopes during installation for access to constituent and event data.

#### For Organization Owners

1. From [Claude.ai](http://claude.ai), navigate to Settings.
2. Select Connectors or Integrations.
3. Select Add server or Browse connectors.
4. Search for and select Blackbaud from the available connectors.
5. Follow the prompts to add the Blackbaud server to your Claude organization.
6. Confirm authorization to enable the integration.

#### For Individual Users

After admin setup is complete:

1. Log into Claude with your enterprise account.
2. Go to Settings, then Connectors.
3. Select Blackbaud Connector, then choose Connect or Authorize.
4. Sign in with your Blackbaud ID and grant permission for Claude to access your data.
5. Your Blackbaud account will show as Linked once authorization is complete.

## Common Use Cases

#### Donor Lookup

Example prompt:

```
Show me the profile for Jane Smith, including her contact information and <br>recent donations.
```

**When to use:** Preparing for donor meetings, reviewing constituent relationships, or verifying contact details.

**Tip:** Include the donor’s full name for more accurate results.

#### Gift History Analysis

Example prompt:

```
What are the details of John Doe’s donations over the past year? Include <br>amounts, dates, and which campaigns they supported.
```

**When to use:** Reviewing donor engagement, preparing acknowledgment letters, or analyzing giving patterns.

**Works well with:** Requests spanning 1-3 years to identify trends without overwhelming detail.

#### Event Research

Example prompt:

```
Find any events titled “Annual Gala” and show me the details including <br>attendance and funds raised.
```

**When to use:** Planning future events, comparing year-over-year performance, or researching past fundraising activities.

**Note:** Use specific keywords that match your event naming conventions for best results.

#### Thank-You Letter Drafting

Example prompt:

```
Draft a personalized thank-you email to Sarah Johnson for her recent $500 <br>donation to the Building Fund campaign.
```

**When to use:** Following up on donations, acknowledging major gifts, or sending timely appreciation messages.

**Key benefit:** Claude retrieves the donor’s information and gift details to create personalized, accurate communications.

#### Constituent Search

Example prompt:

```
Find all constituents named Williams in our database.
```

**When to use:** Locating donors when you have partial name information or searching for related family members.

**Tip:** Start with partial searches and narrow down results based on additional identifying information.

## Tips for Using the Blackbaud Connector

- Use full donor names for more accurate constituent lookups.
- Specify time periods when requesting gift histories (e.g., “past 12 months,” “2024 fiscal year”).
- Ask naturally—describe what you need as if asking a colleague.
- Combine multiple requests when helpful (e.g., “Show me Jane’s profile and draft a thank-you for her last gift”).
- Always review AI-generated communications before sending, especially those involving sensitive donor information.
- Remember that Claude only accesses data your Blackbaud user account is authorized to view.

## Related Articles
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Getting started with Claude for Nonprofits](https://support.claude.com/en/articles/12893767-getting-started-with-claude-for-nonprofits)
- [Using the Benevity Connector in Claude](https://support.claude.com/en/articles/12923227-using-the-benevity-connector-in-claude)
- [Using the Candid Connector in Claude](https://support.claude.com/en/articles/12923235-using-the-candid-connector-in-claude)
- [Use interactive connectors in Claude](https://support.claude.com/en/articles/13454812-use-interactive-connectors-in-claude)
