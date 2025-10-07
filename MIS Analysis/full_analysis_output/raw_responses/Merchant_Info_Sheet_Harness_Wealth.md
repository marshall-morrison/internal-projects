# Raw LLM Analysis: Merchant Info Sheet - Harness Wealth

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:30:29

---

## Chunk 1: Merchant Info Sheet - Harness Wealth_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:29

### Original Content
```
N A Information on how merchant bills Subscription   Usage How contract is broken up N A One off things to know about the merchant They have  40 clients today and doing  1 5M in ARR Contract Processing Steps (Implementation Success to fill) General In contracts - important information is in Section 3 - Revenue Share Regardless of billing cadence, core charge should be called  Annual Platform Fee  For ALL Flat Price billing terms, the quantity will be 1 Assume straight-line billing across all per...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Customer Data Management and Integration",
    "Revenue Recognition and Fee Structure",
    "Communication and Notification Protocols",
    "Platform Fee and Subscription Billing"
  ],
  "rules": [
    "Important contract information is located in Section 3 - Revenue Share",
    "Core charge must be called 'Annual Platform Fee' regardless of billing cadence",
    "For ALL Flat Price billing terms, quantity must be set to 1",
    "Apply straight-line billing across all periods by default",
    "Discounts must be recorded as a separate line item",
    "Only charge for platform fees in Tabs",
    "All customers must come directly from QBO with accurate billing address and email",
    "Service Start Date must use Effective Date from top paragraph of contract",
    "Billing Start Date must be same as Service Start Date",
    "Ignore all sections outside of Effective Date and Section 3 - Revenue Share",
    "Within Section 3, only process BTs for Platform Fee and Additional Taxpayers",
    "Ignore anything pertaining to retained revenue share",
    "Default Service Term is 1 Year",
    "Default Net Payment Terms is 30 days",
    "Default Billing Frequency is stated in section 3a under Revenue Share",
    "Everything maps to Platform Fee Harness Integration Items",
    "Notify Jeff in harness during Implementation phase upon completion of processing batches"
  ],
  "exceptions": [
    "If contract displays different rate for one period, adjust appropriately using discount",
    "See Alpha Financial for example of flat price billing",
    "See JBO for example on additional Taxpayers BTs",
    "CSV Instructions should be ignored for Processing in Garage",
    "Events in contract should be ignored",
    "Rev Share feature (20% of invoice for leads) is requested but NOT URGENT and currently not supported"
  ],
  "merchant_specific": [
    "Merchant name: Harness",
    "Current client base: 40 clients with $1.5M ARR",
    "Billing cadence is merchant-specific and stated in Section 3a",
    "Revenue share model: Takes 20% of invoice for leads generated through platform (not currently implemented)",
    "Integration source: QBO (QuickBooks Online)",
    "Key contact: Jeff (for implementation notifications)",
    "Specific contract sections to focus on: Section 3 - Revenue Share",
    "Product naming: 'Annual Platform Fee' and 'Additional Taxpayers'",
    "Referenced example customers: Alpha Financial, JBO",
    "Historical calls recorded from November 2024 (intro, rev share scoping, proposal sync, sandbox walkthrough)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Harness Wealth_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:32

### Original Content
```
Merchant Demo date: Nov 11, 2024 Scoping start date: Nov 12, 2024 MSA Signature Date: Nov 25, 2024 Onboarding Kick Off Date: Dec 3, 2024 [If Exists] Opt Out Date: Oct Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Head of Finance and Operations: Serg Zhelezniak - https: www linkedin com in sergzhelezniak  Jake Wright - Director of Accounting and Operations Billing POC Etc Company summary (AE to fill) Harness Wealth is the next generation wealt...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Goals and Pain Points",
    "Stakeholder Identification and Roles",
    "Integration and Technical Requirements",
    "Contractual Terms and Opt-Out Provisions"
  ],
  "rules": [
    {
      "rule": "Standard implementation timeline follows sequence: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "confidence": "high"
    },
    {
      "rule": "Implementation POC and GTM POC must be identified for each merchant",
      "type": "requirement",
      "confidence": "high"
    },
    {
      "rule": "Key stakeholders must include Head of Finance and Operations and Billing POC",
      "type": "requirement",
      "confidence": "high"
    },
    {
      "rule": "ERP and Tax Integration systems must be documented during onboarding",
      "type": "requirement",
      "confidence": "high"
    },
    {
      "rule": "Merchant goals and pain points must be documented by AE and Implementation team",
      "type": "process",
      "confidence": "high"
    },
    {
      "rule": "Opt-out clause existence and conditions must be documented",
      "type": "contractual",
      "confidence": "high"
    },
    {
      "rule": "Company summary must be provided by Account Executive (AE)",
      "type": "responsibility",
      "confidence": "high"
    },
    {
      "rule": "Billing model and customer creation process uniqueness must be assessed",
      "type": "requirement",
      "confidence": "medium"
    }
  ],
  "exceptions": [
    {
      "exception": "Revenue recognition component was explicitly excluded from scope to lock in partnership",
      "context": "Despite being a software business (typical use case), rev rec was intentionally not included",
      "confidence": "high"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "context": "Opt-out provisions may vary by merchant; this merchant has none",
      "confidence": "high"
    },
    {
      "exception": "Opt Out Date field shows 'Oct' without year or specific date",
      "context": "Incomplete data entry or placeholder value",
      "confidence": "medium"
    }
  ],
  "merchant_specific": [
    {
      "element": "Timeline dates",
      "customization_needed": "All milestone dates are merchant-specific",
      "examples": ["Demo: Nov 11, 2024", "Go Live: Jan 1, 2025"]
    },
    {
      "element": "Key personnel",
      "customization_needed": "Names, titles, and contact information vary per merchant",
      "examples": ["Serg Zhelezniak - Head of Finance", "Jake Wright - Director of Accounting"]
    },
    {
      "element": "Business model and industry",
      "customization_needed": "Merchant operates in wealth management for builders/founders",
      "examples": ["Wealth management solution", "Software business"]
    },
    {
      "element": "Pain points and goals",
      "customization_needed": "Specific to merchant's operational challenges",
      "examples": ["Automating revenue workflows without increasing headcount"]
    },
    {
      "element": "Scope decisions",
      "customization_needed": "Features included/excluded vary by merchant needs",
      "examples": ["Rev rec component excluded"]
    },
    {
      "element": "Integration systems",
      "customization_needed": "ERP and Tax Integration systems are merchant-specific",
      "examples": ["Fields present but not populated in this document"]
    },
    {
      "element": "Contractual terms",
      "customization_needed": "Opt-out clauses and conditions vary by merchant",
      "examples": ["No opt-out clause for this merchant"]
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Harness Wealth_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:41

### Original Content
```
rewatch com video cvk6eupblhmru4to-harness-sandbox-walkthrough-november-21-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Software Subscription   Usage Fees for   of users Generally Quarterly or Annual Is there any important merchant relationship information 1) What is the merchant temperament Serg is very easy to work with and sees the vision Personal relationship with Rebecca - brought us in as his first buy as a new hire 2) Is there a key POC: (i e : who i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship management and stakeholder engagement",
    "Software subscription billing models and payment structures",
    "Product feature prioritization and customer needs assessment",
    "Implementation team coordination and role delineation"
  ],
  "rules": [
    "Ops International Team should ignore sections marked with [Ops International Team to Ignore]",
    "Implementation team (AE Implementation) is responsible for filling in specific merchant details",
    "Software subscription information must be documented including usage fees and user counts",
    "Payment frequency should be specified as either Quarterly or Annual",
    "Three key merchant relationship questions must be answered: (1) merchant temperament, (2) key POC identification, (3) features the POC cares about",
    "Merchant temperament assessment should be documented for relationship management",
    "Decision maker/buyer must be clearly identified",
    "Specific Tabs features relevant to the merchant must be documented"
  ],
  "exceptions": [
    "Certain document sections are explicitly marked for specific teams to ignore (Ops International Team exclusion)",
    "Personal relationships between merchant contacts and company representatives should be noted when relevant to the business relationship"
  ],
  "merchant_specific": [
    "Merchant temperament varies by client (e.g., 'easy to work with', 'sees the vision')",
    "Key POC/decision maker name (in this case: Serg)",
    "Personal relationship history and context (e.g., Rebecca's relationship, first buy as new hire)",
    "Specific feature priorities vary by merchant (Contract Management, automated invoicing, Rev Rec, Renewals management)",
    "Payment structure (Quarterly vs Annual) is merchant-dependent",
    "Number of users and usage fees are merchant-specific",
    "Video walkthrough references are unique per merchant implementation"
  ],
  "confidence_score": 0.85
}
```

---

