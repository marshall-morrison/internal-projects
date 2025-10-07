# Raw LLM Analysis: MIS Revamp [Changes]

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:38:50

---

## Chunk 1: MIS Revamp [Changes]_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:38:50

### Original Content
```
2) Is there a key POC: (i e : who is the buyer decision maker ) 3) What are the Tabs features that the key POC cares about (
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder identification and decision-making authority",
    "Point of contact (POC) determination",
    "Product feature prioritization and requirements gathering",
    "Customer needs assessment",
    "Sales qualification process"
  ],
  "rules": [
    "Must identify if there is a key Point of Contact (POC)",
    "Must determine who the buyer decision maker is",
    "Must identify which Tabs features the key POC cares about",
    "Decision maker identification is a required qualification step",
    "Feature preferences should be mapped to the key POC's interests"
  ],
  "exceptions": [
    "Implicit exception: scenarios where there may not be a single key POC",
    "Potential for multiple decision makers or committee-based decisions (not explicitly addressed)",
    "Cases where POC may not be the ultimate decision maker"
  ],
  "merchant_specific": [
    "The term 'Tabs features' appears to be product-specific and would need to be replaced with relevant product/service features for different merchants",
    "The definition of 'key POC' may vary by merchant's organizational structure",
    "Decision-making hierarchy and authority levels vary by merchant organization",
    "Specific features that matter will be unique to each merchant's product offering",
    "The qualification criteria for 'buyer decision maker' may differ across merchant types"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document chunk is fragmentary and appears to be part of a larger questionnaire or checklist. The incomplete sentences and numbered format suggest this is an excerpt from a more comprehensive document. While the intent is clear (qualifying sales opportunities by identifying decision makers and their feature preferences), the lack of complete context and detailed instructions limits confidence in capturing all nuances and rules.

---

## Chunk 2: MIS Revamp [Changes]_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:38:58

### Original Content
```
Merchant [Demo date: Nov 14, 2024] - Axe data point Scoping start date: Nov 14, 2024-Delete from MIS MSA Signature Date: Nov 14, 2024-Delete from MIS Onboarding Kick Off Date: Nov 14, 2024-Delete from MIS [If Exists] Opt Out Date: Oct-Delete from MIS Go Live Date: Nov 14, 2024-Delete from MIS, Need to add in Hubspot GTM POC: Implementation POC: CX POC: [IMP to Add[ ERP: [Delete from MIS] Tax Integration: [delete from MIS] Key people at Merchant [Every contact associated with a deal in Hubspot in...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Data Migration and Cleanup - Removing specific data points from MIS (Management Information System) and adding to HubSpot",
    "Stakeholder Management - Identifying and tracking key personnel (POCs) across different functional areas",
    "Contract Processing and Billing Configuration - Establishing default terms, billing models, and processing instructions",
    "Integration and System Setup - Managing ERP, tax integrations, and third-party integration item labeling",
    "Communication Protocols - Defining notification requirements and post-processing workflows"
  ],
  "rules": [
    "Delete the following date fields from MIS: Demo date, Scoping start date, MSA Signature Date, Onboarding Kick Off Date, Opt Out Date, Go Live Date",
    "Add Go Live Date to HubSpot instead of MIS",
    "Delete ERP and Tax Integration fields from MIS",
    "Delete all key personnel contacts from MIS (Accountant, CFO, Customer service rep, AR POC, Billing POC)",
    "Store all contacts associated with a deal in HubSpot instead of MIS",
    "Default Service Term: 1 Year (if none listed)",
    "Default Net Payment Terms: 0 days (if none listed)",
    "Default Billing Frequency: Monthly (if none listed)",
    "Default Tax Line Item Handling: Every tax line item becomes a BT (Billable Tax) (if none listed)",
    "AE (Account Executive) is responsible for filling company summary and merchant temperament",
    "AE and Implementation team jointly fill Goals/North star section",
    "Implementation Success team fills Contract Processing Steps, Events Processing, Integration Items Processing, Post Processing Communications, and Customer Information",
    "Implementation team fills Billing model section",
    "AE and Implementation Success jointly fill Feature Requests and Rewatch Calls sections",
    "Ops International Team should ignore Notes Sections"
  ],
  "exceptions": [
    "Opt Out Date field should only be deleted 'If Exists'",
    "Contract processing may have merchant-specific variations (e.g., 'always back-date invoice date to final day of the month')",
    "Integration items may have special labeling rules per merchant (e.g., 'All Statsig integration items should be labeled as Sales')",
    "Some merchants may have unique customer creation processes",
    "Post-processing notifications are conditional - only required 'if necessary'",
    "Events Processing section only applies 'if necessary'",
    "Integration Items Processing only applies 'if necessary'",
    "Certain invoices may require special memos based on merchant-customer relationships",
    "Invoice changes may be needed due to specific merchant-customer relationships"
  ],
  "merchant_specific": [
    "Company summary describing what the company does",
    "Merchant's goals and pain points being solved",
    "Opt out clause details and conditions",
    "Unique customer creation process requirements",
    "Merchant-specific billing model and contract structure",
    "One-off processing requirements",
    "Contract processing steps and items to ignore",
    "Specific contract processing requests that differ by contract",
    "Events billing information (if applicable)",
    "Integration item labeling instructions (e.g., Statsig, Pinata examples)",
    "Post-processing notification requirements (who, where, when)",
    "Customer-specific information and special invoice requirements",
    "Feature requests with urgency levels",
    "Merchant temperament assessment",
    "GTM POC, Implementation POC, and CX POC assignments"
  ],
  "confidence_score": 0.92
}
```

---

