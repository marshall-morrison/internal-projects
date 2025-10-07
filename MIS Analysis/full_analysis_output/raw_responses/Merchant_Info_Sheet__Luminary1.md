# Raw LLM Analysis: Merchant Info Sheet_ Luminary(1)

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:50:55

---

## Chunk 1: Merchant Info Sheet_ Luminary(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:55

### Original Content
```
If the number of user seats changes, each rev schedule should only be as long as the billing schedule If the number of seats stays the same across multiple billing schedules, the revenue schedules should extend for the duration of the total billing schedules For example, in the picture below this would be a RS BT for Y1, a different RS BT for Y2, and a third RS BT for Y3 The rev schedules would not be Y1-3 This is necessary to show an increase in GAAP revenue across the periods which is importan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Management and Billing Term Alignment",
    "Seat-Based Pricing and User Count Changes",
    "Usage-Based Billing and Overage Handling",
    "GAAP Revenue Recognition Requirements",
    "Item Description Documentation Standards"
  ],
  "rules": [
    "When user seats change, each revenue schedule (RS) must match the length of its corresponding billing schedule",
    "When seat count remains constant across multiple billing schedules, revenue schedules should extend for the total duration of all billing schedules",
    "Revenue schedules must be created separately for each period when seat counts change (e.g., separate RS BT for Y1, Y2, Y3)",
    "Flat fees must be billed at the first of the period",
    "Item descriptions for Luminary Platform Access must include authorized users and active clients",
    "Additional Users billing terms must use event-based triggers and always be unit price billing terms",
    "Additional Users billing terms must be recurring monthly but priced for the entire term",
    "When additional users are added mid-term, usage data must account for the partial term (prorated calculation)",
    "Revenue schedule structure must demonstrate GAAP revenue increase across periods for CEO reporting"
  ],
  "exceptions": [
    "If there is NO overage price for users/households/plans, then no usage-based billing term should be created for users",
    "If there IS an overage cost, a separate billing term must be created with the 'Additional Users' event",
    "Partial term additions require prorated usage data uploads (e.g., 0.75 for 9 months of a 12-month term)"
  ],
  "merchant_specific": [
    "Reference to 'Luminary Platform Access' suggests this may be specific to a particular merchant or product line",
    "CEO requirement for GAAP revenue increase visibility indicates executive-level reporting customization",
    "The specific event name 'Additional Users' may be merchant-configured",
    "Screenshot references suggest merchant-specific UI/system locations for data retrieval",
    "The merchant is responsible for creating and uploading usage data for partial term additions",
    "Terminology like 'authorized users', 'active clients', 'households', and 'plans' may vary by merchant context"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Merchant Info Sheet_ Luminary(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:57

### Original Content
```
merchant Demo date: Oct 2nd, 2024 Scoping start date: Sep 30, 2024 MSA Signature Date: Nov 7, 2024 Onboarding Kick Off Date: Nov 13, 2024 Go Live Date: Dec 12, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Account Receivable POC: Jemima Law, Head of BizOps Billing POC: Mary Huang, Chief Commercial Officer - https: www linkedin com in maryhuan9  Accountant: Joy Hu, CPA at Attivo Company summary (AE to fill) Luminary is a technology platform that automates the comp...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Billing and Contract Structure",
    "Implementation Process and Requirements",
    "Merchant Business Context and Goals"
  ],
  "rules": [
    {
      "rule": "US TEAM ONLY: Customer Name must be correct based on Advisor Name",
      "category": "data_entry",
      "explicit": true
    },
    {
      "rule": "Must ping Ashni Waliaand Marshall Morrison once contract is processed",
      "category": "notification",
      "explicit": true
    },
    {
      "rule": "Use Billing POC Name, Email and Address when creating customers",
      "category": "customer_creation",
      "explicit": true
    },
    {
      "rule": "If contract has no info, create customer with any available information",
      "category": "customer_creation",
      "explicit": true
    },
    {
      "rule": "Subscription SKU may extend across multiple years",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Contract is structured as 2-page document covering subscription and payments",
      "category": "contract_structure",
      "explicit": true
    },
    {
      "rule": "Billing model includes flat platform fee (pre-determined or prorated by seats) and tiered pricing for active clients",
      "category": "billing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "If contract has no billing POC information, use any available information to create customer",
      "condition": "Missing contract information",
      "action": "Use alternative available data"
    },
    {
      "exception": "Platform fee can be either pre-determined OR prorated by number of seats",
      "condition": "Flexible billing arrangement",
      "action": "Apply appropriate fee structure"
    },
    {
      "exception": "US TEAM ONLY restriction on customer name verification process",
      "condition": "Geographic team restriction",
      "action": "Only US team performs this specific task"
    }
  ],
  "merchant_specific": [
    {
      "element": "Stakeholder names and roles",
      "examples": [
        "Jemima Law (Head of BizOps)",
        "Mary Huang (Chief Commercial Officer)",
        "Joy Hu (CPA at Attivo)"
      ],
      "customizable": true
    },
    {
      "element": "Project timeline dates",
      "examples": [
        "Demo date: Oct 2nd, 2024",
        "Go Live Date: Dec 12, 2024"
      ],
      "customizable": true
    },
    {
      "element": "Business context",
      "examples": [
        "Estate planning technology platform",
        "Founded in 2022",
        "Recently eliminated outsourced accounting firm"
      ],
      "customizable": true
    },
    {
      "element": "Billing model specifics",
      "examples": [
        "Flat Platform Fee + Tiered pricing for active clients",
        "Pricing based on number of seats and active clients"
      ],
      "customizable": true
    },
    {
      "element": "Opt-out clause status",
      "value": "No opt-out clause",
      "customizable": true
    },
    {
      "element": "Integration requirements",
      "examples": [
        "ERP integration",
        "Tax Integration"
      ],
      "customizable": true,
      "note": "Fields present but not filled in this document"
    },
    {
      "element": "Customer creation process uniqueness",
      "value": "N/A for this merchant",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet_ Luminary(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:09

### Original Content
```
Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant None Feature Requests (AE Implementation Success to fill) Hubspot Customer Data syncing to Tabs Currently use HS as the source of truth for revenue and want to have Tabs act as a CRM for their customers Rewatch Calls (AE Implementation Success to fill) Intro Call 9 30 24 https: tabs rewatch com video k7fq9guhdnw465z0-mary-and-rebecca-schwartz-tabs-september-30-2024 Custom Demo ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Relationship Management and Integration",
    "Pricing Structure and Billing Configuration",
    "Feature Requirements and System Integration",
    "Merchant Relationship Intelligence",
    "Usage Tracking and Item Mapping"
  ],
  "rules": [
    "Hubspot must be synced with Tabs for customer data",
    "Hubspot serves as the source of truth for revenue data",
    "Tabs should function as a CRM for customers",
    "DocuSign forwarding is used for new deals",
    "Pricing model uses flat platform fee combined with tiered unit pricing for active clients",
    "SSO integration is required for platform access",
    "Usage billing must be tracked and reported",
    "Renewals management functionality is required",
    "Reporting capabilities are a key feature requirement",
    "Multiple item types must be tracked: Platform Access, SSO integration, Additional Users, and Active Client Fee"
  ],
  "exceptions": [
    "Ops International Team should ignore certain notes sections (specifically marked sections)",
    "Platform Access can be tracked as either 'Luminary Platform Access' or 'any other subscription as shown in contract'",
    "Active client fee has tiered pricing (not flat rate like platform fee)"
  ],
  "merchant_specific": {
    "merchant_name": "Luminary",
    "key_contacts": [
      "Mary (buyer/decision maker, former Peloton colleague of Arjun)",
      "Jemima (buyer/decision maker)",
      "Rebecca Schwartz"
    ],
    "merchant_temperament": "Easy to work with, intelligent",
    "relationship_context": "Mary worked with Arjun at Peloton - existing professional relationship",
    "custom_item_names": [
      "Luminary Platform Access",
      "Luminary Builder Platform Access",
      "Additional User",
      "Active Client Fee"
    ],
    "integration_tools": [
      "Hubspot",
      "DocuSign",
      "SSO"
    ],
    "referenced_documents": [
      "Luminary Tabs usage template",
      "Usage data sheet",
      "Intro Call recording (9/30/24)",
      "Custom Demo recording (10/2/24)"
    ],
    "priority_features": [
      "Usage billing",
      "Renewals Management",
      "Reporting"
    ]
  },
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet_ Luminary(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:11

### Original Content
```
All additional users are billed on the calendar month If a deal is signed on May 15th, the Subscription SKUs would be billed May 15th for the period May 15, 2024 - May 14, 2025 and the Additional User item would be billed June 1, recurring monthly for 12 months Solution Tier billing item should always be a quantity of 1 Ignore the number of authorized users Number of clients SKU Many contracts bill by the number of active clients (customers) These may be priced at  x each year which means they s...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Cycles and Frequencies",
    "Subscription and User Management",
    "Product SKU Configuration",
    "Payment Terms and Service Defaults",
    "Tax Handling and Post-Processing"
  ],
  "rules": [
    {
      "rule": "Additional users are billed on the calendar month basis",
      "category": "billing_frequency"
    },
    {
      "rule": "Subscription SKUs are billed from the deal signing date for a 12-month period",
      "category": "billing_cycle",
      "example": "Deal signed May 15th bills May 15, 2024 - May 14, 2025"
    },
    {
      "rule": "Additional User items bill monthly starting the 1st of the month following deal signing, recurring for 12 months",
      "category": "billing_cycle"
    },
    {
      "rule": "Solution Tier billing item must always have a quantity of 1",
      "category": "product_configuration"
    },
    {
      "rule": "Ignore the number of authorized users when configuring Solution Tier",
      "category": "product_configuration"
    },
    {
      "rule": "Number of clients SKU is always billed on the calendar quarter",
      "category": "billing_frequency"
    },
    {
      "rule": "Client SKU billing must start on January 1, April 1, July 1, or October 1, recurring every 3 months",
      "category": "billing_cycle"
    },
    {
      "rule": "Client SKU pricing should be divided by 4 for quarterly billing",
      "category": "pricing"
    },
    {
      "rule": "Default service term is 1 year",
      "category": "service_terms"
    },
    {
      "rule": "Default net payment terms are 30 days",
      "category": "payment_terms"
    },
    {
      "rule": "Default billing frequency: Annual for subscriptions, Quarterly for active client fee, Monthly for number of users",
      "category": "billing_frequency"
    },
    {
      "rule": "No extra tax line item should be added",
      "category": "tax_handling"
    },
    {
      "rule": "Taxes are computed by Quickbooks",
      "category": "tax_handling"
    }
  ],
  "exceptions": [
    {
      "exception": "Ops Team notification requirement is temporary",
      "details": "Message in luminary and CC Arjun Gopalratnam only necessary for Dec 2024 - Feb 2025. After that, no communication needed",
      "time_bound": true
    },
    {
      "exception": "No items to ignore in contracts",
      "details": "Explicitly states 'None' for contract items to ignore"
    },
    {
      "exception": "No specific merchant processing requests",
      "details": "No custom processing like back-dating invoices mentioned"
    }
  ],
  "merchant_specific": [
    {
      "element": "AST Events Processing and Integration Items",
      "customization_needed": "Implementation Success team to fill if necessary"
    },
    {
      "element": "Post Processing Communications",
      "customization_needed": "Implementation Success team to fill if necessary"
    },
    {
      "element": "Notification recipient",
      "details": "Arjun Gopalratnam specified as CC recipient for batch completion notifications"
    },
    {
      "element": "Communication channel",
      "details": "Luminary specified as the messaging platform"
    },
    {
      "element": "Product terminology",
      "terms": ["Solution Tier", "Additional User item", "Number of clients SKU", "active client fee"]
    }
  ],
  "confidence_score": 0.92
}
```

---

