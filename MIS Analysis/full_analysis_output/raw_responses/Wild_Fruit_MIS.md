# Raw LLM Analysis: Wild Fruit- MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:17:43

---

## Chunk 1: Wild Fruit- MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:17:43

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
    "Ignore total price of services in first sentence of fees section; refer to bullets instead"
  ],
  "exceptions": [
    "When sent invoice exists on contact in garage, ask US team to duplicate contract for new BTs",
    "Special case for Wild Fruit customers: Two customers exist (AceCap and Ace) - must double-check correct customer when seeing 'Ace'",
    "Contract-specific processing may differ based on merchant requests",
    "If project name not available in email body, escalate to US team rather than proceeding"
  ],
  "merchant_specific": [
    "Red Antler Customer Creation Workflow (referenced as separate process to follow)",
    "Wild Fruit specific: Always use Andy Meehan as Client Director with ID 7577",
    "Wild Fruit specific: Customer disambiguation between AceCap and Ace",
    "Example contract reference: a3f5017e-184f-49a8-aaa0-c8aa6f2abde4 for Daydream SOW1 Brand Marketing",
    "Example RA reference: 273 128bcd76-b466-42cc-a8c1-49d315d5a0b4",
    "Integration item example: 'Presentation Design' for specific invoice types",
    "Product naming convention: 'Agency Fees - [Project Name]' format for line items",
    "Garage system references (merchant's contract management system)"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Wild Fruit- MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:17:45

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term Refer to contract Default Net Payment Terms Default 15 if none listed Default Billing Frequency None if none is listed How do we handle taxes as a line item No tax Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) Default integration item for wild fruit is:  Presentation Design - Wild...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and Billing Configuration",
    "Default Values and Fallback Rules",
    "Tax Handling Procedures",
    "Integration Item Management",
    "Post-Processing Communication Protocols"
  ],
  "rules": [
    {
      "rule": "Always back-date invoice date to final day of the month",
      "category": "Invoice Dating",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms to 15 days if none listed",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency to None if none is listed",
      "category": "Billing Frequency",
      "explicit": true
    },
    {
      "rule": "Do not include tax as a line item",
      "category": "Tax Handling",
      "explicit": true
    },
    {
      "rule": "Default integration item for Wild Fruit is 'Presentation Design - Wild Fruit'",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Do NOT use 'Professional Fees' as integration item for Wild Fruit",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing information",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing information",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications information",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication Protocol",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Wild Fruit merchant has specific integration item requirement ('Presentation Design - Wild Fruit' instead of 'Professional Fees')",
      "applies_to": "Wild Fruit merchant only"
    },
    {
      "exception": "Default values only apply when no value is explicitly listed in contract",
      "applies_to": "Net Payment Terms and Billing Frequency"
    },
    {
      "exception": "Events billing processing is conditional (only 'if necessary')",
      "applies_to": "Events Processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Service Term",
      "description": "Must refer to individual contract for each merchant",
      "customization_required": true
    },
    {
      "element": "Integration Item naming",
      "description": "Wild Fruit uses 'Presentation Design - Wild Fruit' specifically",
      "customization_required": true
    },
    {
      "element": "Events billing information",
      "description": "Varies by merchant, filled by Implementation Success team",
      "customization_required": true
    },
    {
      "element": "Post-processing notification recipients",
      "description": "Example shows Charlie Niesenbaum for Red Antler merchant, varies by merchant",
      "customization_required": true
    },
    {
      "element": "Notification channel",
      "description": "Example shows 'Red Antler merchant channel', specific to each merchant",
      "customization_required": true
    },
    {
      "element": "Notification timing",
      "description": "When to notify varies by merchant phase and process completion",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

