---
title: "Oracle Recruiting Cloud and HackerRank Integration User Guide"
title_slug: "oracle-recruiting-cloud-and-hackerrank-integration-user-guide"
source_url: "https://support.hackerrank.com/articles/3350882088-oracle-recruiting-cloud-and-hackerrank-integration-user-guide"
article_slug: "3350882088-oracle-recruiting-cloud-and-hackerrank-integration-user-guide"
last_updated_exact: "Dec 28, 2024, 4:37 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Integrations"
  - "Applicant Tracking Systems"
  - "Oracle Recruiting Cloud"
---

# Oracle Recruiting Cloud and HackerRank Integration User Guide

_Last updated: Dec 28, 2024, 4:37 AM (Last updated 1 year ago)_

HackerRank integrates with Oracle Recruiting Cloud for Tests and Interviews to facilitate an easy and seamless hiring experience. This document walks through different use cases supported by the HackerRank—Oracle Recruiting Cloud (ORC) Integration and covers FAQs.

#### **Key Features**

- Send Test invites to candidates from ORC via your Candidate Selection Process.

- View candidate’s Test results in ORC, including score and evaluator feedback.

- Have a direct link to a candidate’s Test report from ORC

- Include Tests in your ORC job application flow - you can choose if candidates take this Inline (while applying to the job) or at the end of the job application.

- Generate HackerRank Interview links for Virtual & Remote Onsite Interviews with candidates.

- View Interview results and scorecard information from interviewers

- Have a direct link to the candidate’s interview report from ORC

#### Prerequisites

1.  HackerRank - ORC Integration Setup is completed

2.  The user has access to a HackerRank license

3.  The user has access to requisitions on ORC

## Types of Assessment Triggers supported

Oracle Recruiting Cloud offers various assessment triggers that can be configured to send assessments to candidates. HackerRank has built the integration to support all these configurations that users can set up in ORC.

These include:

- **Selection Process (CSP) Trigger:** Assessment triggers are tied to ORC Phases and States while configuring a requisition. Each Phase and State can have one assessment tied to it. We support both a Single-phase setup and a Multi-Phase setup. In this case, we send an email invite to candidates to complete the assessment.

- **CSP Automated Initiation via Phase/State:** When a candidate is moved to the trigger Phase and State, the configured assessment will be sent to the candidate.

- **CSP Manual Initiation:** An assessment tied to any phase and state can be manually triggered for a candidate without moving them to the trigger state.

- **External Applyflow Trigger:** When this trigger is set up, candidates will be asked to take the assessment right after completing the job application on their ORC application profile. We recommend using this trigger type only for HackerRank Tests. At this stage, a live HackerRank Interview would not be logical.

**Candidate Experience:**\
After a candidate finishes applying for the job on the career site, they will land on the application confirmation screen.\
They now see a message that they have submitted the job application. Here, they will also see an action item to complete an assessment to be considered for the position with a link to take the assessment.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340601899-35363875917459-b6ff1d3f-2b0b-4a1f-b951-0a711a6df27a?Expires=253370764800&amp;Signature=ukIpai7DjBW-qBdSWB9LS1C8LVrqMMkOo0~JtEhDQQaDOIvyGlHuTwAOmnXCfYPwPqb8I-5U39gB70qZ7HCwPFjrZumDm2iLGFqDnLCMytIAeQAjIEBrJ-M~xE4a4NQbNOeJLUj6JnYdOwEa6X1pV0ymt4tDhAnNs7sQPzL57M2a7GLxHpSN-irrJiwrmOnjk7QzUImF7KNPd8Oc7VFKkYqTqn8UO2PanUThZzih4Jfetba1dOwY4OiI8dhuzRx5vbalve-bCI5I4wcFStSLJoC7nthh-AkSDxRFxQ~I5YOW7nqtZYdqMWXFPR7iqvgwonzKGXQ8GrLG0DqN~KwzFQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

In addition to the message shown by ORC, we also send candidates an email invite. This will use your default HackerRank email settings.\
This is if candidates miss the message on the ORC page or want to attempt it later.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340611466-35363887474451-c6e9aec2-adcc-4d12-afb7-6935f42234ea?Expires=253370764800&amp;Signature=BId0OzCCcAhpOpdqh~K6-PHIugiGgtiffcfuvbBNwGVbaubkCpZ-u-iUnclM20UWK~YNLtTArlpqLva33Gke9c3Q8JVtmi2OTUAKmjyLha3ebwA9U03WlmP-FAsIE0UGLpfTeqE6YHYCXbNq2QS3tagVWlXo3JYux-3LPa1AANYSfkdQwgNJItFWbbkNKNL7SYRiWmY0u~hsi-iCNYhGYw7lqzs8blmF7J5oeDBm8TbrSGAIKH2xFo8P9L3H~4Vl96KPcLCrrt~KMCpFFyeP~YrS50M0klDm~BusJ3ra2a1jgiIRqsn6exwgmMhoMMhT-Vi3S~E3GbGuMnQeSjm7Cw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

