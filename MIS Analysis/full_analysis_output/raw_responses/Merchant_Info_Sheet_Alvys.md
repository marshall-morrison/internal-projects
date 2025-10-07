# Raw LLM Analysis: Merchant Info Sheet - Alvys

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:18:31

---

## Chunk 1: Merchant Info Sheet - Alvys_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:31

### Original Content
```
Other 90  are billed 60 days from contract signature regardless of go live All contracts are different (ie annual vs monthly and   amounts) Starting to incorporate overages into billing Information on how merchant bills Monthly and annual In stripe today with subscriptions How contract is broken up Effective Date vs Start Date One off things to know about the merchant Contract Processing Steps (Implementation Success to fill) Steps to process TWO types of contracts - please refer to the appropri...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Recognition",
    "Billing Terms and Payment Schedules",
    "Service Start Date Determination",
    "Contract Type Classification (Subscription Carrier Plan vs Anticipated Go-Live)",
    "Item and Price Processing"
  ],
  "rules": [
    "Two types of contracts exist: Subscription Carrier Plan and Anticipated Go-Live contracts",
    "Subscription Carrier Plan contracts do not reference an 'Anticipated Go-Live' date",
    "For Subscription Carrier Plan: Service start date uses the date listed on top left corner of document",
    "For Subscription Carrier Plan: Default months of service is 12 months unless stated otherwise",
    "For Anticipated Go-Live with MSA: Service start date uses the effective date of the agreement",
    "For Anticipated Go-Live without MSA: Service start date uses the 'Agreement Term Start Date'",
    "For Anticipated Go-Live with MSA: Months of service calculated from Effective Date to end of Initial Term (based on Go-Live date, not Effective date)",
    "For Anticipated Go-Live without MSA: Months of service calculated from Agreement Term Start Date to Agreement End Date",
    "Item Name should use the item name for associated products",
    "Item Description should copy list of included products under the product",
    "Integration Item should search for closest match; leave blank if no matches",
    "Billing Type is flat price",
    "Total Price uses the price listed in specified column (net of discount if applicable)",
    "Discounts should be made in the same billing term, not as separate billing term",
    "For billing start date: Type A uses same as service start date",
    "Monthly and annual billing is managed in Stripe with subscriptions",
    "Overages are being incorporated into billing"
  ],
  "exceptions": [
    "One-time implementation fees should be set to 0 for Subscription Carrier Plan contracts",
    "All contracts are different (annual vs monthly and amounts vary)",
    "Initial Term end date is based on Go-Live date, NOT Effective date for MSA contracts",
    "If discount exists, use price net of discount rather than original price",
    "Five reference contracts provided for guidance: 8bdfd688-7b22-4041-a374-8ffa3c49e0bf, 900415bd-38fb-4770-87e6-650b127e7bb8, 7baba1f6-0963-4b90-b5e5-31ba07ece52f, F0ff2929-4e87-458e-8e95-15b9012fbf4b, C5720058-bf00-4a91-92be-9c76687c739e"
  ],
  "merchant_specific": [
    "Contract structure varies by merchant (annual vs monthly, different amounts)",
    "Specific product names (e.g., 'Diesel Carrier Plan', 'Alvys Smart Text', 'Per Load Pricing', 'Managed EDI - Premium Diesel', 'EDI Trading Partner', 'Getting Started Package - Enterprise')",
    "Effective Date vs Start Date distinction specific to merchant's contract terminology",
    "Master Services Agreement (MSA) vs non-MSA contract handling",
    "Integration with Stripe for subscription management",
    "Merchant-specific billing cycles and overage policies",
    "One-off contract terms that need individual assessment",
    "Implementation Success team responsible for filling contract processing steps"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Merchant Info Sheet - Alvys_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:38

### Original Content
```
Merchant Demo date: Sep 25, 2024 Scoping start date: Sep 20, 2024 MSA Signature Date: Sep 26, 2024 Onboarding Kick Off Date: Nov 1, 2024 [If Exists] Opt Out Date: Apr 1st, 2025 Go Live Date: Dec 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant 1 person Finance team Director of Finance: Jordan Harris Company summary (AE to fill) Alvys is a cloud-based transportation management system with high-tech automation Alvys provides a logistics platform designed to streaml...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Timeline and Milestones",
    "Merchant Business Context and Goals",
    "Contract Terms and Opt-Out Provisions",
    "Billing and Revenue Model",
    "Stakeholder Management and Key Contacts"
  ],
  "rules": [
    {
      "rule": "Demo must occur before scoping start date",
      "evidence": "Demo date (Sep 25) follows Scoping start date (Sep 20) - appears to be chronological tracking"
    },
    {
      "rule": "MSA signature should occur before or around onboarding kick-off",
      "evidence": "MSA Signature Date: Sep 26, 2024; Onboarding Kick Off Date: Nov 1, 2024"
    },
    {
      "rule": "Go Live Date should be established during initial planning",
      "evidence": "Go Live Date: Dec 1, 2024 is documented upfront"
    },
    {
      "rule": "Opt-out date is calculated as 6 months after Go Live",
      "evidence": "Go Live Date: Dec 1, 2024; Opt Out Date: Apr 1st, 2025 (approximately 4 months shown, but stated as '6 months' in opt-out clause)"
    },
    {
      "rule": "Key stakeholders must be identified including GTM POC, Implementation POC, and Finance team contacts",
      "evidence": "Document requires GTM POC, Implementation POC, Director of Finance identified"
    },
    {
      "rule": "Company summary must be provided by AE",
      "evidence": "Company summary (AE to fill)"
    },
    {
      "rule": "Goals and North Star objectives must be documented by AE and Implementation team",
      "evidence": "Goals (North star) (AE Implementation to fill)"
    },
    {
      "rule": "ERP and Tax Integration systems must be identified",
      "evidence": "ERP: Tax Integration: fields present in document"
    },
    {
      "rule": "Billing model specifics must be documented including customer creation process",
      "evidence": "Billing model (AE Implementation to fill)"
    },
    {
      "rule": "Customer billing percentage at Go Live must be tracked in HubSpot",
      "evidence": "10 of customers are billed on Go Live, which is tracked in HS"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt-out clause is conditional",
      "condition": "Only applies if merchant has opt-out clause in contract (indicated by '[If Exists]')",
      "details": "Opt out after 6 months (Apr 1st, 2025)"
    },
    {
      "exception": "Merchant has specific hesitancy concerns that must be addressed to prevent opt-out",
      "condition": "Hesitancy that Tabs will actually work with his process and across his systems",
      "details": "Success criteria tied to proving system integration and process compatibility"
    },
    {
      "exception": "Non-standard customer billing at Go Live",
      "condition": "Only 10% of customers are billed at Go Live (implies 90% are not)",
      "details": "Suggests phased billing approach or specific customer segmentation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and industry",
      "value": "Alvys - cloud-based transportation management system",
      "customization_needed": true
    },
    {
      "element": "Key personnel names and titles",
      "value": "Director of Finance: Jordan Harris",
      "customization_needed": true
    },
    {
      "element": "Specific dates for all milestones",
      "value": "Demo, Scoping, MSA, Onboarding, Go Live, Opt-out dates",
      "customization_needed": true
    },
    {
      "element": "Merchant's pain points and goals",
      "value": "Revenue automation, automate invoicing, reporting, collections",
      "customization_needed": true
    },
    {
      "element": "Merchant's hesitancy factors",
      "value": "Concern about Tabs working with their process and systems",
      "customization_needed": true
    },
    {
      "element": "Billing model specifics",
      "value": "10% of customers billed on Go Live",
      "customization_needed": true
    },
    {
      "element": "ERP and Tax Integration systems",
      "value": "Not filled in this document but required fields",
      "customization_needed": true
    },
    {
      "element": "GTM POC and Implementation POC",
      "value": "Not filled in this document but required fields",
      "customization_needed": true
    },
    {
      "element": "Opt-out clause terms",
      "value": "6 months opt-out period, specific date",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Alvys_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:46

### Original Content
```
use the anticipated go-live date (circled in purple in example B ) Exception: sometime there is a one-time upfront investment on non-MSA contracts that are billed on the  agreement term start date  Frequency: usually 1 month, unless stated otherwise Period: however long the term is divided by the frequency; default term is 1 year For example, if the term is 1 year   12 months (term)   1 month (frequency)   12 make sure units are the same i e months Net Terms: default 0 unless stated otherwise Ex...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term Configuration and Revenue Schedule Setup",
    "Contract Type Handling (MSA vs Non-MSA, Type A vs Type B)",
    "Default Values and Operational Standards",
    "Usage-Based and Overage Billing",
    "Integration and Event Processing Workflows"
  ],
  "rules": [
    "For Type A contracts: use agreement term start date",
    "For Type B contracts: use anticipated go-live date",
    "Default frequency is 1 month unless stated otherwise",
    "Period calculation: term divided by frequency (default term is 1 year)",
    "Units must be consistent in calculations (e.g., months)",
    "Default net terms is 0 unless stated otherwise",
    "Billing timing is bill in advance, due start of period",
    "Type B contracts require an additional revenue schedule billing term for unit-based billing above contracted amount",
    "Usage-based billing terms should be billed first of next period (arrears)",
    "Tier unit pricing: first level up to contracted quantity is $0, second level above quantity is charged at listed rate",
    "Default service term if none listed: 1 year",
    "Default net payment terms if none listed: 30 days",
    "Default billing frequency if none listed: Monthly",
    "Every tax line item becomes a billing term (BT)",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted"
  ],
  "exceptions": [
    "One-time upfront investment on non-MSA contracts are billed on agreement term start date (not go-live date)",
    "One-time implementation fees are usually net 3 (requires double-checking)",
    "One-time implementation fees are billed first of period (different timing than standard)",
    "Non-MSA forms sometimes do not have per-load pricing product, in which case usage-based BT is not created",
    "Contract-specific processing requests may differ (e.g., back-dating invoice date to final day of month)",
    "Pinata integration items may have merchant-specific labeling exceptions"
  ],
  "merchant_specific": [
    "Anticipated go-live date varies by merchant/contract",
    "Term length may differ by contract",
    "Frequency may be specified differently per contract",
    "Net terms may vary by merchant agreement",
    "Per-load pricing rates and contracted quantities are merchant-specific",
    "Event tracking types (e.g., 'additional load') are merchant-dependent",
    "Processing specifics like invoice date back-dating are merchant-requested customizations",
    "Integration item labeling may have merchant-specific exceptions",
    "Post-processing communication requirements vary by merchant (who to notify and when)",
    "Events billing and integration items processing filled by Implementation Success team per merchant"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Alvys_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:56

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) Automating Go Live to start billing for his 10  of customers from HS Rew...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Success Notification and Communication Protocols",
    "Merchant Billing and Subscription Management",
    "Merchant Relationship and Stakeholder Management",
    "Feature Integration and Automation Requirements",
    "Implementation and Go-Live Process"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
      "category": "notification_protocol",
      "explicit": true
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success team",
      "category": "documentation_responsibility",
      "explicit": true
    },
    {
      "rule": "Feature Requests section must be filled by AE and Implementation Success team",
      "category": "documentation_responsibility",
      "explicit": true
    },
    {
      "rule": "Rewatch Calls section must be filled by AE and Implementation Success team",
      "category": "documentation_responsibility",
      "explicit": true
    },
    {
      "rule": "Notes sections should be ignored by Ops International Team",
      "category": "documentation_responsibility",
      "explicit": true
    },
    {
      "rule": "Notes sections must be filled by AE and Implementation teams",
      "category": "documentation_responsibility",
      "explicit": true
    },
    {
      "rule": "Documentation must include merchant temperament assessment",
      "category": "relationship_management",
      "explicit": true
    },
    {
      "rule": "Documentation must identify key POC (buyer/decision maker)",
      "category": "relationship_management",
      "explicit": true
    },
    {
      "rule": "Documentation must capture Tabs features that key POC cares about",
      "category": "feature_requirements",
      "explicit": true
    },
    {
      "rule": "Documentation must track special memos for certain invoices",
      "category": "billing_management",
      "explicit": true
    },
    {
      "rule": "Documentation must note invoice changes due to merchant-customer relationships",
      "category": "billing_management",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant is moving to all Annual billing but still has Monthly billing for majority of customers during transition",
      "context": "billing_transition",
      "impact": "Requires handling mixed billing cycles during migration period"
    },
    {
      "exception": "Only 10% of merchant's customers start getting billed on Go Live, not all customers",
      "context": "go_live_process",
      "impact": "Phased billing rollout rather than full activation"
    },
    {
      "exception": "Certain invoices require special memos",
      "context": "invoice_processing",
      "impact": "Custom handling for specific invoice types"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship dynamics",
      "context": "invoice_processing",
      "impact": "Flexibility required in invoice generation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Success contact person",
      "example": "Azmat Aziz",
      "customizable": true,
      "type": "stakeholder"
    },
    {
      "element": "Internal notification channel",
      "example": "Messari internal merchant channel",
      "customizable": true,
      "type": "communication"
    },
    {
      "element": "Billing model transition plan",
      "example": "Moving from Monthly to Annual with 10% phased rollout",
      "customizable": true,
      "type": "billing"
    },
    {
      "element": "Key POC and decision maker",
      "example": "Jordan Harris - Director of Finance",
      "customizable": true,
      "type": "stakeholder"
    },
    {
      "element": "Merchant temperament profile",
      "example": "Smart, experienced, easy to work with, somewhat skeptical",
      "customizable": true,
      "type": "relationship"
    },
    {
      "element": "Feature priorities",
      "example": "Stripe, QBO, Pandadocs integration; invoicing rollup; subscription automation",
      "customizable": true,
      "type": "features"
    },
    {
      "element": "Go-Live billing percentage",
      "example": "10% of customers",
      "customizable": true,
      "type": "implementation"
    },
    {
      "element": "Special invoice memo requirements",
      "example": "Certain invoices require special memos",
      "customizable": true,
      "type": "billing"
    },
    {
      "element": "Discovery and demo call recordings",
      "example": "Rewatch links with specific dates",
      "customizable": true,
      "type": "documentation"
    }
  ],
  "confidence_score": 0.85
}
```

---

