# Raw LLM Analysis: in.beat Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:31:22

---

## Chunk 1: in.beat Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:31:22

### Original Content
```
Will tackle this after implementation is complete for the rest of their customers Events Processing (if necessary) A handful of their customers are also villages based on social media usage All calculations are already computed, and they will be using Tabs usage function to upload the monthly   amounts of spend per customer Usage contracts will call this out in a few different ways Look for  Media Management Fee This will exist either in a table or a paragraph, 2 examples listed below If this is...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Usage-based billing and event processing for media management fees",
    "Integration item mapping to service types",
    "Customer segmentation and social media usage tracking",
    "Service type categorization and integration details",
    "Post-processing communication workflows"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "When 'Media Management Fee' is identified in contract (table or paragraph), create a billing term with Title: 'Media Buy Management Fee', Type: 'Unit price', Amount: 1",
      "category": "billing_term_creation"
    },
    {
      "rule_id": "R2",
      "description": "For Media Management Fee billing terms, set Integration item to 'Paid Media Management Fee' and Event Type to 'Paid Media Spend'",
      "category": "integration_mapping"
    },
    {
      "rule_id": "R3",
      "description": "Do not process minimums, access fee discounts when Media Management Fee is present",
      "category": "billing_exclusions"
    },
    {
      "rule_id": "R4",
      "description": "Integration item should equal the Service Type identified in the contract",
      "category": "integration_mapping"
    },
    {
      "rule_id": "R5",
      "description": "If Service Type is not included in contract, leave integration item blank for merchant to update",
      "category": "integration_mapping"
    },
    {
      "rule_id": "R6",
      "description": "Monthly spend amounts per customer are uploaded using Tabs usage function",
      "category": "usage_processing"
    },
    {
      "rule_id": "R7",
      "description": "All calculations are pre-computed before upload",
      "category": "usage_processing"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Some customers are villages based on social media usage - requires special handling",
      "condition": "Customer type classification"
    },
    {
      "exception_id": "E2",
      "description": "Media Management Fee can appear in either table format or paragraph format",
      "condition": "Contract format variation"
    },
    {
      "exception_id": "E3",
      "description": "Minimums and access fee discounts are explicitly excluded from processing when Media Management Fee is present",
      "condition": "Presence of Media Management Fee"
    },
    {
      "exception_id": "E4",
      "description": "If integration item cannot be determined, leave blank for merchant self-service update",
      "condition": "Missing service type information"
    }
  ],
  "merchant_specific": [
    {
      "element": "Service Type to Integration Item Mapping",
      "details": "Specific mappings provided: Influencer Marketing → Influencer Marketing, Spark Ads → Influencer Marketing, User-Generated Content → Influencer Generated Content, Paid Media → Paid Media Management Fee, UGC Only → Influencer Generated Content, SEO Services → Link Building",
      "customization_needed": true
    },
    {
      "element": "Customer segmentation criteria",
      "details": "Villages classification based on social media usage - merchant-specific definition",
      "customization_needed": true
    },
    {
      "element": "Post-processing notification requirements",
      "details": "Ops Team notification requirements for batch completion vary by implementation/active phase",
      "customization_needed": true
    },
    {
      "element": "Usage contract format",
      "details": "Media Management Fee can be presented in multiple formats (table or paragraph)",
      "customization_needed": false
    },
    {
      "element": "Tabs usage function",
      "details": "Specific upload mechanism for monthly spend amounts",
      "customization_needed": false
    }
  ],
  "confidence_score": 0.72
}
```

**Confidence Reasoning**: The document appears to be internal operational instructions with some formatting issues and incomplete sections (e.g., "Post Processing Communications" and "Customer Information" sections have headers but minimal content). The core billing and integration rules are relatively clear, but context about the overall process flow and some conditional logic is fragmented. The service type mapping table is clear, but the relationship between different sections could be better defined.

---

## Chunk 2: in.beat Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:31:24

