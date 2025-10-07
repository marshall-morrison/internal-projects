# Raw LLM Analysis: Instil MIS(1)

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 10:55:41

---

## Chunk 1: Instil MIS(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:41

### Original Content
```
, 36 months) Item Name: Find the name of the service being provided, such as "Cloud-based constituent relationship management solution " Call line item for software charges "Software Fees" and map to item "Software Fees" (do not use name in Services) Default to  Service Fees  if none available Item Description: Leave blank Integration Item: Leave blank, for Software Fees product - map to Software Fees integration item (ID 3) Billing Type: Usually Flat Total Price: Identify the total service fee ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract line item mapping and categorization",
    "Billing and payment term extraction",
    "Service fee and implementation fee handling",
    "Contract renewal processing",
    "QuickBooks Online (QBO) integration mapping"
  ],
  "rules": [
    "Software charges should be labeled as 'Software Fees' and mapped to the Software Fees item",
    "Do not use the name found in Services section for software charges",
    "Default to 'Service Fees' if no specific item name is available",
    "Item Description field should be left blank",
    "Integration Item field should be left blank",
    "Software Fees product must map to Software Fees integration item (ID 3)",
    "Billing Type is usually 'Flat'",
    "Implementation fees with $0 value should not be included",
    "Discounts should be put in line, not as a separate line item",
    "Service start date should be used as the Start Date",
    "Payment terms should be checked under Section 4 'Payment of Fees'",
    "Software fees map to software fees in QBO (item number 3)",
    "Implementation fees map to implementation in QBO",
    "If contract requires payment in advance, use net 0 terms",
    "Auto-renewal in section 5.1 should be processed as flat renewal for one year beyond initial contract term"
  ],
  "exceptions": [
    "If no specific item name is available, default to 'Service Fees'",
    "Zero-dollar implementation fees should be excluded from line items",
    "Discounts require special handling (inline rather than separate line item)",
    "Payment terms of 'pay in advance' translate to 'net 0' terms"
  ],
  "merchant_specific": [
    "QuickBooks Online (QBO) item mapping structure (item numbers 3 for software fees)",
    "Specific contract section references (Section 4 for Payment of Fees, Section 5.1 for renewal terms)",
    "Integration item ID system (ID 3 for Software Fees)",
    "Term length specification (36 months mentioned as example)",
    "Specific field names and structure (Item Name, Item Description, Integration Item, etc.)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Instil MIS(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:48

### Original Content
```
Merchant Demo date: Feb 12, 2025 Scoping start date: MSA Signature Date: Feb 26, 2025 Onboarding Kick Off Date: Mar 3, 2025 [If Exists] Opt-Out Date: NONE Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Nicole https: www linkedin com in nicolebjordan5 Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary (AE to fill) Summary of what company does: Instil is a cloud-based donor management platfor...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Integration Requirements and Technical Setup",
    "Merchant Goals and Pain Points",
    "Contract Terms and Billing Models"
  ],
  "rules": [
    {
      "rule": "Onboarding follows a structured timeline: Demo → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "Key stakeholders must be identified including: Accountant, CFO, Customer Service Rep, AR POC, Billing POC, GTM POC, Implementation POC",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Account Executive (AE) is responsible for filling company summary and billing model information",
      "type": "responsibility",
      "explicit": true
    },
    {
      "rule": "Implementation team is responsible for filling goals and contract processing steps",
      "type": "responsibility",
      "explicit": true
    },
    {
      "rule": "Merchant goals must address: What is the goal, What pain is being solved, Why are they buying",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Opt-out clause status must be documented, including conditions if applicable",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "ERP and Tax Integration systems must be documented",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Contract processing requires identifying Service Start Date and Months of Service from Initial Service Term",
      "type": "process",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Custom scoping required for Hubspot integration data extraction",
      "condition": "When merchant has specific or complex Hubspot setup",
      "merchant": "Instil"
    },
    {
      "exception": "Hubspot integration is critical for sales team to view invoice data",
      "condition": "Merchant-specific requirement for sales visibility",
      "merchant": "Instil"
    },
    {
      "exception": "Merchant had concerns around Hubspot setup requiring special attention",
      "condition": "Pre-existing technical concerns",
      "merchant": "Instil"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "condition": "Contract-specific term",
      "merchant": "Instil"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Type",
      "value": "Cloud-based donor management platform for nonprofit organizations",
      "customizable": true
    },
    {
      "element": "CFO Contact",
      "value": "Nicole (LinkedIn profile provided)",
      "customizable": true
    },
    {
      "element": "Integration Platform",
      "value": "Hubspot",
      "customizable": true,
      "note": "Critical for sales team invoice visibility"
    },
    {
      "element": "Customer Creation Process",
      "value": "Unique aspects related to Hubspot integration",
      "customizable": true
    },
    {
      "element": "Billing Model",
      "value": "Information on how merchant bills and contract breakdown",
      "customizable": true
    },
    {
      "element": "Timeline Dates",
      "value": "Demo: Feb 12, 2025; MSA: Feb 26, 2025; Kick Off: Mar 3, 2025",
      "customizable": true
    },
    {
      "element": "Special Concerns",
      "value": "Hubspot setup concerns requiring custom scoping",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

**Confidence Reasoning**: The document is clearly structured with labeled sections and explicit instructions, making theme and rule extraction straightforward. However, the document appears incomplete (truncated at "e g"), some sections have placeholder values (NONE, empty fields), and certain contextual details about the actual implementation process are missing. The confidence score reflects high certainty about the structure and explicit rules, but moderate uncertainty about implicit requirements and complete process flows.

---

## Chunk 3: Instil MIS(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:56

### Original Content
```
Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any import...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Invoice and billing processing standards",
    "Integration item classification and labeling",
    "Post-processing communication workflows",
    "Customer-specific handling and special cases"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Contract Defaults"
    },
    {
      "rule": "Default net payment terms is 30 days if none specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Billing Frequency"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Classification"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Item Classification"
    },
    {
      "rule": "Ops team must notify designated personnel upon completion of processing batches",
      "category": "Communication Protocol"
    },
    {
      "rule": "Invoice dates may be back-dated to final day of the month per merchant contract specifications",
      "category": "Invoice Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific contract terms may override default service term of 1 year",
      "condition": "When specified in contract"
    },
    {
      "exception": "Pinata integration items can have different labels if noted by merchant",
      "condition": "Unless otherwise noted by Merchant"
    },
    {
      "exception": "Invoice date back-dating applies only when merchant has specifically requested it",
      "condition": "Contract-specific processing requirement"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to specific merchant-customer relationships",
      "condition": "Relationship-dependent modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating rules",
      "customization_type": "Contract-specific processing instruction",
      "example": "Always back-date invoice date to final day of the month"
    },
    {
      "element": "Integration item labeling",
      "customization_type": "Merchant-specific classification rules",
      "example": "Statsig = Sales, Pinata = Software Subscription Bundle"
    },
    {
      "element": "Post-processing notification recipients",
      "customization_type": "Communication workflow customization",
      "example": "Customer Success [Azmat Aziz] via Messari internal merchant channel"
    },
    {
      "element": "Events billing processing",
      "customization_type": "Merchant-specific billing requirements",
      "note": "To be filled by Implementation Success team"
    },
    {
      "element": "Customer-specific information",
      "customization_type": "Individual customer handling requirements",
      "note": "Special memos and invoice modifications per customer relationship"
    },
    {
      "element": "Notification timing",
      "customization_type": "Phase-specific communication triggers",
      "example": "When contracts are processed in Active phase"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Instil MIS(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:56:00

### Original Content
```
app gong io call id 3892700273853143293 account-id 4632005772074296398 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Flat SaaS Changing payment terms (could happen mid-contract) Is there any important merchant relationship information Nicole is the consultant CFO 1) What is the merchant temperament So nice, she loves Tabs and totally aligns with our vision 2) Is there a key POC: (i e : who is the buyer decision maker ) Nicole does it al...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Billing Structure and Payment Terms",
    "Merchant Relationship Management and Key Stakeholders",
    "Tabs Platform Feature Requirements and Priorities",
    "Implementation and Operational Workflow",
    "Revenue Recognition and Financial Reporting"
  ],
  "rules": [
    "International team operations should be ignored for this merchant account",
    "AE (Account Executive) and Implementation team are responsible for filling merchant information sections",
    "Merchant temperament assessment is required during onboarding/setup",
    "Key Point of Contact (POC) identification is mandatory, specifically identifying the buyer/decision maker",
    "Document must capture how merchant bills their customers (billing model)",
    "Payment terms changes must be tracked, including mid-contract modifications",
    "Important merchant relationship information must be documented",
    "Tabs feature preferences of key POC must be recorded"
  ],
  "exceptions": [
    "Payment terms can change mid-contract (non-standard scenario requiring special handling)",
    "Operations International Team should ignore this merchant (geographic or operational exception)",
    "Single POC (Nicole) handles all responsibilities rather than distributed team (consolidated decision-making structure)"
  ],
  "merchant_specific": [
    "Billing model: Flat SaaS structure",
    "Key stakeholder: Nicole (consultant CFO role)",
    "Merchant temperament: Highly positive, aligned with company vision",
    "Decision-making structure: Single point of contact for all functions",
    "Priority features: Auto invoice creation and sending, Dunning and collections workflow, Revenue recognition and reporting, Renewal data and dashboard, Tabs-Hubspot integration",
    "Integration requirements: Hubspot CRM integration for data synchronization",
    "Merchant name/identifier: Associated with Gong.io call ID and specific account ID"
  ],
  "confidence_score": 0.85
}
```

---

