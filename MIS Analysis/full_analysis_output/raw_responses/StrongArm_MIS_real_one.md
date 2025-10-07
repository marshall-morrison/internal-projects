# Raw LLM Analysis: StrongArm MIS (real one)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:47:27

---

## Chunk 1: StrongArm MIS (real one)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:47:27

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urg...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Merchant Relationship Management",
    "Contract and Billing Complexity",
    "Feature Requirements and Customization",
    "Stakeholder Identification and Management"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in the Messari internal merchant channel when contracts are processed",
      "trigger": "Merchant Phase: Active",
      "type": "notification_requirement"
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information section",
      "type": "role_responsibility"
    },
    {
      "rule": "AE Implementation Success team is responsible for filling Feature Requests section",
      "type": "role_responsibility"
    },
    {
      "rule": "AE Implementation Success team is responsible for filling Rewatch Calls section",
      "type": "role_responsibility"
    },
    {
      "rule": "AE Implementation team is responsible for filling Notes sections",
      "type": "role_responsibility"
    },
    {
      "rule": "Ops International Team should ignore Notes sections",
      "type": "role_exclusion"
    },
    {
      "rule": "Document must capture merchant temperament assessment",
      "type": "relationship_documentation"
    },
    {
      "rule": "Document must identify key POC (buyer/decision maker)",
      "type": "stakeholder_documentation"
    },
    {
      "rule": "Document must identify Tabs features that key POC cares about",
      "type": "feature_documentation"
    }
  ],
  "exceptions": [
    {
      "exception": "Certain invoices require special memos due to merchant customer relationship",
      "context": "Invoice processing may have merchant-specific requirements"
    },
    {
      "exception": "Some contracts have complex parent-child relationships",
      "context": "Billing complexity varies by merchant structure"
    },
    {
      "exception": "Merchant bills out of multiple systems (QB and HS)",
      "context": "Billing system integration may vary by merchant"
    },
    {
      "exception": "Hardware and software contracts may be handled differently",
      "context": "Contract type affects processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "example": "Customer Success [Azmat Aziz]",
      "customizable": true
    },
    {
      "element": "Key stakeholders and roles",
      "example": "Alex Teller (President), Mike Angwin (Head of Fin), Taylor Feldt-Hjelvik (Accountant)",
      "customizable": true
    },
    {
      "element": "Merchant temperament description",
      "example": "feels like a friends and family partner",
      "customizable": true
    },
    {
      "element": "Key POC identification",
      "example": "Alex Teller",
      "customizable": true
    },
    {
      "element": "Feature priorities",
      "example": "Ability to manage bespoke contracts",
      "customizable": true
    },
    {
      "element": "Billing systems used",
      "example": "QB and HS",
      "customizable": true
    },
    {
      "element": "Contract structure complexity",
      "example": "parent-child relationships, hardware/software split",
      "customizable": true
    },
    {
      "element": "Special invoice memo requirements",
      "customizable": true
    },
    {
      "element": "Communication channel location",
      "example": "Messari internal merchant channel, Slack Channel",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: StrongArm MIS (real one)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:47:28

### Original Content
```
Merchant Demo date: Oct 9, 2024 Scoping start date: Oct 9, 2024 MSA Signature Date: Dec 24, 2024 Onboarding Kick Off Date: Jan 6, 2025 [If Exists] Opt Out Date: NA Go Live Date: Jan 20, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Company summary (AE to fill) StrongArm sells Hardware Software based around safety in warehouses Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are we solving Why are they buying Tabs Is there an ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Timeline and Milestones",
    "Customer and Contract Data Mapping",
    "Billing Configuration and Processing Rules",
    "Integration and System Setup",
    "Stakeholder Communication and Coordination"
  ],
  "rules": [
    {
      "category": "Customer Creation",
      "rule": "All customers exist in QBO and should not need to be created in Tabs",
      "action": "If customer cannot be found in QBO, create in Garage"
    },
    {
      "category": "Data Mapping",
      "rule": "Customer name is found in 'Client' field (first row in Order Form)"
    },
    {
      "category": "Data Mapping",
      "rule": "Start date for invoicing and revenue is 'Order Form Effective Date'"
    },
    {
      "category": "Data Mapping",
      "rule": "Term length is found in 'Order Form Term'"
    },
    {
      "category": "Data Mapping",
      "rule": "Item Name comes from left-most column in order form (e.g., 'Access' or 'Expenses')"
    },
    {
      "category": "Data Mapping",
      "rule": "Amount comes from right-most column in order form"
    },
    {
      "category": "Processing Exclusions",
      "rule": "Ignore billing terms where Fee is 'WAIVED', 'INCLUDED', or 'N/A'"
    },
    {
      "category": "Payment Terms",
      "rule": "Default Net Payment Terms: 30 days"
    },
    {
      "category": "Service Terms",
      "rule": "Default Service Term is stated in 'Order Form Term'"
    },
    {
      "category": "Billing Frequency",
      "rule": "Use Section 3 Payment Terms to find specific payment schedule"
    },
    {
      "category": "Tax Handling",
      "rule": "No tax line items to be processed (N/A)"
    },
    {
      "category": "Opt Out Clause",
      "rule": "No opt out clause exists for this merchant"
    }
  ],
  "exceptions": [
    {
      "condition": "Customer not found in QBO",
      "action": "Create customer in Garage instead of Tabs"
    },
    {
      "condition": "Fee marked as 'WAIVED', 'INCLUDED', or 'N/A'",
      "action": "Ignore these billing terms during processing"
    },
    {
      "condition": "Billing model varies by customer",
      "note": "Merchant bills differently depending on the customer - very bespoke approach"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "StrongArm sells Hardware/Software for warehouse safety"
    },
    {
      "element": "ERP System",
      "details": "Uses QuickBooks Online (QBO) as primary customer database"
    },
    {
      "element": "Order Form Structure",
      "details": "Specific column layout: left-most for Item Name, right-most for Amount"
    },
    {
      "element": "Order Form Fields",
      "details": "Custom fields include 'Client', 'Order Form Effective Date', 'Order Form Term', 'Section 3 Payment Terms'"
    },
    {
      "element": "Billing Model",
      "details": "Bespoke billing that changes depending on the customer"
    },
    {
      "element": "Integration Items",
      "details": "Pending - waiting on customer to fill out, will update Ashni Waliaw when available"
    },
    {
      "element": "Key Dates",
      "details": "Demo: Oct 9, 2024; MSA: Dec 24, 2024; Kick Off: Jan 6, 2025; Go Live: Jan 20, 2025"
    },
    {
      "element": "Events Billing",
      "details": "Not applicable for this merchant"
    }
  ],
  "confidence_score": 0.92
}
```

---

