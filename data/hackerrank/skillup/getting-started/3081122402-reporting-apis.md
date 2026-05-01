---
title: "‭Reporting APIs Available endpoints Configuring reporting APIs‬ Error handling Best practices Rate limits"
title_slug: "reporting-apis-available-endpoints-configuring-reporting-apis-error-handling-best-practices-rate-limits"
source_url: "https://support.hackerrank.com/articles/3081122402-reporting-apis"
article_slug: "3081122402-reporting-apis"
last_updated_exact: "Oct 14, 2025, 9:05 PM"
last_updated_relative: "Last updated 6 months ago"
breadcrumbs:
  - "SkillUp"
  - "Getting Started"
---

# ‭Reporting APIs Available endpoints Configuring reporting APIs‬ Error handling Best practices Rate limits

_Last updated: Oct 14, 2025, 9:05 PM (Last updated 6 months ago)_

SkillUp’s Reporting APIs allow you to programmatically extract skill signals, badges, and certification data from your organization. These APIs enable you to integrate learning insights with HR systems, build customized reports, and connect learning outcomes to business impact.

**Note:** Only administrators can generate credentials to access these APIs.

# Available endpoints

|  |  |
|----|----|
| **Endpoint** | **Description** |
| Credentials API | Returns a list of all available badges and certifications in SkillUp. |
| Users API | Returns user data, including learning progress, badges, and certifications achieved. |

# Configuring reporting APIs‬

SkillUp APIs use the **OAuth 2.0 Client Credentials** flow for secure access. Only authorized systems can request and retrieve reporting information.

To configure reporting APIs:

## ‭Step 1: Generate OAuth Credentials‬

![ReportingAPIs (2).gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1760426646769-ReportingAPIs%25282%2529.gif?Expires=253370764800&Signature=avWPKb67QURKfzp-9Nd3HGyLRI9LsjwsKxojUbqSWczAMTa6SQ9xa1MZff3QdRXUd--A3fKLJCqmBCB1Y3a1fsaUM0WTjSgMC9NbONDRfBsmSLKxfg6WVOZtsL-5lnvt-N7IWaHSQ~uncnPmFRdswrMbJ8ou21TU58J4x-T~~zhNWKazWx8xv21NjYkEXfLVAUfppmSW3-IKsnk2IG3TMymLMVH-10-AuO2icwH0JuzXKzbhSqamF5KgEJSRqtpdhEVyGXOwgQUfR4Nx6FqOc8-KRnt1E1pQDPpvVTyUngYmh81nIbkWnXol-SdVucX3RtcYcAUwlTz-pB~1TZl7Hw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  ‭Log in to **SkillUp** using an administrator account.

2.  Click your profile icon in the upper-right corner and select **Settings**.

3.  Click **Register New Application**.

4.  Enter a name for your application.

5.  Click **Register Application**.

6.  Copy the **Client ID** and **Client Secret** to the clipboard or click **Download JSON** to save the credentials as a file.

    **Important Note:** The client secret is displayed only once during generation. You must store it securely before closing the dialog because you cannot retrieve it again.

Your application is now successfully registered, and you can start making API requests.

## ‭Step 2: Request Access Token‬

‭As a security measure, you must first obtain an access token by making a POST request to the` /v1/oauth2/token` endpoint.

The Authorization header must include your client credentials encoded in Base64 format.

1.  Combine your client ID and client secret using a colon (:).\
    Example: `client_id:client_secret`

2.  Encode the string using Base64.

3.  Add the prefix `Basic`to the encoded string to create the Authorization header.\
    Example: `Basic <base64_encoded_string>`.

**Note:** The access token (JWT) is valid for **10 minutes**. When it expires, repeat these steps to request a new token.

### Example

<span class="mr-auto truncate">Plain Text</span>

```
If client_id = "abc123" and client_secret = "def456"
Combined: “abc123:def456”

Base64 encoded:”YWJjMTIzOmRlZjQ1Ng==”

Final header:”Basic YWJjMTIzOmRlZjQ1Ng==”
```

**Request**

<span class="mr-auto truncate">Shell</span>

```
curl -X POST https://www.hackerrank.com/skillup/api/v1/oauth2/token \
-H "Authorization: Basic <base64_encoded_credentials>" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "grant_type=client_credentials"
```

**Headers**

|               |              |                                      |
|---------------|--------------|--------------------------------------|
| **Header**    | **Required** | **Value**                            |
| Authorization | Yes          | Basic `<base64_encoded_credentials>` |
| Content-Type  | Yes          | application/x-www-form-urlencoded    |

**Body parameters**

|               |              |                    |
|---------------|--------------|--------------------|
| **Parameter** | **Required** | **Value**          |
| grant_type    | Yes          | client_credentials |

**Response**

<span class="mr-auto truncate">JSON</span>

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "expires_in": 600
}
```

|              |          |                                                |
|--------------|----------|------------------------------------------------|
| **Field**    | **Type** | **Description**                                |
| access_token | string   | The access token for API authentication        |
| expires_in   | integer  | Token validity period in seconds (600 seconds) |

## ‭Step 3: Access SkillUp APIs‬

‭After you obtain a valid access token, use it to call the SkillUp Reporting APIs.

Include the token in the Authorization header of your request.

### Example Request

<span class="mr-auto truncate">Shell</span>

```
curl -X GET https://www.hackerrank.com/skillup/api/v2/credentials \
-H "Authorization: Bearer <access_token>"
```

# Error handling

|                 |                   |                                        |
|-----------------|-------------------|----------------------------------------|
| **Status Code** | **Error**         | **Description**                        |
| 400             | Bad Request       | Missing or invalid parameters          |
| 401             | Unauthorized      | Access token is invalid or expired     |
| 403             | Forbidden         | Token lacks required permissions       |
| 429             | Too Many Requests | Too many requests made in a short time |

# Best practices

- Store credentials securely. Never expose client credentials in client-side code.

- Tokens remain valid for 10 minutes. Cache and reuse access tokens instead of generating new ones for every request

- Request a new token before the current one expires.

# Rate limits

|                  |                      |
|------------------|----------------------|
| **Request Type** | **Limit**            |
| Token requests   | 1 request per second |
| API requests     | 1 request per second |

For more information, contact [skillup-support@hackerrank.com](mailto:skillup-support@hackerrank.com).‭
