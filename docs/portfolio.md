# Project Savanna
## Enterprise Data Management Turnaround
Savanna Retail Group | Board consultancy portfolio

Prepared for the Enterprise Data Management individual capstone.

**KAUDHA LUKIA | 2025-08-40008**

3 October 2026 | MySQL implementation

Repository: https://github.com/Joshmute/lukia-edm-repo

**AI assistance declaration:** OpenAI Codex and Anthropic Claude (Claude Code and Claude for Chrome) assisted with research, drafting, code, simulation data, diagrams, dashboard construction and test execution. All outputs were executed and checked.

[PAGE]

# A1 | Board memo, page 1 of 2
**To:** SRG Board of Directors  
**Subject:** Why two more DBAs will not resolve the data problem

A database administrator can restore a failed database, improve a slow query and restrict a database account. Those are useful skills. They do not decide whether the customer called Amina in one store is the same person as the loyalty member in another, whether a supplier's carton means six units or twelve, or who must act when a laptop disappears.

That distinction explains SRG's repeated clean-ups. Traditional database management keeps individual databases dependable. Enterprise data management makes data usable and accountable across the business, from its collection to its eventual deletion. SRG's 23 store databases can each be technically healthy while the group still issues points to the wrong customer.

The reported 23% duplicate rate is an estimate, not a measured baseline for this project. Even so, the wrong-member loyalty incidents show that identity is already a business control issue. The same is true of five identifiers for one product. Making each database faster would simply move inconsistent records through the business more quickly.

The 11-day monthly reporting cycle is a coordination failure as much as a technology failure. Finance repeatedly decides which spreadsheet to trust because the source systems have no shared definitions or accountable certification process. The 8.4% stock variance may include theft, receiving errors, returns, pack-size mistakes and timing differences. It is not evidence that any one of those causes has been proved.

The Jinja theft is the clearest warning. An unencrypted export of 9,000 customer records left a controlled system and remained unreported internally for 11 days. Database tuning cannot prevent that export or make a frightened employee report a loss promptly. Device controls, approved access routes, a named incident owner and a rehearsed reporting process can.

I recommend using the existing IT staff to support a small shared data service, with short-term specialist support tied to handover. Business managers must own the meanings and permitted uses of data. The Board should ask for evidence of control, not just proof that a server is running.

[PAGE]

# A1 | Board memo, page 2 of 2
## The missing enterprise functions
DAMA-DMBOK [S8] distinguishes eleven knowledge areas. The scenario supports this diagnosis; no organisational interviews are claimed.

**Governance:** No clear decision owner; establish a council and escalation route. **Architecture:** Isolated systems need an offline-tolerant hub. **Modelling:** Agree customer, product and order definitions. **Storage and operations:** Local databases exist, but restores and extracts need common controls.

**Security:** Encrypt devices and restrict exports. **Integration:** Replace manual imports with contracts and reconciliation. **Document management:** Version and assign owners to supplier files. **Reference and master data:** Review identity links and maintain product crosswalks.

**Warehousing and BI:** Certify facts and show freshness. **Metadata:** Record definitions, owners and dependencies. **Quality:** Validate at entry and assign recurring defects to business owners.

Governance, MDM, metadata and continuous quality management are the clearest gaps. Database administration alone cannot supply them.

## Requested Board decision
Approve a three-store pilot, including Jinja and a poorly connected store. Customer service owns identity; procurement owns product codes; Finance certifies financial measures. By month 6, require reconciled daily loads and a close rehearsal within five working days. Validate difficult matches and disputes before accepting a lower duplicate rate.

A managed asset has an owner, definition, permitted purpose, quality threshold and correction route. A one-off clean-up provides none of these lasting obligations.

[PAGE]

# A1 | Customer data lifecycle
![Customer lifecycle](diagrams/lifecycle.png)

**Create — POS, loyalty app, checkout; cashiers and customer service:** Rushed forms, duplicate signups, unclear permission. Use minimum fields, local provisional IDs and separate marketing choice.

**Store — Local DBs and hub; IT manager:** Unencrypted copies or broad access. Encrypt managed devices; restrict raw zone and log exports.

**Use — Loyalty, CRM, BI; customer-service and finance managers:** Wrong identity, stale preferences. Publish reviewed crosswalks and propagate withdrawals first.

**Share — Mobile money processors, distributor, cloud; DPO and procurement:** Excess fields or unclear destination. Approve purpose, processor terms and transfer assessment.

**Archive — Restricted archive and backups; IT manager:** Indefinite retention and forgotten spreadsheets. Apply schedules, legal holds and access reviews.

**Delete — Source systems, hub, processor copies; owner and IT:** Deleted records reappear after restore. Propagate tombstones; reapply deletions before restored systems reconnect.


Mobile money linkage uses a payment reference and verified account relationship. A payer's phone is not automatically the purchaser's identity. A customer may pay for someone else.

[PAGE]

# A2 | A governance charter SRG can operate
**Vision:** A sale should mean the same thing in a store, in Finance and in the Board pack. A customer should be able to understand and challenge how SRG uses their information.

**Scope:** Customer, product, supplier, sales, payment, inventory and employee data across current Ugandan operations. Kenya, Rwanda and EU-facing services require a separate readiness gate before their data enters production.

**Principles:** Collect only what serves an agreed purpose. Keep evidence of changes. Correct problems at their source. Keep trading possible offline. Give a named business owner the final say on definitions. Do not hide uncertainty in a dashboard.

## Operating structure using existing titles
The monthly council consists of the COO (chair), CFO, IT manager, procurement manager, customer-service manager and HR manager. The CEO appoints an existing compliance/company-secretariat officer as DPO, with direct Board escalation and protected time. These titles are assumptions to confirm against SRG's organisation chart; they are responsibilities, not six new hires. If that officer has conflicting duties, the CEO must reassign them and buy limited external advice.

Customer service owns customer identity and loyalty; Procurement owns product and supplier masters; the COO owns stock and stores; the CFO owns sales and payment definitions; HR owns employee data. One experienced officer in each function acts as steward for two protected hours each week. IT operates the controls and cannot approve its own access exceptions.

The council is a 45-minute decision meeting. Stewards resolve routine defects within two working days. Disputes older than five days go to the owner; unresolved cross-domain disputes go to the COO. Privacy risks go directly to the DPO without waiting for the meeting.

## Authority and accountability
The council approves definitions, thresholds and changes to shared attributes. A request must state the problem, owner, affected reports, migration plan and rollback. Approvals are recorded in the repository; no approval by informal chat alone. Every month, the CFO signs the reconciliation, the COO signs store freshness exceptions, and the DPO reviews access and incident evidence.

The RACI register (docs/raci.csv) assigns one accountable role per activity. No new governance committee is needed at store level. Store managers receive an exception queue they can act on, not a second reporting pack.

[PAGE]

# A2 | Three enforceable policies
## P1. Access and classification
**Owner:** IT manager; DPO approves privacy exceptions. Label data Public, Internal, Confidential or Restricted. Customer contacts, payment linkages and HR details are Restricted. Analysts receive aggregated or pseudonymised views; cashiers use a store-scoped application. Shared logins and personal email exports are prohibited.

Within 30 days, every device accessing Restricted data must have managed disk encryption, screen lock and remote revocation. Export requires a recorded purpose, data-owner approval and expiry within 24 hours. Restricted exports cannot be stored on unmanaged laptops or USB media. IT blocks that route and supplies a managed workspace instead. Remove leaver access within four hours of notice; review all access quarterly. Daily endpoint checks must reach 100% coverage; isolate noncompliant devices from Restricted data.

This single enforced policy would have prevented the **unencrypted customer export exposure**, although it could not have prevented the physical theft. The predictable daily violation is the convenient spreadsheet copy. Enforcement needs a usable approved alternative, endpoint controls and owner review of blocked-export logs.

