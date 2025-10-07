# Raw LLM Analysis: Merchant Info Sheet - CliniContact

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 12:12:57

---

## Chunk 1: Merchant Info Sheet - CliniContact_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:57

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
    "Event processing workflow and escalation",
    "Internal communication and flagging procedures",
    "Reference documentation and training materials"
  ],
  "rules": [
    {
      "rule": "Customer names must include institution name when available, formatted as: 'Institution - Title Name'",
      "example": "Rutgers - Dr Chen"
    },
    {
      "rule": "When no institution name is provided, use researcher's full name including professional title",
      "example": "Dr Loren Fishman"
    },
    {
      "rule": "Professional titles (e.g., Dr) must be included in customer names",
      "example": "Dr Full Name format required"
    },
    {
      "rule": "For events processing: Do not process usage data",
      "context": "When events processing is necessary"
    },
    {
      "rule": "Issues or special cases should be flagged to 'Ashni'",
      "context": "Events processing workflow"
    }
  ],
  "exceptions": [
    {
      "condition": "If no institution name is included",
      "action": "Use researcher's full name including title instead of institution-name format"
    },
    {
      "condition": "Events processing is necessary",
      "action": "Don't process usage and flag to Ashni instead"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contact person name: 'Ashni'",
      "type": "Internal escalation contact",
      "customizable": true
    },
    {
      "element": "Customer type: Academic/Research institutions and individual researchers",
      "type": "Customer segment",
      "customizable": true
    },
    {
      "element": "Rewatch training video reference",
      "type": "Internal training resource",
      "customizable": true
    },
    {
      "element": "Usage processing workflow",
      "type": "Business process",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 2: Merchant Info Sheet - CliniContact_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:13:08

### Original Content
```
Merchant Scoping start date: Feb 7, 2024 Implementation Completed Date (Go live date): Feb 7, 2024 MSA Signature Date: Feb 7, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant- Megan (megan clinicontact com) CEO: Kit Dobyns (kit clinicontact com) Company Summary Recruit patients for clinical testing AM Notes Friends with Ali Moved to QBO to start using Tab Active Merchant Billing model Original contracts were very simple: one-page and one-time billing Often one item Recently,...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "Billing Models and Contract Types",
    "Customer Creation and Naming Conventions",
    "Contract Processing Workflow and Escalation Procedures",
    "Stakeholder Communication and Point of Contact Management"
  ],
  "rules": [
    {
      "rule": "Check file name for existing customers before creating new customer records",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Flag to Ashni Walia if uncertain about correct customer mapping",
      "category": "Escalation",
      "explicit": true
    },
    {
      "rule": "Ashni Walia must flag CX for customer creation clarifications",
      "category": "Escalation",
      "explicit": true
    },
    {
      "rule": "Customer naming convention must follow format: 'Institution Name - Researcher Name'",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Institution Names must be Universities, Colleges, or Large Research Organizations",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Researcher Names must be the individual name on the contract",
      "category": "Customer Creation",
      "explicit": true
    },
    {
      "rule": "Stop processing and reach out to CX if usage billing terms are encountered",
      "category": "Billing Processing",
      "explicit": true
    },
    {
      "rule": "All billing terms to date have been flat fee (expected standard)",
      "category": "Billing Processing",
      "explicit": true
    },
    {
      "rule": "Recurring invoices are typically on a monthly cadence",
      "category": "Billing Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Usage billing terms are not standard and require CX intervention",
      "condition": "If usage billing terms are found in contract",
      "action": "Stop processing and reach out to CX"
    },
    {
      "exception": "Original contracts were very simple (one-page, one-time billing, often one item)",
      "condition": "Historical contracts vs. recent recurring invoices",
      "action": "Indicates business model evolution"
    },
    {
      "exception": "Ops to provide more detail from next contract ingested",
      "condition": "Contract Processing Steps section is incomplete",
      "action": "Ashni Walia and Ops team to update documentation after next contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "Clinicontact",
      "type": "Company Identity"
    },
    {
      "element": "Business Model",
      "value": "Recruit patients for clinical testing",
      "type": "Company Summary"
    },
    {
      "element": "Key Contacts",
      "value": {
        "Accountant": "Megan (megan@clinicontact.com)",
        "CEO": "Kit Dobyns (kit@clinicontact.com)",
        "GTM POC": "Not specified",
        "Internal POC": "Ashni Walia"
      },
      "type": "Stakeholders"
    },
    {
      "element": "ERP System",
      "value": "QBO (QuickBooks Online)",
      "type": "Technical Integration"
    },
    {
      "element": "Implementation Dates",
      "value": {
        "Scoping Start": "Feb 7, 2024",
        "Go Live": "Feb 7, 2024",
        "MSA Signature": "Feb 7, 2024"
      },
      "type": "Timeline"
    },
    {
      "element": "Customer Types",
      "value": "Universities, Colleges, Large Research Organizations with individual researchers",
      "type": "Customer Profile"
    },
    {
      "element": "Relationship Context",
      "value": "Friends with Ali; Moved to QBO to start using Tab",
      "type": "Business Relationship"
    },
    {
      "element": "Merchant Status",
      "value": "Active Merchant",
      "type": "Account Status"
    }
  ],
  "confidence_score": 0.92
}
```

---

