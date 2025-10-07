# Raw LLM Analysis: Merchant Info Sheet - Airops_(1)

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 12:04:35

---

## Chunk 1: Merchant Info Sheet - Airops_(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:04:35

### Original Content
```
Merchant Demo date: Nov 4, 2024 Scoping start date: Nov 19, 2024 MSA Signature Date: Dec 10, 2024 Onboarding Kick Off Date: N A [If Exists] Opt Out Date: None Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Finance and ops: Aayush Daftari https: www linkedin com in aayushdaftari Company summary (AE to fill) Summary of what company does: AirOps lets you easily build and scale AI workflows to crush your growth targets Build with 40  AI models, retrieval, and...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Business Model and Product Offering",
    "Usage-Based Billing Requirements",
    "Customer Segmentation and Flow Management",
    "Stakeholder Identification and Roles"
  ],
  "rules": [
    "Tabs integration will only handle B2B segment billing, not PLG (Product-Led Growth) flow",
    "Customers should be expected to come from contract as the primary source",
    "Usage billing must be streamlined for B2B segment specifically",
    "Manual usage tracking in spreadsheets is the current pain point to be resolved",
    "Implementation requires identification of Finance and Operations key personnel",
    "Implementation requires identification of GTM POC and Implementation POC",
    "ERP and Tax Integration details must be documented during scoping",
    "Merchant goals and pain points must be clearly defined before implementation"
  ],
  "exceptions": [
    "PLG customers can graduate to classic B2B billing (transition case)",
    "No opt-out clause exists for this merchant (deviation from standard contract structure)",
    "No unique customer creation process requirements (standard process applies)",
    "Onboarding Kick Off Date marked as N/A (non-standard timeline)"
  ],
  "merchant_specific": [
    "Merchant name: AirOps",
    "Business model: Dual PLG and B2B with usage-based pricing",
    "Product description: AI workflow building platform with 40+ AI models",
    "Key contact: Aayush Daftari (Finance and Ops)",
    "Specific timeline: Demo Nov 4, 2024; Scoping Nov 19, 2024; MSA Dec 10, 2024",
    "Current process: Manual usage tracking in spreadsheets",
    "Integration scope: B2B segment only, excluding PLG flow",
    "Customer transition pattern: PLG to B2B graduation pathway"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Airops_(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:04:43

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
    "Contract Data Extraction and Processing",
    "Customer Setup and Metadata Tracking",
    "Integration with Third-Party Platforms (Rewardful, Stripe, Tabs)"
  ],
  "rules": [
    {
      "rule": "Builders (influencers) receive 20% commission for referrals that stay beyond 30 days",
      "category": "Commission Structure"
    },
    {
      "rule": "Rewardful code must be entered in Stripe as metadata during customer setup",
      "category": "Customer Setup"
    },
    {
      "rule": "Commission payouts are calculated at end of month and disbursed via PayPal",
      "category": "Payment Processing"
    },
    {
      "rule": "Payment method selection depends on invoice size: smaller invoices use Credit Card, larger invoices use ACH",
      "category": "Payment Methods"
    },
    {
      "rule": "Term length is found in first paragraph of contracts titled 'Term' and used for both billing and revenue schedules",
      "category": "Contract Processing"
    },
    {
      "rule": "Effective date should use latest signature date; if no signature date exists, use date in contract name",
      "category": "Contract Processing"
    },
    {
      "rule": "Item names follow standard mapping: 'Platform Fees' for software subscription, 'Usage Fees' for usage component",
      "category": "Contract Processing"
    },
    {
      "rule": "Pricing and billing cadence information is found in Section 2 Pricing",
      "category": "Contract Processing"
    },
    {
      "rule": "Subscription fees should be calibrated as flat price, usage fees as unit price",
      "category": "Pricing Configuration"
    },
    {
      "rule": "Additional Tasks should use 'Usage BT for $1' and be billed 'Month in arrears'",
      "category": "Contract Processing"
    },
    {
      "rule": "Net Terms are found in Section 4 of contracts",
      "category": "Contract Processing"
    },
    {
      "rule": "Customer name can be found in opening paragraph of contract and document name",
      "category": "Customer Creation"
    },
    {
      "rule": "All customers were already created; only create if none exists",
      "category": "Customer Creation"
    }
  ],
  "exceptions": [
    {
      "exception": "One enterprise customer converted from self-serve PLG user to enterprise",
      "context": "Existing customer transition"
    },
    {
      "exception": "For 1 or 2 customers currently paying via ACH credit, two options exist: switch to CC/ACH debit to maintain Rewardful flow, or tag in Tabs with custom field for manual tracking",
      "context": "ACH credit payment handling"
    },
    {
      "exception": "Expected conversion rate is low but could see a few conversions every 6 months",
      "context": "Self-serve to enterprise conversions"
    },
    {
      "exception": "Currently 4 enterprises use the Rewardful process",
      "context": "Limited scope of affiliate program"
    }
  ],
  "merchant_specific": [
    {
      "element": "Rewardful platform integration",
      "description": "Third-party affiliate platform specific to this merchant's referral program"
    },
    {
      "element": "Builder terminology",
      "description": "Merchant uses 'Builders' instead of generic 'affiliates' or 'influencers'"
    },
    {
      "element": "20% commission rate for 30+ day retention",
      "description": "Specific commission structure and retention period"
    },
    {
      "element": "Integration Items mapping reference",
      "description": "References specific mapping document 'AirOps - Integration Items'"
    },
    {
      "element": "PayPal disbursement method",
      "description": "Specific payment method for commission payouts"
    },
    {
      "element": "Contract structure references",
      "description": "Specific section numbers (Section 2 for Pricing, Section 4 for Net Terms)"
    },
    {
      "element": "Tabs platform usage",
      "description": "Custom field tagging and reporting in Tabs system"
    },
    {
      "element": "Mix of PLG and enterprise customers",
      "description": "Business model includes self-serve product-led growth conversions"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Airops_(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:04:54

### Original Content
```
rewatch com video 3himxdvjj8tjrc1g-aayush-tabs-scoping-follow-up-november-27-2024 https: tabs rewatch com video kd894vy5o1r7o3hc-jarrett-tabs-aayush-november-12-2024 https: tabs rewatch com video nknwthislaqwq9rj-jarrett-tabs-aayush-november-5-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills: Usage via CVS Pass-through Revenue: For certain customers, they have a pass-through billing arrangement where costs incurred are directly passed...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing methodologies and arrangements",
    "Usage-based pricing and cost pass-through",
    "Customer-specific billing exceptions and custom logic",
    "Overage charges and usage limits",
    "Monthly billing cycles and volume tracking"
  ],
  "rules": [
    "Usage billing is conducted via CVS (Customer Value System or similar)",
    "Pass-through revenue model: actual usage costs are billed without markup or additional calculation",
    "Fixed limits with overage charges: predefined usage thresholds trigger additional fees when exceeded",
    "Standard usage is calculated up to a threshold before overage fees apply",
    "Billing occurs on a monthly basis",
    "Customer count and volume tracking is required (56 customers mentioned)",
    "Implementation team (AE Implementation) is responsible for filling merchant billing information",
    "International/Ops team should ignore certain sections marked accordingly"
  ],
  "exceptions": [
    "Custom logic required for specific customers with legacy agreements",
    "Special negotiated terms may override standard billing rules",
    "Certain costs may be excluded from billing for specific customers based on predefined rules",
    "Special discounts may apply to particular customers requiring manual intervention",
    "Custom exceptions where specific charges are not billed or are adjusted",
    "Pass-through billing customers are exempt from markup calculations"
  ],
  "merchant_specific": [
    "Billing method selection (pass-through vs. fixed limits vs. custom logic)",
    "Usage threshold limits for overage calculations",
    "Legacy agreement terms and conditions",
    "Negotiated special terms and discounts",
    "Specific cost exclusions or adjustments",
    "Customer volume (56 customers noted, may vary per merchant)",
    "CVS integration and usage tracking methodology",
    "Manual intervention requirements for custom billing scenarios"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Merchant Info Sheet - Airops_(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:04:54

### Original Content
```
Payment Terms  If not found, default to net 30 Anything to ignore in contracts Everything in MSA after signature - just legalese Ignore all usage terms except Additional Tasks Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) N A Default Service Term If None Listed, Ops Default is 1 Year Can find in Section 1 Term Default Net Payment Terms If None, Ops Default is 0 See section 1 Steps to process Defaul...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Contract processing and data extraction guidelines",
    "Billing and invoicing configuration rules",
    "Usage-based pricing and task calculation methods",
    "Communication and notification protocols for processing completion"
  ],
  "rules": [
    {
      "rule": "Default payment terms are Net 30 if not specified in contract",
      "category": "Payment Terms"
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Service Terms",
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
      "rule": "All tax line items default to BT (Billable Tax) if no other instruction",
      "category": "Tax Handling"
    },
    {
      "rule": "Only usage type tracked is 'tasks' for events processing",
      "category": "Usage Billing"
    },
    {
      "rule": "When rate is displayed per 1000 tasks, divide price by tasks to get unit price for Garage system",
      "category": "Rate Calculation",
      "example": "Rate $5/1000 tasks = Garage price $0.05/task"
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
      "rule": "Notify Jeff Kurzman when batch processing is complete",
      "category": "Post-Processing Communications"
    }
  ],
  "exceptions": [
    {
      "exception": "Additional Tasks usage terms should NOT be ignored (exception to general usage terms rule)",
      "context": "Contract processing"
    },
    {
      "exception": "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice dates to final day of month)",
      "context": "Invoice processing specifics"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "context": "Customer-specific billing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract-specific processing instructions",
      "description": "Merchants may request unique processing rules like back-dating invoices to month-end",
      "customizable": true
    },
    {
      "element": "Customer Information section",
      "description": "Merchant-specific customer details, special memos, and invoice requirements",
      "customizable": true
    },
    {
      "element": "Integration Items",
      "description": "Merchant-specific integration assignments (AirOps mentioned as example)",
      "customizable": true
    },
    {
      "element": "Post-Processing Communications",
      "description": "Notification recipients and timing vary by merchant phase (Implementation vs Active)",
      "customizable": true,
      "example": "Customer Success [Azmat Aziz] notified in Messari internal channel when contracts processed in Active phase"
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific feature requests tracked with importance and urgency",
      "customizable": true
    },
    {
      "element": "Events Processing",
      "description": "Only applicable if necessary for specific merchant",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document is somewhat fragmented and appears to be a template or form with incomplete sections. While the core operational defaults and rules are clear, some sections are marked as "(Implementation Success to fill)" indicating incomplete information. The structure suggests this is a standardized template with merchant-specific customization points, but the formatting and incomplete nature of some sections reduces confidence in capturing all nuances.

---

## Chunk 5: Merchant Info Sheet - Airops_(1)_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:05:04

### Original Content
```
Yes Billing model: In arrears Yes Usage data files   They are good with uploading these themselves Are they all standard across all his clients Yes Our contact there says he fully expected to make manual adjustments on the invoice level to support point 3 Is there any important merchant relationship information He s part of FOG could be used as a future reference What is the merchant temperament Very cool very laid back Is there a key POC: (i e : who is the buyer decision maker ) Finance and ops...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing processes",
    "Merchant relationship management and temperament",
    "Data management and file handling",
    "Key stakeholder identification and decision-making",
    "Product feature requirements and preferences"
  ],
  "rules": [
    "Billing model operates in arrears (payment after service delivery)",
    "Usage data files are uploaded by the merchant themselves (self-service model)",
    "Manual adjustments are expected and accepted at the invoice level",
    "Standard processes are consistent across all of the merchant's clients",
    "Finance and operations personnel serve as the primary point of contact for decision-making"
  ],
  "exceptions": [
    "Manual invoice-level adjustments are required to support specific merchant needs (referenced as 'point 3')",
    "Despite standard processes, flexibility exists for invoice modifications",
    "Merchant is part of FOG (special relationship group) which may warrant different handling or priority treatment"
  ],
  "merchant_specific": [
    "Merchant temperament: 'Very cool, very laid back' - suggests flexible communication style and less urgent escalation needs",
    "Key POC: Aayush Daftari (Finance and Operations role)",
    "FOG membership status - indicates special relationship tier or reference group",
    "Required Tabs features: Usage billing, contract ingest, revenue reporting",
    "Self-service capability for usage data file uploads",
    "Expectation setting: merchant proactively expects to make manual adjustments"
  ],
  "confidence_score": 0.85
}
```

---

