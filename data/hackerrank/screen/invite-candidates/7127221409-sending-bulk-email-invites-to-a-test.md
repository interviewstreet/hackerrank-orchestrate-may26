---
title: "Send Bulk Email Invites Sending bulk email invites Troubleshooting bulk invite errors"
title_slug: "send-bulk-email-invites-sending-bulk-email-invites-troubleshooting-bulk-invite-errors"
source_url: "https://support.hackerrank.com/articles/7127221409-sending-bulk-email-invites-to-a-test"
article_slug: "7127221409-sending-bulk-email-invites-to-a-test"
last_updated_exact: "Sep 17, 2025, 12:25 PM"
last_updated_relative: "Last updated 7 months ago"
breadcrumbs:
  - "Screen"
  - "Invite Candidates"
---

# Send Bulk Email Invites Sending bulk email invites Troubleshooting bulk invite errors

_Last updated: Sep 17, 2025, 12:25 PM (Last updated 7 months ago)_

The Bulk Invite feature allows you to send test invitations to many candidates at once using a CSV file.

- **CSV file requirements:** Before you upload the CSV file, ensure that it meets the following requirements:

  - The file must be in `.csv` format.

  - The maximum file size is 2 MB.

  - The file can contain up to 35,000 rows.

<!-- -->

- **CSV content formats:** You can include only email addresses or both names and email addresses in your CSV file.

  - **Email addresses only:** List candidate email addresses in a single column.\
    For example, `evanbrown@gmail.com`, `nancysmith@gmail.com`.

  - **Names and email addresses:** You can include names with email addresses in one of the following ways:

    - **Inline format**: Enter names with email addresses in the format `Name<email>`.\
      For example, `Evan Brown<evanbrown@gmail.com>`, `Nancy Smith<nancysmith@gmail.com>`.

    - **Separate columns**: Enter names in one column and email addresses in another.

**Note:** If you include candidate names in the CSV file, you can personalize invitations by using the Candidate Name placeholder. The system automatically replaces the placeholder with the candidate’s name from your file.

# Sending bulk email invites

To send bulk email invites:

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to the **Tests** tab.

3.  Open the test from which you want to invite candidates.

4.  Click **Invite** in the upper-right corner.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401419672-image.png?Expires=253370764800&Signature=ut2iNsuFCoKeXplryhIzcwHLgurGNe3IqasibYvCAfwUo4pZCBuRZbP4EwWKSx4hYJjodNieW-yz4isDji1ynRa9NWO75j6Kj0ZMN~czb5WcM2bTSoPnWI2zQEYJU0dq1dbatjtNTobF-Qa7qhMOLWN7kK8tNqiSTJAH1R0BeGtnJOU3HuG62KCcT-xzs4yCGUfttp~Ebe~C14ajAmtojh9hK~UfzPFbaFsKwOEMnxndrze5qQrU8N3tQ~1slnR4FzDRuTf96UMfkxQQa0F2LODdv152e-HTqyJA~ttSoZo6nZHKFIFmE7nJ5CDK~hLvBYoqqnGEt1WonIki6vN7vg__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  In the **Send Test Invites** page, click the upload button next to the **To** field.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401446055-image.png?Expires=253370764800&Signature=CwkAaIZph8M~PO6obfREG3wBz20rNl7-h1BhWhI2sUuKwqDAfPeyOGhYmWCGhS2j27GLrCHzGreCAczMs-1ROY4soQuk~8oFOUaaMAMHC8F9Lk73m7dWu9L4O4V5eTnrI-V9iXN-8~fEuwALEYaBkkH3u1eoZkdDXnczjCh5o555WO-Wc2V-c9SwjnmyBKuxNPQTence9DkZRq1jNXMSV8XclPBfPCbJYXLhooxW8Vu0EsIaFxg1lRJaYNAADWA3tW488tbuBqPDW-KBN1HDOcf7M9bZofy~vA81SegW4d0SISYEqC3tV7v-rLx0EkpU1QTc0A92UleX2VCS66Oxow__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Upload CSV**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401464623-image.png?Expires=253370764800&Signature=le3nJY4iJ1GQepBJ5ieZ0VXlqA4hhl6sG3J4oY7t~yHMy4tixk4ltMpknH8Q0UEoX6y1OrW5L9bKyWv5lfCPGGSrjwqE3IInE5r6BaNc3u~zB6eWFUlCE3lrFw~bWantXz6kmcKK8q5EsC2Wumnp0KSwqT2~bpVkfRRIhnP2tf59FDSRPNlSMidZD024B2QAenXLdB0~zKf9elJ3c6TULqY~uHxUqhkyB5A8Lx7u7Q0wl8F07SK8wK2HKe73t2foUmS37rtLXWeNYaIPfkVWU3BEF0N~1hO5y40wSct4GNf5D-d47np5-wP51i45xqiRALQiGe5xApW43gj~r0rYIQ__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Select and upload the CSV file. The email addresses from the file appear in the **To** field.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401477670-image.png?Expires=253370764800&Signature=E~Jdg1Xu1Qchez0G0sTjn0qEU3BXlT4L7rzCr~7F9Jpy3HP0t6mnHFNhZVDj~7OAD-yqZiSrxYz4MVzwZXU7pqI3eI4LH1L79~oXBHhshxWKoU2Cxc1ejuHWA8~2PexEkgaWa019O1uGL15zEbCeW8lndjU--Xl-cMd~2WvFrDbwNSnV8Vrdbe3K2sc--0VuDH6cOwyxUCzpiLX4UUw2-IzKLau4BMYsFFTBi2pZ2iEkjsO-W1xqWyd1FHKnymrQFQCA9rheRLvLO4xnZqE0Z~7pEqDIkUh59roJwqsxv2~eJLNEv1sUF~G98Ngr3-XqZpy~Qm5ld0iisPuLoaPVYQ__&Key-Pair-Id=K3NV4LZ47N8M46)

