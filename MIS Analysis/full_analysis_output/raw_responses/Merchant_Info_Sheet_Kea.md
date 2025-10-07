# Raw LLM Analysis: Merchant Info Sheet - Kea

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 12:11:35

---

## Chunk 1: Merchant Info Sheet - Kea_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:11:35

### Original Content
```
Kea Scoping start date: Nov 6, 2023 Implementation Completed Date (Go live date): Feb 7, 2024 MSA Signature Date: Feb 9, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Head of Finance: Jessica Meksavan  jessica kea cloud  Actually works at Kea, is the primary decision maker Outsourced Accountant: Quincy Zhu  qzhu kranz consulting  Day day in the weeds Company summary Kea uses ai voice technology to receive and process orders on behalf of restaurants AM Notes n a Billing model Events ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Key Dates",
    "Stakeholder Management and Key Contacts",
    "Revenue-Based Billing Model",
    "Custom Contract Processing Workflow",
    "Events-Based Data Processing"
  ],
  "rules": [
    {
      "rule": "Billing is events-based, calculated as a percentage of GMV (Gross Merchandise Value) facilitated per store and/or a straight per-store fee",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Monthly GMV data must be sent by Kea to Tabs for processing",
      "category": "data_submission",
      "explicit": true
    },
    {
      "rule": "Tabs cross-references GMV data with each contract to compute billing appropriately",
      "category": "billing_calculation",
      "explicit": true
    },
    {
      "rule": "Contract processing requires events-based handling (non-standard approach)",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Primary decision maker must be identified for merchant relationship",
      "category": "stakeholder_management",
      "implicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Incredibly unique contract processing workflow - described as non-standard",
      "context": "Unlike typical contracts, requires special events-based processing"
    },
    {
      "exception": "Suggestion to create a Loom video for documentation due to complexity",
      "context": "Indicates process is sufficiently unique to warrant special training materials"
    },
    {
      "exception": "Head of Finance works at client company (Kea) rather than being an external contact",
      "context": "Jessica Meksavan is internal to Kea, while accounting is outsourced to Quincy Zhu at Kranz Consulting"
    }
  ],
  "merchant_specific": [
    {
      "element": "GMV-based billing structure",
      "customization_needed": "Percentage of GMV and/or per-store fee amounts need to be configured per merchant"
    },
    {
      "element": "Events-based processing workflow",
      "customization_needed": "Custom logic required to handle Kea's specific event data and GMV calculations"
    },
    {
      "element": "Monthly data submission format",
      "customization_needed": "GMV data format and submission process specific to Kea's systems"
    },
    {
      "element": "Contract cross-referencing logic",
      "customization_needed": "Each contract may have different terms requiring individual calculation rules"
    },
    {
      "element": "Stakeholder structure",
      "customization_needed": "Mix of internal decision maker and outsourced accounting requires custom communication workflow"
    },
    {
      "element": "Business model terminology",
      "customization_needed": "Kea uses AI voice technology for restaurant orders - understanding of their business model needed for proper billing"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document provides clear information about billing model, key contacts, and processing workflow. However, confidence is reduced due to: (1) incomplete sentences and abbreviations (e.g., "Takes a _ of GMV"), (2) several "n/a" fields suggesting incomplete documentation, (3) informal note-taking style that may lack precision, and (4) references to context not included in this chunk (e.g., "Garage Events Processing").

---

