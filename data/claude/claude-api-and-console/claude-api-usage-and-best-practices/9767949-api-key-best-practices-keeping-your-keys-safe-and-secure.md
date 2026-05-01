---
title: "API Key Best Practices: Keeping Your Keys Safe and Secure"
title_slug: "api-key-best-practices-keeping-your-keys-safe-and-secure"
source_url: "https://support.claude.com/en/articles/9767949-api-key-best-practices-keeping-your-keys-safe-and-secure"
last_updated_iso: "2026-03-16T21:10:26Z"
article_id: "10134625"
breadcrumbs:
  - "Claude API and Console"
  - "Claude API Usage and Best Practices"
---

# API Key Best Practices: Keeping Your Keys Safe and Secure

_Last updated: 2026-03-16T21:10:26Z_

API keys enable access to the Claude API, but they can pose significant security risks if not handled properly. Your API key is a digital key to your account. Much like a credit card number, if someone obtains and uses your API key, they incur charges on your behalf. This article outlines best practices for managing API keys to ensure they remain secure and prevent unauthorized access and charges to your Claude Console account.

## **Common Risks and Vulnerabilities**

One of the most frequent causes of API key leaks is accidental exposure in public code repositories or third-party tools. Developers often inadvertently commit plaintext API keys to public GitHub repositories or input them into third party tools, which can lead to unauthorized access and potential abuse of the associated accounts.

## Best Practices for API Key Security

#### 1. *Never *share your API key

- **Keep it confidential**: Just as you wouldn't share your personal password, don't share your API key. If someone needs access to the Claude API, they should obtain their own key.
- **Don’t share your key in public forums**: Don't include your API key in public discussions, emails, or support tickets, even between you and Anthropic.
- **Exercise caution with third-party tools**: Consider that when you upload your API key to third-party tools or platforms (such as an web-based IDE, Cloud Provider, or CI/CD platform), you are giving the developer of that tool access to your Claude Console account. If you don’t trust their reputation, don’t trust them with your API key.
  - When using a third-party provider, always add your API key as an encrypted secret. Never include it directly in your code or configuration files.

#### 2. Monitor Usage and Logs Closely

