# Raw LLM Analysis: Snapdocs MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:30:05

---

## Chunk 1: Snapdocs MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:05

### Original Content
```
Jason anderson, head of finance in colorado, likely won t come to calls but he was EB Very bro-ey, very nice and also sharp Loves tabs, really likes Ali 3) What are the Tabs features that the key POC cares about Statements (roadmap) Automated contract ingest - especially the accuracy Manually change invoices Rev Rec Commitment tracking Custom Reporting Cash application and their team in the philippines having access
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder relationship management and communication preferences",
    "Product feature prioritization and requirements",
    "Financial operations automation and accuracy",
    "Team collaboration and access management",
    "Revenue recognition and contract management"
  ],
  "rules": [
    {
      "rule": "Jason Anderson (Head of Finance, Colorado) has low meeting attendance expectations",
      "type": "communication_protocol",
      "specificity": "explicit"
    },
    {
      "rule": "Automated contract ingest must prioritize accuracy as a key requirement",
      "type": "feature_requirement",
      "specificity": "explicit"
    },
    {
      "rule": "Philippines-based team requires access to cash application functionality",
      "type": "access_requirement",
      "specificity": "explicit"
    },
    {
      "rule": "Manual invoice modification capability must be available",
      "type": "feature_requirement",
      "specificity": "explicit"
    },
    {
      "rule": "Statements feature is on roadmap and is a priority for key stakeholder",
      "type": "feature_requirement",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Jason Anderson may not attend calls despite being head of finance",
      "context": "Communication expectations differ from typical executive engagement patterns"
    },
    {
      "exception": "Manual invoice changes needed despite automation focus",
      "context": "Suggests automated processes require human override capability"
    }
  ],
  "merchant_specific": [
    {
      "element": "Jason Anderson - Head of Finance in Colorado",
      "category": "stakeholder",
      "customization_needed": "Contact preferences and relationship management approach"
    },
    {
      "element": "Philippines-based team for cash application",
      "category": "organizational_structure",
      "customization_needed": "Geographic access requirements and team configuration"
    },
    {
      "element": "Relationship with 'Ali' and preference for 'Tabs' product",
      "category": "relationship_dynamics",
      "customization_needed": "Account management assignment and product positioning"
    },
    {
      "element": "Custom reporting requirements",
      "category": "feature_configuration",
      "customization_needed": "Reporting templates and data structure"
    },
    {
      "element": "Revenue recognition (Rev Rec) and commitment tracking needs",
      "category": "financial_processes",
      "customization_needed": "Accounting methodology and compliance requirements"
    }
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Snapdocs MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:20

### Original Content
```
Tab 1 Snapdocs Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Products will be in the Digital Closing Services   Fees and Implementation tables Digital Cl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Setup and Billing Term Configuration",
    "Product Mapping and Event Integration",
    "Usage-Based Billing and Prepaid Models",
    "Timeline Management and Service Periods",
    "Merchant-Specific Billing Requirements and Stakeholder Management"
  ],
  "rules": [
    {
      "rule": "General Products must be in the Digital Closing Services section",
      "category": "Product Organization"
    },
    {
      "rule": "Digital Closing Services with '(per closing)' price should be Usage BTs",
      "category": "Billing Term Classification"
    },
    {
      "rule": "Implementation fees must be one-time, flat BTs",
      "category": "Billing Term Classification"
    },
    {
      "rule": "Usage AI must be turned on if contract contains: Prepaid anticipated usage amount, Committed usage amount, or Rollover credit",
      "category": "System Configuration"
    },
    {
      "rule": "Event and integration items must be selected using Product Mapping Sheet (Column B for event name, Column F for integration item)",
      "category": "Product Mapping"
    },
    {
      "rule": "Item Name should be listed in the Service column; do NOT include any description in Item Description field",
      "category": "Data Entry"
    },
    {
      "rule": "Price should use only the dollar amount from Fee Column",
      "category": "Data Entry"
    },
    {
      "rule": "Frequency for usage products is typically 'monthly in arrears'; one-time payments can be NONE",
      "category": "Billing Frequency"
    },
    {
      "rule": "Billing Start Date and Service Start Date should match, typically from 'Order Effective Date' or 'date of last signature'",
      "category": "Timeline Management"
    },
    {
      "rule": "When same product has multiple prices or years, create separate BTs for each year/price combination",
      "category": "Multi-Year Contracts"
    },
    {
      "rule": "Each year of a multi-year product should have 12 months of service starting on respective year anniversary",
      "category": "Multi-Year Contracts"
    },
    {
      "rule": "Months of Service should be listed from 'Order Term' in top right corner",
      "category": "Timeline Management"
    },
    {
      "rule": "If contract term doesn't go through today's date, extend or duplicate BTs so that it does",
      "category": "Timeline Management"
    },
    {
      "rule": "Implementation duration should be specified length if listed (e.g., '60 days'), otherwise assume 2 months",
      "category": "Implementation"
    },
    {
      "rule": "Other one-time fees (non-implementation) should use 0 months of service",
      "category": "One-Time Fees"
    },
    {
      "rule": "Net Terms should be listed from 'Payment Terms' in top right corner",
      "category": "Payment Terms"
    },
    {
      "rule": "For Prepaid/Anticipated Usage: create Flat BT with 'Has Threshold', include all usage products, set billing period for threshold period, set threshold amount as monthly prepaid amount, enable 'charges overages'",
      "category": "Prepaid Usage"
    },
    {
      "rule": "Prepaid service period should cover entire range of prepaid amounts (may be shorter than full contract term)",
      "category": "Prepaid Usage"
    },
    {
      "rule": "Rollover credits follow same setup as prepaid instructions",
      "category": "Rollover Credits"
    },
    {
      "rule": "Amendment BTs must match original contract invoice timing and end at same time as original contract",
      "category": "Amendments"
    },
    {
      "rule": "Amendment BTs should be monthly in arrears starting on date that aligns with original invoices, with same net terms",
      "category": "Amendments"
    },
    {
      "rule": "Closing Commitments should be ignored for now",
      "category": "Special Products"
    },
    {
      "rule": "For 'Closing Quality Control (CQC) Add-on' item, Event and integration item should be 'Funding Quality Control'",
      "category": "Product Mapping"
    },
    {
      "rule": "Statements feature: Break out every billing term into its own invoice on a statement for payment application at BT level",
      "category": "Invoicing"
    }
  ],
  "exceptions": [
    {
      "exception": "If specified end date exists, calculate months between start and end (round up if not exact)",
      "condition": "When end date is explicitly provided"
    },
    {
      "exception": "Only create separate BTs for different years/prices if contract explicitly breaks out separate years",
      "condition": "Multi-year pricing variations"
    },
    {
      "exception": "If unsure how to set up Usage AI for unique model, flag for review",
      "condition": "Non-standard usage billing models"
    },
    {
      "exception": "Rollover credit frequency can be undefined ('will be applied toward any Fees due') or monthly",
      "condition": "Rollover credit terms vary by contract"
    },
    {
      "exception": "For rollover credits with no defined term, select full service term for threshold period; if monthly, select individual billing period",
      "condition": "Rollover credit application timing"
    },
    {
      "exception": "Amendments often won't have end dates because end date is the original contract end date",
      "condition": "Processing amendments"
    },
    {
      "exception": "Multiple years with prepaid amounts and different usage products require manual service period setting and product selection per year",
      "condition": "Complex multi-year prepaid structures"
    }
  ],
  "merchant_specific": [
    {
      "element": "CX POC and IM POC fields",
      "description": "Merchant-specific point of contact information to be filled by implementation team"
    },
    {
      "element": "Billing model section",
      "description": "Unique customer creation process and billing structure varies by merchant"
    },
    {
      "element": "Contract structure",
      "description": "How contract is broken up and one-off merchant-specific details"
    },
    {
      "element": "Post Processing Communications",
      "description": "Merchant-specific notification requirements (who needs to be notified, when, and where)"
    },
    {
      "element": "Customer Information section",
      "description": "Important information on specific customers of the merchant, special memos, invoice changes due to merchant-customer relationships"
    },
    {
      "element": "Integration Items Processing",
      "description": "Merchant-specific instructions for assigning integration items (e.g., Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')"
    },
    {
      "element": "Merchant temperament and stakeholder profiles",
      "description": "Specific personalities and preferences of merchant contacts (e.g., Paul Micheli, Lissa Frease, David Shin for Snapdocs)"
    },
    {
      "element": "Revenue streams",
      "description": "Merchant-specific revenue models (e.g., Snapdocs has Digital, Scheduling Signing, and First Class streams)"
    },
    {
      "element": "Feature Requests section",
      "description": "Merchant-specific feature needs tracked through implementation phases"
    },
    {
      "element": "Product naming conventions",
      "description": "Use judgment to differentiate names for split line items (e.g., 'Volume Tiers (Snapdocs Originated)' vs 'Volume Tiers (Non-Snapdocs Originated)')"
    }
  ],
  "confidence_score": 0.92
}
```

---

