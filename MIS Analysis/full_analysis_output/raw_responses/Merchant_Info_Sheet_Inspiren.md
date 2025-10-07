# Raw LLM Analysis: Merchant Info Sheet - Inspiren

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 12:09:32

---

## Chunk 1: Merchant Info Sheet - Inspiren_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:09:32

### Original Content
```
They will send over location name (sub-customer name), address, and billing contact information These should be set up with the original contract for the parent customer These should only have the software BT on them (unless otherwise specified) Sometimes, there is more than 1 order form for a contract (order form being the table shown above This is often because there might be different sub-customers listed or different start dates for each order form In this case, process per normal requiremen...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Multi-location customer setup and hierarchy (parent-child relationships)",
    "Contract processing and order form handling",
    "Billing configuration and recurring charges (BTs - Billing Transactions)",
    "Default values and operational standards",
    "Hardware and software allocation across customer entities"
  ],
  "rules": [
    "Sub-customers should be set up with the original contract for the parent customer",
    "Sub-customers should only have software BT on them unless otherwise specified",
    "When multiple order forms exist, pull terms from both contracts",
    "Implementation should be processed under parent customer",
    "Hardware should be processed under parent customer if sub-customer amounts are not listed",
    "Hardware can be on sub-customers if amounts for each are determined (unless otherwise specified)",
    "Software usage BTs should be placed on sub-customers",
    "If no sub-customers are specified yet, process software only on parent customer and add later when location list is received",
    "All Arrow recurring BTs (usage or hardware lease) must bill on the 16th of the month",
    "Ignore 'Number of Contract Devices' section at top of contract if multiple locations/sub-customers exist",
    "Default Service Term: 1 Year if none listed",
    "Default Net Payment Terms: Net 30 if none listed",
    "Default Billing Frequency: Monthly if none listed",
    "Default Tax Handling: Every tax line item becomes a BT if none listed",
    "Billing contact for all Arrow locations: homeofficeaccounting@arrowseniorliving.com"
  ],
  "exceptions": [
    "Sub-customers can have more than software BT if otherwise specified",
    "Hardware can be processed differently if amounts per sub-customer are explicitly determined",
    "When multiple order forms exist due to different sub-customers or start dates, special processing is required",
    "Arrow-specific billing date requirement (16th of month) overrides standard billing dates",
    "Number of Contract Devices section should be ignored when multiple locations exist"
  ],
  "merchant_specific": [
    "Customer name: Arrow Senior Living",
    "Specific billing date requirement: 16th of the month for all recurring BTs",
    "Specific locations: Mentor (OH), Summit (AR), Highland Heights (OH)",
    "Centralized billing contact: homeofficeaccounting@arrowseniorliving.com",
    "Feature requests: QBO bundle item support for HW+SW, Reporting by community (sub-customer)",
    "Product terminology: AUGi Base Platform (software), AUGi Base Station (hardware), AUGi Base Station Lease (hardware lease)",
    "Service categories: Software usage BT, Hardware, Hardware Lease, Professional Services (Implementation Services)",
    "Integration items specific to this merchant's product suite",
    "Reference to recorded calls for additional context and setup details"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Inspiren_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:09:37

### Original Content
```
Merchant Scoping start date: 2023 Implementation Completed Date (Go live date): January 2024 MSA Signature Date: Feb 7, 2024 GTM POC: ERP: Tax Integration: (in progress) Avalara migration Key people at Merchant Vin Cocito - Chief Customer Officer (co-founder) Jared Zimmer - chief of staff Company summary Inspiren provides innovative AI-powered solutions for healthcare facilities to optimize patient care and workflow efficiency AM Notes They are super nice and patient They bill very ad hoc relati...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Contract Processing and Billing Term Creation",
    "Hardware Billing (Purchase vs Lease Options)",
    "Software Subscription Billing (Usage-Based)",
    "Sub-Customer Management and Multi-Location Handling",
    "Tax Integration and Payment Terms"
  ],
  "rules": [
    "All payment terms are defined in a 'Billing Terms' section of each contract",
    "Professional Services Implementation is a one-time fee, usually billed upfront",
    "Implementation Services should always be billed to parent customer, not sub-customer",
    "Hardware is named 'AUGi Hardware' with Billing Type: Flat Price and Integration Item: AUGi Base Station",
    "Hardware is typically billed upfront using date specified in Billing Terms section",
    "If no hardware billing date is specified, use the effective date of the contract",
    "Total hardware cost is calculated using total devices specified in the contract table",
    "Software is processed as usage-based billing with name 'AUGi Software'",
    "Software uses Billing Type: Unit Price with Event: has_active_camera",
    "Software Integration Item is 'AUGi Base Platform'",
    "Software billing is NOT in arrears - uncheck 'Is billed in arrears' checkbox for all usage BTs",
    "Software billing frequency follows the Billing Terms section in contract",
    "Multiple locations listed in contract must be created as sub-customers",
    "Each sub-customer receives the same billing terms as parent",
    "Sub-customer billing address should match the address on the contract",
    "Same as shipping address can be checked for sub-customers until other addresses are provided",
    "If location says 'TBD', do not create a sub-customer"
  ],
  "exceptions": [
    "Professional Services Implementation fee is sometimes waived or not included - no BT needed in these cases",
    "If implementation fee says 'waived if signed before a certain date', cross-reference with sign date to determine if BT is needed",
    "EXCEPTION: If multiple locations (sub-customers) exist, hardware should be billed according to amounts specified per location",
    "EXCEPTION: If hardware is leased (not purchased), follow Billing Terms section instructions (often billed monthly or quarterly with software)",
    "For lease option without specified ship/install date, start date should be first of next full month",
    "If 'Lease option' language is present, process both lease and bill-upfront options - merchant will adjust based on customer choice",
    "Hardware Lease uses Integration Item: AUGi Base Station Lease",
    "If hardware cost is $0, no hardware BT is needed",
    "Hardware billed upon shipment/installation should use effective date (but may receive email amendments adjusting amount/date)",
    "Locations are sometimes not determined at signing or added during contract term - merchant will send sub-customer lists to be created later"
  ],
  "merchant_specific": [
    "Merchant name: Inspiren (AI-powered healthcare solutions)",
    "Go-live date: January 2024",
    "Key contacts: Vin Cocito (Chief Customer Officer), Jared Zimmer (Chief of Staff)",
    "Tax integration: Avalara (implemented as of 3/28)",
    "Billing approach: Ad hoc relative to contracts, using 'create your own billing terms' until more systematic",
    "Product terminology: 'AUGi Hardware', 'AUGi Base Station', 'AUGi Software', 'AUGi Base Platform'",
    "Event trigger: 'has_active_camera' for usage-based billing",
    "Merchant characteristic: 'Super nice and patient'",
    "Billing model: Hardware + recurring subscription of varying lengths (quarterly, monthly)",
    "Contract structure: Three fee types - Professional Services Implementation, Hardware, Software",
    "Visual cue in contracts: 'Boxed in Red' indicates important billing information to process"
  ],
  "confidence_score": 0.95
}
```

---

## Chunk 3: Merchant Info Sheet - Inspiren_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 12:09:44

### Original Content
```
com Arrow Senior Living - Boulevard St Peters   500 Bluffstone Circle, St Peters, MO 63304   homeofficeaccounting arrowseniorliving com Arrow Senior Living - Rushwood   2121 N 143rd Street E Wichita, KS 67230   homeofficeaccounting arrowseniorliving com Arrow Senior Living - Crestone   21810 W 119th Street Olathe, KS 66061   homeofficeaccounting arrowseniorliving com Arrow Senior Living - University Living   2865 South Main Street Ann Arbor, MI 48103   homeofficeaccounting arrowseniorliving com ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Senior living facility locations and contact information",
    "Centralized accounting and payment processing structure",
    "Multi-location business operations across multiple states",
    "Standardized email routing for financial transactions"
  ],
  "rules": [
    "All Arrow Senior Living locations use the same accounting email address: homeofficeaccounting@arrowseniorliving.com",
    "All Country Meadows locations use the same accounting email address: AccountsPayable@countrymeadows.com",
    "Each facility location has a unique physical address that must be associated with the centralized accounting contact",
    "Payment and accounting communications should be directed to corporate accounting departments rather than individual facility addresses",
    "Facilities are organized by brand name (Arrow Senior Living, Country Meadows) with location-specific identifiers"
  ],
  "exceptions": [
    "Country Meadows locations use a different email format (AccountsPayable) compared to Arrow Senior Living (homeofficeaccounting)",
    "Country Meadows - Forks includes additional address detail '1' which may indicate a suite or building number",
    "Geographic distribution varies by brand: Arrow Senior Living spans MO, KS, and MI while Country Meadows appears concentrated in PA"
  ],
  "merchant_specific": [
    "Brand-specific naming conventions: 'Arrow Senior Living - [Location Name]' vs 'Country Meadows - [Location Name]'",
    "Location identifiers that may be neighborhood or street names (Boulevard St Peters, Rushwood, Crestone, University Living, Forks, York)",
    "Email domain structure differs by organization (arrowseniorliving.com vs countrymeadows.com)",
    "Centralized vs decentralized accounting department naming conventions",
    "State-specific location clustering may indicate regional management structures"
  ],
  "confidence_score": 0.85
}
```

---

