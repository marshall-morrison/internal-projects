# Raw LLM Analysis: Merchant Info Sheet - Satisfi Labs(1)

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:55:23

---

## Chunk 1: Merchant Info Sheet - Satisfi Labs(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:23

### Original Content
```
1) What is the merchant temperament 2) Is there a key POC: (i e : who is the buyer decision maker ) 3) What are the Tabs features that the key POC cares about
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant relationship assessment and profiling",
    "Stakeholder identification and decision-making hierarchy",
    "Product feature prioritization and value proposition alignment",
    "Customer discovery and needs analysis"
  ],
  "rules": [
    "Must identify and document the merchant's temperament/personality type",
    "Must identify the key Point of Contact (POC) who serves as the buyer decision maker",
    "Must determine which Tabs product features are most important to the key POC",
    "Analysis should focus on the decision-maker's specific feature preferences rather than general merchant needs"
  ],
  "exceptions": [
    "The document does not specify what to do if there are multiple decision makers",
    "No guidance provided for situations where the POC and decision maker are different individuals",
    "No fallback process if merchant temperament cannot be clearly determined"
  ],
  "merchant_specific": [
    "Merchant temperament - varies by individual merchant and requires custom assessment",
    "Key POC identity - specific individual names and roles will differ per merchant",
    "Feature preferences - different merchants/POCs will prioritize different Tabs features based on their business needs",
    "Decision-making structure - may vary significantly across different merchant organizations"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Satisfi Labs(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:55:30

### Original Content
```
Merchant Demo date: Scoping start date: Nov 6, 2023 MSA Signature Date: Feb 7, 2024 Onboarding Kick Off Date: Feb 7, 2024 [If Exists] Opt Out Date: Oct Go Live Date: Feb 7, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC Etc Company summary (AE to fill) Summary of what company does Goals (North star) (AE  Implementation to fill) What is the merchant's goal What pain are...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Contract Processing and Billing Configuration",
    "Stakeholder Management and Communication",
    "Integration and Tax Handling Procedures",
    "Operational Defaults and Customization Requirements"
  ],
  "rules": [
    "Default Service Term: 1 Year (if none listed in contract)",
    "Default Net Payment Terms: 0 days (if none listed in contract)",
    "Default Billing Frequency: Monthly (if none listed in contract)",
    "Default Tax Handling: Every tax line item becomes a BT (Billable Transaction) if not specified",
    "Implementation Success team must fill contract processing steps section",
    "AE and Implementation teams jointly responsible for filling Goals, Billing Model, and Feature Requests sections",
    "Ops International Team should ignore specific sections marked for their exclusion",
    "Post-processing communications must specify who needs notification, where, and when",
    "Integration items must be labeled according to merchant-specific instructions",
    "Contract processing may require ignoring certain contract elements as specified",
    "Events billing processing required when necessary with specific instructions",
    "Customer Success notifications required during Active phase for certain merchants"
  ],
  "exceptions": [
    "Contract-specific processing variations (e.g., back-dating invoice dates to final day of month)",
    "Opt-out clauses may exist with specific merchant requirements to prevent exercise",
    "One-off merchant-specific billing or processing requirements",
    "Special memos required for certain customer invoices",
    "Invoice changes based on merchant-customer relationship dynamics",
    "Unique customer creation processes for specific merchants",
    "Integration item labeling exceptions (e.g., Statsig vs Pinata labeling rules)",
    "Contract structure variations requiring different processing approaches"
  ],
  "merchant_specific": [
    "Merchant Demo date and Go Live Date",
    "MSA Signature Date and Onboarding Kick Off Date",
    "Opt Out Date and clause conditions",
    "Key personnel (Accountant, CFO, Customer Service Rep, AR POC, Billing POC)",
    "GTM POC and Implementation POC assignments",
    "ERP and Tax Integration systems used",
    "Company summary and business description",
    "North star goals and pain points being solved",
    "Billing model specifics and contract structure",
    "Service terms, payment terms, and billing frequency (if different from defaults)",
    "Tax handling methodology",
    "Events billing requirements",
    "Integration item labeling conventions",
    "Post-processing notification requirements and recipients",
    "Customer-specific information and special invoice requirements",
    "Feature requests with urgency levels",
    "Rewatch call recordings and notes",
    "Merchant relationship information and implementation spreadsheets"
  ],
  "confidence_score": 0.95
}
```

---

