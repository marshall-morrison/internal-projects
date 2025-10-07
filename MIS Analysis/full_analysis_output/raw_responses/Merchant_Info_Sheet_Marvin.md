# Raw LLM Analysis: Merchant Info Sheet - Marvin

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:00:02

---

## Chunk 1: Merchant Info Sheet - Marvin_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:00:02

### Original Content
```
You will make different revenue schedules for each different pricing you see under  Subscription term Please see the different revenue schedules created below Refer to  subscription term  Revenue Schedule  1 (outlined in screenshot above in pink) Item Name: Subscription Fee Item Description: 10 User License (or whichever amount license is associated on the contract, refer to contract for number of licenses) Integration Item: Platform Fee Total Price: Refer to contract, example  12,000 Quantity: ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Revenue Schedule Creation and Configuration",
    "Subscription Term Management and Multi-Year Pricing",
    "Invoice and Receipt Processing Workflows",
    "Integration Items and Tax Line Item Handling",
    "Post-Processing Communication and Stakeholder Notification"
  ],
  "rules": [
    "Create separate revenue schedules for each different pricing under Subscription Term",
    "Item Name must be 'Subscription Fee' for all revenue schedules",
    "Item Description must include the number of user licenses from the contract",
    "Integration Item must be labeled as 'Platform Fee'",
    "Total Price must reference the contract amount",
    "Quantity must match the number of user licenses",
    "Start Date must reference the contract subscription term (Year 1 for first schedule, Year 2 for second schedule, etc.)",
    "Period must be set to 'ONE'",
    "Frequency must be set to '1 year'",
    "Net Terms must reference the contract section 'Fees and Invoice Timing'",
    "For receipts: reference the corresponding invoice and calculate difference between issued date and due date for net payment terms",
    "Every receipt must have a corresponding invoice",
    "Receipt frequency can be set to 'None'",
    "Default Service Term is 1 Year",
    "Default Net Payment Terms is 30 days",
    "Default Billing Frequency is 1 year",
    "If no tax handling specified, every tax line item becomes a BT (Balance Transfer)",
    "All Statsig integration items should be labeled as 'Sales'",
    "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
    "Customer Success (Azmat Aziz) needs to be notified in Messari internal merchant channel when contracts are processed in Active phase"
  ],
  "exceptions": [
    "Integration items may differ by merchant and require specific labeling (e.g., Statsig vs Pinata)",
    "Merchants may request specific processing variations that differ by contract (e.g., back-dating invoice dates to final day of month)",
    "Receipt processing only requires processing the receipt and marking matching invoice as processed without BTs",
    "Special memos may be required for certain invoices due to merchant-customer relationships",
    "Invoice changes may be needed based on merchant-customer relationship specifics"
  ],
  "merchant_specific": [
    "Number of user licenses varies by contract and must be extracted from each contract",
    "Total pricing amounts vary by contract and year",
    "Start dates for different years must be extracted from contract subscription terms",
    "Net payment terms location in contract ('Fees and Invoice Timing' section)",
    "Integration item labeling rules (Statsig = 'Sales', Pinata = 'Software Subscription Bundle')",
    "Notification recipients and channels (e.g., Azmat Aziz via Messari internal channel)",
    "Merchant-specific processing requests that may differ by contract",
    "Special customer information including memo requirements and invoice modifications",
    "SFDC feature requests including marketing clause push and subscription data synchronization",
    "Stripe payment flow integration"
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Merchant Info Sheet - Marvin_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:00:08

### Original Content
```
Fx xMerchant Demo date: Jul 19, 2024 Scoping start date: Oct 16, 2024 MSA Signature Date: Nov 7, 2024 Onboarding Kick Off Date: Nov 21, 2024 [If Exists] Opt Out Date: May 1 2025 Go Live Date: Jan 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: - but are doing a nexus study and may want advice on Tax software Key people at Merchant Tim McMinn - our main POC and buyer, more on the sales ops side but in charge of process efficiency and making this all run smoothly Jon - Fractional Burkla...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Revenue Schedule Creation and Contract Processing",
    "Billing Model and Customer Characteristics",
    "Stakeholder Management and Communication",
    "Contract Structure and Component Breakdown"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "description": "When creating a new customer, include the billing email as the main email address",
      "category": "customer_creation"
    },
    {
      "rule_id": "R2",
      "description": "Check contract-ingest for important context about price, service, and term in the email body if not found in the contract",
      "category": "contract_processing"
    },
    {
      "rule_id": "R3",
      "description": "Default net terms are Net30 unless otherwise stated in the contract",
      "category": "payment_terms"
    },
    {
      "rule_id": "R4",
      "description": "Service Start Date should be set to the latest signature date found in contract",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R5",
      "description": "Total Months of Service should be listed under 'term' in the contract",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R6",
      "description": "For multi-component contracts, create separate revenue schedules for each component (Services, Platform Fee, Discounts)",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R7",
      "description": "Revenue Schedule 1: Item Name='Services', Item Description='License Subscription', Integration Item='Platform Fee', use total price from contract",
      "category": "revenue_schedule_services"
    },
    {
      "rule_id": "R8",
      "description": "Revenue Schedule 2: Item Name='Services', Item Description='Other Fees: Platform Fee', Integration Item='Platform Fee', use platform fee amount",
      "category": "revenue_schedule_platform"
    },
    {
      "rule_id": "R9",
      "description": "Revenue Schedule 3: Item Name='Discount', Item Description=blank, Integration Item='Discount', add discount amount from contract",
      "category": "revenue_schedule_discount"
    },
    {
      "rule_id": "R10",
      "description": "All revenue schedules should have Periods=1 and Frequency='1 year' for annual contracts",
      "category": "revenue_schedule"
    },
    {
      "rule_id": "R11",
      "description": "Start Date for all revenue schedules should be the same as service start date",
      "category": "revenue_schedule"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Opt-out clause exists at 6 month mark (May 1, 2025) - merchant can exit if conditions not met",
      "condition": "Time-based opt-out window"
    },
    {
      "exception_id": "E2",
      "description": "While mostly fixed pricing with annual billing, merchant has a handful of monthly/quarterly customers",
      "condition": "Non-standard billing frequency for subset of customers"
    },
    {
      "exception_id": "E3",
      "description": "Merchant may launch PLG (Product-Led Growth) motion in the future, which could change billing model",
      "condition": "Future business model change"
    },
    {
      "exception_id": "E4",
      "description": "AP Portal support was specifically promised and included in contract",
      "condition": "Special contractual commitment"
    },
    {
      "exception_id": "E5",
      "description": "Different contract formats require different processing steps (multiple screenshots referenced)",
      "condition": "Contract format variation"
    },
    {
      "exception_id": "E6",
      "description": "Net terms may differ from Net30 if otherwise stated in contract",
      "condition": "Contract-specific payment terms override"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company: heyMarvin - qualitative data analysis platform",
      "customization_type": "merchant_identity"
    },
    {
      "element": "Key stakeholders: Tim McMinn (POC/buyer), Jon (Fractional CFO), Noah (Fractional accountant), Prayag (CEO)",
      "customization_type": "stakeholder_mapping"
    },
    {
      "element": "Pain points: high DSO, manual work, delays in invoicing, renewals with expansions/upgrades not tracked well",
      "customization_type": "business_challenges"
    },
    {
      "element": "Customer base: ~200 customers, closing 1-2 deals per week",
      "customization_type": "business_metrics"
    },
    {
      "element": "Timeline: Demo (Jul 19, 2024), Scoping (Oct 16, 2024), MSA (Nov 7, 2024), Kick Off (Nov 21, 2024), Go Live (Jan 1, 2025), Opt Out (May 1, 2025)",
      "customization_type": "project_timeline"
    },
    {
      "element": "Tax integration: Considering nexus study and may want tax software advice",
      "customization_type": "integration_requirements"
    },
    {
      "element": "Billing model: Mostly fixed pricing with annual billing, some monthly/quarterly",
      "customization_type": "billing_structure"
    },
    {
      "element": "Contract components: License Subscription, Platform Fee, Discounts",
      "customization_type": "revenue_components"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Merchant Info Sheet - Marvin_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:00:12

### Original Content
```
rewatch com video r8kjqi41cda7x179-tim-ben-sync-november-4-2024 https: tabs rewatch com video gbv4lq9k385iq8z4-tabs-marvin-sync-on-pricing-november-5-2024 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Mostly fixed pricing with annual billing, but have a handful of monthly quarterly customers May launch a PLG motion at some point in the future Is there any important merchant relationship information 1) Merchant temperament is generally p...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing and pricing structure",
    "Merchant relationship management and stakeholder dynamics",
    "Implementation commitments and deliverables",
    "Contract terms and exit conditions",
    "Data integration and automation requirements"
  ],
  "rules": [
    "Merchant primarily uses fixed pricing with annual billing cycles",
    "AP (Accounts Payable) support must be delivered operationally for this customer",
    "Billing automation and data synchronization to SFDC (Salesforce) is required",
    "A 6-month opt-out clause exists in the contract",
    "Opt-out decisions require discussion with GS (likely Customer Success) and Royce",
    "Monthly and quarterly billing customers are supported as exceptions to annual billing",
    "Implementation team (AE & Implementation) is responsible for filling merchant billing information",
    "International/Ops team should ignore certain sections during processing"
  ],
  "exceptions": [
    "While mostly fixed annual pricing, a handful of customers have monthly or quarterly billing arrangements",
    "Potential future PLG (Product-Led Growth) motion may be launched, deviating from current sales model",
    "CEO (Prayag) was a hesitant buyer requiring special contract terms (opt-out clause)",
    "6-month opt-out provision granted despite not being standard practice"
  ],
  "merchant_specific": [
    "Champion contact: Tim (has prior working relationship with Ali at Latch)",
    "Key stakeholders: Tim, Jon, Noah (enthusiastic), Prayag/CEO (hesitant)",
    "Specific deliverable: AP support promised to this merchant",
    "Integration requirement: Push data back to SFDC",
    "Contract term: 6-month opt-out mark",
    "Merchant temperament: Generally positive",
    "Historical relationship: Tim and Ali previously worked together at Latch",
    "Primary goals: Streamline and automate billing processes"
  ],
  "confidence_score": 0.85
}
```

---

