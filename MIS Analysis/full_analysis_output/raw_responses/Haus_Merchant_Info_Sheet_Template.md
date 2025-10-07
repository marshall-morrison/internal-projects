# Raw LLM Analysis: Haus Merchant Info Sheet - Template

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:52:07

---

## Chunk 1: Haus Merchant Info Sheet - Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:07

### Original Content
```
No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant No, Jessie   onboarding manager are manually creating each Information on how merchant bills Flat SaaS, 12 month usually How contract is broken up One off things to know about the merchant Contract Processing Steps (Implementation Success to fill) Haus wants contracts processed according to the Order Effective Date If not available, please use the Term Start Date Read the r...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Recognition",
    "Billing Configuration and Terms",
    "Date Management and Period Handling",
    "Integration Item Assignment and Categorization",
    "Post-Processing Communication Workflows"
  ],
  "rules": [
    "Contracts must be processed according to Order Effective Date; if unavailable, use Term Start Date",
    "Service Start Date must match the Order Effective Date",
    "Default term period is 12 months if none specified",
    "Total Price calculation: Annual price divided by total term period (typically 12 months)",
    "Quantity is always set to 1",
    "Start Date matches Service Start Date, unless it falls within a closed period - then use first day of open period",
    "Default periods is 12 for yearly contracts; adjust for quarterly",
    "Net Terms must be checked in the Payment Terms section of contract",
    "Default Service Term is 1 Year if none listed",
    "Default Net Payment Terms is 0 if none listed",
    "Default Billing Frequency is Monthly if none listed",
    "Every tax line item becomes a BT (Billable Transaction) by default",
    "Billing model is Flat SaaS, typically 12 months",
    "Customer creation is manual, handled by onboarding manager (Jessie)",
    "Integration items should be matched to closest product name; ignore items marked with X"
  ],
  "exceptions": [
    "If start date falls within a closed accounting period, override to use first day of open period instead",
    "Quarterly contracts require period adjustment from default 12",
    "Integration items with 'X' marker should be ignored during processing",
    "Merchant may request contract-specific processing variations (e.g., back-dating invoice dates)",
    "Special memos may be required for certain customer invoices based on merchant-customer relationships"
  ],
  "merchant_specific": [
    "Merchant name: Haus (implied from 'Haus wants contracts processed...')",
    "Specific product categories: Geolift (maps to Geolift), cMMM (maps to cMMM subscription), Casual MMM (maps to cMMM subscription)",
    "Onboarding manager: Jessie (handles manual customer creation)",
    "Customer Success contact: Azmat Aziz (for Active phase notifications)",
    "Notification channel: Merchant-specific internal channel for contract processing completion",
    "Integration item examples: Statsig (labeled as 'Sales'), Pinata (labeled as 'Software Subscription Bundle')",
    "Referenced example contracts and video walkthroughs (Garage Example, LOOM Video)",
    "Gong call recordings available for reference (Intro and Demo calls)"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Haus Merchant Info Sheet - Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:10

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
      "context": "Demo date (Jan 24) precedes Scoping start date (MSA Signature Date: Feb 12)"
    },
    {
      "rule": "Key stakeholder roles must be identified: Accountant, CFO, Customer Service Rep, Account Receivable POC, and Billing POC",
      "type": "explicit",
      "context": "Required personnel documentation with LinkedIn profiles"
    },
    {
      "rule": "Implementation requires identification of ERP and Tax Integration systems",
      "type": "explicit",
      "context": "ERP and Tax Integration fields present in template"
    },
    {
      "rule": "Merchant goals and pain points must be documented before implementation",
      "type": "explicit",
      "context": "Goals section requires AE and Implementation team input"
    },
    {
      "rule": "Opt-out clause status must be tracked and documented",
      "type": "explicit",
      "context": "Opt Out Date field and conditional requirements for preventing opt-out exercise"
    },
    {
      "rule": "Company summary must include business description and value proposition",
      "type": "implicit",
      "context": "Summary section describes what company does"
    },
    {
      "rule": "North star goals must identify specific pain points being solved",
      "type": "explicit",
      "context": "Goals section explicitly asks 'What pain are we solving' and 'Why are they buying'"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date can be 'None'",
      "condition": "Not all merchants have opt-out clauses in their agreements"
    },
    {
      "exception": "Onboarding Kick Off Date may not exist",
      "condition": "Field shows '[If Exists]' indicating optional nature"
    },
    {
      "exception": "Manual processes vary by merchant",
      "condition": "Haus Analytics uses bill.com for manual invoice creation, but other merchants may use different systems"
    }
  ],
  "merchant_specific": [
    {
      "element": "ERP System",
      "customization_needed": "Must identify merchant's specific ERP platform"
    },
    {
      "element": "Tax Integration System",
      "customization_needed": "Must identify merchant's tax software/integration"
    },
    {
      "element": "Billing Platform",
      "customization_needed": "Haus Analytics uses bill.com; other merchants may use different platforms"
    },
    {
      "element": "Stakeholder Names and Contacts",
      "customization_needed": "Unique personnel for each merchant with LinkedIn profiles"
    },
    {
      "element": "Pain Points",
      "customization_needed": "Specific to merchant's operational challenges (e.g., revenue recognition timing, invoice delays, manual data entry, escalation tracking)"
    },
    {
      "element": "Business Description",
      "customization_needed": "Unique company summary describing merchant's industry and value proposition"
    },
    {
      "element": "Implementation Timeline",
      "customization_needed": "Dates vary per merchant (Demo, MSA Signature, Go Live, etc.)"
    },
    {
      "element": "Opt-out Conditions",
      "customization_needed": "Merchant-specific criteria for preventing opt-out clause exercise"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Haus Merchant Info Sheet - Template_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:18

### Original Content
```
app gong io call id 6485198124604882967 Implementation, CS, Pricing https: us-56595 app gong io e c-share tkn 1794enjvb9n111949icd3e9kwz Workshop with Controller https: us-56595 app gong io call id 7410539427932474592 Decks: Demo: https: docs google com presentation d 1JU_ywcB1b7mcsgTgZkDne4yf1x8HAvVe_5TYOFHaJKw edit usp sharing Workshop https: docs
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting and call documentation",
    "Resource sharing and collaboration",
    "Implementation and onboarding processes",
    "Customer success activities",
    "Pricing discussions and workshops"
  ],
  "rules": [
    "Calls and meetings should be recorded in Gong.io platform",
    "Implementation meetings require documentation with call IDs",
    "Customer success interactions should be tracked",
    "Pricing discussions should be documented separately",
    "Workshop materials should be stored in Google Docs/Slides",
    "Demo presentations should be accessible via shared links",
    "Resources should use standardized sharing permissions (edit/view access)"
  ],
  "exceptions": [
    "No explicit exceptions identified in this document chunk",
    "Conditional access may apply based on sharing token parameters"
  ],
  "merchant_specific": [
    "Gong.io call IDs (specific to this organization's instance)",
    "Google Workspace domain (us-56595 appears to be organization-specific)",
    "Specific presentation templates and deck structures",
    "Workshop format and controller involvement may vary by merchant",
    "CS (Customer Success) terminology and processes",
    "Implementation workflow stages"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for low confidence score:**
- The document chunk appears to be a fragment of URLs and meeting references rather than complete instructional content
- Limited context makes it difficult to extract comprehensive, generalizable rules
- Many elements appear to be specific identifiers rather than instructional guidelines
- The content seems to be metadata or reference links rather than actual procedural instructions
- Would benefit from additional context or complete sentences to improve analysis accuracy

---

## Chunk 4: Haus Merchant Info Sheet - Template_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:22

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
    "Operations International Team should ignore sections marked for AE and Implementation teams",
    "Implementation team must request examples of amendments for second year contracts",
    "Implementation team must obtain current revenue recognition schedule to ensure correct mapping",
    "Merchant billing structure information must be documented (specifically flat SaaS pricing model)",
    "Merchant temperament and key stakeholder personalities must be assessed and documented",
    "Key Point of Contact (POC) and decision maker must be identified for each merchant account"
  ],
  "exceptions": [
    "Specific note about Josh's relationship with Nick from Coalesce during a difficult renewal period - indicates special handling may be needed for relationship-sensitive situations",
    "Merchant (Haus) is experiencing 2x growth projection in 2025, which may require different implementation approach than standard customers"
  ],
  "merchant_specific": [
    "Current customer count: 115 customers with 2x growth expected in 2025",
    "Merchant uses flat SaaS pricing model",
    "Key stakeholders identified: Josh (dry, unpleasant but straightforward and fair), Jessie (most engaged in sales process), Linda (newly hired, described as nice and least dry)",
    "Merchant name appears to be 'Haus'",
    "External relationship reference: Nick from Coalesce (previous difficult renewal case)",
    "Merchant temperament characterized as 'positive but hard to read' and 'straightforward'",
    "Revenue recognition schedule mapping required (merchant-specific financial structure)"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: Haus Merchant Info Sheet - Template_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:52:34

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
    "Manual Process Pain Points and Inefficiencies",
    "Contract Escalation and Ramp-up Management",
    "Integration with Financial Systems (Pilot.com, Bill.com)"
  ],
  "rules": [
    {
      "rule": "Revenue recognition edits are currently performed in Pilot.com",
      "type": "current_process",
      "area": "revenue_recognition"
    },
    {
      "rule": "Customer and invoice creation must occur after customer signing",
      "type": "workflow_sequence",
      "area": "customer_onboarding"
    },
    {
      "rule": "Jessie manually enters customer data into Bill.com for each new customer",
      "type": "current_process",
      "area": "data_entry"
    },
    {
      "rule": "Invoicing setup is required for every new customer",
      "type": "requirement",
      "area": "billing_setup"
    },
    {
      "rule": "Contract escalations/ramp-ups are tracked via calendar reminders",
      "type": "current_process",
      "area": "contract_management"
    },
    {
      "rule": "There is a multi-week gap between customer signing and first invoice",
      "type": "process_constraint",
      "area": "billing_timeline"
    }
  ],
  "exceptions": [
    {
      "exception": "Multi-week delay exists between signing and invoicing due to manual processes",
      "impact": "Delays revenue collection and creates operational bottleneck",
      "context": "Current state problem requiring automation solution"
    }
  ],
  "merchant_specific": [
    {
      "element": "Jessie",
      "type": "personnel",
      "description": "Specific person responsible for manual data entry and invoice setup"
    },
    {
      "element": "Josh",
      "type": "personnel",
      "description": "Key POC (Point of Contact) mentioned in context"
    },
    {
      "element": "Pilot.com",
      "type": "system",
      "description": "Current platform used for revenue recognition edits"
    },
    {
      "element": "Bill.com",
      "type": "system",
      "description": "Current platform used for customer data entry and invoicing"
    },
    {
      "element": "Tabs features",
      "type": "product_reference",
      "description": "New system being evaluated to address current pain points"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be meeting notes or requirements gathering, making context somewhat informal
- Clear pain points and desired features are identifiable
- Some ambiguity exists around whether these are requirements for implementation or discovery notes
- Personnel names and systems are clearly stated, but the exact workflow details could benefit from more structure
- The fragment nature (starting with ") Josh 3)") suggests this is part of a larger document

---

