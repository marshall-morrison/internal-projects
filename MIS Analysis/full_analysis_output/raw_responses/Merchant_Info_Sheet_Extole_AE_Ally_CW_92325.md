# Raw LLM Analysis: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:11:29

---

## Chunk 1: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:29

### Original Content
```
These invoices will be handled manually by the merchant Contract Processing Steps Steps to process Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Li...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters for contract processing",
    "Integration item labeling and categorization",
    "Post-processing communication workflows",
    "Merchant-specific feature requests and customizations",
    "Invoice handling and tax processing procedures"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed in contract",
      "category": "contract_processing"
    },
    {
      "rule": "Default net payment terms is 0 (net zero) if none specified",
      "category": "contract_processing"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "contract_processing"
    },
    {
      "rule": "Every tax line item becomes a BT (billable transaction) by default",
      "category": "tax_processing"
    },
    {
      "rule": "Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling"
    },
    {
      "rule": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_labeling"
    },
    {
      "rule": "Ops team must notify designated stakeholders upon completion of processing batches",
      "category": "communication"
    },
    {
      "rule": "Notification timing varies by merchant phase (Implementation or Active)",
      "category": "communication"
    },
    {
      "rule": "Cash App transactions should only be processed in main instance to avoid Slack channel clutter",
      "category": "payment_processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Some invoices require manual handling by the merchant",
      "context": "contract_processing"
    },
    {
      "exception": "Contract-specific processing may include back-dating invoice dates to final day of month",
      "context": "invoice_dating"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "context": "integration_labeling"
    },
    {
      "exception": "Separate Tabs instance for Extole's passthrough invoices to maintain invoice consistency",
      "context": "feature_request"
    },
    {
      "exception": "Typical up-charge for separate instance waived for Ally Lombard's early deals",
      "context": "pricing"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationships",
      "context": "customer_specific"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract-specific invoice date back-dating requirements",
      "customizable": true,
      "description": "May differ by contract per merchant request"
    },
    {
      "element": "Integration item labeling conventions",
      "customizable": true,
      "description": "Specific labels for different integration types (Statsig, Pinata, etc.)"
    },
    {
      "element": "Post-processing notification recipients and timing",
      "customizable": true,
      "description": "Varies by merchant - who to notify, where, and when"
    },
    {
      "element": "Customer-specific invoice requirements",
      "customizable": true,
      "description": "Special memos and invoice changes based on merchant-customer relationships"
    },
    {
      "element": "Passthrough invoice handling",
      "customizable": true,
      "description": "Extole example shows need for separate instance management"
    },
    {
      "element": "Events billing processing",
      "customizable": true,
      "description": "Important information varies by merchant if events billing is necessary"
    },
    {
      "element": "SFDC data integration requirements",
      "customizable": true,
      "description": "Pulling invoice descriptions and PO numbers from Salesforce"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Rationale**: The document appears to be a template or framework for merchant onboarding instructions, with some specific examples (Extole, Statsig, Pinata, Messari). The structure is clear but the content is somewhat fragmented and incomplete (text cuts off mid-sentence). The core operational defaults and rules are explicit, but some sections reference information not fully provided in this chunk. Confidence is moderate-high due to clear structure but reduced due to incomplete content and context.

---

## Chunk 2: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:39

### Original Content
```
Merchant : Extole Demo date: 8 21 25 Scoping start date: Aug 22, 2025 MSA Signature Date: Sep 23, 2025 Onboarding Kick Off Date: Oct 7, 2025 [If Exists] Opt Out Date: N A Go Live Date: TBC (flexible by EoY) GTM POC: Implementation POC: TBC ERP: Tax Integration: Key people at Merchant CFO: Robert Costanzo (Economic Buyer) Finance Manager: Kelly Nguyen (co- End-User) Kelly once mentioned a colleague, Veronica Corghencea (Moldova-based Accountant), who  handles a lot of the AR Management , but Vero...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract-to-Cash Automation and System Consolidation",
    "Revenue Recognition and Accounting Integration",
    "Accounts Receivable Management and Collections Visibility",
    "Manual Process Elimination and Error Reduction",
    "Billing Model Complexity and Multi-Instance Architecture"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Billing Operations",
      "description": "Manual contract interpretation required: 10-30 contracts per month must be manually read and input into SFDC billing objects",
      "source": "Current pain point - manual invoicing process"
    },
    {
      "rule_id": "R2",
      "category": "Revenue Recognition",
      "description": "Journal entries and accruals must be automated and posted into QuickBooks, including accruals for unbilled revenue",
      "source": "Kelly's operational goals"
    },
    {
      "rule_id": "R3",
      "category": "Billing Model",
      "description": "Three distinct billing types: Implementation fees (initial invoice), Subscription invoices (annual/quarterly/monthly), and Passthrough invoices (gift card/rewards balance top-ups)",
      "source": "Billing model section"
    },
    {
      "rule_id": "R4",
      "category": "Instance Architecture",
      "description": "Passthrough invoices must be handled in a separate Tabs instance to avoid contaminating collections, AR Aging, and revenue recognition data",
      "source": "Billing model - passthrough invoices note"
    },
    {
      "rule_id": "R5",
      "category": "Renewals Management",
      "description": "Must track 50-75 renewals per quarter including amendments to start dates and upsells",
      "source": "Revenue leakage pain points"
    },
    {
      "rule_id": "R6",
      "category": "Cash Forecasting",
      "description": "System must provide visibility into payment terms (net 30 vs 60) and expected payment timing by month for accurate cash forecasting",
      "source": "Rob's pain point on cash forecasting"
    },
    {
      "rule_id": "R7",
      "category": "Collections",
      "description": "Must provide clear reporting on outstanding customer balances to prioritize follow-ups and improve collections",
      "source": "Kelly's collections visibility goal"
    },
    {
      "rule_id": "R8",
      "category": "System Integration",
      "description": "Current workflow: Salesforce → manual interpretation → Salesforce billing objects → export → SaasAnt bulk upload → QuickBooks → invoice generation",
      "source": "Current order-to-cash process"
    },
    {
      "rule_id": "R9",
      "category": "Tool Consolidation",
      "description": "Tabs should replace YayPay (invoice automation), Wise Layer (contract error detection), and consolidate partial tools",
      "source": "Rob's strategic goals"
    },
    {
      "rule_id": "R10",
      "category": "Contract Management",
      "description": "No opt-out clause exists in the agreement",
      "source": "Opt Out Date: N/A"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Passthrough invoices for gift card/rewards balance top-ups are NOT revenue and require separate instance handling",
      "trigger_condition": "When Extole invoices Corporate customers for rewards balance refills",
      "rationale": "To prevent contamination of collections, AR Aging, and revenue recognition metrics"
    },
    {
      "exception_id": "E2",
      "description": "Mid-month contract changes create special complexity for revenue recognition",
      "trigger_condition": "When contract amendments or changes occur mid-month",
      "impact": "Requires special handling in manual revrec process (current pain point)"
    },
    {
      "exception_id": "E3",
      "description": "Revenue leakage incidents where invoices are forgotten (e.g., $20k example)",
      "trigger_condition": "Manual contract tracking failures",
      "impact": "Invoices not generated until months later, causing cash flow and revenue recognition issues"
    },
    {
      "exception_id": "E4",
      "description": "Veronica (Moldova-based Accountant) handles AR Management but was not involved in the Tabs procurement process",
      "trigger_condition": "Implementation and training phases",
      "impact": "May require additional stakeholder engagement during onboarding"
    }
  ],
  "merchant_specific": [
    {
      "element": "Business Model",
      "description": "Enterprise referral SaaS platform with B2B customers (fintechs, consumer apps, health brands)",
      "customization_need": "Industry-specific terminology and campaign types (refer-a-friend, drop-a-hint)"
    },
    {
      "element": "Passthrough Billing",
      "description": "Unique rewards/gift card balance top-up invoicing model for Corporate customers",
      "customization_need": "Separate instance architecture to isolate non-revenue transactions"
    },
    {
      "element": "ERP System",
      "description": "QuickBooks Online (QBO) as primary accounting system",
      "customization_need": "Integration requirements specific to QBO API and journal entry posting"
    },
    {
      "element": "Current Tech Stack",
      "description": "Salesforce (CRM/billing objects), YayPay (invoice automation), Wise Layer (contract error detection), SaasAnt (bulk upload tool)",
      "customization_need": "Migration and replacement strategy for existing tools"
    },
    {
      "element": "Payment Methods",
      "description": "ACH, check, and credit card payments accepted",
      "customization_need": "Payment reconciliation workflows for multiple payment types"
    },
    {
      "element": "Contract Volume",
      "description": "10-30 new contracts per month, 50-75 renewals per quarter",
      "customization_need": "Scalability requirements for contract ingestion automation"
    },
    {
      "element": "Stakeholder Structure",
      "description": "CFO (Economic Buyer), Finance Manager (End-User), Moldova-based AR Manager (not involved in procurement)",
      "customization_need": "Multi-role access and permissions, potential international user considerations"
    },
    {
      "element": "Timeline Flexibility",
      "description": "Go Live Date: TBC (flexible by end of year)",
      "customization_need": "Implementation timeline can be adjusted based on merchant readiness"
    },
    {
      "element": "Subscription Billing Frequency",
      "description": "Annual, quarterly, or monthly SaaS platform fee options",
      "customization_need": "Flexible billing cadence configuration"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:42

### Original Content
```
22:  If it isn't explicitly on the contract, the easiest way is to use a custom field in SFDC and match it to a custom field in Tabs This takes  2 minutes to set up FR 3 Invoice descriptions "have a typical format that we like to go and follow" Our email response to Rob Kelly on 9 22:  We can easily standardize the language included on the billing items on the invoice to ensure they include details around invoicing frequency If there are other custom fields that you want on invoice that are stan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Custom field configuration and SFDC integration",
    "Invoice formatting and standardization requirements",
    "Implementation and billing structure",
    "Technical scoping and integration capabilities",
    "Passthrough invoicing for gift card/rewards balance management"
  ],
  "rules": [
    "Custom fields in SFDC must be matched to custom fields in Tabs for integration",
    "Custom field setup takes approximately 2 minutes to configure",
    "Invoice descriptions must follow a typical standardized format",
    "Billing item language on invoices should be standardized to include invoicing frequency details",
    "Standard custom fields (required across all customers) should be set up during implementation",
    "Implementation fees are billed as a separate line item on the initial invoice",
    "Subscription invoices can be issued on annual, quarterly, or monthly basis for SaaS platform fees",
    "Passthrough invoices are triggered when gift card/rewards balance drops below a specified threshold",
    "When balance drops below threshold (e.g., $1,000), a top-up invoice is generated"
  ],
  "exceptions": [
    "If contract terms are not explicitly stated, custom field matching provides an alternative solution",
    "Passthrough invoicing applies specifically to Corporate customers for gift card balance management",
    "Balance threshold for triggering invoices is configurable (example given: $1,000)",
    "Invoice frequency can vary by customer: annual, quarterly, or monthly options available"
  ],
  "merchant_specific": [
    "Merchant name: Extole",
    "Specific use case: Gift card and rewards balance management for Corporate customers",
    "Custom threshold amounts for balance alerts (merchant-defined)",
    "Invoice description format preferences (merchant-specific 'typical format')",
    "Billing frequency preferences (annual/quarterly/monthly selection)",
    "Custom fields required on invoices vary by merchant needs",
    "Integration with Salesforce (SFDC) and QuickBooks Online (QBO)",
    "Whitelabeling requirements for invoice email domain",
    "API endpoint configurations",
    "Journal Entry (JE) generation requirements in QBO"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:50

### Original Content
```
g ,  20,000), then Extole immediately pays their rewards provider Note: this is NOT revenue and therefore will be handled in a separate Tabs instance so as not to muddy collections, A R Aging, revrec, etc These invoices will be handled manually by the merchant Is there any important merchant relationship information 1) What is the merchant temperament Very technically competent finance team; Rob has historically built a ton of automations across their prev patchwork of systems We review API docs...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Rewards payment processing and financial handling",
    "Merchant relationship management and stakeholder engagement",
    "Technical competency and system integration capabilities",
    "Product innovation and AI-driven functionality expectations",
    "Financial operations infrastructure and automation"
  ],
  "rules": [
    "Rewards payments (e.g., $20,000 to rewards provider) must be handled in a separate Tabs instance",
    "Rewards-related invoices must NOT be treated as revenue",
    "Rewards invoices must be kept separate from collections, AR Aging, and revenue recognition processes",
    "Rewards-related invoices will be handled manually by the merchant",
    "Contract terms must be manually entered into SFDC by designated personnel",
    "API documentation reviews are conducted directly with technical stakeholders"
  ],
  "exceptions": [
    "Rewards provider payments are processed immediately by Extole but require special financial treatment (non-revenue classification)",
    "Despite general automation capabilities, rewards invoices specifically require manual merchant handling",
    "Both CFO and Finance Manager jointly manage SFDC data entry despite typical hierarchical delegation"
  ],
  "merchant_specific": [
    "Merchant has a highly technically competent finance team",
    "Key stakeholders: Rob (CFO) and Kelly (Finance Manager) who attend calls together",
    "Rob is decision-maker but consults Kelly on product functionality",
    "Both Rob and Kelly are SFDC power-users",
    "Merchant has historically built extensive automations across previous systems",
    "Merchant has strong interest in AI capabilities and querying functionality",
    "Merchant views Tabs as foundational FinOps infrastructure (sticky product positioning)",
    "Merchant uses Extole as their rewards provider",
    "Collaborative decision-making culture between CFO and Finance Manager"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: Merchant Info Sheet - Extole (AE- Ally) - CW 9.23.25_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:52

### Original Content
```
g what's the AR concentration of my top client; how do different customer segments differ in likelihood of churn  Kelly always joins video off What are the Tabs features that the key POC cares about values Tabs ensuring invoices are correct on the first pass, syncing properly to QuickBooks [their biggest pain is contract ingestion and managing renewals   mid-cycle changes, which is 100  manual today] Rob wants to ensure data captured in Tabs (contract components, revenue schedules) can flow back...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer data analytics and segmentation (AR concentration, churn likelihood)",
    "Contract management and automation (ingestion, renewals, mid-cycle changes)",
    "System integration and data synchronization (Tabs-QuickBooks-Salesforce)",
    "Revenue recognition and billing tracking (unbilled revenue, accruals)",
    "Implementation strategy and configuration (all-at-once vs piecemeal rollout)"
  ],
  "rules": [
    "Invoices must be correct on the first pass",
    "Tabs must sync properly to QuickBooks",
    "Contract data (components, revenue schedules) must flow back into Salesforce via APIs",
    "System must track what hasn't been billed yet for revenue accrual purposes",
    "Implementation should be all-at-once rather than piecemeal",
    "Separate platform instance required for passthrough invoices",
    "Custom automations can be built via API endpoints to pull fields relevant for other functions"
  ],
  "exceptions": [
    "Rob will likely build custom automations via endpoints beyond standard Tabs sync capabilities",
    "Separate platform instance needed specifically for passthrough invoices (non-standard setup)",
    "Kelly always joins video off (operational exception for meetings)"
  ],
  "merchant_specific": [
    "QuickBooks as the accounting system of choice",
    "Salesforce as the CRM system",
    "Extole-specific functions requiring custom field pulls",
    "Contract ingestion and managing renewals with mid-cycle changes identified as biggest pain point (100% manual currently)",
    "Key stakeholders: Kelly (POC), Rob (technical/integration lead)",
    "Specific use cases: AR concentration analysis, customer segment churn analysis",
    "Tabs platform as the contract/revenue management solution"
  ],
  "confidence_score": 0.85
}
```

---

