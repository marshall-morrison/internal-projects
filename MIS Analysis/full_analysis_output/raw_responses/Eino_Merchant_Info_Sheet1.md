# Raw LLM Analysis: Eino Merchant Info Sheet(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:09:40

---

## Chunk 1: Eino Merchant Info Sheet(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:40

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant None Feature Requests (AE Implementation Success to fill) None Rewatch Calls (AE Implementation Success to fill) https: us-56595 app gong io call id 4025946868595269773 account-id 59151...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Merchant Relationship Management",
    "Billing and Payment Processing Systems",
    "Feature Prioritization and Product Requirements",
    "Merchant Onboarding and Implementation"
  ],
  "rules": [
    {
      "rule": "Customer Success (specifically Azmat Aziz) must be notified when contracts are processed",
      "context": "Notification occurs in Messari internal merchant channel during Active merchant phase",
      "type": "communication_protocol"
    },
    {
      "rule": "Merchant relationship information must include temperament assessment, key POC identification, and feature preferences",
      "context": "Standard information gathering during merchant onboarding",
      "type": "relationship_documentation"
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information and feature requests",
      "context": "Role-based responsibility assignment",
      "type": "team_responsibility"
    },
    {
      "rule": "AE Implementation Success team must document and provide Rewatch/Gong call recordings",
      "context": "Call documentation requirement",
      "type": "documentation_requirement"
    },
    {
      "rule": "Operations International Team should ignore Notes Sections marked for AE Implementation",
      "context": "Role-based access and responsibility segregation",
      "type": "team_responsibility"
    }
  ],
  "exceptions": [
    {
      "exception": "Small operators may use simplified billing systems (Stripe and QBO)",
      "condition": "Merchant is classified as 'very small operator'",
      "impact": "May require different onboarding or support approach"
    },
    {
      "exception": "CEO may handle financial operations directly",
      "condition": "When merchant lacks dedicated finance personnel",
      "impact": "POC and decision-maker are the same person"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient (Azmat Aziz)",
      "customization_type": "Personnel assignment varies by merchant or account"
    },
    {
      "element": "Billing system configuration (Stripe and QBO)",
      "customization_type": "Technology stack varies by merchant size and preferences"
    },
    {
      "element": "Key POC identification",
      "customization_type": "Decision-maker role varies by merchant organizational structure"
    },
    {
      "element": "Feature priorities (Reporting and Stripe pass-through)",
      "customization_type": "Feature preferences vary by merchant needs and use case"
    },
    {
      "element": "Merchant temperament assessment (collaborative, nice, easy going)",
      "customization_type": "Relationship management approach tailored to merchant personality"
    },
    {
      "element": "Internal communication channel (Messari internal merchant channel)",
      "customization_type": "May vary by merchant or account team structure"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Eino Merchant Info Sheet(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:42

### Original Content
```
Merchant Demo date: Apr 2, 2025 Scoping start date: n a MSA Signature Date: Apr 16, 2025 Onboarding Kick Off Date: n a [If Exists] Opt Out Date: none Go Live Date: n a GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Payman Samadihttps: www linkedin com in payman-samadi  Company summary (AE to fill) Summary of what company does: Eino is an AI-powered connectivity planning platform that holistically designs and simulates solution architecture for public and private W...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline Management",
    "Contract Processing and Billing Configuration",
    "Default Operational Parameters",
    "Tax and Integration Item Handling",
    "Merchant Business Context and Pain Points"
  ],
  "rules": [
    {
      "category": "Default Service Terms",
      "rule": "If no service term is listed in contract, operations default is 1 Year",
      "explicit": true
    },
    {
      "category": "Default Payment Terms",
      "rule": "If no payment terms specified, operations default is Net 0 (immediate payment)",
      "explicit": true
    },
    {
      "category": "Default Billing Frequency",
      "rule": "If no billing frequency listed, operations default is Monthly",
      "explicit": true
    },
    {
      "category": "Tax Line Items",
      "rule": "If no specific instruction provided, every tax line item becomes a BT (Billable Transaction/Item)",
      "explicit": true
    },
    {
      "category": "Billing Model",
      "rule": "Merchant bills using flat recurring SaaS fees and one-off charges",
      "explicit": true
    },
    {
      "category": "Contract Usage",
      "rule": "Merchant is transitioning from email-based agreements to formal contracts, particularly for tabs",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "condition": "Contract-specific processing variations",
      "description": "Processing instructions may differ by individual contract (e.g., back-dating invoice dates to final day of month)",
      "applies_to": "Contract Processing Steps"
    },
    {
      "condition": "Integration item labeling",
      "description": "Integration items may require specific labels based on merchant or product type (examples given: Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "applies_to": "Integration Items Processing"
    },
    {
      "condition": "Items to ignore in contracts",
      "description": "Some contract elements may need to be excluded from processing (specific items not defined in this document)",
      "applies_to": "Contract Processing Steps"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "Eino - AI-powered connectivity planning platform for WiFi/Cellular network design and simulation",
      "customization_needed": false
    },
    {
      "element": "Merchant Pain Points",
      "details": "Lacks non-GAAP metrics and wants to reduce Stripe payment processing fees",
      "customization_needed": true
    },
    {
      "element": "CEO Contact",
      "details": "Payman Samadi with LinkedIn profile reference",
      "customization_needed": true
    },
    {
      "element": "Timeline Dates",
      "details": "Demo date: Apr 2, 2025; MSA Signature: Apr 16, 2025; Other dates marked as 'n/a' or 'none'",
      "customization_needed": true
    },
    {
      "element": "GTM and Implementation POCs",
      "details": "Fields exist but not populated in this document",
      "customization_needed": true
    },
    {
      "element": "ERP and Tax Integration",
      "details": "Fields exist but not populated in this document",
      "customization_needed": true
    },
    {
      "element": "Post-Processing Communications",
      "details": "May require notification to specific team members after batch processing completion",
      "customization_needed": true
    },
    {
      "element": "Events Billing",
      "details": "Section exists but no specific instructions provided for this merchant",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