**External Applyflow Inline Trigger**\
When this trigger is set up, candidates will be asked to complete an assessment while filling out the job application and before submitting it. We recommend using this trigger type only for HackerRank Tests. At this stage, a live HackerRank Interview would not be a logical assessment.

**Candidate Experience:**\
While candidates are applying for a job, they will see an assessment block that informs them to take an assessment. They need to complete the assessment before they can submit the job application.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340622362-4412386484499-2c7977bf-acda-4070-b4ce-1ecb1888000e?Expires=253370764800&amp;Signature=Q1MOxPJyYCmZcRd4k-VORsbO2szx3w3kDH~-JGrRxbmbsS2i4oeOFL0Gw-Acbpm4utQxTCjAeXjnaNQNEKtafzAk3yfVVzJBbUrwLUAqZU7q9W54berodyn0uknamVMF1yxIf4Fkwira~bjaP~8YZVTRtEXw1oVJW-dvRPhAS7poWeAqTsDMMUQNQ5dCSU1qTFYjPKF7PSGxiRrmJVG0SD8-N4T8Cq4NMPhioC-z2jXSxigai6HQ5iwr9vuPqaz4to6-s7SnQj7~beUJN~HqwYNXAZ36TAuuZcFxJJwlLFculSu8v~03zubpHUCN6E6IQQ40Rw7Y1BmbrPZYehCNUg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

When the candidates click on the **Take Assessment** button, ORC redirects them to HackerRank to complete the assessment.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340632970-35363887475603-c1ae39a2-4b1f-4080-97c6-aa24be06a3b0?Expires=253370764800&amp;Signature=IB3cnxu4I1VViXe36LDiod9i2cN2jL1B6vl-q790VmRtRjFxLPVLgDT0mGDhfFAnFZ-8aisXcp72wXypIYYfwaTW4ndKLA9YkqO9zqvV1E~d4dd2e5QpR-JXyHhlYcA8vB-TefQRBN9caUlWOdIb-1fceCEdiRpV9sT5uuM8itD8PJcQ1ifW3Y2UCiemZ16NE6O6lvmk34236lq3WK4~zbG-Nk3p6JH-Sm3n-RSFU7OiDgtHZ83DkKr8419EyhDOpnFgVmtMgH4uvGXRENRtKFQVFPXJ69yukk0raAYHuNZOC0fe6dVfQrZ9~qjh295s9JHRpoLoCEJT16lWJw8mXg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Once candidates complete the questions, they can submit the assessment.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340641216-35363875923475-12879782-7f51-424e-aeb1-3bd599f120c8?Expires=253370764800&amp;Signature=TKT6wLSvC07NZ2PNp4KWJQBzw3TLNNMdkGCaE7yVezcZ7Vkq975FXAfudyrhzzZsZ7qZ3AKlR7KEXcq405l9uW8~21KC~2fi1NLczUPMOkv1iA7OKgXqRG4XtyxS5J3L8UbueHLX~Qe~gj89AWPgCCAtpIP-I42TJTEs9YgQzSON5wAokgQ14Ry1noEFwPv0gmFqNpGpT5q2En09k5oPUJ4Belxgg7aE8wdME461EdWoQrfyb98x2-BX80oz5T4U1grHnF5YI5LUHaZQ7IH9VxIEj5NuAb6V0Q4VQTLq6hQjd2PevpxwCgY0I3KNivAZvV1UqI0JClMO-Ez5fhptyg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

After submission, they see a success message for a few seconds before being redirected back to their ORC job application.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340651516-35363887478675-153b11df-f87b-4e0a-a656-ef5790dee665?Expires=253370764800&amp;Signature=Xmyo1RqVRNnqsBPcIwti-N9w1BdZtcT~yol~wVIygX80XSLXwa2urNQKTCMiwb1QD8JrzEW74nJizNvwCs-eNPQ5GlpuVuAe5Y4cd9HBgI7NkcJ3KY0o1cclSQrH2z8FhFj-QrYLImaiSfKQJe0KOJKmWbkhju210zsHg2J8PUCF0NK5iLeT08U95d5GNCndZIQKl~WSYTVzoG8JovCeNzfABJlyUVc2Gp2IB~TbSmgRJV9yrA8ArcgoFQ4xT4gYjDhWzAqpmtJiqnmJ7F1LyoUOGlM27XINcS3vzPU6rglFKt0plVHF-57hPMOVn9zBJ4bf9xe2ZJsqijzMjsGA~A__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

