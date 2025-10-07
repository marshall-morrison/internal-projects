# Raw LLM Analysis: Copy of [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:01:13

---

## Chunk 1: Copy of [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:01:13

### Original Content
```
1) What is the merchant temperament 2) Is there a key POC: (i e : who is the buyer decision maker ) 3) What are the Tabs features that the key POC cares about
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship assessment and profiling",
    "Decision-maker identification and stakeholder mapping",
    "Product feature alignment with customer needs",
    "Customer discovery and qualification process"
  ],
  "rules": [
    "Must assess merchant temperament as part of qualification process",
    "Must identify the key Point of Contact (POC) for the merchant account",
    "Must determine who holds buyer decision-making authority",
    "Must understand which Tabs product features are relevant to the key POC",
    "Must align product features with decision-maker priorities"
  ],
  "exceptions": [
    "The key POC may not always be the same as the buyer decision maker (implied by separate mention)",
    "Different POCs may care about different Tabs features based on their role"
  ],
  "merchant_specific": [
    "Merchant temperament - varies by individual merchant personality and business culture",
    "Key POC identity - specific person or role varies per merchant organization",
    "Buyer decision maker - may be different individual/role depending on merchant structure",
    "Tabs features of interest - will vary based on merchant's specific business needs, pain points, and priorities",
    "Organizational structure - decision-making authority may be centralized or distributed differently per merchant"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Copy of [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:01:30

### Original Content
```
Merchant Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Feb 7, 2024 [If Exists] Opt Out Date: Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary Summary of what company does Goals (North star) What is the merchant's goal What pain are we solving Why are they buying Tabs Is there ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters and Standards",
    "Stakeholder Communication and Coordination",
    "Merchant-Specific Customization and Integration Requirements"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (immediate payment) if none specified",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Operations team must track key milestone dates: Demo, Scoping Start, MSA Signature, Onboarding Kick Off, Opt Out (if exists), and Go Live dates",
      "category": "Project Management",
      "explicit": true
    },
    {
      "rule": "Key stakeholders must be identified including Accountant, CFO, Customer Service Rep, AR POC, and Billing POC",
      "category": "Stakeholder Management",
      "explicit": true
    },
    {
      "rule": "Merchant goals and pain points must be documented to understand purchase rationale",
      "category": "Business Requirements",
      "explicit": true
    },
    {
      "rule": "Opt-out clauses must be tracked with specific conditions that prevent merchant from exercising the clause",
      "category": "Contract Management",
      "explicit": true
    },
    {
      "rule": "Integration items must be assigned specific labels according to merchant requirements",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Post-processing notifications must be sent to designated team members at specified phases",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "International Operations Team should ignore AE Implementation Notes sections",
      "category": "Team Responsibilities",
      "explicit": true
    },
    {
      "rule": "Contract processing steps must document anything to ignore in contracts",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Special customer-specific invoice requirements and memos must be documented",
      "category": "Customer Management",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations may override defaults (e.g., back-dating invoice dates to final day of month)",
      "condition": "When merchant requests specific processing that differs by contract",
      "impact": "Standard processing rules may be superseded"
    },
    {
      "exception": "Integration item labeling may have conditional rules based on merchant specifications",
      "condition": "Unless otherwise noted by Merchant (e.g., Pinata items default to 'Software Subscription Bundle' unless specified)",
      "impact": "Default integration labels can be overridden"
    },
    {
      "exception": "Unique customer creation processes may exist for specific merchants",
      "condition": "When merchant has non-standard billing or customer setup requirements",
      "impact": "Standard customer creation workflow may not apply"
    },
    {
      "exception": "Tax handling may deviate from default BT assignment",
      "condition": "When merchant has specific tax processing requirements",
      "impact": "Custom tax line item processing may be needed"
    },
    {
      "exception": "Invoice changes may be required based on merchant-customer relationships",
      "condition": "When specific customer relationships warrant special treatment",
      "impact": "Standard invoice generation may need modification"
    }
  ],
  "merchant_specific": [
    {
      "element": "ERP System",
      "customization_type": "Technology Integration",
      "description": "Each merchant may use different ERP systems requiring custom integration"
    },
    {
      "element": "Tax Integration",
      "customization_type": "Tax Processing",
      "description": "Tax handling varies by merchant's tax system and requirements"
    },
    {
      "element": "Billing Model",
      "customization_type": "Revenue Recognition",
      "description": "Each merchant may have unique billing models and contract structures"
    },
    {
      "element": "Customer Creation Process",
      "customization_type": "Workflow",
      "description": "Merchant-specific processes for how customers are created and managed"
    },
    {
      "element": "Integration Item Labels",
      "customization_type": "Data Classification",
      "description": "Specific labeling conventions for integration items (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')"
    },
    {
      "element": "Post-Processing Communication Recipients",
      "customization_type": "Notification Protocol",
      "description": "Specific team members and channels for notifications vary by merchant and phase"
    },
    {
      "element": "Events Processing",
      "customization_type": "Billing Logic",
      "description": "Event-based billing may be required for certain merchants"
    },
    {
      "element": "Special Customer Memos",
      "customization_type": "Customer-Specific Requirements",
      "description": "Certain customers may require specific memo text on invoices"
    },
    {
      "element": "Contract Processing Steps",
      "customization_type": "Operational Workflow",
      "description": "Merchant-specific instructions for processing contracts, including what to ignore"
    },
    {
      "element": "Feature Requests",
      "customization_type": "Product Development",
      "description": "Merchant-specific feature needs with urgency and importance ratings"
    },
    {
      "element": "Company Summary and Goals",
      "customization_type": "Business Context",
      "description": "Understanding of merchant's business, north star goals, and pain points being solved"
    }
  ],
  "confidence_score": 0.92
}
```

---

