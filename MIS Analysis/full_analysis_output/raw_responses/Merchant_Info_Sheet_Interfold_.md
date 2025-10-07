# Raw LLM Analysis: Merchant Info Sheet - Interfold_

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 12:21:20

---

## Chunk 1: Merchant Info Sheet - Interfold__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:21:20

### Original Content
```
Merchant Interfold Scoping start date: May 3, 2024 Implementation Completed Date (Go live date): May 10, 2024 MSA Signature Date: Feb 7, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant George Li - Co-Founder and CEO Company summary Interfold works with banks to make commercial lending easy  Solve your lending bottlenecks with digital experience and AI  so you can 2x loan volume and turnaround loans in days, not weeks AM Notes George and Ali have a personal relationship Billing model M...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Implementation and Timeline Management",
    "Billing Structure and Payment Terms",
    "Contract Processing Workflow",
    "Customer Setup and Integration",
    "Events-Based Billing Provisions"
  ],
  "rules": [
    {
      "rule": "Create customer in Garage (which auto-creates in QBO) if customer does not exist",
      "category": "Customer Setup",
      "explicit": true
    },
    {
      "rule": "Cancellation Policy is the most important Key Term to extract from contracts",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Create billing terms for both Pilot Period and Regular Period",
      "category": "Billing Setup",
      "explicit": true
    },
    {
      "rule": "All items should use the Integration Item 'Services'",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Verify if Regular Period is billed monthly or annually",
      "category": "Billing Setup",
      "explicit": true
    },
    {
      "rule": "Do not process events-based billing terms currently (despite contract provisions)",
      "category": "Events Processing",
      "explicit": true
    },
    {
      "rule": "No billing terms are necessary for per-user fees",
      "category": "Billing Setup",
      "explicit": true
    },
    {
      "rule": "Pilot periods are billed at lower amounts and billed monthly",
      "category": "Billing Model",
      "explicit": true
    },
    {
      "rule": "Post-pilot billing increases in amount and can be monthly or annually",
      "category": "Billing Model",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts include provisions for additional user fees (e.g., 'up to 7 users' for Prime Alliance Bank), but these are not currently processed as events",
      "condition": "Future capability for capturing growth beyond included users"
    },
    {
      "exception": "Pilot period billing differs from regular period billing in both amount and potentially frequency",
      "condition": "During pilot phase vs. post-pilot phase"
    },
    {
      "exception": "George and Ali have a personal relationship",
      "condition": "Account management consideration for this specific merchant"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model: platform fees as fixed monthly amount",
      "customizable": true,
      "note": "Merchant bills platform fees which are priced per month"
    },
    {
      "element": "Pilot vs. Regular Period pricing structure",
      "customizable": true,
      "note": "Pilot periods billed at lower amounts; regular periods may be monthly or annual"
    },
    {
      "element": "User capacity thresholds",
      "customizable": true,
      "note": "Example: Prime Alliance Bank contract includes 'up to 7 users'"
    },
    {
      "element": "Cancellation Policy terms",
      "customizable": true,
      "note": "Must be extracted from each contract as most important Key Term"
    },
    {
      "element": "Implementation timeline",
      "customizable": true,
      "note": "Scoping start, go-live date, and MSA signature dates vary by merchant"
    },
    {
      "element": "Key stakeholders and contacts",
      "customizable": true,
      "note": "George Li (Co-Founder/CEO) for Interfold; varies by merchant"
    },
    {
      "element": "Business model description",
      "customizable": true,
      "note": "Interfold works with banks for commercial lending; each merchant has unique business"
    }
  ],
  "confidence_score": 0.92
}
```

---

