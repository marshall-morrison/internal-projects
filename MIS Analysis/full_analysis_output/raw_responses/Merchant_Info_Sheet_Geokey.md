# Raw LLM Analysis: Merchant Info Sheet - Geokey

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:15:32

---

## Chunk 1: Merchant Info Sheet - Geokey_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:15:32

### Original Content
```
These should be relatively small   where duplicate contracts are actual changes to the invoices terms Flow 1 (Sales Order   Purchase Agreement) Good reference contracts and loom video Loom video here - https: www loom com share 76a41271b38d47389e9bee31999c893d Reference contracts Purchase Agreement: 970c09bc-e7d4-4bd1-b80d-6ecad1e115c9 Sales Order: a201414f-7b58-4a6f-b9d4-692b93570d78 There should be 2 documents - Sales Order   Purchase Agreement Use the Sales Order for billing terms and use the...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Dual Document Processing (Sales Order and Purchase Agreement)",
    "Document Timing and Escalation Procedures",
    "Payment Structure and Billing Terms Extraction",
    "Tax Handling and Price Inclusivity",
    "Document Section Mapping and Data Sources"
  ],
  "rules": [
    "Two documents must be present: Sales Order and Purchase Agreement",
    "Use Sales Order specifically for billing terms extraction",
    "Use Purchase Agreement specifically for date extraction",
    "Wait for the Purchase Agreement (secondary document) before processing",
    "Purchase Agreement should arrive within 1 hour of Sales Order being sent to Tabs",
    "Escalate to manager if Purchase Order is missing when Sales Order indicates it should exist",
    "Extract payment rules from the first page of Purchase Agreement",
    "Extract payment schedule from the last pages of Purchase Agreement",
    "Do not add tax line items to billing terms as prices are tax-inclusive",
    "Escalate to manager if numbers are off/don't match",
    "Duplicate contracts should only exist when there are actual changes to invoice terms"
  ],
  "exceptions": [
    "Deposit and Downpayment: Almost always refers only to hardware materials and services (but requires reading fine print for confirmation)",
    "Final Payment: Normally inclusive of software (but not always)",
    "Other Payments: Either the software invoice date if not defined elsewhere OR the renewal date (conditional logic)",
    "Payment schedule types vary and require interpretation: Deposit/Downpayment, Final Payment, Other Payments"
  ],
  "merchant_specific": [
    "Reference to specific contract IDs (970c09bc-e7d4-4bd1-b80d-6ecad1e115c9 and a201414f-7b58-4a6f-b9d4-692b93570d78)",
    "Reference to 'Tabs' system as the document processing platform",
    "Loom video training reference (https://www.loom.com/share/76a41271b38d47389e9bee31999c893d)",
    "Specific document structure with payment rules on first page and schedule on last pages",
    "Breakdown by percentage (%) in payment rules",
    "Hardware vs software distinction in payment categorization",
    "Manager escalation workflow and procedures"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Geokey_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:15:34

### Original Content
```
Merchant Scoping start date: D D partner Implementation Completed Date (Go live date): Jun 11, 2024t MSA Signature Date: Feb 7, 2024 GTM POC: Implementation POC: Royce Kok ERP: Sales   CRM : Zoho Tax Integration: (Current systems is in QBO Taxes) Key people at Merchant CEO: Brandon Peterson Sales Order automation: Taylor Williams Tax expert: Dallas Polivka Smartsheet automation: Megan Rossman Controller: Maya AR person Company summary Geokey is a mobile access control software that allows users ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Sales Order Processing Workflow",
    "System Integration and Data Flow",
    "Customer and Subcustomer Management",
    "Billing and Invoice Timing Rules",
    "Document Identification and Duplicate Prevention"
  ],
  "rules": [
    "DO NOT PROCESS any files starting with INV-X, ONLY PROCESS files starting with SO-X",
    "Before processing SO-X files, check garage to see if an identical SO has been uploaded and processed previously",
    "If an identical SO has been processed previously, DO NOT PROCESS",
    "When creating a customer, must add the address",
    "If there is a name under 'reference' in the sales order, create a subcustomer in QBO",
    "Default payment terms: Net 0",
    "Pull the Geokey 'Project ID' from the SO Field 'Reference' (where populated)",
    "Map the 'Project ID' to Tabs' Custom 'additional fields' specifically the 'project name' field",
    "Do not need to populate tax info as part of contract ingest",
    "First half of invoice goes out on signature date",
    "Second half of invoice goes out on installation date (picked up via Smartsheet automation)",
    "If duplicate INV ID is received, delete old contracts and reprocess new contracts"
  ],
  "exceptions": [
    "Two different workflows exist: Flow 1 (Sales Order + Purchase Agreement - more complex) and Flow 2 (Sales Order only - simple)",
    "Flow 1 is identified when Terms & Conditions reference a 'purchase order'",
    "Flow 2 is identified when Terms & Conditions do not specify purchase order",
    "IF POSSIBLE: When Reference field contains 'Quote Number' + 'Project ID', prefer to exclude the Quote Number and only include Project ID (Example: 'QT-011479 (Citylight - Midtown)' should become 'Citylight - Midtown')",
    "Tax integration note: Current system is in QBO Taxes, don't populate tax info as billing term"
  ],
  "merchant_specific": [
    "Merchant name: Geokey",
    "Go live date: Jun 11, 2024",
    "MSA Signature Date: Feb 7, 2024",
    "Key personnel: Brandon Peterson (CEO), Taylor Williams (Sales Order automation), Dallas Polivka (Tax expert), Megan Rossman (Smartsheet automation), Maya (Controller), Royce Kok (Implementation POC)",
    "Systems used: Zoho (CRM/Sales Order source), QBO (QuickBooks Online for taxes), Smartsheet (automation), Avalara (tax integration)",
    "Business description: Mobile access control software for doors, gates, elevators, and padlocks",
    "File naming convention: SO-X format for sales orders, INV-X format for invoices",
    "Custom field mapping: 'Project ID' maps to 'project name' field in Tabs",
    "Subcustomer example: 'Queens Manor' becomes subcustomer",
    "Quote Number format example: QT-011479",
    "Sales Order example: SO-1774",
    "Billing model: Split invoice (50% on signature, 50% on installation)",
    "Note: Large enterprise deal with disparate systems and multiple stakeholders"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Geokey_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:15:50

### Original Content
```
Flow 2 (Invoice only) There should only be one document for the Invoice Only flow Each line item in the sales order will specify how it should be billed If nothing specified, assume non-recurring on the Invoice Date under  Terms and Conditions , otherwise use the Billing Order Date For instance, if a line item shows (Term Quoted: 3-year, price lock agreement if renewed (paying 2-years up front), Divide the total in the  amount  column by 3, and create two billing terms, one worth ⅔ of the total ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice generation and billing workflows",
    "Line item billing specifications and term calculations",
    "Tax calculation discrepancies and reconciliation",
    "Customer-specific handling and relationship management",
    "Document processing rules for Invoice Only flow"
  ],
  "rules": [
    {
      "rule": "Invoice Only flow should contain only one document",
      "category": "document_requirements"
    },
    {
      "rule": "Each line item in sales order must specify billing method",
      "category": "billing_specification"
    },
    {
      "rule": "Default billing assumption: non-recurring on Invoice Date under Terms and Conditions if not specified",
      "category": "billing_default"
    },
    {
      "rule": "If no billing specification exists, use Billing Order Date",
      "category": "billing_fallback"
    },
    {
      "rule": "For multi-year term quotes with upfront payment: divide total amount by term years and create separate billing terms based on payment schedule",
      "category": "term_calculation"
    },
    {
      "rule": "Example calculation: 3-year term with 2-years upfront payment = ⅔ of total on Billing Date, ⅓ on 2-year anniversary",
      "category": "term_calculation_example"
    },
    {
      "rule": "Invoice totals may not match sales order totals due to tax calculation differences between garage system and Avalara",
      "category": "tax_reconciliation"
    },
    {
      "rule": "Cannot assume invoice-sales order matching until subtotal-tax is exposed in garage system",
      "category": "system_limitation"
    }
  ],
  "exceptions": [
    {
      "exception": "Tax values calculated in garage may differ from Avalara calculations",
      "impact": "Invoice totals may not match sales order totals"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "trigger": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "trigger": "Relationship-based modifications"
    },
    {
      "exception": "Multi-year term quotes with price lock and renewal agreements require custom billing term splits",
      "trigger": "Complex payment structures"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Information section",
      "description": "Important specifics about individual customers of the merchant",
      "customization_needed": true
    },
    {
      "element": "Special memos for certain invoices",
      "description": "Invoice-specific notes based on merchant-customer relationships",
      "customization_needed": true
    },
    {
      "element": "Invoice changes due to merchant customer relationship",
      "description": "Relationship-driven modifications to standard invoicing",
      "customization_needed": true
    },
    {
      "element": "Events Processing",
      "description": "Marked as 'None' but appears to be a placeholder for merchant-specific event handling",
      "customization_needed": true
    },
    {
      "element": "Feature Requests section",
      "description": "Merchant-specific feature requests and urgency tracking",
      "customization_needed": true
    },
    {
      "element": "Rewatch Calls",
      "description": "Call review requirements by dates - likely merchant-specific",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document appears to be an internal operations guide with clear billing rules, but some sections are incomplete or truncated (e.g., "Feature Requests FR 1" section, "Rewatch by dates"). The core billing logic and tax reconciliation rules are clearly stated, but the merchant-specific sections lack detail. The confidence score reflects clarity on core processes but uncertainty about incomplete sections and context-dependent elements.

---

