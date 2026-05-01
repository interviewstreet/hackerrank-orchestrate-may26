---
title: "Summary of Bias Audit Results of the HackerRank's Plagiarism Detection System for New York City's Local Law 144"
title_slug: "summary-of-bias-audit-results-of-the-hackerranks-plagiarism-detection-system-for-new-york-citys-local-law-144"
source_url: "https://support.hackerrank.com/articles/9355824728-summary-of-bias-audit-results-of-the-hackerrank%27s-plagiarism-detection-system-for-new-york-city%27s-local-law-144"
article_slug: "9355824728-summary-of-bias-audit-results-of-the-hackerrank%27s-plagiarism-detection-system-for-new-york-city%27s-local-law-144"
last_updated_exact: "Dec 13, 2024, 5:03 AM"
last_updated_relative: "Last updated 1 year ago"
breadcrumbs:
  - "Settings"
  - "GDPR and NYC AI Laws"
---

# Summary of Bias Audit Results of the HackerRank's Plagiarism Detection System for New York City's Local Law 144

_Last updated: Dec 13, 2024, 5:03 AM (Last updated 1 year ago)_

<img src="https://assets.usepylon.com/e6a58e21-be80-4777-9eaf-f73beeee94d9%2F1734046394150-?Expires=253370764800&amp;Signature=jdarGHfEmPbVw30KAZ2LbABPAHcSmjV1aJwDNHnpO6hUPdVKTdfnfvdTbX8RHPL8ZhAv8k8r6swdch0LT4Fhe1igJEYc3nh8GWgXPDL3aUgfoaeJs2r0ep4GoPj6SvDcHm9Yc4YCVMGyGVhm5VZxOL91fWEpUICiBT7IZoQDdZ9mjE7AzO-8LuztC9hwoLX~E95IGKA~xpDTC7smLy6J5s4Tak48RemnRzWsZuhiNHloTNQAnQWO8OsZYuM0p0oJWP4CNYjGYuf6ZjbGAQwRokuvYMT5pgZxkc7K5ojNR8PcPFl3TLsFZwzqFHy-hEE1c0eZgTZGYnzj2SR9YNLsEA__&amp;Key-Pair-Id=K3NV4LZ47N8M46" class="kb-image block" data-drag-handle="false" />

## Letter from the Lead Auditor

From: **Shea Brown**\
           Lead Auditor\
           BABL AI Inc.\
           sheabrown@babl.ai

To: **Interviewstreet Incorporation (HackerRank)**\
      PO Box 1660\
      211 Hope Street\
      Mountain View, California 94041

Re: **Audit Opinion on HackerRank’s Plagiarism Detection System**

07/22/2024

We have independently audited the bias testing assertions and related documentary evidence of HackerRank (the "Company") as of 07/22/2024, presented to BABL AI in relation to Company’s Plagiarism Detection System (the “system”) in accordance with the criteria and audit methodology set forth in this report. The goals of this audit are to:

1.  **Determine whether the bias testing** methodologies, controls, and procedures performed by Company satisfy the audit criteria (see Findings)

2.  **Obtain reasonable assurance** as to whether the statements made by the Company, including the summary of bias testing results presented in this report, are free from material misstatement, whether due to fraud or error.

Note that the criteria presented in this report were constructed specifically to address the requirements of a “bias audit” outlined in NYC Local Law No. 144 of 2021. The system was audited as though it were an automated employment decision tool (AEDT) under NYC Local Law No. 144 of 2021, but we do not make any determination whether the system is, in fact, an AEDT under this law.

### Company Responsibilities

It is the responsibility of Company representatives to ensure that bias testing and related procedures comply with the criteria outlined in this report. The Company representatives are responsible for ensuring that the documents submitted are fairly presented and free of misrepresentations, providing all resources and personnel needed to ensure an effective and efficient audit process, and providing access to evidential material as requested by the auditors.

### BABL AI Responsibilities

It is the responsibility of the lead auditor to express an opinion on the Company's assertions related to the bias testing of the system. In light of the current absence of generally accepted standards for the auditing of algorithms and autonomous systems, our examination was conducted in accordance with the standards and normative references outlined in this report.

Those standards require that we plan and perform audit procedures to obtain reasonable assurance about whether the assertions referred to above 1) satisfy the audit criteria and 2) are free of material misstatement, whether due to error or fraud. Within the scope of our engagement, we performed amongst others the following procedures:

