---
title: "Lever - HackerRank Interview Integration Overview Lever - HackerRank Interview Integration"
title_slug: "lever-hackerrank-interview-integration-overview-lever-hackerrank-interview-integration"
source_url: "https://support.hackerrank.com/articles/8274807044-lever---hackerrank-interview-integration"
article_slug: "8274807044-lever---hackerrank-interview-integration"
last_updated_exact: "Dec 28, 2024, 4:06 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Lever"
---

# Lever - HackerRank Interview Integration Overview Lever - HackerRank Interview Integration

_Last updated: Dec 28, 2024, 4:06 AM (Last updated 1 year ago)_

# Overview

HackerRank Interviews integrates with Lever to facilitate a seamless hiring process for companies. The Interview is an efficient tool for recruiters and technical managers to conduct interactive coding interviews with candidates located remotely. The integration with interview allows Lever users to directly start or schedule coding interviews with their candidates.

This article provides you with detailed steps to integrate **Lever** with **HackerRank Interview**. To know how to use the integration and schedule interviews from Lever, see[📄 Scheduling HackerRank Interviews with Candidates in Lever](/articles/2634152447).

# Lever - HackerRank Interview Integration

## **Prerequisites**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 49.8571%"><p><strong>In HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 134.168%"><p><strong>In Lever</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 49.8571%"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must log in as a <strong>Company Admin</strong> user.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 134.168%"><ul>
<li><p>You must have a user account.</p></li>
<li><p>You must have relevant administrative permissions to the <strong>Integrations</strong> settings page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## **Steps**

Lever - HackerRank Interview integration is a two-step process that involves the following actions.

- Obtaining Webhook signing token and API key from Lever

- Obtaining webhook URL from HackerRank and connect it to Lever

### Obtaining the Webhook Signing Token from Lever 

