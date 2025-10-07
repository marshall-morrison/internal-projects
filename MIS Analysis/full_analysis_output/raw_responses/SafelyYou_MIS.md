# Raw LLM Analysis: SafelyYou MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:27:08

---

## Chunk 1: SafelyYou MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:27:08

### Original Content
```
g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Proce...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Invoice and billing processing procedures",
    "Post-implementation communication and handoff protocols",
    "Merchant relationship management and customer-specific handling",
    "Integration and feature configuration requirements"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year when none is listed",
      "category": "Defaults",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 30 days when none is specified",
      "category": "Defaults",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly when none is listed",
      "category": "Defaults",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "AE fills Merchant Calls for all videos prior to Implementation involvement; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation is the completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "All Statsig integration items should be labeled as 'Sales'",
      "context": "Integration Items Processing",
      "type": "Vendor-specific labeling"
    },
    {
      "exception": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "context": "Integration Items Processing",
      "type": "Vendor-specific labeling with merchant override"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "context": "Customer Information",
      "type": "Relationship-based customization"
    },
    {
      "exception": "Invoice changes may be required due to merchant customer relationship",
      "context": "Customer Information",
      "type": "Relationship-based customization"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing instructions",
      "customizable": true,
      "description": "Important information on events billing varies by merchant"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "description": "Instructions for assigning integration items depend on the specific integrations used"
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "description": "Who needs to be notified, where, and when varies by merchant (example: Customer Success Azmat Aziz via Messari internal merchant channel)"
    },
    {
      "element": "Customer-specific information",
      "customizable": true,
      "description": "Special handling for specific customers of the merchant, including memo requirements"
    },
    {
      "element": "Merchant temperament and POC preferences",
      "customizable": true,
      "description": "Personality traits and communication styles of merchant contacts (example: Hannah is kind and sings, Dan is kind but less sing-song)"
    },
    {
      "element": "Tabs features preferences",
      "customizable": true,
      "description": "Key POC cares about specific features, documented in merchant-specific requirements documents"
    },
    {
      "element": "Billing methodology",
      "customizable": true,
      "description": "How merchant bills (usage vs flat fees), typically monthly"
    },
    {
      "element": "Feature requests",
      "customizable": true,
      "description": "Merchant-specific feature requests with urgency and importance ratings"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: SafelyYou MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:27:16

### Original Content
```
Merchant Name: SafelyYou Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Locate BTs in the pricing table under the Order Form section This merchan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Type Determination (Flat Fee vs Usage)",
    "Revenue Schedule Creation and Proration Logic",
    "Service Start Date and Billing Start Date Calculations",
    "Contract Term Management and Renewal Processing",
    "Sub-customer and Service Site Specific Billing"
  ],
  "rules": [
    "Each sub-customer is billed separately and should already be set in the contract",
    "Only process the service site associated with the sub-customer",
    "Perform global search as pricing may change within contracted term",
    "If maximum number of beds is being used, create flat fee product; otherwise create usage product",
    "For flat fee, use 'first of period' billing timing",
    "For usage, use 'bill last of period' billing timing",
    "Exception: If both flat and usage products exist on a contract, both should use 'bill last of period'",
    "Service Start Date: Use 8 months after the Effective Date (for non-live contracts)",
    "For live contracts: Use date in column D unless contract effective date is earlier than 2024, then use column C",
    "Create MONTH 1 BT for EVERY community regardless of service start date",
    "Month 1 BT has Periods: 1 and Frequency: 1 month",
    "Month 1 BT item name should include '- Month 1' suffix",
    "Month 1 BT billing start date is the first of the month",
    "Do not prorate Month 1 BT",
    "Create prorated first month BT (REV SCHED 1/2) with billing start date matching service start date",
    "Prorated BT frequency is calculated as days remaining to end of month",
    "For flat fee prorated BT: Total Price = min monthly × (days of service remaining / days in month)",
    "Create REV SCHED 2/2 for remainder of term starting first of following month",
    "REV SCHED 2/2 periods = Subscription Term months minus 1",
    "Item Name should match product in reference spreadsheet column C",
    "Do not include 'Insights' in item name",
    "Use 'SafelyYou Respond AL' if column specifies 'Min Active AL Beds'",
    "Item Description: Use column E from reference spreadsheet",
    "Integration Item: Use column D from reference spreadsheet",
    "Quantity for flat fee: use total beds value",
    "Quantity for usage: n/a",
    "Total Price for flat fee: use Min Monthly column",
    "Total Price for usage: use price per bed (or discounted price if available)",
    "Event to track: use name following 'Min Active' in column",
    "No duplicate events to track - flag if two BTs have same billing period frequency and same event",
    "Net Terms: Default to Net 30 if not explicitly listed",
    "Frequency: Set to Monthly unless stated otherwise",
    "DO NOT create Usage AI (no longer required)",
    "For renewal terms: duplicate Rev Sched 2/2, adjust for following year with periods = 12",
    "Renewal BT service start and billing start dates begin day after last billing period",
    "Renewal BTs should not be split into two product billing periods",
    "Last BT year should match column D",
    "DO NOT process implementation fees",
    "For alternative contract format: Create flat fee BT for minimum beds plus separate usage BT for monthly fee per bed",
    "Alternative format usage BT does not require Usage AI",
    "Ignore: Implementation section fees, additional cameras, 100% discounted BTs, SafelyYou-Clarity BETA program, excess camera installs"
  ],
  "exceptions": [
    "If contract effective date is BEFORE 2025, leave as 'new' and flag in pylon ticket",
    "If using column C and Year in C does NOT equal Year in D, check for automatic renewal clause and create additional renewal BTs if present",
    "If both flat and usage products exist on contract, both must use 'bill last of period' (overrides standard flat fee timing)",
    "Historical contracts: Use dates from specific spreadsheet (Rate & Go Live tab)",
    "For contracts with different format (example: 118eae00-c274-4bf1-843a-ad3c5e6232ac), create flat fee for minimum beds plus separate usage BT without Usage AI",
    "If confused by different contract formats, create processing reminders ticket",
    "Month 1 BT is created for EVERY community regardless of service start date (no exceptions)",
    "Prorated first month BT uses actual service start date, not first of month"
  ],
  "merchant_specific": [
    "Merchant Name: SafelyYou",
    "Product names: SafelyYou-Respond, SafelyYou Respond MC, SafelyYou Respond AL, SafelyYou-Clarity BETA",
    "Service labels include 'Insights' designation",
    "Reference to specific spreadsheet with Rate & Go Live tab for historical contract dates",
    "Reference to pricing table location under Order Form section",
    "Sub-customer billing structure (e.g., Brightview - Woodbury Lake)",
    "Specific contract example IDs referenced: 436bfc7f-bb5e-4326-ac33-d38f5571c5f3, 118eae00-c274-4bf1-843a-ad3c5e6232ac",
    "8-month implementation period from Effective Date to Service Start Date",
    "Bed-based pricing model (MC beds, AL beds)",
    "Event tracking based on bed types",
    "Integration with external spreadsheet for product mapping (columns C, D, E)",
    "Pylon ticket system for flagging issues",
    "POC fields: Implementation POC and CX POC to be filled",
    "Implementation Success team responsible for post-go-live contract processing"
  ],
  "confidence_score": 0.92
}
```

---

