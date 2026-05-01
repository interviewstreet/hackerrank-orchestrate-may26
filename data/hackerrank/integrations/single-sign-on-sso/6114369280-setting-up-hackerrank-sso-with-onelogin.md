---
title: "Setting Up HackerRank SSO with OneLogin"
title_slug: "setting-up-hackerrank-sso-with-onelogin"
source_url: "https://support.hackerrank.com/articles/6114369280-setting-up-hackerrank-sso-with-onelogin"
article_slug: "6114369280-setting-up-hackerrank-sso-with-onelogin"
last_updated_exact: "Mar 25, 2026, 2:36 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Setting Up HackerRank SSO with OneLogin

_Last updated: Mar 25, 2026, 2:36 PM (Last updated 1 month ago)_

## Overview

Single Sign-On (SSO) on HackerRank for Work can be configured using efficient and productive Identity providers such as OneLogin.

The OneLogin SSO portal ensures that only authorized users get access to sensitive data. Users have to enter only one set of credentials to access apps in the cloud and behind the firewall – through desktops, smartphones, and tablets. With SAML, OneLogin SSO proves helpful in securely logging users into HackerRank for Work either through the OneLogin portal or over your corporate intranet.

This article is a quick guide about configuring SSO on HackerRank with OneLogin. To know about SSO and its benefits, refer to the article[📄 Getting Started with Single Sign-On](/articles/4264962721).

**Note:** HackerRank accepts only the user's email address. In the setup, the user defines the SAML assertion with the necessary data. HackerRank SSO fails if it receives anything other than an email address.

## Prerequisites

- Your organization has an Enterprise plan with HackerRank.

- You have admin access to your HackerRank and OneLogin accounts.

## Adding HackerRank to OneLogin

1.  Log in to OneLogin with your credentials and proceed to the administrator dashboard. On the account set-up dashboard, click **Add Apps**.

    <figure data-type="figure">
    ![Step1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046507452-?Expires=253370764800&Signature=p9V8xGF4XvcNCBPeRVbIVEiFmtAbc3FQQeVqxH-12YlXZv6pg3GueX9EYUqUjVGmwPzmOfnJudh7W87kb~zwnCUKMEH-g74JaCTuCg~RLjkqlkQer4u17qVdlhg8i19NAfkvODUxN7NRPEJgbW5TSNRoqA~6yyaeW9CB4RXY3FW1z3O7989pW81HslEFMcRQC-dX71RzfUam5jZ02FGRM3SWIthRaHGUpMWWASw~20N-EkjWM7TE1mRPzvLhjFE4hYn4lAEQEWiVyltPT4UAtz93vPymcM2B9Y27HB0SF2gnY8HFyiNjOK8WYk5udr7C8Ijetvd6mPSWDm-FCLFHrA__&Key-Pair-Id=K3NV4LZ47N8M46)
    <figcaption>A new pane is displayed.</figcaption>
    </figure>

