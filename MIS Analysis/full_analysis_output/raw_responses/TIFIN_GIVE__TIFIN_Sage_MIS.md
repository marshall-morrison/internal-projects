# Raw LLM Analysis: TIFIN GIVE_ TIFIN Sage MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:49:46

---

## Chunk 1: TIFIN GIVE_ TIFIN Sage MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:49:46

### Original Content
```
Tab 1 https: docs google com spreadsheets d 1fAQ1rHf_buFcowql7ONgAj6gY01wd3u6nwM4ZAUxqhY edit gid 515133391 gid 515133391 Contract Processing Steps (Implementation Success to fill) DO NOT process the following customers: AssetMark, Ronald Blue Trust, GiveClear For contracts that look like the following, follow the steps below to process Steps to process Service Start Date: Will be noted as  initial term  or under a section that includes the  order form details  Months of Service: Default 36 mont...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow",
    "Default Values and Standardization",
    "Customer Exclusions and Exceptions",
    "Integration Item Categorization",
    "Billing Configuration Parameters"
  ],
  "rules": [
    {
      "rule": "DO NOT process contracts for AssetMark, Ronald Blue Trust, or GiveClear",
      "category": "customer_exclusions"
    },
    {
      "rule": "Service Start Date is found in 'initial term' or 'order form details' section",
      "category": "data_extraction"
    },
    {
      "rule": "Default Months of Service: 36 months (3 years) if no date specified",
      "category": "default_values"
    },
    {
      "rule": "Item Name: Copy and paste line next to item name field",
      "category": "data_entry"
    },
    {
      "rule": "Item Description: Leave as none",
      "category": "data_entry"
    },
    {
      "rule": "Billing type: Flat",
      "category": "billing_configuration"
    },
    {
      "rule": "Total Price: Verify if yearly cost or total contract cost; if total cost, look for annual fee",
      "category": "pricing_validation"
    },
    {
      "rule": "Quantity: Always set to 1",
      "category": "default_values"
    },
    {
      "rule": "Start Date: Same as service start date",
      "category": "date_mapping"
    },
    {
      "rule": "Periods: Default to 3",
      "category": "default_values"
    },
    {
      "rule": "Frequency: 1 year unless otherwise noted",
      "category": "default_values"
    },
    {
      "rule": "Net Terms: Default 30 days",
      "category": "default_values"
    },
    {
      "rule": "Ignore anything marked as 'waived' in contracts",
      "category": "exclusions"
    },
    {
      "rule": "Default Service Term: 3 Years",
      "category": "default_values"
    },
    {
      "rule": "Default Net Payment Terms: 30 days",
      "category": "default_values"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "category": "default_values"
    },
    {
      "rule": "Tax line items: Each tax line item becomes a BT Events Processing item (if none listed)",
      "category": "tax_handling"
    },
    {
      "rule": "TIFIN Netsuite Integration Items: Reference specific integration items list",
      "category": "integration_mapping"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_mapping"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_mapping"
    }
  ],
  "exceptions": [
    {
      "exception": "AssetMark, Ronald Blue Trust, and GiveClear customers must not be processed",
      "condition": "customer_name"
    },
    {
      "exception": "Billing Frequency can differ from monthly default if specified in contract",
      "condition": "contract_specification"
    },
    {
      "exception": "Frequency can differ from 1 year if otherwise noted in contract",
      "condition": "contract_specification"
    },
    {
      "exception": "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice date to final day of month)",
      "condition": "merchant_specific_request"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "condition": "merchant_override"
    },
    {
      "exception": "Items marked as 'waived' should be ignored/excluded from processing",
      "condition": "waived_status"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating to final day of month",
      "type": "custom_processing_rule",
      "note": "Example of merchant-specific processing that may differ by contract"
    },
    {
      "element": "Integration item categorization",
      "type": "configuration",
      "note": "Different merchants may have different integration items (Statsig, Pinata, etc.) with specific labeling requirements"
    },
    {
      "element": "TIFIN Netsuite Integration Items list",
      "type": "reference_data",
      "note": "Requires access to external reference list specific to merchant setup"
    },
    {
      "element": "Events billing information",
      "type": "optional_processing",
      "note": "Implementation Success team fills this if necessary for specific merchants"
    },
    {
      "element": "Service term variations",
      "type": "contract_terms",
      "note": "While default is 3 years, actual term may vary by merchant contract"
    }
  ],
  "confidence_score": 0.85
}
```

---

