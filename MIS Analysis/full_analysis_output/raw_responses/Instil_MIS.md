# Raw LLM Analysis: Instil MIS

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:32:21

---

## Chunk 1: Instil MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:32:21

### Original Content
```
, 36 months) Item Name: Find the name of the service being provided, such as "Cloud-based constituent relationship management solution " Call line item for software charges "Software Fees" and map to item "Software Fees" (do not use name in Services) Default to  Service Fees  if none available Item Description: Leave blank Integration Item: Leave blank Billing Type: Usually Flat Total Price: Identify the total service fee Do not include  0 implementation fees Put discount in line, not own line i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract line item data extraction and mapping",
    "Service fee identification and categorization",
    "Billing and payment term configuration",
    "Contract renewal processing rules",
    "Software and service fee nomenclature standardization"
  ],
  "rules": [
    "Contract term should be extracted and formatted in months (e.g., 36 months)",
    "Software charges must be labeled as 'Software Fees' and mapped to 'Software Fees' item",
    "Do not use the service name from the Services section for software fee items",
    "Default to 'Service Fees' as item name if no specific name is available",
    "Item Description field should be left blank",
    "Integration Item field should be left blank",
    "Billing Type is usually set to 'Flat'",
    "Total Price should identify the total service fee only",
    "Implementation fees with $0 value should not be included",
    "Discounts must be included in the line item, not as a separate line item",
    "Quantity should reflect number of licenses, users, or other applicable units",
    "Start Date should be set to the service start date",
    "Periods should be confirmed through the contract term",
    "Frequency should match the invoicing schedule (annually, upon contract anniversary, or milestone-based)",
    "Payment Terms should be found in Section 4 'Payment of Fees'",
    "If contract specifies 'pay in advance', use Net 0 terms",
    "Auto-renewal contracts (per Section 5.1) should be processed as flat renewal for one year beyond initial term"
  ],
  "exceptions": [
    "If no specific item name is available, default to 'Service Fees'",
    "Zero-dollar implementation fees are excluded from line items",
    "Discounts are handled inline rather than as separate line items",
    "Payment terms of 'pay in advance' translate to Net 0 (not standard net terms)"
  ],
  "merchant_specific": [
    "Reference to specific contract sections (Section 4 for Payment of Fees, Section 5.1 for auto-renewal)",
    "Item naming conventions may vary by merchant ('Software Fees' vs 'Service Fees')",
    "Service description format ('Cloud-based constituent relationship management solution' as example)",
    "Contract structure and section numbering system",
    "Renewal terms and auto-renewal policies in Section 5.1",
    "Screenshot references suggest merchant-specific documentation format"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Instil MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:32:24

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
      "rule": "Contract processing requires identifying Service Start Date and Months of Service from Initial Service Term",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "ERP and Tax Integration details must be documented",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Opt-out clause status must be documented and tracked",
      "type": "requirement",
      "explicit": true
    },
    {
      "rule": "Merchant goals must address: what they want to achieve, what pain is being solved, and why they are buying",
      "type": "requirement",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Custom scoping required for Hubspot integration based on specific data requirements",
      "condition": "When merchant has unique Hubspot setup or data needs",
      "merchant": "Instil"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "condition": "Merchant-specific contract term",
      "merchant": "Instil"
    },
    {
      "exception": "Hubspot integration is critical for sales team to view invoice data",
      "condition": "Business-critical requirement for specific merchant",
      "merchant": "Instil"
    },
    {
      "exception": "Merchant had concerns around Hubspot setup requiring special attention",
      "condition": "Pre-existing technical concerns",
      "merchant": "Instil"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company type and industry",
      "description": "Instil is a cloud-based donor management platform for nonprofit organizations",
      "customizable": true
    },
    {
      "element": "Integration requirements",
      "description": "Hubspot integration with custom data mapping needs",
      "customizable": true
    },
    {
      "element": "Key personnel",
      "description": "CFO Nicole and other stakeholder contacts vary by merchant",
      "customizable": true
    },
    {
      "element": "Timeline dates",
      "description": "Demo, MSA signature, kick-off, and go-live dates are merchant-specific",
      "customizable": true
    },
    {
      "element": "Billing model",
      "description": "Customer creation process and contract structure varies by merchant",
      "customizable": true
    },
    {
      "element": "Opt-out terms",
      "description": "Opt-out clause existence and conditions vary by contract",
      "customizable": true
    },
    {
      "element": "Pain points and goals",
      "description": "Specific business problems and objectives differ per merchant",
      "customizable": true
    },
    {
      "element": "ERP and Tax systems",
      "description": "Technical infrastructure varies by merchant",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Instil MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:32:34

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
    "Integration item categorization and labeling",
    "Post-processing communication workflows",
    "Customer-specific handling and customization"
  ],
  "rules": [
    "Default service term is 1 year when none is listed",
    "Default net payment terms are 30 days when none specified",
    "Default billing frequency is monthly when none listed",
    "Default tax handling: every tax line item becomes a BT (Billable Tax) Events Processing item",
    "Statsig integration items must be labeled as 'Sales'",
    "Pinata integration items must be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Operations team must notify designated stakeholders upon completion of processing batches",
    "Notification timing varies by merchant phase (Implementation or Active)",
    "Invoice dates may be back-dated to final day of month per merchant contract specifications"
  ],
  "exceptions": [
    "Invoice date back-dating to month-end is contract-specific, not universal",
    "Pinata integration items can have alternative labels if merchant specifies otherwise",
    "Tax line item handling can differ if merchant specifies alternative approach",
    "Special memos may be required for certain invoices based on merchant-customer relationships",
    "Invoice changes may be needed due to specific merchant-customer relationships"
  ],
  "merchant_specific": [
    "Contract-specific processing requirements (e.g., invoice date back-dating rules)",
    "Events billing processing instructions (to be filled by Implementation Success)",
    "Integration item labeling conventions (varies by integration partner: Statsig, Pinata, etc.)",
    "Post-processing notification recipients and channels (e.g., Customer Success contact, internal merchant channel)",
    "Notification timing based on merchant phase (Implementation vs Active)",
    "Customer-specific information and special handling requirements",
    "Special invoice memos for particular customers",
    "Feature requests with urgency levels",
    "Referenced Gong call recordings for context"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Instil MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:32:35

### Original Content
```
app gong io call id 3892700273853143293 account-id 4632005772074296398 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Flat SaaS Changing payment terms (could happen mid-contract) Is there any important merchant relationship information Nicole is the consultant CFO 1) What is the merchant temperament So nice, she loves Tabs and totally aligns with our vision 2) Is there a key POC: (i e : who is the buyer decision maker ) Nicole does it al...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Billing Structure and Payment Terms",
    "Merchant Relationship Management and Stakeholder Information",
    "Tabs Platform Feature Requirements and Priorities",
    "Implementation and Operational Workflow",
    "Revenue Recognition and Financial Reporting"
  ],
  "rules": [
    "Operations International Team should ignore sections marked for AE Implementation",
    "Implementation team must document how merchant bills (billing model)",
    "Payment terms changes must be tracked, including mid-contract modifications",
    "Key merchant relationship information must be captured including temperament assessment",
    "Primary Point of Contact (POC) and decision maker must be identified",
    "Critical Tabs features for each merchant must be documented",
    "Auto invoice creation and sending must be configured",
    "Dunning and collections workflow must be implemented",
    "Revenue recognition and reporting capabilities must be enabled",
    "Renewal data and dashboard integration required",
    "Tabs-Hubspot data integration must be established"
  ],
  "exceptions": [
    "Payment terms can change mid-contract (non-standard scenario requiring special handling)",
    "Sections marked '[Ops International Team to Ignore]' are excluded from certain team workflows",
    "Merchant has consultant CFO rather than full-time CFO (non-traditional structure)"
  ],
  "merchant_specific": [
    "Billing model: Flat SaaS structure",
    "Key stakeholder: Nicole (consultant CFO serving as primary POC and decision maker)",
    "Merchant temperament: Highly positive, aligned with Tabs vision",
    "Priority features: Auto invoice creation/sending, dunning/collections, rev rec reporting, renewal dashboard, Hubspot integration",
    "Call reference: Gong.io call ID 3892700273853143293",
    "Account identifier: 4632005772074296398",
    "Integration requirement: Hubspot CRM"
  ],
  "confidence_score": 0.85
}
```

---

