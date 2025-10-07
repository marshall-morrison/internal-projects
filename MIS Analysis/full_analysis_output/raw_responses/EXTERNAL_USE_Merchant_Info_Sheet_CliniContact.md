# Raw LLM Analysis: [EXTERNAL USE] Merchant Info Sheet - CliniContact

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:18:28

---

## Chunk 1: [EXTERNAL USE] Merchant Info Sheet - CliniContact_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:18:28

### Original Content
```
Example Of a Proper Customer Name  Rutgers - Dr Chen  If no institution name is included - Use Researcher s full name including title -  Dr Full Name  Example of a proper customer name with no institution:  Dr Loren Fishman  Events Processing (if necessary) Don t process usage   Flag to Ashni Customer Information n a Feature Requests n a Rewatch Calls Feb 2- https: tabs rewatch com video mhcm08aw16vp7udj-tabs-cliniccontact-demo-february-2-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer name formatting and standardization",
    "Institutional vs individual researcher identification",
    "Events processing workflow and escalation",
    "Internal communication and flagging procedures",
    "Training and reference materials"
  ],
  "rules": [
    {
      "rule": "Customer names must include institution name followed by researcher name with title",
      "example": "Rutgers - Dr Chen",
      "context": "When institution name is available"
    },
    {
      "rule": "When no institution name is available, use researcher's full name including title in format 'Dr Full Name'",
      "example": "Dr Loren Fishman",
      "context": "When institution is not provided"
    },
    {
      "rule": "Do not process usage for events",
      "context": "Events processing workflow"
    },
    {
      "rule": "Flag events-related items to Ashni",
      "context": "Events processing escalation procedure"
    },
    {
      "rule": "Professional titles (e.g., 'Dr') must be included in customer names",
      "context": "Name formatting requirement"
    }
  ],
  "exceptions": [
    {
      "condition": "No institution name is included",
      "action": "Use alternative naming format with researcher's full name and title only"
    },
    {
      "condition": "Events processing scenario",
      "action": "Do not process usage, flag to specific team member (Ashni) instead"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contact person name: Ashni",
      "type": "Personnel reference",
      "customizable": true,
      "note": "Specific team member for escalation may vary by organization"
    },
    {
      "element": "Customer types: Institutions and Researchers",
      "type": "Customer classification",
      "customizable": false,
      "note": "Appears to be industry-specific (academic/research sector)"
    },
    {
      "element": "Rewatch training video link",
      "type": "Training resource",
      "customizable": true,
      "note": "Organization-specific training materials and URLs"
    },
    {
      "element": "Events processing workflow",
      "type": "Business process",
      "customizable": true,
      "note": "May vary based on merchant's operational structure"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document chunk is somewhat fragmented and contains incomplete sentences, making some interpretations uncertain. However, the core rules about customer naming conventions are clear and explicit with examples. The events processing section is brief but actionable. The confidence score reflects clarity on main rules but uncertainty about broader context and complete workflows.

---

## Chunk 2: [EXTERNAL USE] Merchant Info Sheet - CliniContact_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:18:28

### Original Content
```
Merchant Scoping start date: Feb 7, 2024 Implementation Completed Date (Go live date): Feb 7, 2024 MSA Signature Date: Feb 7, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant- Megan (megan clinicontact com) CEO: Kit Dobyns (kit clinicontact com) Company Summary Recruit patients for clinical testing AM Notes Friends with Ali Moved to QBO to start using Tab Active Merchant Billing model Original contracts were very simple: one-page and one-time billing Often one item Recently,...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline",
    "Billing Models and Contract Types",
    "Customer Creation and Naming Conventions",
    "Contract Processing Workflow",
    "Escalation and Exception Handling"
  ],
  "rules": [
    {
      "rule": "Customer naming convention must follow format: 'Institution Name - Researcher Name'",
      "category": "customer_creation",
      "explicit": true
    },
    {
      "rule": "Check file name for existing customers before creating new customer records",
      "category": "customer_creation",
      "explicit": true
    },
    {
      "rule": "Flag to Ashni Walia if uncertain about correct customer mapping",
      "category": "escalation",
      "explicit": true
    },
    {
      "rule": "Ashni Walia escalates customer mapping issues to CX team",
      "category": "escalation",
      "explicit": true
    },
    {
      "rule": "Stop processing and reach out to CX if usage billing terms are encountered",
      "category": "billing_exception",
      "explicit": true
    },
    {
      "rule": "All billing terms to date have been flat fee (expected standard)",
      "category": "billing_model",
      "explicit": true
    },
    {
      "rule": "Institution Names include Universities, Colleges, or Large Research Organizations",
      "category": "customer_naming",
      "explicit": true
    },
    {
      "rule": "Researcher Names are individual names found on the contract",
      "category": "customer_naming",
      "explicit": true
    },
    {
      "rule": "Recurring invoices are typically on a monthly cadence",
      "category": "billing_frequency",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Usage billing terms are not standard - requires CX escalation and processing halt",
      "trigger": "Encountering usage-based billing in contract",
      "action": "Stop processing and contact CX"
    },
    {
      "exception": "Original contracts were very simple (one-page, one-time billing, single item)",
      "context": "Historical billing model differs from current recurring invoice model"
    },
    {
      "exception": "Ops team (Ashni Walia) to provide more detail from next contract ingested",
      "context": "Contract processing steps are incomplete/evolving"
    }
  ],
  "merchant_specific": [
    {
      "element": "Business Model",
      "description": "Clinicontact recruits patients for clinical testing",
      "customization_needed": true
    },
    {
      "element": "Customer Type",
      "description": "Customers are academic/research institutions with individual researchers",
      "customization_needed": true
    },
    {
      "element": "Key Contacts",
      "description": "Accountant: Megan, CEO: Kit Dobyns, Ops POC: Ashni Walia",
      "customization_needed": true
    },
    {
      "element": "ERP System",
      "description": "Moved to QuickBooks Online (QBO) to start using Tab",
      "customization_needed": true
    },
    {
      "element": "Billing Evolution",
      "description": "Transitioned from simple one-time contracts to recurring monthly invoices",
      "customization_needed": true
    },
    {
      "element": "Naming Convention Pattern",
      "description": "Institution Name - Researcher Name (specific to academic research context)",
      "customization_needed": true
    },
    {
      "element": "Implementation Dates",
      "description": "Scoping, Go-live, and MSA all on Feb 7, 2024",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

