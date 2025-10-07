# Raw LLM Analysis: MIS_ Anrok

## Document Overview
- **Total Chunks Analyzed**: 6
- **Analysis Timestamp**: 2025-10-02 12:11:50

---

## Chunk 1: MIS_ Anrok_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:11:50

### Original Content
```
Merchant Name: Anrok Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Hi Ops team The 3 contracts for Initial Calibration needed are below: Retool Core Annual Enterpret Harness Growth Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Anrok is a current Partner of Tabs and we offer an integration with ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Transaction (BT) Creation",
    "Customer and Product Setup Requirements",
    "Revenue Recognition and Service Date Handling",
    "Merchant-Specific Integration and Partnership Details",
    "Exclusions and Items Not to Process"
  ],
  "rules": [
    "Do not create customers manually - flag if customer doesn't exist",
    "Process each line item in the table as a separate product",
    "Include discounts inline within the BT",
    "Do not process contracts that are invoiced monthly (marked as 'total due monthly')",
    "Mark monthly invoiced contracts as processed without creating BT",
    "Item Name should use the name from the product column (e.g., 'Core annual', 'Anrok for Startups', 'Growth annual')",
    "Ignore the 'included taxable sales' column and fineprint",
    "Do not create usage BTs - these refer to events to track",
    "Do not create BTs that have an 'event to track'",
    "If free ramp period is included, ignore and do not include as a BT",
    "Revenue recognition should start from stated term start date regardless of free periods",
    "Billing start date should match service start date unless specific invoicing instructions present",
    "Service Start Date should use 'Term start' or 'Period start' date from pricing table",
    "Item Description is not necessary",
    "Quantity defaults to 1 unless explicitly stated",
    "Total Price should use the price listed for individual billing period",
    "Subscription should be annual - flag if it is not",
    "Use 'total due' amount for pricing",
    "Billing Type should be set to Flat",
    "For the last BT, extend months of service until 2050",
    "Calculate months of service based on difference between Period term start and Period term end",
    "Round months of service to whole months"
  ],
  "exceptions": [
    "If free period exists, billing and revenue should still start on stated term start date (not the service start date after free period)",
    "Monthly invoiced contracts should be marked as processed without BT creation",
    "Last BT in a series should be extended to 2050 regardless of original term end date",
    "Service start date may differ from billing start date when specific invoicing instructions are present",
    "Free ramp periods should be ignored for BT creation but revenue recognition still starts from original term start"
  ],
  "merchant_specific": [
    "Merchant Name: Anrok",
    "Anrok is a current Partner of Tabs with out-of-box integration",
    "Three specific contracts for Initial Calibration: Retool Core Annual, Enterpret, Harness Growth",
    "Specific product naming convention: 'Core annual', 'Anrok for Startups', 'Growth annual'",
    "Placeholder fields for Implementation POC and CX POC to be filled",
    "Billing model section to be filled by Implementation team",
    "Contract Processing Steps section to be filled by Implementation Success Post-Go Live",
    "Merchant-specific pricing table structure with 'Term start', 'Period start', 'included taxable sales' columns",
    "Specific end date convention of extending to year 2050 for final BT"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_ Anrok_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:00

### Original Content
```
g , 3 months for 7 1 2025 9 30 2025; 12 months for 10 1 2025 9 30 2026) Frequency: Use frequency in the  payment terms  section e g set to Year if "Annual subscription" Default to year if nothing is explicitly stated Calculate number of periods based on frequency Number of Periods: extend the last BT so that billing ends 2050 Net Terms: Use terms listed at the top of the contract or in the fees section; default to 30 if unstated Billing Timing: First of period Integration Items: Anrok Platform A...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term Configuration and Calculation",
    "Default Values and Fallback Rules",
    "Integration Items and Tax Processing",
    "Post-Processing Communication Workflows",
    "Merchant-Specific Customization Requirements"
  ],
  "rules": [
    {
      "category": "Billing Terms",
      "rule": "Calculate number of periods based on frequency specified in payment terms section",
      "details": "Example: 3 months for 7/1/2025-9/30/2025; 12 months for 10/1/2025-9/30/2026"
    },
    {
      "category": "Billing Terms",
      "rule": "Extend the last billing term so that billing ends in 2050",
      "details": "Ensures long-term billing continuation"
    },
    {
      "category": "Frequency",
      "rule": "Use frequency from payment terms section (e.g., set to Year if 'Annual subscription')",
      "details": "Default to year if nothing is explicitly stated"
    },
    {
      "category": "Net Terms",
      "rule": "Use terms listed at the top of the contract or in the fees section",
      "details": "Default to 30 days if unstated"
    },
    {
      "category": "Billing Timing",
      "rule": "Bill at first of period",
      "details": "Standard billing timing approach"
    },
    {
      "category": "Integration Items",
      "rule": "Include 'Anrok Platform Annual' for every billing term",
      "details": "Standard integration item requirement"
    },
    {
      "category": "Default Service Term",
      "rule": "If no service term is listed, operations default is 1 Year",
      "details": "Fallback rule for undefined service terms"
    },
    {
      "category": "Default Net Payment Terms",
      "rule": "If no net payment terms listed, operations default is 0 days",
      "details": "Immediate payment expected when terms not specified"
    },
    {
      "category": "Default Billing Frequency",
      "rule": "If no billing frequency listed, operations default is Monthly",
      "details": "Monthly billing as standard fallback"
    },
    {
      "category": "Tax Processing",
      "rule": "Every tax line item becomes a billing term (BT)",
      "details": "Default tax handling approach if none specified"
    },
    {
      "category": "Integration Items - Statsig",
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "details": "Merchant-specific integration item labeling"
    },
    {
      "category": "Integration Items - Pinata",
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "details": "Conditional labeling with merchant override option"
    }
  ],
  "exceptions": [
    {
      "condition": "Merchant-specific processing requests",
      "exception": "May differ by contract (e.g., always back-date invoice date to final day of the month)",
      "details": "Contract-specific variations override standard rules"
    },
    {
      "condition": "Pinata integration items",
      "exception": "Default to 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "details": "Merchant can override default labeling"
    },
    {
      "condition": "Handling SMB Business segment",
      "exception": "Strictly real-time usage billing in their app, separate from enterprise segment",
      "details": "Different billing approach for SMB vs enterprise customers"
    },
    {
      "condition": "Special customer relationships",
      "exception": "Invoice changes may be required due to merchant-customer relationship; special memos may be needed for certain invoices",
      "details": "Customer-specific customization requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling",
      "examples": ["Statsig → 'Sales'", "Pinata → 'Software Subscription Bundle'"],
      "customizable": true
    },
    {
      "element": "Invoice date processing",
      "examples": ["Back-date invoice date to final day of the month"],
      "customizable": true
    },
    {
      "element": "Post-processing notifications",
      "examples": ["Customer Success (Azmat Aziz) needs notification in Messari internal merchant channel when contracts are processed in Active phase"],
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "examples": ["Special memos for certain invoices", "Invoice changes due to merchant-customer relationship"],
      "customizable": true
    },
    {
      "element": "Events billing processing",
      "examples": ["Important information on events billing to be filled by Implementation Success post-go-live"],
      "customizable": true
    },
    {
      "element": "SMB business segment handling",
      "examples": ["Real-time usage billing in app", "API work to push invoices from Tabs to merchant app"],
      "customizable": true
    },
    {
      "element": "Billing term end date",
      "examples": ["Extend last BT to end in 2050"],
      "customizable": false
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document appears to be internal operational instructions with some formatting issues (likely OCR or extraction artifacts). While the core rules and themes are identifiable, the fragmented nature of some sections (particularly around "Examples: Anything to ignore in contracts" and the SMB business section) reduces certainty about complete context. The specific examples (Statsig, Pinata, Messari, Azmat Aziz) are clear, but some sections marked for post-go-live completion suggest this is a template with incomplete information.

---

## Chunk 3: MIS_ Anrok_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:01

### Original Content
```
We are aligned on only supporting their enterprise business in the SOW and sales process Tiered for billing - Demo env Merchant Calls (AE to fill for all videos prior to Imp involvement, Imp to fill prior to go-live Success to fill to fill Post-Go Live) Disco: https: us-56595 app gong io call id 3466057865361804783 Demo https: us-56595 app gong io call id 4117055528466818933 Demo - Enterprise Workflow https: us-56595 app gong io call id 2100036466179227380 POC Kickoff https: us-56595 app gong
```

### LLM Analysis Response
```json
{
  "themes": [
    "Enterprise business focus and scope limitation",
    "Tiered billing structure with demo environment",
    "Merchant call documentation and ownership across lifecycle stages",
    "Sales and implementation process workflow",
    "Stakeholder responsibility mapping (AE, Implementation, Success teams)"
  ],
  "rules": [
    "Only enterprise business is supported in the SOW and sales process",
    "Billing must be structured in tiers",
    "A demo environment must be included in billing structure",
    "AE (Account Executive) must fill merchant call documentation for all videos prior to Implementation team involvement",
    "Implementation team must fill merchant call documentation prior to go-live",
    "Success team must fill merchant call documentation post-go-live",
    "Required call types include: Discovery (Disco), Demo, Demo - Enterprise Workflow, and POC Kickoff",
    "All merchant calls must be documented with Gong call IDs"
  ],
  "exceptions": [
    "Non-enterprise business is explicitly excluded from support scope",
    "Demo environment receives special billing treatment (separate tier)"
  ],
  "merchant_specific": [
    "Specific Gong call IDs referenced (merchant-specific recordings)",
    "Enterprise workflow requirements may vary by merchant",
    "Tiered billing structure details would be customized per merchant",
    "POC (Proof of Concept) scope and timeline",
    "Demo environment specifications and requirements"
  ],
  "confidence_score": 0.72
}
```

**Reasoning for Confidence Score (0.72):**
- The document chunk appears incomplete (cuts off mid-sentence with "gong")
- Clear structure and ownership rules are evident
- Some context is missing about specific billing tier details
- The enterprise-only focus is explicit and clear
- Call documentation workflow is well-defined but implementation details are limited

---

## Chunk 4: MIS_ Anrok_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:09

### Original Content
```
io call id 5134506017868582599 POC Wrap Up https: us-56595 app gong io call id 2899793354001067315 Path to Partnership https: us-56595 app gong io call id 6251739346428489001 ROI Discussion https: us-56595 app gong io call id 8713876302251405766 Commercial Alignment https: us-56595 app
```

### LLM Analysis Response
```json
{
  "themes": [
    "Sales call documentation and tracking",
    "Customer relationship management stages",
    "Partnership development process",
    "Commercial and financial discussions"
  ],
  "rules": [
    "Sales calls must be documented with unique identifiers (call IDs)",
    "Calls should be categorized by type/purpose (POC Wrap Up, Path to Partnership, ROI Discussion, Commercial Alignment)",
    "Call recordings or documentation are stored in Gong.io platform",
    "Each call requires a specific URL format: https://us-56595.app.gong.io/call?id=[call_id]"
  ],
  "exceptions": [
    "Insufficient data to determine exceptions or special cases from this document chunk"
  ],
  "merchant_specific": [
    "Gong.io platform instance identifier: 'us-56595' (may vary by merchant organization)",
    "Call categorization labels (POC Wrap Up, Path to Partnership, ROI Discussion, Commercial Alignment) may be customized per merchant's sales process",
    "Call ID format and numbering system may be platform-specific",
    "Integration with specific CRM or sales enablement tools"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for low confidence score:**
- The document chunk appears incomplete or fragmented (truncated URLs, no full sentences)
- Limited context about the actual instructions or requirements
- Unclear whether this is reference material, a log, or actual instruction content
- Cannot determine complete rules or processes from URL fragments alone
- May be metadata or navigation elements rather than substantive instructions

---

## Chunk 5: MIS_ Anrok_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:13

### Original Content
```
gong io call id 8810264256902447165 Accounting with Emily https: us-56595 app gong io call id 1394215840612473461 Accounting with Emily Part 2 https: us-56595 app gong io call id 4876324589174760727 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills We are handling their enterprise segment Flat subscription fee and tiered unit pricing for Toal   amount of taxable products Currently sending 20-30 invoices a month with the enterprise...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing structure",
    "Enterprise customer segment management",
    "Pricing model configuration",
    "System transition and handoff process",
    "Accounting and implementation coordination"
  ],
  "rules": [
    "Merchant uses flat subscription fee combined with tiered unit pricing",
    "Pricing tiers are based on total amount of taxable products",
    "Enterprise segment customers require special handling",
    "Invoice volume is approximately 20-30 invoices per month for enterprise customers",
    "Account Executive (AE) is responsible for initial information gathering",
    "Implementation team serves as completion DRI (Directly Responsible Individual) on handoff",
    "Documentation must include information on how merchant bills customers"
  ],
  "exceptions": [
    "Enterprise segment receives different billing treatment than standard customers",
    "Invoicing system is transitioning from third-party (Countsy) to in-house (HanYue), indicating a special migration scenario"
  ],
  "merchant_specific": [
    "Merchant name: Emily (from accounting team)",
    "Current invoicing provider: Countsy",
    "New in-house invoicing system: HanYue",
    "Specific invoice volume: 20-30 per month",
    "Customer segment focus: Enterprise",
    "Pricing structure: Flat subscription + tiered unit pricing based on taxable products",
    "Gong.io call references for detailed context (call IDs: 8810264256902447165, 1394215840612473461, 4876324589174760727)"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document appears to be incomplete notes from implementation calls. The text ends abruptly with "1) What is the merchant temperament" suggesting more content follows. There are also formatting issues and incomplete sentences ("Toal amount" appears to be a typo for "Total amount"). While key information about billing structure and system transition is clear, the fragmentary nature and lack of complete context reduces confidence in capturing all relevant rules and requirements.

---

## Chunk 6: MIS_ Anrok_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:24

### Original Content
```
Already a partner of ours and very excited about the relationship Selina (VP of Finance) is our champion - very nice, smart and going on maternity leave in September She ll oversee the Tabs implementation HanYue (Controller) will be the Tabs power user She joined in April Very nice and a Tabs champion Emily (Head of Accounting) is a seasoned finance vet She jpoinged the team at the end of May and is still onboarding Will be intently interested in Month end close and reporting 3) What are the Tab...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Organizational Structure",
    "Contract-to-Cash Process Automation",
    "System Integration and Data Synchronization",
    "Revenue Recognition and Reporting",
    "Collections and Cash Application Management"
  ],
  "rules": [
    {
      "rule": "Contract data must be translated from Salesforce (SFDC) to NetSuite (NS)",
      "type": "process_requirement",
      "current_state": "manual translation"
    },
    {
      "rule": "Invoice schedules must be generated from contract key terms",
      "type": "automation_requirement",
      "current_state": "manual process"
    },
    {
      "rule": "Collections process is being moved in-house from third-party (Countsy)",
      "type": "process_change",
      "current_state": "handled by Countsy"
    },
    {
      "rule": "DSO and overdue invoice visibility required before end of month",
      "type": "reporting_requirement",
      "current_state": "no visibility before EOM"
    },
    {
      "rule": "Usage billing schedules must be maintained accurately",
      "type": "revenue_requirement",
      "current_state": "managed in spreadsheets"
    },
    {
      "rule": "Payment application must be automated to eliminate third-party involvement",
      "type": "automation_requirement",
      "current_state": "manual via Countsy"
    },
    {
      "rule": "NetSuite and Salesforce systems require integration",
      "type": "technical_requirement",
      "current_state": "no integration exists"
    }
  ],
  "exceptions": [
    {
      "exception": "Selina (VP of Finance) going on maternity leave in September",
      "impact": "Transition of oversight responsibilities during implementation"
    },
    {
      "exception": "Emily (Head of Accounting) still onboarding as of end of May",
      "impact": "May require additional training or delayed full engagement"
    },
    {
      "exception": "Usage billing component requires special handling",
      "impact": "Different from standard contract billing, needs automated schedule generation"
    }
  ],
  "merchant_specific": [
    {
      "element": "Stakeholder names and roles",
      "details": "Selina (VP Finance), HanYue (Controller/Power User), Emily (Head of Accounting)",
      "customization_needed": true
    },
    {
      "element": "Third-party service provider",
      "details": "Countsy - currently handling collections and cash application",
      "customization_needed": true
    },
    {
      "element": "System stack",
      "details": "Salesforce (SFDC) and NetSuite (NS) as core systems",
      "customization_needed": true
    },
    {
      "element": "Billing model",
      "details": "Includes usage-based billing component",
      "customization_needed": true
    },
    {
      "element": "Timeline constraints",
      "details": "September maternity leave deadline for key stakeholder",
      "customization_needed": true
    },
    {
      "element": "Month-end close process",
      "details": "Specific focus area for Head of Accounting",
      "customization_needed": false
    }
  ],
  "confidence_score": 0.85
}
```

---

