# Raw LLM Analysis: Copy of Merchant Info Sheet_ Cognition AI

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 10:26:17

---

## Chunk 1: Copy of Merchant Info Sheet_ Cognition AI_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:17

### Original Content
```
Salima went to CBS with Rebecca Smart people who are easy to work with 2) Is there key POC the buyer decision maker Salima, David, and Kyle Salima is main user and champion David is also a user Kyle is a board member 3) What are the Tabs features the key POC care about Invoice scheduling and calculations Automated Follow Up AP Portal automation Reporting and Rev Rec Billing model Flat SaaS Fee (for now, moving to usage) Paid Monthly, Quarterly, or Annually Only  20 contracts Deal with a ton of A...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Key Personnel and Decision-Making Structure",
    "Product Features and Capabilities Requirements",
    "Billing and Payment Models",
    "Contract Structure and Terms",
    "Accounts Payable (AP) Portal Management"
  ],
  "rules": [
    "Billing model must support flat SaaS fee structure",
    "Payment frequency options must include monthly, quarterly, or annually",
    "System must support invoice scheduling and calculations",
    "Automated follow-up functionality is required",
    "AP Portal automation capability is needed",
    "Reporting and revenue recognition (Rev Rec) features must be available",
    "Free trials must be incorporated into contract structure",
    "System must handle contracts with opt-in renewal periods",
    "Manual CS work for AP portal management is acceptable as interim solution"
  ],
  "exceptions": [
    "Currently using flat SaaS fee but planning to transition to usage-based billing in the future",
    "Merchant deals with approximately 20 contracts (relatively low volume)",
    "Willing to accept manual work from customer success team for AP portal handling (temporary workaround)",
    "Contract example includes 6-month initial term with optional 6-month extension (non-standard structure)",
    "Usage billing is being considered but not currently implemented"
  ],
  "merchant_specific": [
    "Key contacts: Salima (main user/champion), David (user), Kyle (board member)",
    "Educational background reference: 'Salima went to CBS with Rebecca'",
    "Specific contract volume: 20 contracts",
    "High volume of AP portals to manage",
    "Specific contract structure: 6-month terms with 6-month opt-in extensions",
    "Current billing model: Flat SaaS Fee (transitioning to usage-based)",
    "Champion and decision-maker hierarchy: Salima as primary, with David and Kyle as secondary stakeholders"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be informal notes or meeting minutes, which reduces clarity
- Some context is missing (e.g., what "CBS" refers to, full company details)
- The structure is fragmented, making some interpretations uncertain
- However, key business requirements and stakeholder information are clearly identifiable
- The billing model and feature requirements are explicitly stated

---

## Chunk 2: Copy of Merchant Info Sheet_ Cognition AI_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:18

### Original Content
```
Merchant Demo date: July 2nd, 2024 Scoping start date: Jul 2, 2024 MSA Signature Date: Jul 9, 2024 Onboarding Kick Off Date: Jul 12, 2024 [If Exists] Opt Out Date: Opt out 6 months in with 30 days notice ahead of 1 12 25 Go Live Date: Aug 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: - need to confirm this Might be using QBO Tax engine Key people at Merchant Accountant: Salima Ghadimi, Head of Ops CFO: David Morgan, Outsourced CFO Customer service rep who is really involved: Kyle Do...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Key Stakeholder Identification and Roles",
    "Merchant Pain Points and Solution Goals",
    "Contract Terms and Opt-Out Provisions",
    "Technical Integration and Systems"
  ],
  "rules": [
    {
      "rule": "Opt-out clause requires 30 days notice",
      "category": "Contract Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Opt-out window is 6 months from start date",
      "category": "Contract Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Onboarding follows structured timeline: Demo → Scoping → MSA Signature → Kick Off → Go Live",
      "category": "Process",
      "specificity": "implicit"
    },
    {
      "rule": "Multiple POCs must be identified for different functional areas (GTM, Implementation, AR, Billing)",
      "category": "Stakeholder Management",
      "specificity": "implicit"
    },
    {
      "rule": "Tax integration requirements must be confirmed during onboarding",
      "category": "Technical Integration",
      "specificity": "explicit"
    },
    {
      "rule": "ERP system information must be documented",
      "category": "Technical Integration",
      "specificity": "implicit"
    }
  ],
  "exceptions": [
    {
      "exception": "This merchant has 'N/A' for opt-out clause goals, suggesting no specific opt-out conditions",
      "context": "Contract Terms"
    },
    {
      "exception": "Tax engine may use QBO instead of standard integration (pending confirmation)",
      "context": "Technical Integration"
    },
    {
      "exception": "CFO is outsourced rather than in-house",
      "context": "Organizational Structure"
    },
    {
      "exception": "Single person (Salima) serves multiple POC roles (Head of Ops, AR POC, Billing POC)",
      "context": "Stakeholder Management"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company profile and business model",
      "details": "Applied AI lab building software agents (Devin product)",
      "customization_needed": true
    },
    {
      "element": "Current systems and tools",
      "details": "Using QBO for billing, Google Sheets for accounting, dealing with AP Portals",
      "customization_needed": true
    },
    {
      "element": "Team size and structure",
      "details": "One-person finance team, outsourced CFO",
      "customization_needed": true
    },
    {
      "element": "Specific pain points",
      "details": "Manual billing, AP Portal management complexity, spreadsheet-based processes",
      "customization_needed": true
    },
    {
      "element": "Named stakeholders",
      "details": "Salima Ghadimi, David Morgan, Kyle Doppelt",
      "customization_needed": true
    },
    {
      "element": "Onboarding dates",
      "details": "All milestone dates from July 2 to August 1, 2024",
      "customization_needed": true
    },
    {
      "element": "Opt-out calculation date",
      "details": "Specific date of 1/12/25 based on 6-month window",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Copy of Merchant Info Sheet_ Cognition AI_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:30

### Original Content
```
Contract Processing Steps When a contract is done processing, please send Slackbot for the first invoice For renewals, still send Slackbot for first invoice Steps to process SaaS billing model for services up front Usually, all flat fees laid out in the contract are billed up front upon SOW execution, which is stated in the contract However, sometimes, there might be amendments or exceptions to this If another billing frequency is outlined in the contact, please defer to that Item name   Service...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Workflow and Notifications",
    "SaaS Billing Models and Upfront Fee Processing",
    "Commit Consumption and Usage-Based Billing",
    "Renewal Contract Processing Rules",
    "Billing Term Configuration and Data Mapping"
  ],
  "rules": [
    "Send Slackbot notification when contract is done processing for the first invoice",
    "Send Slackbot notification for first invoice on renewals",
    "All flat fees laid out in contract are billed up front upon SOW execution by default",
    "Item name should be mapped from Service column",
    "Item description should be mapped from description column",
    "Annual total fees should be added together for initial invoice",
    "Start date should be the effective date on contract",
    "Number of periods should be set to 1 for upfront billing",
    "Frequency should be amount of months in the months column or None if not specified",
    "Usage-based billing should be processed as standard unit pricing",
    "Usage data submissions are only for overages",
    "Billing type for usage model should be Unit price",
    "Integration Item for usage model should be AI License Agent",
    "Start Date for usage billing should match effective date on contract",
    "Frequency for usage billing should be monthly for the amount of months in the term from initial pricing table",
    "Monthly capacity should be ignored as it is tracked internally",
    "For renewal contracts, process billing terms under the renewal contract only",
    "For renewal contracts, only process billing terms under Amended SOW Services section",
    "For renewal contracts, ignore billing terms under Base SOW services as they are already processed under original contract"
  ],
  "exceptions": [
    "If another billing frequency is outlined in the contract, defer to that instead of upfront billing",
    "Amendments or exceptions to upfront billing may exist and should be followed",
    "Some contracts may have two different types of ACU capacities (Devin and Fine-Tuned Devin) which should be processed as two separate billing terms",
    "ACU capacity prices might be the same or different between Devin and Fine-Tuned Devin types",
    "NOT monthly billing should be processed as upfront despite monthly indicators in certain chart sections"
  ],
  "merchant_specific": [
    "Slackbot notification system (communication platform)",
    "SOW (Statement of Work) execution terminology",
    "ACU (likely Application Compute Units) capacity model",
    "Devin and Fine-Tuned Devin as specific product/service types",
    "Event types: 'Devin' and 'Unity_Catalog_Fine_Tuned_Devin'",
    "AI License Agent as integration item",
    "Commit consumption usage model specific to this merchant",
    "Base SOW services vs Amended SOW Services distinction in renewals",
    "Internal capacity tracking system reference"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Copy of Merchant Info Sheet_ Cognition AI_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:34

### Original Content
```
Some old ones mention free trials, please ignore, as they are not part of billing cycle Specifics processing things merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becom...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and billing configurations",
    "Tax and line item processing procedures",
    "Integration item labeling and categorization",
    "Post-processing communication workflows",
    "Enterprise customer management and AP Portal automation"
  ],
  "rules": [
    {
      "rule": "Free trial mentions in old documents should be ignored as they are not part of billing cycle",
      "category": "Billing Processing"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Service Terms"
    },
    {
      "rule": "Default Net Payment Terms is 30 days if none specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Frequency"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction) Events",
      "category": "Tax Processing"
    },
    {
      "rule": "Events Processing uses API calls when merchant moves to this model",
      "category": "Events Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "example": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Labeling",
      "example": true
    },
    {
      "rule": "Ops Team must notify designated personnel upon completion of processing batches in Implementation or Active phase",
      "category": "Post-Processing Communication"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice date may be back-dated to final day of the month per specific merchant contract requirements",
      "condition": "Merchant-specific contract terms"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by Merchant",
      "condition": "Merchant override"
    },
    {
      "exception": "Tax line item processing may differ if merchant specifies alternative handling",
      "condition": "If merchant provides specific instructions"
    },
    {
      "exception": "Default parameters (Service Term, Payment Terms, Billing Frequency) can be overridden by merchant-specific contracts",
      "condition": "When explicitly listed in merchant documentation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating rules",
      "customizable": true,
      "description": "May differ by contract (e.g., always back-date to final day of month)"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "description": "Specific integration vendors (Statsig, Pinata) have default labels but can be overridden"
    },
    {
      "element": "Post-processing notification recipients",
      "customizable": true,
      "description": "Example shows Customer Success (Azmat Aziz) for Messari, but varies by merchant"
    },
    {
      "element": "Notification timing and channels",
      "customizable": true,
      "description": "When and where to notify varies (e.g., Messari internal merchant channel when contracts are processed in Active phase)"
    },
    {
      "element": "Customer characteristics",
      "customizable": true,
      "description": "Important customer information like enterprise focus, large ACV, AP Portal automation needs"
    },
    {
      "element": "Feature requests",
      "customizable": true,
      "description": "Merchant-specific needs like AP Portal Automation, enterprise login tracking"
    }
  ],
  "confidence_score": 0.85
}
```

---

