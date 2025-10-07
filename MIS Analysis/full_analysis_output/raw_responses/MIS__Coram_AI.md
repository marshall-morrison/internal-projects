# Raw LLM Analysis: MIS_ Coram AI

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:00:45

---

## Chunk 1: MIS_ Coram AI_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:00:45

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp han...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Customer and Invoice Management",
    "Revenue Recognition and Billing Models",
    "Merchant Relationship and Temperament",
    "Feature Requests and Implementation Tracking"
  ],
  "rules": [
    "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
    "Implementation Success team is responsible for filling Customer Information section post-go-live",
    "Account Executive (AE) must fill feature requests prior to Implementation handoff",
    "Implementation team must fill feature requests prior to go-live",
    "Success team must fill feature requests post-go-live",
    "AE must fill merchant call videos prior to Implementation involvement",
    "Implementation team must be completion DRI (Directly Responsible Individual) on handoff notes",
    "Contracts are billed upfront for full term value (5-10 year contracts)",
    "Hardware is billed separately based on type and quantity of devices",
    "Pricing is tied to number of active camera feeds defined at contract start"
  ],
  "exceptions": [
    "Special memos required for certain invoices due to merchant-customer relationship specifics",
    "SSP (Software Sales Performance) allocation applies specifically to hardware bundles and free trials",
    "Hardware-software model implementation is medium to high priority with planned Tabs usage in January 2026",
    "Merchant uses upfront invoicing for 5-10 year contracts (non-standard long-term billing)",
    "Usage-based pricing does not apply - quantities are pre-defined in contract"
  ],
  "merchant_specific": [
    "Merchant name: Coram (implied from context)",
    "Key contact: Alex (merchant temperament contact, former Head of Finance at Saltmine)",
    "Alex serves as accounting advisor and is a repeat customer (second purchase)",
    "Business model: Camera feeds software with hardware sales (cameras, devices)",
    "Contract structure: 5-10 year upfront billing cycles",
    "Pricing model: Based on number of active camera feeds, not usage-based",
    "Merchant relationship: Described as 'Tabs friendly' and 'invested in our success'",
    "Internal channel: Messari internal merchant channel for notifications",
    "Specific call reference: Disco Demo Negotiation (7/21) with Gong call ID"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document is somewhat fragmented with incomplete sentences and formatting issues, making some interpretations uncertain
- Clear rules around notification protocols and billing models are evident
- Merchant-specific details (Coram, Alex, camera feeds) are identifiable but context is limited
- Some sections appear to have missing information (e.g., "Success to fill to fill Post-Go Live" suggests duplication/error)
- The overall structure and key themes are discernible despite formatting challenges

---

## Chunk 2: MIS_ Coram AI_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:00:49

### Original Content
```
Merchant Name: Coram AI Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Process all docs that come through, including those marked as  internal use  Ignore...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Data Extraction",
    "Product Categorization (Hardware vs Software)",
    "Billing Configuration and Timing",
    "Address and Contact Management",
    "Integration and Mapping Requirements"
  ],
  "rules": [
    "Process all documents including those marked as 'internal use'",
    "Ignore tax items, do not process at BT (Billing Terms)",
    "Extract billing terms address from contract",
    "Use shipping address from contract if available, otherwise use billing address",
    "Use account payable name/email from contact as billing contact if stated, otherwise keep HubSpot value from Tabs",
    "Only software fees will auto-renew, hardware does not",
    "Software products always contain 'License' in the name",
    "Hardware products are identified in SKUs noted in summary section",
    "If no summary exists, identify software by 'license' in item name",
    "Hardware Products: Service start date = contract date (last signature date)",
    "Hardware Products: Total months of service = 0",
    "Hardware Products: Item Name = value from 'Item/Description' column",
    "Hardware Products: Item Description = value from 'Quantity' column",
    "Hardware Products: Billing Type = flat type",
    "Hardware Products: Total price = gross price (back into it from Total column if shown net of discount)",
    "Hardware Products: Add discount in-line using percentage discount noted",
    "Hardware Products: Quantity = value from 'Quantity' column",
    "Hardware Products: Billing start date = same as service start date",
    "Hardware Products: Periods = 0",
    "Hardware Products: Frequency = None",
    "Hardware Products: Billing Timing = bill first of period",
    "Hardware Products: Net terms default to 0 unless otherwise specified",
    "Software Products: Service start date = date of Licensing Term start",
    "Software Products: Total months of service = months in total subscription years (e.g., 60 months for 5 years)",
    "Software Products: Item Name = value from 'Item/Description' column",
    "Software Products: Item Description = value from 'Quantity' column",
    "Software Products: Billing Type = flat type",
    "Software Products: Total price = gross price divided by payment cadence",
    "Software Products: Add discount in-line using percentage discount noted",
    "Software Products: Quantity = value from 'Quantity' column",
    "Software Products: Billing start date = first payment date from billing cadence section",
    "Software Products: Periods = based on billing cadence (quarterly=4, annual=1)",
    "Software Products: Frequency = based on billing cadence logic (quarterly=every 3 months, annual=12 months/1 year)",
    "Software Products: Billing Timing = bill first of period",
    "Integration Item: Lookup product name and select corresponding QBO Integration Item",
    "Default ops behavior: every tax line item becomes a BT if none listed"
  ],
  "exceptions": [
    "Auto renewals only apply to software fees, not hardware (12 months of service starting after initial term)",
    "If no summary exists in contract, use fallback logic of identifying software by 'license' in item name",
    "Net terms default to 0 unless otherwise specified",
    "Shipping address logic: use shipping address if present on contract, otherwise fall back to billing address",
    "Billing contact logic: use account payable name/email if stated, otherwise keep HubSpot pulled value",
    "Price calculation must account for discounts shown net in Total column (need to back into gross price)",
    "Software total price calculation requires division by payment cadence"
  ],
  "merchant_specific": [
    "Merchant Name: Coram AI (template field)",
    "Implementation POC: (IM to fill) - placeholder for merchant-specific contact",
    "CX POC: [IMP to Add] - placeholder for merchant-specific contact",
    "Billing model section - entire section to be filled by Implementation team",
    "Unique customer creation process information - merchant-specific",
    "How merchant bills - merchant-specific information",
    "Contract structure/breakdown - merchant-specific",
    "One-off merchant-specific items to know",
    "Example contracts referenced: C5f57475-0d83-4f3d-8523-c0a8627878da, 705af407-3f06-4833-ba38-9357a829e1d5, E2022f1a-dc74-414e-8b2c-7f305ade13ab",
    "Items to ignore in contracts - merchant-specific",
    "Tax handling as line item - merchant-specific",
    "Events billing information - merchant-specific (if necessary)",
    "Integration item assignment instructions - merchant-specific (examples: Statsig labeled as 'Sales', Pinata labeled as 'Software Subscription Bundle')",
    "Post-processing communication requirements - merchant-specific notification needs"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: MIS_ Coram AI_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:01:01

### Original Content
```
Very smart and technical - will actively be looking to push the product limits 3) What are the Tabs features that the key POC cares about Automate Invoicing   Standardize Billing Operations Transition ownership of invoicing from Sales Sales Ops to Finance, replacing the current ad hoc, HubSpot-driven process Enable Fast, Scalable Invoice Generation via QuickBooks Go live on QBO quickly (within 3 4 weeks) to streamline invoice creation and collections Integrate HubSpot for Contract Ingestion   Sy...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Automation and Billing Operations Standardization",
    "System Integration and Data Synchronization (HubSpot, QuickBooks)",
    "Revenue Recognition Compliance and Audit Preparation",
    "Ownership Transition from Sales/Sales Ops to Finance",
    "Advanced Revenue Recognition Features and Future Scalability"
  ],
  "rules": [
    {
      "rule": "Invoicing ownership must transition from Sales/Sales Ops to Finance department",
      "type": "organizational",
      "explicit": true
    },
    {
      "rule": "QuickBooks Online (QBO) implementation must be completed within 3-4 weeks",
      "type": "timeline",
      "explicit": true
    },
    {
      "rule": "Revenue schedules must be reconstructed from January 2024 onward",
      "type": "data_requirement",
      "explicit": true
    },
    {
      "rule": "Revenue recognition must comply with ASC 606 standards",
      "type": "compliance",
      "explicit": true
    },
    {
      "rule": "HubSpot must be integrated for contract ingestion and quote-to-invoice workflow",
      "type": "integration",
      "explicit": true
    },
    {
      "rule": "System must support structured deal data extraction automatically from HubSpot",
      "type": "technical",
      "explicit": true
    },
    {
      "rule": "Ad hoc HubSpot-driven invoicing processes must be replaced with standardized operations",
      "type": "process_improvement",
      "explicit": true
    },
    {
      "rule": "Advanced RevRec features (SSP allocation, hardware/software separation, co-terming) implementation timeline is early next year",
      "type": "timeline",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Advanced Revenue Recognition features (SSP, Co-Terming, hardware/software separation) are not immediately urgent",
      "condition": "Timeline deferred to early next year",
      "context": "Phased implementation approach"
    },
    {
      "exception": "Complex contract modifications support (co-terms, blended terms) dependent on Tabs feature rollout",
      "condition": "Features must be available in Tabs platform first",
      "context": "Platform capability dependency"
    }
  ],
  "merchant_specific": [
    {
      "element": "Current invoicing system: HubSpot-driven ad hoc process",
      "category": "existing_infrastructure",
      "customization_needed": "Migration strategy from HubSpot to Tabs"
    },
    {
      "element": "Target accounting system: QuickBooks Online (QBO)",
      "category": "integration_target",
      "customization_needed": "QBO-specific integration configuration"
    },
    {
      "element": "Revenue backfill start date: January 2024",
      "category": "data_migration",
      "customization_needed": "Historical data reconstruction scope"
    },
    {
      "element": "Stakeholder profile: Very smart and technical, will push product limits",
      "category": "customer_profile",
      "customization_needed": "Support and documentation level, advanced feature access"
    },
    {
      "element": "Organizational structure: Sales, Sales Ops, and Finance departments with defined handoff",
      "category": "org_structure",
      "customization_needed": "Role-based access and workflow configuration"
    },
    {
      "element": "Future requirements: SSP allocation, hardware/software revenue separation",
      "category": "roadmap",
      "customization_needed": "Advanced revenue recognition configuration for specific business model"
    },
    {
      "element": "Audit preparation requirement",
      "category": "compliance_driver",
      "customization_needed": "Audit-ready reporting and documentation"
    }
  ],
  "confidence_score": 0.85
}
```

---

