# Raw LLM Analysis: Merchant Info Sheet - Carbon Direct

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:03:08

---

## Chunk 1: Merchant Info Sheet - Carbon Direct_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:03:08

### Original Content
```
pmirDemo date: Jun 11, 2024 Scoping start date: Jun 14, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Aug 1, 2024 [If Exists] Opt Out Date: Go Live Date: Sep 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Jessica Isaacs - VP of Finance Jeff Bennet - Senior Accounting Manager (and primary user) Company summary Help companies Measure, reduce, and remove carbon emissions with Carbon Direct science-backed carbon management solutions Mostly advisor...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Milestone-based billing and contract processing",
    "Revenue recognition complexity across multiple business models",
    "System integration requirements (Hubspot, QBO, Tax)",
    "International business support and scalability",
    "Manual workflow automation and cash forecasting improvements"
  ],
  "rules": [
    {
      "rule": "For milestone-based contracts with first payment, first invoice should be on effective date",
      "category": "billing_timing"
    },
    {
      "rule": "Second invoice defaults to 6 months after first invoice for milestone contracts",
      "category": "billing_timing"
    },
    {
      "rule": "When contracts specify 'earlier of completion or 120 days', use 120 days as default",
      "category": "billing_timing"
    },
    {
      "rule": "When 3 milestones are specified, default first milestone to 3 months after start date, subsequent ones every month after",
      "category": "billing_timing"
    },
    {
      "rule": "50/50 payment splits should be created as 2 different sets of billing transactions (BTs)",
      "category": "billing_structure"
    },
    {
      "rule": "Different BT sets must be linked to different integration items as outlined in Integration Items section",
      "category": "system_integration"
    },
    {
      "rule": "When contract processing is complete, send Slackbot notification for first invoice",
      "category": "notification"
    },
    {
      "rule": "Carbon credit items must match to QBO for inventory drawdown tracking",
      "category": "inventory_management"
    },
    {
      "rule": "Filter Hubspot to 'close won' to identify new contracts requiring processing",
      "category": "contract_identification"
    }
  ],
  "exceptions": [
    {
      "exception": "Project milestones and billing milestones usually align but not 100% of the time",
      "impact": "Requires manual verification with client managers"
    },
    {
      "exception": "Some milestone contracts identify specific payment splits (e.g., 50% upfront, 50% later) rather than standard timing",
      "impact": "Requires custom BT configuration per contract"
    },
    {
      "exception": "International invoices represent very low volume (6-7 out of 200 invoices, less than 5%)",
      "impact": "No international taxes or banking currently needed but must be supported"
    },
    {
      "exception": "Revenue recognition practices are non-standard - sometimes at project end date, sometimes based on completion percentage",
      "impact": "No standardized rev rec process currently in place"
    },
    {
      "exception": "Milestone-based rev rec is not yet supported by system but represents 75% of business",
      "impact": "Feature gap that needs to be communicated"
    }
  ],
  "merchant_specific": [
    {
      "element": "Three distinct billing models: SaaS (10%), Carbon Credits (15%), Milestone-based (75%)",
      "customization_needed": "System must handle all three billing types with different processing rules"
    },
    {
      "element": "Carbon removal credits inventory management",
      "customization_needed": "Special integration with QBO for inventory tracking"
    },
    {
      "element": "Hubspot as primary CRM for contract management",
      "customization_needed": "Integration to streamline contract sends to Tabs and reduce manual workflow"
    },
    {
      "element": "Key contacts: Jeff Bennet (primary user, Senior Accounting Manager) and Jessica Isaacs (VP Finance, buyer)",
      "customization_needed": "Relationship management and communication strategy"
    },
    {
      "element": "Merchant temperament: Easygoing but effective operators, previously burned by vendor promises",
      "customization_needed": "Requires careful expectation management and excellent service delivery"
    },
    {
      "element": "Google sheets currently used for milestone and progress tracking",
      "customization_needed": "System must replace or integrate with existing spreadsheet workflows"
    },
    {
      "element": "Advisory work with site visits and final reports as milestone triggers",
      "customization_needed": "Milestone definitions specific to carbon advisory services"
    },
    {
      "element": "No tax system currently in place",
      "customization_needed": "Future tax integration support needed as business scales"
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 2: Merchant Info Sheet - Carbon Direct_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:03:09

### Original Content
```
Example of what this could look like: Estimated timelines for deliverables could also be embedded within the paragraphs describing the deliverable, and be identified as  Approximately X weeks from SOW Effective Date If this is seen, use this as the bill date for that deliverable Example below: If there is a payment Due Date schedule, defer to that for milestone billing schedule: Use Payment Due Date as invoice date (as opposed to that being the actual due date of the invoice) If effective date f...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Invoice Creation Rules",
    "Milestone and Deliverable Timeline Management",
    "Customer-Specific Processing Requirements",
    "Default Values and Fallback Settings",
    "Contract Processing Workflows and Special Cases"
  ],
  "rules": [
    {
      "rule": "When estimated timelines are embedded in deliverable descriptions (format: 'Approximately X weeks from SOW Effective Date'), use this as the bill date for that deliverable",
      "category": "Timeline Management"
    },
    {
      "rule": "If a Payment Due Date schedule exists, use Payment Due Date as invoice date (not as the actual due date of the invoice)",
      "category": "Billing Schedule"
    },
    {
      "rule": "If effective date falls in a closed period, start billing and revenue recognition on the first of the month of the most recent open period",
      "category": "Period Management"
    },
    {
      "rule": "When Project Title is specified in contract, use the project name in the title of the BT milestone",
      "category": "Naming Convention"
    },
    {
      "rule": "Do not include the prefix 'Energy_Carbon: Carbon Direct' in milestone names",
      "category": "Naming Convention"
    },
    {
      "rule": "For monthly retainers, create 2 BTs: (1) Retainer Fee (description: First month) billed on effective date as one-off, (2) Retainer Fee recurring starting the following full month on the first",
      "category": "Retainer Processing"
    },
    {
      "rule": "For PO processing: Customer = Name of Portfolio, Date = Date of invoice (1 occurrence, billing frequency none), Item title = Credits, Quantity = Number of Credits, Description = Price per credit, Total = Total Purchase Price, MUST ADD PO# TO INVOICE",
      "category": "Purchase Order Processing"
    },
    {
      "rule": "If client name contains any version of 'microsoft', associate the contract with QBO created customer 'Microsoft (c)'",
      "category": "Customer Association"
    },
    {
      "rule": "For contracts between TWO customers, create invoices for both customers tied to the same document, following contract language on cost split",
      "category": "Multi-Customer Contracts"
    },
    {
      "rule": "Default Service Term if none listed: 1 Year",
      "category": "Defaults"
    },
    {
      "rule": "Default Net Payment Terms: 30 days (60 days for Microsoft contracts)",
      "category": "Defaults"
    },
    {
      "rule": "Default Billing Frequency if none listed: Monthly",
      "category": "Defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT",
      "category": "Defaults"
    },
    {
      "rule": "For 50/50 up front and delivered contracts: First 50% BT = Services to be performed, Second 50% BT = Services already performed",
      "category": "Integration Items"
    },
    {
      "rule": "When billed upon delivery: Advisory services/Measure analysis = Platform services to be performed, Advisory Services = Advisory Services",
      "category": "Integration Items"
    },
    {
      "rule": "If contract invoices up front: Services to be performed",
      "category": "Integration Items"
    },
    {
      "rule": "If milestone schedule with clear dates: Advisory services with Project title in name of milestone",
      "category": "Integration Items"
    },
    {
      "rule": "Post-processing notification: Customer Success (Azmat Aziz) needs to be notified in Messari internal merchant channel when contracts are processed in Active phase",
      "category": "Communications"
    }
  ],
  "exceptions": [
    {
      "exception": "Microsoft contracts use 60 net terms instead of default 30 days",
      "condition": "Client name contains any version of 'microsoft'"
    },
    {
      "exception": "Effective date adjustment when falling in closed period",
      "condition": "Effective date falls in a closed accounting period"
    },
    {
      "exception": "Dual customer invoice creation",
      "condition": "Contract is between TWO customers"
    },
    {
      "exception": "Payment Due Date schedule overrides standard billing timeline",
      "condition": "Payment Due Date schedule exists in contract"
    },
    {
      "exception": "Different BT naming when Project Title is specified",
      "condition": "Multiple projects running simultaneously for same customer"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer naming convention for Microsoft",
      "description": "Specific QBO customer name 'Microsoft (c)' for any Microsoft-related contracts"
    },
    {
      "element": "Energy_Carbon prefix exclusion",
      "description": "Specific instruction to exclude 'Energy_Carbon: Carbon Direct' prefix from milestone names"
    },
    {
      "element": "Messari internal channel notification",
      "description": "Post-processing communication to Customer Success (Azmat Aziz) in Messari internal merchant channel"
    },
    {
      "element": "Project naming examples",
      "description": "Examples reference specific projects like 'Rabobank Methodology Review' and 'Microsoft projects'"
    },
    {
      "element": "Integration item categorization",
      "description": "Specific service categories: Advisory services, Measure analysis, Platform services, with distinct billing treatment"
    },
    {
      "element": "Retainer processing workflow",
      "description": "Two-BT system for monthly retainers with specific reference example (9258eb4e-37fa-4e80-9f83-401c0ab74ceb)"
    },
    {
      "element": "PO# requirement",
      "description": "Mandatory addition of PO# to invoices when processing purchase orders"
    },
    {
      "element": "Contract reference system",
      "description": "Uses UUID references for example contracts (e.g., 007260f2-eb06-4fef-a20f-37f0cedc01c6)"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: Merchant Info Sheet - Carbon Direct_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:03:21

### Original Content
```
com video jxkspzes8qbp50ma-intro-to-tabs-may-31-2024 Custom Demo on June 11 - https: tabs rewatch com video q8y44y0dtm6ayk2q-tabs-carbon-direct-custom-demo-june-11-2024 Scoping Call on June 14 - https: tabs rewatch com video ut5guypsvihghfpr-tabs-carbon-direct-june-14-2024 Partnerships discussion on June 17 - https: tabs rewatch com video x1m3uguepeob63qi-tabs-carbon-direct-partnerships-june-17-2024 Final Partnerships discussion June 21 - https: tabs rewatch com video h44dnyiw3at4ndob-hold-tabs-...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting and call documentation tracking",
    "Progressive sales/partnership engagement process",
    "Video recording and archival of client interactions",
    "Chronological progression of business relationship (intro to final partnerships discussion)"
  ],
  "rules": [
    "All client meetings should be recorded and archived with video links",
    "Meeting recordings should include descriptive titles indicating the meeting type and date",
    "Video links should follow a consistent URL structure (tabs.rewatch.com/video/[unique-id]-[description])",
    "Meetings should be documented in chronological order",
    "Meeting progression should follow a structured path: Introduction → Custom Demo → Scoping Call → Partnerships Discussion → Final Partnerships Discussion"
  ],
  "exceptions": [
    "The June 21 meeting is marked with 'HOLD' prefix, suggesting it may have been tentative, rescheduled, or had special status",
    "Meeting cadence varies (May 31 to June 11 is 11 days, but subsequent meetings are 3-4 days apart), indicating flexible scheduling based on discussion needs"
  ],
  "merchant_specific": [
    "Client name: Carbon Direct - this would vary per merchant/client",
    "Specific video IDs and URLs - unique to each recording session",
    "Meeting dates and timeline - specific to this client engagement",
    "The progression from intro to partnerships may vary by client type or deal complexity",
    "Use of 'Tabs' as the product/platform name being demonstrated"
  ],
  "confidence_score": 0.75
}
```

---

