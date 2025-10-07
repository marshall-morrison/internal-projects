# Raw LLM Analysis:  Merchant Info Sheet - Coalesce (Deprecrated)_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:06:57

---

## Chunk 1:  Merchant Info Sheet - Coalesce (Deprecrated)__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:06:57

### Original Content
```
Merchant Scoping start date: Feb 28, 2024 Implementation Completed Date (Go live date): Mar 14, 2024 MSA Signature Date: Feb 9, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Trevor McGuire- Fractional Accountant and everyday user (trevor mcguire coalesce io) CFO: Nick Decesare (nick decesare coalesce io) Buyer and Product Partner Senior Fiance: Tianna Tugulavioa (tianna coalesce io) Company summary: Coalesce helps you transform data your way, by making data transformatio...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Procedures",
    "Merchant Relationship and Account Management",
    "Invoice Creation and Documentation Requirements",
    "Contract Types and Billing Models",
    "Date Management for Billing Events"
  ],
  "rules": [
    "When billing platform seats, show 1 Quantity for 'Coalesce Platform'",
    "When billing all other quantities, show the actual quantity in the BT's quantity section",
    "For discounting, specify the items that have been discounted in the description (e.g., Platform, Additional User License, etc.)",
    "Add seat quantity in the Description field",
    "New contracts: Default billing date to signature date unless explicitly stated otherwise",
    "Renewals: Invoice date will always be written in renewal contract",
    "Renewals billing starts on the date after the first term",
    "Default billing contact name to '[Company Name] AP Dept' on all invoices",
    "Do not process rev share agreements",
    "Add PO number if a PO document has been sent in addition to contract",
    "Place PO via invoices tab in Garage and add PO to specific invoice",
    "PO billing schedule supersedes the contract",
    "If a contract shows a reseller fee, input the subtotal as one BT and the reseller fee as a second BT with a negative value (MSA 4/19 update)"
  ],
  "exceptions": [
    "New contract billing date can differ from signature date if explicitly stated otherwise in contract",
    "PO billing schedule takes precedence over contract terms when PO is present",
    "Rev share agreements should not be processed (exception to normal contract processing)",
    "Reseller fee contracts require special handling with negative value BT entry"
  ],
  "merchant_specific": [
    "Merchant name: Coalesce",
    "Billing model: Mostly annual, multi-year contracts",
    "Contract structure: SaaS-based",
    "International contracts present",
    "Key contacts: Trevor McGuire (Accountant), Nick Decesare (CFO), Tianna Tugulavioa (Senior Finance)",
    "Product-specific terminology: 'Coalesce Platform', 'Platform seats', 'Additional User License'",
    "Implementation timeline: Scoping start Feb 28, 2024; Go live Mar 14, 2024; MSA signed Feb 9, 2024",
    "Account manager notes: Nick is bullish on Tabs, interested in 3-year contract, potential advisor candidate",
    "Company business: Data transformation platform"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2:  Merchant Info Sheet - Coalesce (Deprecrated)__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:07:11

### Original Content
```
(e g 1,000 subtotal with 30  reseller fee, should have 2 BTs One for  1,000 and one for - 300 4 30 update: Discounts: place discounts as negative billing terms separate from gross line item pricing to allow merchant visibility into discounts by line item for their ability to handle expansion on renewal conversations Jumpstart is one time fee typical added to first invoice Not recurring unless noted in contract 6 10 update: Please send comms to Azmat after any international currency contract is p...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Terms and Invoice Structure",
    "Discount and Fee Handling",
    "International Currency Processing",
    "Communication and Notification Protocols",
    "Invoice Generation and Distribution Workflow"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "Reseller fees must be split into separate billing terms (BTs): one for the gross amount and one for the negative fee amount",
      "example": "1,000 subtotal with 300 reseller fee requires two BTs: one for 1,000 and one for -300"
    },
    {
      "rule_id": "R2",
      "description": "Discounts must be placed as negative billing terms separate from gross line item pricing",
      "rationale": "To provide merchant visibility into discounts by line item for expansion and renewal conversations"
    },
    {
      "rule_id": "R3",
      "description": "Jumpstart fees are one-time fees typically added to the first invoice only",
      "exception": "Not recurring unless specifically noted in contract"
    },
    {
      "rule_id": "R4",
      "description": "Send communications to Azmat after processing any international currency contract (effective 6/10)",
      "type": "notification_requirement"
    },
    {
      "rule_id": "R5",
      "description": "Send Slack message using ellipses after processing Coalesce contracts (effective 7/31)",
      "constraint": "Only for the next upcoming invoice in series, not all future invoices"
    },
    {
      "rule_id": "R6",
      "description": "For multi-year contracts, send Slack notification only for the immediate invoice, not future year invoices",
      "example": "3-year contract processed in July 2024 with annual invoicing: send message for July '24 only, not July '25 or '26"
    },
    {
      "rule_id": "R7",
      "description": "International invoice processing workflow steps: (1) Process contract with customer name and address, (2) Review billing terms accuracy, (3) Download PDF invoice, (4) Edit currency in Photoshop, (5) Run Google script for Tabs invoice template, (6) Verify customer email and attachments, (7) Send invoice to customer, (8) Update QBO with support@tabsplatform email"
    },
    {
      "rule_id": "R8",
      "description": "International invoices require Chase wire instructions to be attached",
      "type": "attachment_requirement"
    },
    {
      "rule_id": "R9",
      "description": "International invoices have a 24-hour turnaround expectation for customers",
      "type": "sla_requirement"
    },
    {
      "rule_id": "R10",
      "description": "QBO copy of international invoices must have send-to email updated to support@tabsplatform",
      "type": "system_requirement"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Jumpstart fees are typically non-recurring but can be recurring if explicitly noted in the contract",
      "condition": "Contract must specifically state recurring nature"
    },
    {
      "exception_id": "E2",
      "description": "Slack notifications for Coalesce contracts should only be sent for the immediate next invoice, not subsequent invoices in multi-year contracts",
      "condition": "Applies to contracts with multiple invoice periods (annual, multi-year)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Azmat communication requirement",
      "description": "Specific individual (Azmat) must be notified for international currency contracts",
      "customization_needed": "Contact person may vary by merchant or organization"
    },
    {
      "element": "Coalesce contracts",
      "description": "Specific contract type requiring Slack notification via ellipses method",
      "customization_needed": "Contract type and notification method are merchant-specific"
    },
    {
      "element": "Tabs invoice template",
      "description": "Google script generates specific 'Tabs invoice template' for international invoices",
      "customization_needed": "Template and script are specific to this merchant's system"
    },
    {
      "element": "Chase wire instructions",
      "description": "Specific banking instructions required for international payments",
      "customization_needed": "Banking partner and wire instructions vary by merchant"
    },
    {
      "element": "QBO (QuickBooks Online) integration",
      "description": "Specific accounting system with support@tabsplatform email requirement",
      "customization_needed": "Accounting system and email addresses are merchant-specific"
    },
    {
      "element": "Photoshop currency editing",
      "description": "Manual currency editing process using specific software",
      "customization_needed": "Tool and process may vary by merchant capabilities"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Rationale**: The document chunk is somewhat fragmented with incomplete sentences and unclear formatting, which affects interpretation accuracy. However, the core rules and processes are identifiable. The confidence is reduced due to: (1) unclear context for some abbreviations and references, (2) fragmented sentence structure making some rules ambiguous, (3) missing details about the "ellipses" Slack method, and (4) incomplete information about the international invoice SOP mentioned but not fully detailed.

---

## Chunk 3:  Merchant Info Sheet - Coalesce (Deprecrated)__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:07:11

### Original Content
```
com Do a spot currency conversion from USD to   (e g,  30,000 to  38,358 dollars) Edit the amount on the tabs platform Edit the note to say  XXX  to USD conversion as of XX YY 2024  Press send an invoice to get it out to QBO List of invoices thus far: Coalesce International Invoice Events Processing (if necessary) N A Customer Information Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Currency conversion and invoice processing",
    "Platform integration between Tabs and QuickBooks Online (QBO)",
    "Customer relationship management and documentation",
    "Revenue recognition and reporting requirements",
    "Video call documentation and training materials"
  ],
  "rules": [
    "Perform spot currency conversion from USD to another currency (example: 30,000 to 38,358 dollars)",
    "Edit the conversion amount on the Tabs platform",
    "Update invoice notes with format: 'XXX to USD conversion as of XX YY 2024'",
    "Send invoice to push it to QuickBooks Online (QBO)",
    "Maintain a list of all invoices processed",
    "Process Coalesce International Invoice Events when necessary",
    "Document special memos that certain invoices require",
    "Track invoice changes related to merchant-customer relationships",
    "Maintain video call recordings in chronological order (most recent first)",
    "Revenue recognition reporting is required with medium-high urgency"
  ],
  "exceptions": [
    "International invoice events processing is conditional - marked as 'if necessary' with N/A option",
    "Certain invoices require special memos based on merchant-customer relationship dynamics",
    "Invoice modifications may be needed due to specific merchant-customer relationships"
  ],
  "merchant_specific": [
    "Merchant name: Coalesce (or Coalesce International)",
    "Currency conversion pairs and amounts will vary by merchant",
    "Customer-specific information and special handling requirements",
    "Invoice memo requirements may differ per merchant",
    "Feature requests for Rev Rec (Revenue Recognition) and Reporting capabilities",
    "Video call history and training materials specific to this merchant's onboarding",
    "Specific date formats and conversion dates in invoice notes"
  ],
  "confidence_score": 0.72
}
```

**Reasoning for Confidence Score (0.72):**
- The document appears to be fragmented or partially formatted, making some sections unclear
- Core processes (currency conversion, invoice editing, QBO integration) are relatively clear
- Some context is missing around "XXX" placeholders and specific workflow triggers
- The relationship between different sections (Customer Information, Feature Requests, etc.) is not fully explained
- Video links provide supporting evidence but content isn't accessible from the text alone

---

