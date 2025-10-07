# Raw LLM Analysis: Pirros MIS_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:12:09

---

## Chunk 1: Pirros MIS__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:12:09

### Original Content
```
Merchant Name: Pirros Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Every BT in the Services Section should be a BT  Additional users  that are ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Service Item Configuration and Naming Conventions",
    "Date Handling and Service Term Calculations",
    "Billing Type and Payment Frequency Determination",
    "Price and Discount Management"
  ],
  "rules": [
    "Every BT (Billing Type) in the Services Section should be processed as a BT",
    "Additional users that are unit BT should NOT be processed as a BT",
    "Products mentioned under Additional Terms section should NOT be processed as a BT",
    "Flat fee items called 'additional users' SHOULD be processed",
    "Item Name must use the exact name from the 'Service(s)' column of the Order Form",
    "Quantity defaults to 1 if not explicitly stated",
    "Service Start Date should use the start date from the 'Service Term' field",
    "If Service Start Date not provided (e.g., onboarding services), default to the effective date of the Order Form",
    "Total months of service should be rounded to nearest whole month to reach end of service term",
    "Annual contracts stating dates like '1/1/25 - 1/1/26' should be corrected to '1/1/25 - 12/31/25' (one year contracts)",
    "Do not match service dates until the next year start date (e.g., not until 1/1/26)",
    "Revenue schedule runs from start date in contract until end date minus one day",
    "For one-time service fees or implementation, default to 0 months of service",
    "Billing Type should be 'flat' (flag if different)",
    "Total Price should use the 'Final Price' amount from Order Form",
    "Discounts should be captured in line unless listed as separate line item",
    "For subscriptions/recurring fees: use 'Monthly' if billed monthly, 'Annual' if invoiced annually",
    "For onboarding, support, or one-time items: use 'None' for frequency",
    "Net Terms should use explicitly stated terms in Payment Terms section"
  ],
  "exceptions": [
    "Additional users that are unit BT are excluded from BT processing (exception to general BT rule)",
    "Products under Additional Terms section are excluded from BT processing",
    "Flat fee items labeled as 'additional users' are an exception and SHOULD be processed",
    "Onboarding services without Service Start Date default to Order Form effective date",
    "One-time service fees and implementation have 0 months of service (exception to service term calculation)",
    "Annual contracts with incorrect date ranges (e.g., 1/1/25 - 1/1/26) require correction to proper year-end date",
    "Separate line item discounts (e.g., 'Pirros Onboarding Discount') should be processed separately rather than captured in line"
  ],
  "merchant_specific": [
    "Merchant Name: Pirros",
    "Product naming: 'Pirros Detail Management System' with license counts",
    "Specific discount naming: 'Pirros Onboarding Discount'",
    "Implementation POC and CX POC fields need to be filled by specific teams (IM and IMP)",
    "Billing model section to be filled by Implementation team",
    "Contract Processing Steps section to be filled by Implementation Success team Post-Go Live",
    "Merchant-specific Order Form structure with 'Service(s)' column and 'Service Term' field",
    "Merchant-specific 'Subscriptions & Payments Section' for payment terms reference",
    "Custom fields: 'Final Price' in Order Form",
    "Periods field set to 1 in examples (may be merchant-specific default)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Pirros MIS__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:12:15

### Original Content
```
") If none are listed, default to 30 days Integration Item: Example contracts: E6cde37f-f94c-4043-a5e8-d09b0a26a5a9 71d427c0-7bf8-4f18-aa36-f1a0062c2428 966621d2-148f-4d9c-b786-da240a1e6720 B9fb1786-25a3-47ed-b4b4-3e463ece1e26 Baaee3a9-e8c6-4d22-847a-b8a465b600c6 acd294da-750a-4d8c-8d65-45f33162b5a7 Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term I...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Contract processing and integration workflows",
    "Tax and billing event handling procedures",
    "Post-processing communication protocols",
    "Customer-specific customization and special handling"
  ],
  "rules": [
    {
      "rule": "Default payment terms: 30 days if none are listed in contract",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default service term: 1 year if none listed",
      "category": "Service Terms",
      "explicit": true
    },
    {
      "rule": "Default net payment terms: 0 days if none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default billing frequency: Monthly if none listed",
      "category": "Billing",
      "explicit": true
    },
    {
      "rule": "Tax handling: Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills post-go-live sections for Events Processing, Integration Items Processing, and Post Processing Communications",
      "category": "Workflow Responsibility",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills post-go-live",
      "category": "Workflow Responsibility",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations allowed (e.g., back-dating invoice date to final day of month)",
      "condition": "When merchant has specific requests that differ by contract"
    },
    {
      "exception": "Pinata integration items can have different labels if noted by merchant",
      "condition": "Unless otherwise noted by Merchant"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship",
      "condition": "Specific customer relationships"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract identifiers",
      "description": "Multiple example contract IDs listed (E6cde37f-f94c-4043-a5e8-d09b0a26a5a9, etc.)",
      "customizable": true
    },
    {
      "element": "Items to ignore in contracts",
      "description": "Merchant-specific exclusions from contract processing",
      "customizable": true
    },
    {
      "element": "Integration item labeling rules",
      "description": "Specific rules for Statsig and Pinata, suggesting other merchants may have different rules",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Who needs to be notified, where, and when (e.g., Azmat Aziz via Messari internal channel)",
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos and invoice changes based on individual customer relationships",
      "customizable": true
    },
    {
      "element": "Events billing processing",
      "description": "Merchant-specific instructions for handling events billing",
      "customizable": true
    },
    {
      "element": "CARR reporting requirements",
      "description": "Currently manual process with undefined urgency timeline",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document structure is clear with labeled sections and explicit defaults
- Some formatting issues and incomplete sentences reduce clarity (e.g., fragmented text, unclear abbreviations like "BT")
- Context is partially missing (what "Ops Default" refers to, full workflow context)
- The document appears to be a template or form with some fields filled in, making it harder to distinguish universal rules from example data
- Several acronyms and internal references (AE, Imp, Success, CARR) are used without definition

---

## Chunk 3: Pirros MIS__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:12:22

### Original Content
```
Demo https: us-56595 app gong io call id 2800502320924420397 account-id 6185788025012809606 Pricing   review of their contracts https: us-56595 app gong io call id 6586682561522924877 account-id 6185788025012809606 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills - annual, some multi-year - flat fee (commit to   of users)- mid-contract expansion for more seats - upfront - Their use of  pro-ration  under a seat-based model is not ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Revenue Recognition Model",
    "Contract Structure and Pricing",
    "Payment Processing Workflow",
    "Product Features and Integration Requirements",
    "Customer Growth and Scaling"
  ],
  "rules": [
    "Billing is conducted upfront for annual and multi-year contracts",
    "Pricing model is flat fee based on committed number of users/seats",
    "Mid-contract expansion is allowed for additional seats",
    "Revenue recognition uses 2 SKUs with different schedules per SKU",
    "Quarterly billing adjustments are made for seat-based changes (referred to as 'pro-ration' but not usage-based)",
    "Invoice volume expectation: approximately 20 invoices per month",
    "Payment processing workflow: Pandadoc → Hubspot → Ali creates customer and invoices in Stripe → manual collection → manual cash application for non-Stripe payments",
    "Customer base: 200 customers with expectation to 2x by end of year"
  ],
  "exceptions": [
    "Pro-ration terminology is used but does not reflect true usage-based pro-ration; instead refers to quarterly billing adjustments for seat changes",
    "Manual cash application process required for payments outside of Stripe",
    "Some contracts are multi-year rather than standard annual",
    "Complimentary licenses can be provided as a discount mechanism"
  ],
  "merchant_specific": [
    "Merchant contact: Ari (described as easy to work with and straightforward)",
    "Specific product SKUs: Pirros Detail Management Platform (multiple variants), SSO features, SAML SSO, RBAC, Workspaces, Family Management Add On, Onboarding Service",
    "Integration requirements specific to merchant's tech stack: Pandadoc, Hubspot, Stripe",
    "Account identifiers: account-id 6185788025012809606",
    "Specific call recordings referenced for demo and pricing review",
    "Custom terminology: 'Additional Users', 'Initial Seats', 'Pilot', 'User Accounts' as product line items",
    "Discount structures: Complimentary Licenses, general Discount line items"
  ],
  "confidence_score": 0.75
}
```

---

