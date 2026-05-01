---
title: "Workday - HackerRank Tests Configuration Guide"
title_slug: "workday-hackerrank-tests-configuration-guide"
source_url: "https://support.hackerrank.com/articles/1782819445-workday---hackerrank-tests-configuration-guide"
article_slug: "1782819445-workday---hackerrank-tests-configuration-guide"
last_updated_exact: "Mar 26, 2025, 11:41 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Workday"
---

# Workday - HackerRank Tests Configuration Guide

_Last updated: Mar 26, 2025, 11:41 AM (Last updated 1 year ago)_

## Overview

This article discusses the configurations required to set up HackerRank and Workday integration.

The configuration guide is broadly divided into three sections.

1.  Workday Security Configuration

2.  Assessment Configuration in Workday

3.  HackerRank Configuration

## Workday Security Configuration

Login to your Workday account and follow the steps below to complete the security configuration for setting up the integration between Workday and HackerRank.

1.  Access the **Create Integration System User** task and configure a Workday account for the integration.

    - Name the account “HackerRank_Integration_User.”

    - Keep the Session Timeout Minutes to the default value of zero to prevent session expiration. An expired session can cause the integration to stop before it completes.

    - Select **Do Not Allow UI Sessions**. This option prevents the integration system user from signing in to Workday through the UI.

