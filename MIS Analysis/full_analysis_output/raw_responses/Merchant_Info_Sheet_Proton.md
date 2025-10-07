# Raw LLM Analysis: Merchant Info Sheet - Proton

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 12:18:14

---

## Chunk 1: Merchant Info Sheet - Proton_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:18:14

### Original Content
```
Is there an opt out clause If so, what is the merchant looking for so they do not exercise it No opt out Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant No Information on how merchant bills SaaS seat based billing that maintains a floor of seats - simple in concept but somewhat complex to support: They bill a software fee based on seat count which includes a specific number of seats This number of seats becomes the "floor" ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "SaaS Seat-Based Billing with Dynamic Floor Pricing",
    "Contract Processing and Term Management",
    "Tiered Pricing Structure and Price Breaks",
    "Pro-rated Billing for Mid-Contract Changes",
    "Merchant Billing Model Evolution and Experimentation"
  ],
  "rules": [
    "No opt-out clause exists in the contract",
    "Billing is seat-based with a contractual floor that can only increase, never decrease",
    "Initial seat count establishes the minimum billing floor for the contract term",
    "When seats are added above the floor, the new seat count becomes the permanent new floor",
    "New seats added mid-contract are billed pro-rated for the remaining contract term, paid upfront",
    "Price per seat decreases at specific thresholds: $130/seat/month at 50 seats, $105/seat/month at 75 seats",
    "Service start date equals the effective date specified in the order form",
    "For multi-year contracts, subsequent year service start dates are calculated as effective date + N years",
    "Total months of service must be extracted from the 'initial term' field",
    "One-time payments are indicated by 0 months of service",
    "Renewal contracts without existing customer records should be treated as net new contracts",
    "Contracts specify initial seat purchase as a dollar amount, with separate tiered pricing table for additional seats"
  ],
  "exceptions": [
    "If term length is not specified and not marked as one-time payment, use best judgment to determine service duration",
    "Merchant is planning to revise their billing model and experiment with new pricing models (future state exception)",
    "The billing model is described as 'simple in concept but somewhat complex to support' indicating implementation complexity",
    "Special coordination required with Arjun for supporting this use case",
    "Pre-kickoff meeting needed to discuss implementation details"
  ],
  "merchant_specific": [
    "Reference to specific customer 'BPI' with 45-seat floor example",
    "Specific price break thresholds: 50 seats → $130/seat/month, 75 seats → $105/seat/month",
    "Merchant interested in 'thought partnership on best practices' for pricing models",
    "Merchant-specific contact: Arjun (implementation coordination)",
    "Contract structure: initial purchase amount + tiered pricing table format",
    "Terminology: 'floor' to describe minimum billable seat count",
    "Service start date terminology: uses 'effective date' from order form",
    "Document references 'order form table' as source document for billing terms"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Proton_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:18:18

### Original Content
```
Merchant Demo date: Nov 19, 2024 Scoping start date: Nov 22, 2024 MSA Signature Date: Nov 26, 2024 Onboarding Kick Off Date: Dec 5, 2024 [If Exists] Opt Out Date: Go Live Date: Jan 6, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Yes, but not sure what their provider is (likely AST) Key people at Merchant Main POC: Owen Gallahue - Engagement manager (acting CFO until Wilhelm joins) CFO: Wilhelm Glaser-Gallion - joining as the new CFO over the next few weeks Fiona - Finance at Proton (s...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Business Model and Product Understanding",
    "Pain Points and Solution Requirements",
    "System Integration and Technical Requirements"
  ],
  "rules": [
    {
      "rule": "Demo must occur before scoping start date",
      "evidence": "Demo date: Nov 19, 2024, Scoping start date: Nov 22, 2024",
      "type": "explicit"
    },
    {
      "rule": "MSA signature must be obtained before onboarding kick-off",
      "evidence": "MSA Signature Date: Nov 26, 2024, Onboarding Kick Off Date: Dec 5, 2024",
      "type": "implicit"
    },
    {
      "rule": "Onboarding kick-off should occur before go-live date",
      "evidence": "Onboarding Kick Off Date: Dec 5, 2024, Go Live Date: Jan 6, 2025",
      "type": "explicit"
    },
    {
      "rule": "Tax integration status must be documented during scoping",
      "evidence": "Tax Integration: Yes, but not sure what their provider is (likely AST)",
      "type": "explicit"
    },
    {
      "rule": "Key stakeholders must be identified including Main POC, CFO, and relevant finance/sales personnel",
      "evidence": "Main POC: Owen Gallahue, CFO: Wilhelm Glaser-Gallion, Fiona - Finance, Pete: VP of Sales",
      "type": "explicit"
    },
    {
      "rule": "Company summary must be completed by Account Executive",
      "evidence": "Company summary (AE to fill)",
      "type": "explicit"
    },
    {
      "rule": "Goals and pain points must be documented by AE and Implementation team",
      "evidence": "Goals (North star) (AE Implementation to fill)",
      "type": "explicit"
    },
    {
      "rule": "ERP system must be identified for integration purposes",
      "evidence": "ERP: [field present in document]",
      "type": "implicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date field may not always exist",
      "evidence": "[If Exists] Opt Out Date:",
      "condition": "Conditional field based on merchant circumstances"
    },
    {
      "exception": "CFO may not be present at project start and may join during implementation",
      "evidence": "Wilhelm Glaser-Gallion - joining as the new CFO over the next few weeks",
      "condition": "Leadership transitions during implementation period"
    },
    {
      "exception": "Tax integration provider may be uncertain at scoping stage",
      "evidence": "Yes, but not sure what their provider is (likely AST)",
      "condition": "Integration details may require further discovery"
    },
    {
      "exception": "Acting roles may substitute for permanent positions during transition",
      "evidence": "Owen Gallahue - Engagement manager (acting CFO until Wilhelm joins)",
      "condition": "Temporary role assignments during personnel transitions"
    }
  ],
  "merchant_specific": [
    {
      "element": "Timeline dates",
      "customization_needed": "All milestone dates are merchant-specific",
      "examples": ["Demo date: Nov 19, 2024", "Go Live Date: Jan 6, 2025"]
    },
    {
      "element": "Key personnel names and roles",
      "customization_needed": "Contact information and organizational structure varies by merchant",
      "examples": ["Owen Gallahue", "Wilhelm Glaser-Gallion", "Fiona", "Pete"]
    },
    {
      "element": "Business model description",
      "customization_needed": "Each merchant has unique product offerings and value propositions",
      "examples": ["AI-powered CRM platform tailored for B2B distributors"]
    },
    {
      "element": "Pain points and goals",
      "customization_needed": "Specific challenges and objectives vary by merchant",
      "examples": ["Manual processes in Salesforce", "Revenue Capture Gaps", "Forecasting and MRR visibility"]
    },
    {
      "element": "Integration requirements",
      "customization_needed": "ERP systems and tax providers differ by merchant",
      "examples": ["Tax Integration: Yes, but not sure what their provider is (likely AST)"]
    },
    {
      "element": "Target customer base",
      "customization_needed": "Industry focus and customer segments are merchant-specific",
      "examples": ["mid-to-large-scale distributors across various industries"]
    },
    {
      "element": "Current systems and tools",
      "customization_needed": "Existing technology stack varies by merchant",
      "examples": ["Salesforce", "QuickBooks", "Excel"]
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Proton_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:18:28

### Original Content
```
For example, for professional services fee with fixed quantity, this will likely be billed one time upfront and should be 0 for months of service If multiple years, total months correspond to that period for that BT For example, year 1 and year 2 would each be 12 months unless it is specifically mentioned that the invoice cadence is different For example, if the first 3 years (see below screenshot) are invoiced together, the months of service would correspond and be 36 months Item name will be u...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) identification and processing rules",
    "Service term duration and invoice cadence determination",
    "Multi-year contract handling and payment term interpretation",
    "Renewal contract processing and original contract modification",
    "Items to include vs. exclude from BT processing"
  ],
  "rules": [
    "Professional services fees with fixed quantity are billed once upfront with 0 months of service",
    "Multi-year periods are broken into 12-month increments per year unless invoice cadence specifies otherwise",
    "When multiple years are invoiced together, months of service equals total period (e.g., 3 years = 36 months)",
    "Item names are found under 'Proton Services' or similarly named column",
    "Invoice cadence is determined from Payment Terms section",
    "Billing start date, number of periods, and frequency follow the stated cadence",
    "Net terms are located in Payment Terms section",
    "Take final price only - do not process discounts separately",
    "Renewal contracts are processed under original contract if they modify it",
    "Service start date for renewal BTs is the effective date of the renewal",
    "Mark original contract as processed in garage after processing renewal",
    "When renewal overwrites original contract terms, modify existing BTs and add new ones"
  ],
  "exceptions": [
    "If invoice cadence differs from standard annual (e.g., first 3 years invoiced together), adjust months of service accordingly",
    "If unsure how discount applies to individual BT, escalate to US team",
    "For rare contract formats with only final annual subscription cost and professional services fee, process only those BTs without discounts",
    "Process renewal under renewal contract (not original) only if: (1) no original contract exists, OR (2) renewal doesn't modify original AND dates don't overlap",
    "BTs to exclude: Services Package (hourly rate), Incremental User License Fees, Rate Table (tiered), Workflow Connector Fees, and Discounts",
    "eCommerce fees are excluded if baked into larger annual subscription cost"
  ],
  "merchant_specific": [
    "'Proton Services' column name (may vary by merchant)",
    "'Services Package' terminology for hourly rates",
    "'Payment Terms' section location and format",
    "Specific BT types to ignore: Incremental User License Fees, Workflow Connector Fees, Rate Table",
    "'garage' system reference for marking contracts as processed",
    "Contract structure and format variations",
    "Discount presentation and application methods",
    "Renewal contract language (e.g., 'Supersedes and replaces')"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 4: Merchant Info Sheet - Proton_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:18:37

### Original Content
```
In this case, the renewal overwrites the last 24 months of the original contract, so we have to go into the original contract and delete those BTs The BTs for the first 12 months of the original contract will be left alone Here, we have added the annual payment BTs created by the renewal contract Original for reference Processing upsells What the garage upload will look like LINK Process this without a customer assigned or any BTs What we are doing with this table: Altering the BTs for the relev...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Renewal Processing and Billing Term (BT) Management",
    "Upsell Processing and Invoice Adjustments",
    "Integration Item Mapping and Categorization",
    "Default Operational Parameters and Configuration",
    "Merchant-Specific Processing Instructions and Communications"
  ],
  "rules": [
    {
      "rule": "Contract renewals overwrite the last 24 months of the original contract",
      "context": "Renewal processing requires deletion of BTs for the last 24 months while preserving the first 12 months"
    },
    {
      "rule": "Upsell processing requires two actions: (1) Create one-time invoice on start date, (2) Add specified amount to all future BTs after start date",
      "context": "Upsell processing methodology"
    },
    {
      "rule": "One-time upsell BT configuration: Frequency = none, Description = 'Additional User Licenses 0 months of service', Quantity = number of seats",
      "context": "Specific formatting for one-time upsell billing terms"
    },
    {
      "rule": "Integration item mapping: Annual Subscription/User Licenses → 'Access to Web Portal', Professional Fees → 'Professional Service Fees', Ecommerce Fees → 'E-Commerce API', Standard Services Package → 'Professional Service Fees'",
      "context": "Standard integration item categorization"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "context": "Operational defaults"
    },
    {
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "context": "Operational defaults"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "context": "Operational defaults"
    },
    {
      "rule": "Tax handling: Every tax line item becomes a separate BT (if none listed)",
      "context": "Tax processing default"
    },
    {
      "rule": "Upsell processing should be done without a customer assigned or any BTs initially",
      "context": "Initial upsell upload processing"
    },
    {
      "rule": "Create separate BTs for each invoice to enable individual modifications",
      "context": "BT structure for flexibility"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant may request specific processing that differs by contract (e.g., always back-date invoice date to final day of the month)",
      "condition": "Per merchant-specific instructions"
    },
    {
      "exception": "Statsig integration items should be labeled as 'Sales'",
      "condition": "Merchant-specific integration mapping"
    },
    {
      "exception": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "condition": "Merchant-specific integration mapping with override possibility"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Post-processing notifications may be required to specific team members at specific phases",
      "condition": "Example: Customer Success needs notification in merchant channel when Active phase contracts are processed"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "description": "Different merchants (Statsig, Pinata) have specific integration item categorization requirements",
      "customizable": true
    },
    {
      "element": "Post-processing communication requirements",
      "description": "Who needs to be notified, where, and when varies by merchant",
      "customizable": true
    },
    {
      "element": "Invoice date processing rules",
      "description": "Some merchants may require back-dating or specific date handling",
      "customizable": true
    },
    {
      "element": "Customer-specific information and special memos",
      "description": "Individual customers within a merchant may have unique requirements",
      "customizable": true
    },
    {
      "element": "Feature requests tracking",
      "description": "Merchant-specific feature requests with urgency and rationale",
      "customizable": true
    },
    {
      "element": "Events processing instructions",
      "description": "Merchant may have specific events billing requirements",
      "customizable": true
    },
    {
      "element": "Default operational parameters",
      "description": "While defaults exist, these can be overridden per merchant specification",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: Merchant Info Sheet - Proton_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:18:44

### Original Content
```
com video 3mmj6qcv9okx0mej-tabs-proton-november-26-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills They have a seat based usage billing that is fairly common in SaaS but somewhat complex to handle It can be described as a SaaS seat based billing that maintains a floor of user seats where billing never dips below the floor - more details below Is there any important merchant relationship information Mostly will be engaging with Owen a...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing model and complexity",
    "Merchant relationship management and key contacts",
    "Merchant engagement and temperament",
    "Tabs product features and value proposition",
    "SaaS seat-based usage billing with floor constraints"
  ],
  "rules": [
    {
      "rule": "Seat-based usage billing maintains a minimum floor of user seats",
      "description": "Billing never dips below the established floor regardless of actual usage",
      "type": "billing_constraint"
    },
    {
      "rule": "International operations team should ignore certain sections",
      "description": "Specific sections marked for AE Implementation team only, not for Ops International Team",
      "type": "operational_workflow"
    },
    {
      "rule": "SaaS seat-based billing model is the primary billing structure",
      "description": "Common in SaaS but noted as somewhat complex to handle in this implementation",
      "type": "billing_model"
    }
  ],
  "exceptions": [
    {
      "exception": "Billing floor constraint",
      "description": "Unlike standard usage-based billing, this merchant's billing has a minimum threshold that cannot be reduced even if seat usage decreases",
      "condition": "Applies to all billing cycles regardless of actual seat utilization"
    },
    {
      "exception": "Document sections with restricted access",
      "description": "Certain sections are explicitly marked for specific teams to ignore (Ops International Team)",
      "condition": "Applies to sections marked with '[Ops International Team to Ignore]'"
    }
  ],
  "merchant_specific": [
    {
      "element": "Primary contacts",
      "details": "Owen (primary POC and buyer/decision maker) and Wilhelm",
      "customization_needed": true
    },
    {
      "element": "Merchant temperament",
      "details": "Super engaged and very excited about Tabs",
      "customization_needed": false
    },
    {
      "element": "Key product features of interest",
      "details": "Usage ingest engine for process streamlining and visibility",
      "customization_needed": true
    },
    {
      "element": "Billing complexity",
      "details": "Seat-based billing with floor constraint - described as 'somewhat complex to handle'",
      "customization_needed": true
    },
    {
      "element": "Merchant identifier",
      "details": "Referenced by video code '3mmj6qcv9okx0mej-tabs-proton-november-26-2024'",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be incomplete or truncated (sentences cut off at the end)
- Clear structure and explicit information about billing model, contacts, and merchant temperament
- Some ambiguity around the exact implementation details of the billing floor mechanism
- Missing complete information about Tabs features that the POC cares about (text cuts off)
- Document format suggests this is a working note/template rather than finalized documentation

---

