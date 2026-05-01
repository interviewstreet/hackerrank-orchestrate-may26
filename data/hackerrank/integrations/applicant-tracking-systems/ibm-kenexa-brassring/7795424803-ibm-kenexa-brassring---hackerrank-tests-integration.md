---
title: "IBM Kenexa BrassRing - HackerRank Tests Integration"
title_slug: "ibm-kenexa-brassring-hackerrank-tests-integration"
source_url: "https://support.hackerrank.com/articles/7795424803-ibm-kenexa-brassring---hackerrank-tests-integration"
article_slug: "7795424803-ibm-kenexa-brassring---hackerrank-tests-integration"
last_updated_exact: "Dec 28, 2024, 4:09 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "IBM Kenexa Brassring"
---

# IBM Kenexa BrassRing - HackerRank Tests Integration

_Last updated: Dec 28, 2024, 4:09 AM (Last updated 1 year ago)_

## Overview

The below diagram describes the workflow of the BrassRing and HackerRank integration for recruiters. Recruiters will move a candidate into a custom HackerRank Test status. Upon entering this status, BrassRing will dispatch a payload to HackerRank via the candidate Export API. HackerRank will then send a test invitation to the candidate. After the candidate has completed the test and HackerRank has graded the test, HackerRank will send the results back to BrassRing via the Form Import API. 

![image2.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735339058668-360039450754-e50edc3a-3e1e-4ee3-9acc-145d25fe2ede?Expires=253370764800&Signature=G0vCFotadmKcgStG6ARJO~JVhCbqAP1cff7UjLc-kRBkr~dyZf7JPCJto1qU2~cM9a1HjQ2ZFF7rsBlYOdBZ7vfR9Ut1xbjCw9iP3CuNEUcTx5ZNysnr893IvqghPVYIJPW4cOcFJMfvpkqEEq05CbZmeXwcM62hOUxic16u5-XLWhYAav4BKtiq64RsMBW~vgR0GOdW2krzTLKWFcxt4DlzMYeD-0KFksvQNGIJ3bkH0Gw14uexdTexGfilyPlX2o~G9zSCpo37xZh9~8RaF2bXUJ-tc00KCGgqJEhtCYG~o~nki5byQSBBN1HApB-AT-d86VdpZAOpXaP2ct~9GA__&Key-Pair-Id=K3NV4LZ47N8M46)

## **Prerequisites**

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef"><p><strong>In HackerRank for Work</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef"><p><strong>In BrassRing</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 332px"><ul>
<li><p>You must own an Enterprise plan with a Recruiter license.</p></li>
<li><p>You must have an activated <strong>Recruiter</strong> type user account with <strong>Company Admin</strong> permissions. This user account must belong to any team.</p></li>
<li><p>Recommended: HackerRank for Work Sandbox account for integration testing.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 332px"><ul>
<li><p>You must be a BrassRing customer with access to Candidate Export and Form Import APIs. Contact your IBM representative if you are not sure if you have access to these APIs.</p></li>
<li><p>You must either: be a Workbench Administrator and configure the integration yourself or work with IBM professional services.</p></li>
<li><p>Recommended: BrassRing Sandbox environment for integration testing. </p></li>
</ul></td>
</tr>
</tbody>
</table>

## Integration Steps

The integration involves a 3-step process:

- Configure the List of HackerRank Tests in BrassRing

- Configure the Candidate Export 

- Configure the Form Import 

### Configure the List of HackerRank Tests in BrassRing

The lists of tests need to be set up on the BrassRing side as options in a HACKERRANK_TEST_ID field. 

![integ_brassring.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047113161-?Expires=253370764800&Signature=FNiV8TwIRlf2qVIsIsgHkF8NGXHB6bVwvTJoTdZCbd2EjxOP5idgWgrBWzZVZ~TmSJZL2vsYTtf17BZuosVLLNaqjNBrlzPgy7pcTX6GBBEXe7yZUeHhuOp3psZxbFkBtEIJHc7rqGuWmI1gbNQ2RNGy8EhO15xfxPrEJRzd0rPbAMz3MiOsQ-n~ICH6XjIgMzWBGFvm0Q0b1AheHRq7wYl1MUxWGMqCTvRDt~P8QvTjQY2sUeUOLcySEC90hIs5cExaM9yb5iSkEu0eap6eiHDrGOySnkIkhs8WIMqdnxBc7mQwMI0HyABzR-GALGGUuKLMXUwyOXdiH4L-Pg5djA__&Key-Pair-Id=K3NV4LZ47N8M46)

