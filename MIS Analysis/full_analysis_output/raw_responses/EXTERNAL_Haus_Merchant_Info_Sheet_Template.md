# Raw LLM Analysis: [EXTERNAL] Haus Merchant Info Sheet - Template

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:33:54

---

## Chunk 1: [EXTERNAL] Haus Merchant Info Sheet - Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:33:54

### Original Content
```
Merchant Demo date: Jan 24, 2025 Scoping start date: MSA Signature Date: Feb 12, 2025 Onboarding Kick Off Date: [If Exists] Opt Out Date: None Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Linda https: www linkedin com in linda-turner-5b23ab51  CFO: Josh https: www linkedin com in josh-brown-1985806  Customer service rep who is really involved: Account Receivable POC: Jessie https: www linkedin com in jessica-turner-0aa03b61  Billing POC: Jes...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Merchant Business Context and Operations",
    "Pain Points and Solution Goals",
    "Revenue Recognition and Billing Automation"
  ],
  "rules": [
    {
      "rule": "Demo must occur before scoping start date",
      "type": "explicit",
      "category": "timeline"
    },
    {
      "rule": "MSA signature date establishes the contractual baseline for implementation",
      "type": "implicit",
      "category": "timeline"
    },
    {
      "rule": "Key stakeholders must be identified including Accountant, CFO, AR POC, and Billing POC",
      "type": "explicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Implementation requires coordination between AE (Account Executive) and Implementation team",
      "type": "explicit",
      "category": "process"
    },
    {
      "rule": "Merchant goals and pain points must be documented during onboarding",
      "type": "explicit",
      "category": "requirements_gathering"
    },
    {
      "rule": "Opt-out clause status must be tracked and documented",
      "type": "explicit",
      "category": "contract_management"
    },
    {
      "rule": "Success criteria must be defined to prevent opt-out clause exercise",
      "type": "implicit",
      "category": "success_metrics"
    }
  ],
  "exceptions": [
    {
      "exception": "Onboarding Kick Off Date may not exist in all cases (marked as [If Exists])",
      "condition": "Optional field depending on merchant engagement model"
    },
    {
      "exception": "Opt Out Date listed as 'None' but opt-out clause existence is questioned",
      "condition": "Suggests conditional opt-out rights may exist based on success criteria"
    },
    {
      "exception": "ERP and Tax Integration fields are present but empty",
      "condition": "May not be applicable or required for all merchants"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and business description",
      "customization": "Haus Analytics - marketing science platform",
      "note": "Each merchant will have unique business model"
    },
    {
      "element": "Key personnel with LinkedIn profiles",
      "customization": "Linda (Accountant), Josh (CFO), Jessie (AR/Billing POC)",
      "note": "Contact information and roles vary per merchant"
    },
    {
      "element": "Specific pain points",
      "customization": "Revenue recognition automation, invoice delays, manual data entry in bill.com, tracking escalations/ramp-ups",
      "note": "Each merchant has unique operational challenges"
    },
    {
      "element": "Current systems and tools",
      "customization": "bill.com for invoicing",
      "note": "Technology stack varies by merchant"
    },
    {
      "element": "Timeline dates",
      "customization": "Demo: Jan 24, 2025; MSA: Feb 12, 2025",
      "note": "Implementation timeline is merchant-specific"
    },
    {
      "element": "Success metrics for opt-out prevention",
      "customization": "Faster first invoice, automated customer setup, visibility into cash forecasting, automated escalations",
      "note": "Success criteria tailored to merchant goals"
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 2: [EXTERNAL] Haus Merchant Info Sheet - Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:33:54

### Original Content
```
No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant No, Jessie   onboarding manager are manually creating each Information on how merchant bills Flat SaaS, 12 month usually How contract is broken up One off things to know about the merchant Contract Processing Steps (Implementation Success to fill) Haus wants contracts processed according to the Order Effective Date If not available, please use the Term Start Date Read the r...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Recognition",
    "Billing Configuration and Payment Terms",
    "Service Term and Date Management",
    "Integration Items and Product Categorization",
    "Operational Defaults and Fallback Rules"
  ],
  "rules": [
    "Contracts must be processed according to Order Effective Date; if unavailable, use Term Start Date",
    "Service Start Date must match the Order Effective Date",
    "Months of Service defaults to term period, typically 12 months if none stated",
    "Total Price calculation: Annual price divided by total term period (typically 12 months)",
    "Quantity field must be set to 1",
    "Start Date must match Service Start Date",
    "Periods set to 12 for yearly contracts, adjusted for quarterly",
    "Net Terms must be checked from Payment Terms section in contract",
    "Default Service Term is 1 Year when not listed",
    "Default Net Payment Terms is 0 when not specified",
    "Default Billing Frequency is Monthly when not listed",
    "Tax line items: each tax line item becomes a BT (Billing Type) by default",
    "Integration Item selection: type product name and select closest match; ignore items marked with X",
    "Billing type is Flat for this merchant",
    "Contract structure is Flat SaaS, typically 12 months",
    "Revenue Item Name should be the Product Name"
  ],
  "exceptions": [
    "Some contracts may require back-dating invoice date to final day of the month (merchant-specific request)",
    "Billing frequency may change from default monthly to quarterly depending on contract",
    "Integration items with 'X' marker should be ignored during selection",
    "Processing specifics may differ by individual contract based on merchant requests",
    "Customer creation process has no unique requirements for this merchant (Jessie onboarding manager manually creates each)"
  ],
  "merchant_specific": [
    "Merchant name: Haus (implied from 'Haus wants contracts processed according to...')",
    "Billing model: Flat SaaS, 12 month contracts typically",
    "Contract processing requires reference to LOOM Video Walkthrough and Garage Example",
    "Specific date: Example contract date referenced as '2 1 2025'",
    "Customer creation: Manually handled by Jessie (onboarding manager)",
    "Post-processing notifications may be required to Customer Success team members",
    "Merchant has internal communication channel for notifications",
    "Rewatch calls available: Intro and Demo calls with Gong.io links",
    "Category for Rev Rec field needs to be populated",
    "Feature requests tracking system in place",
    "Events billing processing may be applicable (section present but not filled)",
    "Integration items processing instructions may vary (section present but not filled)"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 3: [EXTERNAL] Haus Merchant Info Sheet - Template_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:34:05

### Original Content
```
app gong io call id 6485198124604882967 Implementation, CS, Pricing https: us-56595 app gong io e c-share tkn 1794enjvb9n111949icd3e9kwz Workshop with Controller https: us-56595 app gong io call id 7410539427932474592 Decks: Demo: https: docs google com presentation d 1JU_ywcB1b7mcsgTgZkDne4yf1x8HAvVe_5TYOFHaJKw edit usp sharing Workshop https: docs
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting and call documentation",
    "Implementation and onboarding processes",
    "Customer success activities",
    "Pricing discussions",
    "Workshop facilitation"
  ],
  "rules": [
    "Calls and meetings should be recorded in Gong.io platform",
    "Implementation discussions should include CS (Customer Success) and pricing components",
    "Workshop sessions should be conducted with relevant stakeholders (e.g., Controller)",
    "Demo materials and workshop content should be stored in Google Docs/Presentations",
    "Meeting resources should be shared via accessible links"
  ],
  "exceptions": [],
  "merchant_specific": [
    "Gong.io call IDs (6485198124604882967, 7410539427932474592) - specific to this organization's tracking system",
    "Google Docs presentation ID (1JU_ywcB1b7mcsgTgZkDne4yf1x8HAvVe_5TYOFHaJKw) - specific document reference",
    "Domain reference 'us-56595' - appears to be organization-specific subdomain or identifier",
    "Workshop participant role 'Controller' - may vary by merchant's organizational structure",
    "Token reference 'tkn 1794enjvb9n111949icd3e9kwz' - merchant-specific sharing token"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for low confidence score**: The document chunk appears to be a fragmented collection of URLs and meeting references rather than a complete instruction document. The content lacks clear instructional language, complete sentences, and explicit rules. The analysis is based on inferring patterns from URL structures and meeting titles, which limits confidence in extracting generalizable rules. A more complete document with actual procedural instructions would yield higher confidence.

---

## Chunk 4: [EXTERNAL] Haus Merchant Info Sheet - Template_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:34:07

### Original Content
```
google com presentation d 1uOVQjycPZ-vkkUB-Ov3ZHQPpu85WKhhW5EncJ1HHvhs edit usp sharing Pricing CS Implementation https: docs google com presentation d 1uOVQjycPZ-vkkUB-Ov3ZHQPpu85WKhhW5EncJ1HHvhs edit usp sharing Implementation Notes: 115 current customers, but 2x in 2025 Ask for examples of amendments for second year contracts Ask for current rev rec schedule to be sure to map correctly Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Fl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Implementation and Onboarding",
    "Contract Management and Renewals",
    "Stakeholder Relationship Mapping",
    "Revenue Recognition and Billing Structure",
    "Customer Growth and Scaling"
  ],
  "rules": [
    "Implementation team must request examples of amendments for second year contracts",
    "Current revenue recognition schedule must be obtained and mapped correctly",
    "Sections marked '[Ops International Team to Ignore]' should be excluded from operational team workflows",
    "AE and Implementation teams are responsible for filling specific merchant information sections",
    "Merchant billing structure information must be documented (flat SaaS price model)",
    "Merchant temperament assessment is required for each key stakeholder",
    "Key POC and decision maker identification is mandatory",
    "Important merchant relationship information must be documented and tracked"
  ],
  "exceptions": [
    "Ops International Team should ignore specific sections marked for AE and Implementation only",
    "Special attention required for customers going through tough renewals (referenced: Coalesce renewal situation)",
    "Newly hired stakeholders (like Linda) may require different engagement approaches"
  ],
  "merchant_specific": [
    "Customer count: 115 current customers with expected 2x growth in 2025",
    "Stakeholder personalities and temperaments (Josh: dry, unpleasant but straightforward and fair; Jessie: most engaged in sales process; Linda: newly hired, nice, least dry)",
    "Internal relationship connections (Josh's relationship with Nick from Coalesce)",
    "Merchant billing model (flat SaaS pricing structure)",
    "Revenue recognition schedule mapping requirements per merchant",
    "Second year contract amendment patterns specific to each merchant"
  ],
  "confidence_score": 0.72
}
```

**Reasoning for Confidence Score (0.72):**
- The document appears to be fragmented notes rather than formal policy documentation
- Some context is missing (incomplete sentences, unclear references)
- Clear actionable items are present but formatting is inconsistent
- Stakeholder information is detailed but subjective
- The URL references suggest this is part of a larger documentation system not fully visible in this chunk

---

## Chunk 5: [EXTERNAL] Haus Merchant Info Sheet - Template_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:34:23

### Original Content
```
) Josh 3) What are the Tabs features that the key POC cares about Rev rec- previously going to Pilot com to make any edits in rev rec Automated customer and invoice creation- currently a multiweek gap between signing a customer and first invoice bc Jessie has to manually type into Bill com and set up invoicing for every new customer Auto escalation or ramp up- Jessie has a calendar reminder to execute
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Recognition (Rev Rec) Management",
    "Customer and Invoice Automation",
    "Manual Process Elimination",
    "System Integration and Migration",
    "Workflow Escalation and Reminders"
  ],
  "rules": [
    {
      "rule": "Revenue recognition edits were previously managed through Pilot.com platform",
      "category": "process_requirement",
      "specificity": "historical"
    },
    {
      "rule": "Customer and invoice creation must be automated to eliminate manual entry",
      "category": "automation_requirement",
      "specificity": "explicit"
    },
    {
      "rule": "New customer setup currently requires manual entry into Bill.com by Jessie",
      "category": "current_process",
      "specificity": "explicit"
    },
    {
      "rule": "Invoicing setup must be configured for every new customer",
      "category": "process_requirement",
      "specificity": "explicit"
    },
    {
      "rule": "There is a multi-week gap between customer signing and first invoice under current manual process",
      "category": "process_issue",
      "specificity": "explicit"
    },
    {
      "rule": "Auto escalation or ramp-up functionality is needed to replace manual calendar reminders",
      "category": "automation_requirement",
      "specificity": "implicit"
    },
    {
      "rule": "Jessie currently uses calendar reminders to execute escalation/ramp-up tasks",
      "category": "current_process",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Multi-week delay between customer signing and first invoice is a current pain point that needs resolution",
      "context": "This represents a gap in the current workflow that the new system should eliminate"
    },
    {
      "exception": "Migration from Pilot.com for revenue recognition edits",
      "context": "Indicates a system transition requirement"
    }
  ],
  "merchant_specific": [
    {
      "element": "Josh (POC - Point of Contact)",
      "type": "personnel",
      "note": "Key stakeholder for Tab features"
    },
    {
      "element": "Jessie",
      "type": "personnel",
      "note": "Person currently responsible for manual Bill.com entry and calendar-based escalations"
    },
    {
      "element": "Pilot.com",
      "type": "system",
      "note": "Previous platform used for revenue recognition management"
    },
    {
      "element": "Bill.com",
      "type": "system",
      "note": "Current system requiring manual customer and invoice data entry"
    },
    {
      "element": "Multi-week gap timeline",
      "type": "process_metric",
      "note": "Specific to this merchant's current operational inefficiency"
    },
    {
      "element": "Tabs features",
      "type": "product",
      "note": "Specific product/platform being evaluated or implemented"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be meeting notes or requirements gathering, which provides clear context about pain points and desired features
- Specific personnel names and systems are mentioned, making merchant-specific elements clear
- Some ambiguity exists around whether "Tabs" refers to a product name or UI features
- The fragmented nature of the text suggests this is an excerpt, so some context may be missing
- Clear identification of current vs. desired state processes increases confidence in rule extraction

---

