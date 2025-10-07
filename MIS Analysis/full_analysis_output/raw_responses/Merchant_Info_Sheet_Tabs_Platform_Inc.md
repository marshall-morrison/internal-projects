# Raw LLM Analysis: Merchant Info Sheet - Tabs Platform Inc

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:16:26

---

## Chunk 1: Merchant Info Sheet - Tabs Platform Inc_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:16:26

### Original Content
```
Merchant Scoping start date: 3 20 24 Implementation Completed Date (Go live date): Feb 1, 2024 MSA Signature Date: Jan 1, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Ali Hussain (CEO) Company summary Tabs is a B2B SaaS coming that focused on Accounts Receivable Automation and is building the first CRM purpose built for Finance teams AM Notes N A Billing model Frequently have ToS MSA Mix of annual   quarterly   monthly   Ramp-up schedules About 10-20 bills per month Contract Proces...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract lifecycle management and key dates",
    "Customer record creation and management",
    "Billing model and frequency",
    "Contract end date handling and renewal policies",
    "Revenue and implementation processing workflows"
  ],
  "rules": [
    {
      "rule": "If customer does not exist in dropdown, create one in Garage and use that customer to create the record on QBO",
      "category": "Customer Management"
    },
    {
      "rule": "Launch Date defaults to signature date if no kick off call or launch date is defined in contract",
      "category": "Implementation Dates"
    },
    {
      "rule": "Default to 1 month implementation date if no implementation date or time period is listed",
      "category": "Implementation Dates"
    },
    {
      "rule": "For contracts with end date in the past, set end date to 6 months from now pending merchant notification",
      "category": "Contract End Dates"
    },
    {
      "rule": "For contracts without an end date, set end date to 6 months from today pending merchant notification",
      "category": "Contract End Dates"
    },
    {
      "rule": "For contracts with future end date within next few months, use the contract end date unless notified otherwise",
      "category": "Contract End Dates"
    },
    {
      "rule": "Billing term for an additional year is automatically included for renewals of Tabs Platform customers",
      "category": "Renewals"
    },
    {
      "rule": "Write Billing Term Description as 'renewal' for renewal contracts",
      "category": "Renewals"
    },
    {
      "rule": "Send a slack bot notification for revenue processing",
      "category": "Revenue Processing"
    }
  ],
  "exceptions": [
    {
      "exception": "Contracts with end dates in the past require special handling (6 months extension)",
      "condition": "End date is in the past"
    },
    {
      "exception": "Contracts without end dates require default 6-month extension",
      "condition": "No end date specified"
    },
    {
      "exception": "Future end dates within next few months follow contract unless merchant provides update",
      "condition": "End date is in near future"
    },
    {
      "exception": "Automatic renewal billing term inclusion applies specifically to Tabs Platform customers",
      "condition": "Customer is Tabs Platform customer"
    }
  ],
  "merchant_specific": [
    {
      "element": "Merchant name: Tabs",
      "type": "Identity"
    },
    {
      "element": "Business model: B2B SaaS focused on Accounts Receivable Automation",
      "type": "Business Context"
    },
    {
      "element": "Billing frequency: Mix of annual, quarterly, monthly with ramp-up schedules",
      "type": "Billing Model"
    },
    {
      "element": "Volume: About 10-20 bills per month",
      "type": "Transaction Volume"
    },
    {
      "element": "Key contact: Ali Hussain (CEO)",
      "type": "Stakeholder"
    },
    {
      "element": "GTM POC, ERP, and Tax Integration fields (values not specified)",
      "type": "System Integration"
    },
    {
      "element": "Contract types: ToS MSA mix",
      "type": "Contract Structure"
    },
    {
      "element": "Customer system: Garage for customer creation, QBO for records",
      "type": "Technology Stack"
    },
    {
      "element": "Tabs Platform customers have specific renewal terms",
      "type": "Product-Specific Policy"
    }
  ],
  "confidence_score": 0.82
}
```

---

