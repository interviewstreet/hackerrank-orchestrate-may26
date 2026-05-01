---
title: "Ashby - HackerRank Integration Configuration Guide"
title_slug: "ashby-hackerrank-integration-configuration-guide"
source_url: "https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide"
article_slug: "4146164514-ashby---hackerrank-integration-configuration-guide"
last_updated_exact: "Mar 11, 2026, 3:54 PM"
last_updated_relative: "Last updated 2 months ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Ashby"
---

# Ashby - HackerRank Integration Configuration Guide

_Last updated: Mar 11, 2026, 3:54 PM (Last updated 2 months ago)_

## Overview

HackerRank's Tests integrate with Ashby to facilitate a seamless and efficient candidate screening process for recruiters. As part of their interview workflow, Ashby users can directly send HackerRank Test invites to candidates and obtain the Test report for further evaluation.

This article provides you with detailed configuration steps on HackerRank and Ashby.

- [Prerequisites](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#prerequisites-4)

- [Configuring Ashby Integration with HackerRank](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#configuring-ashby-integration-with-hackerrank-6)

  - [Generating an API Key from HackerRank](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#generating-an-api-key-from-hackerrank-8)

  - [Adding the API Key in Ashby](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#adding-the-api-key-in-ashby-11)

### Prerequisites

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 436px"><p><strong>In HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 447.139px"><p><strong>In Ashby</strong><br />
<br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 436px"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must have an activated <strong>Recruiter-type</strong> user account with <strong>Company Admin</strong> permissions.</p></li>
<li><p>Log in with this user account.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 447.139px"><ul>
<li><p>Log in using the Ashby account, which has the same email address as the <strong>HackerRank for Work Company Admin</strong> user account. This is important for sending HackerRank Test invites from Ashby.</p></li>
</ul>
<p><em>Example: If the email address in HackerRank for Work is </em>[jackpeters@hackerrank.com,](mailto:jackpeters@hackerrank.com,) <em>the Ashby user account must also include the same email address.</em></p>
<ul>
<li><p>You must have relevant administrative permissions to the <strong>Integrations</strong> page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Configuring Ashby Integration with HackerRank

When configuring the Ashby integration with HackerRank for the first time, the administrator generates an API key. The administrator must keep a record of this API key for further use.

### **Generating an API Key from HackerRank**

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046525251-?Expires=253370764800&Signature=WqmxEZDJxF39BupXQQvM942M4302oiduF9nap8NiqJpr8QJNJyB5ERAFFD9hxDyOlHWNGjmtUxxGwVamGGD-W6F~DWanc56eLwrteKQQlz5azXjL3VfpAIq-R6DxI9HBiuCtTUGx68YuAICKjcnrVmbgtVf4w94fRdr9Up5aweTC~HfM2jYLqBPq2XcxPmBUFaF9MfbgfI3JH3dY4533ORrQmCrURyuvnxZWDPmbA~A0b5gXq~MtLH0LZrVJ9e-70hAE~o7fNjECBAcF1ocZl-rwgt5wCJjgD8buxf7uJuvCor9MK~BPiSTKHyVOAuc6amC15zm-wwwdODVNMZxx4w__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **Ashby** option. You can also search the Integration from the Search bar.

    ![integ_ashby.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046525752-?Expires=253370764800&Signature=qvcaMj3Mb5gnnAt6~yb4MU2ojbqbYjbJ-~m3HZ4B4wC1hj0Kz1ee6UxPu4Lidwy63mX9h-l9VL1nSqCt7RL922WlXP9zJnGoaWGzfOuIIYeo5rsuOmynp9gZ9nJMJ3HOU0yIUd019eSfwth6jmnaxAcPfsJWG67qIxSIOI6aAmv1YNBFr2l6tB~NQ6WtsETIcAKnJ82iq5M3a-ywbX2R~SK6QYgrPa6p5MjDIbqyGR7NJusjVI2J63dpAD9FXucMPKGgm3xytMJcpUugebZrD9f4jvpApuKOqk~~ZPjWbFdq5t~61QgY5lh7KyhOQKoo1xSMfLG-avNNz6pr~cD2hw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Generate API Token** to generate the API token.

    ![integ_ashby1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046526111-?Expires=253370764800&Signature=YCVzHm6TDmZ2ov7U-xVl5zmGMXlt2NdbRYwO0-Ztb2cGA25CRIuqdcM1EVr4w-8Da-eNXixmHYG-x36vzM826ZHuAeMrg2f8TQIuykKtcuotnorfXDXYULCLlRexeRtNNlARSJkQTBLwMtCrggT~fvr6TL7PiLMff19K~w59L~7ZDgVXbg~pzRPTwHALyvtqCTNHe6c-yE8IxP4BaIECvxieHgfOnLxLO6ahxNyMVrgdLVULG8Q~ndDP~fpZF0Kv4rRCQL-YgUq2yrQlQh0BNAGawjEdxmwZawM48iZ9kmYV3F2z1QSox9vuC98HUOe49DJq6LdMD12ZarRdWf8uVg__&Key-Pair-Id=K3NV4LZ47N8M46)

    A unique API Key is displayed.

    ![api_token.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046526481-?Expires=253370764800&Signature=RAR~K66xfg3UGGiKPJsV4S6WHwxUaYoOZv~-a3qtcYMJ4envUhGNUKGQwql2jSHWeCpLsRSTW1ng~iNWhYlD0TutUsQVYOu-2JqGnT9Qc5k2IYMOgIE29SJG7na6iqz-ojyrXGllJxuDlvVDqrU-Vjyb0GO5~0PdvMlgKGJ4wD9nv8Ci~CuZ2d2dRDdSL5g0wu1szwi9IMxUyjn-VyBAlv-DTk4SAZE~8uy3WaG5JRDeJxppmwfOMiioL0LC7RYq89Oui0yXI9uqmtfzUg93ThWuYJlQPW5H9bsl6phwYN4qFHlUGDt7RIQbbrAwI~5Zb1t1kfvEquFoSaR7IzVqiw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Copy this key. You will need to add this key to the Ashby account to establish the integration.

**Note**: Ensure to store the API key safely. Once the popup is closed, you cannot retrieve the key again.

### **Adding the API Key in Ashby**

1.  Log in to **Ashby,** and click **Integrations.**

    ![integration_hr.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046526847-?Expires=253370764800&Signature=Z6vgaRhtey6-FnDvP2tFxCd3p3fFBNhBbgm9PdFBFI46HO5~7B87CxEoMRSiBaIP2RIFkiEEPW7gNW8EJZJoqmSrEWVM7o9Bj79vDkq~wSXR8iyDgmR7UwhXtnYlkaibJq3miXlRWEvccPU5DyFfb0yD4m~XN16j~5S89W~sRQo-yCSZfw5Yy1j3tKW-bN0nUBytIQght-NPZ4kSjYy~Z0YH3hgM9gxJqCh8zqcvJkdj5Bh0a4-0m6IClG9xZ6ZeIZ2FV4qbf-0DY98QbTuyAI7trEStGJUFnkqB2eJs1W4P4cVY6ny0oeqHaNznBMQSkt-gjGHs1VFYm8redh113A__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Search and click the **HackerRank** tile.

3.  The HackerRank pane opens on the right. Click **Enable HackerRank**.

4.  Add the Ashby API key.

    ![hr_api.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046527180-?Expires=253370764800&Signature=AIM38dofl3WVdDwm5pn5IgLx3U8NWb5Y2kJCEI5q3iZF2H5XA~Vs8iqBniu6OwpMUgNRRFtbOFy9XD4yk1vDsA~AwIwvL98T34TSCAnX9ej0IGYq9Nki7g6rS7Xd1wysnUQxi-Mogn4X-SB6NgbRC4w9lYsxzQ~zi9QCriVnKt1OBPDNPrdJJujVNR6x~N-d4vcKpmTeaNFGU14qQqvhH69lpjmWa7BgeBeX2n19EvEs8keA8iq7NrPR~1Hlc9YZOrkj7DCZho3Lzll5S2HIwUO5gsu5QsdWJno7ojKRBFN~i7vCRjT0t-EFKgDReqmhKC84C-dG-HGpCqb7IQCM0w__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click the "**Test API Key**" icon to verify the API works correctly.

    ![test_api.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046527455-?Expires=253370764800&Signature=NcluNbGFzpVIcxO5xpWr-BxlMATjLjPrwj8oXFaz0EXXpMITQXq63QkMmD0l3Iwlinw7NiImLJW~YYuyJKihb0Rmp3LiwpBsH0G3pbNUe5EmVkv0WQZZdb4~EEhgIZmIAixMoNkLZIQTDEAeXzmEbtXA407Qq5GBCq4mqFfC0h9-hR~omv-MCT1ZB6UEzmcmp1SbnfkYNEpkp4ADmp1zfnpqF49BkDhAoHsAM9B9rBY~jNo4oOyhqE7NhwEyLgBviKe5bI8JYy-luP5IfqI0mtJrCKebQ3MTaKBe~Am6LMslN4fPdPA1IJbq4YwaanBoSCwxVd~QAU4zs5c9WbOsVw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Now add the HackerRank API key that you generated from the [HackerRank for Work platform](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#configuring-ashby-integration-with-hackerrank-6)[.](https://support.hackerrank.com/articles/4146164514-ashby---hackerrank-integration-configuration-guide#configuring-ashby-integration-with-hackerrank-6)

    ![hr_ashby_integration.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046527856-?Expires=253370764800&Signature=Ar5~s-N9kinL3J5V01vpCBIDlS7mi4kpwwoZplKXeAfQtF5Fs-V1fD6OqrSCxDuG3N1LLUv8Cjg4C2h-VSE-Cl4VvFwgC9PlSGY0TQd95Tt1v13PgwT7QZJ6L-mtaQ9d-9G4tyW-kh4M8tDVLtkpnuQjDKPNu3nisr1bCVR2ra3Yb98aWT2lZI~gle4L~k1qeZgwD12ED3qEONuz7hjah0-KZLwebAb6sHsgscW~7GYNnX2JTib1NXGDlXgAZeQ0dr3k-AA9z7c0CmUAxta~ow0tZB5ZIOOmBdUQVSh9De6PFaPO7DXahMP9tq0ucpe44gFYivKQkCZqsYNKYN1arA__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Select the integration partner as **HackerRank** from the drop-down.

    ![addapi_key.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046528389-?Expires=253370764800&Signature=fkxrZCHGPkK3ODFtgDdCD-1RzrbUAQ1ymjJjDnaiF5NeVOx~cCw9FX2JzlgfTyhTBQnv28ecd5ztwOKYCfIKuyO46nsEaG87IG9r2LUrsj-zMbFiqHXPTo~96qAiF8mkrG85SVqBBYauB3qiVSuGf8mRtYPpR0AkNFe8T-ElzIYkIGu6pZwoYTulBNGrO-imV5WPT5CuuhJqLmrV5dSPGMR~JGScD6R8LOy8Vf806Vd2S0tydalC-xA~WHHLNce6yxkeYi9fMLOjiPqa8v83ABbjjDYrp1QOV8FYa4Gzyu07fabv8jw8kevBEdmWwpQrj1NhlYlhmIZeWMQ58sv3sA__&Key-Pair-Id=K3NV4LZ47N8M46)

8.  Click **Create API Key**. The API key is created, and the integration is enabled.

9.  To check the integration, go to **Ashby API \> API Keys**. The integration with HackerRank is displayed as **Active**.

    ![active_integration.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046528845-?Expires=253370764800&Signature=XAGF8mfb~r-7W2I2BdJK~gAAA2DO61unRtRbPpXXE1c5ijgODSeGp3lzP57vzY9gJ78MnN5CC9AtYvjqElbHZ1wejUrm9tiNmrEXW72dn0K-A0gF9UtwTIYNVfUk8LGcxaeXN5PV~dDWKpOJ04VeJvO8OWu~FP54qoggmECA7O9tywyhaYpQ00y9Mc-JH9Tt8EvkXtLAI5G0dp4bNM9xdbUWd034n5XXoHYbuUpAJTAFE0eY4POIFuT0sqQ69uhj-OFy6IZPTIXabTKzbo6z3OD6cZLCW9JdAsY6hyn4yxk4Nineh6tN~BI0RcaAyHUPP4yqtsN74xjxILElmLZxeA__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** The email ID that you have used with your Ashby account should be the same as the email ID associated with your HackerRank account for the integration to work seamlessly.

Related Articles:

[📄 Ashby - HackerRank Integration User Guide](/articles/5999209869)

\
