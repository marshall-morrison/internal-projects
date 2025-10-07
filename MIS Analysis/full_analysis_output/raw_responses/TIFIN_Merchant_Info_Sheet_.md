# Raw LLM Analysis: TIFIN Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:33:14

---

## Chunk 1: TIFIN Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:14

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urg...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Customer Relationship Management",
    "Implementation Timeline and Urgency",
    "Billing and Payment Structures",
    "Stakeholder Coordination and Documentation"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed",
      "trigger": "Merchant Phase: Active",
      "type": "notification_requirement"
    },
    {
      "rule": "Implementation Success team must fill customer information section",
      "type": "responsibility_assignment"
    },
    {
      "rule": "AE and Implementation Success teams must document feature requests with three components: what it is, why it's important, and urgency level",
      "type": "documentation_requirement"
    },
    {
      "rule": "AE and Implementation Success teams must maintain rewatch call recordings",
      "type": "documentation_requirement"
    },
    {
      "rule": "Notes sections marked for Ops International Team to Ignore should be filled by AE and Implementation teams",
      "type": "responsibility_assignment"
    },
    {
      "rule": "Merchant billing frequency must be documented (annual, monthly, or quarterly)",
      "type": "billing_documentation"
    },
    {
      "rule": "Merchant temperament and relationship information must be documented",
      "type": "relationship_management"
    }
  ],
  "exceptions": [
    {
      "exception": "Certain invoices may require special memos due to merchant-customer relationship dynamics",
      "context": "Invoice processing may have merchant-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed based on merchant customer relationship",
      "context": "Standard invoice processing may need modification"
    },
    {
      "exception": "Ops International Team should ignore specific notes sections",
      "context": "Not all documentation is relevant to all teams"
    },
    {
      "exception": "Implementation timeline may need alignment with merchant's fiscal year",
      "context": "Standard timelines may be adjusted for merchant preference (example: Jenna's 1/1 fiscal year start)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "example": "Azmat Aziz for this merchant",
      "customizable": true
    },
    {
      "element": "Internal communication channel",
      "example": "Messari internal merchant channel",
      "customizable": true
    },
    {
      "element": "Billing frequency",
      "example": "Annual, monthly, or quarterly",
      "customizable": true
    },
    {
      "element": "Business model",
      "example": "B2B SaaS",
      "customizable": true
    },
    {
      "element": "Merchant temperament and relationship notes",
      "example": "Jenna is awesome, very friendly, works hard to get things done",
      "customizable": true
    },
    {
      "element": "Implementation timeline preferences",
      "example": "Align with fiscal year beginning (1/1)",
      "customizable": true
    },
    {
      "element": "Special invoice requirements",
      "example": "Special memos for certain invoices",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "example": "Merchant-specific feature needs",
      "customizable": true
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: TIFIN Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:15

### Original Content
```
Merchant Demo date: Oct 2, 2024 Scoping start date: Oct 2, 2024 MSA Signature Date: Nov 26, 2024 Onboarding Kick Off Date: Dec 2, 2024 (unscheduled) Go Live Date: TBD GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant VP of Finance: Jenna Keenan jenna keenan tifin com Company summary (AE to fill) Summary of what company does: TIFIN is a holding company that creates and operates new companies that apply data science, AI, and technology to address frictions in wealth and ass...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Billing and Payment Configuration",
    "Contract Processing and Default Settings",
    "Integration and Product Item Management",
    "Merchant Business Context and Pain Points"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none listed",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Default product item should be set to 20400 Deferred Revenue",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Merchant operates with no opt-out policy for billing",
      "category": "Billing Model",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps section",
      "category": "Process Ownership",
      "explicit": true
    },
    {
      "rule": "AE and Implementation teams jointly fill Goals/North Star section",
      "category": "Process Ownership",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing may differ and should be noted (e.g., back-dating invoice dates to final day of month)",
      "context": "Contract Processing Steps",
      "applies_when": "Merchant requests specific processing variations by contract"
    },
    {
      "exception": "Integration items may have specific labeling requirements that override defaults",
      "context": "Integration Items Processing",
      "applies_when": "Specific integration types require custom labels (examples: Statsig as 'Sales', Pinata as 'Software Subscription Bundle')"
    }
  ],
  "merchant_specific": [
    {
      "element": "TIFIN is a holding company with 7 subsidiary companies",
      "customization_needed": "Consolidated billing solution across multiple entities"
    },
    {
      "element": "No automation exists on B2B side currently",
      "customization_needed": "Implementation must account for manual-to-automated transition"
    },
    {
      "element": "Key stakeholder: VP of Finance Jenna Keenan",
      "customization_needed": "Communication and approval workflows"
    },
    {
      "element": "Pain point: Lack of consolidated billing across holdco structure",
      "customization_needed": "Multi-entity billing configuration"
    },
    {
      "element": "Merchant-specific timeline with unscheduled Onboarding Kick Off",
      "customization_needed": "Flexible implementation scheduling"
    },
    {
      "element": "Classic signed agreement to billing model",
      "customization_needed": "Standard contract-to-billing workflow applies"
    },
    {
      "element": "ERP and Tax Integration fields left blank",
      "customization_needed": "May require discovery or default system assignment"
    }
  ],
  "confidence_score": 0.92
}
```

---

