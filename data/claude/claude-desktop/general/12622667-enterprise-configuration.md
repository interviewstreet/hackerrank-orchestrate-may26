---
title: "Enterprise configuration"
title_slug: "enterprise-configuration"
source_url: "https://support.claude.com/en/articles/12622667-enterprise-configuration"
last_updated_iso: "2026-04-17T19:59:26Z"
article_id: "14163405"
breadcrumbs:
  - "Claude Desktop"
  - "General"
---

# Enterprise configuration

_Last updated: 2026-04-17T19:59:26Z_

Administrators on Team or Enterprise plans can control Claude Desktop through system policies.

> **Note:** Enterprise policy controls at the user-machine level will override the in-app **[allowlist](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)**. If you want to use the allowlist, ensure `isDesktopExtensionEnabled` and `isDesktopExtensionDirectoryEnabled` are not set to "false" so the allowlist can populate the available registry.

---

## macOS Enterprise Configuration

Deploy configuration settings through your MDM solution using configuration profiles. Claude Desktop reads preferences from the domain `com.anthropic.claudefordesktop`. Use your MDM tool (Jamf Pro, Kandji, Microsoft Intune) to deploy configuration profiles to target machines or user groups. Configuration profiles allow you to manage Claude Desktop settings centrally without user intervention.

**Configuration profile tools:**

- Built-in MDM profile editors (Jamf Pro, Kandji, Intune)
- **[ProfileCreator](https://github.com/profileCreator/ProfileCreator/)** - Profile management
- **[iMazing Profile Editor](https://imazing.com/profile-editor)** - Configuration profiles

---

## Windows Enterprise Configuration

Deploy configuration settings through your enterprise management solution using **[Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)** or Intune policies. Settings can be configured at machine-wide (HKLM) or per-user (HKCU) level. Machine-level settings take priority over user-level settings when both are configured.

```
```powershell<br># Set machine-wide settings (recommended)<br>New-Item -Path "HKLM:\SOFTWARE\Policies\Claude" -Force<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "disableAutoUpdates" -Value 0 -Type DWord<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "autoUpdaterEnforcementHours" -Value 72 -Type DWord<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionEnabled" -Value 1 -Type DWord<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isDesktopExtensionDirectoryEnabled" -Value 1 -Type DWord<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isLocalDevMcpEnabled" -Value 1 -Type DWord<br>Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Claude" -Name "isClaudeCodeForDesktopEnabled" -Value 1 -Type DWord<br>```
```

---

## Enterprise Policy Options

## Related Articles
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Use enterprise search](https://support.claude.com/en/articles/12489464-use-enterprise-search)
- [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
- [Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
