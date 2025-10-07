# Raw LLM Analysis: Plenful MIS Template

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 09:57:41

---

## Chunk 1: Plenful MIS Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:57:41

### Original Content
```
Merchant Name Plenful https: app hubspot com contacts 43610657 record 0-3 35681553063  Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Mark the contracts as proces...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Processing",
    "Billing Terms (BT) Configuration",
    "Pricing and Payment Cadence Management",
    "Service and Billing Date Determination",
    "Tiered and Overage Pricing Structures"
  ],
  "rules": [
    {
      "rule": "Item Name should use the product or service name listed in the contract",
      "category": "Data Entry"
    },
    {
      "rule": "Quantity defaults to 1 unless explicitly listed",
      "category": "Data Entry"
    },
    {
      "rule": "Total Price should use the listed price from the contract",
      "category": "Pricing"
    },
    {
      "rule": "Service Start Date should use the Effective Date or last signature date",
      "category": "Dates"
    },
    {
      "rule": "If kickoff date is available, use that for Service Start Date; otherwise use last signature date",
      "category": "Dates"
    },
    {
      "rule": "Billing Start Date should use the same date as Service Start Date unless a specific date is listed",
      "category": "Dates"
    },
    {
      "rule": "Months of Service should use the contract term length stated in Subscription and Payments section",
      "category": "Contract Terms"
    },
    {
      "rule": "Frequency should align with the payment cadence in the subscription and payments section",
      "category": "Billing"
    },
    {
      "rule": "Net Terms default to 30 days if not explicitly listed in Payment section",
      "category": "Payment Terms"
    },
    {
      "rule": "Price adjustments must account for billing cadence (e.g., monthly pricing invoiced quarterly needs to be multiplied by 3)",
      "category": "Pricing"
    },
    {
      "rule": "Product fees table pricing must be modified based on billing cadence category",
      "category": "Pricing"
    },
    {
      "rule": "Tiered BTs should be processed on a monthly cadence",
      "category": "Tiered Pricing"
    },
    {
      "rule": "Mark contracts as processed and assign customers with no BTs post-go-live",
      "category": "Post-Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Appendix sections where platform features cannot be matched to quantity and pricing tables can be IGNORED",
      "condition": "When correspondence between features and pricing is unclear"
    },
    {
      "exception": "Short-term contracts (less than a year) should be automatically extended to 12 months",
      "condition": "Contract term is less than one year"
    },
    {
      "exception": "Additional BTs in appendix need to be processed separately from product fees table",
      "condition": "When appendix contains additional billing terms"
    },
    {
      "exception": "Tiered pricing requires attention to included quantities in platform plan to determine structure",
      "condition": "When processing tiered BTs"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name (Plenful)",
      "type": "Identifier"
    },
    {
      "element": "Implementation POC and CX POC",
      "type": "Contact Information",
      "note": "To be filled by Implementation team"
    },
    {
      "element": "Billing model section",
      "type": "Custom Configuration",
      "note": "Implementation team fills this section"
    },
    {
      "element": "Unique customer creation process",
      "type": "Process Customization",
      "note": "Merchant-specific information required"
    },
    {
      "element": "How merchant bills and contract structure",
      "type": "Billing Configuration",
      "note": "Varies by merchant"
    },
    {
      "element": "One-off things to know about the merchant",
      "type": "Special Notes",
      "note": "Merchant-specific exceptions or requirements"
    },
    {
      "element": "Contract Processing Steps",
      "type": "Workflow",
      "note": "Implementation Success team fills post-go-live"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Rationale**: The document is somewhat fragmented and contains incomplete sections (e.g., "IMP to Add", truncated tiered pricing example). However, the core rules and patterns are clear enough to extract meaningful guidance. The confidence is reduced due to incomplete examples and some ambiguous phrasing, but the main operational rules are well-defined.

---

## Chunk 2: Plenful MIS Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:57:41

### Original Content
```
08 This is because the first 10k is included Example  2 Will need to be a tiered BT with quantity  100k claims at  0 09 Process additional support hours as a separate unit BT - no need to make this tiered even if hours are included Events should exist (or something very similar), but if you cannot find one that makes sense, please create the event Integration items: Ignore Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to fin...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Invoice Processing Rules",
    "Default Operational Parameters",
    "Post-Processing and Communication Workflows",
    "Integration and Event Handling",
    "Merchant-Specific Customization Requirements"
  ],
  "rules": [
    {
      "rule": "First 10k is included in tiered billing calculations",
      "category": "billing",
      "specificity": "general"
    },
    {
      "rule": "Tiered BT required for quantities over 100k claims at 0.09",
      "category": "billing",
      "specificity": "general"
    },
    {
      "rule": "Process additional support hours as separate unit BT (non-tiered even if hours are included)",
      "category": "billing",
      "specificity": "general"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "category": "defaults",
      "specificity": "general"
    },
    {
      "rule": "Every tax line item becomes a BT (if none listed)",
      "category": "tax_handling",
      "specificity": "general"
    },
    {
      "rule": "Events should exist or be created if none make sense",
      "category": "events",
      "specificity": "general"
    },
    {
      "rule": "Ignore integration items during initial processing",
      "category": "integration",
      "specificity": "general"
    },
    {
      "rule": "Implementation Success team fills post-go-live sections for Events, Integration Items, and Post Processing Communications",
      "category": "workflow",
      "specificity": "general"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration",
      "specificity": "example"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration",
      "specificity": "example"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific contract variations (e.g., back-dating invoice date to final day of month)",
      "context": "Processing specifics that differ by contract"
    },
    {
      "exception": "Support hours billing does not need to be tiered even if hours are included",
      "context": "Differs from standard tiered billing approach"
    },
    {
      "exception": "Integration items labeled differently based on merchant (Statsig vs Pinata example)",
      "context": "Merchant-specific labeling conventions"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "context": "Customer-specific invoice modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "SaaS fee billing with tiered usage commitments",
      "description": "Usage based on volume of data for warehouse or amount of product SKUs"
    },
    {
      "element": "HTML list monthly usage reporting",
      "description": "Engineering team sends HTML list that requires vlookup calculation for invoicing in QBO"
    },
    {
      "element": "Billing timing: Monthly in arrears",
      "description": "Specific billing frequency for this merchant"
    },
    {
      "element": "Notification requirements",
      "description": "Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase"
    },
    {
      "element": "Merchant temperament: Super nice and excited",
      "description": "Has been following Tabs on LinkedIn"
    },
    {
      "element": "Key features of interest",
      "description": "SF & QBO integrations, Contract ingestion, automated product creation, Usage calculations, Cash forecasting, ARR, Revrec, CARR needs"
    },
    {
      "element": "Invoice date back-dating",
      "description": "Example of merchant-specific request to back-date invoice date to final day of month"
    },
    {
      "element": "System diagram reference",
      "description": "Google presentation link for merchant's system architecture"
    }
  ],
  "confidence_score": 0.75
}
```

---

