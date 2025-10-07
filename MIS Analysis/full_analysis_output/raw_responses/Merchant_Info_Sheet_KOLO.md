# Raw LLM Analysis: Merchant Info Sheet - KOLO

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:12:36

---

## Chunk 1: Merchant Info Sheet - KOLO_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:36

### Original Content
```
Do not process until receiving this list Please create a Customer with the provided name if one does not exist and assign the contract to that new customer GP Kolo contracts tend to be written in a very confusing way Most of the terms can be ignored The bullets below explain what we should keep One billing term for  Subscription fee  with a FLAT_PRICE of the total monthly amount This billing term should be monthly and billed for the stated number of months The quantity should be the  total estim...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract processing workflow and prerequisites",
    "Customer and contract creation procedures",
    "Billing term configuration and pricing structure",
    "Timeline management for project start and billing dates",
    "Fee and term exclusions"
  ],
  "rules": [
    "Do not process contract until receiving a specific list",
    "Create a new Customer with provided name if one does not exist",
    "Assign contract to the newly created customer",
    "Create one billing term labeled 'Subscription fee' with FLAT_PRICE type",
    "Use the total monthly amount as the flat price value",
    "Set billing term to monthly frequency",
    "Bill for the stated number of months in the contract",
    "Set quantity to the 'total estimated devices'",
    "Projects start months after initial contract signature date",
    "Use billing start dates from separately provided Excel sheet",
    "For first 50 contracts, use dates from Excel sheet",
    "If no stated go-live date exists, assume 3 months between contract signing and first billing",
    "Ignore all taxes",
    "Ignore all implementation fees",
    "Ignore all early termination fees",
    "Ignore all ramp-up terms or clauses that change price mid-term"
  ],
  "exceptions": [
    "First 50 contracts require manual date entry from Excel sheet",
    "After first 50 contracts, GP Kolo will update dates independently",
    "Default 3-month delay rule only applies when no go-live date is stated",
    "GP Kolo contracts are written in a confusing way requiring selective interpretation"
  ],
  "merchant_specific": [
    "Merchant name: GP Kolo",
    "GP Kolo-specific contract interpretation guidelines",
    "GP Kolo provides separate Excel sheet for billing start dates",
    "GP Kolo will self-manage date updates after initial 50 contracts",
    "Terminology: 'total estimated devices' as quantity metric",
    "GP Kolo's contract writing style requires filtering most terms",
    "Reference to onboarding documentation specific to this merchant"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - KOLO_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:38

### Original Content
```
Merchant Scoping start date: Sep 1, 2023 Implementation Completed Date (Go live date): May 16, 2024 MSA Signature Date: Apr 30, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Trevor Wade - head of customer ops   business generalist (sort of a GM type) - super friendly, loves Tabs, has been pushing really hard to get us into the org for over a year Company summary Georgia Pacific KOLO is a start-up business unit within GP KOLO manufactures sensor-enabled (IoT) devices for paper towels...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Limited Trial Implementation - Contract Processing Only",
    "Strategic Customer Advocacy and Internal Sales Journey",
    "IoT Hardware/Software Business Model for Facility Management",
    "Deferred ERP Integration and Invoicing Capabilities",
    "Customer Data Mapping and Naming Convention Challenges"
  ],
  "rules": [
    "Implementation scope limited to contract processing capabilities only",
    "No invoicing functionality to be used during trial period",
    "No ERP (SAP) integration required during evaluation phase",
    "Customer names must be mapped using separate Excel sheet provided by merchant",
    "Contract processing reporting must be provided as part of evaluation",
    "MSA must be signed before go-live (signed Apr 30, 2024, go-live May 16, 2024)",
    "Scoping process must occur before implementation (started Sep 1, 2023)"
  ],
  "exceptions": [
    "This is an evaluation/trial contract rather than full implementation",
    "Standard ERP integration is explicitly excluded for this merchant",
    "Standard invoicing workflow is disabled for this engagement",
    "Customer naming conventions are non-standard and require external mapping documentation",
    "Implementation timeline is unusually long (8+ months from scoping to go-live) suggesting complex stakeholder management"
  ],
  "merchant_specific": [
    "Merchant is a startup business unit (KOLO) within larger parent company (Georgia Pacific)",
    "Product line: IoT-enabled paper towel and toilet paper dispensers with software app",
    "Target customers: high-traffic establishments (offices, stadiums, airports)",
    "Key stakeholder: Trevor Wade (head of customer ops, internal champion)",
    "ERP system: SAP (not integrated)",
    "CRM system: Salesforce (SFDC team is competitive alternative for in-house build)",
    "Business model: Hardware + Software (HW SW) use case",
    "Value proposition: Cost savings and guest experience for janitorial operations",
    "Customer naming: Non-obvious from contracts, requires separate Excel mapping",
    "Internal competition: SFDC team attempting to build solution in-house"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - KOLO_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:12:47

### Original Content
```
com video b5mq8hxl5k71rc6l-gp-kolo-tabs-kickoff-may-8-2024 Onboarding v2: https: tabs rewatch com video pgwzat35n5pj10k6-trevor-wade-and-arjun-gopalratnam-may-16-2024
```

### LLM Analysis Response
```json
{
  "themes": [
    "Onboarding process documentation",
    "Video-based training materials",
    "Internal knowledge management and reference materials",
    "Team collaboration and kickoff meetings"
  ],
  "rules": [
    "Onboarding materials are version-controlled (indicated by 'v2')",
    "Training sessions are recorded and stored in Rewatch platform",
    "Video references include specific identifiers for tracking and retrieval",
    "Onboarding involves multiple sessions with different participants (kickoff and follow-up sessions)"
  ],
  "exceptions": [
    "No explicit exceptions or special cases identified in this document chunk",
    "The fragment nature of this content suggests conditional access based on role or onboarding stage"
  ],
  "merchant_specific": [
    "Video platform: 'tabs.rewatch.com' - may vary by organization",
    "Participant names: 'Trevor Wade' and 'Arjun Gopalratnam' - specific to this merchant/team",
    "Project/product name: 'gp-kolo-tabs' - appears to be merchant-specific terminology",
    "Onboarding version number (v2) - indicates merchant has iterated on their process",
    "Specific dates: 'May 8, 2024' and 'May 16, 2024' - merchant-specific timeline"
  ],
  "confidence_score": 0.35
}
```

**Note:** The confidence score is low (0.35) because this appears to be a fragmented document chunk containing primarily video URLs and references rather than complete instructional content. The analysis is based on limited context, making it difficult to extract comprehensive rules or understand the full scope of the merchant's processes. A more complete document would be needed for higher confidence analysis.

---

