# Raw LLM Analysis: Loanwell Merchant Info Sheet _

## Document Overview
- **Total Chunks Analyzed**: 5
- **Analysis Timestamp**: 2025-10-02 11:06:48

---

## Chunk 1: Loanwell Merchant Info Sheet __chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:06:48

### Original Content
```
Merchant Demo date: Feb 7, 2025 Scoping start date: MSA Signature Date: Feb 19, 2025 Onboarding Kick Off Date: Feb 21, 2025 [If Exists] Opt Out Date: Go Live Date: GTM POC: Implementation POC:Jeff ERP: Tax Integration: Key people at Merchant Accountant: Justin https: www linkedin com in justinstraight CFO: Justin https: www linkedin com in justinstraight Customer service rep who is really involved: Account Receivable POC: Justin https: www linkedin com in justinstraight Billing POC Justin https:...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Onboarding Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Merchant Business Context and Goals",
    "Technical Integration Requirements",
    "Contract Terms and Opt-Out Provisions"
  ],
  "rules": [
    "Demo date must be documented before scoping start date",
    "MSA Signature Date must precede Onboarding Kick Off Date",
    "Onboarding Kick Off Date should be scheduled after MSA signature",
    "Key stakeholders must be identified including: GTM POC, Implementation POC, Accountant, CFO, Customer Service Rep, AR POC, and Billing POC",
    "LinkedIn profiles should be captured for key personnel when available",
    "ERP and Tax Integration systems must be documented",
    "Account Executive (AE) is responsible for filling company summary",
    "Both AE and Implementation team are responsible for documenting goals",
    "Three critical goal categories must be documented: Pains, Goals, and Why they're buying Tabs",
    "Opt-out clause existence and conditions must be explicitly documented",
    "Company summary must include what the company does",
    "Go Live Date must be tracked as part of onboarding timeline"
  ],
  "exceptions": [
    "Opt Out Date is conditional - only documented '[If Exists]'",
    "If opt-out clause exists, specific merchant requirements to avoid exercising it must be documented",
    "Some fields may remain empty if not applicable (e.g., ERP, Tax Integration fields shown blank in example)"
  ],
  "merchant_specific": [
    "Merchant name and demo date",
    "All timeline dates (MSA Signature, Kick Off, Go Live, Opt Out)",
    "Specific POC names and contact information",
    "LinkedIn profiles for key personnel",
    "ERP system type",
    "Tax integration system",
    "Company business description and industry vertical",
    "Specific pain points being addressed",
    "Merchant's north star goals",
    "Reasons for purchasing Tabs product",
    "Opt-out clause terms and conditions",
    "Customer service representatives involved in implementation"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Loanwell Merchant Info Sheet __chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:06:53

### Original Content
```
No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant No Information on how merchant bills Flat Subscription Implementation fee How contract is broken up One off things to know about the merchant - We are only rolling on out on their LOS  Loan Origination System  business- basically their SaaS platform - In a future state, they want to scope out and purchase a Tabs upsell expansion for their Marketplace business (this side has...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Service Configuration",
    "Billing Model and Pricing Structure",
    "Merchant Business Scope and Limitations",
    "Customer Portal Features and Future Enhancements",
    "Implementation and Service Start Date Procedures"
  ],
  "rules": [
    {
      "rule": "Billing model is Flat Subscription with Implementation fee",
      "category": "billing",
      "specificity": "explicit"
    },
    {
      "rule": "Service Start Date must be located from 'Effective Date' or 'Subscription Start Date' in agreement or amendment",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Item Name should reference the specific service or software solution being provided (e.g., 'LoanWell SaaS Solution')",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Integration Item field should be left blank",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Billing Type should be set to 'Flat'",
      "category": "billing",
      "specificity": "explicit"
    },
    {
      "rule": "Total Price must include subscription fees, implementation costs, and amendment pricing changes",
      "category": "pricing",
      "specificity": "explicit"
    },
    {
      "rule": "Quantity should specify number of users, licenses, workflows, or other relevant units",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Periods must verify renewal, extension, or modification conditions",
      "category": "contract_processing",
      "specificity": "explicit"
    },
    {
      "rule": "Frequency should be determined from the invoicing schedule in the contract",
      "category": "billing",
      "specificity": "explicit"
    }
  ],
  "exceptions": [
    {
      "exception": "Implementation is only for LOS (Loan Origination System) business/SaaS platform",
      "scope": "Current rollout is limited to one business unit only"
    },
    {
      "exception": "Marketplace business with remittances is excluded from current implementation",
      "scope": "Future state consideration for Tabs upsell expansion"
    },
    {
      "exception": "Feature request for past overdue invoices in customer portal is planned for Q3",
      "scope": "Timeline communicated to Arjun but not to Justin"
    },
    {
      "exception": "No unique customer creation process for this merchant",
      "scope": "Standard process applies"
    }
  ],
  "merchant_specific": [
    {
      "element": "LOS (Loan Origination System) business",
      "type": "business_unit",
      "description": "Primary SaaS platform being implemented"
    },
    {
      "element": "Marketplace business",
      "type": "business_unit",
      "description": "Separate business unit with remittances, not currently in scope"
    },
    {
      "element": "Tabs upsell expansion",
      "type": "future_product",
      "description": "Planned future expansion for Marketplace business"
    },
    {
      "element": "LoanWell SaaS Solution",
      "type": "product_name",
      "description": "Example of merchant's specific service offering"
    },
    {
      "element": "Spanish Translation Amendment",
      "type": "service_amendment",
      "description": "Example of potential service modification"
    },
    {
      "element": "Customer portal overdue invoice visibility",
      "type": "feature_request",
      "description": "Merchant-specific feature request with Q3 timeline"
    },
    {
      "element": "Contract broken up as 'One off things'",
      "type": "contract_structure",
      "description": "Merchant has unique contract breakdown approach"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Loanwell Merchant Info Sheet __chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:02

### Original Content
```
loom com share e8919517428d43b687dbeff1b95b55be Mine: https: us-56595 app gong io call id 283906221102217458 account-id 442100437119775226 https: us-56595 app gong io call id 3577658367042410032 account-id 442100437119775226 https: us-56595 app gong io call id 3550685925728943106 account-id 442100437119775226 https: us-56595 app
```

### LLM Analysis Response
```json
{
  "themes": [
    "External resource references",
    "Video/call recording links",
    "Communication tracking",
    "Documentation sharing"
  ],
  "rules": [],
  "exceptions": [],
  "merchant_specific": [
    "Loom video sharing platform usage",
    "Gong call recording system integration",
    "Specific account ID: 442100437119775226",
    "Multiple call IDs referenced (283906221102217458, 3577658367042410032, 3550685925728943106)",
    "US region identifier (us-56595)"
  ],
  "confidence_score": 0.3
}
```

**Analysis Notes:**

This document chunk appears to be a fragment of URLs and links rather than a complete instruction document. The content consists primarily of:
- Partial Loom sharing link
- Multiple Gong call recording URLs
- Truncated/incomplete text

**Limitations:**
- No actual instructions, rules, or policies are present in this chunk
- The content is fragmented and incomplete
- Cannot extract meaningful operational rules or requirements
- Appears to be metadata or reference links rather than instructional content

**Confidence Justification:**
The low confidence score (0.3) reflects the fact that this chunk does not contain analyzable instruction content. It appears to be either:
1. A reference section with external links
2. An incomplete document fragment
3. Metadata that was accidentally included

To provide a meaningful analysis, a complete instruction document with actual procedural content would be needed.

---

## Chunk 4: Loanwell Merchant Info Sheet __chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:05

### Original Content
```
g , upfront, annual, upon renewal) Implementation is always one time Notes: Amendment number and partner for amendments to be added in additional fields Anything to ignore in contracts Specifics processing things the merchant has requested that may differ by contract (e g always back-date invoice date to final day of the month) Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 0 Default Billing Frequency If None Listed, Ops Default is Mo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing Defaults and Standards",
    "Billing and Invoice Configuration",
    "Integration and Event Processing",
    "Customer-Specific Handling and Communications",
    "Implementation Workflow and Stakeholder Notifications"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Defaults"
    },
    {
      "rule": "Default Net Payment Terms is 0 (Net 0) if none specified",
      "category": "Payment Terms"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Billing Configuration"
    },
    {
      "rule": "Implementation fees are always one-time charges",
      "category": "Fee Classification"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing"
    },
    {
      "rule": "Amendment number and partner information must be added in additional fields for contract amendments",
      "category": "Amendment Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Labeling",
      "example": true
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Labeling",
      "example": true
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific contract processing variations may differ by contract",
      "example": "Always back-date invoice date to final day of the month (merchant-specific request)"
    },
    {
      "exception": "Integration item labeling can be overridden when 'otherwise noted by Merchant'",
      "applies_to": "Pinata integration items"
    },
    {
      "exception": "Certain invoices may require special memos due to merchant-customer relationships",
      "context": "Customer-specific handling"
    },
    {
      "exception": "Invoice changes may be required based on merchant-customer relationship dynamics",
      "context": "Customer Information processing"
    },
    {
      "exception": "Contract specifics may override default processing rules",
      "context": "Items to ignore in contracts section"
    }
  ],
  "merchant_specific": [
    {
      "element": "Contract-specific processing instructions",
      "description": "Merchants may request different processing approaches per contract (e.g., invoice date back-dating)"
    },
    {
      "element": "Integration item labeling conventions",
      "description": "Different merchants (Statsig, Pinata) have specific labeling requirements for their integration items"
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Specific team members need to be notified at specific merchant phases",
      "example": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when contracts are processed in Active phase"
    },
    {
      "element": "Customer-specific invoice requirements",
      "description": "Special memos and invoice modifications based on individual customer relationships"
    },
    {
      "element": "Events billing processing",
      "description": "Handled on a case-by-case basis if necessary, filled by Implementation Success"
    },
    {
      "element": "Feature requests tracking",
      "description": "Merchant-specific feature requests with urgency levels tracked by AE and Implementation Success"
    },
    {
      "element": "Fee timing classifications",
      "description": "Merchants may have different fee timing structures (one-time, upfront, annual, upon renewal)"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 5: Loanwell Merchant Info Sheet __chunk_4

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:07:13

### Original Content
```
gong io call id 7504558327580655886 account-id 442100437119775226 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Flat Subscription Implementation fee Is there any important merchant relationship information - We are only rolling on out on their LOS  Loan Origination System  business- basically their SaaS platform - In a future state, they want to scope out and purchase a Tabs upsell expansion for their Marketplace business (this side has...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Relationship Management and Communication Patterns",
    "Product Implementation Scope and Phasing",
    "Feature Requirements and Product Roadmap",
    "Stakeholder Management and Decision-Making Hierarchy",
    "Billing Model and Revenue Structure"
  ],
  "rules": [
    "International team (Ops International Team) should ignore certain sections marked for AE Implementation",
    "Initial rollout is limited to LOS (Loan Origination System) business only, not Marketplace business",
    "Marketplace business with remittances is explicitly excluded from current scope",
    "CEO approval is required for purchasing decisions",
    "Communication with this merchant type should prioritize scheduled calendar meetings over email/text",
    "Feature requests should be documented but timeline communication to merchant should be managed carefully (internal timeline Q3 was not shared with merchant)",
    "Merchant uses flat subscription billing model with implementation fee"
  ],
  "exceptions": [
    "Future state exception: Marketplace business (with remittances) is planned for future Tabs upsell expansion but excluded from current implementation",
    "Communication exception: Merchant rarely responds to emails or texts, requiring calendar-based engagement strategy",
    "Feature request for customer portal (viewing past overdue invoices) has internal Q3 timeline but was intentionally not communicated to merchant"
  ],
  "merchant_specific": [
    "Merchant operates two distinct business lines: LOS (Loan Origination System) SaaS platform and Marketplace business",
    "Merchant terminology: 'LOS' refers to their Loan Origination System SaaS platform",
    "Key decision maker: Justin Bernard (CEO)",
    "Merchant temperament: 'nice but all over the place', poor email/text responsiveness",
    "Priority features for this merchant: automated invoice creation, renewal dashboard, autocharge setup for bank payments, customer portal for overdue invoices",
    "Billing structure: Flat subscription with implementation fee",
    "Future expansion opportunity: Tabs upsell for Marketplace business segment"
  ],
  "confidence_score": 0.85
}
```

---

