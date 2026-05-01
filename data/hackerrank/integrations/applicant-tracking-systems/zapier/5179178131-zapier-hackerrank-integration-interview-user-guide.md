---
title: "Zapier - HackerRank Integration Interview User Guide Prerequisites Configuring Zaps for HackerRank interviews Sending interview invites Viewing interview results"
title_slug: "zapier-hackerrank-integration-interview-user-guide-prerequisites-configuring-zaps-for-hackerrank-interviews-sending-interview-invites-viewing-interview-results"
source_url: "https://support.hackerrank.com/articles/5179178131-zapier-hackerrank-integration-interview-user-guide"
article_slug: "5179178131-zapier-hackerrank-integration-interview-user-guide"
last_updated_exact: "Mar 6, 2026, 12:30 AM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Zapier"
---

# Zapier - HackerRank Integration Interview User Guide Prerequisites Configuring Zaps for HackerRank interviews Sending interview invites Viewing interview results

_Last updated: Mar 6, 2026, 12:30 AM (Last updated 2 months ago)_

You can use Zapier to automate HackerRank interview workflows. This guide explains how to configure Zapier Tables and Zaps to:

- Send HackerRank interview invites to candidates.

- Receive and store interview results.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have active HackerRank and Zapier accounts.

- The HackerRank integration with Zapier is complete. For more information, see [📄 Zapier - HackerRank Integration Guide](/articles/9883166979).

# Configuring Zaps for HackerRank interviews 

A Zap is an automated workflow that connects two or more applications to perform tasks without manual intervention.

You must configure Zaps to automate the following HackerRank interview workflows:

- Send interview invites to candidates

- Receive and store interview results

**Important Note:** This guide uses **Zapier Tables** to demonstrate how to configure and test Zap workflows. Zapier also supports many other apps as data sources or destinations, including spreadsheets and collaboration tools. You can replace Zapier Tables with any compatible Zapier-supported app based on your integration needs.

**Step 1: Generate a webhook URL to receive assessment results**

This step is used only to generate a webhook URL that HackerRank uses to send assessment results.

1.  Log in to your Zapier account using your credentials.

