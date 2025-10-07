# Raw LLM Analysis: [DRAFT] Trustero MIS

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:56:56

---

## Chunk 1: [DRAFT] Trustero MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:56:56

### Original Content
```
Contract Processing Steps (Ops to fill) 1 Steps to process BTs are most commonly found in the Products and Services and or in the Statement of Work sections Will likely be in a table but also check SoW sections to see if any additional BTs Billing start date: Use the Effective Date or the Purchased Date Range Start as the Billing Start Date unless the contract explicitly lists a different invoice start date Example language: "Purchased Date Range: Mar 31, 2025 - Mar 30, 2026"   Billing Start Dat...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Processing",
    "Billing and Service Date Determination",
    "Pricing and Payment Terms Configuration",
    "Item Filtering and Exclusion Logic",
    "Integration Mapping and Matching"
  ],
  "rules": [
    "BTs (Billing Terms) are typically found in Products and Services or Statement of Work sections",
    "Check both tables and SoW text sections for BTs",
    "Billing start date defaults to Effective Date or Purchased Date Range Start unless explicitly stated otherwise",
    "Service start date follows same logic as billing start date unless contract implies different logic",
    "Months of service should be calculated from date range when available",
    "Use keyword search for term length if date range unavailable",
    "Always use total amount, ignore unit prices",
    "Frequency is determined from invoice terms or other contract language",
    "Net terms default to 30 days if not explicitly stated",
    "Due on receipt equals 0 net terms",
    "Quantity uses explicitly listed value from pricing table, defaults to 1 if not listed",
    "One-time usage BTs should be ignored",
    "Audit pricing available per request should be ignored",
    "Integration items should match language from item name to available integration items",
    "Leave integration item blank if no clear match exists",
    "Late fees should be ignored"
  ],
  "exceptions": [
    "Billing start date may differ if contract explicitly lists a different invoice start date",
    "Service start date may differ from billing start date if contract logic implies otherwise",
    "Additional usage BTs that appear to be one-time should be excluded (e.g., per-unit pricing for additional tests)",
    "SOC 2 Type II Audit items marked as 'not part of this SOW' should be ignored",
    "Items with pricing 'available per request' should be excluded"
  ],
  "merchant_specific": [
    "Trustero-specific terminology: 'Trustero Compliance as a Service Platform', 'Trustero certified US based auditor'",
    "Trustero-specific product names: 'Trustero Compliance Service Platform - Annual License'",
    "Trustero-specific usage items: 'Audit test', 'Basic question', 'Advanced question'",
    "Integration item catalog appears to be merchant-specific and requires matching against available options",
    "BT (Billing Terms) terminology may be organization-specific",
    "Document section names may vary: 'Products and Services', 'Statement of Work' (SoW)"
  ],
  "confidence_score": 0.92
}
```

---

