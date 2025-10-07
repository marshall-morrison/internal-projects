# Raw LLM Analysis: Merchant Info Sheet - Red Antler(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:11:07

---

## Chunk 1: Merchant Info Sheet - Red Antler(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:11:07

### Original Content
```
indMerchant Scoping start date: N A Implementation Completed Date (Go live date): N A MSA Signature Date: Mar 31, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Mike Lawrence CFO: Rich Pacheco Company summary Red Antler LLC provides marketing services The Company offers research, branding, naming, digital designing, engineering, and advertising services Billing model  --- For RED ANTLER Contract Processing Steps For renewal contracts, process all BTs under the renewal con...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Management",
    "Revenue Schedule Configuration",
    "Customer and GL Account Management",
    "Invoice Line Item Naming and Description Standards",
    "Integration Item Mapping and Classification"
  ],
  "rules": [
    "For renewal contracts, process all billing terms under the renewal contract",
    "Contracts with Sent/Paid invoices cannot have their billing terms changed",
    "New edits, additions, or requests from merchant must go on entirely new contract with separate invoice",
    "When seeing a sent invoice in Garage, ask US team to duplicate the contract for new billing terms",
    "Revenue schedule must be set to 12 months",
    "Billing cadence is based on contract dates",
    "Payment terms must be set to Net 0",
    "GL must be connected - search for existing customer in dropdown first",
    "For duplicate customer names, use customer ID associated with Red Antler merchant",
    "If no customers found, create a Tabs customer",
    "For project fees, use project name as item name (flag US team if not available)",
    "For Out of Pocket Expenses, use 'Out of Pocket Expense' as item name",
    "For project fees, item description must specify 'Invoice X of Y' format",
    "Client Fees must use 'Professional Fees' integration item",
    "Out of Pocket must use 'Pass Through Expense' integration item",
    "Do NOT use 'Client Deposit' - deposit-related items are 'Professional Fees'",
    "Use dates from contract when available",
    "Add Product Name field from email to product description in invoice line item"
  ],
  "exceptions": [
    "When dates not available but says 'estimate completion in Q4 2024', use first date of the quarter",
    "When dates not available but says 'estimate completion in a specific month', use first date of the quarter",
    "For milestone-based projects, process with placeholder dates (stakeholder can change later)",
    "If unsure about customer selection with duplicates, flag Ops Team Chirag Manyapu"
  ],
  "merchant_specific": [
    "Merchant name: Red Antler LLC",
    "Key contacts: Mike Lawrence (Accountant), Rich Pacheco (CFO)",
    "MSA Signature Date: Mar 31, 2024",
    "Company provides marketing services (research, branding, naming, digital designing, engineering, advertising)",
    "Specific customer ID association requirement for Red Antler merchant",
    "US team involvement for contract duplication and flagging",
    "Ops Team contact: Chirag Manyapu",
    "Garage system usage for contract and customer management",
    "Tabs customer creation requirement",
    "12-month revenue schedule standard",
    "Net 0 payment terms standard"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Red Antler(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:11:17

### Original Content
```
Example Contract: a3f5017e-184f-49a8-aaa0-c8aa6f2abde4 (No action required, this is just for illustration) The "Project Name" field is "Daydream   SOW1 Brand   Marketing" RA 273 128bcd76-b466-42cc-a8c1-49d315d5a0b4 would then read "Agency Fees - Daydream SOW1 Brand   Marketing" for the line item on the invoice Project Creation Workflow In order to create a project, we need a few of the following data fields First navigate to Garage Secrets https: garage tabsplatform com prod secrets Use Super Po...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Creation and Configuration Workflow",
    "Data Field Requirements and Naming Conventions",
    "ID Mapping and Reference Systems",
    "Communication and Notification Protocols",
    "Red Antler Specific Invoicing Process"
  ],
  "rules": [
    {
      "rule": "Project naming convention must follow format: 'SOW #X: PROJECT NAME'",
      "source": "Naming convention section",
      "type": "formatting"
    },
    {
      "rule": "Invoice line items must read 'Agency Fees - [Project Name]' where Project Name matches the contract",
      "source": "Example Contract section",
      "type": "invoicing"
    },
    {
      "rule": "Project Type ID options: internal=1, client non billable=2, client billable-oop=3, client billable-fee=4",
      "source": "Project Type ID section",
      "type": "classification"
    },
    {
      "rule": "Business Type ID options: organic=1 (Typically SOW #2 or greater), new business=2 (Typically SOW #1)",
      "source": "Business Type ID section",
      "type": "classification"
    },
    {
      "rule": "Client Stage ID options: pre-launch=1, early=2, growth=3, coop=4, non-billable=5",
      "source": "Client Stage ID section",
      "type": "classification"
    },
    {
      "rule": "Budget Fee must be entered as numeric value with dollar sign removed",
      "source": "Budget Fee section",
      "type": "data_entry"
    },
    {
      "rule": "Must navigate to Garage Secrets (https://garage.tabsplatform.com/prod/secrets) to create projects",
      "source": "Project Creation Workflow",
      "type": "process"
    },
    {
      "rule": "Use 'Create Red Antler Project' Super Power for project creation",
      "source": "Project Creation Workflow",
      "type": "process"
    },
    {
      "rule": "Merchant ID and Customer ID must be obtained via Garage",
      "source": "Project Creation Workflow",
      "type": "data_sourcing"
    },
    {
      "rule": "Project Name is available from the contract email",
      "source": "Project Name section",
      "type": "data_sourcing"
    },
    {
      "rule": "Client Director ID must be obtained via NetSuite Red Antler Client Director IDs",
      "source": "Client Director ID section",
      "type": "data_sourcing"
    },
    {
      "rule": "Reach out to Royce for Client Director NS internal IDs (interim process)",
      "source": "Client Director ID section",
      "type": "process"
    },
    {
      "rule": "Project Manager ID should be ignored during project creation",
      "source": "Project Manager ID section",
      "type": "process"
    },
    {
      "rule": "Returned Project ID must be mapped to specific contract using super power",
      "source": "Project ID return section",
      "type": "process"
    },
    {
      "rule": "Ops must send slack bot notifications once processed",
      "source": "Communication Workflow",
      "type": "notification"
    },
    {
      "rule": "Create excel spreadsheet to track Client Director NS internal IDs",
      "source": "Client Director ID section",
      "type": "documentation"
    }
  ],
  "exceptions": [
    {
      "exception": "SOW #1 typically indicates 'new business' (Business Type ID = 2)",
      "condition": "First Statement of Work"
    },
    {
      "exception": "SOW #2 or greater typically indicates 'organic' business (Business Type ID = 1)",
      "condition": "Subsequent Statements of Work"
    },
    {
      "exception": "Events Processing may be required for certain projects with special billing considerations",
      "condition": "When events are involved"
    },
    {
      "exception": "Special memos may be required for certain invoices",
      "condition": "Based on merchant-customer relationship"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship",
      "condition": "Specific merchant-customer dynamics"
    },
    {
      "exception": "Interim process requires reaching out to Royce for Client Director IDs",
      "condition": "Until permanent process is established"
    }
  ],
  "merchant_specific": [
    {
      "element": "Red Antler specific project creation process",
      "description": "Entire workflow is customized for Red Antler merchant",
      "customizable": false
    },
    {
      "element": "Contract reference format (RA 273 followed by UUID)",
      "description": "Red Antler specific contract numbering system",
      "customizable": true
    },
    {
      "element": "Client Director IDs from NetSuite",
      "description": "Red Antler maintains specific client director mappings",
      "customizable": true
    },
    {
      "element": "Project naming with 'SOW #X' format",
      "description": "Red Antler uses Statement of Work numbering",
      "customizable": true
    },
    {
      "element": "Account classification as 'Larger/Enterprise account' with ACV >40k",
      "description": "Red Antler is classified as enterprise tier",
      "customizable": false
    },
    {
      "element": "Specific contact person (Royce) for Client Director IDs",
      "description": "Red Antler has designated internal contact",
      "customizable": true
    },
    {
      "element": "Invoice line item format: 'Agency Fees - [Project Name]'",
      "description": "Red Antler specific invoicing terminology using 'Agency Fees'",
      "customizable": true
    },
    {
      "element": "Customer-specific information tracking requirements",
      "description": "Red Antler requires tracking of specific customer information and special memos",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

