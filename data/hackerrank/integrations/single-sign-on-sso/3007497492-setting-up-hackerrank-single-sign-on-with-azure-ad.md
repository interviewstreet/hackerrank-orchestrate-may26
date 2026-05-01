---
title: "Setting up HackerRank Single Sign-On with Azure AD"
title_slug: "setting-up-hackerrank-single-sign-on-with-azure-ad"
source_url: "https://support.hackerrank.com/articles/3007497492-setting-up-hackerrank-single-sign-on-with-azure-ad"
article_slug: "3007497492-setting-up-hackerrank-single-sign-on-with-azure-ad"
last_updated_exact: "Mar 25, 2026, 2:34 PM"
last_updated_relative: "Last updated 1 month ago"
breadcrumbs:
  - "Integrations"
  - "Single Sign-On (SSO)"
---

# Setting up HackerRank Single Sign-On with Azure AD

_Last updated: Mar 25, 2026, 2:34 PM (Last updated 1 month ago)_

## Overview

SSO (Single Sign-on) on HackerRank for Work can be configured using efficient and productive Identity providers such as Azure AD.

You can log in to HackerRank through Azure AD. Create, update, and deactivate user accounts through SCIM 2.0.

## Prerequisites

- Your organization has an Enterprise plan with HackerRank.

