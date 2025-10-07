# Raw LLM Analysis: Merchant Info Sheet - Talkable(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:05:10

---

## Chunk 1: Merchant Info Sheet - Talkable(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:05:10

### Original Content
```
Merchant Scoping start date: 3 20 24 Implementation Completed Date (Go live date): Apr 3, 2024 MSA Signature Date: Mar 29, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Sun Choi (fractional CFO) Arra and Gail: outsourced accounting clerks (Philippines) Arra is more active here, she manages most of the day to day billing Kate: New accounting manager (Poland) Unsure of her exact role yet  Company summary Talkable offers referral marketing software solutions, enabling businesses to cre...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Date Management and Service Periods",
    "Integration Item Classification and Business Segments",
    "Payment Terms and Billing Frequency Defaults",
    "Customer Information Management and Special Handling"
  ],
  "rules": [
    "Default to net 30 payment terms when no net payment terms are specified",
    "Use the 'Business segments' column (column A) to determine Integration Item (SMB, MID, or ENT)",
    "All items for a specific customer must correspond to the segment identified in column A",
    "Same integration item can be used for both Implementation and Contract Period",
    "Item Description field should be left blank",
    "Class field should be left blank",
    "Category field should be left blank",
    "For amendments with no original MSA contract and no net payment or frequency specified, continue with most recent billing frequency and net terms",
    "For contracts billed monthly during implementation then full for continuation period, if contract extends past term, continue with most recent billing frequency",
    "Do not add professional services as BTs (billing templates) - merchant manages these manually",
    "Do not process BTs for 'management' or 'engineering'",
    "Customer names should be taken from the peach row at the top of regular order form documents",
    "Service Start Date is determined by Implementation effective date (signature)",
    "Pilot Period starts at launch date (go live)",
    "Continuation Period begins at Pilot end date"
  ],
  "exceptions": [
    "Professional services included in contracts should not be added as BTs - managed manually by merchant",
    "No BTs should be processed for 'management' or 'engineering' items",
    "For contracts with mixed billing (monthly during implementation, then full for continuation), billing frequency changes after the initial term",
    "Amendments without original MSA contracts require special handling - inherit most recent billing frequency and net terms"
  ],
  "merchant_specific": [
    "Talkable offers referral marketing software solutions",
    "Approximately 50 bills per month volume",
    "Contracts frequently have ToS MSA and order form as 2 separate documents",
    "Mix of annual, quarterly, and monthly billing cycles",
    "Business segments: SMB, MID, ENT classification system",
    "Key personnel: Sun Choi (fractional CFO), Arra and Gail (outsourced accounting clerks in Philippines), Kate (accounting manager in Poland)",
    "Spreadsheet column I contains 'Prepayment end date' for annual, semi-annual and quarterly billing",
    "Custom dunning requirements: customized messaging and post-30 day automated escalations",
    "Interest in late fees (charging or threatening based on aging)",
    "Feature requests: Rev rec, ARR reporting, custom dunning",
    "Customer information stored in peach row at top of order form documents",
    "Implementation completed/Go live date: Apr 3, 2024",
    "MSA Signature Date: Mar 29, 2024"
  ],
  "confidence_score": 0.92
}
```

---

