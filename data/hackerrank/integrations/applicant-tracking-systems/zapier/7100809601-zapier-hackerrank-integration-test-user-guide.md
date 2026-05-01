---
title: "Zapier - HackerRank Integration Test User Guide Prerequisites Configuring Zaps for HackerRank assessments Sending assessment invites Viewing assessment results"
title_slug: "zapier-hackerrank-integration-test-user-guide-prerequisites-configuring-zaps-for-hackerrank-assessments-sending-assessment-invites-viewing-assessment-results"
source_url: "https://support.hackerrank.com/articles/7100809601-zapier-hackerrank-integration-test-user-guide"
article_slug: "7100809601-zapier-hackerrank-integration-test-user-guide"
last_updated_exact: "Mar 28, 2026, 3:35 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Zapier"
---

# Zapier - HackerRank Integration Test User Guide Prerequisites Configuring Zaps for HackerRank assessments Sending assessment invites Viewing assessment results

_Last updated: Mar 28, 2026, 3:35 PM (Last updated 1 month ago)_

You can use Zapier to automate HackerRank assessment workflows. This guide explains how to configure Zapier Tables and Zaps to:

- Send HackerRank assessment invites to candidates.

- Receive and store assessment results.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- You have active HackerRank and Zapier accounts.

- The HackerRank integration with Zapier is complete. For more information, see [📄 Zapier - HackerRank Integration Guide](/articles/9883166979).

# Configuring Zaps for HackerRank assessments 

A Zap is an automated workflow that connects two or more applications to perform tasks without manual intervention.

You must configure Zaps to automate the following HackerRank assessment workflows:

- Send assessment invites to candidates

- Receive and store assessment results

**Important Note:** This guide uses **Zapier Tables** to demonstrate how to configure and test Zap workflows. Zapier also supports many other apps as data sources or destinations, including spreadsheets and collaboration tools. You can replace Zapier Tables with any compatible Zapier-supported app based on your integration needs.

**Step 1: Generate a webhook URL to receive assessment results**

This step is used only to generate a webhook URL that HackerRank uses to send assessment results.

1.  Log in to your Zapier account using your credentials.

