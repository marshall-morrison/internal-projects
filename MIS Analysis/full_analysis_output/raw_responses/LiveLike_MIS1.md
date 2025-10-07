# Raw LLM Analysis: LiveLike MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:43:11

---

## Chunk 1: LiveLike MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:43:11

### Original Content
```
Default to 30 if not found Default Billing Frequency Found within payment schedule in contract How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Waiting on merchant to fill out this sheet: LiveLike   Integration Items If still blank at time of pro...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Configuration and Fallback Rules",
    "Tax Handling and Line Item Processing",
    "Integration and Implementation Workflow",
    "Post-Processing Communication Protocols",
    "Merchant Relationship Management and Customer-Specific Requirements"
  ],
  "rules": [
    {
      "rule": "Default billing frequency to 30 days if not found in payment schedule",
      "category": "billing_configuration",
      "explicit": true
    },
    {
      "rule": "Billing frequency should be extracted from payment schedule in contract",
      "category": "data_extraction",
      "explicit": true
    },
    {
      "rule": "When no tax handling instruction is listed, default is every tax line item becomes a BT (Billable Tax)",
      "category": "tax_processing",
      "explicit": true
    },
    {
      "rule": "Integration items assignment requires merchant to fill out LiveLike Integration Items sheet",
      "category": "integration_setup",
      "explicit": true
    },
    {
      "rule": "If integration items sheet is blank at processing time, Implementation team handles it",
      "category": "integration_setup",
      "explicit": true
    },
    {
      "rule": "Ops team must notify designated team members upon completion of processing batches",
      "category": "communication",
      "explicit": true
    },
    {
      "rule": "International Ops team should ignore sections marked for AE/Implementation",
      "category": "team_responsibilities",
      "explicit": true
    },
    {
      "rule": "Notification should occur in merchant-specific internal channel",
      "category": "communication",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Special memos may be required for certain customer invoices",
      "condition": "Based on merchant-customer relationship specifics",
      "impact": "Invoice customization required"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship dynamics",
      "condition": "Customer-specific requirements",
      "impact": "Standard invoice format may not apply"
    },
    {
      "exception": "Usage-based billing varies by contract (monthly, quarterly, yearly)",
      "condition": "Contract-specific terms for impressions and clicks",
      "impact": "No single billing pattern applies to all contracts"
    },
    {
      "exception": "Integration items handling deferred to Implementation team",
      "condition": "When merchant hasn't completed integration items sheet by processing time",
      "impact": "Processing can proceed without complete merchant input"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: LiveLike",
      "type": "identifier",
      "customizable": false
    },
    {
      "element": "Key POC: Lawrence",
      "type": "contact_information",
      "customizable": true
    },
    {
      "element": "Merchant temperament: 'very nice, a little bit of an ego, wears a lot of hats'",
      "type": "relationship_notes",
      "customizable": true
    },
    {
      "element": "Notification recipient: Customer Success [Azmat Aziz]",
      "type": "communication_routing",
      "customizable": true
    },
    {
      "element": "Notification timing: when contracts are processed in Active phase",
      "type": "workflow_trigger",
      "customizable": true
    },
    {
      "element": "Billing model: Usage-based on impressions and clicks",
      "type": "billing_methodology",
      "customizable": true
    },
    {
      "element": "Key features of interest: Automatic contract ingestion, Automatically apply usage to invoices",
      "type": "product_priorities",
      "customizable": true
    },
    {
      "element": "Integration Items sheet: LiveLike specific",
      "type": "documentation",
      "customizable": true
    },
    {
      "element": "Internal merchant channel (Messari)",
      "type": "communication_channel",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: LiveLike MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:43:14

### Original Content
```
Merchant Demo date:   Scoping start date: Oct 17, 2024 MSA Signature Date: Nov 15, 2024 Onboarding Kick Off Date: Nov 25, 2024 [If Exists] Opt Out Date: NA Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Ryan Muckey CFO: Lawrence Chan Company summary (AE to fill) LiveLike allows you to add interactive widgets to your content to improve engagement and provide insights into viewers behavior Ex Yahoo sports uses livelike during monday ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Timeline and Key Milestones",
    "Contract Processing and Data Extraction",
    "Billing Model and Revenue Recognition",
    "Customer and Event Management",
    "Service Terms and Payment Conditions"
  ],
  "rules": [
    {
      "rule": "Customers should all be ingested from Netsuite into the system",
      "category": "Customer Management"
    },
    {
      "rule": "If customer not found in system, create in Garage and merchant can populate billing contact info",
      "category": "Customer Management"
    },
    {
      "rule": "Use Contractual Term for start and end dates",
      "category": "Contract Processing"
    },
    {
      "rule": "If no start date in Contractual Term, use Effective Date",
      "category": "Contract Processing"
    },
    {
      "rule": "All billing terms found in 'Financial Terms and Payment Schedule' section of contract along with Section 3 Support Services",
      "category": "Billing Terms"
    },
    {
      "rule": "Fee type column on the left is used for item name",
      "category": "Billing Terms"
    },
    {
      "rule": "Tier (e.g., Silver) can be input as description where applicable",
      "category": "Billing Terms"
    },
    {
      "rule": "Events should all be created already for any usage-based billing terms",
      "category": "Event Management"
    },
    {
      "rule": "If event not found, create event in merchant app",
      "category": "Event Management"
    },
    {
      "rule": "Ignore anything marked as 'optional' (e.g., Optional Upgrade)",
      "category": "Contract Processing"
    },
    {
      "rule": "Ignore anything under 'Rate Card for Optional Add-on Services'",
      "category": "Contract Processing"
    },
    {
      "rule": "Default Service Term found in 'Order Term' at top of contract",
      "category": "Service Terms"
    },
    {
      "rule": "Tie Service period back to duration of billing term",
      "category": "Service Terms"
    },
    {
      "rule": "Each Revenue Schedule (RS) in Garage should spread revenue across the billing period (e.g., 12 month period for annual billing)",
      "category": "Revenue Recognition"
    },
    {
      "rule": "Default Net Payment Terms found in Section 4 Payment Terms",
      "category": "Payment Terms"
    },
    {
      "rule": "Billing frequency is quarterly for this merchant",
      "category": "Billing Model"
    }
  ],
  "exceptions": [
    {
      "exception": "If contract has price increases each year (e.g., 3-year contract with annual price changes), each RS in Garage should spread revenue across 12-month period rather than entire contract term",
      "condition": "Multi-year contracts with annual price variations"
    },
    {
      "exception": "Optional items and add-on services from rate cards should be ignored during contract processing",
      "condition": "Items marked as optional or in add-on rate card sections"
    },
    {
      "exception": "Invoice dates may need to be back-dated to final day of the month based on merchant-specific requests",
      "condition": "Merchant-specific processing requirements that may differ by contract"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "condition": "Standard for this merchant"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company: LiveLike - interactive widget platform for content engagement",
      "type": "Business Description"
    },
    {
      "element": "Key Personnel: Ryan Muckey (Accountant), Lawrence Chan (CFO)",
      "type": "Contacts"
    },
    {
      "element": "Timeline: Demo date unknown, Scoping Oct 17 2024, MSA Nov 15 2024, Kickoff Nov 25 2024, Go Live Jan 1 2025",
      "type": "Project Milestones"
    },
    {
      "element": "Billing Model: Quarterly billing, varies by customer",
      "type": "Billing Configuration"
    },
    {
      "element": "No unique customer creation process",
      "type": "Process Customization"
    },
    {
      "element": "Reference to GOTHAM and LIV contracts as processing examples",
      "type": "Documentation References"
    },
    {
      "element": "ERP System: Not specified",
      "type": "Technical Integration"
    },
    {
      "element": "Tax Integration: Not specified",
      "type": "Technical Integration"
    },
    {
      "element": "Merchant Goals: Fully integrated revenue automation, contract ingestion, usage calculation, comprehensive commercial graph for reporting and revenue recognition",
      "type": "Business Objectives"
    }
  ],
  "confidence_score": 0.85
}
```

---

