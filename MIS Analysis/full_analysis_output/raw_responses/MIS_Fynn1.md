# Raw LLM Analysis: MIS_Fynn(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:05:08

---

## Chunk 1: MIS_Fynn(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:05:08

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 15 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Process...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Operational Parameters and Billing Configuration",
    "Post-Implementation Processing and Workflow Management",
    "Merchant-Specific Customer Handling and Communication Protocols",
    "Integration and Tax Line Item Processing",
    "Stakeholder Notification and Documentation Requirements"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 15 days if none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) if no other instruction listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "AE fills Merchant Calls for videos prior to Implementation involvement; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Workflow Ownership",
      "explicit": true
    },
    {
      "rule": "AE fills Notes Sections if available; Implementation is completion DRI on handoff",
      "category": "Workflow Ownership",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "Merchant provides alternative labeling instructions",
      "default_behavior": "Label as 'Software Subscription Bundle'"
    },
    {
      "exception": "Default operational parameters (Service Term, Payment Terms, Billing Frequency) only apply when none are specified",
      "condition": "If merchant provides specific values",
      "default_behavior": "Use operational defaults"
    },
    {
      "exception": "Tax line item processing may vary if specific instructions are provided",
      "condition": "If merchant provides tax handling instructions",
      "default_behavior": "Convert every tax line item to BT"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Specific customer relationships require customization",
      "default_behavior": "Standard invoice processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing instructions",
      "customization_required": true,
      "filled_by": "Implementation Success Post-Go Live"
    },
    {
      "element": "Integration item labeling rules",
      "customization_required": true,
      "examples": ["Statsig -> Sales", "Pinata -> Software Subscription Bundle"],
      "note": "Merchant may override defaults"
    },
    {
      "element": "Post-processing notification requirements",
      "customization_required": true,
      "components": ["Who to notify", "Where to notify", "When to notify"],
      "example": "Customer Success [Azmat Aziz] in Messari internal merchant channel when contracts processed in Active phase"
    },
    {
      "element": "Customer-specific information and special memos",
      "customization_required": true,
      "note": "Varies by merchant customer relationships"
    },
    {
      "element": "Billing model details",
      "customization_required": true,
      "example_provided": "Upfront SaaS fee per location, parent-child relationships, seat-based usage pro-rated by active users"
    },
    {
      "element": "Merchant temperament and preferences",
      "customization_required": true,
      "example_provided": "Nice, straight-forward, used to Chargebee, values parent-child relationships, reporting, revrec, automated billing, dunning"
    },
    {
      "element": "Key features merchant POC cares about",
      "customization_required": true,
      "example_provided": "Parent-child relationships, reporting and revrec, automated billing, dunning and payment collection"
    },
    {
      "element": "Feature requests with urgency levels",
      "customization_required": true,
      "components": ["What it is", "Why it's important", "Urgency"]
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_Fynn(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:05:08

### Original Content
```
Merchant Name: Fynn Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Service Start Date: Refer to the "Effective Date" listed in the agreement If n...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Mapping",
    "Billing Configuration and Revenue Categorization",
    "Service Timeline and Date Calculations",
    "Merchant-Specific Implementation Requirements",
    "Integration and Item Mapping Procedures"
  ],
  "rules": [
    {
      "rule": "Service Start Date must be derived from the 'Effective Date' in the agreement, or contract signature date if Effective Date is absent",
      "category": "Date Calculation"
    },
    {
      "rule": "Add 2 months to the Effective Date for Fynn flat fee and unit fee start dates",
      "category": "Date Calculation"
    },
    {
      "rule": "Implementation one-time fees start on the Effective Date (no 2-month delay)",
      "category": "Date Calculation"
    },
    {
      "rule": "Map Fynn seats to Fynn QBO Item in Integration Item field",
      "category": "Item Mapping"
    },
    {
      "rule": "Map Implementation Fees to Fynn Implementation Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Map Fynn seats to Usage Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Map Implementation Fees to Service Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Billing Type should be set as 'Flat and Unit'",
      "category": "Billing Configuration"
    },
    {
      "rule": "Total Price should reference the 'Net Total' column from contract",
      "category": "Pricing"
    },
    {
      "rule": "Create a separate unit BT (Billing Type) for the Fynn List Price",
      "category": "Billing Configuration"
    },
    {
      "rule": "Quantity should reference the 'Quantity' column from contract",
      "category": "Pricing"
    },
    {
      "rule": "Periods should reference the months of service from contract",
      "category": "Billing Configuration"
    },
    {
      "rule": "Default billing frequency is monthly unless specified otherwise in contract",
      "category": "Billing Configuration"
    },
    {
      "rule": "Net Terms should reference 'Payment Terms' from contract",
      "category": "Payment Configuration"
    },
    {
      "rule": "Item Description field should be left blank",
      "category": "Item Mapping"
    },
    {
      "rule": "Item Name should be listed under Product in contract",
      "category": "Item Mapping"
    },
    {
      "rule": "Months of Service should reference Contract Term",
      "category": "Contract Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "If Effective Date is not present in agreement, use contract signature date as fallback",
      "condition": "Missing Effective Date"
    },
    {
      "exception": "Implementation one-time fees do not follow the 2-month delay rule applied to recurring fees",
      "condition": "One-time vs Recurring Fees"
    },
    {
      "exception": "Billing frequency may differ from monthly default - must check paragraph under pricing table",
      "condition": "Non-standard billing cycles"
    },
    {
      "exception": "Merchant may have specific processing requests that differ by contract",
      "condition": "Contract-specific variations"
    },
    {
      "exception": "Some contract elements should be ignored (section incomplete but referenced)",
      "condition": "Contract processing exclusions"
    }
  ],
  "merchant_specific": [
    {
      "element": "Fynn Implementation POC and CX POC",
      "description": "Merchant-specific contact information to be filled by implementation team",
      "customizable": true
    },
    {
      "element": "Billing model details",
      "description": "Unique customer creation process and billing structure specific to Fynn",
      "customizable": true
    },
    {
      "element": "Fynn QBO Item mapping",
      "description": "Specific integration item for Fynn's QuickBooks Online setup",
      "customizable": true
    },
    {
      "element": "Fynn seats terminology",
      "description": "Merchant-specific product terminology for user licenses",
      "customizable": true
    },
    {
      "element": "Fynn Implementation Revenue Category",
      "description": "Custom revenue category specific to Fynn's accounting structure",
      "customizable": true
    },
    {
      "element": "Contract-specific processing variations",
      "description": "Merchant may request different processing approaches per individual contract",
      "customizable": true
    },
    {
      "element": "2-month delay for recurring fees",
      "description": "Fynn-specific timing rule for when recurring billing begins",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document is clearly a template with incomplete sections (marked with placeholders like "IM to fill", "IMP to Add", "Implementation to fill")
- Some instructions are clear and specific (date calculations, mapping rules)
- However, several sections are explicitly incomplete or cut off (e.g., "Anything to ignore in contracts" and "Specifics processing things...")
- The structure suggests this is a work-in-progress implementation guide
- Core rules are extractable, but context about exceptions and edge cases is limited

---

