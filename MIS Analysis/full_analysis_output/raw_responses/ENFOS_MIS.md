# Raw LLM Analysis: ENFOS MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:40:58

---

## Chunk 1: ENFOS MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:40:58

### Original Content
```
Merchant Name: ENFOS Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Where your information is coming from: Billing Terms come from Order Forms or...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Order Processing Workflow",
    "Billing Terms and Payment Configuration",
    "Document Hierarchy and Information Sources",
    "Data Validation and Quality Control",
    "Revenue Schedule Creation and Management"
  ],
  "rules": [
    "Billing Terms must come from Order Forms or Sales Orders only",
    "Net Terms must come from the MSA (Master Service Agreement)",
    "DO NOT process any Billing Terms listed in the MSA itself",
    "DO NOT process Purchase Orders (POs) as contracts",
    "PO numbers must be inputted as additional fields on corresponding contract invoices",
    "MSA can be left as processed without BT, but net terms should be reflected on associated Order Form or Sales Order",
    "Service Start Date: use listed start date, default to last signature date if nothing stated",
    "Month of Service: use number of months in term, default to 12 months if nothing stated",
    "Quantity: use stated quantity, default to 1 if nothing stated",
    "Billing Start Date: match service start date unless different invoicing cadence is stated",
    "Billing Timing: Bill in advance, due start of period",
    "When PO and order forms list different net terms, always use the net terms in the MSA",
    "If product price differs per year, create separate revenue schedule for each year",
    "Shipping and billing address from PO should be added to the customer",
    "Item Description must include description of products/services included",
    "Check for special terms and conditions or payment terms for specific invoicing cadences",
    "Number of periods should be inferred from frequency and months of service",
    "Frequency determination: If paid annually use YEAR, if monthly use MONTH",
    "Integration items must refer to specific mapping spreadsheet"
  ],
  "exceptions": [
    "Some contract order forms do not have an associated PO",
    "If price of product is different per year, create separate revenue schedules (one per year) instead of single schedule",
    "Specific processing things may differ by contract based on merchant requests (e.g., back-dating invoice date to final day of month)",
    "Sales Orders require double-checking the corresponding MSA for net terms",
    "Contracts should be processed according to what they state, but with hierarchy rules applied"
  ],
  "merchant_specific": [
    "Merchant Name: ENFOS (template shows this is merchant-specific)",
    "Implementation POC and CX POC fields (to be filled per merchant)",
    "Billing model section (Implementation to fill per merchant)",
    "Unique customer creation process information (merchant-specific)",
    "Contract Processing Steps (Post-Go Live, merchant-specific)",
    "Integration Item mapping (merchant-specific assignments)",
    "Events Processing section (if necessary for specific merchant)",
    "Post Processing Communications requirements (varies by merchant)",
    "Default Service Term (merchant can override 1 Year default)",
    "Default Net Payment Terms (merchant can override 0 default)",
    "Default Billing Frequency (merchant can override Monthly default)",
    "Tax handling as line items (merchant-specific approach)",
    "Specific invoicing cadences and special terms per merchant contract",
    "Contract ID references (unique per merchant implementation)"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: ENFOS MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:01

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp han...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and Communication Protocols",
    "Merchant Lifecycle Phase Management",
    "Role-Based Responsibilities and Handoffs",
    "Customer Information Management",
    "Call and Meeting Documentation"
  ],
  "rules": [
    {
      "rule": "Customer Success (specifically Azmat Aziz) must be notified in the Messari internal merchant channel when contracts are processed",
      "context": "Applies during Active merchant phase"
    },
    {
      "rule": "Customer Information section must be filled by Implementation Success team Post-Go Live",
      "context": "Entire Customer Information section responsibility"
    },
    {
      "rule": "AE (Account Executive) must fill Feature Requests for all requests prior to Implementation handoff",
      "context": "Pre-implementation phase"
    },
    {
      "rule": "Implementation team must fill Feature Requests prior to go-live",
      "context": "Implementation phase"
    },
    {
      "rule": "Success team must fill Feature Requests Post-Go Live",
      "context": "Post-launch phase"
    },
    {
      "rule": "AE must fill Merchant Calls section for all videos prior to Implementation involvement",
      "context": "Pre-implementation phase"
    },
    {
      "rule": "Implementation team must fill Merchant Calls section prior to go-live",
      "context": "Implementation phase"
    },
    {
      "rule": "Success team must fill Merchant Calls section Post-Go Live",
      "context": "Post-launch phase"
    },
    {
      "rule": "Special memos must be documented for certain invoices that require them",
      "context": "Invoice processing"
    },
    {
      "rule": "Invoice changes must be tracked when due to merchant customer relationship factors",
      "context": "Customer relationship management"
    }
  ],
  "exceptions": [
    {
      "exception": "Certain invoices require special memos",
      "condition": "Based on specific customer requirements or situations"
    },
    {
      "exception": "Invoice changes may occur due to merchant customer relationship dynamics",
      "condition": "Relationship-driven modifications"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipient",
      "description": "Specific person (Azmat Aziz) and channel (Messari internal merchant channel) may vary per merchant"
    },
    {
      "element": "Customer-specific information",
      "description": "Important information on specifics of merchant's customers needs to be documented"
    },
    {
      "element": "Feature Requests (FR 1 CARR)",
      "description": "Specific feature requests will vary by merchant needs"
    },
    {
      "element": "Merchant call recordings",
      "description": "Specific Gong call links for Intro, Custom demo, and Partnerships calls are merchant-specific"
    },
    {
      "element": "Special invoice memos",
      "description": "Content and requirements will be unique to each merchant's customers"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document chunk is somewhat fragmented and appears to be a template or form with incomplete information
- Clear role-based responsibilities are identifiable across three phases (AE → Implementation → Success)
- Specific notification protocols are mentioned but context is limited
- Some sections appear truncated (URLs are incomplete, sections have placeholder text)
- The structure suggests a standardized process, but specific details and complete context are missing

---

## Chunk 3: ENFOS MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:41:10

### Original Content
```
io call id 3826951672038898896 account-id 4661979429957038267 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills Billing model: - high ACV, multiyear, paid upfront or annual billing - Historically: Onboarding - defined schedules - based on completion - Software Flat fee - Future state: modules - AP portals for some clients They will scope this with us later down the line- feel free to loop me in here if when we need to revisit Proc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing workflow",
    "Revenue recognition and accounting transition",
    "Stakeholder management and team dynamics",
    "Business growth and scaling",
    "Manual process automation needs"
  ],
  "rules": [
    "Deal closure requires Roger's confirmation before invoicing can begin",
    "PO (Purchase Order) must be obtained before invoice creation",
    "Invoices are manually created in QuickBooks Online (QBO)",
    "Manual follow-up required for invoice chasing",
    "ARR tracking maintained via manual spreadsheet",
    "Company is transitioning from cash basis to GAAP compliant accrual accounting",
    "Billing model includes high ACV with multiyear contracts",
    "Payment terms: paid upfront or annual billing",
    "Historical billing includes onboarding with defined schedules based on completion",
    "Software billed as flat fee",
    "Future state will include modular billing with AP portals for some clients"
  ],
  "exceptions": [
    "AP portals will only be available for 'some clients' (not all)",
    "Future modular billing scope to be determined later with AE involvement",
    "Current system cannot split ARR by product (limitation)",
    "Sherry (EA) is described as 'nitpicky and detail oriented' suggesting need for extra attention to detail in her interactions"
  ],
  "merchant_specific": [
    "Key stakeholders: Alex K (invoicing), Alex B (Chief of Staff), CRO (eval runner), Sherry (EA/billing), George (CS/renewals), Alexa (Implementation)",
    "Growth trajectory: 31 logos currently, 40 by EOY, 50 by end of 2026",
    "Roger must be contacted for invoicing confirmation kickoff",
    "Specific personality profiles for each stakeholder (nice, straightforward, nitpicky, etc.)",
    "Implementation team cares about 'single source of truth'",
    "CS team (George) focused on renewals",
    "Uses QuickBooks Online (QBO) as current invoicing system"
  ],
  "confidence_score": 0.85
}
```

---

