# Raw LLM Analysis: Wild Fruit- MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:26:05

---

## Chunk 1: Wild Fruit- MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:05

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term Refer to contract Default Net Payment Terms Default 15 if none listed Default Billing Frequency None if none is listed How do we handle taxes as a line item No tax Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) Default integration item for wild fruit is:  Presentation Design - Wild...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and Billing Configuration",
    "Default Value Assignment",
    "Tax and Line Item Handling",
    "Integration Item Processing",
    "Post-Processing Communication Workflows"
  ],
  "rules": [
    {
      "rule": "Invoice dates must always be back-dated to the final day of the month",
      "category": "invoicing",
      "explicit": true
    },
    {
      "rule": "Default net payment terms should be set to 15 days if none are listed",
      "category": "payment_terms",
      "explicit": true
    },
    {
      "rule": "Default billing frequency should be set to 'None' if none is listed",
      "category": "billing_frequency",
      "explicit": true
    },
    {
      "rule": "Tax should not be included as a line item",
      "category": "tax_handling",
      "explicit": true
    },
    {
      "rule": "Default integration item for Wild Fruit must be 'Presentation Design - Wild Fruit', NOT 'Professional Fees'",
      "category": "integration_items",
      "explicit": true
    },
    {
      "rule": "Service term should refer to contract for default value",
      "category": "service_terms",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "communication",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Wild Fruit merchant requires specific integration item naming convention (Presentation Design - Wild Fruit instead of Professional Fees)",
      "context": "integration_items"
    },
    {
      "exception": "Default values only apply when no value is explicitly listed in the contract",
      "context": "default_assignment"
    },
    {
      "exception": "Events processing and integration items processing are conditional (marked as 'if necessary')",
      "context": "processing_requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Wild Fruit integration item naming",
      "description": "Specific requirement for 'Presentation Design - Wild Fruit' instead of generic 'Professional Fees'",
      "customizable": true
    },
    {
      "element": "Events billing information",
      "description": "Merchant-specific events billing details to be filled by Implementation Success team",
      "customizable": true
    },
    {
      "element": "Post-processing notification recipients",
      "description": "Example shows Customer Success (Charlie Niesenbaum) for Red Antler merchant - varies by merchant",
      "customizable": true
    },
    {
      "element": "Notification channels",
      "description": "Merchant-specific channels (e.g., 'Red Antler merchant channel')",
      "customizable": true
    },
    {
      "element": "Notification timing and phase",
      "description": "When to notify varies by merchant phase (Implementation vs Active)",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Wild Fruit- MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:05

### Original Content
```
Contract Processing Steps (Implementation Success to fill) Garage Example of Contract Processed  For renewal contracts, process all BTs under the renewal contract Contracts that already have a Sent  Paid invoice cannot have their Billing Terms changed New Edits   Additions   Requests from the merchant will have to go on an entirely new contract and will be on a separate invoice When you see a sent invoice on the contact in garage, ask the US team to duplicate the contract to put the new BTs unde...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Invoice Processing Workflow",
    "Billing Terms and Revenue Schedule Management",
    "Data Field Mapping and Extraction Rules",
    "Customer Identification and Creation Procedures",
    "Contract Modification and Renewal Handling"
  ],
  "rules": [
    "For renewal contracts, process all Billing Terms (BTs) under the renewal contract",
    "Contracts with Sent/Paid invoices cannot have Billing Terms changed",
    "New edits, additions, or requests from merchants must go on an entirely new contract with separate invoice",
    "Service Start Date: Use signature date of contract; if no signature, use date in top left of first page",
    "Total Months of Service: Default to 1 month",
    "Item Name: Use project name from email body; if unavailable, flag to US team",
    "When merchant requests invoice generation, match item name with integration item",
    "Integration Item: Found by scrolling to FEES section",
    "Total Price: Each bullet in FEES section becomes its own revenue schedule with potentially different pricing",
    "Quantity: Default to 1",
    "Start Date for first rev schedule/bullet/payment: Same as service start date",
    "Start Date for subsequent bullets: Add 1 month increments (2nd bullet = +1 month, 3rd bullet = +2 months, etc.)",
    "Frequency: None unless otherwise stated",
    "Net Terms: Refer to contract",
    "Product Description: Add 'Product Name' field from email to product description in line item",
    "Customer Name: Choose from email specification, not filename",
    "For Wild Fruit: Client Director is always Andy Meehan (Director ID: 7577)",
    "Follow Red Antler Customer Creation Workflow for customer creation",
    "Ignore total price of services in first sentence of fees section; refer to bullets instead"
  ],
  "exceptions": [
    "When a sent invoice exists on contact in garage, ask US team to duplicate the contract for new BTs",
    "Wild Fruit has two customers: 'AceCap' and 'Ace' - must double-check to confirm correct customer when seeing 'Ace'",
    "Specifics may differ by contract based on merchant requests",
    "If project name not available in email body, escalate/flag to US team"
  ],
  "merchant_specific": [
    "Example contract reference: a3f5017e-184f-49a8-aaa0-c8aa6f2abde4 (Daydream SOW1 Brand Marketing)",
    "RA 273 reference: 128bcd76-b466-42cc-a8c1-49d315d5a0b4 with line item format 'Agency Fees - [Project Name]'",
    "Wild Fruit specific: Always use Andy Meehan as Client Director (ID: 7577)",
    "Wild Fruit specific: Two customers named 'AceCap' and 'Ace' requiring verification",
    "Red Antler Customer Creation Workflow referenced for customer setup",
    "Integration item example: 'Presentation Design'",
    "Merchant-specific contract processing variations noted as possible"
  ],
  "confidence_score": 0.75
}
```

---

