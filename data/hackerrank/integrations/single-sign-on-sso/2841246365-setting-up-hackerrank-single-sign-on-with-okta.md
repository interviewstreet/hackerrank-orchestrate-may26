---
title: "Set up HackerRank Single Sign-On with Okta Prerequisites Setting up HackerRank Single Sign-On with Okta"
title_slug: "set-up-hackerrank-single-sign-on-with-okta-prerequisites-setting-up-hackerrank-single-sign-on-with-okta"
source_url: "https://support.hackerrank.com/articles/2841246365-setting-up-hackerrank-single-sign-on-with-okta"
article_slug: "2841246365-setting-up-hackerrank-single-sign-on-with-okta"
last_updated_exact: "Apr 10, 2026, 2:26 PM"
last_updated_relative: "Last updated 2 weeks ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Set up HackerRank Single Sign-On with Okta Prerequisites Setting up HackerRank Single Sign-On with Okta

_Last updated: Apr 10, 2026, 2:26 PM (Last updated 2 weeks ago)_

HackerRank for Work supports single sign-on (SSO) using Okta as the identity provider. Okta lets users sign in once and access HackerRank without entering credentials again.

This article explains how to configure and enable SSO between HackerRank and Okta.

For more information about SSO, see [📄 Getting Started with Single Sign-On](/articles/4264962721).

**Note:** HackerRank accepts only the user’s email address for SSO. During setup, define the SAML assertion to send the email address. SSO fails if HackerRank receives any value other than an email address.

# Prerequisites

Before you begin, ensure you meet the following requirements:

- Your organization has an active Enterprise plan with HackerRank.

- You have access to the Okta Admin Console.

# Setting up HackerRank Single Sign-On with Okta

To set up HackerRank single sign-On with Okta:

## Step 1: Copy the SSO unique ID from HackerRank

1.  Log in to your **HackerRank for Work** account using your credentials.

2.  Go to **Settings \> Company \> Single Sign On**.

3.  Copy the **SSO unique ID** under the **Configure SSO** section.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775805916841-image.png?Expires=253370764800&Signature=bocTiueCNkDrP98kiGHjypFNBf8zZSylTbW~SJmNznYR7y09bWAKE4-JGetH2QJvlPiZ6d3YlISnX1wfefXYZFVnC8nRmwerJwCsbSGPdC2MhglzUeS~6kuknb~V4o~i-iPLdkVAnrMUyAVdihZD5azY8jhBTtKcHPyU8k3yGTfWPuEsbZbuvpg6L7WlNHsD5ZDGqZ6av-eFbZBnXwJQykZZ3t6tiEbIl~4PgxeUG9RAGq05YxT99mrpecNULbM4AjI8OX~MVZoYOnc5WHQloVHpCXxmUoBCIzd0abJD4rXwVsVo8jqoqOBlEk7xgmsHe6v43erJThAkrk3l3-vVng__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note**: You need this SSO unique ID in **Step 2: Add HackerRank for Work app in Okta**.

## Step 2: Add HackerRank for Work app in Okta

1.  Log in to your Okta account using your credentials.

2.  Go to **Admin Console** **\>** **Applications \> Applications**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775805941562-image.png?Expires=253370764800&Signature=B4kDfMYYgeudZ8-DY61idvXyv~ejErAPzqcEISuLUwY2zGP58AAS~6Qnh7-aDziXFkWAvfwOPzdn1LI961s0LKRxn1UmAmEYpjkgAe1vCxYMndaNwk239siUpH0fu52ynkSD3N0o2ZVVUiqzBRCYEWt7UDipuENZzWcVoFRtHx1e2WvQe7DarRufnGUw33Ba867STTvHn9fuR2mSqi9NZVU0AiIQb3PNMp7SkCiwthkJ--v~rIKyIk8Xan8Br975vE38SzPHn28z4vjk8npZrgedB~T3zAa3~5Al~2InKre6~zdZl1Hfhf1rostFNKbR4RMopHE3VLncG7UEw6bexg__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Browse App Catalog**.

