# Raw LLM Analysis: Glacier Historical Invoices MIS [Deprecated - Do Not Use]

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:24:50

---

## Chunk 1: Glacier Historical Invoices MIS [Deprecated - Do Not Use]_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:24:50

### Original Content
```
Contract Processing Steps For this format: Customer creation If customer does not already exist, create one Use Bill To section for address info and billing email If city, state, or zip are not included, can ignore Processing Each line item will be a rev schedule Use description info in the contract as the item name Use the Item ID info as the item description Total price will be the total price Qty will be quantity For service start date, use this google sheet (loom instructions for how to use)...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer and Contract Setup",
    "Revenue Schedule Line Item Processing",
    "Date Determination via External Reference Sheet",
    "Tax and Shipping Handling as Separate Line Items",
    "Data Validation and Reconciliation"
  ],
  "rules": [
    "Create customer only if they do not already exist",
    "Use Bill To section for customer address information and billing email",
    "Missing city, state, or zip codes can be ignored during customer creation",
    "Each line item must be processed as a revenue schedule",
    "Use contract description as the item name",
    "Use Item ID information as the item description",
    "Total price field equals the contract total price",
    "Quantity field equals the contract quantity",
    "Total months of service must be set to 3",
    "Billing start date must be taken from the top left of the contract",
    "Payment terms must use the terms listed in top right of contract",
    "Frequency field must be set to NONE",
    "Final total in garage system must match the contract total",
    "Sales tax requires its own separate revenue schedule (if present)",
    "Shipping and handling requires its own separate revenue schedule (if present)",
    "For tax line items: duplicate existing line item revenue schedule, delete description, change item name to 'tax', set total price to tax amount",
    "For shipping line items: duplicate existing line item revenue schedule, delete description, change item name to 'Shipping & Handling', set total price to shipping amount"
  ],
  "exceptions": [
    "If customer already exists, skip customer creation step",
    "City, state, or zip can be omitted without blocking processing",
    "Ignore sales tax processing if no tax is present on contract",
    "Ignore shipping and handling processing if none is present on contract",
    "When multiple invoice numbers match in the reference sheet, match dates on contract with sheet dates to locate correct entry",
    "Service start date determination requires complex lookup: extract invoice number from filename brackets, find corresponding row in column A of Google sheet, identify quarter realized, cross-reference with yellow table to determine exact date"
  ],
  "merchant_specific": [
    "Invoice number format in filename (example: DIV-001 in brackets)",
    "Google sheet reference for service start date lookup (specific URL provided)",
    "Quarter-based date mapping system (e.g., 2024 Q2 = April 1st, 2024)",
    "Yellow table reference in the Google sheet for date conversion",
    "Column A reference for invoice number lookup",
    "Garage system as the target platform",
    "Bill To section format and location on contract",
    "Contract layout: date in top left, terms in top right",
    "3-month service period standard",
    "Specific terminology: 'rev schedule', 'quarter realized', 'garage'"
  ],
  "confidence_score": 0.82
}
```

---

