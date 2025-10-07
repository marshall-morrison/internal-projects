# Raw LLM Analysis: Torch Merchant Info Sheet_

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:36:09

---

## Chunk 1: Torch Merchant Info Sheet__chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:36:09

### Original Content
```
Merchant Demo date: June 8th 2024 Scoping start date: Jul 24, 2024 MSA Signature Date: Aug 15, 2024 Onboarding Kick Off Date: Aug 22, 2024 [If Exists] Opt Out Date: n a Go Live Date: Oct 2, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Accountant: CFO: Jeff Nichols Controller anthony torch io   Good thought partner on implementation   Decision Making Sr Accountant: katie torch io   approves the contract, review the contract Jr Accountant: jonathan torch io   mana...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Management",
    "Customer and Item Data Entry Requirements",
    "Payment Terms and Net Terms Configuration",
    "Integration Mapping and System Configuration",
    "Stakeholder Roles and Communication Protocols"
  ],
  "rules": [
    {
      "rule_id": "R1",
      "category": "Contract Processing",
      "description": "Each line in the Product table represents its own Billing Term (BT)",
      "applies_to": "Torch order forms"
    },
    {
      "rule_id": "R2",
      "category": "Contract Processing",
      "description": "For amendments with new BTs, add them under the amendment contract",
      "applies_to": "Amendment documents"
    },
    {
      "rule_id": "R3",
      "category": "Contract Processing",
      "description": "Do not process PO documents directly; find the corresponding contract and add PO to that contract's invoices",
      "applies_to": "Purchase Order documents"
    },
    {
      "rule_id": "R4",
      "category": "Customer Creation",
      "description": "Include both billing and shipping date when creating new customers",
      "applies_to": "New customer setup"
    },
    {
      "rule_id": "R5",
      "category": "Item Entry",
      "description": "Copy Item Name exactly as it appears in the Product column",
      "applies_to": "All order forms"
    },
    {
      "rule_id": "R6",
      "category": "Item Entry",
      "description": "Copy Item Description exactly as it appears in the Product Description column",
      "applies_to": "All order forms"
    },
    {
      "rule_id": "R7",
      "category": "Item Entry",
      "description": "Use Quantity column value; default to 1 if blank",
      "applies_to": "All order forms"
    },
    {
      "rule_id": "R8",
      "category": "Pricing",
      "description": "If no discounts present, use the Total column value",
      "applies_to": "Total Price calculation"
    },
    {
      "rule_id": "R9",
      "category": "Pricing",
      "description": "If discount line present, calculate BT value net of discount",
      "applies_to": "Total Price calculation with discounts"
    },
    {
      "rule_id": "R10",
      "category": "Pricing",
      "description": "Apply discount proportionally across multiple BTs when one discount applies to multiple items",
      "applies_to": "Multi-BT discount scenarios"
    },
    {
      "rule_id": "R11",
      "category": "Date Configuration",
      "description": "Service Start Date equals Contract Start Date from order form",
      "applies_to": "All contracts"
    },
    {
      "rule_id": "R12",
      "category": "Date Configuration",
      "description": "Billing Start Date equals Service Start Date",
      "applies_to": "All contracts"
    },
    {
      "rule_id": "R13",
      "category": "Contract Terms",
      "description": "Months of Service calculated from contract start to end date length",
      "applies_to": "All contracts"
    },
    {
      "rule_id": "R14",
      "category": "Billing Frequency",
      "description": "Match frequency to contract length: annual contract = 1 year, 6 month contract = 6 months",
      "applies_to": "All contracts"
    },
    {
      "rule_id": "R15",
      "category": "Net Terms",
      "description": "Priority order: (1) Customer MSA, (2) Additional Terms section, (3) Customer-specific mapping, (4) Default Net 30",
      "applies_to": "Payment terms determination"
    },
    {
      "rule_id": "R16",
      "category": "Net Terms",
      "description": "Airbnb uses Net 60 days",
      "applies_to": "Airbnb customer"
    },
    {
      "rule_id": "R17",
      "category": "Net Terms",
      "description": "Sony uses Net 60 days",
      "applies_to": "Sony customer"
    },
    {
      "rule_id": "R18",
      "category": "Net Terms",
      "description": "Default to Net 30 days if no other terms specified",
      "applies_to": "All customers without specific terms"
    },
    {
      "rule_id": "R19",
      "category": "Integration",
      "description": "PASTE the Integration Item ID into Garage, NOT the item name",
      "applies_to": "Item mapping process"
    },
    {
      "rule_id": "R20",
      "category": "Integration",
      "description": "Follow Torch Item Mapping spreadsheet exactly",
      "applies_to": "Item mapping process"
    },
    {
      "rule_id": "R21",
      "category": "Integration",
      "description": "Use best judgement if exact item name not listed in mapping",
      "applies_to": "Item mapping edge cases"
    },
    {
      "rule_id": "R22",
      "category": "Invoice Fields",
      "description": "Add Purchase Order ID to additional invoice fields if available",
      "applies_to": "All invoices with PO numbers"
    },
    {
      "rule_id": "R23",
      "category": "Invoice Fields",
      "description": "If document is a PO, search for corresponding order form and add PO to invoice field",
      "applies_to": "PO document processing"
    },
    {
      "rule_id": "R24",
      "category": "Events Processing",
      "description": "No events billing required",
      "applies_to": "Torch merchant"
    }
  ],
  "exceptions": [
    {
      "exception_id": "E1",
      "description": "Non-Torch order forms require looking for similar Products table with comparable BT structure",
      "condition": "When order form is not on Torch paper"
    },
    {
      "exception_id": "E2",
      "description": "Quantity defaults to 1 only when field is blank",
      "condition": "Missing quantity data"
    },
    {
      "exception_id": "E3",
      "description": "Discount calculation varies: single discount line vs. one discount for multiple BTs (proportional)",
      "condition": "Presence and scope of discounts"
    },
    {
      "exception_id": "E4",
      "description": "Customer-specific net terms override default Net 30 (Airbnb and Sony = Net 60)",
      "condition": "Specific customer identification"
    },
    {
      "exception_id": "E5",
      "description": "Best judgement allowed when exact item name not in mapping spreadsheet",
      "condition": "Item not found in Torch Item Mapping spreadsheet"
    },
    {
      "exception_id": "E6",
      "description": "PO documents should not be processed directly; requires finding corresponding contract",
      "condition": "Document type is Purchase Order"
    }
  ],
  "merchant_specific": [
    {
      "element": "Billing Term Structure",
      "description": "Torch uses specific BT naming: 'Coaching 6 Month Unit - Executive', 'Coaching - Annual - Professional', 'Platform - Mentoring Edition'",
      "customization_needed": true
    },
    {
      "element": "Key Stakeholders",
      "description": "Katie and Anthony (audit background), Jonathan (collections), Adam (CRM integration), Jeff Nichols (CFO)",
      "customization_needed": true
    },
    {
      "element": "Business Context",
      "description": "Torch is downsizing NetSuite bill, previously used ARM modules and Celigo integration with errors",
      "customization_needed": true

---

