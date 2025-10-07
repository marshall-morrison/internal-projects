# Raw LLM Analysis: Merchant Info Sheet - Operator.ai

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:21:49

---

## Chunk 1: Merchant Info Sheet - Operator.ai_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:21:49

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
    "Set integration item as Revenue: SaaS",
    "Do not process $0 lines (there will be many)",
    "Refer to contract billing terms section on first page of quote for payment cadence and discounts",
    "Follow the costs laid out in the invoice for billing setup, regardless of varying terms or opt-out clauses",
    "If contract says quarterly with auto-renewal but charges are outlined for full year, process for a year billed quarterly",
    "If there is an opt-out clause but quote lays out charges post opt-out, still process all charges laid out in the quote",
    "Discount information appears both in contract billing terms section and as a line item at bottom of quote",
    "Flag if instructions are unclear"
  ],
  "exceptions": [
    "Initial POC agreements have varying billing terms and invoice cadences",
    "Most initial POC agreements will have some sort of opt-out auto-renewal clause",
    "There will be many discounts for initial POC agreements",
    "When opt-out clauses conflict with charges outlined in quote, prioritize the charges in the quote",
    "Quote takes precedence over contract terms when determining what to bill"
  ],
  "merchant_specific": [
    "Merchant Demo date: October 9 2024",
    "Scoping start date: Oct 15, 2024",
    "MSA Signature Date: Oct 31, 2024",
    "Onboarding Kick Off Date: Nov 4, 2024",
    "Go Live Date: Nov 18, 2024",
    "No Opt out clause for this merchant",
    "Merchant name: Pleasant (COO is key contact)",
    "Company: Operator ai - generates revenue through AI-driven sales operations tools",
    "Merchant goal: Implement Tabs as primary billing tool for first batch of paying customers arriving late Nov/early December",
    "Pain point: Need automated system to handle billing for incoming customers",
    "Initial contracts come in the form of a quote",
    "GTM POC and Implementation POC roles (to be filled)",
    "ERP and Tax Integration details (to be specified)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Operator.ai_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:21:56

### Original Content
```
Rules might evolve on a case by case basis, so if it unclear how to process the discount, please flag BUT, general rule of thumb: If the invoicing is recurring for the same amount, but there is a discount on the first invoice, then process the discount as a separate BT (since there is no way to apply a discount to only 1 invoice in a recurring BT) If the invoicing is set up where there are varying amounts between the first invoic and future invoices, then the discount can be applied directly to ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Discount Processing and Billing Treatment (BT)",
    "Customer and Contract Setup Procedures",
    "Default Values and Operational Standards",
    "Integration and Post-Processing Communications",
    "Merchant-Specific Billing Information and Relationship Management"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Discount Processing",
      "description": "If invoicing is recurring for the same amount with a discount on first invoice, process discount as a separate BT (cannot apply discount to only 1 invoice in recurring BT)"
    },
    {
      "rule_id": "R2",
      "category": "Discount Processing",
      "description": "If invoicing has varying amounts between first and future invoices, discount can be applied directly to the first BT of the sequence"
    },
    {
      "rule_id": "R3",
      "category": "Customer Setup",
      "description": "Create new customers for contracts that come in (rare for customer to already exist as they are just starting to bill)"
    },
    {
      "rule_id": "R4",
      "category": "Customer Information",
      "description": "Billing address is located at the top of the quote"
    },
    {
      "rule_id": "R5",
      "category": "Customer Information",
      "description": "Billing contact is in its own section at the bottom of the first page of the quote"
    },
    {
      "rule_id": "R6",
      "category": "Default Values",
      "description": "Default Service Term if none listed: 1 Year"
    },
    {
      "rule_id": "R7",
      "category": "Default Values",
      "description": "Default Net Payment Terms if none listed: 0"
    },
    {
      "rule_id": "R8",
      "category": "Default Values",
      "description": "Default Billing Frequency if none listed: Monthly"
    },
    {
      "rule_id": "R9",
      "category": "Tax Processing",
      "description": "Default tax handling: every tax line item becomes a BT"
    },
    {
      "rule_id": "R10",
      "category": "Integration Items",
      "description": "All Statsig integration items should be labeled as 'Sales'"
    },
    {
      "rule_id": "R11",
      "category": "Integration Items",
      "description": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
    },
    {
      "rule_id": "R12",
      "category": "Post-Processing",
      "description": "Customer Success [Azmat Aziz] needs to be notified in Messari internal merchant channel when contracts are processed [Merchant Phase: Active]"
    },
    {
      "rule_id": "R13",
      "category": "General Process",
      "description": "Flag for review if unclear how to process discount - rules evolve case by case"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Discount processing method varies based on whether invoicing is recurring with same amount vs. varying amounts",
      "condition": "Recurring same amount = separate BT; Varying amounts = apply to first BT"
    },
    {
      "exception_id": "E2",
      "description": "Pinata integration items labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "condition": "Merchant can override default labeling"
    },
    {
      "exception_id": "E3",
      "description": "Merchant may request specific processing differences by contract (e.g., always back-date invoice date to final day of month)",
      "condition": "Contract-specific merchant requests"
    },
    {
      "exception_id": "E4",
      "description": "Special memos may be required for certain invoices due to merchant-customer relationship",
      "condition": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing Model",
      "description": "Starting with SaaS billing, no overages initially; consumption product but not using credit system to begin with"
    },
    {
      "element": "Customer Volume",
      "description": "20 customers expected by end of December"
    },
    {
      "element": "Payment Method",
      "description": "Monthly payment, more than likely credit card with Stripe"
    },
    {
      "element": "Merchant Relationship",
      "description": "Pleasant and team have been easy to work with; Operator is a fellow Primary company"
    },
    {
      "element": "Notification Recipients",
      "description": "Customer Success [Azmat Aziz] - Messari internal merchant channel"
    },
    {
      "element": "Integration Examples",
      "description": "Statsig and Pinata mentioned as specific integration examples with labeling rules"
    },
    {
      "element": "Template Sections",
      "description": "Document contains fillable sections for Implementation Success team (Events Processing, Integration Items, Post Processing Communications, Customer Information, Feature Requests, Rewatch Calls)"
    },
    {
      "element": "Discount Example",
      "description": "Specific example provided: First invoice 14,000 - Discount 3,500; 84,000 over 12 months at 7k per month"
    }
  ],
  "confidence_score": 0.85
}
```

---

