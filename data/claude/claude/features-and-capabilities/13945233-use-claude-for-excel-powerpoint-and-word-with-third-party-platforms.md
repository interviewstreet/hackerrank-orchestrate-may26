---
title: "Use Claude for Excel, PowerPoint, and Word with third-party platforms"
title_slug: "use-claude-for-excel-powerpoint-and-word-with-third-party-platforms"
source_url: "https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms"
last_updated_iso: "2026-04-15T21:18:35Z"
article_id: "16218832"
breadcrumbs:
  - "Claude"
  - "Features and capabilities"
---

# Use Claude for Excel, PowerPoint, and Word with third-party platforms

_Last updated: 2026-04-15T21:18:35Z_

If your organization uses AWS Bedrock, Google Cloud Vertex AI, Azure AI Foundry, or an LLM gateway to access Claude, you can use the Claude for Excel, Claude for PowerPoint, and Claude for Word add-ins without a Claude account. The add-in connects through your organization's infrastructure, so your prompts and responses stay within your existing trust boundary.

There are four connection paths, depending on how your organization accesses Claude:

- **LLM gateway**: The add-in sends requests to your gateway (LiteLLM, Portkey, Kong, etc.), which routes them to the provider of your choice. This is the same pattern used by Claude Code. If your organization already runs **[Claude Code through an LLM gateway](https://code.claude.com/docs/en/llm-gateway)**, you can point the Office add-ins at the same endpoint—no new infrastructure is required.
- **Bedrock direct**: The add-in authenticates through Microsoft Entra ID and calls AWS Bedrock directly, with no gateway in between.
- **Vertex AI direct**: The add-in authenticates through Google OAuth and calls Vertex AI directly.
- **Foundry direct: **The add-in authenticates through your Azure AI Foundry resource directly using its API key.

Your IT admin chooses the path during deployment. As an end user, the experience is the same regardless of which path your organization uses.

---

## Requirements

Requirements vary by connection path.

**All paths:**

- Claude for Excel, Claude for PowerPoint, or Claude for Word installed (from Microsoft AppSource or deployed by your admin)
- Microsoft 365 with Entra ID (for admin consent and, in the direct-cloud paths, token issuance)

**LLM gateway:**

- A gateway URL and API token from your IT team

**Bedrock direct:**

- An AWS account with Claude model access enabled in the target region
- An IAM OIDC identity provider and role configured to trust Microsoft Entra ID tokens

**Vertex AI direct:**

- A Google Cloud project with the Vertex AI API enabled and Claude model access in the target region
- A Google OAuth client configured with the add-in's redirect URI

**Foundry direct:**

- **An Azure AI Foundry resource with at least one Claude model deployed (Claude Opus 4.6, Opus 4.5, Sonnet 4.6, or Sonnet 4.5)**
- Deployment names must be left as the default model IDs (e.g. claude-opus-4-6); custom deployment names aren't supported yet. The adapter probes by model ID, so a renamed deployment won't be found.
- The resource's API key, from **Azure Portal → your Foundry resource → Keys and Endpoint → KEY 1**

Your organization's IT team manages these resources. If you don't have the credentials you need, contact them—Anthropic can't provide or reset them for you.

---

## Network allowlist

The add-in needs to reach specific domains to function. Which domains depend on whether your organization uses the Anthropic API directly (1P) or a third-party platform (3P). Share the applicable table with your network or security team so they can allowlist these domains.

> **Important:** In all configurations—including third-party—your prompts and Claude's responses travel only to your chosen inference provider (your gateway, Bedrock, Vertex AI, or Azure AI Foundry). The domains listed below that point to Anthropic (such as pivot.claude.ai) serve the add-in's interface, feature configuration, and operational telemetry. They don't carry prompt or response content.

#### Anthropic API (1P)

Use this table if people in your organization sign in with a Claude account and inference goes to api.anthropic.com.

#### Third-party platforms (3P)

Use this table if people in your organization sign in with Microsoft Entra ID and inference goes to your LLM gateway, Bedrock, or Vertex AI.

---

## Deploy the add-in for third-party use (IT admins)

Use the `claude-in-office` plugin to configure and deploy the add-in across your organization. This tool handles provisioning cloud resources (if using Bedrock or Vertex AI direct), generating the add-in manifest, and obtaining admin consent in a single guided flow.

#### Use the setup wizard

**[Install the plugin](https://github.com/anthropics/financial-services-plugins/tree/main/claude-in-office)** and run the interactive setup wizard:

```
claude plugin marketplace add anthropics/financial-services-plugins<br>claude plugin install claude-in-office@financial-services-plugins<br>/claude-in-office:setup
```

The wizard walks you through your connection path:

- **LLM gateway**: Collects your gateway URL and token, determines which API format to use, generates the manifest, and handles Azure admin consent.
- **Bedrock direct**: Creates the IAM OIDC identity provider and role, generates the manifest, and handles Azure admin consent.
- **Vertex AI direct**: Walks you through creating the Google OAuth client, generates the manifest, and handles Azure admin consent.
- **Foundry direct:**  Captures `azure_resource_name` and `azure_api_key`, then generates the manifest.

When the wizard completes, the add-in is ready to deploy tenant-wide.

> **Note:** The Bedrock and Vertex AI paths require Node.js for manifest generation and validation. The wizard checks for it and prompts you to install it if it's missing.

You can use the following commands inside a `claude-in-office` session:

#### What the wizard provisions

The wizard automates resource creation based on your connection path. Here's what it sets up:

**LLM gateway**: No cloud resources to provision. The wizard collects your gateway URL and token, then generates the manifest.

**Bedrock direct**: Creates an IAM OIDC identity provider that trusts Microsoft Entra ID tokens, a role with bedrock:InvokeModel and bedrock:InvokeModelWithResponseStream permissions, and a trust policy scoped to the Claude add-in's application ID.

**Vertex AI direct**: Walks you through creating a Google OAuth client in the GCP Console (this step can't be automated via CLI), enables the Vertex AI API, and captures the client ID and secret for the manifest.

**Foundry direct**:  No cloud resources to provision; the wizard collects the resource name and API key for the manifest.

#### Per-user configuration

If some values vary per user—for example, different gateway tokens or different AWS roles for different teams—the wizard can write per-user configuration via Microsoft Graph extension attributes. Run `/claude-in-office:update-user-attrs` with the per-user keys after the initial setup.

#### Deploy to Microsoft 365

After the wizard generates your manifest:

1. Open the **Microsoft 365 Admin Center** and go to **Settings** > **Integrated Apps** > **Upload custom apps**.
2. Select “Office Add-in” as the app type, then upload the manifest.xml file.
3. Choose who gets the add-in:
  - If all users share the same configuration, select “Entire organization.”
  - If you wrote per-user attributes in the previous step, assign to **Specific users/groups** matching exactly who was configured. Anyone else would open the add-in with no configuration.
4. Accept permissions and finish deployment.

Propagation to users takes up to 24 hours (usually much faster). The add-in appears under **Home** > **Add-ins** in Excel, PowerPoint, and Word once it lands.

> **Note:** Start with a pilot group to confirm the add-in works, then widen the assignment. You can change assignment later without redeploying.

After deploying the add-in, your users can connect by following the steps below.

---

## Connection instructions for end users

#### LLM gateway

1. Open Excel, PowerPoint, or Word and launch the Claude add-in.
2. On the sign-in screen, select "Enterprise gateway."
3. Enter the **Gateway URL** and **API token** your IT team provided.
  - **Gateway URL**: The HTTPS base URL of your LLM proxy (for example, [https://llm-gateway.yourcompany.com](https://llm-gateway.yourcompany.com)).
  - **API token**: The bearer token your proxy expects. The add-in sends this in the Authorization: Bearer <token> header with every request.
4. The add-in checks the connection by sending a test request to the gateway. If it succeeds, you'll see the main app experience.

Your credentials are stored locally in your browser's localStorage within the add-in's sandboxed iframe. They aren't synced to Anthropic's servers. Because the Office add-in runs inside a sandboxed iframe within the Microsoft application, it can't use your OS keychain the way Claude Code does—for this reason, only enter gateway-issued tokens, not raw cloud provider credentials.

#### Bedrock, Vertex AI, or Foundry direct

1. Open Excel, PowerPoint, or Word and launch the Claude add-in.
2. Authenticate using the method of your provider:
  1. **Bedrock or Vertex AI: **Sign in with your Microsoft work account. The add-in uses your Entra ID token to authenticate with your cloud provider—no separate cloud credentials are needed.
  2. **Foundry:** If your admin pre-filled the Azure resource name and API key, the add-in connects automatically. Otherwise, enter the values your IT team provided and select Connect.
3. The add-in reads the configuration your admin provisioned and connects to Bedrock or Vertex AI directly.

If you see an error at sign-in, confirm with your IT team that your account is in the group assigned to the add-in.

#### Change or update your connection

If your API token expires or your IT team gives you a new URL, go to "Settings" in the add-in sidebar, enter the new values, and select "Test connection."

---

## Gateway requirements for IT teams

The Office add-ins support the same three API formats as Claude Code. Set `gateway_api_format` in your add-in manifest to tell the add-in which format your gateway speaks.

#### CORS requirements

The add-in's taskpane loads from [`https://pivot.claude.ai`](https://pivot.claude.ai). Every request to your gateway is therefore cross-origin, and the browser will silently discard any response that lacks CORS headers.

Your gateway must return `Access-Control-Allow-Origin: [https://pivot.claude.ai](https://pivot.claude.ai)` (or `*`) on every response: GET, POST, OPTIONS, and all error responses. Setting it only on the OPTIONS preflight is not sufficient. For the preflight, return `Access-Control-Allow-Headers: *`.

#### Required endpoints

The endpoints your gateway must expose depend on which API format it speaks. Set `gateway_api_format` in your manifest to match.

**gateway_api_format: anthropic (default)**

**gateway_api_format: bedrock**

Native Bedrock InvokeModel pass-through. `gateway_url` must point at the pass-through prefix (for example, [`https://litellm.example.com/bedrock`](https://litellm.example.com/bedrock)).

**gateway_api_format: vertex**

Native Vertex pass-through. `gateway_url` must include the API-version segment (for example, [`https://litellm.example.com/vertex_ai/v1`](https://litellm.example.com/vertex_ai/v1)). Also requires `gcp_project_id` and `gcp_region` so the add-in can build the path.

#### Required header

For `anthropic` and `vertex` formats, the gateway must forward the `anthropic-version` request header to the upstream provider.

For `bedrock` format, the SDK puts `anthropic_version` in the request body instead — the gateway must preserve it there.

Failure to forward the header or preserve the body field may result in reduced functionality or prevent the add-in from working.

#### Authorization header

The add-in can send your gateway’s authorization token in either the `x-api-key` or the `Authorization` header.

#### Model discovery

On login, the add-in attempts to discover available Claude models via GET /v1/models. If your gateway doesn't expose a model list at that path, the add-in falls back to prompting the user for a model ID manually.

#### Differences from Claude Code gateway setup

---

## Example gateway configuration with LiteLLM

> **Warning:** LiteLLM PyPI versions 1.82.7 and 1.82.8 were compromised with credential-stealing malware. Do not install these versions. If you have already installed them:
>
> - Remove the package
> - Rotate all credentials on affected systems
> - Follow the remediation steps in **[BerriAI/litellm#24518](https://github.com/BerriAI/litellm/issues/24518)**
>
> LiteLLM is a third-party proxy service. Anthropic doesn’t endorse, maintain, or audit LiteLLM’s security or functionality. This guide is provided for informational purposes and may become outdated. Use at your own discretion.

Many organizations use **LiteLLM** as their gateway. Below is a minimal litellm_config.yaml for routing Office add-in requests to Anthropic, Bedrock, or Vertex.

#### Routing to Anthropic directly

**yaml**

```
model_list:<br>  - model_name: claude-sonnet-4-5-20250929<br>    litellm_params:<br>      model: claude-sonnet-4-5-20250929<br>      api_key: os.environ/ANTHROPIC_API_KEY<br><br>litellm_settings:<br>  drop_params: true
```

#### Routing to Amazon Bedrock

**yaml**

```
model_list:<br>  - model_name: claude-sonnet-4-5-20250929<br>    litellm_params:<br>      model: bedrock/anthropic.claude-sonnet-4-5-20250929-v1:0<br>      aws_region_name: us-east-1<br><br>litellm_settings:<br>  drop_params: true
```

#### Routing to Google Cloud Vertex AI

**yaml**

```
model_list:<br>  - model_name: claude-sonnet-4-5-20250929<br>    litellm_params:<br>      model: vertex_ai/claude-sonnet-4-5-20250929<br>      vertex_project: your-gcp-project-id<br>      vertex_location: us-east5<br><br>litellm_settings:<br>  drop_params: true
```

#### Routing to Azure

**yaml**

```
model_list:<br>  - model_name: claude-sonnet-4-5-20250929<br>    litellm_params:<br>      model: azure_ai/claude-sonnet-4-5-20250929<br>      api_base: https://your-resource.services.ai.azure.com/anthropic<br>      api_key: os.environ/AZURE_API_KEY<br>      extra_headers:<br>        x-api-key: os.environ/AZURE_API_KEY<br><br>litellm_settings:<br>  drop_params: true
```

For detailed setup instructions, refer to **[LiteLLM's Anthropic format documentation](https://docs.litellm.ai/)**.

---

## What Anthropic collects

Even when inference goes through your own infrastructure, the add-in communicates with pivot.claude.ai to load its interface and with claude.ai/api/ to evaluate feature flags. These connections transmit operational telemetry—such as which features are used, performance timings, and error rates—so Anthropic can maintain and improve the add-in experience. They don't transmit your prompts or Claude's responses.

Anthropic collects information in accordance with AWS Bedrock, Google Cloud Vertex AI, or Microsoft Azure's terms, consistent with Anthropic's arrangements with customers. Anthropic doesn't have access to a customer's AWS, Google, or Microsoft instance, including prompts or outputs it contains. Anthropic doesn't train generative models with such content or use it for other purposes. Anthropic can access metadata—such as tool use, token counts, and similar items—and use such metadata for analytic and product improvement purposes.

For details on what your organization's gateway or cloud provider logs, contact your IT team.

To route a full audit trail—including prompts, tool inputs, tool outputs, and document references—to your own infrastructure, see **[Configure a custom OpenTelemetry collector for Office agents](https://support.claude.com/en/articles/14447276-)**.

---

## How this differs from signing in with a Claude account

When you sign in with a Claude account, the add-ins connect directly to Anthropic. When you connect through a third-party platform, the add-ins send inference requests to your organization's infrastructure instead, and your IT team controls how that traffic is routed and logged.

Some features that rely on having a Claude account aren't available through third-party platforms yet, but we're working on adding support:

If your team needs these features, talk to your Claude admin about which sign-in path fits your organization.

#### Add MCP connectors to third-party add-ins

MCP connectors are now supported in Claude for Excel, PowerPoint, and Word. As an administrator, you can set the MCP gateway in the add-in manifest following the documentation here: **[MCP servers](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/manifest.md#mcp-servers)**. If you prefer to use the bootstrap endpoint, you can configure MCP connectors following the documentation here: **[`mcp_servers`](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/bootstrap.md#mcp_servers)**.

#### Add Skills to third-party add-ins

Skills are now supported in Claude for Excel, PowerPoint, and Word. The Anthropic financial services skills are available by default. Additional Skills may be added by administrators or manually by individuals.

Administrators can add skills using the bootstrap endpoint, following the documentation here: **[`skills`](https://github.com/anthropics/financial-services-plugins/blob/main/claude-in-office/commands/bootstrap.md#skills)**.

Individuals can manually upload local skills (either as a .zip, .skill, or SKILL.md file) and manage them individually. Skills are uploaded by selecting the "+" button, then Skills → "Upload Skills."

#### Add file uploads to third-party add-ins

File uploads are now supported in Claude for Excel, PowerPoint, and Word. Individuals can upload files by selecting the "+" button, then "Add files or photos" .

---

## Troubleshooting

#### "Connection refused" or network error

The gateway URL or cloud endpoint is unreachable from the user's network. Verify the URL is correct, the service is running, and there are no firewall or VPN restrictions blocking the connection. Check the **Network allowlist** section above to confirm all required domains are allowed.

#### 401 Unauthorized or "Invalid token"

The auth token is invalid or expired. For gateway connections, confirm the token with your IT team. For direct-cloud connections, verify the user's Entra ID account is in the assigned group and that the OIDC trust or OAuth client is configured correctly. For Foundry, regenerate the key in Azure Portal → Keys and Endpoint.

#### 403 Forbidden or "Access denied"

The token is valid but lacks the right permissions. For Bedrock, verify the IAM role has `bedrock:InvokeModel` permissions. For Vertex, verify the service account has `aiplatform.endpoints.predict` permissions. For gateways, check the token's scope with your IT admin. For Foundry, check the resource’s networking rules, or confirm the key belongs to the right resource.

#### 404 Not found

The add-in couldn't reach the expected API path. For gateways, verify the URL is the base URL (for example, [https://litellm-server:4000)—don't](https://litellm-server:4000)%E2%80%94don't) include /v1/messages in the URL field.

#### 500 or other server errors

The gateway or cloud provider encountered an internal error. Check your gateway logs (for example, docker logs litellm if using LiteLLM) for upstream provider errors. Try the request again, and contact your IT admin if the issue persists.

#### "No models available"

The add-in couldn't find Claude models. For gateways, your gateway may not expose a model list at GET /v1/models. Your IT team can either configure the gateway to serve a model list or give you a specific model ID to enter manually. For Bedrock or Vertex, confirm that at least one Claude model (Claude Sonnet 4.5 or later) is enabled in your account and region. For Foundry, confirm at least one Claude model is deployed in the resource (Model catalog).

#### Streaming responses fail or hang

Verify that your gateway supports Server-Sent Events (SSE) pass-through. Some proxy configurations strip or buffer SSE connections, which prevents streaming responses from reaching the add-in.

#### A feature I expected isn't available

Connectors, skills, file uploads, and Working Across Apps aren't available through third-party platforms yet. If you need these, ask your admin about signing in with a Claude account instead.

## Related Articles
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Use Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-for-excel)
- [Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)
- [Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
