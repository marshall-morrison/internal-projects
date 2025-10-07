# Raw LLM Analysis: [DRAFT] 2X MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:56:17

---

## Chunk 1: [DRAFT] 2X MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:56:17

### Original Content
```
Steps to process Where amendments exist, ensure original BTs are adjusted or supplemented according to the amendment's changes Can process net new BTs from amendments under the amendment instance in garage Billing Start Date Use the contract start date or onboarding start date, whichever is explicitly listed for each service period When contracts says  will start X weeks or months from signature date,  make this calculation to determine when the individual BT will start Use the largest time unit...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Management",
    "Date Calculation and Service Period Determination",
    "Amendment Processing and Contract Modifications",
    "Pricing and Fee Structure Extraction",
    "Invoice Terms and Payment Conditions"
  ],
  "rules": [
    "When amendments exist, original BTs must be adjusted or supplemented according to amendment changes",
    "Net new BTs from amendments can be processed under the amendment instance in garage",
    "Billing Start Date should use contract start date or onboarding start date, whichever is explicitly listed",
    "When contract specifies X weeks/months from signature date, calculate to determine individual BT start date",
    "Use the largest time unit listed (e.g., if 4-6 weeks, use 6 weeks)",
    "Service Start Date equals Billing Start Date",
    "For monthly services, default to 12 months unless specified otherwise",
    "Open-ended terms default to 12 months",
    "Round up short-term BTs: 2 weeks = 1 month, 6 weeks = 2 months",
    "Frequency should be determined primarily from invoicing terms section",
    "For fixed fees for deliverables, use 'None' as frequency",
    "Extract Net Terms from invoicing terms section",
    "If Net Terms not stated, default to 30 days",
    "Use quantity of 1 for all items",
    "Item Name should use main service description",
    "Item Description is optional unless needed to distinguish similar BTs",
    "Total Price should use monthly fee or fixed project fee as listed (use total amount)",
    "Discounts must be separate negative BTs",
    "When amendment supersedes previous fees, adjust prior BTs to end before amendment date and add new BTs per amendment"
  ],
  "exceptions": [
    "Shorter BTs like onboarding use specific time frames with rounding rules rather than default 12 months",
    "Fixed fee deliverables use 'None' frequency instead of standard frequency determination",
    "When time frame is not listed, use best judgement instead of defaulting to 12 months",
    "Item Description is optional and only used when helpful to distinguish between similar BTs",
    "Amendments require special handling: ending prior BTs and creating new ones with adjusted dates"
  ],
  "merchant_specific": [
    "Service descriptions and naming conventions (e.g., 'Marketing Execution Team', 'Creative & Design Project')",
    "Contract signature date and calculation methods for start dates",
    "Specific invoicing terms language and payment term variations",
    "Amendment structure and how amendments are documented",
    "Time frames for onboarding and service delivery periods",
    "Discount structures and how they are presented in contracts",
    "The 'garage' system reference for processing amendments",
    "Specific service types and their typical duration patterns"
  ],
  "confidence_score": 0.92
}
```

---

