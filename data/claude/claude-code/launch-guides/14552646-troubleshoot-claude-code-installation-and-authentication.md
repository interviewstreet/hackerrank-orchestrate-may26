---
title: "Troubleshoot Claude Code installation and authentication"
title_slug: "troubleshoot-claude-code-installation-and-authentication"
source_url: "https://support.claude.com/en/articles/14552646-troubleshoot-claude-code-installation-and-authentication"
last_updated_iso: "2026-04-15T01:16:35Z"
article_id: "17023830"
breadcrumbs:
  - "Claude Code"
  - "Launch guides"
---

# Troubleshoot Claude Code installation and authentication

_Last updated: 2026-04-15T01:16:35Z_

These ten issues account for the large majority of installation and authentication support tickets related to Claude Code. Each entry includes the most reliable fix.

## 1. **claude: command not found** right after installing.

The installer added `claude` to your PATH, but your current shell has not picked it up yet. Open a new terminal, or run `source ~/.zshrc` (or `~/.bashrc`). On Windows, close and reopen PowerShell.

## 2. npm install fails with `EACCES` / permission denied.

This usually means the install was run with `sudo`, or your global npm directory is root-owned. Do not use sudo. Instead, use the native installer (`curl -fsSL [https://claude.ai/install.sh](https://claude.ai/install.sh) | bash`), or fix npm's prefix with `npm config set prefix ~/.npm-global` and add that `bin` directory to your PATH.

## 3. "Node version not supported" or silent crash on launch.

Claude Code requires **Node 18 or later**. Check your version with `node -v`. If it is older, install a current version via `nvm install --lts`, or use the native installer, which bundles its own runtime and avoids this issue entirely.

## 4. WSL: **claude** runs the Windows Node instead of Linux Node.

Windows PATH leaks into WSL and overrides nvm. Prepend your Linux node to PATH in `~/.bashrc`: `export PATH="$HOME/.nvm/versions/node/$(nvm current)/bin:$PATH"`

## 5. Installer hangs or fails behind a corporate network.

The download host (`storage.googleapis.com`) is likely blocked. Set your proxy first with `export HTTPS_PROXY=[http://proxy.example.com:port](http://proxy.example.com:port)`, then re-run the installer. If that is not possible, ask your IT team for the offline package.

## 6. **SELF_SIGNED_CERT_IN_CHAIN** or other TLS errors.

Your company injects its own certificate. Point Node at the corporate CA bundle: `export NODE_EXTRA_CA_CERTS=/path/to/company-ca.pem` Add it to your shell profile so it persists.

## 7. **/login** opens a browser but the terminal never finishes ("Waiting for authentication…").

This usually means the localhost callback is blocked, which is common over remote SSH, in devcontainers, or behind a strict firewall. Use the manual flow instead: copy the URL printed in the terminal, complete login in any browser, then paste the returned code back into the terminal.

## 8. "Not authenticated" even though you set `ANTHROPIC_API_KEY`.

There are three common causes: the key was exported in a different shell (run `echo` `$ANTHROPIC_API_KEY` to check), Claude Code has not yet been told to trust this key (it prompts once on first use; until you approve, `ANTHROPIC_API_KEY` takes precedence over any OAuth session only after that approval), or the key is a Console key but your organization requires SSO login instead.

## 9. Bedrock / Vertex: "Could not load credentials."

Claude Code uses the standard provider SDKs, so the fix is the same as for any AWS/GCP CLI tool. For Bedrock, confirm `aws sts get-caller-identity` works and `AWS_REGION` is set to a region where your model is enabled. For Vertex, confirm `gcloud auth application-default login` has been run and that `ANTHROPIC_VERTEX_PROJECT_ID` and `CLOUD_ML_REGION` are set.

## 10. It installed and authenticated, but every request errors with 403 / "model not available."

Your account exists but does not have access to the model Claude Code is requesting. For Enterprise seats, confirm that your seat is active in your organization's admin settings. On Bedrock or Vertex, confirm that the specific Claude model is enabled in that region or project. As a quick workaround, run `/model` and select a model you know you have access to.

## Still stuck?

Run `claude doctor` from your normal shell (not from inside a Claude session). It prints a diagnostic report you can attach to a support ticket. For the full list of known issues, see the **[troubleshooting guide](https://code.claude.com/docs/en/troubleshooting)**.

## Related Articles
- [Claude Code model configuration](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Your first day in Claude Code](https://support.claude.com/en/articles/14552382-your-first-day-in-claude-code)
- [Claude Code cheatsheet](https://support.claude.com/en/articles/14553413-claude-code-cheatsheet)
- [Claude Code user FAQ](https://support.claude.com/en/articles/14554922-claude-code-user-faq)
