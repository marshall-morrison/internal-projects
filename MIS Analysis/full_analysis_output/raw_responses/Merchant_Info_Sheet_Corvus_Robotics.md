# Raw LLM Analysis: Merchant Info Sheet - Corvus Robotics

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:13:04

---

## Chunk 1: Merchant Info Sheet - Corvus Robotics_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:13:04

### Original Content
```
They want one centralized source of truth for contracts and billing Relationship history: Eric used Tabs previously at Outrider and had a positive experience He trusts Tabs already and is excited for the partnership What is the merchant temperament Eric is practical, detail-oriented, and pro-automation He s been clear about wanting to move quickly He s receptive to Tabs and is familiar with the product already Cares about predictability and efficiency Is there a key POC: (i e : who is the buyer ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Centralized contract and billing management",
    "Automation and efficiency optimization",
    "Decision-making hierarchy and stakeholder management",
    "Revenue operations and financial visibility",
    "Prior relationship and product familiarity"
  ],
  "rules": [
    "Eric Andreas (Finance Lead) serves as the primary champion and process leader",
    "Jackie must provide sign-off approval and is likely the final contract signer",
    "Economic buyer approval is required even when champion leads the process",
    "Automated invoicing and dunning must be implemented to eliminate late invoice sending",
    "Revenue recognition and deferred revenue must be automated",
    "Renewals management requires reporting and visibility into upcoming renewal dates",
    "Collections visibility must support cash forecasting capabilities",
    "Contract ingestion must integrate with Hubspot, Google Drive, and Slack",
    "Solution must provide a single centralized source of truth for contracts and billing"
  ],
  "exceptions": [
    "Eric has prior positive experience with Tabs at Outrider, which accelerates trust-building and reduces typical evaluation friction",
    "Despite Jackie being the economic buyer, Eric is empowered to lead the process, suggesting a delegated decision-making structure",
    "Merchant wants to move quickly, potentially shortening standard sales cycles or implementation timelines"
  ],
  "merchant_specific": [
    "Merchant name: Outrider (Eric's previous company where he used Tabs)",
    "Key personnel: Eric Andreas (Finance Lead, Champion), Jackie (Economic Buyer)",
    "Merchant temperament: practical, detail-oriented, pro-automation, values predictability and efficiency",
    "Integration requirements: Hubspot, Google Drive, Slack",
    "Specific pain points: late invoices, lack of renewals visibility, need for cash forecasting",
    "Relationship context: pre-existing trust and product familiarity from Eric's prior usage",
    "Decision velocity: explicit desire to move quickly through the process"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Corvus Robotics_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:13:04

### Original Content
```
Merchant: Corvus Robotics Demo date: 08 21 25 Scoping start date: 08 13 25 MSA Signature Date: 08 29 25 Onboarding Kick Off Date: 09 05 25 [If Exists] Opt Out Date: Yes, first 90 days of the partnership Go Live Date: Oct 1 ideally GTM POC: Implementation POC: Stephen ERP: Tax Integration: Key people at Merchant Eric Andreas   Head of Finance (joined Aug 2025, oversees all finance, invoicing, AR, collections) Jackie   CEO   Founder Notes Sections (AE  Implementation to fill) Info on how merchant ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing processes",
    "Contract management and storage",
    "Payment collection methods",
    "System integrations and technology stack",
    "Project timeline and key stakeholders"
  ],
  "rules": [
    "Contract types are typically 1-3 year agreements with monthly service fees",
    "Billing frequency varies: annual upfront, monthly, quarterly, or 12 months upfront",
    "Invoices must be created for all contracts (currently manual process in QBO)",
    "Some enterprise customers require invoices via procurement portals (Coupa, Ariba)",
    "Payment methods accepted: ACH and enterprise checks",
    "Tax must be calculated on invoices (currently manual process)",
    "Opt-out period exists within first 90 days of partnership",
    "CEO executes contracts, then uploads to Google Drive/Slack/sometimes Hubspot",
    "Implementation fees may be charged upfront in some cases"
  ],
  "exceptions": [
    "Some contracts include upfront implementation fees (not all)",
    "Billing frequency is not standardized - varies by customer agreement",
    "Enterprise customers may require special procurement portal invoice submission (Coupa, Ariba) - merchant did not commit to this process for Corvus Robotics",
    "Contract storage location varies (Hubspot, spreadsheets, Slack, Google Drive) - not centralized",
    "Opt-out clause applies only during first 90 days of partnership"
  ],
  "merchant_specific": [
    "Merchant name: Corvus Robotics",
    "Current ERP: QuickBooks Online (QBO)",
    "No tax integration tool (no Avalara or Anrok)",
    "No payment processor currently in use",
    "Key stakeholders: Eric Andreas (Head of Finance), Jackie (CEO/Founder), Stephen (Implementation POC)",
    "Specific project dates: Demo 08/21/25, Scoping 08/13/25, MSA Signature 08/29/25, Onboarding 09/05/25, Go Live Oct 1 (ideal)",
    "Current pain points: scattered contracts, manual QBO invoicing, late invoices delaying collections, manual tax calculation",
    "Contract storage systems: Hubspot, Google Drive, Slack, spreadsheets",
    "Customer procurement portals: Coupa, Ariba (for enterprise customers)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Corvus Robotics_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:13:15

### Original Content
```
Eric already trusts Tabs from past experience Tabs automates order-to-cash   saves time, reduces manual work, eliminates late billing Tabs provides scalability ahead of growth (they expect to grow significantly in 2025 2026) Tabs provides renewal and revenue visibility that QBO lacks Is there an opt out clause If so, what is the merchant looking for so they do not exercise it Yes, 90 day opt out It was put in place to give peace of mind to the CEO but the Controller (your POC and previous power ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Trust and relationship management with existing customer (Eric/Tabs)",
    "Contract terms and opt-out provisions",
    "Billing timing and revenue recognition workflows",
    "Customer-specific contract structures and fee types",
    "Automation benefits and scalability requirements"
  ],
  "rules": [
    "90-day opt-out clause must be included in contracts",
    "Implementation fees are recognized at go-live date",
    "Service fees should be billed annually upfront (preferred model)",
    "Go-live date can be adjusted once by the merchant",
    "Tabs system automatically reflows billing and revenue recognition schedules when go-live date changes",
    "Contract billing may be delayed until deployment/go-live occurs",
    "Custom work charges must be documented in SOWs (Statements of Work)"
  ],
  "exceptions": [
    "Some contracts allow monthly or quarterly billing instead of annual upfront for service fees",
    "Some Corvus contracts start billing 6-8 weeks after signing (post-deployment)",
    "Custom work is rare but can be included as one-off charges in SOWs",
    "The opt-out clause exists for CEO peace of mind but is not expected to be exercised (Controller has full conviction)"
  ],
  "merchant_specific": [
    "Merchant name: Corvus (implied from context)",
    "Key contacts: Eric (merchant contact), Controller (POC and power user), CEO (requires opt-out for peace of mind)",
    "Expected growth timeline: significant growth in 2025-2026",
    "Deployment timeline: 6-8 weeks from signing to go-live",
    "Previous system: QuickBooks Online (QBO) - lacks renewal and revenue visibility",
    "Contract structure breakdown: Implementation fees + Service fees + occasional Custom work",
    "Specific pain points: late billing, manual work, lack of scalability and revenue visibility"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Corvus Robotics_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:13:15

### Original Content
```
ARR waterfall reporting and ability to export for custom reporting Integration with QBO Company summary (AE to fill) Summary of what company does: Corvus Robotics builds autonomous warehouse inventory scanning robots Their robots autonomously capture real-time inventory data, detect shrinkage, and provide analytics to help large warehouses operate more efficiently Goals (North star) (AE  Implementation to fill) What is the merchant's goal Scale finance operations without adding headcount Support...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue and billing automation",
    "Financial operations scalability",
    "Contract and data centralization",
    "Cash flow and collections management",
    "Integration and reporting capabilities"
  ],
  "rules": [
    "ARR waterfall reporting must be available for export and custom reporting",
    "System must integrate with QuickBooks Online (QBO)",
    "Invoices must be sent timely to reduce Days Sales Outstanding (DSO)",
    "Contracts must be centralized in a single source of truth (not scattered across multiple platforms)",
    "Revenue recognition and deferred revenue processes must be automated (not manual)",
    "Renewals and collections must be tracked systematically (not ad hoc)",
    "Tax calculations must be automated to reduce errors and inefficiency",
    "Billing processes must be scalable to support growth from 50 to hundreds of customers",
    "Finance operations must scale without proportional headcount increases",
    "Cash collections must be timely and predictable"
  ],
  "exceptions": [
    "No explicit exceptions mentioned in this document chunk",
    "Growth timeline specified: scale to hundreds of customers by 2026 (time-bound requirement)"
  ],
  "merchant_specific": [
    "Company name: Corvus Robotics",
    "Industry: Autonomous warehouse inventory scanning robots",
    "Current scale: ~50 active contracts",
    "Target scale: Hundreds of customers by 2026",
    "Current pain points: Contracts scattered across Slack, Hubspot, and Google Drive",
    "Accounting system: QuickBooks Online (QBO)",
    "Product offering: Autonomous robots for real-time inventory data, shrinkage detection, and warehouse analytics",
    "Target customers: Large warehouses",
    "Document owner roles: AE (Account Executive) and Implementation team"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 5: Merchant Info Sheet - Corvus Robotics_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:13:38

### Original Content
```
Renewals: annual, ad hoc today but Tabs will track One off things to know about the merchant Enterprise customers (few) may require special invoice formatting (supplier numbers, procurement portal invoicing) Half of their routine invoices go out late today They never charge late fees, but include them in contracts as leverage Growth target: move from  50 active contracts   hundreds by 2026 Payments include large checks, even from enterprises Contract Processing Steps (Implementation Success to f...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Configuration",
    "Implementation and Onboarding Process",
    "Revenue Recognition and Payment Processing",
    "Customer Relationship Management",
    "Operational Workflows and Communication"
  ],
  "rules": [
    {
      "category": "Billing Timeline",
      "rule": "30 day lead time from signature to go-live before billing starts",
      "specificity": "explicit"
    },
    {
      "category": "Billing Timeline",
      "rule": "Service start date must use the latest signature date",
      "specificity": "explicit"
    },
    {
      "category": "Billing Timeline",
      "rule": "Billing start date = signature date + 30 days for Service Fees",
      "specificity": "explicit"
    },
    {
      "category": "Billing Configuration",
      "rule": "Billing schedules and revenue schedules must match 1:1",
      "specificity": "explicit"
    },
    {
      "category": "Implementation Fee",
      "rule": "One-time implementation fee is upfront payment with Qty: 1, Frequency: none",
      "specificity": "explicit"
    },
    {
      "category": "RaaS Service Fee",
      "rule": "Recurring RaaS service fee defaults to annual frequency unless stated otherwise",
      "specificity": "explicit"
    },
    {
      "category": "Usage-based Fees",
      "rule": "Usage-based development fees billed monthly in arrears using event pricing",
      "specificity": "explicit"
    },
    {
      "category": "Late Fees",
      "rule": "Late fees configured as usage-based with 1.5% price, monthly frequency, starting at contract start date",
      "specificity": "explicit"
    },
    {
      "category": "Late Fees",
      "rule": "Late fees included in contracts as leverage but never actually charged",
      "specificity": "explicit"
    },
    {
      "category": "Payment Terms",
      "rule": "Default net terms are 30 days",
      "specificity": "explicit"
    },
    {
      "category": "Customer Setup",
      "rule": "Customer should always already be created before processing; verify by checking address details if name varies slightly",
      "specificity": "explicit"
    },
    {
      "category": "Contract Scope",
      "rule": "Processing applies to all Order Forms using Corvus's standard Master RaaS Agreement",
      "specificity": "explicit"
    },
    {
      "category": "Service Duration",
      "rule": "Months of service should use full contract term (e.g., 12 or 36 months)",
      "specificity": "explicit"
    },
    {
      "category": "Exclusions",
      "rule": "Ignore complimentary or waived services (e.g., free consulting)",
      "specificity": "explicit"
    },
    {
      "category": "Exclusions",
      "rule": "Ignore API access and hosting options during processing",
      "specificity": "explicit"
    },
    {
      "category": "Renewals",
      "rule": "Renewals are annual and currently ad hoc, but Tabs will track",
      "specificity": "explicit"
    },
    {
      "category": "Invoice Timing",
      "rule": "Half of routine invoices currently go out late",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "condition": "Enterprise customers",
      "exception": "May require special invoice formatting including supplier numbers and procurement portal invoicing",
      "impact": "high"
    },
    {
      "condition": "RaaS service fee frequency",
      "exception": "Default to annual unless stated otherwise in contract",
      "impact": "medium"
    },
    {
      "condition": "Customer name variations",
      "exception": "Customer name may vary slightly from existing records; verify using address details",
      "impact": "medium"
    },
    {
      "condition": "Large enterprise payments",
      "exception": "Payments include large checks, even from enterprises",
      "impact": "low"
    },
    {
      "condition": "Complimentary services",
      "exception": "Do not process complimentary or waived services",
      "impact": "medium"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "Corvus",
      "context": "References 'Corvus's standard Master RaaS Agreement'"
    },
    {
      "element": "Product Type",
      "value": "RaaS (Robotics as a Service)",
      "context": "Core service offering with recurring and usage-based components"
    },
    {
      "element": "Contract Scale",
      "value": "Growth from ~50 active contracts to hundreds by 2026",
      "context": "Indicates scaling merchant with growth targets"
    },
    {
      "element": "Billing Components",
      "value": "Implementation fee, RaaS service fee, Usage-based development & support fees",
      "context": "Specific billing structure for this merchant"
    },
    {
      "element": "Processed Examples",
      "value": "dd3f00c7-79bd-4d83-9deb-54dab2d436c0, 18a7c662-cfde-42d8-ba45-61de5b4b7174",
      "context": "Reference contracts for validation"
    },
    {
      "element": "Internal Contact",
      "value": "Azmat Aziz (Customer Success)",
      "context": "Notification required via Messari internal merchant channel when contracts reach Active phase"
    },
    {
      "element": "Pricing Model",
      "value": "Hybrid: flat-fee + usage-based billing",
      "context": "Both billing types present in contracts"
    },
    {
      "element": "Usage Pricing",
      "value": "Listed price per hour for development fees",
      "context": "Hourly rate structure for usage-based services"
    },
    {
      "element": "Late Fee Policy",
      "value": "1.5% late fees included but not enforced",
      "context": "Used as contractual leverage only"
    }
  ],
  "confidence_score": 0.85
}
```

---

