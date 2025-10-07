# Raw LLM Analysis: Tabs x Responsive _ MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:53:28

---

## Chunk 1: Tabs x Responsive _ MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:28

### Original Content
```
the screenshot below is one BT Currency conversion language Example contract: 0e43c4e6-3444-4171-bc4b-65466fcf7009 Customer is based in the UK - contract is in   BT should be processed as is (in  ) The merchant will do the conversion themselves This customer already existed (pulled in from netsuite) and the currency is in   so that s fine However, if you are creating a customer, please assign the current currency (  in this case) Example Contracts: Abb7c0ae-79fc-417d-abf9-7cac24e4b28c 0b53e739-0...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Currency conversion and handling for international customers",
    "Default operational values for contracts (service terms, payment terms, billing frequency)",
    "Contract processing workflows and responsibilities across teams (AE, Implementation, Success, Ops)",
    "Integration items labeling and categorization",
    "Post-processing communication protocols and stakeholder notifications"
  ],
  "rules": [
    "BT Currency (British Pound) contracts should be processed as-is without conversion when customer is UK-based",
    "Merchant handles currency conversion themselves for BT currency contracts",
    "When creating new customers, assign the contract currency to the customer record",
    "Existing customers pulled from NetSuite retain their existing currency",
    "Default Service Term: 1 Year (if none listed)",
    "Default Net Payment Terms: 0 days (if none listed)",
    "Default Billing Frequency: Monthly (if none listed)",
    "Default Tax Handling: Every tax line item becomes a BT (billable transaction/line item)",
    "Events Processing section must be filled by Implementation Success team post-go-live",
    "Integration Items Processing section must be filled by Implementation Success team post-go-live",
    "Post Processing Communications section must be filled by Implementation Success team post-go-live",
    "Customer Information section must be filled by Implementation Success team post-go-live",
    "Feature Requests: AE fills prior to Implementation handoff, Implementation fills prior to go-live, Success fills post-go-live",
    "Merchant Calls documentation: AE fills prior to Implementation involvement, Implementation fills prior to go-live, Success fills post-go-live"
  ],
  "exceptions": [
    "Contract-specific processing variations may exist (e.g., back-dating invoice dates to final day of month)",
    "Statsig integration items should be labeled as 'Sales' (merchant-specific rule)",
    "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
    "Special memos may be required for certain customer invoices due to merchant-customer relationships",
    "Invoice changes may be needed based on specific merchant-customer relationships"
  ],
  "merchant_specific": [
    "Currency handling preferences (merchant may handle conversion themselves vs. system conversion)",
    "Integration item labeling conventions vary by merchant (Statsig, Pinata examples provided)",
    "Contract-specific processing instructions that differ by merchant agreement",
    "Notification requirements vary by merchant (who to notify, when, and where)",
    "Customer-specific invoice requirements and memos",
    "Merchant phase-specific communication protocols (Implementation vs. Active phase)",
    "Internal merchant channels for team communications"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Tabs x Responsive _ MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:28

### Original Content
```
Merchant Name: Responsive https: app hubspot com contacts 43610657 record 0-3 34893564005 Implementation POC: (IM to fill) Michael Wardrop CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation Process",
    "Contract Data Extraction and Mapping",
    "Service Period and Date Calculations",
    "Pricing and Billing Cadence Configuration",
    "Change Order and Amendment Handling"
  ],
  "rules": [
    "Create one BT per line item listed in subscription or one-time purchase summary sections",
    "Only create BT if the price is not $0",
    "Each subscription or one-time product line should be its own BT",
    "Item Name should use the product or service name from the 'Product' column",
    "Item Description should use subscript under product name or quantity column details if available; leave blank otherwise and ensure it doesn't say 'null'",
    "Quantity should use stated quantity; default to 1 if not specified",
    "Service Start Date should use the Effective Date from contract",
    "Months of Service for subscriptions should use the 'Subscription Term' or number of months between start and end dates",
    "Months of Service should match the time period between effective date and contract expiration date",
    "For Implementation and one-time fees with specified dates, use the start and end date difference; otherwise default to 1 month",
    "For Implementation fees without start/end dates, Months of service would be 0",
    "Integration Items should match the Item Name inclusive of subtext; leave blank if no match in dropdown",
    "Billing Start Date should be checked in 'Billing Information' and 'Customer Info' sections",
    "First invoice usually aligns with the service start date",
    "Total Price should use the line-item total after discounts",
    "BT type should not be 'usage'; change to 'flat' if AI incorrectly sets it",
    "Frequency should match the billing cadence stated in 'Billing Information' section",
    "For one-time and implementation fees, use 1 period and match frequency to service period",
    "Net Terms should use stated payment terms; default to 30 if not specified",
    "PO number should be added to invoices if present on contract",
    "Ignore feature lists or exhibits that describe bundled capabilities as these are not standalone BTs",
    "Locate BTs in tables typically labeled 'SUBSCRIPTION PURCHASE SUMMARY' and 'ONE TIME PURCHASE SUMMARY'"
  ],
  "exceptions": [
    "For change orders: OK to process BT on the change order contract and not the original contract",
    "For change orders: Use the number of months between start date and end date (won't match the subscription term)",
    "For annual, upfront billing cadences that are multi-year subscriptions: Check contract for context clues on whether entirety of subscription is billed at once or annually",
    "For one-time fees without service period stated (months of service = 0): Use 'None' for frequency",
    "If actual usage BT is encountered in contract: Flag to supervisor (have not come across this scenario yet)"
  ],
  "merchant_specific": [
    "Merchant Name: Responsive",
    "Implementation POC: Michael Wardrop (to be filled by IM)",
    "CX POC: To be added by IMP",
    "Billing model section to be filled by Implementation team",
    "Contract Processing Steps section to be filled by Implementation Success team Post-Go Live",
    "Unique customer creation process information (merchant-specific)",
    "How merchant bills (merchant-specific)",
    "Contract structure/breakdown (merchant-specific)",
    "One-off things to know about the merchant (merchant-specific)",
    "Integration item dropdown values (system-specific)",
    "Specific contract references provided as examples (abb7c0ae-79fc-417d-abf9-7cac24e4b28c and 0e43c4e6-3444-4171-bc4b-65466fcf7009)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Tabs x Responsive _ MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:38

### Original Content
```
app gong io call id 7968878822609190585 email_type call-ready-notification xtid v9em320ixnz80n1ya8 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Upfront platform fees   seat based usage   one off service offerings 1) What is the merchant temperament Kind, process oriented Large team with dedicated resources for implementing 3) What are the Tabs features that the key POC cares about SFDC   NS   Stripe integrations Invoice autom...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing structure and revenue models",
    "Merchant temperament and organizational characteristics",
    "Integration requirements and technical capabilities",
    "Implementation handoff process and documentation",
    "Key stakeholder priorities and feature preferences"
  ],
  "rules": [
    "Account Executive (AE) must document notes sections during handoff",
    "Implementation team serves as the Directly Responsible Individual (DRI) for completion after handoff",
    "Merchant billing information must be documented including: platform fees, seat-based usage, and one-off service offerings",
    "Merchant temperament assessment is required as part of the handoff process",
    "Key Point of Contact (POC) feature preferences must be identified and documented",
    "Integration requirements must be specified for each merchant (SFDC, NetSuite, Stripe, etc.)"
  ],
  "exceptions": [
    "Notes sections are conditional - only filled by AE 'if they have' information available",
    "Billing structure may vary by merchant: can include upfront fees, seat-based models, usage-based pricing, or one-off services",
    "Team size and resource availability varies - this merchant has a 'large team with dedicated resources' which may affect implementation approach"
  ],
  "merchant_specific": [
    "Billing model components: upfront platform fees vs seat-based vs usage-based vs one-off services",
    "Merchant temperament description: 'Kind, process oriented'",
    "Team structure: 'Large team with dedicated resources for implementing'",
    "Specific integration platforms: SFDC (Salesforce), NS (NetSuite), Stripe",
    "Feature priorities: Invoice automation and Cash application",
    "Call tracking identifiers: Gong.io call ID, email type, xtid"
  ],
  "confidence_score": 0.75
}
```

---

