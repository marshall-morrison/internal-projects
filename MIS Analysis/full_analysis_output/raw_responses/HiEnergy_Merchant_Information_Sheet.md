# Raw LLM Analysis: HiEnergy Merchant Information Sheet

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:46:28

---

## Chunk 1: HiEnergy Merchant Information Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:46:28

### Original Content
```
Merchant Scoping start date: Nov 6, 2023 Implementation Completed Date (Go live date): Feb 15, 2024 MSA Signature Date: Mar 25, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant CEO: Dexter Dethmers dexter hienergyagency com Cofounder- AR Lead: Jen Goodwin  jen hienergyagency com  Company summary Hi Energy is an affiliate marketing agency AM Notes Friends of Ali Their contract includes a referral clause: For any client referred by Hi Energy Agency who becomes a Tabs customer, Tabs will ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing date processing rules",
    "Merchant relationship and referral agreements",
    "Invoice creation and payment terms configuration",
    "Merchant-specific billing models and contract structures",
    "Documentation and communication tracking"
  ],
  "rules": [
    {
      "rule": "Date hierarchy for contract processing: Use effective date if listed, if not use service date, if neither use signature date, if none available use date contract was uploaded in garage",
      "source": "4 25 update in Contract Processing Steps",
      "priority": "high"
    },
    {
      "rule": "Default service terms: 6 months",
      "source": "Service Terms section",
      "priority": "medium"
    },
    {
      "rule": "Default payment terms: Net 0",
      "source": "Payment Terms section",
      "priority": "medium"
    },
    {
      "rule": "Month-to-month clause processing: If invoice contains month-to-month clause, create 12 monthly invoices in addition to the regular first invoice",
      "source": "8 20 25 update in Payment Terms",
      "priority": "high"
    },
    {
      "rule": "Referral credit: Apply 10% of closed revenue from referred clients to Hi Energy's software costs",
      "source": "AM Notes section",
      "priority": "medium"
    },
    {
      "rule": "Historical instruction: Back-date invoice date to final day of the month (superseded by 4 25 update)",
      "source": "Contract Processing Steps",
      "priority": "low"
    }
  ],
  "exceptions": [
    {
      "exception": "Hi Energy has a special referral clause in their contract providing 10% revenue credit for client referrals",
      "impact": "Affects billing and revenue calculations for referred customers"
    },
    {
      "exception": "Month-to-month contracts require special handling with 12 additional monthly invoices beyond the initial invoice",
      "impact": "Changes invoice generation process significantly"
    },
    {
      "exception": "Date processing rules have been updated multiple times (4 25 update, 8 20 25 update), indicating evolving requirements",
      "impact": "Need to ensure most recent rules are applied"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing model",
      "description": "Flat SaaS with potential usage component coming soon",
      "customizable": true
    },
    {
      "element": "Key contacts",
      "description": "CEO (Dexter Dethmers) and Cofounder-AR Lead (Jen Goodwin) with specific email addresses",
      "customizable": true
    },
    {
      "element": "Merchant relationship",
      "description": "Friends of Ali - indicates personal/strategic relationship",
      "customizable": true
    },
    {
      "element": "ERP and Tax Integration fields",
      "description": "Empty fields suggesting these need to be configured per merchant",
      "customizable": true
    },
    {
      "element": "Contract language support",
      "description": "Commitment to help strengthen contract language and terms",
      "customizable": true
    },
    {
      "element": "Special memo requirements",
      "description": "Certain invoices may require specific memos based on merchant-customer relationship",
      "customizable": true
    },
    {
      "element": "Events processing",
      "description": "Section exists but not populated, suggesting event-based billing may be merchant-specific",
      "customizable": true
    }
  ],
  "confidence_score": 0.85
}
```

---

