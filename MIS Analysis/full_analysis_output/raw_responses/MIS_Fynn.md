# Raw LLM Analysis: MIS_Fynn

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:51:04

---

## Chunk 1: MIS_Fynn_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:51:04

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
    "Service Date Calculation and Timeline Management",
    "Implementation and Post-Go-Live Processing",
    "Merchant-Specific Customization Requirements"
  ],
  "rules": [
    {
      "rule": "Service Start Date must be derived from the 'Effective Date' in the agreement, or contract signature date if Effective Date is absent",
      "category": "Date Calculation"
    },
    {
      "rule": "Months of Service must be extracted from the Contract Term field",
      "category": "Contract Terms"
    },
    {
      "rule": "Item Name must be listed under Product field",
      "category": "Product Mapping"
    },
    {
      "rule": "Item Description field should be left blank",
      "category": "Product Mapping"
    },
    {
      "rule": "Fynn seats must be mapped to Fynn QBO Item in Integration Item",
      "category": "Integration Mapping"
    },
    {
      "rule": "Implementation Fees must be mapped to Fynn Implementation Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Fynn seats must be mapped to Usage Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Implementation Fees must be mapped to Service Revenue Category",
      "category": "Revenue Categorization"
    },
    {
      "rule": "Billing Type should be set as Flat and Unit",
      "category": "Billing Configuration"
    },
    {
      "rule": "Total Price must reference the Net Total column from contract",
      "category": "Pricing"
    },
    {
      "rule": "A separate unit BT (Billing Type) must be created for the Fynn List Price",
      "category": "Billing Configuration"
    },
    {
      "rule": "Quantity must be extracted from the Quantity column",
      "category": "Pricing"
    },
    {
      "rule": "Start Date for Fynn flat fee and unit fee requires adding 2 months to the Effective Date",
      "category": "Date Calculation"
    },
    {
      "rule": "Implementation one-time fees start on the effective date (no 2-month addition)",
      "category": "Date Calculation"
    },
    {
      "rule": "Periods must reference the months of service",
      "category": "Billing Configuration"
    },
    {
      "rule": "Frequency is usually monthly billing cycle, but must be verified in paragraph under pricing table",
      "category": "Billing Configuration"
    },
    {
      "rule": "Net Terms must be extracted from Payment Terms field",
      "category": "Payment Terms"
    }
  ],
  "exceptions": [
    {
      "exception": "If Effective Date is not present in agreement, use contract signature date as fallback",
      "condition": "Missing Effective Date"
    },
    {
      "exception": "Implementation one-time fees have different start date calculation (no 2-month addition) compared to recurring fees",
      "condition": "Fee Type: One-time vs Recurring"
    },
    {
      "exception": "Billing frequency should be verified in contract paragraph rather than assumed to be monthly",
      "condition": "Non-standard billing cycles"
    },
    {
      "exception": "Merchant may have specific processing requests that differ by contract",
      "condition": "Contract-specific variations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Fynn Implementation POC and CX POC",
      "description": "Merchant-specific point of contact information to be filled by implementation team",
      "customization_required": true
    },
    {
      "element": "Billing model section",
      "description": "Unique customer creation process and billing methodology specific to merchant",
      "customization_required": true
    },
    {
      "element": "Contract structure",
      "description": "How the merchant's contract is broken up and organized",
      "customization_required": true
    },
    {
      "element": "One-off merchant characteristics",
      "description": "Unique aspects specific to this merchant's operations",
      "customization_required": true
    },
    {
      "element": "Items to ignore in contracts",
      "description": "Merchant-specific exclusions during contract processing",
      "customization_required": true
    },
    {
      "element": "Contract-specific processing variations",
      "description": "Specific processing requests that may differ by individual contract",
      "customization_required": true
    },
    {
      "element": "Fynn-specific product mappings",
      "description": "Fynn QBO Item, Fynn seats, and Fynn-specific revenue categories",
      "customization_required": false,
      "note": "Specific to Fynn merchant"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_Fynn_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:51:06

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 15 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Process...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Operational Parameters and Billing Configuration",
    "Integration and Event Processing Workflows",
    "Post-Processing Communication and Notification Protocols",
    "Customer-Specific Billing Requirements and Relationships",
    "Merchant Onboarding and Implementation Documentation"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "specificity": "Always applies"
    },
    {
      "rule": "Default Service Term is 1 Year when none is listed",
      "category": "Billing Configuration",
      "specificity": "Default/Fallback"
    },
    {
      "rule": "Default Net Payment Terms is 15 days when none specified",
      "category": "Payment Terms",
      "specificity": "Default/Fallback"
    },
    {
      "rule": "Default Billing Frequency is Monthly when none listed",
      "category": "Billing Configuration",
      "specificity": "Default/Fallback"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "specificity": "Default/Fallback"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Processing",
      "specificity": "Vendor-specific example"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Processing",
      "specificity": "Vendor-specific example with exception clause"
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "Role-based"
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "Role-based"
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "Role-based"
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "Role-based"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "Phase-dependent"
    },
    {
      "rule": "AE fills Merchant Calls for all videos prior to Implementation involvement; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Documentation",
      "specificity": "Phase-dependent"
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can be labeled differently if 'otherwise noted by Merchant'",
      "condition": "Merchant provides specific instructions",
      "impact": "Overrides default 'Software Subscription Bundle' label"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "condition": "Specific customer relationships exist",
      "impact": "Invoice changes may be required"
    },
    {
      "exception": "Usage is pro-rated based on active users",
      "condition": "Seat-based usage billing model",
      "impact": "Billing calculation varies by active user count"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling instructions",
      "customization_type": "Vendor-specific mapping rules",
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification requirements",
      "customization_type": "Stakeholder notification protocols",
      "examples": ["Customer Success [Azmat Aziz] notification in Messari internal merchant channel when contracts are processed"]
    },
    {
      "element": "Customer-specific invoice requirements",
      "customization_type": "Special memos and invoice modifications",
      "examples": ["Special memo requirements based on merchant-customer relationships"]
    },
    {
      "element": "Billing model structure",
      "customization_type": "Revenue model configuration",
      "examples": ["Upfront SaaS fee per location", "Parent-child relationships", "Seat-based usage pro-rated by active users"]
    },
    {
      "element": "Merchant temperament and preferences",
      "customization_type": "Relationship management notes",
      "examples": ["Nice, straight-forward", "Used to Chargebee", "Cares about parent-child relationships, reporting, revrec, automated billing, dunning"]
    },
    {
      "element": "Feature priorities",
      "customization_type": "Product focus areas",
      "examples": ["Parent-child relationships", "Reporting and revrec", "Automated billing", "Dunning and payment collection"]
    },
    {
      "element": "Events billing processing",
      "customization_type": "Event-based billing configuration",
      "examples": ["Processed if necessary, filled Post-Go Live"]
    }
  ],
  "confidence_score": 0.85
}
```

---

