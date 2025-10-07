# Raw LLM Analysis: Merchant Info Sheet - Droplet(1)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:02:14

---

## Chunk 1: Merchant Info Sheet - Droplet(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:02:14

### Original Content
```
Do not display discount percentage or discount amount unless it is explicitly called out as its own line item Do not include bulleted descriptions of line items anywhere on invoice Do not include Transaction Processing Fees - these are handled in Billing Settings Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Contract length and payment terms will differ by contract If stated in contract, include PO...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice formatting and display requirements",
    "Contract-specific terms and customization",
    "Purchase Order (PO) handling and processing",
    "Customer information and address management",
    "Internal communication and notification workflows"
  ],
  "rules": [
    "Do not display discount percentage or discount amount unless explicitly called out as its own line item",
    "Do not include bulleted descriptions of line items on invoices",
    "Do not include Transaction Processing Fees on invoices (handled in Billing Settings)",
    "Contract length and payment terms differ by contract and must be referenced",
    "Include PO number in Key Terms if stated in contract",
    "Default Service Term must refer to contract",
    "Default Net Payment Terms must refer to contract",
    "Default Billing Frequency must refer to contract",
    "No taxes should be included as line items",
    "If PO is uploaded with associated MSA, input PO number on generated invoices and mark as processed with no BTs",
    "If no MSA exists for uploaded PO, process the PO as a contract and generate invoices",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Payment schedule information will be displayed under Payment schedule section"
  ],
  "exceptions": [
    "Discount amounts can be displayed only if explicitly called out as its own line item",
    "Specifics may differ by contract (e.g., back-dating invoice date to final day of month)",
    "PO processing differs based on presence of MSA: with MSA = no BTs, without MSA = process as contract",
    "For PNW BOCES POs: do not use 'Ship To' field for address creation, use 'Item Description' instead",
    "For PNW BOCES POs: customer name should be derived from item description (e.g., 'Oneida CSD' not 'Putnam' or 'Westchester BOCES')",
    "Pinata integration items may have exceptions to standard labeling if noted by merchant",
    "Special memos may be required for certain invoices based on merchant-customer relationships"
  ],
  "merchant_specific": [
    "Contract-specific back-dating requirements for invoice dates",
    "Merchant-specific contract terms (length, payment terms, billing frequency)",
    "Customer-specific notification requirements (e.g., Messari: notify Azmat Aziz in internal channel when contracts processed in Active phase)",
    "Merchant-specific customer naming conventions (e.g., PNW BOCES address handling)",
    "Integration item labeling varies by merchant (Statsig, Pinata examples provided)",
    "Events billing processing requirements (to be filled by Implementation Success)",
    "Post-processing communication protocols vary by merchant phase (Implementation vs Active)",
    "Special invoice modifications based on merchant-customer relationships",
    "Merchant-specific feature requests tracked separately",
    "Rewatch call recordings for merchant context"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Droplet(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:02:21

### Original Content
```
Merchant Demo date: Nov 7, 2024 Scoping start date: Sep 16, 2024 MSA Signature Date: Nov 13, 2024 Onboarding Kick Off Date: Nov 18, 2024 [If Exists] Opt Out Date: Oct Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: eate Tax Integration: - most customers are school districts so they are tax exempt Customer volume: 250 customers Billing model: Annual up front Key people at Merchant Director of Finance: Diego CEO: Mike (focused more on the sales ops side) - Sales side Company summary (A...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Recognition",
    "Customer and Billing Model Configuration",
    "Merchant Business Context and Pain Points",
    "Renewal Terms and Auto-Renewal Handling",
    "Tax Exemption and Public Sector Specifics"
  ],
  "rules": [
    {
      "rule": "Customer names should already exist in Tabs, synced from QBO and will be in contract name",
      "category": "Customer Setup"
    },
    {
      "rule": "Should not need to use sub-customer functionality",
      "category": "Customer Setup"
    },
    {
      "rule": "If contract includes Renewal Terms, set BTs to 5 years worth of periods",
      "category": "Renewals"
    },
    {
      "rule": "For monthly auto-renewing contracts: period = 60",
      "category": "Renewals"
    },
    {
      "rule": "For annual auto-renewing contracts: period = 5",
      "category": "Renewals"
    },
    {
      "rule": "Professional Services typically do not renew",
      "category": "Renewals"
    },
    {
      "rule": "Use Total Price and Quantity from each individual line item in contract",
      "category": "Pricing"
    },
    {
      "rule": "Do not use Unit Price, as there are instances where quantity ≠ 1",
      "category": "Pricing"
    },
    {
      "rule": "Bolded line item under Dates is used for both Item name and Integration item in Garage",
      "category": "Contract Processing"
    },
    {
      "rule": "Use effective date to populate Service start date in Revenue Schedule",
      "category": "Contract Processing"
    },
    {
      "rule": "Net terms found immediately under Payment schedule in contract",
      "category": "Payment Terms"
    },
    {
      "rule": "For Professional Services: Frequency = None in Garage",
      "category": "Professional Services"
    },
    {
      "rule": "Professional Services do not expire and are not tied to a specific period",
      "category": "Professional Services"
    },
    {
      "rule": "Most customers are tax exempt (school districts)",
      "category": "Tax"
    },
    {
      "rule": "Total months of service and periods = 60 for auto-renewing monthly contracts",
      "category": "Service Terms"
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts showing only one month on auto-renew require special processing (refer to Atlantic Diamond Company example)",
      "handling": "Refer to specific garage link, use effective date for service start, set periods to 60"
    },
    {
      "exception": "Contracts showing only one year (not on auto-renew) require different processing (refer to Brunswick County Board of Education example)",
      "handling": "Follow outlined steps but set period = 1 instead of 5"
    },
    {
      "exception": "Contracts including Professional Services require special handling (refer to Silver Creek Mortuary example)",
      "handling": "Set Frequency = None, these do not expire and are not tied to specific period"
    },
    {
      "exception": "Handful of customers have parent-child relationship needs",
      "handling": "2 BOCES customers are main ones to flag"
    },
    {
      "exception": "Occasionally have usage component in addition to flat SaaS fee",
      "handling": "Not standard billing model, requires special attention"
    },
    {
      "exception": "85% or more times customers come back with redlines",
      "handling": "Contract terms vary wildly, particularly jurisdiction clauses"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Base",
      "details": "250 customers, mostly school districts (public sector), tax exempt"
    },
    {
      "element": "Business Model",
      "details": "Digital forms and workflow platform, subscription-based, annual upfront billing"
    },
    {
      "element": "Pain Points",
      "details": "Previous tool (Cacheflow) cannot handle robust enterprise contracting, poor support for SFDC users, rigid quoting, struggles with redlines and MSA variations"
    },
    {
      "element": "Contract Terms",
      "details": "2 year contract with no opt-out clause, MSAs vary wildly"
    },
    {
      "element": "Key Stakeholders",
      "details": "Director of Finance: Diego, CEO: Mike (sales ops focused)"
    },
    {
      "element": "Timeline",
      "details": "Demo: Nov 7, 2024, MSA Signature: Nov 13, 2024, Onboarding: Nov 18, 2024, Go Live: Jan 1, 2025"
    },
    {
      "element": "Integration",
      "details": "Syncs with QBO (QuickBooks Online), SFDC users"
    },
    {
      "element": "Special Customer Types",
      "details": "BOCES customers (2 main ones) with parent-child relationship needs"
    },
    {
      "element": "Redlining Frequency",
      "details": "85%+ of contracts require redlines, particularly jurisdiction clauses for arbitration"
    },
    {
      "element": "Product Mix",
      "details": "Mostly flat SaaS fees, occasionally usage component, Professional Services as add-on"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Droplet(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:02:25

### Original Content
```
com video ovlpkjxsjddwm021-diego-ben-sync-on-proposal-october-30-2024 Main demo with Diego and CEO Mike https: tabs rewatch com video upij2bfzm8vsy9cr-tabs-demo-november-7-2024 Implementation prep call with Diego https: tabs rewatch com video yzxsel6jfpq1s3p0-diego-ben-sync-on-implementation-november-14-2024 Implementation Kick-off https: tabs rewatch com video x6ijbqgui0o2hddt-tabs-droplet-implementation-kick-off-november-19-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementa...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Relationship Management and Key Stakeholder Identification",
    "Billing Complexity and Payment Structure",
    "Implementation Process and Documentation",
    "Parent-Child Organizational Relationships",
    "Customer Success and POC Engagement"
  ],
  "rules": [
    "Annual billing is typically processed upfront",
    "Merchants fall under school district billing cycles",
    "Parent-child relationship billing must be accommodated (e.g., separate Bill-to and Ship-to addresses)",
    "Implementation team and Account Executives must fill in merchant relationship sections",
    "International Operations team should ignore certain sections marked for them",
    "Key POC identification is required for each merchant account",
    "Merchant temperament assessment must be documented",
    "Platform feature preferences of key POC must be identified and documented"
  ],
  "exceptions": [
    "BOC (Bill of Costs) represents a particularly complex ('gnarly') billing scenario requiring special handling",
    "Bill-to address may differ from Ship-to address in parent-child relationships",
    "Some sections are explicitly marked for specific teams to ignore (Ops International Team)"
  ],
  "merchant_specific": [
    "Diego identified as key POC and main platform user",
    "Mike (CEO) identified as secondary stakeholder whose satisfaction depends on Diego's success",
    "Merchant temperament: 'Diego is awesome and going to be an excellent partner'",
    "School district billing cycle timing may vary by merchant",
    "Parent-child organizational structure varies by merchant (complexity level differs)",
    "Specific Tabs platform features valued by POC will vary per merchant"
  ],
  "confidence_score": 0.85
}
```

---

