# Raw LLM Analysis: Flatfile MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 09:57:58

---

## Chunk 1: Flatfile MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:57:58

### Original Content
```
g ,  500 for files, billed once upfront, frequency can match the service period) Need to check the subtotal column header to see what the amount should be If header says  Monthly subtotal  but the invoice period says  Provider will send invoices annually  - you will need to multiply the flat BT by 12 to charge the full annual amount upfront You will need to also multiply the amount by 12 for the usage AI piece The usage AI threshold amount should match the upfront BT See instructions below for u...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Usage-based billing and threshold management",
    "Prepaid billing and upfront charges calculation",
    "Usage AI configuration and automation",
    "Retainer and credit-based billing models",
    "Billing term frequency alignment with invoice periods"
  ],
  "rules": [
    "Flat billing terms (BT) for files are billed once upfront at $500",
    "Check subtotal column header to determine correct billing amount",
    "When header says 'Monthly subtotal' but invoice period is annual, multiply flat BT by 12",
    "Usage AI threshold amount must match the upfront BT amount",
    "Never divide files or PDV prices",
    "Turn on Usage AI for BTs with large quantities like Files and PDV",
    "For prepaid invoicing: select 'Has Threshold' and set threshold period to full service term",
    "Select individual products (usage BT) and name event as 'Prepaid'",
    "Threshold amount should equal subtotal amount (multiply by service period months if monthly)",
    "Always turn on 'charges overages' for usage AI",
    "Apply usage AI steps for each BT when multiple BTs have prepayment",
    "Do NOT select 'apply usage models sequentially'",
    "Create additional usage BT for 'Included products' in usage AI",
    "PDV usage BT should be regular unit BT titled 'PDV (1M Bundles)' - ignore 10M free part",
    "Files should use tier unit BT: first tier up to 50 free, second tier 51+ at $1.00 per file",
    "Usage events must be mapped to 'usage' revenue category",
    "For retainers: create one-time flat billing term for full retainer amount",
    "Retainer usage AI: select 'Has Threshold', call it 'Retainer', select only covered products, use full service term, enable 'Charges overages'",
    "Optional add-on services can be ignored"
  ],
  "exceptions": [
    "Monthly subtotal with annual invoicing requires 12x multiplication",
    "PDV billing ignores the '10M free' component when creating usage BT",
    "Files have tiered pricing structure with first 50 free",
    "Retainer line items are treated as prepaid credits rather than standard billing",
    "Usage AI configuration differs when multiple BTs have prepayment (each requires separate setup)",
    "Quarterly prepaid invoicing (e.g., Assignar) follows same usage AI pattern but with quarterly calculations"
  ],
  "merchant_specific": [
    "Specific merchant examples referenced: NEXL, Deputy, Assignar",
    "Contract-specific processing requests that may differ by contract",
    "Reference implementation IDs: 0b34ca19-80a6-4fb4-b2c3-e98174163950, 1b49eaf0-234d-484f-9710-e74b64b852d8",
    "Merchant-specific pricing: $500 for files, $1.00 per file after 50",
    "PDV bundling in 1M increments (merchant-specific unit)",
    "Retainer coverage scope varies by agreement (only certain products covered)",
    "Invoice frequency customization (monthly, quarterly, annual)",
    "Subtotal column header naming conventions may vary by merchant"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: Flatfile MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:08

### Original Content
```
Flatfile Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Customer Creation Create customer if it doesn t already exist (should exist) Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) BTs are typically found in Cl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term (BT) Creation",
    "Customer Creation and Validation",
    "Pricing Interpretation and Frequency Determination",
    "Usage-Based Billing Configuration",
    "Revenue Categorization and Mapping"
  ],
  "rules": [
    {
      "rule": "Create customer only if it doesn't already exist (should exist)",
      "category": "Customer Creation"
    },
    {
      "rule": "BTs are typically found in Cloud Service Fees table",
      "category": "Contract Processing"
    },
    {
      "rule": "Do not create separate BTs for discounts - use in-line discounting with 'Add discount' button",
      "category": "Discount Handling"
    },
    {
      "rule": "Ignore $0 'included' billing terms",
      "category": "Billing Term Creation"
    },
    {
      "rule": "Billing Start Date: found in 'Subscription Start Date' section",
      "category": "Date Configuration"
    },
    {
      "rule": "Service Start Date: same as billing start date",
      "category": "Date Configuration"
    },
    {
      "rule": "Months of Service: found in 'Subscription Period' or 'Initial Service Term' section (default to 12 months if none)",
      "category": "Service Term"
    },
    {
      "rule": "Frequency: check 'invoice period' or 'billing terms' section (default to annually upfront if none)",
      "category": "Billing Frequency"
    },
    {
      "rule": "Ignore subtotal column header and follow invoice period section on first page",
      "category": "Price Interpretation"
    },
    {
      "rule": "If subtotal says 'Monthly amounts' but invoices are sent annually, multiply amounts by 12",
      "category": "Price Calculation"
    },
    {
      "rule": "If fine print conflicts with Billing Terms section, ignore fine print",
      "category": "Document Interpretation Priority"
    },
    {
      "rule": "Net Terms: check 'payment period' or 'billing terms' section (default to 30 days if none)",
      "category": "Payment Terms"
    },
    {
      "rule": "Total Price: Unless subtotal header specifies 'monthly', assume prices listed are annual",
      "category": "Price Interpretation"
    },
    {
      "rule": "Divide prices by appropriate frequency (e.g., quarterly = divide by 4)",
      "category": "Price Calculation"
    },
    {
      "rule": "Usage BTs default to monthly",
      "category": "Usage Billing"
    },
    {
      "rule": "For Annual Seats: do not divide price even if subtotal implies you should - should be monthly BT in arrears for $12",
      "category": "Annual Seats Exception"
    },
    {
      "rule": "Importer Pro SKU: FLAT BT but NOT a Usage BT, follows frequency from Billing Terms section",
      "category": "SKU-Specific Rules"
    },
    {
      "rule": "Quantity: use listed amount in table",
      "category": "Quantity Configuration"
    },
    {
      "rule": "Usage BTs with 0 quantity: create only usage BT, no additional flat BT needed",
      "category": "Usage Billing"
    },
    {
      "rule": "Usage BTs with quantity > 0: create flat BT with list amount and quantity, then create usage BT for overage (monthly in arrears)",
      "category": "Usage Billing"
    },
    {
      "rule": "Check item description for billing instructions",
      "category": "Billing Configuration"
    },
    {
      "rule": "Revenue Category: Select 'service' or 'subscription' based on line item language for all flat BTs",
      "category": "Revenue Mapping"
    },
    {
      "rule": "All usage BTs must be mapped to 'usage' revenue category",
      "category": "Revenue Mapping"
    },
    {
      "rule": "Usage events should already be created - flag if not",
      "category": "Usage Configuration"
    },
    {
      "rule": "Usage with quantity > 1 represents pre-paid upfront for initial volume - create flat billing term for prepayment",
      "category": "Usage Billing"
    }
  ],
  "exceptions": [
    {
      "exception": "Annual Seats: do not divide price regardless of subtotal column implications",
      "condition": "When processing Annual Seats line items"
    },
    {
      "exception": "Importer Pro SKU is a FLAT BT but NOT a Usage BT",
      "condition": "When processing Importer Pro SKU specifically"
    },
    {
      "exception": "If subtotal says 'Monthly amounts' but invoices are annual, multiply by 12",
      "condition": "When subtotal header conflicts with actual billing frequency"
    },
    {
      "exception": "Ignore fine print when it conflicts with Billing Terms section",
      "condition": "When document sections provide contradictory information",
      "example": "Billing Terms says monthly but fine print says annually"
    },
    {
      "exception": "Usage BTs with 0 quantity: only create usage BT, no flat BT",
      "condition": "When usage billing term has zero quantity"
    },
    {
      "exception": "Usage BTs with quantity > 0: create both flat BT and usage BT",
      "condition": "When usage billing term has quantity greater than zero"
    },
    {
      "exception": "Default to 12 months if Subscription Period not specified",
      "condition": "When service term information is missing"
    },
    {
      "exception": "Default to annually upfront if frequency not specified",
      "condition": "When billing frequency information is missing"
    },
    {
      "exception": "Default to 30 days if net terms not specified",
      "condition": "When payment terms information is missing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Flatfile Implementation POC",
      "type": "Implementation Contact",
      "note": "To be filled by IM"
    },
    {
      "element": "CX POC",
      "type": "Customer Experience Contact",
      "note": "To be added by IMP"
    },
    {
      "element": "Billing model section",
      "type": "Merchant-specific billing configuration",
      "note": "Implementation to fill - includes unique customer creation process, how merchant bills, contract structure, one-off merchant details"
    },
    {
      "element": "Contract Processing Steps",
      "type": "Post-implementation documentation",
      "note": "Implementation Success to fill Post-Go Live"
    },
    {
      "element": "Cloud Service Fees table",
      "type": "Document location reference",
      "note": "Merchant-specific table name where BTs are found"
    },
    {
      "element": "Annual Seats pricing rule",
      "type": "SKU-specific configuration",
      "note": "Fixed at $12 monthly in arrears regardless of contract terms"
    },
    {
      "element": "Importer Pro SKU",
      "type": "SKU-specific configuration",
      "note": "Special handling as FLAT BT but not Usage BT"
    },
    {
      "element": "Usage events",
      "type": "Pre-configuration requirement",
      "note": "Should be created before processing, flag if missing"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Flatfile MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:58:18

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Processi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Post-implementation processing workflows and responsibilities",
    "Merchant-specific billing and customer handling procedures",
    "Cross-team communication and notification protocols",
    "Feature requests and merchant relationship management"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year when none is listed",
      "category": "Service Terms",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 when none is specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly when none is listed",
      "category": "Billing Frequency",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Items",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "AE fills Merchant Calls prior to Implementation involvement; Implementation fills prior to go-live; Success fills Post-Go Live",
      "category": "Responsibilities",
      "explicit": true
    },
    {
      "rule": "Implementation is the completion DRI (Directly Responsible Individual) on handoff for Notes Section",
      "category": "Responsibilities",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by the merchant",
      "condition": "Merchant provides alternative labeling instructions"
    },
    {
      "exception": "Specific merchant billing model: upfront commitment drawn against as usage is used",
      "condition": "Merchant-specific billing arrangement"
    },
    {
      "exception": "Invoices created but not sent, with separate cash app and rev rec processing",
      "condition": "Merchant using Sequence platform with specific workflow requirements"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Customer-specific requirements exist"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship specifics",
      "condition": "Relationship-driven modifications required"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model",
      "description": "One-time upfront commitment drawn against usage",
      "customizable": true
    },
    {
      "element": "Platform integration",
      "description": "Using Sequence platform for billing",
      "customizable": true
    },
    {
      "element": "Invoice workflow",
      "description": "Create invoices but don't send them; separate cash app and rev rec",
      "customizable": true
    },
    {
      "element": "Key contacts and temperament",
      "description": "Josh Baker (Director of Accounting, helpful), Victoria (Accountant, quiet/timid about AI)",
      "customizable": true
    },
    {
      "element": "Priority features",
      "description": "Cash app and rev rec are key POC concerns",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Statsig as 'Sales', Pinata as 'Software Subscription Bundle'",
      "customizable": true
    },
    {
      "element": "Notification requirements",
      "description": "Who to notify, where, and when for batch processing completion",
      "customizable": true
    },
    {
      "element": "Customer-specific information",
      "description": "Special memos and invoice changes per customer relationship",
      "customizable": true
    },
    {
      "element": "Events billing processing",
      "description": "If necessary, merchant-specific handling",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

