# Raw LLM Analysis: Merchant Info Sheet - OpenClinica

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:57:08

---

## Chunk 1: Merchant Info Sheet - OpenClinica_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:57:08

### Original Content
```
OpenClinica Demo date: Aug 7, 2024 Scoping start date: Aug 9, 2024 MSA Signature Date: Aug 22, 2024 Onboarding Kick Off Date: Aug 26, 2024 Go Live Date: Sep 23, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Joe Gilmore - our main POC and super great to work with Elisia: Intern that will be helping Joe pull documents, etc, for the transition COO: Ben Baumann - likely not involved in the implementation process, but cares deeply about the quality of the ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Migration from Maxio to Tabs platform",
    "Billing and subscription management automation",
    "Integration requirements (SFDC, QBO, Slack)",
    "Contract and renewal management",
    "Audit compliance and access control"
  ],
  "rules": [
    {
      "rule": "Late fees must be applied either to a new invoice or added to the next invoice sent",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Most customer contracts auto-renew by default",
      "category": "contract_management",
      "explicit": true
    },
    {
      "rule": "Consulting hours are sold in blocks that expire after a certain period",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Consulting hours blocks can be drawn down from over time",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Multiple SKUs can be billed on a single invoice",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Order forms contain SKUs at the front of the document",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "MSA (Master Service Agreement) stipulates renewal terms separately from order forms",
      "category": "contract_structure",
      "explicit": true
    },
    {
      "rule": "Must achieve feature parity with Maxio platform",
      "category": "implementation",
      "explicit": true
    },
    {
      "rule": "Access control must be tightened to meet audit requirements",
      "category": "compliance",
      "explicit": false
    },
    {
      "rule": "Payment recording and syncing should be automated (not manual)",
      "category": "payment_processing",
      "explicit": false
    },
    {
      "rule": "SFDC sync should not require manual adjustments",
      "category": "integration",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "No opt-out clause exists in the contract",
      "context": "However, merchant created a checklist of required features that essentially serves as success criteria"
    },
    {
      "exception": "Contract PDFs can be either renewals or new orders",
      "context": "Processing steps may differ based on contract type"
    },
    {
      "exception": "Some contracts may not auto-renew (implied by 'most' customer contracts auto-renew)",
      "context": "Need to handle both auto-renewing and non-auto-renewing contracts"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key contacts",
      "details": "Joe Gilmore (main POC, Accountant), Elisia (Intern for document pulling), Ben Baumann (COO, quality oversight)",
      "customization_needed": true
    },
    {
      "element": "Timeline",
      "details": "Specific implementation dates from Aug 7, 2024 (demo) to Sep 23, 2024 (go-live)",
      "customization_needed": true
    },
    {
      "element": "Previous system",
      "details": "Maxio (since 2016) - migration context is critical",
      "customization_needed": true
    },
    {
      "element": "OpenClinica Checklist for Tabs.xlsx",
      "details": "Merchant-specific feature requirements document",
      "customization_needed": true
    },
    {
      "element": "Business model",
      "details": "SaaS platform for clinical trials with consulting hours add-on",
      "customization_needed": true
    },
    {
      "element": "Customer base",
      "details": "Life science companies, academic institutions, government entities",
      "customization_needed": false
    },
    {
      "element": "Contract structure",
      "details": "Order forms with SKUs + separate MSA for renewal terms",
      "customization_needed": true
    },
    {
      "element": "Pain points",
      "details": "Renewals/contract terms, SFDC sync issues, audit access control, manual payment recording, poor reporting",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - OpenClinica_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:57:10

### Original Content
```
Service Start Date: use the Subscription Start Date at the top of the document If not stated, the Start date should be the OC signature date 9 20 24 in the example below: EXCEPTIONS : If there is no Subscription start date or signature available OR if the start date is based on a milestone event that we would not know, please use the Offer Expires date as a place holder AND make a note in this tracker: https: docs google com spreadsheets d 1hRSvskDAUA316EfqqsVitL5PfsREJXLg edit gid 2025275138 gi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Recognition and Scheduling",
    "Service Start Date Determination",
    "Subscription Product Management",
    "Billing Terms and Frequency Configuration",
    "Integration Item Mapping and Categorization"
  ],
  "rules": [
    {
      "category": "Service Start Date",
      "rule": "Use the Subscription Start Date at the top of the document",
      "fallback": "If not stated, use the OC signature date"
    },
    {
      "category": "Service Start Date - Exception",
      "rule": "If no Subscription start date or signature available OR if start date is based on unknown milestone event, use the Offer Expires date as placeholder and document in tracker"
    },
    {
      "category": "Service Term",
      "rule": "For subscription products, follow contract language and use the term of the stated service period (generally one year)"
    },
    {
      "category": "Revenue Recognition - Subscriptions",
      "rule": "Rev rec straightline monthly based on the service term"
    },
    {
      "category": "Revenue Recognition - Subscriptions",
      "rule": "Subscription revenue starts when the campaign begins"
    },
    {
      "category": "Billing - Subscriptions",
      "rule": "Billing starts 3 months ahead of service delivery"
    },
    {
      "category": "Revenue Recognition - Training/Setup",
      "rule": "Revenue schedule should be set to 60 days after the bill date (e.g., if invoiced Jan 15, 2025, revenue schedule is March 15, 2025)"
    },
    {
      "category": "Service Term - Consulting",
      "rule": "For Consulting ≤100 hours, service term is 6 months"
    },
    {
      "category": "Service Term - Consulting",
      "rule": "For Consulting >100 hours, service term is 12 months"
    },
    {
      "category": "Item Name Mapping",
      "rule": "Search for integration item in drop-down list; if not found, check small text below for better fit"
    },
    {
      "category": "Revenue Category",
      "rule": "If item name does not match anything in the first column, set revenue category to 'uncategorized'"
    },
    {
      "category": "Integration Item Mapping",
      "rule": "If integration item is not in drop-down list, flag in tracking spreadsheet"
    },
    {
      "category": "Billing Timing",
      "rule": "Default to 'Bill in Advance, Due Start of Period' unless stated otherwise in contract"
    },
    {
      "category": "Net Terms",
      "rule": "Default to 30 days if not stated in the contract"
    },
    {
      "category": "Billing Frequency",
      "rule": "Use what is stated in the contract (Monthly, Quarterly, or Annual)"
    },
    {
      "category": "Billing Frequency - Default",
      "rule": "If nothing is stated, default is Annually"
    },
    {
      "category": "Billing Frequency - Override",
      "rule": "Filename frequency indication (e.g., 'bill quarterly' in filename) overrides both default and contract contents"
    }
  ],
  "exceptions": [
    {
      "condition": "No Subscription start date or signature available OR start date based on unknown milestone event",
      "action": "Use Offer Expires date as placeholder and document in tracker spreadsheet"
    },
    {
      "condition": "Item name not in integration item drop-down list",
      "action": "Check small text below for better fit; if still not found, flag in tracking spreadsheet"
    },
    {
      "condition": "Revenue category cannot be matched",
      "action": "Set to 'uncategorized'"
    },
    {
      "condition": "Billing frequency in filename differs from contract or default",
      "action": "Filename frequency overrides both default and contract contents; flag in tracking spreadsheet"
    },
    {
      "condition": "Consulting hours ≤100",
      "service_term": "6 months"
    },
    {
      "condition": "Consulting hours >100",
      "service_term": "12 months"
    }
  ],
  "merchant_specific": [
    {
      "element": "Subscription Products List",
      "description": "Specific list of subscription products including DICOM, OpenClinica variants (Academic Enterprise, Core Platform, eConsent, Enterprise, Insight, Participate, Randomize, Unite), and BuildClinical Recruit",
      "customization_needed": true
    },
    {
      "element": "Integration Item Mapping Table",
      "description": "Reference table for mapping item names to integration items and revenue categories (Column 1: item name, Column 2: Rev Rec Category, Column 3: Integration Item)",
      "customization_needed": true
    },
    {
      "element": "Tracking Spreadsheet",
      "description": "Google Sheets tracker for flagging missing information and exceptions (URL: docs.google.com/spreadsheets/d/1hRSvskDAUA316EfqqsVitL5PfsREJXLg)",
      "customization_needed": true
    },
    {
      "element": "OC Signature Date",
      "description": "Merchant-specific signature date reference (example: 9/20/24)",
      "customization_needed": true
    },
    {
      "element": "Billing Lead Time",
      "description": "3 months ahead of service delivery for subscriptions",
      "customization_needed": false,
      "note": "May vary by merchant business model"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - OpenClinica_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:57:19

### Original Content
```
google com spreadsheets d 1hRSvskDAUA316EfqqsVitL5PfsREJXLg edit gid 2025275138 gid 2025275138 How do we handle taxes as a line item No taxes If contract is a PO, add PO   to invoices accordingly Anything to ignore in contracts Ignore any discounts Only show the post-discount amounts For example, in the screenshot below, the billing term should be created as qty 100, unit price    195 50, total price    19,550 Ignore any late fees - do not create a BT for this Additionally, OpenClinica will now ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax handling and line item treatment",
    "Purchase order and invoice management",
    "Discount and pricing display rules",
    "Revenue recognition and scheduling",
    "Merchant-specific processing guidelines and cross-entity handling"
  ],
  "rules": [
    "Do not include taxes as a line item in processing",
    "If contract is a Purchase Order (PO), add PO number to invoices accordingly",
    "Ignore all discounts in contracts - only display post-discount amounts",
    "When creating billing terms with discounts, use the final discounted quantity, unit price, and total price",
    "Do not create billing terms for late fees - ignore them entirely",
    "Revenue schedule for Training SKU should be set to 60 days after the bill date",
    "Training SKU revenue recognition follows a 60-day delay pattern (e.g., Jan 15 invoice → March 15 revenue schedule)",
    "OpenClinica products that are the same as BuildClinical should be processed under OpenClinica entity but follow BuildClinical processing guidelines"
  ],
  "exceptions": [
    "OpenClinica selling BuildClinical products: Process under OpenClinica but use BuildClinical guidelines",
    "Training SKU has special revenue scheduling: 60 days post-bill date instead of standard recognition",
    "Contract-specific variations may exist where invoice dates are back-dated to final day of the month (mentioned as example of possible merchant-specific requests)"
  ],
  "merchant_specific": [
    "Reference to specific merchant entities: OpenClinica and BuildClinical",
    "Training SKU as a specific product type with unique revenue recognition rules",
    "Mention of merchant-requested processing variations (e.g., back-dating invoice dates to month-end)",
    "Reference to external spreadsheet (Google Sheets) for additional documentation",
    "Specific example pricing: qty 100, unit price $195.50, total $19,550",
    "Cross-entity processing rules where one merchant sells another's products"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - OpenClinica_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:57:28

### Original Content
```
This is a new request as of March 20, 2025 Events   Usage Processing (if necessary) No events   usage Integration Items Processing (if necessary) All integration items match the names of the products (3rd column) All revenue schedule names also match the names of the products (2nd column) Post Processing Communications (if necessary) Customer Information None Rewatch Calls Ben and Joe reconnect after initial chats in May standard demo - https: tabs rewatch com video k5zov4glmu9rcwh8-hold-joe-ben...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Data Processing and Integration Requirements",
    "Revenue Schedule and Product Name Alignment",
    "Customer Onboarding and Migration (from Maxio)",
    "Meeting Documentation and Call History",
    "Cash Forecasting and Renewal Data Management"
  ],
  "rules": [
    {
      "rule": "All integration items must match the names of the products (referenced as 3rd column)",
      "category": "Integration Items Processing",
      "explicit": true
    },
    {
      "rule": "All revenue schedule names must match the names of the products (referenced as 2nd column)",
      "category": "Integration Items Processing",
      "explicit": true
    },
    {
      "rule": "Events usage processing should be performed if necessary",
      "category": "Events Usage Processing",
      "explicit": true
    },
    {
      "rule": "Integration items processing should be performed if necessary",
      "category": "Integration Items Processing",
      "explicit": true
    },
    {
      "rule": "Post processing communications should be performed if necessary",
      "category": "Post Processing Communications",
      "explicit": true
    },
    {
      "rule": "No events usage is required for this specific request",
      "category": "Events Usage Processing",
      "explicit": true,
      "context": "As of March 20, 2025"
    },
    {
      "rule": "No customer information is required for post-processing communications",
      "category": "Post Processing Communications",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "This request has no events usage requirements (marked as 'No events usage')",
      "context": "Dated March 20, 2025"
    },
    {
      "exception": "Customer information is marked as 'None' for post-processing communications",
      "context": "Suggests this may be an exception to standard customer communication requirements"
    },
    {
      "exception": "Processing steps are conditional ('if necessary'), indicating not all steps may apply to every request",
      "context": "Events Usage, Integration Items, and Post Processing Communications"
    }
  ],
  "merchant_specific": [
    {
      "element": "OpenClinica",
      "type": "Merchant Name/Customer",
      "notes": "Specific customer being onboarded from Maxio platform"
    },
    {
      "element": "Migration from Maxio",
      "type": "Platform Migration",
      "notes": "Customer-specific migration context requiring scoping and data transfer"
    },
    {
      "element": "Renewal data requirements for cash forecasting",
      "type": "Custom Feature Requirement",
      "notes": "Specific need identified by customer (Joe) during scoping meetings"
    },
    {
      "element": "Product names in columns 2 and 3",
      "type": "Data Structure Reference",
      "notes": "References to specific column positions suggest merchant-specific data format or spreadsheet"
    },
    {
      "element": "Contact names (Joe, Ben, Rebecca, Ali, Ben Baumann, Arjun)",
      "type": "Stakeholders",
      "notes": "Merchant-specific team members and vendor representatives"
    },
    {
      "element": "Rewatch call recordings",
      "type": "Documentation",
      "notes": "Merchant-specific meeting history and requirements gathering sessions"
    }
  ],
  "confidence_score": 0.72
}
```

**Confidence Reasoning**: The document appears to be a partially formatted instruction set with clear rules about data matching requirements, but the context is somewhat fragmented. The reference to "3rd column" and "2nd column" without seeing the actual data structure, combined with the truncated nature of the rewatch links, reduces confidence. However, the explicit rules about integration items and revenue schedule naming are clear and actionable.

---

## Chunk 5: Merchant Info Sheet - OpenClinica_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:57:31

### Original Content
```
com video tzhkwhkc39kp6gwt-joe-ben-rebecca-sync-august-22-2024 AE  Implementation Notes Sections [Ops International Team to Ignore] Info on how merchant bills Are there unique things about the customer creation process for this merchant Customer has a late fee that needs to be applied to either a) a new invoice, or b) the next invoice sent Information on how merchant bills Merchant bills for multiple skus as well as blocks of consulting hours that are typically drawn down from, and expire after ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing and invoicing processes",
    "Customer contract management and auto-renewal terms",
    "Product/SKU categorization and revenue mapping",
    "Merchant migration from Maxio to Tabs platform",
    "Stakeholder relationships and implementation coordination"
  ],
  "rules": [
    "Late fees must be applied to either a new invoice or the next invoice sent",
    "Consulting hours are drawn down from blocks that expire after a certain period of time",
    "Most customer contracts auto-renew by default",
    "Order forms must have SKUs listed at the front",
    "Master Service Agreement (MSA) must stipulate renewal terms",
    "All items not explicitly categorized should be marked as 'Uncategorized' with integration_item_in_qbo left blank",
    "Revenue categorization must follow the mapping structure: item_name_from_maxio → rev_category_in_tabs → integration_item_in_qbo",
    "Training services include web-based and in-person delivery methods",
    "Service items include consulting, training, migration, and setup activities"
  ],
  "exceptions": [
    "Ops International Team should ignore Implementation Notes sections",
    "ALL OTHERS category serves as catch-all for unmapped items with blank QBO integration",
    "BuildClinical Recruit products map to 'Recruit' and 'OpenClinica Recruit' specifically",
    "DICOM product maintains same name across all three mapping columns (item_name, rev_category, integration_item)"
  ],
  "merchant_specific": [
    "Merchant name: OpenClinica",
    "Previous platform: Maxio (migration in progress)",
    "Key stakeholders: Joe Gilmore (Accountant/main POC), Elisia (Intern), Ben Baumann (COO)",
    "Merchant temperament: Very excited to switch to Tabs",
    "Priority features: Renewals, cash forecasting, easy collaboration with CS team",
    "Reference document: 'OpenClinica Checklist for Tabs xlsx'",
    "Product line includes: Core Platform, eConsent, Enterprise, Insight, Participate, Randomize, Unite, Recruit, DICOM",
    "Service offerings: Consulting (Fixed Fee and T&M), Training (web-based and in-person), Migration services",
    "Billing model: Multiple SKUs plus consulting hour blocks"
  ],
  "confidence_score": 0.85
}
```

---

