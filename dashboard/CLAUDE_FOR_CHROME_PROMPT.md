# Prompt for Claude for Chrome

Before starting: sign in to Tableau Public (public.tableau.com) with **Kaudha Lukia's** account in Chrome. Keep `dashboard/lukia_simulated_sales.csv` (11 MB) ready to upload. If Claude for Chrome cannot open the file picker itself, choose the file yourself when the upload dialog appears, then tell it to continue.

Copy everything below the line into Claude for Chrome.

---

Build and publish a Tableau Public dashboard in the account that is already signed in. Use Tableau Public web authoring ("Create" -> "Web Authoring"). Work step by step, and tell me whenever you need me to select a file or confirm something.

**Data:** Upload the CSV file `lukia_simulated_sales.csv` (I will select it if needed). Check that Tableau reads these fields: Month (date), Order Date (date), District, Store, Store ID, Category, Product, Channel, Currency, Net Sales (number), Net Units (number), Order ID, Customer ID, Active Buyer, Segment, Unmatched Payment Value (number), Simulation. If Month, Net Sales or Unmatched Payment Value come in as strings, change their data types.

**Global setup:**
1. Add a data source filter, or a filter applied to all worksheets using this source: Currency = UGX only.
2. Create a hierarchy named "Location": District -> Store.

**Worksheets (name each one exactly):**
1. "Monthly Sales by Channel": MONTH(Month) on Columns (discrete), SUM(Net Sales) on Rows, Channel on Color, as stacked bars. Format the axis as UGX with thousands separators.
2. "Store Ranking": Location hierarchy on Rows (collapsed to District by default), SUM(Net Sales) on Columns, as horizontal bars sorted descending by Net Sales. Show mark labels.
3. "Active Buyers by Segment": MONTH(Month) on Columns, COUNTD(Active Buyer) on Rows, Segment on Color, as lines with markers. Filter Segment to exclude "Anonymous". Title the axis "Distinct active buyers".
4. "Category Heatmap": Category on Rows, MONTH(Month) on Columns, SUM(Net Sales) on Color and on Label, square marks (highlight table). Sort categories by total Net Sales, descending.
5. "Payment Exceptions": SUM(Unmatched Payment Value) as a single large text number (BAN), with the caption "Unmatched ecommerce/app payments, UGX — reconciliation queue, not confirmed fraud". Add Channel to Detail and show the per-channel values in the tooltip.

**Filters:** Add quick filters for Channel, District and Segment (multi-value dropdown). Set each to "Apply to Worksheets -> All Using This Data Source".

**Dashboard:** Create a dashboard named "Dashboard" at fixed size 1366 x 900. Title: "SRG Sales & Customer Health — SIMULATED data, Feb–Jul 2026 (UGX)". Layout: Payment Exceptions BAN and the three filters in a top strip; Monthly Sales by Channel and Active Buyers by Segment in the middle row; Store Ranking and Category Heatmap in the bottom row. Add a small text box: "Synthetic teaching data (seed 40008). Not actual Savanna Retail Group records. KES/RWF excluded; no FX conversion."

**Verify before publishing (report each number back to me):**
- With all filters cleared, total Net Sales = 704,629,100 and the Payment Exceptions BAN = 3,886,000.
- Store Ranking at District level: Kampala 375,272,800; Jinja 139,463,450; Mbarara 106,594,750; Gulu 83,298,100.
- Expanding Location to Store gives 23 bars, with Ntinda Branch first at 43,480,250.
- Active buyers: Family rises from 686 (Feb) to 947 (Jul); Loyal Plus from 680 to 952.
If any number differs, stop and tell me which one rather than adjusting the data.

**Publish:** Save/publish the workbook to Tableau Public as "SRG-Data-Turnaround-Kaudha-Lukia" with "Show sheets as tabs" off. Make sure the viz is public. Give me the final public URL.

**Screenshots:** On the published page take three screenshots (or tell me when to take them): (1) default view; (2) District filter set to Kampala only, where the BAN should show 2,249,500; (3) Store Ranking expanded to store level.
