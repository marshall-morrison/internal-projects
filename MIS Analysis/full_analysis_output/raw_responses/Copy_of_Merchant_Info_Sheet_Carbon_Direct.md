# Raw LLM Analysis: Copy of Merchant Info Sheet - Carbon Direct

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:19:37

---

## Chunk 1: Copy of Merchant Info Sheet - Carbon Direct_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:19:37

### Original Content
```
Example of what this could look like: Estimated timelines for deliverables could also be embedded within the paragraphs describing the deliverable, and be identified as  Approximately X weeks from SOW Effective Date If this is seen, use this as the bill date for that deliverable Example below: If there is a payment Due Date schedule, defer to that for milestone billing schedule: Use Payment Due Date as invoice date (as opposed to that being the actual due date of the invoice) If there is a Proje...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Milestone and Billing Timeline Management",
    "Customer-Specific Billing Rules and Naming Conventions",
    "Purchase Order and Invoice Processing",
    "Default Terms and Configurations",
    "Integration Items and Service Delivery Billing"
  ],
  "rules": [
    "When estimated timelines are embedded in deliverable descriptions (format: 'Approximately X weeks from SOW Effective Date'), use this as the bill date for that deliverable",
    "If a Payment Due Date schedule exists, use Payment Due Date as invoice date (not as the actual due date)",
    "When a Project Title is specified, use the project name in the BT milestone title",
    "Do not include the prefix 'Energy_Carbon: Carbon Direct' in milestone titles",
    "For monthly retainers, create 2 BTs: (1) Retainer Fee (description: First month) billed on effective date as one-off, (2) Retainer Fee recurring starting the following full month on the first",
    "For PO processing: Customer = Name of Portfolio, Date = Date of invoice (1 occurrence, billing frequency = none), Item title = Credits, Quantity = Number of Credits, Description = Price per credit, Total = Total Purchase Price, and ALWAYS ADD PO# TO INVOICE",
    "If client name contains any version of 'microsoft', associate contract with QBO customer 'Microsoft (c)'",
    "Default Service Term if none listed: 1 Year",
    "Default Net Payment Terms: 30 days (60 days for Microsoft contracts)",
    "Default Billing Frequency if none listed: Monthly",
    "Every tax line item becomes a BT",
    "For 50/50 contracts (up front and delivered): First 50% BT = 'Services to be performed', Second 50% BT = 'Services already performed'",
    "When billed upon delivery: Advisory services/Measure analysis = 'Platform services to be performed', Advisory Services = 'Advisory Services'",
    "When contract invoices up front: use 'Services to be performed'",
    "When milestone schedule has clear dates: use 'Advisory services' with project title in milestone name"
  ],
  "exceptions": [
    "Microsoft contracts require 60 net payment terms instead of default 30",
    "Microsoft client names must be associated with specific QBO customer 'Microsoft (c)'",
    "Retainer billing requires special handling with two separate BT entries instead of standard single entry",
    "Payment Due Date schedule overrides standard billing date logic",
    "Contracts with embedded timeline estimates use different date calculation method",
    "50/50 payment structure requires different BT descriptions for each half"
  ],
  "merchant_specific": [
    "Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase",
    "Specific QBO customer mapping for Microsoft: 'Microsoft (c)'",
    "Project naming convention excludes 'Energy_Carbon: Carbon Direct' prefix",
    "Example milestone naming: 'Rabobank Methodology Review: Milestone 1'",
    "Reference to specific retainer example: 9258eb4e-37fa-4e80-9f83-401c0ab74ceb",
    "PO processing format specific to Credits/Portfolio structure",
    "Integration with Rewatch for call recordings (May 31, June 11, June 14)",
    "Merchant phase terminology: Implementation, Active",
    "BT (Billing Template/Transaction) terminology used throughout"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Copy of Merchant Info Sheet - Carbon Direct_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:19:42

### Original Content
```
mirDemo date: Jun 11, 2024 Scoping start date: Jun 14, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Aug 1, 2024 [If Exists] Opt Out Date: Go Live Date: Sep 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Jessica Isaacs - VP of Finance Jeff Bennet - Senior Accounting Manager (and primary user) Company summary Help companies Measure, reduce, and remove carbon emissions with Carbon Direct science-backed carbon management solutions Mostly advisory...
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
      "rule": "Second invoice defaults to 6 months after first invoice for two-payment milestone contracts",
      "category": "billing_timing"
    },
    {
      "rule": "Two-payment milestones should be created as 2 different sets of BTs (Billing Transactions)",
      "category": "billing_structure"
    },
    {
      "rule": "Different BT sets must be linked to different integration items",
      "category": "integration"
    },
    {
      "rule": "When contracts specify 'earlier of completion or 120 days', use 120 days as default",
      "category": "billing_timing"
    },
    {
      "rule": "When 3 milestones are specified, default first milestone to 3 months after start date, subsequent milestones every month after",
      "category": "billing_timing"
    },
    {
      "rule": "When contract is done processing, send Slackbot notification for the first invoice",
      "category": "notification"
    },
    {
      "rule": "Filter Hubspot to 'close won' status to identify new contracts requiring processing",
      "category": "workflow"
    },
    {
      "rule": "Carbon credit items must match to QBO for inventory drawdown tracking",
      "category": "integration"
    }
  ],
  "exceptions": [
    {
      "exception": "Project milestones and billing milestones usually align but not 100% of the time",
      "impact": "May require manual reconciliation or custom milestone mapping"
    },
    {
      "exception": "Some milestone contracts identify 50% up front and 50% later (non-standard split)",
      "impact": "Requires flexible percentage allocation in billing setup"
    },
    {
      "exception": "International invoices are very low volume (6-7 out of 200 invoices, less than 5%)",
      "impact": "No international taxes or banking currently needed but must be supported"
    },
    {
      "exception": "Revenue recognition practices are inconsistent - sometimes at project end date, sometimes based on 75% completion",
      "impact": "Need to establish standardized rev rec practices"
    },
    {
      "exception": "Milestone-based rev rec is not yet supported by system but represents 75% of business",
      "impact": "Critical gap that needs communication and future development"
    }
  ],
  "merchant_specific": [
    {
      "element": "Three revenue streams with different billing models",
      "details": "SaaS (10%), Carbon credits (15%), Milestone-based advisory (75%)"
    },
    {
      "element": "Carbon removal credits inventory management",
      "details": "Requires QBO integration for inventory drawdown tracking"
    },
    {
      "element": "Key personnel and decision-making structure",
      "details": "Jeff Bennet (primary user/key POC), Jessica Isaacs (VP Finance/ultimate buyer)"
    },
    {
      "element": "Hubspot as primary CRM and contract source",
      "details": "Integration priority to streamline contract sends to Tabs and reduce manual follow-up"
    },
    {
      "element": "Merchant temperament and history",
      "details": "Easygoing but effective operators, previously burned by vendor overpromising - requires careful expectation management"
    },
    {
      "element": "Google sheets for milestone and progress tracking",
      "details": "Current manual process for managing billing milestones and revenue recognition estimates"
    },
    {
      "element": "Advisory work structure",
      "details": "Deep diligence on carbon removal processes with site visits and final reports as milestones"
    },
    {
      "element": "No current tax system",
      "details": "Proactively thinking about tax support for future needs"
    },
    {
      "element": "Company size indicator",
      "details": "Small enough that deals closing are communicated via Slack"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Copy of Merchant Info Sheet - Carbon Direct_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:19:48

### Original Content
```
rewatch com video ut5guypsvihghfpr-tabs-carbon-direct-june-14-2024 Partnerships discussion on June 17 - https: tabs rewatch com video x1m 3uguepeob63qi-tabs-carbon-direct-partnerships-june-17-2024 Final Partnerships discussion June 21 - https: tabs rewatch com video h44dnyiw3at4ndob-hold-tabs-carbon-direct-june-21-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Partnership discussions and meetings",
    "Video documentation and recording management",
    "Carbon Direct collaboration timeline",
    "Meeting progression and follow-ups"
  ],
  "rules": [],
  "exceptions": [],
  "merchant_specific": [
    "Carbon Direct - appears to be a specific partner or client organization",
    "Tabs - appears to be the merchant/platform name (tabs.rewatch.com)",
    "Rewatch.com - video hosting/meeting recording platform being used",
    "Specific meeting dates: June 14, June 17, and June 21, 2024",
    "Video ID format and URL structure specific to this platform"
  ],
  "confidence_score": 0.3
}
```

**Analysis Notes:**

This document chunk appears to be a fragment of meeting notes or reference links rather than a complete instruction document. The content consists primarily of video URLs for recorded partnership discussions with Carbon Direct across three dates in June 2024.

**Limitations:**
- No actual instructional content, rules, or policies are present in this chunk
- The text appears to be incomplete or improperly formatted (missing proper URL formatting)
- Without access to the video content or surrounding context, it's impossible to extract meaningful rules or requirements
- This seems to be metadata or reference material rather than actionable instructions

**Confidence Reasoning:**
The low confidence score (0.3) reflects that while I can identify the themes and merchant-specific elements with reasonable certainty, there are no extractable rules or exceptions from this content fragment. A proper analysis would require either the full document context or access to the referenced video content.

---

