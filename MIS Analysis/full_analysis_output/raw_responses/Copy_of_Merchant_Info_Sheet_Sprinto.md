# Raw LLM Analysis: Copy of Merchant Info Sheet - Sprinto

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:57:15

---

## Chunk 1: Copy of Merchant Info Sheet - Sprinto_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:57:15

### Original Content
```
That section will guide you on how many rev schedules you should set up and the dates to put for Start Dates This should be your source of truth See screenshot below of Payment Schedule This will tell you the dates, net terms, and how many revenue schedules you need to create Create a revenue schedule for every line listed in the payment schedule Service Start Date: See screenshot above as an example Total Months of Service: Listed with Service Term Item Name: Copy and Paste item name listed, ex...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Configuration",
    "Payment Schedule Processing and Data Extraction",
    "Default Values and Fallback Rules",
    "Integration and Item Labeling Standards",
    "Post-Processing Communication and Notifications"
  ],
  "rules": [
    {
      "rule": "Payment Schedule section in contract is the source of truth for revenue schedule setup",
      "category": "data_hierarchy"
    },
    {
      "rule": "Create one revenue schedule for every line listed in the payment schedule",
      "category": "revenue_schedule_creation"
    },
    {
      "rule": "Item Name must be copied and pasted from the contract exactly as listed",
      "category": "data_entry"
    },
    {
      "rule": "Billing Type should be set to 'Flat'",
      "category": "revenue_schedule_configuration"
    },
    {
      "rule": "Total Price is found in the Payment Schedule section of the contract",
      "category": "pricing"
    },
    {
      "rule": "Quantity defaults to 1",
      "category": "revenue_schedule_configuration"
    },
    {
      "rule": "Start Date must use the date listed in Payment Schedule for the corresponding line item",
      "category": "revenue_schedule_configuration"
    },
    {
      "rule": "Frequency should be set to 'None'",
      "category": "revenue_schedule_configuration"
    },
    {
      "rule": "Net Terms should refer to Payment Schedule information, default to 15 if not listed",
      "category": "payment_terms"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "defaults"
    },
    {
      "rule": "Default Net Payment Terms is 15 days if none listed",
      "category": "defaults"
    },
    {
      "rule": "Default Billing Frequency is Monthly if none listed",
      "category": "defaults"
    },
    {
      "rule": "Every tax line item becomes a BT (Billing Type) if none listed",
      "category": "tax_handling"
    },
    {
      "rule": "All renewals on the contract must be processed with renewal denoted",
      "category": "renewals"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "integration_labeling"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "integration_labeling"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant may request specific processing variations that differ by contract (e.g., always back-date invoice date to final day of the month)",
      "context": "contract_processing"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "context": "integration_labeling"
    },
    {
      "exception": "Net Terms may vary per contract based on Payment Schedule specifications",
      "context": "payment_terms"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating preferences",
      "description": "Some merchants may request specific invoice date handling (e.g., back-dating to final day of month)",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Specific integration vendors (Statsig, Pinata) have predefined labels but may vary by merchant",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Notification recipients and timing may vary by merchant and implementation phase",
      "customizable": true
    },
    {
      "element": "Events billing processing",
      "description": "Events processing requirements are merchant-specific and filled by Implementation Success",
      "customizable": true
    },
    {
      "element": "Service Term length",
      "description": "While default is 1 year, actual term is contract-specific",
      "customizable": true
    },
    {
      "element": "Net Payment Terms",
      "description": "While default is 15 days, actual terms may be specified in Payment Schedule",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Copy of Merchant Info Sheet - Sprinto_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:57:15

### Original Content
```
l Merchant: Sprinto Demo date: Oct 25, 2024 Scoping start date: Oct 25, 2024 MSA Signature Date: Dec 16, 2024 Onboarding Kick Off Date: Dec 19, 2024 [If Exists] Opt Out Date: Go Live Date: Jan 31, 2025 GTM POC: Implementation POC: (Deepak   Arjun involved during motion) ERP: Zoho for India Tax Integration: Avalara planned for US, Manual GST config for India Key people at Merchant Director of Finance (Main POC): Naga Subramanya Customer service rep who is really involved: Himani Account Receivabl...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Timeline",
    "System Integration and ERP Configuration",
    "Contract Processing and Billing Management",
    "Tax Configuration and Multi-Currency Support",
    "Stakeholder Identification and Communication"
  ],
  "rules": [
    {
      "rule": "Service start dates must be in increments of one year if there is a renewal listed",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Months of Service should be set to 12 for yearly service",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Always scroll to the bottom of the contract to find Payment Schedule",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Integration Item mapping: 'Startup Plan US' if Starter Plan, otherwise search for closest match",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "For multi-year contracts, add one year to start date for year 2, add another year for year 3",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Total Price must be listed separately for year 1, year 2, and year 3",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Quantity field should contain number of users",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "India taxes are calculated manually as either 9+9 or 18 based on Indian State",
      "category": "Tax Configuration",
      "explicit": true
    },
    {
      "rule": "Multi-currency support required for USD and INR",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Separate ERPs must be configured for different entities (QBO for US, Zoho for India)",
      "category": "System Integration",
      "explicit": true
    },
    {
      "rule": "Net Terms and Frequency must be extracted from contract",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Billing type should be set to 'Flat' for fixed SaaS pricing",
      "category": "Contract Processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Usage-based billing is not currently active but is anticipated in the future",
      "condition": "Future state consideration",
      "impact": "May require system reconfiguration"
    },
    {
      "exception": "Cacheflow is sunsetting and being replaced",
      "condition": "System transition period",
      "impact": "Manual checks between Cacheflow and Unium create inefficiencies during transition"
    },
    {
      "exception": "No Avalara integration for India; manual GST configuration required",
      "condition": "India entity only",
      "impact": "Avalara planned for US only, India requires manual tax setup"
    },
    {
      "exception": "Integration Item mapping requires manual search if not 'Starter Plan'",
      "condition": "When plan name doesn't match exactly",
      "impact": "Requires judgment to find closest match"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name and dates",
      "values": ["Sprinto Demo", "Oct 25, 2024", "Dec 16, 2024", "Jan 31, 2025"],
      "customizable": true
    },
    {
      "element": "Key stakeholders and POCs",
      "values": ["Naga Subramanya (Director of Finance)", "Himani (Customer service)", "Kashyap Shettigar (AR POC)", "Deepak & Arjun (Implementation)"],
      "customizable": true
    },
    {
      "element": "ERP systems",
      "values": ["Zoho for India", "QBO for US"],
      "customizable": true
    },
    {
      "element": "Tax integration approach",
      "values": ["Avalara planned for US", "Manual GST config for India"],
      "customizable": true
    },
    {
      "element": "Current tech stack",
      "values": ["HubSpot", "Cacheflow", "Unium", "QBO", "Zoho"],
      "customizable": true
    },
    {
      "element": "Company description",
      "values": ["Fullstack security and compliance automation platform"],
      "customizable": true
    },
    {
      "element": "Primary goals",
      "values": ["Replace manual workflows", "Achieve accurate cash forecasting", "Reduce human errors"],
      "customizable": true
    },
    {
      "element": "Billing model specifics",
      "values": ["Fixed SaaS pricing with annual and multi-period terms", "Multi-currency (USD and INR)"],
      "customizable": true
    },
    {
      "element": "Tax calculation method",
      "values": ["9+9 or 18 based on Indian State"],
      "customizable": true
    },
    {
      "element": "Product plan names",
      "values": ["Startup Plan US", "Starter Plan"],
      "customizable": true
    }
  ],
  "confidence_score": 0.88
}
```

---

## Chunk 3: Copy of Merchant Info Sheet - Sprinto_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:57:31

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Please add the billing and shipping information based on Ship To on the contract Feature Requests (AE Implementation Success to fill) Full Requirements doc FR 1 What is it Why it's important Urgency Rewatch Calls (AE Implementation Success to fill) Oct 10th Intro Call Oct 25th Custom ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding and Implementation Process",
    "Billing and Payment Structure",
    "System Integration and Automation Requirements",
    "Stakeholder Management and Communication",
    "Revenue Recognition and Financial Reporting"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
      "category": "notification",
      "explicit": true
    },
    {
      "rule": "Billing and shipping information must be added based on Ship To field on the contract",
      "category": "data_entry",
      "explicit": true
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information and feature requests",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "AE Implementation Success team is responsible for filling rewatch calls and notes sections",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore notes sections",
      "category": "responsibility",
      "explicit": true
    },
    {
      "rule": "Standard billing model: 70% annual upfront payments, remainder split into half-yearly or quarterly terms",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Indian entity invoices Indian customers in INR",
      "category": "billing_geography",
      "explicit": true
    },
    {
      "rule": "US entity invoices globally in USD",
      "category": "billing_geography",
      "explicit": true
    },
    {
      "rule": "Bespoke terms must be added directly into order forms",
      "category": "contract_management",
      "explicit": true
    },
    {
      "rule": "Feature requests must include: what it is, why it's important, and urgency level",
      "category": "feature_request_format",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Bespoke billing terms can override standard SaaS billing model and must be added to order forms",
      "condition": "when custom terms are negotiated"
    },
    {
      "exception": "Indian customers are invoiced in INR by Indian entity instead of USD",
      "condition": "when customer is located in India"
    },
    {
      "exception": "Previous implementation with Unim took 6 months, creating stakeholder hesitation",
      "condition": "merchant-specific historical context affecting temperament"
    },
    {
      "exception": "Manual spreadsheets currently used for AR aging, cash forecasting, custom revenue recognition, and non-GAAP metrics",
      "condition": "interim solution until full automation is implemented"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Success contact person",
      "example": "Azmat Aziz",
      "customizable": true
    },
    {
      "element": "Internal notification channel",
      "example": "Messari internal merchant channel",
      "customizable": true
    },
    {
      "element": "Key POC/Decision Maker",
      "example": "Naga Subramanya",
      "customizable": true
    },
    {
      "element": "Merchant temperament assessment",
      "example": "engaged but cautious due to critical system reliance",
      "customizable": true
    },
    {
      "element": "Previous implementation history",
      "example": "Unim implementation took 6 months",
      "customizable": true
    },
    {
      "element": "Rewatch calls schedule and dates",
      "example": "Oct 10th Intro Call, Oct 25th Custom Demo, etc.",
      "customizable": true
    },
    {
      "element": "Priority features for key POC",
      "example": "Full automation, AI-driven contract ingestion, Cash Forecasting, Custom AR flexibility",
      "customizable": true
    },
    {
      "element": "Integration requirements",
      "example": "Avalara, HubSpot, Zoho",
      "customizable": true
    },
    {
      "element": "Payment structure percentages",
      "example": "70% upfront, remainder split",
      "customizable": true
    },
    {
      "element": "Currency and invoicing entity",
      "example": "INR for India, USD for global",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

