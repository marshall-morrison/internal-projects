# Raw LLM Analysis: Tabs MIS for WEVO

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:15:33

---

## Chunk 1: Tabs MIS for WEVO_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:33

### Original Content
```
id 6731822181222776398 Demo https: us-56595 app gong io call id 6748069873295800785 PLG SLG discussion with Annie and Tabs Jon https: us-56595 app gong io call id 2175070243838742757 Ben and Annie discuss integrations - https: us-56595 app gong io call id 3366202905538628361 Jon, Annie and Ben discuss PLG SLG motion again - https: us-56595 app gong
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting and call documentation",
    "Product-Led Growth (PLG) and Sales-Led Growth (SLG) strategy discussions",
    "Integration discussions and technical implementation",
    "Cross-functional collaboration between team members (Annie, Tabs, Jon, Ben)"
  ],
  "rules": [],
  "exceptions": [],
  "merchant_specific": [
    "Gong.io platform usage for call recording/tracking (us-56595 app instance)",
    "Specific call IDs as reference system (format: numeric ID followed by description)",
    "Team member names: Annie, Tabs, Jon, Ben",
    "PLG/SLG motion terminology specific to this organization's go-to-market strategy",
    "URL structure pattern: 'us-56595 app gong io call id [number]'"
  ],
  "confidence_score": 0.3
}
```

**Reasoning for low confidence score:**

This document appears to be a fragment of meeting notes or a call log index rather than a complete instruction document. It contains:
- Incomplete URLs (spaces instead of proper formatting)
- Reference links without context or instructions
- No clear rules, policies, or procedural guidance
- No actionable directives or requirements

The content seems to be metadata or an index of recorded calls rather than instructional material that would contain extractable rules or patterns for merchant operations.

---

## Chunk 2: Tabs MIS for WEVO_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:40

