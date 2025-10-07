# Raw LLM Analysis: MIS_ Crelate

## Document Overview
- **Total Chunks Analyzed**: 7
- **Analysis Timestamp**: 2025-10-02 09:59:13

---

## Chunk 1: MIS_ Crelate_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:13

### Original Content
```
Merchant Name (AE to fill): Crelate Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Locate BTs: All billable terms are found in the "Subscription ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Location",
    "Billable Terms (BT) Creation Process",
    "Pricing and Discount Processing",
    "Date Management (Billing and Service Start Dates)",
    "Default Values and Fallback Logic"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Data Location",
      "description": "All billable terms must be located in 'Subscription Purchase Form' and 'Professional Services Statement of Work (SOW)' sections of contract PDFs"
    },
    {
      "rule_id": "R2",
      "category": "Item Naming",
      "description": "Item Name must use the product name from the 'Name' column in pricing tables"
    },
    {
      "rule_id": "R3",
      "category": "Quantity Extraction",
      "description": "Quantity must be extracted from the 'QTY' column in the contract table"
    },
    {
      "rule_id": "R4",
      "category": "Quantity Default",
      "description": "If quantity is not listed, default to 1"
    },
    {
      "rule_id": "R5",
      "category": "Quantity Special Case",
      "description": "For Insights Agent and Discovery Agent, use a specific sheet for quantity determination"
    },
    {
      "rule_id": "R6",
      "category": "Pricing",
      "description": "Total Price must use the subtotal listed per line item"
    },
    {
      "rule_id": "R7",
      "category": "Discount Processing",
      "description": "Discounts must be processed inline as negative billable terms"
    },
    {
      "rule_id": "R8",
      "category": "Billing Start Date",
      "description": "Use the explicitly stated Billing Start Date if listed in the contract"
    },
    {
      "rule_id": "R9",
      "category": "Service Start Date",
      "description": "Service Start Date should match Billing Start Date unless another service commencement date is explicitly listed"
    },
    {
      "rule_id": "R10",
      "category": "Term Length",
      "description": "Months of Service should use the term length if stated in the contract"
    },
    {
      "rule_id": "R11",
      "category": "Term Length Default - Subscriptions",
      "description": "For subscription items, default to 12 months if term length is not stated"
    },
    {
      "rule_id": "R12",
      "category": "Term Length Default - One-time Services",
      "description": "For one-time services (e.g., trainings), default to 1 month if term length is not stated"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Insights Agent and Discovery Agent require quantity lookup from a separate sheet rather than contract QTY column",
      "applies_to": "Quantity extraction for specific products"
    },
    {
      "exception_id": "E2",
      "description": "Discounted items require creation of negative billable terms (e.g., 'New User Classroom' discount creates -$495 BT)",
      "applies_to": "Discount processing"
    },
    {
      "exception_id": "E3",
      "description": "Service Start Date may differ from Billing Start Date if alternative service commencement date is specified",
      "applies_to": "Date management"
    },
    {
      "exception_id": "E4",
      "description": "One-time services use 1 month term instead of standard 12 month subscription term",
      "applies_to": "Term length for non-subscription items"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract Document Structure",
      "description": "Specific sections: 'Subscription Purchase Form' and 'Professional Services Statement of Work (SOW)'",
      "customization_needed": true
    },
    {
      "element": "Product Names",
      "description": "Examples include 'Crelate Recruit - Business Plus', 'New User Classroom', 'Insights Agent', 'Discovery Agent'",
      "customization_needed": true
    },
    {
      "element": "Pricing Table Format",
      "description": "Uses 'Name' column and 'QTY' column structure",
      "customization_needed": true
    },
    {
      "element": "External Reference Sheet",
      "description": "Separate sheet used for Insights Agent and Discovery Agent quantity lookup",
      "customization_needed": true
    },
    {
      "element": "Merchant Metadata",
      "description": "Template includes fields for Implementation POC, CX POC, and billing model information",
      "customization_needed": true
    },
    {
      "element": "Service Types",
      "description": "Distinguishes between subscription items and one-time services (trainings)",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: MIS_ Crelate_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:18

### Original Content
```
Frequency: For subscription lines, use contract billing frequency For one-time items like "New User Classroom", set to  None Net Terms: As listed in the contract If listed as "Due upon receipt"   use 0 for Net Terms Integration Item : Leave blank Ignore: No items need to be ignored in these contracts All listed billable or discounted items should be processed Implementation Fees: Sometimes flat rate - implementation on the contract For example:  5000 40  upfront and 60  on completion Set 60  to ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Billing Configuration",
    "Amendment and Contract Lifecycle Management",
    "Default Values and Fallback Rules",
    "Proration and Revenue Recognition",
    "Implementation Fee Handling"
  ],
  "rules": [
    {
      "category": "Billing Frequency",
      "rule": "For subscription lines, use contract billing frequency",
      "specificity": "explicit"
    },
    {
      "category": "Billing Frequency",
      "rule": "For one-time items like 'New User Classroom', set frequency to None",
      "specificity": "explicit"
    },
    {
      "category": "Net Terms",
      "rule": "Use net terms as listed in the contract",
      "specificity": "explicit"
    },
    {
      "category": "Net Terms",
      "rule": "If listed as 'Due upon receipt', use 0 for Net Terms",
      "specificity": "explicit"
    },
    {
      "category": "Integration Item",
      "rule": "Leave Integration Item field blank",
      "specificity": "explicit"
    },
    {
      "category": "Ignore Flag",
      "rule": "No items need to be ignored in these contracts - all listed billable or discounted items should be processed",
      "specificity": "explicit"
    },
    {
      "category": "Implementation Fees",
      "rule": "Implementation fees can be flat rate with split payments (e.g., 40% upfront and 60% on completion)",
      "specificity": "explicit"
    },
    {
      "category": "Implementation Fees",
      "rule": "Set completion payment (60%) to six months in the future",
      "specificity": "explicit"
    },
    {
      "category": "Mid Cycle Upsell",
      "rule": "Prorate new items to match the remaining period of the current contract cycle",
      "specificity": "explicit"
    },
    {
      "category": "Mid Cycle Upsell",
      "rule": "Add new items to the existing contract, not on the new contract",
      "specificity": "explicit"
    },
    {
      "category": "Mid Cycle Upsell",
      "rule": "Kick in the existing invoice cadence for new items",
      "specificity": "explicit"
    },
    {
      "category": "Churns",
      "rule": "Shorten all current billing terms to the new end date",
      "specificity": "explicit"
    },
    {
      "category": "Churns",
      "rule": "Adjust revenue recognition for new shortened period",
      "specificity": "explicit"
    },
    {
      "category": "Replacement Upsell",
      "rule": "End the current contract as you would a churn by shortening billing terms and revenue recognition",
      "specificity": "explicit"
    },
    {
      "category": "Replacement Upsell",
      "rule": "Use the new contract as the new invoice cadence moving forward",
      "specificity": "explicit"
    },
    {
      "category": "Replacement Upsell",
      "rule": "If items were pre-paid upfront or between invoices, add credits as a new negative amount billing term on the new contract titled 'Credit for [item_name]'",
      "specificity": "explicit"
    },
    {
      "category": "Replacement Upsell Identification",
      "rule": "If contract doesn't have 'Business' or 'Business Plus' designation, it's a replacement (not an addon upsell)",
      "specificity": "explicit"
    },
    {
      "category": "Discounts",
      "rule": "Process discounts with discounts on garage",
      "specificity": "explicit"
    },
    {
      "category": "Default Service Term",
      "rule": "If no service term is listed, operations default is 1 Year",
      "specificity": "explicit"
    },
    {
      "category": "Default Net Payment Terms",
      "rule": "If no net payment terms listed, operations default is 0",
      "specificity": "explicit"
    },
    {
      "category": "Default Billing Frequency",
      "rule": "If no billing frequency listed, operations default is Monthly",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "condition": "One-time items like 'New User Classroom'",
      "exception": "Set billing frequency to None instead of using contract billing frequency"
    },
    {
      "condition": "Net terms listed as 'Due upon receipt'",
      "exception": "Use 0 for Net Terms instead of the literal text"
    },
    {
      "condition": "Implementation fees with split payments",
      "exception": "Create multiple billing terms with specific timing (40% upfront, 60% at 6 months)"
    },
    {
      "condition": "Mid-cycle contract amendments",
      "exception": "Prorate charges instead of using standard billing periods"
    },
    {
      "condition": "Pre-paid items in replacement upsells",
      "exception": "Create negative billing terms (credits) on new contract"
    },
    {
      "condition": "Contract lacks 'Business' or 'Business Plus' designation",
      "exception": "Treat as replacement upsell rather than addon"
    },
    {
      "condition": "Merchant-specific processing requirements",
      "exception": "May differ by contract (e.g., always back-date invoice date to final day of the month)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Product naming conventions",
      "examples": ["New User Classroom", "Business", "Business Plus"],
      "customization_needed": "Product names used for classification may vary by merchant"
    },
    {
      "element": "Discount processing location",
      "reference": "Process discounts with discounts on garage",
      "customization_needed": "Specific system or module for discount processing may be merchant-specific"
    },
    {
      "element": "Invoice date handling",
      "reference": "Always back-date invoice date to final day of the month",
      "customization_needed": "Invoice dating rules may differ by merchant or contract"
    },
    {
      "element": "Implementation fee split percentages",
      "reference": "40% upfront and 60% on completion",
      "customization_needed": "Split percentages and timing may vary by merchant agreement"
    },
    {
      "element": "Completion timeline for implementation",
      "reference": "Set 60% to six months in the future",
      "customization_needed": "Timeline may vary based on merchant's implementation schedule"
    },
    {
      "element": "Tax handling",
      "reference": "How do we handle taxes as a line item",
      "customization_needed": "Tax treatment appears to be an open question requiring merchant-specific guidance"
    },
    {
      "element": "Contract ignore rules",
      "reference": "Anything to ignore in contracts",
      "customization_needed": "Items to ignore may vary by merchant, though current guidance says ignore nothing"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: MIS_ Crelate_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:29

### Original Content
```
id 2335353236226648390 Discussed: End-to-end AR and revenue automation Tabs automates invoicing, collections, revenue recognition, renewals, and reporting from contract execution reducing manual work, improving accuracy, and syncing data back to the ERP (e g , QuickBooks) Customizable, audit-friendly workflows Tabs supports granular rev rec by SKU category, handles billing changes mid-cycle, syncs with HubSpot, and offers flexible controls for things like credit card fee logic, user permissions,...
```

### LLM Analysis Response
```json
{
  "themes": [
    "End-to-end AR and revenue automation capabilities",
    "Integration and synchronization with ERP systems (QuickBooks, HubSpot)",
    "ROI metrics and business value (accuracy, cost reduction, efficiency)",
    "AI-powered contract processing and revenue recognition automation",
    "Customizable workflows and audit compliance"
  ],
  "rules": [
    "Revenue recognition must be granular by SKU category",
    "System must sync data back to ERP systems (e.g., QuickBooks)",
    "AI contract extraction must achieve 90-95% accuracy with 100% accurate audit layer",
    "Platform must support mid-cycle billing changes",
    "Workflows must be audit-friendly and compliant",
    "System must handle contract exception processing",
    "Integration with QuickBooks requires one-click process capability",
    "Legacy data must be pullable during system integration",
    "Credit card fee logic must be configurable",
    "User permissions must be flexible and controllable"
  ],
  "exceptions": [
    "Contract exception handling requires flexible controls",
    "Mid-cycle billing changes need special accommodation",
    "Credit card fee logic can be customized per merchant requirements",
    "Accuracy issues with current solution (Chart B) need to be addressed as special case"
  ],
  "merchant_specific": [
    "ERP system type (QuickBooks mentioned, but may vary by merchant)",
    "CRM integration preferences (HubSpot mentioned)",
    "SKU category structure for revenue recognition",
    "Credit card fee logic preferences",
    "User permission hierarchy and access levels",
    "DSO (Days Sales Outstanding) targets and metrics",
    "Specific ROI calculation methodology per merchant",
    "Contract terms and exception types unique to merchant",
    "Legacy data structure and migration requirements"
  ],
  "confidence_score": 0.75
}
```

---

## Chunk 4: MIS_ Crelate_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:36

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) Any important information on events billing Integration Items Processing (if necessary) (Entire Section: Implementation Success to fill Post-Go Live) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  So...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Post-Processing and Notification Workflows",
    "Integration Requirements and Data Synchronization",
    "Tax and Event Billing Processing Defaults",
    "Historical Data Migration and Timeline Constraints",
    "Auto-Renewal Invoice Generation"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: If none listed, every tax line item becomes a BT Events Processing",
      "category": "Tax Processing",
      "responsibility": "Implementation Success to fill Post-Go Live"
    },
    {
      "rule": "Integration items must be labeled according to merchant specifications (e.g., Statsig items labeled as 'Sales', Pinata items labeled as 'Software Subscription Bundle')",
      "category": "Integration Item Processing",
      "responsibility": "Implementation Success to fill Post-Go Live"
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Post Processing Communications",
      "responsibility": "Implementation Success to fill Post-Go Live"
    },
    {
      "rule": "Feature requests must be filled by AE prior to Implementation handoff, by Implementation prior to go-live, and by Success post-go-live",
      "category": "Feature Request Management",
      "responsibility": "AE, Implementation, Success (sequential)"
    },
    {
      "rule": "No historical work to be performed pre-1/1/25 until merchant commits to moving forward with Tabs after 7/1/25",
      "category": "Historical Data Migration",
      "priority": "High",
      "condition": "Post opt-out period"
    },
    {
      "rule": "Upon auto-renewal, generate new year of invoicing and contracts in Tabs",
      "category": "Auto-Renewals",
      "priority": "Medium"
    },
    {
      "rule": "HubSpot integration should sync payment data and customer information back to Tabs as source of truth for subscription data",
      "category": "Integration",
      "priority": "High"
    },
    {
      "rule": "Rillet integration should function similar to QBO integration as single source of truth for finance",
      "category": "Integration",
      "priority": "High"
    }
  ],
  "exceptions": [
    {
      "exception": "Integration items labeled differently 'unless otherwise noted by Merchant'",
      "context": "Integration item labeling allows merchant override"
    },
    {
      "exception": "Historical data import delayed until post-opt-out commitment (after 7/1/25)",
      "context": "Merchant (Crelate) specific timeline constraint tied to commitment decision"
    },
    {
      "exception": "Special memos required for certain invoices due to merchant-customer relationships",
      "context": "Customer-specific invoice modifications"
    },
    {
      "exception": "Merchant may keep QuickBooks despite implementing Tabs",
      "context": "Crelate transitioning from Chargebee but evaluating QB retention"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipients and channels",
      "example": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when contracts processed",
      "customization_needed": "Who, Where, When parameters vary by merchant"
    },
    {
      "element": "Integration item labeling conventions",
      "example": "Statsig → Sales, Pinata → Software Subscription Bundle",
      "customization_needed": "Each merchant has different integration vendors and categorization needs"
    },
    {
      "element": "ERP system integration requirements",
      "example": "Rillet for this merchant (Crelate)",
      "customization_needed": "ERP system varies by merchant (Rillet, QBO, etc.)"
    },
    {
      "element": "Historical data migration scope and timing",
      "example": "ARR, Rev Rec, and invoicing historicals; delayed until post-7/1/25 commitment",
      "customization_needed": "Data types and migration timeline merchant-dependent"
    },
    {
      "element": "Customer base characteristics",
      "example": "Large customer base with many auto-renewals",
      "customization_needed": "Volume and renewal patterns vary by merchant"
    },
    {
      "element": "Previous systems being replaced",
      "example": "Crelate replacing Chargebee due to data integrity issues",
      "customization_needed": "Migration context and pain points unique to each merchant"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 5: MIS_ Crelate_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:46

### Original Content
```
app gong io call id 8675916270037419868 NOTE: All of what we discussed here are not requirements for implementation Specifically, they will not be customizing the payments portal or pulling products from our API Call with Crelate CS team 3 24 - https: us-56595 app gong io call id 5070163611962506640 Discussed: Autorenewals in Tabs and Adendums mid contract Partnership Alignment 3 31 - https: us-56595 app gong io call id 8851219177822041794 Discussed Rillet integration with Tabs, and need to have...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation requirements and scope clarification",
    "Billing and subscription models",
    "Integration capabilities and priorities",
    "Contract modifications and renewals",
    "Cross-functional alignment and handoff processes"
  ],
  "rules": [
    {
      "rule": "Payments portal customization is NOT required for implementation",
      "type": "explicit",
      "source": "NOTE section stating these are not requirements"
    },
    {
      "rule": "Product pulling from API is NOT required for implementation",
      "type": "explicit",
      "source": "NOTE section stating these are not requirements"
    },
    {
      "rule": "Subscription fees are based on number of users and selected modules",
      "type": "explicit",
      "source": "Info on how merchant bills section"
    },
    {
      "rule": "Billing frequency options include: annual, quarterly, semi-annual, or monthly",
      "type": "explicit",
      "source": "Billing information section"
    },
    {
      "rule": "Implementation services are charged separately from subscription fees",
      "type": "explicit",
      "source": "Also charge for implementation services"
    },
    {
      "rule": "Implementation team is the DRI (Directly Responsible Individual) for completion on handoff",
      "type": "explicit",
      "source": "Notes Sections description"
    },
    {
      "rule": "AE fills initial information if available, Implementation completes on handoff",
      "type": "implicit",
      "source": "Notes Sections workflow description"
    }
  ],
  "exceptions": [
    {
      "exception": "Mid-contract addendums are possible for autorenewals",
      "context": "Discussed in Partnership Alignment call on 3/31"
    },
    {
      "exception": "Integration requirements differentiate between 'need to haves' versus 'nice to haves'",
      "context": "Rillet integration discussion on 3/31"
    }
  ],
  "merchant_specific": [
    {
      "element": "Module selection",
      "customization_type": "Merchant chooses which modules to adopt",
      "impact": "Affects subscription pricing"
    },
    {
      "element": "Billing frequency",
      "customization_type": "Merchant selects from four frequency options",
      "impact": "Affects payment schedule and potentially pricing"
    },
    {
      "element": "Number of users",
      "customization_type": "Variable per merchant",
      "impact": "Directly affects subscription fee calculation"
    },
    {
      "element": "Integration requirements (Rillet, Tabs)",
      "customization_type": "Specific integrations discussed per merchant needs",
      "impact": "Affects implementation scope and timeline"
    },
    {
      "element": "Implementation services scope",
      "customization_type": "Separately charged and likely customized per merchant",
      "impact": "Affects total cost and onboarding timeline"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document is somewhat fragmented with incomplete URLs and abbreviated references
- Context from referenced calls (Gong recordings) is summarized but not fully detailed
- Clear explicit rules are present regarding billing and implementation scope
- Some ambiguity around the "Crelate CS team" context and specific merchant identity
- The "NOT requirements" section is clear, but overall implementation requirements are not fully enumerated
- Merchant-specific elements are identifiable but may not be exhaustive

---

## Chunk 6: MIS_ Crelate_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:47

### Original Content
```
Quantities are set upon contract signature This is not usage and addendums are signed when users are added for the outstanding amount they will be billed for in the term 1) What is the merchant temperament Very chill Clark (VP of Finance and Ops, https: www linkedin com in clarkmahy ) and Chris (Controller Accountant, https: www linkedin com in cburks ) are a two person finance team managing AR for 1000  customers They have the ick from Chargebee and are MASSIVE proponents of AI This was an init...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Management and Product Tracking",
    "Invoice Automation and Scheduling",
    "Payment Terms Management",
    "Merchant Stakeholder Profile and Preferences",
    "AI-Driven Process Improvement"
  ],
  "rules": [
    "Quantities are fixed at contract signature time",
    "Addendums are signed when users are added to existing contracts",
    "Addendum billing covers outstanding amounts for the remaining contract term",
    "Products should be tracked by customer from contracts rather than stored in Google Drive",
    "Invoices should be auto-populated based on contract data",
    "Invoice schedules should be automatically generated",
    "Payment terms must be tracked per customer",
    "Invoices should be schedulable immediately upon contract processing completion"
  ],
  "exceptions": [
    "User additions trigger addendums rather than contract modifications",
    "Addendum billing is prorated for remaining term rather than full term billing"
  ],
  "merchant_specific": {
    "stakeholders": [
      "Clark (VP of Finance and Ops) - primary decision maker",
      "Chris (Controller Accountant) - operational user"
    ],
    "team_characteristics": [
      "Two-person finance team managing AR for 1000+ customers",
      "Previous negative experience with Chargebee",
      "Strong preference for AI-driven solutions",
      "CEO-mandated initiative",
      "Highly engaged in product feedback"
    ],
    "current_pain_points": [
      "Contracts stored in Google Drive rather than centralized system",
      "No systematic way to track customer payment terms",
      "Manual invoice population process",
      "Lack of invoice scheduling capabilities"
    ],
    "terminology": [
      "Addendums for user additions",
      "Contract processing completion as trigger point"
    ],
    "merchant_temperament": "Very chill, collaborative, innovation-focused"
  },
  "confidence_score": 0.85
}
```

---

## Chunk 7: MIS_ Crelate_chunk_6

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:59:59

### Original Content
```
Collections: No visibility into accurate AR aging today and cash forecasting With a large customer base, its very hard to understand which invoices are outstanding by customer Payments: Want to push Credit Card fees onto their customers with Tabs They are currently losing  250k per year in Stripe fees Huge value add for them and immediate win for Tabs Reporting: Doing Rev Rec and ARR reporting in Excel today Debating whether to do this in Tabs or Rillet Source of Truth for Finance: Want one sour...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Accounts Receivable Management and Visibility",
    "Payment Processing and Fee Optimization",
    "Financial Reporting and Revenue Recognition",
    "System Integration and Data Centralization",
    "Cash Flow and Reconciliation Processes"
  ],
  "rules": [
    {
      "rule": "Credit card processing fees must be passed onto customers through Tabs platform",
      "category": "Payment Processing",
      "explicit": true
    },
    {
      "rule": "Financial systems (Tabs and Rillet) must operate bi-laterally as source of truth",
      "category": "System Integration",
      "explicit": true
    },
    {
      "rule": "Invoice payments must be reconciled seamlessly to decrease Days Sales Outstanding (DSO)",
      "category": "Cash Application",
      "explicit": true
    },
    {
      "rule": "AR aging reports must provide accurate visibility for cash forecasting",
      "category": "Collections",
      "explicit": false
    },
    {
      "rule": "Outstanding invoices must be trackable by individual customer",
      "category": "Collections",
      "explicit": true
    },
    {
      "rule": "Revenue Recognition (Rev Rec) and Annual Recurring Revenue (ARR) reporting must be systematized beyond Excel",
      "category": "Reporting",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Rev Rec and ARR reporting location is undecided - may be handled in either Tabs or Rillet",
      "condition": "Decision pending on which system will own this reporting function"
    },
    {
      "exception": "Source of truth can be either Tabs or Rillet, not necessarily one specific system",
      "condition": "Flexibility in system designation as long as bi-lateral integration is maintained"
    }
  ],
  "merchant_specific": [
    {
      "element": "Large customer base requiring scalable invoice tracking",
      "customization_need": "Volume-based AR management capabilities"
    },
    {
      "element": "$250k annual loss in Stripe fees",
      "customization_need": "Specific fee pass-through calculation and implementation strategy"
    },
    {
      "element": "Current Excel-based Rev Rec and ARR reporting",
      "customization_need": "Migration strategy from manual Excel processes to automated system"
    },
    {
      "element": "Tabs and Rillet dual-system architecture",
      "customization_need": "Custom integration requirements between two specific platforms"
    },
    {
      "element": "DSO reduction priority",
      "customization_need": "Merchant-specific DSO targets and reconciliation workflows"
    }
  ],
  "confidence_score": 0.85
}
```

---