At this stage, they see the ORC assessment block updated to reflect the completion of the assessment. Now, the candidates can submit the job application.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340658182-4412378713747-3ee57e83-0dd9-496d-b69f-54414d0485d6?Expires=253370764800&amp;Signature=GS9WOy3VBWlTRTelNCKZo~ubxZJv6z7rHKaQAbfKFvBjLCuUUxnMbr1hZxR9cu6ItcEgvtbATPt7RxMP2cKMizCwXuDWzHxSXcQ1PduIOTVYjpe5UGFUGsi15dIe8IdRSGX2bjjgq3ed~P3IaPHNYUlh15MpsyTMYdvBl1eypNGGs0f6qaTWtJYp2pgK9kWBjEON8v7z4RxgT5XMu5diB7WBNcprPAtMt1VCPj6pSaN82xDb4uS2KlX1NzHcx6v5ohRDcVwBopJbAJw4FTs1It8BlgQ~tdeazP4ixoylKaWr~-jDykRI~b-ZAuDhE6~nktX~WL3hLHM5qE2nFvq3~g__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

For this assessment trigger type, we do not send an email invite to candidates since they will be taking the test before applying and cannot attempt it later.

## Types of HackerRank Assessments

The HackerRank platform supports two types of assessments. Both these types of assessments are supported via integration with ORC.

- **HackerRank Tests**

  - Includes asynchronous coding tests, code review questions, and MCQs.

  - Includes Projects.

  - For HackerRank Test invites from Oracle, we send email invites to candidates with a link to take the assessment, except for the External Applyflow Inline trigger type.

<!-- -->

- **HackerRank Interviews**

  - Includes synchronous interviews with single or multiple interviewers.

  - For HackerRank Interview links generated from ORC, we do not send email notifications to candidates. We send the links back to ORC, and recruiters or coordinators can share this link with candidates and interviewers.

## Adding Assessments to a Requisition

Once the integration is set up and your team has defined the assessments for a job, you should be able to add HackerRank tests and interviews to an ORC requisition.

- Navigate to the **Job Requisitions** page under **Administer Workforce** \> **Hiring**. Click **+Add** in the top right to create a new requisition.

- You will need to follow the steps to create a new requisition, which includes all the necessary requisition setup information.\
  \

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047164072-?Expires=253370764800&amp;Signature=oncFgv0rm4uiFQDHfQ5zFJMhoVPkFCochPEQdwspDFkFIDxgn35NpR9gKs4pRnTbpNU8p0wmE83DwTB9F1CjF6~L6AZY3-LzwtwmPycGmvmNt71ekyZbZS-jw-bjUrlMIkSLaW-MK3mlNq4fYDD13PJes31cZoW-0HUr9Mt3mUpBC2YqInMC4a0OjXsgxkeAVyM8pJQfcnn-AekvptAjXq1aj5wSlry9QQrOAfeiBFE8hch-s1zT34RXnRlYMeUd2ANwzp7MSpvXL4jYNcIyENu-Dt9xgZMaze2a0yighBBsuy-5iZ9iWSrIemaABuzDJtOn4Xk8fpYsLmnbRCrhig__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Under the **Configuration** setup, you can choose the preferred **Candidate Selection Process** and **External Application Flow**.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047164478-?Expires=253370764800&amp;Signature=MLozxF3LD56jN~m7at8x9Vi8SSmTW5XXFA6naWc3qBxvEavjBhRUd3cX1ji64fQeNzM2ifEFB9GHZ~ak7FulcWNOFJltaOfUCwPmuU3O2EEMRjBKd29n1KLPYVP0Vuu4QGL~sUDEs0B6QrxMddNgRRgl4mgCNB50pgPvAkB484z0FIdXgI4xC~46cID7JAgJj-~BixIpusiFjMlYgoZRBbZz6GjzotEKHlOnJUj4S86zFPzhAWsFJxx05n95846SIjcpfAjH9Nq4CVtA3-KGv-YhJZGoA4XEQzOIM2o152EHGIjfnGMdNtfqvl6xR9PD~urW0bblvepCoIprPQARaA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- You will have the option to define Phases and States that trigger an assessment based on the selected CSP flow.

- The **External Application Flow** will define the process through which the candidate is presented with an external assessment. If you prefer not to include an external assessment, the selected External Application Flow will not affect the assessment trigger.

