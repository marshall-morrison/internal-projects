# Raw LLM Analysis:  Autumn _ Tabs Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:29:09

---

## Chunk 1:  Autumn _ Tabs Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:29:09

### Original Content
```
2 for pricing information Make Revenue Schedule  3 for this item Service Start Date: Earliest Agreement Effective Date Total Months of Service: TOTAL LENGTH OF SERVICE Item Description: First and Last Month Total Price: Amount listed below (example: 34,000) (2 months of PR and Affiliate) Periods: 1 If there is NO Section 5 1   5 2 Frequency: 1 Month Net Terms: Net10 For contract length term: search for  Term  in contract Please view loom for instructions below If there is more than 1 contract fo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Management",
    "Contract Processing and Sequencing",
    "Service Date and Term Calculations",
    "Pricing Information Extraction from Contract Sections",
    "Multiple Contract Handling and Addendum Processing"
  ],
  "rules": [
    "Default Item Name must be 'Services'",
    "Default Integration Item is 'Last Month's Retainer'",
    "Default Net Terms is Net30 (except First and Last Month which is Net10)",
    "Pricing information for PR and Affiliate must be extracted from Section 5.1",
    "Pricing information for First and Last Month must be extracted from Section 5.2",
    "Service Start Date should use the Earliest Agreement Effective Date",
    "PR Revenue Schedule (Schedule 1) must start ONE MONTH AFTER CONTRACT START DATE",
    "Affiliate Revenue Schedule (Schedule 2) must start ONE MONTH AFTER CONTRACT START DATE",
    "First and Last Month Revenue Schedule (Schedule 3) must start ONE MONTH AFTER CONTRACT START DATE",
    "Quantity must always be set to 1",
    "Periods must equal Months of Service (except First and Last Month which is 1)",
    "Frequency is typically '1 month' unless specified otherwise",
    "When multiple contracts exist, they must be organized from earliest to latest",
    "For contracts with two dates in Agreement Effective Date, create TWO revenue schedules with naming convention based on what comes after the date",
    "Total of 3 revenue schedules must be made: PR, Affiliate, and First Last Months payment",
    "Affiliate Total Months of Service calculation: (Total Month Term - 2 months for First Last Month Payment)",
    "First and Last Month Total Months of Service is always 1",
    "First and Last Month Periods is always 1",
    "If 1 month paid upfront: second BT frequency = (total service term in months) - 1",
    "If 2 months paid upfront: second BT frequency = (total service term in months) - 2",
    "For addendum contracts, if pricing/net terms/frequency not listed, copy from previous contract",
    "For addendum contracts, SERVICE START DATE and START DATE must be updated even if other fields remain the same"
  ],
  "exceptions": [
    "When Section 5.1 or 5.2 is not present, different processing rules apply",
    "When multiple contracts exist per customer, special sequencing and processing steps are required",
    "When Agreement Effective Date contains TWO dates, create separate revenue schedules for each",
    "First and Last Month payment has Net10 terms instead of standard Net30",
    "Addendum contracts (labeled 'ADDENDUM TO PR SERVICES AGREEMENT') follow modified rules where only certain fields change",
    "Frequency calculation varies based on whether 1 month or 2 months are paid upfront",
    "First BT (billing transaction) for first and last month is always '1 every 1 month' regardless of term length"
  ],
  "merchant_specific": [
    "Reference to 'Garage' system/platform for viewing contract examples",
    "Specific contract sections referenced: Section 5.1 (PR and Affiliate pricing), Section 5.2 (First and Last Month pricing)",
    "Specific service types: PR Services, Affiliate Services",
    "Integration item terminology: 'Last Month's Retainer'",
    "Reference to 'loom' for instructional videos",
    "Specific naming conventions for revenue schedules (PR, Affiliate, First and Last Month)",
    "Red text screenshot references for specific field locations in contracts",
    "Term search methodology: 'search for Term in contract'",
    "Garage link references for processing examples",
    "Contract organization methodology specific to this merchant's workflow"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2:  Autumn _ Tabs Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:29:11

### Original Content
```
Merchant Scoping start date: Oct 18, 2023 MSA Signature Date: Nov 12, 2024 Onboarding Kick Off Date: Nov 13, 2024 [If Exists] Opt Out Date: none Go Live Date: Dec 15, 2023 GTM POC: Implementation POC: ERP: Tax Integration: Moving to Avalara Key people at Merchant Accountant: Seth Johnsonis the Fraction accountant who was newly hired Mouricio is the fractional accountant Etc Company summary (AE to fill) Autumn is a full-service, nationally integrated PR   Creative Marketing agency that amplifies ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Schedule Creation",
    "Merchant Onboarding Timeline and Key Dates",
    "Billing Model and Payment Structure",
    "Stakeholder Roles and Responsibilities",
    "Service Type Classification (PR vs Affiliate)"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "Service Start Date must refer to Agreement Effective Date",
      "category": "contract_processing"
    },
    {
      "rule_id": "R2",
      "description": "Default Item Name must be 'Services'",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R3",
      "description": "Default Integration Item must be either 'PR Services' or 'Affiliate' depending on service type",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R4",
      "description": "Net terms are set to 30 days for all revenue schedules",
      "category": "payment_terms"
    },
    {
      "rule_id": "R5",
      "description": "Frequency is set to 1 month for all revenue schedules",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R6",
      "description": "Quantity is always set to 1 for revenue schedules",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R7",
      "description": "Periods must equal Months of Service",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R8",
      "description": "For single contract with no amendment: create exactly 3 revenue schedules (PR, Affiliate, First and Last Month)",
      "category": "contract_processing"
    },
    {
      "rule_id": "R9",
      "description": "Pricing information must be referenced from section 5.1 of contract",
      "category": "pricing"
    },
    {
      "rule_id": "R10",
      "description": "Item description in revenue schedule should match the name that comes after the date",
      "category": "revenue_schedule"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "If there are TWO dates in Agreement Effective Date, create TWO separate revenue schedules for each with specific naming conventions",
      "condition": "Multiple effective dates present"
    },
    {
      "exception_id": "E2",
      "description": "For Affiliate Revenue Schedule (Schedule 2): Total Months of Service = Total Month Term minus 2 months (to account for First and Last Month Payment)",
      "condition": "Processing Affiliate service type",
      "example": "4 months service period when total term is 6 months"
    },
    {
      "exception_id": "E3",
      "description": "Processing steps differ when there are amendments to contracts (not detailed in this chunk)",
      "condition": "Contract has amendments"
    },
    {
      "exception_id": "E4",
      "description": "Some contracts are one-off rather than monthly recurring agreements",
      "condition": "Non-SaaS billing model"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "Autumn",
      "description": "Full-service PR and Creative Marketing agency"
    },
    {
      "element": "Key Personnel",
      "value": "Seth Johnson (fractional accountant), Mouricio (fractional accountant)",
      "description": "Accountant contacts responsible for billing accuracy, renewals, and autopay transfers"
    },
    {
      "element": "Onboarding Dates",
      "value": "Scoping: Oct 18, 2023; MSA Signature: Nov 12, 2024; Kick Off: Nov 13, 2024; Go Live: Dec 15, 2023",
      "description": "Merchant-specific timeline (note: date inconsistencies suggest possible data entry errors)"
    },
    {
      "element": "ERP/Tax Integration",
      "value": "Moving to Avalara",
      "description": "Tax system integration in progress"
    },
    {
      "element": "Opt Out Clause",
      "value": "No opt out clause exists",
      "description": "Merchant has no exit provisions"
    },
    {
      "element": "Billing Model",
      "value": "Majority are monthly SaaS-like agreements, remainder are one-off contracts",
      "description": "Predominant recurring revenue model"
    },
    {
      "element": "Service Types",
      "value": "PR Services and Affiliate Services",
      "description": "Two primary service categories requiring separate revenue schedules"
    },
    {
      "element": "Merchant Goals",
      "value": "Ensure correct billing amounts, track renewals, transfer recurring billing to autopay",
      "description": "Pain points being addressed"
    },
    {
      "element": "Reference Materials",
      "value": "Society 6 example, garage link, loom video tutorial",
      "description": "Training and reference documentation specific to this implementation"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3:  Autumn _ Tabs Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:29:26

### Original Content
```
g always back-date invoice date to the final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms Default: Net 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and billing configuration defaults",
    "Integration item processing and labeling",
    "Post-processing communication workflows",
    "Customer-specific billing requirements",
    "Merchant relationship management and stakeholder information"
  ],
  "rules": [
    {
      "rule": "Default invoice date should be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Contract Terms",
      "explicit": true
    },
    {
      "rule": "Default net payment terms are Net 30",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling events processing information",
      "category": "Workflow Responsibility",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling integration items processing instructions",
      "category": "Workflow Responsibility",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore certain sections marked for AE and Implementation",
      "category": "Team Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "condition": "Merchant provides specific instructions",
      "applies_to": "Integration item labeling"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements exist",
      "applies_to": "Invoice processing"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship specifics",
      "condition": "Relationship-driven modifications",
      "applies_to": "Invoice modifications"
    },
    {
      "exception": "Notification timing varies by merchant phase (Implementation vs Active)",
      "condition": "Merchant lifecycle stage",
      "applies_to": "Post-processing communications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing information",
      "customizable": true,
      "notes": "Requires Implementation Success to fill per merchant"
    },
    {
      "element": "Integration item labeling rules",
      "customizable": true,
      "notes": "Different rules for different integration types (Statsig, Pinata, etc.)"
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "notes": "Who, where, and when notifications occur varies by merchant"
    },
    {
      "element": "Customer-specific invoice requirements",
      "customizable": true,
      "notes": "Special memos and invoice changes based on merchant-customer relationships"
    },
    {
      "element": "Merchant relationship information",
      "customizable": true,
      "notes": "Includes temperament, key POC, decision makers, and feature priorities"
    },
    {
      "element": "Billing model description",
      "customizable": true,
      "notes": "Example shows monthly SaaS-like agreements vs one-off contracts"
    },
    {
      "element": "Feature requests tracking",
      "customizable": true,
      "notes": "Merchant-specific feature requests with urgency levels"
    },
    {
      "element": "Rewatch calls documentation",
      "customizable": true,
      "notes": "Merchant-specific call recordings and notes"
    }
  ],
  "confidence_score": 0.92
}
```

---

