# Raw LLM Analysis: Dosespot - Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:55:39

---

## Chunk 1: Dosespot - Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:39

### Original Content
```
Merchant 026 Demo date: Sep 13th, 2024 Scoping start date: Sep 13, 2024 MSA Signature Date: Sep 24, 2024 Onboarding Kick Off Date: Oct 1, 2024 [If Exists] Opt Out Date: N A Go Live Date: Dec 9, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Controller: Derrick Rankin Head of FP A: David Leite CFO: Tosin Adesegha Account Receivable POC: David Billing POC: Derrick Company summary (AE to fill) DoseSpot is a Surescripts certified e-Prescribing platform specifically de...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Billing Model and Pricing Structure",
    "Contract Processing and Revenue Recognition",
    "Merchant Business Context and Goals",
    "Pricing Components and Exclusions"
  ],
  "rules": [
    "Monthly billing occurs in arrears for subscription fees",
    "Tiered usage pricing is billed in arrears",
    "Pricing information must be extracted from Exhibit A of the MSA",
    "Fixed monthly fee equals subscription fee and is billed monthly in arrears",
    "Contracts must be assigned to a customer during processing",
    "The lower priced table in pricing documentation is for Non-EPCS prescribers",
    "The higher priced table in pricing documentation is for EPCS prescribers",
    "EPCS Certification or Re-certification data should be ignored during pricing extraction",
    "Hardware tokens data should be ignored during pricing extraction",
    "Pricing extraction must include: Fixed monthly fee, EPCS Prescribers, Non-EPCS Prescribers, Prescription Agents, Prescriptions, and Identity Proofing"
  ],
  "exceptions": [
    "Pricing tables often contain typos that must be accounted for",
    "Regardless of text labels shown, pricing table position (lower vs higher) determines prescriber type classification",
    "No opt-out clause exists for this merchant (Merchant 026)",
    "Opt Out Date is marked as N/A for this merchant"
  ],
  "merchant_specific": [
    "Merchant ID: 026",
    "Company Name: DoseSpot",
    "Industry: Healthcare IT (e-Prescribing platform)",
    "ERP system (to be specified)",
    "Tax Integration method (to be specified)",
    "Key personnel: Controller (Derrick Rankin), Head of FP&A (David Leite), CFO (Tosin Adesegha), Account Receivable POC (David), Billing POC (Derrick)",
    "GTM POC and Implementation POC (to be assigned)",
    "Specific timeline: Demo (Sep 13, 2024), MSA Signature (Sep 24, 2024), Kick Off (Oct 1, 2024), Go Live (Dec 9, 2024)",
    "Merchant goals: Tabs usage data upload, contract management, attachment of receipts to invoices, customized Rev Rec reporting",
    "Product-specific terminology: EPCS (Electronic Prescribing of Controlled Substances), Prescribers, Prescription Agents, Identity Proofing, Surescripts certification"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Dosespot - Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:39

### Original Content
```
Monthly fee often includes 10 free prescribers If so, adjust the contracted tiers of prescribers to be 10 higher than the contract states For example: Contract says 0-100 prescribers is  10 and 101-1000 prescribers is  8 Contract also says 10 prescribers free Process this as 11-110 prescribers at  10, and 111-1010 prescribers at  8 Do not include a tier for the free included amount of prescribers There is usually also tiered pricing associated with Non-EPCS prescribers (NON-EPCS), EPCS prescribe...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tiered pricing structure for prescribers with free tier adjustments",
    "Differentiation between EPCS and Non-EPCS prescriber pricing",
    "Unit pricing for various service components (prescriptions, agents, ID proofing)",
    "Billing term configuration and completeness requirements",
    "Price transparency through description field documentation"
  ],
  "rules": [
    "Monthly fee typically includes 10 free prescribers",
    "When free prescribers are included, adjust contracted tiers by adding 10 to the prescriber count ranges",
    "Do not create a separate tier for the free included prescribers amount",
    "Tiered pricing exists for Non-EPCS prescribers, EPCS prescribers, and prescriptions (RX)",
    "All tiered pricing must include the unit price in the description field",
    "If contract contains only Non-EPCS or only EPCS pricing, duplicate that pricing for the missing category",
    "When EPCS and Non-EPCS are treated the same, create billing terms for both to ensure complete billing",
    "Unit pricing must be configured for prescription agents (AGENTS)",
    "Unit pricing must be configured for ID Proofing (IDP)",
    "All unit pricing should include the unit price in the description field"
  ],
  "exceptions": [
    "Some contracts only contain Non-EPCS pricing (not both types)",
    "Some contracts only contain EPCS pricing (not both types)",
    "When only one prescriber type pricing exists, use same pricing for both types rather than leaving one blank",
    "The standard 10 free prescribers may not apply to all contracts (indicated by 'often' and 'If so' language)"
  ],
  "merchant_specific": [
    "Number of free prescribers included in monthly fee (default is 10 but may vary)",
    "Specific tier breakpoints for prescriber counts (example shows 0-100 and 101-1000)",
    "Specific unit prices for each tier level (example shows $10 and $8)",
    "Whether contract treats EPCS and Non-EPCS prescribers the same or differently",
    "Presence or absence of prescription agents (AGENTS) pricing",
    "Presence or absence of ID Proofing (IDP) pricing",
    "Specific unit prices for RX, AGENTS, and IDP components"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Dosespot - Merchant Info Sheet__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:48

### Original Content
```
rewatch com video 3w2vfbt6yhly27o6-dosespot-tabs-demo-september-10-2024 9 13 24 - Custom Demo https: tabs rewatch com video sw57nnmbql1u8zxz-dosespot-tabs-september-13-2024 9 17 24 - Check In call https: tabs rewatch com video b02eac0296y1tp57-dosespot-tabs-check-in-september-17-2024 9 19 24 - Netsuite Scoping https: tabs rewatch com video 0iq2dp0dxbxvpfu3-dosespot-tabs-netsuite-scoping-september-19-2024 9 20 24 - Referral Call with Joe from OpenClinica https: tabs rewatch com video td22m9oopx7k...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting and call documentation tracking",
    "Merchant billing methodology and data management",
    "Merchant relationship assessment and stakeholder management",
    "Usage-based tiered pricing structure",
    "Implementation and operational workflow coordination"
  ],
  "rules": [
    "Usage data must be pulled on a monthly basis",
    "Spreadsheets are required for tracking usage data",
    "Master Excel file must contain all client data",
    "Number of prescribers must be broken out per prescriber in Excel",
    "Tiered unit pricing model is applied based on usage",
    "Receipts of usage data must be attached to each invoice before sending",
    "International Team in Ops should ignore certain sections marked for AE and Implementation",
    "Documentation must include merchant temperament assessment",
    "Key POC (buyer/decision maker) must be identified and documented"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' are specifically excluded from international operations team review",
    "AE and Implementation teams have specific sections designated for their completion only"
  ],
  "merchant_specific": [
    "Merchant temperament characterization (e.g., 'Very calm and open to figuring out solutions together')",
    "Specific stakeholder types (e.g., 'Technical stakeholders')",
    "Merchant-specific motivation factors (e.g., 'wanted to work with our team to get rid of their billing headaches')",
    "Number of prescribers (varies by merchant)",
    "Tiered pricing structure (likely customized per merchant agreement)",
    "Key POC identification (unique to each merchant)",
    "Meeting cadence and types (Custom Demo, Check In, Scoping, Referral calls)"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Dosespot - Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:55:52

### Original Content
```
If there is an implementation fee, it is billed on the signature date This step can be skipped for old contracts (anything uploaded before Nov 1, 2024) because they have already been billed NEW: Add an additional revenue schedule and billing term for  Included Prescribers This will be UNIT_PRICE with Event to track  FREE  and will be  0 each [ ] Anything to ignore in contracts Ignore pricing related to Certification, Re-Certification, and Hardware Tokens Specifics processing things the merchant ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing configuration",
    "Service term and payment terms defaults",
    "Event-based pricing and tracking",
    "Contract implementation and fee processing",
    "Healthcare-specific prescriber and prescription tracking"
  ],
  "rules": [
    "Implementation fees are billed on the signature date",
    "Old contracts (uploaded before Nov 1, 2024) skip implementation fee billing as already billed",
    "Add revenue schedule for Included Prescribers with UNIT_PRICE event tracking set to FREE at $0 each",
    "Ignore pricing for Certification, Re-Certification, and Hardware Tokens",
    "Default service term is one year starting first day of current month with MONTHLY frequency and 12 invoice duration",
    "Default payment terms are Net 15 unless implementation SKU specifies DUE ON RECEIPT (then use Net 0)",
    "Default billing frequency is Monthly",
    "No taxes are applied as line items",
    "Invoice date defaults to first day of month when signature date is within that month (e.g., Nov 7 signature → Nov 1 billing date)",
    "Auto-attach usage data to invoices showing number of prescriptions for each invoice"
  ],
  "exceptions": [
    "Old contracts uploaded before Nov 1, 2024 are exempt from implementation fee billing",
    "Net 0 payment terms apply when implementation SKU contains DUE ON RECEIPT language (overrides default Net 15)",
    "Merchant-specific requests may override standard processing (e.g., back-dating invoice dates to final day of month)",
    "Certification, Re-Certification, and Hardware Token pricing should be excluded from processing"
  ],
  "merchant_specific": [
    "Event types tracked: NON-EPCS prescribers, EPCS prescribers, Prescriptions (RX), Prescription Agents (AGENTS), ID Proofing (IDP)",
    "Custom feature request: Monthly usage data attachment showing prescription counts",
    "Integration items processing (specific items not detailed in this chunk)",
    "Professional services work planned with eventual automation goal",
    "Current manual process takes 3 days monthly (performed by Derrick)",
    "Healthcare/pharmaceutical industry context (prescribers, EPCS compliance, prescriptions)",
    "Merchant may request custom invoice date handling (e.g., back-dating to month end)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: Dosespot - Merchant Info Sheet__chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:56:02

### Original Content
```
) Derrick and David are main stakeholders Rebecca knows CFO, Tosin, personally 3) What are the Tabs features that the key POC cares about Invoicing, usage upload, receipt attachment, reporting, rev rec Item Name   Integration Item   Event to Track EPCS Prescribers   216 1U-EPCS   EPCS Non-EPCS Prescribers   218 1U-NONEPCS   Non-EPCS Agents   430 1U-AGENT   Agents Prescriptions   221 1RX   Rx ID Proofing   410 IDPROOF   IDP Included Prescribers   433 1U-NONEPCS - First 10 Included   FREE Jumpstar...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Relationships",
    "Product Feature Prioritization (Tabs platform)",
    "Healthcare/Pharmacy Service Item Catalog",
    "Usage Tracking and Billing Integration",
    "EPCS (Electronic Prescribing of Controlled Substances) Classification"
  ],
  "rules": [
    "EPCS prescribers are tracked separately from Non-EPCS prescribers with distinct item codes (216 vs 218)",
    "First 10 Non-EPCS prescribers are included free of charge (Item 433)",
    "Each service type requires specific integration item codes and event tracking identifiers",
    "Prescriptions are tracked per Rx ID using item code 221",
    "ID Proofing is a separate billable service with item code 410",
    "Agents are tracked separately from prescribers using item code 430",
    "Jumpstart Subscription includes 10 users and uses item code 232"
  ],
  "exceptions": [
    "First 10 Non-EPCS prescribers are marked as 'FREE' and 'Included' (Item 433: 1U-NONEPCS - First 10 Included)",
    "Rebecca has a personal relationship with CFO Tosin, which may affect communication channels or decision-making processes",
    "Derrick and David are identified as 'main stakeholders' suggesting elevated priority in engagement"
  ],
  "merchant_specific": [
    "Stakeholder names: Derrick, David, Rebecca, Tosin (CFO)",
    "Key features for this POC: Invoicing, usage upload, receipt attachment, reporting, revenue recognition (rev rec)",
    "Healthcare/pharmacy-specific terminology: EPCS, prescribers, prescriptions, Rx ID, agents",
    "Item naming convention appears merchant-specific (1U-EPCS, 1U-NONEPCS, 1RX, etc.)",
    "Integration between Tabs platform and healthcare prescribing system",
    "Jumpstart subscription tier specific to this merchant's offering"
  ],
  "confidence_score": 0.72
}
```

---

