# Raw LLM Analysis: Mithril MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 10:17:36

---

## Chunk 1: Mithril MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:17:36

### Original Content
```
1) What is the merchant temperament Vivan- Head of strat finance Easy to work with  totally gets the value of Tabs He was just hired so Tabs is his first big bet Adeesh- Ops Strat- has been there longer than Vivan The one that was previously involved in billing  has an understanding of the systems   workflows Olivier  oh liv ee aye - eng that built their homegrown system Previously worked at stripe Knows their systems well Aparajit- head of engineering- likely will be less involved but he previo...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Management and Team Dynamics",
    "Product Feature Prioritization",
    "Technical System Integration and Legacy Infrastructure",
    "Sales Strategy (PLG and SLG approaches)",
    "Financial Operations and Forecasting"
  ],
  "rules": [
    "Identify key stakeholders and their roles before engagement (Head of Strategic Finance, Operations Strategy, Engineering leads)",
    "Understand each stakeholder's background and relationship to existing systems",
    "Map stakeholder involvement levels based on their historical system ownership",
    "Prioritize features based on stakeholder concerns: dunning, visibility, PLG billing, SLG capabilities, cash forecasting",
    "Recognize when a product (Tabs) represents a stakeholder's first major initiative/bet",
    "Account for stakeholders with prior experience at relevant companies (e.g., Stripe) when discussing technical integration",
    "Distinguish between Product-Led Growth (PLG) and Sales-Led Growth (SLG) billing requirements",
    "Ensure solution addresses both PLG and SLG in unified platform"
  ],
  "exceptions": [
    "Aparajit (head of engineering) may be less involved despite previously setting up systems - reduced engagement for senior technical stakeholders who delegated ownership",
    "Newer hires (Vivan) may have higher engagement and stake in new solutions compared to longer-tenured employees",
    "Stakeholders with homegrown system development experience (Olivier) require different technical conversation approach"
  ],
  "merchant_specific": [
    "Stakeholder names and pronunciations (Vivan, Adeesh, Olivier 'oh liv ee aye', Aparajit)",
    "Organizational structure and reporting lines",
    "Existing homegrown billing system that needs replacement/integration",
    "Historical billing involvement and institutional knowledge distribution",
    "Specific feature priorities: dunning, visibility, PLG billing, SLG capabilities, accurate cash forecasting",
    "Mix of PLG and SLG business models requiring unified solution",
    "Company history with Stripe (through Olivier's background)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Mithril MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:17:42

### Original Content
```
Merchant Name: Mithril Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Anything to ignore in contracts Specifics processing things the merchant ha...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Default Terms",
    "Billing Models and Revenue Recognition",
    "Integration and Event Processing Workflows",
    "Stakeholder Communication and Handoff Procedures",
    "Merchant-Specific Customer and Invoice Handling"
  ],
  "rules": [
    {
      "rule": "Default Service Term is 1 Year if none listed in contract",
      "category": "Contract Defaults",
      "source": "explicit"
    },
    {
      "rule": "Default Net Payment Terms is 0 days if none specified",
      "category": "Contract Defaults",
      "source": "explicit"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "Contract Defaults",
      "source": "explicit"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Transaction) by default",
      "category": "Tax Processing",
      "source": "explicit"
    },
    {
      "rule": "Implementation Success team is responsible for filling Contract Processing Steps post-go-live",
      "category": "Responsibility Assignment",
      "source": "explicit"
    },
    {
      "rule": "AE fills Feature Requests prior to Implementation handoff; Implementation fills prior to go-live; Success fills post-go-live",
      "category": "Responsibility Assignment",
      "source": "explicit"
    },
    {
      "rule": "Implementation team is completion DRI (Directly Responsible Individual) for Notes Sections on handoff",
      "category": "Responsibility Assignment",
      "source": "explicit"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Labeling",
      "source": "explicit_example"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Item Labeling",
      "source": "explicit_example"
    }
  ],
  "exceptions": [
    {
      "exception": "Invoice dates may be back-dated to final day of the month per specific merchant contract requests",
      "condition": "Merchant-specific processing requirements that differ by contract",
      "category": "Contract Processing"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "condition": "Unless otherwise noted by Merchant",
      "category": "Integration Processing"
    },
    {
      "exception": "Certain invoices may require special memos based on merchant-customer relationship",
      "condition": "Customer-specific requirements",
      "category": "Invoice Processing"
    },
    {
      "exception": "Some contracts may have items to ignore during processing",
      "condition": "Merchant-specific processing instructions",
      "category": "Contract Processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Mithril Implementation POC and CX POC",
      "type": "Contact Information",
      "requires_customization": true
    },
    {
      "element": "Billing model (PLG vs SLG split)",
      "type": "Business Model",
      "requires_customization": true,
      "note": "Mithril has 10% SLG scaling to 20%, with 100-150 PLG customers"
    },
    {
      "element": "Negotiated rates, discounts, and credits structure",
      "type": "Pricing Model",
      "requires_customization": true
    },
    {
      "element": "Integration with existing systems (replacing Stripe)",
      "type": "Technical Integration",
      "requires_customization": true,
      "note": "Mithril redirecting homegrown script from Stripe to Tabs"
    },
    {
      "element": "Post-processing notification requirements",
      "type": "Communication Protocol",
      "requires_customization": true,
      "example": "Customer Success [Azmat Aziz] notified in Messari internal merchant channel when contracts processed"
    },
    {
      "element": "Customer creation process uniqueness",
      "type": "Operational Process",
      "requires_customization": true
    },
    {
      "element": "Contract structure and breakdown",
      "type": "Contract Management",
      "requires_customization": true
    },
    {
      "element": "Events billing requirements",
      "type": "Billing Process",
      "requires_customization": true
    },
    {
      "element": "Integration item labeling conventions",
      "type": "Data Classification",
      "requires_customization": true
    }
  ],
  "confidence_score": 0.85
}
```

---

