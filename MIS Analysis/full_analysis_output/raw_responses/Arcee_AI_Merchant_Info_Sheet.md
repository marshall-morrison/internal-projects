# Raw LLM Analysis: Arcee AI - Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:19:53

---

## Chunk 1: Arcee AI - Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:19:53

### Original Content
```
Arcee AI Demo date: Nov 1, 2024 Scoping start date: Nov 4, 2024 MSA Signature Date: Nov 4, 2024 Onboarding Kick Off Date: [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Mark McQuade (mark arcee ai) Fractional Controller: Ted _____ (ted neweconomycpa com) Chief of Staff   Billing: Molly Niland (molly arcee ai) Revenue Ops: Amber _____ (amber arcee ai) Business Operations: Mohit Khullar (mohit arcee ai) Company summary Platfor...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Stakeholder Identification and Contact Management",
    "Business Goals and Pain Points",
    "Revenue Operations and Financial Reporting Requirements",
    "Product/Service Offering Context"
  ],
  "rules": [
    {
      "rule": "Demo must occur before scoping start date",
      "evidence": "Demo date: Nov 1, 2024, Scoping start date: Nov 4, 2024",
      "type": "explicit"
    },
    {
      "rule": "MSA signature should align with or precede scoping start",
      "evidence": "MSA Signature Date: Nov 4, 2024 matches Scoping start date",
      "type": "implicit"
    },
    {
      "rule": "Key stakeholder roles must be identified: CEO, Controller, Billing, Revenue Ops, Business Operations",
      "evidence": "Structured list of key people with specific roles",
      "type": "explicit"
    },
    {
      "rule": "Merchant goals and pain points must be documented during onboarding",
      "evidence": "Goals (North star) section with detailed pain points",
      "type": "explicit"
    },
    {
      "rule": "Opt-out clause status must be documented",
      "evidence": "No opt out clause",
      "type": "explicit"
    },
    {
      "rule": "GTM POC and Implementation POC must be assigned",
      "evidence": "Fields present for GTM POC and Implementation POC",
      "type": "explicit"
    },
    {
      "rule": "ERP and Tax Integration systems must be identified",
      "evidence": "Fields for ERP and Tax Integration",
      "type": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Onboarding Kick Off Date field can be left empty if not yet scheduled",
      "evidence": "[If Exists] notation",
      "condition": "Date not yet determined"
    },
    {
      "exception": "Opt Out Date may not exist for all merchants",
      "evidence": "Field present but empty, with 'No opt out clause' noted separately",
      "condition": "Merchant contract does not include opt-out provisions"
    },
    {
      "exception": "Some contact information may be incomplete (last names, full emails)",
      "evidence": "Ted _____ (ted neweconomycpa com), Amber _____ (amber arcee ai)",
      "condition": "Information gathering in progress"
    }
  ],
  "merchant_specific": [
    {
      "element": "Timeline dates",
      "customization": "All dates (Demo, Scoping, MSA, Kick Off, Opt Out, Go Live) are merchant-specific",
      "example": "Nov 1, 2024 for Arcee AI"
    },
    {
      "element": "Key personnel and contact information",
      "customization": "Names, titles, and email addresses vary by merchant organizational structure",
      "example": "CEO: Mark McQuade for Arcee AI"
    },
    {
      "element": "Company summary and business model",
      "customization": "Description of merchant's product/service offering",
      "example": "Small Language Models (SLMs) platform"
    },
    {
      "element": "Merchant goals and pain points",
      "customization": "Specific business objectives and challenges",
      "example": "Ballooning AR due to manual invoicing, Series B prep in 1Q25"
    },
    {
      "element": "Required reporting and features",
      "customization": "Specific features needed based on merchant goals",
      "example": "ARR and Rev Rec reporting, cash forecasting, collections view"
    },
    {
      "element": "ERP and Tax Integration systems",
      "customization": "Technology stack varies by merchant",
      "example": "Fields left blank for Arcee AI"
    },
    {
      "element": "Opt-out clause terms",
      "customization": "Contract terms vary by negotiation",
      "example": "No opt out clause for Arcee AI"
    },
    {
      "element": "Merchant temperament assessment",
      "customization": "Relationship management approach varies",
      "example": "Question noted but not answered in document"
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 2: Arcee AI - Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:19:55

### Original Content
```
CEO is the decision maker He seemed frustrated with the previous invoicing process, but was very friendly and approachable He moves fast and has a technical background (former CTO) 2) Is there key POC the buyer decision maker Mark is the decision maker who gave the final thumbs up He had us do a second demo with his team to get their sign-off ahead of time Ted is the fractional controller who will be a power user, along with Molly who has been managing billing thus far 3) What are the Tabs featu...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Decision-Making Process",
    "Contract Processing and Revenue Schedule Creation",
    "Billing Model Configuration and Payment Terms",
    "System Features and Integration Requirements",
    "Operational Defaults and Processing Standards"
  ],
  "rules": [
    {
      "rule": "CEO/Mark is the final decision maker for approvals",
      "category": "stakeholder_management",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Second demo with team required before final sign-off",
      "category": "sales_process",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Create separate revenue schedule for each payment listed in contract",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Service Start Date must match agreement date from contract",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Periods field should be set to 1",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Frequency field should be set to None",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Net Terms must be extracted from contract next to total price",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Integration Item should be 'SAAS Revenue'",
      "category": "revenue_schedule",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Ignore credits, pricing specifics, and invoicing details in contracts",
      "category": "contract_processing",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Net Payment Terms is 30 days",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Billing Frequency should refer to contract",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "No taxes should be processed as line items",
      "category": "tax_handling",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Item Name should match payment phase name from contract (e.g., 'Phase 1- 1st Payment')",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Total price must be extracted from each payment line item in contract",
      "category": "revenue_schedule",
      "specificity": "general"
    },
    {
      "rule": "Start Date for revenue schedule matches Service Start Date",
      "category": "revenue_schedule",
      "specificity": "general"
    }
  ],
  "exceptions": [
    {
      "exception": "Some contracts have milestone payments while merchant is moving towards pure SaaS",
      "condition": "Legacy contracts vs new contracts",
      "handling": "Process according to contract type shown in screenshots"
    },
    {
      "exception": "Payment terms vary by client",
      "condition": "Client-specific arrangements",
      "handling": "Extract from individual contract"
    },
    {
      "exception": "Some annual payments are upfront depending on client",
      "condition": "Client-specific payment arrangements",
      "handling": "Follow contract specifications"
    },
    {
      "exception": "Specific processing requests may differ by contract",
      "condition": "Special merchant requests",
      "handling": "Example given: back-date invoice date to final day of month"
    },
    {
      "exception": "Different contract formats require different processing steps",
      "condition": "Contract format variation",
      "handling": "Follow screenshot-specific instructions and reference LOOM videos"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key stakeholders",
      "details": "CEO (Mark) as decision maker, Ted (fractional controller) and Molly as power users",
      "customization_needed": true
    },
    {
      "element": "Feature priorities",
      "details": "Contract ingest, collections kanban, cash application, dunning emails, revenue reporting",
      "customization_needed": true
    },
    {
      "element": "Billing model evolution",
      "details": "Transitioning from milestone payments to pure SaaS solution",
      "customization_needed": true
    },
    {
      "element": "Integration item naming",
      "details": "Uses 'SAAS Revenue' as integration item",
      "customization_needed": true
    },
    {
      "element": "Contract processing references",
      "details": "Specific screenshots and LOOM video recordings for this merchant's contract format",
      "customization_needed": true
    },
    {
      "element": "Items to ignore",
      "details": "Credits, pricing specifics, and invoicing details",
      "customization_needed": true
    },
    {
      "element": "Tax handling",
      "details": "No taxes processed as line items",
      "customization_needed": true
    },
    {
      "element": "Payment structure",
      "details": "Varying payment terms, some annual upfront depending on client",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Arcee AI - Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:20:04

### Original Content
```
Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merchant Post Processing Communications (if necessary) Does Ops Team need to notify anyone on the team re: completion of processing batches in Implementation or Active phase Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Item categorization and labeling rules",
    "Team notification and communication protocols",
    "Merchant processing workflow and phases",
    "Feature requests and system integrations",
    "Customer-specific information management"
  ],
  "rules": [
    {
      "rule": "All Statsig integration items must be labeled as 'Sales'",
      "type": "categorization",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' by default",
      "type": "categorization",
      "explicit": true
    },
    {
      "rule": "Customer Success (Azmat Aziz) must be notified when contracts are processed in Active phase",
      "type": "notification",
      "explicit": true
    },
    {
      "rule": "Notifications should be sent via Messari internal merchant channel",
      "type": "communication",
      "explicit": true
    },
    {
      "rule": "Ops Team is responsible for notifying stakeholders upon completion of processing batches",
      "type": "workflow",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items may have different labels if specified by Merchant Post Processing Communications",
      "condition": "When Merchant Post Processing Communications provides alternative instructions",
      "applies_to": "Pinata integration labeling rule"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration vendor names",
      "examples": ["Statsig", "Pinata"],
      "customizable": true,
      "note": "Each merchant may have different integration vendors requiring specific labeling"
    },
    {
      "element": "Notification recipients",
      "examples": ["Customer Success - Azmat Aziz"],
      "customizable": true,
      "note": "Contact person varies by merchant"
    },
    {
      "element": "Merchant processing phases",
      "examples": ["Implementation", "Active"],
      "customizable": false,
      "note": "Appears to be standard workflow phases"
    },
    {
      "element": "Internal communication channels",
      "examples": ["Messari internal merchant channel"],
      "customizable": true,
      "note": "Each merchant likely has dedicated communication channel"
    },
    {
      "element": "Feature requests",
      "examples": ["Hubspot integration for payment info and past due balances"],
      "customizable": true,
      "note": "Merchant-specific integration needs and requirements"
    }
  ],
  "confidence_score": 0.85
}
```

---

