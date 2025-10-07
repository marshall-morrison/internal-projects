# Raw LLM Analysis: Merchant Info Sheet - Hylaine(1)

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 12:22:02

---

## Chunk 1: Merchant Info Sheet - Hylaine(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:22:02

### Original Content
```
Each of these roles should be its own usage BT Net Payment terms are always found in original MSA for all SOW contracts PLease reference MSA for that customer if net payment terms are not found in SOW Sometimes the role title will be listed in a table (as in the image below in bullet  i ) Sometimes they will be bulleted in the  Investment  section (image below) Sometimes it is found in the body of the statement of work in the  Description of Services  section (image below) If there are multiple ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Terms (BT) Creation and Configuration",
    "Revenue Schedule Setup and Date Management",
    "Role-Based Usage Billing Structure",
    "Contract Document Analysis and Data Extraction",
    "Time and Materials Special Handling"
  ],
  "rules": [
    "Each unique role should have its own usage-based Billing Term (BT)",
    "Net payment terms are always found in the original MSA for SOW contracts",
    "Reference MSA for payment terms if not found in SOW",
    "Multiple consultants of the same role should be processed as only 1 BT",
    "BT Detail revenue schedule start date should be taken from email body",
    "Billing Type should be set to 'Unit price' (merchant uses almost 100% usage-based billing)",
    "Integration item should be set to 'Hours'",
    "BT start date should always be the 1st of the month, regardless of actual contract start date",
    "BTs should be recurring monthly by default",
    "Number of periods should be increased by 1 beyond contract months to account for final month billing",
    "Frequency should be 'Monthly' unless otherwise specified",
    "Event type should match the role name listed in the contract",
    "If event type doesn't exist, create new event type in Garage",
    "Merchant name should be 'Hylaine'",
    "Do not include 'Hazard Fees' or 'additional hours' as separate BTs",
    "Amendments or change requests may add new resources or adjust contract dates"
  ],
  "exceptions": [
    "Time and Materials contracts should use weekly frequency (not monthly)",
    "Time and Materials should start on the Monday before the Start date",
    "Time and Materials should use 'Time and Materials' as both BT name and Event type",
    "Roles can be listed in different locations: tables, bulleted in Investment section, or in Description of Services section body",
    "Some rates may be hourly or daily instead of monthly (enter the value regardless of type)",
    "If SOW lacks payment terms, must reference the MSA for that customer"
  ],
  "merchant_specific": [
    "Merchant name: 'Hylaine'",
    "Almost 100% usage-based billing model",
    "Specific document structure: MSA and SOW contracts",
    "Role titles may appear in multiple formats/locations within contracts",
    "Uses Garage system for event type creation",
    "Email body contains start date information",
    "Specific exclusions: 'Hazard Fees' and 'additional hours'",
    "Amendment/change request workflow for resource additions and date adjustments"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Hylaine(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:22:04

### Original Content
```
Merchant Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Feb 7, 2024 [If Exists] Opt Out Date: Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary Technology consulting company offering a sweet of services Goals (North star) What is the merchant's goal What pain are we solving Why ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing lifecycle management",
    "Time-based consultant billing with flexible rate structures",
    "Usage data processing and template customization",
    "Merchant onboarding and implementation tracking",
    "Contract ingestion and processing workflows"
  ],
  "rules": [
    "Contracts must be sent to contract-ingest with key information in the email body",
    "Contract start date must be provided by merchant in email body (no estimation rule applies)",
    "Usage-based billing is the primary billing model for this merchant",
    "Billing is based on actual time worked, not flat rates in contracts",
    "Contracts serve as rate cards and estimates, not final cost determinators",
    "Focus on billable consulting resources during processing, not milestones (with few exceptions)",
    "Class information is not included in contracts and must be obtained separately",
    "T&M contracts: Bill every 7 days, starting on the Monday before start date, bill at end of period",
    "Non-T&M contracts: Bill monthly at end of period",
    "Customers should be generated as needed with no unique creation process",
    "Hours are tracked for billing purposes despite set contract rates",
    "Contracts list consultant titles along with milestones and/or deliverables"
  ],
  "exceptions": [
    "Milestones are generally not used for processing, but there are a few exceptional cases where they matter",
    "Opt-out clause exists with deadline of October 30, 2024 - merchant needs specific conditions met to avoid exercising it",
    "Billing varies from contract rates due to schedule changes (varying start/end dates, vacation days, other schedule modifications)",
    "T&M contracts have different billing frequency (weekly) compared to other contract types (monthly)",
    "T&M contract billing starts on the Monday before the actual start date (not the exact start date)"
  ],
  "merchant_specific": [
    "Merchant is a technology consulting company offering suite of services",
    "Primary goal: Streamline consultant usage data into clean, easy-to-use billing process",
    "Custom usage template is being updated specifically for this merchant's use case",
    "Consultant deliverables have set rates but billing is time-based",
    "Specific date milestones: Demo (unspecified), Scoping (Nov 6, 2023), MSA Signature (Feb 7, 2024), Onboarding Kick Off (Feb 7, 2024), Go Live (Feb 7, 2024), Opt Out (Oct 30, 2024)",
    "Key stakeholder roles tracked: GTM POC, Implementation POC, Accountant, CFO, Customer service rep, Account Receivable POC, Billing POC",
    "ERP and Tax Integration systems (to be specified)",
    "Hourly rate billing settings configuration",
    "Contract structure focuses on consultant titles with associated milestones/deliverables"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Hylaine(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:22:15

### Original Content
```
There is one other one-off use case for Hylaine that is milestone based billing, and this will not be usage If milestone based, each milestone will be outlined with a cost and expected completion date Each milestone should be its own BT, non-recurring Invoice date should be the milestone completion date BT name is Milestone name Example of this is below: Sub-customers They might have many projects running for a customer at a time They create each project as a sub-customer This will be identified...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Milestone-based billing and project structures",
    "Sub-customer management and naming conventions",
    "Purchase order processing and contract reconciliation",
    "Customer-specific billing configurations and role mappings",
    "Default billing parameters and operational standards"
  ],
  "rules": [
    "Milestone-based billing: Each milestone must be its own BT (Billing Term), non-recurring",
    "Milestone invoice date should match the milestone completion date",
    "BT name should be the milestone name for milestone-based projects",
    "Sub-customer naming: Extract name from document title after the colon (:)",
    "Before creating new sub-customer, search for existing sub-customer with same name as SOW",
    "For purchase orders: Check if contract already exists with same customer and dates before processing",
    "If contract exists for PO, add PO number to all invoices for that contract",
    "Amwins customers: All roles should be 'Software Development Consultant' linked to that event type",
    "First Citizens Bank: PM Services should use 'Project Manager' as BT title and Event Type",
    "Ignore project details, milestones, and deliverables in contracts unless costs are tied to milestones",
    "Default Service Term Start Date: 45 days after effective date (if no email body info available)",
    "Email body information supersedes default start date calculations",
    "Default Net Payment Terms: 30 days if none specified",
    "Default Billing Frequency: Monthly if none listed"
  ],
  "exceptions": [
    "Hylaine has one-off milestone-based billing use case that differs from standard usage billing",
    "If sub-customer mapping is not obvious, do not create new customer - contact ask team first",
    "Customer-specific rules override standard rules (Amwins and First Citizens Bank examples)",
    "Milestone-based projects are exception where project details ARE important for billing",
    "Email body information takes precedence over default service term start date calculation"
  ],
  "merchant_specific": [
    "Merchant name: Hylaine",
    "Sub-customer structure used for multiple concurrent projects",
    "Document title format uses colon (:) separator for sub-customer identification",
    "BT (Billing Term) terminology specific to this merchant's system",
    "SOW (Statement of Work) document naming convention",
    "Event Type field used for role mapping",
    "Specific customer configurations: Amwins (Software Development Consultant role), First Citizens Bank (Project Manager for PM Services)",
    "PO (Purchase Order) reconciliation process with existing contracts",
    "Ops Default values: 30 days payment terms, Monthly billing frequency"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Hylaine(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:22:17

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) Yes, outlined above Integration Items Processing (if necessary) What are the instructions for assigning integration items Use  Hours  for all usage based Use  Fixed price milestone  for the milestone contracts USe  Time and Materials  for Time and Materials Post Processing Communications (if necessary) Does the Ops Team need to notify anyone on the team re: completion of processing batches in Impleme...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and billing line item processing",
    "Integration item assignment and categorization",
    "Post-processing communication protocols",
    "Merchant relationship management and documentation",
    "Implementation workflow and feature requests"
  ],
  "rules": [
    {
      "rule": "Default tax line item handling: Every tax line item becomes a BT (Billable Transaction) Events Processing when none are specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Usage-based items must be assigned using 'Hours' designation",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Milestone contracts must use 'Fixed price milestone' assignment",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Time and Materials contracts must use 'Time and Materials' assignment",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Ops Team does not need to notify team members upon completion of processing batches in Implementation or Active phase",
      "category": "Communications",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Implementation Notes sections",
      "category": "Team Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Tax line item default only applies 'If None Listed'",
      "condition": "When no specific tax instructions are provided"
    },
    {
      "exception": "Processing communication requirements are conditional on necessity",
      "condition": "Marked as '(if necessary)' for both Events Processing and Integration Items Processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Information section",
      "description": "Placeholder for merchant-specific customer details (currently 'None')",
      "customizable": true
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific request to split single BT into separate line items for multiple people in same role",
      "customizable": true
    },
    {
      "element": "Merchant temperament documentation",
      "description": "Requires capturing merchant's behavioral characteristics",
      "customizable": true
    },
    {
      "element": "Key POC (Point of Contact) identification",
      "description": "Requires identifying buyer/decision maker for each merchant",
      "customizable": true
    },
    {
      "element": "Tabs features preferences",
      "description": "Requires documenting which product features the key POC values",
      "customizable": true
    },
    {
      "element": "Billing spreadsheets",
      "description": "Merchant-specific billing documentation",
      "customizable": true
    },
    {
      "element": "Rewatch calls by dates and AE",
      "description": "Merchant-specific call recordings organized by date and account executive",
      "customizable": true
    }
  ],
  "confidence_score": 0.82
}
```

---

