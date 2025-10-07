# Raw LLM Analysis: Glacier MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:29:00

---

## Chunk 1: Glacier MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:29:00

### Original Content
```
Tab 1 Merchant Name : Glacier Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Each customer agreement generally includes: Down payments Installation Fees S...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing term (BT) extraction and processing",
    "Service date and billing schedule calculation",
    "Pricing and quantity calculations for contract items",
    "Renewal and subscription term extensions",
    "Default values and assumptions for missing contract information"
  ],
  "rules": [
    "All billing terms (BTs) are generally found under Exhibit A - Product Order Form at the bottom of contracts",
    "Each customer agreement typically includes: Down payments, Installation Fees, Setup Fees, Shipping, Hardware Purchase Fees (multi-year), Software Service Plan Fees (subscription model)",
    "For ongoing renewals, extend software service plan fees (subscriptions) by 3 years - this does NOT apply to Hardware or Scanner BTs",
    "Item Name should use the labeled product title, typically italicized (e.g., 'Robotic Hardware', 'Robot Service Plan')",
    "Item Description should be left as None",
    "Quantity: If BT price is 'per' an event (e.g., per Robotic Hardware), use the quantity provided in the Products section table; default to 1 if no quantity needed",
    "Total Price: For 'per' event BTs, multiply by the appropriate quantity; use net prices only and ignore discounts; include $0 BTs if listed",
    "Service Start Date: Will be contract effective date for most BTs",
    "Months of Service calculation: Take learning term length + subscription term length + 3 years if renewal exists",
    "Net Terms: Use terms stated in agreement (e.g., 'due 30 days after invoice'); otherwise default to 30 days",
    "Always honor 'For the avoidance of doubt' billing schedules if they exist",
    "Pay close attention to quantities in Products table and how they affect total price",
    "Use net prices only, ignore discounts"
  ],
  "exceptions": [
    "Service Start Date exceptions: For Downpayment, Installation, Setup, and Shipping - use the date delivered (billing start date) instead of contract effective date",
    "Months of Service exceptions: For Downpayment, Installation, Setup, and Shipping - use 0 months instead of standard calculation",
    "When contract says 'Purchase date', assume this is 1 year after the effective date",
    "For contracts with scanner and hardware (unless stated otherwise), assume scanner invoices are quarterly",
    "If contract includes 'For the avoidance of doubt' language regarding billing schedule, follow it directly",
    "Default billing start dates when contract isn't explicit: Downpayment (Effective date), Shipping (30 days after effective date), Installation (60 days after effective date), Hardware (1 year after effective date), Subscription and Service Fees (1 year after effective date)",
    "Frequency: If one-time payment, use 'None' instead of 'Annual'"
  ],
  "merchant_specific": [
    "Merchant Name: Glacier (POC fields to be filled by IM and IMP teams)",
    "Contract structure may vary: unique customer creation process, billing methods, contract breakdown",
    "Product-specific terminology: 'Robotic Hardware', 'Robot Service Plan', 'Software Analytics Subscription Fees', 'Scanner'",
    "Learning Term and Subscription Term periods (merchant-specific contract phases)",
    "Exhibit A - Product Order Form location may vary by merchant",
    "Specific processing requests that may differ by contract (noted as incomplete in document)",
    "Reference examples (1, 2, 3) mentioned but not included in this chunk"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Glacier MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:29:02

### Original Content
```
always back-date invoice date to final day of the month) How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) What are the instructions for assigning integration items Example: All Statsig integrations item...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Processing and Tax Handling",
    "Integration Item Classification and Labeling",
    "Post-Processing Communication Protocols",
    "Merchant-Specific Billing Structure and Milestones",
    "Implementation Handoff and Customer Relationship Management"
  ],
  "rules": [
    {
      "rule": "Always back-date invoice date to final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "If no tax handling specified, default is every tax line item becomes a BT (Business Tax)",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Events Processing section must be filled by Implementation Success team Post-Go Live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Integration Items Processing section must be filled by Implementation Success team Post-Go Live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Post Processing Communications section must be filled by Implementation Success team Post-Go Live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success team Post-Go Live",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Feature Requests must be filled by AE prior to Implementation handoff, by Implementation prior to go-live, and by Success Post-Go Live",
      "category": "Documentation Requirements",
      "explicit": true
    },
    {
      "rule": "Merchant Calls recordings must be documented by AE prior to Implementation involvement, by Implementation prior to go-live, and by Success Post-Go Live",
      "category": "Documentation Requirements",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Integration item labeling can be overridden by merchant specification",
      "context": "Pinata integration items default to 'Software Subscription Bundle' unless otherwise noted by Merchant"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "context": "Customer Information section notes potential invoice changes due to merchant customer relationship"
    },
    {
      "exception": "Notification requirements vary by merchant phase (Implementation vs Active)",
      "context": "Example shows Customer Success notification needed when contracts are processed in Active phase"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing structure with three-stage payment model",
      "details": "Upfront fee on signing, shipping/installation fee after few months, success metric fee once machine hits predefined metric",
      "customizable": true
    },
    {
      "element": "Milestone billing requirements",
      "details": "Payment tied to specific contract-defined success metrics",
      "customizable": true
    },
    {
      "element": "Customer notification preferences",
      "details": "Who needs to be notified, where (e.g., internal merchant channel), and when (e.g., after contract processing)",
      "customizable": true
    },
    {
      "element": "Integration item categorization",
      "details": "Merchant-specific labeling for integration items (e.g., Statsig, Pinata)",
      "customizable": true
    },
    {
      "element": "Merchant temperament and relationship notes",
      "details": "Personal relationships (co-founder connections), communication style, current processes",
      "customizable": true
    },
    {
      "element": "Current billing method",
      "details": "Manual billing via Stripe, spreadsheet-based tracking, need for automation",
      "customizable": true
    },
    {
      "element": "Key stakeholder identification",
      "details": "Point of contact (Ally - Chief of Staff), decision makers, feature priorities",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

