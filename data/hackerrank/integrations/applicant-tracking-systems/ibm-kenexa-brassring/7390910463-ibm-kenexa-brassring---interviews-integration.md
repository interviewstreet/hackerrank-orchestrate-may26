---
title: "IBM Kenexa BrassRing - Interviews Integration Overview Integration Steps"
title_slug: "ibm-kenexa-brassring-interviews-integration-overview-integration-steps"
source_url: "https://support.hackerrank.com/articles/7390910463-ibm-kenexa-brassring---interviews-integration"
article_slug: "7390910463-ibm-kenexa-brassring---interviews-integration"
last_updated_exact: "Dec 28, 2024, 4:12 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "IBM Kenexa Brassring"
---

# IBM Kenexa BrassRing - Interviews Integration Overview Integration Steps

_Last updated: Dec 28, 2024, 4:12 AM (Last updated 1 year ago)_

# Overview

The below diagram describes the workflow of the BrassRing and HackerRank Interviews integration for recruiters. Recruiters will move a candidate into a custom HackerRank Interview status. Upon entering this status, BrassRing will dispatch a payload to HackerRank via the Candidate Export API. HackerRank will then generate a new Interview URL and Scheduling link and respond back to BrassRing. The Recruiter can use the Interview URL directly in their own scheduling tool. Optionally, they can access the scheduling link to set up a date and time within HackerRank. HackerRank will then send out the calendar invitation automatically. After the Interview has occurred, a link to the Interview report will be sent back to BrassRing via the Form Import API.

# Integration Steps

The integration involves a 3-step process:

- Step 1: Configure the Candidate Export to generate the Interview links

- Step 2: Configure the Form Import to accept the Interview links

- Step 3: Configure the Form Import to accept the Interview report url

## Configure the Candidate Export to generate the Interview links

### Obtain the BrassRing API key from HackerRank for Work

Note: If you are using the BrassRing Tests integration, you can skip this step and reuse the connection for the following candidate exports.  

1.  Log in to HackerRank for Work with the Company Admin user account.  

2.  On the home page, click the drop-down next to the user icon in the top right corner.

3.  Click **Settings**.

    ![settings.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047115359-?Expires=253370764800&Signature=bhCN-7djBeLEjRgjkzK7pENaw-kbfGGvPRtmEMa-LhdNCn-gsSHgwu1EAMy4Xm79~tHCBVz1XtSLkjQaFYWoUSqyALmjkhnQ96PgCxDbAb0hv6S24hCAdOOMIEB4GhWpOFoO1U4R8WNTW3r0s1iDHlzvk7k3X928SQqPDnDtQ9ykCdYT--Q6Ckjlm6IdhgOeElSJ0~buexz13DghkyBqx1YYRo0SffTKhlm8BQ14gRJQiQglJqjYx6rXd1gR~OvU8GRIn9FaO-NTTUTCgJ73MUle66t9Or5qAQoOrSMaU6IL8U4J7cenYrozZc06-ArBrx0PXoRSAQOl3PVeKax8Hg__&Key-Pair-Id=K3NV4LZ47N8M46)

4.  On the left pane, click **Integrations.** The **Integrations** page is displayed. Scroll down and click **Configure** on the **BrassRing** option. You can also search the Integration from the Search bar.

    ![integ_brassring1.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047115685-?Expires=253370764800&Signature=ClAL5XHAmJ8heU0V9GZXSnlLRK3FtG9PnLEr5KbVMJjhBHEopRaEQFhtLYawcZIHaquYHM~lB1ddaSAKpDmtfJrwUudrJHhUuXFzYL~Ul21OQbjlMnP99XxEEKEN5Sy3qyGFbGd7p83yyZ3aMqvYfgCPBGiXzhGwK4PoeTtgyZ25jB~6bXXwMydO27bcboZWSuc8K4gjlMAt~iC8wmq2~UEQLD4e0hENeCTmif2Rx9wLChacx7d4hNzyL~K2q3PFx68dmkaBdjvblusuKnleAiWh~GjC28FzR4prPyu6wlKHZaiXvTJ-RDUJdr1m6R42v0vvMSf-~yohN8FfXchinw__&Key-Pair-Id=K3NV4LZ47N8M46)

