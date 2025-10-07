# Raw LLM Analysis: Ash MIS

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 10:45:43

---

## Chunk 1: Ash MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:43

### Original Content
```
Merchant Name (AE to fill) : Ash Wellness Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Contract Types: These include MSAs and SOWs; only SOWs carry comm...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Structure and Types",
    "Billing Configuration and Timing",
    "Renewal and Term Management",
    "Usage-based vs Flat-fee Billing Models",
    "Default Values and Fallback Rules"
  ],
  "rules": [
    {
      "rule": "All contracts have a 12-month term",
      "category": "contract_term",
      "specificity": "explicit"
    },
    {
      "rule": "Only SOWs carry commercial terms used for BTs (Billing Terms), not MSAs",
      "category": "contract_types",
      "specificity": "explicit"
    },
    {
      "rule": "Each SOW must be treated as a separate contract when multiple SOWs exist per customer",
      "category": "contract_management",
      "specificity": "explicit"
    },
    {
      "rule": "For renewal contracts, use the exact same event types as the original contract",
      "category": "renewals",
      "specificity": "explicit"
    },
    {
      "rule": "Flat-fee BTs: billing start date uses the effective date",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Usage-based BTs: billing start date assumes effective date + 90 days as placeholder for launch date",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Service start date must match billing start date",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Months of service defaults to 12 months unless otherwise specified",
      "category": "service_duration",
      "specificity": "explicit"
    },
    {
      "rule": "Flat-fee BTs: frequency follows the cadence indicated in SOW or contract (monthly, quarterly, etc.)",
      "category": "billing_frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Usage-based BTs: set frequency to weekly, regardless of invoice cycle",
      "category": "billing_frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Billing term setup should reflect actual accrual or aggregation cadence, not invoice cycle",
      "category": "billing_frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Net terms: use terms provided in contract (typically Net 15 or Net 30)",
      "category": "payment_terms",
      "specificity": "explicit"
    },
    {
      "rule": "Net terms: default to Net 30 if unstated",
      "category": "payment_terms",
      "specificity": "explicit"
    },
    {
      "rule": "Quantity: use stated quantity in BT; if none listed, default to 1",
      "category": "billing_quantity",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Usage-based billing frequency set to weekly even when invoice cycle is monthly",
      "context": "This reflects the aggregation cadence rather than invoicing cadence, as seen in Noom contract example",
      "importance": "high",
      "marked_as_watchout": true
    },
    {
      "exception": "Renewal contracts require opening the original contract to match event types exactly",
      "context": "Special handling required for renewals to maintain consistency",
      "importance": "high"
    },
    {
      "exception": "90-day placeholder for usage-based billing start dates is temporary and will be updated by merchant",
      "context": "Effective date + 90 days is not final; merchant provides actual launch date later",
      "importance": "medium"
    },
    {
      "exception": "Months of service can differ from default 12 months if explicitly specified in contract",
      "context": "Default rule has override condition",
      "importance": "medium"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "note": "Specified as 'Ash Wellness' but template indicates this is merchant-specific",
      "customization_required": true
    },
    {
      "element": "Implementation POC",
      "note": "To be filled by Implementation Manager (IM)",
      "customization_required": true
    },
    {
      "element": "CX POC",
      "note": "To be added by Implementation team",
      "customization_required": true
    },
    {
      "element": "Billing model section",
      "note": "Entire section to be filled by Implementation team with merchant-specific details",
      "customization_required": true
    },
    {
      "element": "Customer creation process",
      "note": "May have unique aspects per merchant",
      "customization_required": true
    },
    {
      "element": "How merchant bills",
      "note": "Merchant-specific billing methodology",
      "customization_required": true
    },
    {
      "element": "Contract structure",
      "note": "How contract is broken up may vary by merchant",
      "customization_required": true
    },
    {
      "element": "One-off merchant considerations",
      "note": "Unique things to know about each merchant",
      "customization_required": true
    },
    {
      "element": "Frequency cadence for flat-fee BTs",
      "note": "Follows merchant's SOW specifications (monthly, quarterly, etc.)",
      "customization_required": true
    },
    {
      "element": "Actual launch date for usage-based billing",
      "note": "Merchant provides this to replace 90-day placeholder",
      "customization_required": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Ash MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:45

### Original Content
```
Waived Fees: Capture as a  0 BT with clear labeling to reflect that the item was waived Usage AI (for contracts with a deposit) Select has threshold Title it  Deposit  Integration item: TABS_Deposit For the products, select all of the usage products that apply to the deposit  The Deposit is only to be used for Kits -  this would apply to all Kit usage products Threshold period is full service term Amount is the deposit Select  charges overages  Events instructions for renewals When we process a ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Fee and Billing Transaction (BT) Processing",
    "Contract Renewal Event Handling",
    "Usage-Based Billing and Deposit Management",
    "Integration Item Configuration and Labeling",
    "Post-Processing Communication Workflows"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Fee Processing",
      "description": "Waived fees must be captured as $0 BT with clear labeling to reflect the item was waived"
    },
    {
      "rule_id": "R2",
      "category": "Deposit Configuration",
      "description": "For contracts with deposits, use Usage AI with 'has threshold' selected, titled 'Deposit', with integration item TABS_Deposit"
    },
    {
      "rule_id": "R3",
      "category": "Deposit Scope",
      "description": "Deposits are only to be used for Kits and apply to all Kit usage products"
    },
    {
      "rule_id": "R4",
      "category": "Deposit Settings",
      "description": "Deposit threshold period is full service term, amount is the deposit value, and 'charges overages' must be selected"
    },
    {
      "rule_id": "R5",
      "category": "Renewal Processing",
      "description": "When processing renewal contracts, find the old contract and use the exact same event types that the merchant selected for specific BTs"
    },
    {
      "rule_id": "R6",
      "category": "Event Types",
      "description": "Renewal contracts must use merchant-created unique events (often beginning with customer's name) rather than general events"
    },
    {
      "rule_id": "R7",
      "category": "Zero Value Processing",
      "description": "Process zero or waived BTs as $0 BTs"
    },
    {
      "rule_id": "R8",
      "category": "Integration Items",
      "description": "Implementation Success team fills integration item processing instructions post-go-live"
    },
    {
      "rule_id": "R9",
      "category": "Post-Processing",
      "description": "Implementation Success defines who needs to be notified upon completion of processing batches and when"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Usage Invoicing Detail for Noom: Despite weekly invoice generation, frequency must be set to weekly for usage even though customers pay monthly",
      "condition": "When language indicates invoices sent at one frequency but payment expected at another"
    },
    {
      "exception_id": "E2",
      "description": "Watch for language like 'Once the Deposit has been exhausted' which indicates aggregated weekly amounts invoiced but paid monthly",
      "condition": "Complex invoicing schedules with aggregation periods"
    },
    {
      "exception_id": "E3",
      "description": "Statsig integration items should be labeled as 'Sales'",
      "condition": "Merchant-specific: Statsig"
    },
    {
      "exception_id": "E4",
      "description": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "condition": "Merchant-specific: Pinata"
    },
    {
      "exception_id": "E5",
      "description": "Special memos or invoice changes required for certain customers due to merchant-customer relationship",
      "condition": "Customer-specific requirements documented in Customer Information section"
    }
  ],
  "merchant_specific": [
    {
      "element": "Event Types for Renewals",
      "description": "Merchants create unique event types with specific formats (often beginning with customer name) that must be replicated in renewal contracts",
      "customization_required": true
    },
    {
      "element": "Integration Item Labels",
      "description": "Different merchants require different integration item labeling conventions (e.g., Statsig='Sales', Pinata='Software Subscription Bundle')",
      "customization_required": true
    },
    {
      "element": "Usage Invoicing Frequency",
      "description": "Merchants like Noom have unique invoicing language requiring careful interpretation of frequency vs payment terms",
      "customization_required": true
    },
    {
      "element": "Post-Processing Notifications",
      "description": "Notification requirements vary by merchant (who, where, when) - example: Messari requires Customer Success notification in internal channel",
      "customization_required": true
    },
    {
      "element": "Customer Information",
      "description": "Merchant-specific customer details including special memos, invoice requirements, and relationship considerations",
      "customization_required": true
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific requests like API usage ingestion, HubSpot integration, and unique customer identifiers for healthcare providers",
      "customization_required": true
    },
    {
      "element": "Internal Tools and Naming Conventions",
      "description": "Merchants may have internal tools for usage tracking and unique customer identifier conventions",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Ash MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:55

### Original Content
```
Sending 30 invoices a week from QBO currently 1) What is the merchant temperament Kyle is Co-Founder and Head of Product A very process oriented thinker Very nice and comes from start up world Will be main user until finance hire onboards Executive Sponsor as well 3) What are the Tabs features that the key POC cares about Usage AI for invoicing Automated collections to track overdue invoices and recent history Cash forecasting for potential to raise a round in the near future Revenue Reporting i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "User Profile and Stakeholder Management",
    "Invoice and Collections Automation",
    "Financial Planning and Cash Flow Management",
    "Healthcare Industry Compliance and Contract Management",
    "Product Feature Prioritization"
  ],
  "rules": [
    "Merchant sends 30 invoices per week from QuickBooks Online (QBO)",
    "Kyle (Co-Founder/Head of Product) will be the main user until finance hire is onboarded",
    "Kyle serves as both primary user and Executive Sponsor",
    "AI-powered invoicing must be implemented for usage tracking",
    "Automated collections system required to track overdue invoices and payment history",
    "Cash forecasting capability is required for fundraising preparation",
    "Real-time revenue reporting must be enabled",
    "Contract management system must handle healthcare-specific contract redlines and terms",
    "System must accommodate process-oriented user workflows"
  ],
  "exceptions": [
    "Main user role will transition from Kyle to a future finance hire (temporary user assignment)",
    "Healthcare industry requires special contract management due to extensive redlines on terms (industry-specific exception)",
    "Cash forecasting is specifically tied to near-future fundraising needs (time-sensitive requirement)"
  ],
  "merchant_specific": [
    "Current invoice volume: 30 per week",
    "Current system: QuickBooks Online (QBO)",
    "Industry: Healthcare (requires specialized contract handling)",
    "Company stage: Startup preparing for fundraising round",
    "Key contact: Kyle (Co-Founder and Head of Product)",
    "User temperament: Process-oriented, startup background, collaborative",
    "Organizational structure: Pre-finance hire stage",
    "Feature priority order: Usage AI, Automated Collections, Cash Forecasting, Revenue Reporting, Contract Management"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: Ash MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:55

### Original Content
```
io call id 857518101207101844 Demo AR Heroes 4 21 https: us-56595 app gong io call id 3818003395387187227 Custom Demo 4 23 (Contracts and Usage) https: us-56595 app gong io call id 2837336306888445382 Implementation and Commercials 4 23 https: us-56595 app gong io call id 4300720398853812596 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Flat SaaS Subscription Fee, Sometimes Implementation professional services, Usage for PxQ T...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Call/Meeting Documentation and Reference Links",
    "Billing and Revenue Models",
    "Implementation and Handoff Processes",
    "Pricing Structure and Tiers",
    "Invoicing Schedule and Timing"
  ],
  "rules": [
    "AE (Account Executive) must fill Notes Sections if information is available",
    "Implementation team serves as DRI (Directly Responsible Individual) for completion on handoff",
    "Invoicing occurs on Tuesdays",
    "Billing follows a Flat SaaS Subscription Fee model",
    "Usage billing is based on PxQ (Price x Quantity) formula",
    "Pricing tiers are determined by phases a Kit can fall into",
    "Week-based invoicing cycle is standard"
  ],
  "exceptions": [
    "Implementation professional services fees are charged 'Sometimes' (not always applicable)",
    "Billing model may vary: can include subscription only, or subscription plus usage, or subscription plus professional services"
  ],
  "merchant_specific": [
    "Specific Gong.io call IDs and URLs (us-56595.app.gong.io domain)",
    "Definition of 'Kit' and associated phases (merchant-specific terminology)",
    "PxQ tier structure and phase definitions",
    "Specific day of week for invoicing (Tuesday) may vary by merchant",
    "Professional services implementation fees (presence and amount)",
    "Usage-based pricing components and calculation methods"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for Confidence Score (0.65):**
- The document chunk appears fragmented with incomplete sentences and unclear context
- Some terminology (e.g., "Kit," "Phases") lacks clear definition
- The structure suggests this is an excerpt from a larger document, making full context difficult to assess
- Clear elements are identifiable (billing models, invoicing day, roles), but relationships between concepts are ambiguous
- Multiple URL references suggest this is documentation metadata rather than complete instructional content

---