- Under **Screening Services**, users can add **Background Checks**, **Assessments**, or **Tax Credit** services. Select **+Add** under the **Assessments** section.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047164908-?Expires=253370764800&amp;Signature=qYxsIU4NW~pNdErFPycj9qCxyZW8L2WuKinl1x-vPMOtNaRX1kxzTK9jgIbpCveqwrp4-Pnkvs-lD4PV87tulSRVR2TJZvBoBDvVDDGRJvkFBf~-fS5Jeb8mCGJ-4t4dMoe6yyPgvssJS4nX8UKi0yZlQ-SHflFXoHkDvPBGjyaMk0B7GuD6BAV~hoZf7GufcMn4CIURXZ~yxOlwSgc-QOOazrY3nFOj3Qxf6xoA8CzfCpUqnJzd2bxGxj-kH7efPelP-wNqpQTSuXkTOms-QsksOLNsBZxxe0p86ltQExTRTdE7U-zSXxh4vBh0uVH4TRCv0XPYjV3ng7sDiDxz8A__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Select **HackerRank** as the assessment partner and choose the relevant user account.

- If you have a specific user account provisioned, you could use that. Otherwise, select **ORC_HACKERRANK_USER** as the user account.

- If you select a specific user email under the user account, then you can only choose a HackerRank test that the user can access. For **ORC_HACKERRANK_USER**, you can select any HackerRank test in your company's account.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047165316-?Expires=253370764800&amp;Signature=XZPd6ZE5lpFhScdEL57rJqno-vIVuyl5nD0JhBm-2bK94eoYzpdV91nMGcrmCEk4uYxjLUwX5UqjsXCUauCrXBtpDnC8yKDeVKMfDXYWGWfHz7HMNRJ1rcQm5rfMnv0t5KTs7mTbuSVbf2POZYafgNvqcb-pa70rfrnuh12H35pf2liHfXoQTQoMXuYAaa-rBow0JdiB15gmmIk~fTrRi7Qqn5KeVQnVel0Ns5HHoYIuWRZZnPPHgDmT4JZLVHl7DJzrojbzs3A~vPPCm2lMn-fAOuIrhje28BM52gfJdC7JJGZqUqCV-GczgZodMh7DOSARqeWsBjWFywplrO8Mdw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Click **OK**. Then click on the edit (pencil) icon. Since the **Add Assessment Phases** box is not selected, this is a single-phase assessment setup.

- Users will be presented with options to choose assessments for various flows.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047165732-?Expires=253370764800&amp;Signature=J1qYmeA92fjMuyxRV6kmmbLuGCBI3V1X0arnPY1EXp3ldfwjniMudI6nNGp-6V9pGa5v~GrT4fvIeqcrH3yVTXB2zclhiCfAkPeMFZzCd~oJKpDo7~18e-~iHweVqrcqs0o90fzuwjbmkt01gOBT6GL8Nrow7XvEXORlVzqmXjJNsaZOJHWzC35DYAbuaovxqOFDGBoY0OXphL-4FFGnXvWA7QMcIk03VJnt6OZSJncE7Tn44N~FWeQBw71Zk86gYl4lCBo6a1tparHBS8AuEGgsd1JQzkEazWsGSycO-TmgJ6bDsBc58gSHgGdOULhoEqn3Ine-jIulx-Ygo0zpOg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Assessments selected under internal and external job assessment flows will be presented to the candidates as a part of the job application flow. (Defined by **External Application Flow** chosen in Step5 )

- Users can also choose a single Phase and State to trigger one assessment for the candidate. The Phase and State can be selected from the drop-down, and users can map one HackerRank assessment to it. Users can choose a HackerRank Test or a HackerRank Interview. This assessment will be triggered via the CSP flow when a candidate is moved to that Phase and State.

  - **For HackerRank Tests:** Choose any test name from the drop-down menu. This test will be sent to the candidate when they are moved to the mapped Phase and State. Please ensure that the recruiter assigned to the requisition has access to the test on HackerRank.

  - **For HackerRank Interviews:** Users can generate a unique HackerRank interview link in up to 5 interview stages. Note that multiple interviewers can use one link for the same candidate. Select one of the 5 HackerRank Interview options for each stage where you must conduct a HackerRank interview.

