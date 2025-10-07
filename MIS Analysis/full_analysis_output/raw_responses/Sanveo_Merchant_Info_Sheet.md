# Raw LLM Analysis: Sanveo Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:43:37

---

## Chunk 1: Sanveo Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:43:37

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Integration Item Labeling and Classification",
    "Post-Processing Communication and Notification Protocols",
    "Customer-Specific Invoice Handling Requirements",
    "Merchant Operational Workflow and Data Processing",
    "Merchant Relationship Management and Feature Priorities"
  ],
  "rules": [
    {
      "rule": "Default tax line item handling: If no specific instruction is listed, every tax line item becomes a BT Events Processing",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Statsig integration items must be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Pinata integration items must be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active phase",
      "category": "Post-Processing Communication",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling in events billing, integration items processing, and customer information sections",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Notes Sections marked for AE/Implementation",
      "category": "Team Scope",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "Merchant provides alternative labeling instruction"
    },
    {
      "exception": "Tax line item processing may vary from default BT Events Processing if specific instructions are provided",
      "condition": "When alternative instructions are explicitly listed"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements exist"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customizable": true,
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification recipients and channels",
      "customizable": true,
      "examples": ["Customer Success contact person", "Internal merchant channel", "Timing of notifications"]
    },
    {
      "element": "Customer-specific invoice requirements",
      "customizable": true,
      "examples": ["Special memos", "Invoice modifications based on customer relationships"]
    },
    {
      "element": "Merchant operational workflow",
      "customizable": true,
      "examples": ["Data compilation method (Excel → Airtable → QuickBooks)", "Invoice volume (90-150/month)", "Payment timing (120+ days)", "Invoice attachments (timesheets, schedules)"]
    },
    {
      "element": "Merchant temperament and relationship dynamics",
      "customizable": true,
      "examples": ["Eager/time-sensitive/decisive", "Key POC: Ameer Shaikh (EVP)", "Priority features: rapid invoice creation, unstructured data handling"]
    },
    {
      "element": "Expected turnaround improvements",
      "customizable": true,
      "examples": ["From 5-15 days to <5 hours for invoice generation"]
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Sanveo Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:43:38

### Original Content
```
Merchant Demo date: Jun 16, 2025 Scoping start date: n a MSA Signature Date: Jun 19, 2025 Onboarding Kick-Off Date: TBD [If Exists] Opt Out Date: none Go Live Date: BD GTM POC: Implementation POC: N a ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC: Ameer Shaikh (EVP) Billing POC: Ameer Shaikh (EVP) Etc Company summary (AE to fill) Summary of what company does: Construction technology company specializing in electr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline Management",
    "Complex Contract and Billing Processing",
    "Automation of Manual AR and Invoicing Workflows",
    "Custom Field and Data Requirements",
    "Contract Processing Standards and Defaults"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed in contract",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Default net payment terms is 0 (net zero) if none specified",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "PO numbers must be visible or editable in the system",
      "category": "data_requirements",
      "explicit": true
    },
    {
      "rule": "EINs must be visible or editable in the system",
      "category": "data_requirements",
      "explicit": true
    },
    {
      "rule": "Custom fields must be visible or editable",
      "category": "data_requirements",
      "explicit": true
    },
    {
      "rule": "Billing cadence varies per project and must be flexible",
      "category": "billing_model",
      "explicit": true
    },
    {
      "rule": "System must support project-based recurring billing",
      "category": "billing_model",
      "explicit": true
    },
    {
      "rule": "Placeholder invoices may be needed for contract-based estimated services",
      "category": "invoicing",
      "explicit": true
    },
    {
      "rule": "Contracts are non-standard and require flexible AR processing",
      "category": "contract_processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Billing cadence varies per project (not standardized)",
      "context": "Different projects may have different billing schedules"
    },
    {
      "exception": "Potential gaps or long delays between jobs in billing cycle",
      "context": "Billing may not be continuous; system must handle irregular patterns"
    },
    {
      "exception": "Invoice dates may need to be back-dated to final day of month",
      "context": "Contract-specific processing may differ; example given of date manipulation"
    },
    {
      "exception": "No opt-out clause present",
      "context": "Standard opt-out monitoring does not apply to this merchant"
    },
    {
      "exception": "No CRM system in place",
      "context": "Cannot integrate with or rely on external CRM data"
    }
  ],
  "merchant_specific": [
    {
      "element": "Industry vertical",
      "value": "Construction technology / electrical contracting",
      "customization_needed": true
    },
    {
      "element": "Project duration",
      "value": "6-30 months",
      "customization_needed": true
    },
    {
      "element": "Key personnel",
      "value": "Ameer Shaikh (EVP) as both AR POC and Billing POC",
      "customization_needed": true
    },
    {
      "element": "Pain points",
      "value": "Slow manual AR, contract review work, overburdened legal staff",
      "customization_needed": false
    },
    {
      "element": "Goals",
      "value": "Replace manual processes, automate invoicing, transition to Rillet, centralize financial ops",
      "customization_needed": false
    },
    {
      "element": "Contract characteristics",
      "value": "Variable, non-standard contracts requiring flexible processing",
      "customization_needed": true
    },
    {
      "element": "Missing information",
      "value": "ERP system, Tax Integration system, Go Live Date (marked as 'BD'), Implementation POC, Onboarding Kick-Off Date",
      "customization_needed": true
    },
    {
      "element": "Tax handling",
      "value": "Question raised about handling taxes as line item (not answered in document)",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

