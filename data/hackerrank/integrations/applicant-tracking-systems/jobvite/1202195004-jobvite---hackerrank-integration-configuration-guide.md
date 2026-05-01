---
title: "Jobvite - HackerRank Integration Configuration Guide"
title_slug: "jobvite-hackerrank-integration-configuration-guide"
source_url: "https://support.hackerrank.com/articles/1202195004-jobvite---hackerrank-integration-configuration-guide"
article_slug: "1202195004-jobvite---hackerrank-integration-configuration-guide"
last_updated_exact: "Mar 11, 2026, 4:49 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Jobvite"
---

# Jobvite - HackerRank Integration Configuration Guide

_Last updated: Mar 11, 2026, 4:49 PM (Last updated 2 months ago)_

## Overview

HackerRank Tests integrate with Jobvite to trigger HackerRank Test invites directly from Jobvite. Recruiters managing candidate profiles in Jobvite can use this integration to carry out a seamless and efficient candidate skills assessment for different requisitions without leaving their Jobvite account. Candidates receive HackerRank Test invites directly from Jobvite, and after they complete the test, their scores and performance data are automatically available for evaluation in their Jobvite profile.

This article describes the configuration steps required for integrating  HackerRank with Jobvite.

## Prerequisites

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 50%"><p><strong>HackerRank</strong><br />
<br />
</p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 82%"><p><strong>Jobvite</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must log in as a <strong>Company Admin</strong> user.</p></li>
<li><p>Log in using the same Company Admin user credentials to create and publish HackerRank Tests, which must be accessible by Jobvite.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 82%"><ul>
<li><p>You must have a user account.</p></li>
<li><p>You must have relevant permissions to edit Requisitions and candidate details in JobVite.</p></li>
</ul></td>
</tr>
</tbody>
</table>

The integration involves a two-step process, after which you must verify whether the HackerRank assessment-related custom fields are available in Jobvite.

## Configuring the Integration for HackerRank - Jobvite

These sections describe the steps to set up the integration on the two platforms.

