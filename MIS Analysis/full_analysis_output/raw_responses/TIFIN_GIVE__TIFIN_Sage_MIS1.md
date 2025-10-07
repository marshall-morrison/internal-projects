# Raw LLM Analysis: TIFIN GIVE_ TIFIN Sage MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:21:39

---

## Chunk 1: TIFIN GIVE_ TIFIN Sage MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:21:39

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
    "Customer Exclusions and Special Handling",
    "Integration Item Classification",
    "Billing Configuration and Terms"
  ],
  "rules": [
    {
      "rule": "DO NOT process contracts for: AssetMark, Ronald Blue Trust, GiveClear",
      "category": "exclusions"
    },
    {
      "rule": "Service Start Date: Extract from 'initial term' or 'order form details' section",
      "category": "data_extraction"
    },
    {
      "rule": "Months of Service: Default to 36 months (3 years) if no date specified",
      "category": "defaults"
    },
    {
      "rule": "Item Name: Copy and paste line next to item name field",
      "category": "data_extraction"
    },
    {
      "rule": "Item Description: Leave as none",
      "category": "data_entry"
    },
    {
      "rule": "Integration Item: Use TIFIN Netsuite Integration Items reference",
      "category": "integration"
    },
    {
      "rule": "Billing type: Set as Flat",
      "category": "billing"
    },
    {
      "rule": "Total Price: Verify if yearly cost or total contract cost; look for annual fee if total cost",
      "category": "pricing"
    },
    {
      "rule": "Quantity: Default to 1",
      "category": "defaults"
    },
    {
      "rule": "Start Date: Same as service start date",
      "category": "dates"
    },
    {
      "rule": "Periods: Default to 3",
      "category": "defaults"
    },
    {
      "rule": "Frequency: Default to 1 year unless otherwise noted",
      "category": "billing"
    },
    {
      "rule": "Net Terms: Default to 30 days",
      "category": "payment_terms"
    },
    {
      "rule": "Ignore any items marked as 'waived' in contracts",
      "category": "exclusions"
    },
    {
      "rule": "Default Service Term: 3 Years",
      "category": "defaults"
    },
    {
      "rule": "Default Net Payment Terms: 30 days",
      "category": "defaults"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "category": "defaults"
    },
    {
      "rule": "Tax line items: Each tax line item becomes a BT Events Processing item (if none listed)",
      "category": "tax_handling"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration"
    },
    {
      "rule": "All 'Pinata' integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration"
    }
  ],
  "exceptions": [
    {
      "exception": "Excluded customers: AssetMark, Ronald Blue Trust, GiveClear - do not process their contracts",
      "condition": "customer_identity"
    },
    {
      "exception": "Waived items in contracts should be ignored",
      "condition": "item_status"
    },
    {
      "exception": "Total Price may be yearly or total contract cost - requires verification and adjustment",
      "condition": "pricing_structure"
    },
    {
      "exception": "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice dates)",
      "condition": "merchant_preferences"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "condition": "merchant_override"
    },
    {
      "exception": "Billing frequency can be overridden if specified in contract (default is monthly)",
      "condition": "contract_specification"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer exclusion list (AssetMark, Ronald Blue Trust, GiveClear)",
      "customization_type": "customer_blacklist"
    },
    {
      "element": "Integration item labeling (Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "customization_type": "integration_mapping"
    },
    {
      "element": "Invoice date back-dating to final day of month",
      "customization_type": "date_handling"
    },
    {
      "element": "TIFIN Netsuite Integration Items reference document",
      "customization_type": "integration_reference"
    },
    {
      "element": "Merchant-requested processing specifics that may differ by contract",
      "customization_type": "processing_rules"
    },
    {
      "element": "Events billing information and handling",
      "customization_type": "billing_configuration"
    }
  ],
  "confidence_score": 0.85
}
```

---

