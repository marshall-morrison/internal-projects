# Raw LLM Analysis: Merchant Info Sheet_ Proof

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:53:07

---

## Chunk 1: Merchant Info Sheet_ Proof_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:07

### Original Content
```
rewatch com video m4wuufwpnfdw0lkg-benjamin-nicholas-april-5-2024 4 8 24 - Scoping call https: tabs rewatch com video hkpw48ap4pdghsoy-ty-nicholas-sync-on-path-forward-april-8-2024 4 11 24 - Additional Demo with outsourced accountants https: tabs rewatch com video 7flqz6vysygcjmkw-ty-nick-april-11-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Video meeting documentation and recordings",
    "Project scoping and requirements gathering",
    "Stakeholder synchronization meetings",
    "Accountant collaboration and outsourced services",
    "Progressive demonstration and iteration process"
  ],
  "rules": [
    "Meeting recordings are stored on rewatch.com platform",
    "Video URLs follow pattern: tabs.rewatch.com/video/[unique-id]-[description]-[date]",
    "Meeting titles include participant names and dates in format M/D/YY",
    "Scoping calls are conducted before path forward synchronization",
    "Additional demonstrations are provided for outsourced accountants",
    "Meeting sequence follows: Scoping → Sync on Path Forward → Additional Demo"
  ],
  "exceptions": [
    "Outsourced accountants may require additional demonstration sessions beyond standard workflow",
    "Meeting recordings may involve different participant combinations (Benjamin-Nicholas vs Ty-Nicholas vs Ty-Nick)"
  ],
  "merchant_specific": [
    "Participant names: Benjamin, Nicholas, Ty, Nick (potentially same person as Nicholas)",
    "Specific video IDs: m4wuufwpnfdw0lkg, hkpw48ap4pdghsoy, 7flqz6vysygcjmkw",
    "Date range: April 5-11, 2024",
    "Use of 'tabs.rewatch.com' as video platform",
    "Reference to 'outsourced accountants' as stakeholder group",
    "Meeting naming conventions specific to this organization"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for Low Confidence Score:**
The content appears to be a list of video meeting URLs and titles rather than a formal instruction document. The extracted "rules" are primarily observational patterns about URL structure and meeting sequences rather than explicit business rules or merchant instructions. Without additional context about what these meetings contain or what instructions were given during them, the analysis is limited to metadata patterns. This may be a reference list or index rather than the actual instructional content.

---

## Chunk 2: Merchant Info Sheet_ Proof_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:10

### Original Content
```
Proof io Scoping start date: Apr 5, 2024 Implementation Completed Date (Go live date): Apr 15, 2024 MSA Signature Date: Apr 12, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Leadra Jarvis (leandra decimal com), Sara Builes (sara decimal com) CFO: Ty Boshyan (ty proof io) Company summary Proof is a B2B Saas platform that aims to lead the next evolution of business intelligence through verified ESG   Impact Data They believe that all future decisions, whether it be busines...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Default Terms",
    "Billing Model and Payment Infrastructure",
    "Stakeholder Roles and Responsibilities",
    "Integration and System Configuration",
    "Revenue Recognition and Accounting Practices"
  ],
  "rules": [
    {
      "rule": "Default contract term to 1 year if not specified",
      "category": "contract_defaults",
      "explicit": true
    },
    {
      "rule": "Default payment terms to Net 30 if not specified",
      "category": "contract_defaults",
      "explicit": true
    },
    {
      "rule": "Default billing frequency to quarterly if not specified",
      "category": "contract_defaults",
      "explicit": true
    },
    {
      "rule": "Auto-extend contracts to 3 months past end date unless canceled",
      "category": "contract_management",
      "explicit": true
    },
    {
      "rule": "Link all billing transactions to 2 integration items: Implementation - SaaS:Implementation and Everything else - SaaS:Subscription",
      "category": "revenue_recognition",
      "explicit": true
    },
    {
      "rule": "Ignore all optional terms like 'upgrade to Pro for x'",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Ignore any events-based terms and escalate to proof-io if needed",
      "category": "events_processing",
      "explicit": true
    },
    {
      "rule": "If no contact emails exist, add manually in Tabs",
      "category": "data_management",
      "explicit": true
    },
    {
      "rule": "Use QBO as general ledger system",
      "category": "systems",
      "explicit": true
    },
    {
      "rule": "Send invoices through Stripe",
      "category": "billing_infrastructure",
      "explicit": true
    },
    {
      "rule": "Track payments in QBO",
      "category": "payment_tracking",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "3-5 contracts out of 22 total have usage-based billing (non-standard recurring terms)",
      "context": "billing_model"
    },
    {
      "exception": "Optional upgrade terms should be ignored during contract processing",
      "context": "contract_processing"
    },
    {
      "exception": "Events-based terms require escalation rather than standard processing",
      "context": "events_processing"
    },
    {
      "exception": "Special memos or invoice changes may be required for certain customers due to merchant-customer relationships",
      "context": "customer_specific_handling"
    }
  ],
  "merchant_specific": [
    {
      "element": "Stakeholders",
      "details": "CFO Ty Boshyan is primary user; outsourced accountants Leandra Jarvis and Sara Builes handle monthly close"
    },
    {
      "element": "Business Model",
      "details": "B2B SaaS platform focused on verified ESG Impact Data and business intelligence"
    },
    {
      "element": "Contract Volume",
      "details": "22 total contracts with mixed billing models"
    },
    {
      "element": "Technology Stack",
      "details": "QBO (QuickBooks Online) for general ledger, Stripe for invoicing and payments"
    },
    {
      "element": "Revenue Categories",
      "details": "Two-category system: Implementation (SaaS:Implementation) and Subscription (SaaS:Subscription)"
    },
    {
      "element": "Expansion Opportunity",
      "details": "Accountants want to bring Tabs to 4-5 other clients post-implementation"
    },
    {
      "element": "Implementation Timeline",
      "details": "Scoping: Apr 5, 2024; Go-live: Apr 15, 2024; MSA signed: Apr 12, 2024"
    },
    {
      "element": "Custom Terminology",
      "details": "References to 'BTs' (likely Billing Transactions), 'Tabs' (the platform being implemented)"
    }
  ],
  "confidence_score": 0.85
}
```

---