- Select HackerRank as the assessment partner for the Multi-Phase Assessment Setup, choose an appropriate user account, and select the **Add Assessment Phases** option. Click **OK**. Then click on the edit (pencil) icon.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047166106-?Expires=253370764800&amp;Signature=C7dkKv9AGFz5c3hs~cSlN9dlBwGGMuyajIYVHwNrkfPqo6~YOPgmaUJpqGOk1BUWcXwFDdcQUsZ7d2W2eNspbeLsIdQ2A4aRdgd~OwMBQ9zyszQfSylEsB7UnNkTXmpEmlKnb-Yd1bKNtVVs~z8P2GdWMnlRKPCxUKrA4OeHb9rMKnrBWucwn3TJsVctrrQboQSQpRdZ52RcPvW43LrEYO8bbFR2v~cxOGB7vMDlPKz9Rty4ekwuzQnfg6fmx1zvQNxn3ODUJdsErFqFJLQe8rgGQ015mnVcIVLvI4Y9E7nafLrRyvHF1K1az7-yv6bT~9DqOLw7tuKCIYAAqmM3Kw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Users will be presented with options to choose assessments for various flows.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047166475-?Expires=253370764800&amp;Signature=p71mFKM1ZXIK480S8QIjn1nJHZBaLOuUiKKictz6E5IRke0gZVx3WptzsgLDKsaFE4yt0LgmNriP4cjP0Vu9PEdCl5letjYZ99eTLH6TZpOMklCe3no95flOR1Yo4PaUXVUU-Sq~FVyX6WR~IxrTHyu1cbeqO-ZgAvEEKSuRMcg5hHTG2Ylw7m7gyoEzf-odO8RwPtL0Vsad3kzRkPbTWPN0WO~Y3x~FYgq1dxX1nZ7xXZh4smQz2BG18g5COphlNhudFiqaPpyxT3N7Q3tqRVzyGPKYC~fVfbOfkv69e73KIjwk39CnQuKHanovBTkGsAzCn3Cy4DsxFqdSKCb9tw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Assessments selected under internal and external job assessment flows will be presented to the candidates as a part of the job application flow. (Defined by **External Application Flow** selected in Step 5)

- Users can also choose one assessment to be triggered for each available Phase and State. Under each phase and state label, users can choose a unique HackerRank Test or a HackerRank Interview. The CSP flow will trigger these assessments when a candidate is moved to that Phase and State.

- Click **Save**. Proceed with the requisition completion. Once it is posted, the requisition will be available for candidates.

## Triggering Assessments to Candidates

Candidates can apply for the position once a requisition has been posted and live. There are multiple flows through which candidates may be asked to take an assessment.

- External Applyflow or External Applyflow Inline Trigger\
  If an assessment is set up to be triggered as part of an external apply flow, it will be presented to the candidates automatically.

- External Applyflow assessments are shown to candidates after they finish their job application, and inline assessments are part of the job application requirements.

- Both assessments will be visible on the candidate profile. Once a candidate sees one, the status will be shown as **Requested**. Since candidate actions trigger these assessments, they will be tagged as **Requested by Candidate.**

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047166895-?Expires=253370764800&amp;Signature=mvX0ZPCRS4Dux7vfGVfnT81i3iArjniIXD4xwV1-ZguZ8Lvhr0oL211Oh~KekGFp799SM42DCTFSrzfCn0CRdxKpXLCGeCwiqyDyw-S7QnPcp5mdqYvAVaG72OGL9j6Y8QjMFlGzRwpzakhsH3eB6EOOPYooONhDuYqG-SH7ESrjbK-34kSYKv8ToDYIeJ4yNqk3LV0oYEFIcn3~-ehULetFL0H6d90x-xniuqfnw2UhsZVlAJYKR1UhnQnIN9u2BcC-3suv7eeL3zymK-vYWzkpRtN3~2E7iTyYKZBPbTZI6ghS2jsUp538IBS~N6~nHwmONmwgJ9MHl~IgBK7yTg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- **Candidate Selection Process Trigger**: When an assessment is tied to a Phase and State in the CSP, it can be triggered by moving candidates to that Phase and State.

- Select **Move** from the top right within the candidate profile to move a candidate.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047167298-?Expires=253370764800&amp;Signature=acyorCajyukdFIwaXBmFAYr6cUVdWg09DN~3IZVUfHgVfDbaP6-O65iOwlBeraBSMB8zR7I8nlIV1cFRMvyecOxCTnGoo-6F4jR3o4EOevkPyZKFKYY2AKRteFlyEfoKTuJvKiKd0EAdwXShF8UrrwMvqUvmhPBADbdfe6oDl7O8OHW-lriGrXA9GR7V5OpmhMNb2~Eyj9gARW~bvLyPaalRB88In1z0oz8~iQ6ALKZq9sh3bgLr-OB1sIvieUf5lCNVUTWOfikxau1eSS5~~h4DK-rMoflb09vmjfZQ5G~jXruV17JW6rG67hn2UffMG9W7xeGQsRM64C19sGXEzg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- From the details section, move the candidate to a desired Phase and State. If an assessment has been set up, users will see a popup confirming that an assessment will be triggered.

### Triggering HackerRank Tests

