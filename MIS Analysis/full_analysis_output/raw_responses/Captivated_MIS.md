# Raw LLM Analysis: Captivated MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:59:55

---

## Chunk 1: Captivated MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:59:55

### Original Content
```
Merchant Name: Captivated Works Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General In the description of line items, there will be usage BTs and tier unit BTs...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Line Item Configuration",
    "Billing Models and Payment Terms",
    "Usage-Based and Tiered Billing Structures",
    "Merchant Onboarding and Implementation Workflow",
    "Post-Processing Communication and Customer Management"
  ],
  "rules": [
    {
      "rule": "Item Quantity defaults to 1 if not listed in contract",
      "category": "Line Item Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Service Start Date uses contract signature or start date",
      "category": "Line Item Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Billing Start Date must match Service Start Date",
      "category": "Line Item Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Default to 12 months for Months of Service if no total length available",
      "category": "Service Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Month-to-month contracts should assume 12 months",
      "category": "Service Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Net Terms default to net 30 if not listed",
      "category": "Payment Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed (Ops Default)",
      "category": "Service Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 if none listed (Ops Default)",
      "category": "Payment Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed (Ops Default)",
      "category": "Billing Frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Thing) if none listed (Ops Default)",
      "category": "Tax Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Usage BTs should be billed Monthly (monthly price typically listed)",
      "category": "Usage Billing",
      "specificity": "explicit"
    },
    {
      "rule": "Annual subscriptions use 1 year frequency",
      "category": "Billing Frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Multi-year subscriptions (e.g., 3 years) use corresponding frequency if charged upfront",
      "category": "Billing Frequency",
      "specificity": "explicit"
    },
    {
      "rule": "For events with included amounts, create tier unit BT using quantity included; anything over charged at specified rate",
      "category": "Tiered Billing",
      "specificity": "explicit"
    },
    {
      "rule": "Ignore Late fees in contract processing",
      "category": "Contract Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Use line item name for Item Name",
      "category": "Line Item Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Item Description defaults to none",
      "category": "Line Item Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Total Price uses subtotal listed for each line item",
      "category": "Line Item Processing",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Month-to-month contracts treated as 12-month terms despite variable nature",
      "context": "Service term calculation"
    },
    {
      "exception": "Contracts may have specific processing requests that differ by contract (e.g., back-dating invoice dates)",
      "context": "Merchant-specific processing variations"
    },
    {
      "exception": "Late fees should be ignored during contract processing",
      "context": "Line item exclusions"
    },
    {
      "exception": "Tier unit BTs only created for events with included amounts; overage charged separately",
      "context": "Usage-based billing"
    },
    {
      "exception": "Integration items may have specific labeling requirements per merchant (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "context": "Integration item processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Captivated Works",
      "type": "Identifier",
      "customizable": true
    },
    {
      "element": "Implementation POC and CX POC fields",
      "type": "Contact Information",
      "customizable": true
    },
    {
      "element": "Billing model: Annual flat fee and usage billed monthly",
      "type": "Billing Structure",
      "customizable": true
    },
    {
      "element": "Merchant temperament: Bryan (CEO) is super friendly, family-oriented",
      "type": "Relationship Notes",
      "customizable": true
    },
    {
      "element": "Key stakeholder: CEO's daughter heads up billing",
      "type": "Contact Information",
      "customizable": true
    },
    {
      "element": "Feature priorities: Flexible billing, disliked Maxio for being too rigid",
      "type": "Product Requirements",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements (who, where, when)",
      "type": "Communication Protocol",
      "customizable": true
    },
    {
      "element": "Customer-specific information (special memos, invoice changes)",
      "type": "Customer Management",
      "customizable": true
    },
    {
      "element": "Integration item labeling rules (Statsig, Pinata examples)",
      "type": "Integration Processing",
      "customizable": true
    },
    {
      "element": "Contract-specific processing variations",
      "type": "Processing Rules",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

