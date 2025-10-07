# Raw LLM Analysis: MIS_ Bland

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:41:24

---

## Chunk 1: MIS_ Bland_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:24

### Original Content
```
, annual), set to Annual If the BT covers a one-time onboarding or milestone, set to None If billed quarterly, use 3 Months Make sure to look at the sections below the order form total to see if billing cadence is listed there  Billing Terms:   Additional Terms:  Net Terms Use payment terms if available If specific days are not listed, default to 30 Revenue Categories  Pilot  First pilot month  Professional Services  Implementation Enterprise services Forward deployed engineer Implementation and...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Configuration and Categorization",
    "Revenue Category Classification",
    "Usage-Based Pricing and Commitment Models",
    "Payment Terms and Billing Cadence",
    "Usage AI Model Configuration"
  ],
  "rules": [
    "If billing cadence is monthly, quarterly, or annual, set to Annual",
    "If BT covers one-time onboarding or milestone, set billing cadence to None",
    "If billed quarterly, use 3 Months as the billing period",
    "Check sections below order form total for billing cadence information",
    "Default to Net 30 payment terms if specific days are not listed",
    "Use payment terms if available in the document",
    "Platform is the default revenue category for all subscription products",
    "Committed usage should be its own flat BT if included in order form total",
    "Usage BTs are often in fine print and must be identified",
    "Free usage events (e.g., free minutes) must be incorporated into the usage AI model",
    "Multi-pathway pricing should be separate BTs if priced separately",
    "Usage AI must be turned on for most contracts",
    "Prepaid or free usage requires 'Has Threshold' model configuration",
    "Minimum usage requirements trigger 'Has Minimum' model configuration",
    "For prepaid usage BTs, select only the prepaid usage BT (not overage BT) when configuring included products",
    "For free usage with specific event types, only select those specific usage products that apply"
  ],
  "exceptions": [
    "Dedicated Infrastructure is old terminology and should be rare",
    "Support should only be categorized separately if it's its own line item",
    "If customers received only specific free usage types (e.g., only call minutes), select only those products even if other usage events exist",
    "During threshold periods (e.g., first year with free minutes), ensure customers are not charged for prepaid or free usage",
    "Usage overage charges only apply after prepaid/free amounts are exhausted"
  ],
  "merchant_specific": [
    "Revenue categories: Pilot, Professional Services, Support, Platform, Dedicated Infrastructure, Usage Based Commit",
    "Service types: Implementation, Enterprise services, Forward deployed engineer, Pathway development support",
    "Usage event types: Connected minutes, Chat messages, SMS messages, Call minutes",
    "Merchant name: Bland (referenced in examples)",
    "Pricing structure: Multi-pathway pricing and pathway bundles",
    "Usage rate example: $0.06 per minute for overages",
    "Free usage example: 15 million free minutes of call time",
    "Terminology: 'BT' (Billing Term), 'Usage AI', pathway-related services"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: MIS_ Bland_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:33

### Original Content
```
Merchant Name: Bland Implementation POC: (IM to fill) CX POC: [IMP to Add] SOW: https: docs google com document d 18PdAa6BJymkO0rPai6gLCPdOnca_fokMXs7kcAAsCSw edit tab t 0 Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Liv...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing and pricing structure configuration",
    "Pilot period handling and subscription lifecycle management",
    "Service and billing date determination rules",
    "Usage-based billing and AI feature enablement",
    "Revenue categorization and billing frequency alignment"
  ],
  "rules": [
    {
      "rule": "Usage AI must be turned on for 'Free Call Minutes' or 'Committed Usage' items",
      "category": "Feature Configuration"
    },
    {
      "rule": "Item names should primarily use the 'Units' column, with best judgment applied when unclear",
      "category": "Data Mapping"
    },
    {
      "rule": "Pilot periods are separate billing terms (BTs) that are in addition to the full subscription length",
      "category": "Pilot Management"
    },
    {
      "rule": "Pilot period products must use revenue category 'Pilot'",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Total price must consider billing frequency (e.g., annual price billed quarterly = total price / 4)",
      "category": "Pricing Calculation"
    },
    {
      "rule": "Service Start Date should use the date stated in the order form",
      "category": "Date Configuration"
    },
    {
      "rule": "When multiple start dates exist for different BTs, use the billing start date as the service date",
      "category": "Date Configuration"
    },
    {
      "rule": "Month of Service should reflect the duration the product covers (e.g., months 2-3 = 2 months)",
      "category": "Duration Calculation"
    },
    {
      "rule": "Billing Start Date should use the service start date and acknowledge different BT start dates",
      "category": "Date Configuration"
    },
    {
      "rule": "Billing frequency should be determined from contract language or billing terms",
      "category": "Frequency Configuration"
    },
    {
      "rule": "If monthly pricing is listed and invoiced monthly, set frequency to Monthly",
      "category": "Frequency Configuration"
    }
  ],
  "exceptions": [
    {
      "exception": "When a pilot period exists, it creates a separate BT before the main subscription begins",
      "condition": "Contract includes pilot period",
      "example": "1 month pilot + 1 year subscription = 2 separate BTs"
    },
    {
      "exception": "Multiple BTs with different start dates require using the billing start date as the service date",
      "condition": "Multiple pricing tiers with different start dates (e.g., month 1 price vs months 2-3 price)"
    },
    {
      "exception": "Lump sum payments covering multiple months require special frequency handling",
      "condition": "Single payment covers multiple billing periods",
      "note": "Document appears truncated at this point"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Bland Implementation",
      "type": "Identifier",
      "customization_needed": true
    },
    {
      "element": "POC (Point of Contact) information - IM and CX POC fields",
      "type": "Contact Information",
      "customization_needed": true
    },
    {
      "element": "SOW (Statement of Work) document link",
      "type": "Documentation Reference",
      "customization_needed": true
    },
    {
      "element": "Billing model section - unique customer creation process",
      "type": "Process Customization",
      "customization_needed": true,
      "note": "Requires Implementation team to fill"
    },
    {
      "element": "Contract Processing Steps",
      "type": "Workflow",
      "customization_needed": true,
      "note": "Requires Implementation Success team to fill post-go-live"
    },
    {
      "element": "Usage AI configuration for specific features",
      "type": "Feature Toggle",
      "customization_needed": true,
      "note": "Merchant-specific features like 'Free Call Minutes' or 'Committed Usage'"
    }
  ],
  "confidence_score": 0.75,
  "confidence_notes": "Document appears to be a template with incomplete sections and truncated content at the end. Several sections are marked as 'to fill' by implementation teams. The rules extracted are clear where content exists, but the incomplete nature of the document suggests there may be additional important information not captured. Confidence reduced due to: (1) incomplete sections, (2) truncated ending, (3) template nature with placeholder text."
}
```

---

## Chunk 3: MIS_ Bland_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:42

### Original Content
```
If it s prepaid usage for ALL usage, select all of the products Threshold period: This depends on what range the prepaid or free minutes goes for If monthly, use  individual billing period  (Example) If annual, use  full service period  (Example) Threshold amount The total prepaid or free amount for that period (the monthly amount if it s for the individual billing period Select  charges overages  Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Prepaid and Free Usage Configuration",
    "Billing Period and Threshold Management",
    "Integration Item Labeling and Processing",
    "Post-Processing Communication Workflows",
    "Customer-Specific Invoice Handling"
  ],
  "rules": [
    {
      "rule": "For prepaid usage covering ALL usage, select all products",
      "category": "Product Selection"
    },
    {
      "rule": "Monthly prepaid/free minutes should use 'individual billing period' as threshold period",
      "category": "Billing Configuration"
    },
    {
      "rule": "Annual prepaid/free minutes should use 'full service period' as threshold period",
      "category": "Billing Configuration"
    },
    {
      "rule": "Threshold amount should equal the total prepaid or free amount for the specified period",
      "category": "Billing Configuration"
    },
    {
      "rule": "Select 'charges overages' for prepaid usage configurations",
      "category": "Overage Handling"
    },
    {
      "rule": "Events Processing section to be filled by Implementation Success team post-go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Integration Items Processing section to be filled by Implementation Success team post-go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Post Processing Communications section to be filled by Implementation Success team post-go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Customer Information section to be filled by Implementation Success team post-go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Implementation team fills Feature Requests prior to go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Success team fills Feature Requests post-go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "AE fills Merchant Calls section for all videos prior to Implementation involvement",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Implementation team fills Merchant Calls section prior to go-live",
      "category": "Responsibility Assignment"
    },
    {
      "rule": "Success team fills Merchant Calls section post-go-live",
      "category": "Responsibility Assignment"
    }
  ],
  "exceptions": [
    {
      "exception": "Statsig integration items should be labeled as 'Sales' (merchant-specific rule)",
      "condition": "When processing Statsig integrations"
    },
    {
      "exception": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "condition": "When processing Pinata integrations, with merchant override possible"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to specific merchant-customer relationships",
      "condition": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "description": "Different merchants (Statsig, Pinata) have specific labeling requirements",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Who needs to be notified, where, and when varies by merchant (example: Messari internal channel)",
      "customizable": true
    },
    {
      "element": "Customer-specific invoice requirements",
      "description": "Special memos and invoice changes based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Threshold period selection",
      "description": "Depends on merchant's prepaid/free minute structure (monthly vs annual)",
      "customizable": true
    },
    {
      "element": "Events billing information",
      "description": "Important information specific to each merchant's events billing needs",
      "customizable": true
    },
    {
      "element": "Feature requests tracking",
      "description": "Merchant-specific feature requests with urgency and importance ratings",
      "customizable": true
    },
    {
      "element": "Merchant call recordings",
      "description": "Links to discovery, demo, and technical scoping calls specific to each merchant",
      "customizable": true
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 4: MIS_ Bland_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:42

### Original Content
```
id 9037405092022941974 Next Steps (6 20) - https: us-56595 app gong io call id 4924670863912071994 ROI and Pricing (6 24) - https: us-56595 app gong io call id 6487012684246113336 Q2 Commercial Alignment (6 30) - https: us-56595 app gong io call id 3020078879149461689 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Pricing models can include flat fee, unit price, tiered flat, and tiered unit Tabs can support commit consumption w...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting Documentation and Reference Links",
    "Pricing and Billing Models",
    "Merchant Onboarding and Handoff Process",
    "Account Management Workflow",
    "Consumption-Based Pricing Structures"
  ],
  "rules": [
    "AE (Account Executive) is responsible for filling in notes sections if available",
    "Implementation team serves as the completion DRI (Directly Responsible Individual) on handoff",
    "Documentation must include information on how the merchant bills",
    "Pricing models must be specified and can include: flat fee, unit price, tiered flat, and tiered unit",
    "Tabs system must support commit consumption with true-up or bill for overages",
    "Merchant temperament assessment is required as part of the documentation process"
  ],
  "exceptions": [
    "Notes sections are conditional - only filled by AE 'if they have' information available",
    "Pricing can follow multiple models depending on merchant needs (flat fee, unit price, tiered structures)",
    "Billing for overages can be handled through either true-up or direct billing methods"
  ],
  "merchant_specific": [
    "Merchant temperament - requires individual assessment per merchant",
    "How the specific merchant bills - varies by merchant",
    "Pricing model selection - customized based on merchant requirements (flat fee vs unit price vs tiered options)",
    "Commit consumption structure - whether true-up or overage billing is used",
    "Meeting references appear to be specific to particular merchant engagements (ROI and Pricing, Commercial Alignment calls)"
  ],
  "confidence_score": 0.72
}
```

---

## Chunk 5: MIS_ Bland_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:55

### Original Content
```
Turner (Head of Ops   Finance, Champion) is young and smart Worked at Jeffries for 4 years and moved to Bland a year ago Mostly focused on efficiency in operations and will be the main POC at Bland Side Note - he went to elementary school with my gf and lives 2 blocks from the office Dan (Fractional CFO, Influencer) is going to be the main user Already using Tabs with  arcee-ai Has a partnership with our partnerships team Tabs Champion Somina (Fractional Controller, Influencer) cares about reven...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder roles and influence mapping",
    "Product feature alignment with user needs",
    "Operational efficiency and automation",
    "Financial process integration and consolidation",
    "Partnership-driven adoption strategy"
  ],
  "rules": [
    "Turner (Head of Ops & Finance) serves as main point of contact and champion",
    "Dan (Fractional CFO) is identified as the main user and existing Tabs user with arcee-ai",
    "Somina (Fractional Controller) focuses on revenue and MEC (Monthly Expense Calculation)",
    "Tabs must automate collections, cash application, and payment infrastructure integration",
    "Tabs must consolidate data from multiple sources: Stripe, HubSpot, QuickBooks, and internal databases",
    "Tabs must use AI to ingest contracts and apply pricing logic for usage-based invoicing",
    "Tabs must sync journal entries, deferred revenue, and AR reporting directly to QuickBooks",
    "Solution must support both enterprise and self-serve customer billing models",
    "Implementation should leverage existing partnerships team relationships"
  ],
  "exceptions": [
    "Dan already has experience with Tabs through arcee-ai implementation (existing user, not net new)",
    "Both Dan and Somina are champions through partnerships team (non-standard acquisition path)",
    "Somina works at EXBO but is influencer for this account (external stakeholder involvement)",
    "Current state is fully manual for Somina's processes (requires migration from zero automation)"
  ],
  "merchant_specific": [
    "Company name: Bland",
    "Specific stakeholder names and personal connections (Turner's elementary school connection)",
    "Integration requirements specific to their tech stack: Stripe, HubSpot, QuickBooks",
    "Dual customer model: enterprise and self-serve customers",
    "Organizational structure: uses fractional CFO and Controller rather than full-time",
    "Geographic proximity: stakeholder lives 2 blocks from office",
    "Partnership relationships: existing connections with arcee-ai and partnerships team",
    "Current manual processes specific to Somina's workflow at EXBO"
  ],
  "confidence_score": 0.85
}
```

---

