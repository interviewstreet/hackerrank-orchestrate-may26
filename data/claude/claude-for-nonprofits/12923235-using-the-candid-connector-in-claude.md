---
title: "Using the Candid Connector in Claude"
title_slug: "using-the-candid-connector-in-claude"
source_url: "https://support.claude.com/en/articles/12923235-using-the-candid-connector-in-claude"
last_updated_iso: "2026-03-16T20:29:37Z"
article_id: "14637558"
breadcrumbs:
  - "Claude for Nonprofits"
---

# Using the Candid Connector in Claude

_Last updated: 2026-03-16T20:29:37Z_

The Candid integration brings the power of Candid’s comprehensive nonprofit and funder data directly into Claude. This article explains how to set up and use the Candid connector to search millions of organizations, discover funding opportunities, and access expert knowledge about the social sector—all through natural conversation.

The Candid integration relies upon Claude’s ability to use remote connectors.

## What this integration provides

The Candid integration connects Claude directly to Candid’s extensive database of nonprofit and philanthropic information. Candid is a nonprofit that provides the most comprehensive data and insights about the social sector, connecting people who want to change the world with the resources they need to do it.

This integration provides access to:

- Over 1.9 million nonprofits and foundations
- Expert knowledge base with research reports, training materials, and news
- Taxonomies describing work across the nonprofit and philanthropic sector
- Comprehensive organizational profiles with mission, location, financials, and grants data

## Who can access the Candid integration?

The Candid integration is available to Claude Pro users. A Candid account is not required to use basic search functionality. Some advanced features may require additional authentication.

> **Note:** This tool is currently in beta. Core functionality is available, but some advanced features are still under development. Please reach out with feedback to [onlinelibrarian@candid.org](mailto:onlinelibrarian@candid.org).

## Setting up the Candid integration

#### For Organization Owners (Team and Enterprise)

1. Navigate to [Admin settings > Connectors](https://claude.ai/admin-settings/connectors)
2. Select “Browse connectors”
3. Search and select “Candid”
4. Select “Add to your team”

#### For Individual Claude Users

1. Navigate to Settings > Connectors
2. Select “Browse connectors”
3. Search and select “Candid”
4. Follow the instructions to enable the Candid connector

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-using-the-connectors-directory-to-extend-claude-s-capabilities) in Claude.

---

## Available tools

The Candid MCP connector provides several powerful tools that Claude can use to answer your questions. Here are the main capabilities:

#### 1. Search organizations

**What it does:** Search for nonprofits and foundations by name, mission description, location, or areas of work.

**Use it for:**

- Finding specific organizations by name or EIN
- Discovering organizations working on particular issues
- Locating nonprofits serving specific geographic areas
- Finding organizations with specific transparency levels or leadership demographics

**Example queries:**

- "Find homeless shelters in New York City that have specific support for women"
- "Show me environmental foundations in Northern California"

**Key features:**

- Hybrid search combining keyword and semantic matching
- Filter by location (postal code, state/province, or geographic IDs)
- Filter by subject areas and populations served
- Filter by transparency seals (Platinum, Gold, Silver, Bronze)
- Filter by leader demographics (women, BIPOC, LGBTQ+, people with disabilities)
- Access organizational mission and program information

#### 2. Find mentioned organizations

**What it does:** Automatically identifies organization names in responses and links them to official Candid profiles.

**Use it for:**

- Getting quick access to detailed organization profiles
- Verifying organization information
- Exploring organizations mentioned in research or news articles

**How it works:** When Claude mentions an organization, this tool finds the official match in Candid's database and creates clickable links to their profiles—no extra work required! If you have a paid subscription to [Candid’s web products](https://candid.org/), you can also click through to see advanced information like specific grant histories, in-depth financials, affiliated people, or openness to funding applications.

#### 3. Knowledge search

**What it does:** Search Candid's expert knowledge base including research reports, training materials, blog posts, and curated news.

**Use it for:**

- Learning about trends in philanthropy
- Finding best practices and expert guidance
- Staying current with sector news
- Accessing academic research on social issues
- Getting help with Candid's platform and tools

**Available sources:**

- Candid insights: Articles from sector experts and thought leaders
- Candid help: FAQs and guidance on using Candid's platform
- Candid learning: Training documents from subject matter experts
- Candid news: Real-time updates on philanthropic activity worldwide
- IssueLab research reports: Academic research on the social sector
- YouTube training: Transcripts from video training seminars

**Example queries:**