5.  Click **Generate API Token** to generate the API token.

    ![integ_brassring_api.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047116385-?Expires=253370764800&Signature=awMxp32WICJ-WyFncEa1hBL9iiiTT0cwNx5dFbtJ7oVcn30rnp5EG0OE0O-f04Cp8VfC1MonRPAcyPr9XtVYkRJJvIaRdQD1yMU6c5va0u4iCAEhfe3EP~5cJIGUI0wMzQhL4zs2v2YhtJQI5fzgbIE-18~-Prk4pypZDM9LsDYxNGrA13Lz~l8qQruYllS4mWAdNTGtbPUuQOOv8t~-Mk-YGMfpofX6BJFnpQpm68DMB~6gxKPIi~tL7WHR6KgXl3X0MIC8rz-VB5DZewMw9qjf26a41MIgUS6p5Tl510Zbqt-XI0O73COV24zAkRrBGO40~brodkOVsQjvZqTlhw__&Key-Pair-Id=K3NV4LZ47N8M46)

    A unique API Key is displayed.

    ![integ_brassring_api_token.png](https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047116693-?Expires=253370764800&Signature=fAidW7JDScS5Cg8SyPajYzexBlM03hfnszz9Vq80UPcQK1lvP6Ox9sQck2fNUDPOPdtpeCiaX1q4dzV62-YxRTrSnOgnkg2Yo843np2fgAZencruNkluAT6jflMV5J7A62b--YpZJWP1pqNfkpxCKBSlk4e-OdGMfnjHe7lKWuphw1nEu33bSRdKbheAyZ8ZlWJGXH7biD5lUYo0ccle37WEsJGP2wklfYu-Ao8SlO73I4OaNODwpY0Vwhvx8wo-oW5L-tmcg0ild5QYrB8Alk0kk7wZRRO2uThJvqKGDDvOGv-jcq4pboOmG3oe9LT2cZ4veXSlUfxm8N4G1sAGwQ__&Key-Pair-Id=K3NV4LZ47N8M46)

6.  Copy this key. You will need to add this key to the BrassRing account to establish the integration.

**Note**: Ensure to store the API key safely. Once the popup is closed, you cannot retrieve the key again.

### **URL and Authentication Setup**

In BrassRing, create a new Candidate Export payload. It should be sent to the following URL:

