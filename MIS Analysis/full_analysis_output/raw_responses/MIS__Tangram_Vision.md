# Raw LLM Analysis: MIS_ Tangram Vision

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 09:58:34

---

## Chunk 1: MIS_ Tangram Vision_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:34

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urgency Rewatch Calls (AE Implementat...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Success Notification and Communication Protocols",
    "Merchant Relationship Management and Stakeholder Information",
    "Contract Structure and Billing Models",
    "Product Feature Adoption and Value Drivers",
    "Implementation and Onboarding Process Documentation"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed",
      "trigger": "Merchant Phase: Active",
      "type": "notification_requirement"
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success team",
      "fields": ["merchant specifics", "special invoice memos", "invoice changes due to merchant-customer relationships"],
      "type": "documentation_requirement"
    },
    {
      "rule": "Feature Requests section must be filled by AE and Implementation Success",
      "fields": ["what it is", "why it's important", "urgency"],
      "type": "documentation_requirement"
    },
    {
      "rule": "Rewatch Calls section must be filled by AE and Implementation Success",
      "fields": ["rewatch by dates", "notes"],
      "type": "documentation_requirement"
    },
    {
      "rule": "Ops International Team should ignore specific sections marked for AE/Implementation",
      "type": "access_control"
    },
    {
      "rule": "Document merchant billing structure information",
      "options": ["Pilot (1-2 month period)", "Month to month", "Annual", "Tiered usage-based pricing with escalators"],
      "type": "contract_documentation"
    },
    {
      "rule": "Capture merchant temperament and relationship dynamics",
      "type": "relationship_management"
    },
    {
      "rule": "Identify key POC (buyer/decision maker)",
      "type": "stakeholder_management"
    },
    {
      "rule": "Document which Tabs features the key POC values",
      "type": "product_adoption_tracking"
    }
  ],
  "exceptions": [
    {
      "exception": "Some big contracts have tiered usage-based pricing with escalators",
      "context": "Not all contracts follow standard pricing models"
    },
    {
      "exception": "Certain invoices require special memos",
      "context": "Invoice handling may vary based on merchant-customer relationships"
    },
    {
      "exception": "Invoice changes may be required due to merchant customer relationship dynamics",
      "context": "Standard invoice processing may need customization"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipients and channels",
      "example": "Customer Success [Azmat Aziz] in Messari internal merchant channel",
      "customizable": true
    },
    {
      "element": "Merchant temperament description",
      "example": "SO nice and easy going, technical Co-founder doing multiple roles",
      "customizable": true
    },
    {
      "element": "Key POC identification",
      "example": "Brandon - one man show, buyer and decision maker",
      "customizable": true
    },
    {
      "element": "Valued product features",
      "example": "key term extraction, renewals extraction, centralization, automated revenue schedule adjustment, cash forecasting, ARR waterfall",
      "customizable": true
    },
    {
      "element": "Billing model",
      "example": "Pilot/Month-to-month/Annual/Tiered usage-based",
      "customizable": true
    },
    {
      "element": "Special invoice requirements",
      "example": "Special memos for certain invoices",
      "customizable": true
    },
    {
      "element": "Merchant relationship context",
      "example": "Recently parted ways with Co-founder",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_ Tangram Vision_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:38

### Original Content
```
Merchant: Tangram Vision Demo date: Dec 2, 2024 Scoping start date: Dec 2, 2024 MSA Signature Date: Dec 6, 2024 Onboarding Kick Off Date: Dec 16, 2024 Said Jan 1 billing terms but I think he s open to starting earlier [If Exists] Opt Out Date: Go Live Date: Jan 31, 2025 Not set in stone GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Brandon Minor (CEO) CFO: Brandon Minor (CEO) Customer service rep who is really involved: Brandon Minor (CEO) Account Receivab...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Billing and Contract Processing Requirements",
    "Merchant Goals and Pain Points",
    "Operational Defaults and Processing Instructions"
  ],
  "rules": [
    {
      "category": "Contract Processing",
      "rule": "Default Service Term: 1 Year (if none listed in contract)",
      "source": "Default Service Term If None Listed, Ops Default is 1 Year"
    },
    {
      "category": "Contract Processing",
      "rule": "Default Net Payment Terms: 0 days (if none listed in contract)",
      "source": "Default Net Payment Terms If None, Ops Default is 0"
    },
    {
      "category": "Contract Processing",
      "rule": "Default Billing Frequency: Monthly (if none listed in contract)",
      "source": "Default Billing Frequency If None Listed, Ops Default is Monthly"
    },
    {
      "category": "Tax Processing",
      "rule": "Every tax line item becomes a BT (if no specific instruction provided)",
      "source": "How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT"
    },
    {
      "category": "Document Structure",
      "rule": "Implementation Success team fills Contract Processing Steps section",
      "source": "Contract Processing Steps (Implementation Success to fill)"
    },
    {
      "category": "Document Structure",
      "rule": "AE and Implementation team jointly fill Billing model section",
      "source": "Billing model (AE Implementation to fill)"
    },
    {
      "category": "Document Structure",
      "rule": "AE and Implementation team jointly fill Goals section",
      "source": "Goals (North star) (AE Implementation to fill)"
    },
    {
      "category": "Document Structure",
      "rule": "AE fills Company summary section",
      "source": "Company summary (AE to fill)"
    }
  ],
  "exceptions": [
    {
      "type": "Opt-Out Clause",
      "description": "No opt-out clause exists for Tangram Vision",
      "condition": "Merchant-specific: This merchant does not have an opt-out clause"
    },
    {
      "type": "Billing Start Date",
      "description": "Merchant initially said Jan 1 billing terms but may be open to starting earlier",
      "condition": "Flexible start date negotiation"
    },
    {
      "type": "Go Live Date",
      "description": "Jan 31, 2025 go-live date is not set in stone",
      "condition": "Date subject to change"
    },
    {
      "type": "Customer Creation Process",
      "description": "No unique things about customer creation process for this merchant",
      "condition": "Standard process applies"
    },
    {
      "type": "Contract-Specific Processing",
      "description": "Specifics processing things may differ by contract (e.g., back-dating invoice dates)",
      "condition": "Contract-by-contract basis"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key Personnel Consolidation",
      "description": "Brandon Minor (CEO) serves as all key contacts: Accountant, CFO, Customer Service Rep, AR POC, Billing POC",
      "customization_needed": "Single point of contact for all operational matters"
    },
    {
      "element": "Business Model",
      "description": "Computer vision AI software for calibrating robots/machines; transitioning from software-only to software + hardware product offering",
      "customization_needed": "May need to handle both software and hardware billing models"
    },
    {
      "element": "Merchant Goals",
      "description": "Specific goals include: centralize contracts, eliminate manual invoicing, eliminate manual reporting, ensure accurate investor reporting, charge customers correctly",
      "customization_needed": "Success metrics should align with these specific pain points"
    },
    {
      "element": "Integration Items Labeling",
      "description": "Template provides examples (Statsig as 'Sales', Pinata as 'Software Subscription Bundle') but no specific instructions for Tangram Vision",
      "customization_needed": "Merchant-specific integration item labels need to be defined"
    },
    {
      "element": "Post-Processing Notifications",
      "description": "No specific notification requirements documented for Tangram Vision",
      "customization_needed": "May need to establish notification protocols"
    },
    {
      "element": "Timeline Tracking",
      "description": "Multiple milestone dates tracked: Demo, Scoping Start, MSA Signature, Onboarding Kick Off, Go Live",
      "customization_needed": "Each merchant has unique timeline"
    }
  ],
  "confidence_score": 0.92
}
```

---

