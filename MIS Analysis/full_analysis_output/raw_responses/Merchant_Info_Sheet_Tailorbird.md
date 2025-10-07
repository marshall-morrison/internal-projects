# Raw LLM Analysis: Merchant Info Sheet - Tailorbird

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:20:51

---

## Chunk 1: Merchant Info Sheet - Tailorbird_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:51

### Original Content
```
Need custom AP portal integrations to the below AP portals Ops team agreed to support the Tailorbird team operationally for 5 hours month to facilitate payments until integrations are productized: Vendor Cafe RealPage NetVendor Paymode X OpsTechnology I-BEAM Risk Ledger IRT Portal (Client-Specific) How contract is broken up Contracts can vary between customers, would be open to partnering with Tabs to help improve their contract structure and streamline it One off things to know about the mercha...
```

### LLM Analysis Response
```json
{
  "themes": [
    "AP Portal Integration Requirements",
    "Contract Processing Standards and Defaults",
    "Merchant Relationship Management and Communication",
    "Custom Processing Instructions and Specifications",
    "Feature Requests and Implementation Tracking"
  ],
  "rules": [
    {
      "rule": "Ops team provides 5 hours monthly operational support to Tailorbird team for payment facilitation until integrations are productized",
      "category": "operational_support"
    },
    {
      "rule": "Default service term is 1 year if none listed in contract",
      "category": "contract_defaults"
    },
    {
      "rule": "Default net payment terms is 0 (net zero) if none specified",
      "category": "contract_defaults"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "contract_defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax) if none specified",
      "category": "contract_defaults"
    },
    {
      "rule": "Merchant is not on Stripe for payment processing",
      "category": "payment_processing"
    },
    {
      "rule": "International team should ignore specific sections marked for AE and Implementation",
      "category": "team_responsibilities"
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts can vary between customers - merchant open to partnering with Tabs to improve contract structure",
      "context": "contract_structure"
    },
    {
      "exception": "Merchant may request specific processing that differs by contract (e.g., back-dating invoice dates to final day of month)",
      "context": "invoice_processing"
    },
    {
      "exception": "Special memos may be required for certain invoices based on customer relationships",
      "context": "customer_specific_requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "context": "relationship_management"
    }
  ],
  "merchant_specific": [
    {
      "element": "AP Portal Integration List",
      "details": "Vendor Cafe, RealPage, NetVendor, Paymode X, OpsTechnology, I-BEAM, Risk Ledger, IRT Portal (Client-Specific)",
      "customization_needed": true
    },
    {
      "element": "Product Requirements Document",
      "details": "Reference to 'Tailorbird product requirements' document",
      "customization_needed": true
    },
    {
      "element": "Integration Item Labeling Rules",
      "details": "Specific instructions for how to label integration items (examples given: Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "customization_needed": true
    },
    {
      "element": "Post-Processing Notification Requirements",
      "details": "Who to notify, where, and when after processing batches (example: Customer Success Azmat Aziz in Messari channel)",
      "customization_needed": true
    },
    {
      "element": "Merchant Temperament Profile",
      "details": "Friendly, straightforward, empathetic and excited about what Tabs is building",
      "customization_needed": true
    },
    {
      "element": "Key Point of Contact",
      "details": "Jacques (CFO) is the POC and decision maker",
      "customization_needed": true
    },
    {
      "element": "Sample Contracts Location",
      "details": "Sample contracts stored in Tailorbird account",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Tailorbird_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:52

### Original Content
```
Merchant: Tailorbird Demo date: Nov 19, 2024 Scoping start date: Dec 26, 2024 MSA Signature Date: Dec 23, 2024 Onboarding Kick Off Date: Jan 3, 2025 [If Exists] Opt Out Date: N A Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Kruze Accounting Firm CFO: Jacques Souk - main POC day to day CEO: Tim Cantwell Account Receivable POC: Jacques Billing POC: Jacques Company summary (AE to fill) Summary of what company does: Tailorbird uses AI to transfo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Business Goals and Pain Points",
    "Billing Model and Customer Structure",
    "Implementation Requirements and Success Criteria"
  ],
  "rules": [
    {
      "rule": "Onboarding follows a structured timeline: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "category": "Process",
      "explicit": true
    },
    {
      "rule": "Key stakeholders must be identified including CFO, CEO, Accountant, AR POC, and Billing POC",
      "category": "Stakeholder Management",
      "explicit": true
    },
    {
      "rule": "Implementation requires understanding of merchant's ERP and Tax Integration systems",
      "category": "Technical Requirements",
      "explicit": true
    },
    {
      "rule": "Merchant goals (North star) must be documented including pain points and reasons for purchase",
      "category": "Requirements Gathering",
      "explicit": true
    },
    {
      "rule": "Opt-out clause status and conditions must be documented",
      "category": "Contract Terms",
      "explicit": true
    },
    {
      "rule": "Customer creation process uniqueness must be identified and documented",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Billing model details must include component types (fixed/usage) and billing frequency",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "AE (Account Executive) and Implementation team have shared responsibility for filling merchant information",
      "category": "Process Ownership",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Parent-child customer relationships require special handling for property management companies and their related properties",
      "condition": "When merchant bills property management companies with multiple properties"
    },
    {
      "exception": "Pro-rated terms may apply to billing cycles",
      "condition": "When billing includes usage tiers and non-standard term lengths"
    },
    {
      "exception": "Opt-out date may not exist for all merchants",
      "condition": "Indicated by 'N/A' or absence of opt-out clause"
    },
    {
      "exception": "Usage-based billing with tiered pricing requires special configuration",
      "condition": "When merchant has variable usage components in addition to fixed fees"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company summary describing business model and industry",
      "customization_needed": "Must be tailored to each merchant's specific business (e.g., AI for real estate floorplans)"
    },
    {
      "element": "Specific pain points and goals",
      "customization_needed": "Varies by merchant (e.g., DSO reduction, manual invoicing elimination, finance team size constraints)"
    },
    {
      "element": "Key personnel names and roles",
      "customization_needed": "Unique to each merchant organization"
    },
    {
      "element": "Accounting firm or outsourced finance partners",
      "customization_needed": "May vary or not exist depending on merchant's finance structure"
    },
    {
      "element": "Current systems and tools",
      "customization_needed": "Merchant-specific tech stack (e.g., Quickbooks, spreadsheets, specific ERPs)"
    },
    {
      "element": "Customer relationship structure",
      "customization_needed": "Varies by business model (e.g., parent-child for property management vs. flat structure)"
    },
    {
      "element": "Billing frequency and components",
      "customization_needed": "Merchant-specific pricing model (annual, monthly, usage-based, tiered, etc.)"
    },
    {
      "element": "Timeline dates",
      "customization_needed": "Unique to each merchant's onboarding schedule"
    },
    {
      "element": "Opt-out clause terms",
      "customization_needed": "Contract-specific, may or may not exist"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Tailorbird_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:21:05

### Original Content
```
QBO integration, invoice automation, payment portal to collect payments faster, parent child structures, cash forecasting, rev rec and revenue reporting 100 current customers Not currently on stripe-they use ACH
```

### LLM Analysis Response
```json
{
  "themes": [
    "Financial system integrations and automation",
    "Payment processing and collection optimization",
    "Revenue management and reporting",
    "Customer account structure and organization",
    "Payment method preferences and constraints"
  ],
  "rules": [
    "Must integrate with QuickBooks Online (QBO)",
    "Invoice automation must be implemented",
    "Payment portal must be provided to accelerate payment collection",
    "System must support parent-child account structures",
    "Cash forecasting capabilities are required",
    "Revenue recognition (rev rec) functionality must be available",
    "Revenue reporting must be current/real-time (100% current)",
    "ACH payment method is currently in use (not Stripe)",
    "Customer base consists of 100 current customers"
  ],
  "exceptions": [
    "Customers are NOT currently on Stripe platform - using ACH instead (indicating a potential migration scenario or platform preference)",
    "The '100 current customers' may represent a baseline that could affect implementation scope or pricing tier"
  ],
  "merchant_specific": [
    "Number of customers: 100 (specific to this merchant's scale)",
    "Current payment processor: ACH (not Stripe) - indicates existing infrastructure",
    "Parent-child structure requirement (suggests B2B or multi-entity business model specific to this merchant)",
    "QBO as the accounting system (merchant's chosen platform)",
    "Emphasis on 'faster' payment collection suggests current pain point or business priority",
    "Revenue reporting being '100 current' may indicate specific compliance or operational requirements"
  ],
  "confidence_score": 0.75
}
```

**Analysis Notes:**
- The confidence score of 0.75 reflects that while the requirements are clear, the document chunk is brief and lacks context about implementation details, priorities, or conditional logic
- The phrase "100 current customers" could mean "100% current" (all up-to-date) or "100 customers currently" - interpreted as the latter based on context
- The ACH vs. Stripe distinction is significant and may indicate integration constraints or future migration needs

---

