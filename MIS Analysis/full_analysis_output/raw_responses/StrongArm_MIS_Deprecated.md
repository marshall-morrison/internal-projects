# Raw LLM Analysis: StrongArm MIS (Deprecated)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:16:11

---

## Chunk 1: StrongArm MIS (Deprecated)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:16:11

### Original Content
```
Merchant Name (AE to fill) StongArm Technologies Implementation POC: (AE to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant no Information on how merchant bills Bills out of QB and HS, come contracts have complex parent child relationships, hardware software How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementa...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Merchant Onboarding and Implementation Workflow",
    "Operational Defaults and Standardization",
    "Stakeholder Communication and Handoff Procedures",
    "Merchant-Specific Customization Requirements"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Operational Default",
      "source": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 if none listed",
      "category": "Operational Default",
      "source": "explicit"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Operational Default",
      "source": "explicit"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Item)",
      "category": "Operational Default",
      "source": "explicit"
    },
    {
      "rule": "AE fills merchant name and implementation POC before handoff",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation team fills CX POC",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success fills Contract Processing Steps post-go-live",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success fills Events Processing section post-go-live if necessary",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success fills Integration Items Processing post-go-live if necessary",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success fills Customer Information section post-go-live",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "Workflow Responsibility",
      "source": "explicit"
    },
    {
      "rule": "Ops International Team should ignore Notes Sections",
      "category": "Workflow Responsibility",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Some contracts may require back-dating invoice date to final day of the month",
      "context": "Merchant-specific processing requests that may differ by contract",
      "type": "Contract Processing Variation"
    },
    {
      "exception": "StrongArm Technologies has complex parent-child relationships in contracts",
      "context": "Customer creation process and billing structure",
      "type": "Merchant Billing Complexity"
    },
    {
      "exception": "StrongArm bills out of QB (QuickBooks) and HS (likely HubSpot)",
      "context": "Billing system integration",
      "type": "Billing System Variation"
    },
    {
      "exception": "Contracts may include both hardware and software components",
      "context": "Contract structure for StrongArm Technologies",
      "type": "Product Mix Variation"
    },
    {
      "exception": "Integration items may require specific labeling (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "context": "Integration item processing",
      "type": "Integration Labeling Rules"
    },
    {
      "exception": "Certain invoices may require special memos based on merchant-customer relationship",
      "context": "Customer-specific invoice requirements",
      "type": "Invoice Customization"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "description": "StrongArm Technologies",
      "customization_type": "Identity"
    },
    {
      "element": "Implementation POC",
      "description": "To be filled by AE",
      "customization_type": "Contact Information"
    },
    {
      "element": "CX POC",
      "description": "To be added by Implementation team",
      "customization_type": "Contact Information"
    },
    {
      "element": "Billing Model",
      "description": "Bills out of QB and HS, complex parent-child relationships, hardware and software components",
      "customization_type": "Billing Configuration"
    },
    {
      "element": "Contract Processing Steps",
      "description": "Specific steps, items to ignore, and processing specifics per merchant request",
      "customization_type": "Processing Workflow"
    },
    {
      "element": "Events Processing",
      "description": "Important information on events billing (if applicable)",
      "customization_type": "Billing Feature"
    },
    {
      "element": "Integration Items Labeling",
      "description": "Instructions for assigning integration items with specific labels",
      "customization_type": "Integration Configuration"
    },
    {
      "element": "Post Processing Communications",
      "description": "Notification requirements for batch completion (who, where, when)",
      "customization_type": "Communication Protocol"
    },
    {
      "element": "Customer Information",
      "description": "Specifics about merchant's customers, special memos, invoice changes",
      "customization_type": "Customer Management"
    },
    {
      "element": "Merchant Temperament",
      "description": "Great temperament, friends and family partner, evaluating since pre-seed",
      "customization_type": "Relationship Context"
    },
    {
      "element": "Key Features",
      "description": "Ability to manage bespoke contracts",
      "customization_type": "Product Requirements"
    }
  ],
  "confidence_score": 0.85
}
```

---