We recommend regularly reviewing [logs](https://console.anthropic.com/settings/logs) and [usage](https://console.anthropic.com/settings/usage) patterns for your API keys within the Console.

- **For Custom Rate Limit API orgs**: Implement usage and spend limits in your account settings.
  - These limits act as a safeguard against unexpected usage due to leaked keys or errant scripts.
- **For Standard Rate Limit API orgs**: Enable and configure auto-reload settings in your account.
  - This feature allows you to set a threshold at which your account will automatically charge the card on file to replenish usage credits.
    - Carefully consider auto-reload limits. While they ensure continuous service, they also act as a safeguard against unexpected high usage that could result from leaked keys or mistakes in your code.

#### 3. Securely Handling API Keys with environment Variables and Secrets

A best practice for safely handling API keys is to use environment variables to securely inject and share environment variables. When you deploy your application to a cloud environment, you can use their secret management solution to securely pass the API key to your application via an environment variable without inadvertently sharing your API key.

If you are storing secrets locally using dotenv, you must add your `.env` files to your source control ignore file (e.g., `.gitignore` for git) to prevent inadvertently distributing sensitive information publicly. In cloud environments, prefer encypted secret storage instead of dotenv files.

**Python example:**

1. Create a `.env` file in your project directory.

2. Add your API key to the `.env` file:

```
ANTHROPIC_API_KEY=your-api-key-here
```

3. Install the `python-dotenv` package:

```
pip install python-dotenv
```

4. Load the API key in your Python script:

```
from dotenv import load_dotenv<br><br>import os<br><br>load_dotenv()<br>my_api_key = os.getenv("ANTHROPIC_API_KEY")
```

5. If you are deploying your application to a cloud hosting environment, refer to your cloud provider’s documentation on how to add your Claude API Key and share it with your application ([AWS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [GCP](https://cloud.google.com/security/products/secret-manager?hl=en#how-it-works), [Azure](https://learn.microsoft.com/en-us/azure/key-vault/general/overview), [Vercel](https://vercel.com/docs/cli/secrets), [Heroku](https://devcenter.heroku.com/articles/config-vars)). Some providers offer multiple ways to securely inject environment variables into your app.

#### 4. Rotate API Keys Regularly

Regularly rotate your API keys on a consistent schedule (for example, every 90 days) by creating new ones and deactivating old ones. This routine helps minimize potential risks if a key is ever compromised.

#### 5. Use separate keys for different purposes

If possible, use different API keys for development, testing, and production environments. This way, you can correlate your usage to different internal use cases. If your API Key is compromised, this allows you to quickly disable just that use case and  limit any potential damage.

#### 6. Scan Repositories for Secrets

Regularly check your source control repositories for accidentally committed secrets.

- [Enable secret scanning directly in your source control provider](https://docs.github.com/en/code-security/secret-scanning/enabling-secret-scanning-features/enabling-secret-scanning-for-your-repository) if available.
- Use SAST tools like Gitleaks ([https://github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)) to scan your repositories for accidentally committed secrets.
- Integrate secret scanning into your CI/CD pipeline to catch any secrets before they are pushed to the main branch..

By incorporating regular secret scanning into your development workflow, you can catch and prevent the accidental exposure of API keys and other sensitive information in your code repositories.

#### 7. Use a Secure Key Management System (KMS)

As organizations scale and the number of API keys and other secrets increases, managing these sensitive credentials securely becomes more challenging. This is where Key Management Systems (KMS) come into play. A KMS provides a centralized solution for storing, accessing, and managing secret keys, including API keys.

## Benefits of using a KMS

1. **Centralized Security**: Store all your secrets in one secure, encrypted location.
2. **Access Control**: Implement fine-grained access controls to determine who can view or use specific keys.
3. **Audit Trails**: Track all access and changes to your secrets for compliance and security purposes.
4. **Key Rotation**: Easily rotate keys on a regular basis to enhance security.
5. **Integration**: Many KMS solutions integrate with popular cloud platforms and development tools.

## Anthropic's Partnership with GitHub for API Key Protection

Anthropic has partnered directly with GitHub to provide an extra layer of protection for our users through GitHub's Secret scanning partner program. This partnership offers proactive security measures to prevent the misuse of accidentally exposed API keys:

- GitHub actively scans public repositories for exposed Claude API keys.
- If a Claude API key is detected in a public GitHub repository, GitHub immediately notifies Anthropic.
- To prevent potential abuse, Anthropic automatically deactivates the exposed API key.
- The affected user receives a detailed email notification from Anthropic about the incident.

## What should I do if I suspect my API key has been compromised?

If you suspect that your API key may be compromised, we recommend revoking the key immediately. You can do so by logging into your Claude Console account, going to the [API keys page](https://platform.claude.com/settings/keys) from your profile, clicking the meatball menu (i.e. the three horizontal dots) next to the key in question, and selecting ‘Delete API Key.’

Refer to this article for more information: [What should I do if I suspect my API key has been compromised?](https://support.claude.com/en/articles/8384961-what-should-i-do-if-i-suspect-my-api-key-has-been-compromised)

API key security is an ongoing process that requires vigilance and regular review of your security measure. By following these best practices, you can significantly reduce the risk of API key leaks and unauthorized access.

## Related Articles
- [Managing API key environment variables in Claude Code](https://support.claude.com/en/articles/12304248-managing-api-key-environment-variables-in-claude-code)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Public Sector FAQs](https://support.claude.com/en/articles/13756069-public-sector-faqs)
- [Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
- [Claude Security](https://support.claude.com/en/articles/14661296-claude-security)
