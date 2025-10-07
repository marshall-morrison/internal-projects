# Raw LLM Analysis: Oscilar Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:51:24

---

## Chunk 1: Oscilar Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:24

### Original Content
```
Oscilar Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Jul 11, 2024 [If Exists] Opt Out Date: Go Live Date: Aug 1, 2024 GTM POC: Implementation POC: Arjun Gopalratnam and Ariel Bernsteinwhile Arjun is ooo ERP: Tax Integration: Key people at Merchant CEO: https: www linkedin com in nehanarkhede  Accountant: https: www linkedin com in kari-cook  (Fractional from Attivo) EA: Cami Dev: Ram Primary mode of communication:  oscilar-tabs-ext Company ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Relationship Timeline and Milestones",
    "Billing and Fee Structure",
    "Stakeholder Management and Communication",
    "Contract Processing and Integration",
    "Merchant Business Context and Goals"
  ],
  "rules": [
    "Platform fees are billed monthly, quarterly, or annually based on contract terms",
    "Usage fees are billed monthly in the second half of the month after Tabs receives usage reports",
    "Usage fees must be invoiced separately from platform fees",
    "Minimum commitments may be billed upfront on a monthly, quarterly, or annual basis",
    "Usage can be billed based on actual consumption (e.g., usage through 3P reseller)",
    "Documents are automatically sent via Docusign integration when contracts are closed-won",
    "Contract ingest information is for internal US team reference only"
  ],
  "exceptions": [
    "Usage billing can occur through alternative method: actual consumption via 3P reseller (instead of standard usage reports)",
    "Minimum commitments have flexible billing frequency options (monthly, quarterly, or annual) rather than a single standard",
    "Implementation POC has conditional coverage: 'Ariel Bernstein while Arjun is out of office' - indicating backup/coverage arrangement"
  ],
  "merchant_specific": [
    "Merchant temperament assessment (personality/working style evaluation)",
    "Key decision maker identification and delegation patterns (e.g., 'Neha who may defer to Kari')",
    "Specific Tabs features the merchant cares about (e.g., 'Usage tabulation' for Oscilar)",
    "Primary mode of communication channel (Slack channel: oscilar-tabs-ext)",
    "Merchant's north star goals (e.g., 'solving their usage tabulation issue')",
    "Merchant-specific timeline dates (Demo, Scoping, MSA Signature, Go Live, etc.)",
    "Merchant stakeholder roster with roles (CEO, Accountant, EA, Dev)",
    "ERP and Tax Integration systems (merchant-specific technical stack)",
    "Company business description and industry context"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Oscilar Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:26

### Original Content
```
Sometimes we get early versions of these docs Please ignore emails unless they say COMPLETED: on the subject and have a PDF attached That should reduce the chance of duplication DO NOT CREATE CUSTOMERS FOR THIS MERCHANT Instead, inform GS Suri when a matching customer does not already exist and he will provide next steps Please provide customer creation details in your message Please make sure when creating customers, that billing email is the one used to create customers Contract Interpretation...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Document Version Control and Email Management",
    "Customer Creation Workflow and Restrictions",
    "Contract Term Structuring and Obligation Management",
    "Revenue Recognition Alignment with Billing",
    "Multi-year Contract Handling"
  ],
  "rules": [
    {
      "rule": "Only process emails with 'COMPLETED:' in subject line and PDF attachment",
      "category": "Document Processing",
      "explicit": true
    },
    {
      "rule": "DO NOT create customers for this merchant independently",
      "category": "Customer Management",
      "explicit": true
    },
    {
      "rule": "Inform GS Suri when matching customer does not exist and await next steps",
      "category": "Customer Management",
      "explicit": true
    },
    {
      "rule": "Include customer creation details when requesting guidance",
      "category": "Customer Management",
      "explicit": true
    },
    {
      "rule": "Use billing email as the email for customer creation",
      "category": "Customer Management",
      "explicit": true
    },
    {
      "rule": "Avoid splitting obligations unnecessarily (e.g., multi-year contracts into quarterly terms)",
      "category": "Contract Structuring",
      "explicit": true
    },
    {
      "rule": "Do not split billing terms (BTs) by quarter",
      "category": "Contract Structuring",
      "explicit": true
    },
    {
      "rule": "Align revenue schedule with billing schedule",
      "category": "Revenue Recognition",
      "explicit": true
    },
    {
      "rule": "Match revenue recognition with full billing term (avoid defaulting to 1 year on 2-year prepaids)",
      "category": "Revenue Recognition",
      "explicit": true
    },
    {
      "rule": "For one-year contracts, create a single revenue schedule covering the whole year",
      "category": "Revenue Recognition",
      "explicit": true
    },
    {
      "rule": "Add recurring billing term that covers the amount and frequency stated in contract",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "For two-year contracts, account for potential price and credit ramp-ups between years",
      "category": "Multi-year Contracts",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Two-year contracts may have ramp-up in price and credits between year one and year two",
      "condition": "Multi-year contract duration",
      "impact": "Requires different handling than single-year contracts"
    },
    {
      "exception": "Early document versions should be ignored",
      "condition": "Email does not contain 'COMPLETED:' in subject or lacks PDF attachment",
      "impact": "Prevents processing of incomplete documents"
    }
  ],
  "merchant_specific": [
    {
      "element": "GS Suri as designated contact",
      "type": "Personnel/Contact",
      "customizable": true,
      "note": "Specific individual responsible for customer creation approvals"
    },
    {
      "element": "Customer creation restriction",
      "type": "Workflow Override",
      "customizable": true,
      "note": "This merchant requires special approval process, unlike standard workflow"
    },
    {
      "element": "Billing term splitting prohibition",
      "type": "Processing Rule",
      "customizable": true,
      "note": "Merchant preference for consolidated billing terms rather than quarterly splits"
    },
    {
      "element": "Email subject line requirement ('COMPLETED:')",
      "type": "Document Control",
      "customizable": true,
      "note": "Merchant-specific document versioning system"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Oscilar Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:40

### Original Content
```
In this case, create two revenue schedules, one for each year Do not write out the number of credits or seats that are included by each product Naming Full SKU name should be in title (Fraud Platform, Credit Decisioning Platform, etc ) No  Annual Fee  in front of SKU name, just the SKU name No need to put anything like  quarterly payments  in description Add on documents - sometimes customers will add more products services mid term Create new BTs if effective dates are different, and of course ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Management",
    "SKU Naming and Documentation Standards",
    "Payment Proration and Split Calculations",
    "Add-on Products and Mid-term Contract Changes",
    "Usage-based Billing and Monthly Minimums"
  ],
  "rules": [
    "Create separate revenue schedules when contracts span multiple years (one per year)",
    "Do not include number of credits or seats in product documentation",
    "Use full SKU name in title (e.g., Fraud Platform, Credit Decisioning Platform)",
    "Do not prefix SKU names with 'Annual Fee' or similar descriptors",
    "Do not add payment frequency descriptors (e.g., 'quarterly payments') in description field",
    "Create new BTs (Billing Transactions) when effective dates differ for add-on products",
    "Create new BTs when new SKUs are introduced mid-term",
    "Combine with previous BTs from original contract ONLY when effective dates and SKUs are identical",
    "Follow specified percentage splits for payment divisions (e.g., 40/60 for biannual payments)",
    "Always break out SKUs into individual line items, even with ramp-up payment schedules",
    "Calculate prorated amounts using formula: (Period Total ÷ Total Contract Amount) × SKU Total",
    "When Monthly Minimum exists, Usage AI must be enabled",
    "Do not process monthly minimum as a separate BT - it is captured by Usage AI module only",
    "Process all usage BTs through the system"
  ],
  "exceptions": [
    "Combine BTs with previous contract BTs only if both effective date AND SKUs are identical",
    "When specific payment splits are mentioned (e.g., 40/60), override standard equal distribution",
    "For ramp-up payment schedules, each SKU requires individual proration calculation for each payment period",
    "Monthly minimum invoicing is conditional: invoice minimum if usage is lower, invoice actual usage if higher",
    "Usage AI automatically handles month-end invoicing when usage falls below monthly minimum threshold"
  ],
  "merchant_specific": [
    "SKU names: 'Fraud Platform', 'Credit Decisioning Platform', 'Unity Plus' (appear to be product-specific)",
    "BT (Billing Transaction) terminology - may be internal system-specific",
    "Usage AI module - specific billing automation tool/system",
    "Payment split percentages (40/60) - varies by contract terms",
    "Monthly Minimum amounts - customer-specific thresholds",
    "Contract structure with 'terms and signature' section containing '2 tables that outline line items and costs'",
    "Proration calculation methodology may need adjustment based on merchant's accounting practices",
    "Revenue schedule creation rules may vary based on merchant's revenue recognition policies"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: Oscilar Merchant Info Sheet__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:51:43

### Original Content
```
Usage AI in garage Select Has usage requirements and Has Minimum Usage name: Monthly Minimum Included products: select ALL usage products You will select these in a dropdown Select individual billing period for minimum period This will cause the monthly minimum to track each billing period for the usage BTs So if there is a monthly API call usage BT, the minimum amount will apply each month since the BT is set up to occur monthly Select  True Up to Meet Minimum  button Default Service Term 1 yea...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Usage-based billing configuration with monthly minimums",
    "Default contract and payment terms setup",
    "Product-to-program mapping for integration items",
    "Event and integration processing workflows",
    "Post-implementation communication protocols"
  ],
  "rules": [
    {
      "rule": "Usage AI products must have 'Has usage requirements' and 'Has Minimum Usage' selected with name 'Monthly Minimum'",
      "category": "Usage Configuration"
    },
    {
      "rule": "All usage products must be included in the Monthly Minimum dropdown selection",
      "category": "Usage Configuration"
    },
    {
      "rule": "Individual billing period must be selected for minimum period to track each billing period for usage BTs",
      "category": "Usage Configuration"
    },
    {
      "rule": "'True Up to Meet Minimum' button must be selected",
      "category": "Usage Configuration"
    },
    {
      "rule": "Default Service Term is 1 year",
      "category": "Contract Terms"
    },
    {
      "rule": "Default Net Payment Terms is Net 30",
      "category": "Payment Terms"
    },
    {
      "rule": "Default Billing Frequency is Annual",
      "category": "Billing Configuration"
    },
    {
      "rule": "Events Processing should not be processed until after August 1, 2024",
      "category": "Events Processing"
    },
    {
      "rule": "Integration Items must use 'Oscilar programs:' prefix and match language in the SKU",
      "category": "Integration Mapping"
    },
    {
      "rule": "Professional Services maps to 'Oscilar Programs:Oscilar Professional Services'",
      "category": "Integration Mapping"
    },
    {
      "rule": "Credit Decisioning maps to 'Oscilar Programs:Oscilar Credit Risk Platform'",
      "category": "Integration Mapping"
    },
    {
      "rule": "Fraud Platform maps to 'Oscilar Programs:Oscilar Fraud Risk Platform'",
      "category": "Integration Mapping"
    },
    {
      "rule": "AML Platform maps to 'Oscilar Programs:Oscilar AML Risk Platform'",
      "category": "Integration Mapping"
    },
    {
      "rule": "Post-processing requires notifying merchant and tagging Kari on Slack channel 'oscilar-tabs-ext'",
      "category": "Communication"
    }
  ],
  "exceptions": [
    {
      "exception": "Events Processing is temporarily suspended (TBD) - MIS will be written after August 1, 2024",
      "condition": "Time-based exception until specific date"
    },
    {
      "exception": "KYC KYB integration mapping is incomplete - noted as 'THEY NEED TO ADD'",
      "condition": "Missing configuration that requires future action"
    },
    {
      "exception": "Monthly minimum applies per billing period when usage BT is set up to occur monthly (e.g., monthly API call usage)",
      "condition": "Conditional based on usage billing term frequency"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: 'Oscilar'",
      "type": "Merchant Identity"
    },
    {
      "element": "Specific Slack channel: 'oscilar-tabs-ext'",
      "type": "Communication Channel"
    },
    {
      "element": "Contact person: 'Kari' for post-processing notifications",
      "type": "Stakeholder"
    },
    {
      "element": "Product suite includes: Credit Risk Platform, Fraud Risk Platform, AML Risk Platform, Professional Services",
      "type": "Product Catalog"
    },
    {
      "element": "Integration items with Oscilar-specific program mappings",
      "type": "Integration Configuration"
    },
    {
      "element": "Reference video: Rewatch call from June 12, 2024",
      "type": "Documentation Reference"
    },
    {
      "element": "Usage scenario: 'Usage AI in garage' with API call usage billing",
      "type": "Use Case"
    }
  ],
  "confidence_score": 0.85
}
```

---

