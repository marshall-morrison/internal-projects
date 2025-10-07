# Raw LLM Analysis: LILT MIS

## Document Overview
- **Total Chunks Analyzed**: 6
- **Analysis Timestamp**: 2025-10-02 10:44:49

---

## Chunk 1: LILT MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:44:49

### Original Content
```
Merchant Demo date: Oct 24, 2024 Scoping start date: Oct 17, 2024 MSA Signature Date: Dec 18, 2024 Onboarding Kick Off Date: Dec 23, 2024 [If Exists] Opt Out Date: June 1 Go Live Date: Mar 28, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Company summary (AE to fill) Translation services Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are we solving Why are they buying Tabs Currently the process is very manual and only one pe...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Merchant Onboarding Requirements and Goals",
    "Customer Account Management and Assignment",
    "Contract Processing and Instance Routing",
    "Opt-Out Clause Conditions and Success Criteria"
  ],
  "rules": [
    {
      "rule": "DO NOT CREATE CUSTOMERS for Lilt - if customers do not exist, flag for review",
      "category": "customer_management",
      "explicit": true
    },
    {
      "rule": "Contracts uploaded to both Lilt, Inc and Lilt Technologies instances should only be processed in ONE instance",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "To determine correct instance for contract processing, check the top left corner of the contract and match it to the instance name",
      "category": "contract_routing",
      "explicit": true
    },
    {
      "rule": "Merchant requires two separate accounts - one for domestic operations and one for Ireland",
      "category": "account_setup",
      "explicit": true
    },
    {
      "rule": "Implementation must be fully complete with all promised features delivered to avoid opt-out clause exercise",
      "category": "success_criteria",
      "explicit": true
    },
    {
      "rule": "Process needs to be accessible to wider team (not just one person)",
      "category": "operational_requirements",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Unique customer creation process - requires dual account structure (domestic + Ireland)",
      "condition": "Merchant-specific requirement"
    },
    {
      "exception": "Contract duplication across instances - same contract uploaded to both Lilt, Inc and Lilt Technologies",
      "condition": "Only process in the instance matching the contract header"
    },
    {
      "exception": "Opt-out clause exists with specific conditions",
      "condition": "Merchant can opt out if not fully implemented with promised features by June 1"
    },
    {
      "exception": "Manual customer flagging required instead of automatic creation",
      "condition": "Applies specifically to Lilt - do not auto-create customers"
    }
  ],
  "merchant_specific": [
    {
      "element": "Timeline dates",
      "details": "Demo: Oct 24, 2024; Scoping: Oct 17, 2024; MSA: Dec 18, 2024; Kickoff: Dec 23, 2024; Opt Out: June 1; Go Live: Mar 28, 2025",
      "customizable": true
    },
    {
      "element": "Merchant pain points",
      "details": "Manual process, single-person dependency, need for wider team functionality",
      "customizable": true
    },
    {
      "element": "Account structure",
      "details": "Two accounts required - one for here, one for Ireland",
      "customizable": true
    },
    {
      "element": "Instance names",
      "details": "Lilt, Inc and Lilt Technologies - specific to this merchant",
      "customizable": true
    },
    {
      "element": "Opt-out conditions",
      "details": "Full implementation and feature delivery required",
      "customizable": true
    },
    {
      "element": "Customer assignment protocol",
      "details": "Flag instead of create for non-existent customers",
      "customizable": true
    },
    {
      "element": "Integration requirements",
      "details": "ERP, Tax Integration, SF integration, Usage API mentioned but not detailed",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: LILT MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:44:49

### Original Content
```
) process If it is NOT in the correct instance (i e Lilt, Inc in Lilt Technologies) please DELETE Before deleting check to see if it was deleted in the other instance If it was deleted and you think it shouldn t have been, create a ticket before you delete yours We will need to reupload to the correct instance Contracts shouldn t be deleted in both instances EVER Other things to note for Customers: When assigning the Customer If the customer names aren t exact or close to exact (for example, the...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Instance Management and Deletion Protocol",
    "Customer Identification and Mapping",
    "Billing Terms Classification (Flat vs Usage)",
    "Contract Processing and Data Entry Requirements",
    "Offline Usage Billing Term Setup"
  ],
  "rules": [
    "Before deleting a contract, verify if it was deleted in the other instance",
    "Contracts should never be deleted in both instances simultaneously",
    "Create a ticket before deleting if a contract was deleted in another instance but shouldn't have been",
    "Customer names must be exact or close to exact matches when assigning",
    "Customer address in garage must match customer address in contract",
    "If address doesn't match and uncertain, create a ticket",
    "Snap contracts should be marked as 'processed no BTs' due to complex billing requirements",
    "Jabra or GN Store Nord A S must use customer ID: bfa7fa33-5b30-4094-a1e4-12c10cc6e732",
    "Brandwatch 1st Floor location should be assigned to Brandwatch - Runtime Collective Limited Sucursal en Espana",
    "Anixter customer should be mapped to Wesco",
    "ALPHA INTERNATIONAL USA IP, LLC should be assigned to AI USA with customer ID: 2cce45ca-dcfc-45a4-8f27-c47fa6ae255d",
    "Every contract requires an Offline Usage BT",
    "Offline Usage BT unit price should be 1",
    "Offline Usage BT event to track should be 'Offline'",
    "Offline Usage BT integration item should be SERV-TRANS-OFFLINE",
    "Offline Usage BT billing time should be 'last of period'",
    "For Flat BTs, use total price column as the total price",
    "Flat BTs are identified by total price column, Annual/Year units, or one-time payment descriptions",
    "Usage BTs are charged per individual action (e.g., per word translated)",
    "Ignore Subtotal column for Usage BTs with Unit Price column",
    "Use additional terms section to find service start date, months of service, billing start date, and number of periods"
  ],
  "exceptions": [
    "If contract is in incorrect instance (e.g., Lilt, Inc vs Lilt Technologies), delete after verification",
    "Snap contracts are not billed through Tabs - mark as processed no BTs",
    "If no usage BTs exist on contract, Offline Usage BT service start date should use first of the month that contract start date is in",
    "If no usage BTs exist, Offline Usage BT should use contract length and billing frequency (monthly or semi-monthly)",
    "If contract date falls in a closed period, move the start date to the first month outside of the closed period",
    "Flat BTs can exist without total price column if unit is Annual/Year or description indicates one-time payment"
  ],
  "merchant_specific": [
    "Instance names: 'Lilt, Inc' and 'Lilt Technologies'",
    "Customer-specific mappings: Snap, Jabra, GN Store Nord A S, Brandwatch, Anixter/Wesco, ALPHA INTERNATIONAL USA IP/AI USA",
    "Specific customer IDs for mapping purposes",
    "Integration item code: SERV-TRANS-OFFLINE",
    "Reference to 'garage' system for customer address verification",
    "Reference to 'Tabs' billing system",
    "Closed period concept for financial processing",
    "Ticket creation system for escalation and issue resolution",
    "SKU-based connector access products",
    "Translation services with per-word billing"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: LILT MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:03

### Original Content
```
SERV-DTP-HR However, if there isn t a close match that isn t an inactive item, leave blank DO NOT use items that have  Inactive  in them Check additional terms for net payment terms Additional examples of flat billing terms for reference: Processing Usage BTs Use item column as the item name Use the Description column as the item description Exception: for Translation Services ( Fuzzy Bands ; screenshot below), the description will be the column header For example, in the screenshot below, for t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Configuration",
    "Item and SKU Selection Rules",
    "Translation Services and Fuzzy Band Processing",
    "Usage-Based Billing Setup and Timing",
    "Project Management and Premier Support Handling"
  ],
  "rules": [
    "Do not use items marked as 'Inactive' under any circumstances",
    "Use item column as the item name and Description column as the item description",
    "Usage Event should be the SKU for most cases",
    "Integration Item should use the SKU (e.g., SERV-TRANS items use 'SERV-TRANS: Verified Translation')",
    "If exact SKU match not found, find the closest match but never use inactive items",
    "Use unit price for total price in usage BTs",
    "Set billing date to the FIRST of the month for all usage BTs",
    "Select 'LAST OF PERIOD' for billing timing on all usage BTs",
    "Use additional terms section to find service start date, months of service, and number of periods",
    "For Project Management or Premier Support BTs: make it a UNIT BT with total price = 1 regardless of listed price",
    "Never use SERV-PRJCT as an event or integration item for any BTs",
    "Each individual column with a price in Fuzzy Bands becomes its own BT",
    "Check additional terms for net payment terms"
  ],
  "exceptions": [
    "Translation Services (Fuzzy Bands): description will be the column header instead of Description column (e.g., 'Exact 101', 'Fuzzy 95-99')",
    "Translation Services with SERV-TRANS-1, SERV-TRANS-2: these are unique events and must be selected if listed (e.g., 'SERV-TRANS-1-101' for Exact 101 fuzzy band BT)",
    "Project Management: use SERV-PRMR as the EVENT and SERV-PRJCT as the INTEGRATION Item (not the individual SKU)",
    "Premier Support: see Project Management exception rules",
    "If contract date falls in a closed period: move the start date to the first month outside of the closed period (e.g., if books closed through Jan, use Feb 1 start date)",
    "Contracts with both Premier Support (SERV-PRMR) AND Project Management: must track in Google sheet and notify via Slack channel 'lilt-processing-workflows'"
  ],
  "merchant_specific": [
    "SKU naming conventions (SERV-TRANS, SERV-PRMR, SERV-PRJCT, SERV-DTP-HR)",
    "Fuzzy Band terminology and structure specific to translation services",
    "Google sheet tracking requirement for 'Customers with SERV-PRMR' (Customer ID, Customer Name, SERV-PRMR as decimal, Merchant name)",
    "Slack channel notification requirement: 'lilt-processing-workflows'",
    "Closed period policies and month-end billing timing preferences",
    "Translation service pricing structure (Exact 101, Fuzzy 95-99 bands)",
    "Integration item naming patterns and SKU structure"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: LILT MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:04

### Original Content
```
For example, if the books are closed through January, make the start date Feb 1 for the BTs Use quantity column for quantity Use item column for item name Description: First: Put the SKU Second: Put the description column For example:  LILT-PLATFORM - Includes access to: Performance Analytics, Workflow Management, Linguistic Data Storage and Management, Fine-tuning Model Builder 3rd party integrations  Frequency: For Annual   1 year flat BTs, use YEAR If the unit column was 2 years for the flat ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Configuration and Frequency Rules",
    "SKU and Item Description Formatting Standards",
    "Invoice Terms Hierarchy and Precedence",
    "Integration Item Mapping and SKU Matching",
    "Document Section Cross-referencing (Additional Terms, Upfront Fees)"
  ],
  "rules": [
    "Start date must be set after books close date (e.g., if closed through January, use Feb 1)",
    "Use quantity column for quantity field in BT creation",
    "Use item column for item name in BT creation",
    "Description field format: First line = SKU, Second line = description column content",
    "For annual 1-year flat BTs, frequency = 'YEAR'",
    "For multi-year flat BTs, frequency = '[X] YEAR(S)' where X is the unit column value",
    "Flat BTs do NOT follow Invoice Terms section by default",
    "Flat BTs should use upfront payment structure unless explicitly overridden",
    "If no frequency is mentioned for flat BT in unit or additional terms, default to 'NONE'",
    "Ignore Invoice Terms section cadence (semi-monthly, monthly) for flat BTs unless it explicitly calls out flat BTs",
    "Integration items should use the exact SKU from the BT",
    "When exact SKU match not found for integration item, find the closest similar SKU"
  ],
  "exceptions": [
    "Check 'Additional Terms' section - if it specifies different invoice cadence for flat BT section, follow that instead of default rules",
    "Example exception: 'quarterly basis for Platform Pricing line items' overrides annual frequency even if BT says Annual/Year",
    "Check 'Upfront Fees' section if available - may contain additional billing frequency information",
    "Invoice Terms section DOES apply to flat BTs if it explicitly mentions a flat BTs section (with screenshot reference)",
    "Section headers determine which BTs are referenced in additional terms (e.g., 'connector' references correspond to 'Connector Pricing' header BTs)"
  ],
  "merchant_specific": [
    "Books close date varies by merchant (determines BT start date)",
    "SKU naming conventions (examples: LILT-PLATFORM, CONN-NS, SERV-DTP)",
    "Product-specific descriptions (e.g., 'Includes access to: Performance Analytics, Workflow Management')",
    "Section header names may vary (Platform Pricing, Connector Pricing, Upfront Fees)",
    "Integration item naming format: '[SKU]: [Product Name]' (e.g., 'CONN-NS: NewStore Connector')",
    "Invoice Terms section structure and terminology",
    "Additional Terms section content and references",
    "Unit column terminology and values"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: LILT MIS_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:18

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urgency Rewatch Calls (AE Implementat...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Communication and Notification Requirements",
    "Billing and Invoicing Complexity (Usage-based, Multi-service, Tiered)",
    "Customer Relationship Management and Key Contacts",
    "Feature Requirements and Product Roadmap Expectations",
    "Revenue Operations and System Integrations"
  ],
  "rules": [
    "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
    "Merchant bills usage in arrears (not upfront)",
    "Platform fees are charged as part of billing structure",
    "Multi-service invoicing must support both usage-based and flat software fee components",
    "Tier-based discounts must be applied to invoicing",
    "Invoice splitting capability required for parent-child architecture to bill multiple cost centers",
    "Government milestone-based invoicing must be supported",
    "CSV export functionality required for revenue recognition purposes",
    "Usage data must be ingested into the system",
    "Commitment consumption tracking is expected (roadmap item treated as current capability)",
    "Minimum true-ups must be tracked for SKUs with and without commits"
  ],
  "exceptions": [
    "Certain invoices require special memos based on merchant-customer relationship",
    "Invoice changes may be needed due to specific merchant-customer relationships",
    "Ops International Team should ignore certain note sections (marked explicitly)",
    "Roadmap items are perceived by merchant as existing capabilities requiring customization rather than net-new features",
    "Invoice audit process required specifically for government-related billing"
  ],
  "merchant_specific": [
    "Key decision makers: Mason Hanson (Head of Business Operations) and Brian Preti (Controller)",
    "Merchant temperament characterized as 'incredible they love us'",
    "Specific stakeholder roster including roles: Program Manager, CFO, Controller, Data Analyst, Sr Manager Rev Ops, Data Analytics Systems Integrations, Accounting Manager, Sr Accountant",
    "Custom billing requirements between Salesforce CPQ and Salesforce integrations",
    "Parent-child cost center architecture specific to this merchant's organizational structure",
    "Government milestone-based invoicing suggests public sector or government contractor status",
    "Expectation management issue: merchant believes roadmap features are already available",
    "Usage-based billing model with platform fees specific to merchant's pricing structure"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 6: LILT MIS_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:45:22

### Original Content
```
In the below red screenshot, there will be 7 BTs The event for each BT will be the SKU    -    the number in the price column For example: for the first  Exact 101  column, the BT will have a price of  0 14 per unit and the event will be  SERV-TRANS-101 You still need to create BTs if they are  0 ( Repetitions ) Exceptions for event type rules: For Fuzzy 84-94 column, the event will be  SERV-TRANS-85-94  NOT 84-94 This is true for all 84-94 fuzzy bands The event will need to use 85-94 For the  R...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Business Transaction (BT) Creation Rules",
    "Reserved Capacity and Prepaid Reserved Capacity Handling",
    "SKU and Event Naming Conventions",
    "Contract Processing Exclusions and Exceptions",
    "Data Tracking and Overlap Management"
  ],
  "rules": [
    "Create 7 BTs based on screenshot columns with event format: SKU - price column number",
    "Create BTs even when price is 0 (Repetitions)",
    "For Fuzzy 84-94 column, event must be SERV-TRANS-85-94 (applies to all 84-94 fuzzy bands)",
    "For Repetitions column, event format is SKU - Repetitions (e.g., SERV-TRANS-Repetitions)",
    "For New 0-74 column, event format is SKU - New Words (e.g., SERV-TRANS-New Words)",
    "Usage BTs with total price, unit price, and qty should be treated as Usage BTs",
    "For PREPAID Reserved Capacity: create FLAT BT for upfront amount, select 'Has Threshold', select 'Full service term' for Threshold Minimum Period",
    "For regular Reserved Capacity (no Prepaid): no BT creation needed, select 'Has Minimum'",
    "For single type of Reserved Capacity: select Usage AI 'Has usage requirements'",
    "Integration item must match correct capacity type (Prepaid Reserved Capacity or Reserved Capacity)",
    "Select both 'Charges Overages' and 'True up to meet minimum' for Reserved Capacity",
    "For BOTH Prepaid and regular Reserved Capacity: select 'Apply usage model sequentially', start with Prepaid then add Reserved",
    "Track all Reserved Capacity contracts in Google sheet with Customer ID, Customer Name, and amounts",
    "Ignore all BTs under 'AI Package' section",
    "Do not process BTs under 'ADDITIONAL OPTIONAL LICENSING AND SERVICES' section",
    "Process only default/baseline amounts when multiple options exist for same BT",
    "Ignore subtotals in fuzzy band BTs, process only usage BTs",
    "Check for overlapping BTs before finishing processing by searching customer ID in garage",
    "Flag overlapping BTs but continue processing the contract"
  ],
  "exceptions": [
    "Fuzzy 84-94 bands use 85-94 in event name (NOT 84-94)",
    "Repetitions column uses 'Repetitions' suffix instead of number",
    "New 0-74 column uses 'New Words' suffix instead of number",
    "Regular Reserved Capacity (without Prepaid) does not require BT creation",
    "Ignore specific SKUs: INST-CL-OVER, INST-CL-SUB, MT-BULK-CL, MT-BULK-OP",
    "Ignore SKUs with multiple monthly volume columns",
    "Ignore contracts not on Lilt paper (mark as 'Process no BTs')",
    "When both PRC and RC exist, enter amounts separately on respective sheets",
    "Process only initial term base year column when multiple options present",
    "Ignore subtotals in fuzzy band BTs"
  ],
  "merchant_specific": [
    "SKU prefix 'SERV-TRANS' appears to be merchant-specific (Lilt)",
    "Specific column names: Exact 101, Fuzzy 84-94, Repetitions, New 0-74",
    "Google sheet tracking system for Reserved Capacity customers",
    "Garage system for checking processed contracts and overlaps",
    "Lilt paper format requirement for contract processing",
    "AI Package section specific to this merchant",
    "Customer ID format and lookup system",
    "Integration item naming conventions",
    "Specific SKU exclusion list (INST-CL-OVER, INST-CL-SUB, MT-BULK-CL, MT-BULK-OP)",
    "Implementation Success team and Ops Team notification requirements"
  ],
  "confidence_score": 0.88
}
```

---

