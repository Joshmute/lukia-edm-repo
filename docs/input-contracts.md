# Input contracts and evidence limits

Only the PDF was provided. The canonical schemas below are implemented by the labelled simulation; adapt them by documented column mapping before using genuine operational extracts. Do not silently map similarly named fields.

| File | Required canonical headers | Optional fields used |
|---|---|---|
| SRG_Customers.csv | customer_id,name,phone,email,district | dob,gender,updated_at |
| SRG_Products.csv | sku,name,unit,category | updated_at |
| SRG_Sales.csv | source,order_id,line_no,order_date,sku,store_id,quantity,unit_price,currency | customer_id,payment_ref |

Source identifiers must be namespaced before combining systems. Customer IDs used by sales must resolve through an approved crosswalk. Product SKUs must resolve uniquely: conflicting duplicates are not safe lookups.

Dates: ISO YYYY-MM-DD by default; YYYY/MM/DD and named-month DD-Mon-YYYY accepted. DD/MM/YYYY is enabled only by explicit `--day-first` after source confirmation. Full timestamps must first be parsed with their actual source timezone, stored as UTC, then converted to Africa/Kampala for the business date. Never truncate an unknown timestamp string into a date.

Phone normalisation currently handles Ugandan numbers with 3/7 prefixes. Kenya/Rwanda need separate verified numbering rules and country fields. Successful syntax is not ownership verification.

Money: the core canonical parser accepts unambiguous decimal notation and optional matching UGX/KES/RWF prefix. Commas are assumed thousands separators under this contract. It rejects negative unit prices, unknown currency, nonfinite quantities and mismatched labels. Returns use negative quantity. No FX conversion takes place. Taxes, discounts and gross/net interpretation need confirmation before claiming accounting revenue.

Reference files are demonstration-only. Obtain the complete approved district list and product taxonomy. Category aliases are explicit correction decisions; pack quantities are never inferred from unit spelling.

## Checks before real deployment

- Suppliers: inspect all versions, profile supplier identifier/name/contact/bank fields, approve master ownership and link products. No fabricated supplier findings.
- Loyalty: preserve points ledger and account/customer crosswalk; reconcile opening + deltas to closing balance before merging accounts.
- HR: inspect actual XLSX headers, classify sensitive fields and isolate them. Never publish workbook rows.
- ETL log: preserve original log and isolate the first causal error; record reproduced test and rerun results.
- Footfall JSON: inspect contract, timestamps, duplicate IDs and any persistent personal identifiers before choosing windows or privacy controls.

## Production boundaries

Python executes conservative cleansing and canonical sales validation. MySQL 8.4 is the only target DBMS. Source-specific live connectors, approved identity merges, historical backfill and publication are not deployed by this prototype. Simulation schemas are explicit teaching assumptions, not claims about instructor files.
