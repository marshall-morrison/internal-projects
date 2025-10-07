# Raw LLM Analysis: HELIX ALTERNATIVE TECHNOLOGIES INC-MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:46:12

---

## Chunk 1: HELIX ALTERNATIVE TECHNOLOGIES INC-MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:46:12

### Original Content
```
Tab 1 Contract Processing Steps (Implementation Success to fill) Contracts for HELIX ALTERNATIVE TECHNOLOGIES INC will look like the following Please follow the steps to process correctly Some contracts include: Flat Payment Initial Payment and Remaining Payment Steps to process You will have to create Different Revenue Schedules for Each type of charge Follow Steps below for Flat Payment (Screenshot example below) Flat Payment Service Start Date: Listed with Order Form Effective Date Months of ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Revenue Schedule Creation",
    "Payment Structure Processing (Flat, Initial + Remaining, Per Employee)",
    "Default Values and Standard Operating Procedures",
    "Integration Item Assignment and Labeling",
    "Contract Field Mapping and Data Entry"
  ],
  "rules": [
    "Create separate revenue schedules for each type of charge in a contract",
    "Flat Payment: Service start date must match order form effective date",
    "Flat Payment: Default periods to 12 with yearly frequency",
    "Flat Payment: Quantity always set to 1",
    "Flat Payment: Net terms default to 30 days",
    "Initial Payment Schedule: Service start date is the order form effective date",
    "Initial Payment Schedule: Periods set to 1 with frequency matching trial length",
    "Remaining Payment Schedule: Start date begins after initial trial period completes",
    "Remaining Payment Schedule: Calculate months as total contract months minus initial period months",
    "Remaining Payment Schedule: Total price equals license price minus initial period price",
    "Per Active Employee pricing: Default to 12 periods if monthly",
    "Per Active Employee pricing: Frequency is yearly unless otherwise specified",
    "All revenue schedules: Net terms default to 30 days unless specified",
    "Default service term is 3 years",
    "Default billing frequency is monthly if none listed",
    "Ignore any contract items marked as 'waived'",
    "Every tax line item becomes a BT (Billing Type) by default",
    "Item description for integration items: 'TIFIN Netsuite Integration Items'",
    "Integration items must be assigned to specific categories (e.g., Sales, Software Subscription Bundle)"
  ],
  "exceptions": [
    "Merchant may request specific processing that differs by contract (e.g., back-dating invoice dates to final day of month)",
    "Billing frequency may be specified differently than monthly default",
    "Net terms may be specified differently than 30-day default",
    "Service term may differ from 3-year default",
    "Per Active Employee pricing frequency can be non-yearly if specified",
    "Integration item labeling varies by type: Statsig items labeled as 'Sales', Pinata items as 'Software Subscription Bundle' unless noted otherwise",
    "Waived items should be excluded from processing"
  ],
  "merchant_specific": [
    "Merchant name: HELIX ALTERNATIVE TECHNOLOGIES INC",
    "Integration item reference: 'TIFIN Netsuite Integration Items'",
    "Specific integration labeling rules: Statsig → 'Sales', Pinata → 'Software Subscription Bundle'",
    "Contract-specific processing variations based on merchant requests",
    "Reference to 'Garage' example for Per Active Employee pricing (Contract ID: 8e2c02ef-8b81-4cd2-a919-99745447ada1)",
    "Item names and descriptions pulled from contract headers and order forms",
    "Custom fields: 'Access Period', 'Term', 'License Price'",
    "Events billing processing (merchant-specific, to be filled by Implementation Success)",
    "Integration items processing instructions (merchant-specific, to be filled by Implementation Success)"
  ],
  "confidence_score": 0.85
}
```

---

