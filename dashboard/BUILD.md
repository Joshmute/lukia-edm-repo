# Published Tableau dashboard

[Lukia UGX Sales Dashboard](https://public.tableau.com/app/profile/joshua.mutesasira/viz/LukiaUGXSalesDashboard/Dashboard1)

Built in Tableau Public web authoring with Claude for Chrome, then published. All data is simulated (seed 40008, February–July 2026); only the assignment PDF was supplied.

## Files

- `Lukia UGX Sales Dashboard.twbx`: the native packaged workbook. It contains the TWB, a Hyper extract and `lukia_ugx_dashboard_slim.csv`, which holds the 59,000 UGX lines and 11 non-identifying fields.
- `lukia_simulated_sales.csv`: the full 60,000-line integrated output of `scripts/analyse_simulation.py`, including KES and RWF lines.
- `CLAUDE_FOR_CHROME_PROMPT.md`: the prompt used to start the build. The final workbook differs from the prompt's draft layout, and this file records what was actually published.
- `screenshots/default.png` and `screenshots/kampala-filter.png`: headless-Chrome captures of the published view on 3 October 2026.

## Workbook contents

| Worksheet | Form | Fields |
|---|---|---|
| Headline KPIs | Text table | Net Sales (UGX m) = SUM(Net Sales)/1e6; Active Buyers = COUNTD(Active Buyer); Orders = COUNTD(Order ID); Unmatched Payment % = SUM(Unmatched Payment Value)/SUM(Net Sales) |
| Net Sales by Channel | Monthly trend coloured by channel | Month (continuous), Net Sales (UGX m), Channel; Channel and Month filters |
| Net Sales by Segment | Bars | Segment, Net Sales (UGX m); filter action source |
| Top 10 Stores | Ranked bars | District / Store, Top 10 by Net Sales; District filter; filter action source |
| Active Buyers by Month | Bars | Month, COUNTD(Active Buyer) |

The datasource defines a Location drill path (District -> Store). Two dashboard filter actions apply a selected store or segment to the whole dashboard.

## Reconciliation (executed against the packaged extract)

| Check | Result |
|---|---|
| Rows | 59,000 UGX lines (60,000 less 500 KES and 500 RWF) |
| Net sales | UGX 704,629,100, matching Python and MySQL |
| Unmatched electronic payments | UGX 3,886,000, matching `evidence/simulation/results.json` |
| Distinct active buyers | 4,054 |
| Orders | 59,000 |

## Published-view checks (3 October 2026)

| Check | Observed on the public page |
|---|---|
| Default view | Active Buyers 4,054; Net Sales 705 (UGX m); Orders 59,000; Unmatched 0.55%. Monthly buyers 2,726 -> 3,354; segment bars Family 183.8, Loyal Plus 183.4, Convenience 158.5, Budget 154.9, Anonymous 24.0 (UGX m). All match the evidence. |
| District = Kampala (URL filter) | Net Sales 375 (UGX m) = 375,272,800; Unmatched 0.60% = 2,249,500 / 375,272,800; Top 10 Stores reduces to nine Kampala branches; all panels change. |
| Not separately exercised | Click-through filter actions and the hierarchy expand control were not exercised on the public page. |

## Measure definitions

Net Sales sums signed line quantity times unit price, so returns reduce sales. Active Buyer is blank for anonymous lines and for return lines. Distinct counts are not additive across months or segments. Unmatched Payment Value covers ecommerce/app lines without a provider reference; it is a reconciliation queue, not a fraud measure.
