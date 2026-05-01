---
title: "Claude Enterprise Analytics API reference guide"
title_slug: "claude-enterprise-analytics-api-reference-guide"
source_url: "https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide"
last_updated_iso: "2026-04-09T14:18:22Z"
article_id: "15825475"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Analytics and usage"
---

# Claude Enterprise Analytics API reference guide

_Last updated: 2026-04-09T14:18:22Z_

## Overview

The Claude Enterprise Analytics API gives your organization programmatic access to engagement data for Claude and Claude Code usage within your Enterprise organization. Whether you're building internal dashboards for user activity or tracking adoption of projects, this API provides the aggregated metrics you need.

## Data aggregation

All data is aggregated **per organization, per day**. Each endpoint returns a snapshot for a single date that you specify. **Data for day (N-1) is run at 10:00:00 UTC time on day N**, and is available for querying three days after aggregation, to ensure accuracy of data.

If data is not available within the timeline above, this usually indicates a data pipeline failure that our team will need to investigate internally. We are usually aware of such problems, but please raise this to your CSM if you want a gut check, or suspect something else.

## Enabling access

In order to mint new analytics API keys, you must be a Primary Owner within your Enterprise organization. You can do so by navigating to **[claude.ai/analytics/api-keys](http://claude.ai/analytics/api-keys)**.

Some more details that might be helpful:

- You can *enable/disable *access to the public API anytime. If you disable access by toggling the switch off, all requests will be denied.
- You’ll need a key with the `read:analytics` scope in order to access the API. You can create multiple keys for your organization, but rate limits apply at the *organization *level, not the *key *level. See the “Rate limiting” section below.
- As always, *we strongly recommend handling API keys securely*: *never *share these keys publicly - they are secret, and should be shared securely.

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2053655566/6858d308d21c1d082cf67cdabd3b/19fadcdf-25f5-491d-a060-887da34b1082?expires=1776784500&signature=8cd26705e53d8b197f192923f5246e88f230bcd0446adcb226f2fc91e3107620&req=diAiFc97mIRZX%2FMW1HO4zXfNQF8HehLeFbDaBcaxqj6ZDP2AOLP5K%2BiPB5kn%0Ai0hhHU8Ed8zjC9GAvPE%3D%0A)

## Base URL

All requests are sent to:

```
https://api.anthropic.com/v1/organizations/analytics/
```

## Authentication

Every request requires an API key passed in the `x-api-key` header. Your API key must have the `read:analytics` scope. You can create and manage API keys from the claude.ai admin settings under the API Keys section.

**Example request headers:**

```
x-api-key: $YOUR_API_KEY
```

## Pagination

Several endpoints return paginated results. Pagination uses a cursor-based approach, where the response includes a `next_page` token you pass back in your next request to retrieve the following page of results.

Two optional parameters control pagination:

**limit** (integer): Number of records per page. Defaults to 20 for the /users endpoint and 100 for all other endpoints. The maximum is 1000.

**page** (string): The opaque cursor token from the previous response's `next_page` field. Omit this on your first request.

When there are no more results, `next_page` will be `null` in the response.

## Error responses

All endpoints return standard HTTP error codes:

## Rate limiting

We do have default rate limits in place. If that isn’t sufficient for your use case, we’d love to understand why. If necessary, we can adjust the rate limits for your organization—please reach out to your CSM.

---

## Endpoints

#### 1. List user activity

`GET /v1/organizations/analytics/users`

Returns per-user engagement metrics for a single day. Each item in the response represents one user and includes their activity counts across Claude (chat) and Claude Code.

**Query parameters**

**Response fields (per user)**

**Office Agent metrics (per user)**

Each user record also includes an `office_metrics` object with per-product breakdowns for Excel and PowerPoint. This block is always present on every record—organizations without Office Agent usage see all-zero values rather than null.

The office_metrics object contains two keys: `excel` and `powerpoint`.

Each key contains the same six fields:

***Note:** Where `[product]` is one of `excel` or `powerpoint`.

**Claude Cowork metrics (per user)**

