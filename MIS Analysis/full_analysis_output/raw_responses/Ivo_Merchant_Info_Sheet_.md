# Raw LLM Analysis: Ivo- Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 4
- **Analysis Timestamp**: 2025-10-02 11:14:56

---

## Chunk 1: Ivo- Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:14:56

### Original Content
```
iscMerchant Demo date: Mar 11, 2025 Scoping start date: MSA Signature Date: Mar 14, 2025 Onboarding Kick Off Date: Mar 17, 2025 [If Exists] Opt Out Date: Go Live Date: Ideally send out their first invoice by Apr 1, 2025 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: Dan from Attivo, Cal from Attivo CFO: None Customer service rep who is really involved: None Account Receivable POC: Dan Billing POC: Dan, previously Muskaan https: www linkedin com in muskaan-b...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Milestones",
    "Contract Processing and Data Extraction",
    "Merchant Billing Model and Customer Creation",
    "Key Stakeholder Identification and Contact Information",
    "Service Agreement Terms and Nomenclature"
  ],
  "rules": [
    {
      "rule": "Pull customer address and email from contract to customer billing information",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Service Start Date must refer to the 'Effective Date' on the SaaS Service Agreement",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Months of Service must refer to the Initial Term in the contract",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "Item Name should be taken from 'Name of License' in the Service Fees section",
      "category": "Contract Processing",
      "explicit": true
    },
    {
      "rule": "First invoice should ideally be sent out by the Go Live Date",
      "category": "Billing Timeline",
      "explicit": true
    },
    {
      "rule": "SFDC standard integration is used for this merchant",
      "category": "Technical Integration",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "Latch is the merchant's old company name - if seen in contracts, it refers to the merchant itself, not a customer",
      "context": "Contract Processing",
      "impact": "Prevents misidentification of merchant as customer"
    },
    {
      "exception": "No opt-out clause exists for this merchant",
      "context": "Contract Terms",
      "impact": "Standard retention applies"
    },
    {
      "exception": "No unique customer creation process - merchant has all contracts ready in Google Drive folder",
      "context": "Customer Onboarding",
      "impact": "Streamlined processing possible"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company name history",
      "details": "Latch was the old name, now Ivo.ai",
      "customization_needed": true
    },
    {
      "element": "Key personnel",
      "details": "Dan from Attivo (Accountant, AR POC, Billing POC), Cal from Attivo, Phil (Head of Rev Ops), Muskaan (previous Billing POC)",
      "customization_needed": true
    },
    {
      "element": "Contract storage location",
      "details": "Google Drive folder containing all contracts",
      "customization_needed": true
    },
    {
      "element": "Business description",
      "details": "AI-powered contract review platform for legal teams",
      "customization_needed": false
    },
    {
      "element": "Contract field mapping",
      "details": "Specific fields: 'Effective Date', 'Initial Term', 'Name of License', 'Service Fees section'",
      "customization_needed": true
    },
    {
      "element": "Timeline dates",
      "details": "Demo: Mar 11, MSA: Mar 14, Kick Off: Mar 17, Go Live: Apr 1, 2025",
      "customization_needed": true
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 2: Ivo- Merchant Info Sheet__chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:00

### Original Content
```
Item Description: Leave blank Integration Item: Leave blank Billing Type: Flat Fee Total Price: Under Total Fee in the Service Fees section sum all discounts to one BT and have it just say "Discount" Integration item: Discount Class: 010-Revenue Category: Platform Anything that is not a discount but a BT, example: Ivo Integration item: IVO Class: 010-Revenue Category: Platform Quantity: Under Quantity in the Service Fees section Start Date: Refer to the Invoice Period Periods: Refer to the Invoi...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Invoice Line Item Configuration and Mapping",
    "Default Values and Operational Standards",
    "Integration Item Classification and Labeling",
    "Billing Terms and Frequency Management",
    "Tax Handling and Discount Processing"
  ],
  "rules": [
    {
      "rule": "Item Description field should be left blank",
      "category": "Field Configuration"
    },
    {
      "rule": "Integration Item field should be left blank by default",
      "category": "Field Configuration"
    },
    {
      "rule": "Billing Type should be set to 'Flat Fee'",
      "category": "Billing Configuration"
    },
    {
      "rule": "All discounts from Service Fees section must be summed into one BT (billing type) labeled as 'Discount'",
      "category": "Discount Processing"
    },
    {
      "rule": "Discount items must have Integration item: 'Discount', Class: '010-Revenue', Category: 'Platform'",
      "category": "Discount Processing"
    },
    {
      "rule": "Non-discount BT items (e.g., Ivo) should have Integration item matching the name, Class: '010-Revenue', Category: 'Platform'",
      "category": "Integration Item Mapping"
    },
    {
      "rule": "Quantity should be sourced from the 'Quantity' field in Service Fees section",
      "category": "Field Mapping"
    },
    {
      "rule": "Start Date should reference the Invoice Period",
      "category": "Date Configuration"
    },
    {
      "rule": "Periods should reference the Invoice Period",
      "category": "Date Configuration"
    },
    {
      "rule": "Frequency should reference the Invoice Period",
      "category": "Billing Configuration"
    },
    {
      "rule": "Net Terms should reference the Payment Period",
      "category": "Payment Configuration"
    },
    {
      "rule": "Default Service Term is 1 Year if none listed",
      "category": "Default Values"
    },
    {
      "rule": "Default Net Payment Terms is 30 days if none listed",
      "category": "Default Values"
    },
    {
      "rule": "Default Billing Frequency is Annual if none listed",
      "category": "Default Values"
    },
    {
      "rule": "Every tax line item becomes a BT (billing type) by default",
      "category": "Tax Processing"
    },
    {
      "rule": "All Statsig integration items should be labeled as 'Sales'",
      "category": "Integration Item Labeling"
    },
    {
      "rule": "All Pinata integration items should be labeled as 'Software Subscription Bundle' unless otherwise noted",
      "category": "Integration Item Labeling"
    }
  ],
  "exceptions": [
    {
      "exception": "Merchant-specific processing requests may differ by contract (e.g., back-dating invoice date to final day of month)",
      "context": "Contract Processing"
    },
    {
      "exception": "Pinata integration items can have different labels if specifically noted by merchant",
      "context": "Integration Item Labeling"
    },
    {
      "exception": "Certain contract items should be ignored based on merchant specifications",
      "context": "Contract Processing"
    }
  ],
  "merchant_specific": [
    {
      "element": "Invoice date back-dating requirements",
      "description": "Some merchants may request specific invoice date handling (e.g., always back-date to final day of month)",
      "variability": "high"
    },
    {
      "element": "Integration item labeling",
      "description": "Different merchants (Statsig, Pinata, Ivo) have specific integration item naming conventions",
      "variability": "medium"
    },
    {
      "element": "Contract-specific items to ignore",
      "description": "Each merchant may have specific elements that should be excluded from processing",
      "variability": "high"
    },
    {
      "element": "Events billing processing",
      "description": "Implementation Success team fills in event-specific billing instructions per merchant",
      "variability": "high"
    },
    {
      "element": "Post-processing communications",
      "description": "Notification requirements vary by merchant and implementation phase",
      "variability": "medium"
    }
  ],
  "confidence_score": 0.85
}
```

---

## Chunk 3: Ivo- Merchant Info Sheet__chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:10

### Original Content
```
Who needs to be notified and when Example: Who: Customer Success [Azmat Aziz] needs to be notified Where: Messari internal merchant channel When: contracts are processed [Merchant Phase: Active] Customer Information (Implementation Success to fill) Any important information on specifics customers of this merchant Special memo s certain invoices require Invoice changes due to merchant customer relationship Feature Requests (AE Implementation Success to fill) FR 1 What is it Why it's important Urg...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Notification and escalation protocols",
    "Customer relationship management and special requirements",
    "Feature request tracking and prioritization",
    "Call documentation and reference materials",
    "Cross-functional coordination (AE, Implementation Success, Customer Success)"
  ],
  "rules": [
    "Customer Success team member (Azmat Aziz) must be notified when contracts are processed",
    "Notifications should be sent to the Messari internal merchant channel",
    "Notifications are triggered when merchant phase reaches 'Active' status",
    "Implementation Success team is responsible for filling customer information section",
    "Account Executive (AE) and Implementation Success teams must jointly fill feature requests section",
    "AE and Implementation Success teams must document and provide links to key calls (Intro, Demo, Pricing/Implementation/CS, Final Pricing Negotiation)",
    "Special memos must be documented for certain invoices based on merchant-customer relationships",
    "Invoice modifications may be required due to specific merchant-customer relationships"
  ],
  "exceptions": [
    "Certain invoices require special memos (specific criteria not defined in this chunk)",
    "Invoice changes may be needed based on individual merchant-customer relationship dynamics",
    "Customer-specific information and requirements need to be documented on a per-merchant basis"
  ],
  "merchant_specific": [
    "Customer Success contact person (example: Azmat Aziz) - likely varies per merchant",
    "Messari internal merchant channel - appears to be merchant-specific communication channel",
    "Specific customer information and requirements unique to each merchant",
    "Special memo requirements for certain invoices - varies by merchant relationship",
    "Feature requests with varying urgency levels - merchant-dependent",
    "Call recordings and links (Gong.io) - unique per merchant sales cycle",
    "Pricing negotiation details - merchant-specific"
  ],
  "confidence_score": 0.72
}
```

**Reasoning for confidence score (0.72):**
- The document appears to be a template or form with incomplete sections, making some context unclear
- Several fields reference "to fill" indicating this is a work-in-progress document
- Specific details like urgency criteria for feature requests and special memo triggers are not fully defined
- The structure and key themes are clear, but some implementation details are ambiguous
- Links are truncated, limiting full understanding of the call documentation process

---

## Chunk 4: Ivo- Merchant Info Sheet__chunk_3

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:15:13

### Original Content
```
gong io call id 9164888570636868884 Notes Sections [Ops International Team to Ignore] (AE  Implementation to fill) Info on how merchant bills Flat price for certain amount of licenses future state- usage (launching mid-year) they have no idea what they want it to look like Is there any important merchant relationship information There s no accounting or finance person at Ivo Previously Muskaan (head of recruiting  yeah, crazy  i know), was doing the billing They just brought on Phil- Head of Rev...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant billing structure and future state planning",
    "Organizational structure and key stakeholders",
    "Tabs platform features and integration requirements",
    "Merchant relationship dynamics and decision-making hierarchy",
    "Automation requirements for billing and revenue operations"
  ],
  "rules": [
    "Implementation team should fill merchant billing information section",
    "Operations International Team should ignore certain sections marked accordingly",
    "Automatic invoice creation must be enabled for merchant",
    "Automated dunning processes must be configured",
    "Automated cash application must be set up",
    "Contracts must be stored in a central repository",
    "Invoices must auto-update based on contract amendments",
    "SFDC integration must be configured to push Tabs data for Account Managers",
    "CS and sales teams require visibility in Salesforce through Tabs integration"
  ],
  "exceptions": [
    "Merchant currently uses flat price for certain license amounts but plans to transition to usage-based billing mid-year",
    "Merchant has no clear vision for future billing structure ('they have no idea what they want it to look like')",
    "No dedicated accounting or finance person exists at the merchant organization",
    "Previous billing was handled by Head of Recruiting (non-standard role assignment)",
    "Merchant experiences high volume of mid-term amendments requiring special invoice update handling",
    "Muskaan transitioning out of involvement despite being a key stakeholder"
  ],
  "merchant_specific": [
    "Merchant name: Ivo",
    "Key stakeholders: Phil (Head of Rev Ops), Muskaan (Head of Recruiting, transitioning out), Dan and Cal (main end users from Attivo)",
    "Organizational context: No finance/accounting personnel, newly hired Rev Ops head",
    "Merchant temperament: Phil described as deferential and 'pushover', defers to Muskaan",
    "Specific pain point: High frequency of mid-term amendments to contracts",
    "Integration requirement: Salesforce (SFDC) as CRM system",
    "Historical context: Dan and Cal came from company called Attivo",
    "Call reference: Gong.io call ID 9164888570636868884"
  ],
  "confidence_score": 0.85
}
```

---

