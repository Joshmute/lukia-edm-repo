PYTHON ?= python3
export PYTHONPATH := src
.PHONY: test demo mysql-test pdf
test:
	$(PYTHON) -m unittest discover -s tests -v
demo:
	$(PYTHON) -m savanna.pipeline --input data/synthetic --output evidence/synthetic --as-of 2026-09-29
	$(PYTHON) -m savanna.sales_cli --sales data/synthetic/SRG_Sales.csv --products evidence/synthetic/products_clean.csv --customers evidence/synthetic/customers_clean.csv --output evidence/synthetic
mysql-test: demo
	./scripts/test_mysql.sh
pdf:
	$(PYTHON) scripts/build_diagrams.py
	$(PYTHON) scripts/build_portfolio.py
