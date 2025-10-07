# Raw LLM Analysis: Capitalize MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:07:08

---

## Chunk 1: Capitalize MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:07:08

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and Events Processing Workflow",
    "Integration Item Labeling and Classification",
    "Post-Processing Communication Protocols",
    "Customer-Specific Invoice Customization",
    "Merchant Relationship Management and Key Stakeholder Identification"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: All tax line items become BT Events Processing when none are specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Integration items must be assigned specific labels based on merchant type (e.g., Statsig items labeled as 'Sales', Pinata items labeled as 'Software Subscription Bundle')",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Notification example: Customer Success (Azmat Aziz) to be notified in merchant internal channel when contracts are processed during Active phase",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling in processing instructions, customer information, and communication protocols",
      "category": "Role Assignment",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling in feature requests and custom demo notes",
      "category": "Role Assignment",
      "explicit": true
    },
    {
      "rule": "International Ops Team should ignore Custom Demo Notes sections",
      "category": "Role Assignment",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items default to 'Software Subscription Bundle' unless otherwise noted by merchant",
      "condition": "Merchant can override default labeling"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to specific merchant-customer relationships",
      "condition": "Relationship-dependent modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customization_needed": "Each merchant may have different integration types requiring specific labels",
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification recipients and timing",
      "customization_needed": "Different merchants may require notifications to different team members at different phases",
      "examples": ["Customer Success notification during Active phase"]
    },
    {
      "element": "Merchant temperament and relationship status",
      "customization_needed": "Each merchant has unique engagement patterns and communication preferences",
      "examples": ["Really excited, went dark for a while but re-engaged"]
    },
    {
      "element": "Key Point of Contact (POC) identification",
      "customization_needed": "Decision makers and stakeholders vary by merchant",
      "examples": ["Aditi as major decision maker", "Mike previously involved but not in current deal"]
    },
    {
      "element": "Feature priorities",
      "customization_needed": "Different merchants care about different platform features",
      "examples": ["Usage ingest", "Invoice calculation and sending", "Reporting"]
    },
    {
      "element": "Billing structure",
      "customization_needed": "Merchants may have tiered usage, multiple event types, or minimums",
      "examples": ["Tiered usage", "2-3 different event types", "sometimes have minimums"]
    },
    {
      "element": "Customer-specific invoice requirements",
      "customization_needed": "Special memos or invoice modifications based on customer relationships"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Capitalize MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:07:09

### Original Content
```
Merchant Demo date: 8 20 24 Scoping start date: 9 5 24 MSA Signature Date: 11 27 24 Onboarding Kick Off Date: TBD [If Exists] Opt Out Date: 5 27 25 Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Aditi Bhatia - VP Finance   Ops Mike Mumma - Director Strategy   Ops Company summary (AE to fill) Capitalize helps individuals take control of their retirement savings by simplifying the process of rolling over old 401(k) accounts into individual retirement accoun...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Usage-Based Billing and Invoice Automation",
    "Contract Processing and Data Ingestion Workflow",
    "Opt-Out Clause Management and Risk Mitigation",
    "Default Operational Parameters and Configuration Settings"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "operational_defaults",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "operational_defaults",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "operational_defaults",
      "explicit": true
    },
    {
      "rule": "Monthly Looker reports must be ingested and adjusted according to configuration settings",
      "category": "data_processing",
      "explicit": true
    },
    {
      "rule": "Adjustments to Looker reports are documented in Green in the reference sheet",
      "category": "data_processing",
      "explicit": true
    },
    {
      "rule": "Six month opt-out clause exists from the opt-out date (5/27/25)",
      "category": "contract_terms",
      "explicit": true
    },
    {
      "rule": "Merchant has very few customers, so contracts rarely come through",
      "category": "processing_volume",
      "explicit": true
    },
    {
      "rule": "Billing model is usage-only (no fixed fees or contracts)",
      "category": "billing_structure",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Opt-out clause triggered if Tabs cannot adequately support merchant's usage needs",
      "condition": "Six month evaluation period to ensure usage data handling capability",
      "context": "Initial demo only covered 2 contracts with no real usage data"
    },
    {
      "exception": "Contract-specific processing variations may exist",
      "condition": "Merchant may request specific processing differences per contract (e.g., back-dating invoice dates)",
      "context": "Document mentions potential for contract-specific requests"
    },
    {
      "exception": "Some contract data may need to be ignored during processing",
      "condition": "Document indicates there may be specific elements to ignore in contracts",
      "context": "Section exists but not populated with specific examples"
    }
  ],
  "merchant_specific": [
    {
      "element": "Looker Report Integration",
      "description": "Merchant uses Looker for monthly usage reporting with custom adjustments required",
      "customization_required": true
    },
    {
      "element": "Key Contacts",
      "description": "Aditi Bhatia (VP Finance & Ops) and Mike Mumma (Director Strategy & Ops)",
      "customization_required": true
    },
    {
      "element": "Business Model",
      "description": "Retirement savings rollover platform (401k to IRA)",
      "customization_required": false
    },
    {
      "element": "Usage Data Configuration",
      "description": "Specific adjustments needed to configure Looker data to Tabs settings (documented in Green)",
      "customization_required": true
    },
    {
      "element": "Low Contract Volume",
      "description": "Very few customers means minimal contract processing",
      "customization_required": false
    },
    {
      "element": "Opt-Out Risk Mitigation",
      "description": "Need to demonstrate capability to handle usage needs within 6 months",
      "customization_required": true
    },
    {
      "element": "Timeline Dates",
      "description": "Demo: 8/20/24, Scoping: 9/5/24, MSA: 11/27/24, Opt-Out: 5/27/25",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

