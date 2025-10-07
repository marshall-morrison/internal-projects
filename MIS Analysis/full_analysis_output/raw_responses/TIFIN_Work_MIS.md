# Raw LLM Analysis: TIFIN @ Work MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:22:29

---

## Chunk 1: TIFIN @ Work MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:22:29

### Original Content
```
Tab 1 Contract Processing Steps (Implementation Success to fill) For contracts that look like the following, follow the steps below to process Be sure to scroll down to the order form to view the information since it typically does not live on the first page Contracts will typically include the following Garage processing example Included Seats Additional Seats Per Active Employee Per Month IMAGE 1 1 IMAGE 1 2 Steps to process You will have to create Different Revenue Schedules for Each type of ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow",
    "Revenue Schedule Creation and Configuration",
    "Multi-tier Pricing Structure Management",
    "Billing and Payment Terms Standardization",
    "NetSuite Integration Data Mapping"
  ],
  "rules": [
    "Scroll down to order form to view complete contract information (typically not on first page)",
    "Create separate revenue schedules for each type of charge",
    "Default service term is 36 months (3 years)",
    "Default billing frequency is Monthly for Per Seat Subscription",
    "Default Net Terms is 30 days",
    "Default periods is 36 if monthly billing",
    "Service Start Date must match Term start date from contract",
    "Start Date for revenue schedule must be same as service start date",
    "Integration Item must be set to 'TIFIN Netsuite Integration Items' for all schedules",
    "REV SCHEDULE 1 (Included Seats): Billing type = Flat, Quantity = 1, Item Name and Description from contract Image 1.1",
    "REV SCHEDULE 2 (Additional Seats): Billing type = UNIT, Event to track = 'Additional Seat', Item Description = Blank",
    "REV SCHEDULE 3 (Per Active Employee Per Month): Billing type = UNIT, Event to track = 'PAPM', Item Description = Blank",
    "Total Price must be extracted from contract for each revenue schedule",
    "Ignore any items marked as 'waived' in contracts"
  ],
  "exceptions": [
    "Billing frequency may differ if explicitly stated otherwise in contract (override Monthly default)",
    "Item naming conventions may vary per contract (e.g., 'Additional Seat or Other naming convention shared')",
    "Merchant may request specific processing variations that differ by contract",
    "Periods default may change if billing is not monthly"
  ],
  "merchant_specific": [
    "Garage processing example referenced as template",
    "TIFIN NetSuite Integration Items (specific integration system)",
    "Event tracking terminology: 'Additional Seat' and 'PAPM' (Per Active Employee Per Month)",
    "Three-tier pricing model: Included Seats, Additional Seats, Per Active Employee",
    "Specific contract layout with Image 1.1 and Image 1.2 references",
    "Implementation Success team responsible for filling contract processing steps",
    "Merchant-specific processing requests that may vary by contract"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: TIFIN @ Work MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:22:31

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term Default 3 Years Default Net Payment Terms Default 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the in...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and billing configuration defaults",
    "Tax handling and line item processing",
    "Events billing procedures",
    "Integration items labeling and categorization",
    "Payment terms and service agreements"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "invoicing",
      "mandatory": true
    },
    {
      "rule": "Default service term is 3 years",
      "category": "service_terms",
      "mandatory": false
    },
    {
      "rule": "Default net payment terms is 30 days",
      "category": "payment_terms",
      "mandatory": false
    },
    {
      "rule": "Default billing frequency is monthly when none is listed",
      "category": "billing_frequency",
      "mandatory": false
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default when not specified",
      "category": "tax_processing",
      "mandatory": false
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling",
      "mandatory": true,
      "merchant": "Statsig"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_labeling",
      "mandatory": true,
      "merchant": "Pinata"
    }
  ],
  "exceptions": [
    {
      "exception": "Billing frequency defaults can be overridden if explicitly listed by merchant",
      "applies_to": "billing_frequency"
    },
    {
      "exception": "Tax line item handling can be specified differently if merchant provides instructions",
      "applies_to": "tax_processing"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "applies_to": "integration_labeling"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing processing",
      "customization_required": true,
      "owner": "Implementation Success team",
      "description": "Requires merchant-specific information on events billing if necessary"
    },
    {
      "element": "Integration items assignment instructions",
      "customization_required": true,
      "owner": "Implementation Success team",
      "description": "Specific labeling rules vary by integration partner (e.g., Statsig, Pinata)"
    },
    {
      "element": "TIFIN Netsuite Integration Items",
      "customization_required": true,
      "description": "Integration-specific labeling conventions that may vary by merchant and integration type"
    },
    {
      "element": "Service terms, payment terms, and billing frequency",
      "customization_required": false,
      "description": "Have operational defaults but can be customized per merchant agreement"
    }
  ],
  "confidence_score": 0.85
}
```

---