4.  Search for **HackerRank for Work** and select it.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775805984448-image.png?Expires=253370764800&Signature=OellCHwbu9EG-9EZ9RQ8shaHF~1iF3d4YwZmEl3fEn6019pp3DuRAfcTpFHMBhQuNwkp5JO7WgtBy3NJBgMsB5dZPq~E0DqH3ZGY1Ptswvo7NMA1~X3b7J77-tRjt-ttoWUyNUL8dorUvv8J2UZ9FxAj2nYGF7T1KJQ2x7odyPcG00EHy2oMHEUWwm1rqAZu-qv~MBzrHaub2UEXnRekxNh-jzW9k6bYH2Snz-LjNGg8UHN~mXDPOzTKDSR-ifqFR0kBv1VhGpi5gOWsCRhEWMYMKu84yDkKnRhrtNMLvaIm8nU5ot9NNRLZ266ehHoo7ufE3JPQfUKDCorFm09C6g__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Add Integration**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806002342-image.png?Expires=253370764800&Signature=t0uTz4FLFPTP95bsv3Nb4lTJHzzTmSv~wX2LcEfX7WomlfP9~6V83KNOoBy1puRR6buce5GSAo5X-4hu04okISkkWXAEgKIak5wIoj8y4hReURASgT2gWNmF6HK52cZfvDu02k0V9IEukP2uoPTa6E2abRLdCBNyQ84i8FwJa6n2G1lRLMejyZ3rl1jtAyONa7jZMKxzMnIkKdxcn63FVjvwBhPPmkhhd2hjfiOOFSljTaHYzd-xE0k94022Pmc4V10MhLW-bcqdQCm1cdWrUyxxpzcsJ2IV9PSauddbNBr9-tnh5OpwetymeVStzA18FLwiXfnCfMaI~rvAKXPdbw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  In the **General Settings** tab:

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806018912-image.png?Expires=253370764800&Signature=aGkgaUTMQZP5KYNJPR4L-WP7TlCMo13jqkHIZOmaTeBa9SKF4X5XuGcOvGu-31u-PlQTDDjwF0SSHtAG4FZn6e-2LKJi10ZGf1rVuNOHVXUjGlWts1Ywp1uUI1ssQdxf9QIC0r4UGNHg0jXweTNJ9fQzMxdjQdnNiZbIwbEjMgONug-ZxLbVpQykn5c~TGFVLHuBWYC10uNL8GHU2TWuHbpmX2DDctuQj0KFrXe5JJn~l0fa3C6ntZ2kOCgsWyLNJPTiDvMxBufk22mi16jZvDFxUOEOtoKEXgeel-b564RcpuOFJV09-~pThqnko6w0EMKo9aTmmarWbbry9IvA9Q__&Key-Pair-Id=K3NV4LZ47N8M46)

    1.  Enter an **Application label.**

    2.  (Optional) Select **Do not display application icon to users** to hide the app.

    3.  Select **Automatically log in when user lands on login page** to enable auto-login.

    4.  Click **Next**.

7.  In the **Sign-On** tab:

    1.  Select **SAML 2.0** under the **Sign on methods** section.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806035087-image.png?Expires=253370764800&Signature=kJ~6wp8iRLFZzZhU8MxAnhIf53x5V4OQpfQyJKXuEvOxqZrb30h4snM3PvcmyhWVpWXQl5QqHDsbsy9cD61GJzpDS6-mPjNhh~buJKJI3wY7wByLZHJJl-RbY~GNHjViaJzwYjd2T0SkibrJ8ej6ubZkpoiPgJp-UH0WW21rRmVqEL1-GRlyKP5844y8GcDdrikfp7SYNGSXmOSbAR2qmsMjllJ4S7Wbth1JVpBkN9UcSf5oT1Al-PJI6t1xjgNFdRQ9KF9K061iPrxerUmUVexhWz4RBD5jk8J2U1P8GppAVXstoH9g-OsvO6y3Et39r0UV~1m30YoKsaNCJB0yPg__&Key-Pair-Id=K3NV4LZ47N8M46)

    2.  Scroll to **Advanced Sign-on** **Settings.**

    3.  In the **SSO unique ID** field, paste the SSO unique ID you copied from HackerRank for Work in Step 1.

        ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806060317-image.png?Expires=253370764800&Signature=G1wai~KL3JH~OYgQwRwL9e-oeydXx6jTcTKJOeyfda9prz~sA6ehf2cYgk9Gx3coFu4gfNrDrm83g73-1m6KD16oJxum-23Qf4puYtF2HIbpxaSLnvqOHO2YVN93RyVIMo0oGf7LH0gdfLCvN6nKsKeRqvVIlogHQ4V-NEKLV9zBvmnhUvY57HfCyPYLHH47f6ypDG78F8ct5OqIsLb0Wa-swxxFoEqyDhgp-0GcaDCmjVY7zxhNqJ636n6U-eDZUgE60TOu5C3FOllaFd57Nx4e3tQSO4nrZFDtYS-zRWeLg~5ZjQL5Qc109a74v77KBv~-TS--vmE7QuwQ6FsV-Q__&Key-Pair-Id=K3NV4LZ47N8M46)

8.  Click **Done**. Okta generates a Metadata URL.

