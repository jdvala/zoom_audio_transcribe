.PHONY: clean
## Remove unneeded files
clean:
	find src -type d -name "__pycache__" -exec rm -rf {} + > /dev/null 2>&1
	find src -type f -name "*.pyc" -exec rm -rf {} + > /dev/null 2>&1

	find tests -type d -name "__pycache__" -exec rm -rf {} + > /dev/null 2>&1
	find tests -type f -name "*.pyc" -exec rm -rf {} + > /dev/null 2>&1

.PHONY: lint
## Run linting
lint:
	python -m mypy src/
	pre-commit run --all-files

.PHONY: test
## Run pytest
test:
	python -m pytest tests/

.PHONY: install
## Install this repo in develop mode
install:
	pip install -r requirements/ci.txt -r requirements/docs.txt
	pre-commit install

.PHONY: docs-build
## Build sphinx docs using projects README and module structure (sphinx-apidoc)
docs-build:
	cd docs && make docs

.PHONY: docs-show
## Open docs main page with default viewer (Linux || Mac)
docs-show:
	xdg-open docs/_build/html/index.html || open docs/_build/html/index.html

.PHONY: help
## Print Makefile documentation
help:
	@perl -0 -nle 'printf("%-25s - %s\n", "$$2", "$$1") while m/^##\s*([^\r\n]+)\n^([\w-]+):[^=]/gm' $(MAKEFILE_LIST) | sort
.DEFAULT_GOAL := help

