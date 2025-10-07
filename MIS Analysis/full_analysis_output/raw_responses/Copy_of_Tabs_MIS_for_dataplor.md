# Raw LLM Analysis: Copy of Tabs MIS for dataplor

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 09:54:47

---

## Chunk 1: Copy of Tabs MIS for dataplor_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:54:47

### Original Content
```
Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) If the contract looks like the screenshot below, follow the steps, use the red font as a guide to where to find information Example of Order Template of Data Services and Fees (Garage example) Service Start Date: Order effective date Months of Service: Refer to the order term Item Name: Fees Item Description: Include the countries listed (or anywhere that lists the countries territories that are included) Int...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract data extraction and field mapping",
    "Service billing configuration and pricing structure",
    "Date handling and term calculation for contracts",
    "Default values and fallback rules for missing information",
    "Contract type-specific processing workflows"
  ],
  "rules": [
    "Service Start Date must be extracted from order effective date or first paragraph of contract",
    "Quantity field defaults to 1 unless otherwise specified",
    "Item Description must include countries/territories listed in the contract",
    "Billing Type should be set to 'Flat' for the contract types shown",
    "Total Price should reflect individual year pricing, not cumulative total",
    "Months of Service should refer to the order term duration",
    "For multi-year contracts, create separate line items for each year (e.g., 'year 1', 'year 2')",
    "Start Date for subsequent years calculated as 1 year after previous start date unless contract specifies otherwise",
    "Periods field defaults to 1 unless contract indicates otherwise",
    "Frequency must be verified from contract terms (yearly vs monthly vs one-time)",
    "Payment terms should be extracted from 'PAYMENT TERMS' section",
    "Default Service Term is 1 Year when not specified in contract",
    "Default Net Payment Terms is 0 when not specified in contract",
    "Default Billing Frequency is Monthly when not specified in contract",
    "Tax line items default to 'BT' (Billing Type) when not otherwise specified",
    "When EXHIBIT date exists, use it as Service Start Date with term ending based on subscription date",
    "Red font indicators in screenshots serve as guides for information location"
  ],
  "exceptions": [
    "EXHIBIT date overrides standard Service Start Date extraction method",
    "Multi-year contracts require separate line items per year rather than single entry",
    "One-time charges require verification that contract doesn't state yearly/monthly frequency",
    "Second year start dates may deviate from standard 1-year increment if contract wording specifies different timing",
    "Contract-specific date ranges (e.g., May 5th, 2023 - December 27th, 2025) override standard term calculations"
  ],
  "merchant_specific": [
    "Contract template types vary by merchant (e.g., 'Order Template of Data Services and Fees' vs 'REPRESENTATIONS contract')",
    "Screenshot layouts and red font guide locations are template-specific",
    "Country/territory inclusion requirements in Item Description field",
    "Payment structure variations (single payment vs multi-year split payments)",
    "Contract section naming conventions (e.g., 'PAYMENT TERMS' section location)",
    "Specific date formats and contract paragraph structures",
    "Integration Item field requirements (appears merchant/system specific)",
    "Garage-specific examples suggest merchant-specific contract formats"
  ],
  "confidence_score": 0.92
}
```

---

