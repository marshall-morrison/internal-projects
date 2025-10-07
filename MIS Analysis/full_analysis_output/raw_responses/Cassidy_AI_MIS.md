# Raw LLM Analysis: Cassidy AI MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:56:28

---

## Chunk 1: Cassidy AI MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:56:28

### Original Content
```
Velo handles their day to day of invoicing and billing but John (and his CEO Justin) care about the reporting
```

### LLM Analysis Response
```json
{
  "themes": [
    "Division of responsibilities between service provider and client",
    "Financial operations management (invoicing and billing)",
    "Reporting and analytics requirements",
    "Stakeholder engagement and priorities"
  ],
  "rules": [
    "Velo is responsible for day-to-day invoicing operations",
    "Velo is responsible for day-to-day billing operations",
    "Reporting must be provided to satisfy client leadership requirements",
    "John and Justin (CEO) are the primary stakeholders for reporting deliverables"
  ],
  "exceptions": [
    "While Velo handles operational tasks (invoicing/billing), reporting remains a client-facing priority that requires special attention",
    "CEO-level involvement suggests reporting may require higher standards or different format than standard operational outputs"
  ],
  "merchant_specific": [
    "Client contact name: John",
    "Client CEO name: Justin",
    "Service provider name: Velo",
    "Specific operational scope: invoicing and billing handled by Velo",
    "Reporting audience: John and Justin specifically",
    "Organizational structure: John reports to or works with CEO Justin"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Cassidy AI MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:56:34

### Original Content
```
Merchant Name: Cassidy AI Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters",
    "Merchant-Specific Billing Model and Revenue Recognition",
    "Stakeholder Communication and Handoff Procedures",
    "Implementation and Post-Go-Live Documentation Requirements"
  ],
  "rules": [
    {
      "category": "Default Parameters",
      "rule": "Default Service Term is 1 Year if none listed",
      "source": "Ops Default"
    },
    {
      "category": "Default Parameters",
      "rule": "Default Net Payment Terms is 0 if none listed",
      "source": "Ops Default"
    },
    {
      "category": "Default Parameters",
      "rule": "Default Billing Frequency is Monthly if none listed",
      "source": "Ops Default"
    },
    {
      "category": "Tax Handling",
      "rule": "Every tax line item becomes a BT (Billable Transaction) if no other instruction listed",
      "source": "Ops Default"
    },
    {
      "category": "Revenue Recognition",
      "rule": "Revenue for the whole contract is straightlined across the period",
      "source": "Merchant-specific (Cassidy AI)"
    },
    {
      "category": "Billing Model",
      "rule": "Annual upfront contracts that contain seats",
      "source": "Merchant-specific (Cassidy AI)"
    },
    {
      "category": "Billing Model",
      "rule": "No proration or usage style billing - only flat SaaS",
      "source": "Merchant-specific (Cassidy AI)"
    },
    {
      "category": "Billing Model",
      "rule": "Do not charge for overages",
      "source": "Merchant-specific (Cassidy AI)"
    },
    {
      "category": "Contract Changes",
      "rule": "If a customer vastly exceeds their contracted amount, a new contract is signed for the new amount (also billed upfront and annually, then straightlined)",
      "source": "Merchant-specific (Cassidy AI)"
    }
  ],
  "exceptions": [
    {
      "exception": "Overage handling - explicit instruction NOT to charge for overages (differs from typical SaaS billing)",
      "context": "Cassidy AI billing model"
    },
    {
      "exception": "Contract backdating - some merchants may request invoice dates always be backdated to final day of the month",
      "context": "Example of contract-specific processing variation"
    },
    {
      "exception": "Integration item labeling varies by merchant (e.g., Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')",
      "context": "Integration Items Processing"
    },
    {
      "exception": "When customers vastly exceed contracted amounts, new contracts are created rather than charging overages",
      "context": "Cassidy AI specific contract expansion process"
    }
  ],
  "merchant_specific": [
    {
      "element": "POC contacts",
      "description": "Implementation POC (IM to fill), CX POC (IMP to Add), Customer Success contact (e.g., Azmat Aziz for Messari example)",
      "customizable": true
    },
    {
      "element": "Billing model details",
      "description": "How merchant bills, contract structure, customer creation process",
      "customizable": true
    },
    {
      "element": "Contract processing specifics",
      "description": "Items to ignore, backdating rules, merchant-requested processing variations",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Specific labels for different integration types per merchant",
      "customizable": true
    },
    {
      "element": "Post-processing notifications",
      "description": "Who to notify, when, and where (e.g., internal merchant channels)",
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos, invoice changes based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Merchant temperament",
      "description": "Understanding key stakeholder preferences and priorities (e.g., John prefers simplicity, cares about reporting)",
      "customizable": true
    },
    {
      "element": "Feature priorities",
      "description": "Which features the key POC cares about most",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

