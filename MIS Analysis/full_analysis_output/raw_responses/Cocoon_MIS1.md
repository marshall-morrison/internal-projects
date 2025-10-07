# Raw LLM Analysis: Cocoon MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:00:32

---

## Chunk 1: Cocoon MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:00:32

### Original Content
```
Merchant Name: NAME Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant has r...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Stakeholder Communication and Responsibility Assignment",
    "Default Values and Operational Standards",
    "Integration and Event Processing Management",
    "Customer-Specific Handling and Customization"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "billing_defaults",
      "source": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 if none listed",
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
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps section post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation fills Feature Requests prior to go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Success team fills Feature Requests post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "AE is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "responsibility_assignment",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., always back-date invoice date to final day of the month)",
      "condition": "merchant-requested specifics that differ by contract",
      "impact": "processing_workflow"
    },
    {
      "exception": "Integration items may have special labeling requirements",
      "condition": "specific integration types (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "impact": "item_categorization"
    },
    {
      "exception": "Certain invoices may require special memos",
      "condition": "based on merchant-customer relationship",
      "impact": "invoice_generation"
    },
    {
      "exception": "Invoice changes may be required",
      "condition": "due to specific merchant-customer relationships",
      "impact": "invoice_modification"
    },
    {
      "exception": "Some contract elements should be ignored during processing",
      "condition": "merchant-specific instructions",
      "impact": "contract_processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_required": true,
      "type": "identifier"
    },
    {
      "element": "Implementation POC",
      "customization_required": true,
      "type": "contact_information"
    },
    {
      "element": "CX POC",
      "customization_required": true,
      "type": "contact_information"
    },
    {
      "element": "Billing model and customer creation process",
      "customization_required": true,
      "type": "business_process"
    },
    {
      "element": "Contract structure and breakdown",
      "customization_required": true,
      "type": "contract_configuration"
    },
    {
      "element": "Post-processing notification requirements",
      "customization_required": true,
      "type": "communication_workflow",
      "details": "Who to notify, where, and when"
    },
    {
      "element": "Integration items labeling rules",
      "customization_required": true,
      "type": "categorization_rules"
    },
    {
      "element": "Customer-specific information and special requirements",
      "customization_required": true,
      "type": "customer_handling"
    },
    {
      "element": "Merchant temperament and key POC preferences",
      "customization_required": true,
      "type": "relationship_management"
    },
    {
      "element": "Feature requests with urgency levels",
      "customization_required": true,
      "type": "product_requirements"
    }
  ],
  "confidence_score": 0.92
}
```

---

