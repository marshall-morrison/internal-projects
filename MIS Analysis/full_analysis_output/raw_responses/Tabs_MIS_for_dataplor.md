# Raw LLM Analysis: Tabs MIS for dataplor

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:24:07

---

## Chunk 1: Tabs MIS for dataplor_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:07

### Original Content
```
id 3900800531128878533 Custom Demo with Slater and Helen: https: us-56595 app gong io call id 2958238626902269142 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Mostly flat fees negotiated with large clients Sometimes bill a bundled amount, sometimes bill by line items Invoicing schedules and revenue schedules are sometimes divorced, ie billing for 24 months of service but providing 30 months of service, etc 1) What is the merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing complexity",
    "Revenue recognition and contract processing",
    "Client relationship management and merchant temperament",
    "Disconnect between invoicing schedules and revenue schedules",
    "ARR reporting and financial accuracy"
  ],
  "rules": [
    "Merchant uses mostly flat fees negotiated with large clients",
    "Billing can be structured as bundled amounts or itemized by line items",
    "Invoicing schedules and revenue schedules can be divorced (e.g., billing for 24 months while providing 30 months of service)",
    "Contract processing is required for both billing and revenue recognition",
    "Revenue recognition and ARR reporting must be corrected and maintained going forward"
  ],
  "exceptions": [
    "Invoicing period may not match service delivery period (e.g., 24-month billing for 30-month service)",
    "Billing structure varies by client: some receive bundled amounts, others receive line-item breakdowns",
    "Fee structure is negotiated on a per-client basis rather than standardized"
  ],
  "merchant_specific": [
    "Merchant contacts: Slater and Helen (with Slater expecting a new baby)",
    "Merchant temperament: competent but exhausted with implementation workload",
    "Merchant described as 'straight shooters' and collaborative",
    "Primary concern: contract processing for billing and revenue recognition",
    "Specific need: fixing and improving revenue recognition and ARR reporting accuracy",
    "Custom demo reference: Gong call ID 2958238626902269142",
    "Merchant ID: 3900800531128878533"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Tabs MIS for dataplor_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:24:21

### Original Content
```
Merchant Name Dataplor Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) If the contract looks like the screenshot below, follow the steps, use the red font as a gui...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Data Extraction",
    "Billing Configuration and Terms",
    "Customer Management and Hierarchy",
    "Default Values and Fallback Rules",
    "Post-Processing Communication and Workflows"
  ],
  "rules": [
    {
      "rule": "Service Start Date for standard contracts uses the order effective date",
      "category": "Contract Processing"
    },
    {
      "rule": "Quantity defaults to 1 for all line items",
      "category": "Billing Configuration"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Default Values"
    },
    {
      "rule": "Default Net Payment Terms is 0 days if none specified",
      "category": "Default Values"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Default Values"
    },
    {
      "rule": "Every tax line item becomes a separate BT (Billing Type) Events item by default",
      "category": "Tax Processing"
    },
    {
      "rule": "Different locations of the same customer are treated as separate sub-customers",
      "category": "Customer Management"
    },
    {
      "rule": "Customer mapping must reflect correct location by creating or assigning subcustomer",
      "category": "Customer Management"
    },
    {
      "rule": "Item Description must include countries, territories, or geographic scope listed in contract",
      "category": "Contract Processing"
    },
    {
      "rule": "For multi-year contracts, recognize each billing term separately (e.g., Year 1, Year 2)",
      "category": "Billing Configuration"
    },
    {
      "rule": "Use individual year prices, not total contract price, for multi-year agreements",
      "category": "Billing Configuration"
    },
    {
      "rule": "Year 2 start date is typically 1 year after initial start date unless contract specifies otherwise",
      "category": "Contract Processing"
    },
    {
      "rule": "Periods default to 1 for most contracts",
      "category": "Billing Configuration"
    },
    {
      "rule": "Billing frequency and periods must be verified against contract terms (yearly vs monthly vs one-time)",
      "category": "Contract Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "If EXHIBIT date exists, use that as Service Start Date instead of order effective date",
      "condition": "Presence of EXHIBIT date in contract"
    },
    {
      "exception": "Term end date based on subscription date when EXHIBIT date is used",
      "condition": "EXHIBIT date scenario",
      "example": "May 5th, 2023 - December 27th, 2025"
    },
    {
      "exception": "Merchant may request specific processing variations like back-dating invoice dates to final day of month",
      "condition": "Merchant-specific requests"
    },
    {
      "exception": "Integration items may have specific labeling requirements that differ from defaults",
      "condition": "Merchant-specific integration item rules",
      "examples": ["Statsig items labeled as 'Sales'", "Pinata items labeled as 'Software Subscription Bundle'"]
    },
    {
      "exception": "Some contracts may have one-time charges instead of recurring billing",
      "condition": "Contract specifies one-time payment"
    },
    {
      "exception": "Special memos may be required on certain invoices based on merchant-customer relationship",
      "condition": "Specific customer requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model section",
      "customization": "Implementation team fills unique customer creation process and billing structure per merchant"
    },
    {
      "element": "Contract template types",
      "customization": "Different processing steps for 'Order Template of Data Services and Fees' vs 'REPRESENTATIONS contract'",
      "examples": ["Garage example templates"]
    },
    {
      "element": "Integration Items labeling",
      "customization": "Merchant-specific rules for categorizing integration items",
      "requires": "Post-go-live documentation by Implementation Success team"
    },
    {
      "element": "Post-processing notifications",
      "customization": "Merchant-specific communication requirements including who to notify, where, and when",
      "example": "Customer Success [Azmat Aziz] notification in Messari internal merchant channel"
    },
    {
      "element": "Customer Information section",
      "customization": "Special handling for specific customers, invoice memo requirements, relationship-based invoice changes"
    },
    {
      "element": "Contract processing specifics",
      "customization": "Merchant may request deviations like invoice date back-dating rules"
    },
    {
      "element": "POC assignments",
      "customization": "Implementation POC and CX POC vary by merchant (Dataplor example shown)"
    },
    {
      "element": "Feature Requests tracking",
      "customization": "Merchant-specific feature requests with urgency and importance ratings"
    },
    {
      "element": "Items to ignore in contracts",
      "customization": "Merchant-specific guidance on what contract elements to exclude from processing"
    }
  ],
  "confidence_score": 0.92
}
```

---

