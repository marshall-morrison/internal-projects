# Raw LLM Analysis: MIS Search Engine Template

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:53:23

---

## Chunk 1: MIS Search Engine Template_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:23

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] [Cell 27]Customer Information Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests FR 1 What is it Why it's important Urgency [Cell 28]Rewatch Calls Rewatch by dates
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder notification and communication protocols",
    "Merchant lifecycle management and contract processing",
    "Customer relationship management and documentation",
    "Feature request tracking and prioritization",
    "Call review and documentation processes"
  ],
  "rules": [
    "Customer Success team member (Azmat Aziz) must be notified when contracts are processed",
    "Notifications should be sent to Messari internal merchant channel",
    "Notifications are triggered during the 'Active' merchant phase",
    "Customer information section must document important specifics about merchant customers",
    "Special memos are required for certain invoices",
    "Invoice modifications must be tracked when they relate to merchant-customer relationships",
    "Feature requests must include: description (What is it), justification (Why it's important), and urgency level",
    "Calls must be reviewed and documented with associated dates in Rewatch"
  ],
  "exceptions": [
    "Certain invoices require special memos (criteria not specified in this chunk)",
    "Invoice changes may occur due to merchant-customer relationship dynamics",
    "Feature request urgency levels may vary (specific thresholds not defined)"
  ],
  "merchant_specific": [
    "Customer Success contact person (currently Azmat Aziz, may vary by merchant)",
    "Internal communication channel (Messari internal merchant channel, may differ)",
    "Specific customer information requirements may vary per merchant",
    "Special memo requirements for invoices are likely merchant-dependent",
    "Feature requests may be unique to each merchant's needs",
    "Contract processing triggers may vary based on merchant phase"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for Confidence Score (0.65):**
- The document chunk appears fragmented with cell references and incomplete sentences
- Some context is missing (e.g., what triggers special memos, specific urgency criteria)
- The structure suggests this is part of a larger template or spreadsheet
- Clear elements are identifiable, but relationships between components are partially unclear
- Merchant-specific vs. universal rules are somewhat ambiguous without additional context

---

## Chunk 2: MIS Search Engine Template_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:53:32

### Original Content
```
Merchant [Cell 1]Demo date: [Cell 2]Scoping start date: Nov 6, 2023 [Cell 3]MSA Signature Date: Feb 7, 2024 [Cell 4]Onboarding Kick Off Date: Feb 7, 2024 [Cell 5]Go Live Date: Feb 7, 2024 [Cell 6]GTM POC: [Cell 7]Implementation POC: [Cell 8]ERP: [Cell 9]Tax Integration: [Cell 10]Key people at Merchant Accountant: CFO: Customer service rep who is really involved: Account Receivable POC Billing POC etc [Cell 11]Company summary Summary of what company does Goals [Cell 12]What is the merchant's goal...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Stakeholder Identification and Relationship Management",
    "Contract Processing and Billing Configuration",
    "Integration and Technical Setup Requirements",
    "Communication and Notification Protocols"
  ],
  "rules": [
    {
      "rule_id": "DEFAULT_SERVICE_TERM",
      "description": "If no service term is listed in contract, operations default is 1 Year",
      "cell_reference": "Cell 22"
    },
    {
      "rule_id": "DEFAULT_NET_PAYMENT",
      "description": "If no net payment terms specified, operations default is 0 (net zero/immediate payment)",
      "cell_reference": "Cell 23"
    },
    {
      "rule_id": "DEFAULT_BILLING_FREQUENCY",
      "description": "If no billing frequency is listed, operations default is Monthly",
      "cell_reference": "Cell 24"
    },
    {
      "rule_id": "MILESTONE_TRACKING",
      "description": "Track key dates: Demo, Scoping start, MSA Signature, Onboarding Kick Off, and Go Live dates",
      "cell_reference": "Cells 1-5"
    },
    {
      "rule_id": "STAKEHOLDER_DOCUMENTATION",
      "description": "Document key merchant personnel including Accountant, CFO, Customer Service Rep, AR POC, and Billing POC",
      "cell_reference": "Cell 10"
    },
    {
      "rule_id": "INTEGRATION_LABELING",
      "description": "Integration items must be properly labeled according to merchant-specific instructions",
      "cell_reference": "Cell 26"
    },
    {
      "rule_id": "CONTRACT_PROCESSING_STEPS",
      "description": "Follow documented steps to process contracts and identify items to ignore",
      "cell_reference": "Cells 18-19"
    },
    {
      "rule_id": "POST_PROCESSING_NOTIFICATION",
      "description": "Notify designated team members upon completion of processing batches during Implementation or Active phase",
      "cell_reference": "Cell 26"
    }
  ],
  "exceptions": [
    {
      "exception_id": "MERCHANT_SPECIFIC_PROCESSING",
      "description": "Some merchants may request specific processing variations (e.g., always back-date invoice date to final day of the month)",
      "cell_reference": "Cell 21"
    },
    {
      "exception_id": "OPT_OUT_CLAUSE",
      "description": "Some contracts may contain opt-out clauses requiring specific conditions to be met to prevent exercise",
      "cell_reference": "Cell 13"
    },
    {
      "exception_id": "CONTRACT_ITEMS_TO_IGNORE",
      "description": "Certain contract elements may need to be ignored during processing based on merchant-specific instructions",
      "cell_reference": "Cell 19"
    },
    {
      "exception_id": "UNIQUE_BILLING_MODEL",
      "description": "Merchants may have unique billing models, contract structures, or customer creation processes",
      "cell_reference": "Cell 17"
    },
    {
      "exception_id": "INTEGRATION_LABELING_EXCEPTIONS",
      "description": "Integration items may have specific labeling requirements that differ by merchant (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
      "cell_reference": "Cell 26"
    }
  ],
  "merchant_specific": [
    {
      "element": "ERP System",
      "description": "Each merchant may use different ERP systems",
      "cell_reference": "Cell 8"
    },
    {
      "element": "Tax Integration",
      "description": "Tax integration setup varies by merchant",
      "cell_reference": "Cell 9"
    },
    {
      "element": "Company Summary and Goals",
      "description": "Merchant-specific business description, goals, pain points, and purchase motivations",
      "cell_reference": "Cell 11-12"
    },
    {
      "element": "Merchant Temperament",
      "description": "Relationship management approach tailored to merchant personality and communication style",
      "cell_reference": "Cell 14"
    },
    {
      "element": "Key POC and Decision Maker",
      "description": "Identification of primary buyer/decision maker varies by merchant",
      "cell_reference": "Cell 15"
    },
    {
      "element": "Feature Priorities",
      "description": "Specific product features that key POCs care about differ by merchant",
      "cell_reference": "Cell 16"
    },
    {
      "element": "Billing Model Details",
      "description": "How merchant bills customers, contract structure, and unique billing considerations",
      "cell_reference": "Cell 17"
    },
    {
      "element": "Events Processing",
      "description": "Merchant-specific instructions for events billing when applicable",
      "cell_reference": "Cell 25"
    },
    {
      "element": "Integration Item Labeling",
      "description": "Merchant-specific rules for categorizing and labeling integration items",
      "cell_reference": "Cell 26"
    },
    {
      "element": "Post-Processing Notifications",
      "description": "Merchant-specific notification requirements and recipients",
      "cell_reference": "Cell 26"
    },
    {
      "element": "GTM and Implementation POCs",
      "description": "Designated points of contact for go-to-market and implementation phases",
      "cell_reference": "Cells 6-7"
    }
  ],
  "confidence_score": 0.92
}
```

---

