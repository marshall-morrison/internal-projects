# Raw LLM Analysis: Merchant Info Sheet - Pinata

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:34:58

---

## Chunk 1: Merchant Info Sheet - Pinata_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:34:58

### Original Content
```
g 1,000 item with a 30  discount, please process as  1,000 for BT 1 and - 300 for BT 2) For QBO integration items please default to  Software Subscription Bundle  for all BTs unless told otherwise For add ons to existing contracts or amendments Please set the billing cadence the same as the MSA Prorate the first invoice of the amendment on the signature date of amendment until the period of the next invoice of MSA Then ensure all amendments addons are charged on the same day and payment terms as...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing procedures",
    "Contract management and amendments",
    "QBO (QuickBooks Online) integration and item categorization",
    "Customer setup and payment configuration",
    "Events processing and partnership billing"
  ],
  "rules": [
    "For discounted items: process full amount on BT 1 and negative discount amount on BT 2 (e.g., $1,000 item with 30% discount = $1,000 for BT 1 and -$300 for BT 2)",
    "For QBO integration items: default to 'Software Subscription Bundle' for all BTs unless specified otherwise",
    "For add-ons/amendments: set billing cadence to match the MSA (Master Service Agreement)",
    "Prorate first invoice of amendment from signature date until next MSA invoice period",
    "All amendments and add-ons must be charged on same day and payment terms as original MSA",
    "All recurring charges should be on same cadence on one invoice per occurrence",
    "DO NOT include professional services and custom development from contract fine print",
    "Price Name field must be left blank - NEVER INPUT A PRICE NAME",
    "For month-to-month contracts with no term: default to 1 year term",
    "Default to Net 0 payment terms unless contract specifies otherwise",
    "Events processing data sent via Slack to 'pinata-ext' or by email in written format",
    "Partnerships are NOT billed as events-based billing - bill as flat billing",
    "Set all new customers and customers without prior contracts to 'auto-charge'",
    "For customers: only select the parent customer"
  ],
  "exceptions": [
    "QBO item categorization can differ from 'Software Subscription Bundle' if explicitly told otherwise",
    "Payment terms can differ from Net 0 if noted on contract",
    "Partnerships are excluded from events-based billing model despite events processing being available",
    "Professional services and custom development are excluded from billing despite being in contract fine print"
  ],
  "merchant_specific": [
    "BT 1 and BT 2 terminology (likely billing tiers or billing types)",
    "QBO integration and 'Software Subscription Bundle' category",
    "MSA (Master Service Agreement) contract structure",
    "Slack channel 'pinata-ext' for events processing",
    "Auto-charge payment configuration",
    "Parent customer selection hierarchy",
    "Events processing workflow and data structure transition",
    "Specific discount processing methodology (split between BT 1 and BT 2)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Pinata_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:35:00

### Original Content
```
Merchant Scoping start date: Jun 7, 2023 Implementation Completed Date (Go live date): Jan 1, 2024 MSA Signature Date: Jan 29, 2024 GTM POC: ERP: (Currently QBO, moving to Rillet) Tax Integration: Key people at Merchant [Primary] Head of Finance: Heath Ritchie  heath gopinata com  COO: Rob Olson  rob gopinata com  Company summary PINATA provides operational software designed for task management, primarily in the food and beverage industry It enables businesses to efficiently manage and optimize ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship management and key stakeholder information",
    "Multi-faceted billing model with usage-based, user-based, and recurring components",
    "Contract processing procedures and documentation requirements",
    "Implementation timeline and system integration details",
    "Special handling instructions for discounts and effective dates"
  ],
  "rules": [
    {
      "rule": "Follow all comments in contracts",
      "type": "explicit",
      "category": "contract_processing"
    },
    {
      "rule": "Effective Date must be printed below the Pinata address at the bottom of the contract",
      "type": "explicit",
      "category": "contract_documentation",
      "effective_date": "4/11 update"
    },
    {
      "rule": "Specify if the effective date is different from the DocuSign date on the final page",
      "type": "explicit",
      "category": "contract_documentation"
    },
    {
      "rule": "Process discounts as 2 BTs (billing transactions): one with original price, second with discounted amount",
      "type": "explicit",
      "category": "discount_processing",
      "effective_date": "4/19 update"
    },
    {
      "rule": "Contracts must include usage-based, user-based, recurring SaaS, and/or implementation fee components",
      "type": "implicit",
      "category": "billing_structure"
    }
  ],
  "exceptions": [
    {
      "exception": "Effective date may differ from DocuSign signature date",
      "condition": "When specified, effective date should be clearly marked below merchant address",
      "handling": "Print effective date separately to distinguish from signature date"
    },
    {
      "exception": "Discount processing requires special handling",
      "condition": "When discounts are applied",
      "handling": "Create two separate billing transactions instead of one net amount"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key stakeholders",
      "details": "Heath Ritchie (Head of Finance, Primary Contact), Rob Olson (COO)",
      "customization_needed": true
    },
    {
      "element": "Billing model composition",
      "details": "Usage-based (reports/events), User-based, Recurring SaaS, Implementation fee",
      "customization_needed": true,
      "note": "Not all merchants will have all components"
    },
    {
      "element": "Industry-specific terminology",
      "details": "Reports (aka events based) - specific to Pinata's platform",
      "customization_needed": true
    },
    {
      "element": "ERP system",
      "details": "Currently QBO, moving to Rillet",
      "customization_needed": true
    },
    {
      "element": "Implementation timeline",
      "details": "Scoping: Jun 7, 2023; Go-live: Jan 1, 2024; MSA: Jan 29, 2024",
      "customization_needed": true
    },
    {
      "element": "Relationship notes",
      "details": "Early adopter, former software engineer, understanding of bugs, supportive",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

