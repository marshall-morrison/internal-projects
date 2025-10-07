# Raw LLM Analysis: Merchant Info Sheet - Fat Earth(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 11:44:59

---

## Chunk 1: Merchant Info Sheet - Fat Earth(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:44:59

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
    "Project ID Management and Synchronization"
  ],
  "rules": [
    "For renewal contracts, process all Billing Terms under the renewal contract",
    "Contracts with Sent/Paid invoices cannot have their Billing Terms changed",
    "New edits, additions, or requests from merchant must go on entirely new contract and separate invoice",
    "When seeing a sent invoice, ask US team to duplicate the contract for new Billing Terms",
    "Always search for existing customer in dropdown when GL is connected",
    "Use customer ID associated with the Fat Earth merchant when duplicates exist",
    "Flag Ops Team (Chirag Manyapu) if unsure about customer selection",
    "Reach out to CSM (Royce as backup) if customer doesn't exist to have Fat Earth team create customer",
    "Billing cadence is Monthly",
    "Default Payment Terms are Net 0 if not listed in contract",
    "Ignore contract terms for service term",
    "Always create invoices in increments of 12 (12, 24, 36, etc.)",
    "Invoice start date should be 1st of following month (e.g., Aug 22, 2023 becomes Sept 1, 2023)",
    "Mark all integration items as Retainer",
    "Media Fee is used for any overage that Red Antler billed (created as one-off items)",
    "Mike creates Project ID for any new customer",
    "Sync Project ID via Garage secrets with specific workflow",
    "Default payment method is ACH credit",
    "Credit Card should be turned OFF (review and confirm on invoice PDF)",
    "Send Slack bot notifications once processed"
  ],
  "exceptions": [
    "5 legacy customers should have CC payments enabled: Alison Lou, Mod Bikes, Ossio, Velotric, Waterlust, Feals",
    "Contracts that already have Sent/Paid invoices require contract duplication for changes",
    "Media Fee overages are handled as one-off items added by Red Antler",
    "If Project ID is not created, follow the Project Creation Workflow",
    "Customer ID list needs to be updated when changes occur and payments reset"
  ],
  "merchant_specific": [
    "Merchant name: Red Antler LLC / Fat Earth",
    "Account Manager: Larger Enterprise account (ACV 40k)",
    "Key contacts: Mike Lawrence (Accountant), Rich Pacheco (CFO)",
    "CSM: Royce (as backup)",
    "Ops contact: Chirag Manyapu",
    "Specific customer IDs associated with Fat Earth merchant",
    "Project ID setup specific to Fat Earth with external project ID list",
    "Custom billing model for Fat Earth contract processing",
    "Specific integration with Garage system",
    "Red Antler-specific 'Media Fee' terminology for overages",
    "Reference to csv file for customer ID list",
    "Loom video link for Project ID setup process"
  ],
  "confidence_score": 0.85
}
```

---

