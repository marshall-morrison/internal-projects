# Raw LLM Analysis: Pipe17 MIS_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:04:28

---

## Chunk 1: Pipe17 MIS__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:04:28

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp han...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder notification and communication protocols",
    "Feature requests and implementation priorities",
    "Third-party integration requirements (Stripe, Pipe17)",
    "Parent-child account billing relationships",
    "Documentation and call tracking"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
      "category": "notification",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Customer Information section post-go-live",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Account Executive (AE) fills Feature Requests prior to Implementation handoff",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Implementation team fills Feature Requests prior to go-live",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Success team fills Feature Requests post-go-live",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Tabs invoice payment data must be pushed to Pipe17 app for Stripe payment rail integration",
      "category": "integration",
      "explicit": true
    },
    {
      "rule": "Customer account updates must be pushed to Stripe to maintain seamless experience",
      "category": "integration",
      "explicit": true
    },
    {
      "rule": "AE fills Merchant Calls section for all videos prior to Implementation involvement",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Implementation fills Merchant Calls section prior to go-live",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Success fills Merchant Calls section post-go-live",
      "category": "responsibility",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Parent-child billing has two implementation options: Option 1 (preferred) where Pipe17 aggregates child events, or Option 2 where Tabs aggregates (requires 2 days to build and test)",
      "condition": "Depends on whether Pipe17 can handle aggregation"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Invoice-specific or relationship-specific requirements"
    },
    {
      "exception": "Invoice changes may occur due to merchant customer relationship dynamics",
      "condition": "Relationship-dependent modifications"
    },
    {
      "exception": "FR3 (MRR reporting) has lower urgency compared to FR1 (Stripe data update)",
      "condition": "Priority-based implementation sequencing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient: Azmat Aziz from Customer Success",
      "type": "contact",
      "customizable": true
    },
    {
      "element": "Notification channel: Messari internal merchant channel",
      "type": "communication_channel",
      "customizable": true
    },
    {
      "element": "Integration platform: Pipe17 app with Stripe payment rails",
      "type": "technology_stack",
      "customizable": true
    },
    {
      "element": "Parent-child billing structure and event aggregation requirements",
      "type": "billing_model",
      "customizable": true
    },
    {
      "element": "Special invoice memos and customer-specific requirements",
      "type": "documentation",
      "customizable": true
    },
    {
      "element": "Feature request priorities (FR1: Priority, FR2: conditional, FR3: not urgent)",
      "type": "implementation_priority",
      "customizable": true
    },
    {
      "element": "Merchant call recordings and documentation links",
      "type": "reference_materials",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Pipe17 MIS__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:04:31

### Original Content
```
Merchant Name Pipe17 Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Customer Creation Customers should exist in Tabs from QBO but please create if not available M...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Creation and Validation",
    "Billing Terms (BT) Configuration and Processing",
    "Usage-Based Billing and Tiered Pricing",
    "Revenue Category Assignment",
    "Contract Processing Workflow and Data Mapping"
  ],
  "rules": [
    "Customers should already exist in Tabs from QBO; do not create new customers",
    "If customer is missing, open a Pylon ticket",
    "Check email domain of customer to verify correct entity (may be subsidiary)",
    "Verify and update billing address and billing email in Garage for existing contracts",
    "Each line item becomes its own BT (Billing Term)",
    "Additional Orders usage BT must be processed as Tiered Unit BT",
    "Ignore all usage BTs in product descriptions except 'Additional Orders'",
    "For Additional Orders: BT name should be 'Tiered Usage', Event Type should be 'Tiered Usage', Revenue category should be 'Usage'",
    "Free tier language is 'Up to 175k orders per year'",
    "Adjust free tier quantity based on billing cadence: Annual=175k, Monthly=175k/12=14,583, Quarterly=175k/4=43,750",
    "Item Name: Use listed name; Additional orders should be 'Tiered Usage'",
    "Item Description: Copy ENTIRE item description",
    "Quantity: Use listed quantity; default to 1 if not specified",
    "Service Start Date: Use contract start date, signature date, or renewal term date (previous end date + 1 day)",
    "Net Terms: ALL will be 0",
    "Process discounts in-line within the BT itself",
    "Revenue Category for one-time BTs: assign 'One-Time'",
    "Revenue Category for usage BTs: assign 'Usage'",
    "MUST assign a revenue category to every BT",
    "Frequency: Use frequency listed next to price or in description",
    "For add-ons with no frequency or one-time fees: use NONE",
    "Additional Orders frequency follows the flat BT frequency it's associated with",
    "Billing Start Date: same as service start date",
    "Read item descriptions and Purchase Terms section closely for payment schedules",
    "Prorated add-ons: prorate on monthly basis (e.g., 10 months out of 12 = multiply by 10/12)",
    "Tax handling: If none listed, Ops Default is every tax line item becomes a BT"
  ],
  "exceptions": [
    "If customer name in contract is a subsidiary, verify via email domain",
    "For renewals without explicit start date, calculate from previous contract end date",
    "If no contract start date, signature date, or renewal date available, use 'Quote Created' date",
    "Additional Orders is the ONLY usage BT to process from product descriptions",
    "For add-ons without listed frequency, can use NONE",
    "Prorated add-ons only apply if contract explicitly states add-ons will be prorated",
    "Integration Items: ignore for now (to be filled post-go-live)",
    "Revenue category assignment uses best judgment if not falling into standard categories"
  ],
  "merchant_specific": [
    "Merchant Name: Pipe17 (placeholder for implementation and CX POC)",
    "Billing model section to be filled by Implementation team",
    "Contract Processing Steps to be filled by Implementation Success post-go-live",
    "Specific free tier threshold: 175k orders per year",
    "Tiered Usage BT naming convention specific to this merchant",
    "Customer existence verification through QBO/Tabs integration",
    "Garage system used for customer billing information management",
    "Pylon ticket system for missing customer escalation",
    "Events Processing section (merchant-specific, to be filled)",
    "Integration Items Processing section (merchant-specific, to be filled)",
    "Post Processing Communications section (merchant-specific, to be filled)",
    "Revenue category mapping (general guidance provided but may need merchant customization)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Pipe17 MIS__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:04:46

### Original Content
```
app gong io call id 7173441176989682448 account-id 6597097703158607878 Partnership: https: us-56595 app gong io call id 1882496550575645430 account-id 6597097703158607878 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Contracts: - Subscription Fee - Usage Complexity: discounts, payment terms, amendments, upsells (30  of revenue) 1) What is the merchant temperament Kathleen- likes Tabs but into the nitty gritty and holds her car...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Relationship Management and Stakeholder Analysis",
    "Revenue Recognition and Billing Complexity",
    "Tabs Platform Features and Product Capabilities",
    "Revenue Stream Classification and Categorization",
    "Implementation and Onboarding Requirements"
  ],
  "rules": [
    {
      "rule": "Account Executives must document merchant temperament and key stakeholder characteristics during handoff",
      "category": "Process",
      "explicit": true
    },
    {
      "rule": "Implementation team becomes the DRI (Directly Responsible Individual) upon handoff completion",
      "category": "Ownership",
      "explicit": true
    },
    {
      "rule": "Merchant billing information must include contract structure (subscription fees and usage)",
      "category": "Documentation",
      "explicit": true
    },
    {
      "rule": "Revenue complexity assessment must cover discounts, payment terms, amendments, and upsells (targeting 30% of revenue)",
      "category": "Revenue Analysis",
      "explicit": true
    },
    {
      "rule": "One-time revenue includes: Configuration, Implementation, Onboarding, Setup, Migration, Training, Pilot, Support Hours, Custom Work, Integration",
      "category": "Revenue Classification",
      "explicit": true
    },
    {
      "rule": "Platform revenue includes: Renewal, Subscription, Plan, Platform Fee, Add-on, Module, Connection, Feature",
      "category": "Revenue Classification",
      "explicit": true
    },
    {
      "rule": "Service revenue includes: Support (except 'Support Hours'), Consulting, Professional Services, Connections (when sold as service)",
      "category": "Revenue Classification",
      "explicit": true
    },
    {
      "rule": "Usage revenue includes: Usage, Tiered Usage, Order Usage, Per Order, Per Shipment",
      "category": "Revenue Classification",
      "explicit": true
    },
    {
      "rule": "Unrealized platform revenue includes: Credit at renewal, Unrealized",
      "category": "Revenue Classification",
      "explicit": true
    },
    {
      "rule": "Key POC feature preferences must be documented during handoff",
      "category": "Documentation",
      "explicit": true
    },
    {
      "rule": "When features are not available out-of-the-box, workarounds or export solutions must be communicated to merchant",
      "category": "Product Management",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "'Support Hours' is classified as One-time revenue, while general 'Support' is classified as Service revenue",
      "context": "Revenue classification has specific carve-outs for similar terms"
    },
    {
      "exception": "'Connections' can be classified as either Platform revenue (as a feature) or Service revenue (when sold as a service)",
      "context": "Classification depends on how the item is sold"
    },
    {
      "exception": "MRR reporting is not available out-of-the-box and requires export workaround",
      "context": "Product limitation requiring temporary solution"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant temperament profiles",
      "description": "Individual stakeholder characteristics (e.g., 'Kathleen- likes Tabs but into the nitty gritty and holds her cards close', 'Akash- super chill and loves Tabs')",
      "customization_required": true
    },
    {
      "element": "Champion identification",
      "description": "Identifying which stakeholders are product champions",
      "customization_required": true
    },
    {
      "element": "Feature priorities",
      "description": "Specific Tabs features that matter to each merchant (e.g., Automated invoice creation, Accurate Reporting and Rev Rec, MRR reporting, Automated dunning)",
      "customization_required": true
    },
    {
      "element": "Billing structure",
      "description": "How the specific merchant structures their contracts (subscription vs usage)",
      "customization_required": true
    },
    {
      "element": "Revenue complexity factors",
      "description": "Merchant-specific discounts, payment terms, amendments, and upsell percentages",
      "customization_required": true
    },
    {
      "element": "Workaround solutions",
      "description": "Custom exports or solutions for missing features based on merchant needs",
      "customization_required": true
    }
  ],
  "confidence_score": 0.75
}
```

---

