# Raw LLM Analysis: OLD MIS

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:30:33

---

## Chunk 1: OLD MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:33

### Original Content
```
5 months), list as separate BTs For tiered user fees, calculate total based on additional users beyond included count Service Start Date Use Order Form Effective Date unless a delayed start is indicated (e g , post-trial or 3 months later) Example: ARIA contract begins 3 months after Order Form Effective Date Billing Start Date Match Service Start Date unless payment terms specify otherwise Example: Delayed Net 120 invoicing may mean billing starts later than service start Always align with mile...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Segmentation",
    "Service and Billing Start Date Determination",
    "Contract Term Duration and Period Calculation",
    "User Fee Structures and Tiered Pricing",
    "Payment Frequency and Milestone-Based Billing"
  ],
  "rules": [
    "Contracts longer than 12 months must be split into separate Billing Transactions (BTs)",
    "Tiered user fees should calculate total based on additional users beyond the included count",
    "Service Start Date defaults to Order Form Effective Date unless delayed start is indicated",
    "Billing Start Date must match Service Start Date unless payment terms specify otherwise",
    "Billing dates must align with milestone due dates when explicitly listed",
    "Trial periods (e.g., 3 months) should be treated as their own separate BTs",
    "Default to 12-month periods if term spans one year without further breakdown",
    "Frequency is 'Annual' if contract refers to full-year fees billed once",
    "Frequency is 'None' if BTs are milestone-based or event-based",
    "Months of Service should be calculated based on specific contract language (e.g., 4.5 months, 7.5 months, 12 months)"
  ],
  "exceptions": [
    "Delayed start scenarios: service may begin post-trial or after a specified delay (e.g., 3 months after Order Form Effective Date)",
    "ARIA contract example: begins 3 months after Order Form Effective Date",
    "Delayed Net 120 invoicing: billing may start later than service start date",
    "Split period contracts: contracts with non-standard durations (4.5 months, 7.5 months) require custom BT segmentation",
    "Milestone-based billing overrides standard frequency rules"
  ],
  "merchant_specific": [
    "ARIA contract - specific merchant example with 3-month delayed start",
    "User fee tiers and included user counts (varies by merchant pricing model)",
    "Trial period duration (mentioned as 3 months but may vary)",
    "Payment terms (e.g., Net 120) specific to merchant agreements",
    "Milestone definitions and due dates (merchant-specific contract terms)",
    "Order Form Effective Date format and definition",
    "Contract term lengths and split period definitions (4.5, 7.5, 12 months)"
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 2: OLD MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:33

### Original Content
```
Merchant Name: AlphaAI Technologies DBA Tavily Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Billing Term Breakdown Create one BT per distinct s...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract setup and billing configuration",
    "Billing Term (BT) creation and structuring",
    "Service item naming and description conventions",
    "Milestone-based payment processing",
    "Merchant-specific implementation requirements"
  ],
  "rules": [
    "Create one Billing Term (BT) per distinct service period or product line as listed in the contract",
    "Create separate BTs for each payment milestone if multiple milestones exist for a single service",
    "Item Name should use the service name from 'Scope of Services' or relevant contract section",
    "Item Description should be used to clarify user tiers or milestone payments only if helpful",
    "Quantity should use the quantity listed in contract; default to 1 if none is specified",
    "Total Price must use exact value from the contract",
    "User Fees quantities (Admin, Editor, Viewer) must be explicitly listed when applicable",
    "Implementation team is responsible for filling billing model section",
    "Implementation Success team handles Contract Processing Steps post-go-live"
  ],
  "exceptions": [
    "Item Description is optional - only use 'if helpful' for clarifying user tiers or milestone payments",
    "Quantity defaults to 1 when not specified in contract",
    "Milestone-based fees require special handling with separate BTs for each milestone within a single service"
  ],
  "merchant_specific": [
    "Merchant Name: AlphaAI Technologies DBA Tavily",
    "Implementation POC placeholder (IM to fill)",
    "CX POC placeholder (IMP to Add)",
    "Billing model section requires merchant-specific implementation details",
    "Customer creation process may have unique requirements per merchant",
    "Contract structure and breakdown varies by merchant",
    "One-off merchant-specific considerations need documentation",
    "Service names and scope definitions are contract-specific",
    "User tier structures (Admin, Editor, Viewer) may vary by merchant"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be a template with incomplete sections (placeholders like "IM to fill", "IMP to Add")
- Clear rules are provided for BT creation, naming conventions, and pricing
- Some context is missing (the text cuts off mid-sentence at "24K for 7")
- The structure suggests this is part of a larger standardized process, but full context is not available
- Core operational rules are clear and extractable despite incomplete sections

---

## Chunk 3: OLD MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:44

### Original Content
```
Monthly if contract explicitly states monthly user charges Net Terms Use stated net terms from Payment Schedule: e g , "Net 30", "Net 120" If none listed, default to 30 Special Cases Vertica contract includes a guaranteed minimum spend and partner setup fees: Process setup fees as separate one-time BTs Guaranteed minimum shortfall is not a BT unless invoiced directly to customer (watch for red flag) Trial Terms (e g , ARIA) should be separate BTs with own start dates and prices Exclusions User-B...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Term (BT) Creation and Processing",
    "Payment Terms and Net Terms Configuration",
    "User-Based Pricing and Tiered Structures",
    "Contract Special Cases and Exclusions",
    "Usage-Based Product Handling"
  ],
  "rules": [
    "Monthly billing terms should only be created if contract explicitly states monthly user charges",
    "Use stated net terms from Payment Schedule (e.g., Net 30, Net 120)",
    "Default to Net 30 if no payment terms are listed",
    "Setup fees must be processed as separate one-time billing terms",
    "Trial terms (e.g., ARIA) require separate billing terms with their own start dates and prices",
    "Create separate billing terms for user tiers above included counts",
    "Calculate annual cost and quantity from pricing tables for user-based pricing",
    "Common usage-based products include: additional admin users, additional editor users, additional viewers"
  ],
  "exceptions": [
    "Vertica contract: includes guaranteed minimum spend and partner setup fees requiring special handling",
    "Guaranteed minimum shortfall is NOT a billing term unless invoiced directly to customer (flagged as red flag scenario)",
    "Setup fees are processed differently as one-time billing terms rather than recurring",
    "Trial terms require separate billing term treatment with independent pricing and dates"
  ],
  "merchant_specific": [
    "Vertica contract mentioned as specific merchant/product requiring special processing",
    "ARIA referenced as example of trial terms requiring special handling",
    "User tier pricing structure (admin users, editor users, viewers) may vary by merchant",
    "Pricing tables format and structure likely merchant-specific",
    "Document references 'things the merchant has requested' indicating customizable processing rules per merchant",
    "Red flag monitoring for guaranteed minimum shortfalls appears to be merchant-specific concern"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: OLD MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:30:57

### Original Content
```
always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Processi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default Operational Settings and Billing Parameters",
    "Post-Implementation Processing and Communication Workflows",
    "Integration Management and Labeling Requirements",
    "Merchant-Specific Business Model and Billing Structure",
    "Feature Requests and System Integration Priorities"
  ],
  "rules": [
    {
      "rule": "Invoice dates must always be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Service Terms",
      "explicit": true
    },
    {
      "rule": "Default Net Payment Terms is 0 if none listed",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Frequency",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) if no other instruction listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Events Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Integration Items Processing section Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Post Processing Communications section Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling Customer Information section Post-Go Live",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff, Implementation fills prior to go-live, Success fills Post-Go Live",
      "category": "Feature Request Management",
      "explicit": true
    },
    {
      "rule": "Implementation is the completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
      "category": "Responsibility Assignment",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Integration item labeling can be overridden by Merchant notation",
      "context": "Pinata integration items default to 'Software Subscription Bundle' unless otherwise noted by Merchant",
      "applies_to": "Integration Labeling"
    },
    {
      "exception": "PLG (Product-Led Growth) motion is intentionally excluded from Tabs integration",
      "context": "Merchant (Shai) wants PLG motion kept separate from Tabs, though open to future integration",
      "applies_to": "Merchant Business Model"
    },
    {
      "exception": "Pay-as-you-go overage billing handled outside Tabs",
      "context": "Customer credit overages are handled in Stripe with potential future Tabs integration",
      "applies_to": "Billing Processing"
    },
    {
      "exception": "Merchant POC works across significant time zone difference",
      "context": "Merchant contact located in Israel (7 hours ahead of New York) but works late at times",
      "applies_to": "Communication Scheduling"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant Name",
      "value": "Aleph",
      "category": "Identity"
    },
    {
      "element": "Primary Contact",
      "value": "Shai",
      "category": "Contact Information"
    },
    {
      "element": "Secondary Contact",
      "value": "Rebecca",
      "category": "Contact Information"
    },
    {
      "element": "Customer Success Contact",
      "value": "Azmat Aziz",
      "category": "Internal Team"
    },
    {
      "element": "Merchant Type",
      "value": "FP&A software",
      "category": "Business Type"
    },
    {
      "element": "Billing Model Components",
      "value": "Flat SaaS platform fee, Credit-based system, Pay-as-you-go overages, Optional security layer (12 months)",
      "category": "Billing Structure"
    },
    {
      "element": "Sales Motion",
      "value": "SLG (Sales-Led Growth) - newly launched within last couple months",
      "category": "Business Model"
    },
    {
      "element": "Excluded Motion",
      "value": "PLG (Product-Led Growth) - kept separate from Tabs",
      "category": "Business Model"
    },
    {
      "element": "Notification Requirements",
      "value": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when contracts are processed [Merchant Phase: Active]",
      "category": "Communication Protocol"
    },
    {
      "element": "Key Features of Interest",
      "value": "Invoice generation, Revenue schedule automation, Avalara integration, Stripe integration, QB Integration, Hubspot, Plaid connection (Chase)",
      "category": "Feature Requirements"
    },
    {
      "element": "Integration Priority",
      "value": "API integration between Aleph and Tabs - Medium priority, anticipated soon into relationship",
      "category": "Technical Requirements"
    },
    {
      "element": "Merchant Temperament",
      "value": "Relatively easy going and open to workflows, not 100% set in his way",
      "category": "Relationship Management"
    },
    {
      "element": "Time Zone",
      "value": "Israel (7 hours ahead of New York)",
      "category": "Operational Consideration"
    }
  ],
  "confidence_score": 0.92
}
```

---