- Obtain your SSO Unique ID by referring to the [Getting Started with Single Sign-On](https://support.hackerrank.com/hc/en-us/articles/360001546888-Getting-Started-with-Single-Sign-On)

- Replace the ID in the URLs below where you find: "YOURSSOUNIQUEID"

- Keep these URLs available for the setup.

  - Entity ID: [https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/metadata](https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/metadata)

  - ACS/Reply URL: [https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/acs](https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/acs)

  - Logout URL: [https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/logout](https://www.hackerrank.com/x/api/v1/sso/saml/YOURSSOUNIQUEID/logout)

**Note:** 

- The Sign-on URL must remain blank during configuration.\
  Entering a value in this field may cause authentication errors

- HackerRank accepts only the user's email address. HackerRank SSO fails if it receives anything other than an email address.

## Configuring the SSO on Azure

1.  Navigate to the customer's Azure Portal: [https://portal.azure.com](https://portal.azure.com)

2.  Goto **Enterprise Applications -\> New Application.**

    ![Azure_AD_SSO_Configuration_image_1.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046353425-?Expires=253370764800&Signature=kdC8bQnquEv7C4YUa4Ic213eENB-GvmC6uJD4WlNr42o2UAaVQII8QyiLJ5ZN3heDChZny3B~U~KB1DrRGIlbz-vN24l~dvVwOc0xuhUE2BCLehpXczdpLcsVkq8mAczRIpWDTThnIEilgvgJF7mWXE~veQK~dyxjMUyGN7BjnggNVHVETCwbEyOcSkiS9qFskGmPSFrfPNbEe1ehXXaTYoueVk4wVCBagolsyFc63UOiWsGcGNO4OJVZi27jYKMqOVbQ4YmOdb12rpHQC0h0wvsH17fV16O03EeJXYV4v4PEFToTpfc1hmsHfq4ZW3Z34zhzAZ8c2Swm5gcHHWADw__&Key-Pair-Id=K3NV4LZ47N8M46)

3.  Click **Create your own application**. Add a name to the app.

    ![Azure_AD_SSO_Configuration_image_2.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046353823-?Expires=253370764800&Signature=kR5aIyFTSyqqAyh26dpSN2pnLI35nJiT~uObc-5mVv8nAfYRiCpbcJ8WqiN7jnzSC3er0bs5Fae~rJXJSPqvVe3O~Z~STjiziv28MCdo2bfxA8nt7tYno2EMe7VEVUjccSS5ihhi9MOur~fbigcqC4TcKmOsBGHycd7~Dug7gQcRj0mCwffms1pqFd6UMFAlG1Al2lUCvL6YwKTLC2DXp90yloUCuUCQADk0TWPbekI0ziYmDSf7blkOUwjH5Kw7Clrbil3XKrgwh~-ceV6lcg4V8M1JvMVuM-407C1hbl4k~mB8Sszzu54vUBTIpkBt9YkE7N8cQnUfwcGjKnPb-g__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  Select **Integrate any other application you don't find in the gallery (Non-gallery).**

    ![Azure_AD_SSO_Configuration_image_3.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046354307-?Expires=253370764800&Signature=IAk17haRoOFSLlPnqsfOTwajLfIen7HOx36LYM4fUH3vS1v40zlPVv2YFRgUzQ~9hkyQT35jeZW2-4s-Zh1NDWTvSXAypkmy-XQDcJAPAz3DjKimPN6IkOdZSUCjqEw5MnQKhADLiBju2HIaoF72rDkX7SzZjGox3ex8k-TGBSPFZdE-kMv4md4-QRmJeUomJNu6Pcws~6vlD6Jxk53BlCORGuP-kVBLa4XFCifwJPRvtycYxK7gMtUaiitDLzKIYwUcLYvuCOHMHSjQ2ss81GIZvs6biKOrJ0fhkpSTu8DdKswh33J3a0Aknf~40FIrezP2Wv8rRtizw2VTS5fkEA__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Set up single sign-on** (Located on the left pane) -\> SAML.

    ![Azure_AD_SSO_Configuration_image_4.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046354805-?Expires=253370764800&Signature=cqcLH-4i6jd5bGFhw43UMRLQb-Qsd13ZzAeJhUf380FeNcV9cp6Ii~hbiVl5JWMyn9Vk5SldpJKKY-t~eISTD75ZjvhMohv-wVTkafh6TzWB-mEjbxymG7FH9idFQ-iR4SnSpyDW3tjUfWAFbNYSsX7CoLYLnYJ3jA-3a4K0BpRDQcTabG2PZcB16YiPRmkBtcmZy6Iwrmsmw6vn34odVmuo-fW--wwNuOXml33XC6qigpW2XjbqgWomizdPy3dJGOQO8gvbKnYOtlZxRGk2lRl5WUN7rd~cSo2TnkUYd0ndWNx1S5LY9FT4mZ642DTm7bVAt66-g6CKbeih9u6XCA__&Key-Pair-Id=K3NV4LZ47N8M46)![Azure_AD_SSO_Configuration_image_5.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046355163-?Expires=253370764800&Signature=lAE0-Conh66aw4ixp7HAriOMk6KRbivPydxnQPmyG08XsTpL67yvvRYdqopx91OWdbH025qreBht0Q0i60fyif8tDqu9I0zF2jkSo76-6fAVxz-vb0lV1tuknwg5pZQXmfdKXU7BmoAqtiglrDtJYlKLt42HBGA4N7gBOwZYeIU4Xk4Dklf-suYmUzRiyn9modFOeeXOSUHYsGdtiGQHEtUfu7ZcCsdD2PjzT9NPyhSVQolu28yOg7h5erFO-LpqQQdhd0FAU1lOsifb7nTtlg~IEGKAoeB3oti50nl7FMGE4WTqaaFNhFbJzuVwNPhHv3fO43skFwV7fPgDyH2G3Q__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Using the URLs from **step 1** (Seen above), you can either create and upload a metadata file and then upload or manually enter the URLs from **step 1** of the instructions as seen in **step 7.**

    ![Azure_AD_SSO_Configuration_image_6.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046355508-?Expires=253370764800&Signature=kMamb3OMlC4H5zOxXL5mro6R9zlN5KglKX~oiONDeXVCpUxldIYvn-SodOEUYpfXfd5vEd2vaebRYk0tjGzAY~yZSmfiwUawY5vJPShWaYBIOzS46EoVIpZFhEgxHZQr4kNEIZ5hy-KyCnAyzxCeqUFnD06mrNM0ZMcRA8M0OsDjlAyM9EhkSmPlzLr5haryiHEhK5kEhuQBE7qHaMYiMBtycnvFRw9RU8DcIDUpRszYeAWCMNqE-ZOW-AV-pk77jNSF6cZNlNkBTryk~32ISoDuvr4~5Ewe2VKrE9WED-TfndLxdB1RD9tXH5-q3xZCQkT6ZvbKBwJYQCiUH83kLQ__&Key-Pair-Id=K3NV4LZ47N8M46)

7.  If metadata has been uploaded, ensure the Identity ID, Reply URL, and Logout URL are correct.

8.  If you are entering the URLs manually, click **Edit** on **Basic SAML Configuration** and enter the URLs from **step 1** manually.\
    \

    ![Azure_AD_SSO_Configuration_image_7.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046355922-?Expires=253370764800&Signature=aRIHkbi8lml0x3Oiu17~mVrDQaZpHn2xIQ26zF-EZMSHdOWj9-nQkykWnu~Nm0dgJFT6osY4oMsoCQ4Tyt53bI4zvlJvUc4h40bJg15PTnag8H1yEteL1AP8RntO1oSOXw1VOwx7zrgN2ASmlrFngiFOmdCs5Ah-6P4EtTmuTXaw709XuHbvkCp~HeUFTsk3YsbmWUuo8wIFvLtoKCWIodufaG6sw39qRFk0N3vNprz8w8UVfvpuwuFsARgkjXl7jTq5RReutpMLpTk1STLZYwIoi17ZZs53aYieivN0-HROHaaUxR4TBl3pwHS9vPrt16znYy-1Lz4tuWOlI7tsEw__&Key-Pair-Id=K3NV4LZ47N8M46)

9.  Click to save.

10. Verify the attributes as the sample below. \
    Download the **Federation Metadata XML**.

    ![Azure_AD_SSO_Configuration_image_8.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046356322-?Expires=253370764800&Signature=sUmILX7fWUluja6buMKul~aZxFhaH1Qzfw0-UR4Ha2pCh9eaeSMHDOLnTbx4GgWfsn7LU0h4Pjtd7vVqpOVyrrnN-4dYGAoEJtyh~sVq876OxRQlsn6p5UC1-93bmJFjGyfuIKb1MJAsD8k005iTwonp9HpiskbE4yQ0YqKZzaWnNjPaYbv0al0BiULMz1aDU5pOyM3LkzDHOAux~MB3iUpa3rzNPEuRsUpI3Q1ZFqb2Cp3dmOY6i3hR16F8aTBmY4TtSN0fnM85HWPLWI04wvEKwSwCFy6FpfejwgdwTPORdfVR~7cPImb17HaUmqIugOVtngpF5EQH2b4z72gT5A__&Key-Pair-Id=K3NV4LZ47N8M46)

11. Upload the metadata file to HackerRank.

## Adding Users to the Group

- This step varies from organization to organization, depending on their security policy.

- You can click on **Users **and **Groups** and add users or groups to provide access to this app.

## Testing the SSO Integration

The SSO integration can be tested in two ways:\
\

- Copying the HackerRank SSO Link from **Step 2**, and trying it in a private or incognito window.

- Clicking **Enable SSO **and test the single sign-on from the Azure Portal.

**Note**: For the second way of testing on the Azure Portal, ensure that you do not close the SSO page while testing. In case the setup is not successful, you can disable SSO on the same page.

![Azure_AD_SSO_Configuration_image_9.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046356674-?Expires=253370764800&Signature=XUzdcmsT5Qm9bS-uVr8cwKV5RgE1AJS6ABKl3HGdkt4Uq8jYd2KGzbTkOZeShN0PsBdJ~znQ8tIp8U04O~nzSekm1IEwiDEvLtL1q-Qk-5-u3PtHZQP~bvhrkEc1Irpg2A5xNY3tzfz4GWJMDSrJ53xMKdY3TZgo~OWsmr~-QWBESweoXZIA4PcPGukTPeD17~zWwP8xcuZ9ejYEVmnAdelKtx~6SPyjpTVWvVw-hJaNogjWAp~Ytme1FuE-Xi4qqz4Zg1IHG~etUhv0cgDsGjSUhd8OIMQ30Sl57Yc5hwmZPku74-mvVVCgsLgovOGpqneKMGxtI5mS78ATrESM4g__&Key-Pair-Id=K3NV4LZ47N8M46)

## References

- [Configuring SAML Single Single Sign-On (SSO) for Azure AD Users](https://www.manageengine.com/products/passwordmanagerpro/help/azure_ad_saml_based_sso_configuration.html#addenterpriseapp)

- [Tutorial: Azure Active Directory single sign-on (SSO) integration with OpenAthens - Microsoft Entra](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/openathens-tutorial#configure-azure-ad-sso)

- [Quickstart: Add an enterprise application  - Microsoft Entra](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal)
