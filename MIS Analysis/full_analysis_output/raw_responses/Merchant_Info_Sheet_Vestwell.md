# Raw LLM Analysis: Merchant Info Sheet - Vestwell

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:53:08

---

## Chunk 1: Merchant Info Sheet - Vestwell_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:08

### Original Content
```
Use 0 04167  as the number to populate for the BT beMake sure to check  Use Billing Term reference in Garage Participant Level Fees   Either Unit Price or Tier Unit Price Event to use  Participants Month  Example below Default Service Term 1 year to start Default Net Payment Terms If None, Ops Default is 15 (Please make sure this is the default as it s specifically requested by Vestwell team) Default Billing Frequency There s four types of billing terms for Vestwell One time setup fee   one time...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Configuration and Terms",
    "Invoice Processing and Tax Handling",
    "Integration and Event Management",
    "Communication and Notification Protocols",
    "Merchant-Specific Customization Requirements"
  ],
  "rules": [
    {
      "rule": "Use 0 04167 as the number to populate for the BT (Billing Term)",
      "category": "billing_configuration"
    },
    {
      "rule": "Check Billing Term reference in Garage Participant Level Fees for Unit Price or Tier Unit Price Event",
      "category": "billing_configuration"
    },
    {
      "rule": "Default Service Term is 1 year to start",
      "category": "service_terms"
    },
    {
      "rule": "Default Net Payment Terms is 15 days (Ops Default if none specified)",
      "category": "payment_terms",
      "note": "Specifically requested by Vestwell team"
    },
    {
      "rule": "One-time setup fee billing frequency: one time only",
      "category": "billing_frequency"
    },
    {
      "rule": "Plan Level Fee billing frequency: monthly",
      "category": "billing_frequency"
    },
    {
      "rule": "Participant Level Fee billing frequency: monthly (every 3 months)",
      "category": "billing_frequency"
    },
    {
      "rule": "AUM fees billing frequency: monthly (every 3 months)",
      "category": "billing_frequency"
    },
    {
      "rule": "Invoice Date should always be the last day of the quarter",
      "category": "invoicing"
    },
    {
      "rule": "If no tax instructions listed, Ops Default is every tax line item becomes a BT Events",
      "category": "tax_handling"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling",
      "example": true
    },
    {
      "rule": "All 'Pinata' integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_labeling",
      "example": true
    }
  ],
  "exceptions": [
    {
      "exception": "Default Net Payment Terms of 15 days can be overridden if specified, but 15 is the fallback",
      "context": "payment_terms"
    },
    {
      "exception": "Pinata integration items default to 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "context": "integration_labeling"
    },
    {
      "exception": "Tax handling follows BT Events default only if none listed",
      "context": "tax_processing"
    },
    {
      "exception": "Special memos and invoice changes may be required due to merchant-customer relationships",
      "context": "customer_specific_invoicing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Vestwell-specific billing terms",
      "description": "Four types of billing terms specifically for Vestwell merchant",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Different merchants may have different integration partners (Statsig, Pinata) requiring specific labels",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Varies by merchant - who to notify, where, and when",
      "customizable": true,
      "example": "Customer Success [Azmat Aziz] via Messari internal merchant channel when contracts are processed"
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos and invoice modifications based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Events Processing instructions",
      "description": "To be filled by Implementation Success team per merchant",
      "customizable": true
    },
    {
      "element": "Feature Requests tracking",
      "description": "Merchant-specific feature requests with urgency and importance ratings",
      "customizable": true
    },
    {
      "element": "BT number assignment",
      "description": "Specific BT number (0 04167) may vary by merchant",
      "customizable": true
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Merchant Info Sheet - Vestwell_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:53:12

### Original Content
```
Merchant Demo date: Early 2024 Scoping start date: May 1, 2024 MSA Signature Date: Sep 30, 2024 Onboarding Kick Off Date: Oct 1, 2024 [If Exists] Opt Out Date: 4 1 2025 Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: (Sage) Tax Integration: Key people at Merchant Dave Sheen, CFO Brendan Keogh, VP Operational Finance - lead for all billing operational finance processes Eva Oleszczuk, Billing and AR Accountant - hands-on for all billing Adriana Morosanu, Senior Billing Manager - junior...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Billing Model and Fee Structure",
    "Contract Processing and Customer Segmentation",
    "Migration from Legacy System (Ordway)"
  ],
  "rules": [
    "Every customer must be split into 2 sub-customers: [Customer Name: Sponsor] and [Customer Name: Participant]",
    "Fees must be allocated to sub-customers based on whether they are paid by Sponsor or Participant",
    "One Time Setup Fees are typically sponsor fees and should be included in the sponsor fee portion using Flat Price Billing Type",
    "Plan Level Fees use Flat Price Billing Type with Monthly cadence and 12-period structure",
    "AUM Fees use Event Type billing with Quarterly cadence (every 3 months)",
    "AUM fees listed in contracts are annualized amounts and must be divided by 4 for quarterly processing",
    "Invoicing occurs once per quarter (4 times per year)",
    "Contract has an opt-out clause after 6 months (April 2025) if implementation is not successful",
    "Upon successful implementation, an annual contract will activate with opportunity to revisit commercials"
  ],
  "exceptions": [
    "The document contains a conflicting instruction: 'divide the number by 12 to monthly rate' when discussing AUM fees, but earlier states AUM fees are quarterly and should be 'divided by 4' - this appears to be an error in the documentation",
    "Current Ordway invoicing takes 5 days and involves manual overrides and CSV imports - this represents the problematic baseline to improve upon",
    "Opt-out date exists (April 1, 2025) as a conditional exit point if implementation fails",
    "Fee allocation depends on contract language specifying 'plan' vs 'participant' designation"
  ],
  "merchant_specific": [
    "Merchant Name: Vestwell (fintech company providing retirement planning solutions)",
    "Scale: ~5000 customers, ~$100M revenue",
    "ERP System: Sage",
    "Legacy System: Ordway (being transitioned away from)",
    "Key Personnel: Dave Sheen (CFO), Brendan Keogh (VP Operational Finance - lead), Eva Oleszczuk (Billing and AR Accountant - hands-on), Adriana Morosanu (Senior Billing Manager), Ann Bodnar (Senior Billing Specialist), Elizabeth Wick (Finance Manager - state reporting), Jonathan Ferrara (COO Platform Solutions), and others",
    "Specific Timeline: Demo (Early 2024), Scoping (May 1, 2024), MSA Signature (Sep 30, 2024), Onboarding Kickoff (Oct 1, 2024), Opt Out Date (April 1, 2025), Go Live (Jan 1, 2025)",
    "Industry-Specific Products: 401(k) and 403(b) retirement plans",
    "Billing Frequency: Quarterly (4x per year)",
    "Fee Types: One Time Setup Fees, Plan Level Fees, AUM (Assets Under Management) Fees",
    "Customer Segmentation Model: Sponsor vs Participant structure"
  ],
  "confidence_score": 0.85
}
```

**Note on Confidence Score Rationale:** The confidence is high (0.85) because the document provides clear structural rules and merchant details. However, it's not perfect (1.0) due to: (1) an apparent documentation error regarding AUM fee calculation (divide by 4 vs divide by 12), (2) incomplete sections marked as "(AE to fill)" and "(Implementation Success to fill)", and (3) some ambiguity around conditional fee allocation based on contract language interpretation.

---

