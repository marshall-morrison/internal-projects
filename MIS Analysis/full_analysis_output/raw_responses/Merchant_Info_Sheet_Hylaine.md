# Raw LLM Analysis: Merchant Info Sheet - Hylaine

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:28:29

---

## Chunk 1: Merchant Info Sheet - Hylaine_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:29

### Original Content
```
Each of these roles should be its own usage BT Net Payment terms are always found in original MSA for all SOW contracts PLease reference MSA for that customer if net payment terms are not found in SOW Sometimes the role title will be listed in a table (as in the image below in bullet  i ) Sometimes they will be bulleted in the  Investment  section (image below) Sometimes it is found in the body of the statement of work in the  Description of Services  section (image below) If there are multiple ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Terms (BT) Creation and Configuration",
    "Role-Based Usage Billing Structure",
    "Revenue Schedule and Date Management",
    "Contract Document Parsing and Data Extraction",
    "Time and Materials Special Handling"
  ],
  "rules": [
    "Each unique role should have its own usage-based Billing Term (BT)",
    "Net payment terms must be referenced from the original MSA if not found in SOW",
    "Multiple consultants with the same role title should be processed as only 1 BT",
    "Billing Type should always be 'Unit price' for this merchant",
    "Integration item should be set to 'Hours'",
    "BT start date must always be the 1st of the month, regardless of actual contract start date",
    "BTs should be set as recurring monthly by default",
    "Number of periods should be increased by 1 beyond the contract months to account for final month billing",
    "Event type should match the role name listed in the contract",
    "Frequency should be Monthly unless otherwise specified",
    "Revenue schedule start date should be taken from the email body",
    "Merchant should be set to 'Hylaine'",
    "Do not include 'Hazard Fees' or 'additional hours' as separate BTs",
    "Amendments or change requests may add new resources or adjust contract dates"
  ],
  "exceptions": [
    "Time and Materials contracts should be billed weekly (not monthly)",
    "Time and Materials BT start date should be the Monday before the actual start date",
    "Time and Materials should use a specific event type called 'Time and Materials'",
    "Time and Materials should have BT name set to 'Time and Materials'",
    "Some contracts may have hourly or daily rates instead of monthly rates",
    "If role name doesn't exist as event type, create new event type in Garage system"
  ],
  "merchant_specific": [
    "Merchant name: Hylaine",
    "This merchant uses almost 100% usage-based billing",
    "Role information can be found in three different locations: tables, bulleted in Investment section, or in Description of Services section",
    "Payment terms reference hierarchy: SOW first, then fallback to MSA",
    "Specific event type creation process references 'Garage' system/SOP",
    "Email body contains the revenue schedule start date",
    "Contract structure includes MSA and SOW documents",
    "Amendments and change requests are part of the workflow"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Hylaine_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:30

### Original Content
```
Merchant Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Feb 7, 2024 [If Exists] Opt Out Date: Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary Technology consulting company offering a sweet of services Goals (North star) What is the merchant's goal What pain are we solving Why ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing lifecycle management",
    "Time-based consulting services billing model",
    "Usage data processing and tracking",
    "Merchant onboarding and implementation timeline",
    "Contract processing workflow and automation"
  ],
  "rules": [
    "Contracts must be sent to contract-ingest with key information in the email body",
    "Contract start date must be provided by merchant in email body (no estimation rule)",
    "Billing for T&M contracts: Every 7 days, starting on the Monday before the start date, bill last of period",
    "Billing for all other contracts: Monthly, bill last of period",
    "Customers should be generated as needed (no unique creation process)",
    "Processing focuses on billable consulting resources, not milestones (with few exceptions)",
    "Consultants are billed based on actual time worked, not flat contract rates",
    "Contracts serve as rate cards and estimates, not final cost determination",
    "Hourly rates are the primary billing setting to extract",
    "Usage template must be updated to serve merchant's use case"
  ],
  "exceptions": [
    "Milestones are generally not used for processing, but there are a few exceptional cases where they matter",
    "Contract rates are set but actual billing varies due to schedule changes (varying start/end dates, vacation days, schedule changes)",
    "Class information is not included in contracts (must be obtained elsewhere)",
    "Opt-out clause exists with date of October 30, 2024, requiring specific deliverables to prevent exercise"
  ],
  "merchant_specific": [
    "Merchant is a technology consulting company offering suite of services",
    "Primary goal: Streamline consultant usage data into clean billing process",
    "ERP system (not specified in document)",
    "Tax integration details (not specified)",
    "Specific POC roles needed: GTM POC, Implementation POC, Accountant, CFO, Customer service rep, AR POC, Billing POC",
    "Contract structure: Consultant titles listed with milestones/deliverables",
    "Billing model: Time-based with contract serving as rate card",
    "Usage data is the primary billing driver for this merchant",
    "Custom usage template requirements",
    "Key dates: Demo, Scoping (Nov 6, 2023), MSA Signature (Feb 7, 2024), Go Live (Feb 7, 2024), Opt Out (Oct 30, 2024)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Hylaine_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:46

### Original Content
```
There is one other one-off use case for Hylaine that is milestone based billing, and this will not be usage If milestone based, each milestone will be outlined with a cost and expected completion date Each milestone should be its own BT, non-recurring Invoice date should be the milestone completion date BT name is Milestone name Example of this is below: Sub-customers They might have many projects running for a customer at a time They create each project as a sub-customer This will be identified...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Milestone-based billing and project structure",
    "Sub-customer management and naming conventions",
    "Purchase order processing and contract reconciliation",
    "Customer-specific billing configurations and role mappings",
    "Default billing parameters and operational standards"
  ],
  "rules": [
    "Milestone-based billing: Each milestone must be its own BT (Billing Transaction), non-recurring",
    "Milestone invoice date should match the milestone completion date",
    "BT name should be the milestone name for milestone-based projects",
    "Sub-customers should be named using the text after the colon (:) in the document title",
    "Before creating a new sub-customer, search for existing sub-customer with same name as SOW",
    "For purchase orders: Check if contract already exists with same customer and dates before processing",
    "If contract exists for PO, add PO number to all invoices for that contract",
    "Amwins customers: All roles should be 'Software Development Consultant' linked to that event type",
    "First Citizens Bank: PM Services should use 'Project Manager' as BT title and Event Type",
    "Default Service Term Start Date: 45 days after effective date (if no email body info available)",
    "Default Net Payment Terms: 30 days (if none specified)",
    "Default Billing Frequency: Monthly (if none listed)",
    "Email body information supersedes default start date rules",
    "Ignore project details, milestones, and deliverables in contracts unless costs are tied to milestones",
    "Focus only on billable consulting resources for billing purposes"
  ],
  "exceptions": [
    "Milestone-based billing for Hylaine is a one-off use case and not usage-based",
    "When mapping is not obvious for sub-customers, do NOT create new customer - contact team instead",
    "If PO has no matching contract, flag to the team instead of processing",
    "Project details in contracts should be ignored EXCEPT when costs are explicitly tied to milestones",
    "Customer-specific rules override general rules (Amwins and First Citizens Bank have special configurations)"
  ],
  "merchant_specific": [
    "Hylaine: Milestone-based billing structure with specific BT requirements",
    "Hylaine: Sub-customer project structure identified by document title format",
    "Amwins: Standardized role as 'Software Development Consultant' for all customers",
    "First Citizens Bank: 'PM Services' maps to 'Project Manager' for BT title and Event Type",
    "BT (Billing Transaction) - appears to be internal terminology",
    "SOW (Statement of Work) - document type referenced",
    "Event Type - billing system field that may vary by merchant",
    "PO (Purchase Order) processing workflow specific to this merchant's operations"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Hylaine_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:28:49

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
      "rule": "Default tax line item processing: Every tax line item becomes a BT Events Processing when none are specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Use 'Hours' for all usage-based integration items",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Use 'Fixed price milestone' for milestone contracts",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Use 'Time and Materials' for Time and Materials contracts",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Ops Team does not need to notify anyone on completion of processing batches in Implementation or Active phase (for this merchant)",
      "category": "Post Processing Communications",
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
      "exception": "Tax processing default only applies 'If None Listed'",
      "condition": "When no specific tax line items are provided"
    },
    {
      "exception": "Post-processing notification requirement varies by merchant (this merchant requires 'No' notification)",
      "condition": "Merchant-specific configuration"
    },
    {
      "exception": "Feature request to split single BT into separate line items for multiple people in same role",
      "condition": "Special handling for role-based billing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Post-processing communication requirements",
      "customizable": true,
      "note": "This merchant does not require notification; others may differ"
    },
    {
      "element": "Customer information section",
      "customizable": true,
      "note": "Marked as 'None' for this merchant but structure exists for capturing specifics"
    },
    {
      "element": "Merchant temperament documentation",
      "customizable": true,
      "note": "Relationship-specific information to be captured per merchant"
    },
    {
      "element": "Key POC (Point of Contact) identification",
      "customizable": true,
      "note": "Buyer/decision maker varies by merchant"
    },
    {
      "element": "Tabs features preferences",
      "customizable": true,
      "note": "Features that key POC cares about are merchant-specific"
    },
    {
      "element": "Rewatch calls by dates and AE",
      "customizable": true,
      "note": "Implementation tracking specific to merchant timeline"
    },
    {
      "element": "Feature request: Split BT into separate line items",
      "customizable": true,
      "note": "Custom billing requirement for this merchant"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document structure is clear with labeled sections, making theme identification straightforward
- Explicit rules are clearly stated with specific instructions
- Some ambiguity exists around context (e.g., "BT" acronym not defined, "if necessary" conditions not fully specified)
- The document appears to be a template with some sections incomplete ("None" entries suggest missing information)
- The phrase "We are building this" suggests work in progress, indicating some rules may be aspirational rather than implemented

---

