# Raw LLM Analysis: 2X + Intelligent Demand MIS

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:25:29

---

## Chunk 1: 2X + Intelligent Demand MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:25:29

### Original Content
```
Merchant Name 2X Marketing Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General These instructions apply to both Intelligent Demand and 2X However, there are al...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Amendment Processing",
    "Billing Template (BT) Creation and Categorization",
    "Revenue Category Classification (MRR, Project, Ad-hoc, Program Spend, Reimbursement)",
    "Proration Requirements for First and Last Month",
    "Merchant-Specific Contract Handling (Broadcom, Intelligent Demand)"
  ],
  "rules": [
    "For amendments: Original BTs must be adjusted or supplemented according to amendment changes",
    "If amendment has net new BTs AND adjusts original contract: (1) adjust original BTs to end before amendment date, (2) add new BTs per amendment under amendment contract",
    "Add proration BTs for first and last month if needed under the amendment contract",
    "For 2X: Combine different categories of line items into a single BT",
    "Five standard categories exist: MRR, Project, Ad-hoc, Program Spend, Reimbursement Travel",
    "MRR includes Monthly Labor Fees (both general and employee-specific line items)",
    "Project Fees are one-time revenue for projects, including fixed fees for transition/onboarding or contracts under 6 months",
    "Ad-hoc work is hourly work billed based on actuals (one-time revenue)",
    "Program Spend covers third-party spend with no mark-up (LinkedIn, Google Ads, Bombora, etc.)",
    "Reimbursable Travel covers client-reimbursed expenses, likely only used in manual invoice creation",
    "Only one BT type per category per contract (excluding prorated BTs)",
    "Never have 2 MRR type BTs in a contract",
    "Never have 2 Project BTs in a contract",
    "Instructions apply to both Intelligent Demand and 2X, with additional Intelligent Demand-specific instructions available"
  ],
  "exceptions": [
    "Broadcom contracts may appear as duplicates but are likely not - requires careful review",
    "Intelligent Demand has specific additional instructions beyond general rules",
    "Prorated BTs are excluded from the 'one type per category' rule",
    "Ad-hoc work is not common but present in some contracts",
    "Reimbursable Travel is unlikely to be seen in regular processing"
  ],
  "merchant_specific": [
    "POC fields: IM POC and CX POC need to be filled by Implementation",
    "Billing model section to be completed by Implementation team",
    "Customer creation process may have unique merchant-specific requirements",
    "Contract structure and breakdown varies by merchant",
    "Broadcom requires special attention due to potential duplicate-looking contracts",
    "Intelligent Demand has separate specific instructions",
    "Program Spend customers commonly include LinkedIn, Google Ads, Bombora",
    "Contract Processing Steps section to be filled post-go-live by Implementation Success team"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: 2X + Intelligent Demand MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:25:38

### Original Content
```
They should be combined into 1 However, you could have 1 MRR BT and 1 project BT Item Name Should be a variation of the name of the category - can use best judgment   take what the contract says For Monthly Recurring Revenue  Monthly Labor Fees   Monthly Recurring Fees  Project Fees Ad-hoc Fees Program Spend Reimbursement Travel Can call discounts  Discount  Item Description: First take the header of the document at the top (will be an SOW description - is often in Red text)  Statement of Work  ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Template (BT) Creation and Categorization",
    "Monthly Fee Proration Logic and Calculations",
    "Item Naming and Description Conventions",
    "Integration Item Classification System",
    "Billing Start Date Determination Rules"
  ],
  "rules": [
    "Maximum of 2 billing templates per category allowed (1 MRR BT and 1 project BT)",
    "Item names should be variations of category names based on contract language",
    "Item descriptions must start with SOW header (often in red text) from document top",
    "Do not use all caps in descriptions - adjust capitalization as needed",
    "Add dash separator followed by category type (Monthly Recurring Charges, Transition Project, etc.)",
    "Only one integration item can be selected per BT from predefined list",
    "Total months of service must match number of periods for each BT",
    "Prorated BTs should have 1 period",
    "If BT starts within 4 days of month start, round to 1st of closest month and skip prorating",
    "Monthly fees starting mid-month require 3 BTs: normal fee, first month prorated, last month prorated",
    "Open-ended contracts do not require third prorated BT for end date",
    "Open-ended contracts must extend through 12/31/2026 at minimum",
    "Default contract length is 24 months when open-ended",
    "First prorated BT: starts on actual start date, 1 period, frequency = days to end of month, billing timing = Last of Period",
    "Second prorated BT (last month): starts first day of final month, 1 period, frequency = remaining days, billing timing = First of Period",
    "Prorated price calculation: (monthly fee ÷ days in month) × days in period",
    "Proration only applies to recurring monthly fees, not one-time fees",
    "Project fees with defined billing schedules: assume 8 weeks project length if not specified",
    "50/50 project split: first 50% recognized in first 4 weeks, second 50% in second 4 weeks",
    "Billing start date: check Invoicing Terms or Timeline section first",
    "Use largest time unit when range given (e.g., 4-6 weeks = use 6 weeks)",
    "If BT start date cannot be determined, set price to $0 for merchant to complete later",
    "When unsure about prorating, default to prorating",
    "If start date can be calculated (e.g., '2 weeks after execution'), perform proration"
  ],
  "exceptions": [
    "BTs starting less than 4 days from month start can skip prorating and start on 1st of nearest month",
    "Open-ended contracts (auto-renewal or 'Until Terminated') do not need third prorated BT",
    "If SOW not on 2X paper, use best judgment for unique identifier",
    "If integration items don't exist from predefined list, leave blank",
    "If BT doesn't fit Monthly Recurring or Transition Project categories, use generic category (Ad-hoc, Program Spend, etc.)",
    "When start date is vague (e.g., 'starts within 2 weeks of kickoff'), set BT to $0",
    "If billing terms have specific dates, use those instead of calculated dates from signature"
  ],
  "merchant_specific": [
    "2X-specific instruction for integration items (MRR - Fixed Resources option only when combining 2 MRR types)",
    "2X prorates their monthly fees (merchant-specific practice)",
    "2X Statement of Work naming convention in examples",
    "Red text indicator for SOW headers (document formatting convention)",
    "Integration item categories: MRR - Fixed Resources, MS - MRR Shared Services, OTP - Transition Project, OTP - Other Project, ADH - Ad-hoc work, Program Spend, Reimbursable Travel",
    "Category naming conventions: Monthly Labor Fees, Monthly Recurring Fees, Project Fees, Ad-hoc Fees, Program Spend, Reimbursement Travel, Discount",
    "FTE (Full Time Employee) charges terminology",
    "Garage system reference (billing system being used)",
    "12/31/2026 as standard extension date for open-ended contracts",
    "Loom video reference for general explanation"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: 2X + Intelligent Demand MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:25:52

### Original Content
```
Service Start Date: Same as billing start date Months of Service: Default to 24 months as the total contract length if there isn t a length listed - many of the 2X contracts are open ended Unless the specific date ranges is given If contract says a service will take 6-8 weeks, months of service would be 2 months For shorter BTs like onboarding, use the time they list and round up If 2 weeks -  1 month If 6 weeks -  2 months If they don t list a timeframe, use best judgement Frequency Mostly can ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing configuration and setup",
    "Service term and date management",
    "Integration item mapping and categorization",
    "Default values and fallback rules for missing information",
    "Merchant-specific processing workflows and customizations"
  ],
  "rules": [
    {
      "category": "Service Terms",
      "rule": "Default contract length is 24 months if not specified",
      "context": "Months of Service"
    },
    {
      "category": "Service Terms",
      "rule": "For services taking 6-8 weeks, set months of service to 2 months",
      "context": "Duration calculation"
    },
    {
      "category": "Service Terms",
      "rule": "For 2 weeks duration, round up to 1 month",
      "context": "Short-term services"
    },
    {
      "category": "Service Terms",
      "rule": "For 6 weeks duration, round up to 2 months",
      "context": "Short-term services"
    },
    {
      "category": "Service Terms",
      "rule": "Service start date equals billing start date",
      "context": "Date alignment"
    },
    {
      "category": "Billing Frequency",
      "rule": "Onboarding/Launch services use Fixed Fee frequency",
      "context": "Service type-based frequency"
    },
    {
      "category": "Billing Frequency",
      "rule": "Monthly Labor Fees determine frequency from invoicing terms",
      "context": "Recurring services"
    },
    {
      "category": "Billing Frequency",
      "rule": "Fixed fee deliverables use 'None' as frequency",
      "context": "One-time payments"
    },
    {
      "category": "Payment Terms",
      "rule": "Default net payment terms is 30 days if not stated",
      "context": "Invoice payment"
    },
    {
      "category": "Payment Terms",
      "rule": "Ops default for net payment terms is 0 if none listed",
      "context": "Fallback rule"
    },
    {
      "category": "Quantity",
      "rule": "Use quantity of 1 for everything",
      "context": "Line item quantity"
    },
    {
      "category": "Discounts",
      "rule": "If discount is its own line item, create separate BT (billing transaction)",
      "context": "Discount handling"
    },
    {
      "category": "Discounts",
      "rule": "If discount is part of specific billing item, use in-line discount",
      "context": "Discount handling"
    },
    {
      "category": "Closed Periods",
      "rule": "If start date falls in closed period, set to first day outside closed period",
      "context": "Billing and service period start dates"
    },
    {
      "category": "Hourly Rates",
      "rule": "Ignore hourly rate tables and only process listed budget or quota amount as flat price BT",
      "context": "Rate table processing"
    },
    {
      "category": "Default Values",
      "rule": "Default service term is 1 year if none listed",
      "context": "Ops default"
    },
    {
      "category": "Default Values",
      "rule": "Default billing frequency is Monthly if none listed",
      "context": "Ops default"
    },
    {
      "category": "Taxes",
      "rule": "Every tax line item becomes a separate BT",
      "context": "Tax handling"
    }
  ],
  "exceptions": [
    {
      "condition": "Intelligent Demand contracts",
      "exception": "Only 3 possible integration products: Agency Fees (PROGRAM SPEND - Third Party Expenses), Media Spend (Program Spend - Media Spend), Reimbursable Travel (Passthrough Spend - Travel)"
    },
    {
      "condition": "2X contracts",
      "exception": "Many are open-ended without specific contract length"
    },
    {
      "condition": "Shorter BTs like onboarding",
      "exception": "Use listed timeframe and round up according to specific rules"
    },
    {
      "condition": "Contract-specific merchant requests",
      "exception": "May differ by contract (e.g., always back-date invoice date to final day of month)"
    },
    {
      "condition": "Statsig integration items",
      "exception": "Should be labeled as 'Sales'"
    },
    {
      "condition": "Pinata integration items",
      "exception": "Should be labeled as 'Software Subscription Bundle' unless otherwise noted"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item mapping",
      "description": "Specific products and categories vary by merchant (e.g., Intelligent Demand, Statsig, Pinata)",
      "customizable": true
    },
    {
      "element": "Invoice date handling",
      "description": "Some merchants require back-dating to final day of month",
      "customizable": true
    },
    {
      "element": "Post-processing notifications",
      "description": "Notification recipients and timing vary by merchant (e.g., Customer Success team for Messari)",
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos and invoice requirements based on merchant-customer relationships",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "description": "Merchant-specific needs like invoice pro-ration for handling mid-month changes",
      "customizable": true
    },
    {
      "element": "Events processing",
      "description": "Implementation Success team fills post-go-live, varies by merchant",
      "customizable": true
    },
    {
      "element": "Contract terminology",
      "description": "Terms like 'BT' (billing transaction), '2X contracts', merchant phases (Implementation, Active)",
      "customizable": false
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: 2X + Intelligent Demand MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:25:53

### Original Content
```
app gong io call id 4861806357239532146 4 7 call with the team Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills SF as CRM - finance starts when opp marked closed won, manually pulling SOW Use third party solution integrated within Netsuite, continuum billing - a lamer version of suite billing Then build a subscription schedule applicable to that customer based off of the resources that we have on the engagement Then set it up to ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing workflow automation",
    "Revenue recognition and reconciliation processes",
    "Contract management and amendment handling",
    "Integration between CRM (Salesforce) and billing system (NetSuite with Continuum Billing)",
    "Manual intervention points in automated billing cycles"
  ],
  "rules": [
    "Finance process starts when opportunity is marked 'closed won' in Salesforce",
    "SOW (Statement of Work) must be manually pulled to initiate billing",
    "Subscription schedules are built based on engagement resources",
    "First month billing is set up for the full period",
    "Engagement kickoff occurs within two weeks of signature date",
    "First month is pro-rated based on actual start date",
    "Invoices are generated 10 days before the bill date in NetSuite",
    "Revenue reconciliation must occur between Excel workbook and NetSuite before invoice transmission",
    "Manual invoice editing is required when workbook shows pro-rated amount but NetSuite shows full amount",
    "All invoices are transmitted in bulk after completing reconciliation for all clients",
    "Variable/ad hoc work requires delivery team feedback before invoicing",
    "Ad hoc work is invoiced either as line items on recurring invoices or as separate manual invoices",
    "Excel workbook serves as the source of truth for revenue forecasting",
    "Each client has a separate tab in the Excel workbook",
    "Revenue is forecasted by month by SOW across rows"
  ],
  "exceptions": [
    "Contracts are amended frequently when additional services are added",
    "Most contract language is evergreen, but schedules are set a year and a half out",
    "Pro-rated billing applies only to the first month of engagement",
    "Variable input work (ad hoc/project-based) follows different invoicing process than recurring work",
    "Manual invoice creation may be needed for certain ad hoc work instead of adding to recurring invoices"
  ],
  "merchant_specific": [
    "Uses Salesforce as CRM system",
    "Uses NetSuite with Continuum Billing (described as 'a lamer version of suite billing')",
    "Excel workbook as source of truth (specific to this merchant's process)",
    "10-day review period before bill date (timing may vary by merchant)",
    "Two-week kickoff timeline from signature (merchant-specific SLA)",
    "Specific reconciliation workflow between workbook and NetSuite",
    "Bulk transmission approach for invoices at end of month",
    "Delivery team feedback loop for variable work",
    "Merchant temperament noted as 'very friendly and excited about Tabs vision'"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: 2X + Intelligent Demand MIS_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:26:02

### Original Content
```
Will be a great product feedback partner as we launch new features, especially AR agents 3) What are the Tabs features that the key POC cares about Billing and revenue schedule automation from contract (Pandadoc) that then automatically integrates with Netsuite and SF They also have a lot of products and services amendments and adjustments so need Tabs to automatically update invoice start dates based on a trigger from SF or their CS team, pro-rate invoices for mid month and easily add remove pr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and revenue automation integration",
    "Contract-to-invoice workflow automation",
    "Product and service amendment management",
    "Multi-system integration (PandaDoc, NetSuite, Salesforce)",
    "Dynamic invoice adjustments and proration"
  ],
  "rules": [
    "Billing and revenue schedules must be automatically generated from contracts in PandaDoc",
    "Contract data must automatically integrate with NetSuite and Salesforce",
    "Invoice start dates must automatically update based on triggers from Salesforce or CS team",
    "Invoices must be pro-rated for mid-month changes",
    "Products must be easily added or removed based on amendments",
    "Price adjustments must trigger automatic invoice updates",
    "System must handle product and service amendments automatically",
    "System must support automatic adjustments for contract modifications"
  ],
  "exceptions": [
    "Mid-month changes require pro-rated invoicing (special calculation logic)",
    "Manual triggers from CS team can override automated invoice start date updates",
    "Amendment-driven changes may bypass standard billing cycles"
  ],
  "merchant_specific": [
    "Uses PandaDoc as contract management system",
    "Uses NetSuite as financial/ERP system",
    "Uses Salesforce (SF) as CRM and trigger source",
    "Has CS (Customer Success) team that can manually trigger invoice updates",
    "Handles 'a lot of products and services' suggesting complex product catalog",
    "Requires AR (Accounts Receivable) agents functionality",
    "POC (Point of Contact) specifically cares about billing automation features",
    "Willing to be product feedback partner for new features"
  ],
  "confidence_score": 0.85
}
```

---