## P2. Data quality
**Owners:** Customer-service and procurement managers for their domains. All new shared records must meet the validation catalogue. Invalid identities, conflicting SKUs and unrecognised currency/date formats are quarantined from certified reporting. Never discard transactions merely to improve a quality percentage.

Run quality checks at entry and nightly. Publish both accepted and rejected counts, their monetary value, and the denominator for every percentage. A critical rule failure blocks certification. A warning creates a steward ticket by 09:00 next working day. Repeated defects from one source require a process change within ten working days. Review a stratified sample of 100 match decisions monthly; suspend automated matching after any confirmed harmful false merge.

## P3. Retention and deletion
**Owner:** DPO; domain owners justify purpose and IT executes. Proposed operating periods: raw intake 30 days after reconciliation; unresolved exceptions reviewed every 30 days; inactive loyalty contacts reviewed after 24 months; operational access logs 12 months; backups expire after 35 days. These are design choices, not statutory periods. Finance and counsel must approve accounting/HR schedules against applicable obligations before activation [S1, s18].

Legal holds override scheduled deletion only for specified records and a documented reason. Run monthly expiry jobs, record counts and processor acknowledgements, and test deletion propagation quarterly. After restore, apply the deletion ledger before granting normal access. An exception requires an owner, reason and expiry; “keep everything” is not an acceptable reason.

[PAGE]

# A2 / C2 | Compliance obligations and gap register
The complete obligation, evidence, owner and priority register is in docs/compliance-register.csv. The immediate gaps concern Uganda DPPA security and notification (ss20,23), registration, rights and marketing; GDPR scope, security, breach and transfer duties; and conditional CCPA applicability. These are operating obligations with named owners, not a claim of certification.

**Assessment:** Desk review of the scenario only. Unknown means evidence was not provided. It does not mean compliant. Priority P0 is immediate; P1 is within 30 days; P2 is before month 12.


**Audit checklist result:** Security and incident handling fail on stated facts. Quality is deficient. Registration, contracts, lawful basis, retention and rights controls are unverified. No control receives a pass without evidence. Reassess at months 3, 6 and 9; obtain an independent readiness review in month 11.
[PAGE]

# A2 | Memo to the CFO
**Subject:** Governance is cheaper when it prevents rework

I agree that a committee without decisions would waste money. The proposed governance process should be judged by fewer reconciliation hours, fewer incorrect loyalty adjustments and a faster close, not by the number of policies it produces.

Consider a deliberately modest planning estimate for the Jinja incident. Contacting 9,000 people at UGX 1,500 each costs UGX 13.5M. Two hundred investigation/support hours at UGX 40,000 cost UGX 8M. External incident advice at UGX 8M and a replacement device at UGX 3M bring the direct response estimate to **UGX 32.5M**. These are assumptions, not invoices or a legal damages estimate. They exclude lost trust, compensation, fines and diverted management time. At half/double the contact cost, the estimate becomes UGX 25.75M/46M.

There is a second cost even without another incident. If consolidation consumes 11 working days each month for three staff at UGX 120,000 per person-day, annual effort is 11 x 3 x 120,000 x 12 = **UGX 47.52M**. Cutting the work to three days would release UGX 34.56M of capacity a year. The brief gives elapsed reporting time, not actual labour input, so Finance must validate this assumption before calling the capacity a saving. Released time is not automatically a cash saving.

Two industry cases show why weak controls deserve attention. The UK ICO fined British Airways GBP 20M in 2020 over a breach affecting more than 400,000 customers. It fined Marriott GBP 18.4M after failures to protect guest records. Their scale, jurisdiction and attack paths differ from SRG's; their fines are not a forecast for Uganda. Their relevant lesson is that failure to maintain and verify basic safeguards can become a board-level cost [S9].

For SRG, the immediate business case is smaller and more concrete: stop unmanaged exports, appoint people who can settle definitions, and require evidence that sales totals reconcile. We will not count all reported stock variance as recoverable profit. The pilot must establish how much comes from valuation, timing, recording errors and actual loss.

Release pilot funding against demonstrated reduction in rework and explained exceptions.

[PAGE]

# B1 | Architecture decision
Scores range from 1 (poor fit) to 5 (strong fit). Weighted score = sum(weight x score) / 100. The scores are reasoned judgements, not benchmark results.

| Criterion | Weight | Central | Decentral | Federated | Hub/spoke |
| Offline continuity | 30 | 1 | 5 | 4 | 5 |
| Four-person team fit | 20 | 4 | 2 | 2 | 3 |
| Cost control | 20 | 4 | 2 | 2 | 4 |
| Shared quality and identity | 20 | 5 | 1 | 3 | 4 |
| Rollout across 23 stores | 10 | 3 | 2 | 3 | 4 |
| Weighted total | 100 | 3.20 | 2.70 | 2.90 | 4.10 |

Offline continuity receives the largest weight because a central dependency at checkout would interrupt revenue. Skills, cost and consistency receive equal weights because failure in any one can stop the programme. Expansion matters, but cannot outrank operating today's stores. If offline weight falls to 10 and central control rises to 40, centralised scores 4.00 and hub-and-spoke 3.90: the choice is sensitive to actual connectivity improvement.

**Choice:** Hub-and-spoke. Stores keep their operational databases and durable outboxes. A small MySQL hub holds source crosswalks, certified reference data and an analytical warehouse. The hub is central in responsibility, but not a mandatory online dependency for every sale.

A fully centralised transactional system is rejected for current connectivity. Decentralisation preserves autonomy but perpetuates conflicting meanings. Federation needs stronger domain engineering and query governance than four IT staff can support. The hub adds sync work; that is the main cost of keeping stores available.

Start with nightly signed extracts and watermarks, then improve selected paths. Keep queues on UPS-backed POS equipment; do not assume a separate always-on store server. If that equipment cannot safely host an outbox, test an encrypted removable export process with custody and daily reconciliation as a temporary exception. No routine personal USB transfers.

**Recovery targets for the pilot:** hub RPO 24 hours and RTO 8 hours; store sales continue offline. Demonstrate restore before rollout. Freshness labels must show stores whose latest data is older than 24 hours.

[PAGE]

# B1 | Conceptual model
![Conceptual ER model](diagrams/conceptual-er.png)

The conceptual model separates customers, products, stores, orders, payments, suppliers and loyalty. Crow's Foot endpoints and labels express minimum and maximum relationships. The logical diagram and executable DDL refine the same model.

A customer may have no orders; an order may be anonymous. Every order belongs to one selling store/channel location. E-commerce receives a virtual store identifier, separate from the physical fulfilment location. Orders contain one or more lines in the business process; the application must reject an empty completed order. A payment is not an order line: joining both directly would multiply amounts for split tender.

Suppliers and products form a many-to-many relationship, resolved through ProductSupplier. A customer has zero or one active loyalty account under the current design. A separate points ledger provides an auditable balance; it must not be reconstructed by overwriting the customer's identity.

## Three assumptions that can break
**One purchaser per order:** A business account may buy for multiple employees. Keep the billing/customer relationship separate from delivery recipients instead of forcing recipients into the purchaser field.

**One loyalty account per customer:** Legacy customers may already have multiple programme accounts. Keep them separate in migration until the business approves consolidation; do not delete their ledgers. Multi-programme expansion would require a programme key in the uniqueness rule.

**One standard unit per product:** Suppliers may sell rice by sack while stores sell kilograms. Model pack quantities and conversion validity separately. Changing “KGS” to “kg” is spelling standardisation, not proof that a sack contains 50 kg.

[PAGE]

# B1 | Logical model and constraints
![Logical ER model](diagrams/logical-er.png)

