# Raw LLM Analysis: LuminAI Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 6
- **Analysis Timestamp**: 2025-10-02 10:40:08

---

## Chunk 1: LuminAI Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:08

### Original Content
```
De-risk key-person reliance (Grace preparing for maternity leave) No opt-out clause Success defined as: High-touch implementation support Flexible ingestion and override of contracts usage Smooth QuickBooks sync and clean handoff for downstream accounting Billing model Billing Model Legacy: Deployment milestone validation fees   mix of usage-based billing (monthly quarterly), flat-fee workflows, and annual SaaS platform fees Current: Hybrid;  10 15 customers in active deployment at a time, with ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing model evolution and transition strategy",
    "Revenue recognition and invoice management processes",
    "Key-person dependency and operational risk mitigation",
    "Implementation fee structure and opt-out policies",
    "Contract standardization and usage-based billing phase-out"
  ],
  "rules": [
    "No opt-out clause is allowed (general policy)",
    "QuickBooks sync must be smooth with clean handoff for downstream accounting",
    "10-15 customers maximum in active deployment at a time",
    "Per-automation fixed fees follow staggered 12-month terms with prorated renewal",
    "Revenue recognition service terms follow per-automation launch dates",
    "Grace's team must review and approve all invoices",
    "Grace's team decides billing when contract language is vague",
    "One-time implementation fee includes 60-day opt-out period",
    "Tabs system creates line items per automation with editable names and dates",
    "Tabs system books implementation fee at first workflow launch",
    "Usage-based billing is being phased out entirely",
    "Future state: standardized flat annual SaaS contracts with limited usage overage carve-outs",
    "2-3 customers on deprecated per-automation model are being transitioned"
  ],
  "exceptions": [
    "Revenue recognition dates can be overridden if needed (despite following automation launch dates by default)",
    "Grace's team handles refunds and opt-outs manually if triggered (for implementation fees)",
    "60-day opt-out period applies to one-time implementation fee (exception to general no opt-out rule)",
    "Limited usage overage carve-outs allowed in future standardized model (exception to flat-fee structure)",
    "Contract language vagueness requires manual billing decision by Grace's team"
  ],
  "merchant_specific": [
    "Grace as key person (preparing for maternity leave - requires de-risking)",
    "Tabs system (specific billing/invoicing platform used)",
    "QuickBooks integration requirement",
    "Three-tier billing model evolution: Legacy (deployment milestone + usage/flat-fee/annual mix), Current (hybrid with 10-15 active deployments), Future (standardized flat annual)",
    "High-touch implementation support as success criterion",
    "Flexible ingestion and override of contracts usage",
    "Grace's team as approval authority for invoices and billing decisions",
    "Per-automation billing structure with editable names and dates",
    "Specific customer count metrics (10-15 active, 2-3 being deprecated)"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: LuminAI Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:14

### Original Content
```
Merchant: Luminai Demo date: Aug 25, 2025 Scoping start date: Sep 4, 2025 MSA Signature Date: Sep 9, 2025 Onboarding Kick Off Date: TBD (target Sep 2025) [If Exists] Opt Out Date: None Go Live Date: TBD Tabs Team GTM POC: Jarrett Martin Implementation POC: Marshall Budin (Solutions Consultant) Tech Stack ERP: QuickBooks (managed via Pilot; plan to transition to internal ownership) Tax Integration: None (no third-party tax software currently) Other systems: Brex (banking), Ramp (expenses), Bill c...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Stakeholder Management",
    "Technology Infrastructure and System Integration",
    "Revenue Recognition and Financial Operations",
    "Pain Points and Solution Requirements",
    "Organizational Structure and Key Personnel"
  ],
  "rules": [
    {
      "rule": "Implementation follows structured phases: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "explicit",
      "category": "process"
    },
    {
      "rule": "GTM POC and Implementation POC must be assigned for each merchant engagement",
      "type": "explicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Tech stack documentation must include ERP, Tax Integration, and Other Systems",
      "type": "explicit",
      "category": "technical_requirements"
    },
    {
      "rule": "Key people documentation must identify Accountant and Finance POC at minimum",
      "type": "explicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Goals must address: merchant's objective, pain points being solved, and reason for purchasing Tabs",
      "type": "explicit",
      "category": "business_requirements"
    },
    {
      "rule": "Solution must support hybrid contract types including milestones, usage-based, and flat SaaS models",
      "type": "implicit",
      "category": "product_requirements"
    },
    {
      "rule": "Solution must provide monthly close capabilities with accurate revenue recognition",
      "type": "explicit",
      "category": "financial_operations"
    },
    {
      "rule": "Solution must include cash forecasting and collection visibility features",
      "type": "explicit",
      "category": "financial_operations"
    },
    {
      "rule": "Implementation must accommodate merchants transitioning from outsourced to internal finance management",
      "type": "implicit",
      "category": "change_management"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date can be 'None' if merchant has not opted out",
      "condition": "Optional field based on merchant status"
    },
    {
      "exception": "Onboarding Kick Off Date and Go Live Date may be 'TBD' during early stages",
      "condition": "Dates not yet determined in planning phase"
    },
    {
      "exception": "Tax Integration may be 'None' if merchant has no third-party tax software",
      "condition": "Not all merchants use tax integration tools"
    },
    {
      "exception": "ERP may be managed by third-party provider with planned transition to internal ownership",
      "condition": "Transitional arrangements for financial system management"
    },
    {
      "exception": "Accountant may be outsourced provider rather than internal resource",
      "condition": "Finance function structure varies by merchant"
    },
    {
      "exception": "Single individual may serve as both decision maker and power user",
      "condition": "Smaller finance teams with consolidated responsibilities"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and branding (Luminai Demo vs LuminAI)",
      "customization_needed": "Merchant-specific naming conventions"
    },
    {
      "element": "Specific dates for implementation milestones",
      "customization_needed": "Timeline varies per merchant engagement"
    },
    {
      "element": "Named POCs (Jarrett Martin, Marshall Budin, Grace Buckingham)",
      "customization_needed": "Contact persons unique to each merchant"
    },
    {
      "element": "Tech stack composition (QuickBooks, Brex, Ramp, Bill.com, Monday.com, Salesforce, DocuSign)",
      "customization_needed": "System landscape varies significantly by merchant"
    },
    {
      "element": "Third-party service providers (Pilot for accounting)",
      "customization_needed": "Vendor relationships unique to each merchant"
    },
    {
      "element": "Business model details (custom AI-enabled automation for healthcare)",
      "customization_needed": "Industry, product type, and customer base vary"
    },
    {
      "element": "Company stage and size (Series B, $5-10M ARR)",
      "customization_needed": "Growth stage and revenue scale differ"
    },
    {
      "element": "Contract types and revenue models (milestones, usage, flat SaaS)",
      "customization_needed": "Pricing and billing models are merchant-specific"
    },
    {
      "element": "Specific pain points (single-threaded ownership, manual work)",
      "customization_needed": "Operational challenges unique to each organization"
    },
    {
      "element": "Finance team structure and responsibilities",
      "customization_needed": "Organizational design varies by merchant"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: LuminAI Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:21

### Original Content
```
Usage with workflow   aggregate minimums (true-ups) 2-3 customer being deprecated Tabs computes both per-workflow and aggregate-minimum true-ups; your team applies business rules (e g , avoid double-charging when aggregate minimum is met) Usage data flow starts with monthly CSV uploads (consolidated or line-item); note the source per customer; API can come later Prepaid usage drawdown 2-3 customer being deprecated Backend supports setting the prepaid bucket; monthly burn-down and overage are cal...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Usage-based billing and true-up calculations",
    "Prepaid usage drawdown and overage management",
    "Customer creation and deployment tracking workflow",
    "Contract structure with multiple workflows and independent terms",
    "Data flow and integration processes (CSV uploads, API)"
  ],
  "rules": [
    "Tabs system computes both per-workflow and aggregate-minimum true-ups",
    "Business rules must be applied to avoid double-charging when aggregate minimum is met",
    "Usage data flow starts with monthly CSV uploads (consolidated or line-item format)",
    "Source must be noted per customer for usage data",
    "Backend must set prepaid bucket for prepaid usage customers",
    "Monthly burn-down and overage are calculated and made visible",
    "Customers must be created manually in QuickBooks and Bill.com",
    "Deployment milestones must be tracked in Monday.com and Slack",
    "Manual verification required before invoicing",
    "Each workflow within a contract has independent launch dates and 12-month service terms",
    "Renewals prorate workflows to align terms in year two",
    "New contracts do not include opt-out validation periods"
  ],
  "exceptions": [
    "Workflow aggregate minimums (true-ups) feature being deprecated for 2-3 customers",
    "Prepaid usage drawdown being deprecated for 2-3 customers",
    "Zero-dollar statements can be sent for visibility or kept internal (optional)",
    "API integration can come later (CSV is initial method)",
    "Older contracts included opt-out validation periods (grandfathered)",
    "Remaining balance display on front end is in progress (not yet available)"
  ],
  "merchant_specific": [
    "Business rules for avoiding double-charging (team-specific logic)",
    "Choice between consolidated or line-item CSV format",
    "Decision to send $0 statements or keep internal",
    "Customer creation process using QuickBooks and Bill.com (specific tools)",
    "Deployment tracking using Monday.com and Slack (specific platforms)",
    "Contract structure with multiple workflows (merchant's service model)",
    "12-month service term standard (merchant-specific term length)",
    "Proration approach for renewal alignment (merchant's renewal policy)",
    "Opt-out validation period policy changes (merchant's contract evolution)"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 4: LuminAI Merchant Info Sheet__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:31

### Original Content
```
One-off Things to Know Grace is single-threaded owner of all finance work QuickBooks data is messy due to Pilot s long tenure; Grace would prefer to start fresh rather than import historic QBO mess Prior billing platforms (Metronome, Stripe) failed due to inflexibility and data mismatches Expect Tabs to provide high-touch implementation and flexibility with overrides, contract ingestion, and integrations Large enterprise customers may require invoicing through their own AP portals (Tabs must sup...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Workflow Usage Fees and Event-Based Billing",
    "Integration and Data Management",
    "Customer-Specific Implementation Requirements",
    "Communication and Notification Protocols"
  ],
  "rules": [
    "All Workflow Usage Fees must have Usage AI turned on",
    "Annual Platform Fees are billed annually with 1 period if service term is 12 months",
    "Workflow Usage Fees are billed monthly",
    "Default payment terms are net 30 days unless specified otherwise",
    "Default service term is 12 months unless specified otherwise",
    "Default billing start date is the effective date (date last signed)",
    "Payment terms can be found under 'Payment of Fees and Billing' section in MSA",
    "Billing triggers (BTs) for Workflow Usage Fees are located under 'Fees and Payment Terms' in MSA",
    "Service term can be found next to 'Term' in MSA",
    "If a minimum is specified for usage fees, set it; ignore maximum if minimum is required",
    "For Workflow Usage Fees: billing type is Unit Price and price is cost per use",
    "Event names should match the Workflow Usage Fees name (e.g., 'QA Interaction Audit', 'Fraud UAR')",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Tabs must support off-platform invoices for large enterprise customers with their own AP portals",
    "Customer must manually update dates and revenue schedules in Tabs or send emails to contract-ingest@tabs.com",
    "Tabs will not automate revenue schedule updates unless customer owns all APIs for pushing data"
  ],
  "exceptions": [
    "QuickBooks data should not be imported due to historical messiness from prior vendor (Pilot)",
    "Ignore maximum usage limits if a minimum is required",
    "Large enterprise customers may require invoicing through their own AP portals (off-platform)",
    "Special handling may be required for certain integration items based on merchant specifications",
    "Specific customers may require special memos or invoice changes due to merchant-customer relationships",
    "LuminAI deal uses automation-based pricing model: $50,000 per automation upon completion (non-standard billing)",
    "Software Subscription Bundle label for Pinata can be overridden if merchant specifies otherwise"
  ],
  "merchant_specific": [
    "Grace Buckingham is single-threaded owner of all finance work",
    "Merchant expects high-touch implementation and flexibility with overrides",
    "Merchant requires contract ingestion support",
    "Prior billing platforms (Metronome, Stripe) failed due to inflexibility",
    "Notification protocol: Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase",
    "Merchant-specific integration labeling rules (Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
    "Workflow Usage Fees terminology and naming conventions specific to merchant's product",
    "LuminAI customer deal structure: $500,000 for 10 workflow automations, billed at $50,000 per completion",
    "Merchant uses MSA (Master Service Agreement) document structure with specific section names",
    "Contract ingestion email: contract-ingest@tabs.com"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 5: LuminAI Merchant Info Sheet__chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:36

### Original Content
```
Extra commentary: Gong Call On the follow-on contract, Luminai will include a credit for the amount of the initial contract that customer was not live for Example: Contract started 1 1 2025 Workflow went live 7 1 2025 Charged  50k on 7 1 2025 New Contract 1 1 2026 This workflow will be only charged  25k for 1 1 2026 - 12 31 2026 Workflow Model 2   Usage-Based Products Gong Call Link Limited to  3 4 legacy deals 5 usage-based products: each with individual minimums   a combined usage minimum Tabs...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract credits and proration for delayed workflow implementation",
    "Usage-based pricing models with minimum commitments",
    "System limitations in hybrid true-up calculations",
    "API integration and data ingestion workflows",
    "Custom field requirements for operational continuity"
  ],
  "rules": [
    "Follow-on contracts must include credits for periods when customer was not live during initial contract",
    "Credit calculation: charge only for the live period in the renewal contract (prorated based on go-live date)",
    "Usage-based products require both individual minimums per product AND a combined usage minimum",
    "Tabs system cannot calculate hybrid true-ups across multiple products simultaneously",
    "True-up calculations must be performed separately or individually, not in hybrid mode",
    "Both true-up options must be displayed on products page for manual selection",
    "LuminAI must manually delete the non-selected true-up option before invoice send",
    "No APIs will be built upfront for usage data ingestion into Metronome",
    "If APIs are pursued later, LuminAI (not the vendor/Tabs) must own the API development",
    "A custom field labeled 'Usage Data Source' must be added per customer in Tabs",
    "Usage Data Source field is informational only with no functional automation"
  ],
  "exceptions": [
    "Credit arrangement applies specifically to follow-on/renewal contracts where initial implementation was delayed",
    "Usage-based model is limited to 3-4 legacy deals only (not standard for all customers)",
    "Manual true-up selection process is a workaround due to system limitation (not standard workflow)",
    "No-API-upfront policy is based on customer's poor prior experience (customer-specific decision)",
    "API ownership by LuminAI (if built later) deviates from typical vendor-built integration pattern"
  ],
  "merchant_specific": [
    "Luminai/LuminAI - merchant name with inconsistent capitalization",
    "Metronome - specific billing/usage tracking system mentioned",
    "Tabs - appears to be the billing/invoicing platform being configured",
    "Workflow Model 2 - specific product or service tier",
    "5 usage-based products - specific to this merchant's product catalog",
    "Combined usage minimum - merchant-specific pricing structure",
    "Grace - appears to be a stakeholder who approved the manual workaround",
    "Gong Call references - merchant uses Gong for call recording/documentation",
    "Usage Data Source field - custom field specific to merchant's operational needs"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 6: LuminAI Merchant Info Sheet__chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:43

### Original Content
```
Final Notes   Callouts Deal closed with explicit scoping clarity: No automation for workflow-based billing No hybrid true-up calculations No Tabs-owned API buildout Customer expectations are well set; Grace aligned on constraints and comfortable moving forward Call out for implementation team: add custom field for  Usage Data Source  to customer records
```

### LLM Analysis Response
```json
{
  "themes": [
    "Deal Scoping and Limitations",
    "Customer Expectation Management",
    "Implementation Requirements",
    "System Customization and Data Tracking",
    "Workflow and Automation Boundaries"
  ],
  "rules": [
    {
      "rule": "No automation for workflow-based billing shall be implemented",
      "type": "explicit_constraint",
      "category": "billing_automation"
    },
    {
      "rule": "No hybrid true-up calculations are to be performed",
      "type": "explicit_constraint",
      "category": "billing_calculations"
    },
    {
      "rule": "No Tabs-owned API buildout will be provided",
      "type": "explicit_constraint",
      "category": "technical_integration"
    },
    {
      "rule": "Custom field 'Usage Data Source' must be added to customer records",
      "type": "implementation_requirement",
      "category": "data_management"
    },
    {
      "rule": "Deal scope must be explicitly documented and communicated to customer",
      "type": "implicit_process",
      "category": "customer_management"
    },
    {
      "rule": "Customer expectations must be set and confirmed before deal closure",
      "type": "implicit_process",
      "category": "customer_management"
    }
  ],
  "exceptions": [
    {
      "exception": "This deal explicitly excludes standard automation features that may be available in other implementations",
      "context": "workflow-based billing automation"
    },
    {
      "exception": "Hybrid true-up calculations are excluded despite potentially being a standard billing feature",
      "context": "billing methodology"
    },
    {
      "exception": "API development responsibility remains with customer (not Tabs-owned)",
      "context": "technical integration approach"
    }
  ],
  "merchant_specific": [
    {
      "element": "Grace",
      "type": "customer_contact_name",
      "note": "Primary stakeholder who has been aligned on constraints"
    },
    {
      "element": "Usage Data Source",
      "type": "custom_field_name",
      "note": "Specific field name for tracking data source in customer records"
    },
    {
      "element": "Tabs",
      "type": "vendor_organization_name",
      "note": "The service provider organization referenced in API ownership"
    },
    {
      "element": "Workflow-based billing",
      "type": "billing_methodology",
      "note": "Specific billing approach that is explicitly excluded"
    },
    {
      "element": "Hybrid true-up calculations",
      "type": "calculation_methodology",
      "note": "Specific calculation approach that is explicitly excluded"
    }
  ],
  "confidence_score": 0.85
}
```

---

