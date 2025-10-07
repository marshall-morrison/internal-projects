# Raw LLM Analysis: Merchant Info Sheet - Inspiren (OLD - IGNORE)

## Document Overview
- **Total Chunks Analyzed**: 3
- **Analysis Timestamp**: 2025-10-02 11:08:56

---

## Chunk 1: Merchant Info Sheet - Inspiren (OLD - IGNORE)_chunk_1

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:08:56

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
    "Billing configuration and timing requirements",
    "Hardware and software allocation across customer entities",
    "Default values and operational standards"
  ],
  "rules": [
    "Sub-customers should be set up with original contract for parent customer",
    "Sub-customers should only have software BT on them unless otherwise specified",
    "Pull terms from all contracts when multiple order forms exist",
    "Implementation should be processed under parent customer",
    "Hardware should be processed under parent customer if sub-customer amounts are not listed",
    "Hardware can be on sub-customers if amounts for each are determined (unless otherwise specified)",
    "Software usage BTs should be placed on sub-customers",
    "If no sub-customers are specified yet, process software only on parent customer and add later",
    "All Arrow recurring BTs (usage or hardware lease) must bill on the 16th of the month",
    "Ignore the 'Number of Contract Devices' section at top of contract if multiple locations/sub-customers exist",
    "Default Service Term: 1 Year if none listed",
    "Default Net Payment Terms: Net 30 if none listed",
    "Default Billing Frequency: Monthly if none listed",
    "Default Tax Handling: Every tax line item becomes a BT if none listed"
  ],
  "exceptions": [
    "Sub-customers can have more than software BT if otherwise specified",
    "Hardware can be processed differently than standard if otherwise specified",
    "Multiple order forms in single contract require processing both separately",
    "When multiple locations exist, ignore the contract device count at top of document",
    "Hardware allocation changes based on whether sub-customer amounts are determined or not"
  ],
  "merchant_specific": [
    "Arrow Senior Living specific: All recurring BTs must bill on 16th of month",
    "Integration items specific to this merchant: AUGi Base Platform (software), AUGi Base Station (hardware), AUGi Base Station Lease (hardware lease), Implementation Services (professional services)",
    "Feature requests: QBO bundle item support for HW+SW, Reporting by community (sub-customer)",
    "Specific location data: Arrow Senior Living locations in Mentor OH, Summit AR, and Highland Heights OH with billing contact homeofficeaccounting@arrowseniorliving.com",
    "Customer uses 'location name' and 'sub-customer name' interchangeably",
    "Reference calls stored in Rewatch system for historical context"
  ],
  "confidence_score": 0.92
}
```

---

## Chunk 2: Merchant Info Sheet - Inspiren (OLD - IGNORE)_chunk_0

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:01

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
    "Hardware is processed as flat price using integration item 'AUGi Base Station'",
    "Hardware is typically billed upfront using date specified in Billing Terms section, or effective date if not specified",
    "Total hardware cost is calculated based on total devices specified in contract table",
    "Software is processed as usage-based billing with integration item 'AUGi Base Platform'",
    "Software billing uses event 'has_active_camera' and is NOT billed in arrears (uncheck 'Is billed in arrears' checkbox)",
    "Software billing frequency follows Billing Terms section in contract",
    "Sub-customers must be created for each location listed in contract (bottom of contract or order form)",
    "Sub-customer billing address should match contract address",
    "Same as shipping address can be checked for sub-customers until other addresses provided",
    "Do not create sub-customer if location says 'TBD'",
    "If implementation fee is 'waived if signed before certain date', cross-reference with signature date to determine if BT is needed"
  ],
  "exceptions": [
    "EXCEPTION: If multiple locations (sub-customers) exist, hardware should be billed according to amounts specified per location",
    "EXCEPTION: If hardware is leased (not purchased), follow Billing Terms section instructions (often billed monthly or quarterly with software)",
    "For hardware lease with unspecified ship/install dates, start date should be first of next full month",
    "Hardware lease uses different integration item: 'AUGi Base Station Lease'",
    "If 'Lease option' language is present, process both lease and upfront purchase options, merchant will adjust based on which is chosen",
    "If hardware cost is $0, no hardware BT is needed",
    "Implementation fee is sometimes waived or not included, requiring no BT",
    "Hardware billing date may be adjusted via email amendments (process still being confirmed)",
    "Merchant bills ad hoc relative to contracts, using 'create your own billing terms' until more systematic approach is developed",
    "Sub-customers may be added during contract term via separate list from merchant"
  ],
  "merchant_specific": [
    "Merchant: Inspiren (AI-powered healthcare solutions)",
    "Go-live date: January 2024",
    "ERP system not specified",
    "Tax integration: Avalara (migration completed as of 3/28)",
    "Key contacts: Vin Cocito (Chief Customer Officer, co-founder), Jared Zimmer (Chief of Staff)",
    "Product names: 'AUGi Hardware', 'AUGi Base Station', 'AUGi Software', 'AUGi Base Platform'",
    "Integration items specific to Insperen: 'Implementation Services', 'AUGi Base Station', 'AUGi Base Station Lease', 'AUGi Base Platform'",
    "Usage event: 'has_active_camera'",
    "Billing model: Hardware + recurring subscription of varying lengths (quarterly, monthly)",
    "Contract structure: Three fee types (Professional Services Implementation, Hardware, Software)",
    "Merchant personality: 'super nice and patient'",
    "Current billing approach: Ad hoc, transitioning to more systematic approach",
    "Contract terminology: 'Communities' used to refer to locations/sub-customers"
  ],
  "confidence_score": 0.95
}
```

