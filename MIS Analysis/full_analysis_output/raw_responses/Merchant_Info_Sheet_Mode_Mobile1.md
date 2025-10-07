# Raw LLM Analysis: Merchant Info Sheet - Mode Mobile(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:35:38

---

## Chunk 1: Merchant Info Sheet - Mode Mobile(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:35:38

### Original Content
```
Mode Mobile Scoping start date: May 2, 2024 Implementation Completed Date (Go live date): MSA Signature Date: Apr 26, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Kathleen, Eric Data: Akanksha Company summary Mode Mobile makes a variant of Android that displays advertising to the user They collect money from the advertising networks based on how many ads were displayed and the contracted prices and share some of that revenue back to the users AM Notes None Billing model...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue sharing billing model based on advertising data",
    "Contract processing workflow and billing term creation",
    "Data-driven invoicing from uploaded reports",
    "Customer account setup and management in QBO",
    "Exception handling for missing contracts or data"
  ],
  "rules": [
    "Data report from Mode Mobile team states monthly billing amounts per provider",
    "Report becomes available one week after month end",
    "Mode uploads report to Tabs through Events system for bill generation",
    "Each uploaded document must be assigned to correct customer (create if not exists in QBO)",
    "Create single billing term named 'Monthly Revenue Share' for each customer",
    "Billing type must be 'unit price'",
    "Event to track must be 'revshare'",
    "Price must be set to '1'",
    "Start date should be first day of month after closed period (e.g., if period ends 5/30/2025, start date is 6/1/2025)",
    "Total invoices should be '12'",
    "Net terms and Integration item found in 'Mode Mobile - Tabs usage data' worksheet",
    "Default to NET 30 days if no row exists in worksheet",
    "No integration item should be used if absent from worksheet",
    "All documents must be marked as processed after completion",
    "For customers in data sheet without contracts, upload fake contract (Contract stand-in pdf)",
    "Create billing terms for customers without contracts following same process as Step 1"
  ],
  "exceptions": [
    "Contracts do not need to be processed by reading them (non-standard approach)",
    "When worksheet lacks customer row: use NET 30 days as default payment terms",
    "When worksheet lacks customer row: use no integration item",
    "Customers without contracts require uploading a fake/stand-in contract PDF but still get billing terms created"
  ],
  "merchant_specific": [
    "Merchant name: Mode Mobile",
    "Business model: Android variant with advertising revenue sharing",
    "Scoping start date: May 2, 2024",
    "Go live date: (not specified)",
    "MSA Signature Date: Apr 26, 2024",
    "Key contacts: Kathleen (Accountant), Eric (Accountant), Akanksha (Data)",
    "Event type name: 'revshare'",
    "Billing term name: 'Monthly Revenue Share'",
    "Data source: Mode Mobile team report via Events system",
    "Reference worksheet: 'Mode Mobile - Tabs usage data' (shared with merchant)",
    "Stand-in contract file: 'Contract stand-in pdf'",
    "Report timing: available one week after month end",
    "Revenue sources: advertising networks based on ad displays and contracted prices"
  ],
  "confidence_score": 0.95
}
```

---

## Chunk 2: Merchant Info Sheet - Mode Mobile(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:35:39

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
    "Customer onboarding workflow and training materials",
    "Video-based knowledge repository using Rewatch platform",
    "Multi-stage customer journey tracking (Sales → Onboarding)"
  ],
  "rules": [
    "Events are handled through self-service model for Mode Mobile customers",
    "Customer information is not provided or stored in this documentation",
    "Feature requests are not tracked or documented in this section",
    "Sales calls are recorded and archived with specific video links",
    "Onboarding sessions are recorded and stored for reference",
    "Multiple sales touchpoints are documented (Sales 1 and Sales 2)",
    "Multiple onboarding sessions are conducted (Onboarding 1 and Onboarding 2)",
    "Video recordings include participant names and dates in titles",
    "All video content is hosted on Rewatch platform (tabs.rewatch.com)"
  ],
  "exceptions": [
    "Customer information explicitly marked as 'None' - suggesting it may be available for other merchants or contexts",
    "Feature requests marked as 'None' - indicating this may be populated in other scenarios",
    "Onboarding 2 labeled as 'v2' suggesting iterative process or updated version"
  ],
  "merchant_specific": [
    "Merchant name: Mode Mobile",
    "Specific participant names: Kathleen Carroll, Jarrett Martin, Arjun Gopalratnam",
    "Specific date range: April 10, 2024 to May 3, 2024",
    "Self-service event model may vary by merchant",
    "Number of sales and onboarding calls may differ per merchant",
    "Video recording practices and platform (Rewatch) may be merchant-specific",
    "The structure of 'Customer Information' and 'Feature Requests' sections likely varies by merchant needs"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document appears to be a structured reference sheet with video links and categorical placeholders. While the structure is clear, the content is minimal with several "None" values, making it difficult to extract comprehensive rules. The format suggests this is part of a larger system, but context about the broader merchant instruction framework is limited. The confidence is moderate because the themes and structure are identifiable, but the sparse content limits deeper rule extraction.

---

