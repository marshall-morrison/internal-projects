# Raw LLM Analysis: River Health Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:26:36

---

## Chunk 1: River Health Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:36

### Original Content
```
Merchant Demo date: Nov 26, 2024 Scoping start date: Nov 26, 2024 MSA Signature Date: Nov 27, 2024 Onboarding Kick Off Date: Dec 5, 2024 [If Exists] Opt Out Date: NA Go Live Date: Dec 9, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant CEO: Kobby Amoah (pronounced like Kobe) Operations: Liang Xiong Company summary (AE to fill) Summary of what company does: Health platform for hourly 1099 workers Taco bell employees who need health insurance TB is the customer and th...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Business Context and Pain Points",
    "Billing Model and Customer Management",
    "Contract Processing and Invoice Configuration",
    "Stakeholder Information and Communication"
  ],
  "rules": [
    {
      "rule": "Service Start Date must refer to the 'Plan Start Date' field",
      "category": "contract_processing"
    },
    {
      "rule": "Months of Service defaults to 12 if none listed",
      "category": "contract_processing"
    },
    {
      "rule": "Item Name must follow format: [Plan Type] - [Coverage Type], where Plan Type is 'River Health Essentials Plan' or 'River Health Complete Plan' and Coverage Type is 'Individual', 'Individual + Partner', 'Individual + Children', or 'Individual + Family'",
      "category": "contract_processing"
    },
    {
      "rule": "Item Description must include unit price",
      "category": "contract_processing"
    },
    {
      "rule": "Integration Item must be set to 'Employer Invoicing'",
      "category": "contract_processing"
    },
    {
      "rule": "Integration Item must include value '2000'",
      "category": "contract_processing"
    },
    {
      "rule": "Revenue Billing Type must be 'Unit price'",
      "category": "contract_processing"
    },
    {
      "rule": "Total Price must refer to pricing details",
      "category": "contract_processing"
    },
    {
      "rule": "Contribution and Discounts should be ignored in processing",
      "category": "contract_processing"
    },
    {
      "rule": "Merchant bills monthly with minimal usage updates",
      "category": "billing_model"
    },
    {
      "rule": "Customer seats are not often updated month to month",
      "category": "billing_model"
    }
  ],
  "exceptions": [
    {
      "exception": "No opt-out clause exists for this merchant",
      "context": "Unlike standard contracts that may include opt-out provisions, this merchant has no opt-out option"
    },
    {
      "exception": "No unique customer creation process for this merchant",
      "context": "Standard customer creation process applies"
    },
    {
      "exception": "Contract break-up structure is marked as 'NA'",
      "context": "No special contract segmentation required"
    },
    {
      "exception": "No one-off special considerations noted",
      "context": "Standard processing applies"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name and branding",
      "details": "River Health - health platform for hourly 1099 workers"
    },
    {
      "element": "Target customer base",
      "details": "Taco Bell employees who need health insurance; TB is the customer, workers get different plans based on hours worked"
    },
    {
      "element": "Key stakeholders",
      "details": "CEO: Kobby Amoah (pronunciation note: 'like Kobe'), Operations: Liang Xiong"
    },
    {
      "element": "Pain point being solved",
      "details": "Liang spends significant time managing contracts manually in spreadsheets"
    },
    {
      "element": "Product naming convention",
      "details": "River Health Essentials Plan and River Health Complete Plan with four coverage tier options"
    },
    {
      "element": "Timeline dates",
      "details": "Demo: Nov 26, 2024; MSA Signature: Nov 27, 2024; Kick Off: Dec 5, 2024; Go Live: Dec 9, 2024"
    },
    {
      "element": "Integration fields",
      "details": "ERP and Tax Integration fields exist but are not populated for this merchant"
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: River Health Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:45

### Original Content
```
Event to Track: Here Start Date: always use bill last of period w  invoice date on first of month Use the "First Invoice is expected on" date from the document start date for all Prime Hospitality accounts to be set to 1 1 2025 Periods: Depends on the frequency and the months of service Frequency: Refer to Invoicing Cadence Net Terms: Refer to Invoicing Terms Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Date and Billing Period Configuration",
    "Default Values and Fallback Rules for Missing Contract Information",
    "Integration Item Labeling and Categorization",
    "Post-Processing Communication and Notification Protocols",
    "Merchant-Specific Customer Handling and Relationship Management"
  ],
  "rules": [
    {
      "rule": "For Prime Hospitality accounts, always set 'First Invoice is expected on' date to 1/1/2025",
      "category": "Invoice Configuration",
      "specificity": "merchant-specific"
    },
    {
      "rule": "Always use bill last of period with invoice date on first of month for Here Start Date event tracking",
      "category": "Invoice Date Configuration",
      "specificity": "general"
    },
    {
      "rule": "Default Service Term if none listed: 1 Year",
      "category": "Default Values",
      "specificity": "general"
    },
    {
      "rule": "Default Net Payment Terms if none listed: 0 (Net 0)",
      "category": "Default Values",
      "specificity": "general"
    },
    {
      "rule": "Default Billing Frequency if none listed: Monthly",
      "category": "Default Values",
      "specificity": "general"
    },
    {
      "rule": "Default tax handling: every tax line item becomes a BT (Billable Transaction) Events",
      "category": "Tax Processing",
      "specificity": "general"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "specificity": "integration-specific"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Labeling",
      "specificity": "integration-specific"
    },
    {
      "rule": "Periods depend on frequency and months of service",
      "category": "Billing Configuration",
      "specificity": "general"
    },
    {
      "rule": "Frequency should refer to Invoicing Cadence from contract",
      "category": "Billing Configuration",
      "specificity": "general"
    },
    {
      "rule": "Net Terms should refer to Invoicing Terms from contract",
      "category": "Payment Terms",
      "specificity": "general"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant may request specific processing that differs by contract (e.g., always back-date invoice date to final day of the month)",
      "condition": "Contract-specific requests",
      "handling": "Review contract specifics for processing variations"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by Merchant",
      "condition": "Merchant provides alternative labeling instructions",
      "handling": "Override default 'Software Subscription Bundle' label"
    },
    {
      "exception": "Different tiers for different employees working at customer companies (e.g., Taco Bell, Cracker Barrel)",
      "condition": "Bespoke contracts with tiered pricing",
      "handling": "Apply appropriate tier based on employee level"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationship",
      "condition": "Specific customer relationships",
      "handling": "Add custom memos as specified"
    }
  ],
  "merchant_specific": [
    {
      "element": "Prime Hospitality accounts",
      "customization": "Fixed start date of 1/1/2025 for first invoice",
      "type": "merchant-specific rule"
    },
    {
      "element": "Customer Success notification requirements",
      "customization": "Notify Azmat Aziz in Messari internal merchant channel when contracts are processed in Active phase",
      "type": "communication protocol"
    },
    {
      "element": "Bespoke contract structures",
      "customization": "Working with companies like Taco Bell, Cracker Barrel with different employee tiers",
      "type": "pricing structure"
    },
    {
      "element": "Integration item labeling",
      "customization": "Statsig = 'Sales', Pinata = 'Software Subscription Bundle'",
      "type": "integration-specific configuration"
    },
    {
      "element": "Invoice date back-dating",
      "customization": "Some contracts require invoice dates to be back-dated to final day of month",
      "type": "contract-specific processing"
    },
    {
      "element": "Post-processing notifications",
      "customization": "Varies by merchant - who to notify, where, and when",
      "type": "communication protocol"
    },
    {
      "element": "Customer-specific invoice changes",
      "customization": "Invoice modifications based on merchant-customer relationships",
      "type": "customer-specific handling"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 3: River Health Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:26:49

### Original Content
```
- Kobby is very nice, calm, business focused but smiles and talks about his weekend too 2) Is there a key POC: (i e : who is the buyer decision maker ) - Kobby 3) What are the Tabs features that the key POC cares about - all of them - especially automatic invoice creation and ability to schedule invoices, collections process including dunning
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder relationship management and communication style",
    "Decision-maker identification and authority",
    "Product feature prioritization and requirements",
    "Invoicing and billing automation",
    "Collections and payment management processes"
  ],
  "rules": [
    {
      "rule": "Primary point of contact is Kobby, who serves as the buyer decision maker",
      "category": "stakeholder_management",
      "explicit": true
    },
    {
      "rule": "Communication approach should balance business focus with personal rapport (weekend discussions, friendly demeanor)",
      "category": "communication_style",
      "explicit": true
    },
    {
      "rule": "All Tabs features are important to the key POC",
      "category": "product_requirements",
      "explicit": true
    },
    {
      "rule": "Automatic invoice creation functionality must be prioritized",
      "category": "invoicing",
      "explicit": true
    },
    {
      "rule": "Invoice scheduling capability must be available",
      "category": "invoicing",
      "explicit": true
    },
    {
      "rule": "Collections process including dunning functionality must be implemented",
      "category": "payment_collections",
      "explicit": true
    },
    {
      "rule": "Maintain calm and nice demeanor with smiles during interactions with Kobby",
      "category": "communication_style",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "While all features matter, automatic invoice creation, invoice scheduling, and collections/dunning receive special emphasis",
      "condition": "Feature prioritization hierarchy exists despite stating 'all of them'"
    }
  ],
  "merchant_specific": [
    {
      "element": "Kobby as named decision maker",
      "type": "personnel",
      "customizable": true,
      "note": "Specific individual name - would vary by merchant"
    },
    {
      "element": "Communication style preferences (nice, calm, business focused with personal touches)",
      "type": "relationship_approach",
      "customizable": true,
      "note": "Individual personality traits requiring tailored interaction approach"
    },
    {
      "element": "Feature priority emphasis (automatic invoicing, scheduling, dunning)",
      "type": "product_configuration",
      "customizable": true,
      "note": "Specific feature priorities may vary by merchant needs"
    }
  ],
  "confidence_score": 0.92
}
```

---

