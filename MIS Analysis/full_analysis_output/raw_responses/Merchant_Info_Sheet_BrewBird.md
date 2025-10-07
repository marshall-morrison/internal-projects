# Raw LLM Analysis: Merchant Info Sheet - BrewBird

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:34:03

---

## Chunk 1: Merchant Info Sheet - BrewBird_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:03

### Original Content
```
Merchant Scoping start date: 2023 Implementation Completed Date (Go live date): 2023 MSA Signature Date: 3 6 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Andrew Schlenger - Head of Product Strategy (BizOps) Jess Hubbard - Strategic Programs Manager Company summary BrewBird manufactures a high-end coffee brewing machine and pods of locally roasted coffee beans They sell or lease the machines to the office market (e g Meta offices) and then sell the pods on a recurring on-demand basi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Purchase Order Processing",
    "Invoice Generation and Validation",
    "Integration with External Systems (OrderTime ERP)",
    "Communication and Notification Protocols",
    "Product-Specific Billing Rules"
  ],
  "rules": [
    "Contracts are POs from OrderTime (merchant's order management system)",
    "BPO must check for new orders, pull POs, and upload to Tabs for processing",
    "Processing flow must be completed in early AM so BrewBird receives notification by 6am PT / 9am ET",
    "Daily communication must be sent to Chirag after OrderTime is checked",
    "Communication must state if there were ship docs from previous day and how many",
    "Invoice must match the Ship Doc Order",
    "If duplicates exist, ping Chirag",
    "CX Invoice Number must be updated from garage, not from merchant app",
    "If OrderTime order includes ground shipping, create a BT for ground shipping with 'Shipping Item' integration",
    "If OrderTime order includes 'Brewbird Event' OR 'Brewbird Event Staff', use 'Services' as integration item",
    "If OrderTime order includes 'Brewbird Coffee Machine', use Integration Item 'Brewers:Brewer Sales'",
    "All items from OrderTime must be included on invoice, even if they have no dollar value",
    "Each item receives its own line item on the invoice",
    "If Customer PO exists in OrderTime, it must be added to invoice in P O Number field",
    "If Customer PO field is blank in OrderTime, it must be blank on the invoice"
  ],
  "exceptions": [
    "Slightly different use case for Tabs as primarily supporting PO-based pod orders (vs typical contract flow)",
    "Flag if more than 1 contract is uploaded for the same customer",
    "Items with no dollar value must still be included on invoice (exception to typical billing logic)",
    "Brewers can be either sold or leased (two different transaction types)",
    "Pods sold on recurring, on-demand basis via POs (not standard subscription)"
  ],
  "merchant_specific": [
    "Merchant name: BrewBird",
    "Key contacts: Andrew Schlenger (Head of Product Strategy), Jess Hubbard (Strategic Programs Manager), Chirag (operations contact)",
    "ERP system: OrderTime (merchant's order management system)",
    "Product categories: Brewers (coffee machines - sold or leased), Pods (coffee - recurring on-demand)",
    "Target market: Office market (e.g., Meta offices)",
    "Specific product names: 'Brewbird Event', 'Brewbird Event Staff', 'Brewbird Coffee Machine'",
    "Integration items mapping: 'Shipping Item', 'Services', 'Brewers:Brewer Sales'",
    "Notification timing: 6am PT / 9am ET",
    "Custom field usage: 'Customer PO' field from OrderTime maps to 'P O Number' field in invoice",
    "Update location: 'garage' system for CX Invoice Number updates"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - BrewBird_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:03

### Original Content
```
If there is any question at all about the accuracy of the  P O Number  field, it is better to put the contract on hold and reach out to CX than to process incorrectly Extremely sensitive merchant P O Number  should be updated at the invoice level from garage Not at the customer level, not in the merchant app (See Screenshot below for proper place to update  P O Number  No Credit Card BTs to be processed (Flag to Chirag   CX for questions) Events Processing (if necessary) POs essentially serve as...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Purchase Order (PO) Number Management and Accuracy",
    "Customer-Specific Payment and Processing Rules",
    "Invoice Processing and Approval Workflows",
    "Payment Methods and Restrictions",
    "Feature Requests and System Improvements"
  ],
  "rules": [
    {
      "rule": "When uncertain about PO Number accuracy, put contract on hold and contact CX rather than processing incorrectly",
      "category": "Quality Control",
      "sensitivity": "high"
    },
    {
      "rule": "PO Number must be updated at the invoice level from garage system",
      "category": "Data Entry",
      "sensitivity": "high"
    },
    {
      "rule": "PO Number should NOT be updated at customer level",
      "category": "Data Entry",
      "sensitivity": "high"
    },
    {
      "rule": "PO Number should NOT be updated in the merchant app",
      "category": "Data Entry",
      "sensitivity": "high"
    },
    {
      "rule": "No Credit Card BTs (Balance Transfers) to be processed",
      "category": "Payment Processing",
      "sensitivity": "high"
    },
    {
      "rule": "Flag Credit Card BT questions to Chirag and CX",
      "category": "Escalation",
      "sensitivity": "medium"
    },
    {
      "rule": "POs serve as 'events' for this merchant",
      "category": "Business Logic",
      "sensitivity": "medium"
    },
    {
      "rule": "Do Not Process any orders for: Brewbird HQ, Brewbird Eng, Brewbird Service",
      "category": "Customer Exclusions",
      "sensitivity": "high"
    }
  ],
  "exceptions": [
    {
      "exception": "Events Processing may be necessary in certain cases (conditional)",
      "context": "POs serve as events"
    },
    {
      "exception": "Snackwise customer is being potentially phased out",
      "context": "Customer relationship status"
    },
    {
      "exception": "Brewbird entities (HQ, Eng, Service) are explicitly excluded from processing",
      "context": "Customer blacklist"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer roster serving Meta",
      "details": "Two main customers: Snackwise and Canteen, both serving Meta at different offices",
      "customization_needed": true
    },
    {
      "element": "Snackwise payment characteristics",
      "details": "Pays via ACH, slower to pay, more difficult to work with",
      "customization_needed": true
    },
    {
      "element": "Canteen payment characteristics",
      "details": "Implied to be easier to work with than Snackwise",
      "customization_needed": true
    },
    {
      "element": "Approval workflow",
      "details": "Currently requires Jess to approve invoices individually",
      "customization_needed": true
    },
    {
      "element": "Feature requests",
      "details": "Auto-approve invoices, Slack approval, customize payment methods by end-customer, customized dunning, faster PO to invoice turnaround",
      "customization_needed": true
    },
    {
      "element": "PO Number field sensitivity",
      "details": "Described as 'extremely sensitive' for this merchant",
      "customization_needed": true
    },
    {
      "element": "Terminology: 'garage'",
      "details": "System or interface where invoice-level updates should occur",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.82
}
```

---

