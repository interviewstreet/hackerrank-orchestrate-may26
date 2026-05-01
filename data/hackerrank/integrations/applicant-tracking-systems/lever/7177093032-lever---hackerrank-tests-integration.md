---
title: "Lever - HackerRank Tests Integration"
title_slug: "lever-hackerrank-tests-integration"
source_url: "https://support.hackerrank.com/articles/7177093032-lever---hackerrank-tests-integration"
article_slug: "7177093032-lever---hackerrank-tests-integration"
last_updated_exact: "Jan 23, 2025, 4:04 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Lever"
---

# Lever - HackerRank Tests Integration

_Last updated: Jan 23, 2025, 4:04 AM (Last updated 1 year ago)_

## Overview

The HackerRank Tests - Lever integration enables Lever users to directly invite their candidates to different HackerRank Tests at the appropriate stages of the job interview process. After candidates attempt HackerRank's Tests, their scores and performance data are automatically updated in their respective profiles in Lever. The ability to leverage HackerRank's Tests for candidate skills assessment facilitates a seamless and efficient candidate screening process in Lever.

This article provides you with detailed integration steps and also describes how you can use the integration to [send HackerRank Test invites from Lever.](https://support.hackerrank.com/articles/7177093032-lever---hackerrank-tests-integration#sending-hackerrank-test-invites-from-candidate-profiles-in-lever-21)

## Integration Steps

**Prerequisites:**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 50%"><p><strong>For HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef; width: 74.8333%"><p><strong>For Lever</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must log in as a <strong>Company Admin</strong> user to generate the Lever API key.</p></li>
<li><p>Log in using the same <strong>Company Admin</strong> user credentials to create and publish HackerRank Tests, which must be accessible in Lever.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 74.8333%"><ul>
<li><p>You must have a user account.</p></li>
<li><p>You must have relevant administrative permissions to the <strong>Integrations</strong> settings page.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## **Steps**

### Obtaining the Lever API key from HackerRank for Work

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047098785-?Expires=253370764800&Signature=ItDyr46xUbsa38as7T~NcnEb6qUDHaqyH~j~XyMGO7dRYLOJeeAeYi5GpKa-89hnHgrYqXisHVjec2rEX1xm67qDmy4BMIiOo4IRHF9t0P~3~AXx5yN7uyLkTK7yvu~MP0QObfaEHwQ45X7rL4x2LicOtnQO2AWwhuCu~w5hnjd~5wKkmECmBggYOIYN3IDnFiTPFQL8U8Nz1XO0OsXmm-E8cnP6x~ssKhZHB8mjpnQzViEK-sZFfA7TU2O6eyDITr2dtY2v~PfxmxAijQ8QNTAG6239gyxj6q2DVVeMIO9-qrjEBtL8xArkmXUUA~TliDEJpPfdfkf0EaWKJLw5JA__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **Lever** option. You can also search the Integration from the Search bar.

    ![gh_connect.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047099521-?Expires=253370764800&Signature=WBS28J25bqLB3OvmUo0m6HIRNSgBnaQmLsc7spVA4ppuNLrA1WAXCV6UyGAjQhfmYPcmUPLgEV6wL5qDVAUUI-Bwj07L3XeIRvASleE81SX0I3YThQPd~SqKrON6Tu~uj6Ez0D6pzfhQe9h4BpDW0fSSIWoCDL6CEj51Enx2qItQIaeSgWBt9t7CF27blovNvA-MztYHRiM7fwM5NpdjEQ3ZqZPjkwqpA-~~SG4ZEP1A~i92joVrabk~wWq1uPThC6bs5HB3sMeUv~D6QnJpoRAQOFw~6pIwGdctCmMmOvsCRdxJy5WWtBFEiEtHTlMFyZs8w~n86OPZDXXF9WLbPA__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Generate API Token** to generate the API token.

    ![integ_lever.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047099928-?Expires=253370764800&Signature=BiO9pP-Xx7e6BMmaiPUeAs81j9G2noK2FI3GNJ~PlfDoE-hZCQipRT5c9DF0i4yV6Soz7xRZ4OBeeKeielTP4b2yGGqWwkRcc5N-IDqqpXNqQnjD1DQN8MOZtha1xVTmdFpRHldCtn~diuOqxN9pITZjrssZ-YFgB90WMdhs~ZM0yv1rvnknCh7HWlqH5IBlUF3HcjQYFdxZRvPdU92KuuV02NdPsoMNF1-5D1dR29OycrGHUV5IJY9ayBSCV8vj0WXJWwc5tw7V1N6uXGU4xfe05rLodV4kQH7F8ET44vlOa31jmgv4ayJi93DQd6X9UipByW81Qh0haRJcv0Isfw__&Key-Pair-Id=K3NV4LZ47N8M46)

    A unique API Key is displayed. 

6.  Copy this key. You will need to add this key to the Lever account to establish the integration.

**Note**: Ensure to store the API key safely. Once the popup is closed, you cannot retrieve the key again.

When a new user is added to the Lever account, the user needs this key to set up the integration. Also, when the admin changes the API Key or generates a new key from HackerRank, all the current users need to update their keys. Hence, admins need to store the key and share it with all current users for them to update on Lever. Each new user added to Lever must enter the API key again. Store this API key securely so it can be shared with new users later.

1.  Log in to HackerRank for Work as a Company Admin user.

2.  On the home page, click the arrow next to the user icon on the top right corner of the page and select **Settings**.

3.  Go to **ATS Integration** and click on the **Configure** button under the **Lever** option. 

4.  Click on the **Generate API Token** button to generate a token

5.  The unique API Key will be displayed in the next pop-up. Copy this key and save it as it is not stored and hence can not be retrieved.

### Adding the API key in Lever

1.  Log in to the **Lever,** and click on the **Integrations** option from the **Settings** menu. 

2.  Scroll down on the page to the **Interviewing** section, and enable the **HackerRank - Tests** option. 

![HackerRank_Tests_option_in_Lever.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047100303-?Expires=253370764800&Signature=Z2Qo0aI8jTOMxedGmYTqb3Bh0kKRf4BJVqNpfr73uTu7ClYmaKo3nuyWso8DJVJIOAGSPtSoHdnLKdqCUW9pTYv-Z5--WpJHSoEdozY9EzXl9s-jiVqucKDOygVfl7oq4csCH5571MYMTRyCz1fZgXDYad6Q8KNG7TXdwzGdAtb~jequl4KGlNJ9giKwim4FNp1enhmcynMqoA4gF-m~tIPbil39GCjjVlGAUxndaFbYM2QDf2TlpSYpgHACwhs6nfJO7JNCAG7X7Pnq0Xtw80mRWRBOxZCdJgwBuemmJABFBFaZljoIHboCxMUzVjHLsYMYsYiuo2O9GPZsOV5ohw__&Key-Pair-Id=K3NV4LZ47N8M46)

*Enabling the "HackerRank Tests" integration in Lever*

1.  In the **Access token** field, add the API key obtained from HackerRank for Work.

2.  Click on the **Verify** button to test the authentication request between Lever and HackerRank. Verification should be successful.

3.  Click on the **Done** button.

    ![verify_token.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047100762-?Expires=253370764800&Signature=WIuI3d6FA6bu1wJunKTN3frL6qabImcSVIH267j5DcgZvDkftJ1q9~kubAfBfIMcEbz68zkoPqxBfwlB8EIi-y10ioRphUBmixl2Z9IWXpvuzi6L7BFJuxWiUgtxsjt~pNDWP6Jj3vRfWlukFw7JPjvT0Ly5YQEoSgTg1rncxqRKrbIvJW4Y8--lxYLLT7SvUIo-kEFaJxpr3PbAaxhxztyMDiVYholzDCzdk4XZmiNLwuTv74ppLA~i~bPa7P49geu9M3IEjbRLSqIohb9CzT-l4-fMaeH1kTOyWIH44lGUn-wwsCNjwI-MZhRwfoZXydNo36W2dm5m9NzeNV0h0Q__&Key-Pair-Id=K3NV4LZ47N8M46)

*Verifying the authentication request from Lever to HackerRank Tests*

### Create Tests in HackerRank for Work

1.  Log in to HackerRank for Work using the same Company Admin user account which was used for generating the API key in the first step. 

2.  Based on the specific job roles or technical skills expected in candidates, create and publish the HackerRank Tests, which must be accessible in Lever to send Test invites to candidates.

    To know more about creating and publishing a test, refer to[📄 Creating a New Test](/articles/7073839065)

    \

**Note**: In HackerRank for Work, you must log in using the same **Company Admin** user account to create the HackerRank Tests and generate the Lever API token required to enable the integration between the two applications.

## Sending HackerRank Test invites from candidate profiles in Lever

The integration automatically creates the **HackerRank** assignment form for the relevant Job interview process stages in Lever, and you can assign this form to the required stages.

![HR_assignment_stage.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047101146-?Expires=253370764800&Signature=uQMiTg-Q-EkAh7t3C9Y8dvddGy4pCSDZKhGYgNIXHeJYCuRHImAon1O778M~Ev4MXJFhUIwls~9Tu57gL0E2DuGm2s1sLh6-~G7i9vgkaIbsCtgkbEim3On5b1vxHMW~TyUMtnoShMiSbo2sxnonTPBNIFf3vZe7SbFoBG7WHbw-y5JM1pA0PIBA186kEyHXSbrHyzfhDB895swb4LrM3mgSPDkIj~QgdRocDepCGI4ZvbqPtlyUa7IME6fqzDJ6fu4OducJqvofazydQJK~OcYSILkquH-MlFU1C7Ru38B-DVP2KQFpIVtd1aanV7WxVSwZnymxWX6fsT7YsZ7eig__&Key-Pair-Id=K3NV4LZ47N8M46)

*The 'HackerRank' assignment form for different interview stages in Lever*

Simply change the candidate pipeline stage to the one that is assigned the **HackerRank** form, and you will find the **Send Test** option to invite the candidate to a HackerRank Test.

![Send_Tests_when_stage_changes.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047101598-?Expires=253370764800&Signature=qxermVmVRElXu9oGC4XE9P1GFZxS0VoZrAuTcYtAKZdikYUnUaqZ~spNO1Jf29k6mq3OcZgev-ZiE4m8zk5xwKQ-oYef9OhmjElboBoYYvu0JAqVXflsS9flbg-k5jar-jX1hbJcHlqEsbxszI~UU4VCBK42R52aRd9Ja3YI7Er1PsIYqj8w4dyRGnCgtjNn7eia0rrb72VJcD-5ZUjVDRQSjdYNEG5o7j~VDCA6LfVHeyfISaEL7mzCXcsHnEOgERyztaISsixWtBVtPhjbMGc0921NPgrJZ0hzsTaUaH3VY0whx9U6ZMCEOa-sz8a8RTYAGKUtCdiOJGt1HEK1HQ__&Key-Pair-Id=K3NV4LZ47N8M46)

*The 'Send Test' option is displayed when the Candidate pipeline stage is changed.*

Alternatively, you can also click the three-dot menu in the candidate's profile and click on the **Send Test** option.

![Send_Test_from_the_three_dot_menu.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047102121-?Expires=253370764800&Signature=pgW5rcl74j8zUOqSbavnwhSffub5UGY~aSxYvk~mDp8onN88XnMY~WBOckSvUadY0DdCQMbaBBTl3qRNBo1aS7N16jweW7jAbzkH5go5WhcWKugjgwD3dHtHpk2~4kreWJ7hp12V9MxevS0jkheg2etRjGxRJn5DwBBp8QLAGzLLGeZMG~C4bYSbBWclBoQxOAAsaXnGJRC1pd6~MnX1y8bIbcczHt8~TEVYKO8X7fkwB6HfUKr~ZafSGRF8U2HV7oOxW7RooHMoN~O0dEwXsSy7ph0cDqB3T6U9CgjD8i~33COr29TfZD5R0UswWR~k2nLqCUfJkWuwzCkerJ2i7Q__&Key-Pair-Id=K3NV4LZ47N8M46)

*The 'Send Test' option from the three-dot menu*

**Note**: A candidate's Lever profile must have a valid email address to send a HackerRank Test invite.

In the Send test window,

1.  Click on the **Choose a Test** option and select the required HackerRank Test. 

2.  Verify that the candidate's valid email address is populated in the email address field.

3.  Lever users can click on the **Send the candidate an additional email** option to send any additional email message to the candidate.

4.  Click on the **Send Test** to send the HackerRank Test email invite.

    ![choose_a_Test.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047102635-?Expires=253370764800&Signature=jl1miRmAyTkNUVbrEyHpBx6vwRFbFFhvYPZ3wGR5agn-xGKpH-8HItr1xH62h-8CKHNkO1sCTzVVP6GXLoxl5rcznPwmW2OKo9Avyp8ws-2GYZEZD-DfvrI4ZqyAb7iA6auIY6F8QrPyhbHwrj509fwMLOHxrkOnssbQUPVkVnvwdl71hlKgBncFulabJDaygUlgr3HYlflz9oGZbsut0TgZj1aeSgKvW046YkjMXqCzGjoF4p2rEZn~8V4~HG6xPi2Edl4RingVkPm0ZoTbR4kL6QJTNtW8lX8s91XiC270drKIElJxl3ql8mQ2WGV4Fxy3VNnpG0rz01Scf1Jj6A__&Key-Pair-Id=K3NV4LZ47N8M46)

When the Test invite is sent, you can see the **Pending** status in the candidate's profile.

![Pending_Test.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047103159-?Expires=253370764800&Signature=YJePeYtBObc-3CAbNnCTXtysI7A01QtgVA~MjPG8Wn6gOKOp7K-KFGcMaO2kycH~zHsLpZ4xKKNLVEA3aPAAtQS1UPYuqvUgFWW9Xb~Thx8nDuR5JSwzonuESxC6Y7Ss5fWLVD8kW0eAEkFdlPGkLE0Ky6AiHnUsZXS6ZFmUdBnkfEQr4lItfjEKTvqx2RxA~n3yrlwYc7~hMrSPG57nTwN6YgxPcfuuS70YV1cC4sOnONYLQVPIJ3gouj6QXJgZvkqGPXyPeuW91vwd-iB~3Cx6aqELQ40P3SlEx7ab0HGffIbwvSDTNPqzqaQLsXkwOr38pmGo0URwmmG-Yuq7hg__&Key-Pair-Id=K3NV4LZ47N8M46)

*Sending a HackerRank Test invite in Lever*

After the candidate submits the Test, a link to the Test performance report is automatically available in the **Add links** section of the candidate's profile page. The Test report is also displayed on the candidate's profile page, as shown below.

![Candidate_Test_Report.jpg](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047103469-?Expires=253370764800&Signature=qbI34SQ1eCjIIKR76A~Q~5ONF6XPuVQ8XPnYsZ-lndjH7h89be-57oMd3A4lSEmtZMuCkSLif3Rk0dXeZQKBX4fId6jfX9XofITDoCTXwMQCiROTHDdO79ZkVGr~YIe6M0GB4UYfpEPm4dlHa5gxAMN6osyI~VNytPwDOxxZxwuomljADryh~0dhzne0NSD2f4dgr4FJZzZskU-k2lk2DMa9GZmZ5GUbyCGoVL1JMc-4HA9764cKWm~ZBTFKc6ACX5D6sHzT-rJLggiUH~bO0-iIn1izk1UYuEi058E6ONCV4gA1ydNgB3qUhfVvz~O-YcY3oq376EuYeM5oWAn7Ug__&Key-Pair-Id=K3NV4LZ47N8M46)

*The Candidate's HackerRank Test report is updated in Lever*

Lever users can review the report to assess the candidate's performance and knowledge in the required areas for the job role, and decide about the next steps in the interview process. 

Please refer to the [Lever support article](https://help.lever.co/hc/en-us/articles/217332106-How-do-I-enable-and-use-the-HackerRank-Integration-) to know how Lever users can view and receive alerts about their candidates' performance in HackerRank Tests.