- [Retrieving the API Key from Jobvite](https://support.hackerrank.com/articles/1202195004-jobvite---hackerrank-integration-configuration-guide#retrieving-the-api-key-from-jobvite-9)

- [Adding the API Key and Secret in HackerRank for Work](https://support.hackerrank.com/articles/1202195004-jobvite---hackerrank-integration-configuration-guide#adding-the-api-key-and-secret-in-hackerrank-for-work-11)

- [Configuring the HackerRank Test ID in Jobvite](https://support.hackerrank.com/articles/1202195004-jobvite---hackerrank-integration-configuration-guide#configuring-the-hackerrank-test-id-in-jobvite-13)

### Retrieving the API Key from Jobvite

You need to contact the Jobvite support to obtain the** API key** and **Secret** that are required for the integration with your HackerRank for Work account.

### Adding the API Key and Secret in HackerRank for Work

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047124343-?Expires=253370764800&Signature=kLVvEn3GQcQOgPuyZhyZhpWQZMgko16CLKIQUjnPIMmwt635ZMMkNVc2Uk42zbaIYOjJU9JQVNixxPw8~s9b1zFA5DPQ4h6GT8bo0URbWymc3BPjZGXYR2BtPNEgcnVEIDoDkR6YkGJ0-cE-mO5pGL26g5jnEmHFwth5kXa0~B89n3v2SycLOkpwNLmaktwcHoo8Suoxe0MyOoaPNCPiK8kS7WtySdW1TNdd9wZyXbrlcEjM4htOBlzE4LcSn~vvC5nzYEN~DPd1mpIapn9KG8si991Ay-YmQixIc299cIQ~W0NKo5dFR9atMPRw2n-juiOUjmazkSyYjBq-ba0dIw__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **Jobvite** option. You can also search the Integration from the Search bar.

    ![integ_jobvite.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047124773-?Expires=253370764800&Signature=EiHOtqgNtfsD52nbVTSrKCdN1RusqvvL0OBhNG2UAf4lqxKfJ-FRE0Dyr-n7s-b91Y3YI1SM6nxDyGrYuEMMKEeX~4jqmAglfftes8NWtqWgiPDGv1AbSKlHmwyNn-0djP7ybD4A-qkQigwRPKmKsd3D0HHhfMKcCiQ3Kxy783UZwoqK--70xoSzG4t7RlIQ-Hm2SXi7pXt68RUc1aIV5Yn2NiCxY~9gBaQUFQQHE-TAUkBrZujMwhV7i7gu6VHLZMlcaWCxxb1gXoB2NRN-OcPFQundpOCtaMN6FlQVJtYWNTr25dJsF6XGEMGcVPIE7fMusUSntJDvO3oqQJ4xOw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Inside the Jobvite configuration, enter the **Jobvite API Token** and **Jobvite Secret** fields obtained from the Jobvite support team.

    ![jobviteapi_token.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047125079-?Expires=253370764800&Signature=KlT~gHkfiDz3HDnjp~k21JwqyfqjLFGeHXapS07l~8K3HMq4~SDWPme2EPAplAC504CfdLkBXHJ-hjsrRcYYUTCOOcKHeihVv10q5ASYSMIwTFK2T3S6561MYX-U8oubBmAo~82ilAUiawGhAciXqvWOqsUuylL35jr1zHBQLXX4hkTdKveLRn4Lm5PMvKcLulv1C4GYPJk~QVn7vZ-WzPXvkHGlIzXt7dYYug8JWhxYS4sYJvmI7jIjbPKwTTtvS8cIBQKx1lPBZyRyh2B1-CtYdsS0hHLd-aEmmtbry2pzlhgaNX-k1Vrpzn1CdHTX4~jiKdr1q1E7r1cIcpxhyQ__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Save**. The integration is now complete.

### Configuring the HackerRank Test ID in Jobvite

In Jobvite, the integration creates HackerRank assessments-related workflow steps in the *Candidate* object and adds custom fields in the *Candidate* and *Requisition* objects.

To validate the HackerRank workflows in Jobvite:

1.  In the *Candidate* object, click on the **Workflows** drop-down list and verify that the HackerRank Assessment workflows are available. There are three workflows:

    - HackerRank Assessment: This assessment workflow indicates the HackerRank Test status sent to the candidate.

    - HackerRank Assessment Completed: This assessment workflow indicates the HackerRank Test completion status of the candidate.

    - HackerRank Assessment Error: This assessment workflow indicates that the test could not be completed by the candidate due to some technical glitches.\
      \

      ![workflow_hr.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047125702-?Expires=253370764800&Signature=Wat2m8NCxsXRIB5CALB-Eqg4M2jAhPOHIVNw7-vnec71QAAcKCm9D9VPeA3mBxlgBobwlraDtO2F83kVnEzqCRtw2hbmorzx0q7yYGRlrU6tUjJWuAwYW0blQIkGyhlsltk-U-bcG-gtRfsF77nS709vxTeopv2y3R01uVeUdLMEwNPC-g-F4lmo7yC9l9dXEq-d3ZACAgCSvOkR96g67p~pxUYM9pktu3JotaKYGQs7MgQfneLK5uDqRW1d-fc~~5tSrPafcMxmyQN0cxHhgTdcjKLv4UMGr3quTdRLOTQIq61uTiPFyGIvBLc3arTrf3exoBd9XDb40-~c-MVIqg__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Navigate to your profile settings and click **Admin.**\
    \

    ![admin.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047126104-?Expires=253370764800&Signature=n2K1GI6lYX3AE6~MzFyEHtWH8EVSAxZMDKO4SO~aaz3idOEcU5a-jkmlzDFqNG9doTyWiEVQim5jHbXSPiXAtIiobj9iGbushgBVKN77-bVqOFPA8CBYBYjP3nqhWmU~gz3TeTXKsk2cjHpQW314B8rFhiTT2DXGkIBp3PANjZ69m~hFZDPL5aFJXvxHat-3PZ55loi6tSLBgjba-W5txD3ZymxMpmqimoLYI3w4xfBtJmxdpZbkDxeOMSNW5L4oIBRtK1TYGfOdDEuLBX5-~ICIG9kLkMBN-rf4hRn~T2tKlQg1bnDwieVjNr6O0PErySeOCUfLlRhm0Ji~U1gCTA__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Configurations.**\
    \

    ![configurations.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047126537-?Expires=253370764800&Signature=LcNfmEw56QUnlWGMXDToOZjReI2Ja1qefX1JOIvARFZ~3h0ubCeyw5PKFL~HAhOlnj2knNcqgP3MXu9n73aexxbupMrkMAm2FeQID1bYJFR0TziLEqVVlo3xqf-qqkaH6HFTFZJNu9rvtol9f~ldGzgXzV6SzFzL1dtPSIq3VNdVaLbyEdnANRqX7DDOjuZi8euMz7KRXBJWSjn1au6553O4WWEaDO6J-MUPIWjaV77eybAqM4ieh0~NEXZKAXLMFF7M6mX9psYVPnuHlX4kAp-hDO1dUsB~RUEZWQU6nB97nyllT8QhXtUh3mHPMXp3usemFrXkBs8zMw4ADXysuA__&Key-Pair-Id=K3NV4LZ47N8M46)

    \

4.  Click **View Custom fields.**\
    \

    ![custom_fields.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047126928-?Expires=253370764800&Signature=qAvbGF3-CVazo7OgmijUJyPl9MXswwoUgWwIp30xNvFDLNk7TXuUbu-8GZlULFlxAnBPNsRnb~PGGyDhfh5vm8od2eDu98q0mKFRwc1yrnHkklYwGSvxDM0Z7~POpT3JbNfbPLewXqWkOxBIakKoShCZUlS-ddVmOj80o9n3ZYg7ZyeQwffyorv2IleH0hyKw~CJUQtJXxptjkYJGJe402ukroZ4yIqVsv3jBP6EygDxUUfns~FCUzJa8xkcV975ZVcVUU8YQqAgB7bbSzdSE6A~rbBj4Wa9V2rhyqOkIEheMQurzYlPNHok2IRwCgA-xuoJUALNOXqcPXMVOhQmKQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    \

5.  Click the **Candidate** tab. Verify that the HackerRank assessment-related custom fields are created for the Candidate object as shown below.\
    \

    ![candidate_hrfields.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047127352-?Expires=253370764800&Signature=a1mqremvDUjsEcC5p5WeQ8pDlyqYQ~iYpElvPif5Oh7fxfUsyftB2XKNbQoBhhJhlxloEEb-dHzYjptDyAEKuLZgpGpVbl3JzaGJ5klImDZNPds9TweNBMLUlZuG-cBctUGpckX3X167C51wlQa-t3lPmoRAXw3txnQurB9U2wc-TAqjZn8vS-qz2unbzViCjv3sdXixw0z9AroQ6FvUfOEGFyS514jm6irKBtekbDpFTOPExNWlxVs-54lTcL7u9wSzj3zKf47B7NUNxI30eW8F5Is~zW2LYZo2cXccs5iJXNiXukVY5tAAM7oTcizJKbOBvY2yyeCKXFQwIqD5GA__&Key-Pair-Id=K3NV4LZ47N8M46)

The following table summarises the custom fields for HackerRank.

|  |  |
|----|----|
| **Candidate - Custom Fields** | **Description** |
| HackerRank Test Link | The URL of the test sent to the candidate. This is useful if the recruiter wants to resend the invite to candidates manually |
| HackerRank Test Status | A string indicating the status of the invite. If this is not empty, then it will be one of the following: “Invited” or “Completed” |
| HackerRank Test Score | The score obtained by the candidate for that particular test |
| HackerRank Test Report Link | The URL of the test report sent to the interviewer. This is useful if the recruiter wants to share the candidate's test performance with other team members |
| HackerRank CodePair Link |   |

Verify that the **HackerRank Test ID** custom field is created under the **Requisition** object.

![requisition_id.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047127674-?Expires=253370764800&Signature=KPtwyJOq1YrvfOItiprIs2cEhwnTJgmJznzIsNwmRImM83VpTIS6ugKQujSFa5eXS-HHlYrZvybCoA9yFH5C99S1Owk1HLen8VVqWnXFLqSWh~hd3mJxWUAEy3ahnnDCJ3flg0LcUwUzCeNBFEafM9HSonth6xrVm9ac97eqYJb8zIqjCV-Z-8kuDkf~4w5-Dv~nTjB-eFEqWSMNcvdZgh6nPsawamlKP7Z8n-DJoDFLGXC6aSpZlksxDsquLX~utJZa9sxesKGBmXOPHylyTJqNlMcXdQaJMijTwlPhxD46n5LOZxXKZz13fTuzWXTcD9D-PXo2-KfF1tTbFkKZZA__&Key-Pair-Id=K3NV4LZ47N8M46)

|  |  |
|----|----|
| **Requisition - Custom Fields** | **Description** |
| HackerRank Test ID | Edit this field to add the required HackerRank Test IDs. When you create or edit a particular Requisition, you select and assign one of the Test IDs from this field. |

**Note**: For each requisition in Jobvite, a HackerRank Test is tied to the requisition.

To view the HackerRank Test Id for the requisition, select the requisition and click the **Details** tab.

![req_details.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047128075-?Expires=253370764800&Signature=agX3m9L4uJr7m3XY8gPfyKp2Sm7AvS7nUH10TCuuVGby9m~CFQirzRxd2hnyyUJv1NGJiuAIeb4XvJZxW~aEJjzG-ucOujZbiroXW9UaAxBR30cdfbdGdq-n5zv4Jn08-LJvDdp4NlH4twNBjOAaYMs2W9PpZwDRpheEbLW3S~gktfe7Xgstgxkgwujepk4N1MFemXCaA3qVPBOkYf6ae5BtkmpXlABZ6m8a14RyZF3GLO77yu5GMLduvdVDgQIP6aUOlxOHIuojXa4yhKbYV1iwFeYLxqMUtfYNI~o-5XVeWS24uYt3BXCLvRytb7-TyP8KRnRKKapLdk9MhaEXlw__&Key-Pair-Id=K3NV4LZ47N8M46)![reqhr_testid.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047128487-?Expires=253370764800&Signature=FbWAvMEO04D2byc783uoj5FnEpTfw6N5jzBjksU~UvbZoe~Tam3CROIc4VM5lye4os~xBz~oIFJbLXl~AOMK7obvt0KiL6kGzvTnRFjNjqj43v0jbTXm1Sy1XY65TmzEqLB22GylnicL68J4uisfqhSYzPt5NvzWeLD2lGorEYXHjpCYqfIflLNzZAgNA~Z8zSkVjKay1GPfwV37IbKfeMsy03VPP4S3mboK4Cy4BXG8JFcOVToWaz5mAPufQAHSyhLlz8hg0Q1mwn6YDBY0z8DmWBiRqG53SQir5RbZky~6PjZ9dwqisQWZuw6ZJOGsj6J7Ow2LnV8S5IUZRZLB-g__&Key-Pair-Id=K3NV4LZ47N8M46)
