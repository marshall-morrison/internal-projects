# Raw LLM Analysis: Merchant Info Sheet - Brevity

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:57:51

---

## Chunk 1: Merchant Info Sheet - Brevity_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:57:51

### Original Content
```
Merchant: Brevity Demo date: Mar 14, 2025 Scoping start date: N A MSA Signature Date: Mar 19, 2025 Onboarding Kick Off Date: March 23, 2025 [If Exists] Opt Out Date: No opt out Go Live Date: ASAP GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: N A CFO: Jeff Fischer Customer service rep who is really involved: Brad Janicki Account Receivable POC: Jeff Fischer   Brad Janicki Billing POC: Jeff Fischer Company summary (AE to fill) Summary of what company does: B...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "Billing and Revenue Recognition Processes",
    "System Integration and Data Synchronization Challenges",
    "Contract Processing and Subscription Management",
    "Scalability and Growth Planning"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Start Date",
      "description": "Start Date is the 1st of the month following the Effective Date, unless the Effective Date is already the 1st of the month",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Contract Dates",
      "description": "All contracts must use the subscription period (not signing date) for service and revenue start and end dates",
      "explicit": true
    },
    {
      "rule_id": "R3",
      "category": "Revenue Category Classification",
      "description": "Contracts 11+ months are classified as 'Seat Fee - Annual Subscription'",
      "explicit": true
    },
    {
      "rule_id": "R4",
      "category": "Revenue Category Classification",
      "description": "Contracts less than 11 months are classified as 'Seat Fee - Pilot Subscription'",
      "explicit": true
    },
    {
      "rule_id": "R5",
      "category": "Revenue Category Classification",
      "description": "Implementation services are classified as 'Implementation services fee - Service'",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Contract Fields",
      "description": "Item Description field should be left blank during contract processing",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Contract Fields",
      "description": "Integration Item field should be left blank during contract processing",
      "explicit": true
    },
    {
      "rule_id": "R8",
      "category": "Billing Type",
      "description": "Billing Type must be either Flat or Usage",
      "explicit": true
    },
    {
      "rule_id": "R9",
      "category": "Contract Termination",
      "description": "No opt-out clause exists for this merchant",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Start date rule exception: If Effective Date falls on the 1st of the month, use that date instead of the following month's 1st",
      "condition": "Effective Date is on the 1st of the month"
    },
    {
      "exception_id": "E2",
      "description": "Trial contracts exist for 2-6 months with goal to transition to annual or multi-year contracts",
      "condition": "Customer is in trial period"
    },
    {
      "exception_id": "E3",
      "description": "Contract duration threshold of 11 months determines revenue category classification (Annual vs Pilot)",
      "condition": "Contract duration relative to 11 months"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "Brevity Demo - AI-powered sales training solutions company"
    },
    {
      "element": "Key Personnel",
      "details": "CFO: Jeff Fischer, Customer Service: Brad Janicki, AR POC: Jeff Fischer & Brad Janicki"
    },
    {
      "element": "Current Systems",
      "details": "Stripe (billing), QuickBooks (accounting), HubSpot (CRM) - currently not well-integrated"
    },
    {
      "element": "Billing Model",
      "details": "Per-seat subscription model with trial contracts (2-6 months) transitioning to annual/multi-year"
    },
    {
      "element": "Contract Volume",
      "details": "Currently averaging 5 contracts/month, projected to scale to 25-30 contracts/month by EOY"
    },
    {
      "element": "Manual Workflow",
      "details": "Sales contract → Brad converts to Stripe subscription → connect to backend platform → send invoice → customer pays → activate subscription → subscription goes live"
    },
    {
      "element": "Pain Points",
      "details": "Manual processes causing errors, lack of system integration, data inconsistencies in MRR/ARR tracking, scalability concerns"
    },
    {
      "element": "Product Identification",
      "details": "Item Name sourced from Product column in contract"
    },
    {
      "element": "Service Duration",
      "details": "Subscription Duration field used for Months of Service"
    },
    {
      "element": "Go Live Timeline",
      "details": "ASAP - with onboarding kick-off on March 23, 2025"
    },
    {
      "element": "Revenue Categories",
      "details": "Three specific categories: Seat Fee - Annual Subscription, Seat Fee - Pilot Subscription, Implementation services fee - Service"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Brevity_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:57:59

### Original Content
```
Total Price: Identify the "Total Cost" for flat pricing and  Unit Cost  for usage  0 BTs to be added as well If implementation fee waived, it should still be shown with a 100  discount Quantity: Under the Quantity column Periods: Locate the "Subscription Duration" Include the renewal period (only if the contract mentions auto renewal) For example, if initial term is 1 year and the renewal term is 1 additional year, then process both years Invoicing Cadence Usually entirely upfront billing (ie: o...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Invoice Generation",
    "Revenue Recognition and Accounting Configuration",
    "SKU-Specific Processing Rules (Seats and Implementation Fee)",
    "Default Values and Operational Standards",
    "Merchant Relationship Management and Communication Protocols"
  ],
  "rules": [
    {
      "category": "Pricing",
      "rule": "Identify 'Total Cost' for flat pricing and 'Unit Cost' for usage",
      "details": "0 BTs (base transactions) to be added as well"
    },
    {
      "category": "Pricing",
      "rule": "If implementation fee is waived, show it with 100% discount",
      "details": "Fee should still appear on invoice"
    },
    {
      "category": "Contract Terms",
      "rule": "Include renewal period only if contract mentions auto-renewal",
      "details": "Example: If initial term is 1 year and renewal is 1 additional year, process both years"
    },
    {
      "category": "Billing",
      "rule": "Default billing is entirely upfront (one invoice for entire contract)",
      "details": "Invoicing cadence is usually upfront billing"
    },
    {
      "category": "Payment Terms",
      "rule": "Net payment terms are dictated by contract",
      "details": "Can vary: net 0, net 30, or net 15"
    },
    {
      "category": "SKU - Implementation Fee",
      "rule": "Revenue Recognition all on same day contract starts"
    },
    {
      "category": "SKU - Implementation Fee",
      "rule": "Revenue Category must be 'Service'"
    },
    {
      "category": "SKU - Implementation Fee",
      "rule": "QBO Item must be 'Implementation Fees'"
    },
    {
      "category": "SKU - Seats",
      "rule": "Revenue Recognition must match contract subscription period"
    },
    {
      "category": "SKU - Seats",
      "rule": "Revenue Category must be 'Annual Subscription' or 'Pilot Subscription'"
    },
    {
      "category": "SKU - Seats",
      "rule": "QBO Item must be 'Seats' if contract is for more than 11 months (annual contract)"
    },
    {
      "category": "Defaults",
      "rule": "Default Service Term: 1 Year (if none listed)"
    },
    {
      "category": "Defaults",
      "rule": "Default Net Payment Terms: 0 (if none listed)"
    },
    {
      "category": "Defaults",
      "rule": "Default Billing Frequency: Monthly (if none listed)"
    },
    {
      "category": "Taxes",
      "rule": "Every tax line item becomes a BT (base transaction) if none listed"
    },
    {
      "category": "Business Model",
      "rule": "Subscriptions are primarily per seat"
    },
    {
      "category": "Business Model",
      "rule": "Consumption-driven model exists but not fully operationalized (tracking minutes used)"
    }
  ],
  "exceptions": [
    {
      "condition": "Contract mentions auto-renewal",
      "action": "Include renewal period in processing"
    },
    {
      "condition": "Implementation fee is waived",
      "action": "Still show fee with 100% discount"
    },
    {
      "condition": "Contract is for more than 11 months",
      "action": "Classify as annual contract with QBO Item of 'Seats'"
    },
    {
      "condition": "Contract is trial-based",
      "action": "Use 'Pilot Subscription' as Revenue Category"
    },
    {
      "condition": "Merchant requests specific processing differences",
      "action": "Follow merchant-specific instructions (e.g., back-date invoice to final day of month)"
    },
    {
      "condition": "Integration items from Statsig",
      "action": "Label as 'Sales'"
    },
    {
      "condition": "Integration items from Pinata",
      "action": "Label as 'Software Subscription Bundle' unless otherwise noted"
    },
    {
      "condition": "Certain customers require special memos",
      "action": "Add special memos to specific invoices based on merchant-customer relationship"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant temperament",
      "description": "Described as 'both straightforward and kind'"
    },
    {
      "element": "Key POC identification",
      "description": "Document template includes section for identifying key point of contact"
    },
    {
      "element": "Contract-specific processing variations",
      "description": "Some merchants may request different processing (e.g., back-dating invoices)"
    },
    {
      "element": "Post-processing notifications",
      "description": "Customizable by merchant - who to notify, where, and when (e.g., Customer Success in merchant channel when contracts processed)"
    },
    {
      "element": "Integration item labeling",
      "description": "Varies by integration partner (Statsig vs Pinata have different labels)"
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos and invoice changes based on merchant-customer relationships"
    },
    {
      "element": "Feature requests",
      "description": "Merchant-specific feature requests tracked with importance and urgency"
    },
    {
      "element": "Events and Integration processing",
      "description": "To be filled by Implementation Success team on per-merchant basis"
    },
    {
      "element": "Rewatch calls section",
      "description": "Merchant-specific call recordings (Discovery, Demo) with dates"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Brevity_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:58:01

### Original Content
```
: who is the buyer decision maker ) Jeff is the Champion, Kelvin (CEO) is the EB, and Brad is the coach 3) What are the Tabs features that the key POC cares about Simplify Pricing Complexity: Accommodate flexible pricing models and unique contract terms Streamline Revenue Processes: Integrate revenue tracking and forecasting into a single platform, reducing manual errors and improving data accuracy Jeff is going to care about Revenue   ARR Brad is going to care about the process - contracts   bi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder identification and role mapping",
    "Decision-maker hierarchy and influence patterns",
    "Feature-to-stakeholder alignment",
    "Revenue and financial process management",
    "Contract and billing workflow optimization"
  ],
  "rules": [
    "Identify three key stakeholder roles: Champion, Economic Buyer (EB), and Coach",
    "Map specific individuals to decision-making roles (Champion, EB, Coach)",
    "Align product features to stakeholder concerns based on their role",
    "Champion role focuses on revenue and ARR metrics",
    "Coach role focuses on operational processes (contracts and billing)",
    "Economic Buyer (typically C-level) has final decision authority",
    "Product positioning must address pricing complexity and flexibility",
    "Solution must integrate revenue tracking and forecasting capabilities",
    "Emphasize reduction of manual errors and improved data accuracy in value proposition"
  ],
  "exceptions": [
    "Stakeholder role assignments may vary by organization structure",
    "Feature priorities may shift depending on which stakeholder has primary influence",
    "CEO may not always be the Economic Buyer in all sales scenarios"
  ],
  "merchant_specific": [
    "Stakeholder names and titles (Jeff, Kelvin, Brad)",
    "Specific organizational hierarchy and reporting structure",
    "Relative importance of revenue vs. process concerns may vary by company",
    "Definition of 'flexible pricing models' and 'unique contract terms' specific to merchant's business model",
    "Integration requirements with existing revenue and billing systems",
    "Specific pain points around pricing complexity unique to this merchant"
  ],
  "confidence_score": 0.85
}
```

---

