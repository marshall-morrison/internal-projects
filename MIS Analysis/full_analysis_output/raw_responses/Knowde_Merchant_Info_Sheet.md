# Raw LLM Analysis: Knowde - Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:31:31

---

## Chunk 1: Knowde - Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:31:31

### Original Content
```
Cesium, Inc d b a Knowde F Demo date: Jul 11, 2024 Scoping start date: Jul 17, 2024 MSA Signature Date: Aug 20, 2024 - Needs updating Onboarding Kick Off Date: Aug 26, 2024 - Need Updating [If Exists] Opt Out Date: Mar 1, 2025 Go Live Date: Feb 7, 2024 - Needs Updating GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Controller (Champion): Griffin Walker - griffin walker knowde com Director of FP A (Decision-Maker): Brian Young - brian young knowde com Head of Finance   ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Implementation Timeline and Milestones",
    "Stakeholder Management and Key Contacts",
    "Business Model and Company Operations",
    "System Integration and Technical Requirements",
    "Financial Operations and Automation Goals"
  ],
  "rules": [
    {
      "rule": "MSA Signature Date must be established and kept current",
      "source": "MSA Signature Date: Aug 20, 2024 - Needs updating",
      "type": "contractual"
    },
    {
      "rule": "Onboarding Kick Off Date must be scheduled and maintained",
      "source": "Onboarding Kick Off Date: Aug 26, 2024 - Need Updating",
      "type": "process"
    },
    {
      "rule": "Go Live Date must be tracked and updated",
      "source": "Go Live Date: Feb 7, 2024 - Needs Updating",
      "type": "process"
    },
    {
      "rule": "Netsuite should serve as the source-of-truth for invoicing",
      "source": "Streamline invoicing and have Netsuite as source-of-truth",
      "type": "technical"
    },
    {
      "rule": "Revenue recognition must be consolidated within one platform",
      "source": "Consolidate rev rec within one platform",
      "type": "financial"
    },
    {
      "rule": "Tabs platform should be leveraged as full A/R platform",
      "source": "Leverage Tabs as a full A R platform",
      "type": "technical"
    },
    {
      "rule": "Salesforce to Netsuite integration is required for billing data access",
      "source": "Salesforce to Netsuite integration and ability to pull in billing data for sales CS teams to have visibility",
      "type": "technical"
    },
    {
      "rule": "Key stakeholders must be identified across Controller, FP&A, Finance Ops, and Accounting roles",
      "source": "Key people at Merchant section",
      "type": "organizational"
    }
  ],
  "exceptions": [
    {
      "exception": "Opt Out Date is conditional - only applicable if it exists",
      "condition": "[If Exists] Opt Out Date: Mar 1, 2025",
      "impact": "Not all implementations may have an opt-out provision"
    },
    {
      "exception": "Company business model changed from marketplace to digitization focus",
      "condition": "Was functioning as a marketplace, but recently changed scope",
      "impact": "Implementation requirements may differ from original marketplace model"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Name",
      "value": "Cesium, Inc d b a Knowde F",
      "customization_needed": true
    },
    {
      "element": "Industry Vertical",
      "value": "Chemical and ingredient industry",
      "customization_needed": true
    },
    {
      "element": "Key Personnel",
      "value": "Griffin Walker (Controller), Brian Young (Director of FP&A), Aleks Lyng (Head of Finance Ops), Gracie Turk (Staff Accountant)",
      "customization_needed": true
    },
    {
      "element": "ERP System",
      "value": "Netsuite (implied from goals)",
      "customization_needed": true
    },
    {
      "element": "CRM System",
      "value": "Salesforce",
      "customization_needed": true
    },
    {
      "element": "Business Model",
      "value": "Product data digitization for suppliers and distributors",
      "customization_needed": true
    },
    {
      "element": "Primary Success Metric",
      "value": "Reduce number of hours to complete projects",
      "customization_needed": true
    },
    {
      "element": "Implementation Dates",
      "value": "Demo: Jul 11, 2024; Scoping: Jul 17, 2024; MSA: Aug 20, 2024; Kickoff: Aug 26, 2024; Go Live: Feb 7, 2024",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Knowde - Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:31:31

### Original Content
```
Billing model Platform fees billed quarterly, biannually, and annually Also have professional services as a growing billing element - will be billed monthly Contract Processing Steps Please note that this merchant is very picky and will review every single contract, please ensure that there s additional review and audit in place and that you re following the instructions closely Steps to process Each Item should be processed as its own Revenue Schedule This is important to note Do NOT have more ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Revenue Recognition",
    "Billing Models and Payment Terms",
    "Product SKU Standardization and Naming Conventions",
    "Quality Control and Review Requirements",
    "System Integration and Feature Requests"
  ],
  "rules": [
    "Each item must be processed as its own Revenue Schedule - do NOT combine multiple billing items under the same revenue schedule",
    "Revenue category must match item name 1:1",
    "Platform fees are billed quarterly, biannually, and annually",
    "Professional services are billed monthly",
    "All SKUs must include the word 'subscription' even if the contract doesn't explicitly state it",
    "Item names must match the approved list: Master Data Management Platform Subscription, Customer Experience Application Subscription, Knowde's Professional Services Support Hours, PIM Solution, White Label Solution, White Label PIM Solution, Basic Storefront Solution",
    "If item name is not in the approved list, escalate to Ashni via Slack",
    "Discounts must be prorated based on individual subscription values using net BT (gross - discount)",
    "Use 'Order Effective Dates' for billing trigger (latter date between two signature dates)",
    "Use 'Subscription Dates' for Revenue Recognition",
    "Subscription term should follow contract language exactly",
    "Default Net Payment Terms: 0 if none listed",
    "Default Billing Frequency: Monthly if none listed",
    "Integration items will use the same name as the item name",
    "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed in Active phase"
  ],
  "exceptions": [
    "This merchant is very picky and requires additional review and audit beyond standard process",
    "If new revenue categories appear, flag them for review rather than processing",
    "If no subscription term is listed, check with manager or implementation manager before proceeding",
    "Ops International Team should ignore AE Implementation Notes sections",
    "Netsuite setup uses invoicing flow without sales orders for e-commerce business (though merchant is open to changing this)",
    "E-commerce business is being phased out to focus on merchant operations"
  ],
  "merchant_specific": [
    "Merchant name: Knowde (inferred from product names like 'Knowde's Professional Services')",
    "Specific contact person: Ashni (for SKU escalations)",
    "Specific contact person: Azmat Aziz (Customer Success, for completion notifications)",
    "Communication channel: Messari internal merchant channel",
    "Example customer reference: Coast Southwest",
    "Uses Avalara for tax management",
    "Cash app identified as a payment pain point",
    "Netsuite integration in place",
    "Salesforce integration requested for Q1 (push invoice status back to SFDC for CSM visibility)",
    "Specific product suite: Master Data Management, Customer Experience Application, PIM Solution, White Label solutions, Basic Storefront",
    "Reference to specific processed example: garage.tabsplatform.com/prod/contracts/d6cf5ee9-6870-40d3-92a1-6de579e454bf/terms/revenue"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Knowde - Merchant Info Sheet_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:31:44

### Original Content
```
They asked if it's on our future roadmap Netsuite customers have Salesforce details SKUs   Pre-discount Price   Amount to use in BTs Product A    200,000    190,000 Product B    400,000    380,000 Description in Contract   Integration Items
```

### LLM Analysis Response
```json
{
  "themes": [
    "System Integration and Roadmap Planning",
    "Pricing Structure and Discounting",
    "Multi-System Data Management (Netsuite and Salesforce)",
    "Contract and Billing Terms Configuration",
    "Product Pricing Reconciliation"
  ],
  "rules": [
    "Pre-discount prices must be recorded separately from amounts used in billing transactions (BTs)",
    "Product pricing requires two values: Pre-discount Price and Amount to use in BTs",
    "SKU details must be maintained across both Netsuite and Salesforce systems",
    "Contract descriptions should reference integration items when applicable",
    "Discount amounts are calculated as the difference between Pre-discount Price and BT Amount (Product A: 10,000 discount, Product B: 20,000 discount)"
  ],
  "exceptions": [
    "Integration items may have special handling in contract descriptions",
    "Netsuite customers appear to have specific requirements for Salesforce detail synchronization",
    "Future roadmap items may affect current pricing or integration structure"
  ],
  "merchant_specific": [
    "Product naming conventions (Product A, Product B) - likely placeholders for actual merchant SKUs",
    "Specific price points (200,000, 400,000) are merchant-dependent",
    "Discount percentages (5% for Product A, 5% for Product B) may vary by merchant",
    "Integration requirements between Netsuite and Salesforce may differ per merchant",
    "Contract description format for 'Integration Items' may be customized",
    "Currency units are not specified and would be merchant-specific"
  ],
  "confidence_score": 0.65
}
```

**Reasoning for Confidence Score (0.65):**
- The document appears to be fragmentary or notes from a discussion rather than formal documentation
- Context is incomplete (unclear what "they asked" refers to, incomplete sentence structure)
- The data table is clear, but surrounding context about application and business rules is limited
- Some interpretation required to infer the relationship between systems and pricing structure
- Terminology like "BTs" (Billing Transactions) is assumed based on context

---

