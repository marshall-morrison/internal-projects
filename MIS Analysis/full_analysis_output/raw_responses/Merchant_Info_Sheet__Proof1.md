# Raw LLM Analysis: Merchant Info Sheet_ Proof(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:46:08

---

## Chunk 1: Merchant Info Sheet_ Proof(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:46:08

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
    "Client synchronization and alignment meetings",
    "Demonstration sessions with stakeholders",
    "Collaboration with outsourced/third-party service providers"
  ],
  "rules": [
    "Meeting recordings are stored and referenced via rewatch.com platform",
    "Video URLs follow a specific format pattern: rewatch.com/video/[video-id]-[participants]-[topic]-[date]",
    "Meeting titles include date stamps in M/D/YY format",
    "Meeting recordings include participant names in the URL structure",
    "Sequential meetings are documented chronologically (April 5, 8, and 11, 2024)",
    "Different meeting types are distinguished: scoping calls, sync meetings, and demos"
  ],
  "exceptions": [
    "Demo meetings may include external parties (outsourced accountants) beyond primary participants",
    "Meeting URLs may have varying levels of detail in their descriptive components",
    "Some meetings are labeled as 'Additional' suggesting follow-up or supplementary sessions"
  ],
  "merchant_specific": [
    "Participant names: Benjamin, Nicholas, Ty, Nick (may be merchant-specific team members)",
    "Use of 'tabs.rewatch.com' domain suggests specific organizational setup",
    "Reference to 'outsourced accountants' indicates specific business relationship structure",
    "Meeting topics like 'path-forward' and 'scoping call' may reflect merchant's project methodology",
    "Video ID format and structure may be organization-specific"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for Low Confidence Score:**
The content appears to be a fragment of meeting URLs/references rather than a complete instruction document. This makes it difficult to extract comprehensive, actionable rules. The analysis is based on structural patterns and naming conventions observed in the URLs, but without the actual content of these videos or surrounding context, the extracted rules are largely inferential. The document chunk seems incomplete or may be metadata rather than substantive instructional content.

---

## Chunk 2: Merchant Info Sheet_ Proof(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:46:11

### Original Content
```
Proof io Scoping start date: Apr 5, 2024 Implementation Completed Date (Go live date): Apr 15, 2024 MSA Signature Date: Apr 12, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Leadra Jarvis (leandra decimal com), Sara Builes (sara decimal com) CFO: Ty Boshyan (ty proof io) Company summary Proof is a B2B Saas platform that aims to lead the next evolution of business intelligence through verified ESG   Impact Data They believe that all future decisions, whether it be busines...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Default Terms",
    "Billing Model and Payment Processing",
    "Integration and System Setup",
    "Stakeholder Roles and Responsibilities",
    "Implementation Timeline and Milestones"
  ],
  "rules": [
    {
      "rule": "Default to 1 year contract term if not specified",
      "category": "contract_defaults",
      "explicit": true
    },
    {
      "rule": "Default to Net 30 payment terms if not specified",
      "category": "payment_terms",
      "explicit": true
    },
    {
      "rule": "Default to quarterly billing if not specified",
      "category": "billing_frequency",
      "explicit": true
    },
    {
      "rule": "Auto extend contract to 3 months past end date unless canceled",
      "category": "contract_renewal",
      "explicit": true
    },
    {
      "rule": "Link all BTs (billing terms) to Implementation - SaaS: Implementation for implementation items",
      "category": "integration_mapping",
      "explicit": true
    },
    {
      "rule": "Link all BTs to SaaS:Subscription for everything else (non-implementation)",
      "category": "integration_mapping",
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
      "rule": "If no contact emails available, add manually in Tabs",
      "category": "data_entry",
      "explicit": true
    },
    {
      "rule": "Use QBO as the general ledger system",
      "category": "system_integration",
      "explicit": true
    },
    {
      "rule": "Send invoices through Stripe",
      "category": "invoicing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "3-5 contracts out of 22 total have usage-based billing instead of standard recurring terms",
      "context": "billing_model"
    },
    {
      "exception": "Optional upgrade terms should be ignored during contract processing",
      "context": "contract_terms"
    },
    {
      "exception": "Events-based terms require escalation rather than standard processing",
      "context": "events_processing"
    },
    {
      "exception": "Special memos may be required for certain invoices due to merchant-customer relationships",
      "context": "invoice_customization"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company: Proof - B2B SaaS platform for verified ESG Impact Data",
      "type": "business_context"
    },
    {
      "element": "Key stakeholders: Ty Boshyan (CFO, primary user), Leandra Jarvis and Sara Builes (outsourced accountants)",
      "type": "personnel"
    },
    {
      "element": "Implementation dates: Scoping Apr 5, 2024; Go-live Apr 15, 2024; MSA signed Apr 12, 2024",
      "type": "timeline"
    },
    {
      "element": "22 total contracts with mixed billing models",
      "type": "contract_volume"
    },
    {
      "element": "Accountants plan to bring Tabs to 4-5 other clients post-implementation",
      "type": "expansion_plan"
    },
    {
      "element": "Current tech stack: QBO (general ledger), Stripe (invoicing and payments), Google Sheets (contract tracking)",
      "type": "systems"
    },
    {
      "element": "Escalation point: 'proof-io' for events-based terms",
      "type": "escalation_process"
    },
    {
      "element": "Integration items labeled as 'SaaS:Implementation' and 'SaaS:Subscription'",
      "type": "terminology"
    }
  ],
  "confidence_score": 0.92
}
```

---

