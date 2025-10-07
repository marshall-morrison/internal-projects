# Raw LLM Analysis: Alaffia Health MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:40:06

---

## Chunk 1: Alaffia Health MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:40:06

### Original Content
```
Merchant Name (AE to fill) Alaffia Health https: app hubspot com contacts 43610657 record 0-3 33176016401  Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Usage-Based Fee Structures and Savings Calculations",
    "Implementation Timeline and Service Terms",
    "Merchant-Specific Business Model (Healthcare Claims Review)",
    "Cross-Functional Communication and Handoff Procedures"
  ],
  "rules": [
    {
      "rule": "Most contracts will have usage fees that are a percentage of realized savings",
      "category": "billing"
    },
    {
      "rule": "Each Business Type (BT) with percentage of savings must have a unique event",
      "category": "contract_processing"
    },
    {
      "rule": "Process discounts as a separate negative BT unless it is for a specific item, then use in-line discounting",
      "category": "contract_processing"
    },
    {
      "rule": "Service Start Date equals order effective date",
      "category": "service_terms"
    },
    {
      "rule": "Months of Service found in 'Term Project Schedule' or 'Initial Term', default to 2 months for implementation",
      "category": "service_terms"
    },
    {
      "rule": "Billing Start Date is same as service start date",
      "category": "billing"
    },
    {
      "rule": "Usage BTs will be monthly in arrears unless stated otherwise",
      "category": "billing_frequency"
    },
    {
      "rule": "Default net payment terms: 30 days (look for clause about payment within 30 calendar days following receipt of invoice)",
      "category": "payment_terms"
    },
    {
      "rule": "If no service term listed, Ops default is 1 Year",
      "category": "defaults"
    },
    {
      "rule": "If no net payment terms listed, Ops default is 0 days",
      "category": "defaults"
    },
    {
      "rule": "If no billing frequency listed, Ops default is Monthly",
      "category": "defaults"
    },
    {
      "rule": "If no tax handling specified, every tax line item becomes a BT",
      "category": "defaults"
    },
    {
      "rule": "Use unique names for item names if BTs are similar; make generic names more specific",
      "category": "naming_conventions"
    },
    {
      "rule": "Ignore any 'Administrative Allowance' items",
      "category": "contract_processing"
    },
    {
      "rule": "If implementation is comprised of multiple BTs, process all individually",
      "category": "contract_processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Alaffia Health has two different percentage rates based on claim review type",
      "details": "Pre-Payment Claim Reviews: 30% of Realized Savings; Post-Payment Claim Reviews: 35% of Realized Savings"
    },
    {
      "exception": "Client only pays Service Fee when prevented overpayments (pre-payment) or retracted overpayments (post-payment) have occurred",
      "details": "Payment is contingent on actual savings realization"
    },
    {
      "exception": "Some parent-child relationships exist with healthcare companies and their subsidiaries",
      "details": "Special customer hierarchy considerations needed"
    },
    {
      "exception": "Upfront platform fee exists in addition to usage-based claims fees",
      "details": "Hybrid billing model with fixed and variable components"
    },
    {
      "exception": "Usage fees are monthly in arrears unless stated otherwise",
      "details": "Allows for contract-specific billing timing variations"
    },
    {
      "exception": "Discounts processed as separate negative BT unless for specific item",
      "details": "Two different discount handling methods based on specificity"
    }
  ],
  "merchant_specific": [
    {
      "element": "Claims review process workflow",
      "description": "Customer sends claims list → Alaffia reviews → finds savings → customer signs off → invoice generated"
    },
    {
      "element": "Dual percentage-based fee structure",
      "description": "30% for pre-payment reviews, 35% for post-payment reviews"
    },
    {
      "element": "Healthcare industry focus",
      "description": "Insurance claims review, healthcare companies with subsidiaries"
    },
    {
      "element": "Merchant temperament",
      "description": "Straightforward, metrics driven"
    },
    {
      "element": "Key features prioritized",
      "description": "QBO connection, reducing DSO (collections), usage calculations on invoices"
    },
    {
      "element": "Realized savings dependency",
      "description": "Billing only occurs when actual savings are prevented or retracted"
    },
    {
      "element": "Parent-child customer relationships",
      "description": "Healthcare companies and their subsidiaries require special handling"
    },
    {
      "element": "Platform fee plus usage model",
      "description": "Upfront platform fee combined with claims-based usage fees"
    },
    {
      "element": "Customer sign-off requirement",
      "description": "Customer must approve realized savings before invoicing"
    }
  ],
  "confidence_score": 0.85
}
```

---

