# Raw LLM Analysis: VieFUND MIS (Beacon)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:47:13

---

## Chunk 1: VieFUND MIS (Beacon)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:47:13

### Original Content
```
General All available BTs should be considered This includes  optional ,  additional ,  case by case  - anything that could possibly be charged at any point Except we can ignore  included  BTs BTs are generally hidden in the text itself -  not broken out cleanly in a table All usage BTs will be monthly in arrears Item Name: License Fee This is the big flat monthly fee - typically won t have a name Use best judgement referencing the name listed Keep it clean and short Total Price: use listed pric...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Classification and Inclusion Criteria",
    "License Fee and Pricing Structure Configuration",
    "Date and Timing Rules for Service and Billing",
    "Tiered Pricing and Usage-Based Billing Models",
    "Exclusions and Special Case Handling"
  ],
  "rules": [
    "Include all available BTs: optional, additional, and case-by-case charges",
    "Exclude 'included' BTs from consideration",
    "BTs are typically embedded in text rather than presented in tables",
    "All usage BTs must be billed monthly in arrears",
    "License Fee item name should be clean and short, using best judgment from listed name",
    "License Fee quantity is always set to 1",
    "Service Start Date defaults to signature date, or contract effective date if signature unavailable",
    "Billing Start Date is always the 1st of the month, even if revenue starts mid-month",
    "Months of Service should match contract term length found in the Term clause",
    "For time-limited BTs (e.g., 6 months), match that specific duration",
    "Usage BTs have Monthly frequency; one-time charges have None frequency",
    "Default to Net 15 payment terms if not explicitly stated",
    "When unit price has a range (e.g., 150-200 per hour), set to 1",
    "Report fee should be $250 flat BT with NONE frequency if available",
    "Hourly rate should be configured as monthly BT in arrears"
  ],
  "exceptions": [
    "Exclude: Late Fees, Travel Expenses, Returned Payment, Report Modification, Data Conversion, Onsite Charges",
    "Exclude any charges listed under 'Additional Charges' section",
    "Must include if present: KYP Tool, Kronos Responsive App, Data Conversion Product (set to $1 if no price listed)",
    "Tiered pricing requires special handling: cascading tier_unit BT structure (example: 10-tier structure for nominee plans with decreasing per-unit costs)",
    "Mid-month revenue start still triggers billing on 1st of that month"
  ],
  "merchant_specific": [
    "Contract signature date location may vary by merchant",
    "Term clause location and format (referenced as 'Term' clause with specific numbering like '13 Term')",
    "Payment schedule clause naming and location (example: 'А 3 - Payment Schedule')",
    "Specific product names: VieFUND, KYP Tool, Kronos Responsive App",
    "Net payment terms vary by contract (need to locate payment clause)",
    "Tiered pricing structures and thresholds are merchant/product-specific",
    "'Additional Charges' section location and naming conventions",
    "Invoice delivery and payment timing language may vary"
  ],
  "confidence_score": 0.85
}
```

---

