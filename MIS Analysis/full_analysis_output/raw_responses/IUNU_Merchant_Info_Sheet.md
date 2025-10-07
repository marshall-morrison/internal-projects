# Raw LLM Analysis: IUNU Merchant Info Sheet

## Document Overview
- **Total Chunks Analyzed**: 2
- **Analysis Timestamp**: 2025-10-02 11:38:38

---

## Chunk 1: IUNU Merchant Info Sheet_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:38

### Original Content
```
always back-date invoice date to final day of the month) None Default Service Term If None Listed, Ops Default is 1 Year Default Net Payment Terms If None, Ops Default is 30 Default Billing Frequency If None Listed, Ops Default is Monthly How do we handle taxes as a line item If None Listed, Ops Default is every tax line item becomes a BT Events Processing (if necessary) None today Integration Items Processing (if necessary) What are the instructions for assigning integration items None for now,...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Default operational parameters and fallback values",
    "Invoice processing and billing configuration",
    "Integration and system limitations",
    "Post-processing communication workflows",
    "Customer-specific handling requirements"
  ],
  "rules": [
    {
      "rule": "Invoice dates must be back-dated to the final day of the month",
      "category": "Invoice Processing",
      "explicit": true
    },
    {
      "rule": "Default service term is 1 year when none is listed",
      "category": "Service Configuration",
      "explicit": true
    },
    {
      "rule": "Default net payment terms is 30 days when none specified",
      "category": "Payment Terms",
      "explicit": true
    },
    {
      "rule": "Default billing frequency is monthly when none listed",
      "category": "Billing Configuration",
      "explicit": true
    },
    {
      "rule": "Every tax line item becomes a BT (Billable Tax) by default",
      "category": "Tax Processing",
      "explicit": true
    },
    {
      "rule": "Integration items are not assigned due to unsupported GL system",
      "category": "Integration",
      "explicit": true
    },
    {
      "rule": "Merchant will not be invoicing in Tabs system",
      "category": "System Usage",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception": "No integration items processing due to unsupported GL (General Ledger) system",
      "impact": "Merchant cannot use Tabs invoicing functionality",
      "condition": "GL system incompatibility"
    },
    {
      "exception": "Special memos required for certain invoices based on merchant-customer relationships",
      "impact": "Invoice customization needed per customer",
      "condition": "Specific customer relationships"
    },
    {
      "exception": "Invoice changes may be required due to merchant customer relationship dynamics",
      "impact": "Standard invoice templates may need modification",
      "condition": "Customer-specific requirements"
    }
  ],
  "merchant_specific": [
    {
      "element": "Customer Information",
      "description": "Important specifics about individual customers of this merchant",
      "customization_required": true
    },
    {
      "element": "Special memos for certain invoices",
      "description": "Customer-specific memo requirements",
      "customization_required": true
    },
    {
      "element": "Invoice changes based on merchant-customer relationships",
      "description": "Relationship-driven invoice modifications",
      "customization_required": true
    },
    {
      "element": "Post-processing notification requirements",
      "description": "Who needs to be notified and when regarding batch processing completion",
      "customization_required": true
    },
    {
      "element": "Feature Requests",
      "description": "Merchant-specific feature requests with urgency levels",
      "customization_required": true
    },
    {
      "element": "GL system type",
      "description": "Merchant uses unsupported GL system affecting integration capabilities",
      "customization_required": false
    }
  ],
  "confidence_score": 0.75
}
```

**Confidence Reasoning**: The document appears to be a partially completed template or form with many "None" values and incomplete sections. While the explicit rules about defaults are clear (0.9 confidence), the sections on customer information, special cases, and feature requests are incomplete or vague (0.6 confidence). The integration limitation is clear but lacks detail about the specific GL system. The overall structure suggests this is a merchant onboarding or configuration document, but missing information reduces certainty about the complete operational picture.

---

## Chunk 2: IUNU Merchant Info Sheet_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:38:40