2.  Select **Create** **\>** **Zap.**

    ![5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769491810164-5.png?Expires=253370764800&Signature=hXErxjHmmswj9sxqmuj773X7qy~fE9S3SclyfwgduVVuKB7siIW~APN9cF61m2h5t5ZLPNcY2AIOjh4uKIgB~KTmJ5-Vir7~dUF2qLHvWNX75OcEgcSweMXOK9jSG38wmfl9W7~qG6LSH1qX3YUCqD4yMTlGJ3wBP8SbEDwQovCu850YMcBXMkxKWtjqrgX039Q1H2F29Yy11hZaRbKlA4FErYAv6bvCmB2xpkAqoDsV2HpB9l6t8nOuIIPBp1qV4tUOQqOG2VX2QyKZnkw-RKZJS5H74IM5j0EaGqNy3oXS15KkW~dBrw9H5Z0LKXb-KHuElN874mb6jROT6I~mMA__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Rename the Zap:

    1.  Select **Untitled Zap** at the top.

    2.  Select **Rename**.

    3.  Enter **Interview results**.

        ![6.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769491918973-6.png?Expires=253370764800&Signature=Hj~wk-CAXfiuLO3PduxTsQmvMpbyo5jGUy0-zrjDBjRqeNVJb1BgVj9cIjlxqqHouGcw5zdQkmDPN-mGufct5mjWGIWChtn6aKCHzc6eWmNhEwZmxrZEc627GSoTOrZc27D0X8dZcX0fSM6GKnuLOVeUaQIU9R4kYoogT1xzMM0QQIbhm9GL0yykCyQns~rWKbw2sEwGOXmAycEc61WDSyE61OIsjXiLPCc05Xj2i90VHUVChg3M4vBvTMe2POcbYp5~QU9pstadf4km3v6lsTE--Pff8nUgcgAheyaqXjcJhh95bxU~Qb3AmiztxhAxTInMSO2S4d-gnnOzehKyEQ__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  In the **Trigger** step, select **Custom \> Webhooks.**

    ![10.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769494359142-10.png?Expires=253370764800&Signature=XiqnWoRZ-JFGimEXNCdYmhtPrdsTlTpef6CLNmtayzbnyCSfSjzWRVZSGR4ewGe0yoESi7Y7oqaVWC0DocY~tN7h0I4~rqSFSPzY-JHKKgzluI8NfQ0Px9tx6BfHqKlbYfr97uYiGrDIzdanSbYez6b2ddKnG6Fcd3aUMyPehs~3PaKqOhQNl1fxIPKuRZhfR79xYy4mazKtDuRpITi8fhDHUOapyqkCytlNGebvNcywYJHgQYuhFl6APHWyQovmTfyT7Pb4OlMjvES14Tru~TTOkDsDQa275oPRRBIfzdaEtfQH-62kPFE74jtkI7DebFdZx0fgra3-xylEf8CULg__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Select **Catch Hook** as the Trigger event.

    ![11.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769492861247-11.png?Expires=253370764800&Signature=EQZywBBsXBdYpVQDzvVHezLc8pAbsuaj4qrTjQCcirmHjIPNeWyagY7pPT-ANwN7Kz1Bioh6ZV9j1JEdbrLwbfhiIx-A3JFcJvk0zTaMawkFyzF5C5FgIDix4cErJOoB-vR8tFZmAjlyZ6eN8hLdArpzqJn01ANWwaw~W6P~poE99su-1oQpg0TtBlLT~3oB9P40nZ0FBchFnbo9VUmA~WGRupC3FVhpiMYxOg~8utEBrd9Sj182tebzK0cjovv0JrwcQFMA2CKXdlLSbuzJ01oSzsTo435GbED8lx4Ti~IDsxsZDgpNZ5NWW7MnXDzLQedkNPL0p2zmwS3qZ3Z4-g__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Continue**.

7.  In the **Configure** section:

    1.  (Optional) Enter **Pick off a Child Key** if you want to capture a specific line item.

    2.  Click **Continue**.

8.  In the **Test** section, click **Copy** to copy the webhook URL to your clipboard.

    ![12.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769493012305-12.png?Expires=253370764800&Signature=gPMPYo4zwgaBWuiE4zXcikWLvMhSRXcNwj~8X8CcdUJPYg1k4EoaPdmufmiXyX8L0cEpzdUM2SOijpy13kf7QBebOuFwaWoARV06~aj-cMZFV3G7KhNLNKx0uKclJ7FFgww9a2SnSYaQqOn2NKC24hPV9ef78KwUispazcZ994F5jRGYFiGVbeUdprDsa8BTFZ589ojRCnRwj4mpPk0dr3D-nW~RxRnj6PrI9clW5hDo1OjtjB7pq-FfRyg7fX~-6xz4dFKMOUegLCwdTICpV2CbWY8Mp~ENtF0aDT3cI~mmIY-vskD0qofkUiv2f15h33pPtjpEUKQpVTSl24clYQ__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: You need this Webhook URL in **Step 2: Create a table to trigger interview invites.**

**Step 2: Create a table to trigger interview invites**

Create a table that Zapier uses to send HackerRank interview invites.

1.  Go to **Assets \>** **Tables**.

2.  Click **Create.**

    ![7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498894142-7.png?Expires=253370764800&Signature=Tuu9-zeEKrmdvPTifd7oj6O~9JgjcJsXNq-vJk6~wCsA6W817vgh1yMJprs5C3ApwCLAtEhpcDUAnoZzdBBn3BQAMc4Lg8~8g0cl-kehcbWeOkB7WOXM26eIZfrBjDvx6aw7pccqY68Ert009FEw6ncMYwGwkb-Aif~loGw-XdQTtIjYgd53JaJVJxpr-IJzaTUN7zmSHOc8X~x15~Etr4NOKE8QEmeCPec-AK5o7YDbuLabTvoAJNHJeUElrYFQjaYa2C3SZPa-Vw6uryvclBv2dQ8PsPCmStcYYZ0o29J18xq5OjGMfdhGrptHcKEgk0OCAzUAhEDyR6K7aEHuBg__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select **Blank table**.

    ![8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498917372-8.png?Expires=253370764800&Signature=UNG3JZNgPfavAi5zYdoLpgMVrijHlbjRrKoZ0eGOaMtdDe-XuCVQDtF0X7eVEi-dMOXm3mvyUCoSg6A1B8fbe9j1fkXl-S-bus6MJ94YmpJc9cwKJsvwQFVpIlwiWSoZ7RCS~t5lTfhQTTJuv9zzboiDCEmB6BJyRe6bdUs~PFc3Vy7fN6mIEieY2WdCO-jLhXxqzIUF6-AMB2BTFnSsgpVCJMRMJF56hhwFRdHUs7DPBB1ycOz7dbsF30FS5vNRfufP7fXug6ugaom2LRQM3yCHtYUczNDKisM4oIbGHCmNk0SdGmuHMHsfuS8mWaPVEzS2o5GDhpJEqzD8PEGgHQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** If you already have data, select **Import data** to upload a CSV file or import data from another platform, or select **Use a template** to start from an existing template.

4.  In the **Create a new table** dialog:

    ![9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769499104907-9.png?Expires=253370764800&Signature=EKBYhcHaZjk0zU2vSui4Cop4U-7AYlN~QDIK6v0MOkMm8ANSn9t6jeDIlewbaoN8P9gk1YBOLO-i0UYCWffVDed3C5gUJ77Mjuwisn~xnaesatfZAfnmFxxS8nGc6aVmUkDrRNd2Ev-dG0TlLwyyDxhbw2j25SF1q0xrYQ4IZrbpw3SJKzTZW6wvDukCl6M9V705GtzTHuLx-a5dBOFU4t-vAFDl0EL2VconlR8WrTYKKJkUz7UadSvgqqwtjedlM55cimVOOwvksB18k~YROG7kC~3bnYapbfb-FYl8TuFi-jJvVL9YdzJaUzgMIvnvYbsYqBjUYlDYn28-4LFLMw__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter **Interview invite** as the table name.

    2.  (Optional) Add a description.

    3.  Click **Create table.**

5.  Click **Add fields** and add the required and optional fields listed in the following table. Select the appropriate field type for each field.

    ![3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769509439609-3.png?Expires=253370764800&Signature=I0nuTrImOOP5iSSKtco5RwytV~22SaispL0mFzcM61DDyVEDlZA4o-MGC-BhO5g8RdjWZdyDnQgwQoGZ9YTPj0D6OreGf9rd1FZNzgKsfp8lsg4Sd2vrfQZwA8un2FYDmPGXu4j3yN7yZBrvtV5qk~cAyJVfunt3Td6x2LM2FooJHpxfaO6Xw9iZuU~BQT638bdhKJYJAoFJD0p6h~IjpnRtU3JOTLRtpDqi6HHquv1-NwSdhVb7eBI3YVvnGrrJC3CvIjW-qTVxutvGN-5ZzYnB4fvfndkz0MtFRBgH1mjaCV8gaqQnhRgM1iW-GhRjf6gc3VyJtrnDqpIMB0-7mQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    <table>
    <colgroup>
    <col style="width: 25%" />
    <col style="width: 25%" />
    <col style="width: 25%" />
    <col style="width: 25%" />
    </colgroup>
    <tbody>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Field name</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Type</strong></p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p><strong>Description</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Required/Optional</strong></p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Title</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Title of the interview invite email.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Requisition ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Job or requisition identifier from your ATS. This value helps you associate the interview with a specific role.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Candidate ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Unique candidate identifier from your ATS. This value helps you track results back to the correct candidate record.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Candidate email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Email address of the candidate who receives the interview invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Send email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Checkbox</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Determines whether HackerRank sends the interview invite email to the candidate. Select this checkbox to send the invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1" data-colwidth="117" style="width: 117px"><p><strong>Result URL</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="171" style="width: 171px"><p>Webhook URL that HackerRank uses to send interview results to Zapier. Paste the webhook URL generated in <strong>Step 1</strong>.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p></td>
    </tr>
    </tbody>
    </table>

6.  Enter sample values in all required fields. You will be using these values to test the configuration in the next steps.

    ![4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769499571608-4.png?Expires=253370764800&Signature=T4ST93L1enK5lgXhUYPnTT3SQ91df5Pmxx5fJBrWDp2ec-bi0Sco-9TaZ7oSg6iu0SuknGSpeXQFXFYCTQA-0fGuHMBb0OKHaktjboiYC3yuibfLoCm6nYkylXc5j6TAVX6iYa8jJ5HeqYPMvIG5q7t6TuJlSD6nUPptixOotQQxk3AQo8xRDGbifn2gFaTDwm0HJ9rNtvN4gVyHxjSez7idqucTvim2sny4FxD3hsPRYmr~TdotSQMeO9BxNMuKa7L5oz3hVQkdvIxOw7sukmJPJI4x4itkc-YB6fFXbMcmwLg2sBil4PXZFFDvb3goCQzHoovyDImZky9WU8sm9g__&Key-Pair-Id=K3NV4LZ47N8M46)

**Step 3: Create a Zap to send interview invites**

This Zap connects the **interview invite** table to HackerRank.

1.  Select **Create** \> **Zap**.

2.  Rename the Zap:

    1.  Select **Untitled Zap** at the top.

    2.  Select **Rename**.

    3.  Enter **Interview invites**.

3.  In the **Trigger** step, select **Products \> Tables.**

    ![5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498462495-5.png?Expires=253370764800&Signature=hlgtzbcTJ2WjnsGkcRGTjx7nDckHb-XYMBP4NmZeTw3~Y8Dxnb2M3VmJ04qpJTbOhb0JhjRmhbau682hvL4v8799RsvWX5BlQCuZS6hKAq9cb27ZpQMDVgjk1KaaNY8k1cGBEo8OowYqH8Mz94HVtgTs~N5WSfn20NQVWrFMRtTWG8DMNFiBT1uPotmAlZNUN4wSUuXWv7oS0jZeTcVeG80K-00oCsE3YfWj1arjTE67DpkWVjA3tfLH8JzqxgUwvkfWn7zqUlUBvTw1PK7WJhO0pb5GOq2zaiNDy9zHrnXUfGTdLTECn07HWKs3sWoiXd1CIu5Kx~ZtUhmtpEkrgA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **New or Updated Record** as the Trigger event.

    ![6.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498570192-6.png?Expires=253370764800&Signature=U7eVdYampmRkXClE5pKLVBlVkjopAL45OnuJcsyF6OAMD~n8DVk9ZeJUubPAs71ZTv9u~ZKs8cfUo9GrDnqqAEDSjQvhfOFZmjuuneqZfYagrF2gRsHo1~3mbp4O9-7zhAEor6qdoeQrCpt4NAttURF~K1NDl-duleyw~qR8J--SCIX6qsk33nt9126D~FTlK4QVrpJzceK3FCE-d1C-ne42Wv9WMEeNxQAtXldTw04sC4D2cT9nEErAn90eLbymdAhnqgOe2LqxUZ3rAmOAO1oWfPolSL0CpJYBdCNXdWkrP4GVSJlm4zem6OHnhKhqNXYq0h7DMGvScTIMjrUyEA__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Continue**.

6.  In the **Configure** section:

    ![7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498601160-7.png?Expires=253370764800&Signature=slt~0wrs~swEmGTKNiVu6CmtXbiNrnCfKU3efqpCYlez7JCaWtQeN3oAvKVXn8S5~pODY8Hf4lwXb-iXiph43aT7Lim37zppQjKFT9601CV9DxBdIvrvSqcugmHIu~hPJbrONJzLmh-7rO3LlnFf-~zzqPwYqA0zZABkoUzwu9QfV~UaO6UW~YeQGfdI6WyQmX7oZNz4R0IVRWCgypMTPyvBZBC0AVXT5g80D7-M2MqoSNseAIpgPtTVP0Q1YInpNnlP80aNKb8VikhX9zAyyimjrGZrJMsW1t7F6ov9~vGPzsPKvFmpT4UKw6s-w8M6xndDw1d3LssNEIUc6f~LzA__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select the **Interview invite** table created in Step 2 from the **Table ID** drop-down.

    2.  Click **Continue**.

7.  In the **Test** section, click **Test Trigger**.

8.  Select a record that contains interview data.

    ![8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498622696-8.png?Expires=253370764800&Signature=JzpcIz9sJtQvqxiMW7RVw7KU8TsXggcq76NhoBQ4sPusZzp9LKTKni8WCUMal1XfgKrw-1V98JyY49e4sU99BSsV628Y2UuWvpbv0r-RytsOee3i-ot8Nx776uJaCVP1svtotH3dGIOQjC~VL9o92CdrvKskfBVo2qnK~ofwzMl2Y4J4W1JmYUF3lJRtK-znsjyu9lI2KhFRXMVlV~KySSAC9A9vwlia0eBUN7wuxx5dpRUvqNw9zWJULaxcsDznSV0lbsUgeI-~fq-o2Ingu2a9HC6l-W7iqkaYFuCVv0K9LtpSTPa7sapIYjUpx6lu~Og6MmKOOSSI7eQz3Ft15w__&Key-Pair-Id=K3NV4LZ47N8M46)

9.  Click **Continue with selected record**.

10. In the **Action** step:

    ![9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498650443-9.png?Expires=253370764800&Signature=Uy5a9YUY53ZOblMrgnkWfy8VwG6TAvM3APqBIToZLBMEmHogjnf9EKl-yP0e0FdUhT6SVhpOnHrb5p6OmMDg2aDlYNKrZHHDLkqbVgrQ3ra1~KMIROHGic-TcNbiCacxiyI3xEHKsyW9H9Pi-SCz97qyH9s8BolHEjjA9QJsTA4a50NVe-Gp2mYMfXfxXBovAVlITW-214lK6s0fLeEPRJI6EaAsrJxJD7~rPErRJUnBNdyTzugZz4qv8ZsUHDKjen9uFUuOZdsNfYnOCixXCEXuN5MGBrx2GzNOkvdwUm3z5aWDwQkQiQ7Z4H3x6A9d8Z0BRsrDwswZnzC1yLQCnQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select **HackerRank**.

    2.  Select **Schedule Interview** as the Action event.

    3.  Click **Continue**.

11. In the **Configure** section:

    ![10.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498673525-10.png?Expires=253370764800&Signature=dHaLo~QV3wdhNf5ljyPoDbIxrmBeRAWNGbbuPX66AyhYRjHLzkyU1GNX9prkryTOswaHkFXojxfW9dDByMbTP2bbU9wM~mlu5km1RvvajUp2vPxJR2cmO3BF3Ock82ogVirTzrUrQ9qAleCMszGsgOr0462okDTECXPX37v1Ch7RlWH-p1IAzvG7YkLS1oQTZ9Yc-JXa0eb5Mjp-r6SgZXDts96iexIJcnd4GEtFrFONKeczBQg8i6YxmAmTk1tqpbg7SaGlpm9vHdnB61buiJQD9CXMO-hiT18uIsxr1kgfbixMvLlhzLCyHBwfz12euIyfwzQl5xxslkj0uZPkxg__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Map each table field to the corresponding Zapier field. Use the forward slash (/) to select values from the table columns. For example, 

        - Map **Title** to the **Title** column from the table. 

        - For checkbox fields (for example, **Send email**), select **Yes** or **No**.

    2.  Click **Continue.**

12. In the **Test** section, click **Test step** to send a HackerRank interview invite using the sample data you added in the **Interview invite** table in Step 2. Verify that the candidate email address receives the email.

13. Click **Publish**.

**Step 4: Create a table to store interview results**

Create a table to store candidate interview results sent from HackerRank.

1.  Go to **Assets \>** **Tables**.

2.  Click **Create.** 

3.  Select **Blank table**.

    **Note:** If you already have data, select **Import data** to upload a CSV file or import data from another platform, or select **Use a template** to start from an existing template.

4.  In the **Create a new table** dialog:

    1.  Enter **Interview results** as the table name.

    2.  (Optional) Add a description.

    3.  Click **Create table.**

5.  Click **Add fields** and add the fields you want to store from the HackerRank interview report (for example, candidate name, score, or test status). Refer to the [HackerRank sample interview report](https://drive.google.com/file/d/1lB29Bmnr11Zve2DzGWPmGCAY2OKZp3I2/view?usp=sharing) to identify the available result fields. Select the appropriate field type for each field (for example, Text, Number, or Checkbox).

**Note:** Zapier Tables is one option to store interview results from HackerRank. You can also store results in apps such as Google Sheets or Slack, depending on your workflow needs.

**Step 5: Complete a sample HackerRank interview**

Complete a sample interview to test the Zap configuration.

1.  Open the interview invite email sent to the email address you entered as sample data in the **Interview invite** table.

2.  Complete the interview.

After you complete the interview, HackerRank sends the interview results to Zapier for testing.

**Step 6: Complete Zap configuration to receive interview results**

Complete the Zap created in **Step 1** to store interview results from HackerRank.

1.  Open the **Interview results** Zap created in Step 1.

2.  In the **Trigger** step, go to the **Test** section and click **Test trigger**.

    ![11.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498380731-11.png?Expires=253370764800&Signature=QhSfSklnuV6ZnjzxPcYVWbzhH-Fkx~6z47Jl2CNazYFNqQ0eCdFHOxfUfElqei4tAUg0tDQ579B-N5DcRD93Wgz86RBSeK0O2sfxAtuN1f7fq7eayqW6L5K2vc3CDizmR7NXv6bZG8KSjzXfFXxcaV8QK6d2hfa7y~PJeDsNqYB7pXA2xVXqglUu7knIRLW0ww037xiK-kafHp9oJwRUUcZhpzDTMAS8AxuZels~4HKSp-1vRUf~VmnLpcM4CsE9XewfGOU6wJ4uQkwUBQeylBD~X2nVz-vcMbUtNp5QpYBjNZ9LzCuBSfwAKLh9kftiW-WzAs0cPk1IqOxwg~eGEA__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select a record that contains interview results of your sample data.

4.  Click **Continue with selected record**.

5.  In the **Action** step:

    1.  Select **Products \> Tables.**

    2.  Select **Create Record** as the Action event.

    3.  Click **Continue**.

6.  In the **Configure** section:

    1.  Select the **Interview results** table created in Step 2 from the **Table ID** drop-down.

    2.  Map each table field to the corresponding Zapier field. Use the forward slash (/) to select values from the table columns. 

        - For example, map **Test ID** to the **Test ID** column from the table. 

    3.  Click **Continue**.

7.  In the **Test** section, click **Test step** to verify that HackerRank sends the interview results to the **Interview results** table created in Step 4.

8.  Click **Publish**.

Your HackerRank interview Zap automation is now complete.

# Sending interview invites

After you have configured the Zaps for HackerRank interview, you can send interview invites to candidates.

To send interview invites to candidates:

1.  Log in to your Zapier account using your credentials.

2.  Go to **Assets** **\>** **Tables**.

3.  Open the **Interview invite** table.

    ![12.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769498266147-12.png?Expires=253370764800&Signature=EKCvcCgYp3UugN4tJ2I1rCTfD-YOBqo-as6SY4Q7tjIV-eB6h8eft4y4yi6bSwQUXYrz4tyrdMSP9jH6XXErZqzG15Hyc-Y7Xn7i3NjG7VuUBrQSL1iOPIaJQiUphIHjSCNjbq30cLNLRixnAQiGb9xM-OR5xXwHjACMdfpwqJmA0Y57soZh6r3hoQNpNUBV278B5PgzQsUP7WsE3sUQSAmFIpXH-TFb9ml2gRyi9k61Hb2s6qvSmg-ckfPcPOeNPUfUN0w9zHn6QJUIUY2kCbxx8V-IMuG-NjccGdhUNukUCSD-mCuDOYrjE~bArF~2pbrwywfMxiWbMR7pj4OiHA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Add a new row for each candidate.

5.  Enter values for the required and optional fields listed below.

    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <tbody>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Field name</strong></p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p><strong>Description</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Required/Optional</strong></p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Title</strong></p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Title of the interview invite email.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Requisition ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Job or requisition identifier from your ATS. This value helps you associate the interview with a specific role.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Unique candidate identifier from your ATS. This value helps you track results back to the correct candidate record.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate email</strong></p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Email address of the candidate who receives the interview invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Send email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Determines whether HackerRank sends the interview invite email to the candidate. Select this checkbox to send the invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Test Result URL</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1" data-colwidth="365" style="width: 365px"><p>Webhook URL that HackerRank uses to send interview results to Zapier. Paste the webhook URL generated in <strong>Step 1</strong>.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    </tbody>
    </table>

<!-- -->

1.  Click **Send pending records**.

    ![13.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769497983631-13.png?Expires=253370764800&Signature=DMBmidjruHbHK4b78G2P3do6B9QZEN8DL8s31yC1EujHbXjhdCeQCOYlbyduCC-TXb5KkK~1FalhDXQCc1DjWdQkS9z4rT5GvSXRXxB33iwodyH0BO1sxia8JjbctpEUSN08XD-qokJgGfDLmQvA8gD8rqEtDsXcVh7hl7iBdZxYrUMDCD53yeyIzIw28QbvC9fIlekSZSVHh5ggK3XtzMOqgm9WofQ5MKxdaRR7fZzJCc1kHAvzFEMdc0HeV3ozF6nfSqfDJBCfgqa7rqqfMwTXaNQlhfCZlmmvmnAy77c72rkahFzrMT9UlKzfAduFcmqPWItNKMKz30QnX8s3gw__&Key-Pair-Id=K3NV4LZ47N8M46)

Zapier sends HackerRank interview invites to candidates based on the data you enter.

# Viewing interview results

When a candidate completes an interview, the results are automatically added to the **Interview results** table.

To view results:

1.  Go to **Assets \> Tables**.

2.  Open the **Interview results** table.

You can now review all candidate submissions from this centralized location.

\
