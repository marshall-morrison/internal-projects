# Raw LLM Analysis: TIFIN AG_ WEALTHTECH_ MAGNIFI_ Axis  MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:31:16

---

## Chunk 1: TIFIN AG_ WEALTHTECH_ MAGNIFI_ Axis  MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:31:16

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
    "Data Extraction from Order Forms - Identifying and mapping specific contract fields to system fields",
    "Default Values and Fallback Logic - Applying standard defaults when contract information is missing",
    "Tax Line Item Handling - Processing tax as separate billing type items"
  ],
  "rules": [
    "Two primary contract types must be identified: Full Payment and Payment Schedule",
    "Full Payment: Service Start Date must be Invoice Date (NOT Order Effective Date)",
    "Full Payment: Default Months of Service is 36 months",
    "Full Payment: Item Name must be 'Annual License Fee'",
    "Full Payment: Billing type must be 'Flat'",
    "Full Payment: Quantity must be 1",
    "Full Payment: Start Date must match Service Start Date",
    "Full Payment: Periods default to 3",
    "Full Payment: Frequency is 1 year unless otherwise noted",
    "Payment Schedule: Service Start Date must be Order Effective Date (different from Full Payment)",
    "Payment Schedule: Create a separate Revenue Schedule for every line item listed",
    "Payment Schedule: Default Months of Service is 12 if not listed in contract",
    "Payment Schedule: Item Name must be 'License Fee'",
    "Payment Schedule: Periods must be set to NONE",
    "Payment Schedule: Frequency must be set to NONE",
    "Payment Schedule: Start Date is individual to each line and found in contract",
    "Default Net Terms is 30 days across both payment types",
    "Default Service Term is 3 years for Full Payment, 1 year for Payment Schedule",
    "Default Billing Frequency is Monthly if none listed",
    "Item Description must be 'Integration'",
    "Integration Item must reference 'TIFIN Netsuite Integration Items'",
    "Order Form Effective Date should be ignored during processing",
    "Initial Term should be ignored during processing",
    "Full amount of license fee should be ignored in Payment Schedule contracts",
    "Tax line items default to becoming a BT (Billing Type) if not otherwise specified"
  ],
  "exceptions": [
    "Frequency can differ from default 1 year if explicitly noted in contract",
    "Invoice dates may be back-dated to final day of month based on merchant-specific processing requests",
    "Months of Service defaults to 12 for Payment Schedule only if none listed in contract",
    "Merchant-specific processing instructions may override standard defaults",
    "Tax handling may vary but defaults to every tax line item becoming a BT if not specified"
  ],
  "merchant_specific": [
    "Back-dating invoice dates to final day of month - varies by merchant/contract",
    "Service term length may differ by specific contract agreement",
    "Net payment terms may vary from 30-day default per merchant agreement",
    "Billing frequency customization per merchant requirements",
    "Tax line item treatment may have merchant-specific variations",
    "TIFIN AG ORDER FORM - specific form name indicates this is for TIFIN merchant",
    "TIFIN Netsuite Integration - merchant-specific integration product",
    "Contract-specific pricing structures (full vs. payment schedule) determined per agreement"
  ],
  "confidence_score": 0.85
}
```

---

