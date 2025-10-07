# Raw LLM Analysis: HELIX ALTERNATIVE TECHNOLOGIES INC-MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:37:07

---

## Chunk 1: HELIX ALTERNATIVE TECHNOLOGIES INC-MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:07

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
    "Service Term and Billing Configuration",
    "Integration Item Assignment",
    "Default Values and Standard Operating Procedures"
  ],
  "rules": [
    "Create separate revenue schedules for each type of charge within a contract",
    "Flat Payment: Service Start Date must match Order Form Effective Date",
    "Flat Payment: Default to 12 periods with Yearly frequency",
    "Flat Payment: Quantity always set to 1",
    "Flat Payment: Net Terms default to 30 days",
    "Initial Payment Schedule: Service Start Date is the order form effective date",
    "Initial Payment Schedule: Periods set to 1 with frequency matching trial length",
    "Remaining Payment Schedule: Start date begins after initial trial period completes",
    "Remaining Payment Schedule: Total Price = License Price minus initial period price",
    "Remaining Payment Schedule: Frequency duration = contract length minus trial period",
    "Per Active Employee pricing: Default to 12 periods if monthly",
    "Per Active Employee pricing: Frequency is Yearly unless otherwise specified",
    "Item Description for Integration Item must reference 'TIFIN Netsuite Integration Items'",
    "All contracts must ignore any items marked as 'waived'",
    "Default Service Term is 3 Years when not specified",
    "Default Net Payment Terms is 30 days when not specified",
    "Default Billing Frequency is Monthly when not specified",
    "Tax line items: Each tax line item becomes a BT (Billing Transaction) when not specified",
    "Integration items must be labeled according to merchant-specific mapping rules"
  ],
  "exceptions": [
    "Contracts with 'waived' items should be ignored/excluded from processing",
    "Billing frequency may differ by contract based on merchant-specific requests",
    "Invoice dates may need to be back-dated to final day of month per merchant request",
    "Integration item labels vary by merchant (e.g., Statsig = 'Sales', Pinata = 'Software Subscription Bundle')",
    "Per Active Employee pricing follows different period/frequency rules than flat payment",
    "Initial + Remaining payment structures require two separate revenue schedules with different calculation methods"
  ],
  "merchant_specific": [
    "Merchant Name: HELIX ALTERNATIVE TECHNOLOGIES INC",
    "Integration Item Location: 'TIFIN Netsuite Integration Items'",
    "Contract-specific processing variations noted as 'may differ by contract'",
    "Merchant-requested invoice date back-dating to month-end",
    "Integration item labeling rules (Statsig, Pinata examples suggest merchant-specific mapping)",
    "Reference to 'Garage' example for Per Active Employee pricing (Contract ID: 8e2c02ef-8b81-4cd2-a919-99745447ada1)",
    "Item names and descriptions pulled from merchant contract headers",
    "Service term lengths and pricing structures vary by merchant agreement"
  ],
  "confidence_score": 0.85
}
```

---

