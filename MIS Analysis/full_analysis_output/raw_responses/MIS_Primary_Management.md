# Raw LLM Analysis: MIS - Primary Management

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:54:22

---

## Chunk 1: MIS - Primary Management_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:54:22

### Original Content
```
Merchant Demo date: August Scoping start date: N A MSA Signature Date: Sep 30, 2024 Onboarding Kick Off Date: Oct 2, 2024 [If Exists] Opt Out Date: N A Go Live Date: GTM POC:   Daniel Implementation POC: ERP: Tax Integration: (pretty sure) Key people at Merchant CFO: Mike Witkowski Operations: Bridget Flaherty Accounting team (outsourced): Standish Company summary (AE to fill) Primary Venture Partners is a venture capital firm with two different entities: Primary Labs (an entity that houses all ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "Organizational Structure and Stakeholder Management",
    "Billing and Invoicing Operations",
    "Contract Processing and Service Documentation",
    "Automation Goals and Current State Assessment"
  ],
  "rules": [
    {
      "rule": "Service Start Date must be located from the 'Start Date' field in the Scope of Work document",
      "category": "Contract Processing"
    },
    {
      "rule": "Contract duration (Months of Service) is determined by calculating the period between start and end dates",
      "category": "Contract Processing"
    },
    {
      "rule": "Item Name should reference the project type or service title from the contract",
      "category": "Contract Processing"
    },
    {
      "rule": "Item Description field should be left blank during processing",
      "category": "Contract Processing"
    },
    {
      "rule": "Integration Item field should be left blank during processing",
      "category": "Contract Processing"
    },
    {
      "rule": "Billing Type should be set to 'Flat'",
      "category": "Contract Processing"
    },
    {
      "rule": "Total Price must be identified from the total contract value",
      "category": "Contract Processing"
    },
    {
      "rule": "Quantity should reference service units, hours, or specific resource allocations when available",
      "category": "Contract Processing"
    },
    {
      "rule": "Monthly invoicing cadence is standard for this merchant",
      "category": "Billing Model"
    },
    {
      "rule": "Primary Labs entity should be onboarded first before adding additional entities",
      "category": "Implementation Sequence"
    }
  ],
  "exceptions": [
    {
      "exception": "Two separate entities exist (Primary Labs and Primary management company) that require different handling",
      "condition": "Primary Labs handles incubation work and charges portcos for payroll expenses; Management company handles platform support services"
    },
    {
      "exception": "Primary Labs invoicing includes one-off services beyond standard payroll expenses",
      "condition": "For companies that haven't yet incorporated"
    },
    {
      "exception": "Management company entity will be added later",
      "condition": "After Primary Labs is successfully implemented and 'when they are ready'"
    },
    {
      "exception": "Dunning and collections currently handled by external accounting firm (Standish)",
      "condition": "This represents outsourced functionality that may need special integration or transition planning"
    }
  ],
  "merchant_specific": [
    {
      "element": "Entity Names",
      "details": "Primary Labs and Primary management company - dual entity structure"
    },
    {
      "element": "Key Stakeholders",
      "details": "CFO: Mike Witkowski, Operations: Bridget Flaherty, Accounting: Standish Company (outsourced)"
    },
    {
      "element": "Invoice Volume",
      "details": "Approximately 50 invoices per month"
    },
    {
      "element": "Service Types",
      "details": "Executive recruiting fees, Design and Engineering Services, OIR (Operator In Residences) Salary, Contract"
    },
    {
      "element": "Customer Base",
      "details": "Portfolio companies and incubated companies (portcos)"
    },
    {
      "element": "Current Process Owners",
      "details": "Bridget handles contracts and automated invoicing; Standish handles dunning and collections"
    },
    {
      "element": "ERP System",
      "details": "Not specified in document"
    },
    {
      "element": "Tax Integration",
      "details": "Noted as '(pretty sure)' - requires confirmation"
    },
    {
      "element": "Implementation Timeline",
      "details": "Demo: August, MSA: Sep 30 2024, Kickoff: Oct 2 2024, Go Live: TBD"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS - Primary Management_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:54:22

### Original Content
```
Start Date: Confirm the official commencement date as outlined in the document Periods: Verify whether the contract is a fixed-term agreement or if it includes renewal options Frequency: Identify the invoicing schedule (e g , monthly payments) Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Terms and Dates Management",
    "Default Values and Operational Standards",
    "Integration and Item Processing Rules",
    "Communication and Notification Protocols",
    "Customer-Specific Customizations and Special Handling"
  ],
  "rules": [
    {
      "category": "Contract Verification",
      "rule": "Confirm official commencement date (Start Date) from contract document",
      "explicit": true
    },
    {
      "category": "Contract Verification",
      "rule": "Verify if contract is fixed-term or includes renewal options",
      "explicit": true
    },
    {
      "category": "Contract Verification",
      "rule": "Identify invoicing schedule frequency (e.g., monthly payments)",
      "explicit": true
    },
    {
      "category": "Default Values",
      "rule": "Default Service Term: 1 Year (if none listed)",
      "explicit": true
    },
    {
      "category": "Default Values",
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "explicit": true
    },
    {
      "category": "Default Values",
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "explicit": true
    },
    {
      "category": "Tax Processing",
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Tax) Events Processing",
      "explicit": true
    },
    {
      "category": "Integration Items",
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "explicit": true
    },
    {
      "category": "Integration Items",
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "explicit": true
    },
    {
      "category": "Roles and Responsibilities",
      "rule": "Bridget handles contract management and tracks design/engineering service hours for invoicing",
      "explicit": true
    },
    {
      "category": "Roles and Responsibilities",
      "rule": "Standish (Accounting team) handles QBO, collections, dunning, and cash applications",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "condition": "Merchant-specific processing requests",
      "exception": "May differ by contract (e.g., always back-date invoice date to final day of the month)",
      "applies_to": "Invoice date processing"
    },
    {
      "condition": "Pinata integration items",
      "exception": "Can be labeled differently if otherwise noted by Merchant",
      "applies_to": "Integration item labeling"
    },
    {
      "condition": "Special customer relationships",
      "exception": "Invoice changes may be required due to merchant-customer relationship",
      "applies_to": "Customer-specific invoicing"
    },
    {
      "condition": "Certain invoices",
      "exception": "May require special memos",
      "applies_to": "Invoice documentation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating rules",
      "customizable": true,
      "note": "Example given: back-date to final day of month"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "note": "Specific labels for Statsig and Pinata integrations; implies other merchants may have different integration labeling rules"
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "note": "Who to notify, where, and when varies by merchant (example: Customer Success Azmat Aziz via Messari internal merchant channel)"
    },
    {
      "element": "Customer-specific information",
      "customizable": true,
      "note": "Special memos and invoice changes based on merchant-customer relationships"
    },
    {
      "element": "Events billing processing",
      "customizable": true,
      "note": "Marked as 'if necessary' - Implementation Success to fill"
    },
    {
      "element": "Feature requests tracking",
      "customizable": true,
      "note": "Includes what, why, importance, and urgency - varies by merchant"
    },
    {
      "element": "Primary team roles",
      "customizable": true,
      "note": "Specific team members (Bridget, Standish) with defined responsibilities - may vary by merchant"
    }
  ],
  "confidence_score": 0.85
}
```

---

