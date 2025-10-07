# Raw LLM Analysis: Merchant Info Sheet - Honor Education(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:20:50

---

## Chunk 1: Merchant Info Sheet - Honor Education(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:20:50

### Original Content
```
Honor Education Scoping start date: n a Implementation Completed Date (Go live date): n a MSA Signature Date: Feb 29, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Fractional Head of Finance: Yoav Cohen  yoav honor education  Ex-colleague at Latch CEO: Joel Podolny  joel honor education  Signatory Company summary Provides education software to schools and universities AM Notes Yoav, the fractional accountant, is a former colleague of Ali, Deepak, and Skoro at Latch Yoav needs to be ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant onboarding and key stakeholder information",
    "Billing model and pricing structure",
    "Contract processing and configuration requirements",
    "Internal relationship management and training needs",
    "Integration and system setup specifications"
  ],
  "rules": [
    {
      "rule": "As of 12/12/2024, any new client should be marked 'bill to merchant'",
      "category": "contract_processing",
      "effective_date": "2024-12-12"
    },
    {
      "rule": "Integration Item should always be 'Sales'",
      "category": "integration_setup",
      "mandatory": true
    },
    {
      "rule": "Base price is charged annually",
      "category": "billing",
      "frequency": "annual"
    },
    {
      "rule": "Overage fees are assessed quarterly",
      "category": "billing",
      "frequency": "quarterly"
    },
    {
      "rule": "Additional learner fees are assessed quarterly, starting on June 1",
      "category": "billing",
      "frequency": "quarterly",
      "start_condition": "June 1"
    },
    {
      "rule": "Standard flat-line billing model is used",
      "category": "billing_model",
      "note": "exploring more nuanced channel distribution model for future"
    }
  ],
  "exceptions": [
    {
      "exception": "Default contract language can be ambiguous and requires careful review",
      "impact": "May require clarification during contract processing"
    },
    {
      "exception": "Events processing not yet applicable but may be implemented later in 2024",
      "status": "future_consideration"
    },
    {
      "exception": "Merchant is exploring a more nuanced channel distribution model but has not yet implemented",
      "status": "under_consideration"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key stakeholders",
      "details": "Fractional Head of Finance: Yoav Cohen; CEO: Joel Podolny",
      "relationship_note": "Yoav is former colleague of internal team members (Ali, Deepak, Skoro) at Latch"
    },
    {
      "element": "Training needs",
      "details": "Yoav needs better training on product usage; currently prefers emailing instead of self-service"
    },
    {
      "element": "Business model",
      "details": "Provides education software to schools and universities"
    },
    {
      "element": "Pricing example",
      "details": "$15,000 charged annually with additional learner fees assessed quarterly starting June 1"
    },
    {
      "element": "MSA signature date",
      "details": "February 29, 2024"
    },
    {
      "element": "ERP and Tax Integration",
      "details": "Not specified (n/a)"
    }
  ],
  "confidence_score": 0.85
}
```

---

