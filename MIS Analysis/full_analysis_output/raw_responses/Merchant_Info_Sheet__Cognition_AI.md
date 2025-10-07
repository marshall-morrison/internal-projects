# Raw LLM Analysis: Merchant Info Sheet_ Cognition AI

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:33:30

---

## Chunk 1: Merchant Info Sheet_ Cognition AI_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:30

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
    "Billing Models and Payment Terms",
    "Contract Structure and Free Trial Management",
    "Accounts Payable (AP) Portal Integration and Automation"
  ],
  "rules": [
    "Billing model must support flat SaaS fee structure",
    "Payment frequency options must include monthly, quarterly, or annually",
    "System must support invoice scheduling and calculations",
    "Automated follow-up functionality is required",
    "AP Portal automation capability is required",
    "Reporting and revenue recognition (Rev Rec) features must be available",
    "Free trials must be incorporated into contract structure",
    "System must handle contracts with opt-in renewal periods",
    "Manual CS work for AP portal management is acceptable as interim solution"
  ],
  "exceptions": [
    "Currently using flat SaaS fee but planning to move to usage-based billing in the future",
    "Merchant deals with approximately 20 contracts (relatively low volume)",
    "Accepts manual work by customer success team for AP portal handling as temporary workaround",
    "Contract example: 6-month initial term with optional 6-month extension (non-standard structure)",
    "Usage billing is being considered but not currently implemented"
  ],
  "merchant_specific": [
    "Key contacts: Salima (main user/champion), David (user), Kyle (board member)",
    "Educational background: Salima and Rebecca attended CBS (Columbia Business School)",
    "Specific contract volume: 20 contracts",
    "High volume of AP portals to manage",
    "Specific contract structure: 6-month terms with 6-month opt-in extensions",
    "Future billing model transition: moving from flat fee to usage-based",
    "Characterization: 'Smart people who are easy to work with'"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be informal notes or a summary, which may lack complete context
- Some abbreviations (CBS, AP, Rev Rec) are interpretable but could have alternative meanings
- The structure suggests this is extracted from a discovery call or customer interview
- Clear information about features, billing, and contacts, but some ambiguity around future plans
- The phrase "Are the unique things about the customer creation process" suggests incomplete transcription or notes

---

## Chunk 2: Merchant Info Sheet_ Cognition AI_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:31

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
    "Technical Integration Requirements"
  ],
  "rules": [
    {
      "rule": "Opt-out clause requires 30 days notice",
      "category": "Contract Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Opt-out window is 6 months from start date (before 1/12/25)",
      "category": "Contract Terms",
      "specificity": "explicit"
    },
    {
      "rule": "Standard onboarding sequence: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "category": "Onboarding Process",
      "specificity": "implicit"
    },
    {
      "rule": "Multiple POCs must be identified: GTM, Implementation, AR, and Billing",
      "category": "Stakeholder Management",
      "specificity": "implicit"
    },
    {
      "rule": "Tax integration method must be confirmed during onboarding",
      "category": "Technical Integration",
      "specificity": "explicit"
    },
    {
      "rule": "ERP system identification is required for integration planning",
      "category": "Technical Integration",
      "specificity": "implicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt-out clause may not apply to all merchants (noted as 'If Exists')",
      "condition": "Contract-dependent feature"
    },
    {
      "exception": "Tax engine may vary by merchant (QBO mentioned as possibility for this merchant)",
      "condition": "Pending confirmation during implementation"
    },
    {
      "exception": "CFO role is outsourced rather than in-house",
      "condition": "Merchant-specific organizational structure"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company profile and business description",
      "customization_needed": "Each merchant will have unique company summary, industry, and product offerings"
    },
    {
      "element": "Key personnel names and roles",
      "customization_needed": "Contact names, titles, and responsibilities vary per merchant"
    },
    {
      "element": "Specific pain points and goals",
      "customization_needed": "Each merchant has unique challenges (e.g., 'Manual billing out of QBO', 'AP Portals', 'Google Sheets for bookkeeping')"
    },
    {
      "element": "Current technology stack",
      "customization_needed": "ERP systems, tax engines, and accounting software differ by merchant"
    },
    {
      "element": "Timeline dates",
      "customization_needed": "All milestone dates are merchant-specific"
    },
    {
      "element": "Opt-out terms",
      "customization_needed": "Opt-out clauses and conditions may vary or not exist for all merchants"
    },
    {
      "element": "Team size and structure",
      "customization_needed": "Finance team composition varies (this merchant has 'one person finance team')"
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 3: Merchant Info Sheet_ Cognition AI_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:46

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
    "Send Slackbot notification when contract processing is complete for the first invoice",
    "Send Slackbot notification for first invoice on renewals",
    "All flat fees outlined in contracts are billed upfront upon SOW execution by default",
    "Map 'Service column' to 'Item name' field",
    "Map 'description column' to 'Item description' field",
    "Annual total fees should be summed together for initial invoice",
    "Start date should be set to the effective date on contract",
    "Set 'of periods' to 1 for upfront billing",
    "Set Frequency to amount of months specified in contract or 'None' if not applicable",
    "Process usage-based billing as standard unit pricing for overages only",
    "For usage billing: Name = 'On-demand ACU'",
    "For usage billing: Description = 'Devin' OR 'Fine-Tuned Devin'",
    "For usage billing: Billing type = 'Unit price'",
    "For usage billing: Integration Item = 'AI License Agent'",
    "For usage billing: Event type = 'Devin' or 'Unity_Catalog_Fine_Tuned_Devin' depending on type",
    "For usage billing: Price = price stated in contract language",
    "For usage billing: Start Date = effective date on contract",
    "For usage billing: Frequency = monthly for the amount of months in the term",
    "Ignore monthly capacity as it is tracked internally by merchant",
    "For renewal contracts, process billing terms under the renewal contract only",
    "For renewal contracts, only process billing terms under 'Amended SOW Services' section",
    "For renewal contracts, ignore billing terms under 'Base SOW services' section as they are already processed under original contract"
  ],
  "exceptions": [
    "If a different billing frequency is outlined in the contract, defer to that instead of upfront billing",
    "Amendments or exceptions to upfront billing may exist and should be followed",
    "Some contracts may have two different types of ACU capacities (Devin and Fine-Tuned Devin) which may have same or different prices",
    "When two ACU capacity types exist, process as two separate billing terms",
    "Despite statements indicating monthly billing in contract, annual fees may need to be billed upfront (example shows 80k total instead of monthly)"
  ],
  "merchant_specific": [
    "Slackbot notification system (communication tool)",
    "SOW (Statement of Work) execution terminology",
    "ACU (likely Application Compute Units or similar) capacity metrics",
    "Devin and Fine-Tuned Devin product/service names",
    "Unity_Catalog_Fine_Tuned_Devin event type naming",
    "AI License Agent integration item",
    "Commit consumption usage model specific to this merchant",
    "Internal capacity tracking system",
    "Contract structure with 'Amended SOW Services' and 'Base SOW services' sections",
    "Specific pricing examples ($2.22, $1.97) that are merchant-specific"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet_ Cognition AI_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:33:48

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
      "category": "billing_processing"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "contract_defaults"
    },
    {
      "rule": "Default Net Payment Terms is 30 days if none listed",
      "category": "payment_defaults"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "billing_defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction) Events",
      "category": "tax_processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling",
      "example": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "integration_labeling",
      "example": true
    },
    {
      "rule": "Events Processing will use API calls if merchant moves to this model",
      "category": "events_processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice dates may be back-dated to final day of month based on specific merchant contract requirements",
      "condition": "merchant-specific contract terms"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by Merchant",
      "condition": "explicit merchant override"
    },
    {
      "exception": "Tax line item processing may differ if merchant specifies alternative handling",
      "condition": "merchant-specific tax requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating rules",
      "customizable": true,
      "description": "Some merchants may require invoice dates to be back-dated to final day of month"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "description": "Different merchants may have specific labeling requirements for integration items (e.g., Statsig, Pinata)"
    },
    {
      "element": "Post-processing notification workflows",
      "customizable": true,
      "description": "Notification recipients, channels, and timing vary by merchant (example: Customer Success [Azmat Aziz] via Messari internal channel for Active phase)"
    },
    {
      "element": "Customer profile characteristics",
      "customizable": true,
      "description": "Merchant works with mostly large ACV enterprises, requires AP Portal automation tracking"
    },
    {
      "element": "Service terms, payment terms, and billing frequency",
      "customizable": true,
      "description": "Can be overridden from defaults based on merchant contract"
    },
    {
      "element": "Events Processing model",
      "customizable": true,
      "description": "API call integration is conditional on merchant adoption"
    }
  ],
  "confidence_score": 0.85
}
```

---

