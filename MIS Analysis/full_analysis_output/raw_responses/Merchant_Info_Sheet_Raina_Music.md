# Raw LLM Analysis: Merchant Info Sheet - Raina Music

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 10:14:12

---

## Chunk 1: Merchant Info Sheet - Raina Music_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:14:12

### Original Content
```
Checks will be important for them Provides direct integration with QuickBooks for seamless reconciliation Will want to set up an API eventually with Zapier to trigger when a customer has been onboarded to their business (not pressing) They know they will not need Zapier anymore to create clients in Stripe Future State: A flow where we can shut off service for customers that are ridiculous late on payments (1 - 2 customers a year get shut off so does not happen a lot, no big expectations but woul...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payment and Billing Configuration",
    "System Integration and Automation",
    "Contract Processing and Implementation",
    "Service Management and Customer Lifecycle",
    "Pricing Structure and Fee Calculation"
  ],
  "rules": [
    {
      "category": "Billing Timing",
      "rule": "Client will be invoiced on the 1st of each month for the upcoming month's service fees",
      "source": "explicit"
    },
    {
      "category": "Billing Start Date",
      "rule": "If contract specifies billing at beginning of month, use the first of the effective date month; otherwise use the effective date",
      "source": "explicit"
    },
    {
      "category": "Service Start Date",
      "rule": "Service Start Date is the same as Billing Start Date",
      "source": "explicit"
    },
    {
      "category": "Contract Duration",
      "rule": "Default contract term is 12 months of service",
      "source": "explicit"
    },
    {
      "category": "One-time Fees",
      "rule": "Use 0 months for one-time fees (e.g., Initial Programming Fees, Hardware Costs)",
      "source": "explicit"
    },
    {
      "category": "Price Calculation - Monthly",
      "rule": "For monthly subscriptions, calculate total price as monthly fee × number of zones if applicable",
      "source": "explicit"
    },
    {
      "category": "Price Calculation - Annual",
      "rule": "For annual contracts, use the total annual price stated, or sum monthly fees × 12 months if needed",
      "source": "explicit"
    },
    {
      "category": "Billing Frequency",
      "rule": "Use 'Monthly' for recurring services, 'Year' for annual fees, 'None' for one-time fees",
      "source": "explicit"
    },
    {
      "category": "Contract Location",
      "rule": "Billing terms (BTs) are typically found in the Statement of Work (SOW) section of each contract",
      "source": "explicit"
    },
    {
      "category": "Integration Requirements",
      "rule": "Must provide direct integration with QuickBooks for seamless reconciliation",
      "source": "explicit"
    },
    {
      "category": "Payment Methods",
      "rule": "Checks will be important payment method for this merchant",
      "source": "explicit"
    }
  ],
  "exceptions": [
    {
      "condition": "Contract specifies billing at beginning of month",
      "action": "Use the first of the effective date month instead of exact effective date"
    },
    {
      "condition": "One-time fees (Initial Programming Fees, Hardware Costs)",
      "action": "Set months of service to 0 and frequency to 'None'"
    },
    {
      "condition": "Customers ridiculously late on payments (1-2 per year)",
      "action": "Service shutoff capability desired for future state, but not currently pressing"
    },
    {
      "condition": "Zone-based pricing",
      "action": "Calculate total price by multiplying monthly fee by number of zones"
    }
  ],
  "merchant_specific": [
    {
      "element": "Zone-based billing",
      "description": "Merchant bills based on number of zones selected under SOW",
      "customization_needed": true
    },
    {
      "element": "QuickBooks integration",
      "description": "Direct integration required for this merchant's reconciliation process",
      "customization_needed": true
    },
    {
      "element": "Check payment importance",
      "description": "Checks are specifically important for this merchant",
      "customization_needed": true
    },
    {
      "element": "Future API/Zapier integration",
      "description": "Merchant wants API setup with Zapier to trigger on customer onboarding (not pressing)",
      "customization_needed": true
    },
    {
      "element": "Service shutoff workflow",
      "description": "Future state capability for shutting off service for late payments (rare occurrence: 1-2 customers/year)",
      "customization_needed": true
    },
    {
      "element": "Monthly advance billing",
      "description": "Invoicing on 1st of month for upcoming month's services",
      "customization_needed": false
    },
    {
      "element": "Contract processing responsibility",
      "description": "Implementation Success team fills in contract processing steps; AE and Implementation fill billing model",
      "customization_needed": false
    },
    {
      "element": "No opt-out clause",
      "description": "This merchant does not have an opt-out clause in their contract",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Raina Music_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:14:14

### Original Content
```
Merchant: Raina Music Demo date: April 9, 2025 Scoping start date: n a MSA Signature Date: April 18, 2025 Onboarding Kick Off Date: Apr 24, 2025 [If Exists] Opt Out Date: none Go Live Date: May 19, 2025 (told him 2 - 3 week timeline) GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Director of Operations: Saagar Chandiramani (Admin Champion) CEO: Vikas Sapra (EB) Admin assistant: Was not met in the process, reports to Saagar Company summary (AE to fill) Summary of what c...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payment Reconciliation Complexity",
    "Manual Process Automation",
    "Multi-Entity Billing Management",
    "Subscription and Contract Management",
    "Payment Method Diversification and Tracking"
  ],
  "rules": [
    {
      "rule": "Implementation timeline expectation is 2-3 weeks from MSA signature to Go Live",
      "source": "Timeline from April 18 MSA to May 19 Go Live"
    },
    {
      "rule": "Admin Champion and Executive Buyer roles must be identified during onboarding",
      "source": "Key people identification with specific role assignments"
    },
    {
      "rule": "Multiple payment terms must be supported (Net 30, Net 60, varying schedules)",
      "source": "Everyone pays on a different schedule tracking requirement"
    },
    {
      "rule": "Check payment processing requires: image capture, check number recording, reconciliation with payment processor, payment marking, and reminder suppression",
      "source": "Check payment workflow details"
    },
    {
      "rule": "System must support multiple payment methods: ACH Debit, Credit Card, and Check",
      "source": "Payment method enumeration"
    },
    {
      "rule": "Contract ingestion should use AI automation to create error-free invoices from DocuSign contracts",
      "source": "Why Tabs - automated contract ingestion feature"
    },
    {
      "rule": "Platform must handle complete order-to-cash process including invoicing, dunning, and reconciliation",
      "source": "Why Tabs requirements"
    },
    {
      "rule": "New client onboarding volume expectation: 10-15 new clients per month",
      "source": "Manual process time calculation"
    },
    {
      "rule": "Subscription setup per client should take no more than 5 minutes (target efficiency)",
      "source": "Current manual process takes 5 minutes per client"
    }
  ],
  "exceptions": [
    {
      "exception": "Clients with multiple entities (separate LLCs) require special reconciliation handling across different accounts",
      "condition": "When client has multiple legal entities"
    },
    {
      "exception": "Clients with multiple venues may have different billing entities that need to pay to different ACH accounts",
      "condition": "Multi-venue clients with separate billing entities"
    },
    {
      "exception": "Stripe limitation: only allows one vendor per system even when clients have multiple venues",
      "condition": "Current Stripe implementation constraint"
    },
    {
      "exception": "Client visibility features are not required immediately but will become important in 2026",
      "condition": "Deferred requirement based on timeline"
    },
    {
      "exception": "Auto-pay functionality issues in Stripe lead to missed payments requiring manual intervention",
      "condition": "When auto-pay fails or is unreliable"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company profile",
      "details": "Raina Music - B2B music service for hospitality brands (Kimpton, Tower Group)",
      "customization_needed": true
    },
    {
      "element": "Revenue metrics",
      "details": "~$45k MRR, ~$500k ARR",
      "customization_needed": true
    },
    {
      "element": "Key personnel",
      "details": "Saagar Chandiramani (Director of Operations/Admin Champion), Vikas Sapra (CEO/EB)",
      "customization_needed": true
    },
    {
      "element": "Business model",
      "details": "Subscription-based with licensed DJ mixes, playlists, and physical hardware players",
      "customization_needed": true
    },
    {
      "element": "Client dashboard integration",
      "details": "Recently built client dashboard integrating music management, billing, and customer support",
      "customization_needed": true
    },
    {
      "element": "Current payment processor",
      "details": "Stripe (with migration to Tabs planned)",
      "customization_needed": true
    },
    {
      "element": "Integration approach",
      "details": "Currently using Zapier due to Stripe API complexity and lack of engineering resources",
      "customization_needed": true
    },
    {
      "element": "Contract management",
      "details": "Uses DocuSign for contracts",
      "customization_needed": false
    },
    {
      "element": "Primary pain points",
      "details": "Delinquent payment follow-ups, check reconciliation, subscription setup, multi-entity billing complexity",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Raina Music_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:14:24

### Original Content
```
: who is the buyer decision maker ) Director of Operations: Saagar Chandiramani (Admin Champion) CEO: Vikas Sapra (EB) What are the Tabs features that the key POC cares about Better managing follow-ups for delinquent payments Improving check reconciliation Streamlining subscription setup Setting up infrastructure for reporting down the road
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder identification and role mapping",
    "Payment management and collections",
    "Financial reconciliation processes",
    "Subscription and recurring payment infrastructure",
    "Reporting and analytics capabilities"
  ],
  "rules": [
    "Director of Operations serves as the Admin Champion role",
    "CEO serves as the Executive Buyer (EB) role",
    "Key decision maker must be identified for buyer role",
    "Follow-up processes must be established for delinquent payments",
    "Check reconciliation procedures must be implemented",
    "Subscription setup must be streamlined",
    "Reporting infrastructure must be established for future use"
  ],
  "exceptions": [
    "The buyer decision maker role is explicitly noted as unclear or to-be-determined (indicated by the incomplete statement)",
    "Reporting infrastructure is noted as 'down the road' suggesting phased implementation rather than immediate requirement"
  ],
  "merchant_specific": [
    "Specific personnel names: Saagar Chandiramani (Director of Operations), Vikas Sapra (CEO)",
    "Role titles may vary by organization (Director of Operations, CEO)",
    "The term 'Admin Champion' appears to be organization or platform-specific terminology",
    "The term 'EB' (Executive Buyer) may be internal sales/implementation terminology",
    "Priority features (delinquent payments, check reconciliation, subscriptions) indicate merchant's specific business model and pain points",
    "Use of checks suggests specific payment methods relevant to this merchant"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Raina Music_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:14:31

### Original Content
```
Net Terms: Default to 30 Usage BTs note: Any line item that is  per  an event will be usage Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, O...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and billing configurations",
    "Contract processing and invoice management procedures",
    "Integration and labeling requirements for third-party services",
    "Communication protocols and stakeholder notifications",
    "Merchant relationship management and customer-specific handling"
  ],
  "rules": [
    {
      "rule": "Default net payment terms are 30 days",
      "category": "billing"
    },
    {
      "rule": "Line items marked as 'per event' should be classified as usage-based billing types",
      "category": "billing_classification"
    },
    {
      "rule": "Default service term is 1 year if not specified in contract",
      "category": "contract_defaults"
    },
    {
      "rule": "Default net payment terms are 0 days if not specified",
      "category": "payment_terms"
    },
    {
      "rule": "Default billing frequency is monthly if not specified",
      "category": "billing_frequency"
    },
    {
      "rule": "Every tax line item becomes a billing type (BT) by default",
      "category": "tax_handling"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_labeling"
    },
    {
      "rule": "Customer Success (Azmat Aziz) needs to be notified in Messari internal merchant channel when contracts are processed in Active phase",
      "category": "post_processing_communication"
    },
    {
      "rule": "Invoices are currently generated through Stripe",
      "category": "invoice_generation"
    },
    {
      "rule": "Payments are reconciled with QuickBooks through accountant",
      "category": "payment_reconciliation"
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing may differ (e.g., back-dating invoice date to final day of month)",
      "context": "Merchant-requested specifics that override defaults"
    },
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "context": "Integration labeling override"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "context": "Customer-specific invoice handling"
    },
    {
      "exception": "Invoice changes may be needed due to specific merchant-customer relationships",
      "context": "Customer relationship management"
    },
    {
      "exception": "Service shut-off for late payments is rare (1-2 customers per year)",
      "context": "Collections and overdue payment handling"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration labeling rules",
      "description": "Statsig and Pinata have specific labeling requirements that may vary by merchant",
      "customizable": true
    },
    {
      "element": "Post-processing notification recipients",
      "description": "Specific team members (e.g., Azmat Aziz) and channels need to be identified per merchant",
      "customizable": true
    },
    {
      "element": "Invoice back-dating preferences",
      "description": "Some merchants may request specific invoice date handling",
      "customizable": true
    },
    {
      "element": "Customer-specific memos and invoice modifications",
      "description": "Special handling based on individual customer relationships",
      "customizable": true
    },
    {
      "element": "Merchant temperament and POC information",
      "description": "Saagar (day-to-day admin, very nice) and Vikas (rambler, hands-off after initial call)",
      "customizable": true
    },
    {
      "element": "Current billing workflow",
      "description": "Manual subscription setup after onboarding, Stripe invoice generation, manual overdue payment handling",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "description": "API integration with Zapier for onboarding triggers, future service shut-off automation",
      "customizable": true
    },
    {
      "element": "Merchant relationship type",
      "description": "Inbound merchant with no personal relationships",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

