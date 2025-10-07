# Raw LLM Analysis: MIS_ Truepic

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 12:16:48

---

## Chunk 1: MIS_ Truepic_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:16:48

### Original Content
```
app gong io call id 2558689265761864240 ROI   Proposal and Dayee introing MEC 5 19 - https: us-56595 app gong io call id 4399922205818376589 Implementation and HS 6 18 - https: us-56595 app gong io call id 6891957760903557960 Custom Demo 6 27 - https: us-56595 app gong io call
```

### LLM Analysis Response
```json
{
  "themes": [
    "Call tracking and documentation",
    "Sales process stages (ROI proposal, implementation, demo)",
    "Meeting recordings via Gong.io platform",
    "Customer engagement timeline tracking"
  ],
  "rules": [],
  "exceptions": [],
  "merchant_specific": [
    "Gong.io platform usage for call recording",
    "Specific call ID format and structure",
    "Meeting types: ROI Proposal, Implementation, Custom Demo",
    "References to 'Dayee' and 'MEC' (likely company or product names)",
    "References to 'HS' (possibly HubSpot or another system)",
    "URL pattern: us-56595.app.gong.io (specific instance/tenant)",
    "Date format for meeting tracking (month/day notation)"
  ],
  "confidence_score": 0.3
}
```

**Explanation of Low Confidence Score:**

This document chunk appears to be metadata or reference links rather than actual merchant instruction content. It consists primarily of:
- Gong.io call recording URLs
- Call IDs
- Meeting titles with dates
- Fragmented text

There are no clear rules, policies, requirements, or actionable instructions present in this content. This appears to be either:
1. Header/footer metadata from a larger document
2. A reference section with meeting links
3. Accidentally extracted non-instructional content

To provide a meaningful analysis of merchant instructions, a different document chunk containing actual procedural guidelines, policies, or operational requirements would be needed.

---

## Chunk 2: MIS_ Truepic_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:16:59