2.  Select **Create \>** **Zap**.

    ![5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769506927314-5.png?Expires=253370764800&Signature=YCU-AqzHnTSWzEiJoQC7uBbhgteM73dITurPvClfjTM16RE53uZwvEpfBztAViAmfTmxKhzKlSR1TPIg0qQDv3zPDo9DKABs5QMic46t~iI527enrt96Y~7kqsUQxWZ6orX-vKj6vDDvsAUa1pC7-zG1APiVZxmZLpM7hdO1A7KJkXHUk2Bwzw870ejnOH3U0QKndJi5vWa458XbocaMpsnIntafwKXKKR2bilsAenYWrh3I1AqKrWPTw7A2GqfHRYyl9W77aQF9PhZtcc6fMUeIKN6hCEvfyKqYIwpkYK~9dP4ytSQ1~GjHWPXWV2KTHgDLKI8OmpxKST~gPg-kPw__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Rename the Zap:

    1.  Select **Untitled Zap** at the top.

    2.  Select **Rename**.

    3.  Enter **Assessment results**.

        ![6.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769506994420-6.png?Expires=253370764800&Signature=rKiv7f0r65jLBOese4X8ugDrltA~bz61DnyppBatG99WmvjtlPibUZfmexFdXYxfzQHpBuHYa8qsWSSOivjpFkZXNHO6BL-cI5gKx4efdtCihVUNS8pGBNbhXZ9AckPF6z~mgebqHnUBerU3uC2to1Lx8FiQMxi9~OJ4Ev5-Q6i5h0gBQjBe2zN6piZm0jj~apxPeCpAEowQXyyNdjD9qT97FhCrQNLXMbtA2jgxQh4vLi4Q-ZI8tMT-Xh295TlhuIbLA3lM3KON1eQ2PXDzCIh9xVrT~59a-elNQGZZr8BQaGegSbyQ84oKUD4Bv1EG3yb-2q4XaQKYEfJQ5vExqg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  In the **Trigger** step, select **Custom \> Webhooks.**

    ![10.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507046687-10.png?Expires=253370764800&Signature=OK83qzUFlX6ibI7DedPvpyVS-WNUzFTjnm7fpXVnB1EsAzZV5fabD9azF4pfnWR-tzgEBu7AhcODjzEDNeaT7NsKnhLWS0ALY78yPsVYhVH6e9LRrBiAjzUnAV7n3~LKalM~kdcZed~jGbnjEfxbdpmNad0wvFOUwIAum-ONPVrc~QkVp1QskkllWUL~joVpVFmozIENK~mEe7ZpEmHBCpkE9Bg3ZMTK20Zv~a0lXpWiYhE1fGaYcrXyhA5AkzM0VwVyEZne2gchaPly4Buj9WqWj10hGwFxsEJ--bXUNFmXJ5AtnfzgXTUKd2MbKDINOSEb8tdlE8tTXKvOeW8Xyw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Select **Catch Hook** as the Trigger event.

    ![11.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507076075-11.png?Expires=253370764800&Signature=sPFqHieD1EVfD7bJAJrk2O53h-huHEwbcKgYZPoSzGO7GsI9hcGa4AbPwdTE93BtxluNF-PJlDa7JVgLh4AjopUFCY4TY9Xd3yNPpWvgnsFdkbPqI2aEHDdYCKGenZGdK7gdvapA0ATzXxgl05TNCGjcUL8qKjiFCAd3hHNO9~SB4OTqU~YeyXoVerjrfjJH8AxlRSahZyTIGERj9FvrOB0XTP99xqFaRzs~bNdRUZLtiHLlQ4~ZHc3mGIEZnIyu211sUNqBmJVA3wMwqEZ~CWoMiu8pYYSiH-tFK0yLCkzH4wUixPg0bMeiQ851d9~zxgaY~S1g91t6CtPo~-6YTA__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Click **Continue**.

7.  In the **Configure** section:

    1.  (Optional) Enter **Pick off a Child Key** if you want to capture a specific line item.

    2.  Click **Continue**.

8.  In the **Test** section, click **Copy** to copy the webhook URL to your clipboard.

    ![12.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507245829-12.png?Expires=253370764800&Signature=HYGSlwMvk3LhEIJ5aPozJ5SVz~5QB6Z3WHl8xVPQd6ccmFqSnSsydbpw4YH5BiJQHx54jfONyHZ4PjXSeg85p0gTdmcwozRO1lwfi3KMlSjQB8TuzjBdDefFhijA5tyek8m6VyqRa602tfQS21nXnp8DDrNrY~U7qPuSOBcu-SV4hH7jRipvZgTTg90Xm-RVrlxXeLVbfpzhdP1-NnaAv2H35si434ppUUUr1BWcENYbyMHSK95YNyEcHkMG0mUUil1F~ko4ngZ86h1r55PdqSUvnDUFWgRXRvPJ5gVq8zmsfbQxq9lwHMB627W3s45x255ZJJ2kSYiz~E~V4Oyp9w__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: You need this Webhook URL in **Step 2: Create a table to trigger assessment invites**.

**Step 2: Create a table to trigger assessment invites**

Create a table that Zapier uses to send HackerRank assessment invites.

1.  Go to **Assets \>** **Tables**.

2.  Click **Create.**

    ![7.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507302412-7.png?Expires=253370764800&Signature=QI6zA7bPNSiu-AyAN4SpVEMPEzolrhAC7bQ1mxykxwaAJeD5-grHFIb55871Nk45VWmaJIekDZaASh5rdneEnaylQQ44ZNkjxg6XS7aRF2OAriX-4lZ1PEKUsUp5XgHphZDO~4o032Le~ZU~tdSTZDcQecUSKD~QAF-vaXzXxTjqN5VmyTduHOXKj-1FrY37HihiiKAJCPYEC3EExl2CqGCV5kv2zBI4PiVc3nBtg6PpYNxQp0qEJH2puJPyVQECmHZwlOhvibkS~fxwx4mrQVRVLyMX3id0s6U7zc2IhVo5Zzo3lXmEKwADbiipeoq7~RbkFieghh2h26OKY50Wxw__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select **Blank table**.

    ![8.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507323947-8.png?Expires=253370764800&Signature=WTy67E1PadbrONaJiRVYYcb8lWtdZkCWvBFEQ23LbZBDLJNC8t3ljcBw8u4zegZiTgVHLTr0med1-K5bfTxlmbww6Q-jWnDAK1uqCmSK98~b2vT9vpM8lduhclnuF3SurbZPgnSxXf~KQwwhj3xCu5qwMicXP-ckLGnCrilQS4Us49hp~AXUokIE3GTXScSS-GmvZuWGbD3GgQEmIQMAKb~RqEV2vsSLU~525l7AVlcc6PPm8j1i7rdSG4e14vdeppfoqbQqxwEn1K-Fc7HYBFH7EgP7bv7Vg5zr0bg~soQX7NGClwee36SFjZbHbGdWyn87VBSt3~Heh0ID9XrgVw__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note:** If you already have data, select **Import data** to upload a CSV file or import data from another platform, or select **Use a template** to start from an existing template.

4.  In the **Create a new table** dialog:

    ![9.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507355765-9.png?Expires=253370764800&Signature=fClKaF~U-AMQoIcm8adcGztg9YEHMXvdVn8rpYPYFuIg9pmtYzuwumORj5hcZm6OgNPjoKFA~GDtF6peJIFSXoQ4xqIJb9vz9Z0EzaR8HprwlCSE9~3cqE4TF8aSNg0netS3u~u1DxoN21Oq8svPDijnZVsdB23ABLwX9YppFP5aP720oy7R7cfE9heNGAg7ev1TybMlGOp0~PAy~7H9~dA25s9vx930wNXt20dq7mX1RFqS0iR4gzTSn~fkjKUXq5tEgyul4qRXTfinu8d6-sNY~8Bk50SpruXss~KEMjCjo7SCxLRcyt6BbFzhGSnUN9m3I9OMX7FpCAAU2KLUlg__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter **Assessment invite** as the table name.

    2.  (Optional) Add a description.

    3.  Click **Create table.**

5.  Click **Add fields** and add the required and optional fields listed in the following table. Select the appropriate field type for each field.

    ![15.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507403578-15.png?Expires=253370764800&Signature=Amt9oeM1M8Gb~M85fPJ0h59X2HhF6p54p3ZeCaG1aXfcjLgTCgcDz8aJo2XP7ZQq1GbaeFCwWQ-srvQN2ClnIGvCH990tAaYteJMofLoBZfK6W3~hOJvjduiLGsxaq~Yy2Aj~hPMeypxoo-~RKcyb~FMSKqb5HkMkNxvLFtwD0gZpaCCNroWyHWEOjk4kspilFA9zqdhcnHG25RC72~jm3ZriWig3xpftuyFaS2Grz153Swqut3MWY12-oe5tNqTQnRKjKHwveczPe27Poo3rYxAUq2PS-4jPG4kWMMdHZJuqD-IZYoPHC3EOx455LrJYKEu-yjPvEd4oOEIyKCgTw__&Key-Pair-Id=K3NV4LZ47N8M46)

    <table>
    <colgroup>
    <col style="width: 25%" />
    <col style="width: 25%" />
    <col style="width: 25%" />
    <col style="width: 25%" />
    </colgroup>
    <tbody>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Field name</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Type</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Description</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Required/Optional</strong></p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Test ID</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Unique identifier of the HackerRank assessment.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Email address of the candidate who receives the assessment invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate full name</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Full name of the candidate receiving the assessment invite</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Requisition ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Job or requisition identifier from your ATS. This value helps you associate the assessment with a specific role.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Unique candidate identifier from your ATS. This value helps you track results back to the correct candidate record.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Send email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Checkbox</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Determines whether HackerRank sends the assessment invite email to the candidate. Select this checkbox to send the invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Test Result URL</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Text</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Webhook URL that HackerRank uses to send assessment results to Zapier. Paste the webhook URL generated in <strong>Step 1</strong>.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Accept result updates</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Checkbox</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Allows HackerRank to send updates if the assessment result changes after initial submission.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Force</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Checkbox</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Forces the assessment invite even if the candidate already exists or has a previous invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Force reattempt</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Checkbox</p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Forces the candidate to reattempt the assessment, even if they have already completed it.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    </tbody>
    </table>

6.  Enter sample values in all required fields. You will be using these values to test the configuration in the next steps.

    ![16.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769507449284-16.png?Expires=253370764800&Signature=WgVcWGMtSxqTX5e28pO~9GhWZ8gA8EkysxHd0qBf6K8ePLoXyO~97Xw6pQCHc3A5tyFTQfeHWpb2rc1-4e7IxmRL~W0nZzez-OkmA3B5jEW9IW7ZgiC7fUkLx9XP-4W6X52igqGfcEa~FgLkXgf61N5KAKkUNCtj4X8AYWqJCvi9NlUoFC-5dWOZbbg8NkY43wsuiw7q-Q7Rez7AE87CslyRHF-p02Re2BnQ~ADtRQ97v49II9TfUpWe4hPwzXLSID~JVYKk~mU~MiCDmrcsUruMMr-EjOJ9eBfJ5FHfJjmkklGySllLpSb-vbTpxjGxBYIoZuTwYf6TNQ6BjXEaOw__&Key-Pair-Id=K3NV4LZ47N8M46)

**Step 3: Create a Zap to send assessment invites**

This Zap connects the **Assessment invites** table to HackerRank.

1.  Select **Create** \> **Zap**.

2.  Rename the Zap:

    1.  Select **Untitled Zap** at the top.

    2.  Select **Rename**.

    3.  Enter **Assessment invites**.

3.  In the **Trigger** step, select **Products \> Tables.**

    ![13.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508259846-13.png?Expires=253370764800&Signature=om6sCOXcEYUkFSNVc9NVIMcSfLEjdb9H0-I6B0deCdLElqOFTdm81rFsOcIKYMvGojFw~-zVXZR2~Sfl7zoRq0JkbM~xBsAIqIMjCEazkVcFcolaMV6NB4A0IxaYrZ2SWXKBpDJEt9M4GPd0Lh8HIU~7pxAPn8XAHI0-11-idTRVB7Khlrhhqg31e-j3N-PomUJSS3FqOmeRVlooNun9cF2bUJQArdHNlaHcCUVjP3TBo7kZ~jKN56m2jMUDozbVKyhMh5204eWRUx-WeEIbepi~50bL9n~qTyCzOVz-d3GKCaNKsFJSN9Mq8muACWiegCaye-Ulxc5FGHlwGtIrdg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **New or Updated Record** as the Trigger event.

    ![14.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508431609-14.png?Expires=253370764800&Signature=NcOcdEMo4~XUfeXHheapXDfKyENNr2rG5AcbCHTu86lljynLSoajJ3CUKmkQxYZ0DvmExmbOEt6TNlFUomrPDbdZ~VnzOt1b~Jllj-FNHLX0S-XGZX8Aqy3yMcsScvKGTgChCaF5uKSzQaJhFJXHsxLSlTjqG3OCLnNKX2S7Nxu0wYu3lMhtj5BEh14lcRxwYiDibqdUEL-uOJMtksP6Efcb8JT4nSdN4NEO2Ec7Td17n3GRSSkF~1tzqCEBHSASCsaAsVHDFwDTrJ2veJUdfrkkoDgQjoHpqeYwuoy7KJs-xCHbP~RRwLUUyRkF~UageNplXfDn52GXJeVhTyC-tg__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Continue**.

6.  In the **Configure** section:

    ![17.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508456475-17.png?Expires=253370764800&Signature=ZwzxmKcx2wiFffSm2oTMogmi7UmkjtTmUlA9VN~S1T-O8c1TvHisB-aGtFGOd59EohkTw3zGviEbn7-NAp4CGa4ZuDljc2~4KtXUTSwAdTj8CW3UVbKf4~P8mfnK5yOw8KKxf9uoPXqF8RjwVWWF8F4ViEoE4eeQq-B3cyRQTdbNo7F42Iq3gazGmeQj0jXhMRTCYnhJHUDDPQ4M-hGHxthZnPUB6j-7PyAp3PtX1UMoUZMwstzjqUg7y7Q-er6iFk~-RFJwTo4AjHuSLEOxaqwgSExALHYzyfzfBcmCLd2e53bsTg-RT8BbPeHgg1R2tU-fgOqtG~P8wXy69UtUaw__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select the **Assessment invite** table created in Step 2 from the **Table ID** drop-down.

    2.  Click **Continue**.

7.  In the **Test** section, click **Test Trigger**.

8.  Select a record that contains assessment data.

    ![19.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508487869-19.png?Expires=253370764800&Signature=VfthfkN7M3klxsA6KvVgaxcAqG9zQyWzbds6Mn~4kwHe-FywO0Cl5-GkoIq0olF6hEktpQC8z8ZNqnOiUy0rDgfLy-BlZtpuaylTNV-0SHvX2cG5YH4aFP2tjVnDbtmjQxEgmGLdjhmZZFAce~wD-YatphkICaBNKe9UZVaSWP-Jstl3SQbzE42MmX45JhmtjqYT7t1tAL4~dQtXFT3Oke1IEEPKUss6TjYaxDg3B~fdHj2UtwYeKOUPK8zICmXbjz2fkJFIMDlgsO0YJXpB5y-IhUXcQajHLIyhd-SrSi5bQQQEXXrUWA2ckctqxF~PH7~itqgZWc0KeG7~S8lHIw__&Key-Pair-Id=K3NV4LZ47N8M46)

9.  Click **Continue with selected record**. 

10. In the **Action** step:

    ![18.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508527340-18.png?Expires=253370764800&Signature=P04t6FpPP8txMJiT9FDGIP31yeCeSDosVZIzo0NrGU~~KCyEaYCw0bqb9zQ9sfhxrPV4RrkNRN1CRyZi7EoFCAhITbpHNwQ3voLJK3Fq3G7wUsgaBnh3gl9XUP6RvELySjeO78X23Fgr0aP-vwzctLvU7K6rSG9aM7zcaxPUQmDWrZKEY7PPPrwlEgJN737L~wt8FT-WxOG1tr~LLx~olQ9eu4gHsV-NypeFHqSsTEvUsHNY7efHcrnOX7Rtlf4sEF5k1PL1L1v41qBAo2fKTT8TUeIT9NNdxJ9ATGbGBO2BWXak4-sApuOa0LGlVsfNejAPyd-o4egwSfrIZELJPg__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select **HackerRank**.

    2.  Select **Send Assessment** as the Action event.

    3.  Click **Continue**.

11. In the **Configure** section:

    ![20.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508549239-20.png?Expires=253370764800&Signature=mcPyFoIMKIupcpykdmT-APoqhRmk~0qLxcu2phLJtbLcvR1X0pYB~1UNERqGmtX4cJl8DFz8VZDNzGa3vcRyjLiGPNfUd9pOSOMExQUI0jbbfWJfzWEMmQbF-znYfLHRh3rQZSxMwtmFeRU~iPYXe5RChaywC2DkFaDmehC7xxCD1XLXd5VZq3~orHN8aUGa6RqdXeJ-fzke-6ooY8aecT033WL6zCYlpFXN1kuHLJaXa8szFvr6qah7oYSlVtyVNFE4qjinr176jMaW6D1a11OmMKgeWYgZgdNvKx0JEQoFVPuzeSrvn06EXzJSkevC6zlvFSVOv-GwXX6j3jRa-A__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Map each table field to the corresponding Zapier field. Use the forward slash (/) to select values from the table columns. 

        - For example, map **Test ID** to the **Test ID** column from the table. For checkbox fields (for example, **Send email**), select **Yes** or **No**.

    2.  Click **Continue.**

12. In the **Test** section, click **Test step** to send a HackerRank assessment invite using the sample data you added in the **Assessment invite** table in Step 2. Verify that the candidate email address receives the email.

13. Click **Publish**.

**Step 4: Create a table to store assessment results**

Create a table to store candidate assessment results sent from HackerRank.

1.  Go to **Assets \>** **Tables**.

2.  Click **Create.** 

3.  Select **Blank table**.

    **Note:** If you already have data, select **Import data** to upload a CSV file or import data from another platform, or select **Use a template** to start from an existing template.

4.  In the **Create a new table** dialog:

    1.  Enter **Assessment results** as the table name.

    2.  (Optional) Add a description.

    3.  Click **Create table.**

5.  Click **Add fields** and add the fields you want to store from the HackerRank assessment report (for example, candidate name, score, or test status). Refer to the HackerRank [sample assessment report](https://drive.google.com/file/d/1jIZzpQhe_NnzJcy7YoW7Jg1BTz18p_q_/view?usp=sharing) to identify the available result fields. Select the appropriate field type for each field (for example, Text, Number, or Checkbox).

**Note:** Zapier Table is one option to store assessment results from HackerRank. You can also store results in apps such as Google Sheets or Slack, depending on your workflow needs.

**Step 5: Complete a sample HackerRank assessment**

Complete a sample assessment to test the Zap configuration.

1.  Open the assessment invite email sent to the email address you entered as sample data in the **Assessment invites** table.

2.  Submit the assessment.

After you submit the assessment, HackerRank sends the assessment results to Zapier for testing.

**Step 6: Complete Zap configuration to receive assessment results**

Complete the Zap created in **Step 1** to store assessment results from HackerRank.

1.  Open the **Assessment results** Zap created in Step 1.

2.  In the **Trigger** step, go to the **Test** section and click **Test trigger**.

    ![21.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508646004-21.png?Expires=253370764800&Signature=LBflA7S7XLyRyjCQZOADKpSWWuemjKkRGla1JTIwqXgBvYtthubWXouxdW~jlLnBjNReOSeev68Z0aPKr4XkFkRtvlrwU4na4ehbXOX03GGPXfTdK6edYkSoTTJSEmvpS2OfIkyudwHVSEXmJza3b6xW-Z1r46R9-1Zuroz46f1TzQ2Fz6gyUOlPnz-etrn5v7iqklp91j2DS3wkT87aDP-2q9JrrbHpJXmBy3Ed5jdA3fsmM985y4fAI3afsICfSioopB8eZ8xlzHDt913CVQj1YzcQkY5zcJuHUrggZz7wGO3MP7YsfIp8oImME9K9PQyqjYvnFoHr5fCqobLqJA__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Select a record that contains assessment results of your sample data.

    ![22.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508674042-22.png?Expires=253370764800&Signature=TlfFLYixq5uTVjODB7PBTYRjXIQ29avfwagemd0iuh08jtjXnnytGTAAJWcIixuNf7TstTiOT-M9HdmJWNEMCWIXUwdISmD2WI213dPtmd1a2mqKpSBdHQtgNyQZTaxSwByFoYJD3y~YiAhknzJK8~75lQE7JkWGkab53lrTxP5ChIp8bwS~M5TJqUI7fZd4dF8RyVrPCIt6dVwhvVA3bxvKjvH5HRYHmypx6IdUx5Z52Wl5zQ3vFUL2WiCxFcu-NpCEwMen1EXijF1WQjWZvTArlNdoPDSq9MnceshFaO0weyEhQ6rbicR35daZglKOB91PEwTBzhbRgp1ReSRC3g__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Click **Continue with selected record**.

5.  In the **Action** step:

    ![24.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508799424-24.png?Expires=253370764800&Signature=Js3tkA4D5wLSGgohKeEJj1j83XonWJH9nfoUdBWOZNuduKU6XYXdLFupt9--25IEXJEfADSKpeE~wNtJV26JRSy~CtDVHni48y5Ke4g9tWciQJvl15KtQ1K~~JEBeyh0j3L51yebzjJnmLagNi0Iv1H9wGIJ2qMTNQK4rzwhvkBXoLKxlM0ZLGcl-yd53ljCifRTq~Xqy46ezfClwLVxCtb7kNuOB8mSJ7p8Rn-1-nNxB-K26sBAD8GAQjeQqLFD3zB0nNoBvOuvT1mb~GUOuTbQHZ6gt8vy21ISU7k6wlvHC6pFvHluAnHZnlYU4tSUYmNpGL-QdbdR1bshXchcuQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select **Products \> Tables.**

    2.  Select **Create Record** as the Action event.

    3.  Click **Continue**.

6.  In the **Configure** section:

    ![23.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508843397-23.png?Expires=253370764800&Signature=KBFVl0mV5ANaTgV71jMaieWqHT7sJ4nell5nJmqH6SQ3Yhw9jMP-SAuYHi2XJ-NgQq~l9qlKuHClK9sketdQaW30Lt53mzrFhcLIC14WZr62ZrFe-m7TZuTpq4UTQ291nIrRIU-W1Eo13A6FN5CktcdTkbmLMaaFpTxLRK1CDw962bKOBJCSFthgjc6zpLGn8gGx-BM6cIWsn72DJgmehsEPxTQWXVnxFRyWLaGCUC0niqDNLyPFOk0kaPJ5EUZBpP4rqxWEZzSR4ATEIc5BBZ1~FG6Bhs5t4SvWip~ZnehE49qeIBfe2GNLo3c2qhpJdRN00cL2uBITMaDtoDEnQA__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Select the **Assessment results** table created in Step 2 from the **Table ID** drop-down.

    2.  Map each table field to the corresponding Zapier field. Use the forward slash (/) to select values from the table columns. 

        - For example, map **Test ID** to the **Test ID** column from the table. 

    3.  Click **Continue**.

7.  In the **Test** section, click **Test step** to verify that HackerRank sends the assessment results to the **Assessment results** table created in Step 4.

8.  Click **Publish**.

Your HackerRank assessment Zap automation is now complete.

# Sending assessment invites

After you have configured the Zaps for HackerRank assessment, you can send assessment invites to candidates.

To send assessment invites to candidates:

1.  Log in to your Zapier account using your credentials.

2.  Go to **Assets** **\>** **Tables**.

3.  Open the **Assessment invites** table.

    ![25.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508900999-25.png?Expires=253370764800&Signature=Mat~NU-1ChWlxS22DP4MtPCbEEawD2sGRVcte1qSglF1nFM8TBj40L6blm38Yj~ngWdJ8ORbi7tePRr90cuXztD32NtJTKW1Ye2rBU5ydgm7G3GiFm2KGrm34mX55Pt~BVclymTgJABOuQQjGzMd-cmE1xZgp3BWJvSSjZg7PpOjoMitNZQKMn2o6F8NKIQUD~ivbLkGUFlcH2w5L6xd4hYuZauPvV0aeObYXMcpymF5gBhhrfXnuksQe9oYA7cONEdHQ1LBrwOwseCDYKBAZT~fBTxUwG8MQ-w2BIh37yve0oxoMVW6dhmzA70mp43KzNjhMikNqqiz3WrIkd42WA__&Key-Pair-Id=K3NV4LZ47N8M46)

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
    <td data-colspan="1" data-rowspan="1"><p><strong>Field name</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Description</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p><strong>Required/Optional</strong></p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Test ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Unique identifier of the HackerRank assessment.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate email</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p>Email address of the candidate who receives the assessment invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate full name</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p>Full name of the candidate who receives the assessment invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Requisition ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Job or requisition identifier from your ATS. This value helps you associate the assessment with a specific role.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Candidate ID</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Unique candidate identifier from your ATS. This value helps you track results back to the correct candidate record.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Send email</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Determines whether HackerRank sends the assessment invite email to the candidate. Select this checkbox to send the invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Test Result URL</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Webhook URL that HackerRank uses to send assessment results to Zapier. Paste the webhook URL generated in <strong>Step 1</strong>.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Required</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Accept result updates</strong></p></td>
    <td data-colspan="1" data-rowspan="1"><p>Allows HackerRank to send updates if the assessment result changes after initial submission.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Force</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Forces the assessment invite even if the candidate already exists or has a previous invite.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    <tr>
    <td data-colspan="1" data-rowspan="1"><p><strong>Force reattempt</strong></p>
    <p><br />
    </p></td>
    <td data-colspan="1" data-rowspan="1"><p>Forces the candidate to reattempt the assessment, even if they have already completed it.</p></td>
    <td data-colspan="1" data-rowspan="1"><p>Optional</p>
    <p><br />
    </p></td>
    </tr>
    </tbody>
    </table>

6.  Click **Send pending records**.

    ![26.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1769508938856-26.png?Expires=253370764800&Signature=eNF7futjWMYFk-faKKv-5I2TECkcNkW8k6DiJ5ybqMGZxGPpdmyQdK6eJmfypiTJMCohREb1bPfmqIxSQfLb6U5hPo4F1G~iVfAj0hVFAlkTj0~oqcRyffcrEeXQq3NsTTNTolUpsS6J-rqNfjZMjDcezdHz1a-ZfoD-7zMIoVLh4TdNNi3A66Krnu3GnWjAGqJUMC4HHhF6UoouC6FYuc1XSgN3hwdiubA~nvLydFsB6oiJ3Juj68uY36wnUPZh1IB8oUVy3yk1vEQb4m7FLQHbma2BdBjAWJxt0xuijX13MM90DCmsypkURSAcEhQxySo8F624uzlX2oABF5JcMA__&Key-Pair-Id=K3NV4LZ47N8M46)

Zapier sends HackerRank assessment invites to candidates based on the on the data you enter.

# Viewing assessment results

When a candidate completes an assessment, the results are automatically added to the **Assessment results** table.

To view results:

1.  Go to **Assets \> Tables**.

2.  Open the **Assessment results** table.

You can now review all candidate submissions from this centralized location.
