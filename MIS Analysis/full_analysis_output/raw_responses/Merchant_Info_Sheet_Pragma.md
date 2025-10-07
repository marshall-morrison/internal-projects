# Raw LLM Analysis: Merchant Info Sheet - Pragma

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:26:47

---

## Chunk 1: Merchant Info Sheet - Pragma_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:47

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
    "Discount and Pricing Variation Management"
  ],
  "rules": [
    "Extract BTs from the fee table at the top of each contract or from attached 'Order Form' or 'Exhibit A' sections",
    "For addendum contracts, process BTs under the original contract",
    "Item Name should use the description from the contract (e.g., 'Platform License Fee', 'Development License')",
    "Billing Start Date should use the 'Effective Date' of the agreement unless another billing date is explicitly listed",
    "Service Start Date should be the same as the Billing Start Date",
    "Months of Service should use the 'Term' from the contract or Order Form",
    "Default to 12 months if only described as 'annual' or not specified",
    "When usage milestones cannot be predicted, default to following the date cutoff",
    "Only process what can be known at the time of contract processing"
  ],
  "exceptions": [
    "Discounts that cause different prices require separate BTs with different invoice schedules during the discount period",
    "Pre-launch or promotional discounts with dual conditions (date OR usage milestone) should default to the date-based cutoff when usage cannot be predicted",
    "Example: Monthly fee changes based on 'sooner of [date] or [usage milestone]' - use the date cutoff as the determining factor",
    "Addendum contracts follow different processing rules (must be linked to original contract)"
  ],
  "merchant_specific": [
    "Merchant Name field (to be filled by AE)",
    "Pragma Implementation POC (to be filled by IM)",
    "CX POC (to be added by IMP)",
    "Billing model section (Implementation team to fill)",
    "Unique customer creation process per merchant",
    "Merchant-specific billing methods and contract structure",
    "One-off merchant-specific considerations",
    "Merchant-specific terminology for line items (e.g., 'Platform License Fee' vs 'Development License')",
    "Merchant-specific discount structures and pricing variations"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Pragma_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:51

### Original Content
```
, automatic 1-month renewal), use only the initial term Frequency: Contract will state what the billing cadence is Mostly monthly or annual Default to monthly if nothing available Total Price: Use the stated monthly fee or usage tier If discount rate is mentioned (e g Pre-Launch Discount - see Example  1), create a BT that follows this logic Quantity: Default to 1 for flat fees unless explicitly mentioned For tiered usage-based fees, use the structure as described (e g , "0-24,999 users") Net Te...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Configuration Rules",
    "Pricing Structure Processing (flat fees, tiered, usage-based)",
    "Default Values and Fallback Logic",
    "Mandatory Usage Components and Standard Inclusions",
    "Exclusion Criteria for Certain Fee Types"
  ],
  "rules": [
    "For auto-renewal contracts, use only the initial term, not the renewal period",
    "Billing frequency defaults to monthly if not specified in contract",
    "Default quantity is 1 for flat fees unless explicitly stated otherwise",
    "Net payment terms default to 30 days if not specified in Payment Terms section",
    "FirstLook License products must use 'Firstlook' revenue category",
    "Always include four mandatory usage components: Buildkite (Unit Fee: 1), Honeycomb (Unit Fee: 1), AWS - Retail Price (Unit Fee: 1), and AWS - Savings (Unit Fee: -1)",
    "Mandatory usage components inherit terms from other usage BTs in contract, or default to monthly in arrears if none exist",
    "Event type must match item name exactly",
    "Process all CCU (Concurrent User) model fees as tiered units",
    "For opt-in BTs with multiple options, create separate BT for each option",
    "Process support fees, which may be tiered unit BTs if monthly allotment exists",
    "Support fees with monthly allotments should be configured as tier unit BT monthly in arrears",
    "Discounts must be processed as negative BTs",
    "AWS - Savings is a negative BT functioning as a discount",
    "Verify support fees are not already bundled into monthly platform fee before processing separately"
  ],
  "exceptions": [
    "Ignore 'Wind Down Pricing' or fallback pricing",
    "Ignore Revenue Sharing arrangements",
    "Do not process Usage Fees that are contingent on customer exceeding a revenue threshold (e.g., Web3 Threshold where usage fees only apply if Web3 revenue exceeds 20% of product revenue)",
    "Do not enter BTs for 'Pass Through Fees' unless a base or fixed component is defined",
    "For tiered usage-based fees, use specific structure format (e.g., '0-24,999 users') rather than default quantity of 1"
  ],
  "merchant_specific": [
    "Revenue Category mapping requires reference to separate sheet",
    "FirstLook License products have specific revenue category assignment",
    "Buildkite, Honeycomb, and AWS components appear to be standard integrations that may vary by merchant",
    "CCU (Concurrent User) model may be specific to certain merchant types",
    "Web3 Threshold example suggests blockchain/crypto merchant scenarios",
    "Support fee structures and bundling vary by merchant agreement",
    "Discount structures and pre-launch pricing are merchant-negotiated",
    "Opt-in BT options require merchant to later select/delete non-chosen options"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Pragma_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:27:06

### Original Content
```
Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on event...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Post-implementation processing workflows and responsibilities",
    "Merchant-specific billing and contract configurations",
    "Cross-team communication and notification protocols",
    "Merchant context and relationship management"
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
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation fills Feature Requests prior to go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Success team fills Feature Requests post-go-live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "All Gong calls should be documented in Slack",
      "category": "Documentation",
      "explicit": true
    },
    {
      "rule": "Implementation is completion DRI (Directly Responsible Individual) on handoff",
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
      "exception": "Invoice date may be back-dated to final day of the month per merchant contract",
      "condition": "Merchant-specific contract requirement",
      "type": "Date Processing Override"
    },
    {
      "exception": "Tax line item handling may differ from default BT Events Processing",
      "condition": "If specifically listed in merchant instructions",
      "type": "Tax Processing Override"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Specific customer relationships",
      "type": "Invoice Customization"
    },
    {
      "exception": "Invoice changes may be required due to merchant-customer relationship",
      "condition": "Specific merchant-customer dynamics",
      "type": "Invoice Modification"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: Pragma (video game engine company)",
      "type": "Company Identity"
    },
    {
      "element": "Primary POC: Gideon (Business Operations Analyst)",
      "type": "Contact Information"
    },
    {
      "element": "Merchant temperament: 'Really nice, has a ton on his plate'",
      "type": "Relationship Context"
    },
    {
      "element": "Key pain point: Manual invoice creation and referencing Google sheets for pricing and usage",
      "type": "Business Problem"
    },
    {
      "element": "Key feature interest: Invoice creation automation",
      "type": "Feature Priority"
    },
    {
      "element": "Customer base: Approximately 40 customers, growing quickly post-Game Developers Conference",
      "type": "Business Context"
    },
    {
      "element": "Billing model: Annual contracts with monthly usage",
      "type": "Billing Configuration"
    },
    {
      "element": "No sales tax solution mentioned",
      "type": "Tax Configuration"
    },
    {
      "element": "Business model: Backend infrastructure for video game creators",
      "type": "Industry Context"
    },
    {
      "element": "Notification example: Customer Success (Azmat Aziz) notified in internal merchant channel when contracts processed in Active phase",
      "type": "Communication Protocol"
    }
  ],
  "confidence_score": 0.85
}
```

---

