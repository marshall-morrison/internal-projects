# Raw LLM Analysis: Hockeystack MIS

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 12:06:03

---

## Chunk 1: Hockeystack MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:06:03

### Original Content
```
app gong io call id 153932604884814192 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills: Tech Stack: QBO as ERP now They are thinking of moving to Campfire in the next 3-6 months, but we have warned them that that would seriously affect their experience on Tabs Partnerships team will maintain monthly conversations with Russ and GFT to postpone this move until we are integrated with Campfire Implementation team should strive for t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Invoicing Process",
    "Technology Stack and System Integration",
    "Payment Methods and Processing",
    "Revenue Recognition and Financial Reporting",
    "Manual Process Automation Needs"
  ],
  "rules": [
    {
      "rule": "ACH is the only accepted payment method currently",
      "category": "payment_processing",
      "explicit": true
    },
    {
      "rule": "No credit card payments are currently processed through Stripe",
      "category": "payment_processing",
      "explicit": true
    },
    {
      "rule": "Stripe charges 0.5% of revenue per invoice",
      "category": "cost_structure",
      "explicit": true
    },
    {
      "rule": "Invoices must be sent manually and individually",
      "category": "invoicing_process",
      "explicit": true
    },
    {
      "rule": "Manual follow-ups required for payment collection",
      "category": "collections_process",
      "explicit": true
    },
    {
      "rule": "QBO serves as the current ERP system",
      "category": "technology_stack",
      "explicit": true
    },
    {
      "rule": "Salesforce is used as reference for invoice creation",
      "category": "technology_stack",
      "explicit": true
    },
    {
      "rule": "No automation exists for invoice scheduling or status tracking",
      "category": "invoicing_process",
      "explicit": true
    },
    {
      "rule": "System must support document attachment (W9s, bank info)",
      "category": "documentation_requirements",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Potential future migration from QBO to Campfire ERP within 3-6 months",
      "impact": "Would seriously affect experience on Tabs platform",
      "mitigation": "Partnerships team to maintain monthly conversations to postpone move until Campfire integration is complete"
    },
    {
      "exception": "May explore Ramp for credit card acceptance in the future",
      "impact": "Would expand payment methods beyond current ACH-only policy",
      "condition": "Future consideration, not current requirement"
    }
  ],
  "merchant_specific": [
    {
      "element": "Hockeystack company name",
      "type": "merchant_identity",
      "customizable": true
    },
    {
      "element": "HR person as previous invoice handler",
      "type": "role_assignment",
      "customizable": true
    },
    {
      "element": "Russ and GFT as key stakeholders",
      "type": "contact_persons",
      "customizable": true
    },
    {
      "element": "Campfire ERP as migration target",
      "type": "technology_preference",
      "customizable": true
    },
    {
      "element": "3-6 month timeline for ERP migration",
      "type": "timeline",
      "customizable": true
    },
    {
      "element": "Visibility needs for deferred revenue and NDR",
      "type": "reporting_requirements",
      "customizable": true
    },
    {
      "element": "ACH-only payment preference",
      "type": "payment_policy",
      "customizable": true
    },
    {
      "element": "0.5% Stripe fee avoidance goal",
      "type": "cost_optimization",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Hockeystack MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:06:05

### Original Content
```
Merchant Name: Hockeystack Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Just add the amount the customer needs to pay: don't need to add the or...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Setup",
    "Billing Configuration and Defaults",
    "Merchant-Specific Implementation Requirements",
    "Post-Processing Communication Protocols",
    "Customer and Invoice Management"
  ],
  "rules": [
    {
      "rule": "Invoice amounts should show final amount only, not original amount with discount applied separately",
      "example": "Should say 27,600 for AI21 Labs, not show discount breakdown"
    },
    {
      "rule": "Contract start date determination: Use later date of two signatures when effective date not explicitly listed",
      "context": "Applies to older contracts; newer contracts will explicitly state effective date"
    },
    {
      "rule": "Billing address and email must be included in contract processing",
      "example": "Referenced in Alvys example"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "type": "ops_default"
    },
    {
      "rule": "Default Net Payment Terms: 0 days (if none listed)",
      "type": "ops_default"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "type": "ops_default"
    },
    {
      "rule": "Tax handling: Every tax line item becomes a BT (if none listed)",
      "type": "ops_default"
    },
    {
      "rule": "Integration items for Statsig should be labeled as 'Sales'",
      "type": "merchant_specific"
    },
    {
      "rule": "Integration items for Pinata should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "type": "merchant_specific"
    }
  ],
  "exceptions": [
    {
      "exception": "Old contracts without explicit effective dates require special date calculation logic",
      "handling": "Use later of two signature dates"
    },
    {
      "exception": "Merchant-specific processing requests may differ by contract",
      "example": "Back-dating invoice date to final day of month"
    },
    {
      "exception": "Integration item labeling varies by merchant",
      "examples": ["Statsig uses 'Sales'", "Pinata uses 'Software Subscription Bundle' with possible overrides"]
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "context": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model configuration",
      "customization": "Implementation team fills this section per merchant"
    },
    {
      "element": "Customer creation process",
      "customization": "May have unique aspects per merchant"
    },
    {
      "element": "Contract structure and breakdown",
      "customization": "Varies by merchant"
    },
    {
      "element": "Post-processing notification requirements",
      "customization": "Specific team members, channels, and timing vary by merchant",
      "example": "Messari: Notify Azmat Aziz in internal channel when contracts processed in Active phase"
    },
    {
      "element": "Integration item labeling conventions",
      "customization": "Different labels for different merchants (Statsig, Pinata, etc.)"
    },
    {
      "element": "Items to ignore in contracts",
      "customization": "Merchant-specific exclusions"
    },
    {
      "element": "Events billing processing",
      "customization": "Only necessary for certain merchants"
    },
    {
      "element": "Customer-specific invoice requirements",
      "customization": "Special memos, invoice changes based on relationships"
    },
    {
      "element": "POC assignments",
      "fields": ["Implementation POC", "CX POC"],
      "responsibility": "To be filled by respective teams"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Hockeystack MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:06:14

### Original Content
```
The previous offshore accounting firm left things  all over the place Manual journal entries are used for revenue recognition 1) What is the merchant temperament Russ is great, super friendly and very professional Cares a lot about building out this new finance tech stack the right way 3) What are the Tabs features that the key POC cares about Loved that Tabs: Ingests contracts automatically from Salesforce Builds invoice schedules instantly Sends invoices on a set date Automates follow-ups (dun...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Automation and elimination of manual processes in revenue operations",
    "Revenue recognition and deferred revenue accounting compliance",
    "Net Dollar Retention (NDR) tracking and analytics as key business metric",
    "Integration capabilities across finance tech stack (Salesforce, QuickBooks, Plaid, Omni)",
    "Tool reliability and maturity requirements based on past negative experiences"
  ],
  "rules": [
    "Manual journal entries must be used for revenue recognition (current state requirement)",
    "Invoices must be sent on predetermined set dates",
    "ACH payments must be reconciled via Plaid integration",
    "Invoice and payment data must sync to QuickBooks",
    "Deferred revenue schedules must be auto-generated and exported to QuickBooks",
    "System must provide visibility into monthly revenue recognition by customer for journal entries and compliance",
    "Contract data must be automatically ingested from Salesforce",
    "Invoice schedules must be built automatically from contract data",
    "Automated follow-ups (dunning) must be implemented for collections",
    "NDR tracking must support customizable cohorts and data slicing capabilities",
    "Tool must demonstrate reliability and maturity (not buggy/early-stage)"
  ],
  "exceptions": [
    "ARR growth is not the primary focus metric - NDR growth is the north star metric instead",
    "Advanced reporting through Omni integration is considered 'icing on the cake' (nice-to-have rather than core requirement)",
    "Previous offshore accounting firm's disorganized approach created need for structured automation"
  ],
  "merchant_specific": [
    "Merchant name: Hockeystack",
    "Key contact: Russ/Russel (described as friendly, professional, detail-oriented)",
    "Company-specific metric priority: NDR growth as north star metric over ARR growth",
    "Current pain point: Previous offshore accounting firm left disorganized processes",
    "Specific tech stack: Salesforce (CRM), QuickBooks (accounting), Plaid (payment reconciliation), Omni (reporting/analytics)",
    "Team structure concern: Reducing headcount burden on revenue accountants",
    "Historical context: Has been burned by buggy early-stage tools previously"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: Hockeystack MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:06:19

### Original Content
```
Cares deeply about not being a  beta tester  and wants confidence that Tabs is stable and reliable Expressed the importance of strong support and is reassured by: Dedicated implementation specialist Premier support with CTO, Head of Product, and CSM Slack channel integration for support Clear ROI Sees clear ROI in reducing Days Sales Outstanding (DSO), which improves cash flow and reduces manual labor
```

### LLM Analysis Response
```json
{
  "themes": [
    "Product Stability and Reliability Concerns",
    "Support Infrastructure and Accessibility",
    "Financial Impact and Return on Investment",
    "Implementation and Onboarding Process",
    "Risk Mitigation for Early Adoption"
  ],
  "rules": [
    {
      "rule": "Must provide evidence of product stability and maturity (not beta status)",
      "type": "explicit",
      "category": "product_requirements"
    },
    {
      "rule": "Must offer dedicated implementation specialist during onboarding",
      "type": "explicit",
      "category": "support_requirements"
    },
    {
      "rule": "Must provide premier/executive-level support access (CTO, Head of Product, CSM)",
      "type": "explicit",
      "category": "support_requirements"
    },
    {
      "rule": "Must integrate Slack channel for support communications",
      "type": "explicit",
      "category": "support_requirements"
    },
    {
      "rule": "Must demonstrate clear ROI metrics, specifically around DSO reduction",
      "type": "explicit",
      "category": "business_case"
    },
    {
      "rule": "Solution should reduce manual labor in financial operations",
      "type": "implicit",
      "category": "operational_efficiency"
    },
    {
      "rule": "Solution should improve cash flow through faster collections",
      "type": "implicit",
      "category": "financial_impact"
    }
  ],
  "exceptions": [
    {
      "condition": "High-touch support model may only apply to enterprise or premium tier customers",
      "note": "Access to C-level executives typically reserved for strategic accounts"
    },
    {
      "condition": "Dedicated implementation specialist may be time-limited or tier-dependent",
      "note": "Not specified if this is permanent or only during onboarding phase"
    }
  ],
  "merchant_specific": [
    {
      "element": "Days Sales Outstanding (DSO) metrics",
      "customization_needed": "Baseline DSO and target reduction percentage will vary by merchant",
      "note": "Each merchant will have different current DSO and improvement goals"
    },
    {
      "element": "Manual labor reduction quantification",
      "customization_needed": "Current manual processes and FTE hours will differ per merchant",
      "note": "ROI calculation needs merchant-specific baseline data"
    },
    {
      "element": "Support channel preferences",
      "customization_needed": "While Slack is mentioned, some merchants may prefer other communication platforms",
      "note": "Integration requirements may vary by merchant's existing tech stack"
    },
    {
      "element": "Definition of 'stable and reliable'",
      "customization_needed": "Risk tolerance and stability requirements vary by merchant size and industry",
      "note": "Enterprise merchants may have stricter uptime and reliability SLAs"
    }
  ],
  "confidence_score": 0.85
}
```

---

