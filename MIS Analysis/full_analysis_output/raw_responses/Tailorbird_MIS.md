# Raw LLM Analysis: Tailorbird MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 09:53:02

---

## Chunk 1: Tailorbird MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:53:02

### Original Content
```
loom com share 653f14e4cfb94a819a428b004a3a2973 sid e63bc5e5-e42e-47bc-bf1e-b2857545b1b0 Eval check in [12 12] https: www loom com share f1a199a9f0a44cf3a7ee9cd3a46fd7ca sid e83a64f4-6450-453c-a3a9-934b7dff45a6 Notes Sections [Ops International Team to Ignore] (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Annual upfront usage fee and onboarding fee Variable usage based on property onboarding volume, which is typically sent via email when a n...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing and fee structure",
    "Merchant relationship and communication style",
    "Product features and integration requirements",
    "Implementation handoff process",
    "Operational team coordination"
  ],
  "rules": [
    "Annual upfront usage fee must be charged to merchant",
    "Onboarding fee must be collected",
    "Variable usage fees are based on property onboarding volume",
    "Property onboarding notifications are typically sent via email when a new property goes live",
    "Implementation team is the DRI (Directly Responsible Individual) for completion on handoff",
    "Account Executive (AE) should fill in merchant information if available",
    "Sections marked 'Ops International Team to Ignore' should be excluded from international operations team workflow"
  ],
  "exceptions": [
    "International Operations Team should ignore specific sections marked for exclusion",
    "Variable usage fees are conditional based on property onboarding volume (not fixed)",
    "AE fills information only 'if they have' it - suggesting optional completion based on availability"
  ],
  "merchant_specific": [
    "Merchant temperament profile: 'Friendly, straightforward, empathetic and excited about what Tabs is building'",
    "Key features prioritized by merchant POC: QBO integration, invoice automation, payment portal, parent child structures, cash forecasting, rev rec, revenue reporting",
    "Property onboarding volume varies by merchant",
    "Communication preferences and style should align with merchant temperament",
    "Feature focus areas are merchant-dependent based on POC priorities"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for confidence score**: The document appears to be internal notes or a template with some formatting issues (URLs are broken up, unclear structure). While the key information about billing, merchant temperament, and feature priorities is clear, the context around the Loom links and some abbreviated sections reduces certainty about complete interpretation. The content is actionable but would benefit from clearer formatting and complete context.

---

## Chunk 2: Tailorbird MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:53:08

### Original Content
```
Merchant Name: Tailorbird Implementation POC: (AE to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters and Fallback Values",
    "Cross-functional Communication and Handoff Procedures",
    "Integration and Event Processing Management",
    "Customer-Specific Requirements and Customizations"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "billing_defaults",
      "owner": "Operations"
    },
    {
      "rule": "Default Net Payment Terms is 0 days if none listed",
      "category": "billing_defaults",
      "owner": "Operations"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_defaults",
      "owner": "Operations"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "tax_handling",
      "owner": "Operations"
    },
    {
      "rule": "Implementation Success team fills contract processing steps post-go-live",
      "category": "responsibility_assignment",
      "owner": "Implementation Success"
    },
    {
      "rule": "Implementation team fills billing model section",
      "category": "responsibility_assignment",
      "owner": "Implementation"
    },
    {
      "rule": "AE fills feature requests prior to implementation handoff",
      "category": "responsibility_assignment",
      "owner": "Account Executive"
    },
    {
      "rule": "Success team fills feature requests post-go-live",
      "category": "responsibility_assignment",
      "owner": "Success Team"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., back-dating invoice dates to final day of month)",
      "context": "Some merchants request specific processing that differs by contract"
    },
    {
      "exception": "Certain contracts may have items to ignore during processing",
      "context": "Contract processing may require selective data handling"
    },
    {
      "exception": "Integration items may have special labeling requirements per merchant",
      "context": "Examples given: Statsig items labeled as 'Sales', Pinata items as 'Software Subscription Bundle' unless noted otherwise"
    },
    {
      "exception": "Special memos may be required for certain customer invoices",
      "context": "Customer-specific invoice customizations based on merchant-customer relationships"
    },
    {
      "exception": "AP Portal submissions handled by Ops team with medium urgency",
      "context": "Some customers require payment via their own AP Portal"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Tailorbird",
      "type": "identifier",
      "customizable": true
    },
    {
      "element": "Implementation POC and CX POC fields",
      "type": "contact_information",
      "customizable": true,
      "note": "To be filled by AE and Implementation teams"
    },
    {
      "element": "Billing model details",
      "type": "billing_configuration",
      "customizable": true,
      "note": "Includes customer creation process, contract structure, and unique merchant characteristics"
    },
    {
      "element": "Integration items labeling instructions",
      "type": "integration_processing",
      "customizable": true,
      "note": "Merchant-specific rules for categorizing integration items"
    },
    {
      "element": "Post-processing notification requirements",
      "type": "communication_workflow",
      "customizable": true,
      "note": "Specifies who to notify, where, and when during different merchant phases"
    },
    {
      "element": "Customer-specific information section",
      "type": "customer_handling",
      "customizable": true,
      "note": "Includes special memos and invoice changes based on relationships"
    },
    {
      "element": "Feature requests tracking",
      "type": "product_requirements",
      "customizable": true,
      "note": "Examples include MRR GDR reporting and AP Portal submissions with urgency levels"
    },
    {
      "element": "Merchant call recordings and documentation",
      "type": "knowledge_management",
      "customizable": true,
      "note": "Includes demo, proposal review, and custom demo videos with timestamps"
    }
  ],
  "confidence_score": 0.85
}
```

---