- "What are recent trends in climate philanthropy?"
- "How do I write an effective grant proposal?"
- "What's new in nonprofit fundraising strategies?"
- "Show me research on food insecurity in rural communities"

#### 4. Find relevant taxonomic terms

**What it does:** Uses AI to identify relevant terms from Candid's Philanthropy Classification System (PCS) taxonomy based on your description.

**Use it for:**

- Understanding how Candid categorizes work in the social sector
- Getting accurate taxonomy codes for advanced searches
- Exploring related subject areas or populations served

**Example queries:**

- "What taxonomy terms relate to mental health services for veterans?"
- "Show me PCS codes for climate change work"

**About the PCS taxonomy:** Candid's taxonomy describes activity across the social and philanthropic sectors, covering subjects (what organizations work on) and populations served (who they serve). Learn more at taxonomy.candid.org.

#### Behind the scenes

The connector also includes technical tools that work automatically in the background to ensure accurate, timely results—like converting location descriptions into searchable geographic codes, or identifying the current date for time-sensitive queries. You don't need to think about these; Claude uses them automatically when needed.

---

## Usage examples

#### Example 1: Finding organizations in your area

**You ask:** "I'm looking for foundations in California that fund youth education programs."

**Claude will:**

1. Use Search Organizations with relevant filters (admin1='CA', search terms related to youth education)
2. Return a list of matching foundations with links to their Candid profiles
3. Provide relevant details like location, mission focus, and Seals of Transparency level

**Sample response:**

Based on my search of Candid's database, I found several notable foundations in California that fund youth education programs:

Quest Foundation - Danville, CA

- Has awarded 243 grants totaling over $9.3 million
- Focuses on: elementary and secondary education, charter schools, higher education, reading promotion, and youth services
- Also supports family services and child welfare

Ross Stores Foundation - Dublin, CA

- Has awarded 225 grants totaling over $4 million
- Accepts applications (though no current open funding opportunities listed)
- Focuses on: higher education, out-of-school learning, reading promotion, and youth development
- Specifically serves children and youth

[Additional details about their focus areas...]

#### Example 2: Researching sector trends

**You ask:** "What are the latest trends in climate philanthropy?"

**Claude will:**

1. Use Knowledge Search to find recent articles, research, and blog posts about climate philanthropy.
2. Use Find Mentioned Organizations to link any organizations mentioned in the content.
3. Synthesize findings into a comprehensive overview.

**Sample response:**

Based on the latest research and insights from the philanthropic sector, here are the key trends shaping climate philanthropy:

*Significant Growth, But Still Insufficient*

Foundation funding for climate mitigation nearly tripled from 2019 to 2023, reaching $4.8 billion according to ClimateWorks Foundation. However, this represents less than 2% of global philanthropic giving—far below what's needed to address the crisis.

*Major Geographic Disparities*

60% of single-region foundation funding goes to the U.S. and Europe, while Africa, Asia, Oceania, and Latin America receive only 20%. Low- to middle-income countries most vulnerable to climate impacts capture just 14% of funding.

[Additional insights with citations and links...]

#### Example 3: Exploring organizations by mission

**You ask: **"Help me find nonprofits working on food access in Seattle that are highly transparent."

**Claude will:**

1. Use Find Named Locations to identify Seattle's geographic ID
2. Use Find Relevant Taxonomic Terms to identify food security subject codes
3. Use Search Organizations with location, subject, and Seals of Transparency filters
4. Return a curated list with profile links and details about their work

#### Example 4: Learning about the sector

**You ask:** "I'm new to grant writing. What are best practices?"

**Claude will:**

1. Use Knowledge Search targeting Candid learning and Candid Help sources
2. Provide expert guidance from Candid's training materials
3. Link to relevant articles and video transcripts for deeper learning

---

## Tips for best results

#### Be specific with locations

When searching for organizations, specific location information helps narrow results:

- ✅ "nonprofits in Brooklyn, New York"
- ✅ "foundations serving rural Montana communities"
- ❌ "organizations in the Northeast" (too broad)

#### Describe work, not just keywords

The search tools understand descriptions of work, not just keywords:

- ✅ "organizations helping homeless youth find permanent housing"
- ✅ "funders supporting immigrant and refugee integration programs"
- ✅ "nonprofits providing mental health services to veterans"

#### Combine filters for precision

#### You can request multiple filters at once:

- "Environmental organizations in California with BIPOC leadership"
- "Healthcare nonprofits in Texas with Platinum transparency seals"

