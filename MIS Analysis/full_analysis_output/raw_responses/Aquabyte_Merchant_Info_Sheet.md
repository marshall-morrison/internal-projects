# Raw LLM Analysis: Aquabyte Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:10:51

---

## Chunk 1: Aquabyte Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:10:51

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year (12 months) Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Check for implementation fees (usually exp...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Operational Parameters",
    "Invoice Processing and Billing Procedures",
    "Integration and Implementation Management",
    "Communication and Notification Protocols",
    "Merchant Relationship Management"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default service term is 1 year (12 months) when none is listed",
      "category": "Default Parameters",
      "explicit": true
    },
    {
      "rule": "Default net payment terms are 30 days when none specified",
      "category": "Default Parameters",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly when none listed",
      "category": "Default Parameters",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default if none listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Implementation fees should be billed when implementation is complete with 30 day net payment term",
      "category": "Implementation Billing",
      "explicit": true
    },
    {
      "rule": "Implementation fees are usually explicitly stated on US contracts",
      "category": "Implementation Billing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated personnel upon completion of processing batches",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "International Ops Team should ignore certain sections marked for AE/Implementation",
      "category": "Team Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "When merchant provides alternative labeling instructions"
    },
    {
      "exception": "Default parameters only apply when no specific terms are listed in contract",
      "condition": "Absence of explicit contract terms"
    },
    {
      "exception": "Some customers pay via different methods (Stripe, Bill.com, or direct bank transfer)",
      "condition": "Customer-specific payment preferences"
    },
    {
      "exception": "Certain invoices require special memos based on merchant-customer relationship",
      "condition": "Special customer relationships or requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "condition": "Specific merchant-customer arrangements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling",
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"],
      "customizable": true
    },
    {
      "element": "Post-processing notification recipients",
      "examples": ["Customer Success - Azmat Aziz via Messari internal merchant channel"],
      "customizable": true
    },
    {
      "element": "Notification timing",
      "examples": ["When contracts are processed in Active phase"],
      "customizable": true
    },
    {
      "element": "Customer payment methods",
      "examples": ["Stripe, Bill.com, direct bank transfer"],
      "customizable": true
    },
    {
      "element": "Invoice complexity and length",
      "examples": ["Itemized invoices up to 10+ pages"],
      "customizable": true
    },
    {
      "element": "Merchant temperament and relationship style",
      "examples": ["Collaborative, eager to move quickly"],
      "customizable": true
    },
    {
      "element": "Key POC and decision makers",
      "examples": ["SFP as partner, Light Labs as client"],
      "customizable": true
    },
    {
      "element": "Internal billing systems",
      "examples": ["Internal system tracks services, triggers API to Stripe"],
      "customizable": true
    },
    {
      "element": "Special customer memos",
      "customizable": true
    },
    {
      "element": "Feature requests and urgency levels",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Aquabyte Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:10:54

### Original Content
```
Merchant: Aquabyte Demo date: Mar 25, 2025 Scoping start date: n a MSA Signature Date: Mar 26, 2025 Onboarding Kick Off Date: Mar 28, 2025 [If Exists] Opt Out Date: none Go Live Date: Nov 14, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC: Harley Pasternak ( Billing POC Etc Company summary (AE to fill) Summary of what company does: Goals (North star) (AE  Implementation to fill) W...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Contract Processing and Billing Configuration",
    "Service and Billing Start Date Determination",
    "Integration Item Selection Based on Billing Frequency"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Service Start Date",
      "description": "Use the date the product package is delivered as the service start date",
      "fallback": "If no specific date is mentioned, use the last signature date"
    },
    {
      "rule_id": "R2",
      "category": "Months of Service",
      "description": "Match the duration listed in the 'Term (Months)' field in the contract"
    },
    {
      "rule_id": "R3",
      "category": "Item Name",
      "description": "Use the name shown in the 'Product' field"
    },
    {
      "rule_id": "R4",
      "category": "Item Description",
      "description": "Use the name shown in the 'Description' field"
    },
    {
      "rule_id": "R5",
      "category": "Integration Item - Monthly",
      "description": "For monthly billing, use 'Monthly Subscription'"
    },
    {
      "rule_id": "R6",
      "category": "Integration Item - Quarterly",
      "description": "For quarterly billing, use 'Quarterly Subscription'"
    },
    {
      "rule_id": "R7",
      "category": "Integration Item - Annual",
      "description": "For annual billing, use 'Annual Subscription'"
    },
    {
      "rule_id": "R8",
      "category": "Integration Item - Default",
      "description": "If no frequency is explicitly mentioned, assume Monthly Subscription"
    },
    {
      "rule_id": "R9",
      "category": "Billing Type",
      "description": "Use 'Flat' as the billing type"
    },
    {
      "rule_id": "R10",
      "category": "Quantity",
      "description": "Use the figure shown in the 'Quantity (Product Package)' column"
    },
    {
      "rule_id": "R11",
      "category": "Billing Start Date",
      "description": "Use the date the product package is delivered if explicitly mentioned",
      "fallback": "Otherwise use the service start date"
    },
    {
      "rule_id": "R12",
      "category": "Periods and Frequency",
      "description": "Use the number in 'Term (Months)' for period if it is a monthly subscription",
      "conditional": "If stated otherwise (e.g., quarterly, annual), use that term"
    },
    {
      "rule_id": "R13",
      "category": "Billing Timing",
      "description": "Bill First of Period"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Service start date fallback: If no specific delivery date is mentioned, use the last signature date instead"
    },
    {
      "exception_id": "E2",
      "description": "Billing start date fallback: If product package delivery date is not explicitly mentioned, use the service start date"
    },
    {
      "exception_id": "E3",
      "description": "Default billing frequency assumption: When no frequency is explicitly mentioned, default to Monthly Subscription"
    },
    {
      "exception_id": "E4",
      "description": "Period calculation varies by subscription type: Monthly uses Term (Months) directly, but quarterly/annual may use different calculations"
    },
    {
      "exception_id": "E5",
      "description": "Merchant-specific processing variations: Document notes that specifics may differ by contract and merchant requests"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key Personnel Tracking",
      "fields": [
        "Accountant",
        "CFO",
        "Customer service rep who is really involved",
        "Account Receivable POC",
        "Billing POC"
      ],
      "customization_needed": true
    },
    {
      "element": "Timeline Dates",
      "fields": [
        "Demo date",
        "Scoping start date",
        "MSA Signature Date",
        "Onboarding Kick Off Date",
        "Opt Out Date",
        "Go Live Date"
      ],
      "customization_needed": true
    },
    {
      "element": "Point of Contact Assignments",
      "fields": [
        "GTM POC",
        "Implementation POC"
      ],
      "customization_needed": true
    },
    {
      "element": "System Integrations",
      "fields": [
        "ERP",
        "Tax Integration"
      ],
      "customization_needed": true
    },
    {
      "element": "Company Information",
      "fields": [
        "Company summary",
        "Goals (North star)",
        "Pain points being solved",
        "Purchase rationale"
      ],
      "customization_needed": true
    },
    {
      "element": "Opt Out Clause",
      "description": "Merchant-specific opt-out terms and conditions to prevent exercise",
      "customization_needed": true
    },
    {
      "element": "Billing Model",
      "description": "Unique customer creation process, billing methodology, contract structure",
      "customization_needed": true
    },
    {
      "element": "Contract-Specific Processing",
      "description": "Merchant-requested variations that may differ by individual contract",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

