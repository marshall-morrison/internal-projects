# Raw LLM Analysis: Merchant Info Sheet - Enzy(1)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:47:58

---

## Chunk 1: Merchant Info Sheet - Enzy(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:58

### Original Content
```
Merchant Demo date: Nov 21, 2024 Scoping start date: Nov 21, 2024 MSA Signature Date: Nov 22, 2024 Onboarding Kick Off Date: Dec 2, 2024 [If Exists] Opt Out Date: Go Live Date: Dec 23, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Ignite Spot Accounting, partner deal, Corbin- Director of Onboarding CEO: Rob Craig Company summary (AE to fill) Enzy co offers a platform designed to improve organizational performance by streamlining workflows and boosting...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Billing Model and Payment Processing",
    "Contract Processing Workflow",
    "Merchant Business Profile and Goals",
    "Customer Creation and Contact Management"
  ],
  "rules": [
    {
      "rule": "When a new contract comes in, customer must already be created before processing",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Ping Ashni and Marshall to verify that BILLING contact is in merchant app",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "For customer email, use the BILLING CONTACT SECTION information",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Fill out customer creation with all information from the billing contact section",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Merchant wants to use primarily automatic payment methods (CC or ACH debit)",
      "category": "Billing",
      "explicit": true
    },
    {
      "rule": "Credit card fees should be passed on to customer",
      "category": "Billing",
      "explicit": true
    },
    {
      "rule": "Automate invoicing, autocharging, and track late fees and tiered overage fees",
      "category": "Billing Automation",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "No opt out clause exists for this merchant",
      "condition": "Standard onboarding includes opt-out clause check, but this merchant has none",
      "impact": "No need to track opt-out conditions or dates"
    },
    {
      "exception": "Partner deal with Ignite Spot Accounting (Corbin - Director of Onboarding)",
      "condition": "Special accountant relationship",
      "impact": "May require special coordination or communication protocols"
    },
    {
      "exception": "Mixed billing structure: some flat fee, some with tiered overages, most with one-time implementation fees",
      "condition": "Not a uniform billing model across all customers",
      "impact": "Requires flexible billing configuration per customer contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Name",
      "value": "Enzy",
      "type": "Identity"
    },
    {
      "element": "Current Customer Count",
      "value": "66 customers",
      "type": "Business Metric"
    },
    {
      "element": "Key Personnel - CEO",
      "value": "Rob Craig",
      "type": "Contact"
    },
    {
      "element": "Key Personnel - Accountant",
      "value": "Ignite Spot Accounting, Corbin (Director of Onboarding)",
      "type": "Contact"
    },
    {
      "element": "Business Model",
      "value": "Subscription-based software for organizational performance, workflows, and team productivity",
      "type": "Business Description"
    },
    {
      "element": "Onboarding Timeline",
      "value": "Demo: Nov 21, 2024; MSA: Nov 22, 2024; Kick Off: Dec 2, 2024; Go Live: Dec 23, 2024",
      "type": "Timeline"
    },
    {
      "element": "Sample Contracts",
      "value": "Caitlin can send over sample contracts",
      "type": "Documentation"
    },
    {
      "element": "Billing Structure Details",
      "value": "Flat fees, tiered overages, one-time implementation fees",
      "type": "Billing Configuration"
    },
    {
      "element": "Processing Reference",
      "value": "EXAMPLE GARAGE PROCESSING video with corrections",
      "type": "Training Material"
    },
    {
      "element": "North Star Goal",
      "value": "Automate invoicing, autocharging, and track late fees and tiered overage fees",
      "type": "Business Objective"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Enzy(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:48:02

### Original Content
```
DO NOT USE THE IMPLEMENTATION CONTACT SECTION Steps to process You will create a revenue schedule for each line item listed, in the screenshot above, there are 2 items so you will create 2 revenue schedules, if you see more line items, you would create a different revenue schedule And then create a 3rd revenue schedule for Base Users Service Start Date: See contract for effective date, refer to screenshot above for where to find Total Months of Service: PUT 2 MONTHS FOR IMPLEMENTATION Default to...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation Process",
    "Billing Configuration and Pricing Models",
    "Contract Date and Timeline Management",
    "Integration Item Mapping and Naming Conventions",
    "Implementation vs Recurring Service Handling"
  ],
  "rules": [
    "DO NOT USE THE IMPLEMENTATION CONTACT SECTION",
    "Create a separate revenue schedule for each line item in the contract",
    "Always create an additional revenue schedule for Base Users",
    "Implementation services: Total Months of Service = 2 MONTHS",
    "All other services: Default to 36 months",
    "Item Description field: Leave blank",
    "Integration items must have 1:1 match with item name",
    "Billing Type for Core Enzy: Flat",
    "Billing Type for Setup and Implementation Services: Flat",
    "Billing Type for ACTIVE USERS: Tier Flat Pricing - VOLUME BASED",
    "Quantity: Default to 1",
    "Start Date for Setup Fee: Sign Date of Contract Net 0",
    "If no signature date: Use SOW effective date; if no SOW effective date, use Order Form effective date",
    "Start Date for other services: Use the effective date from contract",
    "Periods: 36 (default)",
    "Frequency for Implementation Services: NONE",
    "Frequency for all other line items: 1 month (if stated as billed monthly)",
    "Net Terms: 0 for all (general rule), 0 for implementation services, 30 default for other services and line items",
    "Default Billing Frequency if None Listed: Monthly",
    "Default Net Payment Terms: 0 for all",
    "Tax line items: Each tax line item becomes a BT Events",
    "Integration item mapping: Setup and Implementation Services = Setup Services, Core Enzy = Core Enzy, Canvassing Module = Canvassing Module"
  ],
  "exceptions": [
    "Core Enzy integration item mapping is DIFFERENT FROM WHAT WAS SAID ON LOOM VIDEO",
    "Net Terms has conflicting rules: '0 for all' vs '30 default for other services and line items'",
    "If no signature date exists, fall back to SOW effective date, then Order Form effective date",
    "Tier Flat Pricing requires creating tiers for: Users included (e.g., 25 users) and additional user pricing bullets (e.g., At 50 users, at 75 users)",
    "Merchant-specific processing may differ by contract (e.g., back-date invoice date to final day of month)",
    "Special customer-specific memos or invoice changes may be required based on merchant-customer relationship"
  ],
  "merchant_specific": [
    "Merchant name: Enzy (referenced as 'Core Enzy', 'Enzy:Core Enzy')",
    "Specific integration items: Setup Services, Core Enzy, Canvassing Module",
    "Event to track for Tier Flat Pricing: Active Users",
    "Feature requests: Decouple one-time implementation fees from renewals, Select all button for schedule sending invoices",
    "Post-processing notification: Customer Success [Azmat Aziz] needs notification in Messari internal merchant channel when contracts are processed [Merchant Phase: Active]",
    "Integration item labeling examples: Statsig items labeled as 'Sales', Pinata items labeled as 'Software Subscription Bundle'",
    "Rewatch call links and custom demo references specific to this merchant implementation",
    "Contract-specific variations: Service term length, specific user tier thresholds, pricing structures",
    "Customer-specific information section for special memos and invoice requirements"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: Merchant Info Sheet - Enzy(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:48:08

### Original Content
```
com video 9fvjlk9bp83yhfos-tabs-custom-demo-for-enzy First call: https: tabs rewatch com video 7fbb8kbz8az65k3z-tabs-enzy-intro-call Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Recurring subscriptions with overage fees and late fees Is there any important merchant relationship information Caitlin: This is a partner client Partner is Ignite Spot They basically have all the up and coming Salt Lake City companies as clients Trying to imp...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Partner relationship management and client impression",
    "Billing structure complexity (recurring subscriptions with overage and late fees)",
    "Automation and workflow efficiency requirements",
    "Key stakeholder identification and feature prioritization",
    "Integration needs with existing systems (HubSpot)"
  ],
  "rules": [
    "Operations International Team should ignore sections marked for AE Implementation",
    "Merchant billing model includes recurring subscriptions with overage fees and late fees",
    "Partner relationships require special attention and service quality (partner: Ignite Spot)",
    "CEO (Rob Craig) is identified as the primary decision maker and key POC",
    "Implementation must support tiered overage fee management",
    "System must support contract forwarding from HubSpot",
    "Invoicing process should be automated rather than manual",
    "Autocharge functionality is required",
    "Renewal tracking capability is necessary"
  ],
  "exceptions": [
    "This is a partner client (Ignite Spot) requiring special handling to impress the partner",
    "Merchant has 'super chill' temperament - may indicate flexible communication style acceptable",
    "Sections marked '[Ops International Team to Ignore]' should be excluded from certain team workflows"
  ],
  "merchant_specific": [
    "Partner name: Ignite Spot",
    "Geographic market focus: Salt Lake City companies",
    "Key POC: CEO Rob Craig",
    "Merchant temperament: 'super chill'",
    "Specific pain points: manual invoicing workflow, tiered overage fee management",
    "Integration requirement: HubSpot contract forwarding",
    "Priority features: tiered overage fees, automated invoicing, autocharge, renewal tracking"
  ],
  "confidence_score": 0.85
}
```

---

