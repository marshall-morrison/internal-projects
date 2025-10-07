# Raw LLM Analysis: Medicom Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:13:09

---

## Chunk 1: Medicom Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:13:09

### Original Content
```
Why are they buying Tabs Goals: Why now: - they have a 2025 KPI to hit  10m in rev (currently at  6m) - they plan to bring on 35-50 customers with high ACV from their free tier   paid Pain: Is there an opt out clause If so, what is the merchant looking for so they do not exercise it No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant - no Information on how merchant bills - typically, annual upfront - multiyear contracts How...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Customer Migration and Integration (Chargebee to new system)",
    "Revenue Recognition and Reporting Requirements",
    "Product and Discount Mapping Rules",
    "Quality Control and Validation Procedures"
  ],
  "rules": [
    "Service start date must be listed on contract (see red text example)",
    "Total months of service must be listed on contract (see red text example)",
    "Item name must be listed on contract (see red text example)",
    "Integration item: Use QBO Integration Item & Class sheet to determine mapping",
    "Assigned Class in QBO: Use QBO Integration Item & Class sheet to determine mapping",
    "Billing type: Flat",
    "Total price: Use TOI escalation Google sheet to calculate and verify each line item matches",
    "Discounts must be included under discount section, not as a separate billing term",
    "Quantity must be listed on contract (see red text example)",
    "Discount Amount: Use TOI Escalation Google Sheet to calculate",
    "Start Date: Refer to Payment Schedule, create different billing term for each payment schedule",
    "Periods: 1 if processing just 1 year per line item",
    "Frequency: Yearly if processing yearly contract (read contract for billing frequency)",
    "Net Terms: Defer to contract, if no net terms specified use Net 0",
    "1 product in Tabs should agree to 1 contract (1:1 ratio)",
    "Discount sits on product itself",
    "Implementation should always have a 30 month revenue schedule",
    "Use Riverside Healthcare customer as example for product and discount processing",
    "Customer Facing Name column from merchant product page is what appears in contract SOW",
    "Cross reference with appropriate QBO product item",
    "Waived fees should be ignored in contracts",
    "No taxes to be processed as line items",
    "DO NOT CHANGE THE CUSTOMER IF IT MENTIONS 'Uploaded on customer page'"
  ],
  "exceptions": [
    "Discount can be 2:1 ratio for a customer given quarterly payments (exception to 1:1 rule)",
    "If payment schedule is for more than 1 year AND has different charges for each year, flag to Ashni Walia",
    "Merchant has large customers ($1m+) that were not included in Chargebee due to billing model limitations, causing reporting inaccuracies",
    "No opt-out clause exists for this merchant",
    "Specifics processing things may differ by contract (e.g., back-dating invoice date to final day of month) - currently N/A"
  ],
  "merchant_specific": {
    "merchant_context": {
      "current_platform": "Chargebee",
      "revenue_goal": "$10m in 2025 (currently at $6m)",
      "growth_strategy": "Bring on 35-50 customers with high ACV from free tier to paid",
      "typical_billing": "Annual upfront, multiyear contracts",
      "large_customer_threshold": "$1m+"
    },
    "reference_documents": [
      "TOI escalation Google sheet",
      "QBO Integration Item & Class sheet",
      "Merchant product page - Customer Facing Name",
      "ORDER FORM (Garage Example)",
      "LOOM TRAINING RECORDING"
    ],
    "reference_customers": [
      "Riverside Healthcare (example for products and discounts)",
      "Radnet (example for discount processing)"
    ],
    "key_contacts": [
      "Ashni Walia (flag payment schedule issues to this person)"
    ],
    "default_settings": {
      "service_term": "3 years",
      "net_payment_terms": "Net 0",
      "billing_frequency": "Annual",
      "revenue_schedule_for_implementation": "30 months"
    },
    "integration_specifics": {
      "accounting_system": "QBO (QuickBooks Online)",
      "product_mapping": "Medicom Integration Items"
    }
  },
  "confidence_score": 0.85
}
```

---

## Chunk 2: Medicom Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:13:11

