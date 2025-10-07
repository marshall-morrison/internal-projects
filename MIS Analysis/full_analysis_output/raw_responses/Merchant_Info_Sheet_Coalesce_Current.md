# Raw LLM Analysis: Merchant Info Sheet - Coalesce (Current)

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:58:39

---

## Chunk 1: Merchant Info Sheet - Coalesce (Current)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:58:39

### Original Content
```
Merchant Coalesce (v2 implementation with NetSuite) GTM POC: Implementation POC: ERP: Scoping start date: Jul 2, 2024 Implementation Completed Date (Go live date): Aug 21, 2024 MSA Signature Date: Feb 9, 2024 Tax Integration: Key people at Merchant CFO: Nick Decesare (nick decesare coalesce io) Buyer and Product Partner Senior Fiance: Tianna Tugulavioa (tianna coalesce io) Finance: Sylvia Hoang (sylvia hoang coalesce io) Company summary: Coalesce helps you transform data your way, by making data...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Order Management",
    "Customer Creation and Currency Handling",
    "Revenue Schedule Creation for Multi-Year Contracts",
    "Billing Terms and Contract Structure",
    "Service Start Date Determination"
  ],
  "rules": [
    {
      "rule": "Do not process Purchase Orders",
      "category": "Contract Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Only process the Order Form sent",
      "category": "Contract Processing",
      "specificity": "explicit"
    },
    {
      "rule": "If no Order Form found, flag to Ashni Walia",
      "category": "Contract Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Add the PO# from the purchase order into the first invoice",
      "category": "Invoice Processing",
      "specificity": "explicit"
    },
    {
      "rule": "If an existing customer exists, select the existing customer in the garage drop down",
      "category": "Customer Creation",
      "specificity": "explicit"
    },
    {
      "rule": "If US and USD - leave the toggle to show USD",
      "category": "Customer Creation - Currency",
      "specificity": "explicit"
    },
    {
      "rule": "If an international currency is listed (usually in bold next to the total) - select that currency in the dropdown",
      "category": "Customer Creation - Currency",
      "specificity": "explicit"
    },
    {
      "rule": "Use the last signature date for contract signature date (ignore the docusign audit page on the last page of the contract)",
      "category": "Contract Date Processing",
      "specificity": "explicit"
    },
    {
      "rule": "Populate contract signature date in the Key Terms 'Start Date' column",
      "category": "Contract Date Processing",
      "specificity": "explicit"
    },
    {
      "rule": "The instructions in the Merchant email supersede the MIS instructions",
      "category": "Instruction Priority",
      "specificity": "explicit"
    },
    {
      "rule": "For each multiple year line item with the same item name and quantity, create 3 revenue schedules with the same length and start date",
      "category": "Revenue Schedule Creation",
      "specificity": "explicit"
    },
    {
      "rule": "Unless pricing is the same for each year - then you can consolidate into one BT",
      "category": "Revenue Schedule Creation",
      "specificity": "explicit"
    },
    {
      "rule": "Service Start Date will be the subscription start date if explicitly mentioned",
      "category": "Service Start Date",
      "specificity": "explicit"
    },
    {
      "rule": "If subscription start date is not mentioned, default to the last signature date",
      "category": "Service Start Date",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Consolidate into one BT if pricing is the same for each year in multi-year contracts",
      "condition": "When pricing remains constant across all years",
      "impact": "Changes revenue schedule creation from multiple to single"
    },
    {
      "exception": "Merchant email instructions supersede MIS instructions",
      "condition": "When there is conflict between merchant email and standard MIS instructions",
      "impact": "Prioritize merchant-specific guidance"
    },
    {
      "exception": "International currency handling differs from USD handling",
      "condition": "When contract uses non-USD currency",
      "impact": "Requires currency selection in dropdown instead of default USD toggle"
    },
    {
      "exception": "Service Start Date defaults to signature date only when subscription start date is not explicitly mentioned",
      "condition": "When subscription start date is absent from contract",
      "impact": "Fallback date determination logic"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name: Coalesce",
      "type": "Identity"
    },
    {
      "element": "ERP System: NetSuite (v2 implementation)",
      "type": "Technical Infrastructure"
    },
    {
      "element": "Implementation dates: Scoping Jul 2, 2024; Go-live Aug 21, 2024; MSA Feb 9, 2024",
      "type": "Timeline"
    },
    {
      "element": "Key contacts: CFO Nick Decesare, Senior Finance Tianna Tugulavioa, Finance Sylvia Hoang",
      "type": "Stakeholders"
    },
    {
      "element": "Billing model: Mostly annual, multi-year contracts",
      "type": "Business Model"
    },
    {
      "element": "Contract structure: SaaS",
      "type": "Business Model"
    },
    {
      "element": "Special characteristic: International contracts",
      "type": "Business Scope"
    },
    {
      "element": "Company business: Data transformation platform",
      "type": "Industry Context"
    },
    {
      "element": "Example line items: Platform Fee, Silver Package",
      "type": "Product/Service Terminology"
    },
    {
      "element": "Escalation contact: Ashni Walia (for missing Order Forms)",
      "type": "Process Contact"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Coalesce (Current)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:58:43

### Original Content
```
Start date: Year 1 start date Month of service will be 36 Item Item Name: Process Item name as displayed in the contract If discount line item, name should just say discount (write as a negative BT) Item Description: For discounting, please specify the items that it s been discounted for in the description (e g , Platform, Additional User License, etc) Please add discounts in line item going forward Quantity When billing platform seats, show 1 Quantity for  Coalesce Platform  When billing all ot...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing start date determination",
    "Line item processing and quantity handling",
    "Renewal contract processing and autorenewal",
    "Revenue recognition periods and frequencies",
    "Professional services and integration items handling"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Start Date",
      "description": "Start date defaults to Year 1 start date with Month of service at 36"
    },
    {
      "rule_id": "R2",
      "category": "Line Items",
      "description": "Item names should be processed as displayed in contract"
    },
    {
      "rule_id": "R3",
      "category": "Line Items",
      "description": "Discount line items should be named 'discount' and written as negative BT"
    },
    {
      "rule_id": "R4",
      "category": "Line Items",
      "description": "Discount descriptions must specify which items are being discounted (e.g., Platform, Additional User License)"
    },
    {
      "rule_id": "R5",
      "category": "Quantity",
      "description": "When billing platform seats for Coalesce Platform, show quantity as 1"
    },
    {
      "rule_id": "R6",
      "category": "Quantity",
      "description": "For all other line items, show actual quantity in BT's quantity section"
    },
    {
      "rule_id": "R7",
      "category": "Billing Start Date - New Contract",
      "description": "Default to the last signature date unless explicitly stated otherwise"
    },
    {
      "rule_id": "R8",
      "category": "Billing Start Date - New Contract",
      "description": "Alternative rule: use the earliest of service date or signature date when specified"
    },
    {
      "rule_id": "R9",
      "category": "Billing Start Date - Renewals",
      "description": "Invoice date will always be written in renewal contract"
    },
    {
      "rule_id": "R10",
      "category": "Billing Start Date - Renewals",
      "description": "Renewals billing starts on the day after the first term ends"
    },
    {
      "rule_id": "R11",
      "category": "Renewals",
      "description": "If renewal date is missing, make best effort based on previous billing date"
    },
    {
      "rule_id": "R12",
      "category": "Renewals",
      "description": "If autorenewal is included in contract, generate an invoice"
    },
    {
      "rule_id": "R13",
      "category": "Renewals",
      "description": "Check email body in garage for every contract to identify renewals, especially if contract PDF has dates from previous year"
    },
    {
      "rule_id": "R14",
      "category": "Renewals",
      "description": "Process renewal terms on the original contract instance"
    },
    {
      "rule_id": "R15",
      "category": "Renewals",
      "description": "Coalesce may send renewal requests in email body with original contract attached, noting product and renewal period dates"
    },
    {
      "rule_id": "R16",
      "category": "Revenue Recognition",
      "description": "Period and frequency settings impact Revenue Recognition on NetSuite instance and must not be deviated from"
    },
    {
      "rule_id": "R17",
      "category": "Professional Services",
      "description": "Use 3 month integration by default for professional services"
    },
    {
      "rule_id": "R18",
      "category": "Professional Services",
      "description": "Professional services and jumpstart should be in separate revenue schedule with service term of 3 months by default"
    },
    {
      "rule_id": "R19",
      "category": "Professional Services",
      "description": "Billing period should match the service term"
    },
    {
      "rule_id": "R20",
      "category": "Professional Services",
      "description": "If service term starts after the 20th of month, revenue schedule should start on the 1st of the following month"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "N-Able example where invoice date is explicitly stated to be different from signature dates",
      "condition": "When invoice date is explicitly stated in contract"
    },
    {
      "exception_id": "E2",
      "description": "Use earliest of service date or signature date when this rule is specified",
      "condition": "When contract specifies to use earliest date"
    },
    {
      "exception_id": "E3",
      "description": "Use 6 month integration instead of default 3 months",
      "condition": "When explicitly stated in contract for professional services"
    },
    {
      "exception_id": "E4",
      "description": "Revenue schedule starts on 1st of following month",
      "condition": "When service term starts after the 20th of the month"
    },
    {
      "exception_id": "E5",
      "description": "Renewal information may be in email body rather than contract PDF",
      "condition": "When Coalesce sends renewal request via email with original contract attached"
    }
  ],
  "merchant_specific": [
    {
      "element": "Coalesce Platform",
      "type": "Product Name",
      "description": "Specific product requiring quantity of 1 for platform seats"
    },
    {
      "element": "Coalesce Contracts",
      "type": "Contract Type",
      "description": "Specific contract type with defined processing rules"
    },
    {
      "element": "NetSuite instance",
      "type": "System Integration",
      "description": "Revenue Recognition system that period and frequency settings impact"
    },
    {
      "element": "Garage",
      "type": "Tool/System",
      "description": "System used to view email body and contract links"
    },
    {
      "element": "BT (Billing Transaction)",
      "type": "Terminology",
      "description": "Internal term for billing transaction or line item"
    },
    {
      "element": "N-Able",
      "type": "Example Merchant",
      "description": "Referenced as example case with different invoice date handling"
    },
    {
      "element": "Annual/Quarterly/Monthly Contracts",
      "type": "Contract Periods",
      "description": "Different contract frequency types requiring specific processing (details not provided in chunk)"
    },
    {
      "element": "Professional Services and Jumpstart",
      "type": "Service Types",
      "description": "Specific service offerings requiring separate revenue schedule"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Coalesce (Current)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:58:57

### Original Content
```
com video he7pbtaup7tv6k6z-coalesce-tabs-overview-february-28-2024 https: tabs rewatch com video 7t66meowpi7ict5w-nick-decesare-and-ali-hussain-february-2-2024 Nick is very bullish on Tabs Wanted to do a 3-year contract Believes in us and the roadmap He d be a great advisor Tianna has been the most hands-on with NetSuite building and integrations Sylvia is new and was hire as of Jul 22, 2024 Tabs   Coalesce - Netsuite Implementation Periods   Frequency   No of invoice 1 year   1   1 YEAR   1 2 y...
```

### LLM Analysis Response
```json
{
  "themes": [
    "NetSuite Implementation and Integration",
    "Contract Pricing Structures and Billing Periods",
    "Coalesce Platform Licensing and User Management",
    "Professional Services and Support Packages",
    "Item Mapping and Product Catalog Configuration"
  ],
  "rules": [
    "Contract periods are offered in 1-year, 2-year, and 3-year terms",
    "Annual billing generates 1 invoice per year for each contract year",
    "Quarterly billing generates 4 invoices per year (3-month frequency)",
    "Monthly billing generates 12 invoices per year (1-month frequency)",
    "Number of invoices scales with contract length (e.g., 3-year quarterly = 12 total invoices)",
    "Platform licenses can be categorized as core (Developer License, User License) and additional licenses",
    "Professional Services are offered in 3-month and 6-month durations",
    "Jumpstart packages include Basic and Blue Square variants",
    "Reseller margin is tracked as 'Net Referral Fee Adjustment'",
    "Support packages are tiered (Silver, Gold, Private Support Link)",
    "Additional user licenses are tracked separately from base platform licenses"
  ],
  "exceptions": [
    "Nick DeCesare requested a non-standard 3-year contract due to high confidence in product",
    "Sylvia is noted as a new hire (as of July 22, 2024), suggesting potential learning curve considerations",
    "Tianna has specialized hands-on experience with NetSuite building and integrations",
    "Multiple naming conventions exist for similar items (e.g., 'Additional Coalesce User', 'Additional User License', 'Additional Coalesce Non Core User' all map to platform licenses)"
  ],
  "merchant_specific": [
    "Team member names and roles (Nick, Tianna, Sylvia) indicate specific client contacts",
    "Reference to 'Tabs' as the merchant/client name",
    "NetSuite as the specific ERP system being implemented",
    "Coalesce platform as the specific product being sold",
    "Item naming conventions may vary by merchant (multiple variations for similar products)",
    "Package naming (Jumpstart Basic, Blue Square, Silver, Gold) may be customizable",
    "Billing frequency preferences may vary by merchant relationship strength",
    "Video documentation links suggest client-specific training materials"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Merchant Info Sheet - Coalesce (Current)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:58:58

### Original Content
```
Ongoing Services For billing contact name, default on all to ([Company Name] AP Dept) No need to process rev share agreements For any items that net to  0 in charges after discounts, pls make sure to add BTs Anything on contract, should be a BT as the customer has purchased that item, possibly with a discount (up to 100 ) If quantity is equal to 0 then you can skip adding it as a billing term Check for PO number Add PO number if a PO document has been sent or if listed in the contract itself Via...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Terms (BT) Creation and Management",
    "Invoice Processing and PO Number Handling",
    "Contract Processing Workflow",
    "Communication Protocols and Notifications",
    "Special Pricing Structures (Discounts, Reseller Fees, Revenue Share)"
  ],
  "rules": [
    {
      "rule": "Default billing contact name to '[Company Name] AP Dept' for all ongoing services",
      "category": "Contact Information"
    },
    {
      "rule": "Do not process revenue share agreements",
      "category": "Contract Exclusions"
    },
    {
      "rule": "Add billing terms (BTs) for items that net to $0 after discounts",
      "category": "Billing Terms"
    },
    {
      "rule": "Any item on contract should be a BT, even with up to 100% discount",
      "category": "Billing Terms"
    },
    {
      "rule": "Skip adding BT if quantity equals 0",
      "category": "Billing Terms"
    },
    {
      "rule": "Check for and add PO number from PO document or contract itself",
      "category": "Purchase Orders"
    },
    {
      "rule": "Add PO number to the first invoice via invoices tab in Garage",
      "category": "Purchase Orders"
    },
    {
      "rule": "PO billing schedule supersedes the contract MSA",
      "category": "Billing Priority"
    },
    {
      "rule": "For reseller fees: input subtotal as one BT and reseller fee as second BT with negative value",
      "category": "Reseller Fee Processing"
    },
    {
      "rule": "Send Slack-bot message only for the 1st invoice in series, not future invoices",
      "category": "Communications"
    },
    {
      "rule": "Use invoices tab in Garage once a coalesce contract has been processed and reviewed",
      "category": "Post-Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Items with quantity = 0 should be skipped (no BT added)",
      "condition": "Quantity equals zero"
    },
    {
      "exception": "Items netting to $0 after discounts still require BTs",
      "condition": "Net charge is zero but item exists on contract"
    },
    {
      "exception": "Revenue share agreements are excluded from processing",
      "condition": "Agreement type is revenue share"
    },
    {
      "exception": "Multi-year contracts should only trigger Slack message for first invoice year",
      "condition": "Contract spans multiple years with recurring invoices",
      "example": "3-year contract with annual invoices: message only for year 1"
    },
    {
      "exception": "PO billing schedule takes precedence over contract MSA terms",
      "condition": "Both PO and MSA exist"
    }
  ],
  "merchant_specific": [
    {
      "element": "[Company Name] AP Dept",
      "type": "Variable placeholder for merchant-specific company name",
      "customization_needed": true
    },
    {
      "element": "Customer Information section",
      "type": "Merchant-specific customer details and relationships",
      "customization_needed": true,
      "description": "Important information on specific customers, special memos, invoice changes due to merchant-customer relationship"
    },
    {
      "element": "Garage system",
      "type": "Platform/tool reference",
      "customization_needed": false,
      "description": "Appears to be standard invoicing/contract management platform"
    },
    {
      "element": "Coalesce contract",
      "type": "Contract type terminology",
      "customization_needed": false,
      "description": "Specific contract processing workflow"
    },
    {
      "element": "Reseller fee percentage",
      "type": "Variable pricing structure",
      "customization_needed": true,
      "description": "Example shows 30% but may vary by merchant"
    },
    {
      "element": "Slack-bot notifications",
      "type": "Communication channel",
      "customization_needed": true,
      "description": "May vary based on merchant's communication preferences"
    }
  ],
  "confidence_score": 0.82
}
```

---

