# Raw LLM Analysis: Merchant Info Sheet_ Maybern(1)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 09:53:23

---

## Chunk 1: Merchant Info Sheet_ Maybern(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:53:23

### Original Content
```
2) Is there a key POC for the buyer decision maker John Bowman, Chief Business Officer, and Bryan Champ, SVP of Sales 3) What are the Tabs features the key POC cares about Contract Storage, Invoicing, Reporting, Usage Data upload Billing model Info on how merchant bills Quarterly with usage data (they take a Basis Point percentage on fund size How contract is broken up Implementation fee, quarterly billing on usage data, multi year contracts One off things to know about merchant One person finan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Setup and Billing Structure",
    "Implementation Fee Processing",
    "Usage-Based Billing and AUM Calculations",
    "Document Processing and Data Management",
    "Default Operational Parameters"
  ],
  "rules": [
    "Implementation fees must be split into separate billing transactions (BTs) per fund",
    "Implementation is split into two 50% payments per fund",
    "First set of implementation BTs start on effective date, second set on access start date",
    "If access start date not specified in contract, default to 6 months from effective date",
    "Fund estimates in contracts should be ignored as they are usage-based and calculated quarterly",
    "Default service term is 1 year if none listed",
    "Default net payment terms is 0 days if none listed",
    "Default billing frequency is quarterly (except implementation which is 2 invoices)",
    "Every tax line item becomes a separate BT if not otherwise specified",
    "For tiered pricing models, only process the first tier and ignore subsequent tiers",
    "Usage-based billing structure is annual, divided into quarterly payments",
    "Basis point percentages must be converted to decimal format divided by 4 for quarterly billing (e.g., 1 basis point = 0.000025)",
    "Usage-based BTs must be titled 'Fund Service Fee for [Name of Fund]'",
    "Integration item for usage fees should be labeled 'Fund Service Fee'",
    "Merchant uses CSV upload for fund size usage data"
  ],
  "exceptions": [
    "Implementation fee payment schedule may be explicitly outlined in contract, overriding the 6-month default",
    "Customer may have two separate documents (MSA and Order Form) instead of single consolidated document",
    "MSA contains payment terms while Order Form contains billing terms when split",
    "Tiered pricing models exist but only first tier should be processed",
    "Merchant currently has only 5 contracts (small portfolio)"
  ],
  "merchant_specific": [
    "Key decision makers: John Bowman (Chief Business Officer) and Bryan Champ (SVP of Sales)",
    "Required Tabs features: Contract Storage, Invoicing, Reporting, Usage Data upload",
    "Billing model: Quarterly with usage data based on basis point percentage of fund size",
    "Contract structure: Implementation fee + quarterly usage-based billing + multi-year contracts",
    "One-person finance team (resource constraint)",
    "Manual CSV upload process for fund size data",
    "Small contract volume (only 5 contracts currently)",
    "Specific terminology: 'BT' (Billing Transaction), 'AUM fee' (Assets Under Management fee), 'AST Events Processing'",
    "Uses basis points or percentages to calculate fund service fees",
    "Each fund is treated as separate billing entity for implementation"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet_ Maybern(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:53:28

### Original Content
```
Merchant Demo date: Scoping start date: Jun 20, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Jul 1, 2024 [If Exists] Opt Out Date: Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: John Bowman, Chief Business Officer CFO: John Bowman, Chief Business Officer Customer service rep who is really involved: Bryan Champ, SVP of Sales Account Receivable POC: accounting maybern com Billing POC: accounting maybern com Company...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Stakeholder Identification and Roles",
    "Business Goals and Pain Points",
    "System Integration and Migration",
    "Relationship Management and Temperament Assessment"
  ],
  "rules": [
    {
      "rule": "Document key implementation dates in chronological order: Demo date, Scoping start date, MSA Signature Date, Onboarding Kick Off Date, Opt Out Date (if exists), and Go Live Date",
      "type": "explicit",
      "category": "timeline_tracking"
    },
    {
      "rule": "Identify and document GTM POC and Implementation POC for each merchant",
      "type": "explicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Capture ERP and Tax Integration system information",
      "type": "explicit",
      "category": "technical_integration"
    },
    {
      "rule": "Document key merchant personnel including Accountant, CFO, Customer Service Representative, Account Receivable POC, and Billing POC with contact information",
      "type": "explicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Provide company summary describing merchant's business model and operations",
      "type": "explicit",
      "category": "merchant_profiling"
    },
    {
      "rule": "Define merchant's North Star goals including what pain points are being solved and why they are purchasing the product",
      "type": "explicit",
      "category": "goals_alignment"
    },
    {
      "rule": "Document AE (Account Executive) notes including merchant temperament and relationship dynamics",
      "type": "explicit",
      "category": "relationship_management"
    },
    {
      "rule": "Assess and document merchant temperament to inform communication strategy",
      "type": "implicit",
      "category": "relationship_management"
    },
    {
      "rule": "Track migration from existing systems (e.g., Sheets, Google Drive) to new platform",
      "type": "implicit",
      "category": "change_management"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date field is conditional - only documented 'If Exists'",
      "condition": "Not all merchants may have an opt-out date"
    },
    {
      "exception": "Same person (John Bowman) serving dual roles as both Accountant and CFO",
      "condition": "Smaller organizations may have consolidated leadership roles"
    },
    {
      "exception": "Part-time hire working full-time capacity",
      "condition": "John Bowman hired part-time but functioning as full-time COO, indicating flexible role definitions"
    },
    {
      "exception": "Fellow primary PortCo relationship noted",
      "condition": "Special relationship status that may affect service level or priority"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and business description",
      "customization_needed": "Each merchant will have unique company summary and industry vertical"
    },
    {
      "element": "Implementation timeline dates",
      "customization_needed": "Dates vary per merchant based on contract and readiness"
    },
    {
      "element": "Key personnel names, titles, and contact information",
      "customization_needed": "Organizational structure and contacts unique to each merchant"
    },
    {
      "element": "ERP and Tax Integration systems",
      "customization_needed": "Technical stack varies by merchant"
    },
    {
      "element": "North Star goals and pain points",
      "customization_needed": "Business objectives and challenges specific to each merchant's use case"
    },
    {
      "element": "Current systems being replaced",
      "customization_needed": "Migration source systems differ per merchant (e.g., Sheets, Google Drive, other platforms)"
    },
    {
      "element": "Merchant temperament and relationship notes",
      "customization_needed": "Communication style and relationship dynamics unique to each merchant contact"
    },
    {
      "element": "Use case scope",
      "customization_needed": "Specific features being implemented (contract repository, invoicing, reporting, AR operations) vary by merchant needs"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet_ Maybern(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:53:43

### Original Content
```
75 basis point   0 00001875 ( 75 basis point 4 quarterly payments) 5 basis point   0 0000125 ( 5 basis point 4 quarterly payments)  BE SURE TO UNCHECK  IS BILLED IN ARREARS  These are NOT billed in arrears Quarterly billing cadence The first fund service fee should go out right after the 2nd implementation fee Because usage bills are in arrears, the period start date for these terms should be 3 months prior to the 2nd implementation fee invoice date For example: If the 2nd implementation invoice...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Configuration and Timing",
    "Fee Structure and Calculation",
    "Integration and Processing Workflow",
    "Invoice Customization Requirements",
    "Contract Management and Renewals"
  ],
  "rules": [
    {
      "rule": "Fund service fees must NOT be billed in arrears - uncheck 'IS BILLED IN ARREARS' option",
      "category": "billing_configuration",
      "specificity": "explicit"
    },
    {
      "rule": "Quarterly billing cadence applies to fund service fees",
      "category": "billing_frequency",
      "specificity": "explicit"
    },
    {
      "rule": "First fund service fee invoice should be sent immediately after the 2nd implementation fee",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "Usage bill period start dates should be set 3 months prior to 2nd implementation fee invoice date",
      "category": "billing_timing",
      "specificity": "explicit"
    },
    {
      "rule": "75 basis point fee = 0.00001875 (divided into 4 quarterly payments)",
      "category": "fee_calculation",
      "specificity": "explicit"
    },
    {
      "rule": "5 basis point fee = 0.0000125 (divided into 4 quarterly payments)",
      "category": "fee_calculation",
      "specificity": "explicit"
    },
    {
      "rule": "Usage BTs should be assigned to 'Fund Service Fee' integration item",
      "category": "integration_mapping",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation fees should be assigned to 'Implementation Fee' integration item",
      "category": "integration_mapping",
      "specificity": "explicit"
    },
    {
      "rule": "Implementation fees are non-taxable by default (can be changed to taxable if needed)",
      "category": "taxation",
      "specificity": "explicit"
    },
    {
      "rule": "Logo must be included on invoices",
      "category": "invoice_formatting",
      "specificity": "explicit"
    },
    {
      "rule": "No post-processing notifications required to Ops Team",
      "category": "communications",
      "specificity": "explicit"
    },
    {
      "rule": "Contract duration is one year",
      "category": "contract_terms",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Usage bills are in arrears, but fund service fees are NOT billed in arrears",
      "condition": "Different billing treatment for different fee types",
      "impact": "Requires careful configuration to avoid arrears setting"
    },
    {
      "exception": "Tax status can be changed from non-taxable to taxable on a case-by-case basis",
      "condition": "When tax needs to be charged",
      "impact": "Implementation fees may require tax adjustment"
    },
    {
      "exception": "Some customers require BTs separated into different invoices",
      "condition": "Customer-specific invoice requirements",
      "impact": "Currently no operational instructions available - solution in development"
    },
    {
      "exception": "Invoice changes may be required based on merchant-customer relationships",
      "condition": "Specific customer relationships",
      "impact": "Custom invoice handling needed"
    }
  ],
  "merchant_specific": [
    {
      "element": "Basis point fee rates (75 and 5 basis points)",
      "customization_type": "fee_structure",
      "note": "Specific to this merchant's pricing model"
    },
    {
      "element": "Quarterly payment structure (4 payments)",
      "customization_type": "payment_schedule",
      "note": "May vary by merchant contract"
    },
    {
      "element": "Logo requirement on invoices",
      "customization_type": "branding",
      "note": "Merchant-specific branding preference"
    },
    {
      "element": "Separated invoice requirement for certain customers",
      "customization_type": "invoice_structure",
      "note": "Customer-level customization within merchant account"
    },
    {
      "element": "One-year contract term",
      "customization_type": "contract_duration",
      "note": "Merchant-specific contract length"
    },
    {
      "element": "Feature request for renewal escalation and contract visibility",
      "customization_type": "workflow_enhancement",
      "note": "Medium urgency - merchant needs visibility into contract end dates"
    },
    {
      "element": "Timing example: 2nd implementation invoice on 5/31, usage BTs start 3/1, first invoice 6/1",
      "customization_type": "timing_configuration",
      "note": "Specific date calculation example for this merchant"
    }
  ],
  "confidence_score": 0.85
}
```

---

