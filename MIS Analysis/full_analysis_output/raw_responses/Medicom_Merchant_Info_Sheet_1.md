# Raw LLM Analysis: Medicom Merchant Info Sheet_(1)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:24:16

---

## Chunk 1: Medicom Merchant Info Sheet_(1)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:24:16

### Original Content
```
Why are they buying Tabs Goals: Why now: - they have a 2025 KPI to hit  10m in rev (currently at  6m) - they plan to bring on 35-50 customers with high ACV from their free tier   paid Pain: Is there an opt out clause If so, what is the merchant looking for so they do not exercise it No Billing model (AE  Implementation to fill) Are there unique things about the customer creation process for this merchant - no Information on how merchant bills - typically, annual upfront - multiyear contracts How...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Configuration",
    "Customer Migration and Integration Setup",
    "Revenue Recognition and Financial Reporting",
    "Quality Control and Validation Requirements",
    "Merchant-Specific Business Context and Pain Points"
  ],
  "rules": [
    "Service start date must be listed on contract",
    "Total months of service must be listed on contract",
    "Item name must be listed on contract",
    "Use QBO Integration Item + Class sheet to map integration items and assigned classes",
    "Include discounts under discount section, not as separate billing terms",
    "Create different billing term for each payment schedule based on payment schedule section",
    "Set Periods to 1 if processing just 1 year per line item",
    "Set Frequency to Yearly if processing a yearly contract",
    "Default to contract net terms; if no net terms specified, use Net 0",
    "1 product in Tabs should agree to 1 contract (1:1 ratio)",
    "Discount sits on product itself",
    "Implementation should always have a 30 month revenue schedule",
    "Flag to Ashni Walia if payment schedule is for more than 1 year AND has different charges for each year",
    "Ignore any waived fees in contracts",
    "Default Service Term: 3 years",
    "Default Net Payment Terms: Net 0",
    "Default Billing Frequency: Annual",
    "No taxes to be processed as line items",
    "Use TOI escalation Google sheet to calculate and verify line item totals",
    "Use TOI Escalation Google Sheet to calculate discount amounts",
    "Reference Riverside Healthcare customer as example for product and discount processing",
    "Cross reference Customer Facing Name column with appropriate QBO product item",
    "Do not change the customer if it mentions 'Uploaded on customer page'",
    "Use Radnet as example for discount processing"
  ],
  "exceptions": [
    "May need 2:1 product-to-contract ratio for customers with quarterly payments (exception to 1:1 rule)",
    "Merchant currently excludes large ($1m+) customers from Chargebee due to billing model limitations, causing reporting inaccuracies",
    "Merchant typically bills annual upfront with multiyear contracts, but specific payment schedules may vary",
    "Contract-specific processing variations may exist (e.g., back-dating invoice dates to final day of month)",
    "No opt-out clause exists for this merchant"
  ],
  "merchant_specific": [
    "Merchant name: Medicom (referenced in Integration Items section)",
    "Current system: Chargebee (migrating from)",
    "2025 KPI: $10m in revenue (currently at $6m)",
    "Growth plan: 35-50 customers from free tier to paid with high ACV",
    "Billing model: Typically annual upfront, multiyear contracts",
    "Major pain point: Reporting inaccuracy due to excluding large ($1m+) customers from previous billing system",
    "Interest in custom key terms",
    "Specific contact: Ashni Walia (for flagging payment schedule issues and product ratio guidance)",
    "Reference customers: Riverside Healthcare (product/discount example), Radnet (discount example), Garage (order form example)",
    "Training resources: LOOM TRAINING RECORDING referenced",
    "Integration: QBO (QuickBooks Online) integration required",
    "Custom documentation: TOI escalation Google sheet, QBO Integration Item + Class sheet, Merchant product page"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Medicom Merchant Info Sheet_(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:24:18

### Original Content
```
Merchant Demo date: Dec 3, 2024 Scoping start date: Dec 3, 2024 MSA Signature Date: Dec 10, 2024 Onboarding Kick Off Date: Jan 3, 2025 [If Exists] Opt Out Date: None Go Live Date: Apr 30, 2025 No hard timeline July Chargebee Renewal- they want to run parallel billing tracks beforehand GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Kelsey Dunn https: www linkedin com in kelsey-dunn-cpa-263394b9  CFO: Brian McCormick https: www linkedin com in brianpmccormick...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Project Timeline and Milestones",
    "Stakeholder Identification and Roles",
    "Integration and Technical Requirements",
    "Billing and Revenue Recognition Processes",
    "Healthcare Industry Context and EHR Solutions"
  ],
  "rules": [
    {
      "rule": "Go Live Date must be established and documented",
      "source": "Go Live Date: Apr 30, 2025",
      "category": "timeline"
    },
    {
      "rule": "MSA Signature Date must precede Onboarding Kick Off Date",
      "source": "MSA Signature Date: Dec 10, 2024, Onboarding Kick Off Date: Jan 3, 2025",
      "category": "timeline"
    },
    {
      "rule": "Parallel billing tracks should be run before system migration",
      "source": "they want to run parallel billing tracks beforehand",
      "category": "billing_process"
    },
    {
      "rule": "Key stakeholders must be identified including: GTM POC, Implementation POC, Accountant, CFO, AR POC, Billing POC, and Renewals/Ops",
      "source": "Key people at Merchant section with defined roles",
      "category": "stakeholder_management"
    },
    {
      "rule": "LinkedIn profiles should be documented for key stakeholders",
      "source": "Multiple LinkedIn URLs provided for key personnel",
      "category": "documentation"
    },
    {
      "rule": "Opt Out Date must be tracked (even if None)",
      "source": "[If Exists] Opt Out Date: None",
      "category": "timeline"
    },
    {
      "rule": "ERP and Tax Integration requirements must be identified",
      "source": "ERP: Tax Integration: fields present",
      "category": "technical_requirements"
    },
    {
      "rule": "Company summary must include what the company does",
      "source": "(AE to fill) Summary of what company does",
      "category": "documentation"
    },
    {
      "rule": "Goals and pain points must be documented",
      "source": "Goals (North star) (AE Implementation to fill) What is the merchant's goal What pain are we solving",
      "category": "requirements_gathering"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date may not exist for all merchants",
      "condition": "[If Exists] notation indicates optional field",
      "example": "Opt Out Date: None"
    },
    {
      "exception": "Customer service rep involvement may not be applicable",
      "condition": "N/A value indicates role may not be relevant for all merchants",
      "example": "Customer service rep who is really involved: N A"
    },
    {
      "exception": "Timeline flexibility based on external renewal dates",
      "condition": "No hard timeline mentioned due to July Chargebee Renewal",
      "example": "No hard timeline July Chargebee Renewal"
    },
    {
      "exception": "Custom key terms parsing may be requested",
      "condition": "Merchant-specific interest in contract parsing features",
      "example": "Interested in the custom key terms parsing from the contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Chargebee as existing billing system",
      "type": "integration",
      "note": "Merchant uses Chargebee and wants parallel billing tracks"
    },
    {
      "element": "Healthcare/EHR industry vertical",
      "type": "industry",
      "note": "Medicom Technologies specializes in healthcare EHR systems"
    },
    {
      "element": "Revenue Recognition sensitivity",
      "type": "accounting_requirement",
      "note": "Accountant Kelsey Dunn will press on Rev Rec - indicates complex revenue recognition needs"
    },
    {
      "element": "Parallel billing cycles requirement",
      "type": "process",
      "note": "Interested in running parallel cycles in Chargebee before full migration"
    },
    {
      "element": "Custom contract parsing needs",
      "type": "feature_request",
      "note": "Elizabeth Maierhofer interested in custom key terms parsing from contracts"
    },
    {
      "element": "Spreadsheet-based discovery process",
      "type": "process",
      "note": "Ask for Elizabeth to share the spreadsheet, discovery"
    },
    {
      "element": "Key stakeholder: Kelsey Dunn (CPA)",
      "type": "personnel",
      "note": "Serves multiple roles: Accountant, AR POC, Billing POC - central figure with accounting expertise"
    },
    {
      "element": "Key stakeholder: Brian McCormick (CFO)",
      "type": "personnel",
      "note": "Recently took over sales team - indicates organizational changes"
    },
    {
      "element": "Key stakeholder: Elizabeth Maierhofer",
      "type": "personnel",
      "note": "Handles Renewals and Ops - interested in contract parsing"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Medicom Merchant Info Sheet_(1)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:24:35

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
      "rule": "Ops Team must identify notification requirements for batch processing completion",
      "category": "Communication Protocol",
      "explicit": true
    },
    {
      "rule": "Implementation Success must document customer-specific information including special memos and invoice requirements",
      "category": "Documentation Requirements",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success must fill Feature Requests section with: what it is, why it's important, and urgency level",
      "category": "Feature Request Documentation",
      "explicit": true
    },
    {
      "rule": "AE and Implementation Success must document Rewatch Calls with dates and notes",
      "category": "Call Documentation",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore certain sections marked for AE and Implementation",
      "category": "Team-Specific Instructions",
      "explicit": true
    },
    {
      "rule": "Merchant relationship information must include: temperament assessment, key POC identification, and feature preferences by stakeholder",
      "category": "Relationship Documentation",
      "explicit": false
    }
  ],
  "exceptions": [
    {
      "exception": "Post Processing Communications are conditional - only if necessary",
      "condition": "Based on whether Ops Team needs to notify anyone"
    },
    {
      "exception": "Notification timing varies by merchant phase (Implementation or Active)",
      "condition": "Depends on merchant's current phase in lifecycle"
    },
    {
      "exception": "Invoice changes may be required due to specific merchant-customer relationships",
      "condition": "Based on individual customer requirements within merchant account"
    },
    {
      "exception": "Sections marked 'Ops International Team to Ignore' have different audience requirements",
      "condition": "Team-specific content visibility"
    }
  ],
  "merchant_specific": [
    {
      "element": "Notification recipients and channels",
      "example": "Customer Success [Azmat Aziz] via Messari internal merchant channel",
      "customizable": true
    },
    {
      "element": "Notification timing triggers",
      "example": "When contracts are processed in Active phase",
      "customizable": true
    },
    {
      "element": "Customer base metrics",
      "example": "1400 customers, 100 paid customers, goal of 135-150 by EOY 2025",
      "customizable": true
    },
    {
      "element": "Billing structure",
      "example": "Upfront Payment Terms, Multiyear agreements",
      "customizable": true
    },
    {
      "element": "Merchant temperament assessment",
      "example": "Very nice and understanding, detail-oriented",
      "customizable": true
    },
    {
      "element": "Key POC roles and preferences",
      "example": "Brian (DM) - Rev rec, cash forecasting; Kelsey (end user) - invoicing and reporting; Lizzie - key terms, renewal clauses",
      "customizable": true
    },
    {
      "element": "Special invoice requirements and memos",
      "example": "Certain invoices require specific memos",
      "customizable": true
    },
    {
      "element": "Feature priorities by stakeholder",
      "example": "Different features matter to different POCs",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

