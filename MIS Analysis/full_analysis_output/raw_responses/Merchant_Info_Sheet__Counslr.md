# Raw LLM Analysis: Merchant Info Sheet_ Counslr

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:55:07

---

## Chunk 1: Merchant Info Sheet_ Counslr_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:07

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
    "Implementation partnership and communication preferences"
  ],
  "rules": [
    "Sales commission functionality must be available before account executive exercises certain actions",
    "Invoice paid dates are required for commission payout calculations",
    "Manual workarounds are acceptable during implementation phase until full functionality is built",
    "Co-founders (Tyler and Josh) must make decisions together - joint decision-making authority required",
    "Primary communication channel is Slack (DM or merchant channel)",
    "Migration strategy prioritizes non-annual contracts first (collected upfront, easier to manage)",
    "Annual contracts are migrated later in the process due to complexity"
  ],
  "exceptions": [
    "Tyler accepts manual workarounds temporarily while functionality is being developed (flexible on interim solutions)",
    "Josh is not the main user but may be more particular about requirements when involved",
    "Non-annual contracts are prioritized for migration over annual contracts due to upfront collection and management ease"
  ],
  "merchant_specific": [
    "Merchant name: Implied to be Tyler and Josh's company",
    "Key stakeholders: Tyler (champion, primary POC, co-founder) and Josh (co-founder, secondary user, more detail-oriented)",
    "Specific feature priorities: Invoice scheduling and tracking, usage data upload, invoice paid dates for commissions",
    "Migration source: Stripe Billing",
    "Communication preference: Slack DM or dedicated merchant channel",
    "Temperament considerations: Tyler is easy to work with and responsive; Josh is more particular but reasonable",
    "Contract types: Annual contracts (collected upfront) vs non-annual contracts"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet_ Counslr_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:11

### Original Content
```
Merchant Demo date: Jun 11, 2024 Scoping start date: Jun 14, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Jul 3, 2024 [If Exists] Opt Out Date: 01 31 2025 Go Live Date: Sep 1, 2024 GTM POC: Implementation POC: ERP: None Tax Integration: Key people at Merchant CFO: Tyler F , COO and Co-Founder Customer service rep who is really involved: Josh Liss, CEO and Co-Founder Account Receivable POC: officialcounslr gmail com Billing POC: officialcounslr gmail com Company summary Counslr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Billing Model Transition and Automation",
    "Integration and Technical Infrastructure",
    "Stakeholder Identification and Communication",
    "Contractual Terms and Opt-Out Provisions"
  ],
  "rules": [
    {
      "rule": "Onboarding follows a structured timeline: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "Opt-out requires 30 days notice ahead of the opt-out date",
      "type": "contractual",
      "explicit": true
    },
    {
      "rule": "Multiple key stakeholders must be identified including CFO, COO, AR POC, and Billing POC",
      "type": "organizational",
      "explicit": true
    },
    {
      "rule": "Pain points and goals must be documented to understand merchant needs and prevent opt-out",
      "type": "business_requirement",
      "explicit": false
    },
    {
      "rule": "Feature requests should be captured during onboarding (e.g., invoice paid dates in CSV export)",
      "type": "product",
      "explicit": true
    },
    {
      "rule": "Integration requirements must be documented including ERP and Tax systems",
      "type": "technical",
      "explicit": true
    },
    {
      "rule": "Understanding the merchant's previous toolset helps identify automation opportunities",
      "type": "discovery",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Opt-out clause exists with specific date (01/31/2025) requiring 30 days advance notice",
      "condition": "Merchant must provide notice by 01/01/2025 to exercise opt-out"
    },
    {
      "exception": "No ERP integration required for this merchant",
      "condition": "Merchant operates without traditional ERP system"
    },
    {
      "exception": "Custom feature request for CSV export enhancement to support downstream Rippling integration",
      "condition": "Specific to merchant's sales commission workflow"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company mission and industry",
      "value": "Text-based mental health support for schools and communities",
      "customization_type": "business_context"
    },
    {
      "element": "Billing model transition",
      "value": "Moving from standard SaaS to usage-based billing",
      "customization_type": "pricing_model"
    },
    {
      "element": "Previous technology stack",
      "value": "Stripe Billing, QuickBooks Online, Spreadsheets",
      "customization_type": "legacy_systems"
    },
    {
      "element": "Key personnel and roles",
      "value": "Tyler F (CFO/COO), Josh Liss (CEO), specific email contacts",
      "customization_type": "stakeholder_mapping"
    },
    {
      "element": "Downstream integration needs",
      "value": "Rippling for sales commission payouts",
      "customization_type": "workflow_integration"
    },
    {
      "element": "Specific dates",
      "value": "All milestone dates from Jun 11, 2024 to Sep 1, 2024",
      "customization_type": "timeline"
    },
    {
      "element": "Opt-out date",
      "value": "01/31/2025",
      "customization_type": "contractual_terms"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet_ Counslr_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:23

### Original Content
```
50 month by 12 months The BT for this is now  42 user and this will be 1 invoice for the entire year period Events Usage Processing (if necessary) Event based merchant Usage based Use Number of users to track Integration Items Processing (if necessary) Use  Sales  It doesn t really matter at this time because they don t have an GL Post Processing Communications (if necessary) Does Ops Team need to notify anyone on the team re: completion of processing batches in Implementation or Active phase Wh...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Invoice Management",
    "Usage and Event Tracking",
    "Commission Processing and Reporting",
    "Implementation Phase Communication",
    "Customer and Sales Rep Association"
  ],
  "rules": [
    "BT (billing term) is 42 users for annual invoice period",
    "Single invoice generated for entire year period",
    "Number of users should be tracked for integration items processing",
    "Sales rep who sold the deal must be associated with each individual customer",
    "Sales rep information should be populated on invoices for payment visibility",
    "Implementation period requires flagging for Royce to review",
    "Slack bot notification must be sent to merchant when contract processing is complete",
    "CSV export of invoice paid dates is required for commission payouts",
    "Commission structure calculations must be included in CSV export",
    "Commission CSV processing occurs in the second week of every month",
    "Invoice paid dates must be tracked for commission purposes"
  ],
  "exceptions": [
    "GL Post Processing is not applicable at this time because merchant doesn't have a GL (General Ledger)",
    "Event-based and usage-based processing marked as 'if necessary' - conditional requirement",
    "Integration items processing marked as 'if necessary' - conditional requirement",
    "Communications processing marked as 'if necessary' - depends on implementation or active phase"
  ],
  "merchant_specific": [
    "Specific user count: 42 users",
    "Annual billing cycle (12 months)",
    "No finance people currently on staff - Tyler handling manually in Google Sheets",
    "Simple commission structure (merchant-specific calculation method)",
    "Specific stakeholder: Royce for implementation review",
    "Specific stakeholder: Tyler currently managing commission calculations",
    "Feature urgency: ASAP to prevent opt-out risk",
    "Referenced calls with specific dates (June 11, 14, 18, 2024) indicating merchant onboarding timeline",
    "Merchant name appears to be 'Counslr' based on call reference"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Merchant Info Sheet_ Counslr_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:27

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
      "rule": "All new contracts starting August 12, 2024 must be sent to Tabs",
      "category": "migration_timeline"
    },
    {
      "rule": "Use Order Effective Date from Appendix/Order Form for billing, not contract signature date",
      "category": "date_handling"
    },
    {
      "rule": "Customer email must be populated in contract (currently handled manually by Tyler)",
      "category": "customer_data"
    },
    {
      "rule": "No GL ledger should be linked to accounts due to small company size",
      "category": "accounting_setup"
    },
    {
      "rule": "Default Service Term: Use contract specified term (e.g., 12 months), if none listed default to 1 Year",
      "category": "defaults"
    },
    {
      "rule": "Default Net Payment Terms: Use contract specified terms (Net 7, Net 21, etc.), if none listed default to Net 0",
      "category": "defaults"
    },
    {
      "rule": "Default Billing Frequency: Use contract specified cadence (monthly, semi-annual, etc.), if none listed default to Monthly",
      "category": "defaults"
    },
    {
      "rule": "Tax Handling: Every tax line item becomes a BT (Billable Transaction)",
      "category": "tax_processing"
    },
    {
      "rule": "For annual billing with monthly per-person amounts: multiply the monthly amount by 3",
      "category": "billing_calculation"
    },
    {
      "rule": "Tyler handles all AR (Accounts Receivable) operations",
      "category": "organizational"
    },
    {
      "rule": "Merchant has approximately 20 contracts total",
      "category": "organizational"
    }
  ],
  "exceptions": [
    {
      "exception": "Monthly usage contracts are the biggest pain point and will be prioritized for migration",
      "condition": "Billing model is monthly usage-based"
    },
    {
      "exception": "Flat SaaS fee contracts (annual upfront) are not pain points and will migrate slower",
      "condition": "Billing model is annual flat fee"
    },
    {
      "exception": "Most flat SaaS contracts already sent out as of August 2024",
      "condition": "Contract type is flat annual SaaS fee"
    },
    {
      "exception": "Renewed contracts will be sent to Tabs on a rolling basis",
      "condition": "Contract is up for renewal"
    },
    {
      "exception": "Special calculation for annual billing: multiply monthly per-person rate by 3",
      "condition": "Contract shows annual billing with monthly per-person pricing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Tyler as single point of contact for AR",
      "type": "personnel"
    },
    {
      "element": "Small lean team structure",
      "type": "organizational_structure"
    },
    {
      "element": "Approximately 20 total contracts",
      "type": "scale"
    },
    {
      "element": "Kemo Sabe referenced as example customer with per-user per-month billing",
      "type": "customer_example"
    },
    {
      "element": "No GL ledger linking due to company size",
      "type": "accounting_practice"
    },
    {
      "element": "Customer email not currently in contracts (future enhancement planned)",
      "type": "data_field"
    },
    {
      "element": "August 12, 2024 as migration start date",
      "type": "timeline"
    },
    {
      "element": "Monthly usage contracts as primary pain point",
      "type": "business_priority"
    },
    {
      "element": "Billing models: per-employee usage, flat SaaS fee",
      "type": "billing_structure"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document is somewhat fragmented with incomplete sentences and unclear formatting, which affects interpretation. The note about multiplying by 3 for annual billing appears incomplete or potentially contains a typo. Some context is missing (e.g., what "BT" fully stands for, what "Tabs" system capabilities are). However, the core rules around defaults, processing steps, and migration timeline are relatively clear and extractable.

---

