# Data Folder Structure Analysis

## Overview
The `/data` folder contains three main knowledge bases and support documentation:
1. **Claude** - Help Center documentation
2. **HackerRank** - Platform Knowledge Base
3. **Visa** - Support Documentation

---

## 1. Claude Data Structure

**Location:** `/data/claude/`  
**Total Articles:** 321 exported articles  
**Purpose:** Claude Help Center documentation covering features, API usage, deployment options, and support

### Main Categories & Organization:

```
claude/
├── index.md                                    (Category listing)
├── amazon-bedrock/                             (6 articles)
│   └── Q&A format articles on AWS integration
│
├── claude/                                     (12 articles)
│   └── Release notes and general information
│
├── claude-api-and-console/                     (Product Features)
│   ├── api-faq/
│   ├── api-prompt-design/
│   ├── claude-api-usage-and-best-practices/
│   ├── pricing-and-billing/
│   ├── troubleshooting/
│   └── using-the-claude-api-and-console/
│
├── claude-code/                                (Tool-specific)
│   └── Multi-articles on Claude Code usage
│
├── claude-desktop/                             (Desktop Application)
├── claude-for-education/                       (Use Case)
├── claude-for-government/                      (Use Case)
├── claude-for-nonprofits/                      (Use Case)
├── claude-in-chrome/                           (Integration)
├── claude-mobile-apps/                         (Mobile)
├── connectors/                                 (Integration Points)
├── identity-management-sso-jit-scim/          (Authentication)
├── privacy-and-legal/                          (Compliance)
├── pro-and-max-plans/                          (Pricing Tiers)
├── safeguards/                                 (Security)
└── team-and-enterprise-plans/                  (Enterprise)
```

### File Naming Convention:
- Format: `{ARTICLE_ID}-{question-in-slug-format}.md`
- Example: `7996918-what-is-amazon-bedrock.md`
- Each file contains complete help article content

### Key Characteristics:
- Q&A/Help article format
- Comprehensive coverage of Claude features and deployment
- Organized by feature, product, and use case
- Hierarchical folder structure by topic

---

## 2. HackerRank Data Structure

**Location:** `/data/hackerrank/`  
**Total Articles:** 394 exported articles  
**Purpose:** Platform knowledge base for HackerRank products and features

### Main Categories & Organization:

```
hackerrank/
├── index.md                                    (Category listing)
├── chakra/                                     (Product: Chakra)
│   ├── getting-started/
│   ├── integrations/
│   └── manage-chakra/
│
├── engage/                                     (Product: Engage)
│   └── Multiple sub-topics
│
├── general-help/                               (General Support)
│   └── Common questions and troubleshooting
│
├── hackerrank_community/                       (Community Features)
├── integrations/                               (Integration Hub)
├── interviews/                                 (Interview Features)
├── library/                                    (Content Library)
├── screen/                                     (Assessment Feature)
├── settings/                                   (Platform Settings)
├── skillup/                                    (Learning Feature)
└── uncategorized/                              (Other Articles)
```

### File Naming Convention:
- Format: `{ARTICLE_ID}-{topic-in-slug-format}.md`
- Example: `1231590424-assessing-candidates-on-prompt-engineering-skills.md`
- Unique article IDs for tracking

### Key Characteristics:
- Product-centric organization
- Covers recruitment, assessment, and learning products
- Multiple products within the platform
- Organized by feature and use case

---

## 3. Visa Data Structure

**Location:** `/data/visa/`  
**Total Articles:** Not quantified (smaller dataset)  
**Purpose:** Visa payment solutions support documentation

### Organization:

```
visa/
├── index.md                                    (Main index)
├── support.md                                  (Consumer support overview)
└── support/
    ├── consumer/
    │   ├── data-security.md
    │   └── Other consumer-specific docs
    ├── merchant/
    │   └── Merchant-specific documentation
    └── small-business/
        └── Business-focused support
```

### Segment Organization:
1. **Consumer** - End-user payment documentation
2. **Merchant** - Business merchant support
3. **Small Business** - SMB-specific guidance

### Key Characteristics:
- Segment-based organization (Consumer, Merchant, Small Business)
- Direct support documentation
- Flatter structure compared to Claude/HackerRank
- Focus on payment solutions and security

---

## Data Statistics Summary

| Platform | Total Articles | Organization Type | Structure |
|----------|----------------|-------------------|-----------|
| Claude | 321 | Feature/Use-Case based | Hierarchical (14+ categories) |
| HackerRank | 394 | Product-based | Hierarchical (11+ categories) |
| Visa | Small | Segment-based | Flat (3 segments) |

---

## Common Data Patterns

### 1. **File Format**
- All content in markdown (`.md`) format
- Each article is a standalone file
- Index files organize links to articles

### 2. **Naming Convention**
- `{unique-id}-{slug-title}.md`
- IDs enable tracking and deduplication
- Slug format for readability

### 3. **Hierarchy**
- **Claude:** Topic → Sub-topic → Articles
- **HackerRank:** Product → Feature → Articles
- **Visa:** Segment → Category → Articles

### 4. **Index Files**
- Each root folder has `index.md`
- Lists all main categories
- Provides entry points to documentation

---

## Usage Recommendations for Code Processing

1. **Data Loading:** Process by platform (Claude, HackerRank, Visa)
2. **Article Identification:** Use unique IDs from filenames
3. **Category Mapping:** Use folder structure as primary taxonomy
4. **Segment Handling:** 
   - Claude: By feature/product
   - HackerRank: By product line
   - Visa: By customer segment
5. **Indexing:** Leverage index.md files for catalog structure

---

## Notes

- Data appears to be exported from help centers/knowledge bases (timestamp indicated in index files)
- Article IDs likely reference original knowledge base system IDs
- Structure supports multi-tenant knowledge management
- Scalable organization for adding new categories/products
