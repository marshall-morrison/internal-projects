# Raw LLM Analysis: Axion Ray Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:02:43

---

## Chunk 1: Axion Ray Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:02:43

### Original Content
```
Merchant - Axion Ray Demo date: April 12 2024 Scoping start date: Apr 12, 2023 MSA Signature Date: May 21, 2024 Onboarding Kick Off Date: May 24, 2024 Go Live Date: May 24, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Gabe Hoffman Customer service rep who is really involved: Account Receivable POC Billing POC etc Company summary Axion Ray is the leading AI observability command center relied on by global manufacturing companies to detect and sol...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline Management",
    "Billing Model and Contract Processing",
    "Automation and Data Centralization",
    "Stakeholder Management and Relationship Dynamics",
    "Operational Defaults and Processing Standards"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Processing",
      "description": "Do not add descriptions into the description field in BTs when descriptions are extremely long",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Billing Frequency",
      "description": "Default to up-front billing unless there is a schedule specified in the contract (annual, biannual, quarterly)",
      "explicit": true
    },
    {
      "rule_id": "R3",
      "category": "Billing Frequency",
      "description": "There is zero monthly billing for this merchant",
      "explicit": true
    },
    {
      "rule_id": "R4",
      "category": "Service Term",
      "description": "Default Service Term is 1 Year if none listed",
      "explicit": true
    },
    {
      "rule_id": "R5",
      "category": "Payment Terms",
      "description": "Default Net Payment Terms is 0 if none specified",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Billing Frequency",
      "description": "Default Billing Frequency is Monthly if none listed (ops default)",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Tax Processing",
      "description": "Every tax line item becomes a BT (Billing Transaction)",
      "explicit": true
    },
    {
      "rule_id": "R8",
      "category": "Contract Type",
      "description": "Contract is straight SaaS billing with no usage or other billing components",
      "explicit": true
    },
    {
      "rule_id": "R9",
      "category": "Integration",
      "description": "Integration items should be assigned to 'Axion Platform'",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Long descriptions (e.g., Baxter Healthcare) should be processed with no description in BTs",
      "condition": "When descriptions are extremely long",
      "impact": "Deviation from standard description field population"
    },
    {
      "exception_id": "E2",
      "description": "No monthly billing exists for this merchant",
      "condition": "Always applicable for this merchant",
      "impact": "Excludes monthly as a billing frequency option"
    },
    {
      "exception_id": "E3",
      "description": "Merchant has an opt-out renegotiation point in their contract",
      "condition": "At specified contract milestone",
      "impact": "Requires proactive engagement to ensure product adoption and retention"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "Axion Ray - AI observability command center for global manufacturing companies",
      "customization_needed": true
    },
    {
      "element": "Key Stakeholders",
      "details": "CFO: Gabe Hoffman (buyer/decision maker, sharp temperament, not difficult to work with)",
      "customization_needed": true
    },
    {
      "element": "Timeline",
      "details": "Demo: Apr 12 2024, Scoping: Apr 12 2023, MSA: May 21 2024, Kick Off: May 24 2024, Go Live: May 24 2024",
      "customization_needed": true
    },
    {
      "element": "Current State",
      "details": "Manual processes in QBO, tracked in Excel spreadsheets, not high volume yet",
      "customization_needed": true
    },
    {
      "element": "Goals",
      "details": "Consolidation, automation ahead of scale, centralized notes storage, reporting, eventual rev rec",
      "customization_needed": true
    },
    {
      "element": "Key Features",
      "details": "Automation, centralized repository for finance/AR data including merchant notes",
      "customization_needed": true
    },
    {
      "element": "Billing Model",
      "details": "Not very high volume, straight SaaS billing, no usage components, opt-out renegotiation point exists",
      "customization_needed": true
    },
    {
      "element": "Description Processing",
      "details": "Extremely long descriptions (e.g., Baxter Healthcare) - process with no description",
      "customization_needed": true
    },
    {
      "element": "Integration Assignment",
      "details": "Axion Platform",
      "customization_needed": true
    },
    {
      "element": "Retention Risk",
      "details": "Important to get Gabe hooked on product and new tools like rev rec due to opt-out clause",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Axion Ray Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:02:44

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests FR 1 What is it Why it's important Urgency Rewatch Calls first call - https: tabs rewatch com video tngcex2...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and escalation protocols",
    "Customer relationship management and communication",
    "Invoice processing and special requirements",
    "Feature request tracking and prioritization",
    "Internal documentation and knowledge management"
  ],
  "rules": [
    {
      "rule": "Customer Success team member (Azmat Aziz) must be notified when contracts are processed",
      "context": "Notification occurs in Messari internal merchant channel during Active merchant phase",
      "type": "notification_requirement"
    },
    {
      "rule": "Merchant-specific customer information must be documented and tracked",
      "context": "Important information on specific customers of the merchant should be maintained",
      "type": "documentation_requirement"
    },
    {
      "rule": "Special memos are required for certain invoices",
      "context": "Invoice-specific requirements based on merchant-customer relationships",
      "type": "invoice_processing"
    },
    {
      "rule": "Feature requests must be documented with specific attributes",
      "context": "Must include: what it is, why it's important, and urgency level",
      "type": "feature_request_management"
    },
    {
      "rule": "Call recordings must be maintained and referenced",
      "context": "Links to first calls and custom demos should be preserved for reference",
      "type": "documentation_requirement"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice changes may be required due to merchant-customer relationship dynamics",
      "condition": "Specific customer relationships may necessitate invoice modifications",
      "impact": "Standard invoice processing may need adjustment"
    },
    {
      "exception": "Certain invoices require special memos",
      "condition": "Not all invoices require memos, only specific ones based on merchant requirements",
      "impact": "Additional documentation step for select invoices"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "example": "Azmat Aziz for Customer Success",
      "customization_needed": "Different merchants may have different Customer Success representatives"
    },
    {
      "element": "Communication channel",
      "example": "Messari internal merchant channel",
      "customization_needed": "Each merchant likely has their own dedicated internal channel"
    },
    {
      "element": "Customer-specific information",
      "example": "Special customer requirements and relationships",
      "customization_needed": "Each merchant will have unique customer base and requirements"
    },
    {
      "element": "Invoice memo requirements",
      "example": "Certain invoices require special memos",
      "customization_needed": "Memo requirements vary by merchant and their customer relationships"
    },
    {
      "element": "Onboarding documentation",
      "example": "First call and custom demo recordings (Rewatch links)",
      "customization_needed": "Each merchant has unique onboarding calls and demos"
    },
    {
      "element": "Feature requests",
      "example": "FR 1 with specific attributes",
      "customization_needed": "Feature requests are merchant-specific based on their needs"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document chunk is somewhat fragmented and appears to be a template or partial instruction set
- Clear structure is evident for notification protocols and feature request tracking
- Some sections are incomplete (e.g., "Special memo s certain invoices require" appears truncated)
- The Rewatch video links provide concrete examples but context is limited
- The "FR 1" section header exists but details are cut off
- Overall structure and intent are clear, but missing details reduce confidence in completeness

---

