# Raw LLM Analysis: Merchant Info Sheet - Satisfi Labs

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:14:45

---

## Chunk 1: Merchant Info Sheet - Satisfi Labs_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:14:45

### Original Content
```
4 Merchant Demo date: September 30, 2024 Scoping start date: Sep 30, 2024 MSA Signature Date: Oct 29, 2024 Onboarding Kick Off Date: Nov 1, 2024 [If Exists] Opt Out Date: N A Go Live Date: Nov 18, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CFO   CEO: Ed Hagan (ed satisfilabs com) Finance Lead VP: Jonathan Scott (jon satisfilabs com) Company summary (AE to fill) Satisfi Labs is provides an AI Chat platform for customer experience teams Satisfi Labs generates re...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Company Profile and Stakeholder Information",
    "Billing Model and Revenue Structure",
    "Contract Processing Workflow and Requirements",
    "System Integration and Pain Points"
  ],
  "rules": [
    "All customers must already exist in QBO before processing",
    "Flag any customer that does not exist in QBO before adding",
    "Revenue schedules should be created for each individual year, not across all contract years",
    "All line items in the order form table must be processed",
    "Process both Product Name and Description from the table",
    "Use quantities from the quantity table",
    "Bundled items marked as 'Included' should be processed as $0",
    "Multi-year contracts require separate rev schedules per year due to potential product differentiation",
    "Verify customer currency when adding new customers (international currency considerations)",
    "Process contracts from order forms in table format"
  ],
  "exceptions": [
    "Billing is mostly annual upfront, but some exceptions exist for quarterly and monthly billing (will be outlined in contract)",
    "Discount processing can vary (no standard rule specified)",
    "Some usage-based billing for overage related to newly acquired product line",
    "Despite bundling, all line items must still be processed individually",
    "Product differentiation may occur year-over-year in multi-year contracts"
  ],
  "merchant_specific": [
    "Merchant name: Satisfi Labs",
    "Industry: AI Chat platform for customer experience (sports, entertainment, retail focus)",
    "Key stakeholders: CEO Ed Hagan, Finance Lead VP Jonathan Scott",
    "Specific go-live date: Nov 18, 2024",
    "ERP system and Tax Integration: Not specified",
    "No opt-out clause present",
    "Pain points: Manual billing, lack of reporting in QBO, collections/AR issues, lack of SFDC-QBO connectivity",
    "Revenue model: Subscription-based with many SKUs, bundles, discounts, and usage overages",
    "International customer base requiring multi-currency support",
    "Recently acquired new product line with usage-based billing"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Satisfi Labs_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:14:50

### Original Content
```
One type of discount should be in the item and the other is its own line item Discounts - Services: Apply this discount to the BT for Implementation Discounts: This should be a separate BT Integration items If it can easily be found inferred based on item title, link to that If there is no obvious match, leave blank and the system will either auto-match or leave blank   This is because they want to clean up their integration items, and will use Tabs contract processing as a way to start the clea...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Discount and billing treatment configuration",
    "Auto-renewal processing and contract extension",
    "Usage-based billing for WhatsApp and SMS services",
    "Integration item mapping and data cleanup strategy",
    "Default operational values for contract processing"
  ],
  "rules": [
    "Two types of discounts must be handled differently: one applied to the item itself, one as a separate line item",
    "Service discounts should be applied to the BT (Billing Template) for Implementation",
    "Discounts should be created as a separate BT",
    "Integration items should be linked based on item title when easily inferred",
    "If no obvious integration item match exists, leave blank for auto-matching or manual cleanup",
    "ALL Satisfi contracts are allowed to auto-renew by default",
    "Auto-renewal should process 1 extra year based on the terms of the last year",
    "Auto-renewal should create a new set of BTs for the extra year",
    "Usage billing exists for 5 contracts currently (WhatsApp and SMS)",
    "Usage is pay-as-you-go with standard use model",
    "Usage items are identified in ADD-ON Packages section with YES indicator",
    "WhatsApp usage BT should use Integration Item 'Channel:WhatsApp' with Event type 'WhatsApp'",
    "SMS usage BT should use Integration Item 'Channel:SMS' with Event type 'SMS'",
    "Usage billing start date is 1st of the month of contract sign date",
    "If contract not signed on 1st, add an extra month to total months billed",
    "Usage billing is monthly in arrears unless specified otherwise",
    "Default service term is 1 year if none listed",
    "Default net payment terms is 30 days if none listed",
    "Default billing frequency is Annual if none listed",
    "Every tax line item becomes a separate BT",
    "All BTs in a contract are assigned the same class fields",
    "Class field is used for customer segments",
    "Ops should ignore class field processing (Implementation Success handles)",
    "Ops should ignore 'marketing engine' product line for now (still implementing)"
  ],
  "exceptions": [
    "Auto-renewal should NOT be processed if explicitly stated in the contract that it is NOT to auto-renew",
    "Usage billing frequency can differ if specified otherwise in the contract",
    "If contract is not signed on the 1st of the month, add an extra month to account for partial month billing",
    "Integration item mapping should be left blank when not obvious (rather than forcing a match)"
  ],
  "merchant_specific": [
    "Merchant name: Satisfi",
    "Specific products: WhatsApp and SMS usage billing",
    "Integration item cleanup strategy using Tabs contract processing",
    "Master list of processed items exists for integration mapping reference",
    "5 existing usage contracts with plans to expand",
    "New product line 'marketing engine' in implementation phase",
    "Class field implementation plan involves importing for all processed contracts",
    "ADD-ON Packages section format specific to this merchant's contracts",
    "BT naming conventions: 'WhatsApp Messaging' and 'Mass SMS'",
    "Specific integration item channels: 'Channel:WhatsApp' and 'Channel:SMS'"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Satisfi Labs_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:14:56

### Original Content
```
rewatch com video bnsnuyi1m9m2alup-ed-and-rebecca-schwartz-tabs-may-23-2024 June 5 https: tabs rewatch com video aom1sb5hx2srifs5-ed-and-rebecca-schwartz-tabs-june-5-2024 June 7 https: tabs rewatch com video 4kmidjc4ktdcwffx-ed-rebecca-tabs-june-7-2024 September 30 https: tabs rewatch com video kvz9frd0s4j99h8m-satisfi-labs-tabs-september-30-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Spreadsheets related to implementation Is the...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting documentation and video recordings tracking",
    "Implementation team coordination and role separation",
    "Merchant relationship management and stakeholder identification",
    "Billing and financial documentation requirements",
    "Feature prioritization based on key stakeholder preferences"
  ],
  "rules": [
    "Video recordings of merchant meetings must be maintained with dates and accessible URLs",
    "Operations International Team should ignore certain sections marked for AE and Implementation teams",
    "Implementation team is responsible for filling in specific merchant information sections",
    "Merchant billing information must be documented",
    "Implementation-related spreadsheets must be maintained and linked",
    "Merchant relationship information must include three key components: temperament assessment, key POC identification, and feature preferences",
    "Decision maker (buyer) must be identified as part of POC documentation",
    "Tabs features that matter to key stakeholders must be documented"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' are explicitly excluded from certain team workflows",
    "Different teams (AE vs Implementation) have different documentation responsibilities for the same merchant"
  ],
  "merchant_specific": [
    "Merchant temperament assessment (varies per merchant)",
    "Key Point of Contact (POC) identification - specific individuals per merchant",
    "Decision maker/buyer identification - unique to each merchant organization",
    "Tabs feature preferences - customized based on what each merchant's POC values",
    "Merchant billing methods and processes",
    "Implementation spreadsheets tailored to specific merchant needs",
    "Meeting schedules and video recording links specific to each merchant engagement"
  ],
  "confidence_score": 0.75
}
```

---