1.  Log in to **Lever, **click on the **Settings** option.

    ![lever_setting.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047105067-?Expires=253370764800&Signature=X1cCulKciFd2NS6vl5HzsqZUe60rpmT8MSYZ7SfPXYuhR6zlaLSZ9IVCL31zbIACCRRjoO~zNtb-VGMhLdSo8oo1Ii~usE9QiH4GY~ni3OZO9m7rRqlDolwHc8i3H2yNfDl9LRRFS8mfRY~7WY9lhQ6RXAdTzNZnXp0oKAbFLsHgn7HwOabAugugwIQ3Z6OI~hYNfSx9B67DQ6668nZiaigESoXDDpVBUOHMKPCclI60N2ABcy-yhquId2oCbzitDbZbKuzzshJDzwdek6VD7quodx~XUs0B5CwAl0smYSMf2b09Q6jdQV96-fOx5Ieao64MQr50nRUoCbxhBndQpg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Lever Settings*

1.  Click on the **Integration and API **option from the left pane.

    ![Intergration_and_API.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047105476-?Expires=253370764800&Signature=nXe~UMYhxCM1SdA4MlImw3Xt3Y06AOYvoYE-9yJfJpxoHqGW7EAxoDkeolIv5nArcSt0i4TSod4tG0lkN-Z5hxfV-UbFmO5OGh6mgUFhgYlC7RXBDcAe0gWhJwBIpDD6hkLPKyUueIoPRDtjRyAXJVcAUGl73itmhMQQ2YyzkQZ~3amPmTtk255VPBG9yJ3yUslX~GZWve2fobwf-iElByO2pBoqv9HhmMfdasqS9-ZSeZExtbvttxPDlS4aXAHcbIsoNozJMQu10lx4feap8tbT-cyThMyGWG6kJGda6ZaOwYd0J-pP-MWy3tzJgLDNRCwRpZZ0leIJ78JFqIslBQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*Integration and API tab in Lever*

1.  Click on the **Webhooks** tab to open the Webhook configurations page.

    ![Webhooks.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047105949-?Expires=253370764800&Signature=mO-9cOVb7gs6T6lMOuycFRRrM1sFR8IYvZWkYxnWH2tW9ICzWiRcP7iq9jE2o61qgWLHkf4n0e1QBMYVo4YQbPAnU4kp0AJ2f5cz73F-HmAk5N0HxHPgXzV3jIGASHPlhv8gf6sRnR-jOOm0NwurKSuHvSz2ycwz6lI1GVkcgI00cgJrrOHxNmCbsXSda1sKlqgaYeLJVrvI1v6fP5VxXMUFZK783ecxzAhI2BvZm-0YFC24p-S-qta~zQIZKXyp8kCRH29nMPQmqX98HA0vXNUxdUXybhx5XZoOSYnkLTQp8F5goBa9~Xmq3jtW4QQA2GS7-r~P5W6eh1KT0HEX1Q__&Key-Pair-Id=K3NV4LZ47N8M46)

*Webhooks Configuration Page*

1.  Perform one of the following two options to generate the signing token specific to the Webhook URL,

    - Toggle the stage change button.

    - Click on the  '**+ add webhook**' option as shown below.

      ![Options.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047106761-?Expires=253370764800&Signature=IIehfL1VyLv~6ORa7gAGhEsvep28JRmczxumUPJsGy~gmvWo7qXcJNh5-t5pWnqHF36NP7hOPa9J0reZgG2Ka9q-jfXqJSsuh9835KvjsMnzU6wJHU-oE-axJoe54yX2Ez1v9YMU8PTLSpmJgy1xpJ2t9Huy1wy61wyOACWvnoMG9o6J03VaCjSIfqYxy7XP3FgLbDMtHDU6-hLgApXjLXduU1dpCFguuzYrGjMf-sVNrUQRmTk-mep3WJ8pPKjm3A~qlxTKnz-NM0on0~903U~Lf3FTRUTtLj5-U3Hg5CtYkhMUg8sl9jTJ6BCIKPIR-OFl-B84MX7A5sNnxZVrzQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*Options for generating the Webhook URL*

1.  On either of the options (toggle switched on or '+' is clicked) a unique signing token is generated as shown below.

    ![Signing_token.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047107160-?Expires=253370764800&Signature=c7tokvIm~lfZAxJLMS8qvhfNHaeJ6LemgwcOq~2UsB5nWQPFI2DOze-DVAT3a663H-IyiBGF3lA386gE9xun~atd8-FVGV80tVX5kvI7a2ztBA~UE6W6ypnn36yZmNd40dhRFIpv6yZgBQm88szrytmPbrjqW1c6e0ABWX8ExpGl1SBpxD1VRrbn9y-DwaWJgfOLCjAOWun46Zp7CzYV6O3pnCzgLOO2NBivwP4pyFP7KimIoQ1~mduQqPgKPQcupusz~Bq0WP3GxcjealLwxhhh1dTvK5ADUfXxbXT1ZDffFwONlDPxh7ZcSjvs3wMgfsLomSMOeUYvkAnScPSIgA__&Key-Pair-Id=K3NV4LZ47N8M46)

*Unique Signing token generation*

1.  Copy the token and store it as it needs to be added to the HackerRank. 

2.  Click on the **Partner Integrations** tab.

    ![Partner_integration_.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047107604-?Expires=253370764800&Signature=iCTZU9i8yCvcRD8hXiky42cSWRfpmSAShHOhIyEcjtczK09DYPneqviy-CHHGXNxuuS1MfEBDlXOAwWc02CXycT~mTmdKZ8oM7c42FXE65hmTwtxU0xgwek6ELWgqkNvN8dSeZz551sT0yIex8Aepbs2ftrMKTYoshf2TqHCAqvJ7DLS80W7K-BNQeY27WMHCGSgu99qmH6-a3whrT3Tc4xCJpCMCP6tMd~GVXnAvcZ2IWcB7fYGJGHQUzWPVUB5Yhv9ivsaFBHl8O-cT0nqDo~ZTZ9yHzpMhXngf0ZkwmECo~9TjSTzUmcLkqm64Uml2O0Bz8SzKjqBFe60cEx6qQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*This page provides settings to enable integration with HackerRank*

1.  Scroll down on the page to the **Assessment** section, and enable the **HackerRank CodePair** option. \
    **Note: **Although you'll need to enable the HackerRank CodePair, **you will not need to copy the key that is generated**.

    ![Assessment.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047108074-?Expires=253370764800&Signature=OOXfUkZUJzbPPdoZSKKx1MnQlpY7O8GUC-P4i2cf7vuJXGoU6Ye8gavnKcs4Eb7as~5Oy4g5ybEEEWfzzA8GKEUuKu88AlvmvSuP4h1D-Mz8sm4p-qnc3j2MGXPgjP-DON6ypQxY8fPua3rP3eZWgGCc6oX01XfQIawYf~pjfEn8ATfk50ch~DT0SI-rUhlDzmW8vjj9SiBfVp~QkCX8ywRqVhPPZNmDR4qXxxoxxbwbA4h2K6Oe7qJX2E~w2EC0RuuxwZrCkZC9K07SMdPNNL9PkHrfoHN~hNTK6R5ReHGGHr21dDxO8402MJq9SLvIVs5OUr7P6zRS3DsgL3z7QA__&Key-Pair-Id=K3NV4LZ47N8M46)

*Enabling Lever's integration with HackerRank Interview*

1.  After checking on the connection status of HackerRank Tests, scroll up to the top of the page and access the **API Credentials Tab **(At the top of the screen)

    ![Lever_API_Credentials.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047108464-?Expires=253370764800&Signature=TKWkLn0nA7vmmr27ybv02ciuUQ86HP18ObZgnW8fv-MHoNpkzwnIx2XVb6-mSNmtELocCyodQYYsDUpsNhMNPe2nuJNI4iQ2vwrM3fBYwU9FRUwxfkJKM6L7wEm-2hnkKt~7DnZFxk7O-QeXuwkdg9-KEQoLpOiSe1v6A3WpNhKp7C07GHEJlS0TzngzlKyB9NsRKxruG0g-ILYPDuwynRfWW5TmdGXIfYrGIRrPpwMYbsF6FINkbXXPfLkToyE-5qBOgqPSJDB7pQute1qEaY8rpgJUZchZTKix64y4IcgrZXiVJ5XjCsTz63xHVdkMAvpB-m6fHHJicSDXpY71tg__&Key-Pair-Id=K3NV4LZ47N8M46)

    *API Credentials Tab within Lever*

2.  From the **API Credentials t**ab, scroll down to the **Lever API credentials** section**.** (As seen highlighted above within the API Credentials tab)

    - You'll then need to ensure that the Key that you'll be working with for **HackerRank Tests** and **HackerRank Interviews** has the proper **Read **and **Write endpoints** assigned, including both:

      - Create Candidate

      - List Posting

        - The **Read endpoints** and **Write endpoints** are two separate sections; make sure both fields are checked in each section.

          - Scroll down past the **Read endpoints** section (as seen below) to access the **Write endpoints** section.

            ![Read_Endpoints.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047108940-?Expires=253370764800&Signature=Ly13NiLCAyR89rpvJMZyLb-TyJk8DA1LuHN24SpfPvF37AqaNxSFgw6WsT~Smk7R0zHxZtgn7LI7XIMHW3r1dJ7bBMf0ykfK~FLbfnyBLHQhefxqeuMe3pyGLK2KlHvxR1q6mlYW5VLOtTO3COdxtN76nYv91Uyh8buQDX29qvf4wxk-IY~H2OKjJX7H4o28hllHLHdOw09RJVbrryVaKVfi2RHl032kV3rjKdJWd-nGQorFNli7gx9cQ2IkeMhTvfsgEuRNbz74Lpfmtg5XklrmdfPQT~BwT33q7pgofnfqxmkmj1-3MPo15TsS22yOOKc-yjDeFqdNpK4TPegQyw__&Key-Pair-Id=K3NV4LZ47N8M46)

*Read endpoints within Lever API credentials*

### Obtaining the Webhook URL from HackerRank and Adding it in Lever

1.  Log in to **HackerRank for Work** as a **Company Admin** user.

2.  On the home page, click the arrow next to the user icon on the top right corner of the page, and select the **Settings **option.

    ![HR_settings_Lever.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047109348-?Expires=253370764800&Signature=pNz1s8oGgdSW1jY-Q2FEcE2uUX1u0jbsS3C4xGwNBt2Lf2f9DpSE2fgGeTMnckcle-N~LdPEG3PtytO4ndp--MHGTNp4FlHwJhh9oAxJV9FDbEfjBVfTp1l6-4QpDpanzriqbHoXrFLhNRvdvvFTVvkPxgyqgvOBUhVGi-WowD3WZspzFNYfs7VNUao-PH3R-gl7E6gvXYc3wMTq2ro7keEXgfoVUUwjhwg2iev~HPP2rlkdOj~bjEEWofJymPTIaZ4LaDrBmdhrFDU-CkLtLh1ZOb4O7XOG6xpNn8tLb8gOky23EptcrFRusVP55UsIHvilQSbmhLj-ytnesJcgdg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Accessing the settings page in HackerRank for Work*

1.  Click on the **ATS Integration** option, and navigate to the Lever integration area.

    ![Lever_Configure.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047109701-?Expires=253370764800&Signature=F3F33iXGiIU0FFTbM6hOAmj2B2rvWMpB6RWxa6AjX8eR~w3YYJzH8p55SfCgsHUf1dooETDycTExVmm9FXMJoeUJvquD0IHPHLS7vo8Fsm2s-EKkzz0l1p0FfSPYDfIm4N1LAtYGKVUEldxwCOlhGYaMGmBuLrRoVFwpG3fa91EHXsVA1ra6Sn3MGg4axuxjfQYpSkSvdOLlENTOntI7oCYKNAewO1GF~6tPVbWyDWU7bF8gjDecmy7jBHpRqtVSzi4WFYvRKOf~FUAD8H5Gj6CatrQ59uv0IqP29OWz3yTd8yu9ZsI332mSxzDIs4Y6zUDQBD3ydEQ4F6XLVovgpg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Lever Configuration*

1.  In the respective fields, add the **Lever API Key** and **Lever Webhook signing token**, as shown below.

    ![image5.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047110153-?Expires=253370764800&Signature=cavBAec2nkUwJzjaporqaOSqu6cORqpp9Lrwg7KnF7Lkn2KAKMtQse6LKXPbKg3uJ-D8kQEGEAMCSwv0PLQslSDTRSgsAjlVfv9BgyNr8HPcLoUJ2vYirfONwRkXPA0uc6bDmuRxFZpEd-ofxBjY2EHFw7yFCG8C488LNHHRRBm8eYOQawmSJJ9nod9CdmPpDBXhZTvqOXiP1HYs9A3MGilbJERFcYVFyTFLJfFfGW1oB-RF496q2hE8AEGKdQYuNtniOLbHHJaGB5LTEclN7-~mjBPiDByCiwDjh~YwfLjX4n~vzhEsgJXvFDbZUZtrnzkBCfF4FM2hV5vdWw1UhQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*The HackerRank settings page with Lever integration fields*

1.  HackerRank creates the Webhook URL. Copy this URL. The integration completes when you add this URL to Lever.

    ![image2.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047110449-?Expires=253370764800&Signature=FYhxIn1qzS9jIpvboTJa6TcXDMtaO8WRxwFYLPmORmqqKxf-fzuoUSZFMKGpBafzDwKJGgaG98AQZxWC3XlQ~R5D5HL0l77bxsMi2NGUALRGokLsOCJNMBH51pIxkGT3c3deKybQ5EeH0-ClU15C5hc4gxI71AHxVqhwNCB6iquruHtTQBkOUoJDJrgtE8Ok8ZKkQTzZ3zz3JfJIWahkLp7uHr8DaUirdRnWdVDLsZF93du9cZgANjRqY5mXi9V5nfTljuBjZRdf-JcZpqpPUC32ATj5WWnA9MR0zQQUhMpfYiuQE4MbiMI6PsHbmcmNL18Hf6HcpsTQrSuoU5di8Q__&Key-Pair-Id=K3NV4LZ47N8M46)

    *The Webhook URL from the HackerRank settings page*

<!-- -->

1.  In Lever, navigate to the **Webhooks** tab on the **Integrations and API** page.

2.  Click on the **Webhooks** tab, and under the **Webhook Configuration**, turn on the **Candidate Stage Change** event. In Lever, this is the event trigger that sends an interview link request to interview.

    ![Candidate_stage.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047110855-?Expires=253370764800&Signature=Aam5SdlhVtfkuYX5CoidBeMmU0pw6U9pKcd6CBlR1l5ac86Kx~HQylIBuU2u47rv~ARqUYV7jDziQ6F-ycINdrPsq2FOs4cdtCCT9O6Thsmj~qMXTqVMEYdopD1shM~ZpfDDFiorjOSOuWtMePZPMXC4kjHYl4KJ3~5dgLrEb990MkcVZ1dDpAG8Wgdoo0YwGSh0MyC97wKEgYUyTgoqFiTQBV7p6PlPqOcBwXE1Y9ctw1kizlUu~2xVLUDhhcDy7cr85FqNlPOMhxLFmslFxY~EnR37TqbJ1stczud~klXXh2ObrEb2JIT9hoXA4l59HXbB~NbPuEZOkXRKYvucrw__&Key-Pair-Id=K3NV4LZ47N8M46)

*The 'Candidate Stage Change' event trigger sends a request to interview*

1.  Click on the **Add Webhook** option for the **Candidate Stage Change** event, and add the Webhook URL obtained from HackerRank.

    ![add_webhook.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047111289-?Expires=253370764800&Signature=GCktrvSxTNc7UxQ0vFtA8ycWRrcDX0Sn1078ev4zyNS70sGqfugVSkjbZF3f8DvegD-W1-QiH394YCvmeq7q3pkXATfw5icaXwMM~QmTCB-gSMkO9yv~zH36x~g2ZBC6lbKabSVGs1MqQS-osg-yRDhvpF5I5~UKpC6WXFIAbPHFBmEtclMdmu9ohyzUbnCIkVQtV7mm9YGCJJiUU61ePtRhLbuSqZvYqbB24RGfYDw~kdUjvAy1caZAC~YQYCDG8enwXAGTCp7mrDKKUvLYuRQZdmc2IwQNyrxgYW-33vIhgA2Zz-6KgEQ7sCaXHRrQyDaYy4CF8MzOW5L5~Y4CnA__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Click on the **Verify Connection** button. When the URL is verified, you will see a checkmark displayed. You can include or remove the 'https://' from the HackerRank URL.

3.  \

    ![url.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735338969593-url.png-ad91ab99-fe48-45de-a1c9-8da8cc9e3b02?Expires=253370764800&Signature=HEVwXDG~yEGSg1u9pIBykMC-D7JoR-btxiN4SsouIM81rqHmOxp4aMKXbYZ~1YA-iwNaqLX9jfbke7CLP03YuaPRY60f5rmCtDlSdfz0wfA7sdYZPoRYYmNJSTeQWNKT8DL1X4wUnfuysWJ8tc2zLBFxOAOeJNGqTZswGnf4LX7Jc~yr77zMhiu~5P14K6SQl1lAvfkQ9iWuCXYNlg2c8frBNNb8PkMGCRfI72IhRli-xUxlY407d5HeafHBPpWUt~srQwDpHsa3vKZiUXo1o82E5PzQYUjYwhC0J5z3DZf9hnOBkz9juxvyJvAXv81wnZGJpzGJc2oHGDvSvS5HNw__&Key-Pair-Id=K3NV4LZ47N8M46)

    *Adding HackerRank's Webhook URL in Lever*\
    \

In Lever, candidate profiles must meet the following requirements before the "**Candidate stage change**" event can trigger a request to HackerRank Interviews:

1.  A profile must have the candidate's name and a valid email address.

2.  A profile must include the "**HackerRank CodePair"** tag or be linked with a **Job** that has the same tag.

When the candidate stage is changed, an interview link is automatically added to the profile. Recruiters can click on this link to quickly start or schedule an online interview session to assess the candidate.

For more information, see[📄 Scheduling HackerRank Interviews with Candidates in Lever](/articles/2634152447)

\

![Candidate_profile.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047112224-?Expires=253370764800&Signature=WNUr37jatNQQOcn8PX2bGPdDwZLtJj3fOGkpXm9digC6V7pfpVOIMQiFwLuikQv1NWoH8bfCDmjFB7gE61Cog0H~88pM8mftPSygZF4WwUsux7ZuozQSY6AV12AHiVv58sTf568JlJ-IuYdl6CQx0B9Xor9g~ptkvjqhuL~5qOThhUgks5A38Hw4jltaUSh2mbDNwwYV94tvrXiz1xAGDPAwZQ-7wqzPQ7cen1nLwzOGMhEFr86xGPHrGrFFhfJJpoXNJXHG9rlAQfldZbv88jud5DnYNjx8JOOjHKgtSW9p-gkOuMgih63lnB0omfN-2ZOidhc8T6UhegVwEumMsw__&Key-Pair-Id=K3NV4LZ47N8M46)

*Candidate profile in Lever with the "HackerRank Interview" tag*
