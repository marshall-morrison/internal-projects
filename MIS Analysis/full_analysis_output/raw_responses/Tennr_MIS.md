# Raw LLM Analysis: Tennr MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:30:54

---

## Chunk 1: Tennr MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:54

### Original Content
```
Merchant Name: Tennr Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Rules Add billing information to customer If the  Add-on  agreement doesn t have a sta...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Creation",
    "Price and Quantity Normalization Based on Billing Frequency",
    "Product Naming and Description Standardization",
    "Revenue Recognition and Service Period Calculation",
    "Multi-year Contract Handling and Add-on Agreements"
  ],
  "rules": [
    "Add billing information to customer for all contracts",
    "Process each item listed under the pricing section as a separate Billing Term (BT)",
    "For professional services/implementation products, use 12 months for revenue recognition regardless of multi-year contract length",
    "Multi-year products can be combined into one BT if price and quantity are the same",
    "Use stated product/service name from contract for Item Name",
    "Keep naming conventions consistent: use 'Implementation Fee' for managed services or professional services",
    "Mark integration item for all BT",
    "Use specified unit quantity if stated, otherwise default to 1",
    "For quarterly billing: divide annual net price by 4",
    "For monthly billing: divide annual net price by 12",
    "For annual billing: multiply monthly price by 12",
    "Divide quantity by billing frequency if quantity is per year",
    "Use net price if discount is applied",
    "If price is $0 due to 100% discount or waived period, still process the BT and set price to 0",
    "Item Description should include the specified unit quantity if stated",
    "If no quantity is specified (e.g., Implementation Fee or Platform Fee), default Quantity to 1",
    "Billing terms appear in the pricing tables of the Order Form (generally labeled by year)",
    "Locate billing terms in Order Form pricing tables"
  ],
  "exceptions": [
    "If Add-on agreement doesn't have a stated end date, refer to the previous contract and use that end date",
    "Multi-year products can be combined into one BT only if price and quantity remain the same",
    "Professional services products (implementations) always use 12 months for rev rec, even for multi-year contracts",
    "Process BT even when price is $0 due to discounts or waived periods"
  ],
  "merchant_specific": [
    "Merchant Name field (to be filled)",
    "Implementation POC field (IM to fill)",
    "CX POC field (IMP to Add)",
    "Billing model section (Implementation to fill)",
    "Unique customer creation process information",
    "Merchant-specific billing information",
    "Contract structure and breakdown",
    "One-off merchant-specific considerations",
    "Contract Processing Steps (Implementation Success to fill Post-Go Live)",
    "Product names may vary by merchant (e.g., 'Tennr Premium Plus', 'Patient Intake Volume', 'Provider Engagement Coordinator', 'Base Platform Fee')",
    "Specific line items and services vary by merchant (e.g., Qualification Checks, Runs, Document Wrangling, Intake)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Tennr MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:30:55

### Original Content
```
, 29 months, 12 months) Revenue is still recognized in free months so in the example below: You would have to create BT for each product in each pay period Months of service for the first pay period is 18 (7 31 2025 - 1 30 2027) Billing ends 7 30 2026 (4 periods at 3 month frequency for quarterly) Months of service for the second pay period is 12 (1 31 2027 - 1 30 2028) Example contract: ac4022a7-b8ae-40f8-be91-7006602bed43 Service Start Date Use stated start date Billing Start Date Use the "Con...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Creation and Revenue Recognition",
    "Service and Billing Start Date Determination",
    "Free/Complimentary Period Handling",
    "Implementation and Post-Processing Workflows",
    "Merchant-Specific Billing Configurations"
  ],
  "rules": [
    "Revenue is recognized even during free months",
    "Create separate BT for each product in each pay period",
    "Service Start Date: Use stated start date from contract",
    "Billing Start Date: Use Contract Start Date unless there is a stated waived/complimentary period",
    "Free periods are calculated by subtracting full term years from total months (e.g., 29 months - 24 months = 5 months free)",
    "Frequency mapping: Quarterly → Quarterly, Annually → Annual, One-time implementation fees → None",
    "Implementation Fee products follow the same frequency as other products unless specific cadence is stated",
    "Net Terms: Use terms listed under 'Payment Terms' (e.g., Net 30)",
    "If Net Terms not listed, default to Net 30",
    "Overages are currently being ignored",
    "Events Processing section to be filled by Implementation Success Post-Go Live",
    "Integration Items Processing section to be filled by Implementation Success Post-Go Live",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Post Processing Communications section to be filled by Implementation Success Post-Go Live"
  ],
  "exceptions": [
    "Edge Case - Nationwide: Different pricing for different pay periods within same contract (3 years, 6 months free, billed quarterly with escalating prices)",
    "When billing starts on contract start date, free period is at the end; otherwise free period may be at the start",
    "Tenner is pushing to standardize free months at the start for future contracts",
    "Implementation Fee products may have specific billing cadence stated that overrides default frequency",
    "Special memos may be required for certain invoices based on merchant-customer relationship",
    "Invoice changes may be needed due to merchant customer relationship"
  ],
  "merchant_specific": [
    "Contract reference example: ac4022a7-b8ae-40f8-be91-7006602bed43",
    "Merchant contact: Enrique (main contact, detailed, straightforward, laid back but sharp)",
    "Merchant billing model: Implementation (one-time) + Subscription flat fee with minimum commit",
    "5-6 different products including: document intake (# of intakes), Benefits (# of verified transactions)",
    "Unique payment terms per merchant",
    "Not currently charging for overages",
    "Merchant is an AI company interested in AI agents feature",
    "Customer Success contact: Azmat Aziz",
    "Notification requirement: Customer Success needs notification in Messari internal merchant channel when contracts are processed in Active phase",
    "Merchant call history with specific dates (July 9-28) and topics",
    "Merchant phase tracking: Implementation → Active"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: Tennr MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:31:03

### Original Content
```
-Matthew is their owner of SFDC We did not meet with him during the sales process - Their external accounting will be the day-to-day operators of Tabs I am unsure who their other client is but someone else they support uses Tabs today 3) What are the Tabs features that the key POC cares about SFDC integration QB integration Stripe integration Reporting
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder identification and roles",
    "Third-party system integrations",
    "External operational management",
    "Product feature requirements",
    "Sales process and client relationships"
  ],
  "rules": [
    "External accounting teams will serve as day-to-day operators of the Tabs platform",
    "SFDC (Salesforce) integration is a required feature",
    "QuickBooks (QB) integration is a required feature",
    "Stripe integration is a required feature",
    "Reporting functionality is a required feature",
    "Key stakeholders may not be involved in initial sales process",
    "External accounting firms may support multiple clients using the same platform"
  ],
  "exceptions": [
    "Owner (Matthew) was not met during the sales process - deviation from standard sales engagement",
    "Day-to-day operations will be handled by external party rather than internal staff",
    "External accounting firm has prior experience with Tabs through another client (unidentified)"
  ],
  "merchant_specific": [
    "Owner name: Matthew",
    "Owner's role: SFDC owner",
    "Operational model: External accounting firm as operators",
    "Specific integration requirements: SFDC, QB, Stripe",
    "Point of contact (POC) priorities may vary by merchant",
    "Accounting firm relationship and existing Tabs experience",
    "Identity of other client supported by the accounting firm is unknown/unspecified"
  ],
  "confidence_score": 0.75
}
```

---

