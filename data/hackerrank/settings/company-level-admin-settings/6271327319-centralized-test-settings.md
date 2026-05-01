---
title: "Centralized Test Settings"
title_slug: "centralized-test-settings"
source_url: "https://support.hackerrank.com/articles/6271327319-centralized-test-settings"
article_slug: "6271327319-centralized-test-settings"
last_updated_exact: "Dec 26, 2024, 12:34 PM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Settings"
  - "Company Level Admin Settings"
---

# Centralized Test Settings

_Last updated: Dec 26, 2024, 12:34 PM (Last updated 1 year ago)_

The **Centralized Test Settings** page enables Company Admins to configure default test settings for the entire organization. By standardizing test rules and experiences upfront, you can save time and ensure consistency across all tests.

**Tip**: For more details, refer to [Test Settings and Configuration](https://hackerrank-knowledge-base.help.usepylon.com/articles/6629491991-test-settings-and-configuration).

### Prerequisites

- **Company Admin** license

### Accessing Centralized Test Settings

1.  Click your **profile icon** and select **Settings** from the dropdown menu.

2.  In the left-hand menu, navigate to **Test Settings**.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735196396454-image.png?Expires=253370764800&Signature=ijA5M50n9MseNXTp8VsMn6wAJ2Gvmi14IPSQOYrjd~AXW3Sdz3EOqG5k0xDtVfMtKxieXxLXghrQa3MBGPHKAMtHC4C40cmaICwf-1E4mkMg0n6fEghC-ec2IBDkG5YnLfUVlvnNbx72MelicLD1PcJtR8fIAVmjEvF4a1ozKRRkqvxTxtYU~7DhGWDvbBpW0vexuaVOWOIFHkN8gSVzaVHpE0~CtjWEPa8SouODUDv41Q0kLOQ9rYP~FJWTyMJPdV~H4rNkQQpBuKtXSjgJpcpuIMl43PBVVKp4GAEIbL3bI8EPAnN3iz1C4RGWH2gVqKx10dmdb6gkApGsOl7VhQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### Applying Centralized Settings

As a Company Admin, you can manage test settings in two ways:

#### 1. Change Default Settings

- Toggle switches to enable or disable default settings for newly created tests.

- Users can still override these defaults at the individual test level.

#### 2. Lock Default Settings

- Use the **lock icon** to enforce specific settings across all tests.

- Other users cannot modify locked settings, which will apply to every test in your organization.

**Note**:

**1. Unlocked defaults** apply only to new tests and do not retroactively affect existing ones.

**2. Locked defaults** override all test settings, ensuring organization-wide consistency.

### Configuring Test Settings

#### Test Email Settings

Manage the default settings for email communication with candidates during the screening process:

- **Confirmation Email**: Customize content and subject.

- **Invite Email**: Define content and expiry.

- **Reminder Emails**: Set conditions for reminders with or without expiration dates.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735196490692-image.png?Expires=253370764800&Signature=h-z-UaiAmd04dNElFu6AijBsQx-Q7xQipLa2C0f48R~TeoUqAaIqAezgaMBek8MufyRnJLENZ3P7NZUQnKOvvDu9YJ51OvZy9PjSKsY04dZiAYJC9h8wApuv-bOHmNjxtx1ZJ7k3~aGbnBArbUkGjxCdxoAJ64Xf~BWxq1O2waUWaIbkQ4JgmTpgpt0SykJ9bqebuGiQJA2JHxTEKWdVXUmpvliHsl2iSdQ07xmP6EXcOC~ssLkyiDAXIC3IFQivUV1XrK3murTYBsO1afqdwF6z8ETZLQwhMRsyzZPI9nIJg479gVjIJAGXMkQFjbU4K1KTrZ9niOa68BLgdoPGGQ__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** To enable the **Reminder Email** toggle, at least one valid value must be entered for "Reminder Email with Expiration" or "Reminder Email without Expiration.

- Refer to the table below for conditions:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1"><p>With Expiration</p></td>
<td data-colspan="1" data-rowspan="1"><p>Without Expiration</p></td>
<td data-colspan="1" data-rowspan="1"><p>Reminder Email Status</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Disabled</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Disabled</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Disabled</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Enabled</p></td>
</tr>
</tbody>
</table>

#### Test Homepage Settings

Customize the test homepage with standardized instructions, disclaimers, and mandatory fields. Before starting the test, you can add custom fields to the candidate's confirmation form.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735196552475-1735196514292-image.png-ba1f5e50-981e-4265-a132-37c4e9c13951?Expires=253370764800&Signature=XY0dEEgbK8zyu9yykdIIN1FZslLB-Dko4N7YsKrcvT2By6yJdgc9bMclhdUEmMWbU3dZphrVNyvGSBoYmemRhz1vkU5m6IDKxOBUXRkYuY8BVCxW~8vcsqmrMzX8kb4WORW2f4urFI4C84mVYUDPAKlju3EF5giqrdvo7VFdH78wC~pfNWuwm2Ruj1dE7H~msaWvadjd7Q3SRev9fQLR~5IuXnZa8oBcX4jdgsnjDEamO08~WMtqZq9dtUnT8hMJQKc7IlDF0spbdVyFGKI4TEwr-VNorI63d4lL9mndj8Gp8~~~sIFlnap29wR~R~pgYdnW6yzlTh5yLclbYFEdrA__&Key-Pair-Id=K3NV4LZ47N8M46)

#### Test Integrity Settings

Control proctoring settings for all tests, such as enabling **Image Proctoring** or **AI Plagiarism Detection**.

##### Dependencies and Interdependencies

- **AI Plagiarism Detection**: Requires **Copy Paste Tracking** and **Tab Proctoring** to be enabled.

  - If AI Plagiarism is enabled, a dialog box prompts you to enable the dependent settings.

- **Photo Identification vs. Image Proctoring**: These settings are mutually exclusive.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735196685957-image.png?Expires=253370764800&Signature=LYda660j-GUsopMnL0dETVnp3R7QWeaTt5YOQ0uar0pQvYkfljDs8cSFReHyhNLO1Z7rFMT~qNAlyfV1Ecc7TACIY23FDCy12urJ2T0aDSgZ02OAlZOYVvPOCX4rp4LUM362-0vEWX2jBiPDltWtbbHLJ2bdoSw~nc5ysylGHstBXXcwEuxKvSQyXHvwxC739QlSH1iTS4Ln3RhEAcBphFZPEdn78Id45IasZSyjlhFYnESOXNd9z20VnDTJPFTcMZJSpTKAV0rdX1phj2EU7Z15WIwfxudoCrvepvqpITjFZcj6MO4ZQ1U-cSxPqcGH9pVBYleiF0wbIKnYj1LwkA__&Key-Pair-Id=K3NV4LZ47N8M46)

