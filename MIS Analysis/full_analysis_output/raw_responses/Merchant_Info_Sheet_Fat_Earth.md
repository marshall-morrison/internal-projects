# Raw LLM Analysis: Merchant Info Sheet - Fat Earth

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:18:17

---

## Chunk 1: Merchant Info Sheet - Fat Earth_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:18:17

### Original Content
```
Merchant Scoping start date: N A Implementation Completed Date (Go live date): N A MSA Signature Date: Mar 31, 2024 GTM POC: ERP: Tax Integration: Key people at Merchant Accountant: Mike Lawrence CFO: Rich Pacheco Company summary Red Antler LLC provides marketing services The Company offers research, branding, naming, digital designing, engineering, and advertising services AM Notes Larger   Enterprise account for Tabs (ACV  40k) Red Antler x Tabs   2024 Planning convo Red Antler x Tabs   2024 P...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract and Billing Term Management",
    "Customer and GL Integration Setup",
    "Invoice Creation and Scheduling Rules",
    "Payment Method Configuration",
    "Project ID Setup and Synchronization"
  ],
  "rules": [
    "For renewal contracts, process all Billing Terms under the renewal contract",
    "Contracts with Sent/Paid invoices cannot have their Billing Terms changed",
    "New edits, additions, or requests from merchant must go on entirely new contract and separate invoice",
    "When seeing a sent invoice on contact in garage, ask US team to duplicate the contract for new BTs",
    "Customer GL must be connected - search for existing customer in dropdown",
    "Use customer ID associated with the Fat Earth merchant when duplicates exist",
    "If customer doesn't exist, reach out to CSM (Royce as backup) to ask Fat Earth team to create customer",
    "Billing cadence is Monthly",
    "Default Payment Terms are Net 0 (if not listed in contract)",
    "Ignore contract terms for service term",
    "Always create 12 invoices or increments of 12 (e.g., 12, 24, 36)",
    "Invoice start date should be 1st of following month (e.g., if Aug 22, 2023, update to Sept 1, 2023)",
    "Mark all integration items as Retainer",
    "Media Fee is used for any overage that Red Antler billed (created as one-off items)",
    "Mike creates Project ID for any new customer",
    "Project ID must be synced via Garage secrets",
    "Merchant is defaulted to ACH credit payment method",
    "Credit Card should be turned OFF (review and confirm on invoice PDF)",
    "Ops to send slack bot notifications once processed"
  ],
  "exceptions": [
    "5 legacy customers should have CC payments enabled: Alison Lou, Mod Bikes, Ossio, Velotric, Waterlust, Feals",
    "For overage billing, Red Antler uses 'Media Fee' as one-off items",
    "If Project ID is not created, follow the Project Creation Workflow",
    "When customer selection changes, need to update and reset payments"
  ],
  "merchant_specific": [
    "Merchant name: Red Antler LLC / Fat Earth",
    "Key contacts: Accountant Mike Lawrence, CFO Rich Pacheco",
    "MSA Signature Date: Mar 31, 2024",
    "Account type: Larger Enterprise account (ACV 40k)",
    "Specific customer IDs associated with payment configuration",
    "Project ID setup process specific to Fat Earth",
    "Reference to 'Fat Earth - Project IDs - EXTERNAL' document",
    "Specific escalation contacts: Ops Team Chirag Manyapu, CSM Royce",
    "Integration with 'Garage' system for contract and customer management",
    "Special invoice memos may be required based on merchant-customer relationship",
    "CSV file reference for customer ID list",
    "Loom video training link for Project ID setup process"
  ],
  "confidence_score": 0.85
}
```

---