### Original Content
```
Merchant Name: WEVO Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Integration Item: [ ] Billing Timing: Bill First of Period General Process one...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract billing configuration and setup",
    "Credit-based pricing and invoicing models",
    "Billing timing and frequency management",
    "Merchant-specific implementation workflows",
    "Cross-functional communication and handoff processes"
  ],
  "rules": [
    "Bill at the first of the period unless otherwise specified",
    "Default to one billing term per contract term (typically annual) unless contract explicitly splits invoicing",
    "Item names should use 'SaaS Services and Professional Services' unless more specific descriptor is given (e.g., WEVO Insight, WEVO Pulse)",
    "Quantity should use the number of included credits if listed, otherwise default to 1",
    "Total price should use the total contract price for included credits, not divided per credit unless explicitly broken out",
    "Service start date should use the contract's effective date",
    "Billing start date should match service date unless another timing is specified",
    "Default to 12 months of service if not specified",
    "Default net terms to 30 days if not stated in contract",
    "Billing type should be FLAT even though pricing model may be labeled as 'usage' for prepaid credit packages",
    "Calculate months of service based on start and end dates",
    "Additional credits beyond prepaid packages should be processed as separate usage billing terms with unit pricing",
    "Monthly credit packages should use Quantity field for credit count, Frequency as Monthly, and Total Price as monthly amount"
  ],
  "exceptions": [
    "Wawa contract requires both a flat billing term (for prepaid Insight credits following standard rules) and a usage billing term (for additional credits, mapped as monthly in arrears with unit pricing per credit using event type: Credits)",
    "When contract explicitly splits invoicing, deviate from one billing term per contract term rule",
    "When contract explicitly breaks out per-credit pricing, divide total price accordingly instead of using total contract price"
  ],
  "merchant_specific": [
    "CX POC and Implementation POC fields need to be filled per merchant",
    "Billing model section requires merchant-specific implementation details",
    "Customer creation process may have unique merchant-specific requirements",
    "Contract structure and breakdown varies by merchant",
    "Integration items labeling varies by merchant (examples: Statsig labeled as 'Sales', Pinata labeled as 'Software Subscription Bundle')",
    "Post-processing communication requirements vary by merchant (who to notify, when, and where)",
    "Customer-specific information including special memos and invoice changes based on merchant-customer relationships",
    "Feature requests tracked per merchant with urgency levels",
    "Merchant call recordings and documentation tracked per implementation phase",
    "Events processing requirements vary by merchant and may not be necessary for all",
    "Product names may be merchant-specific (WEVO Insight, WEVO Pulse, WEVO GAIS)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Tabs MIS for WEVO_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:46

### Original Content
```
io call id 5258727310429478367 Ben and Vanessa scope needs for Mosaic - https: us-56595 app gong io call id 3403361204937952617 Verbal for Signature and Annie confirming which reports she cares about in Mosaic (4 min convo) - https: us-56595 app gong io call id 8136923179866104842 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills SaaS billing with two primary products May introduce new products in the future 1) What is the merchan...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer onboarding and implementation handoff process",
    "Merchant billing model and product structure (SaaS with multiple products)",
    "Customer relationship management and stakeholder profiling",
    "Product feature prioritization and adoption roadmap",
    "Data integration and reporting requirements (Mosaic, Slack, HubSpot)"
  ],
  "rules": [
    "Implementation team serves as completion DRI (Directly Responsible Individual) on handoff",
    "Account Executives (AE) must fill notes sections if available before handoff",
    "Merchant temperament assessment is required during onboarding",
    "Key POC feature preferences must be documented and tracked",
    "Current feature needs must be distinguished from future feature needs",
    "Merchant billing model must be documented (including number of primary products and potential new products)",
    "Integration requirements must be identified (Slack, HubSpot, Mosaic)",
    "ARR and Bookings data export requirements must be captured",
    "Migration plans (PLG billing to Stripe) should be documented for future implementation"
  ],
  "exceptions": [
    "Notes sections are conditional - AE fills only 'if they have' information available",
    "Future features (PLG billing migration) are dependent on completing Stripe migration first",
    "New product introductions may occur in the future, requiring flexibility in billing structure"
  ],
  "merchant_specific": [
    "Merchant name: Annie (key POC) and team including Ben, Vanessa, Signature",
    "Specific billing model: SaaS billing with two primary products",
    "Personality profile: 'Annie is a talker, exuberant, competent and great to work with'",
    "Specific integrations needed: Mosaic (for ARR/Bookings data), Slack, HubSpot",
    "Current priority features: automated contract management, collaboration, efficiency features",
    "Future roadmap: migrating PLG billing to Stripe for SLG PLG reporting",
    "Specific reports tracked: Reports Annie cares about in Mosaic (referenced in call)",
    "Reference to Gong call IDs for context and verification"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: Tabs MIS for WEVO_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:49

### Original Content
```
They may also migrate from Mosaic to Runway in  October Goals: Increase efficiency and bring more organization to her team's work, as she cannot continue at the current pace Find a solution that can serve as a single source of truth for contracts, as the current disorganized storage in Google Drive is very time-consuming Explore using the solution as a central customer management tool, where her team and the new Customer Success Manager can easily access information about customers using things ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "System Migration and Integration",
    "Operational Efficiency and Automation",
    "Centralized Information Management",
    "Financial Process Optimization",
    "Team Collaboration and Customer Success"
  ],
  "rules": [
    "Must maintain current Annual Recurring Revenue (ARR) tracking during migration from Mosaic to Runway",
    "Solution must serve as single source of truth for contracts",
    "Solution must integrate with Slack and HubSpot for customer information access",
    "Collections process must be automated to reduce dependency on outsourced accounting team",
    "Billing process must remain seamless during any transitions",
    "Customer Success Manager and team must have easy access to customer information",
    "Migration support must be coordinated with Vanessa who has scoped the requirements"
  ],
  "exceptions": [
    "Migration timeline is conditional - 'may migrate' in October rather than definitive",
    "Current Google Drive storage system is acknowledged as temporary/problematic solution requiring replacement",
    "Outsourced accounting team dependency is intended to be reduced but not necessarily eliminated"
  ],
  "merchant_specific": [
    "Mosaic platform - current system being used for ARR tracking",
    "Runway platform - potential migration target",
    "Google Drive - current contract storage method",
    "Vanessa - specific point of contact for migration coordination",
    "Customer Success Manager role - new position being added to team",
    "October timeframe - specific migration window",
    "Current team pace described as unsustainable - specific to this merchant's operational state"
  ],
  "confidence_score": 0.85
}
```

---

