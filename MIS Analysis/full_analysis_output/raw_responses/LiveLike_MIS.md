# Raw LLM Analysis: LiveLike MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:02:32

---

## Chunk 1: LiveLike MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:02:32

### Original Content
```
Default to 30 if not found Default Billing Frequency Found within payment schedule in contract How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Waiting on merchant to fill out this sheet: LiveLike   Integration Items If still blank at time of pro...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Configuration and Fallback Values",
    "Tax and Line Item Processing",
    "Integration and Implementation Workflow",
    "Post-Processing Communication Protocols",
    "Merchant Relationship Management and Customer Intelligence"
  ],
  "rules": [
    {
      "rule": "Default billing frequency to 30 days if not found in payment schedule",
      "category": "billing_configuration",
      "explicit": true
    },
    {
      "rule": "Billing frequency should be found within payment schedule in contract",
      "category": "data_extraction",
      "explicit": true
    },
    {
      "rule": "When no tax handling instructions are listed, default every tax line item to BT (Billable Tax)",
      "category": "tax_processing",
      "explicit": true
    },
    {
      "rule": "Integration items assignment requires merchant to fill out specific sheet (LiveLike Integration Items)",
      "category": "integration_setup",
      "explicit": true
    },
    {
      "rule": "If integration items sheet is blank at processing time, Implementation team handles it",
      "category": "integration_setup",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore sections marked for AE Implementation",
      "category": "team_responsibilities",
      "explicit": true
    },
    {
      "rule": "Customer Success must be notified in merchant internal channel when contracts are processed in Active phase",
      "category": "communication_protocol",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "condition": "Integration items sheet still blank at time of processing",
      "action": "Implementation team will handle post-processing",
      "context": "integration_setup"
    },
    {
      "condition": "Special memo requirements for certain invoices",
      "action": "Apply customer-specific invoice modifications",
      "context": "customer_information"
    },
    {
      "condition": "Invoice changes due to merchant-customer relationship",
      "action": "Apply relationship-based adjustments",
      "context": "customer_information"
    },
    {
      "condition": "Usage-based billing (impressions and clicks)",
      "action": "Each contract is different - monthly, quarterly, yearly variations",
      "context": "billing_model"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant temperament profile",
      "example": "Lawrence is very nice, a little bit of an ego, wears a lot of hats at LiveLike",
      "purpose": "relationship_management"
    },
    {
      "element": "Key POC identification",
      "example": "Lawrence as buyer/decision maker",
      "purpose": "stakeholder_management"
    },
    {
      "element": "Feature priorities per merchant",
      "example": "Automatic contract ingestion, Automatically apply usage to invoices",
      "purpose": "product_customization"
    },
    {
      "element": "Billing model specifics",
      "example": "Usage based on impressions and clicks, varying contract terms",
      "purpose": "billing_configuration"
    },
    {
      "element": "Integration items sheet",
      "example": "LiveLike Integration Items",
      "purpose": "technical_integration"
    },
    {
      "element": "Customer-specific invoice requirements",
      "example": "Special memos, relationship-based changes",
      "purpose": "invoice_customization"
    },
    {
      "element": "Notification recipients",
      "example": "Customer Success [Azmat Aziz]",
      "purpose": "communication_routing"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: LiveLike MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:02:32

### Original Content
```
Merchant Demo date:   Scoping start date: Oct 17, 2024 MSA Signature Date: Nov 15, 2024 Onboarding Kick Off Date: Nov 25, 2024 [If Exists] Opt Out Date: NA Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Ryan Muckey CFO: Lawrence Chan Company summary (AE to fill) LiveLike allows you to add interactive widgets to your content to improve engagement and provide insights into viewers behavior Ex Yahoo sports uses livelike during monday ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Timeline and Milestone Management",
    "Revenue Automation and Billing Configuration",
    "Contract Processing Workflow and Data Extraction",
    "Customer and Event Setup Requirements",
    "Service Terms and Payment Terms Configuration"
  ],
  "rules": [
    "Customers should be ingested from Netsuite; if not found, create in Garage with merchant populating billing contact info",
    "Use Contractual Term for start and end dates",
    "If no start date in Contractual Term, use Effective Date as fallback",
    "Billing terms are found in 'Financial Terms and Payment Schedule' section and Section 3 Support Services",
    "Fee type column on the left is used for item name",
    "Tier information (e.g., Silver) should be input as description where applicable",
    "Events should be pre-created for usage-based billing terms; if not found, create event in merchant app",
    "Ignore anything marked as 'optional' (e.g., Optional Upgrade)",
    "Ignore anything under 'Rate Card for Optional Add-on Services'",
    "Default Service Term is found in 'Order Term' at top of contract",
    "Service period should tie back to duration of billing term",
    "For multi-year contracts with annual price increases, each Revenue Schedule (RS) in Garage should spread revenue across 12-month period",
    "Default Net Payment Terms are found in Section 4 Payment Terms",
    "Billing frequency for this merchant is quarterly"
  ],
  "exceptions": [
    "If contract has price increases by year (e.g., 3-year contract with yearly increases), create separate Revenue Schedules for each 12-month period rather than one schedule for entire contract duration",
    "Optional items and add-on services from rate cards should be excluded from standard contract processing",
    "Merchant may request specific processing variations that differ by contract (example given: back-dating invoice date to final day of month)"
  ],
  "merchant_specific": [
    "Merchant Name: LiveLike",
    "Business Model: Interactive widgets for content engagement (B2B SaaS)",
    "Key Personnel: Ryan Muckey (Accountant), Lawrence Chan (CFO)",
    "Timeline: Demo date unknown, Scoping Oct 17 2024, MSA Nov 15 2024, Kickoff Nov 25 2024, Go Live Jan 1 2025",
    "No opt-out clause exists for this merchant",
    "ERP System: Netsuite (implied from customer ingestion source)",
    "Billing Frequency: Quarterly",
    "Customer creation process: Standard (no unique requirements noted)",
    "Billing varies by customer",
    "Reference to GOTHAM and LIV contracts as processing examples",
    "Merchant uses 'Garage' as the platform/system name for contract management",
    "Pain Points: Need for integrated revenue automation, contract term extraction, usage calculation automation, comprehensive commercial graph for reporting and revenue recognition"
  ],
  "confidence_score": 0.85
}
```

---