### Original Content
```
id 6842820473198013716 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Contracts are typically annual, with some having defined inspection thresholds (e g , 800 inspections per year) Customers are billed upfront for a base amount, and overages are billed when usage exceeds contracted amounts Overages can be billed: Mid-year, when usage exceeds the threshold partway through the term At the end of the term, depending on customer t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Contract Structure",
    "Usage-Based Pricing and Overages",
    "Stakeholder Management and Personalities",
    "CRM and System Integration Requirements",
    "Contract Variability Across Customer Segments"
  ],
  "rules": [
    "Contracts are typically annual in duration",
    "Customers are billed upfront for a base amount",
    "Overages are billed when usage exceeds contracted amounts",
    "Some contracts have defined inspection thresholds (e.g., 800 inspections per year)",
    "Overages can be billed mid-year when usage exceeds threshold during the term",
    "Overages can be billed at end of term depending on customer type and contract structure",
    "Sean (Senior Accountant) handles all contract management and billing",
    "Victoria (Rev Ops) requires Hubspot integration for CRM contract ingestion"
  ],
  "exceptions": [
    "Some customers are on monthly usage-based billing instead of annual contracts",
    "Some customers have annual contracts with per-inspection overages",
    "Overage billing timing varies by customer type and contract structure",
    "Variability exists across customers in billing frequency and structure"
  ],
  "merchant_specific": [
    "Inspection-based usage model (e.g., 800 inspections per year threshold)",
    "Sean is the sole in-house finance hire and primary contact for contract/billing matters",
    "Sean's personality: 'guys guy', enjoys golf and sports, described as 'space cadet'",
    "Victoria is the Rev Ops influencer, detail-oriented, prioritizes Hubspot integration",
    "Hubspot is the merchant's CRM system",
    "Two-stakeholder approval structure: Champion (Sean) and Influencer (Victoria)",
    "Contract ingestion from CRM is a critical requirement for this merchant"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: MIS_ Truepic_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:17:03

### Original Content
```
Merchant Name: Truepic Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Most contracts are standard order forms About half of contracts will have a prepaid ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Usage-Based Billing and Overage Management",
    "Prepaid Commitments and Usage AI Configuration",
    "Integration and Events Processing",
    "Post-Processing Communications and Feature Requests"
  ],
  "rules": [
    {
      "rule": "Item names should use the item description from the contract",
      "category": "Contract Processing"
    },
    {
      "rule": "Quantity should use the listed quantity (e.g., 120 inspections) if stated; default to 1 if not specified",
      "category": "Contract Processing"
    },
    {
      "rule": "Total Price should use the full price shown in the table for committed/prepaid amount",
      "category": "Contract Processing"
    },
    {
      "rule": "Total price must match the invoicing frequency",
      "category": "Contract Processing"
    },
    {
      "rule": "Use in-line discounting - include waived BTs with 100% in-line discount",
      "category": "Contract Processing"
    },
    {
      "rule": "Service Start Date should use 'Effective Start Date' from the order form",
      "category": "Contract Processing"
    },
    {
      "rule": "Billing Start Date is the same as Service Start Date",
      "category": "Contract Processing"
    },
    {
      "rule": "Months of Service should be calculated based on contract length (typically 12 months unless stated otherwise)",
      "category": "Contract Processing"
    },
    {
      "rule": "Frequency will be listed in the 'Payments' section, often Monthly or Annual Upfront",
      "category": "Contract Processing"
    },
    {
      "rule": "'Upfront' payment terms means net 0 days",
      "category": "Contract Processing"
    },
    {
      "rule": "About half of contracts will have a prepaid upfront BT which requires Usage AI to be turned on",
      "category": "Usage AI"
    },
    {
      "rule": "For prepaid amounts with usage, select 'Has Usage Requirements' and 'Has Threshold'",
      "category": "Usage AI"
    },
    {
      "rule": "Threshold period should be set to 'Full service term'",
      "category": "Usage AI"
    },
    {
      "rule": "Threshold amount should be the prepaid annual amount/minimum commitment",
      "category": "Usage AI"
    },
    {
      "rule": "When a single line-item has multiple BTs, differentiate between Flat BT (prepaid) and Usage BT (overage)",
      "category": "Billing Types"
    },
    {
      "rule": "Flat BT can be called 'Annual Minimum Commitment'",
      "category": "Billing Types"
    },
    {
      "rule": "Usage BT can be called 'Vision Pay-as-you-Go Inspections' (use best judgment)",
      "category": "Billing Types"
    },
    {
      "rule": "For overage usage BTs, use the correct overage unit price (could be regular unit price or increased rate)",
      "category": "Overage Processing"
    },
    {
      "rule": "When prepaid annual amount is at a cheaper rate than overage rate, create 2 separate usage BTs",
      "category": "Overage Processing"
    },
    {
      "rule": "First usage BT should use the unit price that the prepaid amount is billed at, using event 'inspections'",
      "category": "Overage Processing"
    },
    {
      "rule": "Second usage BT should use the overage rate unit price, using event 'inspections (overage)' and add '(Overage)' to the item name",
      "category": "Overage Processing"
    },
    {
      "rule": "For Usage AI with overage rates, select the regular rate NOT the overage rate in 'Included products'",
      "category": "Usage AI"
    },
    {
      "rule": "The overage rate product should have '(Overage)' at the end",
      "category": "Usage AI"
    }
  ],
  "exceptions": [
    {
      "exception": "If there is an overage rate, create a usage BT for BOTH the regular amount and the overage amount",
      "condition": "When overage rate differs from regular rate"
    },
    {
      "exception": "If prepaid BT is billed on a different cadence, adjust the total price accordingly",
      "condition": "When billing cadence differs from standard"
    },
    {
      "exception": "Contract length may vary from typical 12 months if stated otherwise",
      "condition": "When contract explicitly specifies different length"
    },
    {
      "exception": "If there is only 1 rate for Usage AI, use that rate; if there is an overage rate, select the regular rate NOT the overage rate",
      "condition": "When configuring Usage AI included products"
    },
    {
      "exception": "Customer doesn't get charged until they have gone over the prepaid amount",
      "condition": "When Usage AI is configured for prepaid/committed amounts"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Truepic",
      "type": "Merchant Identity"
    },
    {
      "element": "Implementation POC and CX POC fields to be filled",
      "type": "Contact Information"
    },
    {
      "element": "Billing model section to be filled by Implementation",
      "type": "Customizable Section"
    },
    {
      "element": "Unique customer creation process information",
      "type": "Customizable Section"
    },
    {
      "element": "Contract Processing Steps section to be filled Post-Go Live by Implementation Success",
      "type": "Customizable Section"
    },
    {
      "element": "Events Processing section to be filled Post-Go Live",
      "type": "Customizable Section"
    },
    {
      "element": "Integration Items Processing section with merchant-specific labeling instructions",
      "type": "Customizable Section",
      "examples": [
        "All Statsig integration items should be labeled as 'Sales'",
        "All 'Pinata' integration items should be labeled as 'Software Subscription Bundle'"
      ]
    },
    {
      "element": "Post Processing Communications section specifying notification requirements",
      "type": "Customizable Section",
      "example": "Customer Success [Azmat Aziz] needs to be notified in Messari internal merchant channel when contracts are processed"
    },
    {
      "element": "Customer Information section for special customer-specific requirements",
      "type": "Customizable Section"
    },
    {
      "element": "Feature Requests section tracking QBO payment links, HS syncing, and revenue reporting needs",
      "type": "Customizable Section"
    },
    {
      "element": "Merchant-specific terminology: 'Vision Pay-as-you-Go Inspections', 'Annual Minimum Commitment'",
      "type": "Terminology"
    },
    {
      "element": "Usage event names: 'inspections', 'inspections (overage)'",
      "type": "Event Naming"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: MIS_ Truepic_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:17:11

### Original Content
```
Jason (Engineer, Influencer) is their technical lead Very social and open to working through ideas on the best way to partner Tom (Fractional Accountant, Influencer) is na older finance vet who had always used Maxio Loves our contract based approach and is speaking with our partnerships team 3) What are the Tabs features that the key POC cares about HS Integration and QBO integration Tabs being the source of truth and moving them out of Excel spreadsheets Contract-first, AI-powered automation: E...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Key stakeholder personas and their motivations",
    "Product integration requirements (HubSpot and QuickBooks Online)",
    "Contract-based billing and revenue recognition automation",
    "Financial workflow automation and system of record",
    "Collections and cash flow management features"
  ],
  "rules": [
    "Tabs must integrate with HubSpot (HS) for CRM functionality",
    "Tabs must integrate with QuickBooks Online (QBO) for accounting",
    "Tabs should serve as the single source of truth replacing Excel spreadsheets",
    "Billing and revenue recognition rules must be extracted directly from contracts",
    "System must support contract-first approach with AI-powered automation",
    "Billing logic must accommodate ramp-ups, monthly/annual billing, overages, and varied renewal structures",
    "Journal entries must sync with QBO with capability for auto-push",
    "Revenue recognition must support straight-line, prorated methods, and category tagging",
    "Journal entries must be exportable",
    "Collections automation must include scheduled invoices, reminder emails, Slack alerts, and dunning processes",
    "Cash forecast engine must learn from customer payment behavior patterns",
    "Technical leads require social collaboration and idea-sharing approach",
    "Finance veterans with Maxio experience respond positively to contract-based methodology"
  ],
  "exceptions": [
    "Tom (Fractional Accountant) has prior Maxio experience which influences his preference for contract-based approach",
    "Jason (Engineer) requires more collaborative, social engagement style versus standard sales approach",
    "Eventual auto-push of journal entries (implies phased implementation or optional feature)",
    "Custom cash forecast engine suggests non-standard forecasting requirements beyond basic AR aging"
  ],
  "merchant_specific": [
    "Stakeholder names and roles: Jason (Engineer/Influencer/Technical Lead), Tom (Fractional Accountant/Influencer)",
    "Current state: Using Excel spreadsheets for financial tracking",
    "Historical context: Tom's prior experience with Maxio platform",
    "Integration requirements: Specific to HubSpot and QuickBooks Online",
    "Communication preferences: Slack alerts for collections",
    "Organizational structure: Uses fractional/part-time accountant model",
    "Partnership discussions: Tom is actively engaged with partnerships team"
  ],
  "confidence_score": 0.85
}
```

---

