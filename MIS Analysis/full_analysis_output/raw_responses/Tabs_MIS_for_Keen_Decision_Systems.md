# Raw LLM Analysis: Tabs MIS for Keen Decision Systems

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 12:02:49

---

## Chunk 1: Tabs MIS for Keen Decision Systems_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:02:49

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  So...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Post-implementation processing workflows and defaults",
    "Integration item categorization and labeling",
    "Internal communication and notification protocols",
    "Customer-specific handling requirements",
    "Feature request and merchant call tracking"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: If no specific instruction is listed, every tax line item becomes a BT Events Processing",
      "category": "Processing Defaults",
      "phase": "Post-Go Live"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Assignment",
      "phase": "Processing"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Item Assignment",
      "phase": "Processing"
    },
    {
      "rule": "Implementation Success team is responsible for filling information Post-Go Live for multiple sections (Events Processing, Integration Items Processing, Post Processing Communications, Customer Information)",
      "category": "Responsibility Assignment",
      "phase": "Post-Go Live"
    },
    {
      "rule": "AE must fill Feature Requests prior to Implementation handoff",
      "category": "Documentation Requirements",
      "phase": "Pre-Implementation"
    },
    {
      "rule": "Implementation team must fill Feature Requests prior to go-live",
      "category": "Documentation Requirements",
      "phase": "Implementation"
    },
    {
      "rule": "Success team must fill Feature Requests Post-Go Live",
      "category": "Documentation Requirements",
      "phase": "Post-Go Live"
    },
    {
      "rule": "Merchant call recordings must be documented with dates and Gong links",
      "category": "Documentation Requirements",
      "phase": "All phases"
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by Merchant",
      "condition": "Merchant provides alternative instruction",
      "default_behavior": "Label as Software Subscription Bundle"
    },
    {
      "exception": "Tax line item processing may differ from BT Events Processing default if specific instructions are provided",
      "condition": "Specific instructions are listed",
      "default_behavior": "BT Events Processing"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Specific customer relationship requirements exist",
      "default_behavior": "Standard invoice processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customization_type": "Merchant-specific vendors (Statsig, Pinata examples)",
      "requires_merchant_input": true
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "Who to notify, where to notify, when to notify",
      "example": "Customer Success [Azmat Aziz] in Messari internal merchant channel when contracts are processed",
      "requires_merchant_input": true
    },
    {
      "element": "Customer-specific information",
      "customization_type": "Special handling requirements, memo requirements, invoice modifications",
      "requires_merchant_input": true
    },
    {
      "element": "Feature requests",
      "customization_type": "What it is, why it's important, urgency level",
      "requires_merchant_input": true
    },
    {
      "element": "Events billing integration processing",
      "customization_type": "Merchant-specific event processing requirements",
      "requires_merchant_input": true
    },
    {
      "element": "Merchant call history",
      "customization_type": "Call dates, purposes, and Gong recording links",
      "requires_merchant_input": false
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Tabs MIS for Keen Decision Systems_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:02:52

### Original Content
```
Merchant Name- Keen Decision Systems Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Customer Creation If it s not a renewal, upsell or expansion and the customer ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Data Entry",
    "Billing and Revenue Recognition",
    "Document Handling and Prioritization",
    "Default Values and Standardization",
    "Item Creation and Field Mapping"
  ],
  "rules": [
    {
      "rule": "Create customer only if not a renewal, upsell, expansion, or existing customer",
      "category": "Customer Creation"
    },
    {
      "rule": "Process standard Keen Order Forms as primary contract documents",
      "category": "Document Processing"
    },
    {
      "rule": "Ignore Third Party Agreements",
      "category": "Document Processing"
    },
    {
      "rule": "Ignore POs unless it is the first document for that customer",
      "category": "Document Processing"
    },
    {
      "rule": "Process emails from HubSpot with instructions contained in the email body",
      "category": "Document Processing"
    },
    {
      "rule": "Process discounts IN-LINE, do not create separate billing items",
      "category": "Discount Handling"
    },
    {
      "rule": "Item Name: Use the name from the 'Product' column",
      "category": "Field Mapping"
    },
    {
      "rule": "Item Description: Add if appropriate, keep to one sentence maximum",
      "category": "Field Mapping"
    },
    {
      "rule": "Quantity: Use 'Quantity' column, default to 1 if not listed",
      "category": "Field Mapping"
    },
    {
      "rule": "Total Price: Use full price listed for each service period",
      "category": "Field Mapping"
    },
    {
      "rule": "Service Start Date: Use 'Service Period' start date for each line item",
      "category": "Field Mapping"
    },
    {
      "rule": "Months of Service: Calculate from service period, round to whole months",
      "category": "Field Mapping"
    },
    {
      "rule": "Billing Start Date: Default to service start date unless explicitly stated otherwise",
      "category": "Field Mapping"
    },
    {
      "rule": "Integration Item: Use 'Subscription Revenue' for all items",
      "category": "Field Mapping"
    },
    {
      "rule": "Frequency: Use stated contract terms",
      "category": "Field Mapping"
    },
    {
      "rule": "Net Terms: Default to 30 if not listed",
      "category": "Field Mapping"
    },
    {
      "rule": "Ignore billing items named 'incremental __'",
      "category": "Exclusions"
    },
    {
      "rule": "Ignore billing items named 'State regional taxes'",
      "category": "Exclusions"
    },
    {
      "rule": "Do NOT process any billing items for taxes",
      "category": "Exclusions"
    },
    {
      "rule": "Default Service Term: 1 Year if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default Net Payment Terms: 0 if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default Billing Frequency: Monthly if none listed",
      "category": "Defaults"
    }
  ],
  "exceptions": [
    {
      "exception": "POs should be processed if it is the first document for a customer",
      "condition": "First document scenario"
    },
    {
      "exception": "Billing Start Date differs from Service Start Date when payment terms explicitly specify invoicing dates",
      "condition": "Explicit invoicing schedule in payment terms",
      "example": "Year 1 on 03/01/2024 for 179k and year 2 on 3/01/2025 for 179k"
    },
    {
      "exception": "Contract-specific processing variations may exist",
      "condition": "Merchant requests specific handling (e.g., back-dating invoice dates)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Keen Decision Systems",
      "type": "Merchant Identity"
    },
    {
      "element": "Implementation POC and CX POC fields",
      "type": "Contact Information",
      "note": "To be filled by Implementation team"
    },
    {
      "element": "Billing model section",
      "type": "Billing Configuration",
      "note": "Implementation team to complete"
    },
    {
      "element": "Unique customer creation process information",
      "type": "Process Customization",
      "note": "Merchant-specific variations"
    },
    {
      "element": "Contract structure and breakdown",
      "type": "Contract Configuration"
    },
    {
      "element": "Standard Keen Order Forms",
      "type": "Document Template",
      "note": "Merchant-specific contract format"
    },
    {
      "element": "HubSpot email processing",
      "type": "System Integration",
      "note": "Specific to merchant's CRM usage"
    },
    {
      "element": "Integration Item: 'Subscription Revenue'",
      "type": "Revenue Classification",
      "note": "Merchant-specific accounting category"
    },
    {
      "element": "Contract-specific processing instructions",
      "type": "Variable Processing Rules",
      "note": "May differ by individual contract"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Tabs MIS for Keen Decision Systems_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:03:00

### Original Content
```
id 5110652899652730931 April 15 reporting discussion with Jack - https: us-56595 app gong io call id 2624889405392607887 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Additional IM Prep Materials See This document for supplemental info Info on how merchant bills Keen s billing is non-standard and labor-intensive under their current system (Maxio   QBO): Manual Invoice Cadence Creation: Every new contract requires manual setup of invoice schedules in Max...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing complexity and manual processes",
    "Stakeholder decision-making criteria and concerns",
    "System migration evaluation (Maxio to Tabs)",
    "Financial reporting and accounting close requirements",
    "Cost-benefit analysis and ROI justification"
  ],
  "rules": [
    "Every new contract requires manual setup of invoice schedules in current system",
    "No automation exists for renewals in current system",
    "Mike manually logs into bank daily to match payments",
    "Collections cadences must be manually shut off after payment matching",
    "CFO requires journal entries and revenue recognition reports for close process",
    "Reporting must show deferred and unbilled values",
    "Sales tax integration must be clean and accurate to avoid customer disputes",
    "Milestone-based or staged billing setup requires 1+ hours per contract",
    "Custom invoice frequencies (6-installment plans, odd pricing, staggered schedules) must be supported"
  ],
  "exceptions": [
    "Occasionally use milestone-based billing (non-standard)",
    "Occasionally use staged billing (non-standard)",
    "Edge cases include 6-installment plans with odd pricing",
    "Some contracts have staggered billing schedules requiring custom setup",
    "Maxio doesn't integrate cleanly with Anrok for sales tax (workaround needed)"
  ],
  "merchant_specific": [
    "Merchant name: Keen",
    "Current systems: Maxio and QBO (QuickBooks Online)",
    "Tax system: Anrok",
    "Key personnel: Mike Althoff (COO, Decision Maker), Jack Siegel (CFO, Key User), Expo (paid hourly staff)",
    "Current system cost: $40-44K for Maxio renewal",
    "Proposed system cost: $32K for Tabs",
    "Billing is described as 'non-standard and labor-intensive'",
    "Mike's temperament: practical, sharp, cost-sensitive, skeptical of new tech",
    "Jack's temperament: detail-oriented, reporting-focused, solutions-oriented",
    "Decision factors: price comparison, time burden on Expo, reporting parity confidence",
    "Preferred validation method: dummy report showing deferred unbilled values"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: Tabs MIS for Keen Decision Systems_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:03:10

### Original Content
```
Billing Automation   Accuracy   Critical Automated invoice schedule creation from contracts They struggle with manual cadence setup in Maxio, especially for custom staged billing Support for edge cases (e g , milestone billing, staggered payments) Painful to configure manually in Maxio; even rare edge cases (every  2 months) take over an hour Support for multi-entity invoicing from a single contract (e g , Revlon   Elizabeth Arden invoiced separately) Tabs promised to handle this via dual custom...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Automation and Invoice Management",
    "Collections and Cash Application Automation",
    "Revenue Recognition and Financial Reporting",
    "Third-Party System Integrations",
    "Manual Process Pain Points and Automation Needs"
  ],
  "rules": [
    {
      "category": "Billing Automation",
      "rule": "Automated invoice schedules must be created directly from contracts",
      "priority": "Critical"
    },
    {
      "category": "Billing Automation",
      "rule": "System must support edge case billing scenarios including milestone billing and staggered payments",
      "priority": "Critical"
    },
    {
      "category": "Billing Automation",
      "rule": "Multi-entity invoicing from a single contract must be supported through dual customer records",
      "priority": "Critical"
    },
    {
      "category": "Tax Compliance",
      "rule": "Anrok integration is required for accurate sales tax calculation on invoices",
      "priority": "Important",
      "rationale": "Incorrect or missing tax lines cause customer disputes and non-payment"
    },
    {
      "category": "Collections",
      "rule": "Dunning campaigns must be automatically managed based on bank activity without manual intervention",
      "priority": "Critical"
    },
    {
      "category": "Cash Application",
      "rule": "AI-powered cash application via Plaid integration must provide direct bank feed matching",
      "priority": "Critical"
    },
    {
      "category": "Collections Alerts",
      "rule": "CSMs must be automatically alerted via Slack for overdue invoices without manual steps",
      "priority": "Important"
    },
    {
      "category": "Collections Visibility",
      "rule": "Overdue invoice information must be visible in HubSpot",
      "priority": "Important"
    },
    {
      "category": "Revenue Recognition",
      "rule": "One-click journal entry export to QuickBooks with correct debit/credit accounts is required",
      "priority": "Critical"
    },
    {
      "category": "Revenue Recognition",
      "rule": "Deferred and unbilled revenue reporting must be available for month-end close",
      "priority": "Critical"
    }
  ],
  "exceptions": [
    {
      "case": "Custom billing cadences",
      "description": "Edge cases like billing every 2 months require special configuration support (currently takes over 1 hour manually in Maxio)"
    },
    {
      "case": "Milestone billing",
      "description": "Non-standard billing trigger based on project milestones rather than time periods"
    },
    {
      "case": "Staggered payments",
      "description": "Payment schedules that don't follow standard monthly/annual patterns"
    },
    {
      "case": "Multi-entity invoicing",
      "description": "Single contract generating separate invoices for different legal entities (example: Revlon and Elizabeth Arden)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Personnel references",
      "details": "Mike (handles collections/dunning), Jack (handles rev rec/accounting), Expo (stakeholder requiring confidence in reporting)",
      "customization_need": "Role-based access and workflow assignments"
    },
    {
      "element": "Current systems",
      "details": "Maxio (current billing system), QuickBooks Online (accounting system), HubSpot (CRM), Plaid (banking integration), Anrok (tax compliance)",
      "customization_need": "Integration mappings and data synchronization requirements"
    },
    {
      "element": "Customer examples",
      "details": "Revlon and Elizabeth Arden as multi-entity invoicing example",
      "customization_need": "Customer-specific billing configurations"
    },
    {
      "element": "Communication channels",
      "details": "Shared Slack channels for collections escalation",
      "customization_need": "Notification routing and channel configuration"
    },
    {
      "element": "Reconciliation workflow",
      "details": "Daily bank login for manual reconciliation (current state)",
      "customization_need": "Frequency and automation level for cash application"
    },
    {
      "element": "Product reference",
      "details": "Tabs (the solution being evaluated/implemented)",
      "customization_need": "Feature enablement and configuration"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 5: Tabs MIS for Keen Decision Systems_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:03:15

### Original Content
```
No increase in close timeline Reporting workflows must not add time to Expo Group s monthly close Core blocker if not addressed Important Custom report support via backend (Omni) Tabs has committed to custom reports while native features are being built Nice-to-have Auto-sync journal entries to QuickBooks (bypassing manual import) Considered useful, but optional depending on comfort ARR   CAR Waterfall Reporting   Critical Committed ARR (CAR) waterfall tracking Must include: Contract signature d...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Financial Close Timeline and Reporting Efficiency",
    "ARR/CAR Waterfall Tracking and Revenue Recognition",
    "System Integration and Data Synchronization",
    "Custom Reporting and Dashboard Requirements",
    "Automation of Billing and Renewal Processes"
  ],
  "rules": [
    {
      "rule": "Reporting workflows must not add time to monthly close process",
      "priority": "Core blocker",
      "category": "Timeline Management"
    },
    {
      "rule": "CAR waterfall tracking must include contract signature date as commit date",
      "priority": "Critical",
      "category": "Revenue Tracking"
    },
    {
      "rule": "Renewal forecasting must assume auto-renew by default",
      "priority": "Critical",
      "category": "Revenue Forecasting"
    },
    {
      "rule": "Churn detection must be performed via lost renewal deals in HubSpot",
      "priority": "Critical",
      "category": "Revenue Tracking"
    },
    {
      "rule": "ARR/CAR dashboard must provide live visibility before month-end close",
      "priority": "Important",
      "category": "Reporting"
    },
    {
      "rule": "Two-way sync with QuickBooks is required",
      "priority": "Critical",
      "category": "System Integration"
    },
    {
      "rule": "Support for expansion, contraction, and churn cohorts required for board reporting",
      "priority": "Important",
      "category": "Reporting"
    },
    {
      "rule": "Custom report support must be available via backend (Omni)",
      "priority": "Important",
      "category": "Reporting"
    }
  ],
  "exceptions": [
    {
      "exception": "Auto-sync journal entries to QuickBooks is optional depending on user comfort level",
      "context": "Considered useful but not required"
    },
    {
      "exception": "HubSpot integration is Phase 2, not immediate requirement",
      "context": "For invoice status, renewals, and alerts"
    },
    {
      "exception": "Pushing renewal opportunities to HubSpot automatically is nice-to-have, not required now",
      "context": "Future direction but not current blocker"
    },
    {
      "exception": "Custom field syncing (e.g., 60-day notice periods) is nice-to-have",
      "context": "Interest expressed but not critical"
    }
  ],
  "merchant_specific": [
    {
      "element": "Expo Group",
      "type": "Company Name",
      "note": "Specific merchant referenced for monthly close timeline"
    },
    {
      "element": "Mike",
      "type": "Stakeholder",
      "note": "Key decision maker who wants real-time ARR/CAR visibility"
    },
    {
      "element": "Jack",
      "type": "Stakeholder",
      "note": "Expressed interest in custom field syncing alongside Mike"
    },
    {
      "element": "Maxio",
      "type": "Previous System",
      "note": "Current system with limitations in billing contact updates"
    },
    {
      "element": "Tabs",
      "type": "System/Vendor",
      "note": "Has committed to custom reports during native feature development"
    },
    {
      "element": "60-day notice periods",
      "type": "Custom Field Example",
      "note": "Specific business term that needs to be synced"
    },
    {
      "element": "M&A diligence",
      "type": "Business Context",
      "note": "Cohort reporting useful for future merger/acquisition scenarios"
    }
  ],
  "confidence_score": 0.85
}
```

---

