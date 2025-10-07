# Raw LLM Analysis: Eino Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:45:19

---

## Chunk 1: Eino Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:19

### Original Content
```
Merchant Demo date: Apr 2, 2025 Scoping start date: n a MSA Signature Date: Apr 16, 2025 Onboarding Kick Off Date: n a [If Exists] Opt Out Date: none Go Live Date: n a GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Payman Samadihttps: www linkedin com in payman-samadi  Company summary (AE to fill) Summary of what company does: Eino is an AI-powered connectivity planning platform that holistically designs and simulates solution architecture for public and private W...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Invoice Handling",
    "Billing Term Configuration and Service Dates",
    "Payment Terms and Frequency Management",
    "Merchant Onboarding and Implementation Timeline",
    "Customer Pain Points and Product Goals"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Invoice Processing",
      "description": "Each invoice line item must be treated as a separate Billing Term (BT)",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Date Management",
      "description": "Billing Start Date must use the invoice date",
      "explicit": true
    },
    {
      "rule_id": "R3",
      "category": "Date Management",
      "description": "Service Start Date defaults to same as Billing Start Date unless otherwise specified",
      "explicit": true
    },
    {
      "rule_id": "R4",
      "category": "Service Duration",
      "description": "Annual licenses or subscriptions use 12 months of service",
      "explicit": true
    },
    {
      "rule_id": "R5",
      "category": "Service Duration",
      "description": "Project-based or one-time items use 0 months of service",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Billing Frequency",
      "description": "Annual or subscription items have Frequency = Annual",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Billing Frequency",
      "description": "One-time services have Frequency = Annual",
      "explicit": true
    },
    {
      "rule_id": "R8",
      "category": "Payment Terms",
      "description": "Net Terms = 0 when invoice states 'Due on receipt'",
      "explicit": true
    },
    {
      "rule_id": "R9",
      "category": "Payment Terms",
      "description": "Net Terms = 45 when invoice states 'Net 45'",
      "explicit": true
    },
    {
      "rule_id": "R10",
      "category": "Payment Terms",
      "description": "Use the TERMS field on each invoice for Net Terms determination",
      "explicit": true
    },
    {
      "rule_id": "R11",
      "category": "Pricing",
      "description": "Total Price uses the Amount field for each line item",
      "explicit": true
    },
    {
      "rule_id": "R12",
      "category": "Pricing",
      "description": "Discounts are processed as a negative Billing Term",
      "explicit": true
    },
    {
      "rule_id": "R13",
      "category": "Quantity",
      "description": "Use the quantity listed per line item; default to 1 if not listed",
      "explicit": true
    },
    {
      "rule_id": "R14",
      "category": "Item Details",
      "description": "Item Name uses the SERVICE DESCRIPTION from each line item",
      "explicit": true
    },
    {
      "rule_id": "R15",
      "category": "Item Details",
      "description": "Item Description should be left blank unless specific context is needed",
      "explicit": true
    },
    {
      "rule_id": "R16",
      "category": "Defaults",
      "description": "Default Service Term is 1 Year if none listed",
      "explicit": true
    },
    {
      "rule_id": "R17",
      "category": "Defaults",
      "description": "Default Net Payment Terms is 0 if none listed",
      "explicit": true
    },
    {
      "rule_id": "R18",
      "category": "Defaults",
      "description": "Default Billing Frequency is Monthly if none listed",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Service Start Date can differ from Billing Start Date when otherwise specified",
      "condition": "When explicitly stated in contract"
    },
    {
      "exception_id": "E2",
      "description": "Specific project-based or one-time items (e.g., clutter data per site) use 0 months instead of 12",
      "condition": "When item is identified as one-time or project-based"
    },
    {
      "exception_id": "E3",
      "description": "Item Description can be populated when specific context is needed",
      "condition": "When additional context is required"
    },
    {
      "exception_id": "E4",
      "description": "Merchant-specific processing may differ by contract",
      "condition": "When merchant requests specific variations (e.g., back-dating invoice dates)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "Eino - AI-powered connectivity planning platform for WiFi/Cellular networks",
      "customizable": false
    },
    {
      "element": "Key Personnel",
      "details": "CEO: Payman Samadi",
      "customizable": false
    },
    {
      "element": "Merchant Goals",
      "details": "Wants non-GAAP metrics and to stop paying Stripe fees",
      "customizable": true
    },
    {
      "element": "Billing Model",
      "details": "Flat recurring SaaS fees and one-offs; transitioning from emails to contracts",
      "customizable": true
    },
    {
      "element": "Contract Processing Variations",
      "details": "May include merchant-requested specifics that differ by contract (e.g., back-dating invoice dates)",
      "customizable": true
    },
    {
      "element": "Tax Handling",
      "details": "Question raised about handling taxes as line items (incomplete information)",
      "customizable": true
    },
    {
      "element": "Implementation Timeline",
      "details": "Demo date: Apr 2, 2025; MSA Signature: Apr 16, 2025; Other dates TBD",
      "customizable": false
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Eino Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:20

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and billing line item processing defaults and assignments",
    "Integration item categorization and labeling rules",
    "Post-processing communication protocols and notification requirements",
    "Customer and merchant relationship management information",
    "Implementation phase documentation and handoff procedures"
  ],
  "rules": [
    {
      "rule": "Default processing: When no specific instruction is listed, every tax line item becomes a BT Events Processing item",
      "category": "Tax Processing",
      "applies_to": "Operations Team"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Labeling",
      "applies_to": "Integration Processing"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Item Labeling",
      "applies_to": "Integration Processing"
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication Protocol",
      "applies_to": "Operations Team"
    },
    {
      "rule": "Example notification requirement: Customer Success (Azmat Aziz) needs to be notified in Messari internal merchant channel when contracts are processed during Active phase",
      "category": "Communication Protocol",
      "applies_to": "Operations Team"
    },
    {
      "rule": "International Ops Team should ignore Notes Sections marked for AE/Implementation",
      "category": "Documentation Scope",
      "applies_to": "International Operations Team"
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "condition": "Merchant provides specific alternative labeling instructions",
      "default_behavior": "Label as Software Subscription Bundle"
    },
    {
      "exception": "BT Events Processing default only applies 'if necessary' and when Implementation Success fills the requirement",
      "condition": "Conditional on necessity and Implementation Success completion",
      "default_behavior": "Apply BT Events Processing to tax line items"
    },
    {
      "exception": "Post-processing communications are conditional on necessity",
      "condition": "Only required if specified as necessary",
      "default_behavior": "No automatic notification"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customization_type": "Per-integration vendor (Statsig, Pinata, etc.)",
      "example": "Different vendors require different category labels"
    },
    {
      "element": "Post-processing notification recipients and timing",
      "customization_type": "Per-merchant notification requirements",
      "example": "Who to notify (Customer Success, specific person), where (channel), and when (phase)"
    },
    {
      "element": "Merchant billing methodology",
      "customization_type": "Per-merchant operational details",
      "example": "This merchant uses Stripe and QBO for invoicing, described as 'very small operator'"
    },
    {
      "element": "Merchant relationship information",
      "customization_type": "Per-merchant temperament and POC details",
      "example": "Temperament: Collaborative, nice, easy going; POC: CEO running finances"
    },
    {
      "element": "Customer-specific information section",
      "customization_type": "Per-merchant customer details",
      "example": "Specifics about merchant's customers (marked as 'None' in this case)"
    },
    {
      "element": "Feature requests and Rewatch calls",
      "customization_type": "Per-merchant implementation tracking",
      "example": "Links to Gong calls and feature request documentation"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: Eino Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:29

### Original Content
```
3) What are the Tabs features that the key POC cares about Reporting and stripe free pass through- he's a simple guy
```

### LLM Analysis Response
```json
{
  "themes": [
    "Product feature prioritization",
    "Stakeholder management and preferences",
    "Reporting capabilities",
    "Payment processing and fee structures"
  ],
  "rules": [
    {
      "rule": "Key POC requires access to Reporting features within Tabs platform",
      "type": "explicit",
      "category": "feature_requirement"
    },
    {
      "rule": "Stripe fee pass-through functionality must be available/enabled",
      "type": "explicit",
      "category": "payment_processing"
    },
    {
      "rule": "Solution should be kept simple to match POC's preferences",
      "type": "implicit",
      "category": "implementation_approach"
    },
    {
      "rule": "Focus implementation on core features (Reporting and Stripe pass-through) rather than comprehensive feature set",
      "type": "implicit",
      "category": "scope_management"
    }
  ],
  "exceptions": [
    {
      "exception": "POC characterized as 'simple guy' suggests preference for streamlined feature set over complex configurations",
      "condition": "Implementation should prioritize simplicity over feature breadth for this specific stakeholder"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key POC identity and role",
      "customization_needed": "Specific point of contact varies by merchant"
    },
    {
      "element": "Feature priorities (Reporting and Stripe pass-through)",
      "customization_needed": "Different merchants may prioritize different Tabs features"
    },
    {
      "element": "Stripe integration requirement",
      "customization_needed": "Payment processor choice may vary by merchant (Stripe vs alternatives)"
    },
    {
      "element": "Complexity preference ('simple guy')",
      "customization_needed": "Stakeholder sophistication and preferences vary by merchant"
    }
  ],
  "confidence_score": 0.75
}
```

---

