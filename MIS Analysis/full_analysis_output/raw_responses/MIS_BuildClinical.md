# Raw LLM Analysis: MIS BuildClinical

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:47:42

---

## Chunk 1: MIS BuildClinical_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:47:42

### Original Content
```
Merchant Demo date: Scoping start date: MSA Signature Date: Oct 1, 2024 Onboarding Kick Off Date: Oct 3, 2024 [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary (AE to fill) Summary of what company does Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are we solving Why are they buy...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Contract Processing and Subscription Management",
    "Billing Model and Revenue Recognition",
    "Bulk Processing Workflow for Implementation"
  ],
  "rules": [
    "Slack notification must be sent after any contract or amendment is processed",
    "Start date shifts the entire schedule by default unless service period is explicitly increased",
    "For bulk processing, all contracts must be found in a designated sheet",
    "A sub-customer must be created for each contract during bulk processing",
    "Sub-customer naming convention: Study ID (mapped from contract file name)",
    "Parent customer matching: Use last name of doctor from file name and QBO custom name if not auto-matched",
    "All contracts require at least 2 touch points during processing (original document + subsequent amendments)",
    "BT Rev Schedule must be created with Start date, End date, and Price from contract/sheet",
    "Revenue schedule BT start date must match the Start Date in sheet",
    "Revenue schedule BT end date must match the End Date in sheet",
    "Contracts are laid out as monthly price, billed monthly"
  ],
  "exceptions": [
    "Service period can be increased instead of shifted if explicitly specified (exception to default start date shift behavior)",
    "Parent customer auto-matching may fail, requiring manual matching via doctor's last name",
    "Opt out clause may exist - if present, specific merchant requirements must be tracked to prevent exercise of clause"
  ],
  "merchant_specific": [
    "Demo date, Scoping start date, MSA Signature Date, Onboarding Kick Off Date, Opt Out Date, Go Live Date",
    "GTM POC and Implementation POC assignments",
    "ERP system type",
    "Tax Integration requirements",
    "Key personnel: Accountant, CFO, Customer service rep, Account Receivable POC, Billing POC",
    "Company summary and goals (North star)",
    "Pain points being solved and purchase rationale",
    "Opt out clause terms and conditions",
    "Unique customer creation process requirements",
    "Billing model specifics",
    "Contract structure and breakdown",
    "One-off merchant-specific considerations",
    "Study ID mapping methodology",
    "Contract file naming conventions"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS BuildClinical_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:47:44

### Original Content
```
However, for initial processing, we will only process the first invoice This is because the recurring billing does not start immediately when the contract is signed Steps to process: Create 1 non-recurring BT for the monthly amount in the contract Item Name: BuildClinical Platform Description: none Integration item: BuildClinical Platform Rev schedule start date: 3 months after signature date, for 1 month duration BT Start date: Date of receipt, non-recurring for 0 months  NOTE that the rev sche...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Initial contract processing and billing setup",
    "IRB approval amendment and recurring billing commencement",
    "Revenue schedule and billing term management",
    "Study pause amendments and fee processing",
    "Timing differences between revenue recognition and billing dates"
  ],
  "rules": [
    "Initial processing only handles the first invoice, not recurring billing",
    "Create 1 non-recurring BT for monthly amount with Item Name 'BuildClinical Platform'",
    "Rev schedule start date is 3 months after signature date for 1 month duration",
    "BT start date is date of receipt, non-recurring for 0 months",
    "Rev schedule start date and BT start dates are different for initial processing",
    "Number of invoices for initial processing is 1",
    "Bill on start date for initial processing",
    "Discounts should not be included in BT, only process total amount",
    "Do not process extra charges (campaign materials, professional services, pause fee) until amendment is received",
    "All contracts will receive IRB Approval amendment at some point (typically 1-6 months from execution)",
    "For IRB approval: create new rev schedule BT for recurring monthly billing",
    "IRB approval BT start date is amendment start date plus 1 month",
    "Rev schedule dates are number of months in contract minus 1",
    "First month is already accounted for in the deposit",
    "If service period not in contract, check PO at end of contract PDF",
    "If no specific service term, default to 12 months",
    "Number of invoices equals number of months specified in contract/PO or default to 12",
    "Billing setting for IRB approval: Bill in advance, due on start of period",
    "Discounts not included in BT for IRB approval amendments"
  ],
  "exceptions": [
    "Rev schedule start date and BT start dates differ in initial processing (3 months after signature vs date of receipt)",
    "Service term may be found in PO instead of contract if not specified in contract",
    "Default to 12 months if no service term is specified in contract or PO",
    "First month billing is handled differently (already accounted for in deposit) requiring minus 1 calculation",
    "Pause study amendments require multiple processing steps and special handling (reference to LOOM VIDEO and example)",
    "Additional charges outlined in contracts are not processed initially but wait for specific amendments"
  ],
  "merchant_specific": [
    "BuildClinical Platform - specific product/service name used as Item Name and Integration item",
    "IRB Approval - industry-specific milestone (clinical research/trials)",
    "Study pause functionality - specific to clinical trial management",
    "Deposit structure tied to first month of service",
    "Campaign materials and professional services as add-on charges",
    "Tabs - appears to be internal system or team name receiving amendments via email",
    "BT (likely Billing Template or Billing Transaction) - internal terminology",
    "Rev schedule - internal revenue schedule terminology",
    "Amendment-based billing trigger system"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: MIS BuildClinical_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:48:02

### Original Content
```
The amendment will be in the BODY of the email The email will have clear information about the pause: Customer, Study ID (this will be the sub-customer), Pause start date,   of months pause pause end date and pause fee if different from the standard rate of  300 To process this, a few things need to happen Extend the existing rev schedule BT This will go under the current subscription BT, which was processed with the last amendment for the customer, the recurring BT rev schedule needs to be exte...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Subscription pause processing and revenue schedule extension",
    "Pause fee calculation and billing for pauses over 30 days",
    "Mid-contract subscription price changes and prorated adjustments",
    "Revenue schedule and billing transaction (BT) management",
    "Invoice timing and missed invoice calculation during pauses"
  ],
  "rules": [
    "Pause amendment information must be in email body with: Customer, Study ID (sub-customer), pause start date, number of months pause, pause end date, and pause fee",
    "Revenue schedule BT must be extended by number of invoices missed during pause period, not necessarily equal to pause duration in months",
    "Pause fee BT is only created if pause exceeds 30 days",
    "Default pause fee is $300 unless specified otherwise in amendment",
    "Pause fee BT starts 30 days from pause start date and ends at pause end date",
    "Pause fee frequency = number of months of pause minus 1",
    "For non-whole number month pauses, always round up to next whole number when identifying occurrences",
    "Pause fee item name: 'Pause Fee', Integration Item: 'Pause Fee'",
    "For subscription price updates: end current rev schedule and BT so no invoices go out after effective date",
    "New subscription BT starts next month on same day as previous cadence with new price",
    "New subscription rev schedule starts on effective date month (may be prior to BT) and lasts 0 months",
    "Price decrease: create negative BT equal to prorated difference for days in previous month",
    "Price increase: create positive BT equal to prorated difference for days in previous month",
    "Updated subscription price integration item: 'BuildClinical Platform'",
    "Proration calculation: compare old price prorated vs new price prorated for overlapping days, calculate difference"
  ],
  "exceptions": [
    "Perfect situation: Even month pause (e.g., 3 months) extends rev schedule by exact pause duration",
    "Imperfect situation: Pause duration doesn't align with invoice dates - extension based on actual missed invoices, not pause duration",
    "Example: 2.5 month pause with invoices on 10th results in 3 months extension (June 5-Aug 20, missing June 10, July 10, Aug 10)",
    "Example: 2.5 month pause with invoices on 3rd results in 2 months extension (June 5-Aug 20, missing only July 3, Aug 3)",
    "Pauses under 30 days: no pause fee BT created",
    "Pauses over 30 days: pause fee BT required with specific calculation rules",
    "Non-whole month pauses: round up for occurrence calculation (e.g., 4.5 months = 4 occurrences, 6 months = 5 occurrences)",
    "Subscription price changes: different processes for price increases vs decreases"
  ],
  "merchant_specific": [
    "Study ID as sub-customer identifier (suggests clinical/research industry)",
    "BuildClinical Platform as integration item (specific platform name)",
    "Default $300 pause fee (may vary by merchant contract)",
    "Invoice day of month varies by customer (3rd, 10th, 24th shown in examples)",
    "Subscription price points vary widely ($1121-$3900 in examples)",
    "Amendment documentation process and email format",
    "Specific revenue schedule extension methodology based on invoice timing",
    "Monthly billing cadence (may differ for other merchants)",
    "Pause fee frequency calculation formula (months - 1)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: MIS BuildClinical_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:48:04

### Original Content
```
13 Rev sched: 12 18 for 0 months Other possible amendments include: These will be less common Manually re-activate study Move pause end date to the date specified in this amendment This means: Pause Fee ends (if applicable) Resumed rev schedule BT dates are adjusted to start on the new pause end date Rev sched BT ends dates are adjusted accordingly Subscription renewal extension Extend current recurring BT based on extended months specified in amendment Early termination End rev schedule and BT ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Amendment Processing and Types",
    "Subscription Schedule Management",
    "Billing and Revenue Schedule Adjustments",
    "Default Configuration Settings",
    "Operational Workflow and Communications"
  ],
  "rules": [
    {
      "rule": "Manual re-activation requires moving pause end date to amendment-specified date, which ends pause fee and resumes revenue schedule",
      "category": "amendment_processing"
    },
    {
      "rule": "Early termination calculated end date must be as close to termination date as possible but AFTER the termination date",
      "category": "early_termination",
      "example": "Early term date 4/1/24, Current schedule 9/20/24-9/29/25, New calc end date 4/19/25 (7 months of service)"
    },
    {
      "rule": "Apply credit to study by adding negative BT with specified amount to next recurring monthly invoice",
      "category": "credits"
    },
    {
      "rule": "Increase/decrease monthly subscription requires adjusting BT for recurring monthly amount to new specified price in amendment",
      "category": "subscription_changes"
    },
    {
      "rule": "Default Service Term if none listed is 1 Year",
      "category": "defaults"
    },
    {
      "rule": "Default Net Payment Terms if none listed is 30 days",
      "category": "defaults"
    },
    {
      "rule": "Default Billing Frequency if none listed is Monthly",
      "category": "defaults"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billing Transaction)",
      "category": "defaults"
    },
    {
      "rule": "Initially ignore pause extra services as outlined, process when amendment is received",
      "category": "processing_sequence"
    },
    {
      "rule": "Pause amendments received via email with information in email body including: Customer, Study ID (sub-customer), Pause start date, number of months pause, pause end date, and pause fee",
      "category": "pause_processing"
    },
    {
      "rule": "Pause processing requires ending existing rev schedule BT and reducing amount of months in revenue schedule",
      "category": "pause_processing"
    },
    {
      "rule": "Subscription renewal extension adjusts current recurring BT based on extended months specified in amendment",
      "category": "amendment_processing"
    },
    {
      "rule": "BT dates are adjusted to start on new pause end date when manually re-activating study",
      "category": "reactivation"
    },
    {
      "rule": "Rev sched BT end dates are adjusted accordingly when pause end date changes",
      "category": "schedule_adjustments"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific processing instructions that may differ by contract (e.g., always back-date invoice date to final day of the month)",
      "note": "Currently listed as 'none' but framework exists for merchant-specific variations"
    },
    {
      "exception": "Less common amendments include: manual re-activation, subscription renewal extension, early termination, credit application, and subscription amount changes",
      "context": "These are contrasted with standard amendments"
    },
    {
      "exception": "Special memos certain invoices require based on merchant-customer relationship",
      "context": "Customer-specific handling"
    },
    {
      "exception": "Integration items may have specific labeling rules (e.g., Statsig labeled as 'Sales', Pinata as 'Software Subscription Bundle')",
      "context": "Integration-specific processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Specifics processing things the merchant has requested that may differ by contract",
      "customizable": true,
      "example": "Back-dating invoice date to final day of the month"
    },
    {
      "element": "Integration Items Processing instructions",
      "customizable": true,
      "note": "Different merchants may have different integration labeling requirements"
    },
    {
      "element": "Post Processing Communications requirements",
      "customizable": true,
      "fields": ["Who needs to be notified", "Where to notify", "When to notify", "Merchant Phase"]
    },
    {
      "element": "Customer Information section",
      "customizable": true,
      "note": "Important information on specific customers of the merchant"
    },
    {
      "element": "Events Processing instructions",
      "customizable": true,
      "note": "To be filled by Implementation Success team"
    },
    {
      "element": "Feature Requests section",
      "customizable": true,
      "fields": ["What is it", "Why it's important", "Urgency"]
    },
    {
      "element": "Pause fee amount",
      "customizable": true,
      "default": "$300",
      "note": "Can differ from standard rate per amendment"
    },
    {
      "element": "Study ID as sub-customer identifier",
      "terminology": "merchant_specific"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 5: MIS BuildClinical_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:48:16

### Original Content
```
Based on this date, you can deduce when the last bill went out, and what service period it was for The end date of the rev schedule should equal the end date of the service period of the last invoice Example: Rev schedule start 2 4 Pause start 7 26 The last bill before the pause was 7 3, for the service period 8 3-9 3 (because these are set as bill in advance, due start of period) So, the rev schedule should end 9 3 Reduce the rev schedule to the amount of months of service from the start date t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue schedule adjustments for service pauses",
    "Prorated billing and credits for partial billing periods",
    "Pause fee calculation and billing for extended pauses",
    "Subscription resumption after pause periods",
    "Bill timing coordination with service periods"
  ],
  "rules": [
    "Revenue schedule end date must equal the end date of the service period of the last invoice",
    "Reduce revenue schedule to the number of months of service from start date to pause date (round up for partial months)",
    "End billing template (BT) by changing number of invoices to match the months of service calculated for revenue schedule",
    "Create prorated negative BT as credit for partial month if pause occurs mid-billing period",
    "Proration calculation formula: (Monthly rate / 30) × number of days left in the month",
    "If pause is over 30 days, create BT for pause fee",
    "If pause is under 30 days, no new revenue schedule is needed",
    "For pauses over 30 days, create recurring BT for pause fee until pause end date",
    "Default pause fee is $300 unless specified otherwise in amendment",
    "Pause fee BT starts 30 days from pause start date and ends at pause end date",
    "Pause fee frequency: number of months of pause minus 1 (with rounding rules applied)",
    "When resuming subscription, create new BT starting on pause end date",
    "Resumed subscription revenue schedule should cover remaining months of contract term (default 12 months if not specified)",
    "If prorated credit was created at pause start, create corresponding prorated BT for final partial month at end of contract term",
    "For non-whole number of pause months, always round up to next whole number when identifying occurrences",
    "Services are billed in advance, due at start of period"
  ],
  "exceptions": [
    "Pauses under 30 days do not require new revenue schedule or pause fees",
    "Pauses over 30 days require recurring pause fee billing",
    "Pause fee can be different from $300 default if specified in amendment",
    "If pause duration is non-whole number of months, round up for occurrence calculation",
    "Prorated credit at pause start requires corresponding prorated charge at contract end"
  ],
  "merchant_specific": [
    "Contract term length (defaults to 12 months but may vary)",
    "Monthly rate amount (used in proration calculations)",
    "Pause fee amount (default $300 but can be customized per amendment)",
    "Integration item names (e.g., 'BuildClinical Platform', 'Credit', 'Pause')",
    "Item names and descriptions in billing templates",
    "Merchant temperament and relationship information",
    "Key POC (buyer/decision maker) identification",
    "Tabs features that key POC cares about",
    "Implementation spreadsheets and billing methodology",
    "Service period dates and billing cycles"
  ],
  "confidence_score": 0.85
}
```

---