PROD: [https://ats.hackerrank.com/brassring-codepair/v3/schedule-codepair](https://ats.hackerrank.com/brassring/v1/schedule-codepair)

STAGE: [https://ats.hackerrank.com/brassring-codepair-stage/v3/schedule-codepair](https://ats.hackerrank.com/brassring/v1/schedule-codepair)

The username for this export should be set to the BrassRing API key generated within HackerRank. (The password field is not used by HackerRank and can be set to any value if it is a mandatory field.)

Note - The API key might be longer than the username and password fields allow. If this is the case, you will need to make a request to your IBM integration representative to have it configured by IBM.  

### **Setup Candidate Export XML Payload**

This is the format for the [Candidate Export XML](http://media.kenexa.com/Training/TSBR/Outbound/IBM_Kenexa_BrassRing_on_Cloud-Candidate_Export_Technical_Specifications_API.docx) that is understood by HackerRank out of the box. You will need to configure Workbench to create a matching XML:

```
<?xml version="1.0" encoding="UTF-8"?>
 
 <Envelope version="01.00">
 
   <Sender>
 
     <Id></Id>
 
     <Credential>26059</Credential>
 
   </Sender>
 
   <Recipient>
 
     <Id>http://server123.testcompany.com:8044/b2bhttp/inbound/kenexa</Id>
 
   </Recipient>
 
   <!-- Target URL where data will be sent -->
 
   <TransactInfo transactType="data">
 
     <TransactId>HSCAND19681</TransactId>
 
     <TimeStamp>2019-08-23 14:23 PM</TimeStamp>
 
   </TransactInfo>
 
   <Packet>
 
     <PacketInfo packetType="data">
 
       <PacketId>1</PacketId>
 
       <Action>SET</Action>
 
       <Manifest>CODEPAIR_CANDIDATE</Manifest>
 
     </PacketInfo>
 
     <Payload><![CDATA[<?xml version="1.0"?>
 
 <CODEPAIR_CANDIDATE>
 
         <CANDIDATEID></CANDIDATEID>
 
         <REQUISITIONNUMBER></REQUISITIONNUMBER>
 
         <BRREQNUMBER></BRREQNUMBER>
 
         <JOBCODE></JOBCODE>
 
         <STATUS></STATUS>
 
   <EMAIL></EMAIL>
 
   <FIRSTNAME></FIRSTNAME>
 
   <LASTNAME></LASTNAME>
 
 </CODEPAIR_CANDIDATE>
 
 ]]></Payload>
 
   </Packet>
 
   <Packet>
 
     <PacketInfo packetType="data">
 
       <PacketId>2</PacketId>
 
       <Action>SET</Action>
 
       <Manifest>CODEPAIR_CANDIDATE_REQEXPORT</Manifest>
 
     </PacketInfo>
 
     <Payload><![CDATA[<CODEPAIR_CANDIDATE_REQEXPORT language="en">
 
         <REQFORM id="111"></REQFORM>
 
   <CHOOSE_CODEPAIR></CHOOSE_CODEPAIR>
 
 </CODEPAIR_CANDIDATE_REQEXPORT>
 
 ]]></Payload>
 
   </Packet>
 
 </Envelope>
```

### **Mandatory System Fields**

Data sent from the Candidate Export: 

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| EMAIL | Varchar | This is the candidate email address. HackerRank needs this to tie the interview to the candidate |
| FIRSTNAME | Varchar | Candidate First Name. |
| LASTNAME | Varchar | Candidate Last Name. |

### **Candidate Export Response**

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| Long Description | Varchar | Schedule link: (link) Interview Link: (short link) |

### **Send Candidate Export XML Payload Preview to HackerRank**

Once the Workbench configuration is complete, generate the sample XML and send to HackerRank for validation.

## Configure the Form Import to accept the Interview links

### **Setup Form Import XML Payload**

This is the format for the [Form Import XML](https://www.ibm.com/links?url=http%3A%2F%2Fmedia.kenexa.com%2FTraining%2FTSBR%2FInbound%2FIBM_Kenexa_BrassRing_on_Cloud-Form_Import_Technical_Specifications_API_update.docx) that is sent from HackerRank out of the box. You will need to configure Workbench to create a matching XML:

```
<?xml version="1.0" encoding="UTF-8"?>

<Envelope version="01.00">

  <Sender>

    <Id>HRXMLEMPLID</Id>

    <Credential>26059</Credential>

  </Sender>

  <Recipient>

    <Id />

  </Recipient>

  <TransactInfo transactType="data">

    <TransactId>15747</TransactId>

    <TimeStamp>2019-08-23 14:26 PM</TimeStamp>

  </TransactInfo>

  <Packet>

    <PacketInfo packetType="data">

      <PacketId>1</PacketId>

      <Action>SET</Action>

      <Manifest>CODEPAIR_LINKS</Manifest>

    </PacketInfo>

    <Payload><![CDATA[<?xml version="1.0"?>

<form formTypeId="376" formName="HackerRank_CodePair_Results" formId="" action="Insert" resumeKey="" FirstName="" LastName="" email="" homePhone="" language="EN" autoreq="" optionalreq="">

<!--form action can be either "Insert" or "Update"-->

<FormInput name="(generated by BR)" title="CodePair Schedule Link"></FormInput>

<FormInput name="(generated by BR)" title="CodePair Interview Link"></FormInput>

<FormInput name="(generated by BR)" title="First Name"></FormInput>

<FormInput name="(generated by BR)" title="Last Name"></FormInput>

<FormInput name="(generated by BR)" title="Requisition ID"></FormInput>

</FormInput>

</form>]]></Payload>

  </Packet>

</Envelope>
```

### **Custom Form Fields**  

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| Interview Schedule Link | Varchar | url to schedule the Interview  |
| Interview Link | Varchar | Url to start the interview. This can be pasted into a calendar invitation. |

### **Send Form Import XML Payload Preview to HackerRank**

The following fields are generated by BrassRing and will be environment specific:

- formTypeID field

- formName field

- Each FormInput name field

Once the XML payload is created, you must send a preview XML to HackerRank so the correct identifiers can be send from HackerRank for Work.  

## Configure the Form Import to accept the Interview report url

### **Setup Form Import XML Payload**

This is the format for the [Form Import XML](https://www.ibm.com/links?url=http%3A%2F%2Fmedia.kenexa.com%2FTraining%2FTSBR%2FInbound%2FIBM_Kenexa_BrassRing_on_Cloud-Form_Import_Technical_Specifications_API_update.docx) that is sent from HackerRank out of the box. You will need to configure Workbench to create a matching XML:

```
<?xml version="1.0" encoding="UTF-8"?>

<Envelope version="01.00">

  <Sender>

    <Id>HRXMLEMPLID</Id>

    <Credential>26059</Credential>

  </Sender>

  <Recipient>

    <Id />

  </Recipient>

  <TransactInfo transactType="data">

    <TransactId>15747</TransactId>

    <TimeStamp>2019-08-23 14:26 PM</TimeStamp>

  </TransactInfo>

  <Packet>

    <PacketInfo packetType="data">

      <PacketId>1</PacketId>

      <Action>SET</Action>

      <Manifest>CODEPAIR_RESULTS</Manifest>

    </PacketInfo>

    <Payload><![CDATA[<?xml version="1.0"?>

<form formTypeId="376" formName="HackerRank_CodePair_Results" formId="" action="Insert" resumeKey="" FirstName="" LastName="" email="" homePhone="" language="EN" autoreq="" optionalreq="">

<!--form action can be either "Insert" or "Update"-->

<FormInput name="(generated by BR)" title="Assessment Name"></FormInput>

<FormInput name="(generated by BR)" title="Candidate Status"></FormInput>

<FormInput name="(generated by BR)" title="Feedback"></FormInput>

<FormInput name="(generated by BR)" title="First Name"></FormInput>

<FormInput name="(generated by BR)" title="Last Name"></FormInput>

<FormInput name="(generated by BR)" title="Requisition ID"></FormInput>

<FormInput name="(generated by BR)" title="Date of Assessment"></FormInput>

<FormInput name="(generated by BR)" title="Link to Assessment Summary Page"></FormInput>

</form>]]></Payload>

  </Packet>

</Envelope>
```

### **Custom Form Fields**   

|  |  |  |
|----|----|----|
| Field Name | Format | Note |
| Feedback | Varchar | This is the text that is set during the interview |
| Candidate Status | Varchar | We will send the status of the interview. For exaple: Qualified, Failed, Evaluation Required |
| Report Link | Varchar | url to the report |

### **Send Form Import XML Payload Preview to HackerRank**

The following fields are generated by BrassRing and will be environment specific:

- formTypeID field

- formName field

- Each FormInput name field

Once the XML payload is created, you must send a preview XML to HackerRank so the correct identifiers can be sent from HackerRank for Work.
