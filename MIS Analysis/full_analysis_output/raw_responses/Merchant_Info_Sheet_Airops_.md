# Raw LLM Analysis: Merchant Info Sheet - Airops_

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:50:14

---

## Chunk 1: Merchant Info Sheet - Airops__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:14

### Original Content
```
Merchant Demo date: Nov 4, 2024 Scoping start date: Nov 19, 2024 MSA Signature Date: Dec 10, 2024 Onboarding Kick Off Date: N A [If Exists] Opt Out Date: None Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Finance and ops: Aayush Daftari https: www linkedin com in aayushdaftari Company summary (AE to fill) Summary of what company does: AirOps lets you easily build and scale AI workflows to crush your growth targets Build with 40  AI models, retrieval, and...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Business Model and Use Case",
    "Usage-Based Billing Requirements",
    "Customer Segmentation and Flow Management",
    "Stakeholder Identification and Coordination"
  ],
  "rules": [
    "Tabs solution will only handle B2B segment billing, not PLG (Product-Led Growth) flow",
    "Customers should be expected to come from contract as the primary source",
    "Usage billing must be streamlined for B2B segment specifically",
    "PLG customers can graduate to classic B2B billing model",
    "Manual usage tracking in spreadsheets is the current pain point to be replaced",
    "Implementation requires identification of Finance and Operations key personnel",
    "Implementation requires designation of GTM POC and Implementation POC",
    "ERP and Tax Integration information must be documented during scoping"
  ],
  "exceptions": [
    "No opt-out clause exists for this merchant (marked as 'None')",
    "PLG flow is explicitly excluded from Tabs implementation scope",
    "PLG customers transitioning to B2B billing represent a special customer creation scenario",
    "Customer creation process has no unique requirements beyond standard contract-based flow with occasional PLG graduation"
  ],
  "merchant_specific": [
    "Merchant name: AirOps",
    "Business description: AI workflow building platform with 40+ AI models",
    "Dual business model: PLG and B2B with usage-based components",
    "Key contact: Aayush Daftari (Finance and Ops)",
    "Specific timeline: Demo (Nov 4, 2024), Scoping (Nov 19, 2024), MSA Signature (Dec 10, 2024)",
    "North star goal: Streamline usage billing tool for B2B segment",
    "Current state: Manual usage tracking in spreadsheets",
    "Customer segments: PLG users and B2B contract customers with potential crossover"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Airops__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:19

### Original Content
```
Information on how merchant bills See above How contract is broken up N A (Contract examples in Garage) One-off things to know about the merchant They use a affiliate platform called Rewardful that leverages stripe Merchant s overview: We have Builders (lets say like Influencers) who get a 20  commission for referrals that stay beyond 30 days They are setup in a system called Rewardful Currently we have 4 enterprises with the Rewardful process One of them just converted from a self-serve PLG use...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Affiliate/Referral Commission Management",
    "Payment Processing and Methods",
    "Contract Data Extraction and Customer Setup",
    "Integration with Third-Party Systems (Rewardful, Stripe, Tabs)",
    "Billing and Revenue Schedule Configuration"
  ],
  "rules": [
    "Builders (influencers) receive 20% commission for referrals that stay beyond 30 days",
    "Rewardful code must be entered in Stripe as metadata during customer setup",
    "Commission payouts are calculated at end of month and disbursed via PayPal",
    "Payment method selection depends on invoice size: smaller invoices use Credit Card, larger invoices use ACH",
    "Term length is found in first paragraph of contracts titled 'Term' and used for both billing and revenue schedules",
    "Effective date should use latest signature date; if no signature date exists, use date in contract name",
    "Customer name is found in opening paragraph of contract and document name",
    "Pricing and billing cadence information is located in Section 2 Pricing",
    "Subscription fees should be calibrated as flat price, usage fees as unit price",
    "Net terms information is found in Section 4",
    "Additional Tasks product should be created for all new customers by default",
    "Additional Tasks should start at the beginning of the month of the start date (e.g., if contract starts 6/20, product starts 6/1)",
    "When invoice sent with CC and ACH debit enabled, it automatically creates customer record in Stripe"
  ],
  "exceptions": [
    "One enterprise customer converted from self-serve PLG user to enterprise (special case)",
    "Currently 4 enterprises use the Rewardful process (limited scope)",
    "Expected conversions: a few every 6 months (low volume exception)",
    "For 1-2 customers paying via ACH credit: either switch to CC/ACH debit to maintain Rewardful flow, OR tag in Tabs with custom field for manual tracking",
    "All customers were already created (implementation note - may not apply to future state)",
    "Additional Tasks usage should use specific Integration Item (52 relations) not the auto-selected December 2023 item"
  ],
  "merchant_specific": [
    "Merchant uses 'Builders' terminology for influencers/affiliates",
    "Rewardful platform integration (third-party affiliate system)",
    "Specific product names: 'Platform Fees', 'Additional Tasks', 'AirOps Platform (14)', 'AirOps Professional Services (53)'",
    "Integration mapping reference: 'AirOps - Integration Items'",
    "Custom field tagging in Tabs system for tracking",
    "Specific contract structure with sections (Section 2 Pricing, Section 4 for Net Terms)",
    "Usage billing type (BT) of $1 for Additional Tasks",
    "Event name: 'Additional Tasks' for usage tracking",
    "PayPal as commission disbursement method",
    "Mix of payment methods (CC and ACH) based on merchant preference"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Airops__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:31

### Original Content
```
Payment Terms  If not found, default to net 30 Anything to ignore in contracts Everything in MSA after signature - just legalese Ignore all usage terms except Additional Tasks Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) N A Default Service Term If None Listed, Ops Default is 1 Year Can find in Section 1 Term Default Net Payment Terms If None, Ops Default is 0 See section 1 Steps to process Defaul...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational values and fallback rules",
    "Contract processing and data extraction guidelines",
    "Billing and invoicing configuration (payment terms, frequency, pricing)",
    "Usage-based billing and event processing (tasks as units)",
    "Communication and notification protocols for batch processing"
  ],
  "rules": [
    {
      "rule": "Default payment terms are Net 30 if not specified in contract",
      "category": "Payment Terms"
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Service Term",
      "source": "Section 1 Term"
    },
    {
      "rule": "Default net payment terms are 0 days if none specified",
      "category": "Payment Terms",
      "source": "Section 1"
    },
    {
      "rule": "Default billing frequency is Monthly if not specified",
      "category": "Billing Frequency",
      "source": "Section 2 Pricing"
    },
    {
      "rule": "All tax line items become BT (Billable Tax) by default if no other instruction",
      "category": "Tax Handling"
    },
    {
      "rule": "Ignore all content in MSA after signature (considered legalese)",
      "category": "Contract Processing"
    },
    {
      "rule": "Ignore all usage terms except Additional Tasks",
      "category": "Contract Processing"
    },
    {
      "rule": "For task-based pricing: divide rate by 1000 to get unit price for Garage system",
      "category": "Usage Billing",
      "example": "Rate $5/1000 tasks = Garage price $0.05/task"
    },
    {
      "rule": "Only usage type processed is 'tasks'",
      "category": "Events Processing"
    },
    {
      "rule": "Notify Jeff Kurzman when batch processing is complete",
      "category": "Communications"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific processing requests may differ by contract",
      "example": "Back-dating invoice date to final day of the month",
      "note": "Listed under 'Specifics' section"
    },
    {
      "exception": "Special memos may be required for certain customer invoices",
      "context": "Customer Information section"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationships",
      "context": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Additional Tasks processing requirements",
      "customizable": true,
      "note": "Only usage terms to not ignore"
    },
    {
      "element": "Back-dating invoice dates",
      "customizable": true,
      "note": "Example of merchant-specific processing request"
    },
    {
      "element": "Integration Items assignment (AirOps)",
      "customizable": true,
      "note": "Requires Implementation Success to fill"
    },
    {
      "element": "Post-processing notification recipients",
      "customizable": true,
      "example": "Customer Success [Azmat Aziz] via Messari internal merchant channel"
    },
    {
      "element": "Customer-specific memo requirements",
      "customizable": true,
      "note": "Varies by merchant customer relationship"
    },
    {
      "element": "Feature requests tracking",
      "customizable": true,
      "note": "Includes urgency and importance ratings"
    },
    {
      "element": "Contract sections to reference",
      "terminology": "Section 1 (Term), Section 2 (Pricing)",
      "note": "Standard document structure"
    },
    {
      "element": "Garage system",
      "terminology": "Internal billing/pricing system for data entry"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Airops__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:31

### Original Content
```
rewatch com video 3himxdvjj8tjrc1g-aayush-tabs-scoping-follow-up-november-27-2024 https: tabs rewatch com video kd894vy5o1r7o3hc-jarrett-tabs-aayush-november-12-2024 https: tabs rewatch com video nknwthislaqwq9rj-jarrett-tabs-aayush-november-5-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills: Usage via CVS Pass-through Revenue: For certain customers, they have a pass-through billing arrangement where costs incurred are directly passed...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing methodologies and arrangements",
    "Usage-based pricing and cost pass-through models",
    "Customer-specific billing exceptions and custom logic",
    "Overage charges and usage limit management",
    "Monthly billing cycles and volume tracking"
  ],
  "rules": [
    "Usage billing is conducted via CVS (Customer Verification System or similar)",
    "Pass-through revenue model: costs are billed directly to customers without markup",
    "Fixed limits with overage charges: predefined usage thresholds trigger additional fees for excess usage",
    "Standard usage is calculated up to a threshold before overage fees apply",
    "Billing occurs on a monthly basis",
    "Customer count/volume tracked: 56 customers under this billing structure",
    "AE (Account Executive) and Implementation teams are responsible for filling merchant billing information",
    "Ops International Team should ignore certain sections marked for AE/Implementation"
  ],
  "exceptions": [
    "Custom logic required for specific customers with legacy agreements",
    "Special negotiated terms may override standard billing rules",
    "Certain costs may be excluded from billing for specific customers based on predefined rules",
    "Special discounts may be applied to select customers requiring manual intervention",
    "Custom exceptions where certain charges are not billed or are adjusted",
    "Pass-through billing customers are exempt from markup calculations"
  ],
  "merchant_specific": [
    "Individual customer billing arrangements (pass-through vs. fixed limits vs. custom)",
    "Customer-specific usage thresholds and overage rates",
    "Legacy agreement terms that create unique billing requirements",
    "Negotiated discounts or cost exclusions per customer",
    "Manual intervention requirements for specific customer accounts",
    "Customer volume count (56) suggests this applies to a specific merchant or merchant segment",
    "CVS billing system integration may be merchant-specific"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: Merchant Info Sheet - Airops__chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:50:42

### Original Content
```
Yes Billing model: In arrears Yes Usage data files   They are good with uploading these themselves Are they all standard across all his clients Yes Our contact there says he fully expected to make manual adjustments on the invoice level to support point 3 Is there any important merchant relationship information He s part of FOG could be used as a future reference What is the merchant temperament Very cool very laid back Is there a key POC: (i e : who is the buyer decision maker ) Finance and ops...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing processes",
    "Client self-service capabilities and data management",
    "Merchant relationship and communication style",
    "Key stakeholder identification and product feature priorities",
    "Manual adjustment workflows and flexibility requirements"
  ],
  "rules": [
    "Billing model operates on an 'in arrears' basis (payment after service delivery)",
    "Usage data files are uploaded by the merchant themselves (self-service model)",
    "All processes/standards are consistent across all of the merchant's clients",
    "Manual adjustments at the invoice level are expected and supported",
    "Finance and operations team member (Aayush Daftari) serves as the primary point of contact and decision maker"
  ],
  "exceptions": [
    "Manual adjustments are expected to be made at the invoice level to accommodate specific needs (referenced as 'point 3', suggesting deviation from standard automated billing)",
    "Merchant is part of FOG (Friends of Group/special relationship category) which may warrant special treatment or priority consideration for future opportunities"
  ],
  "merchant_specific": [
    "Merchant name/identity: Part of 'FOG' group",
    "Primary POC: Aayush Daftari (Finance and Operations role)",
    "Merchant temperament: 'Very cool, very laid back' - suggests flexible communication style and lower urgency expectations",
    "Feature priorities: Usage billing, contract ingest, revenue reporting (specific to this merchant's needs)",
    "Self-service capability: Merchant handles their own usage data file uploads",
    "Client structure: Merchant has multiple clients of their own with standardized processes"
  ],
  "confidence_score": 0.85
}
```

---

