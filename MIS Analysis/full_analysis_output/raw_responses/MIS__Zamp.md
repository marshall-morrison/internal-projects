# Raw LLM Analysis: MIS_ Zamp

## Document Overview
- **Total Chunks Analyzed**: 6
- **Analysis Timestamp**: 2025-10-02 10:10:34

---

## Chunk 1: MIS_ Zamp_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:34

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp han...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Tax Integration Requirements and Limitations",
    "Customer Information Management",
    "Feature Request Documentation and Handoff Process",
    "Expectation Setting and Scope Management"
  ],
  "rules": [
    "Customer Success (specifically Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
    "Customer Information section must be filled by Implementation Success team Post-Go Live",
    "Account Executives (AE) must fill Feature Requests prior to Implementation handoff",
    "Implementation team must fill Feature Requests prior to go-live",
    "Success team must fill Feature Requests Post-Go Live",
    "Zamp Tax Integration will only go live on Tabs with a bridge integration to send invoices with Zamp tax calculated",
    "Go-live is blocked without the Zamp integration being built",
    "Tax calculations are only needed on sent invoices, not on tax estimates",
    "Expectations must be set that Zamp integration is unique and provides no benefit to other merchants",
    "Expectations must be set that this is not a channel for Zamp to acquire other Tabs clients",
    "Tax exemptions are not supported in the current system",
    "Tax codes are not managed in Tabs"
  ],
  "exceptions": [
    "Zamp has tax exempt clients, but this occurs rarely",
    "Zamp has an exemption property in their API, but Tabs doesn't support exemptions",
    "Tax refunds on credit memos are theoretically possible but Zamp cannot think of an instance where this has happened",
    "Special memos may be required for certain invoices based on merchant-customer relationships"
  ],
  "merchant_specific": [
    "Merchant name: Messari (in notification example), Zamp (in feature request)",
    "Specific contact person: Azmat Aziz for Customer Success",
    "Merchant-specific internal communication channel (Messari internal merchant channel)",
    "Contract start date: 12/31/25 (Zamp-specific)",
    "Critical call reference with Gong ID for context",
    "Merchant phase status (e.g., 'Active')",
    "Specific customer information requirements that vary by merchant relationship",
    "Invoice-specific memo requirements based on individual merchant-customer relationships",
    "Integration type and scope (bridge integration for Zamp)",
    "Tax provider selection (Zamp as the specific tax provider)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_ Zamp_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:40

### Original Content
```
Merchant Name: Zamp Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Free months: When free months are included on the front end, merchant would li...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Configuration",
    "Payment Terms and Timing",
    "Service Classification and SKU Management",
    "Processing Workflows and Defaults",
    "Stakeholder Communication and Documentation"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Free Months Processing",
      "description": "When free months are included on the front end, payment is due once free months have expired",
      "example": "2 free months upfront, then 12 month contract billed monthly means payment due on day 61 (assuming 30 days/month)"
    },
    {
      "rule_id": "R2",
      "category": "Service Types",
      "description": "Services must be split into recurring services (subscription fees) and one-time services (overdue filing charges)",
      "details": "One-time services are charged for overdue filings that customers need help with"
    },
    {
      "rule_id": "R3",
      "category": "Payment Timing",
      "description": "One-time services must be paid up front",
      "related_question": "Should this be a separate invoice or can it be included on agreement with Tabs generating 2 invoices"
    },
    {
      "rule_id": "R4",
      "category": "Default Service Term",
      "description": "If no service term is listed, Ops default is 1 Year"
    },
    {
      "rule_id": "R5",
      "category": "Default Payment Terms",
      "description": "If no payment terms listed, Ops default is Net 0 (immediate payment)"
    },
    {
      "rule_id": "R6",
      "category": "Default Billing Frequency",
      "description": "If no billing frequency listed, Ops default is Monthly"
    },
    {
      "rule_id": "R7",
      "category": "Tax Handling",
      "description": "If no specific instruction listed, Ops default is every tax line item becomes a BT (Billable Transaction) Event"
    },
    {
      "rule_id": "R8",
      "category": "SKU Management",
      "description": "One-time services require a new SKU that is yet to be setup"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Contract-specific processing variations may exist",
      "example": "Always back-date invoice date to final day of the month (merchant-specific request)"
    },
    {
      "exception_id": "E2",
      "description": "Integration items may have special labeling requirements",
      "examples": [
        "All Statsig integration items should be labeled as 'Sales'",
        "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
      ]
    },
    {
      "exception_id": "E3",
      "description": "Certain contract elements may need to be ignored during processing",
      "note": "Specific items to ignore should be documented per merchant"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "description": "Zamp Implementation POC",
      "customization_required": true
    },
    {
      "element": "POC Contacts",
      "description": "Implementation POC and CX POC need to be filled in per merchant",
      "customization_required": true
    },
    {
      "element": "Billing Model",
      "description": "Entire section to be filled by Implementation team per merchant",
      "customization_required": true
    },
    {
      "element": "Customer Creation Process",
      "description": "Unique aspects of customer creation process vary by merchant",
      "customization_required": true
    },
    {
      "element": "Contract Structure",
      "description": "How contract is broken up and one-off merchant-specific details",
      "customization_required": true
    },
    {
      "element": "Contract Processing Steps",
      "description": "Entire section to be filled by Implementation Success team post-go-live",
      "customization_required": true
    },
    {
      "element": "Events Processing",
      "description": "Important information on events billing (if necessary) - merchant-specific",
      "customization_required": true
    },
    {
      "element": "Integration Items Processing",
      "description": "Instructions for assigning integration items vary by merchant and integration type",
      "customization_required": true
    },
    {
      "element": "Post Processing Communications",
      "description": "Notification requirements for batch processing completion vary by merchant",
      "customization_required": true
    },
    {
      "element": "Free Months Calculation",
      "description": "Number of free months and payment due date calculation is merchant-specific",
      "customization_required": true
    },
    {
      "element": "Invoice Backdating",
      "description": "Specific processing requests like backdating invoices differ by contract/merchant",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: MIS_ Zamp_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:50

### Original Content
```
gong io call id 8453558021261596874 Next Steps and Zamp Partnership 8 26 https: us-56595 app gong io call id 4045714213021396919 Technical Scoping and Validation 8 28 https: us-56595 app gong io call id 8552194763416521825 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Zamp bills customers based on tiers related to the number of states they operate in, with different pricing for different state count ranges This is tiered unit ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tiered pricing structure and billing configuration",
    "Proration policy and overage handling",
    "Contract types and billing terms setup",
    "Customer segmentation by state operations",
    "Implementation handoff and stakeholder management"
  ],
  "rules": [
    "Proration is NOT supported for this merchant",
    "Overages must be added to the next month's invoice (not prorated in current period)",
    "Pricing tiers are based on number of states the customer operates in",
    "Sales representatives can negotiate discounts within the tiered structure",
    "Annual payment contracts require 2 billing terms: 1 flat fee and 1 tiered volume flat",
    "Monthly payment contracts require 1 billing term: 1 tiered volume flat",
    "Implementation team is the DRI (Directly Responsible Individual) for completion on handoff",
    "Account Executive must fill in notes sections prior to handoff"
  ],
  "exceptions": [
    "Different pricing applies for different state count ranges (tiered structure creates exceptions based on volume)",
    "Discounts can be negotiated by sales reps, creating customer-specific pricing exceptions within tiers",
    "Annual contracts have different billing term configuration (2 terms) compared to monthly contracts (1 term)"
  ],
  "merchant_specific": [
    "Merchant name: Zamp",
    "Key stakeholder: Carie (Head of CS, main Champion for Tabs)",
    "Billing model: State-based tiered pricing (unique to how Zamp's customers operate)",
    "Customer base characteristic: Customers are segmented by number of states they operate in",
    "Specific overage handling approach: Add to next invoice rather than prorate",
    "Contract structure: Mix of annual and monthly payment options with different billing term requirements"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: MIS_ Zamp_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:52

### Original Content
```
We will instead hard-code a single tax code for all transactions line items we send them Confirmed for their business it would be R_DIG_SAAS_B2B Follow up items for product: OPTION 1: Universal Tax Integrator: Ariel mentioned that she s done some work on creating a universal tax integrator OPTION 2: Product Delivery: Jean can create a one-off integration following similar requirements to what we do for direct integrations with Anrok   Avalara Other uncertain items: Use case 1: Upgrades - when a ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax code configuration and integration options",
    "Billing term setup for annual and monthly payment contracts",
    "Upgrade and overage handling when customers exceed tier thresholds",
    "Delinquent payment tracking and account management",
    "System integration between Zamp, Tabs, and tax providers (Anrok/Avalara)"
  ],
  "rules": [
    {
      "rule_id": "TAX_001",
      "description": "Hard-code tax code R_DIG_SAAS_B2B for all transaction line items",
      "category": "tax_configuration",
      "explicit": true
    },
    {
      "rule_id": "BILLING_001",
      "description": "Annual payment contracts require 2 billing terms: 1 flat and 1 tiered volume flat",
      "category": "billing_configuration",
      "explicit": true
    },
    {
      "rule_id": "BILLING_002",
      "description": "Monthly payment contracts require 1 billing term: 1 tiered volume flat",
      "category": "billing_configuration",
      "explicit": true
    },
    {
      "rule_id": "UPGRADE_001",
      "description": "Do NOT support proration for upgrades when customers exceed tier thresholds",
      "category": "upgrade_handling",
      "explicit": true
    },
    {
      "rule_id": "UPGRADE_002",
      "description": "Add overage charges to the next month's invoice instead of prorating",
      "category": "upgrade_handling",
      "explicit": true
    },
    {
      "rule_id": "PAYMENT_001",
      "description": "Track delinquent payments using PaymentStatus, Invoice status, and Due date fields from Tabs",
      "category": "payment_management",
      "explicit": true
    },
    {
      "rule_id": "PAYMENT_002",
      "description": "Mark accounts with failed payment recovery in Zamp Admin to prevent servicing unpaid accounts",
      "category": "payment_management",
      "explicit": true
    },
    {
      "rule_id": "INTEGRATION_001",
      "description": "Zamp can pull delinquent payment data from Tabs via billing report export or API connection",
      "category": "system_integration",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "EXC_001",
      "description": "Proration is explicitly NOT supported - overages are deferred to next billing cycle",
      "applies_to": "upgrade_handling",
      "condition": "When customer exceeds tier threshold amount"
    },
    {
      "exception_id": "EXC_002",
      "description": "Two integration options available for tax: Universal Tax Integrator (Ariel's work) or one-off integration (Jean's approach similar to Anrok)",
      "applies_to": "tax_integration",
      "condition": "Product team decision pending"
    }
  ],
  "merchant_specific": [
    {
      "element": "Tax code R_DIG_SAAS_B2B",
      "customization_needed": true,
      "note": "This specific tax code is confirmed for this merchant's business; other merchants may require different tax codes"
    },
    {
      "element": "Tier threshold amounts",
      "customization_needed": true,
      "note": "Tracked in Zamp Admin and likely varies by merchant business model"
    },
    {
      "element": "Billing term configuration (flat vs tiered volume)",
      "customization_needed": true,
      "note": "Number and type of billing terms may vary based on merchant's pricing model"
    },
    {
      "element": "Payment recovery process",
      "customization_needed": true,
      "note": "Recovery efforts and thresholds for marking accounts delinquent may be merchant-specific"
    },
    {
      "element": "Tabs integration",
      "customization_needed": false,
      "note": "Merchant uses Tabs as their billing system; references to specific Slack channels and Gong calls indicate custom implementation"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 5: MIS_ Zamp_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:03

### Original Content
```
Cares immensely about renewals and having a single source of truth for revenue Very nice, lives in Bozemon, MT - consistently taking calls on her porch Amelia will be the day to day billing specialist She ll be in the weeds charging customers and tracking collections Has vocalized Tabs will make her life way easier and also a strong champion Jae is their RevOps lead and cares about HS Currently severely underutilized and will leverage Tabs data sync to optimize their CRM Will be main POC for HS ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder roles and responsibilities",
    "Revenue operations and billing management",
    "CRM integration and data synchronization",
    "Payment processing and fee management",
    "Implementation and adoption strategy"
  ],
  "rules": [
    {
      "rule": "Maintain single source of truth for revenue data",
      "category": "data_management",
      "specificity": "general"
    },
    {
      "rule": "Sync Tabs data to HubSpot CRM for optimization",
      "category": "integration",
      "specificity": "specific"
    },
    {
      "rule": "Use Tabs for contract ingestion into HubSpot",
      "category": "workflow",
      "specificity": "specific"
    },
    {
      "rule": "Sync invoices back to HubSpot system",
      "category": "integration",
      "specificity": "specific"
    },
    {
      "rule": "Push credit card fees onto customers for smaller deals",
      "category": "payment_processing",
      "specificity": "conditional"
    },
    {
      "rule": "Encourage ACH payment method to avoid fees",
      "category": "payment_processing",
      "specificity": "general"
    },
    {
      "rule": "Executive buyer (COO) tracks implementation progress",
      "category": "governance",
      "specificity": "specific"
    }
  ],
  "exceptions": [
    {
      "exception": "Credit card fees only pushed to customers on smaller deals (not all deals)",
      "condition": "deal_size",
      "implication": "Requires deal size threshold determination"
    },
    {
      "exception": "COO involvement is limited to tracking, not day-to-day operations",
      "condition": "stakeholder_role",
      "implication": "Different engagement levels by role"
    }
  ],
  "merchant_specific": [
    {
      "element": "Stakeholder names and roles (Amelia, Jae, Matt, Caitlin, Clete)",
      "type": "personnel",
      "customization_needed": true
    },
    {
      "element": "Geographic location reference (Bozeman, MT)",
      "type": "location",
      "customization_needed": true
    },
    {
      "element": "HubSpot as primary CRM system",
      "type": "technology_stack",
      "customization_needed": true
    },
    {
      "element": "Partnership announcement timing (fall)",
      "type": "timeline",
      "customization_needed": true
    },
    {
      "element": "Current state: HubSpot severely underutilized as data dump",
      "type": "system_maturity",
      "customization_needed": true
    },
    {
      "element": "Deal size threshold for fee application",
      "type": "business_rule",
      "customization_needed": true
    },
    {
      "element": "Stripe as payment processor",
      "type": "technology_stack",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 6: MIS_ Zamp_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:11:10

### Original Content
```
Partnership for Tax - part of the reason they're paying 50k is for us to build a Zamp integration via bridge tech This will move towards a larger partnership conversation in the future Context (this was not written into MIS but is the expectation):  With Zamp as a customer, we are willing to commit to the following for the partnership: Automate Zamp s order-to-cash process as discussed with Carie Stand up a bridge integration in the short-term to enable Tabs to ingest Zamp s tax calculations for...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Strategic Partnership Development",
    "Technical Integration Requirements",
    "Revenue Operations and Data Consolidation",
    "Invoicing and Cash Collection Efficiency",
    "Customer Renewal Management"
  ],
  "rules": [
    {
      "rule": "Partnership contingent on $50k payment for Zamp integration via bridge technology",
      "category": "commercial_agreement",
      "explicit": true
    },
    {
      "rule": "Bridge integration must be stood up in short-term to enable Tabs to ingest Zamp's tax calculations",
      "category": "technical_requirement",
      "explicit": true
    },
    {
      "rule": "Target go-live date is December 2025",
      "category": "timeline",
      "explicit": true
    },
    {
      "rule": "Partnership discussions must kick-off in September",
      "category": "timeline",
      "explicit": true
    },
    {
      "rule": "Public partnership announcement planned for Q4",
      "category": "timeline",
      "explicit": true
    },
    {
      "rule": "Full product integration development begins only after identifying at least 3 mutual customers",
      "category": "technical_requirement",
      "explicit": true
    },
    {
      "rule": "Joint prospecting efforts to begin after Q4 partnership announcement",
      "category": "commercial_agreement",
      "explicit": true
    },
    {
      "rule": "Single source of truth for revenue required to replace fragmented systems (QBO, Stripe, Spreadsheets, HS)",
      "category": "data_management",
      "explicit": true
    },
    {
      "rule": "Invoicing must be cleaned up and delivered on time",
      "category": "operational_requirement",
      "explicit": true
    },
    {
      "rule": "Renewals tracking system must be implemented for customer success team",
      "category": "operational_requirement",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Partnership expectations not formally written into MIS (Merchant Instruction Sheet) but are operational expectations",
      "condition": "Informal agreement structure",
      "impact": "May require separate documentation or confirmation"
    },
    {
      "exception": "Full product integration is conditional on achieving 3+ mutual customers milestone",
      "condition": "Milestone-based development trigger",
      "impact": "Engineering resources allocated only after business validation"
    },
    {
      "exception": "Bridge integration is temporary solution before full product integration",
      "condition": "Short-term vs long-term technical approach",
      "impact": "Two-phase integration strategy required"
    }
  ],
  "merchant_specific": [
    {
      "element": "Zamp-specific tax calculation integration",
      "customization_needed": "Bridge technology configuration for Zamp's tax engine",
      "merchant": "Zamp"
    },
    {
      "element": "Data sources: HubSpot (HS), Stripe, QuickBooks Online (QBO)",
      "customization_needed": "Integration mappings specific to Zamp's current tech stack",
      "merchant": "Zamp"
    },
    {
      "element": "Customer success team as main champions for renewals",
      "customization_needed": "Renewals report tailored to CS team workflows",
      "merchant": "Zamp"
    },
    {
      "element": "Contract complexity causing invoicing delays",
      "customization_needed": "Custom invoicing logic to handle Zamp's contract structures",
      "merchant": "Zamp"
    },
    {
      "element": "Order-to-cash process automation",
      "customization_needed": "Workflow automation specific to Zamp's discussed requirements with Carie",
      "merchant": "Zamp"
    },
    {
      "element": "$50k partnership fee",
      "customization_needed": "Non-standard pricing for strategic partnership value",
      "merchant": "Zamp"
    }
  ],
  "confidence_score": 0.88
}
```

---

