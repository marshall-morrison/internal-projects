# Raw LLM Analysis: Arist MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:48:30

---

## Chunk 1: Arist MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:48:30

### Original Content
```
Merchant Name: Arist Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant has ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Process",
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters and Standards",
    "Cross-functional Communication and Stakeholder Management",
    "Merchant-Specific Customization and Exception Handling"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Billing Defaults",
      "source": "Ops Default"
    },
    {
      "rule": "Default Net Payment Terms is 0 if none listed",
      "category": "Billing Defaults",
      "source": "Ops Default"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Defaults",
      "source": "Ops Default"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "source": "Ops Default"
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps section Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Implementation fills Feature Requests prior to go-live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Success team fills Feature Requests Post-Go Live",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "Responsibility Assignment",
      "source": "Section ownership"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., always back-date invoice date to final day of the month)",
      "context": "Contract Processing Steps",
      "note": "Merchant may request specific processing that differs by contract"
    },
    {
      "exception": "Integration item labeling may vary by merchant (e.g., Statsig items labeled as 'Sales', Pinata items as 'Software Subscription Bundle')",
      "context": "Integration Items Processing",
      "note": "Unless otherwise noted by Merchant"
    },
    {
      "exception": "Certain contracts may have items to ignore during processing",
      "context": "Contract Processing Steps",
      "note": "Specified on per-merchant basis"
    },
    {
      "exception": "Special memos may be required for certain invoices based on customer relationships",
      "context": "Customer Information",
      "note": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "context": "Customer Information",
      "note": "Relationship-dependent modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_type": "Identity",
      "example": "Arist Implementation POC"
    },
    {
      "element": "CX POC and IM POC contacts",
      "customization_type": "Stakeholder Information",
      "note": "To be filled by Implementation team"
    },
    {
      "element": "Billing model specifics",
      "customization_type": "Billing Configuration",
      "note": "How merchant bills, contract structure, unique customer creation process"
    },
    {
      "element": "Contract processing steps",
      "customization_type": "Operational Process",
      "note": "Merchant-specific processing requests and contract handling"
    },
    {
      "element": "Events billing information",
      "customization_type": "Billing Configuration",
      "note": "If necessary for the merchant"
    },
    {
      "element": "Integration items labeling rules",
      "customization_type": "Data Classification",
      "note": "Merchant-specific integration categorization"
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "Communication Protocol",
      "note": "Who to notify, where, and when based on merchant phase"
    },
    {
      "element": "Customer-specific information",
      "customization_type": "Customer Management",
      "note": "Special requirements for specific customers of the merchant"
    },
    {
      "element": "Feature requests tracking",
      "customization_type": "Product Requirements",
      "note": "What, why, importance, and urgency per merchant"
    },
    {
      "element": "Merchant temperament and key POC preferences",
      "customization_type": "Relationship Management",
      "note": "Understanding merchant personality and feature priorities"
    }
  ],
  "confidence_score": 0.85
}
```

---

