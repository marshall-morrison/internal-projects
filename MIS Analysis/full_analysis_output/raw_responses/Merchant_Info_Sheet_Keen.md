# Raw LLM Analysis: Merchant Info Sheet - Keen

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 09:52:20

---

## Chunk 1: Merchant Info Sheet - Keen_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:52:20

### Original Content
```
-Their Invoicing is based on hours worked for payroll, plus their markup -Being really diligent on billing and invoicing is super important - need to receive invoiced amounts on time because they have to process payroll by the 18th of the month so people get paid by the end of the month -All currency is USD today, Europe will eventually be a market for them Billing model SOW, then calendar based billing at net 10-15, all via ACH As they onboard new employees for the company, these employees will...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payroll-based invoicing and billing timing constraints",
    "Contract processing and billing term creation workflow",
    "Implementation fee handling and deposit structures",
    "Recurring fee scheduling and proration logic",
    "Employee onboarding as usage-based billing trigger"
  ],
  "rules": [
    "All currency is USD (Europe planned for future)",
    "Billing model: SOW followed by calendar-based billing at Net 10-15 via ACH",
    "Invoices must be received on time for payroll processing by the 18th of the month",
    "Payroll must be completed by end of month",
    "Default all billing terms to 12 months if no end date specified",
    "All billing terms go into the same revenue schedule",
    "Implementation fees are billed upon signature with Net 0 terms",
    "Implementation fee counts as or toward the first month of recurring fees",
    "Implementation fee billing term date is the signature date",
    "Each contract role/item gets its own billing term",
    "Recurring fees start the month AFTER the first full month of billing",
    "Recurring invoices are scheduled for the 1st of the month",
    "Number of periods for recurring fees defaults to 12 months unless specified",
    "Partial months between start date and month-end must be prorated",
    "Employee hires trigger usage-based billing at set rates"
  ],
  "exceptions": [
    "Split implementation fees: When implementation fee is split in half, create 1 billing term with 2 recurring payments",
    "Split fee calculation: Estimate months between sign date and start date, round down, use for frequency (e.g., 1 month frequency for July 6 sign to August 20 start)",
    "Split fee description: Use '50% Deposit Fee' instead of standard 'First Deposit Fee'",
    "Recurring fee start date exception: If role starts on August 26, first recurring invoice is October 1 (skips September)",
    "Proration amendments: Required for partial month between start date and end of month before recurring invoices begin"
  ],
  "merchant_specific": [
    "Payroll processing deadline of 18th of month",
    "Employee onboarding as billing trigger with set rates per employee",
    "SOW-based contract structure",
    "Net 10-15 payment terms",
    "ACH as exclusive payment method",
    "Contract structure with roles table and unit prices per month",
    "Implementation fee terminology ('First Deposit Fee', '50% Deposit Fee')",
    "Specific proration logic for start dates mid-month",
    "Revenue schedule consolidation requirement",
    "12-month default billing term length"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Keen_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:52:22

### Original Content
```
Merchant Demo date: Jun 13, 2024 Scoping start date: Jun 27, 2024 MSA Signature Date: Jun 26, 2024 Onboarding Kick Off Date: Jul 1, 2024 [If Exists] Opt Out Date: Go Live Date: Jul 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Jake Petersen - Co-Founder   CEO Martin - Co-Founder Company summary Dedicated Offshore recruiting firm, hiring dedicated talent for your company from talent pools in Colombia and South Africa They work with brands (hotel chains, e-comme...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Business Model and Service Offering (Offshore Recruiting)",
    "System Implementation and Growth Strategy",
    "Stakeholder Identification and Relationship Management",
    "Early-Stage Business Requirements"
  ],
  "rules": [
    {
      "rule": "Onboarding process follows sequential milestones: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "First invoices are sent out in July, coinciding with Go Live date",
      "type": "operational",
      "explicit": true
    },
    {
      "rule": "Merchant prefers avoiding expensive systems that exceed growth capacity",
      "type": "business_constraint",
      "explicit": true
    },
    {
      "rule": "Key decision maker (Jake) must be identified as key POC during onboarding",
      "type": "stakeholder_management",
      "explicit": true
    },
    {
      "rule": "AE must document merchant temperament, key POC/decision maker, and feature priorities",
      "type": "documentation_requirement",
      "explicit": true
    },
    {
      "rule": "Implementation should align with merchant's current client base and growth trajectory",
      "type": "implementation_strategy",
      "implicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date field exists conditionally ([If Exists] notation)",
      "condition": "Only applicable if merchant opts out"
    },
    {
      "exception": "No systems currently in place - greenfield implementation",
      "condition": "Merchant has no existing infrastructure to integrate with"
    },
    {
      "exception": "ERP and Tax Integration fields are present but empty",
      "condition": "May not be applicable for all merchants or at this stage"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key personnel names and roles (Jake Petersen - Co-Founder/CEO, Martin - Co-Founder)",
      "customization_needed": "Must be captured for each merchant"
    },
    {
      "element": "Company summary and business model description",
      "customization_needed": "Unique to each merchant's industry and service offering"
    },
    {
      "element": "North star goals and current state assessment",
      "customization_needed": "Varies by merchant maturity and objectives"
    },
    {
      "element": "Merchant temperament assessment",
      "customization_needed": "Subjective evaluation per merchant relationship"
    },
    {
      "element": "Feature priorities and use cases",
      "customization_needed": "Based on merchant's specific business needs"
    },
    {
      "element": "Timeline dates (Demo, Scoping, MSA, Go Live)",
      "customization_needed": "Unique to each merchant's onboarding schedule"
    },
    {
      "element": "GTM POC and Implementation POC assignments",
      "customization_needed": "Assigned based on merchant needs and internal resources"
    },
    {
      "element": "Current client count and growth projections",
      "customization_needed": "Specific to merchant's business stage"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Keen_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:52:34

### Original Content
```
However, the start dates in the contract are target start dates The true start dates will be communicated to us via email The email will include: Customer List of roles Start dates for those roles This email might also include salary updates This email might have information in the body of the email as well as an attachment Please refer to both when processing Customer information is best found via sender email address From this information, we need to generate a BT for each role reflective of t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Prorated billing calculations for mid-month start dates",
    "BT (Billing Transaction) generation and timing rules",
    "Email-based contract amendment processing",
    "Revenue schedule alignment with billing periods",
    "Contract amendment handling for delayed role staffing"
  ],
  "rules": [
    "Contract start dates are targets; actual start dates come via email",
    "Email communications may contain information in both body and attachments - both must be reviewed",
    "Customer identification should be done via sender email address",
    "Proration calculation: (Total amount for role / Total business days M-F in month) × Business days worked in billing period",
    "BTs must be dated for the first full month of service AFTER the start date, not the sign date",
    "BT net payment terms must match the recurring invoices already processed for that contract",
    "BTs should be processed on the amendment record in Garage",
    "Revenue schedule period should equal the BT period (e.g., 9/1 for 1 month)",
    "BT titles should use role names only, excluding any individual names added to role titles in amendments",
    "All prorated amounts should be rounded to .00 decimal (whole dollars)",
    "Use same net payment terms as contract to ensure BT appears on correct invoice",
    "If start date is after first day of first recurring invoice, adjust original BT to next month"
  ],
  "exceptions": [
    "If start date falls within the month of invoice date: create negative BT for days NOT worked and prorate accordingly",
    "If a role cannot be staffed in time (not in confirmed start dates list): Do NOT add as prorated BT for current amendment",
    "For unstaffed roles: Date the prorated BT based on when amendment is received (if received in August with 9/10 start, date for Sept 1; if received in September, date for October)",
    "Email may include salary updates in addition to start date information"
  ],
  "merchant_specific": [
    "Reference to 'Garage' system for processing BTs on amendment records",
    "Use of 'BT' (Billing Transaction) terminology",
    "Reference to 'Lancer amendment' as example case",
    "Business days defined as Monday-Friday only",
    "Specific date format conventions (e.g., '8 19' for August 19)",
    "Rev schedule terminology and system",
    "Amendment processing workflow and record structure"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Keen_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:52:41

### Original Content
```
Ex: Start date October 10, recurring invoices start October 1 Update this role s BT to start November 1 and decrease   of period by 1 If this contract had a 50  deposit fee clause, then a one-off BT for half of the amount will need to be created for the date of amendment with net 0 terms Sample Template for processing amendments Body of the email will have invoice totals, but the sheet attached will show details Date on top of the section is the invoice date, net terms should still match the net...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Amendment Processing",
    "Recurring Invoice and Billing Template (BT) Management",
    "Default Values and Operational Standards",
    "Credit and Deposit Handling",
    "Merchant-Specific Customization and Communication Protocols"
  ],
  "rules": [
    {
      "rule": "When start date is after recurring invoice start date, update BT to start the following month and decrease period by 1",
      "example": "Start date October 10, recurring invoices start October 1 - Update BT to start November 1 and decrease period by 1"
    },
    {
      "rule": "For contracts with 50% deposit fee clause, create one-off BT for half the amount on amendment date with net 0 terms",
      "context": "Amendment processing"
    },
    {
      "rule": "If Balance Due = 0, no invoice is needed for that period",
      "context": "Invoice generation"
    },
    {
      "rule": "Credit (from Deposit) should be applied to the invoice as negative BT",
      "context": "Credit application"
    },
    {
      "rule": "Ongoing Item Changes listed at bottom require updates to existing recurring BTs starting in following months",
      "context": "Recurring billing updates"
    },
    {
      "rule": "Default Service Term: 1 Year (if none listed)",
      "type": "default"
    },
    {
      "rule": "Default Net Payment Terms: 0 (if none listed)",
      "type": "default"
    },
    {
      "rule": "Default Billing Frequency: Monthly (if none listed)",
      "type": "default"
    },
    {
      "rule": "Default Tax Handling: Every tax line item becomes a BT (if none listed)",
      "type": "default"
    },
    {
      "rule": "Invoice date appears on top of section, net terms should match original contract terms",
      "context": "Invoice formatting"
    },
    {
      "rule": "Business days per month should be referenced from provided table",
      "context": "Scheduling"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific processing requests may differ by contract",
      "example": "Always back-date invoice date to final day of the month"
    },
    {
      "exception": "Credit Left has no invoice ramifications, shown only to indicate credit affecting future invoices",
      "context": "Credit tracking"
    },
    {
      "exception": "Integration items may have specific labeling requirements",
      "examples": [
        "All Statsig integration items labeled as 'Sales'",
        "All Pinata integration items labeled as 'Software Subscription Bundle' unless otherwise noted"
      ]
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "context": "Customer-specific requirements"
    },
    {
      "exception": "Items marked to ignore in contracts should be excluded from processing",
      "context": "Contract processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration Items Processing",
      "customization": "Merchant-specific labeling rules for integration items (e.g., Statsig, Pinata)",
      "variability": "high"
    },
    {
      "element": "Post Processing Communications",
      "customization": "Notification requirements vary by merchant (who, where, when)",
      "example": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when Active contracts processed"
    },
    {
      "element": "Customer Information",
      "customization": "Special handling for specific customers, custom memos, relationship-based invoice changes",
      "variability": "high"
    },
    {
      "element": "Contract-specific processing preferences",
      "customization": "May include custom invoice dating, specific terms, or unique billing arrangements",
      "variability": "medium"
    },
    {
      "element": "Events Processing",
      "customization": "Merchant-specific events billing information when necessary",
      "variability": "medium"
    },
    {
      "element": "Amendment Template Structure",
      "customization": "Email body shows totals, attached sheet shows details with specific sections",
      "variability": "low"
    },
    {
      "element": "Merchant Phase Tracking",
      "customization": "Implementation vs Active phase determines communication timing",
      "variability": "low"
    }
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: Merchant Info Sheet - Keen_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:52:49

### Original Content
```
com video ngcj632hqqz3adz0-jake-benjamin-meeting-june-13-2024 October 1, 2024 Product Development Manager (10 1 - 10 31)    4,000 Brand Marketing and eCommerce Director (10 15 - 10 31) 20 hours per week    1,900 October Total    5,900 Paid (from Deposit)    10,850 Balance Due    0 Credit Left    4,950 November 1, 2024 Product Development Manager (11 1 - 11 30)    4,000 Brand Marketing and eCommerce Director (11 1 - 11 14) 20 hours per week    1,900 Brand Marketing and eCommerce Director (11 15 -...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Employee staffing and role assignments with time-based transitions",
    "Deposit-based payment structure with credits and balances",
    "Variable work schedules (part-time to full-time transitions)",
    "Monthly billing cycles with prorated periods",
    "Business day tracking across multiple months"
  ],
  "rules": [
    "50% deposit fee required upfront for each employee role",
    "Deposits create credits that can be applied to future invoices",
    "Product Development Manager has a fixed monthly rate of $4,000",
    "Brand Marketing and eCommerce Director part-time (20 hours/week) rate is $1,900 per period",
    "Brand Marketing and eCommerce Director full-time rate is $3,800 per period",
    "Billing periods can be split within a month (e.g., 10/1-10/31 split into two periods)",
    "Credits from deposits are applied before calculating balance due",
    "Monthly costs are tracked separately for each employee role",
    "Payment status must be tracked (PAID vs Balance Due)",
    "Business days are counted and tracked for each month"
  ],
  "exceptions": [
    "October 2024: Balance due is $0 because payment was covered entirely from deposit credit ($10,850 available, only $5,900 needed)",
    "November 2024: Brand Marketing and eCommerce Director transitions from part-time (20 hrs/week) to full-time mid-month (11/15)",
    "Prorated billing periods: Directors can have split billing within same month with different rates",
    "Credit carryover: Unused deposit credit ($4,950) carries forward to next billing period",
    "Variable monthly business days: Ranges from 18 to 22 days depending on the month"
  ],
  "merchant_specific": [
    "Employee names: Nooran (Product Development Manager), Jaen-Pierre (Brand Marketing and eCommerce Director)",
    "Specific role titles: Supply Chain Director, Social Media and Community Manager, Product Development Manager, Brand Marketing and eCommerce Director",
    "Custom deposit amounts: $3,425 (Supply Chain Director and Brand Marketing Director), $2,250 (Social Media Manager), $1,750 (Product Development Manager)",
    "Specific date ranges and transition dates (e.g., 10/15-10/31, 11/15-11/30)",
    "Reference to meeting video: 'ngcj632hqqz3adz0-jake-benjamin-meeting-june-13-2024'",
    "Monthly rate variations specific to this merchant's staffing needs",
    "Business day calendar specific to merchant's operational calendar (August 2024 - December 2025)"
  ],
  "confidence_score": 0.75
}
```

---

