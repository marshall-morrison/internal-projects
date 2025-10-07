# Raw LLM Analysis:  Onebrief Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:13:44

---

## Chunk 1:  Onebrief Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:13:44

### Original Content
```
Merchant Scoping start date: May 22, 2025 MSA Signature Date: May 29, 2025 Onboarding Kick Off Date: Apr 17, 2025 [If Exists] Opt Out Date: none Go Live Date: N a GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Head of Finance   DRI: Nadav Yuhjtman Senior Accountant: Leslie Romer Accounting Firm: Countsy (outsourced, transitioning out) Main Point of Contact for Tabs: Nadav Customer Success Target: Streamlined AR, improved audit readiness, single source of truth for fina...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant onboarding timeline and key dates",
    "Stakeholder identification and organizational structure",
    "Business model and customer profile (government SaaS contractor)",
    "Implementation goals and pain points (automation, scalability, audit readiness)",
    "Billing complexity and contract management (third-party government contracts)"
  ],
  "rules": [
    "MSA Signature Date must be captured during merchant scoping",
    "Key stakeholders must be identified: Head of Finance, Senior Accountant, Main Point of Contact",
    "Implementation requires identification of ERP and Tax Integration systems",
    "AE and Implementation team must document merchant goals and pain points",
    "Billing model documentation must include customer creation process details",
    "Contract paper ownership must be identified (third-party vs merchant paper)",
    "Company summary must explain what the company does and their business model",
    "Customer Success Target must be defined during scoping"
  ],
  "exceptions": [
    "Opt Out Date can be 'none' if not applicable",
    "Go Live Date may be 'N/a' if not yet determined",
    "Accounting may be outsourced initially and transition to in-house",
    "Government contractors may bill through intermediary prime contractors rather than end customers directly",
    "Contracts may be on third-party paper (government primes) rather than merchant's own contract templates"
  ],
  "merchant_specific": [
    "Specific date values (May 22, 2025, May 29, 2025, Apr 17, 2025)",
    "Named individuals (Nadav Yuhjtman, Leslie Romer)",
    "Accounting firm name (Countsy)",
    "ERP system selection (context suggests NetSuite)",
    "Industry-specific terminology (government primes, CENTCOM, subcontracting relationships)",
    "Specific pain points (replacing NetSuite revenue module, government billing complexities)",
    "Customer Success Target definition (Streamlined AR, improved audit readiness, single source of truth)",
    "Business vertical (government-focused SaaS)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2:  Onebrief Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:13:53

### Original Content
```
, HII), not the end government customer (e g , CENTCOM) How contract is broken up Each is different and on government paper Contract Processing Steps (Implementation Success to fill) Steps to process Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Bill...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow",
    "Default Operational Parameters",
    "Billing and Invoice Management",
    "Integration Item Classification",
    "Stakeholder Communication Protocols"
  ],
  "rules": [
    {
      "rule": "Bill the prime contractor, not the end government customer",
      "category": "Billing",
      "specificity": "merchant-specific"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Contract Defaults",
      "specificity": "operational-default"
    },
    {
      "rule": "Default Net Payment Terms is 0 if none specified",
      "category": "Contract Defaults",
      "specificity": "operational-default"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Contract Defaults",
      "specificity": "operational-default"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "specificity": "operational-default"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Classification",
      "specificity": "integration-specific"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Classification",
      "specificity": "integration-specific"
    },
    {
      "rule": "Ops Team must notify designated stakeholders upon completion of processing batches",
      "category": "Communication",
      "specificity": "process-requirement"
    },
    {
      "rule": "International Team should ignore Notes Sections",
      "category": "Team Responsibilities",
      "specificity": "team-specific"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice date may be back-dated to final day of month per merchant request",
      "condition": "Merchant-specific processing requirements",
      "applies_to": "Invoice Processing"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "condition": "Merchant override",
      "applies_to": "Integration Classification"
    },
    {
      "exception": "Default parameters can be overridden by contract-specific instructions",
      "condition": "Contract specifications present",
      "applies_to": "All Default Settings"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements",
      "applies_to": "Invoice Generation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model",
      "description": "Primarily annual SaaS with occasional one-off professional services",
      "customizable": true
    },
    {
      "element": "Customer type",
      "description": "Bills prime contractors (e.g., HII) rather than end government customers (e.g., CENTCOM)",
      "customizable": true
    },
    {
      "element": "Invoice date processing",
      "description": "May require back-dating to final day of month",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Specific rules for Statsig and Pinata integrations",
      "customizable": true
    },
    {
      "element": "Post-processing notifications",
      "description": "Specific stakeholders (e.g., Customer Success - Azmat Aziz) need notification in merchant channels",
      "customizable": true
    },
    {
      "element": "Customer-specific invoice requirements",
      "description": "Special memos and invoice changes based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "description": "Mosaic integration noted as nice-to-have",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Rationale**: The document appears to be a template or form with some filled sections and some placeholder text. The repetitive content and incomplete sentences suggest this is a working document. Confidence is reduced due to: (1) fragmented text structure, (2) unclear context for some abbreviations (BT, AE), (3) mixed completed and template sections, and (4) potential OCR or formatting issues. However, the core operational rules and structure are clear enough to extract meaningful patterns.

---

## Chunk 3:  Onebrief Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:13:53

### Original Content
```
g , CENTCOM) Contracts are on third-party paper (usually government primes) Internal preference to report by end-customer entity Is there any important merchant relationship information 1) What is the merchant temperament Onebrief's temperament is collaborative and eager to move quickly They see Tabs as a strategic partner to help modernize and automate their financial operations, especially as they transition away from outsourced accounting and prepare for growth 2) What are the Tabs features t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Government contracting and third-party paper management",
    "Financial operations modernization and automation",
    "Revenue recognition automation for complex contracts",
    "Merchant relationship management and strategic partnership",
    "Transition from outsourced to in-house accounting operations"
  ],
  "rules": [
    "Contracts are executed on third-party paper, typically government primes",
    "Internal reporting preference is by end-customer entity rather than contracting entity",
    "Revenue recognition must be automated to eliminate manual work",
    "Contract ingestion should utilize AI to handle complex government contracts",
    "Invoicing and collections must be integrated and centralized for AR management",
    "Billing workflows must accommodate government-specific requirements",
    "NetSuite's revenue module should be avoided in favor of automated alternatives"
  ],
  "exceptions": [
    "Contracts may be on government prime paper rather than direct merchant paper",
    "Reporting structure differs from standard practice - focuses on end-customer entity despite third-party contracting arrangements",
    "Special handling required for government and third-party contracts due to complexity"
  ],
  "merchant_specific": [
    "Merchant name: Onebrief",
    "Merchant operates in government/defense sector (indicated by CENTCOM reference)",
    "Merchant temperament: collaborative and eager to move quickly",
    "Merchant is transitioning away from outsourced accounting",
    "Merchant is preparing for growth phase",
    "Merchant views Tabs as a strategic partner for financial modernization",
    "Key POC priorities: automated revenue recognition, AI contract ingestion, integrated invoicing/collections",
    "Merchant has complex government contracting arrangements requiring specialized handling"
  ],
  "confidence_score": 0.92
}
```

---

