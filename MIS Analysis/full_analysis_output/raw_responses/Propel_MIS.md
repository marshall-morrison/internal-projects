# Raw LLM Analysis: Propel MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:59:14

---

## Chunk 1: Propel MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:59:14

### Original Content
```
Propel (AE to fill) Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Service Start Date: Locate the campaign start date mentioned in the contract M...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Implementation and Setup Process",
    "Billing Configuration and Payment Terms",
    "Contract Data Extraction and Processing",
    "Stakeholder Roles and Responsibilities",
    "Service Agreement Parameters and Timelines"
  ],
  "rules": [
    "Service Start Date must be located from campaign start date in contract",
    "Months of Service determined by checking campaign end date",
    "Item Description field should be left blank",
    "Integration Item field should be left blank",
    "Billing Type must be set to 'Flat'",
    "Total Price must include all contract updates and amendments",
    "Quantity should reference pricing structure (e.g., cost per click) and unit measurement",
    "Start Date requires confirmation from agreement effective date or campaign launch",
    "Start Date can be back-dated from due date if needed",
    "Contract periods must be identified as recurring, fixed-term, or subject to renewal",
    "Invoice frequency must be determined and documented",
    "Item Name should reflect service type (e.g., 'User Acquisition Campaign')",
    "Minimum and maximum amounts must be identified where applicable",
    "Late fees must be documented where applicable"
  ],
  "exceptions": [
    "Merchant-specific processing requests that may differ by contract",
    "Contract items that should be ignored during processing (merchant-specific)",
    "Unique customer creation processes that vary by merchant",
    "One-off merchant requirements outside standard procedures",
    "Contract structure variations (how contract is broken up)"
  ],
  "merchant_specific": [
    "Propel field (to be filled by AE)",
    "Implementation POC (to be filled by IM)",
    "CX POC (to be added by IMP)",
    "Billing model section (Implementation team responsibility)",
    "Unique customer creation process per merchant",
    "Merchant-specific billing methods",
    "Contract breakdown structure (varies by merchant)",
    "Merchant-requested processing specifications",
    "Items to ignore in contracts (merchant-dependent)",
    "Campaign-specific terminology and service names"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Propel MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:59:17

### Original Content
```
g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Proces...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Post-processing communication and notification workflows",
    "Merchant-specific billing and customer handling procedures",
    "Integration item categorization and labeling",
    "Feature requests and merchant relationship management"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Default Service Term is 1 Year when none is listed",
      "category": "Service Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 when none is specified",
      "category": "Payment Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Default Billing Frequency is Monthly when none is listed",
      "category": "Billing Frequency",
      "specificity": "explicit"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Handling",
      "specificity": "explicit"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "specificity": "explicit"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Labeling",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibility Assignment",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "Merchant provides alternative labeling instructions",
      "applies_to": "Integration item labeling"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Specific customer relationships require special handling",
      "applies_to": "Invoice processing"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship specifics",
      "condition": "Merchant has unique customer relationship requirements",
      "applies_to": "Invoice modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant temperament and personal details",
      "example": "Doug is described as 'the nicest guy ever', lives in Tampa, has a golden retriever named Hamilton",
      "customization_type": "Relationship management context"
    },
    {
      "element": "Key POC feature priorities",
      "example": "Automation across the board, making live changes to invoices based on amendments, automated dunning and collections",
      "customization_type": "Feature prioritization"
    },
    {
      "element": "Notification recipients and channels",
      "example": "Customer Success [Azmat Aziz] needs notification in Messari internal merchant channel when contracts are processed",
      "customization_type": "Communication workflow"
    },
    {
      "element": "Integration item labeling rules",
      "example": "Statsig and Pinata have specific labeling requirements",
      "customization_type": "Integration-specific processing"
    },
    {
      "element": "Customer-specific invoice requirements",
      "example": "Special memos and invoice changes based on merchant-customer relationships",
      "customization_type": "Customer handling procedures"
    },
    {
      "element": "Merchant phase-specific actions",
      "example": "Different responsibilities for Implementation vs Active phase",
      "customization_type": "Lifecycle stage processing"
    }
  ],
  "confidence_score": 0.85
}
```

---

