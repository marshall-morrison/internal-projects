# Raw LLM Analysis: Merchant Info Sheet - Statsig

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:03:32

---

## Chunk 1: Merchant Info Sheet - Statsig_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:03:32

### Original Content
```
Statsig Scoping start date: Apr 3, 2024 Implementation Completed Date (Go live date): May 10, 2024 MSA Signature Date: Apr 30, 2024 GTM POC: ERP: Tax Integration: Anrok via QBO Key people at Merchant Lauren Burke  lauren statsig com  Head of Revenue Ops Very interested in our key terms tracking functionality Stephen Praast  stephen statsig com  Head of Finance Signatory and keen on invoicing Company summary  Thousands of companies, from startups to Fortune 500s, rely on Statsig: the single platf...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Management",
    "Usage-Based Billing and Tracking",
    "Invoice Automation and ERP Integration",
    "Collections and Accounts Receivable",
    "Contract Processing Workflow"
  ],
  "rules": [
    "Billing starts at the start of the subscription term (ignore signature date and other dates)",
    "All contracts have a one-page order form with Statsig logo containing necessary information",
    "Do not create any Billing Transactions (BTs) for overages",
    "All usage-based terms should be skipped during processing",
    "Billable Events Line Items are written as Flat Price BTs (not in arrears)",
    "Integration with Anrok via QuickBooks Online (QBO) for tax",
    "If customer does not exist in QBO, create the customer record",
    "Leave integration items blank or assign to Sales until future guidance provided",
    "Only process the one-page order form; skip other PDF content",
    "Usage data uploads trigger overages or create visibility into waived amounts"
  ],
  "exceptions": [
    "Legacy pricing models require support alongside future models due to pricing evolution",
    "95% of customer contracts have usage-based billing but it is not uniformly enforced",
    "Some contracts are quarterly and monthly (exception to 'mostly annual' pattern)",
    "Future contracts will have Stephen provide guidance on integration items (deviation from current blank/Sales assignment)"
  ],
  "merchant_specific": [
    "Statsig-specific terminology: 'Billable Events', 'events' as contracted quantity metric",
    "Key contacts: Lauren Burke (Head of Revenue Ops), Stephen Praast (Head of Finance)",
    "Statsig logo on order forms as identifier for processing",
    "ERP system: QuickBooks Online (QBO)",
    "Tax integration: Anrok via QBO",
    "Billing model: Mostly annual, some quarterly/monthly, fixed price upfront",
    "Product focus: Feature shipping, testing, and analysis platform",
    "Specific pain points: manual invoicing, spreadsheet-based AR, high DSO, aging receivables",
    "Implementation timeline: Scoping Apr 3, 2024; Go-live May 10, 2024; MSA signed Apr 30, 2024"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Statsig_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:03:36

### Original Content
```
Leave all quantities as 1 and instead put the quantity of events in the description field This is essential because QBO cannot support a quantity over 100b See attached screenshot for explanation: Events Processing (if necessary) N A Customer Information N A Feature Requests N A Rewatch Calls Onboarding v1   https: tabs rewatch com video x8cplq61by5559wv-stephen-praast-and-matthew-skoro-may-9-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Quantity field handling and workarounds",
    "QuickBooks Online (QBO) system limitations",
    "Data entry procedures for high-volume events",
    "Documentation and reference materials",
    "Process standardization for event processing"
  ],
  "rules": [
    {
      "rule": "Always set quantity field to 1 regardless of actual quantity",
      "category": "data_entry",
      "priority": "critical",
      "rationale": "QBO system limitation"
    },
    {
      "rule": "Enter actual quantity of events in the description field instead of quantity field",
      "category": "data_entry",
      "priority": "critical",
      "rationale": "Workaround for QBO quantity limitation"
    },
    {
      "rule": "QBO cannot support quantities over 100 billion",
      "category": "system_limitation",
      "priority": "high",
      "rationale": "Technical constraint of QuickBooks Online platform"
    },
    {
      "rule": "Reference attached screenshot for explanation when needed",
      "category": "documentation",
      "priority": "medium",
      "rationale": "Supporting documentation available"
    }
  ],
  "exceptions": [
    {
      "condition": "Events Processing (if necessary)",
      "note": "Marked as N/A, suggesting this process may not apply in all cases or contexts"
    },
    {
      "condition": "Customer Information marked as N/A",
      "note": "May indicate this instruction applies regardless of customer-specific details"
    },
    {
      "condition": "Feature Requests marked as N/A",
      "note": "Suggests this is not related to feature request processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Quantity threshold of 100 billion",
      "customization_needed": false,
      "note": "This appears to be a QBO platform limitation rather than merchant-specific"
    },
    {
      "element": "Events processing workflow",
      "customization_needed": true,
      "note": "The specific handling of 'events' may vary by merchant type and business model"
    },
    {
      "element": "Description field format for quantities",
      "customization_needed": true,
      "note": "Merchants may need specific formatting standards for how quantities are documented in descriptions"
    },
    {
      "element": "Rewatch video reference",
      "customization_needed": true,
      "note": "Training materials and onboarding documentation are merchant/team specific"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The core rule about quantity handling is clearly stated and critical
- Context is somewhat fragmented with N/A markers and incomplete sentences
- The QBO limitation (100b) is specific and verifiable
- Some ambiguity around what constitutes "events" in this context
- Reference to external materials (screenshot, video) that aren't available for full context
- The document appears to be an excerpt from a larger instruction set

---

