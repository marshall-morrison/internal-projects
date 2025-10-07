# Raw LLM Analysis: Merchant Info Sheet - Mode Mobile

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:26:19

---

## Chunk 1: Merchant Info Sheet - Mode Mobile_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:19

### Original Content
```
Mode Mobile Scoping start date: May 2, 2024 Implementation Completed Date (Go live date): MSA Signature Date: Apr 26, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Kathleen, Eric Data: Akanksha Company summary Mode Mobile makes a variant of Android that displays advertising to the user They collect money from the advertising networks based on how many ads were displayed and the contracted prices and share some of that revenue back to the users AM Notes None Billing model...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue sharing billing model based on advertising data",
    "Contract processing workflow with specific billing term creation",
    "Data-driven invoicing using uploaded reports from merchant",
    "Customer and billing term setup in QBO (QuickBooks Online)",
    "Exception handling for customers without contracts"
  ],
  "rules": [
    "Data report from Mode Mobile team states billing amounts for each provider monthly",
    "Report is available one week after month end",
    "Mode uploads report to Tabs through Events system",
    "Tabs generates bills for relevant partners based on uploaded data",
    "Do not process contracts by reading them - follow standardized steps instead",
    "Assign document to correct customer (create if doesn't exist in QBO)",
    "Create single billing term named 'Monthly Revenue Share'",
    "Billing type must be 'unit price'",
    "Event to track must be 'revshare'",
    "Price must be set to '1'",
    "Start date should be first of month after closed period (e.g., closed period ends 5/30/2025, start date is 6/1/2025)",
    "Total invoices should be '12'",
    "Net terms and Integration item found in 'Mode Mobile - Tabs usage data' worksheet",
    "Default to NET 30 days if no row exists in worksheet",
    "Use no integration item if not specified in worksheet",
    "Mark contract as processed after completion",
    "For customers in data sheet without contracts, upload fake contract (Contract stand-in pdf)",
    "Create billing terms for customers without contracts following same Step 1 process"
  ],
  "exceptions": [
    "If customer does not exist in QBO, create new customer",
    "If no row exists in the Mode Mobile worksheet for net terms/integration item, default to NET 30 days and no integration item",
    "For customers in data sheet lacking contracts, use attached fake contract PDF and still create billing terms"
  ],
  "merchant_specific": [
    "Merchant name: Mode Mobile",
    "Business model: Android variant displaying advertising with revenue sharing",
    "Scoping start date: May 2, 2024",
    "MSA Signature Date: Apr 26, 2024",
    "Key contacts: Kathleen (Accountant), Eric (Accountant), Akanksha (Data)",
    "Specific event name: 'revshare'",
    "Specific billing term name: 'Monthly Revenue Share'",
    "Data source: Mode Mobile team report uploaded through Events system",
    "Reference worksheet: 'Mode Mobile - Tabs usage data' (shared with merchant)",
    "Fake contract template: 'Contract stand-in pdf'",
    "Report timing: Available one week after month end",
    "Revenue source: Advertising networks based on ad displays and contracted prices"
  ],
  "confidence_score": 0.95
}
```

---

## Chunk 2: Merchant Info Sheet - Mode Mobile_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:21

### Original Content
```
Events are self-service for Mode Mobile Customer Information None Feature Requests None Rewatch Calls Sales 1: https: tabs rewatch com video y75bzzt21uou5oma-kathleen-carroll-and-jarrett-martin-april-10-2024 Sales 2: https: tabs rewatch com video mvriyvulb4on6qgm-kathleen-carroll-and-jarrett-martin-april-22-2024 Onboarding 1: https: tabs rewatch com video 3ert6fp8xbvdphrx-kathleen-carroll-and-jarrett-martin-arjun-gopalratnam-may-2-2024 Onboarding 2: https: tabs rewatch com video 383dxh20trss19jl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Self-service event management for Mode Mobile customers",
    "Sales process documentation and call recordings",
    "Customer onboarding process with multiple sessions",
    "Video-based training and reference materials via Rewatch platform",
    "Customer lifecycle tracking (sales through onboarding)"
  ],
  "rules": [
    "Events are handled on a self-service basis for Mode Mobile customers",
    "Sales calls are recorded and archived in Rewatch with specific naming conventions (participant names and dates)",
    "Multiple sales touchpoints are documented (Sales 1 and Sales 2)",
    "Onboarding process consists of at least two sessions (Onboarding 1 and Onboarding 2)",
    "All customer interaction videos are stored in tabs.rewatch.com domain",
    "Video recordings include participant names in the title for tracking purposes",
    "Onboarding sessions may include multiple participants (e.g., Kathleen Carroll, Jarrett Martin, Arjun Gopalratnam)"
  ],
  "exceptions": [
    "Customer Information is marked as 'None' - suggesting either no special customer information requirements or information not provided in this context",
    "Feature Requests are marked as 'None' - indicating either no feature requests exist or they are tracked separately",
    "The second onboarding session is labeled 'v2' suggesting it may be a revised or updated version of the onboarding process"
  ],
  "merchant_specific": [
    "Merchant name: Mode Mobile",
    "Specific contact persons: Kathleen Carroll, Jarrett Martin, Arjun Gopalratnam",
    "Specific video URLs unique to this merchant's sales and onboarding journey",
    "Timeline: Sales process started April 10, 2024, onboarding completed by May 3, 2024",
    "Use of 'Tabs' platform/product name in video titles",
    "Self-service event model may be specific to Mode Mobile's service tier or contract type"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document appears to be a structured reference list with minimal contextual information. While the structure and URLs are clear, the lack of detailed instructions, policies, or procedural information limits the ability to extract comprehensive rules. The "None" entries for Customer Information and Feature Requests suggest this may be a partial document or template. The confidence is moderate because the themes and merchant-specific elements are clearly identifiable, but the broader operational rules and requirements are largely inferred rather than explicitly stated.

---

