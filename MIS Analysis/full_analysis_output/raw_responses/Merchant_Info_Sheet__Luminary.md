# Raw LLM Analysis: Merchant Info Sheet_ Luminary

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:37:48

---

## Chunk 1: Merchant Info Sheet_ Luminary_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:48

### Original Content
```
If the number of seats stays the same across multiple billing schedules, the revenue schedules should extend for the duration of the total billing schedules For example, in the picture below this would be a RS BT for Y1, a different RS BT for Y2, and a third RS BT for Y3 The rev schedules would not be Y1-3 This is necessary to show an increase in GAAP revenue across the periods which is important to the CEO For flat fees, please ensure to bill first of period Item Description for anything that i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Management and Billing Term Configuration",
    "GAAP Revenue Recognition and Financial Reporting Requirements",
    "Usage-Based Billing for Additional Users/Resources",
    "Item Description Requirements for Platform Access Products",
    "Billing Timing and Proration Rules"
  ],
  "rules": [
    "When seat count remains constant across multiple billing schedules, create separate Revenue Schedule Billing Terms (RS BT) for each period (Y1, Y2, Y3) rather than combining them",
    "Separate revenue schedules per period are required to demonstrate GAAP revenue increases across periods for CEO reporting",
    "Flat fees must be billed at the first of the period",
    "Item descriptions for Luminary Platform Access must include authorized users and active clients information",
    "Overage costs for users/households/plans require a separate billing term with 'Additional Users' event assignment",
    "Additional Users billing terms must use unit price billing type",
    "Additional Users billing terms are recurring monthly but priced for the entire term",
    "All additional users are billed on the calendar month basis",
    "When no overage price exists for users, no usage-based billing term should be created",
    "Merchant creates and uploads usage data for partial term additions (e.g., 0.75 for 9 months)"
  ],
  "exceptions": [
    "If there is no overage price for the number of users/households/plans, the usage-based billing term rule does not apply",
    "Partial term additions require prorated usage data calculation (e.g., 9 months = 0.75 of full term)",
    "The general rule of combining billing schedules is overridden when demonstrating GAAP revenue increases is required"
  ],
  "merchant_specific": [
    "CEO requirement for showing GAAP revenue increases across periods",
    "Luminary Platform Access product naming and structure",
    "Specific terminology: 'authorized users', 'active clients', 'households', 'plans'",
    "Event naming convention: 'Additional Users'",
    "Screenshot references suggest merchant-specific UI/system locations for data retrieval",
    "Merchant responsibility for creating and uploading usage data for partial terms",
    "Specific pricing example: $500 for additional users for entire term"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet_ Luminary_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:52

### Original Content
```
merchant Demo date: Oct 2nd, 2024 Scoping start date: Sep 30, 2024 MSA Signature Date: Nov 7, 2024 Onboarding Kick Off Date: Nov 13, 2024 Go Live Date: Dec 12, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Account Receivable POC: Jemima Law, Head of BizOps Billing POC: Mary Huang, Chief Commercial Officer - https: www linkedin com in maryhuan9  Accountant: Joy Hu, CPA at Attivo Company summary (AE to fill) Luminary is a technology platform that automates the comp...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Billing and Revenue Model",
    "Contract Processing Workflow",
    "Merchant Business Context and Goals"
  ],
  "rules": [
    {
      "rule": "US TEAM ONLY: Customer Name must be correct based on Advisor Name",
      "category": "data_validation",
      "action_required": "Ping Ashni Walia and Marshall Morrison once processed"
    },
    {
      "rule": "Subscription SKU may extend across multiple years",
      "category": "subscription_management",
      "implication": "Long-term subscription handling required"
    },
    {
      "rule": "If number of user seats changes, each revenue schedule should only be as long as the billing schedule",
      "category": "revenue_recognition",
      "implication": "Revenue schedules must align with billing periods when seat count changes"
    },
    {
      "rule": "Use Billing POC Name, Email and Address when creating customers",
      "category": "customer_creation",
      "implication": "Specific contact information must be used for customer records"
    },
    {
      "rule": "Contract processing requires verification by specific team members (Ashni Walia and Marshall Morrison)",
      "category": "approval_workflow",
      "implication": "Quality control checkpoint in processing"
    }
  ],
  "exceptions": [
    {
      "exception": "US TEAM ONLY restriction on customer name processing",
      "condition": "Geographic team limitation",
      "special_handling": "Only US team members should handle customer name verification"
    },
    {
      "exception": "Variable revenue schedule length based on seat changes",
      "condition": "When number of user seats changes",
      "special_handling": "Revenue schedule must be adjusted to match billing schedule length, not extend beyond it"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "condition": "Contract termination",
      "special_handling": "Standard opt-out considerations do not apply"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing Model",
      "details": "Flat Platform Fee (predetermined or prorated by seats) + Tiered pricing for number of active clients",
      "customization_needed": true
    },
    {
      "element": "Contract Structure",
      "details": "2-page contract covering subscription and payments",
      "customization_needed": true
    },
    {
      "element": "Key Stakeholders",
      "details": "Jemima Law (AR POC), Mary Huang (Billing POC), Joy Hu (Accountant)",
      "customization_needed": true
    },
    {
      "element": "Business Context",
      "details": "Estate planning technology platform, founded 2022, recently removed outsourced accounting, scaling quickly",
      "customization_needed": true
    },
    {
      "element": "Merchant Goals",
      "details": "Rev Ops under non-finance background leader, need unified system for finance management, automate revenue workflows",
      "customization_needed": true
    },
    {
      "element": "ERP and Tax Integration",
      "details": "Fields present but not filled in document",
      "customization_needed": true
    },
    {
      "element": "Customer Creation Process",
      "details": "Customer names based on Advisor Names (specific to business model)",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet_ Luminary_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:04

### Original Content
```
If a deal is signed on May 15th, the Subscription SKUs would be billed May 15th for the period May 15, 2024 - May 14, 2025 and the Additional User item would be billed June 1, recurring monthly for 12 months Solution Tier billing item should always be a quantity of 1 Ignore the number of authorized users Number of clients SKU Many contracts bill by the number of active clients (customers) These may be priced at  x each year which means they should look like this: (NOTE that I have priced this QU...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing timing and frequency rules",
    "SKU and product quantity specifications",
    "Default contract terms and payment conditions",
    "Tax handling and invoicing procedures",
    "Team communication and notification protocols"
  ],
  "rules": [
    "Subscription SKUs are billed on deal signing date for annual period (e.g., May 15 to May 14)",
    "Additional User items are billed monthly starting on the 1st of the following month after deal signing, recurring for 12 months",
    "Solution Tier billing item must always have a quantity of 1",
    "Number of authorized users should be ignored in billing calculations",
    "Active client fee products are always billed on calendar quarters (January 1, April 1, July 1, or October 1)",
    "Active client fee pricing should be divided by 4 for quarterly billing",
    "Default service term is 1 year",
    "Default net payment terms are 30 days",
    "Default billing frequency: Annual for subscriptions, Quarterly for active client fees, Monthly for number of users",
    "No separate tax line items should be added - taxes are computed by Quickbooks",
    "Team notifications required only for batches processed between December 2024 and February 2025",
    "Notifications should be sent in Luminary channel with CC to Arjun Gopalratnam"
  ],
  "exceptions": [
    "Active client fee billing must start on specific calendar quarter dates (Jan 1, Apr 1, Jul 1, or Oct 1) regardless of deal signing date",
    "Communication protocol is temporary - only required from Dec 2024 to Feb 2025, then discontinued",
    "Merchant may request contract-specific variations (e.g., backdating invoice dates), though none currently specified"
  ],
  "merchant_specific": [
    "Feature request: Hubspot Customer Data syncing to Tabs",
    "Merchant uses HubSpot as source of truth for revenue",
    "Desire to use Tabs as CRM for their customers",
    "Specific contact for notifications: Arjun Gopalratnam",
    "Communication channel: Luminary",
    "Referenced intro call dated 9/30/24",
    "Specific SKU types: Subscription SKUs, Additional User items, Solution Tier, Number of clients SKU"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet_ Luminary_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:06

### Original Content
```
rewatch com video k7fq9guhdnw465z0-mary-and-rebecca-schwartz-tabs-september-30-2024 Custom Demo 10 2 24 https: tabs rewatch com video ukg5affvd9fpoeff-luminary-tabs-custom-demo-october-2-2024 Notes Usage data sheet: Luminary   Tabs usage template Using docusign forwarding for new deals Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Flat Platform Fee and Tiered unit pricing for Active Clients Is there any important merchant relationship information 1) What is the m...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Onboarding and Implementation",
    "Usage-Based Billing and Pricing Structure",
    "Merchant Relationship Management",
    "Product Feature Configuration and Integration",
    "Contract Management and Documentation"
  ],
  "rules": [
    "Flat Platform Fee combined with Tiered unit pricing model must be applied for Active Clients",
    "DocuSign forwarding process should be used for new deals",
    "Operations International Team should ignore specific sections marked for AE and Implementation teams",
    "Usage data must be tracked using the Luminary Tabs usage template",
    "SSO integration must be configured as a trackable item/event",
    "Additional users must be tracked as separate billable items",
    "Active Client Fee must be tracked as a distinct event/metric",
    "Key POC (buyer/decision maker) must be identified during implementation",
    "Merchant temperament assessment should be documented",
    "Platform Access subscriptions must align with contract specifications"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' are excluded from certain team workflows",
    "AE and Implementation teams have specific sections designated for their input only",
    "Custom demo recordings and notes are maintained separately for reference (dated entries: September 30, 2024 and October 2, 2024)"
  ],
  "merchant_specific": [
    "Merchant temperament characterization (e.g., 'Easy people to work with - intelligent')",
    "Key POC names and roles (Mary, Jemima as decision makers; Mary's previous relationship with Arjun at Peloton)",
    "Specific Tabs features prioritized by merchant (Usage billing, Renewals Management, Reporting)",
    "Custom item naming conventions (e.g., 'Luminary Platform Access', 'Luminary Builder Platform Access')",
    "Integration-specific tracking items tailored to merchant's product offerings",
    "Historical relationship context (previous work experience at Peloton)",
    "Merchant-specific subscription types as defined in their contract"
  ],
  "confidence_score": 0.75
}
```

---

