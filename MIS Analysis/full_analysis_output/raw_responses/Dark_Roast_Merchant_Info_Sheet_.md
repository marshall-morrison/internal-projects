# Raw LLM Analysis: Dark Roast Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:34:53

---

## Chunk 1: Dark Roast Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:53

### Original Content
```
rewatch com video t340da1q1s9ejqyp-tabs-dark-roast-follow-up-october-15-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Today, when someone wants to buy he just sets up a stripe subscription Monthly flat Soon to add variables Is there any important merchant relationship information 1) What is the merchant temperament Very very cool 2) Is there a key POC: (i e : who is the buyer decision maker ) CEO- Trevor 3) What are the Tabs featur...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing and payment setup",
    "Merchant relationship management and communication",
    "Product feature priorities and requirements",
    "Implementation and operational workflows",
    "Subscription and payment processing methods"
  ],
  "rules": [
    "International Operations team should ignore certain sections marked for Account Executive (AE) and Implementation",
    "Current billing method uses Stripe subscription setup",
    "Billing frequency is monthly with flat rate structure",
    "Variable billing features are planned to be added in the future",
    "Key decision maker (CEO) must be identified for merchant relationships",
    "Merchant temperament assessment is required as part of relationship documentation",
    "Point of contact (POC) identification is mandatory for merchant setup"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' should be excluded from international operations team workflows",
    "Current flat-rate billing will transition to include variable components (timing not specified)",
    "ACH payment method is a special requirement for this merchant alongside standard features"
  ],
  "merchant_specific": [
    "Merchant temperament: 'Very very cool' - indicates relationship quality assessment",
    "Key POC: CEO named Trevor - specific decision maker",
    "Priority features: Variable billing and ACH payment processing",
    "Current payment processor: Stripe",
    "Billing structure: Monthly flat rate (transitioning to variable)",
    "Video reference: 'rewatch com video t340da1q1s9ejqyp-tabs-dark-roast-follow-up-october-15-2024' - merchant-specific documentation",
    "Company context: 'Dark Roast' appears to be merchant name or project code"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Dark Roast Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:34:58

### Original Content
```
Merchant Demo date: Oct 11 th Scoping start date: October 15th MSA Signature Date: October 17th Onboarding Kick Off Date: October 28th [If Exists] Opt Out Date: n a Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Trevor Pare Company Summary (AE to fill) Design subscription of CPG Brands Goals (North star) (AE  Implementation to fill) They were spending  9K per billing cycle on Stripe fees Stripe is great for SaaS, but wont work as they add services an...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Billing Model and Payment Processing",
    "Contract Processing and Configuration",
    "Integration and Tax Handling",
    "Customer-Specific Requirements and Communications"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Handling",
      "explicit": true
    },
    {
      "rule": "Contracts are billed at the beginning of each term",
      "category": "Billing Model",
      "explicit": true
    },
    {
      "rule": "Quarterly billing equals 3 months per billing cycle",
      "category": "Billing Model",
      "explicit": true
    },
    {
      "rule": "Operations team may need to notify stakeholders upon completion of processing batches",
      "category": "Post Processing Communications",
      "explicit": true
    },
    {
      "rule": "Integration items must be properly labeled according to merchant specifications",
      "category": "Integration Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant has both Canadian and US accounts requiring separate money flow based on billing location",
      "context": "Multi-country payment routing"
    },
    {
      "exception": "No formal contracts exist, only spreadsheet of customer info",
      "context": "Customer creation process"
    },
    {
      "exception": "Start date appears on 2 different dates causing confusion",
      "context": "Contract template questions"
    },
    {
      "exception": "Merchant may request invoice dates to be back-dated to final day of month",
      "context": "Contract-specific processing variations"
    },
    {
      "exception": "Special memos may be required for certain invoices based on customer relationships",
      "context": "Customer-specific invoicing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Demo date, Scoping start date, MSA Signature Date, Onboarding Kick Off Date, Go Live Date",
      "type": "Timeline milestones",
      "customizable": true
    },
    {
      "element": "GTM POC and Implementation POC assignments",
      "type": "Team assignments",
      "customizable": true
    },
    {
      "element": "ERP and Tax Integration systems",
      "type": "Technical integration",
      "customizable": true
    },
    {
      "element": "Key people at Merchant (CEO name)",
      "type": "Stakeholder information",
      "customizable": true
    },
    {
      "element": "Company Summary and Goals (North star)",
      "type": "Business context",
      "customizable": true
    },
    {
      "element": "Current billing system (e.g., Stripe)",
      "type": "Legacy system",
      "customizable": true
    },
    {
      "element": "Integration item labeling rules (e.g., Statsig, Pinata)",
      "type": "Product/service categorization",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements and recipients",
      "type": "Communication workflow",
      "customizable": true
    },
    {
      "element": "Feature requests tracking",
      "type": "Product enhancement",
      "customizable": true
    },
    {
      "element": "Rewatch call recordings",
      "type": "Documentation reference",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

