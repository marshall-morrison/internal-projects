# Raw LLM Analysis: [EXTERNAL USE] Pragma MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:39:25

---

## Chunk 1: [EXTERNAL USE] Pragma MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:39:25

### Original Content
```
, automatic 1-month renewal), use only the initial term Frequency: Contract will state what the billing cadence is Mostly monthly or annual Default to monthly if nothing available Total Price: Use the stated monthly fee or usage tier If discount rate is mentioned (e g Pre-Launch Discount - see Example  1), create a BT that follows this logic Quantity: Default to 1 for flat fees unless explicitly mentioned For tiered usage-based fees, use the structure as described (e g , "0-24,999 users") Net Te...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Configuration and Setup",
    "Pricing Structure Processing (flat fees, tiered usage, discounts)",
    "Mandatory Usage Components and Default Values",
    "Contract Data Extraction Rules (term length, frequency, pricing)",
    "Exclusion Criteria for Certain Fee Types"
  ],
  "rules": [
    "For term length: use initial term only, ignore auto-renewal periods",
    "Default billing frequency to monthly if not specified in contract",
    "Default quantity to 1 for flat fees unless explicitly stated otherwise",
    "Default net terms to 30 days if payment terms not specified in agreement",
    "Always include four mandatory usage components: Buildkite (Unit Fee: 1), Honeycomb (Unit Fee: 1), AWS - Retail Price (Unit Fee: 1), AWS - Savings (Unit Fee: -1)",
    "Mandatory usage components inherit terms from other usage BTs in contract, or default to monthly in arrears if none exist",
    "Event type must match item name exactly for usage components",
    "Process all CCU (Concurrent User) model fees as tiered units",
    "For opt-in BTs with multiple options, create separate BT for each option",
    "Process support fees, checking if they should be tiered unit BTs based on monthly allotments",
    "Verify support fees are not already bundled into monthly platform fee before processing",
    "Process discounts as negative BTs",
    "AWS - Savings should be processed as negative BT (discount)",
    "When discount rate is mentioned, create BT following specific logic",
    "Use stated monthly fee or usage tier for total price"
  ],
  "exceptions": [
    "Ignore Wind Down Pricing or fallback pricing",
    "Ignore Revenue Sharing arrangements",
    "Do not process Usage Fees contingent on revenue thresholds (e.g., Web3 Threshold example where usage fees only apply after 20% revenue threshold)",
    "Do not enter BTs for Pass Through Fees unless a base or fixed component is defined",
    "For tiered usage-based fees, use special structure format (e.g., '0-24,999 users')",
    "Merchant will later delete non-chosen options from opt-in BTs with multiple options"
  ],
  "merchant_specific": [
    "Buildkite - specific usage component requirement",
    "Honeycomb - specific usage component requirement",
    "AWS pricing components (Retail Price and Savings) - specific to AWS integrations",
    "Web3 Threshold - example of merchant-specific revenue threshold terminology",
    "CCU (Concurrent User) model - specific pricing model that may vary by merchant",
    "Support fee structures and monthly allotments - varies by merchant service agreements",
    "Opt-in BT options - merchant determines which option to keep",
    "Payment Terms location - typically in body of Agreement but may vary",
    "Pre-Launch Discount - example of merchant-specific discount types"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: [EXTERNAL USE] Pragma MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:39:28

### Original Content
```
Merchant Name (AE to fill) Pragma Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) 1 Steps to process BT location: Extract BTs from the fee table at the top of each...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and BT (Billing Transaction) Extraction",
    "Billing Model Configuration and Customer Creation",
    "Date Management (Billing Start, Service Start, Effective Dates)",
    "Contract Term and Renewal Logic Handling",
    "Pricing Variations and Discount Processing"
  ],
  "rules": [
    {
      "rule_id": "BT_EXTRACTION_001",
      "description": "Extract BTs from the fee table at the top of each contract or from attached 'Order Form' or 'Exhibit A' sections",
      "category": "data_extraction"
    },
    {
      "rule_id": "ADDENDUM_001",
      "description": "For addendum contracts, process BTs under the original contract",
      "category": "contract_processing"
    },
    {
      "rule_id": "DISCOUNT_SEPARATION_001",
      "description": "Discounts that cause different prices require separate BTs with different invoice schedules during the period",
      "category": "billing_logic"
    },
    {
      "rule_id": "USAGE_MILESTONE_001",
      "description": "When usage milestones cannot be predicted, default to following the date cutoff specified in the contract",
      "category": "conditional_billing"
    },
    {
      "rule_id": "PROCESSING_SCOPE_001",
      "description": "Only process what can be known at the time of processing (current information)",
      "category": "data_processing"
    },
    {
      "rule_id": "ITEM_NAME_001",
      "description": "Use the description from the contract for Item Name (e.g., 'Platform License Fee,' 'Development License')",
      "category": "naming_convention"
    },
    {
      "rule_id": "BILLING_START_001",
      "description": "Use the 'Effective Date' of the agreement as Billing Start Date unless another billing date is explicitly listed",
      "category": "date_management"
    },
    {
      "rule_id": "SERVICE_START_001",
      "description": "Service Start Date should be the same as the Billing Start Date",
      "category": "date_management"
    },
    {
      "rule_id": "TERM_LENGTH_001",
      "description": "Use the 'Term' from the contract or Order Form for Months of Service",
      "category": "contract_term"
    },
    {
      "rule_id": "TERM_DEFAULT_001",
      "description": "Default to 12 months if term is only described as 'annual' or not specified",
      "category": "contract_term"
    }
  ],
  "exceptions": [
    {
      "exception_id": "EXC_001",
      "description": "Pre-Launch Discount with dual conditions (date OR usage milestone)",
      "handling": "When usage milestone cannot be predicted, default to the date cutoff (e.g., August 1, 2025)",
      "example": "Monthly Fee of $10,000 until sooner of August 1, 2025 or when average CCU per hour exceeds 500"
    },
    {
      "exception_id": "EXC_002",
      "description": "Addendum contracts require different processing approach",
      "handling": "Process BTs under the original contract rather than creating new contract"
    },
    {
      "exception_id": "EXC_003",
      "description": "Explicitly listed billing dates override the Effective Date",
      "handling": "Use the explicitly listed billing date instead of the Effective Date"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "customization_needed": "AE (Account Executive) to fill",
      "type": "identification"
    },
    {
      "element": "Pragma Implementation POC",
      "customization_needed": "IM (Implementation Manager) to fill",
      "type": "contact_information"
    },
    {
      "element": "CX POC",
      "customization_needed": "IMP (Implementation) to add",
      "type": "contact_information"
    },
    {
      "element": "Billing Model Section",
      "customization_needed": "Implementation team to fill entire section including unique customer creation process, billing method, contract breakdown, and one-off merchant specifics",
      "type": "configuration"
    },
    {
      "element": "Contract Processing Steps",
      "customization_needed": "Implementation Success team to fill post-go-live",
      "type": "process_documentation"
    },
    {
      "element": "Item Name terminology",
      "customization_needed": "Varies by merchant (e.g., 'Platform License Fee' vs 'Development License')",
      "type": "terminology"
    },
    {
      "element": "Fee table location",
      "customization_needed": "May be at top of contract, in Order Form, or in Exhibit A depending on merchant",
      "type": "document_structure"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: [EXTERNAL USE] Pragma MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:39:46

### Original Content
```
Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on event...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Processing Rules and Configurations",
    "Post-Go-Live Implementation Procedures",
    "Merchant-Specific Billing and Customer Information",
    "Cross-Team Communication and Handoff Protocols",
    "Merchant Context and Relationship Management"
  ],
  "rules": [
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Contract Defaults",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Billing Defaults",
      "explicit": true
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax)",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Events Processing section post-go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Integration Items Processing section post-go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Post Processing Communications section post-go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team fills Customer Information section post-go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff",
      "category": "Handoff Process",
      "explicit": true
    },
    {
      "rule": "Implementation fills Feature Requests prior to go-live",
      "category": "Handoff Process",
      "explicit": true
    },
    {
      "rule": "Success team fills Feature Requests post-go-live",
      "category": "Handoff Process",
      "explicit": true
    },
    {
      "rule": "All Gong calls should be documented in Slack",
      "category": "Documentation",
      "explicit": true
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff notes",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Match integration item names with the integration item; if unclear, continue processing but note to US team",
      "category": "Integration Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice date can be back-dated to final day of the month per merchant contract",
      "condition": "Merchant-specific processing request",
      "type": "Date Processing Override"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Customer-specific requirements",
      "type": "Invoice Customization"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship",
      "condition": "Relationship-based modifications",
      "type": "Invoice Modification"
    },
    {
      "exception": "When integration item match is unclear, continue processing but flag for US team review",
      "condition": "Ambiguous integration mapping",
      "type": "Processing Exception"
    }
  ],
  "merchant_specific": [
    {
      "element": "Pragma (merchant name)",
      "description": "Video game engine company that helps maintain backend infrastructure for game creators",
      "category": "Merchant Identity"
    },
    {
      "element": "Gideon (POC)",
      "description": "Business operations analyst, described as nice but has a lot on his plate",
      "category": "Point of Contact"
    },
    {
      "element": "Approximately 40 customers, growing quickly after Game Developers Conference",
      "description": "Customer base size and growth trajectory",
      "category": "Business Context"
    },
    {
      "element": "Annual contracts with monthly usage billing model",
      "description": "Specific billing structure for this merchant",
      "category": "Billing Model"
    },
    {
      "element": "No sales tax solution mentioned",
      "description": "Tax handling status",
      "category": "Tax Configuration"
    },
    {
      "element": "Key feature need: Invoice creation automation",
      "description": "Primary pain point is manual invoice creation and referencing Google sheets for pricing and usage",
      "category": "Feature Requirements"
    },
    {
      "element": "Customer Success [Azmat Aziz] notification in merchant channel when contracts processed",
      "description": "Example of post-processing communication requirement",
      "category": "Communication Protocol"
    },
    {
      "element": "Merchant phase-specific actions (Implementation vs Active)",
      "description": "Different notification and processing requirements based on merchant lifecycle phase",
      "category": "Lifecycle Management"
    }
  ],
  "confidence_score": 0.85
}
```

---

