# Raw LLM Analysis: StrongArm MIS (real one)(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:53:46

---

## Chunk 1: StrongArm MIS (real one)(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:46

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
    "Customer and Contract Information Tracking",
    "Feature Requests and Product Feedback",
    "Billing and Invoice Management"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in the Messari internal merchant channel when contracts are processed",
      "condition": "Merchant Phase: Active",
      "category": "notification"
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information section",
      "category": "responsibility"
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling Feature Requests section",
      "category": "responsibility"
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling Rewatch Calls section",
      "category": "responsibility"
    },
    {
      "rule": "Operations International Team should ignore the Notes section",
      "category": "responsibility"
    },
    {
      "rule": "AE and Implementation teams are responsible for filling the Notes section",
      "category": "responsibility"
    },
    {
      "rule": "Document must capture merchant temperament assessment",
      "category": "relationship_management"
    },
    {
      "rule": "Document must identify key POC (buyer/decision maker)",
      "category": "relationship_management"
    },
    {
      "rule": "Document must track which Tabs features the key POC cares about",
      "category": "product_management"
    }
  ],
  "exceptions": [
    {
      "exception": "Special memos may be required for certain invoices",
      "context": "Based on merchant-customer relationship"
    },
    {
      "exception": "Invoice changes may occur due to merchant customer relationship dynamics",
      "context": "Requires tracking and documentation"
    },
    {
      "exception": "Some contracts have complex parent-child relationships",
      "context": "Affects billing structure (hardware/software)"
    },
    {
      "exception": "Operations International Team explicitly excluded from Notes section",
      "context": "Team-specific workflow exception"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "example": "Customer Success [Azmat Aziz]",
      "customizable": true
    },
    {
      "element": "Key contacts and roles",
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
      "element": "Billing system configuration",
      "example": "Bills out of QB and HS",
      "customizable": true
    },
    {
      "element": "Contract structure complexity",
      "example": "complex parent child relationships, hardware software",
      "customizable": true
    },
    {
      "element": "Feature priorities",
      "example": "Ability to manage bespoke contracts",
      "customizable": true
    },
    {
      "element": "Communication channels",
      "example": "Messari internal merchant channel, Slack Channel",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: StrongArm MIS (real one)(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:52

### Original Content
```
Merchant Demo date: Oct 9, 2024 Scoping start date: Oct 9, 2024 MSA Signature Date: Dec 24, 2024 Onboarding Kick Off Date: Jan 6, 2025 [If Exists] Opt Out Date: NA Go Live Date: Jan 20, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Company summary (AE to fill) StrongArm sells Hardware Software based around safety in warehouses Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are we solving Why are they buying Tabs Is there an ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Timeline and Milestones",
    "Customer and Billing Configuration",
    "Contract Processing Workflow",
    "Data Source Mapping and Field Extraction",
    "Integration and Communication Requirements"
  ],
  "rules": [
    {
      "rule": "All customers exist in QBO (QuickBooks Online) and should not need to be created in Tabs",
      "category": "Customer Creation",
      "action": "If customer cannot be found in QBO, then create in Garage"
    },
    {
      "rule": "Customer name is extracted from 'Client' field (first row in Order Form)",
      "category": "Data Mapping",
      "source": "Order Form"
    },
    {
      "rule": "Start date for invoicing and revenue is extracted from 'Order Form Effective Date'",
      "category": "Data Mapping",
      "source": "Order Form"
    },
    {
      "rule": "Term length is extracted from 'Order Form Term'",
      "category": "Data Mapping",
      "source": "Order Form"
    },
    {
      "rule": "Item Name comes from left-most column in order form (e.g., 'Access' or 'Expenses')",
      "category": "Data Mapping",
      "source": "Order Form"
    },
    {
      "rule": "Amount comes from right-most column in order form",
      "category": "Data Mapping",
      "source": "Order Form"
    },
    {
      "rule": "Ignore billing terms where Fee is 'WAIVED', 'INCLUDED', or 'N/A'",
      "category": "Contract Processing",
      "action": "Skip these line items"
    },
    {
      "rule": "Default Service Term is stated in 'Order Form Term'",
      "category": "Billing Configuration",
      "default_value": "From Order Form"
    },
    {
      "rule": "Default Net Payment Terms is 30 days",
      "category": "Billing Configuration",
      "default_value": "30"
    },
    {
      "rule": "Billing Frequency is determined using Section 3 Payment Terms",
      "category": "Billing Configuration",
      "source": "Section 3 Payment Terms"
    },
    {
      "rule": "Taxes are not handled as a line item (N/A)",
      "category": "Tax Processing",
      "action": "No tax line items"
    }
  ],
  "exceptions": [
    {
      "exception": "If customer cannot be found in QBO, create in Garage instead",
      "condition": "Customer not found in QBO",
      "action": "Create in Garage system"
    },
    {
      "exception": "Billing terms with fees marked as 'WAIVED', 'INCLUDED', or 'N/A' should be ignored",
      "condition": "Fee status is waived, included, or not applicable",
      "action": "Skip processing these terms"
    },
    {
      "exception": "Billing model changes depending on the customer and is very bespoke",
      "condition": "Customer-specific requirements",
      "action": "Review individual customer billing needs"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "StrongArm",
      "description": "Sells Hardware/Software for warehouse safety"
    },
    {
      "element": "ERP System",
      "value": "QBO (QuickBooks Online)",
      "description": "Primary system for customer records"
    },
    {
      "element": "Opt Out Clause",
      "value": "No",
      "description": "No opt-out clause exists in contract"
    },
    {
      "element": "Contract Structure",
      "value": "Not Applicable",
      "description": "No specific contract breakdown mentioned"
    },
    {
      "element": "Billing Model",
      "value": "Bespoke/Customer-dependent",
      "description": "Billing changes depending on customer, very customized"
    },
    {
      "element": "Document Source",
      "value": "Order Form",
      "description": "Primary document for extracting contract data"
    },
    {
      "element": "Key Data Fields",
      "value": ["Client", "Order Form Effective Date", "Order Form Term", "Section 3 Payment Terms"],
      "description": "Specific fields to extract from Order Form"
    },
    {
      "element": "Integration Items",
      "value": "Pending",
      "description": "Waiting on customer to fill out, will update Ashni Waliaw when available"
    },
    {
      "element": "Events Billing",
      "value": "N/A",
      "description": "No events billing required"
    },
    {
      "element": "Tax Integration",
      "value": "Not specified",
      "description": "No tax integration details provided"
    },
    {
      "element": "Timeline",
      "value": {
        "demo_date": "Oct 9, 2024",
        "scoping_start": "Oct 9, 2024",
        "msa_signature": "Dec 24, 2024",
        "onboarding_kickoff": "Jan 6, 2025",
        "go_live": "Jan 20, 2025"
      },
      "description": "Merchant-specific implementation timeline"
    }
  ],
  "confidence_score": 0.88
}
```

---

