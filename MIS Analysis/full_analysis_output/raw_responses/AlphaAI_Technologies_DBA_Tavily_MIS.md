# Raw LLM Analysis: AlphaAI Technologies DBA Tavily MIS

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:43:16

---

## Chunk 1: AlphaAI Technologies DBA Tavily MIS_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:43:16

### Original Content
```
Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Entire Section: Implementation Success to fill Post-Go Live) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE to fill for all requests prior to Imp handoff, Imp to fill prior to go-live...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant onboarding and handoff process across teams (AE → Implementation → Customer Success)",
    "Billing structure and payment processing workflow",
    "Product integration requirements and feature priorities",
    "Merchant communication and stakeholder management",
    "Documentation and information tracking across merchant lifecycle phases"
  ],
  "rules": [
    "Customer Success (specifically Azmat Aziz) must be notified in Messari internal merchant channel when contracts are processed during Active merchant phase",
    "AE is responsible for filling Feature Requests section prior to Implementation handoff",
    "Implementation team fills Feature Requests section prior to go-live",
    "Customer Success fills Feature Requests section post-go-live",
    "AE fills Merchant Calls section for all videos prior to Implementation involvement",
    "Implementation fills Merchant Calls section prior to go-live",
    "Customer Success fills Merchant Calls section post-go-live",
    "Implementation team serves as completion DRI (Directly Responsible Individual) on handoff for Notes Sections",
    "Customer Information section (Implementation Success to fill Post-Go Live) must include special memos for invoices and invoice changes due to merchant-customer relationships"
  ],
  "exceptions": [
    "PLG (Product-Led Growth) motion exists but merchant (Shai) does not want it integrated into Tabs currently, keeping it separate in Stripe",
    "Merchant is open to PLG integration in future but not today",
    "Pay-as-you-go overage handling will be managed in Stripe, not Tabs, with potential future migration to Tabs",
    "Contract credits and overages are not to be processed in Tabs at this time",
    "Merchant works late hours despite 7-hour time difference (Israel to New York), accommodating scheduling flexibility"
  ],
  "merchant_specific": [
    "Merchant contact: Shai (located in Israel, 7-hour time difference from New York)",
    "Merchant temperament: relatively easy going, flexible with workflows, not rigidly set in processes",
    "Billing model: Flat SaaS platform fee + contract-based credits + optional pay-as-you-go overages",
    "Additional product offering: 12-month security layer outlined in contract",
    "Sales motion: SLG (Sales-Led Growth) is new, launched within last couple months",
    "Key features prioritized by merchant POC: Invoice generation, Revenue schedule automation, Avalara integration, Stripe integration, QB Integration, Hubspot, Plaid connection (Chase)",
    "Merchant name: Messari",
    "Current payment processor: Stripe",
    "Accounting system: QuickBooks (QB)",
    "CRM: Hubspot",
    "Banking: Chase (via Plaid connection)"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: AlphaAI Technologies DBA Tavily MIS_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:43:21

### Original Content
```
Merchant Name: AlphaAI Technologies DBA Tavily Implementation POC: (IM to fill) CX POC: [IMP to Add] Billing model (Entire Section: Implementation to fill section) Are there unique things about the customer creation process for this merchant Information on how merchant bills How contract is broken up One off things to know about the merchant Contract Processing Steps (Entire Section: Implementation Success to fill Post-Go Live) Steps to process Customer Creation Please make sure you are adding t...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and BT (Billing Transaction) Item Creation",
    "Customer Profile Setup and Billing Contact Management",
    "Product Classification and Pricing Rules",
    "Billing Frequency, Timing, and Payment Terms Configuration",
    "Items to Exclude from Processing (Overages, Pay-Go, Future Options)"
  ],
  "rules": [
    "Add billing contact and their email address to customer profile after creation on the 'view customer' page",
    "Primary contact email can be cc'd as billing contact",
    "Each distinct product or fee in contract summary must be processed as a separate BT",
    "Label any product titled 'Service Fee' (not in reference to sections titled 'service fees') as 'Enterprise Platform Fee'",
    "API Credits - Bulk Purchases should be processed as flat fee BT if committed to",
    "Do not create usage products for overage fees tied to API credits",
    "Do not process API Credits-PayGo products",
    "Use 'Order Form Effective Date' as the Service Start Date",
    "Default quantity to 1 if no quantity is listed or applicable",
    "Enterprise Platform Fee quantity will almost always be 1",
    "Use total cost for listed item as shown in agreement; if first-year discount exists, use discounted value",
    "Use stated term for agreement or item (typically under 'order form term'); default to 12 months if not stated",
    "Billing Start Date defaults to Service Start Date unless different invoicing schedule is clearly stated",
    "Enterprise Platform Fee will almost always be 'Year' (frequency) and '1' (period)",
    "Default to period/frequency '1, Year' if not stated",
    "Use contract-stated net terms (usually under 'Payment Terms'); default to 30 if not provided",
    "Billing Timing: Bill first of period",
    "Do not create usage BTs for overage pricing unless explicitly priced as committed purchase",
    "Ignore upgrade rights or future optional items unless explicitly priced in current contract term",
    "Ignore API credit expiration terms for BT creation purposes",
    "If contract invoice has PO number, add it as additional field to each invoice",
    "Default Service Term if none listed: 1 Year",
    "Default Net Payment Terms if none listed: 0",
    "Default Billing Frequency if none listed: Monthly",
    "Every tax line item becomes a BT if none listed"
  ],
  "exceptions": [
    "API Credits - Bulk Purchases processed as flat fee only if committed to (not as usage-based)",
    "Do not process overage or 'pay-go' fees unless explicitly priced as committed purchase in contract",
    "Billing frequency may differ by product within same contract (e.g., monthly for API-PayGo vs annual for Enterprise Platform Fee)",
    "First-year discounts or promotions should use discounted value instead of standard pricing",
    "Item Description is optional and only used if helpful to clarify or distinguish items",
    "Different invoicing schedule may override default Billing Start Date = Service Start Date rule",
    "PO numbers are conditionally added only if listed in contract invoice",
    "Merchant-specific processing requests may differ by contract"
  ],
  "merchant_specific": [
    "Merchant Name: AlphaAI Technologies DBA Tavily",
    "Implementation POC and CX POC fields to be filled by specific teams",
    "Billing model section to be filled by Implementation team",
    "Contract Processing Steps section to be filled by Implementation Success team post-go-live",
    "Events Processing section to be filled by Implementation Success team if necessary",
    "Integration Items Processing section to be filled by Implementation Success team (includes mapping instructions)",
    "Post Processing Communications section defines notification requirements per merchant",
    "Example contracts referenced with specific IDs (ba36ac09-31bb-47dc-a4fa-db62b11c1083, etc.)",
    "Merchant-specific terminology: 'BT' (Billing Transaction), 'Enterprise Platform Fee', 'API Credits'",
    "Merchant may have specific requests that differ by contract (e.g., back-dating invoice dates)",
    "Integration items may require specific labeling per merchant (examples: Statsig as 'Sales', Pinata as 'Software Subscription Bundle')",
    "Notification requirements for Ops Team vary by merchant and phase (Implementation vs Active)"
  ],
  "confidence_score": 0.92
}
```

---