If a HackerRank Test is triggered via the CSP, candidates will receive an email from HackerRank asking them to take the test.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340770546-35363887481363-f0fb7876-b1b8-4145-9124-7d8dd2634bd6?Expires=253370764800&amp;Signature=rkAcdV9ytkD718eOeQUwdetfdZoyxuUv7ItSdNBjEmzFmR50ejdJuF2rqAf9gCzP5gsnu9qk~o~GVyTXRPW45JSuxkhJiqCvVRjuL9bwcle~gS2yQwWrLGpP54nTl~hxITnViaXU-lj2u-so4YYSnRjR4mdVyV~YTVrqS7M-qDS004nNP37MrG-ni2Z5vxsHJXcxfxRb7Sac2OtIvM3-iWg~92AfG-XiPcne10yBVcHFQ6OYn0YHC6ObFcgid7N8dIvy57tSYbEk6tUrDcWeGXIr0XWt3AwoIl-gydxEGtmE8QkgX37ocm8evNA4Xj4o9FHluaLJDeDlQMmUBTOWKw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

If a HackerRank Interview is requested via the CSP, HackerRank generates a unique interview link and sends it back to the candidate’s ORC profile.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340782121-35363887485715-daa68a11-988c-4e70-9939-832e4bed15b6?Expires=253370764800&amp;Signature=ABRn1ZXcWH~84jHtAwSExvC7StEk4X-0n8t0CwR~N9QdKZGpe2WavnP4LyQ43YmAxIupbR5zKqv7d~GLrf4HkEgKxclUhwagkFz-CU75O8jJmfpfXQFFq2-PE268UXc-thPqwfHfw-a5YvVJfZsM8nmG6snrg2dFR1cacOp5ANH2WNTtZIVKLB6rTdXCe6iY0nMilHybBx~UxM8H2JRuxWg~m8LLbVcSCyDtVE-BbgaxfLGJR-6qva9Q221AsvA7X8BxXnFO6uQJAtleRCtozJEVhilBR7SO6y49UMbkjV9ZJsarQ4jYHKwJRWhyk9QcXzvUgHZEIUFG2zLF9QmpQw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

After the assessment (test or interview) is triggered, the candidate’s HackerRank profile will also reflect the action. This will maintain a mapping of the user who requested the assessment from ORC.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340790163-35363887486995-64cfae9b-1400-4eb3-8fb9-9e58af869043?Expires=253370764800&amp;Signature=YlsdcUfke-sMOK6B-kxrMvmQGkbPY0T96seE6EPmqWFT310uGg~pRyYzA43xRKEkIxdUZPxmkq6FSbAzHjFZ7izRLmdRfI3cHAuaimnObfZMs7~21GuhbAcnwDUQgTvqV2soGzvFqwYpY8e96XEj-mOqKpWl~9mDpsXznYHGavB6fc~1OSOSSjIZx6QAV5ajS5ws3KwvQz1KnwNPeDxSH~53ZOfVe66lJg0PXvthw0Sldb9vbYTcUGAa~64gcfVjccnP4rye-DARzQpy3onvE0CEZqOHzS5NJUyeIKe1NOXo0hTQGvs2FB5CClUKJ2BqiOq0f19-X63ZynFsu97R-g__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

The recruiter requesting assessments from ORC needs a HackerRank license with the same email address.

## Reviewing Results and Evaluation

Once a candidate has completed their HackerRank test or interview, their results will be available on HackerRank and synced with ORC.

The feedback available for HackerRank tests and interviews is different. Here is a screenshot of the candidate’s ORC profile before completing a HackerRank assessment.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340801992-35363875937811-fe26ed90-e9c4-45e2-8d42-438704775eb1?Expires=253370764800&amp;Signature=kySW8HjVuOIwNrQjxH8Xhizvbw-IeGqr30TiH6DDF61UKhvNKEdZVhbN~zY65H8yIphQbkx7l8oNPiRaut~sdtmziWsQhPT4WyjmlVWvj0M~HgbhlD9Hva0d3wmLrKq2BhaVY7y2oRBh5-jM8kx62bojyINYkxc3OVROBOz2R7upZrt7zlOYxDBhanIpDDAG~O7hIx1l6CI9Wc0Rav7xTgb9F-ekgsHmyMIanUTcvfTRJfHIgifhGj9qpdUcc4tFE2avWW9dkz4LasPnbNpix72mhz9kWtG-X7oo4XQEdjuXaLMUDlvucnXDezunQ5-f7r06cNSxmMTHwflQY0X20A__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

ORC provides six fields for HackerRank to update:

- **Status:** Reflects the status of the assessment

- **Score:** Candidate’s score on the assessment

- **Assessment Percentile:** Percentile based on the maximum score

- **Band**: Current band on assessment

- **Comments:** Additional information to help understand assessment results

- **View Results:** Button with a hyperlink to detailed HackerRank reports

### HackerRank Tests

