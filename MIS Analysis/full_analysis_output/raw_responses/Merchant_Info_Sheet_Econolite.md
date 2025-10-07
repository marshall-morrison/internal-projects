# Raw LLM Analysis: Merchant Info Sheet - Econolite

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:13:58

---

## Chunk 1: Merchant Info Sheet - Econolite_chunk_0

**Chunk Type**: context  
**Analysis Time**: 2025-10-02 11:13:58

### Original Content
```
fcusMerchant Scoping start date: N A Implementation Completed Date (Go live date): N A MSA Signature Date: Mar 31, 2024 ERP: Bespoke then to Dynamics Tax Integration: GTM POC: Implementation POC: ERP:   SailPoint Tax Integration: N A Key people at Merchant Huy Huynh (VP of Finance) Brenda Leto (Project Finance) Christopher Chen (New hire for finance) Serey Kim (AR automation) Jennifer Lleva (AR automation) Company summary Econolite is a company that develops traffic management software to improv...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Customer Setup Process",
    "Software Maintenance Agreement (SMA) Billing Model",
    "Customer Naming Conventions and Hierarchy",
    "Contract Term and Pricing Management",
    "Accuracy Requirements for Multi-Year Contracts"
  ],
  "rules": [
    {
      "rule": "Customer name must be extracted from the section containing 'hereafter referred to as Agency'",
      "category": "Customer Setup"
    },
    {
      "rule": "Use naming convention before 'hereafter referred to as Agency' when creating customers",
      "category": "Customer Setup"
    },
    {
      "rule": "Create customer manually when no ERP is linked",
      "category": "Customer Setup"
    },
    {
      "rule": "Check for Path Master (distributors) and create sub-customer based on contract, associating it as sub-customer",
      "category": "Customer Hierarchy"
    },
    {
      "rule": "Item descriptions must be extracted from the highlighted section in contract",
      "category": "Item Processing"
    },
    {
      "rule": "Start Date should be determined by looking for 'Coverage effective Period'",
      "category": "Contract Terms"
    },
    {
      "rule": "Contract cadence is typically 1 year (most common), 2 years, or more years",
      "category": "Contract Terms"
    },
    {
      "rule": "Multi-year contracted terms must be captured correctly with high accuracy",
      "category": "Contract Terms"
    },
    {
      "rule": "Net Terms should be based on contract specifications",
      "category": "Payment Terms"
    },
    {
      "rule": "Pricing must be verified against signature date to confirm early pricing or preferential pricing locks",
      "category": "Pricing"
    },
    {
      "rule": "Review updated contracts for clearer pricing boxes for easier pricing review",
      "category": "Pricing"
    }
  ],
  "exceptions": [
    {
      "exception": "Econolite does not have an ERP linked, requiring manual customer creation",
      "context": "Standard process may assume ERP integration"
    },
    {
      "exception": "Some contracts have terms longer than 1 year, requiring special attention to accuracy",
      "context": "1 year is most common, but multi-year terms exist"
    },
    {
      "exception": "Early pricing or preferential pricing may be locked based on signature date",
      "context": "Standard pricing may not apply if early/preferential pricing was secured"
    },
    {
      "exception": "Path Master acts as distributor requiring sub-customer creation",
      "context": "Standard customer setup vs. distributor relationship"
    }
  ],
  "merchant_specific": [
    {
      "element": "Business Type: Software Maintenance Agreement (SMA)",
      "customization_needed": "Billing model specific to Econolite's service offerings"
    },
    {
      "element": "Reference contracts: F4319322-0884-44ca-b691-0379ce755da5 and 2d98df31-e734-44dd-9c7a-05e65d5cd9ec",
      "customization_needed": "Merchant-specific contract templates and examples"
    },
    {
      "element": "Key contacts: Huy Huynh (VP Finance), Brenda Leto (Project Finance), Christopher Chen, Serey Kim, Jennifer Lleva",
      "customization_needed": "Merchant-specific stakeholders and escalation paths"
    },
    {
      "element": "ERP: Bespoke then to Dynamics",
      "customization_needed": "Merchant-specific system integration requirements"
    },
    {
      "element": "Tax Integration: GTM",
      "customization_needed": "Merchant-specific tax calculation system"
    },
    {
      "element": "Path Master distributor relationship",
      "customization_needed": "Merchant-specific distribution channel and customer hierarchy"
    },
    {
      "element": "Contract naming convention using 'hereafter referred to as Agency'",
      "customization_needed": "Merchant-specific contract language and terminology"
    },
    {
      "element": "ACV: 27k - Larger Enterprise account for Tabs",
      "customization_needed": "Merchant-specific account classification and value"
    },
    {
      "element": "Accuracy emphasis on multi-year contract capture",
      "customization_needed": "Merchant-specific quality requirements and pain points"
    }
  ],
  "confidence_score": 0.85
}
```

---

