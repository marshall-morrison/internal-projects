# Raw LLM Analysis: Alkira _ Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:21:32

---

## Chunk 1: Alkira _ Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:21:32

### Original Content
```
g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) Any important information on events billing Integration Items Processing (if necessary) What are the instructions for assigning in...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Invoice and billing processing standards",
    "Integration item categorization and labeling",
    "Customer-specific pricing and commitment tracking",
    "Usage-based billing and price book management"
  ],
  "rules": [
    "Invoice dates must be back-dated to the final day of the month",
    "Default Service Term: 1 Year (when none listed)",
    "Default Net Payment Terms: 0 (when none listed)",
    "Default Billing Frequency: Monthly (when none listed)",
    "Default tax handling: every tax line item becomes a BT (when none listed)",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed in Active phase",
    "Set up a price book for every new customer onboarded with correct pricing and discounting information",
    "Upload usage data monthly to generate monthly invoicing",
    "Data charge is always $0.06 regardless of listed prices (Alkira-specific)",
    "Discounting ramps to 65% when committed spend amount is achieved"
  ],
  "exceptions": [
    "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
    "Invoice changes may be required due to merchant-customer relationship",
    "Special memos may be required for certain invoices",
    "Usage file mapping may require additional layer of sorting vs event setup",
    "Right to renegotiate pricing every 3 months (customer-specific)",
    "Ops International Team should ignore Implementation Notes Sections"
  ],
  "merchant_specific": [
    "Alkira merchant example with specific business model details",
    "Customer commitment tracking requirements (e.g., $7.2MM over 36 months)",
    "Merchant-specific pricing structures (60% discount, ramping to 65%)",
    "Custom price books per customer with merchant-specific discounting",
    "Merchant-specific integration item labeling (Statsig, Pinata)",
    "Merchant-specific notification requirements and channels",
    "Usage-based billing models vs standard invoicing",
    "Committed spend amount tracking by contract or customer",
    "Customer-specific contract terms (start/end dates, commitment periods)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Alkira _ Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:21:34

### Original Content
```
Merchant Demo date: Scoping start date: MSA Signature Date: Onboarding Kick Off Date: Jun 14, 2024 [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CFO: rakib azad alkira net Account Receivable POC: tracie rex alkira net System POC: shoma alkira net Finance POC: colin mccloskey alkira net Company summary Summary of what company does Goals (North star) What is the merchant's goal What pain are we solving Why are they buying Tabs Is ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Billing Models and Revenue Recognition",
    "Contract Structure and Processing Requirements",
    "Merchant Goals and Pain Points"
  ],
  "rules": [
    "Document must capture MSA Signature Date, Onboarding Kick Off Date, and Go Live Date",
    "Must identify key personnel including CFO, Account Receivable POC, System POC, and Finance POC",
    "Must document ERP system and Tax Integration details",
    "Must specify GTM POC and Implementation POC",
    "Must identify which of 7 billing models applies to the merchant",
    "Billing Model 1 (PAYG): Charge based on actual monthly usage at quoted/discounted prices",
    "Billing Model 2 (Commit Consume): Requires committed amount for contract duration, paid monthly or upfront",
    "Billing Model 3 (Fixed Infrastructure): Uses maximum value between committed minimum per month and actual usage, with overage charges",
    "Must document opt-out clause existence and conditions if present",
    "Must capture merchant's north star goals and pain points being solved",
    "Must document any unique customer creation process requirements",
    "Must specify contract processing steps and items to ignore",
    "Must note any merchant-specific processing requests that differ by contract"
  ],
  "exceptions": [
    "Opt Out Date field is conditional - only required '[If Exists]'",
    "Opt-out clause may or may not exist for each merchant",
    "Billing model selection is merchant-specific (1 of 7 types)",
    "Fixed Infrastructure billing uses 'Pick the maximum value of the two events types' logic",
    "Overage charges only apply in certain billing models when usage exceeds committed amounts",
    "Contract processing may have 'one off things' unique to specific merchants",
    "Processing specifics may 'differ by contract' even for the same merchant"
  ],
  "merchant_specific": [
    "Company summary and business description",
    "North star goals definition",
    "Specific pain points being addressed",
    "Reason for purchase decision",
    "Opt-out clause terms and conditions",
    "Selected billing model from available options",
    "Committed dollar amounts and contract duration",
    "Product family pricing and discount structures",
    "Customer creation process variations",
    "Contract breakdown structure",
    "Items to ignore during contract processing",
    "Merchant-requested processing variations",
    "Key personnel names and contact information",
    "ERP system type",
    "Tax integration approach"
  ],
  "confidence_score": 0.85
}
```

---

