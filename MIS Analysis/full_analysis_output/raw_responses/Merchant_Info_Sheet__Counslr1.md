# Raw LLM Analysis: Merchant Info Sheet_ Counslr(1)

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:38:50

---

## Chunk 1: Merchant Info Sheet_ Counslr(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:50

### Original Content
```
Need to have the sales commission functionality in order to not exercise this AE Notes Any important relationship information 1) What is Merchant Temperament Tyler is our champion and very easy to work with (i e manual workarounds in place until we build towards functionality) Josh will not be main user - he is a little bit of a stickler, but decent guy overall 2) Is there key POC the buyer decision maker Tyler and Josh are Co-Founders and make every decision together Tyler is the primary POC fo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Sales commission functionality and requirements",
    "Merchant relationship management and stakeholder dynamics",
    "Platform migration from Stripe Billing to Tabs",
    "Invoice management and tracking capabilities",
    "Implementation partnership and communication protocols"
  ],
  "rules": [
    "Sales commission functionality must be implemented before account executive (AE) can be assigned",
    "Invoice paid dates are required for commission payout calculations",
    "Co-founders (Tyler and Josh) must jointly approve all decisions",
    "Tyler serves as primary point of contact for implementation matters",
    "Communication should occur via Slack DM or merchant channel",
    "Non-annual contract invoices should be migrated first (collected upfront)",
    "Annual contracts should be migrated later in the process",
    "Manual workarounds are acceptable during functionality build-out phase"
  ],
  "exceptions": [
    "Tyler is flexible with manual workarounds during implementation, while Josh is more particular about processes",
    "Non-annual contracts are prioritized for migration because they are collected upfront and easier to manage",
    "Annual contracts are deferred in migration timeline due to complexity"
  ],
  "merchant_specific": [
    "Merchant has co-founder decision-making structure (Tyler and Josh)",
    "Tyler characterized as 'champion' with high flexibility",
    "Josh characterized as 'stickler' but not primary user",
    "Merchant is actively migrating from Stripe Billing",
    "Key features needed: invoice scheduling/tracking, usage data upload, invoice paid dates",
    "Merchant uses Slack for primary communication",
    "Merchant has both annual and non-annual contract types",
    "Commission payout structure tied to invoice payment dates"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet_ Counslr(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:58

### Original Content
```
Merchant Demo date: Jun 11, 2024 Scoping start date: Jun 14, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Jul 3, 2024 [If Exists] Opt Out Date: 01 31 2025 Go Live Date: Sep 1, 2024 GTM POC: Implementation POC: ERP: None Tax Integration: Key people at Merchant CFO: Tyler F , COO and Co-Founder Customer service rep who is really involved: Josh Liss, CEO and Co-Founder Account Receivable POC: officialcounslr gmail com Billing POC: officialcounslr gmail com Company summary Counslr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Business Model Transition (SaaS to Usage-Based Billing)",
    "Integration and Technology Stack",
    "Pain Points and Solution Requirements",
    "Contractual Terms and Opt-Out Provisions"
  ],
  "rules": [
    {
      "rule": "Onboarding process follows a structured timeline: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "Opt-out requires 30 days notice ahead of the opt-out date",
      "type": "contractual",
      "explicit": true
    },
    {
      "rule": "Key stakeholder roles must be identified: CFO, COO, CEO, AR POC, Billing POC, GTM POC, Implementation POC",
      "type": "organizational",
      "explicit": true
    },
    {
      "rule": "Merchant goals and pain points must be documented during onboarding",
      "type": "documentation",
      "explicit": true
    },
    {
      "rule": "Feature requests should be captured and tracked (e.g., invoice paid dates in CSV export)",
      "type": "product",
      "explicit": true
    },
    {
      "rule": "Integration requirements must be documented (ERP, Tax Integration, existing tools)",
      "type": "technical",
      "explicit": true
    },
    {
      "rule": "Company summary and business context should be captured for each merchant",
      "type": "documentation",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "ERP field shows 'None' - indicating not all merchants require ERP integration",
      "condition": "ERP integration is optional based on merchant needs"
    },
    {
      "exception": "Opt-out clause exists with specific date (01/31/2025) - not all merchants may have opt-out provisions",
      "condition": "Opt-out clause is conditional and marked with '[If Exists]'"
    },
    {
      "exception": "Tax Integration field is empty - suggesting this is optional or not applicable for all merchants",
      "condition": "Tax integration requirements vary by merchant"
    },
    {
      "exception": "Custom feature request for CSV export modification linked to third-party tool (Rippling) for sales commissions",
      "condition": "Merchant-specific workflow requirements may necessitate product customizations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Business vertical: Mental health support for schools and communities",
      "customization_type": "industry_specific"
    },
    {
      "element": "Billing model transition: Standard SaaS to usage-based billing",
      "customization_type": "pricing_model"
    },
    {
      "element": "Existing tech stack: Stripe Billing, QuickBooks Online (QBO), Spreadsheets",
      "customization_type": "integration_requirements"
    },
    {
      "element": "Downstream integration: Rippling for sales commission payouts",
      "customization_type": "workflow_integration"
    },
    {
      "element": "Contact information: officialcounslr@gmail.com for AR and Billing",
      "customization_type": "communication_channels"
    },
    {
      "element": "Key personnel: Tyler F (CFO/COO), Josh Liss (CEO), specific involvement levels",
      "customization_type": "stakeholder_management"
    },
    {
      "element": "Specific opt-out date: January 31, 2025",
      "customization_type": "contractual_terms"
    },
    {
      "element": "Pain point: Back office AR automation for usage billing transition",
      "customization_type": "solution_focus"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet_ Counslr(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:39:09

### Original Content
```
50 month by 12 months The BT for this is now  42 user and this will be 1 invoice for the entire year period Events Usage Processing (if necessary) Event based merchant Usage based Use Number of users to track Integration Items Processing (if necessary) Use  Sales  It doesn t really matter at this time because they don t have an GL Post Processing Communications (if necessary) Does Ops Team need to notify anyone on the team re: completion of processing batches in Implementation or Active phase Wh...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Invoice Configuration",
    "Usage and Event Tracking",
    "Commission Management and Reporting",
    "Implementation Communication Protocols",
    "Customer Data Association and Visibility"
  ],
  "rules": [
    "BT (billing term) is set to 42 users with 1 invoice for entire year period",
    "Use number of users to track integration items processing",
    "In implementation period, flag for Royce to review",
    "Slack bot notification must be sent to merchant when contract processing is complete",
    "Sales rep who sold the deal must be associated with each individual customer",
    "Sales rep information should be populated on invoices for visibility into payment status",
    "Commission CSV extraction occurs in the second week of every month",
    "Simple commission structure is to be used for calculations"
  ],
  "exceptions": [
    "GL Post Processing is not required at this time because merchant doesn't have a GL (General Ledger)",
    "Event-based and usage-based processing marked as 'if necessary' - conditional implementation",
    "Integration Items Processing marked as 'if necessary' - not mandatory for all cases"
  ],
  "merchant_specific": [
    "Specific user count: 42 users",
    "Annual billing cycle (12 months, single invoice)",
    "Tyler is currently handling commission tracking manually in Google Sheets",
    "No finance people currently on staff",
    "Commission payout CSV with invoice paid dates is a critical feature request",
    "Feature is marked ASAP priority to prevent merchant opt-out",
    "Royce is the designated reviewer during implementation",
    "Specific meeting dates and recordings referenced (June 11, 14, 18, 2024)",
    "Merchant name appears to be 'Counslr' based on video title"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Merchant Info Sheet_ Counslr(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:39:10

### Original Content
```
Monthly usage ones are the biggest pain point They will start sending all new contracts to Tabs as of Aug 12, 2024, and as company renewed, they ll send to Tabs Billing model Info on how merchant bills Monthly, quarterly, or annually (very few) How contract is broken up Current contracts in Tabs - Billing by   of employees using the platform per user   per month (e g, Kemo Sabe) Flat SaaS fee today - Annual up front, these are not their pain points They ll be slower in migrating these over as of...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Migration and Onboarding Timeline",
    "Billing Models and Payment Terms",
    "Contract Processing Workflow",
    "Default Values and Fallback Rules",
    "Organizational Structure and Pain Points"
  ],
  "rules": [
    {
      "rule": "All new contracts to be sent to Tabs starting August 12, 2024",
      "category": "migration_timeline"
    },
    {
      "rule": "Use Order Effective Date from Appendix/Order Form for billing, not contract signature date",
      "category": "date_handling"
    },
    {
      "rule": "Create Customer with no GL ledger linked due to small company size",
      "category": "account_setup"
    },
    {
      "rule": "Default Service Term: Use contract info (e.g., 12 months); if none listed, default is 1 Year",
      "category": "service_terms"
    },
    {
      "rule": "Default Net Payment Terms: Use contract terms (Net 7, Net 21, etc.); if none listed, default is Net 0",
      "category": "payment_terms"
    },
    {
      "rule": "Default Billing Frequency: Use contract info (monthly, semi-annual, etc.); if none listed, default is Monthly",
      "category": "billing_frequency"
    },
    {
      "rule": "Tax Handling: Every tax line item becomes a BT (Billable Item/Bill Template)",
      "category": "tax_processing"
    },
    {
      "rule": "For annual billing with monthly per-person amounts: multiply the monthly amount by 12",
      "category": "calculation"
    },
    {
      "rule": "Extract client name, order effective date, order terms, pricing, service plan, and payment terms from Order Form",
      "category": "data_extraction"
    }
  ],
  "exceptions": [
    {
      "exception": "Monthly usage contracts are the biggest pain point and will be prioritized for migration",
      "condition": "billing_model_type"
    },
    {
      "exception": "Flat SaaS fee contracts (annual upfront) are not pain points and will migrate slower",
      "condition": "billing_model_type"
    },
    {
      "exception": "Most flat SaaS contracts already sent out as of August 2024",
      "condition": "migration_status"
    },
    {
      "exception": "Customer email not currently in contracts but planned for future addition",
      "condition": "missing_data"
    },
    {
      "exception": "Tyler knows how to populate customer email in contract (workaround for missing data)",
      "condition": "data_workaround"
    },
    {
      "exception": "Special calculation required when billed annually but contract shows monthly per-person amount",
      "condition": "billing_frequency_mismatch"
    }
  ],
  "merchant_specific": [
    {
      "element": "Small lean team with only ~20 contracts",
      "type": "organizational_context"
    },
    {
      "element": "Tyler handles all AR (Accounts Receivable)",
      "type": "personnel"
    },
    {
      "element": "Two billing models: (1) Per-user per-month (e.g., Kemo Sabe), (2) Flat SaaS fee annual upfront",
      "type": "billing_structure"
    },
    {
      "element": "Monthly usage contracts identified as primary pain point",
      "type": "business_priority"
    },
    {
      "element": "No GL ledger linked to accounts due to company size",
      "type": "accounting_setup"
    },
    {
      "element": "Customer email handling: Tyler has workaround knowledge",
      "type": "process_knowledge"
    },
    {
      "element": "Contract renewal triggers migration to Tabs",
      "type": "migration_trigger"
    },
    {
      "element": "Variable payment terms (Net 7, Net 21, etc.) rather than standardized",
      "type": "payment_flexibility"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document provides clear operational instructions and default rules, but contains some formatting issues, incomplete sentences, and ambiguous references (e.g., "multiplied the 3" appears truncated). The core themes and rules are extractable with reasonable confidence, but some details may require clarification from the source.

---