After completing the HackerRank test, candidates' test scores and percentiles will be sent back to ORC.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340811216-35363887489427-465c536c-2466-4d3d-a7bc-f70cf9e42646?Expires=253370764800&amp;Signature=uhjcYxXV0DoWf62Mn1l1EUWTtUH2Ktbem0HiE2MCpirv7dOZv7zTluLfO-nts4expuTKEMCo6aCvEluaszwg0giFKNQRlpZ2PynWfyqMgwmfrWUIam1TUoUHNBBOQJ0pQuyJO3KI~95-IV-Mv6Vimsupvr7Fkb9Er9UWNPiZhHJGHUNzAg85YpN09y09pBl6mL6e-sgP2Y5ogwun1wNh~i2DzaCYKp1JC3ViNMlM1KdP5g2HnyvD8zTEzmFTMs~yDRrz7NiBNmKyNkouif2CAr9UuJB6P2YE~NUipy6qOXaGjMaZ3UNATYIDlH3QYtd4jeEEepOGjRjoZ2KMdCT0hQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

HackerRank updates the provided fields as follows:

- **Status**: This field will reflect the latest status. Based on the type of trigger, this field can take one of the following values: Not Triggered, Requested, Initiated, Started, Completed By Candidate, Completed - Pass, Completed - Fail

- **Score:** This will reflect a numeric value for the candidate’s test score.

- **Assessment Percentile:** This will reflect a numeric value for the candidate’s test percentile.

- **Band:** Upon completion, the band can be **Evaluated**, **Pass**, or **Fail**. By default, it will be set to **To Be Evaluated** upon assessment completion. If a cutoff score is set on the test level in HackerRank, the band will automatically update to **Pass** or **Fail**.

- **Comments:** For HackerRank tests, we provide additional test results in the comment section. This includes the **Max Score**, attempt end time and **Question Details**.

- **View Results:** Upon test completion, this link will direct to the most recently completed HackerRank assessment report.

**Evaluating HackerRank test results**

- When a candidate has completed their assessment, the result fields on the ORC profile will be updated. The following two fields will indicate recently completed and unevaluated test results.

  - **Status**: Completed by Candidate

  - **Band**: To Be Evaluated

- Users can review candidates’ scores. For a detailed HackerRank report, click the **View Results** button. This button will direct you to the candidate’s most recently completed HackerRank assessment report.

- Users will require a HackerRank license to view a candidate’s detailed report on HackerRank.

- Once a user evaluates the candidate’s test submission and code, the user can mark the candidate as **Test Completed** - **Qualified** or **Test Completed - Failed** on HackerRank.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047169809-?Expires=253370764800&amp;Signature=HH3G3FVhwrIvu8sy-bzLPO4qkq7-wXP~wJ-0b0ROQid7GkI3mplhRRGjGOipGgvrqQAZsv54MTXn5okxTvb8Px5v5rSrFvNeOQ7Ws4QUPQd5XKLxKWIPtl5M~spt02JFv2BgP8RH~9vOxkwC048PZViq0A~DUSs~n4gZbpjn9Ey5p7t1jVSqZk-3mzvTSGRDkcruLdGIHJsnbYlpBNOczjtV06knEAIhSEWiMyJankQq9XIy8x3bOnWY-AsV2JMLYRoXoI3tA9zT-EaCecDo5nMrYMcdTEtUiQl1lEwhx1YiZhFYqjEcEC6kALAF3iyJ80jN3NbNZ0kWfBzDTNemqw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Based on the evaluation on HackerRank, the ORC profile status for that particular test will update to **Completed** - **Pass** or **Completed** - **Fail**. The Band will also update to **Pass** or **Fail**.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047170221-?Expires=253370764800&amp;Signature=RdHc3oOV4RmxyzYSevOl2ad6LYv1qpIx0BUFc0Ir8HtkHr-z80ggpEadwl-6PVlt0fn-slpzuQvTuMFZ1i2aTjuUP5dg~MhmJt1kSZWXX1XrosK5Bu4U0vPY5-Bbxbr74HgrerlDvcfIzf06z3hBLbvI-9fW4oHznz~DCC4Js4vvSQBmK-vEr~zdt7zU6gMCWlXGFU-kCMRJi0x8RrcKzRmDWaX4BhVUrTC0LRotHunkT-iFdrNb2olnZPAmrfCVEQjhJt0xkmohp7WDm~og6913jhHzvSOzt3FxvO2MZxWPiWmSvCK1-qtlwHNLm4RWhPQynIbU08Uqi968mlV0xg__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Once this is done, the hiring team can decide whether to disposition the candidates or move them forward in the hiring process.

Please note that ORC only supports updating the Status once. So, you may be unable to update the candidate’s status between **Pass** and **Fail** multiple times.

### HackerRank Interviews

