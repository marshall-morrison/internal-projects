# Raw LLM Analysis: Merchant Info Sheet - Operator.ai(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:06:39

---

## Chunk 1: Merchant Info Sheet - Operator.ai(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:06:39

### Original Content
```
Merchant Demo date: October 9 2024 Scoping start date: Oct 15, 2024 MSA Signature Date: Oct 31, 2024 Onboarding Kick Off Date: Nov 4, 2024 [If Exists] Opt Out Date: None Go Live Date: Nov 18, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Pleasant - COO Company summary (AE to fill) Operator ai generates revenue by providing advanced AI-driven tools that streamline sales operations, emphasizing quality engagement over volume By focusing on personalized, high-impact...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Quote Interpretation and Line Item Processing",
    "Discount and Payment Cadence Management",
    "Opt-out Clauses and Auto-renewal Handling",
    "Merchant Onboarding Timeline and Stakeholders"
  ],
  "rules": [
    "Send Slackbot message for the first invoice of the billing sequence when contract is processed",
    "Process all line items with amounts, quantity, and item name from quote",
    "Include start date, service period, and frequency from quote",
    "Use billing terms specified in quote",
    "Set integration item as 'Revenue: SaaS'",
    "Do not process $0 lines (there will be many)",
    "Refer to contract billing terms section on first page of quote for payment cadence and discounts",
    "Follow costs laid out in the invoice for billing setup, regardless of varying terms or opt-out clauses",
    "If quarterly billing with auto-renewal but charges outlined for full year, process for full year billed quarterly",
    "If opt-out clause exists but quote shows charges post opt-out, process all charges laid out in the quote",
    "Flag if instructions are unclear"
  ],
  "exceptions": [
    "Initial POC agreements have varying billing terms and invoice cadences",
    "Most initial POC agreements have opt-out auto-renewal clauses",
    "Many discounts expected for initial POC agreements",
    "When conflict exists between contract terms (e.g., opt-out clause) and quote charges, prioritize the quote charges",
    "Discount appears both as line item at bottom of quote and in billing terms section"
  ],
  "merchant_specific": [
    "Merchant name: Operator AI (Pleasant - COO is key contact)",
    "Merchant goal: Implement Tabs as primary billing tool for first batch of paying customers in late Nov/early Dec",
    "No opt-out clause for this merchant",
    "Specific timeline: Demo (Oct 9), Scoping (Oct 15), MSA Signature (Oct 31), Kickoff (Nov 4), Go Live (Nov 18)",
    "Company focus: AI-driven sales operations tools with personalized engagement approach",
    "Initial contracts come in form of quotes",
    "GTM POC and Implementation POC roles (to be filled)",
    "ERP and Tax Integration details (to be specified)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Operator.ai(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:06:46

### Original Content
```
Rules might evolve on a case by case basis, so if it unclear how to process the discount, please flag BUT, general rule of thumb: If the invoicing is recurring for the same amount, but there is a discount on the first invoice, then process the discount as a separate BT (since there is no way to apply a discount to only 1 invoice in a recurring BT) If the invoicing is set up where there are varying amounts between the first invoic and future invoices, then the discount can be applied directly to ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Discount Processing and Billing Treatment",
    "Customer and Contract Setup Procedures",
    "Default Values and Operational Standards",
    "Integration and Post-Processing Communications",
    "Merchant-Specific Billing Information and Relationship Management"
  ],
  "rules": [
    {
      "rule": "If invoicing is recurring for the same amount with a discount on first invoice, process discount as separate BT",
      "rationale": "No way to apply discount to only 1 invoice in a recurring BT"
    },
    {
      "rule": "If invoicing has varying amounts between first and future invoices, apply discount directly to first BT of sequence",
      "rationale": "Allows for proper discount application in non-uniform billing"
    },
    {
      "rule": "Create new customers for incoming contracts",
      "rationale": "Very rare for customers to already exist as they are just starting to bill"
    },
    {
      "rule": "Billing address is located at the top of the quote",
      "rationale": "Standard location for extraction"
    },
    {
      "rule": "Billing contact is in its own section at the bottom of the first page of the quote",
      "rationale": "Standard location for extraction"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "rationale": "Ops default standard"
    },
    {
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "rationale": "Ops default standard"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "rationale": "Ops default standard"
    },
    {
      "rule": "Every tax line item becomes a BT (if none listed)",
      "rationale": "Ops default for tax handling"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "rationale": "Integration-specific labeling requirement"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "rationale": "Integration-specific labeling requirement"
    },
    {
      "rule": "Customer Success (Azmat Aziz) needs to be notified in Messari internal merchant channel when contracts are processed in Active phase",
      "rationale": "Post-processing communication requirement"
    }
  ],
  "exceptions": [
    {
      "exception": "Rules may evolve on a case by case basis",
      "action": "Flag if unclear how to process discount"
    },
    {
      "exception": "Specifics processing things may differ by contract",
      "example": "Always back-date invoice date to final day of the month"
    },
    {
      "exception": "Pinata integration items labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "condition": "Merchant can override default labeling"
    },
    {
      "exception": "Special memos certain invoices require",
      "context": "Invoice changes due to merchant customer relationship"
    }
  ],
  "merchant_specific": [
    {
      "element": "Discount processing methodology",
      "customizable": true,
      "note": "May vary based on recurring vs. varying invoice amounts"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "examples": ["Statsig -> Sales", "Pinata -> Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "note": "Who to notify, where, and when varies by merchant"
    },
    {
      "element": "Invoice date handling",
      "customizable": true,
      "example": "Back-dating to final day of month"
    },
    {
      "element": "Merchant billing model",
      "note": "This merchant: SaaS billing, no overages initially, consumption product without credit system to begin"
    },
    {
      "element": "Customer volume expectations",
      "note": "This merchant: 20 customers by end of December, monthly payment via CC with Stripe"
    },
    {
      "element": "Merchant relationship information",
      "note": "This merchant: Pleasant and team easy to work with, fellow Primary company"
    },
    {
      "element": "Feature requests section",
      "customizable": true,
      "note": "Varies by merchant needs and urgency"
    },
    {
      "element": "Special customer information",
      "customizable": true,
      "note": "Special memos and invoice changes based on merchant-customer relationships"
    }
  ],
  "confidence_score": 0.85
}
```

---

