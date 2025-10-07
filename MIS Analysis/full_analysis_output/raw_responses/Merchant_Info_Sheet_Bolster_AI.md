# Raw LLM Analysis: Merchant Info Sheet - Bolster AI

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:04:48

---

## Chunk 1: Merchant Info Sheet - Bolster AI_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:48

### Original Content
```
we Merchant Demo date: Nov 14, 2024 Scoping start date: Nov 14, 2024 MSA Signature Date: Nov 14, 2024 Onboarding Kick Off Date: Nov 14, 2024 [If Exists] Opt Out Date: Oct Go Live Date: Nov 14, 2024 GTM POC: Implementation POC: ERP: 7 Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary (AE to fill) Summary of what company does: Goals (North star) (AE  Implementation to fill) What is the mercha...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Roles",
    "Merchant Goals and Value Proposition",
    "Billing Model and Customer Creation Process",
    "Contract Processing and Service Configuration"
  ],
  "rules": [
    "Service Start Date defaults to 'License Start Date'",
    "If License Start Date is unavailable, use 'Effective Date' as fallback",
    "Contract term must be identified and stated in months (e.g., 9-month co-term)",
    "Item Name must be located and specified (product name identification required)",
    "Multiple critical dates must be tracked: MSA Signature Date, Scoping Start Date, Onboarding Kick Off Date, Go Live Date, and optional Opt Out Date",
    "Key stakeholders must be identified across multiple functions: Accountant, CFO, Customer Service Rep, Account Receivable POC, Billing POC",
    "ERP and Tax Integration systems must be documented",
    "GTM POC and Implementation POC must be assigned",
    "Company summary must include what the company does (AE responsibility)",
    "Goals section must document: merchant's goal, pain points being solved, and purchase motivation",
    "Opt-out clause existence must be verified and documented",
    "If opt-out clause exists, conditions to prevent exercise must be identified",
    "Billing model documentation must cover: customer creation process uniqueness, billing methodology, and contract structure"
  ],
  "exceptions": [
    "Opt Out Date is conditional - only required '[If Exists]'",
    "Service Start Date has a fallback hierarchy: License Start Date (primary) → Effective Date (secondary)",
    "Unique customer creation processes may exist per merchant requiring special documentation",
    "One-off merchant-specific items may need to be documented outside standard fields"
  ],
  "merchant_specific": [
    "ERP system type (varies by merchant)",
    "Tax Integration system (merchant-dependent)",
    "Specific key personnel names and roles (Accountant, CFO, CSR, AR POC, Billing POC)",
    "Company summary and business description",
    "North star goals and specific pain points",
    "Purchase motivation and use case",
    "Billing model variations and contract structure",
    "Customer creation process uniqueness",
    "Opt-out clause terms and prevention conditions",
    "One-off merchant-specific requirements",
    "Product/Item names (e.g., 'Bolster Dark Web Module', 'Bolster Platform Access')",
    "Contract term length (e.g., 9-month co-term)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Bolster AI_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:49

### Original Content
```
Item Description: remove tier from description Leave blank Integration Item: Platform   Enterprise Platform Social Media   Social Media Dark Web   Darkweb Discount   Discount Billing Type: Usually Flat Total Price: Locate the gross price prior to any applicable discounts Process discounts as a separate BT All discounts lump summed together regardless of name (ie legacy discount, CEO discount, reseller discount, etc) Quantity: Identify if there is a mention of the number of licenses or units cove...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Normalization",
    "Billing Configuration and Invoice Processing",
    "Default Values and Standardization",
    "Merchant-Specific Customization and Communication",
    "Integration Item Classification and Mapping"
  ],
  "rules": [
    {
      "category": "Item Description",
      "rule": "Remove tier information from description and leave blank for integration items"
    },
    {
      "category": "Integration Item Mapping",
      "rule": "Platform maps to Enterprise Platform"
    },
    {
      "category": "Integration Item Mapping",
      "rule": "Social Media maps to Social Media"
    },
    {
      "category": "Integration Item Mapping",
      "rule": "Dark Web maps to Darkweb"
    },
    {
      "category": "Integration Item Mapping",
      "rule": "Discount maps to Discount"
    },
    {
      "category": "Billing Type",
      "rule": "Usually set to Flat"
    },
    {
      "category": "Total Price",
      "rule": "Locate gross price prior to any applicable discounts"
    },
    {
      "category": "Discount Processing",
      "rule": "Process all discounts as a separate billing type (BT)"
    },
    {
      "category": "Discount Processing",
      "rule": "All discounts are lumped together regardless of name (legacy discount, CEO discount, reseller discount, etc.)"
    },
    {
      "category": "Quantity",
      "rule": "Identify number of licenses or units covered under the agreement"
    },
    {
      "category": "Quantity Default",
      "rule": "Default to 1 if nothing else is mentioned"
    },
    {
      "category": "Start Date",
      "rule": "Identify the 'Effective Date' which is usually the last signature date"
    },
    {
      "category": "Start Date Fallback",
      "rule": "Default to 'License Start Date' if Effective Date isn't available"
    },
    {
      "category": "Periods",
      "rule": "Verify whether the contract is a one-time purchase or an ongoing subscription"
    },
    {
      "category": "Frequency",
      "rule": "Determine how often invoices are issued"
    },
    {
      "category": "Payment Terms",
      "rule": "Payment terms are mentioned in the contract under 'Terms of Use'"
    },
    {
      "category": "Billing Timing",
      "rule": "Bill first of period"
    },
    {
      "category": "Default Service Term",
      "rule": "If none listed, Ops default is 1 Year"
    },
    {
      "category": "Default Net Payment Terms",
      "rule": "If none listed, Ops default is 30 days"
    },
    {
      "category": "Default Billing Frequency",
      "rule": "If none listed, Ops default is Monthly"
    },
    {
      "category": "Tax Line Items",
      "rule": "Every tax line item becomes a billing type (BT)"
    }
  ],
  "exceptions": [
    {
      "description": "Merchant-specific processing that may differ by contract",
      "example": "Always back-date invoice date to final day of the month (merchant-specific request)"
    },
    {
      "description": "Integration item labeling exceptions",
      "example": "All Statsig integration items should be labeled as 'Sales'"
    },
    {
      "description": "Integration item labeling with conditional override",
      "example": "All 'Pinata' integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
    },
    {
      "description": "Special customer-specific requirements",
      "example": "Special memos certain invoices require, invoice changes due to merchant customer relationship"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract Processing Specifics",
      "description": "Merchant-requested processing that may differ by contract (e.g., invoice date back-dating)"
    },
    {
      "element": "Integration Item Assignment",
      "description": "Specific instructions for assigning integration items vary by merchant (Statsig, Pinata examples provided)"
    },
    {
      "element": "Post Processing Communications",
      "description": "Notification requirements vary by merchant - who needs to be notified, where, and when"
    },
    {
      "element": "Customer Information",
      "description": "Merchant-specific customer details, special memos, and invoice changes based on customer relationships"
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific feature requests with importance and urgency tracking"
    },
    {
      "element": "Merchant Relationship Information",
      "description": "Important context about how merchant bills and relationship dynamics"
    },
    {
      "element": "Events Processing",
      "description": "Merchant-specific instructions for events billing (if necessary)"
    },
    {
      "element": "Example Contract Reference",
      "description": "Arlo Anything mentioned as example contract with specific items to ignore"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Bolster AI_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:57

### Original Content
```
1) What is the merchant temperament 2) Is there a key POC: (i e : who is the buyer decision maker ) 3) What are the Tabs features that the key POC cares about
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship assessment and profiling",
    "Stakeholder identification and decision-making hierarchy",
    "Product feature prioritization and value proposition alignment",
    "Customer discovery and needs analysis"
  ],
  "rules": [
    "Must identify and document the merchant's temperament/personality type",
    "Must identify the key Point of Contact (POC) who serves as the buyer decision maker",
    "Must determine which Tabs product features are most important to the key POC",
    "Information gathering should focus on three specific dimensions: temperament, decision maker, and feature preferences"
  ],
  "exceptions": [
    "No explicit exceptions mentioned in this document chunk",
    "Implicit flexibility: the 'key POC' may vary by merchant organizational structure"
  ],
  "merchant_specific": [
    "Merchant temperament - will vary by individual merchant personality and business culture",
    "Key POC identity - specific person/role will differ per merchant organization",
    "Feature priorities - different merchants will care about different Tabs features based on their business needs",
    "Decision-making structure - may vary from single decision maker to committee-based decisions",
    "The term 'Tabs features' suggests a specific product offering that requires merchant-specific feature mapping"
  ],
  "confidence_score": 0.85
}
```

---

