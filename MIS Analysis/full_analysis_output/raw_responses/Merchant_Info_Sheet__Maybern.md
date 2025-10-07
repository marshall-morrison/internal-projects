# Raw LLM Analysis: Merchant Info Sheet_ Maybern

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:10:55

---

## Chunk 1: Merchant Info Sheet_ Maybern_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:10:55

### Original Content
```
Merchant Demo date: Scoping start date: Jun 20, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Jul 1, 2024 [If Exists] Opt Out Date: Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: John Bowman, Chief Business Officer CFO: John Bowman, Chief Business Officer Customer service rep who is really involved: Bryan Champ, SVP of Sales Account Receivable POC: accounting maybern com Billing POC: accounting maybern com Company...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Stakeholder Identification and Roles",
    "Business Goals and Pain Points",
    "System Integration and Migration",
    "Relationship Management and Merchant Temperament"
  ],
  "rules": [
    "MSA Signature Date must be captured for all merchants",
    "Onboarding Kick Off Date should be scheduled after MSA signature",
    "Go Live Date must be documented",
    "GTM POC and Implementation POC must be identified",
    "ERP and Tax Integration systems must be documented",
    "Key stakeholders must be identified: Accountant, CFO, Customer Service Rep, AR POC, and Billing POC",
    "Company summary must describe merchant's business model and services",
    "North star goals must document: merchant's goal, pain points being solved, and reason for purchasing",
    "AE Notes should capture relationship information and merchant temperament",
    "Demo date and Scoping start date should be tracked when applicable",
    "Opt Out Date should be tracked if it exists"
  ],
  "exceptions": [
    "Opt Out Date is conditional - only tracked '[If Exists]'",
    "Demo date and Scoping start date may not always be applicable or available",
    "In this case, the CFO and Accountant are the same person (John Bowman), which may be atypical for enterprise merchants",
    "John Bowman was hired part-time but works practically full-time, indicating flexible role definitions"
  ],
  "merchant_specific": [
    "Merchant name and business description (Maybern - investment management software)",
    "Specific dates for all milestones (Demo, MSA, Kick Off, Go Live)",
    "Individual names and titles of key personnel",
    "Contact email addresses (accounting@maybern.com format)",
    "Specific pain points (currently using Sheets/Google Drive for contract repository)",
    "Specific use cases (contract repository, invoicing, reporting, AR operations)",
    "Relationship context (fellow primary PortCo, temperament assessment)",
    "Current systems being replaced (Google Sheets, Google Drive)",
    "Scope of Tabs usage (all invoicing, reporting, finance operations for AR)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet_ Maybern_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:10:56

### Original Content
```
2) Is there a key POC for the buyer decision maker John Bowman, Chief Business Officer, and Bryan Champ, SVP of Sales 3) What are the Tabs features the key POC cares about Contract Storage, Invoicing, Reporting, Usage Data upload Billing model Info on how merchant bills Quarterly with usage data (they take a Basis Point percentage on fund size How contract is broken up Implementation fee, quarterly billing on usage data, multi year contracts One off things to know about merchant One person finan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Setup and Structure",
    "Billing and Payment Processing",
    "Implementation Fee Management",
    "Usage-Based Billing and AUM Calculations",
    "Customer Account Hierarchy and Organization"
  ],
  "rules": [
    "For new customers, create both a parent and sub account, with sub being the fund name",
    "Create BTs (billing terms) under the subcustomer level",
    "Each fund requires its own BT for implementation fees",
    "Implementation fees are split into two 50% payments",
    "First set of implementation BTs start on effective date, second set start on access start date",
    "If access start date not specified in contract, default to 6 months from effective date",
    "Usage-based billing follows simple percentage stated in contract",
    "Ignore fund estimates in contracts as these are usage-based terms calculated quarterly",
    "Default service term is 1 year if none listed",
    "Default net payment terms is 0 days if none listed",
    "Default billing frequency is quarterly (except implementation which is 2 invoices 6 months apart)",
    "Every tax line item becomes a separate BT if not otherwise specified",
    "For tiered basis point models, only process the first tier and ignore subsequent tiers",
    "Basis point structure is calculated per year (e.g., 1 basis point = 0.01% annually)",
    "Fund Service Fee BTs must include: Title with fund name, Integration item 'Fund Service Fee', Amount as percentage reflecting basis point"
  ],
  "exceptions": [
    "Sometimes contracts have 2 documents (MSA and Order Form) - MSA contains payment terms, Order Form contains billing terms",
    "Merchant is attempting to consolidate into single document when possible but may not always succeed",
    "Implementation fee payment schedule may be outlined in contract, overriding the default 6-month spacing",
    "Usage-based terms can be stated in different formats: in a chart with basis points, in a paragraph as percentage, or as a tiered model",
    "Tiered pricing models exist but only first tier should be processed"
  ],
  "merchant_specific": [
    "Key POCs: John Bowman (Chief Business Officer) and Bryan Champ (SVP of Sales)",
    "Merchant cares about: Contract Storage, Invoicing, Reporting, Usage Data upload",
    "Billing model: Quarterly with usage data using basis point percentage on fund size",
    "Contract structure: Implementation fee + quarterly billing on usage data + multi-year contracts",
    "Merchant has one-person finance team",
    "Merchant manually pulls fund size usage data into CSV for upload",
    "Currently only has 5 contracts",
    "Uses AST Events Processing for usage-based billing to calculate AUM (Assets Under Management) fees",
    "Specific terminology: 'Fund Service Fee', 'AUM fee', 'basis point on fund size'",
    "Previous process used '0.000025 per unit' calculation which is now replaced with simple percentage method"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet_ Maybern_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:11:06

### Original Content
```
com video 035bd5l6jtkqqic6-bryan-and-rebecca-schwartz-tabs-june-5-2024 June 26th, 2024 Proposal Review https: tabs rewatch com video hf04vcnv4a5627a0-maybern-tabs-proposal-sync-june-26-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Video documentation and meeting records",
    "Proposal review and synchronization processes",
    "Client engagement tracking (Bryan and Rebecca Schwartz, Maybern)",
    "Tabs platform usage for video management"
  ],
  "rules": [],
  "exceptions": [],
  "merchant_specific": [
    "Client names: Bryan and Rebecca Schwartz, Maybern",
    "Tabs platform (tabs.rewatch.com) - specific video management system",
    "Video identifiers: 035bd5l6jtkqqic6, hf04vcnv4a5627a0",
    "Meeting types: Proposal Review, Proposal Sync",
    "Date references: June 5, 2024 and June 26, 2024"
  ],
  "confidence_score": 0.3
}
```

**Explanation of Low Confidence Score:**

This document chunk appears to be metadata or reference links to video recordings rather than actual instruction content. It contains:
- Video URLs from a platform called "Tabs/Rewatch"
- Client/meeting names
- Dates

However, it does **not** contain:
- Actual instructions, policies, or procedures
- Rules or requirements to follow
- Guidelines or standards
- Actionable directives

The content seems to be a fragment of a larger document, possibly a meeting notes header or video archive reference list. Without the actual instructional content from these videos or associated documentation, it's impossible to extract meaningful rules or patterns. A proper analysis would require access to the actual meeting content or accompanying instruction documents.

---

## Chunk 4: Merchant Info Sheet_ Maybern_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:11:14

### Original Content
```
000025 (1 basis point 4 quarterly payments) 75 basis point   0 00001875 ( 75 basis point 4 quarterly payments) 5 basis point   0 0000125 ( 5 basis point 4 quarterly payments)  BE SURE TO UNCHECK  IS BILLED IN ARREARS  These are NOT billed in arrears Quarterly billing cadence The first fund service fee should go out right after the 2nd implementation fee Because usage bills are in arrears, the period start date for these terms should be 3 months prior to the 2nd implementation fee invoice date Fo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Configuration and Cadence",
    "Fee Structure and Basis Points Calculation",
    "Invoice Timing and Sequencing",
    "Integration and Processing Workflow",
    "Customer-Specific Invoice Customization"
  ],
  "rules": [
    {
      "rule": "Basis point calculations must be divided by 4 for quarterly payments",
      "details": "25 basis points = 0.0000625, 75 basis points = 0.00001875, 5 basis points = 0.0000125"
    },
    {
      "rule": "Must uncheck 'IS BILLED IN ARREARS' for fund service fees",
      "details": "These fees are explicitly NOT billed in arrears"
    },
    {
      "rule": "Quarterly billing cadence is required",
      "details": "All fees follow a quarterly payment schedule"
    },
    {
      "rule": "First fund service fee must be issued immediately after the 2nd implementation fee",
      "details": "Timing sequence: 2nd implementation fee, then fund service fee"
    },
    {
      "rule": "Usage bill period start dates must be 3 months prior to 2nd implementation fee invoice date",
      "details": "Example: If 2nd implementation invoices on 5/31, usage BTs start from 3/1, first invoice on 6/1"
    },
    {
      "rule": "Usage BTs are assigned to Fund Service Fee integration items",
      "details": "Specific assignment rule for integration processing"
    },
    {
      "rule": "Implementation fees are assigned to Implementation Fee integration items",
      "details": "Separate integration item assignment from usage fees"
    },
    {
      "rule": "Implementation fees are non-taxable by default",
      "details": "Can be changed to taxable if tax needs to be charged"
    },
    {
      "rule": "No post-processing notifications required to Ops Team",
      "details": "Team does not need to be notified upon completion of processing batches"
    },
    {
      "rule": "Logo must be included on invoices",
      "details": "Merchant requires branding on all invoices"
    },
    {
      "rule": "Contract duration is one year",
      "details": "Merchant is contracted for annual terms"
    }
  ],
  "exceptions": [
    {
      "exception": "Tax status can be changed from non-taxable to taxable on implementation fees",
      "condition": "If tax needs to be charged"
    },
    {
      "exception": "Some customers require BTs separated into different invoices",
      "condition": "Customer-specific requirement, currently being worked on with no Ops instructions yet"
    },
    {
      "exception": "Special memos may be required on certain invoices",
      "condition": "Depends on specific customer requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationships",
      "condition": "Relationship-dependent modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Basis point fee structure",
      "customization": "Specific rates: 25, 75, and 5 basis points with quarterly division"
    },
    {
      "element": "Invoice timing sequence",
      "customization": "Specific sequence with 2nd implementation fee as trigger point"
    },
    {
      "element": "Logo requirement",
      "customization": "Merchant-specific branding on invoices"
    },
    {
      "element": "Customer invoice separation",
      "customization": "Some customers need separate invoices for different BTs (billing terms)"
    },
    {
      "element": "Feature request for renewal escalation",
      "customization": "Need visibility into contract end dates and key dates (medium urgency)"
    },
    {
      "element": "Integration item assignments",
      "customization": "Specific mapping: Usage BTs to Fund Service Fee, Implementation to Implementation Fee"
    },
    {
      "element": "Terminology",
      "customization": "Uses 'BTs' (billing terms), 'Fund Service Fee', 'Implementation Fee'"
    }
  ],
  "confidence_score": 0.85
}
```

---

