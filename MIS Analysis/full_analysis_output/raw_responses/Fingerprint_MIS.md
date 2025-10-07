# Raw LLM Analysis: Fingerprint MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:36:37

---

## Chunk 1: Fingerprint MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:36:37

### Original Content
```
id 1902688754138778778 account-id 7661388937693840866 Demo https: us-56595 app gong io call id 4445181161382765404 account-id 7661388937693840866 Scoping   Pricing https: us-56595 app gong io call id 8281191693865243762 account-id 7661388937693840866 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills 1) Self Serve- Stripe 2) Contracts ( 9k- 3m invoices) - payment terms - payment frequency - Commit to a bucket of API calls - amendme...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Payment Structure",
    "Revenue Recognition (UBRR)",
    "Implementation and Handoff Process",
    "Data Integration and Reporting",
    "Stakeholder Management and Key Contacts"
  ],
  "rules": [
    "Self-serve customers use Stripe for billing",
    "Contract customers ($9k-$3m range) receive invoices with defined payment terms and frequency",
    "Contracts commit to a bucket of API calls with CS-managed amendments for overages",
    "Revenue recognition follows UBRR (Usage-Based Revenue Recognition) model based on actual usage",
    "Unused revenue remainder is added to the last month of the contract period",
    "Account Executive (AE) fills initial information; Implementation team becomes completion DRI (Directly Responsible Individual) on handoff",
    "Usage data accessed via Sigma and Snowflake",
    "CSV format is acceptable as starting point for data delivery",
    "External accounting handled by Mystartupcfo"
  ],
  "exceptions": [
    "Contract amendments required for API call overages (handled by Customer Success team)",
    "Revenue recognition remainder treatment - deferred amounts added to final month rather than distributed",
    "Merchant currently accepts CSV despite having Sigma/Snowflake capability (temporary/transitional state)"
  ],
  "merchant_specific": [
    "Merchant has 160 customers to manage",
    "Key contacts: Bobby (operational contact, easy to work with, currently handles manual processes) and Jeff (Executive Buyer with decision-making authority)",
    "Current state: Bobby manages processes manually via huge spreadsheet",
    "Priority features for this merchant: UBRR functionality and contract data extraction",
    "Merchant uses external accounting team (Mystartupcfo) rather than in-house",
    "Two-tier billing model: Self-serve via Stripe and enterprise contracts via invoicing",
    "Contract range specific to this merchant: $9k-$3m"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Fingerprint MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:36:52

### Original Content
```
Merchant Name: Fingerprint Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Billing address should come off the contract and be stored at the customer level...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Service Start Dates and Billing Periods Management",
    "Product and Line Item Processing Rules",
    "Integration Items and Tax Handling",
    "Post-Processing Communication and Customer Management"
  ],
  "rules": [
    {
      "rule": "Billing address must come from contract and be stored at customer level for each contract processed",
      "category": "Customer Setup"
    },
    {
      "rule": "Service Start Date should use the 'Start Date' column from contract",
      "category": "Billing Timeline"
    },
    {
      "rule": "Months of Service calculated to reach the 'End Date' column date",
      "category": "Billing Timeline"
    },
    {
      "rule": "Item Name should use 'Product Name' column",
      "category": "Product Processing"
    },
    {
      "rule": "Item Description should use 'Description' column",
      "category": "Product Processing"
    },
    {
      "rule": "Integration item should be 'Contracted' for every product",
      "category": "Product Processing"
    },
    {
      "rule": "Billing Type is Flat unless product is usage-based",
      "category": "Billing Configuration"
    },
    {
      "rule": "Create usage BT if contract notes overage API calls are charged",
      "category": "Usage Billing"
    },
    {
      "rule": "Total Price calculation: divide Customer Total by number of billing periods if payment schedule specifies multiple periods",
      "category": "Price Calculation"
    },
    {
      "rule": "Quantity should use 'Quantity' column",
      "category": "Product Processing"
    },
    {
      "rule": "Start Date for billing uses first billing date in 'payment invoice deadlines' section",
      "category": "Billing Timeline"
    },
    {
      "rule": "Number of periods uses number of billing periods from contract",
      "category": "Billing Timeline"
    },
    {
      "rule": "Frequency listed with 'Payment Frequency' under 'Billing Details'",
      "category": "Billing Configuration"
    },
    {
      "rule": "If frequency not listed, calculate months between each payment in 'payment invoice deadlines'",
      "category": "Billing Configuration"
    },
    {
      "rule": "If payment cadence is not even/consistent, create separate BT for each period",
      "category": "Billing Configuration"
    },
    {
      "rule": "Net terms use 'Payment Terms' from 'Billing Details', default to net 30 if not stated",
      "category": "Payment Terms"
    },
    {
      "rule": "Billing Timing is 'Bill first of period'",
      "category": "Billing Configuration"
    },
    {
      "rule": "Default Service Term: 1 Year if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default Net Payment Terms: 0 if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default Billing Frequency: Monthly if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default Tax Handling: every tax line item becomes a BT",
      "category": "Defaults"
    },
    {
      "rule": "Products with same characteristics and matching invoice schedule can be combined into one BT",
      "category": "Product Consolidation"
    }
  ],
  "exceptions": [
    {
      "exception": "Usage-based products require different Billing Type (not Flat)",
      "condition": "When product is usage-based"
    },
    {
      "exception": "Separate BTs required when payment cadence is not even or consistent",
      "condition": "When calculating frequency from payment invoice deadlines shows irregular intervals"
    },
    {
      "exception": "Multiple products can be combined into one BT",
      "condition": "When products are the same and invoicing schedule divides total contract amount into payments instead of matching invoice to product/service period"
    },
    {
      "exception": "Merchant-specific processing variations may differ by contract",
      "condition": "Example given: back-dating invoice date to final day of month",
      "note": "Merchant may request specific processing that differs from standard rules"
    },
    {
      "exception": "Integration items may have specific labeling requirements",
      "condition": "Varies by merchant (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')"
    }
  ],
  "merchant_specific": [
    {
      "element": "Fingerprint Implementation POC and CX POC",
      "type": "Contact Information",
      "note": "To be filled by IM/IMP"
    },
    {
      "element": "Billing model section",
      "type": "Configuration",
      "note": "Implementation team fills with merchant-specific billing details"
    },
    {
      "element": "Unique customer creation process",
      "type": "Process Customization",
      "note": "Merchant-specific customer setup requirements"
    },
    {
      "element": "Contract structure and breakdown",
      "type": "Contract Configuration",
      "note": "How merchant structures their contracts"
    },
    {
      "element": "Product table location and structure",
      "type": "Data Source",
      "note": "Varies by merchant contract format"
    },
    {
      "element": "Column names for data extraction",
      "type": "Data Mapping",
      "note": "Specific column names like 'Start Date', 'End Date', 'Product Name', 'Description', 'Quantity', 'Customer Total'"
    },
    {
      "element": "Payment frequency and schedule fields",
      "type": "Data Mapping",
      "note": "Location and format of payment terms in contract"
    },
    {
      "element": "Items to ignore in contracts",
      "type": "Processing Instructions",
      "note": "Merchant-specific exclusions"
    },
    {
      "element": "Events billing requirements",
      "type": "Billing Configuration",
      "note": "If necessary for merchant"
    },
    {
      "element": "Integration items labeling",
      "type": "Categorization",
      "note": "Merchant-specific integration item labels (e.g., Statsig, Pinata examples)"
    },
    {
      "element": "Post-processing notification requirements",
      "type": "Communication Protocol",
      "note": "Who to notify, where, and when after processing"
    },
    {
      "element": "Customer-specific information",
      "type": "Customer Management",
      "note": "Special memos, invoice changes based on merchant-customer relationships"
    },
    {
      "element": "Feature requests tracking",
      "type": "Enhancement Management",
      "note": "Filled by AE, Implementation, and Success teams at different phases"
    }
  ],
  "confidence_score": 0.92
}
```

---