Each user record also includes a cowork_metrics object with per-user Cowork engagement. This block is always present on every record—organizations without Cowork usage see all-zero values rather than null.

**Example request**

```
curl -X GET "https://api.anthropic.com/v1/organizations/analytics/users?date=2025-01-01&amp;limit=3"<br>   --header "x-api-key: $YOUR_API_KEY"
```

#### 2. Activity summary

`GET /v1/organizations/analytics/summaries`

Returns a high-level summary of engagement and seat utilization **per-day** for your organization for a given date range. The response is a list of days with aggregated counts within the date range. Note that the maximum difference between `ending_date` and `starting_date` must be **31 days**, and there is a three-day delay in data availability. This is useful for tracking daily active users, weekly and monthly trends, and seat allocation at a glance.

**We define “active”** if any one of the following is true:

- The user sent at least one chat message on Claude (chat).
- The user had at least one Claude Code (local or remote) session associated with the C4E org, with tool use/git activity
- The user had at least one Claude Cowork session with tool use or message activity.

**Query parameters**

**Response fields**

> **Note:** The rolling windows for weekly and monthly counts look backward from the specified date (inclusive). If data is incomplete for some days within the window (for example, if the date is less than 30 days in the past), the monthly count may undercount activity.

**Example request**

```
curl -X GET "https://api.anthropic.com/v1/organizations/analytics/summaries?starting_date=2025-01-01"<br>   --header "x-api-key: $YOUR_API_KEY"
```

#### 3. Chat project usage

`GET /v1/organizations/analytics/apps/chat/projects`

Returns usage data broken down by chat project for a given date. Projects are specific to Claude (chat), so this endpoint focuses on that surface. Each item shows the project name, how many unique users interacted with it, and the total number of conversations held in that project.

**Query parameters**

**Response fields (per project)**

**Example request**

```
curl -X GET "https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects?date=2025-01-01&amp;limit=50"<br>   --header "x-api-key: $YOUR_API_KEY"
```

#### 4. Skill usage

`GET /v1/organizations/analytics/skills`

Returns skill usage data across both Claude (chat) and Claude Code within your organization for a given date. Each item represents a skill and shows how many unique users used it.

**Query parameters**

**Response fields (per skill)**

**Office Agent metrics (per skill)**

Each skill record also includes an office_metrics object that reports how many Office Agent sessions used the skill, broken down by product. This block is always present—organizations without Office Agent usage see all-zero values.

**Claude Cowork metrics (per skill)**

Each skill record also includes a `cowork_metrics` object that reports how many Cowork sessions used the skill. This block is always present—organizations without Cowork usage see all-zero values.

**Example request**

```
curl -X GET "https://api.anthropic.com/v1/organizations/analytics/skills?date=2025-01-01"<br>   --header "x-api-key: $YOUR_API_KEY"
```

#### 5. Connector usage

`GET /v1/organizations/analytics/connectors`

Returns MCP/connector usage data across both Claude (chat) and Claude Code within your organization for a given date. Each item represents a connector and shows how many unique users used it. Connector names are normalized from various sources — for example, "Atlassian MCP server," "mcp-atlassian," and "atlassian_MCP" would all appear as "atlassian."

**Query parameters**

**Response fields (per connector)**

**Office Agent metrics (per connector)**

Each connector record also includes an office_metrics object that reports how many Office Agent sessions used the connector, broken down by product. This block is always present—organizations without Office Agent usage see all-zero values.

**Claude Cowork metrics (per connector)**

Each connector record also includes a `cowork_metrics` object that reports how many Cowork sessions used the connector. This block is always present—organizations without Cowork usage see all-zero values.

**Example request**

```
curl -X GET "https://api.anthropic.com/v1/organizations/analytics/connectors?date=2025-01-01"<br>   --header "x-api-key: $YOUR_API_KEY"
```

## Related Articles
- [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Claude Enterprise Analytics API: Access engagement and adoption data](https://support.claude.com/en/articles/13694757-claude-enterprise-analytics-api-access-engagement-and-adoption-data)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)
