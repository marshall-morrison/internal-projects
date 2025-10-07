# Raw LLM Analysis: Merchant Info Sheet - Hubble

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:37:27

---

## Chunk 1: Merchant Info Sheet - Hubble_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:37:27

### Original Content
```
1) What is the merchant's temperament 2) Is there a key POC: (i e : who is the buyer decision maker ) 3) What are the Tabs features that the key POC cares about
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship assessment and profiling",
    "Stakeholder identification and decision-maker mapping",
    "Product feature prioritization based on customer needs",
    "Customer discovery and requirements gathering",
    "Sales qualification and account planning"
  ],
  "rules": [
    "Must identify and document the merchant's temperament/personality type",
    "Must identify the key Point of Contact (POC) who serves as the buyer decision maker",
    "Must determine which Tabs product features are most important to the key POC",
    "All three elements (temperament, POC, and feature preferences) must be documented for each merchant",
    "Analysis should focus on the decision-maker's specific interests rather than general merchant needs"
  ],
  "exceptions": [
    "No explicit exceptions mentioned in this instruction set",
    "Implicit flexibility may exist in how temperament is assessed or categorized",
    "Multiple POCs or decision-makers may need to be identified if no single buyer exists"
  ],
  "merchant_specific": [
    "Merchant temperament - will vary significantly by merchant and requires individual assessment",
    "Key POC identity - unique to each merchant organization and their decision-making structure",
    "Feature preferences - different merchants/POCs will prioritize different Tabs features based on their business needs",
    "Decision-making hierarchy - organizational structure varies by merchant",
    "Tabs features - refers to a specific product (Tabs) with various features that need to be mapped to merchant needs"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Hubble_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:37:32

### Original Content
```
HUBBLE MIS   This was a legacy deal from pre-AE times MIS purpose for contract processing by Ops - see Contract Processing Steps section  Merchant Demo date: Scoping start date: MSA Signature Date: Onboarding Kick Off Date: Dec 4, 2024 [If Exists] Opt Out Date: Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Customer volume: Billing model: Key people at Merchant Valerie (Siegfried) Abe (Hubble) Company summary (AE to fill) Goals (North star) (AE  Implementation to fi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow",
    "Merchant Onboarding and Timeline Management",
    "Billing and Subscription Configuration",
    "Integration Items and Customer Management",
    "Cross-functional Communication and Coordination"
  ],
  "rules": [
    "Customer names should already exist in Tabs and be synced from QBO",
    "Customer information can be found in first paragraph of contract",
    "Use effective date from first paragraph for start date and service start date",
    "Term length must be extracted from section 1 of contract",
    "Fee information must be extracted from section 3 of contract",
    "Implementation Fee Billing name should be 'Pilot Subscription'",
    "Integration Item should be labeled as 'Pilot Subscription'",
    "Service terms, payment terms, and billing frequency should refer to contract specifications",
    "No taxes should be handled as line items for this merchant",
    "Ops International Team should ignore Notes Sections",
    "Contract processing requires coordination between AE and Implementation Success teams",
    "Post-processing notifications may be required to Customer Success or other stakeholders"
  ],
  "exceptions": [
    "This is a legacy deal from pre-AE times with MIS purpose for contract processing",
    "Opt out clause may exist - requires monitoring of merchant goals to prevent exercise",
    "Unique customer creation processes may exist per merchant",
    "Contract-specific variations possible (e.g., back-dating invoice dates to final day of month)",
    "Integration items may have special labeling requirements (examples: 'Sales' for Statsig, 'Software Subscription Bundle' for Pinata)",
    "Special memos may be required for certain customer invoices",
    "Invoice changes may be needed due to merchant-customer relationships"
  ],
  "merchant_specific": [
    "Merchant name: HUBBLE",
    "Key contacts: Valerie (Siegfried), Abe (Hubble)",
    "Onboarding Kick Off Date: Dec 4, 2024",
    "Go Live Date: Jan 1, 2025",
    "GTM POC and Implementation POC fields (to be filled)",
    "ERP system (to be specified)",
    "Tax Integration details (to be specified)",
    "Customer volume metrics (to be specified)",
    "Merchant-specific billing model",
    "North star goals and pain points being solved",
    "Merchant-specific contract breakup structure",
    "Merchant-specific events billing (if applicable)",
    "Merchant-specific integration item labeling rules",
    "Merchant-specific post-processing notification requirements",
    "Merchant internal channel for communications",
    "Special customer information and invoice requirements"
  ],
  "confidence_score": 0.85
}
```

---

