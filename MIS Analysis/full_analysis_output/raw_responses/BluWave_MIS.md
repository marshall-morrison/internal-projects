# Raw LLM Analysis: BluWave MIS

## Document Overview
- **Total Chunks Analyzed**: 8
- **Analysis Timestamp**: 2025-10-02 10:09:21

---

## Chunk 1: BluWave MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:21

### Original Content
```
0Merchant Demo date: Feb 5, 2025 Scoping start date: Feb 17, 2025 MSA Signature Date: Feb 28, 2025 Onboarding Kick Off Date: Mar 17, 2025 [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Tom https: www linkedin com in thomas-dunworth-a335b39b main user CFO: Jeff https: www linkedin com in jeff-berry-4b41b334 champion Controller: Scott https: www linkedin com in scotttruesdale Account Receivable POC: Markup Business- Val...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Technical Integration Requirements",
    "Merchant Business Context and Goals",
    "Point of Contact Assignment by Function"
  ],
  "rules": [
    "Implementation follows a structured timeline with specific milestone dates (Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live)",
    "Key stakeholder roles must be identified and documented (Accountant, CFO, Controller, AR POC, Billing POC, etc.)",
    "LinkedIn profiles should be captured for key personnel for verification and networking purposes",
    "GTM POC (Go-To-Market Point of Contact) must be assigned",
    "Implementation POC must be designated",
    "Technical integration points must be documented (ERP, Tax Integration, SFDC, Snowflake, S3)",
    "Multiple POCs may be assigned for a single function (e.g., 'Tom and Val' for Billing)",
    "Company summary must include what the company does",
    "Goals section must define merchant's objectives and pain points being solved",
    "AE (Account Executive) is responsible for filling company summary",
    "AE and Implementation team jointly fill goals section",
    "Opt Out Date is conditional field marked as '[If Exists]'"
  ],
  "exceptions": [
    "Opt Out Date is optional and only included if it exists",
    "Some fields may have multiple assignees (e.g., Billing POC can have two people)",
    "Referral Business field may reference existing contacts from other roles",
    "Not all technical integrations may be required (ERP, Tax Integration, SFDC, Snowflake, S3 are listed but may be selectively used)"
  ],
  "merchant_specific": [
    "All timeline dates (Demo date, Scoping start date, MSA Signature Date, etc.)",
    "Names and LinkedIn profiles of all key personnel",
    "ERP system type",
    "Tax integration platform",
    "Specific technical systems in use (SFDC, Snowflake, S3)",
    "Company business model and industry description",
    "Merchant's specific goals and pain points",
    "Referral source information",
    "Role assignments (who serves as champion, main user, etc.)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: BluWave MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:21

### Original Content
```
Why are they buying Tabs Pains: Manual Cash app- Val doing manual application in NS today Is there an opt out clause If so, what is the merchant looking for so they do not exercise it No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant They will need a Customer   subcustomer set up for Referral business: Customer- Service Provider Sub customer- Client engagement Products- Milestones Information on how merchant bills See abov...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Three-party referral billing model (Service Provider, Client, BluWave)",
    "Customer hierarchy structure (Parent Customer and Sub-customer setup)",
    "Contract processing with percentage-based revenue calculation",
    "Document types and their roles in billing (Referral Agreement, MSA/SOW, Support documents)",
    "Revenue recognition limited to referral percentage only"
  ],
  "rules": [
    "Products must only be created at the sub-customer level, never at parent level",
    "Revenue tracking is exclusively between Service Provider and BluWave (not SP-Client revenue)",
    "Product pricing must be calculated by multiplying child-level contract price by parent-level referral percentage",
    "Referral percentage is defined in a table at the top of the Referral Agreement document",
    "Parent customer Referral Agreement document must be titled '[Customer Name] Referral Agreement'",
    "Three document types required for billing: Referral Agreement (BluWave-SP), MSA/SOW (SP-Client), and Support documents (actuals)",
    "Service Start Date must be located from 'Effective Date' or project start date in SOW/contract",
    "Contract duration (Months of Service) must be identified from the initial term in the contract",
    "Only recognize revenue for the referral percentage, not full SP-Client billing amount",
    "Both parent-level Referral Agreement AND child-level contract are required to create products"
  ],
  "exceptions": [
    "No opt-out clause exists for this merchant",
    "Parent customer may have multiple documents, but only the one titled '[Customer Name] Referral Agreement' should be used",
    "Billing model needs to be filled in by AE and Implementation team",
    "Manual Cash app process currently being used (Val doing manual NS application)"
  ],
  "merchant_specific": [
    "Merchant name: BluWave",
    "Customer/Sub-customer hierarchy: Customer = Service Provider, Sub-customer = Client engagement",
    "Product naming convention: Milestones (e.g., 'Milestone 1')",
    "Referral percentage varies by Service Provider and is defined in individual agreements",
    "Three-party relationship structure unique to this merchant's business model",
    "Manual application process in NetSuite (NS) currently in use",
    "Specific document naming convention: '[Customer Name] Referral Agreement'",
    "Referral agreement template is standardized with percentage table at top"
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 3: BluWave MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:32

### Original Content
```
Item Name: Look for the title of the project, service, or software solution being provided Item Description: Leave blank Integration Item: Leave blank Billing Type: Determine whether the contract follows a fixed fee, milestone-based, or performance-based pricing model Total Price: Locate the total fees, including any breakdowns by phases, resources, or cost structure When a service provider s SOW includes both a low and a high range for invoice estimates, default to the low range When sub-custom...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Data Extraction and Field Mapping",
    "Pricing Models and Financial Terms",
    "Default Values and Fallback Rules",
    "Data Simplification and Granularity Management",
    "Billing Timing and Invoice Scheduling"
  ],
  "rules": [
    "Item Name should contain the title of the project, service, or software solution",
    "Item Description field should be left blank",
    "Integration Item field should be left blank",
    "Billing Type must be determined as fixed fee, milestone-based, or performance-based",
    "Total Price should include all fees with breakdowns by phases, resources, or cost structure",
    "When service provider SOW includes low and high range estimates, default to the low range",
    "For overly granular sub-customer contract line items, use summary-level groupings instead of detailed items",
    "Quantity should identify number of licenses, service units, or hours allocated",
    "Start Date must be the official commencement date from the agreement",
    "Periods should be classified as one-time engagement, recurring service, or ongoing retainer",
    "Frequency should identify how often invoices are issued",
    "Default billing timing is 'bill last of period'",
    "Default service term is 1 year when not specified in contract",
    "Default net payment terms is 0 days when not specified",
    "Default billing frequency is monthly when not specified"
  ],
  "exceptions": [
    "When invoice estimates have a range (low to high), use the low range value instead of high or average",
    "Sub-customer contracts with excessive detail require aggregation to summary level rather than full extraction",
    "Merchant-specific processing may differ by contract (e.g., backdating invoice dates to final day of month)",
    "Tax handling as line items requires special processing (rule incomplete in document)"
  ],
  "merchant_specific": [
    "Bluwave preference for summary-level groupings over granular line items",
    "Contract-specific processing variations (e.g., invoice date backdating to month-end)",
    "Merchant may have custom rules for handling taxes as line items",
    "Ops team defaults (1 year term, 0 net payment terms, monthly frequency) may vary by merchant",
    "Service provider SOW range handling may be merchant-configurable"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 4: BluWave MIS_chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:44

### Original Content
```
If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) (Implementation Success to fill) Any important information on events billing Integration Items Processing (if necessary) (Implementation Success to fill) What are the instructions for assigning integration items Example: All Statsig integrations items should be labeled as  Sales  Example: All  Pinata  integration items should be labeled as  Software Subscription Bundle  unless otherwise noted by Merc...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Tax and billing event processing workflows",
    "Integration item categorization and labeling",
    "Post-processing communication protocols",
    "Customer-specific handling requirements",
    "Feature requests and call documentation tracking"
  ],
  "rules": [
    {
      "rule": "Default tax line item processing: All tax line items become BT Events Processing when none are specifically listed",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Statsig integration items must be labeled as 'Sales'",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Pinata integration items must be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Labeling",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling operational defaults, integration processing instructions, and customer information",
      "category": "Team Responsibilities",
      "explicit": true
    },
    {
      "rule": "Ops Team must notify designated team members upon completion of processing batches",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Notification requirements vary by merchant phase (Implementation or Active)",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Feature requests require documentation of: what it is, why it's important, and urgency level",
      "category": "Feature Request Management",
      "explicit": true
    },
    {
      "rule": "Rewatch calls must be documented with Gong.io links for disco, custom demo, and demo feedback sessions",
      "category": "Documentation",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Pinata integration items can have different labels if 'otherwise noted by Merchant'",
      "condition": "Merchant provides specific instructions"
    },
    {
      "exception": "Special memos may be required for certain invoices based on merchant-customer relationships",
      "condition": "Specific customer relationships require custom handling"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship specifics",
      "condition": "Customer-specific requirements exist"
    }
  ],
  "merchant_specific": [
    {
      "element": "Tax line item processing rules",
      "customizable": true,
      "note": "Defaults to BT Events Processing but can be customized per merchant"
    },
    {
      "element": "Integration item labeling",
      "customizable": true,
      "note": "Examples given for Statsig and Pinata, but each merchant may have different integration vendors requiring specific labels"
    },
    {
      "element": "Post-processing notification recipients",
      "customizable": true,
      "note": "Example shows Azmat Aziz from Customer Success, but varies by merchant"
    },
    {
      "element": "Notification timing and channels",
      "customizable": true,
      "note": "When to notify (e.g., contract processing) and where (e.g., internal merchant channel) varies by merchant"
    },
    {
      "element": "Customer information and special memos",
      "customizable": true,
      "note": "Specific to each merchant's customer base and relationships"
    },
    {
      "element": "Merchant phase designation",
      "customizable": true,
      "note": "Implementation vs Active phase affects processing requirements"
    }
  ],
  "confidence_score": 0.75
}
```

**Reasoning for Confidence Score (0.75):**
- The document appears to be a template or form with incomplete sections marked "(Implementation Success to fill)"
- Clear examples are provided for some rules (Statsig, Pinata, notification example)
- Some sections are fragmentary or cut off (end of document appears truncated)
- The structure is clear but content completeness varies by section
- Terminology is specific but context could be clearer for some operational processes

---

## Chunk 5: BluWave MIS_chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:47

### Original Content
```
id 4837951014932591331 NS Scoping https: us-56595 app gong io call id 3019649572402883206 SFDC Scoping https: us-56595 app gong io call id 7788091213121386800 Solutions Dry run https: us-56595 app gong io call id 2680703784817091416 Technical Solutions Presentation https: us-56595 app gong
```

### LLM Analysis Response
```json
{
  "themes": [
    "Meeting/Call Documentation",
    "Project Scoping Activities",
    "Technical Solutions Process",
    "Gong Platform Integration"
  ],
  "rules": [
    "Multiple scoping sessions are required (NS Scoping and SFDC Scoping identified)",
    "Solutions require a dry run phase before final presentation",
    "Technical solutions must be formally presented",
    "All sessions should be documented with unique identifiers",
    "Gong platform (us-56595 instance) is used for call recording and tracking"
  ],
  "exceptions": [
    "Insufficient data to identify specific exceptions or conditional requirements from this document chunk"
  ],
  "merchant_specific": [
    "Gong instance identifier (us-56595) - likely merchant-specific",
    "NS Scoping - may refer to NetSuite or merchant-specific namespace scoping",
    "SFDC Scoping - likely Salesforce-related, implementation may vary by merchant",
    "Specific call IDs appear to be unique to this merchant's implementation process",
    "The sequence and types of scoping sessions may be customized per merchant needs"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for Low Confidence Score:**
- The document chunk appears to be a fragment or list of URLs/references rather than complete instructional content
- Limited context makes it difficult to extract comprehensive rules or understand full processes
- No explicit policy statements or detailed requirements are provided
- The content seems to be metadata or navigation links rather than substantive instructions
- Cannot determine implicit rules with high certainty due to incomplete information

---

## Chunk 6: BluWave MIS_chunk_5

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:09:55

### Original Content
```
io call id 2607662941098577658 Partnership- implementation, CS, pricing, ROI https: us-56595 app gong io call id 1935952502197590868 Negotiations https: us-56595 app gong io call id 7195472802035490700 Required Capabilities Workshop https: us-56595 app gong io call id 1784998193930395587 Custom demo for Tom testing out invoices https: us-56595 app
```

### LLM Analysis Response
```json
{
  "themes": [
    "Sales and partnership discussions",
    "Product demonstrations and testing",
    "Commercial negotiations and pricing",
    "Implementation and customer success processes",
    "ROI analysis and capability workshops"
  ],
  "rules": [
    "Multiple stakeholder calls are tracked via Gong.io platform",
    "Call IDs are used for reference and documentation purposes",
    "Partnership discussions include implementation, customer success, and pricing components",
    "Custom demos are conducted for specific features (e.g., invoices)",
    "Required capabilities workshops are part of the sales/implementation process",
    "Negotiations are tracked as separate discussion points"
  ],
  "exceptions": [
    "Custom demo created specifically for user 'Tom' to test invoice functionality",
    "Different call types serve different purposes in the sales cycle (partnership vs. negotiation vs. workshop vs. demo)"
  ],
  "merchant_specific": [
    "Gong.io call tracking system with specific URL structure (us-56595.app.gong.io)",
    "Unique call IDs for each interaction type",
    "Custom demo requirements may vary by merchant contact or use case",
    "Partnership structure including CS (Customer Success) and ROI components",
    "Invoice feature testing requirements",
    "Required capabilities may differ based on merchant needs"
  ],
  "confidence_score": 0.45
}
```

**Reasoning for low confidence score**: The document chunk appears to be a fragmented list of Gong.io call links with minimal context. The content lacks complete sentences, detailed instructions, or comprehensive rule statements. The analysis is based on inferring patterns from call titles and URL structures rather than explicit documented rules or guidelines. More complete documentation would be needed for higher confidence in the extracted patterns.

---

## Chunk 7: BluWave MIS_chunk_6

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:04

### Original Content
```
gong io call id 8594379417957792457 Negotiations pt 3 https: us-56595 app gong io call id 1747923342785272927 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills 2 business motions: Markup and refferal Markup: hourly rate or flat percentage Referral: Milestone billing Takes a   fee Is there any important merchant relationship information We will roll out on Referral business first bc they are considering bringing on a new hr tracking tool (cu...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Dual Business Model Operations (Markup vs Referral)",
    "Milestone-Based Billing and Revenue Recognition",
    "System Integration and Data Flow (NetSuite, SFDC, S3)",
    "Phased Implementation Strategy",
    "Customer/Sub-customer Hierarchical Structure"
  ],
  "rules": [
    {
      "rule": "Referral business requires Customer/Sub-customer setup where Customer = Service Provider and Sub-customer = Client engagement",
      "category": "data_structure"
    },
    {
      "rule": "Products must be linked to Milestones for Referral business",
      "category": "billing_configuration"
    },
    {
      "rule": "No data should be pushed to SFDC from Tabs platform",
      "category": "integration"
    },
    {
      "rule": "Tabs data must be sent to merchant's S3 bucket instead of SFDC",
      "category": "integration"
    },
    {
      "rule": "NetSuite projects setup should be deprecated once milestone billing is handled by the platform",
      "category": "system_migration"
    },
    {
      "rule": "Referral business should be rolled out first before Markup business",
      "category": "implementation_sequence"
    },
    {
      "rule": "Milestone billing must support auto-update of invoices based on milestone completion",
      "category": "billing_automation"
    },
    {
      "rule": "Remittance use cases for Markup business should be handled by Ramp",
      "category": "payment_processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Markup business has remittance use case that is being pushed to Ramp side instead of being handled internally",
      "context": "payment_processing"
    },
    {
      "exception": "Dunning functionality deferred to potential Q3 design partnership (not committed)",
      "context": "feature_rollout"
    },
    {
      "exception": "Merchant currently uses Tesorio for dunning but open to switching - not immediate requirement",
      "context": "third_party_tools"
    },
    {
      "exception": "Ops International Team should ignore certain sections marked in notes",
      "context": "internal_operations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Two distinct business models: Markup (hourly rate/flat percentage) and Referral (milestone billing with fee)",
      "customization_needed": "Separate billing logic and workflows for each business type"
    },
    {
      "element": "Integration with Ramp for remittance handling",
      "customization_needed": "Custom integration setup with Ramp platform"
    },
    {
      "element": "S3 bucket data delivery instead of SFDC integration",
      "customization_needed": "Custom data export pipeline to specific S3 bucket"
    },
    {
      "element": "Existing NetSuite projects structure to be migrated",
      "customization_needed": "Migration plan from NetSuite projects to platform's milestone system"
    },
    {
      "element": "Tesorio currently used for dunning",
      "customization_needed": "Potential future migration from Tesorio to platform dunning"
    },
    {
      "element": "Merchant temperament: quiet, non-reactive but engaged listeners",
      "customization_needed": "Communication style adjustment - may need more proactive follow-up and written summaries"
    },
    {
      "element": "HR tracking tool being considered for Referral business",
      "customization_needed": "Potential integration requirements with new HR tracking system"
    }
  ],
  "confidence_score": 0.82
}
```

---

## Chunk 8: BluWave MIS_chunk_7

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:10:08

### Original Content
```
They typically have delayed reactions Jeff is the most vocal Jeff is very understanding and easy to work with He s a SUPER strong champion They appreciate when you bring energy 2) Is there a key POC: (i e : who is the buyer decision maker ) Jeff but he really cares about what the team thinks, particularly Tom 3) What are the Tabs features that the key POC cares about Milestone billing- auto update of invoices when milestone completion documentation is ingested into Tabs Automatic invoice creatio...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Decision-Making Dynamics",
    "Product Feature Requirements and Priorities",
    "Customer Communication and Relationship Style",
    "Workflow Automation and Manual Process Replacement",
    "Implementation Timeline and Phasing"
  ],
  "rules": [
    "Jeff is the primary decision maker but requires team consensus, particularly from Tom",
    "Energy and enthusiasm should be demonstrated in customer interactions",
    "Milestone billing must auto-update invoices when milestone completion documentation is ingested",
    "Invoice creation should be automated",
    "Cash application process (currently manual by Val) needs automation",
    "Dunning functionality is required but scheduled for later implementation phase"
  ],
  "exceptions": [
    "Despite Jeff being the buyer/decision maker, his decisions are heavily influenced by team input, especially Tom's opinion",
    "Dunning feature implementation is deferred to a later timeline rather than immediate deployment",
    "Customer has delayed reaction patterns which may affect feedback and decision cycles"
  ],
  "merchant_specific": [
    "Key stakeholders: Jeff (vocal, understanding, strong champion, primary POC), Tom (significant influence on decisions), Val (currently handling manual cash application)",
    "Current manual process: Val performing cash application manually",
    "Existing tool to replace: Tesorio (for dunning functionality)",
    "Communication style preference: High energy interactions appreciated",
    "Decision-making style: Collaborative with delayed reactions",
    "Priority features: Milestone billing with auto-updates, automatic invoice creation, cash app automation",
    "Future requirements: Dunning capability to replace Tesorio"
  ],
  "confidence_score": 0.85
}
```

---