![A screenshot of a cell phone Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047141270-?Expires=253370764800&Signature=B2rkHj~qMkO98EI529HrHRGML-qtjGdyz4c~pZ4r8azr5BEjKiuAv1QCohREY945STnk3oMaQbmBbDnDVqUYx--b-zX543GPyXLVmH1e84BtoUkxd1q7pISnSYOC6GqWBie7W5hTNeUUK20HKFuXH59x~CR9bJHQ2sNK8sy3auvLN0-dnRKP3KFG09C0qJW9fY7OduvSmqETzSrmZlOLRWRRaTZA-ntNaws7ZGLLe48jE1KDoOXmDzSxMB93SnNfQZ6NzKSyz5I16HH6BaqxMUL90iD4tUmUpDtBFGhtz6-IruTNtqNHrvHVNmd~na2SZCeno9nA9z2glZMN0pO2ng__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note**: It is advised not to use special characters such as "& (ampersand), = (equals), ?(question mark), % (percent) / (forward slash), \\ (backward slash) while creating an ISU password for Workday.

1.  Create Integration System Security Groups (Unconstrained).

    - Access the **Create Security Group** task.

    - Choose Integration System Security Group (Unconstrained)

    - Name the Security Group “HackerRank_Integration_SG”

![A screenshot of a cell phone Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047141646-?Expires=253370764800&Signature=QC4ozJacipcXeXVcdq-Gdj41ms478nSE7Vd43roB69f194N61PwIkMvlhL7-ea7ABomc6juhrpkd3ENwN0p7c8IuC5UEtL-L1inVDFrm-4Kra5tKp3i3LKcjqZRje15ZFu9ECJqE7GnOsZBExvLVuNnazD-g805vZFCb-fWsruuiw4FoQQUVCgOQ4H2imJ45SWJDs8XcPqYK9mm6ybto61T5WhcRSwbgA5TgIs1eCSIH5uja8uY-~D4Zbj5CdBW-BY9FmcjoGiBHirafFHhdWJrWO64Xcq960KA5zriuNAU3FHYplRCOhjOZug7~ko1BBlUXEEc0rf20QP~Qo6e4EA__&Key-Pair-Id=K3NV4LZ47N8M46)

- Click **OK.**

- On the **Edit Integration System Security Group (Unconstrained)** screen, select the Integration System User account *User HackerRank_Integration_User* to include in the security group.

1.  Edit the **Domain Security Policies**.

    - The Domain Security Policy permissions required for the Security Group are:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 41px"><p><strong>Functional Area</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 41px"><p><strong>Domain Security Policy</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 41px"><p><strong>Domain Security Policies Inheriting Permission</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 41px"><p><strong>Type of Permission</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; height: 41px"><p><strong>Operation</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Recruiting</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Candidate Data: Job Application</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Candidate Data: Bundle Resumes</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Integration Permission</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Get Only</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Recruiting</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Candidate Data: Assessment Results</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p> </p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Integration Permission</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 41px"><p>Get and Put</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 144px"><p>Contact Information</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 144px"><p>Person Data: Work Contact Information</p>
<p> </p></td>
<td data-colspan="1" data-rowspan="1" style="height: 144px"><p>Person Data: Work Email</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 144px"><p>Integration Permission</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 144px"><p>Get Only</p></td>
</tr>
</tbody>
</table>

- To grant the security group access to the domains required by your integration, follow these steps for each domain:

  - Access the **View Domain** report and find the domain.

  - As a related action on the domain, select **Domain \> Edit Security Policy Permissions**.

    ![A screenshot of a social media post Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047142241-?Expires=253370764800&Signature=TuBu05opnytjt6qG~0CkpT48K5jgJscvBf8awD8fzm515M-n9bZ4Md-Rw9omIQmCAxTSIqteFmfdGVkDyfe0XRs-1Du4kndT7crUqv-FV9~yOOpuF1ALdk39yIjYHO4EsJ8~~0zpDMZFiI5x5jSIE~wTlQqMcIC8rreQBaDWNkydwTVieiSyVe9Wqh6I6xFxCVXDtEtQIblwcvqqf9ZjmhU5DpDlkjbGUkDhrghJDYny2Ys2uLcJxAkwXjbZ3xhRq8bivLQie-JwTzRTkr8tywedBEZWfHKY~nclcWzIuC6alY9KpjNuiWKONGkiUon8OorPdNieeU2BUamDmhXccA__&Key-Pair-Id=K3NV4LZ47N8M46)

  - Add the security group you created to the Integration Permissions and select Get and Put based on the table above.

    ![A screenshot of a cell phone Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047142577-?Expires=253370764800&Signature=WNfSlFcDoPEewcGq1vkz~opiOgvOxrtZ0CC9votCKp7-2e9uigYDwiI3xmywgPCfqvxBaaYqg5q352YQlngfHgdRF5deLWfGj~yRSKnlQ1SY~Y1BS8WKq6uocGsCae0zeCX7a2S5EV-EhBCNX8YqcXudCL9wdlU48KtOijkHnqcAGick5ZlsHvs3OY6ttJrhSx6mN9yqN4SGUj3RG0O-ycr18sjybV9T22XK284eNK7rDviSzsvqxbOfzcVewQFoEW4Mf63-lUQbNNYHySpwx8zO7WqJh~7~iXlLProVizvNFHB32kBc4oJSOb1IsvEllYOcJ7p3KMWFXJavkOtaTw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Activate Pending Security Policy Changes.

- Access the Activate Pending Security Policy Changes task.

- Describe your changes in the Comment field.

- Select the Confirm checkbox to activate your changes.

1.  If the ISU authenticates using the user name and password, access the Maintain Password Rules task. Add the integration system user to the System Users exempt from the password expiration field.

- To avoid integration errors caused by expired passwords, Workday recommends that you prevent Workday passwords from expiring.

### IP Address Allowlisting (Optional)

You can add an <u>extra</u> layer of security by implementing an IP Allowlist. The HackerRank service communicates to Workday from the following two IP addresses:

- 100.25.76.193

- 3.233.184.164

We suggest implementing in a sandbox or implementation environment first and testing completely end to end before introducing the static IP address restriction to simplify troubleshooting. 

## Assessment Configuration in Workday

 This is a two-step process that involves

- Setup Assessment Status in Workday

- Setup HackerRank Assessment in Workday

### Setup Assessment Status in Workday

In this step, you need to set up the assessment status on the workday. 

|  |  |  |  |
|----|----|----|----|
| **Assessment Status Name** | **Reference ID** | **Overall Status** | **Test Status** |
| **HackerRank Send Invite** | HackerRank_Send_Invite | Yes |   |
| **HackerRank Accepted** | HackerRank_Accepted | Yes |   |
| **HackerRank Declined** | HackerRank_Declined | Yes |   |
| **HackerRank Invited** | HackerRank_Invited |   | Yes |
| **HackerRank Completed - Qualified** | HackerRank_Completed_Qualified |   | Yes |
| **HackerRank Completed - Evaluation Required** | HackerRank_Completed_Evaluation_Required |   | Yes |
| **HackerRank Completed - Failed** | HackerRank_Completed_Failed |   | Yes |

Follow the below steps to set up the Assessment task.

1\. Access the **Maintain Assessment Statuses** task 

![image1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047142862-?Expires=253370764800&Signature=JQJQVeNCxbl~n96jR2fneGaKnATLYdwM9mAPosoYHCH3MLVbGyyNjbe3MSUJL7QptmZgCI1z5~HWnpDG39CC-VzkuTGcnvB68crlCRJfhurW6ZNcE3bc1ndztzsq3C93bwomQUjbmcrXHGtcCYLbwiYoK2FWQb0rEcbBMWnCoN5FHtI7qaTOn9uO77Qt29ak2THQ~iEwfryaa9A5gFFCJklS551tKOsykTEW29M7dXjoxNC8ooiIOOmlOQEXHSu87gnlLwMy3A31xobXyWwhJx8f6vPNqhXxVEx3V-Qn0QRUGoMJtZuWi4OKnZgea1yyvHt81yd4VUfl8NU1rMFzhQ__&Key-Pair-Id=K3NV4LZ47N8M46)

2. Click on the Plus mark at the top to add a new Status

3\. Give a name, then check the box for Overall Status or Test Status. Overall Status will refer to the integration working. Test statuses will be used to track the candidate’s performance on the test. 

4\. Click on the **OK** button at the bottom of the page. 

**5. After the page saves, Hover over the magnifying glass and click on the three dots for more options. Go to Integration IDs -\> Edit Reference ID.**

![image2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047143253-?Expires=253370764800&Signature=nbaLIfwBUqpLoPHpo8tPRCuGg8PfrEOBuRO9VJaQs-5Pt8bqeosQRWEguCXTOagzlTU6RZ7PBePI9Y0XgPOr9ctoaZGr-9Ja8qufcC1bzj9GoD0e~N5fwWF-zSJimZ0u8lPV8uiQPjXFma5LRJuPJz0XZMM8fXLH60EC2BcX2jKllX1fmGgmfPUuYJWzADK5l~1T-j62EfskKtSmBTuqTN4PabdwYWUwwYR-JGBJh9LpxcwvJh47PGFI2DjnqhYgX5vZxTfjESHqtV1YqWOEn7jtOwePr5zXE1K5jvd-9iEOIzsoB2iVDFjlUPeUbAFmAjtAiDN5xExt~6kDOWRYjw__&Key-Pair-Id=K3NV4LZ47N8M46)

6\. Set the Reference ID to match the value in the table above and then click on the OK button.

![image3.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047143565-?Expires=253370764800&Signature=HqxIzUygeZU2j~Ls8J8ioBUNI44U~GUp~7HlMKJfu6tIEgAiDEnPgloI3IdXwt5q9lmPHv9zVAFwLc5JJXHoGIT0EuCiia5KHezYSBdYOPAyyuEzRne4A9MMvFN9DI65sTd3Z6dDiT9bnejfhSHBBFCAHHuIzsjrkSI5I3CjYdSarGEzrX5aZ2yxhdvH0JgZOkb5Wn7R8Dw9k30zRYupCmzGtgMdBpkOVY3PmPDl98yklq29IDaGGbqNSCOEy59yxtGr~e0BjwXD9FyoZp5aPLtEYSRe6zeofyOhduEVBuumPZYlhseFeL9vYtW7NJ~9oabx3nMoSBmw8~r74kXyeA__&Key-Pair-Id=K3NV4LZ47N8M46)

This is what the table should look like when you are done. Note the order, which will make it easier for recruiters to use.

![image1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047143879-?Expires=253370764800&Signature=VMG~HD9xdMZ9XF8y5vNqSqXsViXriuLsi7jyYhf-Tn5jELYL6KgqyfHI0afHLhM-zU4KX4x0BAiNN7sK1kFBSaGL1Sc2mMSt7SRk8GsHCNg9GkoRXeEtpLAFZKRiJBhGgiHfr2b3T-4STFOsntKA2rX75sYdLKGjw6UvD6AcV-VkYSBZ~o1LOW9OqGEXJrWmWTwVvofTue1u5hxv5xl5C4DQxngGOw15ySgIjYaMja-El~Btaeve125go0AmGHycYjuPJNHXKzhqxJW2SCt~HA2aymnacdFLm0ScN2IQIKxtZC-SmrOAH3Tu3U3A8YNk4CxGtyhMjz8Wu32qUkWFtQ__&Key-Pair-Id=K3NV4LZ47N8M46)

### Setup HackerRank Assessment in Workday

HackerRank customers can create their own custom tests, and the identifiers for these tests are unique for each customer. Therefore, any test names and test IDs must be added to Workday on a per-customer basis. This process is not something that can be automated, so it requires an implementer to add tests manually to Workday.

**Steps:**

1.  Open a test in HackerRank

2.  Note down the Name and Test ID from the HackerRank Test page and the page URL, respectively. In the example below, the Test ID is 1128102, and the Test Name is “Software Engineer Hiring Test.”  

![jobvite_test_id.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047144262-?Expires=253370764800&Signature=J0W51Hq6S1H3vl1Ge3vSln4z-SERTD1XCLuExQMsZkt7NC7tp0qelVM0w1gOkm6v0nKulDGXzV7XVt3xH8S2PvWKohEJTcsCsuyAlSg3BN~V0tKm-izW546mDNZu7aFubh8GBU5Psk5yJ4G9T7R~odEVphWFh~HeaZmFok3fLwpQyoAZAu4oBuEWMVwgHFoAgLnAumAPWyhSpu8Uce7KZtJDAYnWqX1Qx8VoMwhhqM8D90tK7LMYqty7~QW4y5thAMyhajsmPw3bqaw-yzNQYIeRv8YYEGgx2wClho0joiJnclBhl1Gfdv2WMrwWzutkxycbVHYExpWpu70tHphUxw__&Key-Pair-Id=K3NV4LZ47N8M46)

1.  Open Workday and access the **Maintain Recruiting Assessment Tests** task.

2.  Add a new Test. Set name to the *Test Name*

    <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047144963-?Expires=253370764800&amp;Signature=Lh~0XPDdCOisecnOmADW6v2-H2SOt8D8YCrwYf~94ncMcurAhhMuCGGtC~Czm0aOXnBYTWJfuPVnNHg0etRd5IW1~usCr0oh1buVu5xAbGlv79as7UmTGkPZJHuduhWn2ydV~fiUJarh8dcAIvGHdPeZwyKMUP2UDQXdOB3EEv89t3o~l~ujHgH~5cWFqgQiWDY55mh1lzzjVFYgWubZNDTv~XoNZrFTu7KunZgvLesVk0lNvHUzU8DSWIYQMfp2sFbvJFRqeSTGb2AjHxZtrpP0bUjRM6Wr5zyzAkGFBJfT8w5~RlF5em5eaJ-Vkbl1~d6jaDF0U7uaPA~L6vYWzQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

<!-- -->

1.  Chose Ok on the page

2.  After the page saves, hover next to the magnifying glass and choose Integration IDs -\> Edit reference ID.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047145600-?Expires=253370764800&amp;Signature=vZpW2PJrl50ejvWYHo7SGYgU4VDdVRYbE3R~gQel1jn1Tl76yqI40Ugo248TKTDyDU6mda6qZuiJsVy3uByPQgMxaVR1oS6D7xxuoztYdEDaU4hdlEBJU-KAA0oO9ciGoKoilNB6j4PXA5eXFhaMY84EeY1nUVbze-ORvK~ZqtPS63egqUZFJH2c26Qjdg1K5zcS9SUgCBmxC5l5pm9oSBK93bHhr3ltT3mznMmVejWYwDb7RweVGdW6ypki1Zyd9RfKCkd-csavlmFFcgI6lSERUSvofDTxJ5koak-cMs7LUmqOVrB84JKZhjeQ50gnhHCqXcBPPZllxzcpeDJiCA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

1.  Set the Reference ID to the *Test ID* from HackerRank

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047145938-?Expires=253370764800&amp;Signature=c~TljWkBDvzRu~ndWeK3VmTVIjiIBWeOndZaTbjAsQYWk11NDsB85tD8KnreBnyhyLgx6PTLIaDsA8ELIWFss6Ak6Bw44VaawodO-J~amTSBtSjA90iFoWDx4xX-TKMSMEcun3gE78-JvjxcSWFyWLgnOo91~EnuZ7pubVA6RbGh1~E4ZbDJqk4Glb2FptR6~86Qb8vqiPqipEnLI9DMelJWda8UtkVNOa-bizljbOVP61iEiT7GjJLNmfaf7dOn59aOeMFY57PeNpWAJM0MLgM2LkeDN~jvshkMAgdj5QwMarMik5cqwjKzDBYFg0S3yhRjyAIB7H6sZda6VsPkag__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Note: When building out and testing the integration for the first time, you can get the Name and Test ID from the HackerRank Test page and the page URL, as described above.

When the integration is ready, you can log into your HackerRank for Work account and do a one-time bulk export of all the tests that need to be entered into Workday.

Follow the below steps in your HackerRank account to bulk export the available tests.

- Click on the **Settings** button from the top left menu

- Select the **Integrations** option from the left panel

- Under Workday, click on the **Configure** button.

- Under the CodeScreen Integration setup section, click on download all published tests.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047146235-?Expires=253370764800&amp;Signature=QczVpKFM6i0RAcGqyzpNyWS1EYT~vHjzCZuz5F0dcZXyi5CXQqr1FRM1LHj5k8r06LnK-BfdWjUj-m3DSTvd3tGlJxyljFEYbhgD3Vi6s9DONJ46TFhInrnhuc7AZl~x98hHMo25XSUXhJqdsrQtQ1U0-aVf6hG0hfK8aKakjD1uJKGpvuxiek83NV439pR9lVA3~Nn~-a6JFqg3BIhWMqrNki9ddwdtlB7jFkwlIVf-EgyS58rI0Zv7Tsk5ODdl-muREUzvndsnnhP9AfoabRMJunsamhSXIzE6MJPsaTCAkR3i2VSbhOyg8m6C0HyUxvDVRbrW~~A1rw5NH29luQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Note: You need to add all new tests that are created in HackerRank and need to be used in Workday manually. 

## Business Process Configuration

This integration gets initiated from the Assess Candidate Business Process. This integration does not require any configuration that is different from the default.

Make sure you configure the Job Application business process to include assessment.

## Configure Default Tests (Optional setup)

Follow the below steps to configure default tests in Workday.

**Steps**:

1.  Access the **Edit Job Requisition** task.

2.  Search for and open the **Job Requisition**.

3.  Proceed to the Job section of the Job Requisition and scroll to the bottom of the page.

4.  Click on the **Edit** icon in the Assessments section.

5.  Add a test to the **Default Assessment Tests** selection box.

![A screenshot of a cell phone Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047146519-?Expires=253370764800&Signature=SKYerdxo0LA2jWaP6~5L0P~tlK-2mOTw300WU5FUGTqATUsBH~drh4ENjL140pQDkE6l0C~OU1~aQ62Gj8mFl3QGpliBPZbhPEAshtl4s-n9g1cLueaHQtDsvp3GBRbilMITJIhuvIH5jaeTnU0sDGpHv3yjUSExnwEbD6Hde1J18DM7dzRarhml6B~PPAy1s2--W~Qg0xEdp1CSigbhR0J~R1HS9C4qu1d-Wzrj5N1arvk36j2p7JdeRYuLy8HWB4aT7vwWm-OC0Q6nR27h~JuhgrI7QHQtAdQMDxKwAcq5ARoqbdKrrUdYaOfvzj4SEIS5BfQ0LDTgXYXKc8~brA__&Key-Pair-Id=K3NV4LZ47N8M46)

- When assigning an assessment to the candidate, the default test will show up by default in the list of assessment tests. The recruiter can change this before sending the test if the default is not right for the candidate.

  ![A screenshot of a cell phone Description automatically generated](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047146786-?Expires=253370764800&Signature=PM0s49QTQ~yv4mvjWLlEBb0B6xJW7ThyjEc0zxxqrDwVvlpCQ8PrQ~enRm7GiKIrNyq6s8Sy3qpoNj3bC~rIS9wYAHoWwb7lVEDCtGGIbLHckFCUqX-SB1MRuE-WcyzMQOXhLr7fgH0nLK8hBYCQFkAIvAthbn7JGMfe42UCNGAoQWn4I25GXpx2INXl20g2Lt0bHqBx6vXlH-c5R1BwAhKFLBBgi4VeeYg-qU6MZYByJY4rsZ2lDNK3~2QVmTGxpkHpsHpvNL8tKVIq5SmNQ7Dfpgmicrvfa19dnK-5W3OUQT0HV9rmMo~YzzrefveYLY84uwujMyEas9H25d1rdA__&Key-Pair-Id=K3NV4LZ47N8M46)

**Note:** A default test cannot be added once the job is live and candidates are added to it.

## **HackerRank Configuration**

The HackerRank side configuration involves the URL and authentication setup.

- Login to HackerRank with an account that has Company Admin permissions.

- Click **Settings**.

- On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **Workday** option. You can also search the Integration from the Search bar.

  ![integ_workday.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047147412-?Expires=253370764800&Signature=YnfB5EjJeENTQV5oLa4B7WUxWiHT3RQoAFndkfvgra-bW1bnxV90RHVy0xC1YRLTuNI983HZTgx7UghSDfrnzt1UTQvicGe0SPLzx5bFkpoo2oEaSqtyR4QmfTLl9hGSTaitjq6EWjOf3AKdyAuqjf~UefpG1722s8gFzGvCNk48z1QtT07a4Lin1b4yxWar8byymYeiNWqXTZ~XqX65qDJLhi4jh2TmX65scKk8gH9JJFC1T9FDEbPXjokfN~usP37cnzYiW7fSDCOHv1-AZDPuFSFgHuNv0-iESDyOl2grHsU4cVHMwnOZXOrdX3rTPeNniApKiytRMHHZDeX3Pg__&Key-Pair-Id=K3NV4LZ47N8M46)

- The Workday Integration page is displayed.

  ![integ_workday1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047148262-?Expires=253370764800&Signature=qL2KCbUFYMXP50qZK8BW0wGgasCP8tcJyuZr3MZD-GTr3nnjGVgeXOmZBlvY9c49up7oJs3Blzu~lBn-RCx7kuX9CIyhTCCWMJ0z8T99sj2tsXCCSWh3vhdlMJBPJ9sv4UIAVyVqSVWVRC48ciL7B9oiA-zFT2X9fkbz4EPsugPYW1De5gub8XQERRtNKF-dUsa4z13I-d5gCmOgNYXOFHoDN5V13qSAYYgCeG0TI96N3bY3tBZeNV23nJkiHHlU2K-Okqqjikxz8l47ZQtGgwZhKaYytma~IcBQ40j4FQyleKQLcB449Tw6a72mnNymHSdWG94LJkaK~UiTf4E2gw__&Key-Pair-Id=K3NV4LZ47N8M46)

- Enter the valid Workday Security Configuration and the URL and Authentication Setup details.

- Click **Save and Test.**

**Note:**  Once the recruiter invites a candidate to take a test, HackerRank will not invite the candidate again to retake the same test or take a different test. If you want to change this setup and want your candidate to get another chance after a certain period of time, you may control the setting from the below option.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047148670-?Expires=253370764800&amp;Signature=TPuClbX3H~1kayuAFklxILjabhnyt0scx5Kpmc-bP2ww9fab2DqLLY-N8ihQ3mSbC-GmLbUmKfq2tCgVEeUhsFNq8FN-P92cSoUQlsRQPPiDzBMwJzHlrWh-A0-UpH7foSIKHG0I9iFIM-KRsL7bH11rxvfj-6jJWBArEn-JJQB47P3UW5SObzgy28TPPjAGmbfQbEoAL3iQldu2xqjCc2q-rU1uxBw3BzCMDIDjd6p89hGgh1QPdBysbksfgAYQYjGC899Lf2wxXwljl6IoNABNu~7lpO10Yuud8qP-95f-sEx2rovj75LshjaL~64oKd1uFsNozLFqkvFg~CInpg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Important:** Once the configuration is completed, click the **Enable Integration** button to complete the process.

![Screenshot 2023-10-30 at 5.12.11 PM.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047149235-?Expires=253370764800&Signature=Bbq6XaRtAM3Uq581FKa6MF4XZgcSrPI8tfg46EAPceRqvZuz566gJeev8eqw2ONWbeDOAig4FcrMu3Jgtm30Hy5246MhQpStm0lOg~kdRnHaaWEuv6JxtfcYuy1dJeN5xtkxd6NFtTmKZRQncbREUqovUNlRohGjg0uVmzSlc2o1WIDkGMnFwKhsYmFca8rxU2hV-i~5bKU0IUu3eQxffg6GraWeaEZeMoqePXgZaMMcyLjQUBxCCJ2pOwPXVzNiM6hCe6OdqMSiJft7X4ponqquWFs~AHlFGJN04kQEIZpVtpm6rpLH4k8YI96eIl5jmoWQxIerWdE5tp8jTVdF1A__&Key-Pair-Id=K3NV4LZ47N8M46)

This marks the end of the configuration process. After this, you can invite candidates for HackerRank assessments from Workday and view their results.

You can check the[📄 Workday - HackerRank Tests User Guide](/articles/1999755553)to learn more about the workflow.
