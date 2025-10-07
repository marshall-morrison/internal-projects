# Raw LLM Analysis: MIS - Primary Lab

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 09:58:52

---

## Chunk 1: MIS - Primary Lab_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:52

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
    "Team Roles and Responsibilities",
    "Contract and Invoice Management",
    "Feature Requests and Feedback Tracking"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in the Messari internal merchant channel when contracts are processed",
      "trigger": "Merchant Phase: Active",
      "type": "notification_requirement"
    },
    {
      "rule": "Bridget handles contract management and is responsible for tracking design and engineering service hours",
      "type": "role_responsibility"
    },
    {
      "rule": "Bridget ensures the correct amount of hours is invoiced out",
      "type": "billing_requirement"
    },
    {
      "rule": "Standish (Accounting team) handles QBO, collections, dunning, and cash applications",
      "type": "role_responsibility"
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information",
      "type": "role_responsibility"
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling feature requests and rewatch call information",
      "type": "role_responsibility"
    },
    {
      "rule": "Ops International Team should ignore certain notes sections",
      "type": "process_exclusion"
    }
  ],
  "exceptions": [
    {
      "exception": "Certain invoices require special memos due to merchant-customer relationships",
      "context": "Invoice changes may be needed based on specific merchant customer relationships"
    },
    {
      "exception": "Ops International Team explicitly excluded from certain notes sections",
      "context": "Role-based access or responsibility limitations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Success contact person (Azmat Aziz)",
      "customization_type": "personnel_assignment"
    },
    {
      "element": "Messari internal merchant channel",
      "customization_type": "communication_channel"
    },
    {
      "element": "Special memos for certain invoices",
      "customization_type": "billing_customization"
    },
    {
      "element": "Important customer information specifics",
      "customization_type": "customer_details"
    },
    {
      "element": "Feature requests with urgency levels",
      "customization_type": "merchant_requirements"
    },
    {
      "element": "Rewatch call dates and notes",
      "customization_type": "merchant_interaction_tracking"
    },
    {
      "element": "Primary Lab Team composition (Bridget and Standish)",
      "customization_type": "team_assignment"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document structure is somewhat fragmented and appears to be a template with placeholder sections
- Some sections are incomplete (e.g., "FR 1 What is it Why it's important Urgency")
- Clear role assignments and notification requirements are present
- The merchant-specific nature of many elements is evident but details are limited
- Some ambiguity exists around the exact workflow and dependencies between teams

---

## Chunk 2: MIS - Primary Lab_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:55

### Original Content
```
Merchant Demo date: August Scoping start date: N A MSA Signature Date: Sep 30, 2024 Onboarding Kick Off Date: Oct 2, 2024 [If Exists] Opt Out Date: N A Go Live Date: GTM POC:   Daniel Implementation POC: ERP: Tax Integration: (pretty sure) Key people at Merchant CFO: Mike Witkowski Operations: Bridget Flaherty Accounting team (outsourced): Standish Company summary (AE to fill) Primary Venture Partners is a venture capital firm with two different entities: Primary Labs (an entity that houses all ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "Billing Models and Invoice Processing",
    "Contract Management and Service Terms",
    "Default Operational Parameters",
    "Stakeholder Roles and Responsibilities"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "contract_defaults"
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "payment_terms"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_frequency"
    },
    {
      "rule": "For executive recruiting fees without specific dates, default to increments of 30 days",
      "category": "recruiting_fees"
    },
    {
      "rule": "Hourly fee of $125 should be set up as usage type invoicing for monthly, in arrears billing",
      "category": "usage_billing"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) Events by default",
      "category": "tax_handling"
    },
    {
      "rule": "OIR (Operator In Residences) salary items are added as one-off items by stakeholder Bridget",
      "category": "special_billing"
    },
    {
      "rule": "Use amount and payment terms outlined in contract for executive recruiting fees",
      "category": "recruiting_fees"
    },
    {
      "rule": "Process hourly fees at two rates: $125 and $150 as separate event types",
      "category": "usage_billing"
    }
  ],
  "exceptions": [
    {
      "exception": "OIR salary invoicing is handled manually by Bridget as one-off items, not through standard automated process",
      "condition": "when_billing_oir_salary"
    },
    {
      "exception": "Executive recruiting fees follow contract-specific payment terms when available, otherwise default to 30-day increments",
      "condition": "when_contract_specifies_terms"
    },
    {
      "exception": "Merchant has two entities (Primary Labs and Primary management company) but implementation starts with Primary Labs only",
      "condition": "phased_entity_onboarding"
    },
    {
      "exception": "No contracts should be ignored (explicitly stated as 'No' to ignoring contracts)",
      "condition": "contract_processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Entity Structure",
      "details": "Two entities: Primary Labs (incubation work) and Primary management company",
      "customization_needed": true
    },
    {
      "element": "Invoice Volume",
      "details": "Approximately 50 invoices per month",
      "customization_needed": false
    },
    {
      "element": "Key Stakeholders",
      "details": "CFO: Mike Witkowski, Operations: Bridget Flaherty, Accounting: Standish Company (outsourced)",
      "customization_needed": true
    },
    {
      "element": "Service Types",
      "details": "Executive recruiting fees, Design and Engineering Services, OIR Salary, Contract Processing",
      "customization_needed": true
    },
    {
      "element": "Billing Recipients",
      "details": "Portfolio companies and incubated companies (portcos)",
      "customization_needed": true
    },
    {
      "element": "Event Types",
      "details": "Hourly Fee ($125), Hourly Fee ($150)",
      "customization_needed": true
    },
    {
      "element": "Current Process Owners",
      "details": "Contracts and invoicing: Bridget, Dunning & collections: Standish",
      "customization_needed": true
    },
    {
      "element": "Goals",
      "details": "Manage contracts, Automated invoicing, Dunning & collections, Simpler reporting",
      "customization_needed": false
    }
  ],
  "confidence_score": 0.88
}
```

---

