# Raw LLM Analysis: MIS_ Engaged MD

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 10:42:28

---

## Chunk 1: MIS_ Engaged MD_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:42:28

### Original Content
```
Merchant Name (AE to fill) : Engaged MD Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General BTs will mostly be found in the slides at the end of the contract W...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Billing Transaction (BT) Creation and Configuration",
    "Item Naming Conventions and Standardization",
    "Provider Seat Management and Pricing",
    "Service and Billing Date Configuration"
  ],
  "rules": [
    "General BTs are found in slides at the end of the contract",
    "Item names must follow strict mapping and should not deviate unless explicitly instructed",
    "MDC contracts should be ignored as they are for subsidiaries and process with no BTs",
    "Item descriptions should be ignored",
    "For Platform access, create a flat BT using the quantity from 'Number of Provider Seats'",
    "Do not make tiered unit BTs for usage BTs",
    "Events should match the item name exactly",
    "Most usage BTs are set to monthly arrears - confirm in billing frequency section",
    "For provider seats, create both a flat BT and a usage BT called 'Additional Provider Seats (usage)'",
    "Use 'duplicate' function for all usage BTs and only change item name, integration item, price, and event",
    "For flat provider seats BT: calculate total price as per-seat-per-month price × number of seats",
    "Service Start Date: Use 'Order Effective Date' or listed start date, default to signature date if neither available",
    "Billing Start Date: Same as service start date",
    "Months of Service: Use 'Initial Term' from contract (commonly 12 or 24 months)",
    "Frequency: Almost everything is monthly - confirm in Billing Frequency section",
    "Net Terms: Use terms from Payment Terms section, default to Net 30 if not stated",
    "Implementation Fee should be a flat BT",
    "For Implementation Fee with multiple options, choose the largest number"
  ],
  "exceptions": [
    "Bundled pricing is the only exception to strict item naming - can use bundle name with 'Bundle' appended at the end",
    "For bundled products, the bundle name can be used to create the event as well",
    "If line item has a specific discount, use in-line discounts; if separate line item, create a separate negative BT",
    "When Engaged bills a parent company with children clinics, combine all flat BTs for individual clinics",
    "Implementation Fee has 3 options ($1,000 eLearn only, $1,000 eSign only, $1,500 eLearn + eSign combined) - select largest"
  ],
  "merchant_specific": [
    "Merchant Name (to be filled by AE)",
    "Implementation POC (to be filled by IM)",
    "CX POC (to be added by IMP)",
    "Billing model section (Implementation to fill)",
    "Unique customer creation process information",
    "How merchant bills",
    "Contract structure/breakdown",
    "Number of Provider Seats (determines flat BT)",
    "Integration Item Mapping (merchant-specific mappings)",
    "MDC contracts reference (subsidiary-specific)",
    "Parent company with children clinics structure (Engaged-specific billing scenario)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: MIS_ Engaged MD_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:42:38

### Original Content
```
com prod contracts 167fded3-e996-40af-aefc-f0db60062de1 terms keyof the clinic tables into individual BTs that equals to total of the table Usage AI If you see anything that resembles a minimum commitment or allotment, we will need to turn on Usage AI Examples For minimums Example Select Has Usage -  Has Minimum If minimum period is monthly, select  Individual Billing Period  IF minimum period is ANNUAL or greater, please select  Full Service Period  Select the included products that the minimum...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Usage AI Configuration and Minimum Commitments",
    "Billing Terms (BTs) Creation and Management",
    "Default Values and Operational Standards",
    "Integration and Post-Processing Workflows",
    "Feature Requests and System Requirements"
  ],
  "rules": [
    {
      "rule": "When minimum commitment or allotment is present, Usage AI must be turned on",
      "category": "Usage AI"
    },
    {
      "rule": "For monthly minimum periods, select 'Individual Billing Period'",
      "category": "Usage AI Configuration"
    },
    {
      "rule": "For annual or greater minimum periods, select 'Full Service Period'",
      "category": "Usage AI Configuration"
    },
    {
      "rule": "Select 'True up to meet minimum' for minimum commitments",
      "category": "Usage AI Configuration"
    },
    {
      "rule": "For allotments/prepaid usage, select 'Has Threshold' with 'Full service term' unless amount covers billing period",
      "category": "Usage AI Configuration"
    },
    {
      "rule": "Threshold amount equals total dollar amount prepaid",
      "category": "Usage AI Configuration"
    },
    {
      "rule": "Add '(flat)' to prepaid amount BT for overages",
      "category": "Billing Terms"
    },
    {
      "rule": "Ignore services labeled 'included at no cost' or 'covered by pharmacy'",
      "category": "Billing Terms Exclusions"
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default net payment terms is 0 if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Defaults"
    },
    {
      "rule": "Every tax line item becomes a separate BT if no other instruction",
      "category": "Tax Handling"
    },
    {
      "rule": "Events processing section to be filled by Implementation Success post-go-live",
      "category": "Workflow"
    },
    {
      "rule": "Integration items processing section to be filled by Implementation Success post-go-live",
      "category": "Workflow"
    },
    {
      "rule": "Post-processing communications section to be filled by Implementation Success post-go-live",
      "category": "Workflow"
    },
    {
      "rule": "Customer information section to be filled by Implementation Success post-go-live",
      "category": "Workflow"
    }
  ],
  "exceptions": [
    {
      "exception": "Threshold period should match billing period of usage product if prepaid amount covers it (e.g., quarterly prepaid amount)",
      "condition": "When prepaid amount covers specific billing period"
    },
    {
      "exception": "Services labeled 'included at no cost' or 'covered by pharmacy' should be ignored",
      "condition": "Free or included services"
    },
    {
      "exception": "Merchant-specific processing may differ by contract (e.g., back-dating invoice dates)",
      "condition": "When merchant has specific requests documented"
    },
    {
      "exception": "Integration item labeling varies by provider (Statsig vs Pinata example)",
      "condition": "Depends on integration provider"
    }
  ],
  "merchant_specific": [
    {
      "element": "Minimum commitment naming conventions",
      "example": "eLearn & eSign minimum - use best judgement",
      "customizable": true
    },
    {
      "element": "Product selection for minimums",
      "example": "Select all products in eLearn & eSign",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "example": "Statsig items labeled as 'Sales', Pinata items as 'Software Subscription Bundle'",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "example": "Customer Success [Azmat Aziz] notified in Messari internal channel when contracts processed",
      "customizable": true
    },
    {
      "element": "Special invoice memos for specific customers",
      "example": "Customer relationship-specific invoice changes",
      "customizable": true
    },
    {
      "element": "Contract-specific processing variations",
      "example": "Back-dating invoice dates to final day of month",
      "customizable": true
    },
    {
      "element": "Feature requests",
      "example": "HubSpot integration requirement, reporting on products and pricing",
      "customizable": true
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document is somewhat fragmented and contains incomplete sentences, making some sections difficult to interpret with full certainty. However, the core operational rules around Usage AI configuration, defaults, and workflow responsibilities are clearly stated. The confidence is reduced due to formatting issues, incomplete sections (marked for post-go-live completion), and some ambiguous phrasing. The merchant-specific examples (Statsig, Pinata, Messari) provide good context but suggest this is a template with variable content.

---

## Chunk 3: MIS_ Engaged MD_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:42:39

### Original Content
```
id 596001280436517846 AR heroes Demo 3 14 https: us-56595 app gong io call id 4343401292629545313 Custom Demo 4 8 https: us-56595 app gong io call id 55071692069188938 Custom Demo pt 2 4 22 https: us-56595 app gong io call id 417850449197241829 Implementation and Commercials 4 24 https: us-56595 app
```

### LLM Analysis Response
```json
{
  "themes": [
    "Call/Meeting Documentation",
    "Demo Sessions and Presentations",
    "Implementation Process Tracking",
    "Commercial/Business Discussions"
  ],
  "rules": [
    "Calls and demos are tracked with unique identifiers",
    "Multiple demo sessions may be required (Demo 3, Demo 4, Custom Demo pt 2)",
    "Implementation discussions include commercial aspects",
    "All sessions are logged with timestamps/durations (format appears to be minutes:seconds)",
    "Sessions are accessible via Gong.io platform URLs"
  ],
  "exceptions": [
    "Custom demos appear to have different naming conventions than standard demos",
    "Implementation sessions may combine multiple topics (Implementation and Commercials)"
  ],
  "merchant_specific": [
    "Merchant identifier: 'AR heroes' (appears to be merchant name or code)",
    "Gong.io instance: 'us-56595' (specific tenant/instance identifier)",
    "Call IDs are unique per merchant/session",
    "Demo numbering sequence may vary by merchant engagement stage",
    "Session duration tracking may be customized per merchant needs"
  ],
  "confidence_score": 0.45
}
```

**Note:** The confidence score is relatively low (0.45) because the document chunk appears to be fragmented or improperly formatted data, possibly from a call log or CRM export. The content lacks clear instructional language, complete sentences, or explicit rules. The analysis is based on pattern recognition from what appears to be metadata or system-generated tracking information rather than formal merchant instructions.

---

## Chunk 4: MIS_ Engaged MD_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:42:52

### Original Content
```
gong io call id 3720637875091247517 Integration call 4 28 https: us-56595 app gong io call id 4577131967406111666 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Flat SaaS for platform Subscription Fee Products with P x Q usage Commit consumption with drawdowns 1) What is the merchant temperament Carson (controller) is a strong believer in Tabs and our champion Sees the vision and pulled weight internally to get this done Main u...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant stakeholder analysis and temperament assessment",
    "Billing and revenue model structure (SaaS, subscription, usage-based, consumption commits)",
    "Implementation handoff process and documentation requirements",
    "Product feature requirements and phased rollout (Contract Processing visibility)",
    "Integration and system process concerns"
  ],
  "rules": [
    "Account Executive (AE) must fill in merchant information sections during handoff",
    "Implementation team serves as the DRI (Directly Responsible Individual) for handoff completion",
    "Merchant billing structure must be documented including: flat SaaS platform fees, subscription fees, P x Q usage products, and commit consumption with drawdowns",
    "Stakeholder temperament and role analysis must be captured for key decision makers",
    "Key features that POC (Point of Contact) cares about must be identified and documented",
    "Phase 1 implementation focuses on Contract Processing with omni output visibility requirement",
    "Gong.io call recordings must be referenced and linked for context"
  ],
  "exceptions": [
    "Merchant had 'awful experience with ChargeBee' - may require special handling or sensitivity around previous vendor comparisons",
    "VP of Finance (Adam) is noted as 'much slower and methodical' coming from Capital One - may require adjusted timeline or communication approach",
    "Multiple stakeholder types with different priorities: Controller (champion/believer), VP Finance (methodical), COO (process-focused), CEO (vision/top-line focused) - requires tailored engagement strategy per role"
  ],
  "merchant_specific": [
    "Merchant name/identifier appears to be implied but not explicitly stated",
    "Specific stakeholder names and roles: Carson (Controller/Champion), Adam (VP Finance), Shane (COO), Taylor (CEO)",
    "Billing model combination: Flat SaaS + Subscription + Usage (P x Q) + Commit drawdowns - specific to this merchant's revenue structure",
    "Phase 1 priority: Contract Processing with omni output visibility - merchant-specific implementation priority",
    "Integration requirements driven by COO's focus on 'process, systems, and integrations'",
    "Previous vendor context: ChargeBee (negative experience) - relevant for positioning and messaging"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: MIS_ Engaged MD_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:42:54

### Original Content
```
Specifically - contract dates, key terms, products, and associated pricing by customer Phase 2 - Billing, collections, and revenue reporting Contracts are immediate need then billing next for a complex usage model with some commit consumption Rev Rec and visibility into invoices is very important Currently managing everything in slack with CSMs and want to remove them from this process Item Name to Use (MUST BE EXACT)   Context   Description   Other names it goes by Becoming an Egg Donor COVID  ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Pricing Management - Focus on extracting contract dates, key terms, products, and customer-specific pricing",
    "Billing and Revenue Operations - Complex usage-based billing models with commit consumption tracking, collections, and revenue recognition",
    "Fertility Healthcare Services and Products - Comprehensive catalog of fertility-related medical procedures, testing, and educational content",
    "Technology Platform Components - Digital tools including eSign, eLearn, integrations, authentication, and provider seat management",
    "Process Automation - Transitioning from manual Slack-based coordination with CSMs to automated systems"
  ],
  "rules": [
    "Item names must be used EXACTLY as specified in the standardized list",
    "Phase 1 priority: Extract contract dates, key terms, products, and associated pricing by customer",
    "Phase 2 priority: Billing, collections, and revenue reporting (with contracts as immediate need, billing as next priority)",
    "Revenue recognition and invoice visibility are critical requirements",
    "CSMs must be removed from the current Slack-based management process",
    "Usage-based billing model must accommodate commit consumption tracking",
    "Alternative names/aliases for items are documented but exact standardized names must be used"
  ],
  "exceptions": [
    "Provider Seats have two variants: 'Provider Seats (flat)' for flat-rate billing and 'Additional Provider Seats (usage)' for usage-based billing",
    "IVF can be referenced as 'IVF' or 'Freeze-All IVF' but must use exact naming convention",
    "Some items have multiple common names (e.g., COVID/COVID-19, Zika/Zika Virus, Wellness/Fertility videos) but standardized name must be used",
    "Discount appears as a standalone item without additional context or categorization"
  ],
  "merchant_specific": [
    "Fertility clinic/healthcare provider specialization - entire product catalog is fertility-focused",
    "Custom integration requirements: Meditex Integration Fees suggests specific EMR/practice management system",
    "Implementation fees and professional services suggest customized onboarding per client",
    "Provider seat licensing model indicates B2B SaaS component serving healthcare providers",
    "Current workflow involves CSMs managing processes via Slack (merchant-specific operational model)",
    "Usage model with commit consumption suggests enterprise-level contracts with minimum commitments",
    "Bundle offerings (Inception Essentials Bundle) may be customized per merchant agreement"
  ],
  "confidence_score": 0.82
}
```

---

