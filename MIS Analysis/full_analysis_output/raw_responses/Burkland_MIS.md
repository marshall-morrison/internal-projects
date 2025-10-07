# Raw LLM Analysis: Burkland MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:03:14

---

## Chunk 1: Burkland MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:03:14

### Original Content
```
There are a few features they are excited about that we committed to building at some point (did not commit to a timeline) which are outlined in Slack: 1) approval workflow (e g two levels of signoff), 2) role based controls so the individuals at Burkland can log in and only see the clients they work on (structured in teams)
```

### LLM Analysis Response
```json
{
  "themes": [
    "Feature commitments and product roadmap",
    "Access control and permissions management",
    "Approval workflows and authorization hierarchies",
    "Multi-tenant client management",
    "Team-based organizational structure"
  ],
  "rules": [
    {
      "rule": "Features mentioned are committed to be built but without specific timeline commitments",
      "type": "explicit",
      "category": "product_development"
    },
    {
      "rule": "Approval workflow must support multi-level signoff (minimum two levels mentioned)",
      "type": "explicit",
      "category": "authorization"
    },
    {
      "rule": "System must implement role-based access controls (RBAC)",
      "type": "explicit",
      "category": "security"
    },
    {
      "rule": "Users (Burkland individuals) should only see clients they are assigned to work on",
      "type": "explicit",
      "category": "data_visibility"
    },
    {
      "rule": "Client access must be structured by teams",
      "type": "explicit",
      "category": "organizational_structure"
    },
    {
      "rule": "System must support individual user login with differentiated access",
      "type": "implicit",
      "category": "authentication"
    }
  ],
  "exceptions": [
    {
      "exception": "Timeline flexibility - features are committed but delivery dates are not fixed",
      "context": "Product development commitments"
    },
    {
      "exception": "Approval workflow levels may vary - 'two levels' mentioned as example (e.g.) suggesting flexibility",
      "context": "Authorization requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Burkland",
      "type": "merchant_name",
      "description": "Specific client/merchant referenced - likely an accounting or consulting firm based on context"
    },
    {
      "element": "Team structure for client organization",
      "type": "organizational_model",
      "description": "The specific way clients are grouped into teams may vary by merchant"
    },
    {
      "element": "Number of approval levels",
      "type": "workflow_configuration",
      "description": "Two levels mentioned as example, but actual requirements may differ per merchant"
    },
    {
      "element": "Role definitions",
      "type": "access_control",
      "description": "Specific roles and permissions would need to be customized per merchant's organizational structure"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Burkland MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:03:20

### Original Content
```
Merchant Name Burkland Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant ha...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters",
    "Merchant Implementation and Handoff Procedures",
    "Integration and Event Processing Guidelines",
    "Customer-Specific Requirements and Communications"
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
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "tax_handling",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success team fills contract processing steps post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "AE fills feature requests prior to implementation handoff",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) on handoff for notes sections",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Integration items must be labeled according to merchant-specific instructions",
      "category": "integration_processing",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may exist (e.g., back-dating invoice dates to final day of month)",
      "condition": "When merchant requests differ by contract",
      "category": "contract_processing"
    },
    {
      "exception": "Integration item labeling varies by merchant (Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "condition": "Depends on merchant and integration type",
      "category": "integration_processing"
    },
    {
      "exception": "Post-processing notifications required only if necessary",
      "condition": "When merchant requires notification of batch completion",
      "category": "communications"
    },
    {
      "exception": "Events processing section only applicable if necessary for merchant",
      "condition": "When merchant has event-based billing",
      "category": "billing_model"
    },
    {
      "exception": "Special memos or invoice changes may be required for specific customers",
      "condition": "Based on merchant-customer relationship",
      "category": "customer_information"
    }
  ],
  "merchant_specific": [
    {
      "element": "Burkland billing model includes mix of standalone flat fees, services hours, and prepaid services with draw-down",
      "type": "billing_structure",
      "customizable": true
    },
    {
      "element": "Merchant temperament: accounting firm, detail-oriented, organized, thorough",
      "type": "relationship_management",
      "customizable": true
    },
    {
      "element": "Key POC: Karen Burkland (DRI for implementation, wife of Founder/CEO)",
      "type": "contact_information",
      "customizable": true
    },
    {
      "element": "Merchant priorities: automation of usage calculations, source of truth for agreements, systematic rate changes",
      "type": "feature_priorities",
      "customizable": true
    },
    {
      "element": "Twice-monthly billing process",
      "type": "billing_frequency",
      "customizable": true
    },
    {
      "element": "Rate changes require documentation or email cc to Tabs for confirmation",
      "type": "change_management",
      "customizable": true
    },
    {
      "element": "Implementation POC and CX POC fields to be filled",
      "type": "contact_information",
      "customizable": true
    },
    {
      "element": "Integration item labeling instructions (merchant-specific examples provided)",
      "type": "integration_configuration",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements (who, where, when)",
      "type": "communication_protocol",
      "customizable": true
    }
  ],
  "confidence_score": 0.88
}
```

---

