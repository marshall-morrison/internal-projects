# Raw LLM Analysis: Merchant Info Sheet - Droplet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:45:44

---

## Chunk 1: Merchant Info Sheet - Droplet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:44

### Original Content
```
Merchant Demo date: Nov 7, 2024 Scoping start date: Sep 16, 2024 MSA Signature Date: Nov 13, 2024 Onboarding Kick Off Date: Nov 18, 2024 [If Exists] Opt Out Date: Oct Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: eate Tax Integration: - most customers are school districts so they are tax exempt Customer volume: 250 customers Billing model: Annual up front Key people at Merchant Director of Finance: Diego CEO: Mike (focused more on the sales ops side) - Sales side Company summary (A...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Background and Business Context",
    "Contract Processing and Revenue Recognition",
    "Customer Characteristics and Tax Treatment",
    "Integration and System Requirements",
    "Pain Points and Solution Requirements"
  ],
  "rules": [
    "Customer names should already exist in Tabs (synced from QBO)",
    "Do not use sub-customer functionality",
    "Use effective date to populate Service start date in Revenue Schedule",
    "Total months of service and periods = 60",
    "Use bolded line item under Dates for both Item name and Integration item in Garage",
    "Use Total Price and Quantity from each individual line item in contract",
    "Do not use Unit Price, as there are instances where quantity ≠ 1",
    "Net terms are found immediately under Payment schedule in contract",
    "Most customers are tax exempt (school districts)",
    "For single-year contracts: period = 1 (not on auto-renew)",
    "For Professional Services line items: Frequency = None in Garage",
    "Professional Services do not expire and are not tied to a specific period",
    "Billing model is Annual up front",
    "Contract term is 2 years with no opt-out clause"
  ],
  "exceptions": [
    "If contract only shows one year: refer to Brunswick County Board of Education example, set period = 1, contract is not on auto-renew",
    "If contract includes Professional Services: refer to Silver Creek Mortuary example, use Frequency = None, items do not expire",
    "Occasionally have usage component in addition to flat SaaS fee (though mostly flat SaaS)",
    "Handful of customers have parent-child relationship needs (specifically 2 BOCES customers flagged as main ones)",
    "85% or more contracts come back with redlines requiring modifications",
    "MSAs vary wildly requiring flexible handling"
  ],
  "merchant_specific": [
    "Customer base: 250 customers, mostly school districts (public sector focus)",
    "ERP: eate",
    "Tax Integration: Most customers tax exempt",
    "Key contacts: Diego (Director of Finance), Mike (CEO, sales ops focused)",
    "Previous tool: Cacheflow (being replaced due to limitations with enterprise contracting)",
    "CRM: Salesforce (SFDC)",
    "Go Live Date: Jan 1, 2025",
    "Specific customer examples: Brunswick County Board of Education, Silver Creek Mortuary, 2 BOCES customers",
    "Jurisdiction redlining is most frequent modification",
    "Heavy redlining process (85%+ of contracts)",
    "Contract complexity: MSAs vary wildly, robust enterprise contracting needs",
    "Garage link references for processing examples (merchant-specific documentation)",
    "QBO (QuickBooks Online) integration for customer sync"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Droplet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:46

### Original Content
```
Do not display discount percentage or discount amount unless it is explicitly called out as its own line item Do not include bulleted descriptions of line items anywhere on invoice Do not include Transaction Processing Fees - these are handled in Billing Settings Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Contract length and payment terms will differ by contract If stated in contract, include PO...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Display and Formatting Rules",
    "Contract and Payment Terms Configuration",
    "Purchase Order (PO) Processing Workflows",
    "Customer Information and Address Handling",
    "Internal Communication and Notification Protocols"
  ],
  "rules": [
    "Do not display discount percentage or discount amount unless explicitly called out as its own line item",
    "Do not include bulleted descriptions of line items anywhere on invoice",
    "Do not include Transaction Processing Fees (handled in Billing Settings)",
    "No taxes should be included as a line item",
    "Contract length and payment terms differ by contract and must refer to contract",
    "Default Service Term must refer to contract",
    "Default Net Payment Terms must refer to contract (displayed under Payment schedule)",
    "Default Billing Frequency must refer to contract",
    "If PO is uploaded with associated MSA, input PO number on originally generated invoices and mark PO as processed with no BTs",
    "If no MSA exists for uploaded PO customer, process the PO as a contract and generate invoices",
    "Include PO# in Key Terms if stated in contract",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant"
  ],
  "exceptions": [
    "Discount display exception: Only show if explicitly called out as its own line item",
    "PO processing exception: Different workflows for customers with MSA vs without MSA",
    "PNW BOCES special case: Do not use 'Ship To' field for address creation; use 'Item Description' instead",
    "PNW BOCES customer naming: Use actual customer name (e.g., 'Oneida CSD') not the ship-to name (e.g., 'Putnam No Westchester BOCES')",
    "Pinata integration labeling exception: Default to 'Software Subscription Bundle' unless merchant specifies otherwise",
    "Contract-specific variations: Some contracts may have back-dated invoice dates (e.g., final day of month)",
    "Merchant-specific invoice memos: Certain invoices require special memos due to merchant-customer relationships"
  ],
  "merchant_specific": [
    "Contract length (varies by merchant/contract)",
    "Payment terms (varies by merchant/contract)",
    "Service term (varies by merchant/contract)",
    "Billing frequency (varies by merchant/contract)",
    "Events billing processing (Implementation Success to fill per merchant)",
    "Integration item labeling rules (merchant-specific: Statsig, Pinata examples provided)",
    "Post-processing notification requirements (who to notify, when, and where - varies by merchant)",
    "Customer-specific address handling rules (e.g., PNW BOCES)",
    "Special invoice memos based on merchant-customer relationships",
    "Feature requests tracking (per merchant)",
    "Rewatch call recordings (merchant-specific: Droplet, Diego Benjamin examples)",
    "Internal merchant channels for notifications (e.g., Messari internal merchant channel)",
    "Merchant phase tracking (Implementation vs Active)",
    "Specific customer names and contact persons (e.g., Azmat Aziz for Customer Success)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Droplet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:45:54

### Original Content
```
com video ovlpkjxsjddwm021-diego-ben-sync-on-proposal-october-30-2024 Main demo with Diego and CEO Mike https: tabs rewatch com video upij2bfzm8vsy9cr-tabs-demo-november-7-2024 Implementation prep call with Diego https: tabs rewatch com video yzxsel6jfpq1s3p0-diego-ben-sync-on-implementation-november-14-2024 Implementation Kick-off https: tabs rewatch com video x6ijbqgui0o2hddt-tabs-droplet-implementation-kick-off-november-19-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementa...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship management and key stakeholder identification",
    "Billing complexity and payment structures",
    "Implementation process and documentation",
    "Parent-child organizational relationships",
    "Customer temperament and partnership quality assessment"
  ],
  "rules": [
    "Billing is typically annual and paid up front",
    "Merchants fall under school district billing cycles",
    "Parent-child relationship billing must be accommodated",
    "Bill-to and ship-to addresses may differ and need separate handling",
    "Key POC (Point of Contact) must be identified as the buyer/decision maker",
    "Platform usage should align with key POC's needs and satisfaction",
    "Implementation team and Account Executive (AE) are responsible for filling merchant relationship information",
    "Operations International Team should ignore certain sections marked for AE/Implementation"
  ],
  "exceptions": [
    "BOC is noted as 'one of the more gnarly ones' - indicating it requires special handling for bill vs ship-to address complexity",
    "Some merchants may have complexities in parent-child billing relationships that deviate from standard processes",
    "School district cycle timing may create exceptions to standard billing schedules"
  ],
  "merchant_specific": [
    "Merchant temperament assessment (e.g., 'Diego is awesome and going to be an excellent partner')",
    "Key POC identification (Diego as main user, Mike as secondary stakeholder)",
    "Specific stakeholder relationships (Mike's satisfaction depends on Diego's happiness)",
    "Individual merchant's preferred Tabs features",
    "Organizational structure (parent-child relationships)",
    "Billing address configurations (bill-to vs ship-to)",
    "Industry vertical (school district in this case)",
    "Payment timing preferences (annual up front)"
  ],
  "confidence_score": 0.85
}
```

---

