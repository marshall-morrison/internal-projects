# Raw LLM Analysis: Merchant Info Sheet - Keen(1)

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 12:20:03

---

## Chunk 1: Merchant Info Sheet - Keen(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:03

### Original Content
```
-Their Invoicing is based on hours worked for payroll, plus their markup -Being really diligent on billing and invoicing is super important - need to receive invoiced amounts on time because they have to process payroll by the 18th of the month so people get paid by the end of the month -All currency is USD today, Europe will eventually be a market for them Billing model SOW, then calendar based billing at net 10-15, all via ACH As they onboard new employees for the company, these employees will...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payroll-based invoicing and billing cycles",
    "Contract processing and billing term (BT) creation",
    "Implementation fees and deposit handling",
    "Recurring fee scheduling and proration",
    "Time-sensitive payment requirements"
  ],
  "rules": [
    "All currency is USD (Europe will be a future market)",
    "Billing model: SOW followed by calendar-based billing at net 10-15 via ACH",
    "Invoices must be received on time for payroll processing by the 18th of the month",
    "Payroll must be processed by 18th so employees are paid by end of month",
    "All billing terms (BTs) go into the same revenue schedule",
    "Default all BTs to 12 months if no end date specified",
    "Monthly recurring billing is standard",
    "Implementation fees are billed upon signature with Net 0 terms",
    "Implementation fee counts as or toward the first month of recurring fees",
    "Implementation fee BT date is the signature date",
    "Recurring fees should be set to 12 months unless contract states otherwise",
    "Recurring invoices start the month AFTER the first full month of billing",
    "Recurring invoices should be scheduled for the 1st of the month",
    "Partial months between start date and end of month must be prorated for first invoice",
    "Each role in contract gets its own BT with unit price per month",
    "Employee rates are based on usage data per employee hire"
  ],
  "exceptions": [
    "Split implementation fees: When implementation fee is split in half, calculate as 1 billing term with 2 recurring payments",
    "Split fee frequency: Estimate months between sign date and start date, round down, use that for frequency",
    "Split fee description: Use '50% Deposit Fee' for split implementation fees",
    "Standard implementation fee description: Use 'First Deposit Fee' for full implementation fees",
    "Recurring fee start timing: If role starts on August 26, first recurring invoice is October 1 (skipping the partial first month and the first full month)",
    "Proration amendments: Required for partial month between start date and end of month before recurring invoices begin"
  ],
  "merchant_specific": [
    "Payroll processing deadline of 18th of month",
    "End-of-month employee payment schedule",
    "Specific markup model based on hours worked for payroll",
    "Employee onboarding with set rates per hire",
    "Contract structure with roles and unit prices per month",
    "ACH as payment method",
    "Net 10-15 payment terms for calendar-based billing",
    "Net 0 terms for implementation fees",
    "12-month default billing term duration",
    "Revenue schedule consolidation (all BTs in same schedule)",
    "Specific proration logic for start dates mid-month",
    "Future expansion to Europe market"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Keen(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:06

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
      "rule": "Onboarding follows a structured timeline: Demo → Scoping → MSA Signature → Kick Off → Go Live",
      "type": "process",
      "explicit": true
    },
    {
      "rule": "First invoices are sent in the month of Go Live (July in this case)",
      "type": "operational",
      "explicit": true
    },
    {
      "rule": "Implementation should avoid expensive systems that merchant cannot grow into",
      "type": "business_constraint",
      "explicit": true
    },
    {
      "rule": "Key decision maker (Jake) must be identified and engaged as primary POC",
      "type": "relationship_management",
      "explicit": true
    },
    {
      "rule": "Secondary stakeholders (Martin) should be identified for platform usage involvement",
      "type": "relationship_management",
      "explicit": true
    },
    {
      "rule": "Merchant temperament assessment should be documented during onboarding",
      "type": "relationship_management",
      "explicit": true
    },
    {
      "rule": "Current client count and growth trajectory should be tracked",
      "type": "business_intelligence",
      "explicit": true
    },
    {
      "rule": "No existing systems in place indicates need for foundational setup",
      "type": "implementation",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date field exists conditionally ([If Exists])",
      "condition": "Only applicable if merchant opts out of certain features or services"
    },
    {
      "exception": "This merchant has no existing systems, requiring ground-up implementation",
      "condition": "Differs from typical merchants who may have legacy systems to integrate"
    },
    {
      "exception": "Merchant is at very early stage (first two clients, first invoices in July)",
      "condition": "May require different support level or feature set than established businesses"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key Personnel Names",
      "customization_needed": "Jake Petersen (CEO, Co-Founder) and Martin (Co-Founder) - specific to this merchant"
    },
    {
      "element": "Business Model",
      "customization_needed": "Offshore recruiting firm with focus on Colombia and South Africa talent pools"
    },
    {
      "element": "Target Customer Base",
      "customization_needed": "Hotel chains, e-commerce companies, and other brands"
    },
    {
      "element": "Timeline Dates",
      "customization_needed": "All dates (Demo: Jun 13, MSA: Jun 26, Go Live: Jul 1, 2024) are merchant-specific"
    },
    {
      "element": "GTM POC and Implementation POC",
      "customization_needed": "Fields present but not populated - would be specific to each merchant"
    },
    {
      "element": "ERP and Tax Integration",
      "customization_needed": "Fields present but not populated - integration requirements vary by merchant"
    },
    {
      "element": "Growth Stage",
      "customization_needed": "First two clients with more onboarding soon - early-stage specific"
    },
    {
      "element": "Merchant Temperament Description",
      "customization_needed": "Great entrepreneurs excited to work with a very cool startup - relationship-specific"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Keen(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:18

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
    "Prorated amount calculation: (total amount for role / total business days M-F in month) × business days in billing period",
    "Business days are defined as Monday through Friday only",
    "BTs must be dated for the first full month of service AFTER the start date, not the contract sign date",
    "BT net payment terms must match the original contract's recurring invoice terms",
    "BTs should be processed on the amendment record in Garage",
    "Revenue schedule period should equal the BT period (e.g., 9/1 for 1 month)",
    "BT titles should use role names only, excluding any individual names added to role titles",
    "All prorated amounts should be rounded to .00 decimal (whole dollars)",
    "Same net payment terms as contract must be used to ensure BT appears on correct invoice"
  ],
  "exceptions": [
    "If start date falls within the month of the invoice date: create a negative BT for days NOT worked and prorate accordingly",
    "If a role cannot be staffed in time and is NOT in the confirmed start dates list: do not create a prorated BT for that amendment",
    "For unstaffed roles: when amendment arrives in month X with start date in month Y, date BT for month Y+1; if received in same month as start date, date for following month",
    "If start date is after the first day of the first recurring invoice: adjust the original BT to the next month"
  ],
  "merchant_specific": [
    "Reference to 'Garage' system for processing BT records",
    "Use of 'BT' (Billing Transaction) terminology - may be company-specific",
    "Reference to 'Lancer amendment' as an example case",
    "Rev schedule terminology and structure",
    "Amendment processing workflow specific to this organization",
    "Email-based communication protocol for start date confirmations",
    "Contract structure with recurring invoices and amendments"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - Keen(1)_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:19

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
    "Integration Items and Labeling Requirements",
    "Post-Processing Communication Protocols"
  ],
  "rules": [
    "When start date differs from recurring invoice start date, update the role's BT to align with the later start date and decrease period count by 1",
    "For contracts with 50% deposit fee clause, create a one-off BT for half the amount on amendment date with net 0 terms",
    "If Balance Due = 0, no invoice is needed for that period",
    "Credit (from Deposit) should be applied to invoices as negative BT",
    "Ongoing Item Changes section requires updates to existing recurring BTs starting in following months",
    "Default Service Term if none listed: 1 Year",
    "Default Net Payment Terms if none listed: 0 (net zero)",
    "Default Billing Frequency if none listed: Monthly",
    "Default tax handling: every tax line item becomes a BT",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Invoice date should be shown on top of section with net terms matching original contract",
    "Balance Due represents total balance for the invoice date listed"
  ],
  "exceptions": [
    "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice date to final day of month)",
    "Pinata integration items have default labeling 'unless otherwise noted by Merchant'",
    "Special memos may be required for certain invoices based on merchant-customer relationship",
    "Invoice changes may occur due to specific merchant-customer relationships",
    "Integration item field should be left blank until merchant adds specific item"
  ],
  "merchant_specific": [
    "Business days table reference (mentioned but not shown in chunk)",
    "Merchant-specific contract processing variations",
    "Customer Success notification requirements (example: Azmat Aziz for Messari)",
    "Merchant phase-specific notifications (Implementation vs Active phase)",
    "Internal merchant channel communication requirements",
    "Merchant-specific integration item labeling (Statsig, Pinata examples)",
    "Events billing processing requirements (if applicable to merchant)",
    "Special customer information and invoice memo requirements",
    "Feature requests tracking per merchant"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 5: Merchant Info Sheet - Keen(1)_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:20:32

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
    "Brand Marketing and eCommerce Director full-time rate is $3,800 per period (or $7,600-$11,600 monthly)",
    "Billing periods can be split within a month for role or schedule changes",
    "Balance due is calculated as: charges minus credits/payments",
    "Credits from deposits roll forward to subsequent invoices until exhausted",
    "Monthly costs vary based on employee schedule changes (part-time vs full-time)"
  ],
  "exceptions": [
    "October 2024: Brand Marketing Director only worked 20 hours/week for partial month (10/15-10/31)",
    "November 2024: Brand Marketing Director transitioned from part-time (11/1-11/14) to full-time (11/15-11/30) mid-month",
    "October balance due was $0 due to sufficient deposit credit ($10,850 paid from deposit)",
    "November had $4,950 credit remaining from deposit applied to reduce balance",
    "Supply Chain Director and Social Media Manager had deposits paid but no ongoing monthly charges shown in the billing periods"
  ],
  "merchant_specific": [
    "Employee names: Nooran (Product Development Manager), Jean-Pierre (Brand Marketing and eCommerce Director)",
    "Specific role titles: Product Development Manager, Brand Marketing and eCommerce Director, Supply Chain Director, Social Media and Community Manager",
    "Deposit amounts vary by role: $4,000, $3,800, $3,425, $2,250, $1,750",
    "Business day counts tracked per month (ranging from 18-22 days)",
    "Reference to video meeting: 'ngcj632hqqz3adz0-jake-benjamin-meeting-june-13-2024'",
    "Billing start date: August 5, 2024",
    "Service period extends through December 2025"
  ],
  "confidence_score": 0.75
}
```

---