8.  Click **Send Invites**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401490324-image.png?Expires=253370764800&Signature=YapPGWuP6LpMUmjF6a73C-YOhqzjvSvAFJjTLIsiCi3YN6FuOKly5YZdapT2Y9wJkm0k9WvBi8Oswo2oGoX64Kdl~5jhVizJgRKGq8c3EahhtmlpfkrxlDu969esfyxIcxHMIck2flYQhuafagXhsmGhQJH2etZt~7t3pPAAYVNE7qVyOldcXYrTIBeEiWPJNG9S9DcOmx8xqEZabQWFeaELNCQKCS1WODmau0LFBpy4gPGRvGjGNgNEx7kDaeqpIc5lf-KX04ye-7MmRoCtiByrTN2yYe3qKYrCO5ygLtlt~-bbLWJYKQvLeLoj4iPNxGbaFqAfGnA5G~nHBegkJg__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: 

- Each candidate receives an individual invite. Candidates cannot see the details of other recipients.

- Do not use emojis in the subject line of your email invitations.

# Troubleshooting bulk invite errors

When you upload a CSV file, the system automatically validates the entries. If the file contains invalid invitations, an error message appears.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401512990-image.png?Expires=253370764800&Signature=aOc4~Jm239OmICxAJ69exN~7ij0HqxiHVgaJKG~BpPcqzfgReXnDtriJJeXCXiiZ7aklDerle5zrsmwhcOzBmpOOdbdQ9AJFQpXTvdtniK5aPxZv71fzUBlQNZVYNk4JmbMfP75LmzHPvnnD5~L~rKIr9F2xFNj52NkwD2dueQvwulFAGV5vewON0W1rFmnO4vUbLn2UCex0X471pE~9LjlTg~16Lqe7lVjf1Qy78gSh-xos~sC-cD2hzJoJQT-f9YPjEP6Tp8C6Zr2aBOaSUmTeGihwdtJKYmeYcW9sVxEQOHNKB7Hrf6Gtx92sAdrDrape~xe51-gbTJXH6Bh7tw__&Key-Pair-Id=K3NV4LZ47N8M46)

Select **Resolve** to view a list of all invalid invites with details such as the number of invalid invites and reasons for invalid email invites.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1757401535565-image.png?Expires=253370764800&Signature=eo3CbUuhWtWEjqm4Gd4wQ~tTsIhHVQWqxzfAWgaV8vxRGcnVePwc9teq~Vmgp57zCxkpPwQ8HOjHnYleghV9b-TyzB1yy9J5rFPChkXh2VVLFU7Jaz46kYvTzrF80m5ZiZWi8OJyQeBOn6dpIvKJUIsywIV0m9Rv1e67qr-fZgA~lEOiXL1aQsu7H6Tk0cj-RRLFO-iUz7walJcrFyl0qBzBhXbJGM~T401d5Mkm-x2ke04Q5b~rkLmFRwopQjMZ8g4vomCS6YuvH6ymGSWjYOcanldAtWnfTav8h4EfHfafdcqsnof92jLtyLBrBVS-c8tzcpzkmDBhqJjojgFGnw__&Key-Pair-Id=K3NV4LZ47N8M46)

You may encounter the following errors:

- **Previously invited:** Candidates who already received an invitation cannot be included in the CSV upload.\
  To troubleshoot, click **Re-invite** candidates to send another invite, or remove these candidates from the CSV file.

- **Incorrect email structure:** An email address does not follow the correct format.\
  To troubleshoot, correct the email address using a valid format, such as `name@example.com` or `Name<name@example.com>`.

- **Duplicate emails:** The same email address appears more than once in the CSV.\
  To troubleshoot, remove duplicate email addresses from the CSV file before uploading it again.

\
