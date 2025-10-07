# Raw LLM Analysis: Merchant Info Sheet - Talkable

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:35:20

---

## Chunk 1: Merchant Info Sheet - Talkable_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:35:20

### Original Content
```
Merchant Scoping start date: 3 20 24 Implementation Completed Date (Go live date): Apr 3, 2024 MSA Signature Date: Mar 29, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Sun Choi (fractional CFO) Arra and Gail: outsourced accounting clerks (Philippines) Arra is more active here, she manages most of the day to day billing Kate: New accounting manager (Poland) Unsure of her exact role yet  Company summary Talkable offers referral marketing software solutions, enabling businesses to cre...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Implementation Timelines",
    "Billing Frequency and Payment Terms",
    "Contract End Date Management and Renewals",
    "Customer Information and Organizational Structure",
    "Professional Services and Billing Item Exclusions"
  ],
  "rules": [
    {
      "rule": "Default to signature date for launch/live date if no kick-off call or launch date is defined and there is no implementation or pilot period",
      "category": "Implementation Dates"
    },
    {
      "rule": "Default to 1 month implementation period if no implementation date or time period is listed",
      "category": "Implementation Dates"
    },
    {
      "rule": "For contracts with end date in the past, set end date to 6 months from processing date in garage",
      "category": "End Date Management"
    },
    {
      "rule": "For contracts without an end date, set end date to 6 months from processing date in garage",
      "category": "End Date Management"
    },
    {
      "rule": "Default to net 30 payment terms when no net payment terms are specified",
      "category": "Payment Terms"
    },
    {
      "rule": "For contracts billed monthly during implementation then full for continuation period, continue with most recent billing frequency if contract extends past term",
      "category": "Billing Frequency"
    },
    {
      "rule": "For amendments with no original MSA and no payment/frequency specified, continue with most recent billing frequency and net terms",
      "category": "Amendments"
    },
    {
      "rule": "Do not add professional services as billing templates (BTs) - merchant manages these manually",
      "category": "Billing Items"
    },
    {
      "rule": "Do not process BTs for 'management' or 'engineering'",
      "category": "Billing Items"
    },
    {
      "rule": "Integration item determined by Business segments column (column A) in spreadsheet",
      "category": "Integration"
    },
    {
      "rule": "All items for a specific customer should correspond to segment identified: SMB, MID, or ENT",
      "category": "Customer Segmentation"
    },
    {
      "rule": "Column I 'Prepayment end date' refers to next billing date for annual, semi-annual and quarterly billing",
      "category": "Billing Dates"
    },
    {
      "rule": "Look at peach row at top of regular order form documents for customer names",
      "category": "Customer Information"
    }
  ],
  "exceptions": [
    {
      "exception": "For contracts with end date in the future but potentially ending within next few months, go by contract end date unless notified otherwise",
      "condition": "End date is in future but within few months"
    },
    {
      "exception": "Merchant will notify if customer canceled, sent amendment, or sent renewal agreement for contracts with past end dates",
      "condition": "Contract end date management"
    },
    {
      "exception": "If contract extends past original term for monthly-then-full billing pattern, continue with most recent frequency",
      "condition": "Contract extension beyond original term"
    },
    {
      "exception": "Professional services are excluded from automated billing templates",
      "condition": "Professional services items"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: Talkable",
      "type": "Company Identity"
    },
    {
      "element": "Key contacts: Sun Choi (fractional CFO), Arra and Gail (outsourced accounting clerks, Philippines), Kate (accounting manager, Poland)",
      "type": "Personnel"
    },
    {
      "element": "Business model: Referral marketing software solutions",
      "type": "Business Description"
    },
    {
      "element": "Billing volume: About 50 bills per month",
      "type": "Volume Metrics"
    },
    {
      "element": "Contract structure: Frequently have ToS MSA + order form (2 separate docs), Mix of annual/quarterly/monthly",
      "type": "Contract Structure"
    },
    {
      "element": "Customer segmentation: SMB, MID, ENT (three tiers)",
      "type": "Segmentation Model"
    },
    {
      "element": "Spreadsheet reference: Column A for Business segments, Column I for Prepayment end date",
      "type": "Data Management"
    },
    {
      "element": "Communication channels: Slack or email for implementation date communication",
      "type": "Communication Preferences"
    },
    {
      "element": "Feature requests: Rev rec, ARR reporting, Custom dunning with automated escalations, Late fees capability",
      "type": "Future Requirements"
    },
    {
      "element": "Visual identifier: Peach row at top of order forms for customer names",
      "type": "Document Format"
    },
    {
      "element": "Implementation dates: Scoping start 3/20/24, Go live 4/3/24, MSA signature 3/29/24",
      "type": "Timeline"
    }
  ],
  "confidence_score": 0.88
}
```

---

