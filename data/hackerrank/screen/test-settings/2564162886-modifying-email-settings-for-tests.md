---
title: "Configure Email Settings for Tests"
title_slug: "configure-email-settings-for-tests"
source_url: "https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests"
article_slug: "2564162886-modifying-email-settings-for-tests"
last_updated_exact: "Oct 15, 2025, 6:12 PM"
last_updated_relative: "Last updated 6 months ago"
breadcrumbs:
  - "Screen"
  - "Test Settings"
---

# Configure Email Settings for Tests

_Last updated: Oct 15, 2025, 6:12 PM (Last updated 6 months ago)_

You can manage the emails sent before, during, and after a test. HackerRank lets you configure the following types of test emails:

- Test Reports Email

- Leakage Alert Emails

- Reminder Emails

- Invite Email

- Confirmation Email

## Prerequisites

You must have already created a test.

## Configuring email settings

To configure email settings:

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Tests** tab.

3.  Open the test you want to configure.

4.  Go to **Settings \> Emails.**

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759742909047-image.png?Expires=253370764800&Signature=Tk--K6Q3O8j7nEhyYKrHEf0QRWl3TInrjANEzctyiEoaC7-1vSkMyY75FiBondcaVeZFDiQ49Z1OJ4W-M~oUm5cQjMLogaanHkz5drCU0tikRPuZK5apzu218vCePeYVXXnOUARbLcSdf5hd2f9gd5o5B~81YYzRAstKmsc4nGn00Y0VtJ~f3wbQDllurohXyuJJUMBKggSEvpY0NzysxwTRWPEG6CeGGJonZeVgePcO-2vFnGDcmCxckLbtf9lusQ90emqRj23k-xDgQqB1cgZDn87xfsXKVewCJvCFAVFQbD4TEMLf5UhK~1MQJcGwTVO3QDiCGkfIYxp~G0vvFw__&Key-Pair-Id=K3NV4LZ47N8M46)

    In the **Emails** section, you can:

    - [Configure Test Reports Email](https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests#configure-test-reports-emails-7)

    - [Configure Leakage Alert Emails](https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests#configure-leakage-alert-emails-14)

    - [Configure Reminder Emails](https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests#configure-reminder-emails-20)

    - [Configure Invite Email](https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests#configure-invite-email-24)

    - [Configure Confirmation Email](https://support.hackerrank.com/articles/2564162886-modifying-email-settings-for-tests#configure-confirmation-emails-29)

5.  Click **Save** **Changes** to apply your changes.

**Note:** When multiple levels of email templates exist, the system applies them in the following order of priority.

1.  If the email template in **Centralized Test Settings** is locked, it takes the highest priority. This configuration overrides all other template settings.

2.  If the **Centralized Test Settings** are unlocked but include a default message:

    1.  The test-level template takes precedence, even if a user has set a personal default template.

    2.  If no test-level template is defined, the system uses the user’s default email template.

3.  If no **Centralized Test Settings** are locked, and neither test-level nor user-level templates are defined, the system uses the default language template from the **Centralized Test Settings**.

### Configure Test Reports Emails

You can add team members to receive candidate test reports in addition to the test owner.

By default, the recruiter who invites a candidate receives the test report. If a candidate takes the test through a public link, the system treats the test owner as the inviting recruiter.

To add additional recipients:

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759740196746-image.png?Expires=253370764800&Signature=bBnJStcH7CBJFW2my5synNPqx0hdxMqWcDE9L46A79AElfHLs0dYE2iMxR81D2ihBYL9-s1V6M~PCOrA6Xgo3yostGGOvKEb2gTsxk9UnAudD9zpyp50ds~~XPN-tXyFBRCoKfzYyUPFQJQ2nm0h92IPDV~2g1sTzsShcEo4l~EGMRfK763W-uCsGgzOSV5mArRV3GZhby9X4huX9x6VTulTDF16LleVgrxLCVd-f-bxaAR4k6HKAvFhFp6DrElKpuqBLUnpmLL-WRnFWE3JNbfxksWhuXNiHHGH7G28dSWTsSd-NTIJIAsBoYmsrku5I3XiMy9AYbVqzr8E7j~KrQ__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  In the **Test Reports Email** section, enter the email address in the input field 

2.  Click **+ Add**.

**Note:** All added recipients receive reports for every candidate attempt, regardless of who invited the candidate.

### Configure Leakage Alert Emails

You can add users to receive notifications when HackerRank detects a leaked test question.

To enable leakage alerts for specific team members:

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759740500199-image.png?Expires=253370764800&Signature=r-hUOFQI-w8SIo~zyuBEVdRiQWYKSeZ9ihqLUl-OsB2IPvibugJDkJZkeS4-qufLYoirDmTwxb6SPVtiM-IJw6jmWeu9cqChbvIsVXdz4ECJxilFnZMGifsKxjz5Cs29pm2rM5xkPWqHHyfO6aChCB3B0LtYdo4EvoroG0H~tG0JE6ecGqXlAKSGYbl8QzLI-Y58Mtrm5jaWfijzNkkTlA-EDUWioF94NIfDSEuXJmlh5Ozmes2mnoIHEnOuOvfHhk0~U-jQulR4eMvBJExjHYn7G15A6f5ecvS2wcfzG9gHgl-S2bKIkdnk8ywfmK1aeNsxg9hWGDXUcD-pcGjH~Q__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  In the **Leakage Alert Emails** section, select the **Enable** drop-down menu.

2.  Select the checkbox to add users from the list or use the search bar to filter by name or email.

**Note: **

- By default, only users with edit access to the test can receive leakage alerts.

- HackerRank automatically sends an email notification to these users when a potential content leak is detected.

### Configure Reminder Emails

Send reminder emails to candidates who have not attempted the test. By default, reminder emails are disabled, and each candidate receives only one reminder.

To enable and customize reminder emails:

1.  Turn on the **Reminder Emails** toggle.

2.  Select one of the following options:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759740620117-image.png?Expires=253370764800&Signature=hFTZH0LwzO7CvE5xHn9OTnqHv3RhOl12MBaUwSjGrMtB6yaEiekWcFqMG0ZzxD1duAFkif2YFX6NhKIk--oKvH7-fBQkepfz-Cdpd1gM8YB3bWYuOpThmxCiKoogRf-U3EjXiOrSGcKMYcF9AZu733NS~7SiZ0koZ7REI8p-8~Vdx1uNKRkBA1PE6so9Ip5Gsh~~lDUfagsKWujKuEnDGHb7UEU78V-DZgsluiFJt4yZI21g3vdP~~Tel~9N3Zflsl5ICgF6f68IJbv9zXDxh5waakDvxBd7hczdUFzfi~3lfcxFCZ-Ddk~IZtwb-U6Z2onQemwqPcF1QpEOBBCX1w__&Key-Pair-Id=K3NV4LZ47N8M46)

    - If the test has an expiration date, select how many days before the expiration date to send the reminder.

    - If the test has no expiration date, select how many days after the invite to send the reminder.

3.  Customize the message in the **Reminder Email Contents** section\
    Or\
    Click **Use Default Message** to apply the default content instead.

### Configure Invite Email

You can configure a custom invite email template at the test level. This option allows you to tailor the invitation message to match the context of each test, ensuring candidates always receive accurate and relevant information.

To enable and customize the invite email at the test level:

![EnhancedInviteswithTemplates.gif](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F377a3ecf-0c0e-4676-9b27-d7ba98e58f29-1759736569691-EnhancedInviteswithTemplates.gif-304b229f-f726-4e42-9811-2fbd162b3a1c?Expires=253370764800&Signature=HJyLurRw5lp0Z2EXxgoWMIxvGg4BN1IjubmQVDPac8zs60ulkv41g6QhIIBXr3rhOSRIoSI6bpmby82t4V0b7roljlt5xdnT-uGoZsgUBTtzqClZqGVZZU1eAjSe~wiPWcvj1eEA5ED2qOJ1RgKvP8z-iGWcYP37gufSFTj~1K7pH~clXsfInH-Z3-luQMfoif3eMRJG6R5orW3r9ykQa7p9k1KJadi1wPJ6GKEYym14M2bBx-UG9Xe43j-1mZyyWLCwjd8p2-h-VDZJZDdk1ddi1iU0b2Ib5S1~0gukwUkU9TLaGEolZSZdF70-DQ~Z2USffnjSqoCi~TXAlZDjfw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Turn on the **Invite Email** toggle.

2.  Edit the **Invite Email Subject** and **Invite Email Content** text boxes as needed.

Note:

- When Centralized Test Settings lock the invite message, that message takes priority.

- When centralized settings are unlocked, the system applies the test-level template.

- When no test-level template exists, the system applies the user-level template.

- When no templates exist, the system uses the default message in the centralized settings.

### Configure Confirmation Emails

Send confirmation emails to candidates after they complete a test. By default, this setting is enabled.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1759740745664-image.png?Expires=253370764800&Signature=iEEAvGWrDXMlxG-Krj0do9wNyvt4Xp02hdboLsav0fvPRz3Wc5KvWSv7bGRQ6yg5hf55xddumBwEYmMrEhEunLTg3MoQ3LYN7peiZ5UePY7a9rG7pbaSv866W8HRpciktMEceUJ-PFf5FK1UFv-hPbbqdZB6d4rj3SbAdPENyAPDJL4BuxLt1YBAJBA1tFbgOXvuRxktEozxDzvtnJLhy2UYL8sXAqEvcVcaJpGSRFqXn6YtZLiPKA9mGfxO3EW~L8P1mNPxJMUmA2OVI~3RzlxALqhMipL0f7v2diLY7DXpSSZFxdhO9IKJPSjrScq53Zi-Iwa-j49M~WjtGntxJQ__&Key-Pair-Id=K3NV4LZ47N8M46)

To enable and customize confirmation emails:

1.  Turn on the **Confirmation Email** toggle.

2.  Edit the confirmation email content in the text box to include next steps or additional links.\
    \

\
