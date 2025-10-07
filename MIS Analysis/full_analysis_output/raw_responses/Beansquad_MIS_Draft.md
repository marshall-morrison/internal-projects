# Raw LLM Analysis: Beansquad MIS Draft

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:04:31

---

## Chunk 1: Beansquad MIS Draft_chunk_0

**Chunk Type**: general  
**Analysis Time**: 2025-10-02 10:04:31

### Original Content
```
BeanSquad primarily bills merchants on flat monthly fees based on annual contracts, with some ad hoc service work billed separately BTs can be found in the Scope of Work Section (screenshot below) The BTs for a standard contract will primarily consist of only a one-time set-up fee, a monthly bookkeeping fee and a late fee Additional BTs will be specified For example, sales tax filing in the screenshot Service start date: effective date Total months of service: found in Term section Will usually ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing structure and fee types for merchant contracts",
    "Contract term identification and date extraction",
    "Billing term (BT) configuration and processing rules",
    "Payment terms and net terms determination",
    "Document section mapping for data extraction"
  ],
  "rules": [
    "BeanSquad uses flat monthly fees based on annual contracts with separate ad hoc service billing",
    "Billing terms (BTs) are located in the Scope of Work Section",
    "Standard contracts include: one-time setup fee, monthly bookkeeping fee, and late fee",
    "Service start date equals the effective date from the contract",
    "Total months of service is found in the Term section and is usually 12 months",
    "Billing start date must be explicitly listed for each billing term; if not listed, use the effective date",
    "One-time setup fees have 'None' for number of periods",
    "All other fees must state their frequency explicitly",
    "Number of periods should cover the full term length",
    "Net terms are primarily found in 'Fees and Expenses; Payment Terms; Interest on Late Payments' section",
    "If net terms are not available in standard section, search document for associated keywords",
    "Default to 30-day net terms if no payment terms are listed",
    "Late fees should be processed as a percentage of the Past Due Amount",
    "Most contracts include late fees and they are typically monthly over the contract term",
    "Ignore any billing terms marked as N/A, waived, or free"
  ],
  "exceptions": [
    "Additional billing terms beyond standard three (setup, monthly bookkeeping, late fee) may be specified for services like sales tax filing",
    "Ad hoc service work is billed separately from standard monthly fees",
    "If billing start date is not explicitly listed, fall back to using the effective date",
    "If net terms cannot be found in standard section, perform keyword search before applying default",
    "Billing terms marked as N/A, waived, or free should be excluded from processing"
  ],
  "merchant_specific": [
    "Additional billing terms beyond the standard three (e.g., sales tax filing services)",
    "Specific billing start dates that differ from effective date",
    "Contract term length (though typically 12 months, may vary)",
    "Late fee percentage calculation method",
    "Custom net terms that differ from the 30-day default",
    "Frequency of recurring fees (monthly, quarterly, etc.)",
    "Number of periods for each billing term based on contract length"
  ],
  "confidence_score": 0.85
}
```

---

