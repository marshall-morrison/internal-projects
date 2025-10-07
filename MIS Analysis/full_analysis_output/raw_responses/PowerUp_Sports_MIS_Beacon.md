# Raw LLM Analysis: PowerUp Sports MIS (Beacon)

## Document Overview
- **Total Chunks Analyzed**: 1
- **Analysis Timestamp**: 2025-10-02 10:29:34

---

## Chunk 1: PowerUp Sports MIS (Beacon)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 10:29:34

### Original Content
```
Processing Steps General BTs will be found in the Fees section IGNORE Payment Processing fees  0 BTs 1  Gross Profit BT BT for  Any registrations that are sub  100 will be charged at 2  If a contract has  Minimum annual registrations,  we will need to turn on Usage AI (instructions below) Discount Use the net price after discounts for BTs Item Name: Use the label of the fee but keep it clean and concise (e g , "Licensing Fee," "Website Hosting," "Youth Team Fee") Quantity: For licensing fees, ca...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Billing Transaction (BT) Creation and Configuration",
    "Fee Structure and Pricing Models",
    "Usage-Based Billing and Thresholds",
    "Service Terms and Timing Parameters",
    "Licensing Fee Processing"
  ],
  "rules": [
    "General BTs are found in the Fees section of contracts",
    "Payment Processing fees should be ignored (0 BTs)",
    "Gross Profit BT equals 1 BT for registrations",
    "Registrations under $100 are charged at 2%",
    "Use net price after discounts for BT calculations",
    "Item names should be clean and concise labels (e.g., 'Licensing Fee', 'Website Hosting', 'Youth Team Fee')",
    "For licensing fees, quantity can use number of players if listed",
    "Service and Billing Start Date should use the 'Effective Date' from contract",
    "For multi-year fees, Year 1 uses effective date, Year 2 uses effective date + 12 months",
    "Default to 12 months of service if nothing specified",
    "Billing frequency follows the cadence listed in fees section header (overrides Invoicing/Billing section)",
    "One-time setup fees should have frequency set to 'None'",
    "Default net terms are 30 days unless otherwise specified",
    "No-Show Fee of $100 should be set up as usage fee, billed monthly in arrears",
    "For Usage AI with minimum annual registrations: create flat BT first in dollar amount (not player count)",
    "Threshold amount should be dollar representation of minimum (multiply player count by per-player fee if needed)",
    "Select 'charges overages' for threshold configuration",
    "Threshold period is full service term"
  ],
  "exceptions": [
    "Contracts with 'Minimum annual registrations' require Usage AI to be turned on",
    "Sub-$100 registrations have special 2% charge rate",
    "Multiple year fees require separate BTs with staggered start dates",
    "Fees section headers override instructions in Invoicing/Billing section",
    "Licensing fees can have multiple setups: flat annual fee, flat fee with overage, or tiered per player",
    "No-Show Fee is conditional on 'Failure to attend scheduled training without prior notice' clause",
    "For tiered per player registration: use tiered usage BT with no flat fee needed",
    "For flat fee with overage: combine flat price for annual fee with tiered usage BT for overage"
  ],
  "merchant_specific": [
    "Player registration quantities and thresholds (varies by sports organization)",
    "Specific fee amounts (e.g., $1,200 CAD, $100 no-show fee)",
    "Contract effective dates and termination dates",
    "Billing frequency preferences (quarterly, annually, monthly)",
    "Discount structures and net pricing",
    "Minimum registration requirements (e.g., 1,200 players)",
    "Per-player rate structures",
    "Training session policies and no-show penalties",
    "Currency specifications (CAD mentioned)",
    "Custom fee labels and terminology per merchant"
  ],
  "confidence_score": 0.85
}
```

---

