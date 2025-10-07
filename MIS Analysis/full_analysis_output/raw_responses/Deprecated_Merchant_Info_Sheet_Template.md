# Raw LLM Analysis: [Deprecated] Merchant Info Sheet - Template

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:48:56

---

## Chunk 1: [Deprecated] Merchant Info Sheet - Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:48:56

### Original Content
```
USE THIS UPDATED VERSION INSTEAD HERE Merchant Scoping start date: 3 20 24 Implementation Completed Date (Go live date): Apr 3, 2024 MSA Signature Date: Mar 29, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant XYZ ABCD (fractional CFO) Company summary XYZ Co offers referral marketing software solutions, enabling businesses to create and manage referral programs that drive customer acquisition and retention effectively AM Notes N A Billing model Frequently have ToS MSA   order form (2 s...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Implementation Timeline Management",
    "Contract End Date Handling and Defaults",
    "Merchant Billing and Documentation Structure",
    "Contract Processing Workflow and Date Logic",
    "Merchant Profile and Business Context"
  ],
  "rules": [
    {
      "rule": "Default launch date to signature date if no kick off call or launch date is defined in contract",
      "category": "Implementation Dates"
    },
    {
      "rule": "Default to 1 month implementation date if no implementation date or time period is listed",
      "category": "Implementation Dates"
    },
    {
      "rule": "For contracts with end date in the past, set end date to 6 months from now and await merchant confirmation on status (cancelled, amended, or renewed)",
      "category": "End Date Processing"
    },
    {
      "rule": "For contracts without an end date, set end date to 6 months from today and await merchant confirmation",
      "category": "End Date Processing"
    },
    {
      "rule": "For contracts with future end date within next few months, use the contract end date unless notified otherwise",
      "category": "End Date Processing"
    },
    {
      "rule": "Merchant frequently has separate Terms of Service (ToS), MSA, and order form documents",
      "category": "Documentation Structure"
    },
    {
      "rule": "Billing occurs on mix of annual, quarterly, and monthly cycles",
      "category": "Billing Model"
    },
    {
      "rule": "Approximately 50 bills processed per month",
      "category": "Billing Volume"
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts with end dates in the past require special handling with 6-month extension",
      "condition": "End date is in the past"
    },
    {
      "exception": "Contracts with no end date receive automatic 6-month extension",
      "condition": "No end date specified"
    },
    {
      "exception": "Future end dates within few months are honored unless merchant provides updates",
      "condition": "End date is in near future"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: XYZ Co",
      "type": "Identity"
    },
    {
      "element": "Business type: Referral marketing software solutions",
      "type": "Business Model"
    },
    {
      "element": "Key contact: ABCD (fractional CFO)",
      "type": "Personnel"
    },
    {
      "element": "Scoping start date: March 20, 2024",
      "type": "Timeline"
    },
    {
      "element": "Go live date: April 3, 2024",
      "type": "Timeline"
    },
    {
      "element": "MSA Signature Date: March 29, 2024",
      "type": "Timeline"
    },
    {
      "element": "Approximately 50 bills per month",
      "type": "Volume Metric"
    },
    {
      "element": "Mix of annual, quarterly, and monthly billing cycles",
      "type": "Billing Configuration"
    },
    {
      "element": "Separate ToS, MSA, and order form documentation structure",
      "type": "Documentation Pattern"
    }
  ],
  "confidence_score": 0.85
}
```

---

