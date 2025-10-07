# Raw LLM Analysis: Merchant Info Sheet - ServiceUp

## Document Overview
- **Total Chunks Analyzed**: 6
- **Analysis Timestamp**: 2025-10-02 10:03:34

---

## Chunk 1: Merchant Info Sheet - ServiceUp_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:03:34

### Original Content
```
Faterdenvermazonalanaus t ServiceUp Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Feb 7, 2024 Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: Ariel ERP: Tax Integration: ƒ Key people at Merchant Accountant: Caitlyn Mendenhall,(caitlyn serviceup com_) VP of Finance: David Holtzman (david serviceup com) Customer service rep who is really involved: Unknown Account Receivable POC: Unknown Billing POC: Unknown (Likely Caitlyn) etc Company ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "Fleet Repair Platform Business Model and Billing Workflow",
    "Contract and Document Processing Rules (MSAs and Repair Orders)",
    "Key Stakeholder Identification and Roles",
    "System Integration and AR Automation"
  ],
  "rules": [
    "All customer creation comes from contracts with no repair order",
    "If the RO does not match a customer, flag to GS (likely Garage ServiceUp) for approval",
    "ROs are sent from ServiceUp system to Tabs for processing",
    "Tabs processes ROs based on rules set in MIS (Merchant Information System)",
    "Processed ROs sync from Tabs to QBO (QuickBooks Online)",
    "Invoices with 'Bill Merchant' setting enabled are not sent directly to customers (AP portal or other preferences)",
    "Invoices are generated once repair shop sends totals to ServiceUp",
    "Renee Rojas sends all invoices daily",
    "MSAs must include: Payment terms, Service Term, and Recurring fees (if applicable)",
    "MSAs should ignore: Discounts, Credits, Commission structures, and State based fees (these are handled in ROs)",
    "ROs must include: Customer name, Date, Billing line items, Location (if applicable), Tax (if applicable), and RO number"
  ],
  "exceptions": [
    "Some customers operate in different states requiring customer sub-customer model",
    "Some invoices are not sent directly to customers based on 'Bill Merchant' setting and customer preferences (AP portal)",
    "Discounts are often applied to certain customers (handled at RO level, not MSA level)",
    "Recurring fees are only applicable to some customers",
    "Tax and Location fields in ROs are conditional (if applicable)"
  ],
  "merchant_specific": [
    "ServiceUp operates a fleet repair coordination platform with vehicle pick-up, repair, and drop-off services",
    "ServiceUp takes a spread between charges to fleet owners and repair shop costs",
    "High volume of documents processed weekly",
    "Uses Bill.com for remitting payments back to repair shops (potential future use of remittances feature)",
    "Document types: MSAs (Master Service Agreements) and ROs (Repair Orders)",
    "Key terminology: 'RO' (Repair Order), 'Bill Merchant' setting, 'GS' flag",
    "Key personnel: Caitlyn Murdick (Accounting Manager, main POC), Renee Rojas (Outsourced AR), David Holtzman (VP of Finance, decision maker)",
    "Go Live Date: Feb 7, 2024",
    "ERP: QuickBooks Online (QBO)",
    "Primary feature interest: AR Automation"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - ServiceUp_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:03:36

### Original Content
```
Steps to process ROs: Refer to the Company Name to find the name of the Customer and the Date to find the start date Each of these ROs represents a moment in time, so this will be the start state of both the revenue schedule and the billing term, and it will be a single occurrence Date frequency: 1 invoice per every None periods Company Name Processing Detail For customers below, please always use the name on the RIGHT : Zipcar Always Use: Zipcar Inc Sixt Always USe: Sixt Rent a Car LLC Clearcov...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Name Standardization and Mapping",
    "Repair Order (RO) Processing and Date Management",
    "Billing Terms and Line Item Mapping",
    "Tax Classification and Integration Item Mapping",
    "Discount Processing and Special Item Handling"
  ],
  "rules": [
    "Use Company Name field to identify customer and Date field for start date of revenue schedule and billing term",
    "Each RO represents a single occurrence moment in time",
    "Invoice frequency is 1 invoice per undefined period (None specified)",
    "Always use standardized customer names from the provided mapping (right side of mapping)",
    "Refer to line items in RO for billing terms configuration",
    "Item names should match Tabs Invoice Line Item Title with NO description",
    "If items not found in primary list, check supplemental items sheet",
    "If item not found in any list and is in PARTS column, link to Parts Revenue",
    "If item cannot be matched, leave blank rather than guessing",
    "Never use the integration item 'Labor Revenue' - use 'Mechanical Labor' (product/service, not category) instead",
    "Ignore quantity for all items except Towing - set Quantity to 1 and process totals",
    "For Towing line items, show actual quantity",
    "Do not process bolded line-items",
    "Process discounts as negative billing terms",
    "SKUs with 0.00 value do not need to be processed as billing terms",
    "All repair orders contain a gray box with total at the bottom"
  ],
  "exceptions": [
    "Towing line items are exception to quantity rule - must show actual quantity instead of defaulting to 1",
    "Bolded line-items should be ignored/not processed",
    "Pre-tax discounts use specific 'pre-tax discount integration item' rather than equivalent integration item",
    "Discounts with same titles as services use equivalent integration item (not the discount integration item)",
    "Labor Revenue item has special handling - must use 'Mechanical Labor' and ensure it's product/service type",
    "0.00 SKUs are excluded from billing term processing",
    "Items in PARTS column have fallback mapping to 'Parts Revenue' when not found in lists"
  ],
  "merchant_specific": [
    "Customer name standardization mappings: Zipcar → Zipcar Inc, Sixt → Sixt Rent a Car LLC, Clearcover Insurance → Clearcover, Voyager → Voyager Global Mobility3973bf86-1b48-4d7e-acdf-00a54973af5e, Kyte Systems Inc (not 'Kyte (Customer)'), Park N Fly → The Parking Spot (effective 7/1/2025)",
    "Two types of taxable items: SU Connect and SU 360 (identified next to Order on top right of RO)",
    "Tax type determines which integration items are mapped to each line item",
    "Reference to specific sheets for billing term mapping and supplemental items",
    "Tabs Invoice Line Item Title as source for item naming",
    "Integration item mapping table specific to this merchant's system",
    "Mechanical Labor must be selected as 'product' or 'service' type, not 'category'",
    "Gray box with total at bottom of all repair orders (merchant document format)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - ServiceUp_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:03:47

### Original Content
```
Ignore UNLESS: Rebate is listed If so, this will be a negative amount in the BT Taxes are listed If so, process as billing terms The integration item for Sales Tax will be associated with a state, and this state will be identified in the Market field in the Customer Information section at the top of the RO This field will identify a city, which will be matched to a state This is all reflected in the above table If Market is listed, but the city is not listed in the above table, flag to Ashni Wal...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice and RO (Repair Order) Processing",
    "Tax and Rebate Handling",
    "Geographic Market Mapping and Location Assignment",
    "Vehicle Information Data Entry (VIN, Odometer)",
    "Duplicate Contract Management"
  ],
  "rules": [
    "Rebates must be entered as negative amounts in BT (Billing Terms)",
    "Taxes listed in documents must be processed as billing terms",
    "Sales Tax integration items are associated with states identified in the Market field",
    "Market field cities must be matched to states using a reference table",
    "Invoice Location field must be populated from the Market field in Customer Information section",
    "Location is set via Action dropdown > Edit additional fields > select city from RO",
    "Odometer value must be copied from Customer Information section to Edit additional fields section",
    "VIN must be copied from Customer Information section to Edit additional fields section in invoice",
    "All invoices must use the same number as the RO number",
    "Invoice number is adjusted via Actions dropdown > Edit Number",
    "RO number is found on the top right of the RO document",
    "When duplicate contracts are uploaded with non-identical billing terms, both contracts must be processed"
  ],
  "exceptions": [
    "Only process rebates IF rebate is listed in the document",
    "Only process taxes IF taxes are listed in the document",
    "If Fleet Name includes 'Austin', the market is automatically 'Texas'",
    "SU Connect documents DO NOT require mapping to a market",
    "If Market is listed but city is not in the reference table, flag to Ashni Walia for state assignment guidance",
    "Duplicates are only processed when billing terms are not identical between uploads"
  ],
  "merchant_specific": [
    "Reference to 'Ashni Walia' as escalation contact for unmapped cities",
    "ServiceUp (SU) specific document types and upload processes",
    "SU Connect documents have different processing rules",
    "Fleet Name containing 'Austin' triggers specific Texas market assignment",
    "Specific field names: 'Market', 'Customer Information', 'BT', 'RO'",
    "City-to-state mapping table (referenced but not shown in document)",
    "Actions dropdown menu structure and field editing workflow"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Merchant Info Sheet - ServiceUp_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:02

### Original Content
```
92 discount Airport Van Rental: - 0 95 Integration item for both of the above discounts should be: Discounts Calculation sheet here Defaults: Default Service Term ROs do not need service term period Default Net Payment Terms Default all to Net 30 Default Billing Frequency N A How do we handle taxes as a line item Per above instruction, if taxes are shown in RO, process at BT Integration Items Processing (if necessary) What are the instructions for assigning integration items Integration items th...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Discount and Integration Item Mapping",
    "Default Configuration Settings",
    "Tax Processing and Handling",
    "Error Handling and Support Issues",
    "Communication and Notification Protocols"
  ],
  "rules": [
    "Airport Van Rental discount is 0.95 (5% discount)",
    "Integration item for discounts should be mapped to 'Discounts Calculation sheet'",
    "Default Service Term: ROs do not need service term period",
    "Default Net Payment Terms: Net 30 for all",
    "Default Billing Frequency: N/A",
    "Taxes shown in RO should be processed at BT (Bill To) level",
    "Integration items must correspond with each item within an RO as mapped in the document",
    "Use TaxJar for taxes (not integrated in QBO)",
    "Process taxes at BTs level",
    "Class field automation feature is enabled",
    "Location field processing is enabled and shown on invoice",
    "Attach contract to invoice email and merge PDFs",
    "Custom fields support is built in",
    "When duplicate documents are caught, delete them without notifying SU",
    "Invoices can be reset and resent in Tabs when mistakes occur"
  ],
  "exceptions": [
    "Zipcar customer does NOT want to receive dunning emails (special customer exception)",
    "Customer Integration time does not exist error: occurs occasionally when customer is mapped to wrong customer record in garage (such as deleted customer or Tabs customer)",
    "Market not listed error: occurs when RO with Sales Tax does not have a Market listed - requires reaching out to SU to determine which Market to use",
    "Mistakes by user (rare): marking as paid by mistake or sending incorrect invoice - can be corrected using reset and resend feature",
    "No notification required to Ops Team for completion of processing batches in Implementation or Active phase"
  ],
  "merchant_specific": [
    "Merchant uses QBO (QuickBooks Online) but TaxJar is not integrated",
    "Single primary customer: Zipcar (with specific dunning email exclusion)",
    "Specific discount structure: Airport Van Rental at 0.95",
    "Uses 'garage' system for customer mapping",
    "Uses 'Tabs' platform for invoice management",
    "References 'SU' (likely Setup/Support User or team)",
    "References 'Ashni' as specific contact person for error flagging",
    "Uses 'RO' terminology (likely Repair Order or similar)",
    "Uses 'Market' field for sales tax integration item determination",
    "Custom workflow between Tabs and SU systems",
    "Specific integration items mapped in referenced document/table"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 5: Merchant Info Sheet - ServiceUp_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:02

### Original Content
```
Please place a leading zero in front of the second contract's associated invoice IE: RO123 is uploaded twice with different terms, process Invoice 123 AND invoice 0123 Service up will void the contract that is not correct If invoice number already exists (Ie: Service Up has uploaded an identical RO to one tabs has already processed - please create the invoice with a leading zero, or zeros ) Example below: SU uploads RO 1234 Tabs processes INV 1234 SU Uploads RO 1234 (2) (or any other naming conv...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Duplicate Invoice Handling and Leading Zero Convention",
    "Customer Name Mapping and Standardization",
    "Fee Application Based on Invoice Type (SU Connect vs SU 360)",
    "Customer-Specific Discount Processing",
    "Special Customer Payment Terms and Configurations"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "When a duplicate repair order (RO) is uploaded, create invoice with leading zero(s) to differentiate",
      "details": "First occurrence: INV 1234, Second: INV 01234, Third: INV 001234"
    },
    {
      "rule_id": "R2",
      "description": "Add 1.99% fee to all SU Connect invoices",
      "details": "Fee calculated on total invoice amount including tax, mapped to 'Transaction Fees'"
    },
    {
      "rule_id": "R3",
      "description": "Do NOT add 1.99% fee to SU 360 invoices",
      "details": "Process SU 360 invoices normally without additional fees"
    },
    {
      "rule_id": "R4",
      "description": "Customer name mapping: 'Kyte Systems Inc' variations should map to 'Kyte'",
      "details": "May appear as '39521, Kyte SF' - use word 'Kyte' in title as signal"
    },
    {
      "rule_id": "R5",
      "description": "Customer name mapping: 'Voyager Global Mobility' variations",
      "details": "May appear as 'Fast Track Leasing LLC' or just 'Voyager' - always map to 'Voyager Global Mobility'"
    },
    {
      "rule_id": "R6",
      "description": "Customer name mapping: 'Hyrecar' should be mapped to 'Getaround'"
    },
    {
      "rule_id": "R7",
      "description": "Customer name mapping: 'Apple' should be mapped to 'Doneln - Apple'"
    },
    {
      "rule_id": "R8",
      "description": "IndieCampers always has net 15 payment terms"
    },
    {
      "rule_id": "R9",
      "description": "Use full legal name 'Town & Country Couriers LLC' (not just 'Town & Country')"
    },
    {
      "rule_id": "R10",
      "description": "Discount processing requires adding a new line item with negative value",
      "details": "Calculate as: Invoice Total × Discount Percentage, enter as negative amount"
    },
    {
      "rule_id": "R11",
      "description": "Apple and Airport Van Rental require extra BT (billing transaction) creation for each transaction"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "If RO with 'voyager' is unclear, reach out to CX before creating new client",
      "condition": "Unclear Voyager-related repair orders"
    },
    {
      "exception_id": "E2",
      "description": "Service Up will void incorrect contract if duplicate invoice number exists",
      "condition": "When identical RO already processed"
    },
    {
      "exception_id": "E3",
      "description": "Customer-specific discounts apply only to certain items for certain customers",
      "condition": "Per customer discount requirements list (specific list appears truncated in document)"
    },
    {
      "exception_id": "E4",
      "description": "SU Connect invoices require 1.99% fee, but SU 360 invoices do not",
      "condition": "Invoice type determines fee application"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice Type Classification",
      "description": "Distinction between 'SU Connect' and 'SU 360' invoice types",
      "customization_needed": "Merchant may have different invoice type categories"
    },
    {
      "element": "Customer Name Mapping Table",
      "description": "Specific customer aliases and their canonical names (Kyte, Voyager, Hyrecar, Apple, etc.)",
      "customization_needed": "Each merchant will have unique customer mapping requirements"
    },
    {
      "element": "Fee Structure",
      "description": "1.99% transaction fee specific to SU Connect invoices",
      "customization_needed": "Fee percentages and applicability vary by merchant"
    },
    {
      "element": "Payment Terms",
      "description": "Customer-specific net terms (e.g., IndieCampers = net 15)",
      "customization_needed": "Payment terms are merchant and customer-specific"
    },
    {
      "element": "Discount Rules",
      "description": "Customer-specific discount percentages and application rules",
      "customization_needed": "Discount structures vary by merchant agreements"
    },
    {
      "element": "Repair Order (RO) Terminology",
      "description": "Use of 'RO' and 'Service Up' as system/process names",
      "customization_needed": "Different merchants may use different document types and terminology"
    },
    {
      "element": "Escalation Process",
      "description": "Instruction to 'reach out to CX' for unclear cases",
      "customization_needed": "Escalation contacts and procedures vary by merchant"
    }
  ],
  "confidence_score": 0.82
}
```

**Confidence Score Rationale (0.82):**
- **Strengths**: Clear rules for duplicate handling, customer mapping, and fee application are well-defined
- **Limitations**: 
  - Document appears truncated (discount list incomplete, Apple BT instruction cut off)
  - Some ambiguity in "amazon Customer Specifics" heading placement
  - Discount calculation example formatting could be clearer
  - Missing complete details on which customers receive which specific discounts
  - "BT" acronym not explicitly defined (assumed to be billing transaction)

---

## Chunk 6: Merchant Info Sheet - ServiceUp_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:04:18

### Original Content
```
This happens because Market is not a required field for their team members to complete when closing out an RO on their side They are trying to be more prescriptive internally to enforce everyone to fill this out, so it happens less However, it still happens sometimes Account period closed: Invoice did not send because the account period was closed For this, let SU know and then tell them to reset and resent once they re-open the period Duplicate invoice number: Invoice did not send or invoice   ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Error Handling and Troubleshooting",
    "Product/Service Mapping Between Platforms (SU 360, SU Connect, QBO)",
    "Sales Tax Configuration by Geographic Location",
    "Customer-Specific Discount Structures",
    "Integration and Data Synchronization Issues"
  ],
  "rules": [
    "When Market field is missing: Invoice will not send; notify SU to have team members fill out Market field when closing RO",
    "When account period is closed: Invoice will not send; notify SU and instruct to reset and resend once period is reopened",
    "When duplicate invoice number occurs: Invoice cannot be sent or updated; flag to SU to confirm contract deletion (rare occurrence)",
    "Integration item not found errors: Leave blank, no need to notify SU (issue resolved)",
    "Body labor maps to 'Body Labor Revenue' in QBO",
    "Mechanical labor maps to 'Mechanical Labor Revenue' in QBO",
    "Paint labor maps to 'Paint Labor Revenue' in QBO",
    "Parts and Fluids map to 'Parts Revenue' in QBO",
    "Sales tax must be mapped according to specific state and city locations",
    "Pre-tax discounts map to 'Discounts' in QBO",
    "Hazardous Materials fees map to 'Miscellaneous Labor Revenue'",
    "Towing services map to 'Towing' category",
    "Oil changes and filters map to respective labor and parts revenue categories"
  ],
  "exceptions": [
    "Integration item not found: Previously an issue, now resolved - items are left blank without notification",
    "Duplicate invoice numbers: Rarely happens since transition out of QBO invoicing",
    "Amazon Last Mile Rental (Amazon LMR): Do NOT apply discount to Merchants Amazon Last Mile Rental, only apply 10% discount to Amazon LMR",
    "Customer-specific discount exception: 'No Discount' applies to certain customers (Apple)",
    "Geographic sales tax exceptions: Different tax rates and mappings apply based on 19+ different city/state combinations"
  ],
  "merchant_specific": [
    "Customer discount rates vary by merchant: Nexgen (4%), Hotwire Communications (5%), BluSky (4%), Traffic Management LA (4%), Airport Van Rental (4%), Acertus (10%), DHI2 Element Last Mile Rental (10%), Amazon Last Mile Rental (10% for Amazon LMR only)",
    "Platform-specific mappings: SU 360 vs SU Connect have different product/service mapping structures",
    "Market field completion requirements vary by team (not universally enforced)",
    "QBO Product Service Mapping tabs and naming conventions are merchant-specific",
    "Invoice description formats and PDF naming conventions appear to be customizable",
    "Geographic location determines sales tax mapping (19 different state/city combinations listed)"
  ],
  "confidence_score": 0.75
}
```

---

