# Raw LLM Analysis: MIS_ Teleskope AI

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:19:36

---

## Chunk 1: MIS_ Teleskope AI_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:19:36

### Original Content
```
Merchant Name (AE to fill) : Teleskope (https: www teleskope ai ) Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Creating Customers: Billing emai...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Creation and Billing Email Management",
    "Contract Processing and Service Start Dates",
    "Product/Offering Configuration and Billing Terms",
    "Teleskope-Specific Product Handling (Data Protection Platform)",
    "Pricing and Quantity Calculation Rules"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "Billing email must always be included when creating a customer",
      "source": "Customer Email for Invoices field in contract",
      "criticality": "Very important - must flag if missing"
    },
    {
      "rule_id": "R2",
      "description": "Service Start Date must use the Effective Date from the contract",
      "source": "Contract Effective Date field"
    },
    {
      "rule_id": "R3",
      "description": "Billing terms must be located in the 'License Terms' section of the contract",
      "source": "License Terms section"
    },
    {
      "rule_id": "R4",
      "description": "Each offering must be processed as a separate billing term (BT)",
      "source": "Products column in contract"
    },
    {
      "rule_id": "R5",
      "description": "Item Name should use the product name from the 'Products' column",
      "source": "Products column"
    },
    {
      "rule_id": "R6",
      "description": "Item Description is optional unless needed to distinguish offerings",
      "source": "General processing guideline"
    },
    {
      "rule_id": "R7",
      "description": "Quantity defaults to 1 if no quantities are listed",
      "source": "General processing guideline"
    },
    {
      "rule_id": "R8",
      "description": "Total Price should use the annual amount listed for each offering",
      "source": "Contract pricing information"
    },
    {
      "rule_id": "R9",
      "description": "Billing Start Date calculation: If opt-out/Evaluation period exists, use number of days + Service Start Date",
      "source": "Contract evaluation period terms"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "For 'Teleskope Data Protection Platform' products, connectors must be listed in the Item Description",
      "example": "Description: AWS S3, AWS RDS, AWS Redshift, Databricks",
      "applies_to": "Teleskope Data Protection Platform product only"
    },
    {
      "exception_id": "E2",
      "description": "For 'Teleskope Data Protection Platform', Quantity should list the number of connectors (not default to 1)",
      "example": "Quantity: 4 (for 4 connectors)",
      "applies_to": "Teleskope Data Protection Platform product only"
    },
    {
      "exception_id": "E3",
      "description": "Billing Start Date has conditional logic based on presence of opt-out/Evaluation period",
      "condition": "If evaluation period exists, add days to Service Start Date"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "Teleskope",
      "customizable": false
    },
    {
      "element": "Product Name",
      "value": "Teleskope Data Protection Platform",
      "customizable": false,
      "note": "Has special handling rules for connectors"
    },
    {
      "element": "Contract Section Names",
      "values": ["License Terms", "Products", "Customer Email for Invoices", "Effective Date"],
      "customizable": true,
      "note": "These field/section names may vary by merchant"
    },
    {
      "element": "Connector Types",
      "examples": ["AWS S3", "AWS RDS", "AWS Redshift", "Databricks"],
      "customizable": true,
      "note": "Specific to Teleskope's platform offerings"
    },
    {
      "element": "Billing Model",
      "note": "Section exists but not filled in this document - to be completed by Implementation team"
    },
    {
      "element": "POC Contacts",
      "fields": ["Implementation POC", "CX POC"],
      "customizable": true,
      "note": "Merchant-specific contact information"
    }
  ],
  "confidence_score": 0.75,
  "confidence_notes": "Document appears incomplete (cut off mid-sentence, missing sections marked 'to fill'). Core rules are clear, but some context about billing model and complete evaluation period handling is missing. High confidence in extracted rules that are present, lower confidence that all rules are captured."
}
```

---

## Chunk 2: MIS_ Teleskope AI_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:19:40

