# Raw LLM Analysis: Elephant Energy MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:12:41

---

## Chunk 1: Elephant Energy MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:12:41

### Original Content
```
Elephant Energy Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process PLEASE MAKE SURE THE CUSTOMER IS ASSIGNED CORRECTLY - the below should not be happ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Two-invoice billing structure with downpayment and completion payment",
    "Contract data extraction from Project Cost Breakdown and System Designs pages",
    "Revenue recognition timing and billing term configuration",
    "Product specification documentation requirements for HVAC equipment",
    "QuickBooks Online integration and classification rules"
  ],
  "rules": [
    "Every project must have exactly two invoices",
    "First invoice is for downpayment (typically 50% but verify on contract signature page)",
    "Second invoice itemizes all line items from Project Cost Breakdown up to Out-of-Pocket Cost",
    "Use 'Services' for all products in QBO",
    "QBO Class must be set to the state in customer's address; leave blank if state not available",
    "Service Start Date: 1 year from signature date (or prepared by date if signature unavailable)",
    "Total months of service: 1 (recognize revenue in month invoice is sent)",
    "Net terms: 0 (bill in advance, due start of period)",
    "Number of periods: 1",
    "Frequency: none",
    "First invoice Billing Start Date: date of last signature or proposal date from page 1",
    "Second invoice Billing Start Date: one month after first invoice billing start date",
    "Second invoice must include negative 'Downpayment Credit' line item",
    "Ignore all line items after 'Out-of-Pocket Cost' section",
    "Do not include total lines (e.g., 'total cost' or 'total point of sale rebates')",
    "If sum of line items doesn't match total out-of-pocket costs, use sum of line items",
    "Item descriptions required for main products (heat pumps, water heaters)",
    "Item descriptions must include: Outdoor Unit model, Indoor unit model, AHRI number, EER2, SEER2, HSPF2 (separated by semicolons)",
    "Customer must be assigned correctly to project",
    "Billing email address must be assigned to customer",
    "Change orders modify original contract billing terms and take effect after first 50% deposit invoice"
  ],
  "exceptions": [
    "Downpayment percentage varies - not always 50%, must verify on contract signature page or Payment Schedule section",
    "If no downpayment amount listed, default to 50% of Out-of-Pocket Cost",
    "If signature date unavailable, use prepared by date from front page for Service Start Date",
    "If state not available in QBO dropdown, leave Class field blank",
    "Some contracts have edge cases requiring special attention (referenced but not detailed)",
    "Water heater item descriptions may have fewer specification fields (e.g., only HPTS model and AHRI number)",
    "Credits marked 'direct to customer' should be ignored"
  ],
  "merchant_specific": [
    "Merchant name: Elephant Energy",
    "Contract structure: Project Cost Breakdown page and System Designs page",
    "Terminology: 'Out-of-Pocket Cost (Amount paid to Elephant or Financed)'",
    "Product types: Heat pumps, water heaters, mini-split systems",
    "HVAC-specific specifications: AHRI numbers, EER2, SEER2, HSPF2 ratings",
    "State-based classification system for QBO",
    "Two-phase payment model: upfront downpayment and completion payment",
    "Change order process specific to this merchant's workflow",
    "Customer assignment issues mentioned as recurring problem",
    "Contract ID format example: be806827-9baf-4a26-b063-b3400e87b573"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Elephant Energy MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:12:45

### Original Content
```
Only the final invoice will be impacted You do not need to change the amount of the  Downpayment Credit  If they re removing something: just the price of that item would change to  0 If they're adding or changing the price of something: List out the Item Name as  Change Order    Item Name  Make sure you apply any change orders made to point of sale incentives rebate line items to the subcustomer contract as well (read section below) Point of Sale Incentives Rebates Duplicate the contract and cre...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and Contract Processing Workflow",
    "Change Order Management",
    "Point of Sale Incentives and Rebates Handling",
    "Billing Terms and Default Values",
    "Special Discounts and Financing Arrangements"
  ],
  "rules": [
    {
      "rule": "Only the final invoice is impacted by changes, not the downpayment credit",
      "category": "Change Orders"
    },
    {
      "rule": "For item removals in change orders, set the price to 0",
      "category": "Change Orders"
    },
    {
      "rule": "For item additions or price changes, list as 'Change Order - [Item Name]'",
      "category": "Change Orders"
    },
    {
      "rule": "Apply change orders to point of sale incentives rebate line items on subcustomer contract",
      "category": "Change Orders"
    },
    {
      "rule": "Duplicate contract and create sub-customer titled '[Main Customer] Customer Incentives' for rebates",
      "category": "Point of Sale Incentives"
    },
    {
      "rule": "Process Point of Sale Incentives Rebates as positive (+) BT (Billing Terms)",
      "category": "Point of Sale Incentives"
    },
    {
      "rule": "Set billing start dates one day apart for multiple products to track on separate invoices (e.g., 6/12, 6/13, 6/14)",
      "category": "Billing Terms"
    },
    {
      "rule": "If first deposit amount is 0, assume upfront payment and add 3% discount on 2nd invoice",
      "category": "Upfront Discount"
    },
    {
      "rule": "Synchrony financing discount is 7% of synchrony financing amount, applied ONLY to final invoice",
      "category": "Financing Partner"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "category": "Defaults"
    },
    {
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "category": "Defaults"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "category": "Defaults"
    },
    {
      "rule": "Every tax line item becomes a BT (Billing Term) if none listed",
      "category": "Tax Handling"
    },
    {
      "rule": "Two invoices are issued: first on signing, second when job is complete",
      "category": "Invoice Workflow"
    },
    {
      "rule": "Each invoice is half the total amount",
      "category": "Invoice Workflow"
    },
    {
      "rule": "Ops team sends email trigger when job is complete for second invoice to be sent",
      "category": "Invoice Workflow"
    }
  ],
  "exceptions": [
    {
      "exception": "Upfront discount: 3% discount applied when first deposit is 0 (full payment upfront vs two separate payments)",
      "condition": "First deposit amount = 0"
    },
    {
      "exception": "Synchrony Financing Discount: Special 7% discount line item required by financing partner",
      "condition": "When 'synchrony financing amount' is noted on contract",
      "details": "Does not affect first deposit amount, only final invoice"
    },
    {
      "exception": "Point of Sale Incentives Rebates processed differently than standard items",
      "condition": "When rebates are present",
      "details": "Requires sub-customer contract creation and positive BT processing"
    },
    {
      "exception": "Billing start dates staggered by one day for multiple products",
      "condition": "When merchant wants to track items on separate invoices",
      "details": "Sequential day increments (e.g., 6/12, 6/13, 6/14)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Elephant Energy merchant name",
      "type": "Merchant Identity"
    },
    {
      "element": "Two-invoice billing structure (signing and job completion)",
      "type": "Billing Workflow",
      "customizable": true
    },
    {
      "element": "Point of Sale Incentives Rebates processing with sub-customer creation",
      "type": "Rebate Handling",
      "customizable": true
    },
    {
      "element": "Sub-customer naming convention: '[Main Customer] Customer Incentives'",
      "type": "Naming Convention",
      "customizable": true
    },
    {
      "element": "3% upfront payment discount",
      "type": "Discount Policy",
      "customizable": true
    },
    {
      "element": "Synchrony financing partnership and 7% discount",
      "type": "Financing Terms",
      "customizable": true
    },
    {
      "element": "Email trigger from Ops team for second invoice",
      "type": "Communication Process",
      "customizable": true
    },
    {
      "element": "Example contract IDs provided for reference",
      "type": "Reference Materials"
    },
    {
      "element": "Integration items labeling (Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "type": "Integration Processing",
      "customizable": true
    },
    {
      "element": "Customer Success notification requirement (Azmat Aziz in merchant channel)",
      "type": "Post-Processing Communication",
      "customizable": true
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 3: Elephant Energy MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:12:52

### Original Content
```
They are looking to us to help them get their AR in order, they have ideas but are open to ours based on what s realistic Jon Schwartz-Frac CFO very friendly, very bright - huge champion for tabs Straight shooter Jade - Accountant, quiet but will be your main contact Only call out is rebate APIs to get rebate data into Tabs Want to do it after some additional scoping and are very open to our feedback since we are experts in the field 3) What are the Tabs features that the key POC cares about Ele...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Automation and AR Management",
    "System Integration and Data Flow",
    "Operational Efficiency and Time Reduction",
    "Compliance and Audit Requirements",
    "Stakeholder Management and Partnership"
  ],
  "rules": [
    "Invoices must be automatically created, sent, and have cash applied",
    "Customer data must be automatically scraped from contracts",
    "Cash application must be automated based on geography and type of payment",
    "All billing must sync to QBO (QuickBooks Online) in real time",
    "All changes must be logged in an audit log with time and date stamps",
    "SOC II compliance must be maintained",
    "PII (Personally Identifiable Information) exposure must be minimized",
    "Tabs must integrate with bank and Stripe payment systems",
    "Month-end close process should be reduced to days (from presumably longer period)",
    "Rebate APIs integration should occur after additional scoping and expert feedback"
  ],
  "exceptions": [
    "Rebate API integration is deferred - to be implemented after scoping phase with Tabs expert guidance",
    "Client (Elephant Energy) is open to Tabs recommendations over their own ideas based on what is realistic",
    "Implementation approach is flexible based on Tabs expertise rather than rigid requirements"
  ],
  "merchant_specific": [
    "Primary contacts: Jon Schwartz (Frac CFO, champion), Jade (Accountant, main contact)",
    "Company name: Elephant Energy",
    "Specific payment processors: Stripe and bank integrations",
    "Accounting system: QBO (QuickBooks Online)",
    "Industry-specific needs: Contract-based customer data, geography-based payment routing",
    "Custom future state requirements written by client themselves",
    "Rebate data management specific to their business model",
    "Team focus areas: driving revenue and product development (suggesting tech/product company)"
  ],
  "confidence_score": 0.92
}
```

---