- Inspection of submitted documents and external documentation

- Interviewing Company employees to gain an understanding of the process for

  determining the disparate impact and risk assessment results

- Observation of selected analytical procedures used in Company’s bias testing

- Inspection of the select samples of the bias testing data

- Inquiry of personnel responsible for governance and oversight of the bias testing and

  risk assessment

We believe that the procedures performed provide a reasonable basis for our opinion.

### Independence

Our role as an independent auditor conforms to ForHumanity and Sarbanes-Oxley definitions of Independence. Fees associated with this contract are for the provision of the service to assess compliance. The payment of fees is unrelated to the decision rendered. Our decision is grounded solely in the criteria presented below.

### Opinion

In our opinion, based on the procedures performed and the evidence received to obtain assurance, the bias testing and results presented by Company, as of 07/22/2024, is prepared, in all material respects, in accordance with the criteria outlined below.

Sincerely,

Shea Brown, Ph.D.\
Lead Auditor, BABL AI Inc.

### Emphasis of Matter

We emphasize several matters related to the dataset sourced by HackerRank to test for disparate impact: 1) self-declared demographic labels were not available for the system, so sex and race/ethnicity labels were inferred, 2) the use of inferred demographic labels means that the data is likely to be considered “Test Data” under § 5-3001, and 3) the amount and quality of the testing dataset (see Findings) were limited due the lack of historical data. Consequently, the conclusions drawn from the disparate impact quantification are subject to the limitations arising from the dataset and should be interpreted in light of this constraint. Our opinion is not modified with respect to this matter.

1 This is at the descresion of the NYC Department of Consumer and Worker Protection. 4

## System Description

BABL AI was engaged to audit HackerRank’s testing of its Plagiarism Detection System.

From HackerRank: “Plagiarism detection system uses user-generated signals into an advanced machine-learning algorithm to flag suspicious behavior during an assessment. By understanding code iterations made by the candidate, the model can predict if they had major external help.

It’s important to note,... \[that HackerRank\] made the following efforts to prevent potential bias from PII or coding habits or question difficulty related bias:

- No race, gender or PII information in its training or at the time of inference.

- No typing speed data is used in the model since we consider typing speed is more like a

  personal habit instead of plagiarism indicators.

- Features are normalized in respect of the same question to minimize the bias from different question difficulties.

- Human-in-the-loop decision making: ML coding plagiarism \[system\] will never automatically drop candidates from the model prediction. Instead, we provide a comprehensive report of the suspicious attempt\[s\]... Our customers can review the detailed report and check the code replay by themselves to decide whether to move a candidate forward.”

## Audit Summary

### Background

New York City Local Law No. 144 of 2021 requires yearly “bias audits” for automated employment decision tools (AEDTs) used to substantially assist or replace decisions in hiring or promotion. Specifically, the law states that (1) the bias audit must “assess the \[AEDTs’\] disparate impact” on certain persons, (2) the audit must be conducted by an “independent auditor ... no more than one year prior to the use”, and (3) a “summary of the results of the most recent bias audit ... \[must be\] made publicly available on the website of the employer or employment agency.” The audit outlined in this document has been conducted to satisfy the law’s requirement for a bias audit only, and does not include other requirements such as candidate notifications. This report does not make any determination whether the system under this audit is, in fact, an automated employment decision tool as defined under NYC Local Law 144, or not.

### Auditor Responsibilities

It is the responsibility of BABL AI auditors to:

1.  **Obtain reasonable assurance** as to whether the statements made by the auditee are free from material misstatement, whether due to fraud or error,

