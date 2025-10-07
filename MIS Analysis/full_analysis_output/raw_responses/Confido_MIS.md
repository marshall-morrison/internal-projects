# Raw LLM Analysis: Confido MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:33:08

---

## Chunk 1: Confido MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:33:08

### Original Content
```
io call id 527527815851812189 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) This is a very basic deal, maybe the simplest merchant i ve ever closed Very straightforward contracts, the simplest OF i ve seen Very early stage, just closed Series A Info on how merchant bills: Tech Stack: QBO as ERP HubSpot as CRM Manual Invoicing Process Founder is creating invoices in QBO manually 1) What is the merchant temperament Justin is very straightforward, he is a ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant onboarding and handoff process",
    "Technical infrastructure and billing systems",
    "Stakeholder management and communication",
    "Product feature alignment and value proposition",
    "Deal complexity and implementation scope"
  ],
  "rules": [
    "Notes sections must be filled by AE if available, with Implementation as DRI on handoff",
    "Document merchant temperament as part of onboarding process",
    "Identify and document key POC (Point of Contact) preferences",
    "Record merchant's tech stack including ERP and CRM systems",
    "Document current invoicing process and workflow",
    "Capture information on how merchant bills customers",
    "Identify which Tabs features are important to key stakeholders"
  ],
  "exceptions": [
    "Very basic/simple deals may have streamlined contracts (simplest OF mentioned)",
    "Early stage companies (e.g., just closed Series A) may have simpler requirements",
    "Manual invoicing processes indicate need for automation focus",
    "International team members (e.g., EA in Philippines) may require special communication considerations"
  ],
  "merchant_specific": [
    "Merchant temperament varies (founder-led vs corporate structure)",
    "Tech stack components (QBO, HubSpot, or alternatives)",
    "Invoicing process methodology (manual vs automated)",
    "Key stakeholder roles and locations (founder, EA, geographic distribution)",
    "Feature priorities differ by merchant (automation focus in this case)",
    "Deal complexity levels vary significantly between merchants",
    "Contract complexity can range from very simple to complex"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Confido MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:33:16

### Original Content
```
Merchant Name: Confido Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant ha...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters",
    "Merchant-Specific Customization and Implementation",
    "Post-Processing Communication Protocols",
    "Integration and Event Management"
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
      "rule": "Implementation Success team fills sections post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "AE fills feature requests prior to implementation handoff",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation team fills merchant calls and feature requests prior to go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    },
    {
      "rule": "Success team fills feature requests and merchant calls post-go-live",
      "category": "responsibility_assignment",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations (e.g., always back-date invoice date to final day of the month)",
      "condition": "Merchant-requested specifics that may differ by contract",
      "impact": "Overrides standard processing procedures"
    },
    {
      "exception": "Certain contracts may have items to ignore during processing",
      "condition": "Specified by merchant requirements",
      "impact": "Selective processing of contract elements"
    },
    {
      "exception": "Integration items may have special labeling requirements",
      "condition": "Depends on integration type (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "impact": "Custom categorization per integration vendor"
    },
    {
      "exception": "Special memos or invoice changes may be required for specific customers",
      "condition": "Based on merchant-customer relationship",
      "impact": "Customer-specific invoice customization"
    }
  ],
  "merchant_specific": [
    {
      "element": "POC contacts (Implementation POC and CX POC)",
      "customization_type": "contact_information",
      "requires_merchant_input": true
    },
    {
      "element": "Billing model and contract structure",
      "customization_type": "billing_configuration",
      "requires_merchant_input": true
    },
    {
      "element": "Customer creation process uniqueness",
      "customization_type": "operational_process",
      "requires_merchant_input": true
    },
    {
      "element": "Contract processing steps and specifications",
      "customization_type": "processing_workflow",
      "requires_merchant_input": true
    },
    {
      "element": "Events billing procedures",
      "customization_type": "billing_configuration",
      "requires_merchant_input": true
    },
    {
      "element": "Integration items labeling and assignment",
      "customization_type": "categorization_rules",
      "requires_merchant_input": true
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "communication_protocol",
      "requires_merchant_input": true,
      "example": "Customer Success notification in merchant channel when contracts processed"
    },
    {
      "element": "Customer-specific information and invoice requirements",
      "customization_type": "customer_management",
      "requires_merchant_input": true
    },
    {
      "element": "Feature requests tracking",
      "customization_type": "product_requirements",
      "requires_merchant_input": true
    },
    {
      "element": "Merchant call recordings and documentation",
      "customization_type": "communication_history",
      "requires_merchant_input": true
    }
  ],
  "confidence_score": 0.92
}
```

---

