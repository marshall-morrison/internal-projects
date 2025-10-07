# Raw LLM Analysis: Summer Discovery - MIS

## Document Overview
- **Total Chunks Analyzed**: 7
- **Analysis Timestamp**: 2025-10-02 10:47:01

---

## Chunk 1: Summer Discovery - MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:01

### Original Content
```
Merchant Name Summer Discovery Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Ops to fill) Steps to process BTs are most commonly found in the Payment Schedule section toward the end of the contract Each lin...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Transaction (BT) Creation",
    "Payment Schedule Interpretation and Data Extraction",
    "Date Calculation Rules (Billing Start Date, Service Start Date)",
    "Pricing and Amount Determination from Contract Line Items",
    "Milestone-Based Billing Model"
  ],
  "rules": [
    "Each line item in the Payment Schedule becomes its own BT",
    "All committed payments in Payment Schedule become BTs, even if total cannot be calculated (use $0 in those cases)",
    "Billing Start Date is always 15 days before the due date listed in Payment Schedule",
    "Net terms are always 15 days",
    "Service Start Date equals Billing Start Date for each line item",
    "Item name should use the details column: use entire sentence for short details, use best judgment to shorten long details",
    "Months of Service defaults to 0 months",
    "Total Price uses the amount listed per payment in Payment Schedule (no calculation needed)",
    "Use amounts in parentheses as the total price when provided",
    "Frequency is set to None (milestone-based billing, not recurring)",
    "Quantity defaults to 1",
    "Create BT with $0 for to-be-determined or variable amounts without estimates"
  ],
  "exceptions": [
    "When amount is to-be-determined or variable based on actual expenses that haven't occurred yet, create a BT with $0",
    "When estimate is not listed in contract, create a BT with $0",
    "For long detail descriptions, shorten using best judgment rather than using entire sentence",
    "Payment Schedule may include estimated amounts based on prior year data - these still become BTs"
  ],
  "merchant_specific": [
    "Merchant Name: Summer Discovery",
    "Implementation POC and CX POC fields need to be filled",
    "Billing model section to be completed by Implementation team",
    "Contract Processing Steps section to be completed by Ops team",
    "BTs are typically found in Payment Schedule section toward the end of contract",
    "Milestone-based billing model (not recurring intervals)",
    "Common payment types include: deposits, residential life management fees, insurance fees, staffing efforts, reimbursed expenses",
    "Uses non-refundable deposits applied to total per student management fee"
  ],
  "confidence_score": 0.95
}
```

---

## Chunk 2: Summer Discovery - MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:11

