# Raw LLM Analysis: MIS_ Paiv

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 09:49:48

---

## Chunk 1: MIS_ Paiv_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:49:48

### Original Content
```
MPMerchant Name (AE to fill) Paiv AI - https: www paiv ai  Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Service Start Date: Refer to the "Contr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Creation",
    "Service Pricing and Payment Schedule Management",
    "Date and Frequency Mapping from Contracts",
    "Quantity and Price Calculation Rules",
    "Post-Processing Setup and Auto-Pay Configuration"
  ],
  "rules": [
    "Service Start Date must refer to the 'Contract effective start date'",
    "Months of Service must match the billing period (1 every 1 month = 1 month, 1 every 2 months = 2 months, 3 every 3 months = 9 months)",
    "Item Name should be taken from the 'Subscription' table for itemized services",
    "Item Description should be left blank",
    "Integration Item must have 1:1 match to the item name",
    "Billing Type is usually flat pricing, but check General Terms section for usage pricing",
    "Total Price should refer to the Total Price column for each item",
    "If gross amount has strikethrough, process with discount to result in net amount in bold",
    "Include net $0 items in processing",
    "For change orders, include any billing terms despite the amount",
    "If payment schedule amounts differ from line item amounts, follow the payment schedule",
    "Quantity should refer to the Quantity column, default to 1 unless otherwise specified",
    "Start Date should refer to the 'Billing Start Date'",
    "Periods should refer to the length column",
    "Frequency should refer to the Billing Frequency (monthly, yearly, or otherwise)",
    "Flag to Ashni Marshal to set up auto-pay once processed and reviewed",
    "Dates for both billing and revenue must match the contract",
    "Discounts should be in-line instead of being a separate billing term",
    "US team must set up 'Auto-Pay' for the merchant in the merchant app"
  ],
  "exceptions": [
    "Contracts with quantity increases over time must be flagged to Ashni Marshall and processed with specific breakdown format",
    "For quarterly frequency with additional months, break out as separate billing term (BT)",
    "For broken out BT, International team processes with contract date, then US team changes date to match first invoice in front end",
    "Example reference: d5de5964-b00e-4e18-a9fd-9c2b8af98c54 shows multi-BT structure with varying quantities and frequencies",
    "Special handling for contracts with strikethrough pricing requiring discount calculation"
  ],
  "merchant_specific": [
    "Merchant Name: Paiv AI (https://www.paiv.ai)",
    "Implementation POC field (to be filled by IM)",
    "CX POC field (to be added by IMP)",
    "Billing model section requires merchant-specific information about customer creation process",
    "Contract structure and breakdown varies by merchant",
    "One-off merchant-specific considerations need to be documented",
    "Payment schedule may vary from standard line item amounts per merchant",
    "Auto-pay setup is merchant-specific and requires coordination between teams"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_ Paiv_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:49:50

### Original Content
```
No Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) No Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Succes...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Post-implementation processing and handoff procedures",
    "Cross-team communication and notification protocols",
    "Responsibility assignment across teams (AE, Implementation, Success, Ops)",
    "Contract and billing configuration management"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "billing_defaults"
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "billing_defaults"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax) Events",
      "category": "tax_processing"
    },
    {
      "rule": "Events Processing must match or create events as listed in the contract",
      "category": "events_processing"
    },
    {
      "rule": "Integration Items must have 1:1 match with the item name",
      "category": "integration_processing"
    },
    {
      "rule": "Implementation Success team fills in Events Processing, Integration Items, and Post Processing Communications sections Post-Go Live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation fills Feature Requests prior to go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Success team fills Feature Requests Post-Go Live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Customer Information section tracks all customers on auto-pay",
      "category": "customer_management"
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "responsibility_assignment"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice date to final day of month)",
      "condition": "Contract-specific requirements override defaults"
    },
    {
      "exception": "Post Processing Communications are conditional - only required 'if necessary'",
      "condition": "Not all merchants require post-processing notifications"
    },
    {
      "exception": "Events Processing and Integration Items Processing are marked as 'if necessary'",
      "condition": "Only applicable to certain merchant configurations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract-specific processing instructions",
      "description": "Merchants may have unique requests like back-dating invoices to month-end",
      "customization_required": true
    },
    {
      "element": "Post Processing Communications recipients and timing",
      "description": "Notification requirements vary by merchant (example shows Customer Success [Azmat Aziz] notification in merchant channel when contracts processed in Active phase)",
      "customization_required": true
    },
    {
      "element": "Billing structure and modules",
      "description": "Merchant bills for platform with different modules - structure varies by merchant",
      "customization_required": true
    },
    {
      "element": "Auto-pay customer list",
      "description": "Each merchant has different customers on auto-pay",
      "customization_required": true
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific feature requests tracked through lifecycle",
      "customization_required": true
    },
    {
      "element": "Merchant call recordings",
      "description": "Specific Gong call IDs for Discovery and Demo calls",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: MIS_ Paiv_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:49:59

### Original Content
```
Their clients pay per user, upfront at contract execution They use a CPQ connected to HS to generate quotes Seat-based usage model - This is not supported well in the platform 1) What is the merchant temperament Jason is great Young, very intelligent They are trying to be a profitable business and he cares a ton about cash forecasting Disorganized business Cacheflow deprecating the day of where they are buying Tabs leaving them with no billing software going into next week, requiring us to exped...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Business Model and Payment Structure",
    "Merchant Temperament and Business Priorities",
    "Platform Migration and Implementation Urgency",
    "Financial Management and Cash Flow Visibility",
    "Revenue Optimization and Cost Recovery"
  ],
  "rules": [
    "Clients pay per user/seat-based pricing model",
    "Payment is collected upfront at contract execution",
    "CPQ system must be connected to HubSpot for quote generation",
    "Stripe fees should be passed through to customers",
    "Collections process should be automated through AI billing manager",
    "Cash forecasting must be accurate and visible",
    "Revenue reporting must be available",
    "DSO (Days Sales Outstanding) tracking is required",
    "Invoicing functionality must be supported",
    "Seat-based usage models need platform support"
  ],
  "exceptions": [
    "Seat-based usage model is not well-supported in the current platform (noted limitation)",
    "Expedited implementation required due to Cacheflow deprecation timing",
    "Emergency migration scenario - merchant left without billing software going into next week",
    "Bootstrapped business context (1M ARR) may have different requirements than venture-backed companies"
  ],
  "merchant_specific": [
    "Merchant name: Paiv (Jason as key contact)",
    "Current tech stack: CPQ connected to HubSpot, transitioning from Cacheflow",
    "Business stage: Bootstrapped, $1M ARR, targeting profitability in 2025",
    "Organizational maturity: Described as 'disorganized business'",
    "Key decision-maker profile: Young, intelligent, cash-focused",
    "Priority features for this merchant: Cash Forecasting, Collections, Invoicing, Revenue Reporting, Stripe fee pass-through",
    "Current pain points: No visibility into collections, DSO, or cash forecasting",
    "Business philosophy: 'Every dollar matters' - extreme cost consciousness"
  ],
  "confidence_score": 0.92
}
```

---

