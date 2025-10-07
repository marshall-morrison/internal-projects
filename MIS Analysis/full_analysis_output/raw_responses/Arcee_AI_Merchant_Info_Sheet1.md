# Raw LLM Analysis: Arcee AI - Merchant Info Sheet(1)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:49:42

---

## Chunk 1: Arcee AI - Merchant Info Sheet(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:49:42

### Original Content
```
Arcee AI Demo date: Nov 1, 2024 Scoping start date: Nov 4, 2024 MSA Signature Date: Nov 4, 2024 Onboarding Kick Off Date: [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Mark McQuade (mark arcee ai) Fractional Controller: Ted _____ (ted neweconomycpa com) Chief of Staff   Billing: Molly Niland (molly arcee ai) Revenue Ops: Amber _____ (amber arcee ai) Business Operations: Mohit Khullar (mohit arcee ai) Company summary Platfor...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Identification and Contact Management",
    "Business Goals and Pain Points",
    "Revenue Operations and Financial Reporting",
    "Merchant Relationship Context"
  ],
  "rules": [
    "Demo must occur before scoping start date",
    "MSA signature should be obtained before or concurrent with scoping",
    "Onboarding kick-off follows MSA signature",
    "Key stakeholder roles must be identified: CEO, Controller, Chief of Staff/Billing, Revenue Ops, Business Operations",
    "GTM POC and Implementation POC must be assigned",
    "ERP and Tax Integration systems must be documented",
    "Company summary describing business model is required",
    "North star goals must be clearly defined and documented",
    "Primary pain points must be identified and recorded",
    "ARR and Revenue Recognition reporting requirements must be captured",
    "Opt-out clause status must be documented",
    "AE relationship notes should be maintained"
  ],
  "exceptions": [
    "Opt Out Date field can be left blank if no opt-out clause exists (as in this case: 'No opt out clause')",
    "Go Live Date may be pending/unknown during initial documentation",
    "Onboarding Kick Off Date may not be set at time of MSA signature",
    "Some contact information may be incomplete (last names, partial email domains) during initial capture"
  ],
  "merchant_specific": [
    "Company business model description (SLMs/AI platform vs other industries)",
    "Specific pain points (ballooning AR, manual invoicing/dunning vs other operational issues)",
    "Valued features (time to invoice, collections view, cash forecasting)",
    "Funding stage and timeline (Series B in 1Q25)",
    "Organizational structure and key personnel titles",
    "ERP system type",
    "Tax integration requirements",
    "Merchant temperament assessment methodology"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Arcee AI - Merchant Info Sheet(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:49:52

### Original Content
```
CEO is the decision maker He seemed frustrated with the previous invoicing process, but was very friendly and approachable He moves fast and has a technical background (former CTO) 2) Is there key POC the buyer decision maker Mark is the decision maker who gave the final thumbs up He had us do a second demo with his team to get their sign-off ahead of time Ted is the fractional controller who will be a power user, along with Molly who has been managing billing thus far 3) What are the Tabs featu...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Decision-Making Hierarchy",
    "Contract Processing and Revenue Schedule Creation",
    "Billing Model Configuration and Payment Terms",
    "Product Features and Customer Requirements",
    "Operational Defaults and Processing Standards"
  ],
  "rules": [
    {
      "rule": "CEO/Mark is the final decision maker for approvals",
      "category": "stakeholder_management",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Ted (fractional controller) and Molly are designated power users",
      "category": "stakeholder_management",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Create a separate revenue schedule for each payment listed in the contract",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Service Start Date should be taken from 'agreement date' field in contract",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Months of Service equals the length of contract",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Item Name should match the payment name from contract (e.g., 'Phase 1- 1st Payment')",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Total price should be taken from contract for each phase/payment",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Start Date for revenue schedule should match service start date",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Periods should be set to 1",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Frequency should be set to None",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Net Terms should be extracted from contract next to total price",
      "category": "contract_processing",
      "specificity": "general"
    },
    {
      "rule": "Integration Item should be 'SAAS Revenue'",
      "category": "contract_processing",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Ignore any credits and pricing and invoicing in contracts",
      "category": "contract_processing",
      "specificity": "merchant_specific"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "operational_defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Net Payment Terms is 30 days",
      "category": "operational_defaults",
      "specificity": "general"
    },
    {
      "rule": "Default Billing Frequency should refer to contract",
      "category": "operational_defaults",
      "specificity": "general"
    },
    {
      "rule": "No taxes should be included as line items",
      "category": "tax_handling",
      "specificity": "merchant_specific"
    }
  ],
  "exceptions": [
    {
      "exception": "Some contracts may have milestone payments (previous contracts) while moving towards pure SaaS solution",
      "condition": "Contract type variation",
      "impact": "Different processing approach may be needed for legacy contracts"
    },
    {
      "exception": "Some annual payments are upfront but depends on the client",
      "condition": "Client-specific payment arrangements",
      "impact": "Payment timing varies by client agreement"
    },
    {
      "exception": "Varying payment terms across different contracts",
      "condition": "Contract-specific terms",
      "impact": "Must extract terms from each individual contract"
    },
    {
      "exception": "Specific processing requests that may differ by contract (e.g., back-dating invoice date to final day of month)",
      "condition": "Contract-specific processing requirements",
      "impact": "Custom processing logic may be required per contract"
    },
    {
      "exception": "Two different contract formats requiring different processing steps (milestone-based vs payment schedule-based)",
      "condition": "Contract format variation",
      "impact": "Different workflows based on contract structure"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key stakeholders: Mark (CEO/decision maker), Ted (fractional controller), Molly (billing manager)",
      "type": "personnel",
      "customization_needed": true
    },
    {
      "element": "Product features prioritized: Contract ingest, collections kanban, cash application, dunning emails, revenue reporting",
      "type": "feature_requirements",
      "customization_needed": true
    },
    {
      "element": "Billing model transition: Moving from milestone payments to pure SaaS solution",
      "type": "business_model",
      "customization_needed": true
    },
    {
      "element": "Integration Item designation: 'SAAS Revenue'",
      "type": "system_configuration",
      "customization_needed": true
    },
    {
      "element": "Contract processing references: Screenshot examples and LOOM video recordings for specific contract types (e.g., 'garage contract')",
      "type": "training_materials",
      "customization_needed": true
    },
    {
      "element": "Instruction to ignore credits and pricing specifics in contracts",
      "type": "processing_rule",
      "customization_needed": true
    },
    {
      "element": "No tax handling required",
      "type": "tax_configuration",
      "customization_needed": true
    },
    {
      "element": "Contract-specific back-dating requirements for invoice dates",
      "type": "processing_customization",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Arcee AI - Merchant Info Sheet(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:49:52

### Original Content
```
Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merchant Post Processing Communications (if necessary) Does Ops Team need to notify anyone on the team re: completion of processing batches in Implementation or Active phase Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Item Categorization and Labeling Rules",
    "Team Notification and Communication Protocols",
    "Merchant Processing Workflow and Phases",
    "Customer Success Management",
    "System Integration and Feature Requests"
  ],
  "rules": [
    {
      "rule": "All Statsig integration items must be labeled as 'Sales'",
      "type": "categorization",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless modified by Merchant Post Processing Communications",
      "type": "categorization",
      "explicit": true
    },
    {
      "rule": "Customer Success (specifically Azmat Aziz) must be notified when contracts are processed during Active merchant phase",
      "type": "notification",
      "explicit": true
    },
    {
      "rule": "Notifications should be sent in the Messari internal merchant channel",
      "type": "communication_channel",
      "explicit": true
    },
    {
      "rule": "Ops Team must determine if notification is needed upon completion of processing batches during Implementation or Active phase",
      "type": "workflow",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration labeling can be overridden by Merchant Post Processing Communications",
      "condition": "When specifically noted by Merchant Post Processing Communications",
      "applies_to": "Software Subscription Bundle categorization"
    }
  ],
  "merchant_specific": [
    {
      "element": "Statsig integrations",
      "category": "vendor/integration",
      "customizable": true
    },
    {
      "element": "Pinata integrations",
      "category": "vendor/integration",
      "customizable": true
    },
    {
      "element": "Customer Success contact (Azmat Aziz)",
      "category": "personnel",
      "customizable": true
    },
    {
      "element": "Messari internal merchant channel",
      "category": "communication_channel",
      "customizable": true
    },
    {
      "element": "Merchant phases (Implementation, Active)",
      "category": "workflow_stages",
      "customizable": false
    },
    {
      "element": "Hubspot integration feature request",
      "category": "integration_request",
      "customizable": true,
      "note": "Request to push payment info and past due balances back to Tabs"
    }
  ],
  "confidence_score": 0.85
}
```

---

