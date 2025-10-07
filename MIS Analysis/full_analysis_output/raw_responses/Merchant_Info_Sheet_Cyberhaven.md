# Raw LLM Analysis: Merchant Info Sheet - Cyberhaven

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:31:47

---

## Chunk 1: Merchant Info Sheet - Cyberhaven_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:31:47

### Original Content
```
3sMerchant Scoping start date: 2 13 Implementation Completed Date (Go live date): MSA Signature Date: 4 23 GTM POC: ERP: Tax Integration: (Anrok) Key people at Merchant CFO - John Morris - has been at the org for  6 months VP Biz Ops   COO - Rickie Goyal - super nice guy Has been closest to invoicing since John is newer more strategic anyway Edwin - head of the outsourced finance squad We haven t met him yet, but he s closest to their actual mechanics of invoicing and I expect him to play a role...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Document Handling",
    "Customer Assignment and Creation Rules",
    "Billing Terms and Invoice Processing",
    "Integration Item Mapping and SKU Management",
    "Reseller vs End User Relationship Management"
  ],
  "rules": [
    "Three documents are received for contract processing: Table in email body, Cyberhaven Quote, and Purchase Order",
    "Email body table must be uploaded to Tabs but no BTs processed under this document",
    "All BTs should be processed under the Cyberhaven Quote document",
    "Purchase Order is only needed for billing/shipping address when creating new customers",
    "Customer assignment: If 'Channel Partner' row has a value, use Channel Partner as customer (reseller agreement)",
    "Customer assignment: If 'Channel Partner' row says 'n/a', use 'End User Account' as customer",
    "Link to existing customer in Tabs if customer already exists",
    "For new customers, billing address is found on PO",
    "For reseller agreements, do NOT add shipping address when creating customer",
    "Add shipping address from PO only when 'Channel Partner' row shows 'n/a'",
    "Billing contact information found in email body table under 'Invoice contact' and 'Email for Invoice' rows",
    "Item name comes from Quote (SKU starting with CYB)",
    "Description includes full description from quote",
    "Quantity comes from QTY column in quote",
    "Amount is total amount from quote",
    "Net terms: DO NOT USE QUOTE - refer to email body table 'Net Payment Terms' row",
    "Start date/service period: Use quote if available, otherwise refer to email body table",
    "PO Number priority: Use 'PO Number from Channel Partner' if available, otherwise use 'PO Number from End User' if Channel Partner shows 'n/a'",
    "After BTs are processed, enter PO from the PO document via Invoice tab from Additional Actions section"
  ],
  "exceptions": [
    "If quote/purchase order does not have certain billing terms, use the email body table document as fallback",
    "Shipping address exception: For reseller agreements (when Channel Partner has a value), do NOT add shipping address",
    "Shipping address exception: Only add when Channel Partner row shows 'n/a' or mark as 'same as billing address' if applicable",
    "Integration items in Tabs show display names while quote shows SKU names - mapping required between the two",
    "Some integration item display names match SKU names, but some are name vs code and require translation"
  ],
  "merchant_specific": [
    "Merchant: Cyberhaven (3sMerchant)",
    "Key personnel: CFO John Morris (6 months tenure), VP Biz Ops, COO Rickie Goyal, Edwin (head of outsourced finance)",
    "Business model: High ACV cybersecurity software sold directly or through channel partners/resellers",
    "Billing model: Basic subscriptions with varying cadences (annual, quarterly), bills ahead of time with Net 180 terms",
    "ERP: Not specified",
    "Tax Integration: Anrok",
    "Specific SKU prefix: CYB (e.g., CYB-SW-DDR, CYB-PS-ADVANCED, CYB-PS-LAUNCH, CYB-ADV-CONT-INSP)",
    "Integration item mappings: CYB-SW-DDR = Cyberhaven License, CYB-PS-ADVANCED = CYB-PS-ADVANCED, CYB-PS-LAUNCH = Cyberhaven Professional Services, CYB-ADV-CONT-INSP = Cyberhaven Advanced Content Inspection",
    "Document branding: Cyberhaven Quote has Cyberhaven logo at top",
    "Current practice: Bills ahead of time so they don't have to remember to bill for future periods",
    "Complexity: Determining when to bill reseller vs end user and managing POs"
  ],
  "confidence_score": 0.92
}
```

---