Primary keys identify entities; foreign keys preserve their links. Source and source_order_id are jointly unique. OrderLine uses (order_id, line_no), so an order can contain the same product more than once at different prices. Payment uses a provider-scoped reference, with a unique (provider, provider_ref) key; MySQL permits multiple null references.

The model permits negative line quantities for returns and nonnegative unit prices. A linked return can point to its original line. A missing return reference becomes a reconciliation exception rather than an excuse to discard a real financial movement. Cash can have no electronic reference; settled mobile money cannot.

CustomerCrosswalk preserves every (source, source_id) to golden-ID mapping. IDs are never inferred from a phone alone. Technical customer IDs are distinct from confidential phone/email attributes. ProductSupplier preserves supplier-specific codes; a broader source-product crosswalk follows the same pattern for POS and e-commerce.

See sql/01_core.sql for the operational DDL and sql/02_warehouse.sql for analytical structures. The implementation includes a points ledger in addition to the eight required core entities. Inserting an order header and all lines must be one application transaction; SQL foreign keys alone do not enforce the minimum-one-line business rule.

[PAGE]

# B1 | Normalisation and reporting trade-off
The actual unnormalised instructor extract was not supplied. The following is an **illustrative working example**, not a transformation claimed against that missing file.

**UNF:** Sale(order_id, date, customer_id, customer_name, store_id, store_name, {sku, product_name, qty, unit_price}, {payment_ref, payment_amount}). Repeating product and payment groups prevent reliable row identification.

**1NF:** Put each product occurrence in a row keyed by (order_id, line_no). Put each payment in its own row keyed by payment_id. Attributes are atomic within the agreed business meaning. Do not create a line-by-payment Cartesian product.

**2NF:** With the composite line key, order_date, customer_id and store_id depend on order_id alone. Move them to Order. Quantity and sale-time unit_price remain on OrderLine because they depend on the entire line key. A product's current list price is not a substitute for the actual historical sale price.

**3NF:** Customer name depends on customer_id, store name on store_id and product description on product_id. Move them into Customer, Store and Product. Supplier details live in Supplier; ProductSupplier resolves its many-to-many relationship. Payment details depend on payment_id, not customer name. These steps remove transitive dependencies and reduce update anomalies.

| Functional dependency | Final relation |
| order_id -> source, customer_id, store_id, ordered_at, currency | Order |
| (order_id, line_no) -> product_id, quantity, sale price | OrderLine |
| customer_id -> current contact attributes | Customer |
| product_id -> canonical name, category, unit | Product |
| payment_id -> order_id, provider, reference, amount, status | Payment |

**One deliberate denormalisation:** A daily store/product/currency sales summary table maintained by a scheduled job can reduce dashboard scan work. Refresh only after certified loads and compare summary totals to the fact table. The integrity cost is stale/duplicated aggregates. Publish the refresh timestamp, rebuild from atomic facts, and never allow manual edits to the summary. The core remains the source of financial truth; the summary is disposable.

Benchmark before adding the summary table. At 60,000 rows, a well-indexed fact table may already be fast enough. Complexity needs a measured benefit.

[PAGE]

# B2 | Quality measurement and cleansing
The six dimensions were measured on the complete simulated extracts. Accuracy below means agreement with generator truth, not independently verified real-world accuracy. A syntactically valid phone does not prove ownership. The fixed assessment date is 31 July 2026; timestamps were preserved during cleansing.

| Dimension | Operational definition and denominator |
| Accuracy | Correct values / checked values against generator truth: customer name, phone, email and district; product name, unit and category. Real deployment requires independent checks. |
| Completeness | Customer rows with name and at least one contact / all rows; product rows with SKU, name, unit, category / all rows. |
| Consistency | Canonical phone syntax or canonical unit / all rows. Do not confuse consistent with correct. |
| Timeliness | Updated within 90 days / rows with valid nonfuture updated_at; also publish timestamp coverage. The 90-day limit is proposed. |
| Validity | Customers with accepted phone syntax and approved district / all rows; products with permitted SKU syntax and units / all rows. |
| Uniqueness | 1 - excess candidate duplicate rows / all rows. Customer candidate key is normalised name + phone + email, all present. It estimates duplication, not verified persons. |

The scripts normalise whitespace, Uganda phone formats, explicit category aliases and approved dates. Unknown districts and conflicting product codes are reviewed. No address, date of birth, gender or phone is guessed. Only exact repeated normalised records with the same customer ID are removed automatically. Identity merges require evidence and a reversible crosswalk decision.

**Executed simulation:** Customer records fell from 5,000 to 4,060; product records from 1,200 to 1,080. Removal was limited to repeated source records. A separate simulated call-centre verification file supplied 1,177 logged attribute corrections. No missing contact was invented by the cleanser.

| Dimension (%) | Customers before / after | Products before / after |
| Accuracy (generator truth) | 92.75 / 100.00 | 94.44 / 100.00 |
| Completeness | 90.18 / 100.00 | 100.00 / 100.00 |
| Consistency | 17.84 / 100.00 | 25.00 / 100.00 |
| Timeliness | 83.32 / 83.33 | 90.00 / 90.00 |
| Validity | 84.52 / 100.00 | 12.50 / 100.00 |
| Uniqueness | 84.18 / 100.00 | 90.00 / 100.00 |

Customer accuracy checked 20,000 values before and 16,240 after; products checked 3,600 and 3,240. Only one product row in four already used a canonical unit (kg, l, g, each), so consistency starts at 25%. Validity starts at 12.5% because a row also needs an uppercase SKU, and lowercase POS codes fail that check. The customer candidate key detects 791 repeated rows (15.82%), fewer than the 940 deliberately repeated source rows, because 788 rows lack a complete name-phone-email key. This illustrates why the scenario's 23% estimate must not be substituted for a profiling result. Timeliness moved only from 83.32% to 83.33% because the denominator changed when repeats were removed: cleaning a spelling must not reset a source timestamp. Full denominators, hashes, issues and corrections are in evidence/simulation/.

[PAGE]

# B2 | Validation and recurring causes
The fifteen preventive validation rules (Q01-Q15) are listed in docs/validation-rules.csv. They cover contacts, dates, district codes, units, product identity, foreign keys, payment references, quantities and duplicate events, with a named business owner for each.

Monitor nightly: unresolved product mappings >0 block certification; unmatched electronic settlements >0 alert Finance; missing contacts >2% warn the customer owner; source freshness >24 hours warns COO; reconciliation amount mismatch other than documented rounding blocks the affected source. Thresholds are proposals to calibrate with the baseline, not measured service levels.

An invalid phone may come from a cashier's format habit; a missing contact may reflect a customer's legitimate refusal. These require different responses. Measure optional-field coverage separately so a quality target does not pressure staff to invent personal information.

[PAGE]

# B2 | Investigating the 8.4% stock variance
![Stock variance fishbone](diagrams/fishbone.png)

The fishbone distinguishes point-of-entry errors (P) from systemic causes (S). All branches are hypotheses. The reported 8.4% is not a causal diagnosis, and its denominator is unspecified.

First agree whether variance means absolute unit difference, signed unit difference or value difference. Use a blind physical count and freeze or timestamp stock movements during counting. Reconcile opening stock + receipts + transfers in - transfers out - sales + returns - write-offs to closing stock by store and product.

Test pack-size errors against purchase orders and receiving records; test timing against offline queue age; test transfer mismatches by paired dispatch/receipt IDs; test returns against original sales and restocking status. Review adjustments and repeated overrides separately from ordinary sales.

Sample fast-moving items in three pilot stores, including one with prolonged outages. A second independent count checks measurement error. Compare matched periods before and after each intervention. If variance falls only when the snapshot cutoff changes, the initial problem may have been timing rather than physical loss.

