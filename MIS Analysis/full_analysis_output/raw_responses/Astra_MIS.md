# Raw LLM Analysis: Astra MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:37:42

---

## Chunk 1: Astra MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:37:42

### Original Content
```
io call id 1144396161279514880 account-id 4213540540444994996 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills They have an internal system to create and calc invoices (very complex) - interchange components - platform - license - chargeback Tabs will be ingesting their invoices as  contracts  to then essentially copy the invoices and send out of Tabs 1) What is the merchant temperament Nice and collaborative Sam- a bit dryer Zac...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Complex invoicing and billing system integration",
    "Merchant relationship and stakeholder management",
    "Product feature prioritization and use cases",
    "Contract and invoice data ingestion workflow",
    "Payment processing and financial operations"
  ],
  "rules": [
    "Invoices must be ingested into Tabs as 'contracts' before being copied and sent out",
    "Invoice calculations include multiple components: interchange, platform, license, and chargeback",
    "Merchant uses internal system for invoice creation and calculation (not Tabs native)",
    "Implementation team is DRI (Directly Responsible Individual) for completion upon handoff",
    "AE (Account Executive) responsible for filling Notes Sections if available"
  ],
  "exceptions": [
    "This merchant has a 'very complex' internal invoicing system that requires special handling",
    "Standard Tabs invoicing workflow is modified - invoices are ingested rather than created natively",
    "Invoice components are non-standard and include specialized financial elements (interchange, platform, license, chargeback)"
  ],
  "merchant_specific": [
    "Account ID: 4213540540444994996",
    "Call ID: 1144396161279514880",
    "Key contacts: Sam (described as 'a bit dryer'), Zach (described as 'great')",
    "Merchant temperament: 'Nice and collaborative'",
    "Primary purchase drivers: Cash App integration and dunning functionality",
    "Secondary priority: Revenue recognition (rev rec)",
    "Custom invoice components: interchange, platform, license, chargeback tabs",
    "Workflow: Ingest invoices as contracts → copy → send out of Tabs"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Astra MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:37:53

### Original Content
```
Merchant Name: Astra Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General All contracts will generally be invoices with flat BTs Pay attention to how line items...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Invoice Processing Workflow",
    "Billing Terms and Line Item Configuration",
    "Merchant Implementation and Onboarding",
    "Stakeholder Communication and Notifications",
    "Integration and Customer-Specific Handling"
  ],
  "rules": [
    {
      "rule": "All contracts will generally be invoices with flat BTs (Billing Terms)",
      "category": "contract_processing"
    },
    {
      "rule": "Quantity: use the count column if available; otherwise, use 1",
      "category": "line_item_processing"
    },
    {
      "rule": "Total Price: Use the total listed for that line item",
      "category": "line_item_processing"
    },
    {
      "rule": "Process negative amounts (e.g., User Fees credits) as negative BT",
      "category": "line_item_processing"
    },
    {
      "rule": "Process $0 BTs (zero-value billing terms)",
      "category": "line_item_processing"
    },
    {
      "rule": "Service Start Date and Billing Start Date: Use the first of the month for whatever the date of the invoice is",
      "category": "date_handling",
      "example": "If invoice date is July 27, 2025, use July 1, 2025 as start date"
    },
    {
      "rule": "Months of Service: Always 1 month for monthly invoices",
      "category": "billing_period"
    },
    {
      "rule": "Frequency: Month (monthly billing frequency)",
      "category": "billing_frequency"
    },
    {
      "rule": "Net Terms: use net 0 (immediate payment)",
      "category": "payment_terms"
    },
    {
      "rule": "If totals aren't matching up, create an additional BT for the difference called 'Additional Fee'",
      "category": "reconciliation"
    },
    {
      "rule": "Pay attention to how line items total up to make sure that the total in Garage lines up with the total on the invoice",
      "category": "validation"
    }
  ],
  "exceptions": [
    {
      "exception": "Negative line items (credits) should be processed as negative BT rather than standard positive amounts",
      "condition": "When line item total is negative (e.g., User Fees credits)"
    },
    {
      "exception": "Use quantity of 1 as fallback when count column is not available",
      "condition": "When count column is missing or unavailable"
    },
    {
      "exception": "Create 'Additional Fee' BT for reconciliation differences",
      "condition": "When line item totals don't match invoice total"
    },
    {
      "exception": "Integration items may have different labels based on merchant type",
      "condition": "Merchant-specific integration labeling (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Astra",
      "type": "merchant_identifier",
      "customizable": true
    },
    {
      "element": "Implementation POC and CX POC fields",
      "type": "stakeholder_assignment",
      "customizable": true,
      "note": "To be filled by Implementation team"
    },
    {
      "element": "Billing model section",
      "type": "billing_configuration",
      "customizable": true,
      "includes": ["Customer creation process", "How merchant bills", "Contract structure", "One-off merchant specifics"]
    },
    {
      "element": "Events Processing section",
      "type": "events_billing",
      "customizable": true,
      "conditional": "if necessary"
    },
    {
      "element": "Integration Items Processing",
      "type": "integration_configuration",
      "customizable": true,
      "note": "Instructions for assigning integration items vary by merchant (e.g., Statsig, Pinata examples provided)"
    },
    {
      "element": "Post Processing Communications",
      "type": "notification_workflow",
      "customizable": true,
      "includes": ["Who to notify", "Where to notify", "When to notify"],
      "example": "Customer Success notification in merchant channel when contracts processed"
    },
    {
      "element": "Customer Information section",
      "type": "customer_specifics",
      "customizable": true,
      "includes": ["Special memos", "Invoice changes", "Customer relationship specifics"]
    },
    {
      "element": "Feature Requests tracking",
      "type": "enhancement_tracking",
      "customizable": true,
      "fields": ["What is it", "Why it's important", "Urgency"]
    },
    {
      "element": "Merchant Calls with Gong links",
      "type": "documentation_reference",
      "customizable": true,
      "note": "Different stakeholders fill at different phases (AE, Implementation, Success)"
    }
  ],
  "confidence_score": 0.85
}
```

---

