# Raw LLM Analysis: Kat_s [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:36:22

---

## Chunk 1: Kat_s [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:36:22

### Original Content
```
Merchant Demo date: Scoping start date: MSA Signature Date: Onboarding Kick Off Date: [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Notes Sections (AE  Implementation to fill) Info on how merchant bills Is there any important merchant relationship information What is the merchant temperament Is there a key POC: (i e : who is the buyer decision maker ) What are the Tabs features that the key POC cares about Company summary (AE to...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Stakeholder Identification and Relationship Management",
    "Merchant Goals and Pain Points",
    "Billing and Contract Structure",
    "Contract Processing Procedures"
  ],
  "rules": [
    "Document must capture key dates: Demo date, Scoping start date, MSA Signature Date, Onboarding Kick Off Date, Opt Out Date (if exists), and Go Live Date",
    "Must identify GTM POC and Implementation POC for each merchant",
    "ERP and Tax Integration systems must be documented",
    "Key people at merchant must be identified and documented",
    "Merchant billing process must be documented",
    "Decision maker (buyer POC) must be identified",
    "Tabs features relevant to key POC must be documented",
    "Company summary describing what the company does is required",
    "North star goals must be documented by AE and Implementation teams",
    "Pain points being solved must be clearly stated",
    "Reason for purchasing Tabs must be documented",
    "Opt-out clause existence and conditions must be documented",
    "Customer creation process unique characteristics must be noted",
    "Contract structure breakdown must be documented",
    "Contract processing steps must be defined by Implementation Success team",
    "Items to ignore in contracts must be specified",
    "Contract-specific processing variations must be documented"
  ],
  "exceptions": [
    "Opt Out Date is conditional - only required 'If Exists'",
    "Opt-out clause may or may not exist for each merchant",
    "One-off merchant-specific requirements may exist that differ from standard processes",
    "Contract processing specifics may differ by individual contract within the same merchant",
    "Certain contract elements may need to be ignored during processing (merchant-specific)"
  ],
  "merchant_specific": [
    "Merchant temperament assessment",
    "Merchant relationship information",
    "Unique customer creation process per merchant",
    "How merchant bills (billing methodology)",
    "Contract breakdown structure varies by merchant",
    "One-off merchant requirements",
    "Specific Tabs features that matter to each merchant's key POC",
    "Merchant-specific contract processing steps",
    "Items to ignore in contracts (varies by merchant)",
    "ERP system type",
    "Tax Integration system type",
    "Opt-out conditions and thresholds",
    "North star goals unique to each merchant"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Kat_s [MAKE A COPY DO NOT EDIT] Merchant Info Sheet - Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:36:25

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementa...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Invoice and billing configuration standards",
    "Cross-team communication and notification protocols",
    "Merchant-specific customization and customer handling",
    "Implementation workflow and processing procedures"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "specificity": "always"
    },
    {
      "rule": "Default Service Term is 1 Year when none is listed",
      "category": "Service Configuration",
      "specificity": "default"
    },
    {
      "rule": "Default Net Payment Terms is 0 when none is specified",
      "category": "Payment Terms",
      "specificity": "default"
    },
    {
      "rule": "Default Billing Frequency is Monthly when none is listed",
      "category": "Billing Configuration",
      "specificity": "default"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "specificity": "default"
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication Protocol",
      "specificity": "conditional"
    },
    {
      "rule": "Notifications should specify who, where, and when communication occurs",
      "category": "Communication Protocol",
      "specificity": "required"
    }
  ],
  "exceptions": [
    {
      "exception": "Events billing processing may be necessary based on merchant requirements",
      "condition": "if necessary",
      "responsibility": "Implementation Success to fill"
    },
    {
      "exception": "Integration items processing may be required for specific merchants",
      "condition": "if necessary",
      "responsibility": "Implementation Success to fill"
    },
    {
      "exception": "Post-processing communications may be needed depending on merchant",
      "condition": "if necessary",
      "responsibility": "Implementation Success to fill"
    },
    {
      "exception": "Special memos may be required for certain invoices based on customer relationships",
      "condition": "merchant-specific customer information",
      "responsibility": "varies"
    },
    {
      "exception": "Invoice changes may occur due to merchant-customer relationship dynamics",
      "condition": "relationship-dependent",
      "responsibility": "varies"
    }
  ],
  "merchant_specific": [
    {
      "element": "Events billing instructions",
      "customization_level": "high",
      "notes": "Requires Implementation Success team input per merchant"
    },
    {
      "element": "Integration items assignment instructions",
      "customization_level": "high",
      "notes": "Merchant-specific integration requirements"
    },
    {
      "element": "Notification recipients and channels",
      "customization_level": "high",
      "notes": "Example shows Customer Success contact and internal merchant channel specifics"
    },
    {
      "element": "Customer-specific information and invoice memos",
      "customization_level": "high",
      "notes": "Varies by merchant's customer base and relationships"
    },
    {
      "element": "Feature requests tracking",
      "customization_level": "medium",
      "notes": "Requires AE and Implementation Success collaboration per merchant"
    },
    {
      "element": "Rewatch calls schedule",
      "customization_level": "medium",
      "notes": "Date-specific per merchant implementation"
    },
    {
      "element": "Merchant phase designation (Implementation vs Active)",
      "customization_level": "medium",
      "notes": "Affects when notifications are triggered"
    }
  ],
  "confidence_score": 0.85
}
```

---

