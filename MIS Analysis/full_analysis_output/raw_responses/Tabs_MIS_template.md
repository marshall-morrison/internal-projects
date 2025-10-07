# Raw LLM Analysis: Tabs MIS template

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:46:49

---

## Chunk 1: Tabs MIS template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:46:49

### Original Content
```
Merchant Name (AE to fill) Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Merchant Onboarding and Implementation Workflow",
    "Stakeholder Communication and Responsibility Assignment",
    "Default Settings and Operational Standards",
    "Customer-Specific Handling and Customization"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Billing Defaults",
      "source": "Contract Processing Steps"
    },
    {
      "rule": "Default Net Payment Terms is 0 days if none listed",
      "category": "Billing Defaults",
      "source": "Contract Processing Steps"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Defaults",
      "source": "Contract Processing Steps"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "source": "Contract Processing Steps"
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps section Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Multiple sections"
    },
    {
      "rule": "AE (Account Executive) fills merchant name and feature requests prior to implementation handoff",
      "category": "Responsibility Assignment",
      "source": "Document headers"
    },
    {
      "rule": "Implementation team fills billing model section and implementation-related fields",
      "category": "Responsibility Assignment",
      "source": "Document headers"
    },
    {
      "rule": "Success team fills post-go-live updates for feature requests and merchant calls",
      "category": "Responsibility Assignment",
      "source": "Feature Requests and Merchant Calls sections"
    },
    {
      "rule": "Implementation is the completion DRI (Directly Responsible Individual) on handoff notes",
      "category": "Responsibility Assignment",
      "source": "Notes Sections"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., always back-date invoice date to final day of the month)",
      "condition": "When merchant has specific requests that differ by contract",
      "source": "Contract Processing Steps"
    },
    {
      "exception": "Integration items may have special labeling requirements",
      "condition": "Depends on integration type (e.g., Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')",
      "source": "Integration Items Processing"
    },
    {
      "exception": "Certain invoices may require special memos",
      "condition": "Based on merchant-customer relationship specifics",
      "source": "Customer Information"
    },
    {
      "exception": "Invoice changes may be required based on merchant-customer relationship",
      "condition": "Customer-specific arrangements",
      "source": "Customer Information"
    },
    {
      "exception": "Some contract elements may need to be ignored during processing",
      "condition": "As specified in merchant-specific instructions",
      "source": "Contract Processing Steps"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_required": true,
      "filled_by": "AE"
    },
    {
      "element": "Implementation POC",
      "customization_required": true,
      "filled_by": "IM (Implementation Manager)"
    },
    {
      "element": "CX POC (Customer Experience Point of Contact)",
      "customization_required": true,
      "filled_by": "IMP (Implementation)"
    },
    {
      "element": "Billing model and customer creation process",
      "customization_required": true,
      "filled_by": "Implementation team"
    },
    {
      "element": "Contract processing steps and specifics",
      "customization_required": true,
      "note": "May differ by contract within same merchant"
    },
    {
      "element": "Events billing information",
      "customization_required": true,
      "conditional": "If necessary"
    },
    {
      "element": "Integration items labeling rules",
      "customization_required": true,
      "conditional": "If necessary",
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification requirements",
      "customization_required": true,
      "includes": ["Who to notify", "Where to notify", "When to notify"]
    },
    {
      "element": "Customer-specific information and invoice requirements",
      "customization_required": true,
      "note": "Varies by merchant's customer relationships"
    },
    {
      "element": "Merchant temperament and key POC preferences",
      "customization_required": true,
      "note": "Includes Tabs features that POC cares about"
    },
    {
      "element": "Non-standard deal conversations",
      "customization_required": true,
      "filled_by": "SC (Success/Sales Consultant)",
      "requires_documentation": true
    }
  ],
  "confidence_score": 0.92
}
```

---

