# Raw LLM Analysis: MIS - Primary Management(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:09:25

---

## Chunk 1: MIS - Primary Management(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:25

### Original Content
```
Start Date: Confirm the official commencement date as outlined in the document Periods: Verify whether the contract is a fixed-term agreement or if it includes renewal options Frequency: Identify the invoicing schedule (e g , monthly payments) Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Terms and Dates Management",
    "Default Operational Values and Fallback Rules",
    "Integration and Labeling Instructions",
    "Communication and Notification Protocols",
    "Customer-Specific Processing Requirements"
  ],
  "rules": [
    {
      "category": "Contract Verification",
      "rule": "Must confirm official commencement date from document",
      "field": "Start Date"
    },
    {
      "category": "Contract Verification",
      "rule": "Must verify if contract is fixed-term or includes renewal options",
      "field": "Periods"
    },
    {
      "category": "Contract Verification",
      "rule": "Must identify invoicing schedule frequency",
      "field": "Frequency"
    },
    {
      "category": "Default Values",
      "rule": "If no service term listed, default is 1 Year",
      "field": "Service Term"
    },
    {
      "category": "Default Values",
      "rule": "If no payment terms listed, default is Net 0",
      "field": "Payment Terms"
    },
    {
      "category": "Default Values",
      "rule": "If no billing frequency listed, default is Monthly",
      "field": "Billing Frequency"
    },
    {
      "category": "Tax Processing",
      "rule": "If no instruction listed, every tax line item becomes a BT (Billable Transaction)",
      "field": "Tax Line Items"
    },
    {
      "category": "Integration Labeling",
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "field": "Integration Items"
    },
    {
      "category": "Integration Labeling",
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "field": "Integration Items"
    },
    {
      "category": "Team Responsibilities",
      "rule": "Bridget handles contract management and tracks design/engineering service hours for invoicing",
      "field": "Roles"
    },
    {
      "category": "Team Responsibilities",
      "rule": "Standish accounting team handles QBO, collections, dunning, and cash applications",
      "field": "Roles"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant may request contract-specific processing (e.g., always back-date invoice date to final day of month)",
      "context": "Contract-specific variations override standard processing"
    },
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "context": "Integration labeling has merchant override capability"
    },
    {
      "exception": "International team should ignore certain sections marked for AE/Implementation",
      "context": "Role-based section exclusions"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "context": "Customer-specific invoice modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating rules",
      "customizable": true,
      "note": "May differ by contract per merchant request"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "note": "Specific rules for Statsig and Pinata, implies other merchants may have different rules"
    },
    {
      "element": "Post-processing notification requirements",
      "customizable": true,
      "note": "Who, where, and when notifications occur varies by merchant (example: Azmat Aziz for Messari)"
    },
    {
      "element": "Customer information and special memos",
      "customizable": true,
      "note": "Specific to merchant-customer relationships"
    },
    {
      "element": "Events billing processing",
      "customizable": true,
      "note": "Only processed if necessary, filled by Implementation Success"
    },
    {
      "element": "Feature requests and urgency levels",
      "customizable": true,
      "note": "Merchant-specific feature needs tracked with importance and urgency"
    },
    {
      "element": "Primary team roles and responsibilities",
      "customizable": true,
      "note": "Example shows Bridget and Standish for specific merchant, implies variation across merchants"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS - Primary Management(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:25

### Original Content
```
Merchant Demo date: August Scoping start date: N A MSA Signature Date: Sep 30, 2024 Onboarding Kick Off Date: Oct 2, 2024 [If Exists] Opt Out Date: N A Go Live Date: GTM POC:   Daniel Implementation POC: ERP: Tax Integration: (pretty sure) Key people at Merchant CFO: Mike Witkowski Operations: Bridget Flaherty Accounting team (outsourced): Standish Company summary (AE to fill) Primary Venture Partners is a venture capital firm with two different entities: Primary Labs (an entity that houses all ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Timeline Management",
    "Organizational Structure and Stakeholder Identification",
    "Invoice Processing and Billing Operations",
    "Contract Management and Service Delivery",
    "Data Extraction and Invoice Generation Workflow"
  ],
  "rules": [
    {
      "rule": "Service Start Date must be located from the 'Start Date' field in the Scope of Work document",
      "category": "Contract Processing"
    },
    {
      "rule": "Months of Service must be calculated from contract start and end dates",
      "category": "Contract Processing"
    },
    {
      "rule": "Item Name should reference the project type or service title (e.g., 'Market Development')",
      "category": "Invoice Line Items"
    },
    {
      "rule": "Item Description field should be left blank",
      "category": "Invoice Line Items"
    },
    {
      "rule": "Integration Item field should be left blank",
      "category": "Invoice Line Items"
    },
    {
      "rule": "Billing Type should be set to 'Flat'",
      "category": "Billing Configuration"
    },
    {
      "rule": "Total Price must be identified from the total contract value",
      "category": "Pricing"
    },
    {
      "rule": "Quantity should reference service units, hours, or specific resource allocations",
      "category": "Invoice Line Items"
    },
    {
      "rule": "Merchant invoices on a monthly basis for portfolio companies",
      "category": "Billing Frequency"
    },
    {
      "rule": "Implementation should start with Primary Labs entity before adding other entities",
      "category": "Phased Rollout"
    }
  ],
  "exceptions": [
    {
      "exception": "Primary Venture Partners operates with two separate entities (Primary Labs and Primary management company) that require different handling",
      "condition": "Entity-specific invoicing rules apply"
    },
    {
      "exception": "Primary Labs invoices incubated companies for payroll expenses when they haven't yet incorporated, plus other one-off services",
      "condition": "Pre-incorporation status of portfolio companies"
    },
    {
      "exception": "Management company invoicing is specifically for Platform support services to portfolio companies",
      "condition": "Different service types for different entities"
    },
    {
      "exception": "Phased implementation approach - start with Primary Labs, then add management company entity when ready",
      "condition": "Entity readiness for onboarding"
    }
  ],
  "merchant_specific": [
    {
      "element": "Entity Structure",
      "details": "Two entities: Primary Labs (incubation work) and Primary management company",
      "customization_needed": true
    },
    {
      "element": "Service Types",
      "details": "Executive recruiting fees, Design and Engineering Services, OIR (Operator In Residences) Salary",
      "customization_needed": true
    },
    {
      "element": "Invoice Volume",
      "details": "Approximately 50 invoices per month",
      "customization_needed": false
    },
    {
      "element": "Key Stakeholders",
      "details": "CFO: Mike Witkowski, Operations: Bridget Flaherty, Accounting: Standish Company (outsourced)",
      "customization_needed": true
    },
    {
      "element": "Current Process Owners",
      "details": "Bridget handles contracts and automated invoicing; Standish handles dunning and collections",
      "customization_needed": true
    },
    {
      "element": "Customer Base",
      "details": "Portfolio companies and incubated companies",
      "customization_needed": true
    },
    {
      "element": "Merchant-Specific Terminology",
      "details": "OIR (Operator In Residences), portcos (portfolio companies), Platform support",
      "customization_needed": true
    },
    {
      "element": "Goals",
      "details": "Manage contracts, automated invoicing, dunning & collections, simpler reporting",
      "customization_needed": false
    }
  ],
  "confidence_score": 0.88
}
```

---

