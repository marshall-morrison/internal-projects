# Raw LLM Analysis: in.beat Merchant Info Sheet(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:09:05

---

## Chunk 1: in.beat Merchant Info Sheet(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:05

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
    "Multi-Currency and Tax Handling",
    "Merchant Relationship and Implementation Details"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Processing",
      "description": "When processing contracts with Fee Breakdown columns, each fee item should become its own billing term with invoice stage and percentage in the description",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Milestone Defaults - 3 Milestones",
      "description": "For contracts with 3 milestones when dates not specified: First invoice at project start date (Net 0), Mid-term invoice at 45 days from start (Net 15), Final invoice at 90 days from start (Net 15)",
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
      "category": "Default Service Term",
      "description": "If no service term listed, operations default is 1 Year",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Default Payment Terms",
      "description": "If no payment terms specified, operations default is Net 0",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Default Billing Frequency",
      "description": "If no billing frequency listed, operations default is Monthly",
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
      "category": "Contract Processing",
      "description": "Nothing should be ignored in contracts during processing",
      "explicit": true
    },
    {
      "rule_id": "R10",
      "category": "Billing Term Structure",
      "description": "Each billing term should include: Item name, Item Description (with invoice stage and percentage), Price, and Payment Terms",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Tax exception: Canada customers are charged sales tax while most other customers are not",
      "condition": "Customer location is Canada"
    },
    {
      "exception_id": "E2",
      "description": "First milestone in 3-milestone structure uses Net 0 instead of Net 15",
      "condition": "Contract has 3 milestones and is the first invoice"
    },
    {
      "exception_id": "E3",
      "description": "Milestone structures vary based on number of milestones (2 vs 3 have different date calculations)",
      "condition": "Number of milestones in contract"
    },
    {
      "exception_id": "E4",
      "description": "Monthly term contracts use Net 15 default instead of Net 0",
      "condition": "Contract specifies Month 1, Month 2, etc. structure"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "inBeat is a performance-forward Creator Content Marketing Agency",
      "customizable": false
    },
    {
      "element": "Multi-currency Support",
      "details": "Merchant operates with multiple currencies",
      "customizable": true
    },
    {
      "element": "Key Personnel",
      "details": "CFO: Yan Ray, Account Receivable POC: Reymon",
      "customizable": true
    },
    {
      "element": "Merchant Temperament",
      "details": "Very chill",
      "customizable": true
    },
    {
      "element": "Business Goal",
      "details": "Automate the manual process in their AR workflow",
      "customizable": true
    },
    {
      "element": "Fee Structure Terminology",
      "details": "Uses specific fee types: Influencer Marketing Fee, Media Management Fee, Media Budget",
      "customizable": true
    },
    {
      "element": "Milestone Terminology",
      "details": "Uses project-based milestones: Project Kick-off, Mid-Project Checkpoint, Project Completion",
      "customizable": true
    },
    {
      "element": "Contract Structure",
      "details": "Contracts operate based on milestones of project deliverables rather than fixed dates",
      "customizable": false
    },
    {
      "element": "Customer Creation Process",
      "details": "No unique requirements for customer creation",
      "customizable": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: in.beat Merchant Info Sheet(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:07

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
    "Service type categorization and taxonomy",
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
      "category": "exclusion_rule"
    },
    {
      "rule_id": "R4",
      "description": "Integration item should equal the Service Type identified in the contract",
      "category": "integration_mapping"
    },
    {
      "rule_id": "R5",
      "description": "If Service Type is not included in contract, leave integration item blank for merchant to update",
      "category": "data_handling"
    },
    {
      "rule_id": "R6",
      "description": "Monthly spend amounts per customer are uploaded using Tabs usage function",
      "category": "data_upload"
    },
    {
      "rule_id": "R7",
      "description": "All calculations are pre-computed before processing",
      "category": "data_preparation"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Some customers are villages based on social media usage - requires special handling",
      "condition": "Customer type is village"
    },
    {
      "exception_id": "E2",
      "description": "Events processing is only necessary for a handful of customers",
      "condition": "Customer requires events processing"
    },
    {
      "exception_id": "E3",
      "description": "Usage contracts call out Media Management Fee in different ways (table or paragraph format)",
      "condition": "Variable contract format"
    },
    {
      "exception_id": "E4",
      "description": "Integration item left blank when Service Type not specified - merchant updates later",
      "condition": "Missing Service Type in contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Service Type taxonomy",
      "description": "Specific mapping of service types to integration items: Influencer Marketing, Spark Ads, User-Generated Content, Paid Media Management Fee, UGC Only, SEO Services/Link Building",
      "customization_needed": true
    },
    {
      "element": "Customer segmentation",
      "description": "Village-based customers identified by social media usage patterns",
      "customization_needed": true
    },
    {
      "element": "Post-processing notifications",
      "description": "Ops Team notification requirements for batch completion vary by implementation/active phase",
      "customization_needed": true
    },
    {
      "element": "Media Management Fee detection",
      "description": "Contract language and format for identifying Media Management Fee varies",
      "customization_needed": true
    },
    {
      "element": "Usage upload method",
      "description": "Tabs usage function used for monthly spend uploads",
      "customization_needed": false
    }
  ],
  "confidence_score": 0.72
}
```

**Confidence Reasoning**: The document appears to be internal operational instructions with some fragmented formatting and incomplete sections (e.g., "Will tackle this after implementation is complete" suggests work-in-progress documentation). The core rules around Media Management Fee processing are clear and explicit, as is the service type mapping table. However, several sections reference processes "if necessary" without clear criteria, and some contextual information about the merchant's business model and complete workflows is missing. The confidence score reflects high certainty about the explicit billing rules but moderate uncertainty about the complete operational context and edge cases.

---

