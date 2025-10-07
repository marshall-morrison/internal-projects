# Raw LLM Analysis: TIFIN @ Work MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:38:20

---

## Chunk 1: TIFIN @ Work MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:20

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
    "NetSuite Integration and Data Mapping"
  ],
  "rules": [
    "Scroll down to order form to view complete contract information (not on first page)",
    "Create separate revenue schedules for each type of charge",
    "Default service term is 36 months (3 years)",
    "Default billing frequency is Monthly for Per Seat Subscription",
    "Default Net Terms is 30 days",
    "Default periods is 36 if monthly billing",
    "Service Start Date must match Term start date from contract",
    "Start Date for revenue schedule must match service start date",
    "Integration Item must be set to 'TIFIN Netsuite Integration Items' for all schedules",
    "Included Seats: Billing type is 'Flat', Quantity is 1",
    "Additional Seats: Billing type is 'UNIT'",
    "Per Active Employee Per Month (PAPM): Billing type is 'UNIT'",
    "Item Name and Item Description must reference contract details (Image 1.1)",
    "Total Price must be extracted from contract for each charge type",
    "Additional Seats requires Event to track: 'Additional Seat'",
    "PAPM requires Event to track: 'PAPM'",
    "Ignore any items marked as 'waived' in contracts"
  ],
  "exceptions": [
    "Billing frequency may differ from Monthly 'unless otherwise stated' in contract",
    "Item naming conventions may vary ('Additional Seat or Other naming convention shared', 'Per Active Employee Per Month or Other naming convention shared')",
    "Merchant may request specific processing differences by contract",
    "Item Description is blank for Additional Seats and PAPM schedules (unlike Included Seats which references Image 1.1)"
  ],
  "merchant_specific": [
    "Garage processing example used as reference template",
    "TIFIN NetSuite Integration Items (specific integration system)",
    "Contract layout and image references (Image 1.1, Image 1.2) may vary by merchant",
    "Specific pricing tiers: Included Seats, Additional Seats, Per Active Employee Per Month",
    "Event tracking terminology: 'Additional Seat' and 'PAPM'",
    "Document notes 'Specifics processing things the merchant has requested that may differ by contract' indicating customization requirements",
    "Implementation Success team responsible for filling/processing"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: TIFIN @ Work MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:21

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term Default 3 Years Default Net Payment Terms Default 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the in...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Configuration and Defaults",
    "Payment and Billing Terms",
    "Tax Line Item Processing",
    "Events and Integration Items Management",
    "Netsuite Integration Labeling"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default service term is 3 years",
      "category": "Service Terms",
      "explicit": true
    },
    {
      "rule": "Default net payment terms is 30 days",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly when none is listed",
      "category": "Billing Frequency",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) when no instruction is listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling events billing information when necessary",
      "category": "Events Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling integration items instructions when necessary",
      "category": "Integration Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by the merchant",
      "applies_to": "Integration Labeling"
    },
    {
      "exception": "Defaults only apply 'If None Listed' - merchant-specific instructions override defaults",
      "applies_to": "All Default Settings"
    },
    {
      "exception": "Events processing is conditional and only performed 'if necessary'",
      "applies_to": "Events Billing"
    },
    {
      "exception": "Integration items processing is conditional and only performed 'if necessary'",
      "applies_to": "Integration Items"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing information",
      "customization_type": "Implementation Success to provide merchant-specific details",
      "variability": "high"
    },
    {
      "element": "Integration items assignment instructions",
      "customization_type": "Merchant-specific labeling rules (e.g., Statsig, Pinata)",
      "variability": "high"
    },
    {
      "element": "Tax line item handling",
      "customization_type": "May vary from default BT processing based on merchant requirements",
      "variability": "medium"
    },
    {
      "element": "Billing frequency",
      "customization_type": "Can override monthly default if merchant specifies",
      "variability": "medium"
    },
    {
      "element": "Service term length",
      "customization_type": "Can override 3-year default",
      "variability": "medium"
    },
    {
      "element": "Payment terms",
      "customization_type": "Can override Net 30 default",
      "variability": "medium"
    },
    {
      "element": "TIFIN Netsuite Integration Items",
      "customization_type": "Merchant-specific integration naming and categorization",
      "variability": "high"
    }
  ],
  "confidence_score": 0.85
}
```

---

