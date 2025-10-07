# Raw LLM Analysis: Audiense Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:52:00

---

## Chunk 1: Audiense Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:52:00

### Original Content
```
Merchant Demo date: Jun 12, 2025 Scoping start date: Jun 25, 2025 MSA Signature Date:Jun 30, 2025 Onboarding Kick Off Date: TBD [If Exists] Opt Out Date: none Go Live Date: Targeting Mid Q4 2025 (Sep Oct) GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CFO: Marc Thomas Finance Lead   Onboarding POC: Stacey Sundal Revenue Ops Lead: Juan S Angel Customer Success: TBD (but Juan has systems integration oversight) Billing Accounts Receivable POC: Juan S Angel Company summary...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Migration and System Consolidation Goals",
    "Billing and Revenue Operations Requirements",
    "Multi-channel and International Business Complexity"
  ],
  "rules": [
    {
      "rule": "Document must capture demo date, scoping start date, MSA signature date, and go-live date",
      "category": "Timeline Management",
      "explicit": true
    },
    {
      "rule": "Key stakeholders must be identified including CFO, Finance Lead, Onboarding POC, Revenue Ops Lead, Customer Success, and Billing/AR POC",
      "category": "Stakeholder Management",
      "explicit": true
    },
    {
      "rule": "Company summary must include what the company does, provided by Account Executive",
      "category": "Merchant Profile",
      "explicit": true
    },
    {
      "rule": "Goals section must document merchant's objectives, pain points being solved, and reason for purchase",
      "category": "Requirements Gathering",
      "explicit": true
    },
    {
      "rule": "Opt-out clause status and conditions must be documented",
      "category": "Contract Terms",
      "explicit": true
    },
    {
      "rule": "Billing model documentation must cover customer creation process, billing methodology, and contract structure",
      "category": "Billing Operations",
      "explicit": true
    },
    {
      "rule": "Implementation POC and GTM POC roles must be assigned",
      "category": "Project Management",
      "explicit": true
    },
    {
      "rule": "ERP and Tax Integration systems should be identified if applicable",
      "category": "Technical Integration",
      "explicit": true
    },
    {
      "rule": "Contract processing steps must be documented by Implementation Success team",
      "category": "Implementation Process",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Onboarding Kick Off Date may be 'TBD' if not yet determined",
      "condition": "Early stage implementations"
    },
    {
      "exception": "Opt Out Date can be 'none' if no opt-out clause exists",
      "condition": "Contract terms dependent"
    },
    {
      "exception": "Customer Success POC may be 'TBD' with interim oversight assigned to another role",
      "condition": "Resource allocation pending"
    },
    {
      "exception": "Go Live Date can be expressed as a target range rather than specific date",
      "condition": "Planning phase with flexibility needed"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company geographic footprint",
      "example": "Operations across 70 countries with concentration in US and UK",
      "customization_needed": true
    },
    {
      "element": "Sales channel mix",
      "example": "Direct, self-serve, and partner-led channels",
      "customization_needed": true
    },
    {
      "element": "Legacy systems to migrate from",
      "example": "Recurly, Xero, ChartMogul",
      "customization_needed": true
    },
    {
      "element": "Target systems to consolidate to",
      "example": "Tabs for billing, Stripe for self-serve",
      "customization_needed": true
    },
    {
      "element": "Compliance requirements",
      "example": "Multi-currency and VAT-compliant invoicing",
      "customization_needed": true
    },
    {
      "element": "Business model type",
      "example": "SaaS-focused subscription business",
      "customization_needed": true
    },
    {
      "element": "Specific pain points",
      "example": "Manual revenue recognition, fragmented billing systems",
      "customization_needed": true
    },
    {
      "element": "Analytics requirements",
      "example": "ARR/MRR analytics replacement",
      "customization_needed": true
    },
    {
      "element": "Ownership structure",
      "example": "Recently acquired by parent company",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Audiense Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:52:01

### Original Content
```
Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any importa...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Processing Parameters and Operational Standards",
    "Billing Model Segmentation (Self-Serve, Managed Services, Partner-Led)",
    "Tax Handling and Multi-Currency Operations",
    "Integration Item Classification and Labeling",
    "Post-Processing Communication and Stakeholder Notification"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Contract Defaults"
    },
    {
      "rule": "Default net payment terms is 0 (net zero/immediate) if none specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Billing Frequency"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax) Events Processing item",
      "category": "Tax Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Classification"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Item Classification"
    },
    {
      "rule": "VAT logic applied manually following UK and EU rules",
      "category": "Tax Processing"
    },
    {
      "rule": "Contracts are priced in USD, GBP, or EUR depending on customer",
      "category": "Currency Management"
    },
    {
      "rule": "Most invoices are flat-fee with few usage-based",
      "category": "Billing Structure"
    },
    {
      "rule": "Professional services tied to go-live dates",
      "category": "Service Delivery"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice date may be back-dated to final day of the month per specific merchant contract",
      "condition": "Contract-specific requirement"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by merchant",
      "condition": "Merchant override"
    },
    {
      "exception": "Special memos required for certain invoices due to merchant-customer relationships",
      "condition": "Customer-specific requirements"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship specifics",
      "condition": "Relationship-based modifications"
    },
    {
      "exception": "Recurly used for analytics and subscription tracking but not for partner deal billing",
      "condition": "Partner-led billing model"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model segmentation",
      "details": "Self-Serve (30% customers, 5% revenue via Recurly/Stripe/PayPal), Managed Services (70% customers, majority revenue via Xero), Partner-Led (monthly data reconciliation via Xero)"
    },
    {
      "element": "Post-processing notification requirements",
      "details": "Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase"
    },
    {
      "element": "Integration item labeling",
      "details": "Specific rules for Statsig and Pinata integrations that may vary by merchant"
    },
    {
      "element": "Customer-specific invoice requirements",
      "details": "Special memos and invoice changes based on individual customer relationships"
    },
    {
      "element": "Merchant temperament",
      "details": "Collaborative, eager to partner - affects communication approach"
    },
    {
      "element": "Multi-currency support",
      "details": "USD, GBP, EUR pricing based on customer location"
    },
    {
      "element": "Tax handling approach",
      "details": "Manual VAT logic for UK/EU, no sales tax currently implemented"
    },
    {
      "element": "Platform usage",
      "details": "Xero for invoicing, Recurly for analytics, multiple payment processors (Stripe, PayPal)"
    }
  ],
  "confidence_score": 0.92
}
```

---