#### Ask follow-up questions

Once you have results, dig deeper:

- "Tell me more about [organization name]"
- "What is this organization's mission?"
- "Are there similar organizations in other states?"

#### Use knowledge search for context

Before diving into organizational data, get context:

- "What should I know about funding for affordable housing?"
- "What are current best practices in nonprofit board governance?"

#### Be careful with analytical questions

The current tool is designed for searching about specific organizations or general sector knowledge. It does not currently directly support questions involving calculations, aggregations, or analysis like:

- "Which nonprofits received the 3 largest grants for community healthcare in 2023?”
- “What was the % change in funding from these grant providers in the last 5 years?”

Claude may still try to answer these questions, but it may not be fully accurate. We are working on supporting such questions directly in the future - stay tuned! In addition, deeper information on grants funding and trends is always available through Candid's subscription products on candid.org.

## Common use cases

#### Find organizations

Search for nonprofits and foundations by name, mission, location, leadership demographics, or area of work.

Example prompts:

```
“Find nonprofits focused on climate change adaptation in California.”<br>“Show me foundations that fund education initiatives in rural areas.”<br>“What organizations work on affordable housing in Chicago?”
```

#### Research organizational profiles

Get comprehensive details about specific organizations including their mission, programs, financials, and leadership.

Example prompts:

```
“Tell me about the Ford Foundation’s grantmaking priorities”<br>“What is the annual budget of Habitat for Humanity?”<br>“Who are the board members of the Sierra Club Foundation?”
```

#### Discover funding opportunities

Find foundations and funding opportunities that match specific criteria or project areas.

Example prompts:

```
“What foundations fund early childhood education programs?”<br>“Find corporate giving programs that support STEM education”<br>“Which funders have given grants to organizations working on food<br>insecurity?”
```

#### Access expert knowledge

Tap into Candid’s research reports, training materials, and social sector news.

Example prompts:

```
“What are current trends in nonprofit fundraising?”<br>“How do I write a strong grant proposal?”<br>“What are best practices for nonprofit board governance?”
```

## FAQs

#### Is the Candid integration free to use?

Yes! Basic search functionality is free for all paid Claude plans. Some advanced features requiring access to premium Candid data may require additional authentication.

#### How current is the data?

Candid updates its data continuously:

- **Organization data:** Updated regularly from IRS filings, official registrations, and direct organization input.
- **Knowledge base:** Updated continuously with new research, articles, and news.
- **News:** Updated daily with curated sector news.

The integration provides real-time access to the latest available data.

#### Can I search international organizations?

Candid has the most comprehensive and up-to-date coverage of US organizations.

#### What if I can't find a specific organization?

Not all organizations are in Candid's database. Coverage is most comprehensive for:

- US IRS-registered 501(c)(3) organizations
- US grantmaking foundations
- Organizations that have claimed their Candid profiles

If you can't find an organization, try:

- Searching by EIN (for US organizations)
- Using alternate names or acronyms
- Broadening your search terms

#### How do I interpret Seals of Transparency?

Candid Seals of Transparency indicate how much information an organization has shared:

- **Platinum:** Most comprehensive information provided including metrics.
- **Gold:** Dive deep into detailed financials and demographics information.
- **Silver:** More organizational information shared such as program information.
- **Bronze:** Basic core organization information provided.
- **No Seal:** Organization claimed their profile but didn't complete the transparency process.

---

## Privacy and data usage

- The Candid integration accesses publicly available nonprofit organization information
- No personal user data is shared with Candid through the integration
- Search queries are used only to retrieve relevant organizational results
- All data comes from Candid’s verified nonprofit database

## Need more help?

If you’re experiencing issues with the Candid integration or have questions not covered here, please contact Claude support or visit our help center for additional troubleshooting guides. For Candid-specific questions, you can reach out to [onlinelibrarian@candid.org](mailto:onlinelibrarian@candid.org).

## Related Articles
- [Using Research on Claude](https://support.claude.com/en/articles/11088861-using-research-on-claude)
- [Getting started with Claude for Nonprofits](https://support.claude.com/en/articles/12893767-getting-started-with-claude-for-nonprofits)
- [Using the Blackbaud Connector in Claude](https://support.claude.com/en/articles/12923221-using-the-blackbaud-connector-in-claude)
- [Using the Benevity Connector in Claude](https://support.claude.com/en/articles/12923227-using-the-benevity-connector-in-claude)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