2.  In the search bar, search for *HackerRank for Work* and click **Add**. HackerRank for Work is OneLogin verified and is now added to your list of applications.

    ![Step2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046507740-?Expires=253370764800&Signature=eHdXlvDD4oxm6YOcDhk1H1MmATgsYXZ1ox9FwrjO~B41AR~-JlNtXYP24TGOuVE1J7OMLbmOmNkOOqjYIgRtPf-wAqT0WWJMSEIgiFIJKOHUHcLTB8KJ8md9fIGECG1VlMMW79nuXeBIDeaCkOr84b5bZ9wfz~TMhY8x4R6Q~wdpTAjgdyNBYVXE7xIumD9GcWeVXvuRPMVAK54026HV-WCiRqHN7zx0ALMwNiDedfcy1~4k66gHRSHM1h1YNybzNEe1m4Y6fLykEOB5XaMYm0loutDnjXR8LW6jGLKOgfbAebNfFYsM47TPHisDDSQnvyD4yxn91OaCiJ843etpUw__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Make sure to choose the application with SAML 2.0.

4.  Configure the HackerRank application with an appropriate display name, icons, and portal visibility.

5.  Click **Save** to confirm that HackerRank has been added as an application.

    ![Step3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046508128-?Expires=253370764800&Signature=eyepFcvsjU5kQIxnL1eJYfPPm25xGKFzt1I2hBDi6xR~LuvuvPdXh0eUPrFExew-0IlgLQ~vkKxWY1Z2gbzcFjpOyuOtPwhzSq93lykTGZFBeyRbaxU07iiLnh32NI1N2xj7dgn~fFDQZadAqXx1Idih7ISa1N7Fp01tPN2FvTFpwXQBBklvtvwKlKfltNkfCEZn4ECm9eFP00wbgvdaaNlbNWUeJvZWDaHAlcs-btYnhXm983ED58p2myZpIN7h~ZeIZI~WJcwf0hyGfR3gpzqBCF8pcHR64lK0P8Diq0ra3b9p87zJJDAsKKE6D11Hd90UgG1Ayi~HBNx2w5xOdw__&Key-Pair-Id=K3NV4LZ47N8M46)

## Configuring SSO on HackerRank

In this step, you must enter a unique HackerRank SSO Key.

1.  Access the Settings page of your HackerRank for Work account.

2.  Under the **Settings** option, click **Single Sign-On** to copy the SSO Unique ID. It is available in the **Configure SSO** section.

    ![sso.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046508811-?Expires=253370764800&Signature=fwDPEOnt1-DxZ1ISPM--N4M7N714MC3srv71abr9uHmkVYtrBJZuOs6Rl2tljB9FKlBUN7r0KRzXQru8t93HN52ekSNuM~Cim~xnoIEV2F5X2IVpFc0K5QomYIwC0DcdMUtdS2estF-3AXvw6mIo5A1qRkw3QKN~IUuyssWZuqjV~7VQYfKI3LbZWMwNMxLYi9puRZLyAJjrdSSRkq7YIrHeoCB6v~cEcUYGUBPvy21Dl~s2Kn5emdRQBgequGI~yCi0n2HxEzF77wlIMJb2te~IdRS9bkh~Jub~2cFbNI~iHAJqKZ2aCqOuJ-QxEh~FoLT5yx-xc72ywQrju8Kr6g__&Key-Pair-Id=K3NV4LZ47N8M46)

## Adding the SSO ID on OneLogin and Enabling SSO

1.  Copy the SSO Unique ID to the **Application Details** tab on the OneLogin **Configuration** page.

    ![Step4.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046509317-?Expires=253370764800&Signature=O6nyXC0WbNvAmTa9~C-edBctZ0n2BEVEF0ld-ykiW57xl1lOUjLyWqFBhI0TPPFrqFp-SMCtqzG5wbjCOO2HDNbEFYvnY6hG1mLp~tNWhNZe10JGxHvj4GzZm221OutRVes7Uz97Xqx8CgexCU33~bfUlW0qXdZqmJRy~jAOg~P1esIl~q7GJEOl6XeSGWctsc8pYThdI1aBd1bwUiNcOV~Z~~LMNkrwvMB787LwzgR7hVQCOVpP3ICiyPBSbaUg6H-rK3JwYDMt7gmeIcwv-H5d0RzxWeBT7p9m4Fi6cD-ng85Brv0VI~SYqqzVSCv49j2ufzqUpt4ChkX8r4KNcw__&Key-Pair-Id=K3NV4LZ47N8M46)

2.  Click **Save**.

3.  Click on the **More Action** drop-down and select **SAML Metadata.** This permits you to acquire the XML Metadata file that needs to be uploaded onto HackerRank’s SSO Settings Portal.

    ![Step5.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046509629-?Expires=253370764800&Signature=uKo1MznzEhJ9-s7OfYAaAdDOzo0iAAV2LOGz11oVbo62irQpdIOVscuL~cuin2eRyfwR2UgNtq93PxhDBMCk9JdqwjbMvP8NII24Ci796nzxknwYTm-aidP3QWspUlfxDbkNMxYXqh3p-MJN6rjoXyijNrdLUMyAy8vi8ZIxpzwhjdDZCtLkKRQhxGSr~~9h5siaRbeDqiFg8awsXefnO~DTaG-JmLK1r-hE3dTssNE7kRxGuVzDIOleUu5XGTBQsQrIJWADU1UPZiJsOY0A9y8Dsp3F0LdN5G1Xu6zCS3Qewdwfq3gVvv7dQhFHlA7X-ErlORlMBkx0d69NPAOZyw__&Key-Pair-Id=K3NV4LZ47N8M46)![Upload_Metatdata.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046509923-?Expires=253370764800&Signature=ek7LAQFeIcP3N2mmTLtTyo1n5DEzIFTeyE-fyIDFOohm9xYTnDdhELPFMKor9VzTuhTLR7tI-6PYN9nun8SQR~A4gW4mVsrNlQ9NCXdM1EiWRNHqPYrOkFXhHjD~p6MIC0WqpbYdoFJQyyAZDkEL5JoHz9mqccACaVcDCd8ft6CuXQSQo0DU7eQa31dmRR7ybySBe48EJDeeRUHCb95xgq5dbuGMrr~wUy3ooQTZw-TqjZvh2xcCO7PWAsLTRrVee81-NBEW8T-mF4i0J4hdX74hmJzQ5Cefaqa-k9QyBRU8Dg32YSusxHgM7U8rHUBjwx1yBxd2S6s1K5w1~~ugyg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Once the XML metadata file is uploaded, the Single Sign-On metadata URL is automatically generated.

5.  Copy the URL generated by uploading the metadata XML file to an incognito browser window for testing. You should be able to see the OneLogin sign-in page.

6.  Sign in and confirm that you are taken back to HackerRank.   

    ![Metadata_URL.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046510228-?Expires=253370764800&Signature=S0o6oMGcU5FV7ijOtWgtAzYQyseaIpPi35lEEaGdcrdHfII3RiFPJQosz-POxtsoNkpq452ESqdPDT4aMBKBNjU1Lk4SP~aBlKEEp3GiXX5LtLbpaGXi-Yig1jS3vxcMnbPGmbUcAuHl63Ms4vae3Dh~tAYFRUvLBB8s8zHkntnP85TMjeIqF-ubb4CwQkfHHGpgT5xlsFDCB45KWUhRUheRuecKEIj4DjLuQwNDcgGUGwZjxn~lphPjY3HpEtjI2bwt~zLKiaumS~TqMU9AbhC-R5pasnYW6ougXdaxWN0nV1quRNd88IVuAKx0BFBtmyYox3F0fpnUu~5-jP5ANw__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  Once SSO is enabled, all users within your organization will be redirected to the OneLogin sign-in page, when logging into their HackerRank for Work account.

8.  You can disable the SSO setup for your company by clicking **Disable SSO**.

**Note**: After enabling SSO, the user need not enter the account password while logging in. Entering the correct username or email will automatically redirect to an SSO login.

\
