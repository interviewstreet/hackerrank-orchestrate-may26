---
title: "Public Sector FAQs"
title_slug: "public-sector-faqs"
source_url: "https://support.claude.com/en/articles/13756069-public-sector-faqs"
last_updated_iso: "2026-03-25T16:05:41Z"
article_id: "15900816"
breadcrumbs:
  - "Claude"
  - "Account management"
---

# Public Sector FAQs

_Last updated: 2026-03-25T16:05:41Z_

## 1. Products and features

#### What products are available to Public Sector customers?

Select your product based on both your technical/functional requirements, and also your compliance/security/deployment environment requirements. Here is a list of options:

![Embedded media](https://downloads.intercomcdn.com/i/o/lupk8zyo/2197717161/79965a24090029e9e58c727c3c24/pubsec-product-matrix_png+%281%29.jpg?expires=1776784500&signature=70e721771c8773debffe930bbae582c1923407328093298a41f17ff77e5ac556&req=diEuEc5%2FmoBZWPMW1HO4zU94IV8iFdk12WxtU42UVC3whVLG1s8q1dXkaNvS%0AjuP%2Fe1L6qJF9UBDMum4%3D%0A)

#### What is Claude for Government (C4G)?

Claude for Government is Anthropic's FedRAMP-High authorized product, which is available to both government customers and contractors.

Learn more here: **[Offering expanded Claude access across all three branches of the U.S. government](https://www.anthropic.com/news/offering-expanded-claude-access-across-all-three-branches-of-government)**

#### How do I access Claude for Government?

Submit a request here: **[Contact Sales](https://claude.com/contact-sales)**

#### What is the difference between Claude Enterprise and Claude for Government?

Claude Enterprise (CE) has robust enterprise-level security features that meet many standards of highly regulated industry and is appropriate for the majority of State and Local government uses. Claude for Government (C4G) is our standalone application that is FedRAMP-High authorized. C4G does not yet include Claude Code or Cowork (though they are on the roadmap to be released this year).

#### Does Claude for Government include Claude Code?

Not yet; though it’s coming this year. Until then, customers can use Claude Code through Bedrock or Vertex if they need a FedRAMP authorized environment.

#### Can I use Claude API in government environments?

Yes. Claude API is available via Amazon Bedrock (in AWS GovCloud - FedRAMP High, and in IL5+) and Google Vertex with Assured Workloads (FedRAMP-High).

For more information, see our **[Claude Code product page](https://claude.com/product/claude-code)**.

#### What models are available in Claude for Government?

Our Claude for Government application is updated with our latest commercial model releases.

---

## 2. FedRAMP, Impact Levels, and compliance

#### What types of data can be used in Claude?

CUl and FIPS 199 High Impact data are authorized in Claude for Government, which is FedRAMP High authorized. Additionally, per our third-party NIST attestation, Claude Enterprise meets compliance requirements for CUl as well. The third-party NIST attestation is available under NDA here: **[[Anthropic] 2026 NIST 800-171r3 Attestation Letter](https://trust.anthropic.com/resources?s=zfucqt7j6yandbrsvlk2&name=[anthropic]-2026-nist-800-171-r-3-attestation-letter)**

ITAR data can only be processed in Claude via AWS Bedrock, which is IL5 accredited.

For most other government agencies like State and Local handling PHI or PII:, Anthropic offers a HIPAA-ready configuration for Enterprise and API customers, including the ability to sign a Business Associate Agreement (BAA). A couple of key points:

- The BAA is available for Enterprise plans and direct API customers—not consumer (Free, Pro, Max) or Team plans.
- It requires a Zero Data Retention (ZDR) agreement, meaning Anthropic does not store your inputs or outputs.
- Certain features/integrations have limitations under the BAA (e.g., web search is excluded).

You can learn more here:

- BAA details: **[Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)**
- Certifications overview (HIPAA, SOC 2, ISO 27001): **[What Certifications has Anthropic obtained?](https://support.claude.com/en/articles/10015870-what-certifications-has-anthropic-obtained)**
- **[Trust Portal](https://trust.anthropic.com)**

#### What is Claude's FedRAMP authorization level?

Claude for Government (C4G), and Claude via Amazon Bedrock in AWS GovCloud and Google Vertex with Assured Workloads are all FedRAMP-High.

Learn more here: **[Claude in Amazon Bedrock: Approved for use in FedRAMP High and DoD IL4/5 workloads](https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high)**

#### Are Claude's models themselves FedRAMP authorized?

FedRAMP and DoD Impact Levels are certifications for cloud services (IaaS, PaaS, SaaS). AI models are software components, not cloud services. Claude models deploy within authorized environments, and customers maintain their compliance posture through the hosting platform.

#### How can I get access to your FedRAMP authorization information and other associated documentation?

Please submit a request for the package directly to FedRAMP using this **[FedRAMP Package Access Request Form](https://www.fedramp.gov/resources/documents/Agency_Package_Request_Form.pdf)**.

#### Can I use Claude for CUI (Controlled Unclassified Information)?

Yes. Claude Enterprise has received a third-party NIST attestation for use of CUI data. Alternatively, CUI data can be processed in a FedRAMP High environment via Claude for Government, Bedrock, or Vertex. The third-party NIST attestation is available under NDA here: **[[Anthropic] 2026 NIST 800-171r3 Attestation Letter](https://trust.anthropic.com/resources?s=zfucqt7j6yandbrsvlk2&name=[anthropic]-2026-nist-800-171-r-3-attestation-letter)**

#### Can I use Claude in IL6/Secret environments?

Yes. Claude is available in the AWS Secret region (IL6) via Amazon Bedrock.

#### If a customer purchases Claude Enterprise via AWS Marketplace, is that FedRAMP?

No. At present, our only product offering on AWS Marketplace is Claude Enterprise which is not FedRAMP authorized. Customers requiring FedRAMP compliance must use Claude for Government (C4G) or access Claude models through FedRAMP-authorized CSPs (Bedrock GovCloud or Vertex Assured Workloads).

Learn more here: **[Claude in Amazon Bedrock: Approved for use in FedRAMP High and DoD IL4/5 workloads](https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high)**

---

## 3. Cloud service providers and deployment

#### How do I deploy Claude in Amazon Bedrock on AWS GovCloud / GCP Vertex in Assured Workloads?

Work with your AWS / GCP account teams. Claude is available as a managed service through Bedrock/Vertex. These links can help to get you started:

- **[Access Amazon Bedrock foundation models in AWS GovCloud (US)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html#model-access-govcloud)**
- **[Claude on Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)**

#### What is the pricing and commitment information for Claude on Vertex/Bedrock?

Contact AWS directly for pricing and commitment requirements. Usage is typically pay-per-token through standard Bedrock pricing.

Learn more here: **[Claude in Amazon Bedrock: Approved for use in FedRAMP High and DoD IL4/5 workloads](https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high)**

**AWS Bedrock: [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)**

**Google Cloud Vertex AI:** **[Cost of building and deploying AI models in Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/pricing)**

---

## 4. Pricing and procurement

#### What is the $1/month government offer and who qualifies?

The $1/month offer is specifically for federal, judicial, and legislative agencies for C4G only. It does not extend to defense contractors, FFRDCs, or state/local governments, which receive standard pricing.

#### Can we purchase directly from Anthropic or only through Carahsoft?

Both options are available. Anthropic can sell directly, and/or resell / distribute via Carahsoft to specific government customers.

#### How much does Claude cost?

C4G is $60/seat/month with usage limits and no additional consumption charges.

Claude Enterprise is $20/seat/month with additional charges for token consumption (PAYG).

Other pricing plans are available here: **[Team and Enterprise plan pricing](https://claude.com/pricing#team-&-enterprise)**

Learn more here: **[Offering expanded Claude access across all three branches of the U.S. government](https://www.anthropic.com/news/offering-expanded-claude-access-across-all-three-branches-of-government)**

## Related Articles
- [What is Amazon Bedrock?](https://support.claude.com/en/articles/7996918-what-is-amazon-bedrock)
- [Claude Code FAQ](https://support.claude.com/en/articles/12386420-claude-code-faq)
- [Use Claude for Excel, PowerPoint, and Word with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-excel-powerpoint-and-word-with-third-party-platforms)
- [Get started with Claude for Government](https://support.claude.com/en/articles/14503590-get-started-with-claude-for-government)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
