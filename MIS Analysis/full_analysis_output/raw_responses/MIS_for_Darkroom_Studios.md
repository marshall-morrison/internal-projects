# Raw LLM Analysis: MIS for Darkroom Studios

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:07:28

---

## Chunk 1: MIS for Darkroom Studios_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:28

### Original Content
```
g if the effective date is 5 8 and the monthly fee is  2,500 First billing period is 5 8 - 6 7 Prorated period is 6 8 - 6 30 so prorated amount is 2500 30 23   1916 66666667 1916 66666667 is the amount you would use Quantity: 1 Billing start date: the first of the partial month For the example above it would be 6 1 Number of periods: 1 Frequency: MONTH Net terms: Check this sheet for the customer and statement of work: https: docs google com spreadsheets d 1AxdIIN7sU86BNohK6F7q1udPDWpl5npYalHJj2...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Prorated billing calculations for partial months",
    "Billing term (BT) creation and configuration for recurring services",
    "Service start dates and billing cadence management",
    "Integration item mapping and product configuration",
    "Net terms determination and customer-specific billing rules"
  ],
  "rules": [
    "Prorated amount calculation: (monthly fee / days in month) × days in prorated period",
    "Prorated billing quantity is always 1",
    "Prorated billing start date is the first day of the partial month",
    "Prorated billing has 1 period with MONTH frequency",
    "Default net terms is 25 if customer/SOW not found in reference sheet",
    "Prorated billing timing: Bill first of period",
    "Remainder term fees go out on the 1st of the month",
    "Total months of service is 60 for all recurring service SOWs",
    "Item name should be 'Monthly Fees' or 'Management Fees'",
    "Item description uses the name of the SOW",
    "Billing type for remainder term is Flat",
    "Remainder term quantity is always 1",
    "Remainder term frequency is MONTH",
    "Integration items must be mapped using Product Mapping tab (column B to column C)",
    "Leave integration item blank if no product found in mapping sheet",
    "Net terms must be checked against customer and SOW reference sheet"
  ],
  "exceptions": [
    "If effective date is the 1st of the month with no prorated period: billing start date is the first of the month following the initial deposit billing period",
    "If effective date is the 1st of the month with no prorated period: number of periods is 59 instead of 58",
    "If SOW is non-recurring service: use stated term in contract instead of 60 months",
    "Unique invoicing schedules (e.g., x amount for first 2 months, y amount for remaining): create multiple BTs with only amount and number of periods changing",
    "If customer/SOW not in reference sheet: use net terms of 25 despite contract terms"
  ],
  "merchant_specific": [
    "Reference to specific Google Sheets for customer/SOW lookup and net terms",
    "Reference to specific Google Sheets for Product Mapping (column B to column C mapping)",
    "SOW (Statement of Work) naming conventions",
    "Item naming conventions: 'Monthly Fees' vs 'Management Fees'",
    "60-month standard term for recurring services",
    "Default net terms value of 25",
    "Integration item mapping process and product catalog",
    "Specific billing cadence patterns and unique invoicing schedules per customer"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS for Darkroom Studios_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:30

### Original Content
```
Merchant Name: Darkroom Studios Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General: MRR - pro ration of first month Burlebo started 22nd September start date ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing structure and Statement of Work (SOW) processing",
    "Initial deposit and first month fee billing procedures",
    "Prorated billing calculations and timing",
    "Product mapping and billing term configuration",
    "Merchant-specific implementation timelines and go-live dates"
  ],
  "rules": [
    "Billing terms are located under Statement of Work (SOW) sections in contracts",
    "Contracts may contain multiple SOWs that must be processed separately",
    "Look for Fees, Pricing, and Additional Payment Terms section in SOW",
    "Products are typically categorized as Monthly Fees, Management Fees, or Initial Deposit",
    "Every SOW must be billed: First month fee at signing, Prorated partial month (if applicable), Fees for remainder of term",
    "First month fee is due upon signing (last signature date)",
    "Initial deposit equals first month's fee - do NOT create separate billing terms for both",
    "MRR (Monthly Recurring Revenue) includes proration of first month",
    "NRR (New Recurring Revenue) has no proration",
    "Service start date should be set to the SOW Effective date",
    "Total months of service: 60 for all recurring service SOWs",
    "Initial Deposit billing term: Item name 'Initial Deposit', Billing type Flat, Quantity 1, Number of periods 1, Net terms 0, Billing timing 'Bill first of period'",
    "Frequency for initial deposit calculated in DAYS from last signature to end of first billing period (effective date + one month)",
    "First billing period defined as effective date + one month",
    "Merchant wants to bill on the 1st of the month for every month following first month",
    "Prorated partial month item name format: '[Fee Name] - Prorated Month'",
    "Integration items must be mapped using Product Mapping spreadsheet (Column B to Column C)",
    "Leave Integration Item blank if no product found in mapping sheet"
  ],
  "exceptions": [
    "No prorated partial month billing term if SOW effective date is the 1st of the month",
    "If SOW is non-recurring service, use stated term in contract instead of 60 months",
    "Net terms for initial deposit is 0, despite what contract may say",
    "If multiple SOWs exist and deposit allocation is unclear, flag to supervisor for merchant clarification"
  ],
  "merchant_specific": [
    "Implementation POC and CX POC fields need to be filled per merchant",
    "Billing model section requires implementation team customization",
    "Unique customer creation processes vary by merchant",
    "Contract structure and breakdown differs per merchant",
    "Specific merchant start dates listed: Burlebo (Sept 22), City Beauty Retention (Sept 29), Aunty Ranas (Sept 29), Biro (Sept 29), Lulus (Oct 1), Laundry Sauce (Sept 29), Fellow (Oct 6), Starwood (Oct 2)",
    "Merchant-specific billing examples provided (e.g., Burlebo billing cycle: Sep 29 - Oct 28, then Oct 29 - Oct 31)",
    "SOW names and fee structures are merchant-specific (e.g., 'Web Support (Recurring Service)')",
    "Contract reference example: 76d13680-43ab-448c-8c00-a3ce9e26696c",
    "Product mapping requires merchant-specific integration item identification"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: MIS for Darkroom Studios_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:43

### Original Content
```
id 4937769203243940908 Note there are other videos from prior conversations over the last  6 months, but the above 2 are the most relevant Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills   Invoice Cadence  70 invoices month, and growing (6 new clients signed already this month) Invoices are created manually in QuickBooks Online (QBO) A separate Google Sheet tracks due dates, invoice numbers, fees, payment status, and ACH authori...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Complex billing and proration requirements",
    "Manual invoice creation and payment tracking processes",
    "Multi-system tech stack integration needs",
    "Merchant temperament and relationship management",
    "Automation requirements for invoice generation and collections"
  ],
  "rules": [
    "Invoice volume: 70 invoices per month and growing",
    "Invoices must be created in QuickBooks Online (QBO)",
    "Google Sheet must track: due dates, invoice numbers, fees, payment status, and ACH authorization flags",
    "Each client requires custom contracts with unique billing terms",
    "Billing structure includes: monthly retainers (flat fees) and variable components (ad spend or revenue share)",
    "Proration calculation required for mid-month client starts",
    "Proration formula: Month 1 = full fee, Month 2 = prorated fee based on start date",
    "ACH-authorized clients: automatic deduction on due date",
    "Non-ACH clients: manual email follow-up required for collections",
    "Payments accepted via: ACH, checks, and other methods",
    "Manual reconciliation required for payments outside QBO",
    "Tech stack includes: QuickBooks Online (ERP), HubSpot (CRM), PandaDoc (Contracts), Google Sheets (tracking/cash flow)",
    "No current tax software or Stripe integration"
  ],
  "exceptions": [
    "Dynamic fee changes month-to-month (e.g., $3K MRR in Month 1, $5K in Month 2)",
    "Mid-month start dates requiring custom proration calculations (e.g., Aug 9 to Sep 1)",
    "Clients without ACH authorization require different collection process (manual follow-up)",
    "Payments received outside QBO system require special manual reconciliation",
    "Some contracts have variable components based on ad spend or revenue share instead of flat fees"
  ],
  "merchant_specific": [
    "Merchant name: Darkroom",
    "Key contacts: Ramy (detail-oriented, risk-aware decision maker) and Malak (pragmatic executor focused on automation)",
    "Current invoice volume: 70/month with 6 new clients signed in current month",
    "Merchant temperament: cautious but partnership-minded, requires confidence in automation before full trust",
    "Specific proration example: Aug 9 to Sep 1 calculation",
    "Specific fee examples: $3K MRR Month 1, $5K Month 2",
    "Merchant values: transparency, control, long-term relationship building, pricing alignment with current stage",
    "Current manual processes: Malak calculates prorations, enters data into sheets and QBO, sends follow-up emails",
    "Desired Tabs features: Automated invoice generation, proration/complex billing logic, collections/dunning automation, bank reconciliation/cash matching"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: MIS for Darkroom Studios_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:50

### Original Content
```
gid 991872617 gid 991872617  if the customer and statement of work is not in that sheet, use 25, despite what the contract may say Billing timing: Bill first of period Nuances Usage based BT do not need a prorated BT You can just start the BT on the first of the month of the effective date Billing timing: billed in arrears Example Contracts Eb9dbc57-872b-40a9-ad44-55de28b9b376 76d13680-43ab-448c-8c00-a3ce9e26696c SOW with different billing cadences C70c5558-ea78-4b1b-abc8-55ce021b8ef8 26ec8f4d-2...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing timing and cadence configuration",
    "Contract processing and default values",
    "Tax handling and line item processing",
    "Integration item labeling and categorization",
    "Post-processing communication workflows"
  ],
  "rules": [
    {
      "rule": "If customer and statement of work is not in the specified sheet, use 25 as default value regardless of contract terms",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Bill first of period for billing timing",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Usage-based billing terms (BT) do not require proration",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Start billing term on the first of the month of the effective date for usage-based billing",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Billing timing is billed in arrears",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "If no tax handling specified, Ops default is every tax line item becomes a billing term (BT)",
      "category": "tax_processing",
      "specificity": "explicit"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling",
      "specificity": "explicit"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "integration_labeling",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team fills in Events Processing section post-go-live",
      "category": "workflow_responsibility",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team fills in Integration Items Processing section post-go-live",
      "category": "workflow_responsibility",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team fills in Post Processing Communications section post-go-live",
      "category": "workflow_responsibility",
      "specificity": "explicit"
    },
    {
      "rule": "Account Executive (AE) fills feature requests prior to implementation handoff",
      "category": "workflow_responsibility",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation team fills feature requests prior to go-live",
      "category": "workflow_responsibility",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Default value of 25 can be overridden if customer and SOW are present in the designated sheet",
      "condition": "customer_and_sow_presence"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "merchant_override"
    },
    {
      "exception": "Merchant may request specific processing differences per contract (e.g., back-dating invoice date to final day of month)",
      "condition": "merchant_specific_request"
    },
    {
      "exception": "SOW with different billing cadences may have special handling",
      "condition": "multiple_billing_cadences",
      "reference_contracts": ["C70c5558-ea78-4b1b-abc8-55ce021b8ef8", "26ec8f4d-2fb4-4086-9df6-58aa42e92ef6"]
    }
  ],
  "merchant_specific": [
    {
      "element": "Default value lookup sheet for customer and SOW validation",
      "customization_type": "data_source"
    },
    {
      "element": "Integration item labeling rules (Statsig, Pinata examples provided)",
      "customization_type": "labeling_taxonomy"
    },
    {
      "element": "Post-processing notification requirements (who, where, when)",
      "customization_type": "communication_workflow",
      "example": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when contracts processed in Active phase"
    },
    {
      "element": "Customer-specific invoice memos and special handling",
      "customization_type": "customer_relationship_management"
    },
    {
      "element": "Contract-specific processing instructions that may differ by contract",
      "customization_type": "contract_processing_rules",
      "example": "Back-dating invoice date to final day of month"
    },
    {
      "element": "Merchant call recordings and documentation",
      "customization_type": "knowledge_management"
    },
    {
      "element": "Feature requests with urgency and importance tracking",
      "customization_type": "requirements_management"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document appears to be a template or instruction guide with some sections incomplete (marked as "to fill"). The structure is clear but some content is fragmented or contains placeholder text. The rules extracted are explicit and clear, but context about the overall system and some abbreviations (BT, SOW, AE) requires domain knowledge. The confidence is moderate due to incomplete sections and some ambiguous references.

---

## Chunk 5: MIS for Darkroom Studios_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:56

### Original Content
```
), especially those outside QuickBooks Contract Ingestion from PandaDoc Seamlessly pull billing terms and fee structures from signed contracts without manual entry Flexible Approval   Control Ability to review edit invoices before they go out   especially important due to trust concerns
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing automation integration",
    "Third-party software integration (QuickBooks, PandaDoc)",
    "Invoice approval and quality control workflows",
    "Trust and accuracy in financial processes",
    "Automated data extraction from contracts"
  ],
  "rules": [
    "Contracts from PandaDoc must be ingested to extract billing terms and fee structures",
    "Manual entry of contract data should be avoided in favor of automated ingestion",
    "Invoices require review and editing capability before being sent to clients",
    "Approval controls must be implemented for invoice distribution",
    "System must support integration with QuickBooks for contract ingestion",
    "Billing terms and fee structures must be pulled directly from signed contracts"
  ],
  "exceptions": [
    "Special attention required for contracts or data sources outside of QuickBooks",
    "Manual intervention allowed during invoice review stage despite automation goals",
    "Trust concerns may trigger additional review requirements before invoice distribution"
  ],
  "merchant_specific": [
    "Choice of contract management platform (PandaDoc mentioned, but may vary)",
    "Specific accounting software integration (QuickBooks mentioned, but alternatives may exist)",
    "Definition of 'billing terms' and 'fee structures' may vary by merchant industry",
    "Level of approval authority and who has edit permissions on invoices",
    "Threshold or criteria that trigger mandatory review due to 'trust concerns'",
    "Specific fields to extract from contracts (billing terms, fee structures, potentially others)"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for Confidence Score:**
The confidence score of 0.65 reflects moderate uncertainty due to:
- The document chunk appears incomplete (starts mid-sentence with ")")
- Context is limited, making it difficult to understand the full scope of requirements
- Some terminology like "trust concerns" is vague without additional context
- The relationship between different systems and workflows is not fully clear
- However, the core themes around automation, integration, and approval workflows are reasonably clear

---

