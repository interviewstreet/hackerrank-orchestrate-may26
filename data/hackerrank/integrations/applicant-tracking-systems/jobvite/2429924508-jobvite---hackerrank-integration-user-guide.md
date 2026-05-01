---
title: "Jobvite - HackerRank Integration User Guide"
title_slug: "jobvite-hackerrank-integration-user-guide"
source_url: "https://support.hackerrank.com/articles/2429924508-jobvite---hackerrank-integration-user-guide"
article_slug: "2429924508-jobvite---hackerrank-integration-user-guide"
last_updated_exact: "Mar 11, 2026, 9:40 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Jobvite"
---

# Jobvite - HackerRank Integration User Guide

_Last updated: Mar 11, 2026, 9:40 PM (Last updated 2 months ago)_

## Overview

This article describes how you can use the integration to trigger HackerRank Test invites for candidates from Jobvite.

The section also provides helpful troubleshooting tips for common issues encountered while enabling and using the integration.

## Configuring Settings to Send HackerRank Test Invites From Jobvite

After integrating HackerRank with Jobvite, you can send HackerRank Assessments from Jobvite to candidates. The following sections guide you on the settings required for both platforms to send assessments to candidates.

- [Creating Specific Tests in HackerRank for Jobvite Candidates](https://support.hackerrank.com/articles/2429924508-jobvite---hackerrank-integration-user-guide#creating-specific-tests-in-hackerrank-for-jobvite-candidates-6)

- [Associating Requisitions with HackerRank Test IDs](https://support.hackerrank.com/articles/2429924508-jobvite---hackerrank-integration-user-guide#associating-requisitions-with-hackerrank-test-ids-9)

- [Triggering HackerRank Test Invites to Candidates](https://support.hackerrank.com/articles/2429924508-jobvite---hackerrank-integration-user-guide#triggering-hackerrank-test-invites-to-candidates-15)

### Creating Specific Tests in HackerRank for Jobvite Candidates

Before using the integration to trigger HackerRank Test invites from Jobvite, you must create and publish the required Tests in HackerRank for Work.

1.  Log into **HackerRank for Work** using your **Company Admin** user account.

2.  Create and publish the HackerRank Tests based on the specific job roles or technical skills expected of the candidates. To know more about creating and publishing a test, refer to[📄 Creating a New Test](/articles/7073839065)
    \

3.  In Jobvite, you must associate the HackerRank Test IDs with Requisitions. Therefore, note the IDs for the required HackerRank Tests.

    1.  Click **Tests** and open the required Test.

    2.  Locate the 5-6 digit number in the URL, which is the Test ID. Note this ID for all the required Tests.\
        \

        ![integ_brassring.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047128869-?Expires=253370764800&Signature=GtPJD1jHXEVnBA-Ca7mdiXSbXwBjUX68B7Od2whpZJfdgpmcPUQej4pZ5ZhqNu-vKfPIrMfMhUQNH~WUplLlMbMeXEznl8C-yim1Nk3NK~V0PmQbYrcAKtjIGScdXFIKwxCPhQbn-24DewYmZnoDYOtpOnS1zJx-5aU4Pi6lWJIikesIX-645NAmwzZlyMfw-EsjNtpzByVFkqRJDMeOJoEKgrzO6EpBwBqCC4v8Yi9HdKtFYQrNk9ojVDk4x1iIsaUfBshaGl5uIIZ-g3kcDc0-gaPIciTmMu-X~liSta8oOPn56kpgaJdaw3AJJmQM4JAmG4Nrpdqwzu2cIyWDzQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### Associating Requisitions with HackerRank Test IDs

1.  On Jobvite, add the required Test IDs in the **HackerRank Test ID** field of the *Requisition* object.

2.  Edit the **HackerRank Test ID** custom field to include the Test IDs and click **Save**.

    ![Jobvite_Test_IDs.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047129202-?Expires=253370764800&Signature=i~obXrD6~gQqgEmnUL6hPYaJ2RciH5RI-aS4DmBGgDMik-aW0ObaWZ8rlfpKOrAZysaCOKtVEEJwRjaDlgfkzYukRYYg2UKLU4-UW3bBVUJ4cWHwNDojwWYyj4lRRhApKict9g9WbB-~y8hylFTrnKwiPcffxjnhUUlKjVZUuTZuHg~K8KrzrZEQ60lazI~4PFzvyMWPOn5HIPu9l-lyfQK-7mX30kRoDf3wbapxUR0tiXK23iwvbiAc5SQseo9BiUJigRx-8JGs~AWEPtYcP7dgSA-Qb1goPmNUwEpi1BlWPvCx78pv3aJ7VM8T-0uRIEVbIBR-Eg6BgLhJqvO8ag__&Key-Pair-Id=K3NV4LZ47N8M46)

You can assign one of the above HackerRank Test IDs to a Requisition. For candidate profiles associated with this Requisition, when the Workflow status is changed to *HackerRank Assessment*, the event triggers invites for the HackerRank Test.

1.  Edit a Requisition and in the **HackerRank Test ID** field, select the ID of the required HackerRank Test and click **Save**.

2.  Similarly, you can associate a particular HackerRank Test ID with all other **Requisitions**.

    ![Associate_Test_ID.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047129575-?Expires=253370764800&Signature=n62vehTBbVmSAsYEEXIU7R2CtuPC6WLWjpCkKNmyHdzDk5aB1ZsueycO8sNEGjKJ8orcAevPElpf5eTCEBuwH5pmrpRQDpOAU7UxK4nv-p6E8RLh6rDf6DYZQ5CFBgaNhwvjnz6cCMSdEKo6bgZtDS0WhfMmSWnILFYfCaoNHQC2XZlCkg5I11LqUvCKMn2iSqz1f4uo0Q9LNEA4ImZcLm6QGSJFK9wcNLpKRfYbKaZySvGXamWVp~WvzqEhzqzeXO9yksIudjdgkUWySTPkhdkGq0cPEDTzkphnjGMQ649L5gxdEwjtR8PfIEbbS2PuRn5PSfMvz0GM5iraaHmfCQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*Linking a Test ID to a Requisition*

1.  Link the candidate profiles with the relevant Requisitions containing the HackerRank Test IDs.

### Triggering HackerRank Test Invites to Candidates

1.  When the candidate is ready to take an assessment, change the **Candidate Workflow** status to *HackerRank Assessment*.\
    \

    ![hrassessment_status.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047130014-?Expires=253370764800&Signature=EqvJfP2jt8NJu64m61cHWW61rXfnBhbWTYfwBe1tcJSesTtSCvxORAb4Smf7VkiaNXO6SXWfjwNKJyKfepeCZ7gAhLjgi0hNmWWGwT1t76sQgDQ~JJM7CL-7YfUgTexRb89~imiKoq9CFOsRmkOGLXAIKMOThb3Dvaeq8ajaXv~DzpFbjoNvSnUKkNuA8Ab0LWmczl3amVHSP87Xr7e5iCF3hjTBG3WLOviGZQ3hi2E8FXNG7X8AHbG36DF8GS18B9~MqnlSEJs3MnSlGbwZSfm2cyu8kTZ-fnHUkeTBGpVkQB0qtD2bN-XTZOjlZ8dRl0dYlmInBOrJMC4gzqt8AQ__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  The candidate will receive an email invite with a link to the Test for that specific requisition.\
    \

    ![emailinvite_test.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047130345-?Expires=253370764800&Signature=rv3TPSl6rkkHsNVlCJLT2DvRW3~O586swfNDUJv1Mc-6PpW3UH9wIuwz2HQ1Tnhzdl5YlwUnqVRyoZuGA6yRPJ-jriprQkN8XsoA889p-H5CUfU7EVkPSmejcGTKKEQ4mctJEooKo8S9wvRcmLJIW2jJpKo9PneitVudGA0PxJ9s5kWkPDULwn4TB2hHAE8~QmQHwsrDhhXYS9czusKgMyKzStX3-~8y680vDAxzLn1p7SBbt9mhWDfIZCRZM~dCcO5JX6w5~P-yVXIbLjsEUCphc0-fLixAF4Xp1DHrnmpT07pI9T5HgQmFs6pEKjOw1qd5UqwvAmRpmBsUtjDxnw__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Once the test is completed, the workflow status in Jobvite changes to *HackerRank Assessment* *Completed.*

4.  The Test report is automatically updated in the candidate record of Jobvite.

    ![candidate_hrreport.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047130696-?Expires=253370764800&Signature=pdRCbKYbqm8cDN7ZtnPXyZTQs1WMAnIS4-ulPArpgEhcFgjsNSizjegPhh-av8FLDEA193yihhhs9m5rh9yY78KAVFsqQlMSQr9M7NHrd1Zgv56pDeSfPBzZVa37p9X7BHRH6mT7x5cfcjEV~hzk7DlHwdEEmK9N6pFynvJK-HqQOWEP~SykK7TXniocUp0S~DVLcMWZP~sOz34IGO9wtE6bNjjGQCw7Td8PzlKNCZ-m5MPy~y58PAW9tBage8i6wuFNQBBLrlPva0odSMNhZoaQFWWwwyZ3D4Ca1CoBbGxZk8twF5JL3eUYk0x9hmGpSA7EUh5GKmJPuz7rVctsfw__&Key-Pair-Id=K3NV4LZ47N8M46)

## Troubleshooting

View the **Application Details** section of the Candidate profile to note any issues encountered which failed to send the Test invite.

![application_details.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047131025-?Expires=253370764800&Signature=h9ksZoS-fbZ1lFWvc2D0vLDiPW-EOd9ZKdHw439jra9G1k~Uvxegq6zd6REeKBFdoPRh043b0OJ0mwGkgHSupCwu90OJshtUidoTU7z3FaNDwWHXRIzLz05zM8yDUx-ZDj4NFlmfV38DMVkW1fHzcpUlnqo-HGtV~Cu7gKXG01u6CWioEWZLw-jcywGTjs~7N0Uy2xlztPw3zEIeWBZEBlI3RDhR2L8HiDC7llVOJjKogRK5GaOE8a99ZqzHhcy5P-ZeMA9-rZD2wca1Nk-aDUt-S3qL1mYK7bgtvTGZVOyoDqZY0H77QCWmwdcP4iCWtnVJEoU7vIx-jf3PAP-h0Q__&Key-Pair-Id=K3NV4LZ47N8M46)

The **HackerRank Test Status** is set to error status when an invite cannot be sent or another such error exists. These are the possible error statuses and the resolutions:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; vertical-align: top"><p><strong>Error Status</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; vertical-align: top"><p><strong>Possible Resolutions</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p><em>Not Invited. Email address is not valid for this candidate</em></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p>Verify that the candidate's email address is valid. Add an alternate email address and try changing the workflow status to <em>HackerRank Assessment</em></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p><em>Not Invited. Email address is missing for this candidate.</em></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p>Ensure that the candidate's profile has a valid email address</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p><em>Test ID is missing for this requisition/No such test exists.</em></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p>In HackerRank for Work, ensure that the Test ID linked with the Requisition exists and is a published Test.</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p><em>Not Invited. Company/Test Owner in HackerRank does not have permission to invite candidates.</em></p>
<p><em>Not Invited. Company/Test Owner in HackerRank does not have permission to read the test.</em></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p>In HackerRank for Work, ensure that the Company Admin user account is set to the <strong>Recruiter</strong> type and has the required permissions to send invites.</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p><em>Not Invited. Inviting Owner's HackerRank Account is not activated.</em></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 314.375px"><p>Ensure that the HackerRank for Work user account is activated.</p></td>
</tr>
</tbody>
</table>

## Frequently Asked Questions (FAQs)

### After the Test result is initially synched if I change the score in HackerRank, will it be synched back to Jobvite?

Yes. The first time HackerRank sends results to Jobvite is at the end of the test once the report is generated. After that, any user action in HackerRank for Work that changes the candidate report will be synched back to Jobvite. The significant visible changes are:

- A change in the candidate's score

- A change in the status of the test report - for example, from Completed - Evaluation Required to Completed - Failed.

### I moved a candidate to the HackerRank Assessment state, but the candidate has not yet received the email. Why?

The HackerRank servers pull the Jobvite servers once in every 60 minutes. Therefore, it can take an hour for the candidate to receive the invitation email.

### Who is treated as the inviting recruiter if invited through Jobvite?

The owner or creator of the test is treated as the recruiter inviting the candidate.

### Can I use a custom template that is saved on HackerRank?

You cannot save a custom template to be sent to the candidate. The HackerRank for Work default template is used.
