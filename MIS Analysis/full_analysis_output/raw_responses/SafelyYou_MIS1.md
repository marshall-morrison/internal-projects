# Raw LLM Analysis: SafelyYou MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:22:16

---

## Chunk 1: SafelyYou MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:22:16

### Original Content
```
Merchant Name: NAME Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant has r...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Stakeholder Management and Communication",
    "Default Operational Parameters",
    "Integration and Event Handling",
    "Customer-Specific Requirements and Customization"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "billing_defaults",
      "source": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none listed",
      "category": "billing_defaults",
      "source": "explicit"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_defaults",
      "source": "explicit"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction)",
      "category": "tax_processing",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling contract processing steps post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "AE fills feature requests prior to implementation handoff",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation team fills feature requests prior to go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Success team fills feature requests post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) on handoff notes",
      "category": "responsibility_assignment",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice dates may be back-dated to final day of month per merchant request",
      "condition": "merchant-specific processing requirements",
      "example": "always back-date invoice date to final day of the month"
    },
    {
      "exception": "Integration item labeling varies by merchant",
      "condition": "merchant-specific integration rules",
      "examples": [
        "All Statsig integration items labeled as 'Sales'",
        "All Pinata integration items labeled as 'Software Subscription Bundle' unless otherwise noted"
      ]
    },
    {
      "exception": "Contract processing steps may differ by contract within same merchant",
      "condition": "specific merchant requests",
      "note": "Specifics processing things the merchant has requested that may differ by contract"
    },
    {
      "exception": "Certain invoices may require special memos",
      "condition": "based on merchant-customer relationship",
      "note": "Invoice changes due to merchant customer relationship"
    },
    {
      "exception": "Some contract elements should be ignored during processing",
      "condition": "merchant-specific instructions",
      "note": "Anything to ignore in contracts"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_required": true,
      "filled_by": "varies"
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
      "element": "Billing model",
      "customization_required": true,
      "filled_by": "Implementation team",
      "includes": [
        "Customer creation process uniqueness",
        "How merchant bills",
        "Contract structure"
      ]
    },
    {
      "element": "Contract Processing Steps",
      "customization_required": true,
      "note": "May include merchant-specific processing requests that differ by contract"
    },
    {
      "element": "Events Processing instructions",
      "customization_required": true,
      "condition": "if necessary",
      "filled_by": "Implementation Success post-go-live"
    },
    {
      "element": "Integration Items Processing",
      "customization_required": true,
      "condition": "if necessary",
      "note": "Specific labeling rules per merchant (e.g., Statsig, Pinata)"
    },
    {
      "element": "Post Processing Communications",
      "customization_required": true,
      "condition": "if necessary",
      "includes": [
        "Who needs notification",
        "When notification is required",
        "Where to communicate"
      ]
    },
    {
      "element": "Customer Information",
      "customization_required": true,
      "includes": [
        "Specific customer details",
        "Special invoice memos",
        "Customer relationship considerations"
      ]
    },
    {
      "element": "Feature Requests",
      "customization_required": true,
      "attributes": [
        "What is it",
        "Why it's important",
        "Urgency"
      ]
    },
    {
      "element": "Merchant temperament",
      "customization_required": true,
      "note": "Qualitative assessment of merchant personality/style"
    },
    {
      "element": "Key POC feature preferences",
      "customization_required": true,
      "note": "Tabs features that key POC cares about"
    }
  ],
  "confidence_score": 0.92
}
```

---

