# Raw LLM Analysis: TIFIN AG_ WEALTHTECH_ MAGNIFI_ Axis _ TIFIN IP MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 12:02:17

---

## Chunk 1: TIFIN AG_ WEALTHTECH_ MAGNIFI_ Axis _ TIFIN IP MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:02:17

### Original Content
```
Tab 1 Contract Processing Steps (Implementation Success to fill) Scroll to the Section in a contract called TIFIN AG ORDER FORM it will look like this screenshot here You will see two types of pricing Full payment Payment is split up into payment schedules Please find the section below accordingly to process labeled Full Payment or Payment Schedule Full Payment (see screenshot below as example) Service Start Date: Invoice Date, not Order Effective Date Months of Service: 36 months Item Name: Ann...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflows - Distinguishing between full payment and payment schedule processing methods",
    "Revenue Recognition and Billing Configuration - Setting up service terms, billing frequencies, and revenue schedules",
    "Data Extraction from Contracts - Identifying and mapping specific contract fields to system fields",
    "Default Values and Fallback Logic - Establishing standard values when contract information is missing",
    "Invoice and Payment Terms Management - Handling dates, net terms, and tax line items"
  ],
  "rules": [
    "Two primary processing types exist: Full Payment and Payment Schedule",
    "Full Payment: Service Start Date must be Invoice Date (not Order Effective Date)",
    "Full Payment: Default Months of Service is 36 months",
    "Full Payment: Item Name must be 'Annual License Fee'",
    "Full Payment: Item Description must be 'Integration'",
    "Full Payment: Billing type must be 'Flat'",
    "Full Payment: Quantity must be 1",
    "Full Payment: Start Date must match Service Start Date",
    "Full Payment: Default Periods is 3",
    "Full Payment: Default Frequency is 1 year unless otherwise noted",
    "Payment Schedule: Service Start Date must be Order Effective Date (not Invoice Date)",
    "Payment Schedule: Default Months of Service is 12 if none listed",
    "Payment Schedule: Create a Revenue Schedule for every line listed",
    "Payment Schedule: Item Name must be 'License Fee'",
    "Payment Schedule: Periods must be set to NONE",
    "Payment Schedule: Frequency must be set to NONE",
    "Payment Schedule: Each line item requires individual revenue schedule creation",
    "Default Net Payment Terms is 30 days across both processing types",
    "Default Service Term is 3 years for Full Payment, 1 year for Payment Schedule",
    "Default Billing Frequency is Monthly if none listed (Ops Default)",
    "Tax line items default to BT (Billing Type) if none listed",
    "Order Form Effective Date should be ignored during processing",
    "Initial Term should be ignored during processing",
    "Full amount of license fee should be ignored in Payment Schedule processing",
    "Integration Item reference: TIFIN Netsuite Integration Items"
  ],
  "exceptions": [
    "Frequency can differ from default 1 year if otherwise noted in contract (Full Payment)",
    "Merchant may request contract-specific processing variations (e.g., back-dating invoice date to final day of month)",
    "Months of Service defaults to 12 for Payment Schedule only if none listed in contract",
    "Service Start Date differs based on payment type: Invoice Date for Full Payment vs Order Effective Date for Payment Schedule",
    "Payment Schedule requires individual start dates per line item found in contract",
    "Tax handling can vary but defaults to BT if not specified"
  ],
  "merchant_specific": [
    "Invoice date back-dating to final day of month (mentioned as example of merchant-specific processing)",
    "Contract-specific variations in processing that may differ by merchant",
    "TIFIN-specific terminology: 'TIFIN AG ORDER FORM', 'TIFIN Netsuite Integration Items'",
    "Implementation Success team responsible for filling Tab 1 Contract Processing Steps",
    "Merchant may have custom payment term requirements beyond default 30 days",
    "Merchant-specific billing frequency preferences that override monthly default",
    "Custom tax handling preferences per merchant beyond default BT classification"
  ],
  "confidence_score": 0.85
}
```

---

