# Project Savanna

Enterprise Data Management individual capstone for Savanna Retail Group. **DBMS: MySQL 8.4 LTS.**

KAUDHA LUKIA · 2025-08-40008

[Portfolio PDF](output/pdf/kaudha-lukia-edm-portfolio.pdf) · [Editable portfolio](docs/portfolio.md)

## Assignment artifacts

| Requirement | Files |
|---|---|
| A1-A2: diagnostic, governance, policies and compliance | `docs/portfolio.md` |
| B1: ER models and normalisation | `diagrams/`, `sql/01_core.sql`, portfolio B1 |
| B2: profiling, cleansing and validation | `src/savanna/quality.py`, `pipeline.py`, `evidence/simulation/` |
| B3: MDM and integration flows | Portfolio B3, `diagrams/mdm-flows.drawio` |
| B4: ETL, warehouse and history | `src/savanna/etl.py`, `sales_cli.py`, `sql/02*`, `03*`, `07*` |
| C1: metadata dictionary and lineage | `docs/data-dictionary.csv`, `diagrams/lineage.drawio` |
| C2: security, DPIA and masking | Portfolio C2, `sql/04_rbac.sql`, `src/savanna/masking.py` |
| C3: BI workflow and technology evaluation | Portfolio C3, `dashboard/BUILD.md`, `sql/06_board_queries.sql` |
| D1-D2: roadmap, decisions, red team and reflection | Portfolio D1-D2; `docs/decision-log.csv` |
| Required registers | `docs/assumptions.csv`, `raci.csv`, `risk-register.csv` |
| Execution evidence | `evidence/unit-tests.txt`, `mysql-tests.txt`, `evidence/simulation/` |

## Run

Python 3.11+ is sufficient for the transformation scripts. MySQL integration tests use Docker and the official MySQL 8.4 image in a disposable container with no network or exposed ports. The test script also uses `rg`.

```sh
make test
make demo
make mysql-test
```

For instructor data, approve the mappings in [input contracts](docs/input-contracts.md), replace the demonstration reference lists, and run:

```sh
PYTHONPATH=src python3 -m savanna.pipeline \
  --input data/raw --output data/processed --as-of 2026-09-29
```

SQL files 01-04 install the design into a fresh MySQL instance. Files 05 and 08 are synthetic test fixtures. SCD2 procedures commit their own transactions and must precede the fact transaction. Direct ETL writes to history dimensions are denied. Late history requires a controlled rebuild. Test accounts are confined to the disposable instance.

Rebuild the PDF using `requirements-docs.txt`, then `make pdf PYTHON=.venv/bin/python`.

## Data and executed results

Only the assignment PDF was supplied. `data/simulation/` contains explicitly generated replacement inputs (seed 40008, February–July 2026), not instructor datasets or real SRG records. The simulation has 5,000 customer records, 1,200 products and 60,000 sales. Cleansing produces 4,060 customer records and 1,080 products. MySQL retains exactly 60,000 facts after two identical loads; three currency totals reconcile independently.

```sh
python3 scripts/generate_simulation.py
PYTHONPATH=src python3 scripts/analyse_simulation.py
PYTHONPATH=src python3 scripts/diagnose_simulated_etl.py
./scripts/run_simulation_mysql.sh
```

Full measures and denominators: `evidence/simulation/before_after.csv`, `results.json`, `mysql-run.txt`. The HR CSV and ETL log are labelled simulations. The [published Tableau dashboard](https://public.tableau.com/app/profile/joshua.mutesasira/viz/LukiaUGXSalesDashboard/Dashboard1) has five views (headline KPIs, channel trend, segment bars, top-10 stores with District -> Store hierarchy, monthly active buyers), quick filters and dashboard filter actions. The native workbook is `dashboard/Lukia UGX Sales Dashboard.twbx`; checks are in `dashboard/BUILD.md`.

AI assistance: OpenAI Codex and Anthropic Claude (Claude Code and Claude for Chrome) assisted with research, drafting, code, simulation data, diagrams, dashboard construction and test execution, as declared in the portfolio and required by the assignment.