**Accountability:** Store managers investigate entry defects; Procurement settles units; Finance validates valuation; IT measures missing/late messages; the COO owns the final explanation. Loss prevention investigates theft only when the evidence supports it. Do not accuse staff based on a dashboard residual.

[PAGE]

# B3 | Customer master data design
**Style:** Begin with consolidation, then introduce controlled coexistence after the pilot. Consolidation gives a trusted hub view without interrupting stores. Coexistence later returns approved corrections and mappings to POS, e-commerce, loyalty and CRM. Registry-only leaves too much inconsistent data in daily use; fully centralised MDM would make sign-up depend on connectivity.

| Golden attribute | Survivorship and business reason |
| golden_customer_id | Hub-issued immutable ID; never a phone number. |
| name | Latest customer-verified value; retain source and verification time. Recency alone does not prove accuracy. |
| phone | Latest ownership-verified contact; retain effective dates and change history. Shared or recycled numbers cannot identify a person alone. |
| email | Latest customer-verified address; unverified sources cannot overwrite verified data. |
| address/district | Latest confirmed delivery/contact address for its stated purpose; preserve previous values only while justified. |
| preferences/consent | Purpose-specific event history; withdrawal takes precedence over stale affirmative flags. No majority vote across systems. |
| source links | Preserve all source IDs and merge/unmerge decisions with reviewer and evidence. |

**Matching:** Deterministic source links require an established crosswalk; verified programme identifiers can support identity after conflict checks. A heuristic weighted score gives phone 40, email 25, name similarity 25 and district 10. Missing values contribute zero. Scores 70-94 enter review; lower scores remain separate. A score >=95 is only eligible for auto-merge after independent verified identifiers agree, no conflict exists and a labelled validation set demonstrates acceptable precision. Auto-merge is disabled in this implementation. These are heuristic scores, not calibrated probabilities.

Evaluate a stratified labelled set, record precision/recall and the cost of each false merge, and check performance across naming conventions, shared phones and language groups. A false merge can expose purchases and transfer loyalty value, so initial policy favours missed matches over harmful merges.

Customers may optionally confirm household membership for a defined service. Do not infer households from surname, phone or district. Product hierarchy is category -> subcategory -> product, with versioned membership. The customer owner approves new attributes; the DPO reviews purpose; unresolved disputes go to the COO. Every merge must be reversible without losing the points ledger.

[PAGE]

# B3 | Master-data integration flows
![MDM integration flows](diagrams/mdm-flows.png)

The hub accepts source events and returns reviewed golden-ID mappings, attribute corrections and consent changes. POS, e-commerce, loyalty and CRM retain their source IDs. Each message carries event ID, origin and mapping version; acknowledgements allow retry without repeated business effects. The diagram shows the proposed coexistence stage after consolidation is stable.

Local sign-ups remain provisional during outages. The source record is linked only after matching and stewardship review. Disputed merges can be reversed using the decision ledger, while loyalty transactions retain their original references.

| Master hierarchy | Rule |
| Customer -> household | Optional, customer-confirmed relationship with purpose and effective dates; never inferred from a shared phone. |
| Category -> subcategory -> product | Procurement-approved membership with history; pack size is a separate attribute. |

[PAGE]

# B3 / B4 | Integration and warehouse
![Integration and warehouse](diagrams/warehouse.png)

Five source families feed the design: store POS, e-commerce, loyalty app, CRM and Odoo inventory. Mobile money settlement files are an additional reconciliation feed, not a substitute for sales. Supplier files support product/supplier enrichment. HR is excluded from retail analytics by default.

**Fact grain:** FactSales is one source order line; FactPayment is one provider event; FactInventorySnapshot is one product/store/time observation. Do not join payment events to order lines before separately aggregating each to order level. DimDate and DimCustomer are shared; DimProduct and DimStore preserve Type 2 history. Loyalty events should become a separate points fact when ledger data arrives; CRM enriches consent-aware attributes, not invented transactions.

The store manager's “quick record” remains possible offline: the POS creates a source-scoped UUID and an outbox event. The customer may transact anonymously. Loyalty accrual can be provisional, but redemption requiring current balance waits for verification or an explicitly capped exception. That limit protects customers from double spending without blocking a cash sale.

After reconnection, the hub acknowledges accepted event IDs and returns mapping versions. The store keeps unacknowledged records and retries. Approved changes carry a version and origin to avoid update loops. Consent withdrawals take priority; queued marketing is checked against the current suppression list before release. Explain the new process as protection for checkout staff, and measure added entry time during the pilot.

**Source extraction:** POS uses local incremental manifests plus durable queue; the existing PostgreSQL e-commerce source uses watermark extracts initially; loyalty/CRM use paginated APIs with checkpoint and backoff; Odoo uses approved incremental exports/API and stock snapshots; settlement CSVs carry provider/date/batch IDs and control totals. Schema changes stop only the affected source, not all stores.

[PAGE]

# B4 | ETL workflow and failure handling
![ETL workflow](diagrams/etl.png)

Each batch records source, schema version, extract time, event-time range, count, amount totals and SHA-256. Load into restricted immutable intake, validate the contract, standardise explicit formats, resolve product/customer crosswalks, apply dimensions through their own controlled transactions, then load facts in a separate transaction. Mark the source watermark complete only after reconciliation and commit.

Product and store history use nonoverlapping [valid_from, valid_to) periods. A replay with unchanged attributes creates no new row. Fact lookups use event time, not load time. Late facts can use existing historical versions. A late dimension change that rewrites an earlier period requires a controlled interval rebuild and affected-fact rekey; the current SQL rejects it explicitly instead of silently corrupting history.

| Criterion | ETL now | ELT after controlled cloud migration |
| Latency | Nightly/micro-batch; enough for Board reporting | Flexible warehouse transforms; not inherently real-time |
| Cost | Small controlled compute and narrow extracts | Storage/compute can rise through repeated scans |
| Scale | Adequate for supplied sample and pilot | Easier elastic transformations with skilled operations |
| Complexity | Visible scripts and straightforward support | More warehouse governance, permissions and cost monitoring |
| SRG fit | Preferred: validate/mask before certified load | Pilot only after raw-zone controls and usage caps |

**Executed broken-job simulation:** Because no instructor log was supplied, a labelled replacement log reproduces three failures: a POS day-first date rejected by an ISO parser, a lowercase SKU missing its dimension match, and a duplicate-key retry. Source-specific date parsing, canonical SKU mapping and idempotent event keys resolve them. The diagnosis script reproduces each failure and tests its correction; evidence/simulation/etl_diagnosis.txt records the run. MySQL loaded all 60,000 sales twice and retained exactly 60,000 facts. Currency totals matched the independent Python totals. The footfall fixture contains 847 events: 840 unique and seven replays. One event in nine is an exit (count_delta -1). The fixture demonstrates deduplication and occupancy arithmetic, not a measured store attendance rate.

[PAGE]

# B4 | Real-time where it earns its keep
![Selective streaming architecture](diagrams/streaming.png)

A footfall event measures entry/exit or a count. It cannot by itself establish live stock or mobile money fraud. Stock needs sales, returns, receipts and transfers; fraud needs provider events, amounts, references and settlement state. The generated sensor sample implements the proposed contract below; it is not an observed store feed.

**Contract:** event_id, store_id, device_id, event_time_utc, ingest_time_utc, count_delta, schema_version and sequence. No face, phone or persistent shopper identifier. At the edge, persist before acknowledgement. A lightweight broker accepts at-least-once messages, with consumer deduplication by source/event_id, bounded retry, dead-letter queue and replay retention.

**Footfall:** aggregate five-minute windows, allow ten minutes for late events, then mark later corrections visibly. Monitor device restart and clock drift; negative occupancy is an exception. Deliver aggregate traffic and conversion context to store operations. Turnstile counts may include employees or repeat entries, so the ratio is an operational proxy, not a precise customer conversion rate.

