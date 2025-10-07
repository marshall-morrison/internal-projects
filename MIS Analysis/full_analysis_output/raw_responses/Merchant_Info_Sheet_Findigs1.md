# Raw LLM Analysis: Merchant Info Sheet - Findigs(1)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 09:50:16

---

## Chunk 1: Merchant Info Sheet - Findigs(1)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 09:50:16

### Original Content
```
Findigs Scoping start date: Oct 13, 2023 Implementation Completed Date (Go live date): May 10, 2024 MSA Signature Date: Feb 15, 2024 GTM POC: Implementation POC: ERP: Tax Integration: Key people at Merchant Head of Finance: Sebastian Hart Primary PoC and Decision Maker Finance Associate: Ellie Barney We re replacing the manual work she used to have to do Engineering: Parth Company summary  Findigs makes renting safe and easy for renters and property managers Rent units faster with zero fraud Our...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Remittance Workflow Management",
    "Contract and Billing Processing",
    "Third-Party Integration (Orum, QBO)",
    "Monthly Usage-Based Event Processing",
    "Multi-Step Approval and Communication Flow"
  ],
  "rules": [
    "Monthly usage-based billing model in arrears",
    "Remittance processing involves approximately 200 transactions per month",
    "Orum transfers take approximately 4 days to process",
    "Two-step approval required: Ellie (Findigs) approves first, then Tabs approves in Garage before sending to Orum",
    "Bank account information must be collected via Survey Monkey from portfolio managers",
    "New contracts require customer-to-vendor conversion (Hyung performs this flip)",
    "Orum setup requires two superpowers: 'Create Orum Business' and 'Create Orum External Account'",
    "Remittance amount calculated from column 'total_remittance_to_portfolio' (column AH) in usage data",
    "Two automated emails sent: (1) 'New Remittance xxx from Findigs for $xx on [Date]' after Tabs approval, (2) 'Payment confirmation for Remittance xx from Findigs for $XX' after QBO sync",
    "Orum business and bank account accuracy must be verified by logging into Orum",
    "Status must be observed changing from 'Pending' to 'Completed' in Orum",
    "Deepak pipeline creates one-off billing terms for Findigs",
    "Ops team must confirm remittance amounts are accurate by combining QBO Vendor ID totals",
    "Usage file is broken down by Property Manager in each row"
  ],
  "exceptions": [
    "No contracts provided by client - use sample tabs contract for processing",
    "Client (Ellie) may need to update or change remittance amounts - this is acceptable and Deepak can update",
    "If 4-5 events processed in a month (like May), okay to push back to next month if needed",
    "Contract processing steps may differ from standard - none provided from client in this case"
  ],
  "merchant_specific": [
    "Merchant name: Findigs",
    "Key contacts: Sebastian Hart (Head of Finance), Ellie Barney (Finance Associate, Primary PoC)",
    "Engineering contact: Parth",
    "GTM POC and Implementation POC fields (not filled)",
    "Specific dates: Scoping start (Oct 13, 2023), Go live (May 10, 2024), MSA signature (Feb 15, 2024)",
    "Business description: Digital underwriting platform for rental applications",
    "Remittance partner: Orum",
    "Survey link: Survey Monkey for collecting bank account information",
    "Usage data file naming convention: 'Findigs Usage Data - [Month]'",
    "Approximately 200 remittances per month (merchant-specific volume)",
    "Custom remittance workflow built from scratch for this merchant",
    "Specific approval workflow: Ellie approves → Tabs approves → Orum processes",
    "Integration systems: Orum, QBO (QuickBooks Online)",
    "Internal contacts: Azmat Aziz (usage processing), Hyung Seok Choi, Royce Kok (Orum setup), Deepak (billing terms/updates)"
  ],
  "confidence_score": 0.92
}
```

---

