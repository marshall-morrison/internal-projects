# Raw LLM Analysis: Cocoon MIS

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 09:55:02

---

## Chunk 1: Cocoon MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:55:02

### Original Content
```
8 discount Note: often the   discount won t calculate correctly, so you will need to do this math to show it in-line Frequency: Year for annual software BTs Implementation   none Set to Monthly for usage BTs if usage is invoiced monthly in arrears Net Terms: Use Net 30 unless a different payment term is stated Additional considerations: You DO NOT need to process any usage BTs for  Additional Employees  or additional PEPM unless  There are multiple years of per customer fees Example First year, ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Configuration",
    "Discount and Pricing Calculations",
    "Usage-Based vs Flat-Price Billing Models",
    "Post-Processing Workflows and Team Notifications",
    "Merchant-Specific Customer and Integration Handling"
  ],
  "rules": [
    "Discount calculations must be done manually and shown in-line as they often don't calculate correctly automatically",
    "Frequency should be set to 'Year' for annual software BTs",
    "Frequency should be set to 'Monthly' for usage BTs if usage is invoiced monthly in arrears",
    "Net Terms default to Net 30 unless a different payment term is stated",
    "Do NOT process usage BTs for 'Additional Employees' or additional PEPM unless there are multiple years of per customer fees",
    "First year billing should use a flat price BT when employee count is known",
    "Second year and beyond should use usage BT when employee count cannot be predetermined",
    "Service and billing start date for usage BTs should be the date of the second year start",
    "If no tax terms are listed, the Ops Default is that every tax line item becomes a BT",
    "All Statsig integration items should be labeled as 'Sales'",
    "All 'Pinata' integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by Merchant",
    "Implementation Success team is responsible for filling post-go-live sections including Events Processing, Integration Items Processing, and Post Processing Communications"
  ],
  "exceptions": [
    "Usage BTs for additional employees/PEPM are only created when there are multiple years of per customer fees",
    "Tiered unit BT logic requires special attention (e.g., rate of $2.50 for 1-100 employees, $2.00 for 101-1,000 employees)",
    "Integration item labeling can be overridden by merchant-specific instructions",
    "Payment terms can differ from Net 30 default if explicitly stated in contract",
    "When no number is available to calculate a Flat BT, create a usage BT instead"
  ],
  "merchant_specific": [
    "Customer Success notification requirements (e.g., Azmat Aziz needs notification in Messari internal merchant channel when contracts are processed in Active phase)",
    "Specific processed contract IDs referenced (e398024d-b70c-4399-83e6-e04cce19443a, 0d114800-7073-48a8-8967-cacb57c3495a)",
    "Integration labeling rules vary by merchant (Statsig vs Pinata examples)",
    "Special memos may be required for certain invoices based on merchant-customer relationships",
    "Customer-specific information and invoice changes based on merchant relationships",
    "Feature requests tracked per merchant with urgency levels",
    "Merchant-specific call recordings and demos maintained"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Cocoon MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:55:04

### Original Content
```
Merchant Name: Cocoon Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) General Billing email to be extracted from the contract   renewal doc it can override what's ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Setup",
    "Billing Types and Fee Structures",
    "Service Start Dates and Timing Rules",
    "Discount Calculations and Handling",
    "Renewal Contract Processing"
  ],
  "rules": [
    "Extract general billing email from contract renewal document, which can override customer-level settings",
    "Billing Terms (BTs) are generally found in the order form at the top of the contract or in Exhibit A",
    "Contracts typically include an annual subscription fee and an implementation fee",
    "Do not process anything related to renewals for initial contracts",
    "For renewal contracts, process renewal BTs under the renewal contract",
    "Example Period should be for 1 month (not the whole year) for: Implementation Fee, Transfer Leaves Fee, Additional Entity Fee",
    "Annual subscription fee period is for full year",
    "Per Leave Fee and Monthly Software Fee are classified as Unit Price billing types",
    "Track events: Per Leave Fee tracks 'Leaves', Monthly Software Fee tracks 'Per Employee'",
    "If there is a minimum requirement, turn on Usage AI",
    "Service Start Date is found in the Services and Term section",
    "For Flat BTs with monthly invoicing clause: start invoice on the first of the following month after contract start date",
    "For Usage BTs: start on the first of the signature month and add a month for duration",
    "Billing Start Date is same as service start date",
    "Months of Service: Use the length of the initial term for software fees, use 1 month for implementation",
    "Create in-line discounts for both annual software and implementation fees if listed",
    "Include $0 BTs in the setup",
    "If a BT is 'waived', add a 100% in-line discount",
    "For annual software fee, manual calculation may be required to determine discount amounts"
  ],
  "exceptions": [
    "When contract has monthly invoicing clause (e.g., 'invoiced every three months following'): Flat BTs start first of following month, Usage BTs start first of signature month",
    "Renewal contracts require different processing than initial contracts - create new doc and process renewal BTs separately",
    "Waived fees are handled as 100% discounts rather than being omitted",
    "$0 BTs must be included rather than excluded",
    "Annual software fee discount may require reverse calculation from final price to determine original price and discount percentage"
  ],
  "merchant_specific": [
    "Merchant Name: Cocoon",
    "Implementation POC and CX POC fields to be filled",
    "Specific fee types: Per Leave Fee, Monthly Software Fee, Transfer Leaves Fee, Additional Entity Fee",
    "Event tracking specific to merchant: 'Leaves' and 'Per Employee'",
    "PEPM (Per Employee Per Month) pricing model",
    "Census-based employee count for calculations",
    "Specific discount calculation example: $7.70 PEPM reduced to $6.16 PEPM with 20% discount",
    "Three-month billing cycle mentioned in example",
    "Implementation Success team fills post-go-live section"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Cocoon MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:55:13

### Original Content
```
gong io call id 6863775313232708213 account-id 374704045599844429 Hubspot scoping https: us-56595 app gong io call id 3214368775749721243 account-id 374704045599844429 Partnership https: us-56595 app gong io call id 6094306695344481553 account-id 374704045599844429 Implementation questions https: us-56595 app gong io call
```

### LLM Analysis Response
```json
{
  "themes": [
    "Call tracking and documentation",
    "CRM integration (Hubspot)",
    "Account management and identification",
    "Meeting categorization (scoping, partnership, implementation)"
  ],
  "rules": [
    "Each call must have a unique call ID for tracking purposes",
    "All calls must be associated with a specific account ID",
    "Calls should be categorized by type (scoping, partnership, implementation questions)",
    "Call records appear to follow a structured format: platform (gong.io) + call-id + account-id + category/description",
    "Integration with Hubspot CRM system is required for call tracking"
  ],
  "exceptions": [
    "No explicit exceptions identified in this document chunk",
    "The document appears to be a log or reference list rather than containing conditional logic"
  ],
  "merchant_specific": [
    "Account ID: 374704045599844429 (appears to be merchant-specific identifier)",
    "Gong.io platform usage (specific call recording/analytics tool)",
    "Hubspot CRM integration (specific CRM platform choice)",
    "URL pattern: us-56595.app.gong.io (region-specific or instance-specific)",
    "Call categorization terminology may vary by merchant (scoping, partnership, implementation)"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for low confidence score:**
- The document chunk appears to be incomplete or corrupted (URLs are fragmented, formatting is unclear)
- Context is limited - this seems to be a reference list or log rather than instructional content
- Difficult to determine if these are prescriptive rules or simply examples of past calls
- Unclear whether this represents a standard operating procedure or just historical data
- Missing critical context about what merchants should do with this information

---

## Chunk 4: Cocoon MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:55:18

### Original Content
```
id 217469488918329472 account-id 374704045599844429 Notes Sections (AE to fill if they have, Implementation to be completion DRI on handoff) Info on how merchant bills 1 Historical contracts (30 ) -   of leaves - implementation - billed monthly (arrears, upfront, retroactive) 2 New standard contracts (70 ) - PEPM flat rate - implementation - discounts, payment terms Process: Deal closed   Accounting lead manually inputs contract info into Chargebee   CSM updates on usage (historical) Chargebee n...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and Contract Structure",
    "Manual Process and System Limitations",
    "Merchant Relationship Management",
    "Scaling Challenges and Capacity Constraints",
    "Payment Reconciliation Workflow"
  ],
  "rules": [
    "Historical contracts (30% of business) are billed monthly in arrears, upfront, or retroactively based on number of leaves",
    "New standard contracts (70% of business) use PEPM (Per Employee Per Month) flat rate billing model",
    "Deal closure triggers manual contract input into Chargebee by Accounting lead",
    "CSM is responsible for updating usage data for historical contracts",
    "Manual payment reconciliation is required due to Chargebee not being connected",
    "Implementation team serves as DRI (Directly Responsible Individual) for completion on handoff",
    "Discounts and payment terms are applicable to new standard contracts",
    "Current capacity is 15-20 customers per month",
    "Expected capacity by EOY is 30-40 customers per month"
  ],
  "exceptions": [
    "Historical contracts (30%) follow different billing methodology than standard contracts",
    "Customer corrections require manual intervention and rework",
    "External contact (Courtney) is involved in merchant relationship alongside internal contact (Lisa)"
  ],
  "merchant_specific": [
    "Merchant contacts: Lisa (internal, described as 'super nice and very easy to work with') and Courtney (external, also 'very nice and easy to work with')",
    "Specific contract split: 30% historical vs 70% new standard",
    "Uses Chargebee as billing system (though not fully integrated)",
    "Billing based on 'leaves' metric for historical contracts",
    "PEPM pricing model for new contracts",
    "Merchant temperament noted as collaborative and easy to work with",
    "Reference to 'Tabs features' that POC cares about (though not detailed in this chunk)"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be implementation notes with some incomplete sections and fragmented information
- Clear billing structure and process flow are documented
- Some ambiguity exists around specific percentages and whether they represent customer count or revenue
- The "Tabs features" section is mentioned but not completed
- Merchant temperament is clearly documented
- The manual process workflow is well-defined despite system limitations

---