**Live stock:** use stock movement events and local quantity checks. Refresh a pilot operational view every one to five minutes while connected; display last-seen time and suppress automatic transfer advice when stale. HQ stock is eventually consistent during outages. Reconcile daily against a signed inventory snapshot.

**Mobile money:** receive authenticated provider events; flag repeated provider references, reversals after goods release and unusual velocity within a short window. Correlate with orders and settlement. Alerts go to a human reviewer; do not automatically accuse or block a customer on an uncalibrated rule. During network loss, use payment-provider confirmation policy rather than pretending the hub is current.

Nightly processing remains suitable for Board reports, customer cohorts and supplier summaries. Pilot streaming in two stores only after batch reconciliation is stable. Continue only if reduced stock-out cost or confirmed fraud loss exceeds support and connectivity costs. The programme budget cannot fund real-time replication of everything.

[PAGE]

# C1 | Metadata, lineage and change control
![Monthly active customer lineage](diagrams/lineage.png)

**Monthly active customer (MAC):** distinct resolved customer keys with at least one positive-quantity purchase line in the selected calendar month, based on business event date in Africa/Kampala. Anonymous purchases and unresolved identities are excluded and counted separately. Returns alone do not make a customer active. A fully returned purchase still counts under this definition; Finance may request a separate retained-purchase measure rather than silently redefining MAC.

Every dictionary entry has business meaning, type, source, transformation, owner, refresh, quality rule and classification. The dictionary (docs/data-dictionary.csv) contains more than 25 elements. Tags use domain:customer/product/sales/inventory/payments; sensitivity:internal/confidential/restricted; quality:provisional/certified/quarantined. A tag does not itself enforce access; SQL and application permissions must implement it.

**Address change impact:** Splitting free-text address into country, district_code and delivery_detail changes POS forms, e-commerce checkout, source adapters, MDM survivorship, delivery labels, CRM filters, rights exports and deletion searches. District sales reports can break if code/label mappings change. MAC should not change unless address was wrongly used as an identity key. Introduce a versioned contract, dual-read during migration, backfill only verified values, compare outputs and retire the old field after all consumers sign off.

| Tool | Fit and operating cost judgement |
| Apache Atlas | Supports classifications, metadata and lineage APIs [S11]. No licence fee does not mean no cost: self-hosting and connector work exceed current team capacity. Defer. |
| Microsoft Purview | Managed discovery and governance reduce some platform administration; metered assets/quality processing require a usage estimate [S12]. Prefer a capped pilot if SRG adopts Azure. |

Use the versioned CSV dictionary now. Reserve at most UGX 6M of the tool budget for a Purview pilot; this is a cap, not a price quote. Do not migrate until a pilot demonstrates useful lineage for SRG's actual sources within that cap. The customer/procurement/finance stewards update meanings; IT updates technical lineage in the same change request as code. Review monthly and reject releases without metadata updates.

[PAGE]

# C2 | Security that matches the risks
The trust boundaries are checkout device -> local queue -> transfer channel -> raw hub -> warehouse -> BI export. Actors include a rushed employee, malicious insider, external attacker, vendor administrator and person finding a stolen device. Assets include identities, purchase histories, money movement, stock, staff records and credentials. An outage makes both stale information and improvised exports more likely.

**Priority controls:** encrypt managed devices and backups; minimise exports; use individual accounts and MFA for administration; isolate HR; restrict analytics to approved views; keep recoverable backups and prove restore. A central alerting platform without these basics would be premature.

The role-by-object access matrix is in docs/access-matrix.csv. Analysts receive aggregate views, customer stewards limited contact updates, ETL controlled loading privileges, and HR a separate schema; cashiers have no direct SQL access.

The MySQL scripts use GRANT/REVOKE and column-level update grants. Tests actually attempted forbidden reads and writes under the analyst role and received MySQL access-denied errors (1142/1143). A steward contact update succeeded while consent update failed. Logs appear in evidence/mysql-tests.txt. These tests validate database privileges, not the full application, endpoint or network controls. Privileged MySQL administrators can change grants and definer objects; application users must not have those privileges [S13].

**Encryption and masking:** TLS 1.2+ with certificate validation in transit; encrypted device volumes, database storage and backups at rest; managed keys separate from data and restricted recovery access. Rotate keys after compromise and test recovery. The Python masking script drops name/phone/email and HMACs the customer ID using a secret from the environment. This is pseudonymisation: district and linked transactions may still identify someone. Only reviewed aggregates with small-cell suppression may be published publicly.

No HR workbook was supplied. The labelled 52-row SRG_HR.csv simulation contains employee name, salary, bank account, national ID, health note and next-of-kin contact. Salary and bank details are restricted financial information; health notes require the strongest access controls; identifiers and contact details remain restricted personal data. The field classification is recorded in evidence/simulation/hr_classification.csv. All identifiers in this fixture are deliberately fictitious. The dashboard excludes every HR field.

[PAGE]

# C2 | DPIA: EU-facing loyalty rollout
**Controller:** SRG. **Accountable sponsor:** COO. **Assessment owner:** DPO. **Status:** Pre-launch design assessment; no approval claimed. The instructor DPIA template is absent, so this substitute records the required decisions.

**Purpose and scope:** Account enrolment, points accrual/redemption, customer support and optional personalised offers. Proposed data includes customer identity, verified contact, purchase/points events and purpose-specific choices. Payment credentials and HR data are excluded. The EU-facing rollout requires an Article 3 scope assessment; a European supplier alone does not establish GDPR territorial applicability [S4].

**Necessity and alternatives:** A basic points balance needs an account ID and ledger, not precise location, date of birth or family relationships. Offer nonpersonalised rewards and a purchase route without marketing enrolment. Avoid face recognition and cross-store tracking of identifiable sensor visitors. Use contract necessity only for genuinely necessary account operation and separate permission for optional marketing, subject to local legal review [S6].

**Risks to people:** Wrong identity merges can expose purchases and points (initial 5 x 5 =25); opaque marketing can remove meaningful choice (4 x 4 =16); overseas processors may complicate rights (4 x 4 =16); account takeover can steal rewards (4 x 4 =16); proxy-based segments may disadvantage groups (3 x 4 =12).

**Mitigations and residual targets:** Verified matches and reversible ledgers aim for 2 x 5 =10; separate plain-language choices and immediate suppression aim for 2 x 3 =6; documented processor/transfer controls aim for 2 x 4 =8; MFA for staff and risk-based account recovery aim for 2 x 4 =8; subgroup testing and human review aim for 2 x 3 =6. Residual scores are forecasts requiring tests, not a certification.

**Consultation:** Obtain feedback from customers using shared phones, store cashiers, customer service, the EU partner and privacy counsel. No consultation has yet occurred. Test notice comprehension and withdrawal in the languages customers use.

**Gate:** The DPO records unresolved issues; the COO funds remediation; the CEO accepts only documented residual business risk. Where GDPR Article 36 requires prior supervisory consultation for unmitigated high risk, launch waits. Complete processor contracts, transfer assessment, rights simulation, restore/deletion test and a false-merge review before approval. Reopen the DPIA after new profiling, biometrics, a significant breach or a material change of market.

[PAGE]

# C2 | Rewriting the Jinja response
The discovery of the theft should trigger the incident process immediately. The clock must record discovery, organisational awareness, internal escalation and external notification separately. Staff report a suspected loss to the duty number as soon as discovered; the internal target is within 15 minutes. Managers may not delay escalation to avoid blame.