2.  **Determine whether the statements** made by the auditee provide sufficient evidence that the audit criteria (see [Findings](https://docs.google.com/document/d/1_ceI6RdRjdXBqr-E8pOOxcGasVvA3sSFOBeXbTv9uR8/edit#heading=h.lnxbz9)) have been satisfied, and

3.  **Issue an auditor’s report** that includes an opinion.

As part of an audit in accordance with good auditing practice, BABL AI exercises professional judgment and maintains professional skepticism throughout the audit. Specifically, BABL AI auditors identify and assess the risks of material misstatement in documents provided by the auditee, perform audit procedures responsive to those risks, and obtain audit evidence that is sufficient and appropriate to provide a basis for our opinion, per Public Company Accounting Oversight Board (PCAOB)’s Auditing Standard 1105 on Audit Evidence,2 where applicable. In addition, this audit report follows International Standard on Assurance Engagements (ISAE) 3000’s guidelines on Assurance Report, where applicable.3

BABL AI is also responsible for maintaining auditors’ independence and objectivity to ensure the integrity of the opinion and certification provided. BABL AI as an organization, and all employee and contract auditors, adhere to strict independence as codified by the Sarbanes–Oxley Act of 20024 and the ForHumanity’s Code of Ethics.5 In addition, BABL AI Lead Auditors are ForHumanity Certified Auditors under NYC AEDT Bias Audit.6 For more details about our methodology and process, see Appendix – Audit Methodology.

2 [https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105](https://pcaobus.org/oversight/standards/auditing-standards/details/AS1105)\
3 [https://www.iaasb.org/publications/international-standard-assurance-engagements-isae-3000 -revised-assurance-engagements-other-audits-or-0](https://www.iaasb.org/publications/international-standard-assurance-engagements-isae-3000%20-revised-assurance-engagements-other-audits-or-0)

### Scope & Objective

|  |  |
|----|----|
| **Audit Section** | **Audit Objective** |
| Disparate Impact Quantification | To ensure that the auditee has conducted sufficient testing of their model to “assess the tool’s disparate impact on persons of any component 1 category,” – i.e., race and gender – as the minimal requirement for a bias audit under Local Law 144 of 2021. |
| Governance | To ensure that effective internal governance exists to own, manage, and monitor risks related to bias and fairness. |
| Risk Assessment | To ensure that risks of the model that potentially contribute to bias have been rigorously identified, acknowledged, and assessed. |

#### **\
Out of Scope**

1.  The audit did not ensure sufficient testing of the tool’s disparate impact on any other protected class beyond race/ethnicity and gender

2.  The audit did not certify that the system is “bias-free”

3.  The audit is not intended for compliance purposes for any legislation other than the NYC Local Law No. 144

4 [https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf](https://www.govinfo.gov/content/pkg/PLAW-107publ204/pdf/PLAW-107publ204.pdf)\
5 [https://forhumanity.center/code-of-ethics/](https://forhumanity.center/code-of-ethics/)\
6 [https://forhumanity.center/nyc-bias-audit/](https://forhumanity.center/nyc-bias-audit/)

### Conclusions

Our opinions for the bias audit of **Plagiarism Detection System** by **HackerRank** are as follows:

|                                 |             |
|---------------------------------|-------------|
| **Audit Section**               | **Opinion** |
| Disparate impact quantification | **PASS**    |
| Governance                      | **PASS**    |
| Risk assessment                 | **PASS**    |
| **Overall**                     | **PASS**    |

## Findings

Note: The information disclosed under each criterion is not documentary evidence.

### Disparate Impact Quantification

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 765.451px; background-color: #6fa8dc"><p><strong>Audit Criteria</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 320.208px; background-color: #6fa8dc"><p><strong>Opinion</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 765.451px"><p><strong>Q.A. Components:</strong> The system to be tested for disparate impact shall be defined.</p>
<ul>
<li><p>Q.A.1. Where the system comprises more than one automated component, evidence shall show appropriate definition of the system.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 320.208px"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Components or combinations of components that were tested**: N/A

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.7373%; height: 299px"><p><strong>Q.B. Testing dataset</strong>: The dataset on which disparate impact was quantified shall be defined and characterized.</p>
<ul>
<li><p>Q.B.1. Evidence shall show justification for why the selected dataset was appropriate for disparate impact testing.</p></li>
<li><p>Q.B.2. Where test data as defined in § 5-300 was used, evidence shall show</p>
<ul>
<li><p>a. justification for not using historical data,</p></li>
<li><p>b. that historical data is not sufficient to perform a statistically significant disparate impact testing,<br />
and</p></li>
<li><p>c. the methodology by which test data was collected</p></li>
</ul></li>
<li><p>Q.B.3. Where disparate impact testing was not completed by BABL, evidence shall show</p>
<ul>
<li><p>a. that the most recent testing was conducted less than one year prior to the start date of this audit, or after a major update to the system, unless the update was more than one year prior to the start date of this audit, in which case, evidence shall show</p></li>
<li><p>b. justification for why such testing was still appropriate.</p></li>
</ul></li>
<li><p>Q.B.4. Evidence shall show that the data used in the testing was within one year of the start date of the disparate impact testing.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 89.5484%; vertical-align: middle; height: 299px;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Testing conducted by**: HackerRank\
**Date of last testing**: 05/10/2023\
**Time span of data**: Nov 2022 – Feb 2023

**Justification for the use of Test Data**: From HackerRank: “Given the data protection contract with our customers, open source libraries are selected for name to race and name to gender estimation since no data transfer is required to a different vendor.”

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.C. Disparate-impact quantifiable PCVs:</strong> PCVs that can be quantified using the testing dataset shall be defined.</p>
<ul>
<li><p>Q.C.1. Evidence shall identify PCVs that were quantifiable in regard to disparate impact.</p></li>
<li><p>Q.C.2. Evidence shall show that the PCVs that can be quantified include at the least: race, and gender.</p></li>
<li><p>Q.C.3. Evidence shall disclose the method by which PCV data was collected.</p></li>
<li><p>Q.C.4. Evidence shall identify and disclose PCVs that were not quantified in regard to disparate impact.</p></li>
<li><p>Q.C.5. Where PCV data was inferred, evidence shall</p>
<ul>
<li><p>a. identify the method by which PCV data was inferred, and</p></li>
<li><p>b. show justification for why the selected method of PCV inference was appropriate.</p></li>
</ul></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**PCVs for which disparate impact was quantified:**

1\. Gender\
2. Race/ethnicity

**PCVs for which disparate impact was not quantified:**

1.  Age

2.  Immigration or citizenship status

3.  Disability status

4.  Marital status and partnership status

5.  National origin

6.  Pregnancy and lactation accommodations

7.  Religion/creed

8.  Sexual orientation

9.  Veteran or Active Military Service Member status

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.D. Positive vs. negative outcome:</strong> Where the selection rate method was used, positive and negative outcomes of the model shall be clearly defined.</p>
<p>Q.D.1. Evidence shall show justification for why the selected definition of positive outcome was appropriate.</p>
<p>Q.D.2. Where thresholding is used, evidence shall show justification for why the level/levels of threshold to determine positive vs. negative outcomes was/were appropriate.</p>
<p>Q.D.3.  Evidence shall identify and disclose</p>
<ul>
<li><p>a. all user-configurable settings,</p></li>
<li><p>b. whether each setting affects positive outcomes, and for all settings that affect outcomes,</p></li>
<li><p>c. their extents of user configurability,</p></li>
<li><p>d. their default values, and</p></li>
<li><p>e. justification for why such default values were appropriate.</p></li>
</ul>
<p>Q.D.4.  Evidence shall disclose the user-configurable settings and combinations of settings on which disparate impact was tested.</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Positive outcome**: not being flagged by the system

**User-configurable settings that can affect positive outcome**: N/A

**Settings on which disparate impact was tested**: N/A

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.E. Selection rate or scoring rate</strong>: A metric corresponding to selection rate or scoring rate shall be defined.</p>
<p>Q.E.1. Where the selection rate method was used, evidence shall show that the selection rate of a group was defined as the ratio of positive outcome to all outcomes for that group.</p>
<p>Q.E.2. Where the scoring rate method was used, evidence shall show that the scoring rate of a group was defined as the rate at which that group receives a score from the AEDT above the median score of the sample</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Method of quantifying disparate impact**: selection rate defined as the rate at which candidates in a demographic group are not flagged by the system

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.F. Favored, disfavored groups</strong>: Favored and disfavored groups shall be defined, for all PCVs.</p>
<p>Q.F.1. Evidence shall show that favored and disfavored groups were defined according to selection rates or scoring rates ordered by PCV.</p>
<p>Q.F.2. Evidence shall show that the groups pertaining to race and ethnicity satisfy § [60-3.4 B in the EEO guidelines.](https://www.ecfr.gov/current/title-41/subtitle-B/chapter-60/part-60-3/subject-group-ECFRf5bdb68c4f63a08/section-60-3.4)</p>
<p>Q.F.3. Where the groups pertaining to race and ethnicity do not satisfy EEO guidelines, evidence shall show justification for why EEO grouping was not used, and the appropriateness of any substituted groupings.</p>
<p>Q.F.4. Evidence shall show that the groups pertaining to gender contain at least “Male” and “Female”.</p>
<p>Q.F.5. Evidence shall show intersectional groups containing all permutations of gender and race/ethnicity group combinations.</p>
<p>Q.F.6. Where race/ethnicities and genders are not known for a sample of candidates assessed by the AEDT, evidence shall disclose its sample size.</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.G. Impact ratio</strong>: Impact ratios shall be disclosed for all disfavored groups, for all PCVs.</p>
<p>Q.G.1. Where an impact ratio for a disfavored group is below 0.8, evidence shall show justification for why the disfavored group is disadvantaged.</p>
<p>Q.G.2. Evidence shall show results of uncertainty analysis (e.g., standard error for the mean) or error propagation of impact ratios in the form of errors or error bars.</p>
<p>Q.G.3. Where PCV data was inferred, evidence shall show that systematic errors due to PCV inference were properly propagated in impact ratio calculations.</p>
<p>Q.G.4. Where a gender, race/ethnicity, or intersectional group was excluded from impact ratio calculation due to its size being below 2% of the total sample size of each analysis, evidence shall show</p>
<ol>
<li><p>justification for the exclusion of such group</p></li>
<li><p>the sample size of such group, and</p></li>
<li><p>the selection rate or scoring rate of such group</p></li>
</ol></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Non-intersectional, Gender, sorted by Impact ratio**

|        |              |                |              |
|--------|--------------|----------------|--------------|
|        | N applicants | Selection rate | Impact ratio |
| Male   | 3,732        | 0.798          | 1.000        |
| Female | 2,112        | 0.784          | 0.982        |

**Non-intersectional, Race/ethnicity, sorted by Impact ratio**

|                                   |              |                |              |
|-----------------------------------|--------------|----------------|--------------|
|                                   | N applicants | Selection rate | Impact ratio |
| Hispanic or Latino                | 1,127        | 0.860          | 1.000        |
| Asian                             | 1,184        | 0.835          | 0.971        |
| White                             | 1,797        | 0.774          | 0.900        |
| Black or African American         | 1,070        | 0.762          | 0.866        |
| Native American or Alaskan Native | 3            | 0.667          | N/A          |

**Intersectionals**

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p> </p></td>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p> </p></td>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p> </p></td>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p><strong>N applicants</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p><strong>Selection rate</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 121px; height: 22px; background-color: #6fa8dc"><p><strong>Impact ratio8</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 44px"><p>Hispanic or Latino</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>Male</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>790</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.857</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.995</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>Female</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>287</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.861</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>1.000</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 356px"><p><br />
<br />
<br />
<br />
<br />
<br />
<br />
Non- Hispanic or Latino</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 178px"><p><br />
<br />
<br />
Male</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>White</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>711</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.839</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.974</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>Asian</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>924</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.774</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.899</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 67px"><p>Black or African American</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
807</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
0.756</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
0.878</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 67px"><p>Native American or Alaskan Native</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
2</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
0.500</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
N/A</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 178px"><p><br />
<br />
<br />
Female</p></td>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>Asian</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>697</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.772</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.897</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 22px"><p>White</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>389</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.833</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 22px;"><p>0.967</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 67px"><p>Black or African American</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
807</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
0.756</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
0.878</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="height: 67px"><p>Native American or Alaskan Native</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
1</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
1.000</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; height: 67px;"><p><br />
N/A</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
<td data-colspan="1" data-rowspan="1"><p><br />
</p></td>
</tr>
</tbody>
</table>

 

**Note*:*** Data on these applicants was not included in the calculations above:

1.  123 applicants with an unknown gender category

2.  1053 applicants with an unknown race/ethnicity category, and

3.  1176 applicants with at least an unknown gender or an unknown race/ethnicity

7 N/A refers to the demographic group representing less than 2% of the total N applications in the table

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>Q.H. Statistical significance</strong>: Where the selection rate method was used, statistical significance calculation shall satisfy [UGESP](https://www.dol.gov/agencies/ofccp/faqs/employee-selection-procedures) guidelines.</p>
<p>Q.H.1. Evidence shall show that statistical significance was calculated using the Two Independent-Sample Binomial Z-Test for sample sizes of 30 or more, and using the Fisher’s Exact Test for sample sizes of fewer than 30.</p></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

### Governance

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.6413%; background-color: #6fa8dc"><p><strong>Audit Criteria</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 89.6447%; background-color: #6fa8dc"><p><strong>Opinion</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.6413%"><p><strong>G.A. Accountable party for disparate impact risks</strong>: The auditee shall have a party who is accountable for risks related to disparate impact.</p>
<ul>
<li><p>G.A.1. Evidence should show that the accountable party is a committee, but may also show that the accountable party is a single individual.</p></li>
<li><p>G.A.2. Evidence shall clearly show that risks related to disparate impact are owned and managed by the accountable party.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 89.6447%"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Accountable party**: Committee on Automated Decision Making Tools\
**Contact information**: [rohan.raman@hackerrank.com](mailto:rohan.raman@hackerrank.com)\
**Role in the auditee organization**: Governance group/committee

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>G.B. Defined duties of the accountable party</strong>: Duties of the party accountable for disparate impact risks shall be clearly defined.</p>
<ul>
<li><p>G.B.1. Evidence shall show that such duties pertain to the ownership, management, and monitoring of disparate impact risks.</p></li>
<li><p>G.B.2. Evidence shall show that the accountable party has influence over product changes per effective challenge in Federal Guidance on Model Risk Management.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>G.C. Documentation pertaining to duties carried out</strong>: The auditee shall provide evidence that the defined duties of the party accountable for disparate impact risks are carried out.</p>
<ul>
<li><p>G.C.1. Evidence shall show that the defined duties were carried out prior to the start date of this audit.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

### Risk Assessment

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.6413%; background-color: #6fa8dc"><p><strong>Audit Criteria</strong></p></td>
<td data-colspan="1" data-rowspan="1" style="width: 89.6447%; background-color: #6fa8dc"><p><strong>Opinion</strong></p></td>
</tr>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.6413%"><p><strong>R.A. Completion</strong>: The auditee shall have completed a risk assessment of the model.</p>
<ul>
<li><p>R.A.1. Evidence shall show that a risk assessment or an equivalent analysis was completed less than one year prior to the issuance date of this audit.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="width: 89.6447%"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

**Evidence of Risk Assessment completion**: Risk Assessment Documents (risk assessment spreadsheet and narrative notes), and verbal testimony from Risk Assessment participants.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>R.B. Identification of risks</strong>: Risk assessment shall show identification of relevant risks related to bias.</p>
<ul>
<li><p>R.B.1. Evidence shall show identification of risks related to various biases along all stages of the AI life cycle as listed in NIST Standard for Identifying and Managing Bias in Artificial Intelligence.</p></li>
<li><p>R.B.2. Evidence shall show awareness of the parties potentially affected by the decisions made along all stages of the AI life cycle.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-colspan="1" data-rowspan="1" style="width: 69.2825%"><p><strong>R.C. Evaluation of risks</strong>: Risk assessment shall demonstrate appropriate evaluation of relevant risks.</p>
<ul>
<li><p>R.C.1. Evidence shall show that the identified risks are assessed from the perspectives of multiple affected external and internal stakeholders, with justifications for the extent of and mechanism by which such risks affect these stakeholders.</p></li>
<li><p>R.C.2. Evidence shall show that the identified risks are assessed in a sufficiently rigorous manner, using a quantitative and/or qualitative evaluation scheme, and along multiple dimensions, such as but not limited to likelihood of harm and severity of harm.</p></li>
<li><p>R.C.3. Evidence shall show justification for the provided evaluation of risks.</p></li>
</ul></td>
<td data-colspan="1" data-rowspan="1" style="text-align: center; width: 90.0035%; vertical-align: middle;"><p><strong>PASS</strong></p></td>
</tr>
</tbody>
</table>

## Appendix

## Audit Methodology

### The Process Audit

The BABL AI audit framework is the Process Audit, defined as “an impartial verification and evaluation process conducted by an independent auditor to determine whether sufficient evidence exists to warrant the judgment that AI risks have been prevented, detected, mitigated, or otherwise managed.” A process audit is modeled after the financial auditing practice as a cooperative third-party audit, and is distinguished from other commonly used forms of assessment of algorithms, such as first- or second-party assessments, and assurance.8 The audit framework contains three phases:

1.  **Scoping** – The auditor conducts a preliminary survey of the auditee’s algorithm to gain a full understanding to contextualize documentary evidence

2.  **Evaluation & Verification** – The auditee submits documentation containing evidence demonstrating satisfaction of the audit criteria which the auditors evaluate and verify.

3.  **Certification** – If the auditee is determined to pass the audit criteria, the auditor drafts the auditor’s report and certifies the auditee’s algorithm.

### Evaluation & Verification

The procedure for all BABL AI auditors in conducting a process audit follows the guidelines set forth in the Public Company Accounting Oversight Board (PCAOB)’s Auditing Standard 1105 on Audit Evidence, where applicable. Specifically, the auditors:

1.  **Obtain audit claims and statements** from the auditee’s submitted documentation which either support or contradict the criteria and sub-criteria,

2.  **Evaluate the claims and statements** in regard to satisfying the criteria and sub-criteria, based on the sufficiency and appropriateness of the evidence, and

3.  **Verify that the claims and statements** made by the auditee are free from material misstatement, whether due to fraud or error.9

8 Carrier, R., & Brown, S. (2021). Taxonomy: AI Audit, Assurance & Assessment. ForHumanity.

[https://forhumanity.center/blog/taxonomy-ai-audit-assurance-assessment/](https://forhumanity.center/blog/taxonomy-ai-audit-assurance-assessment/)

9 “Reasonable assurance” is a high level of assurance but is not a guarantee that an audit conducted in accordance with good auditing practice always detects a material misstatement when it exists. Misstatements can arise from fraud or error and are considered material if, individually or in aggregate, they could reasonably be expected to influence the decisions of stakeholders taken based on these statements.

In addition, evaluation and verification of claims and statements may involve requesting additional supporting documentary evidence, and/or interviewing those responsible for the governance of the algorithm, other relevant employees of the auditee organization, or other third parties referenced in the submitted documentation.

At the end, the auditors reach an audit opinion based on:

1.  The sufficiency and appropriateness of the audit evidence, and

2.  The risk of material misstatement of the audit evidence.

## Terminologies & Definitions

|  |  |  |
|----|----|----|
| **Term** | **Abbrev** | **Definition** |
| automated employment decision tool | AEDT | “any computational process, derived from machine learning, statistical modeling, data analytics, or artificial intelligence, that issues simplified output, including a score, classification, or recommendation, that is used to substantially assist or replace discretionary decision making for making employment decisions that impact natural persons.” – see § 20-870 of the Code and § 5-300 of the adopted rule for full definition |
| disfavored group |   | any gender or race/ethnicity group not having the highest selection rate or average score |
| disparate impact or adverse impact |   | “a selection rate for any race, sex, or ethnic group which is less than four-fifths (⁄) (or 80%) of the rate for the group with the highest rate will generally be regarded by the Federal enforcement agencies as evidence of adverse impact” – see § 60-3.4.D of UGESP (1978) for full definition |
| error propagation |   | calculation or computation of a variable's uncertainty that is dependent on another variable’s uncertainty |
| favored group |   | the gender or race/ethnicity group having the higher selection rate or average score compared to the other groups |
| impact ratio |   | “either (1) the selection rate for a category divided by the selection rate of the most selected category or (2) the scoring rate for a category divided by the scoring rate for the highest scoring category. ” – see § 5-300 of the [adopted rule](https://rules.cityofnewyork.us/wp-content/uploads/2023/04/DCWP-NOA-for-Use-of-Automated-Employment-Decisionmaking-Tools-2.pdf) for full definition |
| scoring rate |   | “the rate at which individuals in a category receive a score above the sample’s median score, where the score has been calculated by an AEDT” |
| justification |   | a compelling reason that illuminates the issue and carries normative force, as opposed to solely explanatory power |
| positive outcome |   | the basis for selection rate, the favorable outcome for a candidate from the use of the model, such as being selected to move forward in the hiring process or assigned a classification by an model |
| protected category variables | PCV | defined per jurisdiction, equivalent to protected class, including but not limited to: race/ethnicity, age, gender, religion, ability or disability, sexual orientation, color, nation of origin, socioeconomic class |
| risk assessment |   | an assessment of the risk that the use of the algorithm negatively impacts the rights and interests of stakeholders, with a corresponding identification of situations of the context and/or features of the algorithm which give rise or contribute to these negative impacts9 |
| selection rate |   | “the rate at which individuals in a category are either selected to move forward in the hiring process or assigned a classification by an AEDT” – see § 5-300 of the adopted rule for full definition |
| testing dataset |   | the dataset used to test for or quantify disparate impact |
| uncertainty analysis |   | calculation or computation to quantify the uncertainty of a variable, outputting errors or error bars |

10 Hasan, A., Brown, S., Davidovic, J., Lange, B., & Regan, M. (2022). Algorithmic Bias and Risk Assessments: Lessons from Practice. Digital Society, 1(1). https://doi.org/10.1007/s44206-022-00017-z