### Original Content
```
agreement terms state that they can opt-in after 30 days so billing will start on the effective date (service start date)   30 Some of Teleskope's contracts have a 60 day opt out This 60 day trial period adjusts their billing start date and net terms: instead of billing on contract start date with 90 day net terms, the first billing date becomes 60 days after contract start date and the original 90 day net terms becomes 30 days Otherwise, Match the Service Start Date Months of Service: Use [x] m...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing timing and payment terms configuration",
    "Contract term defaults and frequency settings",
    "Integration item categorization and handling",
    "Opt-in/opt-out trial period adjustments",
    "Document processing workflow and team notifications"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "defaults"
    },
    {
      "rule": "Default net payment terms is 30 days if none listed",
      "category": "defaults"
    },
    {
      "rule": "Default billing frequency is Monthly if none listed",
      "category": "defaults"
    },
    {
      "rule": "Months of Service should use [x] months based on subscription term years; default to 12 if none mentioned",
      "category": "billing_configuration"
    },
    {
      "rule": "Set frequency to Annual based on annual price when no sub-annual billing mentioned",
      "category": "billing_configuration"
    },
    {
      "rule": "Match Service Start Date to contract terms",
      "category": "billing_configuration"
    },
    {
      "rule": "Use explicitly stated net terms, default to 30 days if nothing mentioned",
      "category": "payment_terms"
    },
    {
      "rule": "Every tax line item becomes a separate BT (billing transaction)",
      "category": "tax_handling"
    },
    {
      "rule": "Ignore 'User Management & SSO' and 'Enterprise 24/7 Support' as these are bundled and listed as 'Included'",
      "category": "exclusions"
    },
    {
      "rule": "Ignore legal, invoicing, and contact info sections as not relevant for BTs",
      "category": "exclusions"
    },
    {
      "rule": "Implementation Success team fills post-go-live sections for Events Processing and Integration Items Processing",
      "category": "workflow"
    },
    {
      "rule": "AE fills Feature Requests and Merchant Calls prior to Implementation handoff",
      "category": "workflow"
    }
  ],
  "exceptions": [
    {
      "exception": "30-day opt-in clause: Billing starts on effective date (service start date) + 30 days",
      "condition": "When agreement includes 30-day opt-in terms"
    },
    {
      "exception": "60-day opt-out trial: First billing date becomes 60 days after contract start date, and original 90-day net terms becomes 30 days",
      "condition": "Some Teleskope contracts with 60-day opt-out",
      "impact": "Adjusts both billing start date and net terms"
    },
    {
      "exception": "Net terms adjustment: Original payment terms minus the number of days in evaluation opt-in/opt-out period",
      "condition": "When there is an opt-out or opt-in clause"
    },
    {
      "exception": "Enterprise deals on other company's paper: Process two documents (Teleskope proposal for billing terms/prices, Purchase Order for PO number and start date)",
      "condition": "Occasionally for Enterprise deals"
    },
    {
      "exception": "Integration items for Statsig should be labeled as 'Sales'",
      "condition": "Merchant-specific: Statsig"
    },
    {
      "exception": "Integration items for Pinata should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "condition": "Merchant-specific: Pinata"
    },
    {
      "exception": "Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase",
      "condition": "Merchant-specific: Messari"
    }
  ],
  "merchant_specific": [
    {
      "merchant": "Teleskope",
      "elements": [
        "Some contracts have 60-day opt-out trial periods",
        "30-day opt-in clauses in some agreements",
        "Integration items: Cloud Data Store Connector, Enterprise Support, User Management & SSO",
        "Occasionally sends Enterprise deals on other company's paper (two-document process)",
        "Annual upfront payments for annual or multiyear contracts",
        "Flat Subscription Fee for 100% of contracts",
        "Some customers have usage-based billing: # of integrations × price per integration",
        "Currently manually billing in QBO and reporting in Excel",
        "Purchased Tabs for flexible platform to support fundraising reporting"
      ]
    },
    {
      "merchant": "Statsig",
      "elements": [
        "All integration items labeled as 'Sales'"
      ]
    },
    {
      "merchant": "Pinata",
      "elements": [
        "Integration items labeled as 'Software Subscription Bundle' unless otherwise noted"
      ]
    },
    {
      "merchant": "Messari",
      "elements": [
        "Customer Success (Azmat Aziz) notification required in internal merchant channel when contracts processed in Active phase"
      ]
    },
    {
      "customization_areas": [
        "Invoice date back-dating (e.g., to final day of month)",
        "Integration item categorization varies by merchant",
        "Post-processing notification requirements",
        "Customer-specific memos on certain invoices",
        "Invoice changes due to merchant-customer relationships"
      ]
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: MIS_ Teleskope AI_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:19:49

### Original Content
```
They currently have a ton of pain around midcontract amendments and tracking cash forecasting and collections 1) What is the merchant temperament Super chill Adam is VP of Operations and part of the founding team Runs finances and wants to automate it to take it off of his plate Lizzy is CEO and knows Ali and Rebecca through Primary Great personality and very bubbly 3) What are the Tabs features that the key POC cares about Automated Collections to have visibility into DSO Payment reconciliation...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payment and Collections Automation",
    "Financial Reporting and Forecasting",
    "Accounting System Integration (QuickBooks Online)",
    "Contract Management and Revenue Recognition",
    "Operational Efficiency and Process Automation"
  ],
  "rules": [
    {
      "rule": "Automated collections must provide visibility into Days Sales Outstanding (DSO)",
      "category": "collections",
      "explicit": true
    },
    {
      "rule": "Payment reconciliation must sync to QuickBooks Online (QBO)",
      "category": "integration",
      "explicit": true
    },
    {
      "rule": "QBO integration must match contracts and products to customers",
      "category": "integration",
      "explicit": true
    },
    {
      "rule": "Cash forecasting must be based on future invoices",
      "category": "forecasting",
      "explicit": true
    },
    {
      "rule": "Revenue recognition and ARR reporting must provide board-ready confident data",
      "category": "reporting",
      "explicit": true
    },
    {
      "rule": "System must address mid-contract amendments tracking",
      "category": "contract_management",
      "explicit": false
    },
    {
      "rule": "Solution must reduce manual workload for operations/finance team",
      "category": "automation",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Mid-contract amendments require special tracking and handling",
      "context": "Current pain point that needs addressing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key stakeholders: Adam (VP Operations, founding team) and Lizzy (CEO)",
      "type": "personnel",
      "customization_needed": "Stakeholder communication and approval workflows"
    },
    {
      "element": "Merchant temperament: 'Super chill'",
      "type": "relationship_management",
      "customization_needed": "Communication style and support approach"
    },
    {
      "element": "QuickBooks Online as accounting system",
      "type": "integration",
      "customization_needed": "Specific QBO integration configuration"
    },
    {
      "element": "Board reporting requirements",
      "type": "reporting",
      "customization_needed": "Custom report formats and metrics for board presentations"
    },
    {
      "element": "Connection through Primary (Ali and Rebecca)",
      "type": "relationship",
      "customization_needed": "Relationship management and referral tracking"
    },
    {
      "element": "Pain points: mid-contract amendments, cash forecasting, collections tracking",
      "type": "business_process",
      "customization_needed": "Prioritization of feature rollout and implementation"
    }
  ],
  "confidence_score": 0.85
}
```

---