**First hour:** IT revokes sessions, isolates affected endpoints, preserves logs and attempts managed remote lock/wipe where feasible. The incident lead records what was exported, when, who could access it, encryption state and whether other copies exist. Do not destroy evidence during containment. Customer service prepares a verified contact route.

**Uganda:** DPPA s23 calls for immediate notification on the specified unauthorised-access/acquisition belief; Regulation 33 provides Form 7. Do not replace this with a 72-hour rule. The DPO submits available facts promptly, records remedial steps and follows the Authority's direction on customer notification [S1,S2].

**GDPR where applicable:** Article 33 requires notification without undue delay and, where feasible, within 72 hours of awareness unless risk to people is unlikely. Supply missing details in phases and explain delay. Article 34 requires communication without undue delay when high risk exists, subject to its exceptions. Document every breach and the reasoning for any decision not to notify [S5].

The Jinja facts justify urgent assessment and notification handling; the delay already occurred and cannot be repaired by changing timestamps. Record the actual 11-day internal delay, explain it, and notify now through the proper process. Do not wait for a complete forensic report or the next Board meeting. Give affected people practical advice without claiming their records were definitely misused.

**Next 24-72 hours:** Confirm counts and categories, coordinate with payment partners where relevant, assess likely harm, preserve a chronology and assign remedial owners. Only the designated spokesperson communicates externally; that does not prevent the DPO from meeting notification duties.

**Within ten working days:** Complete a no-blame review of why the export and delay were possible, verify device compliance, and test the revised escalation route in every store. Track actions to closure and test again at month 3. Offline reporting must remain possible by phone/SMS; the incident procedure cannot depend on the unavailable store network.

[PAGE]

# C3 | Five Board questions and a BI build specification

The five questions are member inactivity, segment growth, stock transfers, payment exceptions and expansion readiness. docs/analytics-workflows.csv specifies the source, preparation, method and decision for each workflow.

**Platform:** Tableau Public. The workbook "Lukia UGX Sales Dashboard" was built in Tableau Public web authoring with Claude for Chrome. Its source is a UGX-only extract of the reconciled simulation: 59,000 of the 60,000 lines (February–July 2026). KES and RWF lines are excluded rather than converted. The repository holds the native packaged workbook (dashboard/Lukia UGX Sales Dashboard.twbx) and the full integrated CSV.

**Live dashboard:** https://public.tableau.com/app/profile/joshua.mutesasira/viz/LukiaUGXSalesDashboard/Dashboard1

Five worksheets: Headline KPIs (sales, buyers, orders, unmatched %); monthly sales lines by channel; segment bars; Top 10 Stores on the District -> Store hierarchy; and monthly active-buyer bars. Channel, Month and District quick filters are provided. Clicking a store or segment filters the whole dashboard through filter actions.

**Published-view check (3 October 2026):** The default view shows 4,054 buyers, UGX 705M, 59,000 orders and 0.55% unmatched. With District = Kampala, every panel changes: UGX 375M (375,272,800), 0.60% unmatched (UGX 2,249,500) and nine Kampala branches.

Net sales = sum(quantity x unit_price); returns remain negative. The extract matches the Python and MySQL evidence: UGX 704,629,100 net sales, UGX 3,886,000 unmatched (0.55%) and 4,054 distinct buyers. "Unmatched" means a reconciliation exception, not confirmed fraud. All records are synthetic; real data would need private BI and small-group suppression. Details: dashboard/BUILD.md.
[PAGE]

# C3 | Executive insight brief and technology choices
## Executive insight brief: simulated February–July 2026
**Growth is concentrated in two segments.** UGX monthly net sales rose from UGX 102,313,550 in February to UGX 132,126,950 in July (+29.14%), with a dip of 8.29% from April to May. Monthly distinct buyers rose from 2,726 to 3,354 (+23.04%), so most of the growth came from more buyers rather than larger baskets. The rise is uneven. Family buyers grew from 686 to 947 (+38.05%) and Loyal Plus from 680 to 952 (+40.00%). Budget (+7.34%) and Convenience (+6.63%) barely moved. The Commercial Manager should find out what drew the new Family and Loyal Plus members before moving promotional spend to them. This pattern was built into the simulation; it is not evidence of SRG growth.

**Churn sits in the slower segments.** As at 1 August, 484 of the 3,477 customers with enough observation time had made no purchase for at least 90 days (13.92%). All 484 are in Budget (242 of 868, 27.88%) or Convenience (242 of 871, 27.78%). The denominator excludes customers whose first purchase was too recent to assess. The Loyalty Manager should check identity links first, then test a consented win-back offer against a holdout group. Inactivity is a review flag, not proof that a customer has left for good.

**The payment exception queue is small but must still be cleared.** The UGX queue has 322 unmatched ecommerce and app payments, with a net value of UGX 3,886,000. Ecommerce accounts for 204 of these and the loyalty app for 118. Finance should match provider references and check settlement timing before escalating anything. KES (1 record, KES 492) and RWF (4 records, RWF 33,845) stay separate, and no exchange rate was invented. POS cash is excluded. These figures describe reconciliation gaps in the simulation, not confirmed fraud.

The 60,000-line totals reconciled exactly to MySQL: UGX 704,629,100; KES 220,563; RWF 2,345,520. Returns (1,824 lines) remain negative. The simulation supports testing these workflows; deployment decisions need real source reconciliation and owner approval.

## Emerging technology verdicts
**Azure managed stack: PILOT.** Consider Azure Database for MySQL, object storage, scheduled integration and private BI rather than an entire analytics suite. Managed services can reduce server maintenance, but cannot remove store outages or source governance. Use the cloud/integration budget cap, verified regional pricing, a transfer assessment and a restore test before procurement. Microsoft documents smaller warehouse patterns, but SRG still needs its own workload estimate [S14].

**AI-assisted data quality: PILOT for suggestions only.** Suggest category aliases or steward review candidates on masked samples. Do not let a model invent contact details, approve consent or merge identities. Compare precision and review minutes against deterministic rules. Stop if false-merge risk, data-transfer requirements or supervision costs exceed benefit.

**Maturity:** With no instructor framework supplied, use an explicit provisional five-level rubric: ad hoc, repeatable, defined, measured, optimised. SRG appears ad hoc from the brief. Reach repeatable controls by month 6, defined ownership and contracts by month 12, measured service levels by months 18-24. Do not promise predictive maturity before trustworthy histories exist.

**Visual critique (deleted charts):** The first draft had a category pie and a dual-axis line of sales against buyers. The pie was deleted because five similar slices cannot be compared by angle: Cleaning and Personal Care differ by about 1%. The dual axis was deleted because its two scales were arbitrary and implied that buyers drive sales one-for-one. The published version shows segment sales as bars on a zero baseline and gives buyers their own chart. The store chart ranks the top ten by value rather than listing all 23 in geographic order, so the leaders are easy to find. The cost is that the weakest branches are hidden, so a bottom-ten view is a sensible addition. Missing periods would appear as gaps, not zeros.

[PAGE]

# D1 | Funded 18-month roadmap
All amounts are UGX millions. Existing staff salaries remain in the operating budget; protected time has an opportunity cost disclosed below. New specialist support, licences, cloud and training are included here. Obtain quotations including tax and exchange-rate exposure before committing funds.

| Cost line | Months 1-12 | Months 13-18 | Total |
| Fixed-term engineering support + handover | 96 | 36 | 132 |
| Training and operational backfill | 24 | 12 | 36 |
| Hub/cloud hosting and backup | 36 | 18 | 54 |
| Managed endpoint security and MFA rollout | 36 | 12 | 48 |
| Connectivity and selected UPS support | 24 | 12 | 36 |
| BI and catalog pilot licences | 18 | 9 | 27 |
| Privacy advice, audit and incident exercises | 24 | 9 | 33 |
| Integration, testing and recovery tooling | 24 | 12 | 36 |
| Stakeholder training and customer notices | 12 | 6 | 18 |
| Contingency, CFO-controlled | 36 | 6 | 42 |
| Total | 330 | 138 | 468 |

