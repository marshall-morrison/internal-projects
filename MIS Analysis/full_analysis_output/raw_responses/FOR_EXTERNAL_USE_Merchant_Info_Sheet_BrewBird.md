# Raw LLM Analysis: [FOR EXTERNAL USE] Merchant Info Sheet - BrewBird

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:34:40

---

## Chunk 1: [FOR EXTERNAL USE] Merchant Info Sheet - BrewBird_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:40

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
    "Processing must be completed in early AM to notify BrewBird by 6am PT / 9am ET",
    "Daily communication must be sent to Chirag after OrderTime is checked",
    "Communications must state if there were ship docs from previous day and quantity",
    "Invoice must match the Ship Doc Order",
    "CX Invoice Number must be updated from garage, not from merchant app",
    "If OrderTime order includes ground shipping, create a BT for ground shipping with 'Shipping Item' integration",
    "If OrderTime order includes 'Brewbird Event' OR 'Brewbird Event Staff', use 'Services' as integration item",
    "If OrderTime order includes 'Brewbird Coffee Machine', use 'Brewers:Brewer Sales' as integration item",
    "All items from OrderTime must be included on invoice, even if they have no dollar value",
    "Each item receives its own line item on the invoice",
    "If Customer PO exists in OrderTime, it must be added to invoice in P O Number field",
    "If Customer PO field is blank in OrderTime, it must be blank on invoice"
  ],
  "exceptions": [
    "Flag in communications if more than 1 contract is uploaded for the same customer",
    "If duplicates exist, ping Chirag",
    "Items with zero dollar value must still be included on invoice (exception to typical billing practices)",
    "Different integration items based on product type (ground shipping vs events vs coffee machines)"
  ],
  "merchant_specific": [
    "Merchant name: BrewBird",
    "Key contacts: Chirag (daily comms recipient), Andrew Schlenger (Head of Product Strategy), Jess Hubbard (Strategic Programs Manager)",
    "ERP system: OrderTime (order management system)",
    "Business model: High-end coffee brewing machines (sold or leased) and pods (recurring, on-demand)",
    "Target market: Office market (e.g., Meta offices)",
    "Specific product terminology: 'Brewbird Event', 'Brewbird Event Staff', 'Brewbird Coffee Machine', 'Brewer', 'Pods'",
    "Specific integration items: 'Shipping Item', 'Services', 'Brewers:Brewer Sales'",
    "Time zone preference: 6am PT / 9am ET notification deadline",
    "Invoice update location: 'garage' (specific system/interface)",
    "Use case: PO-based pod orders (noted as slightly different from typical Tabs usage)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: [FOR EXTERNAL USE] Merchant Info Sheet - BrewBird_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:42

### Original Content
```
If there is any question at all about the accuracy of the  P O Number  field, it is better to put the contract on hold and reach out to CX than to process incorrectly Extremely sensitive merchant P O Number  should be updated at the invoice level from garage Not at the customer level, not in the merchant app (See Screenshot below for proper place to update  P O Number  No Credit Card BTs to be processed (Flag to Chirag   CX for questions) Events Processing (if necessary) POs essentially serve as...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Purchase Order (PO) Number Management and Accuracy",
    "Payment Processing Rules and Restrictions",
    "Customer-Specific Information and Handling",
    "System Feature Requests and Workflow Improvements",
    "Invoice Processing and Approval Workflows"
  ],
  "rules": [
    {
      "rule": "If there is any uncertainty about PO Number accuracy, put contract on hold and contact CX rather than processing incorrectly",
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
      "rule": "No Credit Card Balance Transfers (BTs) to be processed",
      "category": "Payment Processing",
      "sensitivity": "high"
    },
    {
      "rule": "Credit Card BT questions should be flagged to Chirag and CX",
      "category": "Escalation",
      "sensitivity": "medium"
    },
    {
      "rule": "Do Not Process orders for: Brewbird HQ, Brewbird Eng, Brewbird Service",
      "category": "Customer Restrictions",
      "sensitivity": "high"
    },
    {
      "rule": "POs serve as 'events' for this merchant",
      "category": "Business Logic",
      "sensitivity": "medium"
    }
  ],
  "exceptions": [
    {
      "exception": "Events Processing may be necessary in certain cases (conditional)",
      "condition": "When specified as necessary",
      "impact": "Requires special handling"
    },
    {
      "exception": "Snackwise customer pays via ACH and is slower to pay, more difficult to work with",
      "condition": "When dealing with Snackwise customer",
      "impact": "Payment timing and collection expectations differ"
    },
    {
      "exception": "Snackwise is potentially being phased out",
      "condition": "Future state consideration",
      "impact": "May affect long-term processing decisions"
    }
  ],
  "merchant_specific": [
    {
      "element": "PO Number field sensitivity",
      "description": "This merchant treats PO Numbers as extremely sensitive requiring invoice-level updates from garage system",
      "customization_needed": true
    },
    {
      "element": "Customer base serves Meta",
      "description": "Two main customers (Snackwise and Canteen) both serve Meta at different offices",
      "customization_needed": true
    },
    {
      "element": "Blocked customer names",
      "description": "Specific Brewbird entities (HQ, Eng, Service) must not be processed",
      "customization_needed": true
    },
    {
      "element": "Payment methods by customer",
      "description": "Snackwise uses ACH payment method specifically",
      "customization_needed": true
    },
    {
      "element": "Approval workflow",
      "description": "Currently requires Jess to approve invoices individually; merchant wants auto-approve and Slack approval features",
      "customization_needed": true
    },
    {
      "element": "Feature requests",
      "description": "Customize payment method options by end-customer, customized dunning by end-customer, faster turnaround from order PO to invoice",
      "customization_needed": true
    },
    {
      "element": "Terminology: 'garage'",
      "description": "Merchant-specific system or interface called 'garage' where PO Numbers should be updated",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

