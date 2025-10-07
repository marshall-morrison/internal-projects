# Raw LLM Analysis: Merchant Info Sheet - Honor Education

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:58:45

---

## Chunk 1: Merchant Info Sheet - Honor Education_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:58:45

### Original Content
```
Honor Education Scoping start date: n a Implementation Completed Date (Go live date): n a MSA Signature Date: Feb 29, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Fractional Head of Finance: Yoav Cohen  yoav honor education  Ex-colleague at Latch CEO: Joel Podolny  joel honor education  Signatory Company summary Provides education software to schools and universities AM Notes Yoav, the fractional accountant, is a former colleague of Ali, Deepak, and Skoro at Latch Yoav needs to be ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and billing configuration",
    "Merchant relationship management and key contacts",
    "Product training and user adoption challenges",
    "Contract processing workflow updates",
    "Pricing model structure (flat-line with overage fees)"
  ],
  "rules": [
    {
      "rule": "As of 12/12/2024, any new client should be marked 'bill to merchant'",
      "category": "contract_processing",
      "effective_date": "2024-12-12"
    },
    {
      "rule": "Integration Item should always be 'Sales'",
      "category": "contract_processing",
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
      "status": "current"
    }
  ],
  "exceptions": [
    {
      "exception": "Default language in contract can be ambiguous",
      "implication": "Requires careful review and clarification during contract processing",
      "category": "contract_language"
    },
    {
      "exception": "Merchant is exploring a more nuanced channel distribution model, but have not yet implemented",
      "status": "future_consideration",
      "category": "billing_model"
    },
    {
      "exception": "Events Processing not yet applicable, but may be later in 2024",
      "status": "potential_future_requirement",
      "category": "processing"
    },
    {
      "exception": "Fractional accountant often emails instead of using the product himself",
      "implication": "Training gap and workflow inefficiency",
      "category": "user_adoption"
    }
  ],
  "merchant_specific": [
    {
      "element": "Key personnel contacts",
      "details": {
        "fractional_head_of_finance": "Yoav Cohen (yoav@honor.education)",
        "ceo": "Joel Podolny (joel@honor.education)",
        "signatory": "Joel Podolny"
      }
    },
    {
      "element": "Relationship context",
      "details": "Yoav is a former colleague of Ali, Deepak, and Skoro at Latch"
    },
    {
      "element": "Company type",
      "details": "Provides education software to schools and universities"
    },
    {
      "element": "MSA Signature Date",
      "details": "Feb 29, 2024"
    },
    {
      "element": "Pricing example",
      "details": "$15,000 charged annually plus additional learner fees assessed quarterly starting June 1"
    },
    {
      "element": "Training needs",
      "details": "Yoav needs better training on using the product"
    },
    {
      "element": "Integration specifications",
      "details": {
        "erp": "n/a",
        "tax_integration": "n/a"
      }
    }
  ],
  "confidence_score": 0.85
}
```

---

