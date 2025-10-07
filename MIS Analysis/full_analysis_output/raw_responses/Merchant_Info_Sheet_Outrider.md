# Raw LLM Analysis: Merchant Info Sheet - Outrider

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:56:42

---

## Chunk 1: Merchant Info Sheet - Outrider_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:56:42

### Original Content
```
Questionnaire   Outrider Configuration 1 Netsuite flow Create Sales Order Sync Sales Order Invoice Only   Update: Adjust to Sales Order flow as Tabs support Sales Order flow for a single account 2 Sales order Data Fields   Department is the Revenue (ID: 105) 3 Invoice creation   Invoice   Customer Subsidiary Location Department: Revenue Items   Pricing 4 Items   FedEx Operational Services Site Setup Autonomy Kit Sync integration item 5 Customer Creation   Not applicable 6 Taxes   No taxes 7 Paym...
```

### LLM Analysis Response
```json
{
  "themes": [
    "NetSuite Integration Configuration",
    "Sales Order and Invoice Management",
    "Financial Account Mapping and Payment Processing",
    "Customer and Item Setup Requirements",
    "Implementation Timeline and System Access"
  ],
  "rules": [
    {
      "rule": "Use Sales Order flow instead of Invoice Only flow",
      "category": "workflow",
      "details": "Adjusted to Sales Order flow as Tabs support Sales Order flow for a single account"
    },
    {
      "rule": "Department must be set to Revenue with ID: 105",
      "category": "data_mapping",
      "details": "Required field for Sales Order data"
    },
    {
      "rule": "Invoice must include: Customer, Subsidiary, Location, Department (Revenue), Items, and Pricing",
      "category": "invoice_creation",
      "details": "Mandatory fields for invoice generation"
    },
    {
      "rule": "No taxes should be applied",
      "category": "taxation",
      "details": "Tax exemption for this configuration"
    },
    {
      "rule": "Payments must be mapped to account 10000 - PacWest (Sq One) Bank - Checking Acct",
      "category": "payment_processing",
      "details": "Specific bank account designated for revenue"
    },
    {
      "rule": "API access required for both Sandbox and Production environments",
      "category": "system_access",
      "details": "Production access has been acquired"
    },
    {
      "rule": "Customer creation is not applicable",
      "category": "customer_management",
      "details": "Customer creation process is disabled or handled externally"
    }
  ],
  "exceptions": [
    {
      "exception": "Original plan was Invoice Only flow, but adjusted to Sales Order flow",
      "reason": "Tabs platform supports Sales Order flow for single account",
      "impact": "Changes the entire order processing workflow"
    },
    {
      "exception": "Tax exemption applied",
      "details": "No taxes to be calculated or applied despite typical invoice requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Outrider Configuration",
      "type": "merchant_name",
      "customizable": true,
      "notes": "Specific merchant/client name"
    },
    {
      "element": "Department ID: 105 (Revenue)",
      "type": "accounting_structure",
      "customizable": true,
      "notes": "Merchant-specific department configuration in NetSuite"
    },
    {
      "element": "PacWest (Sq One) Bank - Checking Acct (Account 10000)",
      "type": "bank_account",
      "customizable": true,
      "notes": "Merchant-specific banking details"
    },
    {
      "element": "Items: FedEx Operational Services, Site Setup, Autonomy Kit, Sync integration item",
      "type": "product_catalog",
      "customizable": true,
      "notes": "Merchant-specific product/service offerings"
    },
    {
      "element": "Timeline: August 1st, 2024",
      "type": "implementation_date",
      "customizable": true,
      "notes": "Project-specific deadline"
    },
    {
      "element": "Dunning configuration",
      "type": "billing_policy",
      "customizable": true,
      "notes": "Merchant-specific payment reminder/collection process"
    },
    {
      "element": "Logo and billing information",
      "type": "branding",
      "customizable": true,
      "notes": "Merchant-specific visual and contact details"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Outrider_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:56:42

### Original Content
```
fMerchant: Outrider Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: [If Exists] Opt Out Date: Go Live Date: Jul 31, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CFO: Eric Andreas Company summary Outrider, the pioneer in autonomous yard operations for logistics hubs, helps large enterprises improve safety and increase efficiency The only company exclusively focused on automating all aspects of yard operations, ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Models",
    "Default Operational Parameters",
    "Implementation Timeline and Milestones",
    "Stakeholder Communication and Notifications",
    "Tax and Payment Processing"
  ],
  "rules": [
    {
      "rule": "Two distinct business models must be processed: (1) Actual Company contracts (Outrider automation) and (2) Sub-tenant agreements",
      "category": "billing_model",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "contract_defaults",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "payment_terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_frequency",
      "explicit": true
    },
    {
      "rule": "No taxes are expected for Outrider at completion of implementation",
      "category": "tax_handling",
      "explicit": true
    },
    {
      "rule": "For Subtenants: Use 'Base Rent' for Base Rent portion and 'Security Deposit' for Security Deposit portion",
      "category": "integration_items",
      "explicit": true
    },
    {
      "rule": "Ops Team does not need to notify anyone regarding completion of processing batches in Implementation or Active phase",
      "category": "communication",
      "explicit": true
    },
    {
      "rule": "Post-implementation check-in required 2 weeks after go-live (Aug 13th) for Cash Application and Reporting",
      "category": "post_implementation",
      "explicit": true
    },
    {
      "rule": "Nothing should be ignored in contracts during processing",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Notify Outrider in their channel and set up a bot for them",
      "category": "customer_notification",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant has two different business models requiring separate processing workflows (company contracts vs sub-tenant agreements)",
      "context": "billing_model"
    },
    {
      "exception": "No tax line items expected specifically for Outrider (differs from standard tax handling)",
      "context": "tax_processing"
    },
    {
      "exception": "Ops International Team should ignore certain sections marked as such",
      "context": "team_assignments"
    },
    {
      "exception": "Customer Service team must review Netsuite-specific documentation",
      "context": "cs_requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and business model",
      "value": "Outrider - autonomous yard operations for logistics hubs",
      "customizable": true
    },
    {
      "element": "Key dates",
      "value": "Scoping: Nov 6, 2023; MSA: Feb 7, 2024; Go Live: Jul 31, 2024",
      "customizable": true
    },
    {
      "element": "Key personnel",
      "value": "CFO: Eric Andreas",
      "customizable": true
    },
    {
      "element": "ERP system",
      "value": "Netsuite (implied from documentation references)",
      "customizable": true
    },
    {
      "element": "Contract examples with specific IDs",
      "value": "Subtenant: 6ff84c22-7151-426e-bb98-b049be3ee4b4; Business: 5f60604e-1ee0-42a5-8b6f-e36cac483211",
      "customizable": true
    },
    {
      "element": "Communication channel",
      "value": "Outrider-specific channel with bot setup",
      "customizable": true
    },
    {
      "element": "Dual business model structure",
      "value": "Company contracts and sub-tenant agreements",
      "customizable": true
    },
    {
      "element": "Post-implementation check-in timing",
      "value": "2 weeks after go-live (Aug 13th)",
      "customizable": true
    },
    {
      "element": "Integration item naming conventions",
      "value": "Base Rent and Security Deposit for subtenants",
      "customizable": true
    }
  ],
  "confidence_score": 0.88
}
```

---