Arithmetic: 132+36+54+48+36+27+33+36+18+42 = **468M**. Headroom against a 480M programme cap = **12M**. The annual constraint is also respected: year 1 =330M; first six months of year 2 =138M. The Board must separately fund ongoing operations after month 18; the roadmap does not imply the platform becomes free.

| Phase | Funding ceiling | Milestone, dependency and release gate |
| M1-3 | 108 | Contain export risk, appoint owners, confirm source contracts and baseline. Gate: incident drill and restore test. |
| M4-6 | 102 | Three-store quality/MDM/ETL pilot; reporting rehearsal <=5 working days. Depends on approved identifiers. |
| M7-12 | 120 | Expand to 12 then 23 stores as gates pass; metadata, rights/deletion tests; audit ready by M11. |
| M13-18 | 138 | Stabilise all stores, test selective streaming and country readiness. Gate: demonstrated benefit and handover. |

Phase ceilings sum to 468M and include contingency. The CFO allocates each cost line to purchase orders and phase codes; contingency is not counted twice. Two SQL-capable staff each reserve one day weekly; the other two retain support coverage. Five business stewards reserve two hours weekly. If this allocation proves impossible, slow rollout rather than conceal unpaid workload.

[PAGE]

# D1 | How the parts reinforce one another
Governance begins with a decision that otherwise has no owner. Procurement agrees what a product means and who can change its pack size. That decision becomes an entry rule and a supplier intake check. Quality improves because the same ambiguity is no longer solved differently in fourteen spreadsheets.

Better source records make master data safer. Customer service can distinguish an established identity link from a phone that happens to match. A reversible crosswalk lets integration preserve local IDs while producing a shared view. The outbox keeps stores trading; the hub does not claim that an offline store is current.

Integration then turns those agreed identities into reconciled facts. Source totals, rejected values and replay counts explain what reached the warehouse. Product and store history preserve what was true when a sale happened. Metadata makes those choices visible to the next analyst. Without that record, a staff change could quietly turn a stable KPI into a different measure.

Security applies at every step: protected collection, managed devices, restricted raw access, pseudonymised analytical keys, approved sharing and tested deletion. It cannot be postponed until a dashboard is finished. The stolen export demonstrates that the boundary outside a database matters as much as permissions inside it.

Analytics should earn the next investment. A store transfer recommendation needs comparable units, fresh stock and a cost estimate. A retention offer needs a stable customer definition and valid marketing permission. A fraud alert needs a payment trail and human review. The Board receives measures with enough provenance to challenge them, rather than a visually polished version of the same uncertainty.

## Success gates and failure responses
By month 3, 100% of in-scope devices meet the restricted-access baseline; failures lose that access. By month 6, all pilot loads reconcile and the close rehearsal is within five working days; otherwise hold rollout. By month 12, high-priority audit actions are closed with evidence, not self-attestation. By month 18, target reporting within three working days and 95% of stores synced within 24 hours; display the exceptions.

Target stock variance below 4% by month 18 only after agreeing its denominator and validating the baseline. Target candidate duplication below 5% only alongside reviewed match precision and no unresolved harmful merges. Targets are not delivered results. At each gate, the COO may pause expansion while IT and domain owners fix the failed control.

[PAGE]

# D2 | Red-team critique, part 1
The strongest criticism of this strategy is that it assumes time SRG does not have. Four IT staff already support a retailer with 23 stores. Reserving two days of SQL capacity each week looks modest in a plan, but a failed checkout system will always take precedence. A contractor may build an elegant hub and leave the same four people with another fragile service. Training sessions do not prove that anyone can diagnose a broken incremental load during a busy weekend.

That criticism is fair. The answer is to attach payment and rollout gates to demonstrated handover, not attendance. An SRG employee should restore the database, replay a failed batch and explain the reconciliation without the contractor taking the keyboard. Until that happens, the pilot has not passed. This will slow delivery, and the Board needs to accept that slower deployment can be the cost of an operable system.

A second attack is that the budget is precise without being certain. The line items add up, but there are no vendor quotations, data-volume measurements or network tests. Cloud charges, tax, currency movements and security licences can invalidate the assumptions. Even UGX 42M contingency may be inadequate if all stores need better power and connectivity. The programme also stops at month 18 while operating bills continue.

I concede that the arithmetic establishes affordability only under the stated allowances. It does not establish a binding total cost. Procurement should quote the pilot first, including support and exit costs. The CFO should review monthly forecast-to-complete and reject commitments that consume the reserve without reducing scope. If costs rise, defer streaming and catalog automation before cutting incident response, restore testing or payment reconciliation. A cost overrun cannot be solved honestly by moving necessary work into an unnamed future budget.

The governance proposal is vulnerable to political capture. A senior manager may pressure a steward to clear a red indicator before the Board meeting. Procurement may defend an incorrect pack size because admitting the error exposes months of bad receiving. Finance may prefer a measure that agrees with its spreadsheet. A council chaired by the COO can formalise those preferences rather than challenge them.

The defence is evidence that survives disagreement: immutable intake, change history, two-person approval for material master changes and a visible exception register. The DPO must retain direct escalation outside the council. Still, technology cannot guarantee that leadership will welcome uncomfortable facts. If the Board rewards green indicators over explained exceptions, this strategy will fail despite technically correct code.

[PAGE]

# D2 | Red-team critique, part 2
Offline design introduces another weakness. A local outbox can lose data if the POS disk fails before syncing. Source clocks can be wrong. A retry can arrive after a correction, and a customer may earn points in two disconnected stores before either knows the other's balance. Calling the system eventually consistent does not make these conflicts harmless.

The plan therefore needs tested crash recovery, durable writes, event IDs, acknowledgements and explicit conflict rules. Store time should not be the only ordering authority. Reconciliation detects gaps, but detection after the event does not recover a destroyed disk. The Board must accept a bounded residual risk or fund more durable local storage. Offline redemption is restricted because the hub cannot guarantee a balance it has not seen. This is a business compromise that should be explained to customers and staff before rollout.

The matching policy can also fail while appearing careful. Requiring name, phone and email excludes many customers who share phones or do not use email. Reviewers may trust familiar naming patterns and reject unfamiliar ones. False negatives leave fragmented loyalty histories and can bias apparent segment growth. High reported precision could simply reflect testing on easy matches.

A useful validation sample must include difficult cases and record disagreements. Report match coverage alongside precision, preserve the right to correct identity, and never punish a customer for declining optional information. If the review backlog exceeds protected steward capacity, narrow the eligible matching population rather than lower the threshold to clear the queue.

Finally, the evidence package is incomplete. Without the instructor files, the quality results, broken-job diagnosis and Board findings cannot be authenticated. Synthetic fixtures are useful engineering evidence, but they cannot fill that gap. The analysis must be rerun when the files arrive. The same standard should govern the implementation: when a store is offline or a source fails reconciliation, the dashboard should say so.

My overall rebuttal is conditional. The strategy is workable if the Board protects staff time, treats exceptions as information and releases money against operational tests. If it insists on full rollout, real-time reporting and uninterrupted project speed at the same time, the red team wins. The responsible recommendation would then be a narrower programme centred on privacy controls and reconciled daily sales.

[PAGE]

# D2 | Reflective essay, part 1
**Career-path assumption:** Data/BI analysis progressing into data governance; to be confirmed by the student.

The most useful lesson from Project Savanna is that a technically correct database can still support poor decisions. It is easy to focus on tables, keys and query performance because those problems have visible answers. SRG's more difficult questions concern responsibility: who is allowed to declare that two records belong to the same person, who can approve an export, and who must act when information is lost? The architecture matters, but it cannot answer those questions on behalf of the business.

