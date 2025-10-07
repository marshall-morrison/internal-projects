# Raw LLM Analysis: [Deprecated] Master Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:03:57

---

## Chunk 1: [Deprecated] Master Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:03:57

### Original Content
```
Who is Decision maker How what is their billing model Events Milestone Example: Flat fee   usage based on things in the field (For example- we helped 500 residents of this company become more energy efficient) How quickly do they go from sales to invoice Example: Invoices are tabulated at EOM Is all their billing info in one contract or is it multiple (MSA  PO Amendments) This Merchant has MSA that get adjusted with annual amendments Technical   Technical Are there remittances Unsure SFDC or oth...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Models and Revenue Recognition",
    "Contract Structure and Documentation",
    "Sales-to-Invoice Workflow Timing",
    "Technical Integration and Systems",
    "Information Gathering and Documentation Requirements"
  ],
  "rules": [
    "Decision maker identification is required for each merchant",
    "Billing model must be documented (flat fee vs usage-based)",
    "Usage-based billing requires clear metrics definition (e.g., number of residents served)",
    "Invoice timing and tabulation schedule must be established (e.g., End of Month)",
    "Contract structure must be documented (MSA, PO, Amendments, or combination)",
    "Sales-to-invoice timeline must be determined",
    "Remittance information needs to be collected",
    "CRM/CPQ system identification required (SFDC or alternatives)",
    "Additional supporting documentation must be requested with specific deadlines",
    "System compatibility and support limitations must be identified upfront"
  ],
  "exceptions": [
    "Billing information may be consolidated in single contract OR distributed across multiple documents (MSA + PO + Amendments)",
    "Usage-based billing metrics vary by merchant type and service provided",
    "Some technical information may be uncertain or unavailable initially (marked as 'Unsure')",
    "Additional documentation may be provided on delayed timeline (e.g., by specific date like April 2, 2024)"
  ],
  "merchant_specific": [
    "Decision maker identity and role",
    "Specific billing model choice (flat fee vs usage-based)",
    "Custom usage metrics (e.g., 'residents helped with energy efficiency')",
    "Invoice tabulation schedule (EOM or other cadence)",
    "Contract structure preference (single MSA vs multiple documents)",
    "Sales-to-invoice cycle duration",
    "Existing technical systems (SFDC, other CPQ, additional software)",
    "Remittance processes and requirements",
    "Documentation delivery timelines",
    "Known system limitations or unsupported features"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: [Deprecated] Master Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:03:59

### Original Content
```
USE THIS UPDATED VERSION INSTEAD HERE : The scoping pre-work doc creates efficient and clear communication between GTM and Product leads ahead of Scoping calls Scoping is necessary for Netsuite integrations or QBO with custom tolling or requirements Requirement: Please complete the required information and deliver it to your product partner 24 hours before your Scoping call Merchant Scoping start date: 3 20 24 Implementation Completed Date (Go live date): Apr 3, 2024 MSA Signature Date: Mar 29, ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Scoping and Implementation Process",
    "Contract Processing and Date Management",
    "Merchant Communication and Documentation Requirements",
    "Integration Requirements (ERP, Tax, Accounting Systems)",
    "Customer Lifecycle Management (Launch, End Dates, Renewals)"
  ],
  "rules": [
    {
      "rule": "Scoping pre-work document must be completed and delivered to product partner 24 hours before Scoping call",
      "category": "Pre-work Requirements"
    },
    {
      "rule": "Scoping is necessary for NetSuite integrations or QuickBooks Online (QBO) with custom tooling or requirements",
      "category": "Integration Requirements"
    },
    {
      "rule": "Default launch date to signature date if no kick-off call or launch date is defined in contract",
      "category": "Launch Date Processing"
    },
    {
      "rule": "Default to 1 month implementation date if no implementation date or time period is listed",
      "category": "Implementation Timeline"
    },
    {
      "rule": "For contracts with end date in the past: set end date to 6 months from now, await merchant confirmation on cancellation/amendment/renewal",
      "category": "End Date Processing"
    },
    {
      "rule": "For contracts without an end date: set end date to 6 months from today, await merchant confirmation",
      "category": "End Date Processing"
    },
    {
      "rule": "For contracts with future end date within next few months: use contract end date unless notified otherwise",
      "category": "End Date Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts with past end dates require manual intervention and merchant confirmation",
      "condition": "End date is in the past"
    },
    {
      "exception": "Contracts without defined end dates default to 6-month extension",
      "condition": "No end date specified"
    },
    {
      "exception": "Launch date defaults to signature date only when no kick-off call or launch date exists",
      "condition": "Missing launch date information"
    },
    {
      "exception": "Implementation date defaults to 1 month only when no date or time period is specified",
      "condition": "Missing implementation timeline"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: Talkable",
      "type": "Company Identity"
    },
    {
      "element": "Key contact: Sun Choi (fractional CFO)",
      "type": "Stakeholder Information"
    },
    {
      "element": "Business model: Referral marketing software solutions",
      "type": "Business Description"
    },
    {
      "element": "Billing model: Mix of annual/quarterly/monthly, approximately 50 bills per month",
      "type": "Billing Configuration"
    },
    {
      "element": "Contract structure: Frequently have ToS MSA + order form (2 separate documents)",
      "type": "Contract Structure"
    },
    {
      "element": "Feature requests: Rev rec ARR reporting, Custom dunning with customized messaging and post-30 day automated escalations, Late fees interest",
      "type": "Custom Requirements"
    },
    {
      "element": "Implementation dates: Start 3/20/24, Completed 4/3/24, MSA Signature 3/29/24",
      "type": "Timeline"
    },
    {
      "element": "ERP and Tax Integration fields (to be specified per merchant)",
      "type": "Integration Configuration"
    },
    {
      "element": "Rewatch call recordings for reference",
      "type": "Documentation"
    }
  ],
  "confidence_score": 0.85
}
```

---

