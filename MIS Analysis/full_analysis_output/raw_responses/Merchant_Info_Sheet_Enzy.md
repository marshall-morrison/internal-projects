# Raw LLM Analysis: Merchant Info Sheet - Enzy

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:37:22

---

## Chunk 1: Merchant Info Sheet - Enzy_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:22

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
      "rule": "When a new contract comes in, verify that BILLING contact is in merchant app by pinging Ashni and Marshall",
      "category": "contract_processing"
    },
    {
      "rule": "For customer creation, use email from the BILLING CONTACT SECTION",
      "category": "customer_creation"
    },
    {
      "rule": "Customer must be created with all information from the billing contact section",
      "category": "customer_creation"
    },
    {
      "rule": "Merchant wants to use primarily automatic payment methods (credit card or ACH debit)",
      "category": "billing"
    },
    {
      "rule": "Credit card fees should be passed on to customer",
      "category": "billing"
    },
    {
      "rule": "Implementation POC and GTM POC must be identified during onboarding",
      "category": "onboarding"
    },
    {
      "rule": "Key stakeholders (Accountant, CEO) must be documented",
      "category": "onboarding"
    },
    {
      "rule": "Merchant goals and pain points must be documented by AE and Implementation team",
      "category": "onboarding"
    }
  ],
  "exceptions": [
    {
      "exception": "No opt out clause exists for this merchant",
      "context": "Unlike standard contracts that may include opt-out provisions"
    },
    {
      "exception": "Some customers are billed flat fee, some with tiered overages",
      "context": "Billing model varies by customer type"
    },
    {
      "exception": "Most contracts have one-time implementation fees",
      "context": "Not all contracts include this fee"
    },
    {
      "exception": "Customer may already be created when contract comes in",
      "context": "Contract processing workflow branches based on customer existence"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: Enzy co",
      "type": "identity"
    },
    {
      "element": "Current customer base: 66 customers",
      "type": "business_metric"
    },
    {
      "element": "Accountant: Ignite Spot Accounting (partner deal, Corbin - Director of Onboarding)",
      "type": "stakeholder"
    },
    {
      "element": "CEO: Rob Craig",
      "type": "stakeholder"
    },
    {
      "element": "Business model: Subscription-based software for organizational performance",
      "type": "business_profile"
    },
    {
      "element": "Specific dates: Demo (Nov 21, 2024), MSA Signature (Nov 22, 2024), Kick Off (Dec 2, 2024), Go Live (Dec 23, 2024)",
      "type": "timeline"
    },
    {
      "element": "Goals: Automate invoicing, autocharging, track late fees and tiered overage fees",
      "type": "requirements"
    },
    {
      "element": "Reference to Caitlin for sample contracts",
      "type": "internal_contact"
    },
    {
      "element": "Contract structure: Simple, with flat fees and tiered overages",
      "type": "billing_structure"
    },
    {
      "element": "Integration requirements: ERP and Tax Integration (to be filled)",
      "type": "technical"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Enzy_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:24

### Original Content
```
DO NOT USE THE IMPLEMENTATION CONTACT SECTION Steps to process: New format: de3fdb64-2911-452a-9c06-d64bc3280cf7 The SOW effective date should still be the date the setup fee is sent out (the incorrect date was generated for this invoice 9 9 25 instead of 9 2 25 The E-signed Documents usage line item should be mapped to "Documents Sent" product The outbound domestic SMS line item should be mapped to "Messages Sent" product Instead of a tiered approach for additional users, the usage fees section...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Configuration",
    "Contract Data Mapping and Line Item Processing",
    "Date Management and Effective Date Rules",
    "Billing Type Classification and Tier Pricing",
    "Implementation Services vs Recurring Services Handling"
  ],
  "rules": [
    "DO NOT USE THE IMPLEMENTATION CONTACT SECTION",
    "SOW effective date should be the date the setup fee is sent out",
    "E-signed Documents usage line item maps to 'Documents Sent' product",
    "Outbound domestic SMS line item maps to 'Messages Sent' product",
    "Create separate revenue schedule for each line item listed in contract",
    "Create additional revenue schedule for Base Users",
    "Implementation services default to 2 MONTHS total service period",
    "All other services default to 36 months total service period",
    "Item Description field should be left blank",
    "Integration Item must match 1:1 with the item name",
    "Billing Type for Core Enzy: Flat",
    "Billing Type for Setup and Implementation Services: Flat",
    "Billing Type for Active Users: Tier Flat Pricing - VOLUME BASED",
    "Default Quantity: 1",
    "Start Date for Setup Fee: Sign Date of Contract Net 0",
    "If no signature date exists, use SOW effective date; if no SOW effective date, use Order Form effective date",
    "Start Date for other services: Use the effective date",
    "Default Periods: 36",
    "Frequency for Implementation Services: NONE",
    "Frequency for all other line items if billed monthly: 1 month",
    "Net Terms: 0 for all (for setup/implementation), 30 default for other services",
    "Default Net Payment Terms: 0 for all",
    "Default Billing Frequency if None Listed: Monthly",
    "Every tax line item becomes a BT Events Processing item",
    "Usage fees show price per additional user above baseline committed user count"
  ],
  "exceptions": [
    "If there is no signature date, fallback to SOW effective date",
    "If there is no SOW effective date, fallback to Order Form effective date",
    "Integration Item for Setup and Implementation Services differs from Loom video instructions",
    "Net Terms: 0 for implementation services but 30 default for other services and line items",
    "Merchant may request specific processing that differs by contract (e.g., back-dating invoice date to final day of month)",
    "Additional users calculated incrementally: 11 users = $50, 12 users = $100, etc.",
    "Tier Flat Pricing requires creating tiers for users included and any additional user pricing bullets"
  ],
  "merchant_specific": [
    "Contract format reference: de3fdb64-2911-452a-9c06-d64bc3280cf7",
    "Baseline committed user count example: 10 users for Friendly Energy Solutions",
    "Price per additional user example: $50",
    "Specific product mappings may vary by merchant (Documents Sent, Messages Sent)",
    "Integration Items labeling: 'All Statsig integrations items should be labeled as Sales'",
    "Integration Items labeling: 'All Pinata integration items should be labeled as Software Subscription Bundle unless otherwise noted'",
    "Service term length: Refer to specific contract",
    "Effective dates: Refer to specific contract",
    "Tier creation for Additional Users: Based on contract specifics (e.g., 25 users included, at 50 users, at 75 users)",
    "Post-processing communications requirements vary by merchant",
    "Items to ignore in contracts vary by merchant request"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Enzy_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:34

### Original Content
```
2) Is there a key POC: (i e : who is the buyer decision maker ) CEO - Rob Craig 3) What are the Tabs features that the key POC cares about Forwarding contracts from Hubspot Having better system to manage his tiered overage fees More automated system to invoice - doesn t like the manual workflow Autocharge Keeping track of renewals
```

### LLM Analysis Response
```json
{
  "themes": [
    "Key stakeholder identification and decision-making authority",
    "Contract management and CRM integration requirements",
    "Billing automation and invoicing workflow optimization",
    "Revenue management for tiered pricing structures",
    "Customer lifecycle management and renewal tracking"
  ],
  "rules": [
    "CEO (Rob Craig) is identified as the primary buyer decision maker and key point of contact",
    "System must support forwarding contracts from Hubspot CRM",
    "Platform must provide automated invoicing capabilities to replace manual workflows",
    "System must include autocharge functionality for payment processing",
    "Platform must track and manage contract renewals",
    "System must handle tiered overage fee structures and management"
  ],
  "exceptions": [
    "Manual workflow for invoicing is explicitly not desired - automation is required",
    "Standard contract management may need special handling for Hubspot integration",
    "Tiered overage fees require specialized tracking beyond standard billing"
  ],
  "merchant_specific": [
    "Key POC name: Rob Craig (CEO) - specific to this merchant",
    "Hubspot as the CRM system - merchant uses specific third-party platform",
    "Tiered overage fee structure - indicates merchant-specific pricing model",
    "Current manual invoicing workflow - indicates existing process that needs replacement",
    "Renewal tracking requirements - may vary based on merchant's contract terms and business model"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Enzy_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:37:37

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Wants us to decouple o...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Customer Relationship Management",
    "Feature Requests and Product Improvements",
    "Billing Structure and Invoice Management",
    "Partner Relationship Management"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in the Messari internal merchant channel when contracts are processed during Active merchant phase",
      "category": "notification_protocol",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information section",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling feature requests section",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "Rewatch calls must be documented with links and dates",
      "category": "documentation",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore the Notes Sections",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "AE and Implementation teams must document merchant billing structure (recurring subscriptions, overage fees, late fees)",
      "category": "billing_documentation",
      "explicit": true
    },
    {
      "rule": "Merchant temperament should be documented",
      "category": "relationship_management",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Depends on specific customer requirements",
      "impact": "Invoice processing workflow"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship dynamics",
      "condition": "Relationship-specific circumstances",
      "impact": "Standard invoice processing"
    },
    {
      "exception": "Partner client relationships (e.g., Ignite Spot partnership) require special attention to impress partner",
      "condition": "When merchant is a partner client",
      "impact": "Service level and relationship management approach"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "example": "Customer Success [Azmat Aziz]",
      "customizable": true
    },
    {
      "element": "Internal communication channel",
      "example": "Messari internal merchant channel",
      "customizable": true
    },
    {
      "element": "Merchant phase trigger",
      "example": "Active phase for contract processing",
      "customizable": true
    },
    {
      "element": "Billing structure",
      "example": "Recurring subscriptions with overage fees and late fees",
      "customizable": true
    },
    {
      "element": "Partner relationships",
      "example": "Ignite Spot partnership with Salt Lake City companies",
      "customizable": true
    },
    {
      "element": "Merchant temperament",
      "example": "Super chill",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "example": "Decouple one-time implementation fees from renewals, select all button for scheduled invoices",
      "customizable": true
    },
    {
      "element": "Special invoice requirements",
      "example": "Special memos for certain invoices",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

