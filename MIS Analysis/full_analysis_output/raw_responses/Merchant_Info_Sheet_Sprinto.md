# Raw LLM Analysis: Merchant Info Sheet - Sprinto

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:59:16

---

## Chunk 1: Merchant Info Sheet - Sprinto_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:59:16

### Original Content
```
That section will guide you on how many rev schedules you should set up and the dates to put for Start Dates This should be your source of truth See screenshot below of Payment Schedule This will tell you the dates, net terms, and how many revenue schedules you need to create Create a revenue schedule for every line listed in the payment schedule Service Start Date: See screenshot above as an example Total Months of Service: Listed with Service Term Item Name: Copy and Paste item name listed, ex...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Configuration",
    "Payment Schedule Processing and Mapping",
    "Default Values and Fallback Rules",
    "Contract Processing Workflow and Data Extraction",
    "Post-Processing Communication and Notifications"
  ],
  "rules": [
    {
      "rule": "Payment Schedule section is the source of truth for revenue schedule setup",
      "category": "data_hierarchy"
    },
    {
      "rule": "Create one revenue schedule for every line listed in the payment schedule",
      "category": "schedule_creation"
    },
    {
      "rule": "Item Name must be copied and pasted from the contract exactly as listed",
      "category": "data_entry"
    },
    {
      "rule": "Billing Type should be set to 'Flat'",
      "category": "billing_configuration"
    },
    {
      "rule": "Total Price must be found in contract Payment Schedule section",
      "category": "pricing"
    },
    {
      "rule": "Quantity defaults to 1",
      "category": "default_values"
    },
    {
      "rule": "Start Date must use the date listed in Payment Schedule for corresponding line item",
      "category": "date_mapping"
    },
    {
      "rule": "Frequency should be set to 'None'",
      "category": "billing_configuration"
    },
    {
      "rule": "Net Terms should refer to Payment Schedule; if none listed, default to 15",
      "category": "payment_terms"
    },
    {
      "rule": "Default Service Term is 1 Year when not specified",
      "category": "default_values"
    },
    {
      "rule": "Default Net Payment Terms is 15 days when not specified",
      "category": "default_values"
    },
    {
      "rule": "Default Billing Frequency is Monthly when not specified",
      "category": "default_values"
    },
    {
      "rule": "Every tax line item becomes a BT (Billing Type) by default if not specified",
      "category": "tax_handling"
    },
    {
      "rule": "All renewals on the contract must be processed and denoted",
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
      "condition": "merchant_specific_request"
    },
    {
      "exception": "Pinata integration items can have different labels if otherwise noted by Merchant",
      "condition": "merchant_override"
    },
    {
      "exception": "Net Terms can vary from default 15 if specified in Payment Schedule",
      "condition": "payment_schedule_specification"
    },
    {
      "exception": "Service Term, Net Payment Terms, and Billing Frequency defaults can be overridden if specified in contract",
      "condition": "contract_specification"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating preferences",
      "description": "Some merchants may request always back-dating invoice dates to final day of month",
      "customizable": true
    },
    {
      "element": "Integration item labeling",
      "description": "Different merchants (Statsig, Pinata) have specific labeling requirements for integration items",
      "customizable": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Ops Team may need to notify specific people based on merchant and processing phase (Implementation or Active)",
      "customizable": true
    },
    {
      "element": "Events billing processing",
      "description": "Events processing requirements are merchant-specific and filled by Implementation Success",
      "customizable": true
    },
    {
      "element": "Contract-specific processing variations",
      "description": "Merchants may have specific processing requests that differ by individual contract",
      "customizable": true
    },
    {
      "element": "Item names and service descriptions",
      "description": "Item names like '2023 Starter' are merchant and contract-specific",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Sprinto_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:59:17

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
      "rule": "Service start dates must be in increments of one year for renewals",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Months of service should be set to 12 for yearly service contracts",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Always scroll to the bottom of the contract to find Payment Schedule",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Integration Item mapping: 'Startup Plan US' if Starter Plan, otherwise search for closest match",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Billing type should be set to 'Flat' for fixed SaaS pricing",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Start dates for multi-year contracts: Year 1 as listed, Year 2 add one year, Year 3 add another year",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Total price must be extracted separately for year 1, year 2, and year 3",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Quantity field should contain number of users",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Net terms and frequency must be extracted from contract as listed",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Item name should be listed exactly as shown in contract",
      "category": "contract_processing",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "India taxes are manually configured (9+9 or 18% based on Indian State) due to no Avalara integration",
      "condition": "For India entity only",
      "impact": "Manual tax calculation required"
    },
    {
      "exception": "Different ERPs for different entities: QBO for US, Zoho for India",
      "condition": "Multi-entity setup",
      "impact": "Separate system configurations required"
    },
    {
      "exception": "Multi-currency support required (USD and INR)",
      "condition": "Operations in US and India",
      "impact": "Currency-specific processing needed"
    },
    {
      "exception": "Usage-based billing anticipated in future but not currently implemented",
      "condition": "Future state consideration",
      "impact": "System should support future usage-based billing"
    },
    {
      "exception": "Cacheflow is sunsetting and being replaced",
      "condition": "System transition in progress",
      "impact": "Migration from legacy system required"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key Personnel",
      "details": "Director of Finance (Naga Subramanya), Customer Service (Himani), AR POC (Kashyap Shettigar), Billing POC (Naga Subramanya)",
      "customization_needed": true
    },
    {
      "element": "ERP Systems",
      "details": "Zoho for India, QBO (QuickBooks Online) for US",
      "customization_needed": true
    },
    {
      "element": "Tax Integration",
      "details": "Avalara planned for US, Manual GST configuration for India with 9+9 or 18% rates",
      "customization_needed": true
    },
    {
      "element": "System Integrations",
      "details": "HubSpot, Cacheflow (sunsetting), Unium, QBO, Zoho",
      "customization_needed": true
    },
    {
      "element": "Product Plans",
      "details": "Startup Plan US, Starter Plan - requires mapping to integration items",
      "customization_needed": true
    },
    {
      "element": "Business Goals",
      "details": "Replace manual workflows, achieve automated cash forecasting and AR reporting, reduce human errors",
      "customization_needed": true
    },
    {
      "element": "Billing Model",
      "details": "Fixed SaaS pricing with annual and multi-period terms, multi-currency (USD/INR)",
      "customization_needed": true
    },
    {
      "element": "Timeline Dates",
      "details": "Demo: Oct 25, 2024; MSA Signature: Dec 16, 2024; Kick Off: Dec 19, 2024; Go Live: Jan 31, 2025",
      "customization_needed": true
    },
    {
      "element": "Company Profile",
      "details": "Sprinto - fullstack security and compliance automation platform (SOC2, ISO 27001, GDPR, HIPAA)",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 3: Merchant Info Sheet - Sprinto_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:59:33

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Please add the billing and shipping information based on Ship To on the contract Feature Requests (AE Implementation Success to fill) Full Requirements doc FR 1 What is it Why it's important Urgency Rewatch Calls (AE Implementation Success to fill) Oct 10th Intro Call Oct 25th Custom ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Customer Success Notification and Communication Protocols",
    "Billing and Payment Structure Management",
    "System Integration and Implementation Requirements",
    "Revenue Recognition and Financial Reporting",
    "Stakeholder Management and Relationship Building"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
      "category": "notification_protocol",
      "explicit": true
    },
    {
      "rule": "Billing and shipping information must be added based on Ship To field on the contract",
      "category": "data_entry",
      "explicit": true
    },
    {
      "rule": "Implementation Success is responsible for filling Customer Information section",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "AE Implementation Success must fill Feature Requests and Rewatch Calls sections",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "Ops International Team should ignore Notes Sections",
      "category": "role_responsibility",
      "explicit": true
    },
    {
      "rule": "Standard billing model: 70% annual upfront payments with remainder split into half-yearly or quarterly terms",
      "category": "billing",
      "explicit": true
    },
    {
      "rule": "Indian entity invoices Indian customers in INR currency",
      "category": "billing_geography",
      "explicit": true
    },
    {
      "rule": "US entity invoices global customers in USD currency",
      "category": "billing_geography",
      "explicit": true
    },
    {
      "rule": "Bespoke payment terms must be added directly into order forms",
      "category": "billing_customization",
      "explicit": true
    },
    {
      "rule": "Feature requests must include: description (What is it), justification (Why it's important), and Urgency level",
      "category": "feature_request_format",
      "explicit": true
    },
    {
      "rule": "Full Requirements documentation must be provided for feature requests",
      "category": "documentation",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Bespoke payment terms can override standard 70% upfront billing model when added to order forms",
      "condition": "Custom terms negotiated with merchant"
    },
    {
      "exception": "Indian customers are invoiced in INR rather than standard USD",
      "condition": "Customer location is India"
    },
    {
      "exception": "Implementation timeline may need extension beyond standard due to merchant's previous 6-month implementation experience",
      "condition": "Merchant has cautious temperament from previous implementation challenges"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key POC/Decision Maker name",
      "example": "Naga Subramanya",
      "customization_required": true
    },
    {
      "element": "Merchant temperament assessment",
      "example": "engaged but cautious due to critical system reliance",
      "customization_required": true
    },
    {
      "element": "Previous implementation history",
      "example": "Unim implementation took 6 months",
      "customization_required": true
    },
    {
      "element": "Priority features for specific POC",
      "example": "Full automation of post-close workflows, AI-driven contract ingestion, Cash Forecasting",
      "customization_required": true
    },
    {
      "element": "Current manual processes and pain points",
      "example": "Manual spreadsheets for AR aging, cash forecasting, custom revenue recognition",
      "customization_required": true
    },
    {
      "element": "Integration requirements",
      "example": "HubSpot, Tabs, ERP, Avalara, Zoho",
      "customization_required": true
    },
    {
      "element": "Billing model specifics",
      "example": "70% annual upfront with half-yearly or quarterly remainder",
      "customization_required": true
    },
    {
      "element": "Entity structure for invoicing",
      "example": "Indian entity for INR, US entity for USD",
      "customization_required": true
    },
    {
      "element": "Call history and timeline",
      "example": "Series of calls from Oct 10th to Dec 10th",
      "customization_required": true
    },
    {
      "element": "Custom reporting metrics",
      "example": "ARR metrics, cross-sell price increase reporting",
      "customization_required": true
    }
  ],
  "confidence_score": 0.85
}
```

---