Once a HackerRank interview is triggered for the candidate, a unique link will be posted back to the candidate’s ORC profile. This interview link can be used to conduct interviews with the candidate.

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1735340843580-35363887494163-49343e96-ef1b-47b1-8033-56d86359fc05?Expires=253370764800&amp;Signature=rq7EkSLZvUimrNfEhvQqdFD0zz~rb0KTeG4yhuGnWR7RglKqP6c5iGGJ-p7oZQ43dxSf-H9EB1nAmdcok1DCNNBNpG2HxaQB7nFwpPYkqgle1ri8fDVyz2DUB4TmVPzLZ8RKS-GkZBMPBgwbC1R7jrLvJr0~KVUBgiJFbP6JoaUmpqmXNuSCSRh9Iyzejt0i0-pqrjX0LvIMRb5vD1P7YoPPypWeZfsUjtnGEh6kv8Sa9puZPBWdKJYAnV2aqrNme~YGaomT4zY-3dspKHSViKz6LSUZWDr6kX2p0snNv7Al86nFKNE1JFxEQHDWl8FGOqzZqR~8vYiYjORn40djdA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

HackerRank updates the provided fields as follows:

- **Status:** This field will reflect the latest status. Based on the type of trigger, this field can take one of the following values: **Not** **Triggered**, **Requested**, **Initiated**, **Started**, **Completed By Candidate**, **Completed - Pass**, **Completed - Fail.**

- **Score:** This will remain blank or 0 for HackerRank interviews.

- **Assessment Percentile:** It will remain blank or 0 for HackerRank interviews.

- **Band:** Upon completion, the band can be **Evaluated**, **Passed**, or **Failed**. As a default, the band will be set to **To Be Evaluated** upon assessment completion.

- **Comments:** We provide additional details in the comment section for HackerRank interviews. This includes the Title, Start Time, End Time, Interviewer Details, and Scorecard.

- **View Results:** Upon completion, this link will direct you to the most recently completed HackerRank assessment report.

**Evaluating HackerRank interview results**

- When the interview ends, the result fields on the ORC profile will be updated. The following two fields will indicate recently completed and unevaluated interviews.

  - **Status:** Completed by Candidate

  - **Band**: To Be Evaluated

- Users can review the interview feedback. For a detailed HackerRank report, click the **View Results** button. This button will direct you to the candidate’s most recently completed HackerRank assessment report.

- Users will require a HackerRank license to view candidates’ detailed reports on HackerRank.

- On the detailed HackerRank interview report, users can see candidates’ live coding submissions, whiteboards, and feedback from interviewers.

- After reviewing the necessary information, users can choose the evaluation and mark the candidate with a **Thumbs Up** or **Thumbs Down** on HackerRank.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047171215-?Expires=253370764800&amp;Signature=O2wnp5PqN35z0e9S6oXpTa8Fct9M3D-TrL-DLvXrL0NxFP-8Vue5vU7TyHTZJS4vRPsSxwFaFu~6sdLGAoy53VIT1b-59dV6dR--aViHheZK0V30biV4ZAfFL2oXSEPWHCaPN3CIQ2AlUT-iaxmddOcYD3k12mu95D026NXzzZApJvelbBtHlY4nKINz9cpmcUIMuI~u1i5lvzo1WSsj-TK~DDUbFJq7iZnLzlNBX5wcqb4Ff6jU4lX1AFuUkNef8pmYFOMpcPfTKg3AM2mYRizFnPUEvU84TpPMYkBpfNDMVXVpQtHP0w17HdiOnH2r3-LSePXDBGSj~8d6h1zTCQ__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

- Based on the evaluation on HackerRank, the ORC profile status for that particular interview will update to **Completed - Pass** or **Completed - Fail**. The Band will also update to **Pass** or **Fail**.

  <img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734047171679-?Expires=253370764800&amp;Signature=Phal5gMeEhkE5ngWBWOE9E4sDh3UrFZdcZ3yOQW3F0ZVNycrRz52qMA03~LiVP3s5G5xuVTYBSs-1xgZ1tJd-gFgyJArjG5RlCpKzLoquDANCgqssu4xpAQmCQaR5fuqe6JDiuh8YRjyMKBO4NOne2u-6EvcoEupSFzqD9m4bjMI5zaSHRrqiyjbfXwpYS5o219AgpcH-h6JUaQNuz23mYzWs0Uh3GRqXBag1w5k7zO-8WsanddixnW1XNAtjRJ6IqBoCF0s8D~tCATauIl9KYaq451rc3s~nYvOMYPpdBT6WQpD0HFVu5ogNR782bfs0N9zLCoQd7fjkQS1aHL4pw__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

Once this is done, the hiring team can decide whether to disposition the candidates or move them forward in the hiring process.

Please note that ORC only supports updating the Status once. So, you may be unable to update the candidate’s status between **Pass** and **Fail** multiple times.

The hiring team can follow the same steps to review results for successive assessments upon completion.
