# Raw LLM Analysis: [EXTERNAL USE] Merchant Info Sheet - Harness Wealth

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 09:51:24

---

## Chunk 1: [EXTERNAL USE] Merchant Info Sheet - Harness Wealth_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:51:24

### Original Content
```
N A Information on how merchant bills Subscription   Usage How contract is broken up N A One off things to know about the merchant They have  40 clients today and doing  1 5M in ARR Contract Processing Steps (Implementation Success to fill) Steps to process All customers coming directly from QBO and should have billing address and email accurately populated Use Effective Date from top paragraph of contract In contracts - important information is in Section 3 - Revenue Share Regardless of billing...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Data Extraction",
    "Billing Configuration and Revenue Recognition",
    "Integration and Product Mapping",
    "Stakeholder Communication and Notifications",
    "Revenue Share Management"
  ],
  "rules": [
    "All customers must come directly from QBO with billing address and email accurately populated",
    "Use Effective Date from top paragraph of contract",
    "Section 3 (Revenue Share) contains the most important contract information",
    "Core charge must always be called 'Annual Platform Fee' regardless of billing cadence",
    "For ALL Flat Price billing terms, quantity must be set to 1",
    "Assume straight-line billing across all periods",
    "Only charge for platform fees in Tabs (not revenue share)",
    "CSV Frequency setting: 1 every 1 none",
    "CSV Quantity setting: 1",
    "Flat Billing Recurring field: No",
    "Ignore all contract sections outside of Effective Date and Section 3 - Revenue Share",
    "Ignore anything pertaining to retained revenue share",
    "Within Section 3, only create billing terms for Platform Fee and Additional Taxpayers",
    "Default Service Term: 1 Year",
    "Default Net Payment Terms: 30 days",
    "Default Billing Frequency: Stated in section 3a under Revenue Share",
    "All integration items map to Platform Fee Harness",
    "Notify Jeff in harness during Implementation phase upon completion of processing batches"
  ],
  "exceptions": [
    "If contract displays different rate for one period, adjust appropriately using discount (deviation from straight-line billing)",
    "Additional Taxpayers billing terms are an exception to standard platform fee processing (see JBO for example)",
    "Revenue share feature (20% of invoice for leads) is requested but NOT URGENT and currently not supported by the platform"
  ],
  "merchant_specific": [
    "Merchant name: Harness",
    "Current client base: 40 clients",
    "Annual Recurring Revenue (ARR): $1.5M",
    "Revenue model includes 20% revenue share from advisor leads (not currently processed in Tabs)",
    "Reference customers: Alpha Financial (example), JBO (Additional Taxpayers example)",
    "Key stakeholder: Jeff (to be notified during Implementation)",
    "Integration source: QuickBooks Online (QBO)",
    "Product terminology: 'Annual Platform Fee', 'Additional Taxpayers', 'Platform Fee Harness'",
    "Specific call recordings referenced for context (11/11/24, 11/12/24, 11/19/24)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: [EXTERNAL USE] Merchant Info Sheet - Harness Wealth_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:51:29

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
    "Contractual Terms and Opt-Out Clauses"
  ],
  "rules": [
    {
      "rule": "Implementation follows a structured timeline: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "Key stakeholders must be identified including GTM POC, Implementation POC, Head of Finance and Operations, and Billing POC",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Account Executive (AE) is responsible for filling company summary and goals sections",
      "type": "responsibility",
      "explicit": true
    },
    {
      "rule": "Implementation team collaborates with AE to document merchant goals and billing model details",
      "type": "responsibility",
      "explicit": true
    },
    {
      "rule": "Opt-out clause terms must be documented if they exist, including conditions for non-exercise",
      "type": "contractual",
      "explicit": true
    },
    {
      "rule": "Technical integration points must be documented (ERP, Tax Integration)",
      "type": "technical",
      "explicit": true
    },
    {
      "rule": "Merchant's business model and unique billing processes must be captured",
      "type": "requirement",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Revenue recognition component was explicitly excluded from scope to secure the partnership",
      "condition": "Despite being relevant to the merchant's needs, rev rec was aligned on 'not doing' to lock in partnership"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "condition": "This appears to be merchant-specific; the template suggests opt-out clauses may exist for other merchants"
    },
    {
      "exception": "Opt Out Date field shows 'Oct' without year or specific date",
      "condition": "Incomplete data entry or placeholder value"
    }
  ],
  "merchant_specific": [
    {
      "element": "Timeline dates",
      "customization": "Each merchant will have unique demo, scoping, signature, kickoff, and go-live dates"
    },
    {
      "element": "Stakeholder names and LinkedIn profiles",
      "customization": "Merchant-specific personnel including Head of Finance, Directors, and POCs"
    },
    {
      "element": "Company description and industry",
      "customization": "Harness Wealth operates in wealth management for business builders - each merchant will have different business models"
    },
    {
      "element": "Merchant goals and pain points",
      "customization": "This merchant seeks to automate revenue workflows without headcount increase; goals vary by merchant"
    },
    {
      "element": "Software business classification",
      "customization": "Business type drives the purchase decision and implementation approach"
    },
    {
      "element": "Opt-out clause presence and terms",
      "customization": "Some merchants have opt-out clauses with specific conditions, others do not"
    },
    {
      "element": "Scope exclusions",
      "customization": "Revenue recognition was excluded for this merchant; scope varies by merchant needs"
    },
    {
      "element": "ERP and Tax Integration systems",
      "customization": "Technical stack varies by merchant (fields left blank in this document)"
    },
    {
      "element": "Customer creation process uniqueness",
      "customization": "Billing model section asks about unique aspects of customer creation per merchant"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: [EXTERNAL USE] Merchant Info Sheet - Harness Wealth_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:51:34

### Original Content
```
com video gcvx1ltxyeroclcd-harness-tabs-prosposal-sync-november-19-2024 11 21 24 - Sandbox Walkthrough https: tabs rewatch com video cvk6eupblhmru4to-harness-sandbox-walkthrough-november-21-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Software Subscription   Usage Fees for   of users Generally Quarterly or Annual Is there any important merchant relationship information 1) What is the merchant temperament Serg is very easy to work with and sees the vision Pe...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Relationship Management",
    "Stakeholder Communication and Coordination",
    "Product Feature Prioritization",
    "Implementation Documentation and Onboarding",
    "Subscription Billing Models"
  ],
  "rules": [
    "Operations International Team should ignore certain sections marked explicitly",
    "AE (Account Executive) and Implementation team are responsible for filling specific sections",
    "Software subscription usage fees are calculated based on number of users",
    "Billing cycles are generally Quarterly or Annual",
    "Documentation must capture merchant temperament assessment",
    "Key Point of Contact (POC) identification is mandatory",
    "Buyer/decision maker must be identified and documented",
    "Feature preferences of key POC must be documented",
    "Implementation notes should include merchant relationship information"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' are excluded from certain team workflows",
    "Personal relationships with company representatives (e.g., Rebecca) may influence merchant engagement approach",
    "First-time buyers from new hires may require special attention or handling"
  ],
  "merchant_specific": [
    "Merchant temperament assessment (e.g., 'easy to work with', 'sees the vision')",
    "Personal relationship context (e.g., connection with Rebecca)",
    "Specific feature priorities vary by merchant (Contract Management, automated invoicing, Rev Rec, Renewals management)",
    "Key POC identification (in this case: Serg)",
    "Merchant's organizational context (e.g., 'first buy as a new hire')",
    "Billing frequency preference (Quarterly vs Annual)",
    "Number of users for usage fee calculation"
  ],
  "confidence_score": 0.75
}
```

---