### Original Content
```
Merchant Demo date: April, 22, 2024 Scoping start date: none MSA Signature Date: May 28, 2024 Onboarding Kick Off Date: TBD Go Live Date: TBD GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: n a CFO: Yan Ray (raise inbeat agency) Customer service rep who is really involved: Account Receivable POC: Reymon Billing POC: n a etc Company summary inBeat is a performance-forward Creator Content Marketing Agency Goals To automate the manual process in their AR workfl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Creation",
    "Milestone-Based Payment Structures",
    "Default Values for Missing Contract Information",
    "Merchant Profile and Relationship Management",
    "Multi-Currency and Tax Handling"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Processing",
      "description": "When processing contracts with Fee Breakdown columns, each fee item should become its own billing term with the invoice stage and percentage included in the description",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Milestone Defaults - 3 Milestones",
      "description": "For contracts with 3 milestones when dates are not specified: First invoice at project start date (Net 0), Mid-term invoice at 45 days from project start (Net 15), Final invoice at 90 days from project start (Net 15)",
      "explicit": true
    },
    {
      "rule_id": "R3",
      "category": "Milestone Defaults - 2 Milestones",
      "description": "For contracts with 2 milestones: First invoice at project start date, Second invoice at 60 days from project start date",
      "explicit": true
    },
    {
      "rule_id": "R4",
      "category": "Monthly Terms",
      "description": "When contract specifies Month 1, Month 2, etc., default to consecutive monthly terms with Net 15 if payment terms not specified",
      "explicit": true
    },
    {
      "rule_id": "R5",
      "category": "Default Values",
      "description": "Default Service Term if none listed: 1 Year",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Default Values",
      "description": "Default Net Payment Terms if none listed: Net 0",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Default Values",
      "description": "Default Billing Frequency if none listed: Monthly",
      "explicit": true
    },
    {
      "rule_id": "R8",
      "category": "Tax Handling",
      "description": "Most customers are not charged sales tax, only Canada customers are charged sales tax",
      "explicit": true
    },
    {
      "rule_id": "R9",
      "category": "Billing Term Structure",
      "description": "Each billing term should include: Item name, Item Description (with invoice stage and percentage), Price, and Payment Terms",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Multi-currency support required for this merchant",
      "context": "Merchant has multi-currency billing needs"
    },
    {
      "exception_id": "E2",
      "description": "Tax is only applied to Canadian customers, not to most other customers",
      "context": "Tax handling differs by customer geography"
    },
    {
      "exception_id": "E3",
      "description": "Milestone payment terms vary based on number of milestones (2 vs 3) and have different Net terms",
      "context": "First milestone in 3-milestone structure has Net 0, while subsequent milestones have Net 15"
    },
    {
      "exception_id": "E4",
      "description": "Milestone structures are not limited to kick-off/mid-term/completion naming conventions",
      "context": "The example structure is provided but other milestone naming is acceptable"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "inBeat is a performance-forward Creator Content Marketing Agency",
      "customizable": true
    },
    {
      "element": "Key Personnel",
      "details": "CFO: Yan Ray, Account Receivable POC: Reymon",
      "customizable": true
    },
    {
      "element": "Merchant Goals",
      "details": "Automate manual AR workflow processes",
      "customizable": true
    },
    {
      "element": "Merchant Temperament",
      "details": "Very chill",
      "customizable": true
    },
    {
      "element": "Fee Structure",
      "details": "Typical fees include: Influencer Marketing Fee, Media Management Fee, Media Budget",
      "customizable": true
    },
    {
      "element": "Multi-Currency Support",
      "details": "Merchant requires multi-currency billing capabilities",
      "customizable": true
    },
    {
      "element": "Milestone-Based Billing",
      "details": "Contracts operate based on project deliverable milestones rather than fixed calendar dates",
      "customizable": true
    },
    {
      "element": "Contract Ignore Rules",
      "details": "Nothing to ignore in contracts for this merchant",
      "customizable": true
    },
    {
      "element": "Project Timeline Dates",
      "details": "Demo: April 22, 2024; MSA Signature: May 28, 2024; Onboarding and Go Live: TBD",
      "customizable": true
    }
  ],
  "confidence_score": 0.92
}
```

---