---

## Chunk 3: Merchant Info Sheet - Inspiren (OLD - IGNORE)_chunk_2

**Chunk Type**: instructions  
**Analysis Time**: 2025-10-02 11:09:06

### Original Content
```
com Arrow Senior Living - Boulevard St Peters   500 Bluffstone Circle, St Peters, MO 63304   homeofficeaccounting arrowseniorliving com Arrow Senior Living - Rushwood   2121 N 143rd Street E Wichita, KS 67230   homeofficeaccounting arrowseniorliving com Arrow Senior Living - Crestone   21810 W 119th Street Olathe, KS 66061   homeofficeaccounting arrowseniorliving com Arrow Senior Living - University Living   2865 South Main Street Ann Arbor, MI 48103   homeofficeaccounting arrowseniorliving com ...
```

### LLM Analysis Response
```json
{
  "themes": [
    "Senior living facility locations and contact information",
    "Centralized accounting email routing structure",
    "Multi-location business operations across multiple states",
    "Standardized communication channels for financial transactions"
  ],
  "rules": [
    "All Arrow Senior Living locations use the same accounting email: homeofficeaccounting@arrowseniorliving.com",
    "All Country Meadows locations use the same accounting email: AccountsPayable@countrymeadows.com",
    "Each facility location has a unique physical address",
    "Accounting communications are centralized at the corporate/home office level rather than handled at individual facility locations",
    "Two distinct senior living organizations are represented: Arrow Senior Living and Country Meadows"
  ],
  "exceptions": [
    "Country Meadows locations use a different email domain and structure (AccountsPayable vs homeofficeaccounting) compared to Arrow Senior Living",
    "Country Meadows - Forks includes additional address details ('1' designation) not present in other listings",
    "Geographic distribution varies: Arrow Senior Living spans MO, KS, and MI; Country Meadows is concentrated in PA"
  ],
  "merchant_specific": [
    "Organization name prefix (Arrow Senior Living vs Country Meadows)",
    "Specific facility names/identifiers (Boulevard St Peters, Rushwood, Crestone, University Living, Forks, York)",
    "Accounting email addresses and domains (arrowseniorliving.com vs countrymeadows.com)",
    "Physical addresses and geographic service areas",
    "Email naming conventions (homeofficeaccounting vs AccountsPayable)"
  ],
  "confidence_score": 0.85
}
```

---

