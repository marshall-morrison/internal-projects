# Raw LLM Analysis:  Veruna Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:21:25

---

## Chunk 1:  Veruna Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:21:25

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and billing event processing workflows",
    "Integration item categorization and labeling",
    "Post-processing communication protocols",
    "Customer-specific invoice handling requirements",
    "Implementation and operations team coordination"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: Every tax line item becomes a BT Events Processing when none are specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Statsig integration items must be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Pinata integration items must be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active phase",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling in events billing, integration items processing, customer information, and feature requests",
      "category": "Team Responsibilities",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success teams are responsible for documenting feature requests and rewatch calls",
      "category": "Team Responsibilities",
      "explicit": true
    },
    {
      "rule": "International Ops Team should ignore the Notes Sections",
      "category": "Team Scope",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by the merchant",
      "condition": "Merchant provides alternative labeling instructions"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Specific customer relationships require custom handling"
    },
    {
      "exception": "Invoice changes may be necessary due to merchant customer relationship specifics",
      "condition": "Customer-specific requirements override standard processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "description": "Each merchant may have different integration types (Statsig, Pinata) requiring specific labels",
      "customizable": true
    },
    {
      "element": "Post-processing notification recipients",
      "description": "Who needs to be notified, where, and when varies by merchant (example shows Azmat Aziz for Messari)",
      "customizable": true
    },
    {
      "element": "Customer-specific invoice requirements",
      "description": "Special memos and invoice modifications based on individual customer relationships",
      "customizable": true
    },
    {
      "element": "Billing frequency",
      "description": "Merchants may bill annually, monthly, or quarterly",
      "customizable": true
    },
    {
      "element": "Service delivery method",
      "description": "Services component may be manual or automated depending on merchant",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "description": "Merchant-specific feature needs with urgency levels",
      "customizable": true
    },
    {
      "element": "Merchant phase",
      "description": "Processing varies between Implementation and Active phases",
      "customizable": false
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2:  Veruna Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:21:26

### Original Content
```
verMerchant Demo date: Nov 25, 2024 Scoping start date: none MSA Signature Date: Nov 26, 2024 Onboarding Kick Off Date: Dec 2, 2024 Go Live Date: TBD GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Chris Light clight veruna com Company summary (AE to fill) Summary of what company does: Veruna is the  1 Salesforce com-native agency management system Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are we solving Why are they buyi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Contract Auditing and Historical Billing Verification",
    "Default Billing and Contract Parameters",
    "Contract Processing Workflow and Requirements",
    "Merchant Business Context and Pain Points"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Defaults",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Billing model follows classic signed agreement to billing process",
      "category": "Billing Workflow",
      "explicit": true
    },
    {
      "rule": "No opt-out option for customers",
      "category": "Customer Management",
      "explicit": true
    },
    {
      "rule": "Priority task is auditing previous contracts for correct billing amounts",
      "category": "Implementation Priority",
      "explicit": true
    },
    {
      "rule": "Historical contracts need to be pulled and reviewed",
      "category": "Contract Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract processing specifics may differ by individual contract",
      "context": "Mentioned as potential variation (e.g., back-dating invoice dates)"
    },
    {
      "exception": "Merchant has halted GTM (Go-To-Market) activities",
      "context": "Impacts how contract breakup is handled",
      "status": "Incomplete information - sentence appears truncated"
    },
    {
      "exception": "Tax handling as line item requires clarification",
      "context": "Question posed but not answered in document"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Identity",
      "details": "Veruna - #1 Salesforce.com-native agency management system"
    },
    {
      "element": "Key Contact",
      "details": "CEO Chris Light (clight@veruna.com)"
    },
    {
      "element": "Timeline",
      "details": {
        "demo_date": "Nov 25, 2024",
        "msa_signature": "Nov 26, 2024",
        "onboarding_kickoff": "Dec 2, 2024",
        "go_live": "TBD"
      }
    },
    {
      "element": "Merchant-Specific Priority",
      "details": "CEO's #1 priority is auditing previous contracts for billing accuracy"
    },
    {
      "element": "Merchant Resources",
      "details": "Hiring assistant (starting Monday) to pull historic contracts"
    },
    {
      "element": "Customer Creation Process",
      "details": "None - described as standard/not unique"
    },
    {
      "element": "Integration Requirements",
      "details": {
        "erp": "Not specified",
        "tax_integration": "Not specified",
        "gtm_poc": "Not specified",
        "implementation_poc": "Not specified"
      }
    }
  ],
  "confidence_score": 0.72,
  "confidence_notes": "Document appears to be incomplete or in-progress with several fields marked as 'n/a', 'none', or left blank. Some sentences are truncated (e.g., 'They've halted GTM so How contract is broken up'). The default rules are clearly stated, but merchant-specific processing requirements and integration details are largely missing. The primary merchant pain point (contract auditing) is clear, but implementation specifics are underdeveloped."
}
```

---

## Chunk 3:  Veruna Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:21:35

### Original Content
```
Seats that can change and need proration Is there any important merchant relationship information 1) What is the merchant temperament Chris will be a great partner for Tabs He s all business and has high expectations, abut he also understands that there is more that needs to be built out on the platform
```

### LLM Analysis Response
```json
{
  "themes": [
    "Seat-based pricing and proration",
    "Merchant relationship management",
    "Partner expectations and temperament assessment",
    "Platform development and feature completeness",
    "Business relationship dynamics"
  ],
  "rules": [
    "Seats that can change require proration calculations",
    "Merchant relationship information should be documented and tracked",
    "Partner temperament and expectations should be assessed and recorded",
    "Platform limitations should be acknowledged in merchant relationships"
  ],
  "exceptions": [
    "Chris (merchant contact) understands platform is still being built out - may have different expectations than typical merchants",
    "High-expectation merchants may require special handling despite platform limitations"
  ],
  "merchant_specific": [
    "Merchant contact name: Chris",
    "Merchant temperament: 'all business' with high expectations",
    "Merchant understanding: aware of platform development needs",
    "Relationship quality: described as 'great partner for Tabs'",
    "Communication style preference: business-focused approach",
    "Tolerance level: patient with platform development roadmap"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document chunk appears to be fragmented or incomplete, with unclear sentence structure (particularly the opening about seats and proration). The merchant relationship information is clearer and more actionable, but the overall context is limited. The confidence is moderate because while some clear patterns emerge (relationship documentation, proration needs), the incomplete nature of the text makes it difficult to extract fully reliable, generalizable rules.

---

