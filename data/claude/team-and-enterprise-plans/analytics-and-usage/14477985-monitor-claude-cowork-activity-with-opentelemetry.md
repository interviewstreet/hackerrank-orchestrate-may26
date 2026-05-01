---
title: "Monitor Claude Cowork activity with OpenTelemetry"
title_slug: "monitor-claude-cowork-activity-with-opentelemetry"
source_url: "https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry"
last_updated_iso: "2026-04-15T22:24:47Z"
article_id: "16934534"
breadcrumbs:
  - "Team and Enterprise plans"
  - "Analytics and usage"
---

# Monitor Claude Cowork activity with OpenTelemetry

_Last updated: 2026-04-15T22:24:47Z_

This article explains how to use OpenTelemetry (OTel) to monitor Claude Cowork activity across your organization. With OTel, your security and operations teams can stream Cowork events into the observability tools you already use to track usage, investigate incidents, and analyze performance.

> OpenTelemetry monitoring for Claude Cowork is available on Team and Enterprise plans. It requires Claude Desktop version 1.1.4173 or later.

---

## What you can monitor

When you connect Claude Cowork to an OpenTelemetry collector, Cowork streams events covering:

- **User prompts. **The full text of prompts users submit to Cowork.
- **Tool and MCP invocations. **Every tool call Claude makes during a session, including MCP server name, tool name, parameters, success or failure, and execution time.
- **File access. **File paths Claude reads, modifies, or otherwise touches during a session, including files accessed through MCPs and folder-scoped local files.
- **Skills and plugins. **Which skills and plugins Claude invokes within a session.
- **Human approval decisions. **Whether each tool action was approved by the user, rejected by the user, or initiated automatically based on existing permissions.
- **API requests and errors. **Per-request model, token counts, estimated cost, duration, and any errors returned.

A shared `prompt.id` attribute links every event triggered by a single user prompt, so you can reconstruct everything Claude did in response to one input.

For the full list of event types and attributes, see the **[Cowork monitoring reference](https://claude.com/docs/cowork/monitoring#events)** in our Claude Docs.

---

## When to use OpenTelemetry

OpenTelemetry gives you a real-time stream of structured Cowork events that you can route into your existing SIEM and observability tools. It's the right choice for security monitoring and incident investigation, tracking tool and file access patterns across your organization, cost and performance analysis, and building dashboards and alerts in your existing pipeline.

OpenTelemetry is **not** a replacement for audit logging. Cowork activity isn't currently captured in audit logs, the Compliance API, or data exports, and OpenTelemetry events don't fill that gap for compliance purposes. If your organization requires formal audit trails, don't use Cowork for regulated workloads. For more, see **[Use Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-cowork-on-team-and-enterprise-plans)**.

## Compatible destinations

Cowork's OpenTelemetry output works with any standard OTel collector. Common destinations include:

- **SIEM platforms **like Splunk and Cribl
- **Log aggregation systems **like Elasticsearch and Loki
- **Columnar stores **like ClickHouse
- **Observability platforms **like Honeycomb and Datadog

You can route events to multiple destinations at once by configuring your collector accordingly.

---

## Set up OpenTelemetry monitoring

To configure Cowork to export events to your collector:

1. Open Claude Desktop and navigate to **Organization settings > Cowork**.
2. Enter your **OTLP endpoint** (your OpenTelemetry collector URL).
3. Select the **OTLP protocol** your collector uses: HTTP/JSON or HTTP/protobuf.
4. Add any **OTLP headers** required for authentication, such as a bearer token.
5. Save your settings.

Events begin flowing to your collector immediately. Authentication headers are encrypted at rest on Anthropic servers.

---

## Security and privacy considerations

A few things to be aware of before you turn on OpenTelemetry export:

- **User prompt content is included in events by default. **If your organization has policies against logging prompt content to your SIEM, configure filtering or redaction in your collector before routing events downstream.
- **Tool parameters may include sensitive values. **File paths, command arguments, and other tool inputs are exported in the tool_parameters field. Plan your retention and access policies accordingly.
- **User email addresses are included in event attributes. **If this is a concern, filter or redact at the collector.
- **Events are only exported when an admin configures an OTLP endpoint. **No data flows by default.

---

## Joining OpenTelemetry data with the Compliance API

Each Cowork OTel event includes a shared user account identifier you can use to correlate events with records from the **[Compliance API](https://support.claude.com/en/articles/13015708-access-the-compliance-api)**. This lets you build a unified view that combines real-time telemetry from OTel with longer-term records from Compliance API queries.

## Related Articles
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
- [Configure a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-configure-a-custom-opentelemetry-collector-for-office-agents)
