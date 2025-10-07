# Raw LLM Analysis: Merchant Info Sheet - Incendium

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:17:23

---

## Chunk 1: Merchant Info Sheet - Incendium_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:17:23

### Original Content
```
Incendium Scoping start date: n a Implementation Completed Date (Go live date): n a MSA Signature Date: Feb 1, 2024 GTM POC: ERP: Freshbooks (unsupported) Tax Integration: Key people at Merchant Nate Houghton  nate incendiumstrategies com  CEO and primary PoC for billing Company summary Provides outbound email automation services to go-to-market teams, primarily at startups AM Notes They re a mess, many changes on who is primary PoC and what billing model they want to pursue Friend of Ali s Tabs...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing configuration",
    "Merchant relationship and account management",
    "System integration challenges and limitations",
    "Internal process documentation and operational notes",
    "Default contract processing parameters"
  ],
  "rules": [
    {
      "rule": "Default payment terms to net 30",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Default service term to 12 months",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Default billing frequency to monthly",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Use customer name only if that is the only information available",
      "category": "contract_processing",
      "explicit": true
    },
    {
      "rule": "Mark payments as paid in both Freshbooks and tabs system",
      "category": "billing_operations",
      "explicit": true
    },
    {
      "rule": "Recurring straight-line retainer charged in perpetuity until canceled or adjusted",
      "category": "billing_model",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Freshbooks ERP is unsupported - no integration available",
      "impact": "Manual dual-entry required for payment tracking",
      "note": "This is noted as a point of contention"
    },
    {
      "exception": "Multiple changes to primary point of contact and billing model",
      "impact": "Account requires careful attention and verification",
      "note": "Account manager notes this as 'a mess'"
    },
    {
      "exception": "Mutual business relationship exists (friend of Ali, mutual service utilization)",
      "impact": "May require special handling or consideration",
      "note": "They use tabs service, tabs uses their service"
    },
    {
      "exception": "Events processing not currently applicable but merchant is interested in exploring",
      "impact": "Potential future feature requirement",
      "note": "May need to revisit configuration later"
    }
  ],
  "merchant_specific": [
    {
      "element": "Primary contact: Nate Houghton (CEO)",
      "type": "contact_information"
    },
    {
      "element": "ERP system: Freshbooks (unsupported)",
      "type": "technical_integration"
    },
    {
      "element": "Business type: Outbound email automation services for go-to-market teams at startups",
      "type": "business_context"
    },
    {
      "element": "Billing model: Recurring straight-line retainer",
      "type": "billing_configuration"
    },
    {
      "element": "Relationship context: Friend of Ali, mutual service utilization",
      "type": "relationship_management"
    },
    {
      "element": "MSA signature date: Feb 1, 2024",
      "type": "contract_milestone"
    },
    {
      "element": "Conversation scheduled for next week regarding dual-entry fix",
      "type": "action_item"
    },
    {
      "element": "Tax integration: None specified",
      "type": "technical_integration"
    }
  ],
  "confidence_score": 0.85
}
```

---

