# Raw LLM Analysis: Merchant Info Sheet - Red Antler

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:16:37

---

## Chunk 1: Merchant Info Sheet - Red Antler_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:16:37

### Original Content
```
Merchant Scoping start date: N A Implementation Completed Date (Go live date): N A MSA Signature Date: Mar 31, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Mike Lawrence CFO: Rich Pacheco Company summary Red Antler LLC provides marketing services The Company offers research, branding, naming, digital designing, engineering, and advertising services Billing model  --- For RED ANTLER Contract Processing Steps For renewal contracts, process all BTs under the renewal contra...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Term Processing",
    "Customer Management and GL Integration",
    "Revenue Schedule Configuration",
    "Invoice Item Categorization and Naming",
    "Date Handling and Milestone-Based Projects"
  ],
  "rules": [
    "For renewal contracts, process all billing terms under the renewal contract",
    "Contracts with Sent/Paid invoices cannot have their billing terms changed",
    "New edits, additions, or requests from merchant must go on an entirely new contract and separate invoice",
    "When a sent invoice exists on the contact in garage, ask US team to duplicate the contract for new billing terms",
    "Revenue schedule must be set to 12 months",
    "Billing cadence is based on contract dates",
    "Amount is based upon the contract",
    "Payment terms are specified net terms, usually 15 or 30 days",
    "GL is connected - must search for existing customer in dropdown before creating new",
    "For duplicate customers with same name, go to customers tab in Garage and use customer ID associated with Red Antler merchant",
    "If unsure about customer selection, flag Ops Team Chirag Manyapu",
    "Before creating new customer, manually sync via Merchants > red antler > Sync Netsuite now and wait a few minutes",
    "For project fees, use the project name as item name (flag US team if not available)",
    "For Out of Pocket Expenses (OOP Fees), use 'Out of Pocket Expense' as item name",
    "For project fees, specify 'Invoice X of Y' in item description where X is sequence and Y is total number",
    "Client Fees must use 'Professional Fees' integration item",
    "Out of Pocket must use 'Pass Through Expense' integration item",
    "Do NOT use 'Client Deposit' - deposit-related items are still 'Professional Fees'",
    "Use dates from contract when available",
    "When dates not available but quarter mentioned (e.g., Q4 2024), use first date of the quarter",
    "When specific month mentioned for estimated completion, use first date of the quarter",
    "For milestone-based projects, process with placeholder dates that stakeholders can change",
    "Add 'Product Name' field from email to product description in line item of invoice"
  ],
  "exceptions": [
    "Contracts with Sent/Paid invoices require special handling - new contract must be created for any changes",
    "Duplicate customers require manual verification using customer ID in Garage",
    "When dates are not available, use quarter-based estimation rules",
    "Milestone-based projects use placeholder dates instead of exact dates",
    "Deposit-related items are an exception to normal categorization - they use 'Professional Fees' not 'Client Deposit'"
  ],
  "merchant_specific": [
    "Merchant name: Red Antler LLC",
    "Company provides marketing services including research, branding, naming, digital designing, engineering, and advertising",
    "Key contacts: Accountant Mike Lawrence, CFO Rich Pacheco",
    "MSA Signature Date: Mar 31, 2024",
    "Specific escalation contact: Ops Team Chirag Manyapu",
    "Specific sync path: Merchants > red antler > Sync Netsuite now",
    "Customer ID association specific to Red Antler merchant",
    "Two specific integration item options: 'Professional Fees' and 'Pass Through Expense'",
    "Specific payment terms: usually 15 or 30 days net",
    "Project-based and milestone-based billing model"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Red Antler_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:16:51

### Original Content
```
Example Contract: a3f5017e-184f-49a8-aaa0-c8aa6f2abde4 (No action required, this is just for illustration) The "Project Name" field is "Daydream   SOW1 Brand   Marketing" RA 273 128bcd76-b466-42cc-a8c1-49d315d5a0b4 would then read "Agency Fees - Daydream SOW1 Brand   Marketing" for the line item on the invoice Project Creation Workflow In order to create a project, we need a few of the following data fields First navigate to Garage Secrets https: garage tabsplatform com prod secrets Use Super Po...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Creation Workflow and Data Requirements",
    "Naming Conventions and Field Mapping",
    "Invoice Line Item Configuration",
    "ID Retrieval and System Integration (Garage, NetSuite)",
    "Communication and Documentation Protocols"
  ],
  "rules": [
    {
      "rule": "Project naming convention must follow format: 'SOW #X: PROJECT NAME'",
      "source": "Naming convention SOW X: PROJECT NAME"
    },
    {
      "rule": "Invoice line items must read 'Agency Fees - [Project Name]' where Project Name matches the contract",
      "source": "RA 273 128bcd76-b466-42cc-a8c1-49d315d5a0b4 would then read 'Agency Fees - Daydream SOW1 Brand Marketing'"
    },
    {
      "rule": "Project Type ID options: internal=1, client non billable=2, client billable-oop=3, client billable-fee=4",
      "source": "Determine and populate the Project Type ID Options"
    },
    {
      "rule": "Business Type ID options: organic=1 (Typically SOW #2 or greater), new business=2 (Typically SOW #1)",
      "source": "Determine and populate the Business Type ID Options"
    },
    {
      "rule": "Client Stage ID options: pre-launch=1, early=2, growth=3, coop=4, non-billable=5",
      "source": "Determine and populate the Client Stage ID Options"
    },
    {
      "rule": "Budget Fee must be input as a number with dollar sign removed",
      "source": "Input the number of the cost of the project, with the dollar sign removed"
    },
    {
      "rule": "Merchant ID must be obtained via Garage",
      "source": "Get the Merchant ID Obtained via Garage"
    },
    {
      "rule": "Customer ID must be obtained via Garage",
      "source": "Get the Customer ID Obtain via Garage"
    },
    {
      "rule": "Client Director ID must be obtained via NetSuite Red Antler Client Director IDs",
      "source": "Obtained via NetSuite Red Antler Client Director IDs"
    },
    {
      "rule": "Project Manager ID should be ignored during project creation",
      "source": "Ignore the Project Manager ID"
    },
    {
      "rule": "Project ID must be mapped to specific contract using super power after creation",
      "source": "Use this project ID and mapped it to a specific contract by using the super power"
    },
    {
      "rule": "Ops must send slack bot notifications once processed",
      "source": "Ops to send slack bot notifications once processed"
    },
    {
      "rule": "Project creation requires navigation to Garage Secrets at https://garage.tabsplatform.com/prod/secrets",
      "source": "First navigate to Garage Secrets https: garage tabsplatform com prod secrets"
    },
    {
      "rule": "Use 'Super Power Create Red Antler Project' for project creation",
      "source": "Use Super Power Create Red Antler Project"
    }
  ],
  "exceptions": [
    {
      "exception": "SOW #1 typically indicates 'new business' (Business Type ID = 2)",
      "condition": "First statement of work"
    },
    {
      "exception": "SOW #2 or greater typically indicates 'organic' (Business Type ID = 1)",
      "condition": "Subsequent statements of work"
    },
    {
      "exception": "Client Director ID requires interim contact with Royce and manual excel spreadsheet tracking",
      "condition": "Reach out to Royce at the interim Please start creating an excel spreadsheet to get the Client Director NS internal IDs"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Special memo s certain invoices require Invoice changes due to merchant customer relationship"
    },
    {
      "exception": "Events billing may require special processing",
      "condition": "Events Processing (if necessary)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Red Antler specific project creation process",
      "description": "Entire workflow is customized for Red Antler merchant"
    },
    {
      "element": "Contract reference example: a3f5017e-184f-49a8-aaa0-c8aa6f2abde4",
      "description": "Specific contract ID format for Red Antler"
    },
    {
      "element": "Merchant ID: 24891748-0cee-446e-9c4e-df50c4f72882",
      "description": "Red Antler specific merchant identifier"
    },
    {
      "element": "Customer ID: ec71bc10-de13-4f85-a1e7-aa89a1e1190a",
      "description": "Example customer ID for Red Antler"
    },
    {
      "element": "Project example: 'SOW #5: Pouch Packaging Update' with budgeFee: 2500",
      "description": "Red Antler specific project naming and structure"
    },
    {
      "element": "Red Antler Client Director IDs in NetSuite",
      "description": "Merchant-specific director mapping system"
    },
    {
      "element": "Sales notes indicate 'Larger Enterprise account for Tabs (ACV 40k)'",
      "description": "Red Antler account size and value classification"
    },
    {
      "element": "Invoice line item prefix: 'Agency Fees -'",
      "description": "Red Antler specific invoice formatting"
    },
    {
      "element": "Customer information and special memos for specific customers",
      "description": "Red Antler may have unique customer relationship requirements"
    }
  ],
  "confidence_score": 0.85
}
```

---

