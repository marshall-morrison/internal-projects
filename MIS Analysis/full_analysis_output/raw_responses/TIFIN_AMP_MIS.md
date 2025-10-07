# Raw LLM Analysis: TIFIN AMP MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:10:21

---

## Chunk 1: TIFIN AMP MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:21

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
    "Service Term and Payment Configuration",
    "Integration Item Assignment",
    "Default Values and Fallback Rules"
  ],
  "rules": [
    "Setup fees must have Service Start Date matching the contract effective date",
    "Setup fees use Billing type: Flat, Quantity: 1, Frequency: NONE, Net Terms: 0, Periods: null",
    "Setup fees use Item Name: 'Setup Fee' with Integration Item: TIFIN Netsuite Integration Items",
    "Initial fee credited against first month uses Item Name: 'License' with Periods: 1, Frequency: 1 month, Net Terms: 30",
    "Initial fee discount amount equals the initial fee price",
    "Remaining license fees use Item Name: 'Licenses' with Billing type: Flat, Quantity: One, Frequency: monthly, Net Terms: 30",
    "Remaining license fees start date is ONE MONTH AFTER the contract start date",
    "Remaining license fees Periods = contract length minus one month (e.g., 11 for one year contract)",
    "Default Service Term is 1 Year if none listed",
    "Default Net Payment Terms is 0 if none listed",
    "Default Billing Frequency is Monthly if none listed",
    "Every tax line item becomes a BT (Billing Type) Events Processing item",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
  ],
  "exceptions": [
    "Merchant may request specific processing that differs by contract (e.g., always back-date invoice date to final day of the month)",
    "Pinata integration items can have different labels if specifically noted by Merchant",
    "Contract-specific variations in processing may override standard procedures"
  ],
  "merchant_specific": [
    "Service Start Date (varies by contract)",
    "Months of Service (varies by contract)",
    "Total Price amounts (contract-specific)",
    "Discount amounts (contract-specific)",
    "Setup fee presence and amount (optional, contract-specific)",
    "Initial fee credit structure (optional, contract-specific)",
    "Custom processing requests that differ by contract",
    "Events billing information (if necessary)",
    "Integration item assignments (merchant-dependent: Statsig, Pinata, TIFIN)",
    "Tax handling as line items"
  ],
  "confidence_score": 0.92
}
```

---

