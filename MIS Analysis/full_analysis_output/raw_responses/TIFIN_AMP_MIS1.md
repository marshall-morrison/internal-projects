# Raw LLM Analysis: TIFIN AMP MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:55:14

---

## Chunk 1: TIFIN AMP MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:14

### Original Content
```
Tab 1 Contract Processing Steps (Implementation Success to fill) Contract may include the following: Setup Fee Initial fee credited against the first month Remaining license fees Steps to process SETUP FEE If there is a setup fee listed, like the screenshot below, follow the steps to process: Service Start Date: Search for  effective date  Months of Service: Will be listed in term Item Name: Setup Fee Item Description: none Integration Item: TIFIN Netsuite Integration Items find here Billing typ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow",
    "Fee Structure and Billing Configuration",
    "Service Term and Payment Timeline Management",
    "Integration Item Assignment and Categorization",
    "Default Values and Operational Standards"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Setup Fee Processing",
      "description": "Setup fees must be processed with specific parameters: Service Start Date from effective date, Months of Service from term, Item Name as 'Setup Fee', Integration Item as 'TIFIN Netsuite Integration Items', Billing type as 'Flat', Quantity as 1, Frequency as 'NONE', Net Terms as 0, Periods as null"
    },
    {
      "rule_id": "R2",
      "category": "Initial Fee Credit Processing",
      "description": "When initial fee is credited against first month: Item Name is 'License', Billing type is 'Flat', Discount equals the initial fee amount, Quantity is 1, Periods is 1, Frequency is '1 month', Net Terms is 30"
    },
    {
      "rule_id": "R3",
      "category": "Remaining License Fees",
      "description": "Monthly licenses processed with: Item Name as 'Licenses', Billing type as 'Flat', Quantity as 1, Start Date as ONE MONTH AFTER contract start date, Periods as contract length minus one month (e.g., 11 for one year contract), Frequency as 'monthly', Net Terms as 30"
    },
    {
      "rule_id": "R4",
      "category": "Default Service Term",
      "description": "If no service term is listed in contract, operational default is 1 Year"
    },
    {
      "rule_id": "R5",
      "category": "Default Net Payment Terms",
      "description": "If no net payment terms specified, operational default is 0"
    },
    {
      "rule_id": "R6",
      "category": "Default Billing Frequency",
      "description": "If no billing frequency listed, operational default is Monthly"
    },
    {
      "rule_id": "R7",
      "category": "Tax Line Items",
      "description": "If not specified, operational default is that every tax line item becomes a BT (Billing Transaction)"
    },
    {
      "rule_id": "R8",
      "category": "Integration Item Assignment",
      "description": "All integration items must be assigned according to TIFIN Netsuite Integration Items guidelines"
    },
    {
      "rule_id": "R9",
      "category": "Integration Item - Statsig",
      "description": "All Statsig integration items should be labeled as 'Sales'"
    },
    {
      "rule_id": "R10",
      "category": "Integration Item - Pinata",
      "description": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Merchant-specific processing requests may differ by contract (e.g., always back-date invoice date to final day of the month)",
      "condition": "When merchant has specific processing requirements documented in contract"
    },
    {
      "exception_id": "E2",
      "description": "Pinata integration items can have different labels if specifically noted by Merchant",
      "condition": "When merchant explicitly requests different labeling for Pinata items"
    },
    {
      "exception_id": "E3",
      "description": "Contract items to ignore based on specific merchant requirements",
      "condition": "When contract contains items that merchant has requested to exclude from processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice Date Backdating",
      "description": "Some merchants may request specific invoice date handling (e.g., backdating to final day of month)",
      "customization_required": true
    },
    {
      "element": "Integration Item Labeling",
      "description": "Integration item categories may vary by merchant (Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "customization_required": true
    },
    {
      "element": "Contract Items to Ignore",
      "description": "Specific contract elements to exclude from processing vary by merchant requirements",
      "customization_required": true
    },
    {
      "element": "Events Billing Processing",
      "description": "Important information on events billing needs to be filled by Implementation Success team on per-merchant basis",
      "customization_required": true
    },
    {
      "element": "Service Start Date Calculation",
      "description": "Effective date search and interpretation may vary based on contract format",
      "customization_required": false
    }
  ],
  "confidence_score": 0.85
}
```

---