### Original Content
```
Merchant Demo date: 4 16 Scoping start date: Apr 16, 2024 MSA Signature Date: May 20, 2024 Onboarding Kick Off Date: May 23, 2024 Go Live Date: Jun 1, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Richard Jacroux Fractional CFO Customer service rep who is really involved: Account Receivable POC Billing POC etc Company summary iUNU- Harware software - - technology for autonomous crop growing (serving agriculture) -  using computer vision AI Grower...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Merchant Onboarding Timeline and Key Dates",
    "Stakeholder Management and Communication Preferences",
    "Contract Structure and Billing Models",
    "Contract Processing Workflow and Fee Types",
    "ERP Integration and System Setup Requirements"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Processing",
      "description": "Most contract information is found at the end in Exhibit C",
      "explicit": true
    },
    {
      "rule_id": "R2",
      "category": "Effective Date",
      "description": "Use sign date as effective date if not otherwise specified",
      "explicit": true
    },
    {
      "rule_id": "R3",
      "category": "Provisioning Fee",
      "description": "Provisioning is a one-time fee sent out on the effective sign date",
      "explicit": true
    },
    {
      "rule_id": "R4",
      "category": "Service Fees",
      "description": "Service fees are recurring fees for service term duration",
      "explicit": true
    },
    {
      "rule_id": "R5",
      "category": "Service Start Date",
      "description": "Service start date or ready date should be assumed as 45 days after effective date if not specified",
      "explicit": true
    },
    {
      "rule_id": "R6",
      "category": "Installation Fee",
      "description": "If installation is listed, process as billing term 30 days after effective date with identified price",
      "explicit": true
    },
    {
      "rule_id": "R7",
      "category": "Shipping Fee",
      "description": "If shipping is listed, process as billing term 30 days after effective date as $0.00",
      "explicit": true
    },
    {
      "rule_id": "R8",
      "category": "Trial Period",
      "description": "Trial period accounts for the period between effective date and service start/ready date",
      "explicit": true
    },
    {
      "rule_id": "R9",
      "category": "Communication",
      "description": "Key POC (Richard) requires training on system setup, contract addition, user management, and note-taking",
      "explicit": true
    },
    {
      "rule_id": "R10",
      "category": "System Requirements",
      "description": "Merchant requires single database for contract collaboration (Finance CRM functionality)",
      "explicit": true
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Contracts tend to be bespoke, but billing types are fairly simple with just different rates",
      "context": "Contract variability"
    },
    {
      "exception_id": "E2",
      "description": "Merchant uses Xero ERP which is acknowledged as not optimal for current integration",
      "context": "ERP Integration"
    },
    {
      "exception_id": "E3",
      "description": "Key POC is focused during calls but scatterbrained in responding outside of calls",
      "context": "Communication management"
    },
    {
      "exception_id": "E4",
      "description": "Service fees may reference starting 'on or before' a ready date or service start date",
      "context": "Service fee timing flexibility"
    },
    {
      "exception_id": "E5",
      "description": "Document indicates 'Specifics processing things merchant has requested that may differ by contract' but details are cut off",
      "context": "Contract-specific variations"
    }
  ],
  "merchant_specific": [
    {
      "element": "Company Profile",
      "details": "iUNU - Hardware/software technology for autonomous crop growing using computer vision AI (agriculture sector)"
    },
    {
      "element": "Key Personnel",
      "details": "CFO: Richard Jacroux (Fractional CFO) - primary decision maker and key POC"
    },
    {
      "element": "ERP System",
      "details": "Xero (acknowledged as suboptimal for integration)"
    },
    {
      "element": "Billing Model",
      "details": "Flat service fees with long lists of terms followed by billing sheet"
    },
    {
      "element": "Contract Structure",
      "details": "Bespoke contracts with simple billing types at different rates"
    },
    {
      "element": "Primary Use Case",
      "details": "Single database for contract collaboration - Finance CRM functionality for team collaboration"
    },
    {
      "element": "Timeline",
      "details": "Demo: Apr 16, 2024; MSA Signature: May 20, 2024; Kick Off: May 23, 2024; Go Live: Jun 1, 2024"
    },
    {
      "element": "Fee Types",
      "details": "Provisioning (one-time), Service Fees (recurring), Installation (conditional), Shipping (conditional, $0.00)"
    },
    {
      "element": "Communication Preference",
      "details": "Schedule calls for important discussions; expect delayed responses outside of scheduled meetings"
    }
  ],
  "confidence_score": 0.85
}
```

---

