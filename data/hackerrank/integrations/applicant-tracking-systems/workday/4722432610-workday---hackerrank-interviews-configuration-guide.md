---
title: "Workday - HackerRank Interviews Configuration Guide"
title_slug: "workday-hackerrank-interviews-configuration-guide"
source_url: "https://support.hackerrank.com/articles/4722432610-workday---hackerrank-interviews-configuration-guide"
article_slug: "4722432610-workday---hackerrank-interviews-configuration-guide"
last_updated_exact: "Jan 23, 2025, 3:49 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Workday"
---

# Workday - HackerRank Interviews Configuration Guide

_Last updated: Jan 23, 2025, 3:49 AM (Last updated 1 year ago)_

This guide describes the configuration steps to deploy Interviews for Workday Integration.

### Prerequisites:

1.  You must have the Workday Recruiting Module enabled and in scope.

2.  ‘Interview (Default Definition)’ business process must exist in the tenant.

    1.  Search for ‘bp: Interview’ to check if this exists in the tenant already.

    2.  If not, set up and configure the ‘Interview (Default Definition)’ Business Process in your Workday tenant using the ‘Create Business Process Definition (Default Definition)’ task. Refer to the [Workday Community guide](https://www.workday.com/en-us/homepage.html)[.](https://www.workday.com/en-us/homepage.html) Also, you can refer to [additional documentation.](https://doc.workday.com/admin-guide/en-us/human-capital-management/recruiting/interviews/wks1564421850508.html?toc=3.12.0)

<!-- -->

1.  Download and Install Workday Studio on your computer. For more information, refer to the [Installation Guide](https://community.workday.com/node/11810).

## Configure the Workday Studio

Configuring the Workday Studio involves a series of steps:

1.  [Import the CLAR File into Workday Studio](https://support.hackerrank.com/articles/4722432610-workday---hackerrank-interviews-configuration-guide#import-the-clar-file-into-workday-studio-7)

2.  [Add a Connection in Workday](https://support.hackerrank.com/articles/4722432610-workday---hackerrank-interviews-configuration-guide#add-a-connection-in-workday-9)

3.  [Deploy the CLAR File to Workday Tenant Using Workday Studio](https://support.hackerrank.com/articles/4722432610-workday---hackerrank-interviews-configuration-guide#deploy-the-clar-file-to-workday-tenant-using-workday-studio-14)

### Import the CLAR File into Workday Studio

1.  On the Studio menu bar, select **File -\> Import.**

    1.  Select the CLAR file import wizard in the **Workday** folder. You can find the CLAR file at this [link](https://s3.amazonaws.com/downloads.hackerrank.com/ats/Hackerrank_Interview_Integration.clar).

    2.  Click **Browse** and select a CLAR file to import.

    3.  Click **Next** to display the collections and projects in the CLAR file.

    4.  Select collections and projects to import from the CLAR file.

    5.  Edit all project name conflicts if applicable.

        - Select a project with a name conflict.

        - Click **Edit**.

        - In the **Project Name** field, rename the project.

    6.  Edit all collection name conflicts if applicable.

        - Select a collection with a name conflict.

        - Click **Edit**.

        - In the **Collection Name** field, rename the collection.

    7.  Click **Finish**.

### Add a Connection in Workday

1.  Select **Window -\> Preferences -\> Workday -\> Connections**. If this is not accessible, you can do the following: Go to **Window -\> Show View -\> Cloud Explorer**. Click the icon in the upper left corner of the **Cloud Explorer** box to open **Connection Details**.  

<!-- -->

1.  Click **Add**.

    1.  On the **Add Connection** window, consider:

        - **Option** **Description**

        - **Name** ** **           The name of the connection.

        - **URL**             The URL of the connection. - [https://workdayinc.force.com/partnercenter/apex/PartnerPortalKnowledge?id=kA04X000001DXF4SAO](https://workdayinc.force.com/partnercenter/apex/PartnerPortalKnowledge?id=kA04X000001DXF4SAO)

          <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046123055-?Expires=253370764800&amp;Signature=OHkqvD51b3dcdSQz5V5WMXv38XSTrs~ajPWd6uXe08HG5Og-xaQR2YtHdLPIRy~5MrtYkg4Xhb64B6dUveWh2z0Tc7QDd~T~Sc2cTOwECyenLp882p59aJip9ADOq4hqvXqCdao0M~UK1XXH35kW~IJnJooAqeRnTkyktGX72qVDcE-EkyZd1s6g6LJTfi6fxl2nTc6H1OaG09Nd59Ew4kTR362AUTfAuJYIsTWpJVP7H35JajljdE9xL0jQx7MBtZwi76LneLXeIYP0Myj-zCIXvENUgii-dsfgUP8Irr-UEyCymbstinEbvdFvXANgbV-gwPdAY61RIViWwZNcIQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

        - **Group** **           ** Adds the connection to a group. (Optional)

<!-- -->

1.  In the **Credentials** section, specify the Tenant and select an authentication method, Basic Auth, or OAuth 2.0.

    1.  To use OAuth 2.0 authorization, you must first register an API client. For more information, see the [Workday Community Article.](https://doc.workday.com/admin-guide/en-us/authentication-and-security/authentication/oauth/dan1370797831010.html)

        <table>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <tbody>
        <tr>
        <td data-colspan="1" data-rowspan="1" style="height: 22px; width: 19.2926%"><p><strong>Option</strong></p></td>
        <td data-colspan="1" data-rowspan="1" style="height: 22px; width: 47.2669%"><p><strong>Description</strong></p></td>
        </tr>
        <tr>
        <td data-colspan="1" data-rowspan="1" style="height: 22px; width: 19.2926%"><p>Basic Auth</p></td>
        <td data-colspan="1" data-rowspan="1" style="height: 22px; width: 47.2669%"><p>Specify the Username and Password for the connection.</p></td>
        </tr>
        <tr>
        <td data-colspan="1" data-rowspan="1" style="height: 134px; width: 19.2926%"><p>OAuth 2.0</p></td>
        <td data-colspan="1" data-rowspan="1" style="height: 134px; width: 47.2669%"><p>Specify these details for the connection:</p>
        <ol>
        <li><p>Grant Type</p></li>
        <li><p>Client ID</p></li>
        <li><p>Authorization Endpoint</p></li>
        <li><p>Token Endpoint</p></li>
        <li><p>Access Token</p></li>
        </ol></td>
        </tr>
        </tbody>
        </table>

<!-- -->

1.  Click **Test Connection**.

    - The Studio confirms whether it can access the connection.

    - The user needs to have certain permissions to deploy. Refer to the list in Workday Studio to ensure the user is a part of at least one of the security groups for each section needed to deploy the CLAR to the tenant. For more information, see the [Workday Article for User-Based Security Groups](https://resourcecenter.workday.com/en-us/signin.html?fromURI=https://signin.resourcecenter.workday.com/app/workdayciam_aembetadoc2_1/exkd1j067lBdQMGYl4x7/sso/saml).

      ![confg_guide1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046123389-?Expires=253370764800&Signature=EUXEZqRnzLkuE~eez1n1v8ZPep6egPsCxsCW5S1-0S9TY7ot3U5L7sn7qnusVsZWqvxoKrOotYxx0VCpGCWsvSDSMfm1jtg-zLfbb5KlYWNu94xsccY9bj14fKAK~YEuoyR94cz5f5bydBD7mmSZExvmiY17SJI9sdxtS64XgQ9-b~xq4B18mJzDn~ag7wAf23EQLXBBk4s1kzR1m5Px10oOrpvweECcE1~KYibtwFRTgZW797EUAv7kyu8GOFZZHbawWpDp96eUAxSDGDt8oVV66SZVPYB4ikBBxJXnMSbpshy-rrG0PliksekDbfqJcy~WS2LsYV954gIdSev9TQ__&Key-Pair-Id=K3NV4LZ47N8M46)![confg_guide_testconnections.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046123815-?Expires=253370764800&Signature=F-EBc0fAOy1MSKm7Q46k0segf5G7WcefhZIbtd1rKrvA1-j4bJMCGG4gPxz8zC5IH6xkzykjOanHVLLJu5W9nsaAyLG-~bhIEHIn6uG0XuR6jJq0JrgeJXzDNG5yTrvsXCFIv7d-GM5cgwrIHBIG62Ip44TOde9CE1HquKpQVg7CCynDbQLP~8cC6fyKocR5LvDJoTFk-rtQYmQKKnDauThdo4js3E0FxIFk7tpgYFX0mufN-pgpctM2NHB68-EsFzVY1SynIGXNNQSCfq~K3OdRaoCznTOF-l~HrRcFJpfa2D0UML2GBK6tAu-h93FZFWY69D5bljnf~IgbhUszzw__&Key-Pair-Id=K3NV4LZ47N8M46)![confg_guide_testconnections2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046124227-?Expires=253370764800&Signature=BoSpt7spaRVeZ4kQ-dhM065aL2eInLZCxmdPYp3etfD-JxgwoVX1fCnHagbyPikL~xmLuI4UwnpScKuRJSnJmphEmtw1V3CbdFgnhd-d~O~JBEENe91emeAFBwrUh-rA4pdTrAFCcWbpl3p43wFO0B9bGVkaMacjRQ8XlpxRaFxsv5XAt8E2HpXSJ-XV9JDuFBH-MxJ1mebVFoYf2hlaGupGJt8wxvBn~XjsC3s1Xr2PoIFZYM-cZxAk50nn90DeMP-vwAV4Oeuwkf2KoQaIwFkTLO96vimPBvgnSOhRV~17U0LP2yXrJTVi0gvwgthVVvR0~jCghU9R9ONx9QbXnA__&Key-Pair-Id=K3NV4LZ47N8M46)![confg_guide_testconnections3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046124704-?Expires=253370764800&Signature=c-CjTRGsZJmzEcQrzWyj0hoNPNwiK3Crxs6Z3JqwApI1wuSiS3khoSJwiTpnQYk5XSdmyfSqZUVVjtYTHyWvuSkyjLr-QBSBeYKbd-od3lZSgFTQVZX4idKflZAr6QI5O-A465o1gHTo1UIHlAq4ehm5m5q-tUDWIwsz5JCwaFDEaOteh6Tkd4HKGaw9ITbkxU1g7D5QlOdniJJXffZ7~8b8xmS73fj-RocSUTimP705yjgBkDe1iXnuj3BruylRxAomjU7P2Ap0ebBN5reXHcUhTC1ZAqcpoa5YvHjnPPI0iT6ax-bihf~zpTxqNGEvgrI2v6pdGWXoEGEqkBOTPw__&Key-Pair-Id=K3NV4LZ47N8M46)<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046125142-?Expires=253370764800&amp;Signature=UoiXQUoY4054xcJu9ky4PmzPtgZIPjsKgnxNRUVja0muCV1Q6NIJZj-NNoIB15156WQXVCzVBGAncloHXAuOgUgCINdRsdZjqjXihHAVP59z2qgF8iIairwhI-t7tVrc~ddJ~fX6EGfie7MF6SQ-BDCXKbtjORz7bZ5pUdXd-YDA46ZuNXlB~yduuaH2ZhIWxiepfP8DXfsYKSk8uSWrAZr5UeY0EssIdwLIsZrxvbnpiZMoQUIirQAKeWmGGJdgqWX5cA-nNeQKBMVgpZEXGb8HzmTNItO-HkpM258UC9lagydCLwbc2l9bQ0DanmacJFFKhltf--at6-fBjbrT~A__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

### Deploy the CLAR File to Workday Tenant Using Workday Studio

1.  Deploy CLAR to Workday Tenant by right-clicking on the project in Workday Studio and clicking **Deploy to Workday**.

2.  Select the Workday environment you wish to deploy the CLAR file. Make sure the option **Include source code in deployed CLAR** is selected.

3.  Click **Next.**

4.  Make sure your project is under the **Configured** section.

5.  Click **Finish**.

## Configure the Workday Tenant

### Prerequisite

You will need access to the domain ‘**Security: Security Configuration’** to perform the following steps.

**Create and Configure Access for an Integration System User (ISU) Account**

**Note**: If you are unable to perform these steps, then update the security fields accordingly. If you are not able to access a specific task or report that is a part of this guide, use the **View Security for Securable Item** report to review the domains required for that task or report and the security groups. 

1.  **Integration System User Configuration:**

    - Access the Create Integration System User task and configure a Workday account for the integration.

    - Name the account as “HackerRank_Interview_Integration_User_Step1”.

    - Specify a password and save credentials somewhere for future use.

    - Keep the **Session Timeout Minutes** to the default value of zero to prevent session expiration. An expired session can cause the integration to stop before it completes.

    - Select **Do Not Allow UI Sessions**. This option prevents the integration system user from signing in to Workday through the UI.

      <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046125470-?Expires=253370764800&amp;Signature=LhWwERvSxrzkUCSBpZr6GHZlsaKydBc7CA09s5d6kb1nsC9LDiwnSVtdq1B9ynUibHQeNg4rh9B9M8kDNU7XBp-TW95UXoK2yUxYfQV0K-UA82SRYiBngUbDPkDgkHGmiFoLHhcuXyG0vdeUg-XNyrIs3xSof~s7QTf5mGomYb7Et3J3BpwtkLY-xPEEI92hCq1e8~D14YFVLVUvCripspzPz5LLGJU9qFlI~UlwRIpoK6Tab7Eh~8zOIsWAduOzs9m5E8CowPl2tdnTQr173lMY-mvqY2pal5tiOsts-wLHN9Gj4MbVBCSlgOyB9~slUPjcmER5leBBLOlgcE44eQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    Follow the above steps and create an additional Integration System User named ‘HackerRank_Interview_Integration_User_Step2’.

2.  **Create Integration System Security Groups (Unconstrained).**

    - Access the ‘Create Security Group’ task and configure an Integration System Security Group for the integration.

    - Select the type of ‘Integration System Security Group (Unconstrained)’

    - Name the group as “ISSG_HackerRank_Interview_Integration.

      ![A screenshot of a group Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046125817-?Expires=253370764800&Signature=gXRndnACieXePBqwNrauHQPEFy2X82tB78I8UqS-oO0zD7PyUBDUKc7r4DhGCJdV0RJZZFqLg-GF33Z3MtV0t7vIdVPQU~sM~AA2Wuor-KpSjQ7Giv2s2EUfCOWooFAme1NowQNp7Jcx5r8wS3c72CCvPiZ-V~~BhCFx610UwUwoRBjFTSou257Fc9XZrgAdopRWusCMcW-xhYXi2Q1cAzGxPxEzD4Cn6SWrh7IZPiPem0CoRjySxWr-03eNDELKy71~3Q1NXRLyp2rCxBrb6EZ3362ESx1a9av3F8vkTydcW33LB~fy9T09rWlwaOGA~YgTS0GQbUy5WFK0xfGAmw__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Select the ISUs you created in [Step A](https://docs.google.com/document/d/1IrNn1ZeGfUsSf76WNQMDD2-QJUEbaZRkjhwLjCTc5Z8/edit#bookmark=id.uxfve663sjpr) in the **Integration System User** box.

    - Click **OK** to save.

3.  Edit **the Domain Security Policies.**

    1.  To grant the security group access to the domains required by your integration, follow these steps for each domain:

        1.  Domains Required:

            - Interview Integrations

            - Candidate Data: Interview Schedule

            - Candidate Date: Interview Feedback Results

            - Worker Data: Public Worker Reports

            - Person Data: Work Contact Information

            1.  Access the **View Domain** report from the search bar and find the domain.

            2.  As a related action on the domain, select **Domain \> Edit Security Policy Permissions.**

                <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046126100-?Expires=253370764800&amp;Signature=V7mRnbC9cIplltpKIyX8Ut4tj33YM1S12~60qRo1HA99e7sNItj4DYLdS3Ue4H4XnrnuLbkrclbaA8Jw8w0rnRDr4Xb1fuKGiBcs6sjlFMrWsDhhAXQ5vpZZ3BLTg2rPkxAaTphWDTC~Ww~1zyJxmGxLG5aewkCaQz0O0QTwc6lqxCdEyh0IL3q3vR1vjIBahtJIFwPsc6i6W5IWdExzG-8jB7wcByxK-IzheDNBloR4S7HOXy65FOtZMj~iNMqUHxrdrJ9AZaMJOo-5ExT98X4IbYwuPLtJMtH2z5n2AbLUKBPB3pjo-WP1xLrHA9YzhojZMD4hZmWy9q95vV2ONw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

    2.  Add the security group you created to the Report or Task Permissions and Integration Permissions. Select Get, Put, View, and/or Modify based on the table in the following step.\
        \

        ![A screenshot of a computer Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046126452-?Expires=253370764800&Signature=kyR3QSB~lbDUjJu3uqtGiS5rVQk1~BymsFUGfeuQF3EXEjfqmrXIg9lR5DWi~88mSXqJ7IOwtK6wd69bgDO89VupGRTYUN5-c3RYe1JcOaNStrEbtIvDoGYy76ElI-PAdGvFqPZtRAtnJhg2wyhuECNks9eVJdV9GkcfkJO25H6Mi1kF51QYoNFF~qQ4fHvkWQ8-AXJTKnJ6PuB1~x7wGe0UR6OjLUYfX2Mo82Pb0iQoCCKz8csaEL0n0TZ3GgmdJVdoy4vJ51sYbZuTWteHqVhBmibRmzHtsF41KhO2xqdVToaPxq7UF69UMZjOLhsSqIqMLOPXWLMQ8PISk-EtwA__&Key-Pair-Id=K3NV4LZ47N8M46)

     

    - Activate Pending Security Policy Changes.

    - Access the Activate Pending Security Policy Changes task.

    - Describe your changes in the Comment field.

    - Select the Confirm checkbox to activate your changes.

4.  **Access the Maintain Password Rules task**. Add the integration system users to the System Users exempt from the password expiration field.\
    Note: **To avoid integration errors caused by expired passwords, Workday recommends that you prevent Workday passwords from expiring.**

5.  **Assign ISU to the Integration System.**

    1.  Search for ‘intsys: Hackerrank_Interview_Integration_Step2” and click into the Integration System.

    2.  Using the Related Actions off of the integration, navigate to Workday **Account -\> Edit.**

    3.  Select your ISU named ‘HackerRank_Interview_Integration_User_Step2’.

    4.  Repeat these steps for adding the other ISU for ‘Hackerrank_Interview_Integration_Step1’ Integration System.

        ![confg_guide_editaccount.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046126740-?Expires=253370764800&Signature=BHBMwpwaMiTHy4od6Pn38Qi~Or-FbQWluY6PelqbFlQJ7ebszAkSXjTxJCXc6Zx29Bux6MMuZdEdQq8AP9a5gh56-yW6EHTGiszJPO9O36FyyzDD0SNKMAj0-f7UUSkrfbO289Cr77BZ2Ueaf0438EEMJZS0P12X8VJZrOuUxEqVc5ZldVFCfEm5P7NJSnoew-zIYW1bD7fP~lSbLm2rABwEcJ9XtV3nlJH6aQ9hz7Y-iIYxrQ3GOncD8nwGSfiDDWopsfm0gF7YCBuP5NI-hjl06QGxvEuqp-KsXlmeHcQBqP~kC~dWXq3F5QxbmuCZGf8aK2gzcTS5VzyXAv97Ig__&Key-Pair-Id=K3NV4LZ47N8M46)![confg_guide_unknown.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046127179-?Expires=253370764800&Signature=iYXqcQP210E-c2TlLerCUQuYAhZ8gMW8qcTQDgWqueQGa~aEK8GL~v8Ruvugd2pPQsLl84AiYxBtkUMJoabLgbVq8Fcu3BM6GPNv-pMx6Z6d66d64IkmWTnByq4J4dOoRfhvlcuam3Gm3DSP~nLbMWCLKacDFs1ZtbuP-1dguekZaRalY4STdr1iFWTXKUgEFj6glqC5Co-2r19SSZKAm5ie~CpEmb8t6s7wpFDuZiq~xTwBHcLzZ9Npp7p8dpF1aO~SxTe2CIlA4DHu3EkpIXGkaeS6C3fQpeUGY~fBghmwTxTe2bEu6e4SAv9zHNtWRnlLc35yDfkRKJR5xvaaCw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  **Manage Authentication Policies for API Access**

    - Navigate to ‘Manage Authentication Policies’.

    - Edit the authentication policy for the environment that you are currently working in.

    - Create a new Authentication Ruleset using the Plus icon in the top left corner.

    - Provide a Rule Name.

    - Select your Integration System Security Group created above under ‘Security Group.’

    - Enter a value for ‘Authentication condition name.’

    - Choose ‘User Name Password’ for the ‘Allowed Authentication Types’ section.

    - Click **OK**.

    - Navigate to ‘Activate All Pending Authentication Policy Changes’ to activate your changes.

      **Note**: If this is not set up correctly, it might result in issues with HackerRank making web service calls back to Workday. If there are issues with authentication, use the ‘Signons and Attempted Signons’ report to troubleshoot the failed sign-on attempt.

### Add HackerRank-specific Fields to the Integration

**Note**: Refer to the [Configure the HackerRank Settings](https://support.hackerrank.com/articles/4722432610-workday---hackerrank-interviews-configuration-guide#configure-the-hackerrank-settings-page-39) section below in the document and complete the setup in HackerRank to retrieve the access_token and Company ID needed in the following steps.

1.  **Search for the integration in the tenant by searching ‘intsys: HackerRank_Interview_Integration_Step2’ in the search bar.**

- Add the ‘**Access Token**’ provided by HackerRank to the ‘Access Token.’ Integration Attribute using the Related Actions of the Integration System (Integration System -\> Configure Integration Attributes).

- Add the ‘**Company ID’** provided by HackerRank to the ‘Company ID’ Integration Attribute using the Related Actions off the Hackerrank_Interview_Integration_Step2 integration system and doing Integration System -\> Configure Integration Attributes.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046127669-?Expires=253370764800&amp;Signature=pIZLOSooW7lE5bLyRsfV0sJ1ZMTLiyqwW1c~SQujWMqQgkX9IAiQ8ytZfRfC3HW9Se3XosF5ZLPzcRTlEP9frG-q1x2VWYHRHgM63roqY8dq1oFusXoZtAtjwD6SiolBE6kCEdJ8M1AnhMksMzBNP1RnHmHSJEu6~W-R6PFaKAi553cLRPeP11re7ETrkgHyZLO~jpXobu1tB7ZDgGstyXjlj7FnjJCR1uLgKFvU~a9xbtYNTvBfQ4ScN-lN7CRd38fFVASwdEUF50O3hPRANHh4NfN00EppTsJ-JbKfR4PvJz6cFbRxpGWYjpPjIzEvZNzwapA~2U-dsRhalA~2JQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

1.  **Access the Register External OAuth Client task.**

    - Navigate to the ‘Register External Oauth Client’ task.

    - Find and select your integration system named ‘Hackerrank_Interview_Integration_Step1’.

    - Enter these values provided by your HackerRank contact:

      1.  OAuth 2.0 Client Name

      2.  OAuth 2.0 Client ID

      3.  OAuth 2.0 Client Secret

      4.  Scope

      5.  Authorize Endpoint URL

      6.  Token Endpoint URL

    - Click **OK** to save.

      ![workday_new_ss.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046127983-?Expires=253370764800&Signature=nVg9rVtppI5Osfo5z197sC5PMMG6myyI8CKuh08izirymgaJKGnEwfU8XcvzTebKGU0QtsJkMYCwCR2YaTny53wobMuQXadMqGxvz5H44t08ZRKyTY9sRBOH9x1U7qgopyxGU8toXa9lOW-4he4FvJuQnqKdXc6NbaZfHCOXYsBjact3nFCKP0l~yRDy76TadpBQ5EQFOB~66NsaqF3IDF9GPRLrCPj4MaRTxBZ697FRsF9~SEcfVJVTH0fCfOnwgKXGPUjb7P8dWMgPartSUqvQNjA4aVHG2rZGDxvt9U1nVAOu9M-R-ZiG56ONVldjBQ3FRjlaTajFJoP4TbiXRg__&Key-Pair-Id=K3NV4LZ47N8M46)

### Navigate to the Edit Tenant Setup - Recruiting Task

1.  Select the integration system named ‘Hackerrank_Interview_Integration_Step1’ from the Web Conference Integration System prompt and save.

    ![confg_guide_webconf.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046128305-?Expires=253370764800&Signature=CL9gHEOuwsWi8rXbkyGl~MVjTPs99SOleVmr0i9KyQZn~g~n1cY3M25CQC387J5KaghdfuFFueHJmVHn99P-2FDVsKHrSMRisPIbj7BVPJBYPKWbLwcYt0r3dHGoczI7twLrU8vcEJAOTzaMf3ywfO5QtUeqeGU4UNSWT7T285T~mLfkfj7tmwG5OyWGT1zF8WeP2IYK68yo4Y5vGNOu9GLrZ~yYWCpIOBrxCZ7VI4yjIq73VRM7eTGcKnqKcJRtFconRJkpIS~Sx97AVxZ~-QkVymMavuyF-VIBlf3lmqD4QLzq5I2hvuhBHBEu4VOfWWn~5C9Qu9a3KcI6Uv3rDQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### Build Calculated Fields

Build out the following calculated fields using the **Create Calculated Field** task using the following screenshots:

1.  **Field Name: CFI LRV Candidate from Interview**

    ![A screenshot of a job search Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046128609-?Expires=253370764800&Signature=KMdK2OmkvqoGG7ub41AcF4A3ZDkbAWLElpitsVHse5kxqYgY3pYH3CUYTRppM0YnxuSYBUoqrayKn~ycNXzyFXKyKkzPmP9pCxxGr6QrQFRXfDNv8Vi-pNW72GFxlZdIjPZ4RstVf510jSRqpBFA5PNQwyj1tIe3VZ33hR9Hfq42Sqf6iuLPCprZUYthiBtIcYsf0w6xGalILdgGRgxIQjkp31jmh2d08yyh-VcM3IMoswdm3jn1-aumwsjwZF67TlZWnhkND2SALZiPNZ7DBhJd1IuwpIfortZrs9Ra3uI71QHXSryeJvsxqW18GtyXLWL1m5vJ6OUAAHPlY6AkzA__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Function: Lookup Related Value

    - Business Object: Interview

    - Lookup Field: Job Application

    - Return Value: Candidate – Field Type: Self-referencing instance (Viewable from the Related Actions off of the field)

<!-- -->

1.  **Field Name: CFI LRV Candidate Email for Candidate from Interview**

    ![A screenshot of a web page Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046128892-?Expires=253370764800&Signature=C6LrvCJyBfeyHlXTkixYeq0RFOub04C63dhv-ZiJpeKm7mIv81UTQz2rjfgob2w5BTMJK2CnHUzCBfpYSIBuuRciBwSgJBo1KxrMDytZZDen1BSiWygIWU2QWUzR1AOhxQihVoDZn6rZJAj~cVFHZOSnQhGU6zPD8aok7mfZS0nJ8tQXld9WhIq5zfOVIdqqRzsP9ccDYW09qfn0YonF-3pCuh5dTUk5Np7oK7C5OTcYuexxgldp0vjG63sb7vMfg7n80nFWzUj0Tm4sndpQ~88bkNTva10xCA272-NitenMsVVRORURvaZUisat5oHUn3tCNGW1l-zx40dJXUE~0g__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Function: Lookup Related Value

    - Business Object: Interview

    - Lookup Field: CFI LRV Candidate from Interview

    - Return Value: Email

<!-- -->

1.  **Field Name: CFI LRV Recruiter for Interview**

    ![A screenshot of a computer Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046129255-?Expires=253370764800&Signature=BmT8xtx48UYW2yskW3M3rJNKr3E~e5EiNTHZkdulOzyrXQHD8Ntqg5KueIPdFEmWzEIgQe~5QVAyzHVZkYN12ywRXhL0UTMrq2tUOTQ35ifAtDTjnPtTZTZ1cbOlLwR6brUw5IE9S8jROTyAjkmT9ncVZu6QJBgiFSRwMsZ21EtQzU5vWbPHasmTjqLhOdl~Rer8uucQlbI-G5r9A6bPnsv922-7TLTYxdq196Eq3Zs2Pk~xlgK3vjemLCxrUMHMbTor5mevkehQmpf8QWwRIUOyjAIEZQ18sfl8ia1~CE6qTT-rpqIK1fJ05KKzPPpU-vnlv85fYvwx4foUshuqhg__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Function: Lookup Related Value

    - Business Object: Interview

    - Lookup Field: Job Application

    - Return Value: Recruiter

<!-- -->

1.  **Field Name: CFI LRV Recruiter Email for Interview**

    ![A screenshot of a computer Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046129551-?Expires=253370764800&Signature=XhPnj30GcMcIl6U0pvLB5N3-EwdAVLlNu8T0TvLeXct-~3MdJNaQRlpVTRx5Zy4zqEU5BideUy-L96JJLvXpRa02iLA26M1DwJHU5n8nkOTW-h5mn-prlsm7G3H7wzz7lgyEN5E8R8gSVkW5xzdOCRlOZadmMASde6yv0EF17TaRBwpctFy4aaqsLJ3-0zZ-oDry04FTKL4IySDWSgMvECAEUwAxFwGE-LHTk27zMF~2bnpA4VtC~N1Z9JgElerwZJoga47Jpggmv5798maSjzzxsanBrlT0DQ5J31qwvyHfNLUKkvsOq53r-ytxlz037RJZ~AzKwTiliNiqMdu97w__&Key-Pair-Id=K3NV4LZ47N8M46)

    - Function: Lookup Related Value

    - Business Object: Interview

    - Lookup Field: CFI LRV Recruiter for Interview

    - Return Value: Email - Primary Work

### Business Process Configuration

**Note:** Workday recommends the following setup and has been tested for the integration to work. We recommend keeping all the steps mentioned below in the specified order. If you have additional steps in your setup, make sure first to test if the integration works for your setup.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046129895-?Expires=253370764800&amp;Signature=pzExGMHhLleUMjuIgmNENxi6IgiAtkUmWYAQwQiO0BHPqVBg3zgjQa6A8RLfcWfAmPnYx5s9XAT8y5Ejv7~P2MLtoVcg1yL0vDZcCuu0XN9zzsv4iKIOQwq-qsEm5VZIUWTDqamCIFSh9rXH9wZ3Df6NZYgH16gbDchuk9KWZjI-dukPQZllK1TiTL47JFzHSdrkY2CiLZlpnLXBLMNuEfQqBfihfTxclkj3WllYqr6r3YkVEP~x9GDf-SarwGM7Y4prW4BHcNeKfrGkSC6lDTFCNf8zpaDKQKuxUK7b4DEqmZX9Y~q7nYi3MQVzdCUNKnJXgYzon-ZEidFEZx313Q__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

1.  Search for ‘bp:interview’.

2.  Click into your ‘Interview (Default Definition).’

3.  Edit the business process definition using the Related Actions and navigating to **Business Process -\> Edit Definitio**n. Click **OK.**

4.  **Set up Schedule Interview Step:**

    - Add a new step using the Plus icon in the top left corner.

    - Type a letter for ‘Order’ that places the Schedule Interview step after the ‘Initiation’ step.

    - Select ‘Action’ in the ‘Type’ column.

    - Select **Schedule Interview** in the **Specify** column.

    - Choose a security group for the **Group** column that should handle the ‘Schedule Interview’ step.

    - **(Optional**) Populate the **Due Date** column.

5.  **Set up Integration Step:**

    - Add a new step using the Plus icon in the top left corner.

    - Type a letter for ‘Order’ that places the Integration step after the **Schedule Interview** action step. For example, if the ‘Schedule Interview’ step is Order b, make the Integration step Order c.

    - Select **Integration’** in the **Type** column. Click **OK**.

    - Hover over the magnifying glass for the Integration step and click **Related Actions**. Navigate to **Business Process -\> Maintain Redirect.**  Click **OK**. Select the **Move to Next Step** and **Rerun and Integration** check boxes and select the allowed security groups for the redirect.

      **Note**: If there are no security groups in the drop-down, click **Related Actions** off the Business Process Definition and navigate to **Business Process Policy - Edit**. Add the desired security groups in the Redirect Action box.

    - For the step that you just created, click **Configure**.

    - Select your integration system (Integration System Name: Hackerrank_Interview_Integration_Step2) and Click **OK.**

    - Configure the Integration Criteria as follows:

      ![A screenshot of a computer Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046130252-?Expires=253370764800&Signature=ZfetuH2Opz5C0LeXgYNN2w9cwcs9ki73p2rS8rNGOYAO0tjcgksguuW1afuxdhMqQ90TN9LOzOjyRriITl9OOIMovrrwKNtLVCeW7Rrfy5-nC0JeffclL5IZoCVvPWuRABI3ZaIldlMMrn~rM75MIOembxSE2g6MJ50FxBhIP7wvXGRyHGkDCtqAUtRfnyRX9DiR7E3fEarukirNl0Jdm70V7xpypZgfkaJiHDbZyGbhWAZePbistx6Bt5Mw-wiBwMS6yDDLYHKSnXAs3UpwtAU4ko4raWhwck2i9V1so2NhQGHLa2LXthfC2s4VlqPO3Dj7gPKwzr1Fw7~fnIPDyg__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  **Set up Manage Interview Feedback:**

    - Add a new step using the Plus icon in the top left corner.

    - Type a letter for ‘Order’ that places the ‘Manage Interview Feedback’ step after the ‘Integration’ step.

    - Choose **Shared Participation** from the **Type** column drop-down.

    - Choose **Manage Interview Feedback** from the **Specify** column.

    - Choose the appropriate security group(s) under the **Group** column.

7.  **Set up Make Interview Decision Step:**

    - Add a new step using the Plus icon in the top left corner.

    - Type a letter for ‘Order’ that places the ‘Make Interview Decision’ step after the ‘Manage Interview Feedback’ step.

    - Choose **Action** from the **Type** column drop-down.

    - Choose Make Interview Decision from the **Specify** column.

    - Choose the appropriate security group(s) under the **Group** column.

    - **(Optional**) Populate the **Due Date** column.

    - Click **OK** to save.

    - Hover over the magnifying glass for the ‘Make Interview Decision’ step and click on the **Related Actions**. Go to **Business Process -\> Set** and set as **Completion**.

    - Click **OK**.

## Configure the HackerRank Settings Page

1.  Use any one of the Integration System User's Username you have created.

2.  Use the Corresponding Integration System User Password.

3.  Specify the **Recruiting Public Web Services Endpoint:**\
    Search for the ‘Public Web Services’ report in your Workday tenant. Navigate to the **Recruiting (Public) Web Service**. Click on the **Related Actions** next to it and navigate to  **Web Service -\> View WSDL**. Search for ‘soapbind:address’ in the WSDL.

4.  Enter the Interview Rating IDs from Workday that should map to ‘Pass’ and ‘Fail’ on the HackerRank Side.

    1.  The ‘Maintain Interview Feedback Ratings’ task can be used to configure the ratings initially. After setting up initially, the task can be used to update the feedback descriptions only.

    2.  Navigate to the ‘Maintain Reference IDs’ task to update or view the reference IDs for the ‘Interview Feedback Rating’ business object.

**Note**: If you move tenants, provide updated credentials to the HackerRank team.

\
