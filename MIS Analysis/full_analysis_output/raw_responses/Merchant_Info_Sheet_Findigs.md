# Raw LLM Analysis: Merchant Info Sheet - Findigs

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:18:03

---

## Chunk 1: Merchant Info Sheet - Findigs_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:03

### Original Content
```
Findigs Scoping start date: Oct 13, 2023 Implementation Completed Date (Go live date): May 10, 2024 MSA Signature Date: Feb 15, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Head of Finance: Sebastian Hart Primary PoC and Decision Maker Finance Associate: Ellie Barney We re replacing the manual work she used to have to do Engineering: Parth Company summary  Findigs makes renting safe and easy for renters and property managers Rent units faster with zero fraud Our...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Key Dates",
    "Billing and Remittance Processing Workflow",
    "Stakeholder Management and Communication",
    "Monthly Usage-Based Event Processing",
    "Custom Remittance Workflow Development"
  ],
  "rules": [
    {
      "rule": "Monthly billing processed in arrears based on usage events",
      "category": "billing",
      "specificity": "explicit"
    },
    {
      "rule": "Events processing occurs as part of end-of-month flow",
      "category": "processing_schedule",
      "specificity": "explicit"
    },
    {
      "rule": "Usage data must be broken down by Property Manager in each row",
      "category": "data_format",
      "specificity": "explicit"
    },
    {
      "rule": "Deepak pipeline creates one-off billing terms for Findigs",
      "category": "billing_setup",
      "specificity": "explicit"
    },
    {
      "rule": "Ops team must confirm remittance amounts are accurate before processing",
      "category": "quality_control",
      "specificity": "explicit"
    },
    {
      "rule": "Calculate total remittance by combining QBO Vendor ID (column: total_remittance_to_portfolio, column AH)",
      "category": "calculation_method",
      "specificity": "explicit"
    },
    {
      "rule": "Generic contract sample must be uploaded as prerequisite to generating billing terms events",
      "category": "prerequisites",
      "specificity": "explicit"
    },
    {
      "rule": "Finance Associate (Ellie Barney) can request updates or changes to remittance amounts",
      "category": "authorization",
      "specificity": "explicit"
    },
    {
      "rule": "Deepak should be contacted to update remittance amounts when changes are needed",
      "category": "process",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Acceptable to push processing to next month if needed (after 4-5 events processed in May)",
      "condition": "Volume threshold reached",
      "context": "Processing flexibility"
    },
    {
      "exception": "Remittance amounts can be updated or changed at Ellie's request",
      "condition": "Finance Associate approval",
      "context": "Post-calculation adjustments allowed"
    },
    {
      "exception": "No formal contracts provided by client (using generic sample instead)",
      "condition": "Client-specific arrangement",
      "context": "Contract documentation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Remittance workflow built entirely from scratch for this merchant",
      "type": "custom_workflow",
      "note": "Not a standard implementation"
    },
    {
      "element": "Property Manager breakdown in usage data rows",
      "type": "data_structure",
      "note": "Specific to Findigs' business model (property management platform)"
    },
    {
      "element": "Key contacts: Sebastian Hart (Head of Finance), Ellie Barney (Finance Associate, Primary PoC)",
      "type": "stakeholders",
      "note": "Merchant-specific personnel"
    },
    {
      "element": "QBO Vendor ID used for remittance calculation",
      "type": "system_integration",
      "note": "QuickBooks Online integration specific to this merchant"
    },
    {
      "element": "Column AH (total_remittance_to_portfolio) for remittance totals",
      "type": "data_mapping",
      "note": "Merchant-specific spreadsheet structure"
    },
    {
      "element": "Findigs Usage Data file format (example: April usage file)",
      "type": "data_format",
      "note": "Custom usage reporting format"
    },
    {
      "element": "Business context: Digital underwriting platform for rental applications",
      "type": "business_model",
      "note": "Informs billing structure and event types"
    }
  ],
  "confidence_score": 0.82
}
```

---