- The table below outlines valid combinations:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1"><p><strong>Photo Identification</strong></p></td>
<td data-colspan="1" data-rowspan="1"><p><strong>Image Proctoring</strong></p></td>
<td data-colspan="1" data-rowspan="1"><p><strong>Validity</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Valid</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Valid</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="cross_mark" data-type="emoji" contenteditable="false">❌</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Valid</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><span data-name="check_mark_button" data-type="emoji" contenteditable="false">✅</span>
<br />
</td>
<td data-colspan="1" data-rowspan="1"><p>Invalid</p></td>
</tr>
</tbody>
</table>

#### Additional Settings

Control if individual users can configure test cutoff scores.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735196598426-image.png?Expires=253370764800&Signature=KjknIhkyQLVf2npHJ0Ms1rc9bp6yr5bBUR9J5eUPhJVUpMhXz6WascVAgx-S7-iu-~ngrOTfJoDGoE4c7czwtzhl8-oBwcpVzqDCN6f~MxthrQB9gSsGrE2MpRPFAwggAYEI6WVyIqhl4kBg-lulFtC1uzpPSvdfUagUI4732xHjoyUEKVKbVP-I4LrBaIsuo85pjXNjEP~Rnn2KU6BmUrYKk4eGbXQpAXb3apDZC9w6UbqMLL9emzZ4JrRhxARiZgBuuR6~CtSHnRkOCkGMed988vFcq38C3s0s6yJEZg59eFPUlE8h4rGOKsGJuK2zt7C~KgbcFg6rpnq~U~QQbw__&Key-Pair-Id=K3NV4LZ47N8M46)

### Saving Your Settings

After making changes, click **Save Changes** to apply the new default settings.

\
