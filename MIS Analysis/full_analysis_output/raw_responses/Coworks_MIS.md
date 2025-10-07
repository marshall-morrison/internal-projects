# Raw LLM Analysis: Coworks MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:30:03

---

## Chunk 1: Coworks MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:03

### Original Content
```
For opt out agreements, start 1 month after signature date Periods and Frequency: Contracts are usually annual but check for other information Extend till 2026 Make BTs always recurring and do not use NONE as frequency For Onboarding: 1 every 1 none If annual invoice, net 30, if monthly, net 0 Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Configuration and Defaults",
    "Billing Terms and Frequency Management",
    "Post-Processing and Go-Live Procedures",
    "Integration and Tax Handling",
    "Communication and Notification Protocols"
  ],
  "rules": [
    {
      "rule": "Opt-out agreements start 1 month after signature date",
      "category": "Contract Timing"
    },
    {
      "rule": "All contracts should be extended till 2026",
      "category": "Contract Duration"
    },
    {
      "rule": "Make BTs (Billing Transactions) always recurring and do not use NONE as frequency",
      "category": "Billing Configuration"
    },
    {
      "rule": "For onboarding: 1 every 1 none",
      "category": "Onboarding Process"
    },
    {
      "rule": "If annual invoice, net 30; if monthly, net 0",
      "category": "Payment Terms"
    },
    {
      "rule": "Default Service Term if none listed: 1 Year",
      "category": "Contract Defaults"
    },
    {
      "rule": "Default Net Payment Terms if none listed: 0",
      "category": "Payment Defaults"
    },
    {
      "rule": "Default Billing Frequency if none listed: Monthly",
      "category": "Billing Defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT",
      "category": "Tax Processing"
    },
    {
      "rule": "Contracts are usually annual but check for other information",
      "category": "Contract Review"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Labeling"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice date may be back-dated to final day of the month based on merchant-specific requests",
      "condition": "Merchant-specific processing requirements"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "condition": "Merchant override"
    },
    {
      "exception": "Contract periods may differ from annual standard",
      "condition": "Must check contract for other information"
    },
    {
      "exception": "Payment terms vary based on invoice frequency (annual vs monthly)",
      "condition": "Invoice type determines net payment terms"
    }
  ],
  "merchant_specific": [
    {
      "element": "Opt-out agreement timing",
      "customizable": true,
      "note": "May differ by contract"
    },
    {
      "element": "Invoice date back-dating preferences",
      "customizable": true,
      "note": "Merchant-specific processing requests"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "note": "Examples given for Statsig and Pinata, implies other merchants may have different requirements"
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "note": "Who, where, and when notifications occur varies by merchant (example: Azmat Aziz for Messari)"
    },
    {
      "element": "Customer-specific invoice memos",
      "customizable": true,
      "note": "Special memos required for certain invoices based on customer relationships"
    },
    {
      "element": "Events billing processing",
      "customizable": true,
      "note": "Implementation Success to fill post-go-live, if necessary"
    },
    {
      "element": "Feature requests",
      "customizable": true,
      "note": "Example given: automated renewal uplift charge (referenced for Luxsci merchant)"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Coworks MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:06

### Original Content
```
Merchant Name (AE to fill): Coworks Coworks is a coworking space management software designed to help flexible workspace operators manage their spaces efficiently It provides tools for handling memberships, booking conference rooms, processing payments, managing events, and communicating with members The platform also offers analytics and reporting features to optimize space usage and enhance the coworking experience Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Sec...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Service Configuration",
    "Billing and Payment Structure",
    "Date Management and Service Timelines",
    "Product/Service Categorization and Naming",
    "Revenue Recognition and Pricing Rules"
  ],
  "rules": [
    {
      "rule": "Service Start Date must use the document signature date as the effective start date",
      "category": "Date Management"
    },
    {
      "rule": "For Onboarding, set start date to 0 months of service",
      "category": "Service Configuration"
    },
    {
      "rule": "For opt-out agreements, start 1 month after signature date",
      "category": "Date Management"
    },
    {
      "rule": "Months of Service should refer to the term listed in purchase terms (typically 1 year)",
      "category": "Contract Terms"
    },
    {
      "rule": "Revenue Category for Onboarding must be 'one time fee'",
      "category": "Revenue Recognition"
    },
    {
      "rule": "Item Name should be extracted from the 'Products & Services' section",
      "category": "Product Configuration"
    },
    {
      "rule": "Item Description must include descriptions and features (member limits, billing, integrations, etc.)",
      "category": "Product Configuration"
    },
    {
      "rule": "Integration Item depends on billing frequency: Monthly Subscription (monthly), Quarterly Subscription (quarterly), Annual Subscription (annually)",
      "category": "Billing Structure"
    },
    {
      "rule": "For Onboarding, Integration Item should be 'setup fee'",
      "category": "Billing Structure"
    },
    {
      "rule": "Billing Type is usually flat",
      "category": "Billing Structure"
    },
    {
      "rule": "Total Price should use the Total column and ignore late fees",
      "category": "Pricing"
    },
    {
      "rule": "For Flok Coworking, discounts should reoccur at the same percentage in forward years",
      "category": "Pricing"
    },
    {
      "rule": "Quantity should use the quantity listed in contract",
      "category": "Product Configuration"
    },
    {
      "rule": "Start Date should be viewed from the contract period start date",
      "category": "Date Management"
    },
    {
      "rule": "New revenue schedule required for price increases",
      "category": "Revenue Recognition"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt-out agreements have different start date calculation (1 month after signature vs. signature date)",
      "condition": "Agreement type is opt-out"
    },
    {
      "exception": "Onboarding has special configuration: 0 months of service, 'one time fee' revenue category, 'setup fee' integration item",
      "condition": "Process type is Onboarding"
    },
    {
      "exception": "Flok Coworking has special discount treatment where discounts reoccur at same percentage",
      "condition": "Merchant is Flok Coworking"
    },
    {
      "exception": "Integration Item varies based on billing frequency (monthly/quarterly/annual)",
      "condition": "Billing frequency determines integration item type"
    },
    {
      "exception": "Late fees should be ignored when calculating Total Price",
      "condition": "When extracting pricing information"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Coworks",
      "type": "Identifier"
    },
    {
      "element": "Business Description: Coworking space management software with specific features (memberships, booking, payments, events, analytics)",
      "type": "Context"
    },
    {
      "element": "Flok Coworking discount recurrence rule",
      "type": "Pricing Policy",
      "note": "Suggests there may be sub-brands or variants requiring specific handling"
    },
    {
      "element": "Products & Services section location",
      "type": "Document Structure",
      "note": "Merchant-specific contract format"
    },
    {
      "element": "Implementation POC, CX POC, Billing model sections marked as 'to fill'",
      "type": "Incomplete Information",
      "note": "Template requires merchant-specific contact and billing details"
    },
    {
      "element": "Total column reference for pricing",
      "type": "Document Structure",
      "note": "Assumes specific contract layout"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Coworks MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:15

### Original Content
```
gong io call id 4745386139491587881 account-id 4433651522798251308 Demo https: us-56595 app gong io call id 7065551662233635702 account-id 4433651522798251308 Partnership- implementation, cs, pricing https: us-56595 app gong io call id 1553436356100389679 account-id 4433651522798251308 Notes: - passing on CC fees Flat fees Annual recurring fees   monthly Use stripe as payment rals   connect stripe with Tabs Auto payment Notes Sections (AE to fill if they have, Implementation to be completion DRI...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payment processing and fee structure",
    "Merchant billing and pricing models",
    "Revenue recognition and financial reporting automation",
    "Implementation and customer success handoff process",
    "Stripe integration and payment automation"
  ],
  "rules": [
    "Credit card fees must be passed on to customers",
    "Use Stripe as the payment rails/processor",
    "Connect Stripe with Tabs platform for integration",
    "Enable automatic payment functionality",
    "Implementation team is the DRI (Directly Responsible Individual) for handoff completion",
    "Account Executives should fill in available notes sections before handoff",
    "Flat fees and annual recurring fees should be billed monthly",
    "Revenue recognition must be accurate and eliminate spreadsheet-based processes",
    "Contract data extraction should be automated from invoices",
    "Cash application, dunning, and collections processes should be automated"
  ],
  "exceptions": [
    "Non-profit discount may be applied (sometimes applicable to pricing)",
    "Renewal uplift pricing adjustments (conditional on renewal terms)",
    "Flat SaaS pricing model (as opposed to usage-based or tiered pricing)"
  ],
  "merchant_specific": [
    "Merchant name: Coworks (scaling business)",
    "Primary contact: Phil (described as 'super easy to work with' and 'excited about Tabs')",
    "Merchant temperament: Cooperative and proactive",
    "Merchant understanding: Values proactive implementation before scaling",
    "Key features prioritized by this POC: Accurate rev rec, reporting elimination of spreadsheets, passing on CC fees, automatic contract extraction, automated cash app/dunning/collections",
    "Business model: Flat SaaS with annual recurring fees billed monthly",
    "Potential non-profit status or discount eligibility"
  ],
  "confidence_score": 0.75
}
```

---