The Ugandan setting changes what a credible design looks like. The scenario includes intermittent connectivity, limited engineering capacity, mobile money and stores that rely on UPS-backed POS equipment. A design that requires every transaction to contact a central service would impose its weakest infrastructure assumption on the cashier and customer. Keeping local trading possible is therefore more than a technical preference. It recognises that digital transformation must work under the conditions in which people actually use the system.

At the same time, “offline” cannot excuse weak accountability. A provisional customer record still needs a source identifier. A sale still needs to enter a durable queue and reconcile when connectivity returns. A missing device still needs to be reported through a channel that works without the store network. The tension between availability and control is not resolved by choosing one over the other. It is managed through explicit limits, tested recovery and honest communication about what the central system knows.

Customer matching makes the ethical stakes particularly clear. A shared phone might connect a family, a small business or unrelated users at different times. Treating that phone as a person could expose purchases, misallocate points and interfere with correction or deletion requests. An apparently impressive reduction in duplicates might therefore represent harm rather than improvement. A careful analyst needs to explain both the matching rule and the mistakes it can make, including the people the rule leaves unmatched.

[PAGE]

# D2 | Reflective essay, part 2
Consent is another place where a tidy field can hide an untidy process. A Boolean named consent does not show what was explained, whether the customer had a real choice or whether permission was later withdrawn. For a loyalty programme, useful discounts should not become a reason to bundle unrelated marketing into account creation. The design keeps purpose-specific choices and treats withdrawal as an event that must reach every destination. This is more demanding than selecting the latest value, but it better represents the customer's decision.

Footfall sensors raise a different question: how much observation does the business actually need? Aggregate counts can help plan staffing and compare traffic with sales. That does not justify identifying individual visitors or tracking them between stores. Starting with anonymous counts is a practical way to limit surveillance while testing whether the proposed benefit exists. Even aggregate conversion ratios need care because staff movements and repeat visits can distort the denominator. A useful chart should make that uncertainty visible rather than imply precision it cannot support.

The quality work also changes how I would describe evidence in a professional setting. Validity, consistency and accuracy are different claims. A phone can have the right format and still belong to the wrong customer. A district can be spelled consistently and still be incorrect. Where independently verified records are unavailable, reporting accuracy as unknown is more responsible than using a convenient proxy without explanation. Likewise, synthetic test results can show that a function handles returns or rejects ambiguous dates, but they cannot establish the condition of SRG's real records.

The same discipline applies to AI. An AI tool can help draft a rule, compare options or identify a candidate typo, but it can also produce a confident explanation without adequate evidence. The appropriate response is not to hide assistance. It is to disclose it, verify the sources, execute the code and retain enough detail to explain the result. For this assignment, the absence of supplied datasets led to a disclosed simulation with reproducible inputs and checked outputs. Those results demonstrate the method; they do not establish SRG performance. Claiming completed fieldwork would undermine the very governance principles the portfolio recommends.

[PAGE]

# D2 | Reflective essay, part 3
For a proposed career path in data and BI analysis, this project suggests that SQL skill is necessary but incomplete. I would need to become comfortable defining a measure with Finance, challenging an unsafe identity rule and explaining why an attractive dashboard is not ready for use. Moving toward data governance would require judgement about ownership, privacy, change management and the cost of controls, alongside technical competence. 

The CDMP framework offers a practical way to organise that learning. DAMA identifies Data Management Fundamentals as the common foundation, with specialist areas including Data Quality, Data Governance, Metadata, Modelling, Integration, MDM and Warehousing/BI [S8]. A sensible first step would be preparation for the Associate foundation, supported by small reproducible projects. Later specialisation in Data Quality and Data Governance would connect the technical work of checking records with the organisational work of preventing defects. Certification would be a learning target, not evidence that I already possess professional experience.

My main development priority would be explaining trade-offs with evidence. I should be able to show why a return remains negative, why a repeated event does not create another sale, and why a customer merge needs review. I should also be able to admit where the design is incomplete. The budget allowances need quotations, the risk scores need operational review, and the dashboard needs the actual datasets. That willingness to distinguish a proposal from a result is part of professional credibility.

Ultimately, successful transformation at SRG would look ordinary: staff know where to report a loss, Finance can trace a total, a customer can correct a record, and a store continues trading through an outage. Those outcomes are less dramatic than a promise of real-time intelligence everywhere, but they are easier to defend and more useful to the people who rely on the data.

[PAGE]

# References
Sources checked 3 October 2026. Legal controls require review for the actual deployment, processing scope and record types. References support stated principles; budget figures and proposed thresholds are SRG planning judgements.

[S1] Parliament of Uganda. Data Protection and Privacy Act, 2019. Sections cited in the compliance register. https://bills.parliament.ug/attachments/Data%20Protection%20and%20Privacy%20Act%202019.pdf

[S2] PDPO. Data Protection and Privacy Regulations, 2021. Registration and breach notification, including regulation 33. https://pdpo.go.ug/media/2022/03/Data_Protection_and_Privacy_Regulations-2021.pdf

[S3] PDPO. Registration Classification and Guidance Notes. Renewal and annual reporting. https://pdpo.go.ug/media/2022/01/20102021105143-Registration_Classification_and_Guidance_Notes.pdf

[S4] European Data Protection Board. Guidelines 3/2018 on territorial scope of GDPR, final version. https://www.edpb.europa.eu/documents/guideline/guidelines-32018-on-the-territorial-scope-of-the-gdpr-article-3-version-adopted_en

[S5] EDPB. Data breaches: small business guide; Guidelines 9/2022. https://www.edpb.europa.eu/sme/assess-the-risks/data-breaches_en

[S6] EDPB. Respect individuals' rights; GDPR Article 6 legal-basis guidance. https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en

[S7] EDPB. Standard contractual clauses. https://www.edpb.europa.eu/topics/international-transfers-and-international-cooperation/standard-contractual-clauses_en

[S8] DAMA International. DAMA-DMBOK and CDMP examination framework. https://dama.org/learning-resources/dama-data-management-body-of-knowledge-dmbok/ ; https://dama.org/certification/exam-information-and-pricing/

[S9] UK ICO. Annual report 2020/21, regulatory action, p30. https://ico.org.uk/media2/migrated/2620166/hc-354-information-commissioners-ara-2020-21.pdf

[S10] California Department of Justice. CCPA overview and rights. https://oag.ca.gov/privacy/ccpa

[S11] Apache Atlas. Features: classifications, lineage and metadata APIs. https://atlas.apache.org/

[S12] Microsoft Learn. Data governance billing in Microsoft Purview. https://learn.microsoft.com/purview/ms-purview-dg-pricing-concepts

[S13] MySQL 8.4 Reference Manual. Using Roles and Stored Object Access Control. https://dev.mysql.com/doc/refman/8.4/en/roles.html ; https://dev.mysql.com/doc/refman/8.4/en/stored-objects-security.html

[S14] Microsoft Learn. Modern data warehouses for small/medium businesses. https://learn.microsoft.com/en-us/azure/architecture/example-scenario/data/small-medium-data-warehouse

Primary assignment source: ENTERPRISE DATA MANAGEMENT.pdf, supplied twelve-page brief. No instructor datasets or interview transcripts were available when this edition was produced. Supporting registers (assumptions, RACI, risk, decision log, data dictionary, compliance, validation and access) are in the repository docs/ folder: https://github.com/Joshmute/lukia-edm-repo

**AI assistance declaration:** OpenAI Codex and Anthropic Claude (Claude Code and Claude for Chrome) assisted with research, drafting, code, simulation data, diagrams, dashboard construction and test execution. All outputs were executed and checked.