When building out and testing the integration for the first time, you can get the Name and Test ID from the HackerRank Test page and the page URL, respectively. In the example below, the Test ID is 454785 and the Test Name is “HackerRank Full-stack Developer Hiring Test.”

When the integration is ready, your HackerRank Solutions Engineer can do a one time bulk export of all Test Names and Test IDs to be entered into BrassRing.

Any time new tests are created in HackerRank that need to be used in BrassRing, you will need to add them in manually. 

### Configure the Candidate Export 

#### **Obtain the BrassRing API key from HackerRank for Work**

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047113574-?Expires=253370764800&Signature=S0swkFPuDGbPT9yOP7eZVv0DPW4L35MaaHA0V08r21xbnml0ppHhRdI2hyaiuw7V5XF-6bzqMYMEGbnekFQvlGLlL1O7KjCaQ85N7SAye2CS7xFu4ymzM3ykbVwjnNvUKQpNOpbV27iciJu4oKKoDDqD5ha07r6eLfgG-ilXZ3oQ8lx15FL89T~npET-sLIOXsBLOpqhQHfzM6Cw20bhq4M8XwVQlJ-J9c-aW7eixUFscOO4O8Tw2HoVhHiCH2fZjjmFDaIvITJe~bdg-4VcxDjPrOf2FkeOk7XJzC5pNlC8LeY5h~VAI7GFpj48u8hy7yP0zV0-CZryrLY3mK7-og__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **BrassRing** option. You can also search the Integration from the Search bar.

    ![integ_brassring1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047114090-?Expires=253370764800&Signature=JL4OJLXWQxVjixi7RGVyZJswW5EPWf1uVlcruvj0L3ma4brHIYSrFD5oMIWNw1G8ol99Fsk5dAbpyI7oxcweeZR1shVU-c7dOfuCQFv0wHUcCVqyNa~ITJKeJ1KTAOYwzKoNbSTOZUrC7rNjjO1vMOcaRj7rqNvthW7lAs8wiFMEzr6FGpunMKECztzxzGDNmOTu5jDckU-IR7fGgqPQWwZpnFwTp~2kP2Cwf3NYcyl1R95hXwpd3ZZWtl5avTJOyRw--B0cfKXGEyHyIkh7~HH2GTlwmVkSkM8tUagLA8i2-mf5Ar-aUZsFYWLSQ0cFsYPe0sO3kGZOM7n8i~u5uw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Generate API Token** to generate the API token.

    ![integ_brassring_api.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047114510-?Expires=253370764800&Signature=CFnCNJwlUGrEhVylH~7jKueu-Zs6-MQCcBWNIDFSF1-T2sQOHU9HQeJZLQrjk~1q60nhGnmulVQnQlzZfqmkJc4CPj7tXYTArMRsdUmOB~IQ256Wo~agdeNuA8Q1LSk2aCgCnp2nmmbvA2hbLMDikERWYa4hGf1Buwg5LR1ghHi~iam54rehX0kceUK7cst86w6tFDAl-4dqB7iV4UUXVJ8627tV1Wc8MR6MtxTyKVuiDKM9j5LbozgtJbqPJw4IaYTjfVhOpvLM8Y-46sd1abtsEak7MGQ-ldBX31nP1WD7TkwRB4~8hFsMvHgpBrZNxjiSfxKkJPloNCnIC28xsQ__&Key-Pair-Id=K3NV4LZ47N8M46)

    A unique API Key is displayed.

    ![integ_brassring_api_token.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047114833-?Expires=253370764800&Signature=VOZF25qo10yNvdWNCL44KM~-rT4CZGd2K83i44nV95mWGmflf199sm3SqUuTBKmCGd0rT4GnX~a3N2jfEwGRuKYRonoCEYxwsAvOG~LI2WIC2fSH1ZQkpn-G9bOmyAw-jcpQ96SvQoLvphgL1Rsq8QSLq-Yg~IglkRx4HzOUGl4zDjVgUYrTVYDOv39WvPn-rwpgUYeNWgMbeMIG8NAYKtfuWri3YrpiHMfkpdg4CB8SjC1hgZAUJBDEpVvuCrb5NmZWesI83er6Adoa3cdchDlDNnd0o50zNx6gEB8S-FBFHN5lkrPlXqKBoBoUwOvr1F7bbn0heZiswiCinSiSIw__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Copy this key. You will need to add this key to the BrassRing account to establish the integration.

**Note**: Ensure to store the API key safely. Once the popup is closed, you cannot retrieve the key again.

#### **URL and Authentication Setup**

In BrassRing, create a new Candidate Export payload. It should be sent to the following URL:

[https://ats.hackerrank.com/brassring/v2/invite](https://ats.hackerrank.com/brassring/v2/invite)

The username for this export should be set to the BrassRing API key generated within HackerRank. (The password field is not used by HackerRank and can be set to any value if it is a mandatory field.) 

Note - The API key might be longer than the username and password fields allow. If this is the case, you will need to make a request to your IBM integration representative to have it configured by IBM.   

#### **Setup Candidate Export XML Payload**

This is the format for the [Candidate Export XML](http://media.kenexa.com/Training/TSBR/Outbound/IBM_Kenexa_BrassRing_on_Cloud-Candidate_Export_Technical_Specifications_API.docx) that is understood by HackerRank out of the box. You will need to configure Workbench to create a matching XML:

```
<?xml version="1.0" encoding="UTF-8"?>
<Envelope version="01.00">
  <Sender>
    <Id></Id>
    <Credential></Credential>
  </Sender>
  <Recipient>
    <Id></Id>
  </Recipient>
  <TransactInfo transactType="data">
    <TransactId></TransactId>
    <TimeStamp></TimeStamp>
  </TransactInfo>
  <Packet>
    <PacketInfo packetType="data">
      <PacketId>1</PacketId>
      <Action>SET</Action>
      <Manifest>HACKERRANK_CANDIDATE</Manifest>
    </PacketInfo>
    <Payload><![CDATA[<?xml version="1.0"?>
<HACKERRANK_CANDIDATE>
        <CANDIDATEID></CANDIDATEID>
        <REQUISITIONNUMBER></REQUISITIONNUMBER>
        <BRREQNUMBER></BRREQNUMBER>
        <JOBCODE></JOBCODE>
        <STATUS></STATUS>
 <EMAIL></EMAIL>
 <FIRSTNAME></FIRSTNAME>
 <LASTNAME></LASTNAME>
 <HR_ACCOMMODATION></HR_ACCOMMODATION>
</HACKERRANK_CANDIDATE>
]]></Payload>
  </Packet>
  <Packet>
    <PacketInfo packetType="data">
      <PacketId>2</PacketId>
      <Action>SET</Action>
      <Manifest>HACKERRANK_CANDIDATE_REQEXPORT</Manifest>
    </PacketInfo>
    <Payload><![CDATA[<HACKERRANK_CANDIDATE_REQEXPORT language="en">
        <REQFORM id="111"></REQFORM>
 <RECRUITEREMAIL></RECRUITEREMAIL>
 <HACKERRANKTESTID></HACKERRANKTESTID>
</HACKERRANK_CANDIDATE_REQEXPORT>
]]></Payload>
  </Packet>
</Envelope>
```

#### **Mandatory System Fields**

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| CANDIDATEID | Integer | This is the unique identifier of the candidate in the BrassRing system |
| REQUISITIONNUMBER | Varchar | (Optional) This is the Client Req number also referred as the Optional Req Number. The value will be blank if client does not use it |
| BRREQNUMBER | Varchar | This is the unique identifier of the Job in BrassRing. It is always a value that ends with “BR”, for example 100 BR, 3423BR, etc. |
| JOBCODE | Varchar | (Optional) This is the standard job code associated with the Job |
| STATUS | Varchar | (Optional) This is the HR Status value that triggered the integration |

#### **Custom Candidate Fields ** 

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| EMAIL | Varchar | This is the candidate email address. HackerRank will send the invitation email.  |
| FIRSTNAME | Varchar | Candidate First Name.  |
| LASTNAME | Varchar | Candidate Last Name.  |
| HR_ACCOMMODATION | Varchar | (Optional) This field represents a time accomodation that is candidate specific. The field expects a value in percent. The percent time will be added to the test to create a candidate specific test time. For example, if the test is 1 hour, you can send in 50 to make the test 1 hour and 30 minutes.   |

#### **Custom Requisition Fields ** 

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| RECRUITEREMAIL | Varchar | This is the email address of the user in BrassRing who is taking the action. This is important so that the report from HackerRank is sent to the right recruiter. Additionally, this ensures correct auditing in HackerRank.  |
| HACKERRANKTESTID | Varchar | This is the Test ID of the test that should be sent to the candidate. For example, the Test ID for the following test URL is 454785: [https://www.hackerrank.com/work/tests/454785/questions](https://www.hackerrank.com/work/tests/454785/questions) |

#### **Send Candidate Export XML Payload Preview to HackerRank **

Once the Workbench configuration is complete, generate the sample XML and send to HackerRank for validation.

### Configure the Form Import 

#### **Setup Candidate Export XML Payload**

This is the format for the [Form Import XML](https://www.ibm.com/links?url=http%3A%2F%2Fmedia.kenexa.com%2FTraining%2FTSBR%2FInbound%2FIBM_Kenexa_BrassRing_on_Cloud-Form_Import_Technical_Specifications_API_update.docx) that is sent from HackerRank out of the box. You will need to configure Workbench to create a matching XML:

```
<?xml version="1.0" encoding="UTF-8"?>
<Envelope version="01.00">
  <Sender>
    <Id>HRXMLEMPLID</Id>
    <Credential></Credential>
  </Sender>
  <Recipient>
    <Id />
  </Recipient>
  <TransactInfo transactType="data">
    <TransactId></TransactId>
    <TimeStamp>M</TimeStamp>
  </TransactInfo>
  <Packet>
    <PacketInfo packetType="data">
      <PacketId>1</PacketId>
      <Action>SET</Action>
      <Manifest>HACKERRANK_FORM_IMPORT</Manifest>
    </PacketInfo>
    <Payload><![CDATA[<?xml version="1.0"?>
<form formTypeId="(generated by BR)" formName="HackerRank Results" formId="" action="UpdateIndividual" resumeKey="" FirstName="" LastName="" email="" homePhone="" language="EN" autoreq="" optionalreq="">
<FormInput name="(generated by BR)" title="Assessment Name"></FormInput>
<FormInput name="(generated by BR)" title="First Name"></FormInput>
<FormInput name="(generated by BR)" title="Last Name"></FormInput>
<FormInput name="(generated by BR)" title="Percentage"></FormInput>
<FormInput name="(generated by BR)" title="Requisition ID"></FormInput>
<FormInput name="(generated by BR)" title="Date of Assessment"></FormInput>
<FormInput name="(generated by BR)" title="Link to Assessment Summary Page"></FormInput>
<FormInput name="(generated by BR)" title="Overall Score"></FormInput>
<FormInput name="(generated by BR)" title="Assessment Code/ID"></FormInput>
<FormInput name="(generated by BR)" title="Candidate Status"></FormInput>
</form>]]></Payload>
  </Packet>
</Envelope>
```

#### **Custom Form Fields ** 

This is the status of the candidate’s results. It matches the status that is shown in HackerRank.  

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef"><p>Field Name </p></td>
<td data-colspan="1" data-rowspan="1" style="background-color: #eafcef"><p>Note</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>Assessment Name</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>This is the candidate email address. HackerRank will send the invitation email. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>First Name</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>Candidate First Name. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>Last Name</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>Candidate Last Name. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><p>Percentage</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><p>This is the percentage score for the candidate</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>Requisition ID</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>This is the Requisition number. It will match the BRREQNUMBER from the Candidate Export. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>Date of Assessment</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>This is the date of the assessment</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>Link to Assessment Summary</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 44px; width: 50%"><p>This is a link back to the test results in HackerRank</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>Overall Score</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px; width: 50%"><p>This is the score, in points. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><p>Assessment Code/ID</p></td>
<td data-colspan="1" data-rowspan="1" style="width: 50%"><p>This is the test that was taken. </p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 46px; width: 50%"><p>Candidate Status</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
</tbody>
</table>

#### **Send Form Import XML Payload Preview to HackerRank**

The following fields are generated by BrassRing and will be environment-specific: 

- formTypeID field

- formName field

- Each FormInput name field

Once the XML payload is created, you must send a preview XML to HackerRank so the correct identifiers can be send from HackerRank for Work.
