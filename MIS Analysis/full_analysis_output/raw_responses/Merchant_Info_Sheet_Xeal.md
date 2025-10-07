# Raw LLM Analysis: Merchant Info Sheet - Xeal

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:39:43

---

## Chunk 1: Merchant Info Sheet - Xeal_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:39:43

### Original Content
```
Xeal Energy MSA Signature Date: Feb 1, 2024 Onboarding Kick Off Date: May 1, 2024 Go Live Date: Jul 15, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Carl Rojas RevOps: Joan Dunne Company summary Xeal sells electric car chargers to apartment buildings They charge for the hardware and also charge an annual license for the software Drivers Goals (North star) What is the merchant's goal What pain are we solving Why are they buying Tabs Is there an opt ou...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Identification and Relationship Management",
    "Billing Model and Contract Structure",
    "Default Operational Parameters and Processing Rules",
    "Customer Success and Retention Strategy"
  ],
  "rules": [
    "Default Service Term: 1 Year (if none listed in contract)",
    "Default Net Payment Terms: 0 days (if none listed in contract)",
    "Default Billing Frequency: Monthly (if none listed in contract)",
    "Contract processing must identify and document opt-out clauses",
    "Tax handling must be specified as line item treatment",
    "ERP and Tax Integration systems must be documented during onboarding",
    "Key personnel roles must be identified: Accountant and RevOps contacts",
    "Implementation requires documented GTM POC and Implementation POC",
    "Merchant temperament assessment is required for relationship management",
    "Contract processing may require merchant-specific date handling (e.g., back-dating invoices)",
    "Billing model must document how contracts are broken up/structured",
    "Customer creation process variations must be documented per merchant"
  ],
  "exceptions": [
    "Invoice dates may need to be back-dated to final day of month (merchant-specific request)",
    "Some contract elements may need to be ignored during processing (to be specified per merchant)",
    "Opt-out clauses require special tracking and success metrics to prevent exercise",
    "Processing steps may differ by individual contract within same merchant account",
    "Unique customer creation processes may override standard procedures"
  ],
  "merchant_specific": [
    "Company business model: Xeal Energy sells EV chargers to apartment buildings with hardware + annual software license revenue model",
    "Key contacts: Carl Rojas (Accountant), Joan Dunne (RevOps)",
    "Timeline: MSA signed Feb 1 2024, Onboarding May 1 2024, Go Live Jul 15 2024",
    "Merchant's North Star goals and pain points being solved",
    "Tabs platform features that specific POCs care about",
    "Decision maker identification and buyer hierarchy",
    "Relationship temperament and communication preferences",
    "Contract structure and one-off billing peculiarities",
    "Specific ERP and tax integration system choices"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Xeal_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:39:54

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) Any important information on events billing Integration Items Processing (if necessary) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merchant Post Processing Communications (if necessary) Does Ops Team n...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax Line Item Processing and Default Operations",
    "Integration Items Classification and Labeling",
    "Post-Processing Communication and Notification Protocols",
    "Customer-Specific Information and Invoice Customization",
    "Feature Requests and Call Review Management"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: Every tax line item becomes a BT Events Processing when none is specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Integration items must be assigned specific labels based on the integration type",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Processing",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication",
      "explicit": true
    },
    {
      "rule": "Notifications should specify who needs to be notified, where (communication channel), and when (trigger event)",
      "category": "Communication",
      "explicit": true
    },
    {
      "rule": "Special memos may be required for certain customer invoices based on merchant-customer relationships",
      "category": "Customer Management",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if specifically noted by the merchant",
      "condition": "Merchant provides alternative labeling instructions"
    },
    {
      "exception": "Tax line item processing may deviate from BT Events Processing default if specific instructions are listed",
      "condition": "When alternative tax processing instructions are provided"
    },
    {
      "exception": "Invoice changes may be required due to specific merchant-customer relationships",
      "condition": "Special customer relationships exist"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling rules",
      "customization_needed": "Each merchant may have different integration types (e.g., Statsig, Pinata) requiring unique labels",
      "examples": ["Statsig → Sales", "Pinata → Software Subscription Bundle"]
    },
    {
      "element": "Post-processing notification recipients",
      "customization_needed": "Specific team members and channels vary by merchant",
      "examples": ["Customer Success (Azmat Aziz) via Messari internal merchant channel"]
    },
    {
      "element": "Notification timing and triggers",
      "customization_needed": "When notifications occur depends on merchant phase and processing stage",
      "examples": ["When contracts are processed in Active phase"]
    },
    {
      "element": "Customer-specific invoice requirements",
      "customization_needed": "Special memos and invoice modifications based on individual customer relationships"
    },
    {
      "element": "Events billing processing requirements",
      "customization_needed": "May vary based on merchant needs and tax structure"
    },
    {
      "element": "Feature requests tracking",
      "customization_needed": "Merchant-specific feature needs with urgency levels"
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document appears to be a template or form with placeholders and examples rather than complete instructions. The structure is clear, but some sections contain incomplete information (e.g., "FR 1 What is it Why it's important" without actual content). The examples provided (Statsig, Pinata, Azmat Aziz) are concrete, but the overall context suggests this is a framework to be filled in per merchant rather than a complete set of instructions. The confidence score reflects this uncertainty about whether all rules and patterns have been fully captured.

---

