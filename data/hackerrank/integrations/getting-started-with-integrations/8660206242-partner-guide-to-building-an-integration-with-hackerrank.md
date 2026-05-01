---
title: "Partner Guide to building an integration with HackerRank"
title_slug: "partner-guide-to-building-an-integration-with-hackerrank"
source_url: "https://support.hackerrank.com/articles/8660206242-partner-guide-to-building-an-integration-with-hackerrank"
article_slug: "8660206242-partner-guide-to-building-an-integration-with-hackerrank"
last_updated_exact: "Feb 7, 2026, 3:34 PM"
last_updated_relative: "Last updated 3 months ago"
breadcrumbs:
  - "Integrations"
  - "Getting started with Integrations"
---

# Partner Guide to building an integration with HackerRank

_Last updated: Feb 7, 2026, 3:34 PM (Last updated 3 months ago)_

This document is meant for partners who wish to develop an integration with HackerRank for Work. We are constantly working with ATS vendors to develop integrations for a better user experience. This document will give you all the information you need to develop an integration yourself.

## Background

A number of our enterprise customers - i.e those who use HackerRank for Work Tests and Interviews for the evaluation phase, also use some other IT systems to manage their overall hiring process. These systems could either be Commercial Off-the-shelf (COTS) systems such as Oracle Taleo, Jobvite, Greenhouse, Lever, Kenexa, RecruiterBox, etc., or some bespoke home-grown system. We will refer to these apps jointly as Applicant Tracking Systems (ATS).

Such customers frequently ask for integration between their ATS and HackerRank for Work so that routine actions of managing their candidates can be done inside their ATS workflow. Examples of such routine actions include (a) inviting a shortlisted candidate to take a HackerRank for Work test, (b) viewing the results of a test for such candidates in their ATS, (c) scheduling a HackerRank interview session between an engineer and a selected candidate, (d) viewing Interview reports within the ATS interface, etc. Thus, the most commonly requested integration points involve pulling data from an existing HackerRank for Work account and doing specific actions from inside the ATS interface. We have API calls that will help implement these actions from within the ATS UI.

## General Workflow

The integration typically involves adding functionality to the ATS via a plugin or customization using the HackerRank for Work API. This is best explained visually using the following diagrams.

### **Conventions Used in the workflows below:**

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047080233-?Expires=253370764800&amp;Signature=VN9zlc1jUFgXiZWqDR7ma4arRwqTRRVTxVq6qTRm7-rnOO5-ELJZlwWaGaOhonm-RgvYQYChNfSO3afjdta-KRuWzDfyGGuu8DigaADDM0tdBuZi0DAqg0Fvq4Szz-IvxEdjwa~1F1fIEcvq3z~W33BhYFB6Jpb47OsNURQxqu0Es18wj4YMeDgimuDJMsCWT4fr3yKUeaLK405Z70biZyr8Qp9ez7bbSvwDg4LbRv3ENqjIsqzb3y-nnJNLwSyUKwmq4t2KAJ-1DAIIHMQzdmNyroByEVBg-VOHkrOobc4r-3caB31GslYI9LU0lhCS97q8BC9Wvt3DV27UJ--k-w__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

 

