# Raw LLM Analysis: MavenAGI Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 10:24:36

---

## Chunk 1: MavenAGI Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:36

### Original Content
```
Merchant: MavenAGI Demo date: Scoping start date: n a MSA Signature Date: Jun 27, 2025 Onboarding Kick Off Date: Jun 30, 2025 [If Exists] Opt Out Date: none Go Live Date: Nov 14, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Tracy Wayne Lauren Murphy (Head of Operations, oversees Finance Legal People) Customer service rep who is really involved: Jillian Smerechniak (Finance Manager) Accounts Receivable POC: Jillian Smerechniak Billing POC: Jillian Sme...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline Management",
    "Billing Model Configuration (Usage-based and Prepaid)",
    "System Integration and Data Synchronization",
    "Contract Processing and Invoice Customization",
    "Stakeholder Identification and Role Assignment"
  ],
  "rules": [
    {
      "rule": "Most contracts will be order forms",
      "category": "Contract Processing",
      "specificity": "general"
    },
    {
      "rule": "If any mention of 'overage' exists, usage AI must be turned on",
      "category": "Usage Tracking",
      "specificity": "conditional",
      "trigger": "overage mention in contract"
    },
    {
      "rule": "Overage-related contracts require threshold usage AI models to track prepaid amounts",
      "category": "Usage Tracking",
      "specificity": "specific"
    },
    {
      "rule": "Use item name and integration item from mapping when available",
      "category": "Item Configuration",
      "specificity": "specific"
    },
    {
      "rule": "If item name doesn't fit mapping, use a simple, clean name derived from the contract",
      "category": "Item Configuration",
      "specificity": "fallback"
    },
    {
      "rule": "Use quantity listed in contract; default to 1 if not specified",
      "category": "Item Configuration",
      "specificity": "specific"
    },
    {
      "rule": "Invoice descriptions need to be contract-specific and editable",
      "category": "Invoice Management",
      "specificity": "general"
    },
    {
      "rule": "Overages trigger standalone invoices",
      "category": "Billing",
      "specificity": "specific"
    },
    {
      "rule": "Usage data can be imported via API or CSV",
      "category": "Data Integration",
      "specificity": "specific"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract terms differ customer to customer (monthly, quarterly, annual)",
      "impact": "Billing frequency must be configured per customer contract"
    },
    {
      "exception": "Item naming can use best judgement when standard mapping doesn't fit",
      "impact": "Allows flexibility in item configuration"
    },
    {
      "exception": "Opt-out clause exists but none specified for this merchant",
      "impact": "Need to track opt-out conditions when present"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key Personnel",
      "details": "Tracy Wayne, Lauren Murphy (Head of Operations), Jillian Smerechniak (Finance Manager, AR POC, Billing POC), Mitch Morrison (HubSpot POC)",
      "customization_needed": true
    },
    {
      "element": "ERP and Tax Integration",
      "details": "QuickBooks integration required, tight sync with HubSpot needed",
      "customization_needed": true
    },
    {
      "element": "Business Model",
      "details": "Mix of prepaid usage (credits) and fixed platform fees; usage tracked in Google Sheets CSVs",
      "customization_needed": true
    },
    {
      "element": "Merchant Goals",
      "details": "Eliminate manual invoicing, automate collections, support usage-based billing with prepayment/overage logic, improve visibility into ARR/aging/rev rec/commissions",
      "customization_needed": true
    },
    {
      "element": "Company Context",
      "details": "Series B stage, agentic AI solutions for enterprise support, rapidly scaling with increasing billing complexity",
      "customization_needed": true
    },
    {
      "element": "Timeline",
      "details": "MSA: Jun 27, 2025; Onboarding: Jun 30, 2025; Go Live: Nov 14, 2024 (note: date inconsistency)",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MavenAGI Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:39

### Original Content
```
For Resolution Volume, make sure to use the quantity purchased  175,000    0 76 resolution    175,000 quantity Total Price Use the listed total amount divided to match the listed billing period Most total prices are listed annually and common billing periods are quarterly and upfront (divide annual total by 4 for quarterly) Sometimes the specific payment cadence is listed under the BT table in the payment schedule (see below) Process all  0 BTs Discounts: Need to use in-line discounting and spre...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Configuration",
    "Discount Processing and Application",
    "Usage-Based Billing and Overage Management",
    "Date and Term Configuration (Service Start, Billing Start, Frequency)",
    "Resolution Volume and Quantity Handling"
  ],
  "rules": [
    "Resolution Volume must use the quantity purchased as listed in the contract",
    "Total Price should use the listed total amount divided to match the billing period",
    "Annual total prices divided by 4 for quarterly billing periods",
    "All BTs must be processed without exception",
    "Discounts must use in-line discounting spread evenly across relevant products",
    "Calculate discount percentage by dividing discount amount by total amount when not explicitly listed",
    "Do not create separate negative BTs for discounts (exception: Partnership Credit)",
    "Partnership Credit should be treated as a separate negative BT",
    "Service Start Date should use the effective date from contract",
    "Billing Start Date equals Service Start Date unless Payment Schedule specifies explicit invoice date",
    "Months of Service should use the Initial Term section",
    "Frequency should use Billing Period section unless Payment Schedule specifies otherwise",
    "Net Terms should use billing method section, default to net 0 if not specified",
    "Ignore overage language stating 'billed at agreed on per ticket pricing' when no fixed rate is provided",
    "Usage BTs should be created annually in arrears for resolution unit price",
    "Usage AI should be set up as threshold that charges overages",
    "Usage BT item name should be 'Resolutions (Usage)' with integration item event as resolutions",
    "Threshold amount equals the prepaid amount",
    "Sales tax should be ignored and not processed if item says '(only where applicable)'",
    "Final garage total must match the total payment due number in the contract"
  ],
  "exceptions": [
    "Partnership Credit is the only discount that should be a separate negative BT (all other discounts use in-line discounting)",
    "Billing Start Date differs from Service Start Date only when Payment Schedule explicitly specifies an invoice date",
    "Frequency uses Payment Schedule specification instead of Billing Period section when explicitly stated",
    "Ignore clause 'Overages will be billed at agreed on per ticket pricing annually' in certain contexts",
    "Tiered pricing with multiple years requires separate usage AI models for each year with non-overlapping date ranges",
    "First year threshold may be higher than prepaid amount (e.g., 135,001 to 168,750 provided at no additional charge)",
    "For tiered models, first year threshold calculated by multiplying overage rate by top of free range",
    "Usage AI models with multiple years require unchecking 'service period same as contract' and entering exact date ranges"
  ],
  "merchant_specific": [
    "Resolution-based pricing model (may vary by merchant type)",
    "Platform Fee as separate line item (mentioned in Digital ai and UltraCamp examples)",
    "Specific billing periods (quarterly, upfront, annually) may vary by merchant",
    "Tiered unit pricing structures with year-over-year variations",
    "Prepaid resolution amounts that differ across contract years",
    "Integration item event types (e.g., 'resolutions') specific to merchant's product",
    "Payment Schedule format and location within contract documents",
    "BT table structure and associated payment schedule sections",
    "Merchant-specific terminology like 'garage total' vs 'total payment due'",
    "Specific examples reference merchants: Digital ai (15-month term, quarterly billing) and UltraCamp (quarterly billing with separate BTs)"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: MavenAGI Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:55

### Original Content
```
(LINK) Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merchant Post Processing Communications (if necessary) (Imple...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Integration Item Labeling and Classification",
    "Post-Processing Communication Protocols",
    "Customer-Specific Invoice Handling",
    "Billing Process Automation and Migration",
    "Merchant Relationship Management"
  ],
  "rules": [
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Items Processing",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Items Processing",
      "explicit": true
    },
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active phase",
      "category": "Post Processing Communications",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore sections marked for AE/Implementation to fill",
      "category": "Document Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing, Integration Items Processing, Post Processing Communications, and Customer Information sections",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling Feature Requests and Rewatch Calls sections",
      "category": "Responsibility Assignment",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by the Merchant",
      "condition": "Merchant provides alternative labeling instructions",
      "applies_to": "Integration Items Processing"
    },
    {
      "exception": "Special memos may be required for certain invoices based on customer-specific requirements",
      "condition": "Specific customer relationships or invoice requirements exist",
      "applies_to": "Customer Information"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "condition": "Unique merchant-customer relationship circumstances",
      "applies_to": "Customer Information"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customization_needed": "Each merchant may have different integration partners (e.g., Statsig, Pinata) requiring unique labeling conventions",
      "example": "Statsig → Sales, Pinata → Software Subscription Bundle"
    },
    {
      "element": "Notification recipients and channels",
      "customization_needed": "Different merchants may require notifications to different team members via different communication channels",
      "example": "Azmat Aziz via Messari internal merchant channel"
    },
    {
      "element": "Notification timing triggers",
      "customization_needed": "When notifications should be sent varies by merchant phase and processing stage",
      "example": "When contracts are processed in Active phase"
    },
    {
      "element": "Customer-specific invoice requirements",
      "customization_needed": "Special memos, invoice modifications, and descriptions may vary per merchant's customer base",
      "example": "Long invoices with customized descriptions"
    },
    {
      "element": "Billing methodology",
      "customization_needed": "Billing structure varies (fixed platform fees, prepaid usage credits, overage billing)",
      "example": "Some customers billed fixed fees, others via prepaid credits with overage triggers"
    },
    {
      "element": "Current billing infrastructure",
      "customization_needed": "Each merchant has different existing systems (HubSpot, QuickBooks, Excel, spreadsheets)",
      "example": "Contract data in HubSpot, invoices in QuickBooks, rev rec in Excel"
    },
    {
      "element": "Merchant temperament and collaboration style",
      "customization_needed": "Relationship management approach should adapt to merchant characteristics",
      "example": "Highly collaborative, fast-moving, organized, post-Series B with urgency"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: MavenAGI Merchant Info Sheet__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:55

### Original Content
```
Key POC   Decision Makers: Lauren Murphy (ultimate decision-maker), Jillian (day-to-day finance lead), Mitch (RevOps integration lead) Key Tabs features they care about: PDF contract ingestion   automated billing Usage   prepayment   overage handling Revenue recognition   cash forecasting Dunning automation   Slack reminders HubSpot sync (writeback invoice payment status) Invoice customization (headers, contacts, descriptions) Role-based user permissions and audit-ready exports SFP is the partne...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract item mapping and normalization for billing integration",
    "Stakeholder roles and decision-making hierarchy for platform implementation",
    "Revenue management features including billing automation, usage tracking, and financial forecasting",
    "System integration requirements focusing on CRM and operational tool connectivity",
    "Product licensing and volume-based pricing structures with discount handling"
  ],
  "rules": [
    "Contract line items must be mapped to standardized integration item names for proper system processing",
    "Multiple variations of similar items (e.g., 'Maven AGI Product Licenses', 'Maven Integrations') should consolidate to a single integration item",
    "Volume-based items (Resolutions, Interactions) require tracking against contracted thresholds",
    "Discount line items must be identified and categorized separately from product/service items",
    "Platform fees should be distinguished from usage-based charges",
    "Invoice payment status must sync back to HubSpot CRM",
    "User permissions must be role-based with audit trail capabilities",
    "PDF contracts require automated ingestion and parsing",
    "Overage handling must be configured for usage-based items that exceed contracted volumes",
    "Dunning processes should include Slack notification integration"
  ],
  "exceptions": [
    "Time-limited promotional discounts (e.g., 'End of August Promo') require special handling with expiration dates",
    "Multi-year discounts apply different pricing rules than standard annual contracts",
    "Partnership-specific discounts (e.g., 'Maven Partnership Marketing Discount') may have unique approval or application logic",
    "SFP acts as partner/reseller while Light Labs is the end client, requiring multi-party contract structure",
    "Some contract items use inconsistent naming conventions (e.g., 'Ticket Volume' vs 'Resolution Volume') that map to the same integration item"
  ],
  "merchant_specific": [
    "Decision-maker hierarchy: Lauren Murphy (ultimate), Jillian (finance), Mitch (RevOps)",
    "Client-partner relationship structure: SFP as partner, Light Labs as client",
    "Product-specific terminology: 'Maven AGI Product Licenses', 'Resolutions', 'Interactions'",
    "Volume thresholds: 17,000 resolutions, 25,200 resolutions, 2,083/month tickets",
    "Pricing models: per-resolution pricing ($2.00, $3.75), annual platform fees",
    "Integration requirements: HubSpot CRM writeback, Slack for dunning notifications",
    "Custom invoice requirements: specific headers, contacts, and description formatting",
    "Edition-based offerings: 'Start-Up Edition' as a platform tier"
  ],
  "confidence_score": 0.75
}
```

---

