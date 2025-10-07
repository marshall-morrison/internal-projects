# Raw LLM Analysis: BenefitFlow MIS_

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:35:24

---

## Chunk 1: BenefitFlow MIS__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:35:24

### Original Content
```
Merchant Name: BenefitFlow Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Contract Processing Steps Generalized instructions for processing BTs f...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Terms (BT) Creation",
    "Date Handling and Default Values",
    "Merchant Onboarding and Implementation Workflow",
    "Integration and Revenue Recognition",
    "Communication and Stakeholder Management"
  ],
  "rules": [
    {
      "rule_id": "BT-001",
      "description": "Each billing item line in the product service table should be its own BT",
      "category": "Billing Terms Creation"
    },
    {
      "rule_id": "BT-002",
      "description": "Discounted or $0 lines should still be processed as BTs",
      "category": "Billing Terms Creation"
    },
    {
      "rule_id": "BT-003",
      "description": "Do not make a BT for sales tax",
      "category": "Billing Terms Creation"
    },
    {
      "rule_id": "BT-004",
      "description": "Process $0 items when clearly marked as included or waived",
      "category": "Billing Terms Creation"
    },
    {
      "rule_id": "QTY-001",
      "description": "Use the quantity listed for the BT (usually 1). If not listed, default to 1",
      "category": "Quantity Handling"
    },
    {
      "rule_id": "PRICE-001",
      "description": "Use the full price listed for the product",
      "category": "Pricing"
    },
    {
      "rule_id": "PRICE-002",
      "description": "If monthly pricing is shown and subtotal is annualized, calculate based on frequency and unit price",
      "category": "Pricing"
    },
    {
      "rule_id": "DATE-001",
      "description": "Service Start Date: Use Subscription Start Date, Signature Date, or similar phrasing if stated",
      "category": "Date Handling"
    },
    {
      "rule_id": "DATE-002",
      "description": "If Service Start Date not stated: default to signature date in contract body or audit trail",
      "category": "Date Handling"
    },
    {
      "rule_id": "DATE-003",
      "description": "If no signature date exists, default to quote expiration date on first page, top right corner",
      "category": "Date Handling"
    },
    {
      "rule_id": "DATE-004",
      "description": "Billing Start Date should match Service Start Date unless otherwise stated",
      "category": "Date Handling"
    },
    {
      "rule_id": "TERM-001",
      "description": "Use full contract term as stated. Most contracts are 12 months",
      "category": "Contract Terms"
    },
    {
      "rule_id": "TERM-002",
      "description": "Default Service Term if none listed: 1 Year",
      "category": "Contract Terms"
    },
    {
      "rule_id": "FREQ-001",
      "description": "Identify frequency based on unit price and payment terms (e.g., $2,400/month = Monthly frequency)",
      "category": "Billing Frequency"
    },
    {
      "rule_id": "FREQ-002",
      "description": "If contract shows annual flat rate, Frequency = Annual",
      "category": "Billing Frequency"
    },
    {
      "rule_id": "FREQ-003",
      "description": "Default Billing Frequency if none listed: Monthly",
      "category": "Billing Frequency"
    },
    {
      "rule_id": "NET-001",
      "description": "Use Net Terms listed under Purchase Terms or similar",
      "category": "Payment Terms"
    },
    {
      "rule_id": "NET-002",
      "description": "If Net Terms not listed, default to 30 days",
      "category": "Payment Terms"
    },
    {
      "rule_id": "NET-003",
      "description": "Default Net Payment Terms if none: 0 days",
      "category": "Payment Terms"
    },
    {
      "rule_id": "TIMING-001",
      "description": "Billing Timing: Bill first of period",
      "category": "Billing Timing"
    },
    {
      "rule_id": "INT-001",
      "description": "All items should be mapped to Sales MRR",
      "category": "Integration"
    },
    {
      "rule_id": "TAX-001",
      "description": "Default handling: every tax line item becomes a BT (if none listed)",
      "category": "Tax Handling"
    }
  ],
  "exceptions": [
    {
      "exception_id": "EXC-001",
      "description": "ParetoHealth renewal contracts may have 24-month terms instead of standard 12 months",
      "context": "Contract term length variation"
    },
    {
      "exception_id": "EXC-002",
      "description": "Some merchants may request specific processing differences by contract (e.g., always back-date invoice date to final day of the month)",
      "context": "Merchant-specific processing requests"
    },
    {
      "exception_id": "EXC-003",
      "description": "BenefitFlow has majority of customers billed annually, but some are monthly or quarterly",
      "context": "Billing frequency variation"
    },
    {
      "exception_id": "EXC-004",
      "description": "BenefitFlow includes credits within flat fees and does not charge for overages today",
      "context": "Merchant-specific billing model"
    },
    {
      "exception_id": "EXC-005",
      "description": "Conflict in default Net Payment Terms: document states both '30 days' and '0 days' as defaults",
      "context": "Ambiguous default values"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "description": "BenefitFlow",
      "customization_needed": true
    },
    {
      "element": "POC contacts",
      "description": "Implementation POC, CX POC to be filled per merchant",
      "customization_needed": true
    },
    {
      "element": "Billing model",
      "description": "Flat fees with included credits, no overage charges, majority annual billing with some monthly/quarterly",
      "customization_needed": true
    },
    {
      "element": "Integration Item mapping",
      "description": "All items mapped to Sales MRR for BenefitFlow; other merchants may have different mappings (e.g., Statsig to Sales, Pinata to Software Subscription Bundle)",
      "customization_needed": true
    },
    {
      "element": "Example contracts",
      "description": "Five specific contract IDs provided as reference examples",
      "customization_needed": true
    },
    {
      "element": "Post Processing Communications",
      "description": "Notification requirements vary by merchant (e.g., Messari example: notify Azmat Aziz in internal channel when contracts processed)",
      "customization_needed": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos, invoice changes due to merchant-customer relationships",
      "customization_needed": true
    },
    {
      "element": "Merchant temperament",
      "description": "Pedro is first finance hire, easy going, texting basis relationship",
      "customization_needed": true
    },
    {
      "element": "Key features of interest",
      "description": "Contract ingestion, auto invoice/billing/revenue schedule creation, renewal tracking, integrations with HubSpot, QB, and Stripe",
      "customization_needed": true
    },
    {
      "element": "Item naming convention",
      "description": "Use product name from left-hand column (e.g., 'BenefitFlow Enterprise Subscription')",
      "customization_

---