### **Integration Setup - One Time activity**

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047080592-?Expires=253370764800&amp;Signature=u-P~EqYTf-gl2RdYl3xyTkwD6SVQ6A-GNTLVDTBRGuiyDMMsW74koFGcJRfkhlOWkXxCLlo-KSZgLtlw~E-cZzCuoXwd91Pb9ry~ZC1A1BrYsC0UW-sZhw78Pdqc7xLCiLLmjEiNimNz9Mey3WkMKXgtLLrLq1FIEd4oXtr~zCvonWBhyM3AvnLcfJJC08Tt6M7k8pfDS9FUPVaMfPLfVKX4bttKKyarpOKXYeamOEoX4HvtXtd6FCiNd4LYimPvepnDiy0uQ-o8lrKrgCpjeWMXtOT~obLOTRN-3zb3n8vJesj8OXx-fQZGoV4wt2oe~TCvzjJ4TTkIk3nXQaAv9w__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**Note:** Every official ATS integration will have a section within HackerRank for Work where each company’s account admin will be able to generate a key. Your ATS will appear in the following location: [https://www.hackerrank.com/work/settings/api](https://www.hackerrank.com/work/settings/api) 

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047080957-?Expires=253370764800&amp;Signature=ZNtmuCQOb11bz2EiO2Ml6DdLw3ErXaVuWwFjP55y5wEUuwL48ZPBVviYeSnw9OmhqOAxxPVND7DsHFGFuxs9z9GpB0zSPBpYoVLvnj0z6Px5x2F6lsYXAwh1jRu12txpedaA5tGt4oCvAus0uuQTK5BGxXnN5wlZ4q8d4oVkvV7vuvwS2pihl4B2~pgS5Shc0a9KpaagEXhZ6wpLOaaiIIh5cdehTuSGL6DkmXhX1c4MuZyyvreAmt9fL8roZgH0pWGt8vc1Yje4QQUVFU2ULdyg1uUMkoFxa98KbyvLASPBzwE5iK1MctzhSVIOQ2lNW8KSId5tKN-p-KpsOtLoXw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

### **Overall Test Flow**

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047081363-?Expires=253370764800&amp;Signature=DxCJA9GbgkotF06lgUozYwyJu3lnz45U51jJjyMZg131t8~KITMd4Acn~T~NjphlWfUI-ztIMziL1udkfp4sObGCwPpUazBD1O1w9~gQx-ZBsxVndvmmtIHQXRU5ghSGeUbl~vnIYwX3Yy0i5y4K8cfQ5uu7Y3lg2lZZOPVfbot2Iz6GdBjLRdKgTdb8uSXmfSOcy-c7h1aNU~KtWN5DHkHZ01JDaElTdkCVcZi752IT7rA~QEuQmVxKXVbTUMSzPpPWOMahruD3FU1H4Z7byuOO0yShBeeGdO29pT1BEA5vVHgvQ6W72rxoBCoqoPZyvhUiymF3tNYZa7dfibL3bw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

### **Overall CodePair (Interviews API) Flow**

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047081784-?Expires=253370764800&amp;Signature=EC3ZDzn1vknHmkb5KNjbjWqw77Y~BQbqvpnXYN1yKntEg~M0IODSfqRKFUxz8TagZf69pWvrb6Ov3dWio0ORV4VIRsY7dAhMmyj5tVXRcsEj6xsBwjjjTNIN0X1wY7udlMuvi4lt~WjJYqCehh7Oh3NF~PCUR12~1eOJBj7lUKnK16SLEYJJrJAuDt7GxlsVfZV~Jbsjt~CeoE0udbJsiL-EXSWy9FfnJ8R87rXhJEVKWBFItrtMvYU5zQ78ZeURZ8QtuE-BcJZiaSAeSiQFyp22wXjz93QeUwuaDNc3A8KM8C3YwSY0IeZnPotERGRo3VguRY3awt9vcpjzN0qRFA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

## The integration Process

### **Sign up for a Free Trial**

Head to [https://www.hackerrank.com/work/signup](https://www.hackerrank.com/work/signup) to sign up for a free 14 day trial of our product. This account will be required in order to explore our API (see below) and to test your integration.

### **Explore our API**

We have a simple RESTful API that will form the basis for the integration. You should start learning about our API here:

[https://www.hackerrank.com/work/apidocs](https://www.hackerrank.com/work/apidocs) 

**Note:** The above documentation is written with our end customers in mind. You should explore the API in your test account as an end customer. If you have any questions about the API you should reach out to your HackerRank point of contact or raise a support request by writing to [support@hackerrank.com](mailto:support@hackerrank.com).

### **Register your Integration**

After you familiarize yourself with the API and mapped out the flows you want to support, contact your HackerRank point of contact or email [support@hackerrank.com](mailto:support@hackerrank.com) to request a **partner key**. HackerRank also issues a company-wide API key to use with your integration.

### **Change Authentication Mechanism in your Integration Code**

Make the following changes in your integration:

1.  **Add the partner authorization header:** Include the following custom header in every request:

    `X-HRW-Partner-Authorization: abcd`

    Replace `abcd` with the provided partner key.

2.  **Add the user email header:** Include the following custom header:

    `HRW-User-Email: user@email.com`

    Replace `user@email.com` with the email address of the user who initiates the request from your application.\
    This email must match an existing user in the customer’s HackerRank for Work account.

3.  **Use the Company-wide API Key** in the place of the Personal Access Token you would have used while you explored the API in your account.

4.  With every call you make you may also choose to **include some additional metadata** in your payload if there is metadata you need HackerRank to save. Some commonly seen fields include

5.  **user_email** should identify the user initiating the request. This should match an existing user in the customer's HRW account.

6.  **candidateId** may be the unique identifier for this candidate in your system. Some API calls are not candidate-specific, and in such cases, you can ignore this field.

7.  **applicationId** can be used if a candidate is able to apply to more than one Req. This can be a different field and identify the specific application. Some API calls are not candidate-specific, and in such cases, you can ignore this field.

{

    ...

    "metadata": {

        "candidateId": "16651587",

        "applicationId": "25145412",

         "user_email": "abcd@example.com"

    }

}

Using the Partner authorization token and per-company keys are important as we have a different set of policies and rate limits. It also helps us troubleshoot customer issues originating from you more easily leading to a better user experience.

### **Integration Validation**

Once you have modified the integration to use the above partner-authorization, we will evaluate the integration for happy paths and also some of the known corner cases we have run into with integrations in the past.

Review of End User Documentation will be an important part of the validation exercise.

### **General Availability**

Once the validation is completed we will add an entry in the ATS Integrations page that shows all the supported integrations. Using that interface common customers will be able to enable or disable your integration by themselves.

Your integration will be available as an option on our Integration Settings Page: [https://www.hackerrank.com/work/settings/api](https://www.hackerrank.com/work/settings/api) 

 

## Integration Best Practices

### **Error Scenarios**

In our experience with ATSes, some common scenarios that lead to errors in inviting candidates are:

1.  The API Key is not valid for your HackerRank for Work account. (Needs to be the per-company Key and the Partner-authorization should be working properly)

2.  The recruiter's email address for the ATS account (sent via the metadata) is different than the email used within HackerRank for Work (e.g. using sriram.karra@hackerrank.com in the ATS account and sriram@hackerrank.com in your HRW accounts). It does not matter which one you fix as long as they are the same.

3.  Candidate email address is missing or invalid

4.  Candidate with this email has already been invited.

5.  Recruiter does not have a "Recruitment Seat" on HackerRank, and as such does not have the privilege to invite candidates

6.  Recruiter does not have permission to access a particular test

7.  Recruiter's HackerRank Account is not activated.

 

We recommend that you test your integration for all of the above scenarios and ensure the application behavior is graceful.

### **Error Handling**

**Tests API**

For test API we return errors in two different formats - you need to cover both formats of responses and show the right type of message to the end-user.

**Case 1:** The error is local to the candidate, for example re-inviting a candidate. This has the following format:

{

  "data": {

    "username": “error@hackerrank.com",

    "password": "96d3efe9",

    "test_link": “link",

    **"status": false,**

    "error": 1002,

    **"error_message": "Candidate has already been invited to take the same test. If you want to reinvite, cancel the invite in your HackerRank for Work account first."**

  },

"message": "No candidates invited.",

}

The bolded fields indicate that an error has occurred. If there are uncaught errors in creating the candidate, they also display in this format.

**Case 2:  **If there is an error in the recruiter’s configuration itself (usually as a result of bad config or bad format), it is returned in the following format:

{

  "data": {},

  "status": false,

  "message": "No such test exists",

}

Actions triggering this error include invalid recruiter account, invalid emails, incorrect test id, etc.

Successful requests will be returned with 200 response codes.

**Incorrect Access Token:** In addition to these two error scenarios, if the user has configured the integration with an incorrect access code, we will return the error in the following format with response code 401:

{

    "model": {},

    "message": "Invalid Access Token"

}

**CodePair API (Interviews API)**

**Incorrect Access Token:** If the access token present in the request is invalid, we will return an empty response with a 403 status code.

**Invalid information: **In case the request has one or more errors other than the access token error, we will return a list of all of the errors in the errors field with a request status of 422. For example:

{

    "errors": \[

        "title is a required field",

        "interview time range is invalid",

        "......."

    \]

}
