# Raw LLM Analysis: MIS for Astranis

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:52:49

---

## Chunk 1: MIS for Astranis_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:49

### Original Content
```
Given the long build cycle for satellites (12 24 months), billing is often tied to milestones such as build phases, delivery, or service commencement, rather than a recurring monthly cadence 1) What is the merchant temperament Astranis  temperament was engaged, curious, and collaborative They were consistently open in sharing context, quick to give feedback, and willing to dive into technical details with our team They came across as thoughtful and methodical asking good questions, seeking to fu...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Milestone-based billing for long-cycle products",
    "Deferred revenue and revenue recognition automation",
    "NetSuite ERP integration requirements",
    "Merchant engagement and collaboration style",
    "Automated invoice generation and accounting workflows"
  ],
  "rules": [
    {
      "rule": "Billing must be tied to milestones (build phases, delivery, service commencement) rather than recurring monthly cadence",
      "context": "Applies to products with long build cycles (12-24 months), specifically satellites"
    },
    {
      "rule": "Invoices must flow through a single deferred revenue or revenue clearing account",
      "context": "Invoice generation workflow requirement"
    },
    {
      "rule": "System must provide flexibility to post directly to revenue when needed",
      "context": "Alternative to deferred revenue posting"
    },
    {
      "rule": "Revenue recognition journal entries must be generated monthly",
      "context": "Automated rev rec process"
    },
    {
      "rule": "Revenue recognition entries must be auditable and align with merchant's accounting rules",
      "context": "Compliance and accounting standards requirement"
    },
    {
      "rule": "Journal entries and invoices must post directly into NetSuite",
      "context": "ERP integration requirement"
    },
    {
      "rule": "Integration must minimize manual intervention",
      "context": "Automation and efficiency requirement"
    }
  ],
  "exceptions": [
    {
      "exception": "Option to bypass deferred revenue account and post directly to revenue",
      "condition": "When flexibility is needed for specific transactions"
    },
    {
      "exception": "Non-standard billing cadence",
      "condition": "For products with 12-24 month build cycles, milestone-based billing replaces standard recurring billing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Build cycle duration",
      "value": "12-24 months for satellites",
      "customization_needed": "Other merchants may have different product build cycles"
    },
    {
      "element": "Milestone definitions",
      "value": "Build phases, delivery, service commencement",
      "customization_needed": "Milestone types and timing will vary by merchant and product type"
    },
    {
      "element": "ERP system",
      "value": "NetSuite",
      "customization_needed": "Different merchants use different ERP systems (QuickBooks, SAP, Oracle, etc.)"
    },
    {
      "element": "Merchant temperament",
      "value": "Engaged, curious, collaborative, methodical",
      "customization_needed": "Communication style and engagement level varies by merchant"
    },
    {
      "element": "Revenue recognition rules",
      "value": "Specific to long-term contracts and milestone-based delivery",
      "customization_needed": "Rev rec rules vary based on industry, contract structure, and accounting standards (ASC 606, etc.)"
    },
    {
      "element": "Account structure",
      "value": "Deferred revenue/revenue clearing account preference",
      "customization_needed": "Chart of accounts and accounting methodology varies by merchant"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: MIS for Astranis_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:50

### Original Content
```
Merchant Name: Astranis Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant h...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters and Overrides",
    "Post-Processing Communication and Notifications",
    "Merchant-Specific Billing Models and Revenue Recognition",
    "Cross-Functional Responsibility Assignment (AE, Implementation, Success Teams)"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed in contract",
      "category": "billing_defaults"
    },
    {
      "rule": "Default net payment terms is 0 days if none specified",
      "category": "billing_defaults"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "tax_handling"
    },
    {
      "rule": "Implementation Success team fills contract processing steps post-go-live",
      "category": "responsibility_assignment"
    },
    {
      "rule": "AE fills feature requests prior to implementation handoff",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) on handoff for notes sections",
      "category": "responsibility_assignment"
    },
    {
      "rule": "Integration items must be properly labeled according to merchant specifications",
      "category": "integration_processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Astranis uses recurring billing that is milestone-driven rather than high-volume subscription or usage billing",
      "context": "merchant_specific_billing"
    },
    {
      "exception": "Astranis has 1 contract = 1 satellite model (bespoke deliverables)",
      "context": "merchant_specific_billing"
    },
    {
      "exception": "Astranis has no standard seasonality or high transaction volume",
      "context": "merchant_specific_billing"
    },
    {
      "exception": "Astranis revenue recognition books invoicing to deferred revenue first, then reclasses monthly as revenue is recognized",
      "context": "revenue_recognition"
    },
    {
      "exception": "Contract-specific processing may differ (e.g., always back-date invoice date to final day of the month)",
      "context": "contract_processing_variations"
    },
    {
      "exception": "Success measured in small number of annual contracts (e.g., 12 contracts per year considered successful)",
      "context": "merchant_volume_expectations"
    }
  ],
  "merchant_specific": [
    {
      "element": "POC fields (Implementation POC, CX POC)",
      "customization_type": "contact_information"
    },
    {
      "element": "Billing model description",
      "customization_type": "billing_configuration"
    },
    {
      "element": "Contract processing steps and specifics",
      "customization_type": "operational_procedures"
    },
    {
      "element": "Events processing requirements",
      "customization_type": "billing_configuration"
    },
    {
      "element": "Integration items labeling rules (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "customization_type": "integration_mapping"
    },
    {
      "element": "Post-processing notification requirements (who, where, when)",
      "customization_type": "communication_workflow"
    },
    {
      "element": "Customer-specific information (special memos, invoice changes)",
      "customization_type": "customer_handling"
    },
    {
      "element": "Feature requests tracking",
      "customization_type": "product_requirements"
    },
    {
      "element": "Merchant call notes and recordings",
      "customization_type": "documentation"
    },
    {
      "element": "Revenue recognition model (deferred revenue to monthly recognition)",
      "customization_type": "accounting_treatment"
    }
  ],
  "confidence_score": 0.85
}
```

---

