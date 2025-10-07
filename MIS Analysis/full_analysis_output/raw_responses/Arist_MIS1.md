# Raw LLM Analysis: Arist MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:23:50

---

## Chunk 1: Arist MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:23:50

### Original Content
```
Jasper is relatively easy going and wears many hats at Arist He will also outsource some of the manual work to a contractor at times 3) What are the Tabs features that the key POC cares about Scalable solution to support their growth, Jasper is a team of 1 Integration with Quickbooks Automated reporting on O2C - all very manual today ANY SORT OF NON-STANDARD DEAL CONVERSATIONS TO BE FILLED OUT BY THE SC, with documentation linked How any mid contract upgrades in seats will be treated
```

### LLM Analysis Response
```json
{
  "themes": [
    "Point of Contact (POC) Management and Roles",
    "Product Features and Integration Requirements",
    "Automation and Scalability Needs",
    "Non-Standard Deal Documentation",
    "Contract Modification Procedures"
  ],
  "rules": [
    "Non-standard deal conversations must be filled out by the SC (Sales/Success Consultant)",
    "Non-standard deals require documentation to be linked",
    "Mid-contract seat upgrades must have defined treatment procedures",
    "Integration with QuickBooks is a required feature",
    "Automated reporting on O2C (Order-to-Cash) must be provided",
    "Solution must be scalable to support growth",
    "Manual work may be outsourced to contractors"
  ],
  "exceptions": [
    "Non-standard deals require special SC documentation process (deviation from standard deal flow)",
    "Mid-contract upgrades in seats are treated as special cases requiring predefined handling",
    "Jasper may outsource manual work to contractors (exception to in-house handling)"
  ],
  "merchant_specific": [
    "Merchant name: Arist",
    "Key POC: Jasper (described as 'easy going' and 'wears many hats')",
    "Current state: O2C reporting is 'all very manual today'",
    "Team size: Jasper is a team of 1",
    "Specific integration requirement: QuickBooks",
    "Pain points: Manual processes, need for scalability, single-person team operations"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document provides clear information about POC, features, and requirements
- Some context is missing (e.g., what "SC" stands for, specific upgrade policies)
- The fragment nature suggests this is part of a larger document
- Terminology like "O2C" and "Tabs features" is used without full explanation
- The instruction about non-standard deals is clear but lacks detailed procedures

---

## Chunk 2: Arist MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:23:58

### Original Content
```
Merchant Name Arist Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant has r...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Merchant Onboarding and Implementation Workflow",
    "Default Operational Parameters and Overrides",
    "Stakeholder Communication and Responsibility Assignment",
    "Customer-Specific Billing Customizations"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Default Net Payment Terms is 0 days if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction)",
      "category": "tax_processing"
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation Success team fills Events Processing section post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation Success team fills Integration Items Processing section post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation Success team fills Customer Information section post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "AE fills Merchant Calls section prior to Implementation involvement",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation team fills Merchant Calls section prior to go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Success team fills Merchant Calls section post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Arist pricing is per-seat but flat SaaS model",
      "category": "merchant_billing",
      "merchant": "Arist"
    },
    {
      "rule": "Arist does not recognize revenue as seats are activated",
      "category": "merchant_billing",
      "merchant": "Arist"
    },
    {
      "rule": "Arist seats are not added on individual basis",
      "category": "merchant_billing",
      "merchant": "Arist"
    },
    {
      "rule": "New Arist seats are tracked via email and invoiced once for new amount",
      "category": "merchant_billing",
      "merchant": "Arist"
    },
    {
      "rule": "Arist provides prorated amounts for seat additions",
      "category": "merchant_billing",
      "merchant": "Arist"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing may differ (e.g., always back-date invoice date to final day of month)",
      "context": "Contract Processing Steps section allows for merchant-requested variations"
    },
    {
      "exception": "Integration item labeling varies by merchant (Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')",
      "context": "Integration Items Processing requires merchant-specific mapping rules"
    },
    {
      "exception": "Special memos may be required for certain customer invoices",
      "context": "Customer Information section notes customer-specific requirements"
    },
    {
      "exception": "Invoice changes may occur due to merchant-customer relationship dynamics",
      "context": "Customer Information section"
    },
    {
      "exception": "Arist has smaller volume but high-value contracts due to enterprise focus",
      "context": "Merchant temperament and business model"
    }
  ],
  "merchant_specific": [
    {
      "element": "Implementation POC and CX POC fields",
      "customization_type": "contact_assignment",
      "description": "Each merchant requires designated points of contact"
    },
    {
      "element": "Billing model description",
      "customization_type": "billing_configuration",
      "description": "Unique customer creation process and contract structure per merchant"
    },
    {
      "element": "Contract processing specifics",
      "customization_type": "processing_rules",
      "description": "Merchant may request specific processing variations like invoice date back-dating"
    },
    {
      "element": "Integration item labeling rules",
      "customization_type": "categorization_mapping",
      "description": "Each merchant may have different categorization rules for integration items"
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "communication_workflow",
      "description": "Specific stakeholders and timing for batch completion notifications"
    },
    {
      "element": "Customer-specific billing instructions",
      "customization_type": "customer_exceptions",
      "description": "Special handling for individual customers within a merchant account"
    },
    {
      "element": "Merchant temperament notes",
      "customization_type": "relationship_context",
      "description": "Business model characteristics (e.g., enterprise focus, contract volume/value)"
    }
  ],
  "confidence_score": 0.85
}
```

---

