# Raw LLM Analysis: Attention - Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:16:33

---

## Chunk 1: Attention - Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:16:33

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) Will need to understand frequency of seat usage Integration Items Processing (if necessary) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merchant Post Processing Communications (if necessary) Does the Op...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and Revenue Processing Workflows",
    "Integration Item Classification and Labeling",
    "Post-Processing Communication Protocols",
    "Customer Relationship Management and Upsells",
    "Implementation and Contract Management"
  ],
  "rules": [
    {
      "rule": "Default tax processing: Every tax line item becomes a BT Events Processing when none listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active phase",
      "category": "Post Processing Communications",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Implementation Notes sections",
      "category": "Operational Scope",
      "explicit": true
    },
    {
      "rule": "Frequency of seat usage must be understood for processing",
      "category": "SaaS Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by Merchant",
      "condition": "Merchant provides alternative labeling instructions"
    },
    {
      "exception": "Post-processing communications are conditional on necessity",
      "condition": "Only required 'if necessary' based on merchant requirements"
    },
    {
      "exception": "Tax processing default only applies when 'None Listed'",
      "condition": "Alternative instructions may override the BT Events Processing default"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customizable": true,
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"],
      "note": "Each merchant may have different integration vendors requiring specific labels"
    },
    {
      "element": "Notification recipients and channels",
      "customizable": true,
      "examples": ["Azmat Aziz via Messari internal merchant channel"],
      "note": "Who, where, and when notifications occur varies by merchant"
    },
    {
      "element": "Contract structure and billing model",
      "customizable": true,
      "examples": ["SaaS contracts based on seat usage"],
      "note": "Billing models and contract types differ per merchant"
    },
    {
      "element": "Key contacts and stakeholders",
      "customizable": true,
      "examples": ["Anis (main contact)", "Jacob (interim handler)", "fractional accountant"],
      "note": "Contact persons and organizational structure are merchant-specific"
    },
    {
      "element": "Customer priorities",
      "customizable": true,
      "examples": ["Upsells are very important"],
      "note": "Business priorities and focus areas vary by merchant"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Attention - Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:16:38

### Original Content
```
Merchant Demo date: Aug 8, 2024 Scoping start date: Aug 8, 2024 MSA Signature Date: Aug 19, 2024 Onboarding Kick Off Date: [If Exists] Opt Out Date: Nov 17, 2024 Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Anis Bennaceur - anis attention tech Head of Sales: Jacob Fleisher - jacob attention tech Billing POC: anis attention tech Etc Company summary AI-powered sales agent that automatically fills out CRMs after sales calls, scores conversations and o...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Billing Model and Revenue Recognition (SaaS + Usage-based)",
    "Contract Processing Defaults and Standards",
    "Stakeholder Management and Points of Contact",
    "Business Goals and Pain Points (CRM automation, invoicing, AR automation, reporting)"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Frequency",
      "explicit": true
    },
    {
      "rule": "Annual contracts are billed upfront",
      "category": "Billing Model",
      "explicit": true
    },
    {
      "rule": "Seat usage must be tracked separately for upsells",
      "category": "Usage Tracking",
      "explicit": true
    },
    {
      "rule": "Merchant currently uses Stripe for invoice creation and billing management",
      "category": "Current Systems",
      "explicit": true
    },
    {
      "rule": "Tax handling as line item needs to be defined",
      "category": "Tax Processing",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing may differ (e.g., back-dating invoice dates to final day of month)",
      "condition": "When merchant requests specific processing variations per contract",
      "note": "This is mentioned as a potential example but not confirmed as an active requirement"
    },
    {
      "exception": "Some items in contracts may need to be ignored during processing",
      "condition": "Section exists but no specific items listed",
      "note": "Placeholder for future definition"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "AI-powered sales agent for CRM automation - this context affects their billing needs"
    },
    {
      "element": "Key Stakeholders",
      "details": "CEO: Anis Bennaceur, Head of Sales: Jacob Fleisher, Billing POC: Anis - all with 'attention tech' domain"
    },
    {
      "element": "Current State",
      "details": "180 total contracts, sales team manually creating invoices through Stripe"
    },
    {
      "element": "Primary Pain Points",
      "details": "Need to track upsells (seat usage), scaling sales team, need better billing approach, AR automation, reporting capabilities"
    },
    {
      "element": "Revenue Model",
      "details": "Dual model: SaaS subscription + seat-based usage charges"
    },
    {
      "element": "Integration Requirements",
      "details": "ERP and Tax Integration fields present but not populated - needs to be defined"
    },
    {
      "element": "Timeline",
      "details": "Demo to Opt Out span: Aug 8 - Nov 17, 2024 (approximately 3 months)"
    },
    {
      "element": "Missing Information",
      "details": "Onboarding Kick Off Date, Go Live Date, GTM POC, Implementation POC not specified"
    }
  ],
  "confidence_score": 0.85
}
```

**Confidence Reasoning**: The document is clearly structured with explicit default rules and merchant information. However, several sections are incomplete (ERP, Tax Integration, specific contract processing steps, Go Live Date), and some critical details like how to handle taxes and what to ignore in contracts are undefined. The confidence score reflects high certainty about what IS documented, but acknowledges significant gaps in the implementation details.

---

