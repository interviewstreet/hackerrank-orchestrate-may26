---
title: "Deploy Claude Desktop for Windows"
title_slug: "deploy-claude-desktop-for-windows"
source_url: "https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows"
last_updated_iso: "2026-03-25T20:23:28Z"
article_id: "14163463"
breadcrumbs:
  - "Claude Desktop"
  - "General"
---

# Deploy Claude Desktop for Windows

_Last updated: 2026-03-25T20:23:28Z_

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically across their organization to manage installations and updates centrally. We offer MSIX packages for Windows deployments via Microsoft Intune, SCCM, Group Policy, or PowerShell, enabling secure, scalable distribution.

## Installation requirements

- For individual installations with full feature support including Cowork, administrator privileges are required. Users will see a Windows UAC prompt during installation. Users without admin access can still install Claude, but Cowork will not be available. Access the user-friendly installer from **[our download page](https://claude.com/download)**.
- For silent deployment without user interaction, use the MSIX package directly with your enterprise management tool.

## Cowork requirements

Claude Desktop for Windows requires the **[Virtual Machine Platform](https://support.microsoft.com/en-us/windows/enable-virtualization-on-windows-c5578302-6e43-4b4b-a449-8ced115f58e1)** to use Cowork. You can automate installation of this feature via most endpoint management solutions, but you may also run the following command to install it manually:

```
Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform -All -NoRestart
```

## Download

- **[Claude MSIX (x64)](https://claude.ai/api/desktop/win32/x64/msix/latest/redirect)**
- **[Claude MSIX (arm64)](https://claude.ai/api/desktop/win32/arm64/msix/latest/redirect)**

## Installation commands

For manual installation on individual machines, use the following PowerShell commands:

#### Install for single user

```
```powershell<br>Add-AppxPackage -Path "Claude.msix"<br>```
```

For more details, see Microsoft's **[Add-AppxPackage](https://learn.microsoft.com/en-us/powershell/module/appx/add-appxpackage?view=windowsserver2022-ps)** documentation.

#### Install for all users (provisions machine-wide)

```
```powershell<br>Add-AppxProvisionedPackage -Online -PackagePath "Claude.msix" -SkipLicense -Regions "all"<br>```
```

For more details, see Microsoft's **[Add-AppxProvisionedPackage](https://learn.microsoft.com/en-us/powershell/module/dism/add-appxprovisionedpackage?view=windowsserver2022-ps)** documentation.

## Deploy via MDM

Claude Desktop can be deployed through various enterprise software distribution services. Choose the method that aligns with your organization's existing infrastructure:

- **[Microsoft Intune](https://docs.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-intune)**
- **[Microsoft Endpoint Configuration Manager (SCCM)](https://learn.microsoft.com/en-us/windows/msix/desktop/managing-your-msix-deployment-mem-adminconsole)**
- **[Group Policy Software Installation](https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/use-group-policy-to-install-software)**
- **[Deployment Image Servicing and Management (DISM.exe)](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/preinstall-apps-using-dism?view=windows-10)**
- **[PowerShell Scripts](https://learn.microsoft.com/en-us/windows/msix/desktop/powershell-msix-cmdlets)**

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see **[Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)**.

## Troubleshooting

#### MSIX package not working with AppLocker?

By default, packaged apps may be restricted by AppLocker policies. Ensure your AppLocker rules allow MSIX packages, or add Claude Desktop to your allowed applications list. Consult your organization's security policies before making changes.

## Related Articles
- [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
