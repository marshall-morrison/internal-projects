# Raw LLM Analysis: MIS Template [12.22.24 Amended]

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:56:25

---

## Chunk 1: MIS Template [12.22.24 Amended]_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:56:25

### Original Content
```
Merchant Name: NAME Implementation POC: (IM to fill) CX POC: [IMP to Add] Key people at Merchant Accountant: Not specified CFO: Richard Rein Director of FP A: Matt Boland Customer service rep who is really involved: Not specified Account Receivable POC: Richard Rein (currently overseeing outsourced contractor) Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Process",
    "Contract Processing and Billing Configuration",
    "Stakeholder Management and Communication Protocols",
    "Default Operational Parameters and Standards",
    "Post-Implementation Support and Customization"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax)",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Implementation team must fill billing model section",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Contract Processing Steps post-go-live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Events Processing section post-go-live if necessary",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Integration Items Processing section post-go-live if necessary",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Customer Information section post-go-live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills post-go-live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "AE fills Merchant Calls notes prior to Implementation involvement; Implementation fills prior to go-live; Success fills post-go-live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "Process Ownership",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., back-dating invoice date to final day of month)",
      "condition": "When merchant requests specific processing that differs by contract",
      "impact": "Overrides standard processing procedures"
    },
    {
      "exception": "Integration items may have specific labeling requirements",
      "condition": "Depends on integration type (e.g., Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')",
      "impact": "Requires custom categorization per integration"
    },
    {
      "exception": "Post-processing communications are conditional",
      "condition": "Only required if specified for the merchant",
      "impact": "Ops team may need to notify specific stakeholders at specific times"
    },
    {
      "exception": "Events Processing section is conditional",
      "condition": "Only filled if necessary for the merchant",
      "impact": "Not all merchants require events billing"
    },
    {
      "exception": "Special invoice requirements may exist for certain customers",
      "condition": "Based on merchant-customer relationship",
      "impact": "May require special memos or invoice changes"
    }
  ],
  "merchant_specific": [
    {
      "element": "Implementation POC",
      "customization_type": "Contact Information",
      "notes": "Filled by IM (Implementation Manager)"
    },
    {
      "element": "CX POC",
      "customization_type": "Contact Information",
      "notes": "Added by IMP (Implementation team)"
    },
    {
      "element": "Key people at Merchant (Accountant, CFO, Director of FP&A, Customer Service Rep, Account Receivable POC)",
      "customization_type": "Stakeholder Mapping",
      "notes": "Merchant-specific contacts for various functions"
    },
    {
      "element": "Billing model",
      "customization_type": "Process Configuration",
      "notes": "Includes customer creation process, how merchant bills, contract structure, one-off considerations"
    },
    {
      "element": "Contract Processing Steps",
      "customization_type": "Process Configuration",
      "notes": "Merchant-specific processing steps, items to ignore, specific processing requests"
    },
    {
      "element": "Integration Items Processing instructions",
      "customization_type": "Technical Configuration",
      "notes": "Merchant-specific labeling and categorization rules"
    },
    {
      "element": "Post Processing Communications",
      "customization_type": "Communication Protocol",
      "notes": "Who to notify, where, and when based on merchant phase"
    },
    {
      "element": "Customer Information",
      "customization_type": "Customer Management",
      "notes": "Specific customer details, special memo requirements, invoice changes"
    },
    {
      "element": "Merchant temperament",
      "customization_type": "Relationship Management",
      "notes": "Understanding merchant personality and preferences"
    },
    {
      "element": "Tabs features that key POC cares about",
      "customization_type": "Feature Prioritization",
      "notes": "Merchant-specific feature importance"
    }
  ],
  "confidence_score": 0.92
}
```

---