9.  Copy the metadata URL from the **Sign-On** tab and open it in your browser to download the XML file.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806118869-image.png?Expires=253370764800&Signature=GtOKnEywVIoLOg9u-sZeD9vmXYsW752UspZQMP2lclPyaIWVRdaLnMgFHUdeN5UqoahSpRsovn~vMmQjDZ9tBnbagnOFeI-xBQWCmIq4NZZWaJBGTOANqrGS3tOd540WdOHlwzFf8U8DZwLgLkwfh05t4ZVmqTucqQoQTqeDass8gY7mqKdd1605UM1yfG-ts6W5ajBTJ2f6atYFu7w1G8~Yr2YS4ztfMYFPIcdPZjqgiiQkZKy12s309CDv1TQz0QRrTSaMM1qbfjbWckYdEGsnQRmNUHFFhrADcqTSan0Jjj99LnmwF3ETee4K89idHMWi9pNgP8F32XNILOWwaw__&Key-Pair-Id=K3NV4LZ47N8M46)

    **Note**: You need this XML file in **Step 3: Upload metadata in HackerRank**.

## Step 3: Upload metadata in HackerRank

1.  Open your **HackerRank for Work** account.

2.  Go to **Settings \> Company \> Single Sign On**.

3.  Click **Upload Metadata** under the **Configure SSO** section.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806151652-image.png?Expires=253370764800&Signature=ZybYaff-~VZrrAn1U-72QzRGNQRhFwoLu0GusOBMO1gGGmLkO6fwJ0oAyFTOKZQzXKM0P1s2urEuwySQIMvmrWA3XQEtIYK9vX4IXgKGfMM6dzdRj0u8fsR09O4pOArMPExb12ulfZ5mdYFNLTdjLf5eYDRx066T94Grxn4HNdQeiqrzE4ot8GIO7HeAb7eXXDaL13kW6VFy4k6YnvUnMlKznpRaRxhegrKsCUuoIw2Roa532KgcNvn5-EHflZpmNQ4EQ73cFtQjsAWY3m8z5L8CrCOW4Tt88KsMmj1zrezFpYOaxhEkNjTXWJUVvR1Z1fIJLyA-UM~OLa6yjEJn-w__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Upload the XML file that you downloaded from Okta in Step 2.

After the upload completes, HackerRank displays the autogenerated metadata URL.

## Step 4: Enable SSO

1.  Go to **Settings \> Company \> Single Sign On**.

2.  In the **Enable SSO** section, click **Enable SSO**.

    ![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806168561-image.png?Expires=253370764800&Signature=l~hkPksw89TOJhhEPJc6rccG3vgmrSazXl2XC-bFhvc4N6CQXyaG4CjrQppHOUeb0AxI1PZX~2kvOqm3CXsgzca1~7iCP8QWbJLMK9R~MIuhfw-rCjtT-4s4c75PnfZv2WEbdeXXP2wNic3aUEbJC1AcNf1wv9XrQT8foPnGrkxt-BlUMM4bBJzGKhN5MNNMcbJoCl0dh-n9TkY7VnWZ~a5oWxIG1w26uQm7~sGFwcebI1Ee6GnIH2MQkTFJANZ2w3xGkEEdmvEs6kJMTzPquIvoj7IdK1RnWf3Cxlbd4yKYaVjYruxXHNqsUr9TmHSaRB5XFVxtUcHY6yI1A9RWoA__&Key-Pair-Id=K3NV4LZ47N8M46)

After you enable SSO:

- Users can sign in to HackerRank through Okta.

- When users enter their email address, HackerRank redirects them to the Okta sign-in page.

**Note**: To disable SSO, click **Disable SSO**.

![image.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1775806203149-image.png?Expires=253370764800&Signature=faymt6TroPfwsq2gftDpSY9xkIunogB0w8Eq-JJ5nj8S6c1IAQofr~1ajPvO3w5~MchM--wQTA1nRpuMBHkA3~14yXuV5Dk2FrzhpYZdn7UL~FKMiVBpG~LeTSXiGVR7JMEGogwbq0ks4llPxJP4O3WnN1OLWEhxl~HB8g2T64n~RNRI5GqfCZ9BdVVKXK61CVjhS-EXdWgXOfoM3FsBWuONUBD~JpLfmMAYfYIKnZG14LFywqkWCQsxKlddxXVVNR~xdZ8GR9hndC4X9IDjQkAyZuAjFt7Yl8dCyfx3B9bDAajgKnoiTltLO1p~RwdohXAlYqPfyA9sTAe-WPhI3Q__&Key-Pair-Id=K3NV4LZ47N8M46)

\
