# Raw LLM Analysis: Merchant Info Sheet - FindMine

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:28:13

---

## Chunk 1: Merchant Info Sheet - FindMine_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:13

### Original Content
```
Add-ons, details above Auto-renewals - there will always be a new document so never process auto-renewal Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Annual How do we handle taxes as a line item If None Listed, Ops Default is every...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Document processing rules and workflows",
    "Merchant-specific customization and special handling",
    "Communication protocols and stakeholder notifications",
    "Integration and billing configuration"
  ],
  "rules": [
    {
      "rule": "Never process auto-renewal documents; always wait for new document",
      "category": "Processing Policy",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Default Values",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 30 days if none specified",
      "category": "Default Values",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Annual if none listed",
      "category": "Default Values",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) if no other instruction provided",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Notes Sections filled by AE/Implementation",
      "category": "Team Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Contract-specific processing variations (e.g., back-dating invoice date to final day of month)",
      "context": "Specifics processing section indicates merchant may have differing requirements by contract"
    },
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "context": "Integration Items Processing"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationship",
      "context": "Customer Information section"
    },
    {
      "exception": "Each customer has bespoke pricing and terms",
      "context": "Merchant billing structure with tiered subscriptions and varying usage components"
    }
  ],
  "merchant_specific": [
    {
      "element": "Post-processing notification requirements",
      "description": "Who to notify, where, and when after batch processing completion",
      "customizable": true,
      "example": "Customer Success [Azmat Aziz] notification in Messari internal merchant channel when contracts processed in Active phase"
    },
    {
      "element": "Integration item labeling rules",
      "description": "Specific labels for different integration types",
      "customizable": true,
      "example": "Statsig → Sales, Pinata → Software Subscription Bundle"
    },
    {
      "element": "Customer-specific invoice requirements",
      "description": "Special memos and invoice changes based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Events billing processing instructions",
      "description": "Important information on events billing to be filled by Implementation Success",
      "customizable": true
    },
    {
      "element": "Contract back-dating rules",
      "description": "Specific date manipulation requirements per merchant contract",
      "customizable": true,
      "example": "Back-date invoice date to final day of the month"
    },
    {
      "element": "Feature requests",
      "description": "Usage-based revenue recognition and other merchant-specific feature needs",
      "customizable": true
    },
    {
      "element": "Merchant relationship context",
      "description": "Key stakeholder information and relationship dynamics",
      "customizable": true,
      "example": "LJ is engaged and excited, Michelle is CEO, need support with bespoke agreement management"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - FindMine_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:16

### Original Content
```
Merchant Demo date: Sep 20, 2024 Scoping start date: Sep 30, 2024 MSA Signature Date: Sep 30, 2024 Onboarding Kick Off Date: Oct 1, 2024 [If Exists] Opt Out Date: N A Go Live Date: Nov 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Chief of Staff: Lauren Jones Company summary (AE to fill) FindMine inspires shoppers throughout their journey with on-brand, dynamic, and inventory-aware outfitting   styling The world s leading brands like Lululemon, Gap, and Anine ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Structure",
    "Subscription Tier Management",
    "Revenue Recognition and Scheduling",
    "Contract Components and Add-ons",
    "Implementation and Onboarding Timeline"
  ],
  "rules": [
    {
      "rule": "Default tier processing: Only the bottom tier applies when multiple tiers are listed",
      "category": "Subscription Tiers",
      "specificity": "Tier option 1 is the most common and should be the default method"
    },
    {
      "rule": "Annual Subscription Fees should use Integration Item: Annual Subscription Fees, Category: Platform",
      "category": "Billing Terms"
    },
    {
      "rule": "Implementation Fee defaults to 1 month revenue schedule, Integration Item: Implementation, Category: Implementation",
      "category": "Billing Terms"
    },
    {
      "rule": "Professional Services should use Integration Item: Professional Services, Category: Professional Services",
      "category": "Billing Terms"
    },
    {
      "rule": "Early payment discounts must be processed as a separate negative BT on the effective date",
      "category": "Discounts",
      "specificity": "Integration Item: Discount, Category: Discount"
    },
    {
      "rule": "Add-ons (hourly professional services, additional products) should be IGNORED and not processed",
      "category": "Contract Processing"
    },
    {
      "rule": "Default invoice cadence is Annual if not specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default net payment terms are 30 days if not specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default contract term is 1 year if not stated",
      "category": "Contract Terms"
    },
    {
      "rule": "Default to effective date for first annual bill; if no effective date, use sign date",
      "category": "Billing Dates"
    },
    {
      "rule": "For amendments that adjust contract amounts: End the original rev schedule and create new rev schedule and BT for updated product",
      "category": "Amendments"
    },
    {
      "rule": "Check MSA for invoice cadence or net payment terms if not on order form",
      "category": "Contract Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Tier option 2: Customer moves through tiers throughout the contract",
      "condition": "Only process this way if contract explicitly states tiers will automatically apply",
      "note": "This is rare - only one contract like this exists"
    },
    {
      "exception": "Tier option 2 proration schedule",
      "details": [
        "First tier bills at contract beginning",
        "Next tier bills 6 months in, prorated to annualize",
        "Next tier bills 9 months in, prorated to annualize",
        "If multi-year, 2nd annual invoice uses final tier at full annual rate"
      ]
    },
    {
      "exception": "Tier upgrades require amendments",
      "condition": "When customer moves to next tier under Tier option 1",
      "note": "Next tier up is reference only unless amendment is received"
    },
    {
      "exception": "Professional services can be added at flat rate",
      "condition": "When included in contract",
      "action": "Process as stated in contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant identity and business model",
      "details": "FindMine - AI-powered outfitting/styling platform for brands like Lululemon, Gap, Anine Bing"
    },
    {
      "element": "Current infrastructure",
      "details": "No infrastructure outside of QuickBooks Online (QBO)"
    },
    {
      "element": "Contract complexity",
      "details": "Very large, complex, unique contracts requiring administration infrastructure"
    },
    {
      "element": "Billing model specifics",
      "details": "Mostly tiered subscription with some usage components depending on customer"
    },
    {
      "element": "Remittance use cases",
      "details": "Rebates for business referrals and other clauses"
    },
    {
      "element": "Key personnel",
      "details": "Chief of Staff: Lauren Jones"
    },
    {
      "element": "Timeline",
      "details": {
        "demo_date": "Sep 20, 2024",
        "scoping_start": "Sep 30, 2024",
        "msa_signature": "Sep 30, 2024",
        "onboarding_kickoff": "Oct 1, 2024",
        "go_live": "Nov 1, 2024"
      }
    },
    {
      "element": "Opt-out status",
      "details": "No opt out (N/A)"
    },
    {
      "element": "Contract structure variability",
      "details": "Many types of contract structures with overlapping terms between various structures"
    },
    {
      "element": "BT naming convention",
      "details": "Name should match contract terminology (e.g., 'Tier X Subscription Fee')"
    }
  ],
  "confidence_score": 0.92
}
```

---