### Original Content
```
Merchant Demo date: Dec 3, 2024 Scoping start date: Dec 3, 2024 MSA Signature Date: Dec 10, 2024 Onboarding Kick Off Date: Jan 3, 2025 [If Exists] Opt Out Date: None Go Live Date: Apr 30, 2025 No hard timeline July Chargebee Renewal- they want to run parallel billing tracks beforehand GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Kelsey Dunn https: www linkedin com in kelsey-dunn-cpa-263394b9  CFO: Brian McCormick https: www linkedin com in brianpmccormick...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Billing and Revenue Recognition Requirements",
    "Healthcare Industry Software Solutions",
    "Integration and Technical Requirements"
  ],
  "rules": [
    {
      "rule": "Onboarding process follows structured timeline: Demo → Scoping → MSA Signature → Onboarding Kick Off → Go Live",
      "type": "explicit",
      "category": "process"
    },
    {
      "rule": "Parallel billing tracks must be run before Chargebee renewal transition",
      "type": "explicit",
      "category": "billing"
    },
    {
      "rule": "Multiple POCs must be identified across key functional areas: GTM, Implementation, Billing, Account Receivable, Renewals and Ops",
      "type": "implicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "Key stakeholders should include Accountant, CFO, and operational representatives",
      "type": "implicit",
      "category": "stakeholder_management"
    },
    {
      "rule": "LinkedIn profiles should be documented for key stakeholders",
      "type": "explicit",
      "category": "documentation"
    },
    {
      "rule": "ERP and Tax Integration requirements must be identified during scoping",
      "type": "implicit",
      "category": "technical"
    },
    {
      "rule": "Company summary must include description of merchant's business and products",
      "type": "explicit",
      "category": "documentation"
    },
    {
      "rule": "Goals and pain points must be documented by AE and Implementation team",
      "type": "explicit",
      "category": "discovery"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date can be 'None' if not applicable",
      "condition": "If Exists"
    },
    {
      "exception": "Customer service rep involvement may be N/A for some merchants",
      "condition": "Based on merchant structure"
    },
    {
      "exception": "No hard timeline specified - flexibility around July Chargebee Renewal",
      "condition": "Dependent on merchant readiness and parallel billing testing"
    },
    {
      "exception": "Custom key terms parsing from contracts may be requested",
      "condition": "Merchant-specific interest (Elizabeth's request)"
    }
  ],
  "merchant_specific": [
    {
      "element": "Go Live Date",
      "customization": "Varies by merchant (Apr 30, 2025 for this merchant)"
    },
    {
      "element": "Billing system renewal dates",
      "customization": "Chargebee renewal in July for this merchant"
    },
    {
      "element": "Key stakeholder names and roles",
      "customization": "Kelsey Dunn (Accountant/AR/Billing POC), Brian McCormick (CFO), Elizabeth Maierhofer (Renewals/Ops)"
    },
    {
      "element": "Revenue recognition requirements",
      "customization": "Accountant will press on Rev Rec - indicates heightened scrutiny"
    },
    {
      "element": "Parallel billing cycles requirement",
      "customization": "Interest in running parallel cycles in Chargebee"
    },
    {
      "element": "Custom contract parsing",
      "customization": "Interest in custom key terms parsing from contracts"
    },
    {
      "element": "Industry vertical",
      "customization": "Healthcare/EHR software - may require specific compliance considerations"
    },
    {
      "element": "Discovery artifacts",
      "customization": "Spreadsheet to be shared by Elizabeth during discovery"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Medicom Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:13:28

### Original Content
```
Most of the integration items should be mapped to -DR or DevRev in product name in QBO Moving forward, all  Implementation Services should be mapped to the following (ID66): Post Processing Communications (if necessary) (Implementation Success to fill) Does the Ops Team need to notify anyone on the team re: completion of processing batches in Implementation or Active phase Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal m...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Integration and Product Mapping in QBO",
    "Post-Processing Communication Protocols",
    "Customer and Merchant Relationship Management",
    "Feature Requests and Product Development",
    "Stakeholder Information and Key Points of Contact"
  ],
  "rules": [
    {
      "rule": "Most integration items should be mapped to -DR or DevRev in product name in QBO",
      "category": "Integration Mapping",
      "explicit": true
    },
    {
      "rule": "All Implementation Services should be mapped to ID66",
      "category": "Integration Mapping",
      "explicit": true
    },
    {
      "rule": "Implementation Success team must fill Post Processing Communications section",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Ops Team must identify who needs to be notified about batch processing completion",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Notification requirements must specify: Who, Where, and When",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Customer Success must be notified when contracts are processed in Active phase",
      "category": "Communication Protocol",
      "explicit": true,
      "example": "Azmat Aziz via Messari internal merchant channel"
    },
    {
      "rule": "Implementation Success must document customer-specific information including special memos and invoice requirements",
      "category": "Documentation",
      "explicit": true
    },
    {
      "rule": "Feature Requests must include: description, importance rationale, and urgency level",
      "category": "Feature Request Management",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success must fill Feature Requests and Rewatch Calls sections",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Notes Sections",
      "category": "Responsibility Assignment",
      "explicit": true
    },
    {
      "rule": "Merchant relationship information must document: temperament, key POC/decision maker, and feature preferences by stakeholder",
      "category": "Relationship Management",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Post Processing Communications are conditional - only if necessary",
      "condition": "Based on merchant needs"
    },
    {
      "exception": "Invoice changes may be required due to merchant-customer relationship specifics",
      "condition": "Varies by merchant customer relationship"
    },
    {
      "exception": "Ops International Team explicitly excluded from filling Notes Sections",
      "condition": "Team-specific exclusion"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification channels and recipients",
      "customization_needed": "Each merchant may have different internal channels and stakeholders to notify",
      "example": "Messari internal merchant channel, Azmat Aziz"
    },
    {
      "element": "Billing structure and payment terms",
      "customization_needed": "Varies by merchant (upfront, multiyear agreements, etc.)",
      "example": "Typically Upfront Payment Terms, Multiyear agreements"
    },
    {
      "element": "Customer base metrics",
      "customization_needed": "Each merchant has different customer counts and growth targets",
      "example": "1400 customers, 100 paid customers, goal of 135-150 by EOY 2025"
    },
    {
      "element": "Key stakeholder preferences",
      "customization_needed": "Different POCs care about different features",
      "example": "Brian: Rev rec, cash forecasting; Kelsey: invoicing and reporting; Lizzie: key terms, renewal clauses"
    },
    {
      "element": "Merchant temperament and communication style",
      "customization_needed": "Understanding personality and decision-making dynamics",
      "example": "Very nice and understanding, Kelsey detail-oriented, Brian listens to team"
    },
    {
      "element": "Decision maker hierarchy",
      "customization_needed": "Identifying buyer vs end user vs influencers",
      "example": "Brian is DM, Kelsey is main end user"
    },
    {
      "element": "Special invoice requirements and memos",
      "customization_needed": "Merchant-specific invoice handling needs",
      "example": "Special memos certain invoices require"
    }
  ],
  "confidence_score": 0.85
}
```

---

