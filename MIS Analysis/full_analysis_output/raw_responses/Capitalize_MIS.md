# Raw LLM Analysis: Capitalize MIS

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 10:05:53

---

## Chunk 1: Capitalize MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:05:53

### Original Content
```
Merchant Demo date: 8 20 24 Scoping start date: 9 5 24 MSA Signature Date: 11 27 24 Onboarding Kick Off Date: TBD [If Exists] Opt Out Date: 5 27 25 Go Live Date: GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Aditi Bhatia - VP Finance   Ops Mike Mumma - Director Strategy   Ops Company summary (AE to fill) Capitalize helps individuals take control of their retirement savings by simplifying the process of rolling over old 401(k) accounts into individual retirement accoun...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Usage-Based Billing and Invoice Automation",
    "Contract Processing and Data Integration",
    "Opt-Out Clause Management and Risk Mitigation",
    "Service Period and Billing Configuration Rules"
  ],
  "rules": [
    "Billing model is usage-based only (no one-time fees)",
    "Usage fees are invoiced in arrears as specified in contract",
    "Default service period matches contract period (service period same as contract)",
    "Billing Start Date must use the designated go-live or implementation date",
    "Service Start Date must match contract effective date",
    "Default term is 12 months (initial term) unless contract specifies otherwise",
    "Monthly Looker reports must be ingested with specific adjustments configured to system settings",
    "Only select relevant items for minimums (specifically: SecFi, Public, Robinhood, Advisor Wealth)",
    "Tier BTs (billing triggers) required for Rollover Fee Schedule",
    "Integration types include: Revenue, Rollover Platform Usage AI",
    "Contracts are rarely received due to very few customers",
    "Adjustments to Looker reports must be documented and listed (referenced as 'Green' items in source document)"
  ],
  "exceptions": [
    "Six-month opt-out clause exists due to limited demo scope (only 2 contracts with no real usage data)",
    "Opt-out can be exercised if system doesn't adequately support merchant's usage needs",
    "Months of Service defaults to 12 unless contract specifies otherwise",
    "Merchant has very few customers, so contract flow differs from typical volume",
    "Custom demo was limited in scope (only 2 contracts, no real usage data), creating implementation validation risk"
  ],
  "merchant_specific": [
    "Merchant name: Capitalize",
    "Business model: Retirement savings rollover platform (401k to IRA)",
    "Key contacts: Aditi Bhatia (VP Finance & Ops), Mike Mumma (Director Strategy & Ops)",
    "Data source: Monthly Looker report with custom adjustments",
    "Specific minimums apply to: SecFi, Public, Robinhood, Advisor Wealth",
    "Event types need confirmation from Charlie for Rollover Fee Schedule",
    "Opt-out date: 5/27/25 (6 months from likely go-live)",
    "MSA Signature Date: 11/27/24",
    "Pain points: Automate usage-based invoice calculations, ingest contracts and manage unique rates/minimums",
    "Low customer volume impacts contract processing workflow"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Capitalize MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:05:57

### Original Content
```
Net Terms: Use contract language if specified; default to 30 days if not Total Price: as listed in contract Usage AI Setup Enable for rollover usage fees Service period   contract term Configure thresholds where tiered pricing applies Ensure  charges overages  is enabled, since fees accrue per transaction without a cap Renewal   Termination Contracts generally renew annually unless terminated with advance notice [Auto generate BTs ] Item Name   Event Type mapping Remove tier names from all contr...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Configuration and Setup",
    "Billing and Payment Terms",
    "Usage-Based Pricing and Overages",
    "Integration and Item Processing Rules",
    "Operational Defaults and Standardization"
  ],
  "rules": [
    {
      "rule": "Net payment terms should use contract language if specified, otherwise default to 30 days",
      "category": "Payment Terms"
    },
    {
      "rule": "Total price must be taken as listed in the contract",
      "category": "Pricing"
    },
    {
      "rule": "Usage AI Setup must be enabled for rollover usage fees",
      "category": "Usage Billing"
    },
    {
      "rule": "Service period should match contract term",
      "category": "Contract Terms"
    },
    {
      "rule": "Thresholds must be configured where tiered pricing applies",
      "category": "Pricing"
    },
    {
      "rule": "Charges for overages must be enabled since fees accrue per transaction without a cap",
      "category": "Usage Billing"
    },
    {
      "rule": "Contracts generally renew annually unless terminated with advance notice",
      "category": "Renewal and Termination"
    },
    {
      "rule": "Auto-generate BTs (Billable Items) with Item Name and Event Type mapping",
      "category": "Billing Configuration"
    },
    {
      "rule": "Remove tier names from all contracts except for Sofi",
      "category": "Contract Processing"
    },
    {
      "rule": "Default service term is 1 year if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Default net payment terms is 0 days if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Default billing frequency is monthly if none listed",
      "category": "Operational Defaults"
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Item) if no other instruction is provided",
      "category": "Tax Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Processing"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted by merchant",
      "category": "Integration Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Sofi contracts retain tier names while all other contracts have tier names removed",
      "condition": "Merchant is Sofi"
    },
    {
      "exception": "Invoice date may be back-dated to final day of the month based on merchant-specific requests",
      "condition": "Merchant has requested specific processing differences"
    },
    {
      "exception": "Pinata integration items may have different labels if specifically noted by merchant",
      "condition": "Merchant provides alternative labeling instructions"
    },
    {
      "exception": "Net terms default to 30 days unless contract specifies otherwise",
      "condition": "Contract contains specific net terms language"
    },
    {
      "exception": "Operational default for net payment terms is 0 days, which differs from the 30-day default mentioned for contract language",
      "condition": "No terms specified in contract"
    }
  ],
  "merchant_specific": [
    {
      "element": "Tier name handling",
      "customization": "Sofi retains tier names, all others have them removed"
    },
    {
      "element": "Invoice date processing",
      "customization": "May require back-dating to final day of month per merchant request"
    },
    {
      "element": "Integration item labeling",
      "customization": "Statsig uses 'Sales' label, Pinata uses 'Software Subscription Bundle' with merchant override option"
    },
    {
      "element": "Post-processing communications",
      "customization": "Notification requirements vary by merchant - who needs to be notified and when"
    },
    {
      "element": "Events processing",
      "customization": "Implementation Success team fills in necessary event billing information per merchant"
    },
    {
      "element": "Contract-specific processing requests",
      "customization": "Merchants may have unique processing requirements that differ by contract"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Capitalize MIS_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:06:09

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urgency Rewatch Calls (AE Implementat...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Stakeholder Communication and Notification Requirements",
    "Customer Relationship Management and Key Contacts",
    "Usage-Based Billing and Event Type Configuration",
    "Feature Requirements and Implementation Priorities",
    "Invoice Processing and Reporting Workflows"
  ],
  "rules": [
    {
      "rule": "Customer Success (Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed",
      "condition": "Merchant Phase: Active",
      "category": "notification"
    },
    {
      "rule": "Implementation Success team is responsible for filling customer information section",
      "category": "responsibility"
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling Feature Requests section",
      "category": "responsibility"
    },
    {
      "rule": "AE and Implementation Success teams are responsible for filling Rewatch Calls section",
      "category": "responsibility"
    },
    {
      "rule": "Ops International Team should ignore Custom Demo Notes sections",
      "category": "responsibility"
    },
    {
      "rule": "Usage ingest requires scheduled report setup from Looker",
      "category": "technical_implementation"
    },
    {
      "rule": "Tiered usage structure with 2-3 different event types, sometimes with minimums",
      "category": "billing_structure"
    }
  ],
  "exceptions": [
    {
      "exception": "Special memos required for certain invoices due to merchant customer relationship",
      "context": "Invoice processing may require custom handling"
    },
    {
      "exception": "Invoice changes may be needed due to merchant customer relationship dynamics",
      "context": "Standard invoice processing may not apply universally"
    },
    {
      "exception": "Merchant went dark for a period and required re-engagement efforts",
      "context": "Non-standard communication pattern requiring special attention"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key POC identification",
      "details": "Aditi identified as major decision maker; Mike historically involved but not in current deal process",
      "customization_type": "stakeholder_mapping"
    },
    {
      "element": "Merchant temperament assessment",
      "details": "Really excited initially, went dark, then re-engaged",
      "customization_type": "relationship_status"
    },
    {
      "element": "Feature priorities",
      "details": "Usage ingest, Invoice calculation and sending, Reporting",
      "customization_type": "feature_requirements"
    },
    {
      "element": "Event type taxonomy",
      "details": "Six distinct event types: Consumer - New IRA, Consumer - Existing IRA, Consumer, RaaS, Rollover, with corresponding item names for referral fees, embedded rollover transaction fees, and rollover fees",
      "customization_type": "billing_configuration"
    },
    {
      "element": "Integration requirements",
      "details": "Looker integration for scheduled reporting",
      "customization_type": "technical_integration"
    },
    {
      "element": "Notification channel",
      "details": "Messari internal merchant channel",
      "customization_type": "communication_channel"
    }
  ],
  "confidence_score": 0.75
}
```

---

