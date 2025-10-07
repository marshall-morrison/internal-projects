# Raw LLM Analysis: Copy of Torch Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:01:59

---

## Chunk 1: Copy of Torch Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:01:59

### Original Content
```
Merchant Demo date: June 8th 2024 Scoping start date: Jul 24, 2024 MSA Signature Date: Aug 15, 2024 Onboarding Kick Off Date: Aug 22, 2024 [If Exists] Opt Out Date: n a Go Live Date: Oct 2, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Jeff Nichols Controller anthony torch io   Good thought partner on implementation   Decision Making Sr Accountant: katie torch io   approves the contract, review the contract Jr Accountant: jonathan torch io   mana...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Roles and Responsibilities",
    "System Integration and Feature Requests",
    "Invoice and Payment Terms Management"
  ],
  "rules": [
    {
      "rule": "Use LAST signature date, not contract start date for processing",
      "category": "Date Processing",
      "explicit": true
    },
    {
      "rule": "Do not process discounts as a BT (Billing Transaction), use only net BT amounts",
      "category": "Discount Handling",
      "explicit": true
    },
    {
      "rule": "Pro-rate discounts based on the ratio of amounts associated with each BT",
      "category": "Discount Handling",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 30 days if none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "No taxes in the interim - do not need to worry about taxes as line items",
      "category": "Tax Handling",
      "explicit": true
    },
    {
      "rule": "Add PO (Purchase Order ID) as stated in contract in the invoices tab",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Invoice Date should be based on last signature date on the order form",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Period can be the contract start date to end date from the order form",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Include short description and all details text in the second column for items",
      "category": "Item Processing",
      "explicit": true
    },
    {
      "rule": "Include quantity as displayed in the contract",
      "category": "Item Processing",
      "explicit": true
    },
    {
      "rule": "For new merchants, add both invoicing and shipping address",
      "category": "Address Management",
      "explicit": true
    },
    {
      "rule": "Process Service Term as noted in contract",
      "category": "Contract Terms",
      "explicit": true
    },
    {
      "rule": "Process Billing Frequency as stated in the contract",
      "category": "Billing Configuration",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "No events billing required for this merchant",
      "context": "Events Processing section indicates not applicable"
    },
    {
      "exception": "Opt Out Date is marked as 'n a' (not applicable)",
      "context": "Timeline dates"
    },
    {
      "exception": "Nothing to ignore in contracts (N/A specified)",
      "context": "Contract processing"
    },
    {
      "exception": "Ops International Team should ignore certain sections",
      "context": "AE Implementation Notes sections marked for exclusion"
    }
  ],
  "merchant_specific": [
    {
      "element": "Torch Item Mapping spreadsheet",
      "type": "Integration mapping",
      "description": "Custom item mapping for Torch merchant"
    },
    {
      "element": "Key stakeholders with specific roles",
      "type": "Personnel",
      "description": "CFO Jeff Nichols, Controller Anthony, Sr Accountant Katie, Jr Accountant Jonathan, Adam for CRM integration"
    },
    {
      "element": "Business goal: Downsize NetSuite bill",
      "type": "Business objective",
      "description": "Replacing ARM modules and Celigo integration to reduce errors and costs"
    },
    {
      "element": "Feature Request 1: SalesForce Integration",
      "type": "Integration requirement",
      "description": "CRM data to NetSuite, urgency October, DRI: Royce Kok/Deepak Bapat"
    },
    {
      "element": "Feature Request 2: Access controls and Permissions Banking",
      "type": "Security requirement",
      "description": "Custom access control needs"
    },
    {
      "element": "Feature Request 3: Approval Workflow",
      "type": "Workflow requirement",
      "description": "Conversation started with Jon on Tabs Team"
    },
    {
      "element": "Katie and Anthony audit background",
      "type": "Stakeholder context",
      "description": "Relevant for understanding their approach to financial processes"
    },
    {
      "element": "Torch slack channel and Rewatch Calls",
      "type": "Communication channels",
      "description": "Merchant-specific communication references"
    },
    {
      "element": "Company description: People development platform",
      "type": "Business context",
      "description": "Understanding merchant's business model"
    }
  ],
  "confidence_score": 0.92
}
```

---