### Original Content
```
Usage Overage Items: Ignore Only need to follow the payment schedule, which should be flat fees only There will be many BTs throughout the document, but we only want to focus on the given payment schedule Example to ignore: "Additional meals may be purchased at  25 per meal" Integration Item Mapping 3 types Billable Expenses For any expenses, use the billable expenses integration item with the customers name at the end Will use this for pretty much everything that doesn t specifically say  fee  ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Line Item Classification and Mapping",
    "Default Operational Parameters and Settings",
    "Contract Processing Guidelines and Exclusions",
    "Post-Implementation Communication and Handoff Procedures",
    "Merchant-Specific Customization and Feature Requests"
  ],
  "rules": [
    {
      "rule": "Usage overage items should be ignored; only follow the payment schedule with flat fees only",
      "category": "Line Item Processing"
    },
    {
      "rule": "Billable Expenses integration item should include the customer's name at the end",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "Use Billable Expenses for items that don't specifically say 'fee' or 'deposit'",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "Items labeled as 'fee' should use Management Fee - Insurance integration item",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "Items labeled as 'deposit' should use Deposit - Management Fee - Insurance (Revenue) integration item",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "No difference between 'Billable Expenses Deposit' and 'Billable Expenses' - match customer name",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Default net payment terms is 0 if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Default billing frequency is Monthly if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Every tax line item becomes a BT (billable transaction) if none listed",
      "category": "Tax Processing"
    },
    {
      "rule": "If item doesn't fit Billable Expenses or fee/deposit categories, leave as 'none' and flag to team in Slack",
      "category": "Exception Handling"
    },
    {
      "rule": "Events Processing section to be filled by Implementation Success post-go-live",
      "category": "Workflow Responsibility"
    },
    {
      "rule": "Integration Items Processing section to be filled by Implementation Success post-go-live",
      "category": "Workflow Responsibility"
    },
    {
      "rule": "Post Processing Communications section to be filled by Implementation Success post-go-live",
      "category": "Workflow Responsibility"
    },
    {
      "rule": "Customer Information section to be filled by Implementation Success post-go-live",
      "category": "Workflow Responsibility"
    },
    {
      "rule": "Feature Requests: AE fills prior to Implementation handoff, Implementation fills prior to go-live, Success fills post-go-live",
      "category": "Workflow Responsibility"
    },
    {
      "rule": "Merchant Calls: AE fills prior to Implementation involvement, Implementation fills prior to go-live, Success fills post-go-live",
      "category": "Workflow Responsibility"
    }
  ],
  "exceptions": [
    {
      "exception": "Ignore usage overage items like 'Additional meals may be purchased at $25 per meal'",
      "condition": "Only focus on given payment schedule"
    },
    {
      "exception": "Contract-specific processing differences may exist (e.g., always back-date invoice date to final day of the month)",
      "condition": "Merchant has requested specific processing requirements"
    },
    {
      "exception": "Integration items may have special labeling rules per merchant",
      "condition": "Example: All Statsig items labeled as 'Sales', All Pinata items labeled as 'Software Subscription Bundle' unless otherwise noted"
    },
    {
      "exception": "Special memos may be required for certain invoices",
      "condition": "Based on merchant-customer relationship specifics"
    },
    {
      "exception": "Invoice changes may be needed due to merchant-customer relationship",
      "condition": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Integration item labeling conventions",
      "description": "Different merchants may have different rules for how integration items should be labeled (e.g., Statsig as 'Sales', Pinata as 'Software Subscription Bundle')"
    },
    {
      "element": "Contract processing specifics",
      "description": "Merchants may have unique processing requirements like back-dating invoice dates"
    },
    {
      "element": "Customer information and relationships",
      "description": "Special memos and invoice changes based on specific merchant-customer relationships"
    },
    {
      "element": "Post-processing communication requirements",
      "description": "Different merchants may require notification to different team members at different phases (e.g., Customer Success in Messari internal channel)"
    },
    {
      "element": "Events billing instructions",
      "description": "Merchant-specific information on how to handle events billing"
    },
    {
      "element": "Feature requests tracking",
      "description": "Merchant-specific feature requests with urgency and importance ratings"
    },
    {
      "element": "Payment schedule structure",
      "description": "Focus only on flat fees in payment schedule, ignoring variable usage charges"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Summer Discovery - MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:13

### Original Content
```
app gong io call id 2831710205078223476 account-id 8515207541940086288 Contract scoping: (Austin, Vanessa, and Scott) https: us-56595 app gong io call id 7020260913517554594 account-id 8515207541940086288 Demo call (with Summer Discovery s CFO and Finance Manager) https: us-56595 app gong io call id 3049351006388037880 account-id 8515207541940086288 Netsuite scoping call (with NetSuite overseer) https: us-56595 app gong io call
```

### LLM Analysis Response
```json
{
  "themes": [
    "Call documentation and tracking",
    "Multi-stakeholder engagement process",
    "Technical integration scoping (NetSuite)",
    "Contract and financial review procedures",
    "Cross-functional collaboration (Finance, CFO, Technical teams)"
  ],
  "rules": [
    "Calls must be logged with unique call IDs in Gong.io system",
    "Account ID must be associated with all call records (8515207541940086288)",
    "Contract scoping requires involvement of multiple stakeholders (Austin, Vanessa, and Scott)",
    "Demo calls should include finance leadership (CFO and Finance Manager)",
    "NetSuite integration requires dedicated scoping call with system overseer",
    "All calls must be accessible via us-56595 app gong io domain"
  ],
  "exceptions": [
    "Different stakeholder combinations may be required depending on call type (contract scoping vs demo vs technical scoping)",
    "NetSuite scoping calls require specialized technical oversight rather than standard participants"
  ],
  "merchant_specific": [
    "Account ID: 8515207541940086288 (specific to this merchant)",
    "Stakeholder names: Austin, Vanessa, Scott (merchant-specific team members)",
    "Client organization: Summer Discovery (merchant name)",
    "Integration platform: NetSuite (merchant's specific ERP/financial system)",
    "Gong.io instance: us-56595 (potentially merchant or region-specific)",
    "Role titles: CFO, Finance Manager, NetSuite overseer (organizational structure)"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for confidence score**: The document appears to be a fragment of call tracking links rather than complete instruction documentation. While I can infer patterns about call documentation processes and stakeholder involvement, the incomplete nature of the content (truncated URLs, minimal context) limits confidence in extracting comprehensive rules. The themes and patterns identified are based on observable structure, but without full documentation context, there may be additional rules or nuances not captured.

---

## Chunk 4: Summer Discovery - MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:23

### Original Content
```
id 5792724963386849071 account-id 8515207541940086288 Austin s Rolling Notes from the Sales Cycle: Key Stakeholders: Scott Rosenbluth, Operations Director Was told he might have to do dunning No linkedin Fatma Abubaker - Finance Manager Megan Mancini - Operations Manager Myra Cortado - CFo Ashley - Netsuite overseer Company Info: Summer Discovery runs pre-college enrichment programs at various universities Recently bought a program in the UK Two different businesses: Managed - Managed services i...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer and stakeholder identification for sales cycle",
    "Company business model and operations (Managed vs Branded services)",
    "Current technology stack and system integrations",
    "NetSuite configuration and invoicing workflow",
    "Organizational changes and budget constraints"
  ],
  "rules": [
    "Invoice-only flow is used (no other transaction types)",
    "Customers are created manually in the system",
    "Standard required fields must be present on invoices: Program, Class, Department, Location",
    "Tax is not charged on invoices",
    "No multi-currency functionality is enabled",
    "Only 12-20 customers exist in the system",
    "No customer information is tracked on customer records beyond basic creation",
    "For Managed services: receive invoices from universities (invoicing assistance needed)",
    "For Branded services: company pays universities directly (not receiving payments from them)"
  ],
  "exceptions": [
    "Managed services business model requires different invoicing handling - they receive invoices and need assistance processing them",
    "Branded services business model involves direct contracts with universities where Summer Discovery pays the universities",
    "UK program acquisition may introduce future multi-currency or international requirements despite current single-currency setup",
    "CRM (HubSpot) is explicitly noted as 'not in scope' despite being part of tech stack"
  ],
  "merchant_specific": [
    "Custom required fields: Program, Class, Department, Location (specific to educational program tracking)",
    "Business operates in pre-college enrichment space with university partnerships",
    "Two distinct business models requiring different financial workflows (Managed vs Branded)",
    "AP system in transition (Brex to Ramp migration in progress)",
    "Small customer base (12-20) suggests high-value, low-volume transaction model",
    "Organizational transition period: new CFO onboarding, controller departing, budget locked until fall",
    "Key stakeholders identified with specific roles in dunning and financial operations"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: Summer Discovery - MIS_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:27

### Original Content
```
No AR Lots of contracts Very seasonal business Ownership of all contracts has been fragmented in the past Customers typically pay ACH or Wire You can configure some settings for payment methods as well Pricing Model: Branded - dependent on the number of rooms they can fulfill   We will NOT work with this part of their business Managed - not dealing with housing agreements but dealing with a per student cost per week E g Work with Barnard and they were taking a building down to install AC, and th...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Payment Methods and Accounts Receivable",
    "Business Model and Pricing Structure",
    "Contract Management and Seasonality",
    "Revenue Calculation and Billing Processes",
    "Risk Mitigation through Minimum Guarantees"
  ],
  "rules": [
    "No accounts receivable (AR) system in place",
    "Customers pay via ACH or Wire transfer only",
    "Branded pricing model (room-based) will NOT be supported/worked with",
    "Managed pricing model uses per-student-per-week calculation",
    "Management fees include startup/planning fees plus ongoing per-student-per-week fees",
    "All billback expenses incurred during program operation must be billed to customer",
    "Baseline costs are tracked in Excel only (no invoicing software)",
    "Payment structure: annual cost paid in installments",
    "Per-student-per-week fees are multiplied by number of weeks for total cost",
    "Minimum guarantees are required to protect against revenue loss from facility issues"
  ],
  "exceptions": [
    "Branded business model is explicitly excluded from scope",
    "Minimum guarantees can be negotiated when facility issues (e.g., building maintenance, AC installation) threaten revenue",
    "Management fees may include optional startup/planning fees in addition to standard per-student-per-week fees",
    "Billback expenses are variable and added on top of baseline management fees"
  ],
  "merchant_specific": [
    "Summer Disco - appears to be the merchant/company name or product name",
    "Barnard example - specific customer reference showing real-world application of minimum guarantees",
    "Fragmented contract ownership history - indicates past organizational structure issues",
    "Highly seasonal business nature - requires special consideration for cash flow and revenue timing",
    "Excel-based cost tracking system - current state that may need migration/integration",
    "Two-tier pricing model (Branded vs Managed) - unique business structure",
    "Room fulfillment capacity as pricing factor for Branded model",
    "Student housing/accommodation context - industry-specific vertical"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 6: Summer Discovery - MIS_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:38

### Original Content
```
Then the billable invoices are given separately Pain: Unorganized data management They have 50 programs, and they don t know which one is the most expensive to run  No synergy between cost of services and enrollment data  So they re curious if they can build or it buy it Right now all this unstructured data is in spreadsheets Not sending invoices on time If they re not sending invoices on time, the university isn t going to pay on time Tulane example Biggest pain point for the business Risks: No...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing and invoicing challenges",
    "Data management and organization issues",
    "Program cost tracking and financial visibility",
    "Contract structuring and pricing flexibility",
    "Business operational overhaul and system implementation"
  ],
  "rules": [
    "Billable invoices must be given separately",
    "Current billing schedule requires a $25,000 deposit",
    "Billing schedule includes estimated expenses component",
    "Invoices must be sent on time to ensure timely university payment",
    "Cost of services data should be synced with enrollment data",
    "Implementation team becomes DRI (Directly Responsible Individual) on handoff",
    "AE (Account Executive) must fill in notes sections before handoff",
    "Billing information requires documentation (whiteboard session screenshots)",
    "Managed business billing schedule is subject to change/customization"
  ],
  "exceptions": [
    "Shortened contract option available with renewal date aligned to fiscal year",
    "First year contract can be offered at reduced price with automatic increase in year 2",
    "Merchant is open to changing their unique billing schedule for managed business",
    "No budget currently allocated, but testing period possible before fiscal year",
    "Summer period can be used as trial/testing phase"
  ],
  "merchant_specific": [
    "Merchant operates 50 programs requiring individual cost tracking",
    "Tulane referenced as specific example/client",
    "Merchant has acquired new programs requiring integration",
    "Current data stored in unstructured spreadsheets",
    "Merchant has both managed and non-managed business segments",
    "Fiscal year timing drives contract and implementation decisions",
    "Merchant undergoing complete operational overhaul of people and systems",
    "Specific contacts mentioned: Austin and Vanessa for billing information"
  ],
  "confidence_score": 0.72
}
```

**Reasoning for confidence score**: The document appears to be informal notes from a discovery or sales call, with incomplete sentences and fragmented information. While core themes and pain points are clear, some rules and requirements are implied rather than explicitly stated. The incomplete sentence at the end and conversational nature of the notes reduce certainty about complete context, though the main business challenges and potential solutions are identifiable.

---

## Chunk 7: Summer Discovery - MIS_chunk_6

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:47:41

### Original Content
```
background checks) 50  of the Managed Services fee (usage based on number of students It s a per student, per week calculation, and this calculation could differ depending on the university) Remaining amount of the Managed Service fee Any Overages (from expenses incurred by staff) and remaining Expenses 1) What is the merchant temperament Eager to get started Open to consultative advice on their process Open to Tabs recommending processes   ways to operate and even format contracts so that it wo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Complex fee structure with multiple calculation components",
    "Merchant readiness and openness to process optimization",
    "Automation of billing and invoicing workflows",
    "Data consolidation from scattered unstructured sources",
    "Integration requirements with existing systems (NetSuite)"
  ],
  "rules": [
    "Managed Services fee is calculated on a per-student, per-week basis",
    "Fee calculation methodology can vary by university/institution",
    "Fee structure includes multiple components: 50% allocation, remaining amount, overages, and expenses",
    "Overages are generated from staff-incurred expenses",
    "Background checks contribute to the fee calculation",
    "Invoices must be automatically created and sent",
    "Automated dunning processes are required",
    "System must connect back to NetSuite (NS)",
    "Billing data from unstructured sources must be consolidated into invoices"
  ],
  "exceptions": [
    "Per-student calculation differs depending on the specific university",
    "Fee structure has variable components (overages and remaining expenses) that are not fixed",
    "Merchant is open to reformatting contracts to work better with the system, suggesting flexibility in implementation"
  ],
  "merchant_specific": [
    "Student-based billing model (education/university sector)",
    "Managed Services fee structure specific to this merchant",
    "Background checks as a fee component (industry-specific requirement)",
    "NetSuite (NS) as the backend system for integration",
    "Staff expense tracking and overage management",
    "University-specific calculation variations requiring configurable rules",
    "Unstructured data sources unique to merchant's current operations",
    "Consultative relationship preference indicating need for guided onboarding"
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document provides clear information about merchant temperament and key features
- Fee structure details are somewhat fragmented and incomplete (the "50 of the Managed Services fee" appears truncated)
- Strong clarity on automation requirements and pain points
- Some ambiguity in the exact fee calculation formula and component relationships
- Missing context about the full scope of services and complete billing cycle

---

