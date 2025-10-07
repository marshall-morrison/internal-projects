# Raw LLM Analysis: General Catalyst MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:22:55

---

## Chunk 1: General Catalyst MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:22:55

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
    "Merchant-Specific Customization and Special Requirements",
    "Cross-functional Handoff and Documentation"
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
      "rule": "Implementation POC must be filled by IM (Implementation Manager)",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "CX POC must be added by IMP (Implementation)",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Billing model section must be filled by Implementation team",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Contract Processing Steps must be filled by Implementation Success Post-Go Live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Events Processing section must be filled by Implementation Success Post-Go Live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Integration Items Processing must be filled by Implementation Success Post-Go Live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success Post-Go Live",
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
      "rule": "Success team fills Feature Requests Post-Go Live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "responsibility_assignment",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice dates may be back-dated to final day of month per merchant request",
      "condition": "Merchant-specific processing requirements that differ by contract",
      "context": "contract_processing"
    },
    {
      "exception": "Statsig integration items should be labeled as 'Sales'",
      "condition": "Specific integration vendor",
      "context": "integration_items"
    },
    {
      "exception": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "condition": "Specific integration vendor with merchant override option",
      "context": "integration_items"
    },
    {
      "exception": "Some contracts may have items to ignore during processing",
      "condition": "Merchant-specific contract processing requirements",
      "context": "contract_processing"
    },
    {
      "exception": "Certain invoices may require special memos based on merchant-customer relationship",
      "condition": "Customer-specific requirements",
      "context": "customer_information"
    },
    {
      "exception": "Invoice changes may be required due to merchant-customer relationship",
      "condition": "Customer-specific requirements",
      "context": "customer_information"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_type": "identifier",
      "required": true
    },
    {
      "element": "Implementation POC",
      "customization_type": "contact_assignment",
      "required": true
    },
    {
      "element": "CX POC",
      "customization_type": "contact_assignment",
      "required": true
    },
    {
      "element": "Billing model details",
      "customization_type": "billing_configuration",
      "required": true,
      "includes": ["customer creation process", "how merchant bills", "contract structure", "one-off merchant specifics"]
    },
    {
      "element": "Contract processing steps",
      "customization_type": "operational_procedures",
      "required": true,
      "includes": ["processing steps", "items to ignore", "specific processing requests"]
    },
    {
      "element": "Service Term",
      "customization_type": "billing_parameter",
      "required": false,
      "default": "1 Year"
    },
    {
      "element": "Net Payment Terms",
      "customization_type": "billing_parameter",
      "required": false,
      "default": "0"
    },
    {
      "element": "Billing Frequency",
      "customization_type": "billing_parameter",
      "required": false,
      "default": "Monthly"
    },
    {
      "element": "Tax handling",
      "customization_type": "billing_configuration",
      "required": false,
      "default": "every tax line item becomes a BT"
    },
    {
      "element": "Events billing information",
      "customization_type": "billing_configuration",
      "required": false,
      "conditional": "if necessary"
    },
    {
      "element": "Integration items labeling instructions",
      "customization_type": "operational_procedures",
      "required": false,
      "conditional": "if necessary"
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "communication_protocol",
      "required": false,
      "conditional": "if necessary",
      "includes": ["who to notify", "where to notify", "when to notify"]
    },
    {
      "element": "Customer-specific information",
      "customization_type": "customer_requirements",
      "required": false,
      "includes": ["special memos", "invoice changes", "customer relationship details"]
    },
    {
      "element": "Feature Requests",
      "customization_type": "product_requirements",
      "required": true,
      "includes": ["what it is", "why it's important", "urgency"]
    },
    {
      "element": "Merchant temperament",
      "customization_type": "relationship_management",
      "required": true
    },
    {
      "element": "Key POC feature preferences",
      "customization_type": "relationship_management",
      "required": true
    }
  ],
  "confidence_score": 0.92
}
```

---

