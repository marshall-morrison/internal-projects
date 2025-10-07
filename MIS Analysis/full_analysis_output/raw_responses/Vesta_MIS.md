# Raw LLM Analysis: Vesta MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:17:29

---

## Chunk 1: Vesta MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:17:29

### Original Content
```
Merchant Name: Vesta Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant has ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Configuration",
    "Default Processing Parameters and Overrides",
    "Stakeholder Communication and Handoff Procedures",
    "Merchant-Specific Customer Relationship Management",
    "Implementation Lifecycle Documentation"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction/Item)",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps section Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) for Notes Section on handoff",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Integration items must be labeled according to merchant-specific instructions",
      "category": "Integration Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., always back-date invoice date to final day of the month)",
      "context": "Contract Processing Steps",
      "conditional": true
    },
    {
      "exception": "Special memos may be required for certain customer invoices",
      "context": "Customer Information",
      "conditional": true
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship specifics",
      "context": "Customer Information",
      "conditional": true
    },
    {
      "exception": "Integration item labeling may vary by merchant (e.g., Statsig vs Pinata have different labeling rules)",
      "context": "Integration Items Processing",
      "conditional": true
    },
    {
      "exception": "Post-processing notifications vary by merchant phase (Implementation vs Active)",
      "context": "Post Processing Communications",
      "conditional": true
    }
  ],
  "merchant_specific": [
    {
      "element": "POC (Point of Contact) assignments",
      "fields": ["IM POC", "CX POC"],
      "customizable": true
    },
    {
      "element": "Billing model details",
      "description": "Unique customer creation process, contract structure, billing methodology",
      "customizable": true
    },
    {
      "element": "Integration item labeling conventions",
      "examples": ["Statsig items labeled as 'Sales'", "Pinata items labeled as 'Software Subscription Bundle'"],
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "fields": ["Who to notify", "Where to notify", "When to notify"],
      "customizable": true
    },
    {
      "element": "Merchant temperament and communication preferences",
      "example": "Nolan needs explicit instructions and clear action items; first-time software buyer",
      "customizable": true
    },
    {
      "element": "Key feature priorities",
      "examples": ["Quickbooks integration", "Auto-generate invoices", "Usage data ingestion via API"],
      "customizable": true
    },
    {
      "element": "Billing structure types",
      "examples": ["Platform fees", "Usage with minimums"],
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special handling for specific customers, invoice modifications",
      "customizable": true
    }
  ],
  "confidence_score": 0.88
}
```

---

