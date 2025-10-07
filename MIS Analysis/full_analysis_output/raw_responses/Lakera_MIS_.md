# Raw LLM Analysis: Lakera MIS_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:53:59

---

## Chunk 1: Lakera MIS__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:59

### Original Content
```
Merchant Name: Lakera Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Locate billing items Identify billing items based on the structure and conte...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Item Extraction",
    "Default Values and Fallback Rules",
    "Merchant-Specific Customization and Configuration",
    "Integration Item Classification and Labeling",
    "Post-Processing Communication and Notification Workflows"
  ],
  "rules": [
    {
      "category": "Service Duration",
      "rule": "Calculate inclusive full months between Order Start Date and Order End Date",
      "default": "Default to 12 months if nothing is stated (most contracts are annual)"
    },
    {
      "category": "Billing Start Date",
      "rule": "Use service start date unless otherwise specified by a different invoicing trigger (e.g., upon signature)"
    },
    {
      "category": "Billing Frequency",
      "rule": "Determine from invoicing terms in Order Form",
      "default": "If unstated: Fixed subscriptions = Annual upfront; One-time milestone fees = None",
      "ops_default": "Monthly (if none listed)"
    },
    {
      "category": "Net Payment Terms",
      "rule": "Extract from Payment Terms in Order Form",
      "default": "Default to Net 30 if not specified",
      "ops_default": "Net 0 (if none listed)"
    },
    {
      "category": "Quantity",
      "rule": "For fixed fees: use 1 unless otherwise specified",
      "note": "If volume caps are listed (e.g., API request limit), record the threshold for reference only"
    },
    {
      "category": "Amount Calculation",
      "rule": "Use the total contract amount",
      "conditional": "If invoiced periodically, divide evenly across periods"
    },
    {
      "category": "Discounts",
      "rule": "Add discounts in-line and not as a separate product"
    },
    {
      "category": "Service Term Default",
      "rule": "Ops Default is 1 Year if none listed"
    },
    {
      "category": "Tax Line Items",
      "rule": "Every tax line item becomes a BT (Billing Transaction) Events",
      "default": "Applied if none listed"
    },
    {
      "category": "Data Sources",
      "rule": "Item Name: Use the item name as listed in the Order Form",
      "rule2": "Service Start Date: Use the effective date or order start date from the contract"
    }
  ],
  "exceptions": [
    {
      "case": "Invoicing Trigger Override",
      "description": "Billing Start Date can differ from Service Start Date if a different invoicing trigger is specified (e.g., upon signature)"
    },
    {
      "case": "Periodic Invoicing",
      "description": "When amount is invoiced periodically, divide total contract amount evenly across periods instead of using full amount"
    },
    {
      "case": "Volume Caps",
      "description": "Volume caps (e.g., API request limits) are recorded for reference only and do not affect quantity calculation"
    },
    {
      "case": "Merchant-Specific Processing",
      "description": "Specific processing requirements may differ by contract (e.g., always back-date invoice date to final day of the month)"
    },
    {
      "case": "Contract Items to Ignore",
      "description": "Certain items in contracts may need to be ignored based on merchant-specific instructions"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant POC Information",
      "description": "Implementation POC and CX POC fields to be filled per merchant",
      "customizable": true
    },
    {
      "element": "Billing Model",
      "description": "Unique customer creation process, billing methodology, and contract structure vary by merchant",
      "customizable": true
    },
    {
      "element": "Integration Item Labeling",
      "description": "Specific instructions for assigning integration items (e.g., Statsig items labeled as 'Sales', Pinata items as 'Software Subscription Bundle')",
      "customizable": true,
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Contract Processing Variations",
      "description": "Merchant-requested processing specifics that may differ by contract (e.g., invoice date back-dating rules)",
      "customizable": true
    },
    {
      "element": "Post-Processing Notifications",
      "description": "Notification requirements vary by merchant - who needs to be notified and when after batch processing completion",
      "customizable": true
    },
    {
      "element": "Events Billing",
      "description": "Important information on events billing varies by merchant and may not be necessary for all",
      "customizable": true
    },
    {
      "element": "Items to Ignore",
      "description": "Specific contract items to ignore are merchant-dependent",
      "customizable": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Lakera MIS__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:54:01

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp handoff, Imp to fill prior to go-live...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder notification and communication protocols",
    "Merchant lifecycle phase management (Active phase focus)",
    "Cross-functional handoff procedures (AE to Implementation to Customer Success)",
    "Customer-specific documentation and special requirements",
    "Feature request tracking and prioritization"
  ],
  "rules": [
    {
      "rule": "Customer Success representative (Azmat Aziz) must be notified when contracts are processed during Active merchant phase",
      "context": "Notification requirement",
      "explicitness": "explicit"
    },
    {
      "rule": "Notifications should be sent to Messari internal merchant channel",
      "context": "Communication channel requirement",
      "explicitness": "explicit"
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success team Post-Go Live",
      "context": "Documentation responsibility",
      "explicitness": "explicit"
    },
    {
      "rule": "AE (Account Executive) must fill Feature Requests prior to Implementation handoff",
      "context": "Pre-implementation phase responsibility",
      "explicitness": "explicit"
    },
    {
      "rule": "Implementation team must fill Feature Requests prior to go-live",
      "context": "Implementation phase responsibility",
      "explicitness": "explicit"
    },
    {
      "rule": "Customer Success must fill Feature Requests Post-Go Live",
      "context": "Post-launch phase responsibility",
      "explicitness": "explicit"
    },
    {
      "rule": "AE must document all merchant call videos prior to Implementation involvement",
      "context": "Pre-implementation documentation",
      "explicitness": "explicit"
    },
    {
      "rule": "Implementation team must document merchant calls prior to go-live",
      "context": "Implementation phase documentation",
      "explicitness": "explicit"
    },
    {
      "rule": "Customer Success must document merchant calls Post-Go Live",
      "context": "Post-launch documentation",
      "explicitness": "explicit"
    },
    {
      "rule": "Feature requests must include: description (What is it), justification (Why it's important), and Urgency level",
      "context": "Feature request documentation standard",
      "explicitness": "explicit"
    },
    {
      "rule": "Merchant calls should be categorized by type: Intro, Demo, and ROI call",
      "context": "Call documentation taxonomy",
      "explicitness": "explicit"
    },
    {
      "rule": "Call recordings should be stored in Gong platform with proper linking",
      "context": "Call recording management",
      "explicitness": "implicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Special memos required for certain invoices",
      "condition": "Based on merchant-customer relationship specifics",
      "impact": "Invoice processing modifications"
    },
    {
      "exception": "Invoice changes may be required",
      "condition": "Due to merchant customer relationship dynamics",
      "impact": "Standard invoice processing may need adjustment"
    },
    {
      "exception": "Customer-specific important information",
      "condition": "Varies by merchant's specific customers",
      "impact": "Requires customized handling per merchant"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient (Azmat Aziz)",
      "customization_needed": "Customer Success contact person varies by merchant or account"
    },
    {
      "element": "Internal merchant channel",
      "customization_needed": "Each merchant may have dedicated communication channel"
    },
    {
      "element": "Customer-specific information section",
      "customization_needed": "Entirely dependent on merchant's customer base and requirements"
    },
    {
      "element": "Special memo requirements for invoices",
      "customization_needed": "Varies based on individual merchant-customer relationships"
    },
    {
      "element": "Feature requests",
      "customization_needed": "Unique to each merchant's needs and use cases"
    },
    {
      "element": "Gong call recordings and links",
      "customization_needed": "Unique URLs and call IDs per merchant engagement"
    },
    {
      "element": "Merchant phase (Active)",
      "customization_needed": "Phase status varies by merchant lifecycle position"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Rationale**: The document structure is clear and provides explicit role-based responsibilities and phase-based workflows. However, the content appears to be a template or example with some formatting issues (missing slashes in URLs, fragmented sentences), which reduces confidence slightly. The core rules and handoff procedures are well-defined, but some contextual details about the broader process are missing.

---

## Chunk 3: Lakera MIS__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:54:11

### Original Content
```
id 5532650537271318207 account-id 4510569308154570916 Sync with sales ops https: us-56595 app gong io call id 3279173550303081490 account-id 4510569308154570916 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Very Bespoke, high ACV ( 100k) contracts  10 customers 1 invoice month Today: Usage commit Services -  red team  upfront, or after completion (milestone) Implementation Future state: usage All contracts are in english and b...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Bespoke high-value contract structure with usage-based billing transition",
    "Product offerings spanning SaaS and self-hosted AI security solutions",
    "Professional services including implementation, red teaming, and additional support",
    "Billing complexity management with auto-generated invoices for scaling",
    "Merchant relationship management and stakeholder preferences"
  ],
  "rules": [
    "All contracts must be in English",
    "All billing must be processed out of the US",
    "High ACV contracts require minimum $100k value",
    "Current billing model: Usage commit + Services (red team upfront or milestone-based)",
    "Invoice frequency: 1 invoice per month per customer (approximately 10 customers)",
    "Future state requirement: All contracts transition to usage-based billing",
    "Implementation team serves as DRI (Directly Responsible Individual) on handoff completion",
    "AE must fill notes sections if available before handoff"
  ],
  "exceptions": [
    "Services billing can be either upfront OR after completion based on milestones (flexible timing)",
    "Red team services specifically can be billed upfront or post-completion",
    "High bespoke nature suggests custom contract terms per deal rather than standardized agreements"
  ],
  "merchant_specific": [
    "Merchant name: Aloys (contact/company reference)",
    "Merchant temperament: 'really easy to work with and super straightforward'",
    "Key POC priorities: (1) Auto-generated invoices for scaling, (2) Flexibility for future usage-based billing",
    "Product catalog specific to Lakera: Guard (SaaS/Self-hosted variants), Implementation Package, Red Teaming services",
    "NetSuite integration items referenced for product mapping",
    "Customer base size: approximately 10 customers",
    "Gong call reference for context: call id 3279173550303081490"
  ],
  "confidence_score": 0.82
}
```

---

