# Raw LLM Analysis: FIF MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:58:57

---

## Chunk 1: FIF MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:58:57

### Original Content
```
This would mean that it is a duplicate and does not need to be processed Examples of what the email will look like are below There are 3 potential formats, all with the same information Notes Sections [Ops International Team to Ignore] (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills 1) What is the merchant temperament 3) What are the Tabs features that the key POC cares about
```

### LLM Analysis Response
```json
{
  "themes": [
    "Duplicate detection and processing workflow",
    "Email format standardization and documentation",
    "Internal team coordination and role assignment",
    "Merchant relationship management and profiling",
    "Feature prioritization and stakeholder engagement"
  ],
  "rules": [
    "Duplicate items should not be processed",
    "There are 3 potential email formats containing the same information",
    "Ops International Team should ignore specific sections marked for them",
    "Account Executive (AE) is responsible for initial information filling",
    "Implementation team serves as the completion DRI (Directly Responsible Individual) during handoff",
    "Documentation must include information on merchant billing methods",
    "Documentation must capture merchant temperament assessment",
    "Documentation must identify which Tabs features the key POC (Point of Contact) prioritizes"
  ],
  "exceptions": [
    "Sections marked '[Ops International Team to Ignore]' are excluded from certain team workflows",
    "AE fills information conditionally ('if they have'), suggesting optional or availability-dependent data entry",
    "Implementation team takes over completion responsibility specifically at handoff stage"
  ],
  "merchant_specific": [
    "Merchant billing methodology varies by merchant",
    "Merchant temperament is individualized and requires assessment",
    "Key POC feature preferences differ per merchant",
    "Tabs features of interest are merchant-dependent",
    "POC identification and relationship dynamics are merchant-specific"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document chunk appears to be fragmented or mid-section, making complete context difficult to establish. The content references processes and formats without fully explaining them, and contains incomplete sentence structures. However, the core operational workflow elements (duplicate handling, team responsibilities, merchant profiling requirements) are reasonably clear.

---

## Chunk 2: FIF MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:59:01

### Original Content
```
Merchant Name (AE to fill) Implementation POC: (AE to fill) CX POC: Charlie They have QBO Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Not a normal B2B membership model where individual people are part of the collective They are just starting to charge membership fees Information on how merchant bills Membership fees and sponsorships How contract is broken up No contracts One off things to know about ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Customer Processing Workflow",
    "Billing Configuration and Revenue Recognition",
    "Integration Item Management and Classification",
    "Communication and Notification Protocols",
    "Alternative Processing Methods for Future Implementation"
  ],
  "rules": [
    "Process contracts approximately once a week from received sheets",
    "Each row on the sheet must be added as a new customer",
    "Add document for each customer as a 'contract'",
    "Create Billing Terms (BT) according to amount and frequency on sheet",
    "Use 'FIF Collective Membership' as the Name field",
    "Use 'Membership Fees' as the Integration Item",
    "Set start date as January 1, 2025 for revenue schedule and BT",
    "Support two frequency options: Annual (1 yearly) or Monthly (12 monthly)",
    "Set Net terms to 0",
    "Default Service Term is 1 Year if none listed",
    "Default Net Payment Terms is 0 if none listed",
    "Default Billing Frequency is Monthly if none listed",
    "Every tax line item becomes a BT (default handling)",
    "Do not create duplicate customers - check if customer already exists before creating new one",
    "Merchant has no contracts (one-off arrangement)",
    "Merchant uses QBO (QuickBooks Online)",
    "Partnership arrangement: Tabs uses service for free as official partner"
  ],
  "exceptions": [
    "Not a normal B2B membership model - individual people are part of collective",
    "Merchant is just starting to charge membership fees",
    "No contracts exist for this merchant (unusual arrangement)",
    "Partnership with Tabs involves free service usage",
    "Alternative processing method exists in Appendix but does NOT currently apply",
    "Future state: May receive email notifications to contract-ingest for new members instead of sheets",
    "Some customer addresses may be international",
    "Email address fields may be blank - if so, leave blank",
    "On rare occasions, customer may already exist - do not create duplicate"
  ],
  "merchant_specific": [
    "Merchant Name: FIF Collective (to be filled by AE)",
    "CX POC: Charlie",
    "Billing model: Membership fees and sponsorships",
    "Integration Item label: 'Membership Fees'",
    "Contract Name: 'FIF Collective Membership'",
    "Specific start date: January 1, 2025",
    "Partnership arrangement with Tabs",
    "Weekly processing cadence for this merchant",
    "Sheet-based intake process (current state)",
    "Email-based intake process (future state, not currently active)",
    "Customer type: Members of a collective rather than traditional B2B customers"
  ],
  "confidence_score": 0.92
}
```

---

