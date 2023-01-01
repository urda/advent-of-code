########################################################################################################################
# Variables
########################################################################################################################

CLEAN_TARGETS = ./htmlcov .coverage
PYTHON_PATH = ./src

# Composite Variables

PYLINT_PATH = $(PYTHON_PATH)/main.py $(PYTHON_PATH)/advent_days $(PYTHON_PATH)/advent_utils

########################################################################################################################
# `make help` Needs to be first so it is ran when just `make` is called
########################################################################################################################

.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' ${MAKEFILE_LIST} |\
	sort -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: clean
clean: # Clean project files
	rm -rf $(CLEAN_TARGETS) && \
	find . | grep -E "(.pytest_cache|__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf && \
	:

########################################################################################################################

.PHONY: run
run: # Run the CLI App
	./src/main.py

########################################################################################################################

# Linting Tools

.PHONY: lint
lint: # Run linting
lint: flake8
lint: pycodestyle
lint: pylint

flake8:
	flake8 -v

pycodestyle:
	pycodestyle --verbose ./src/

pylint:
	pylint --output-format=text --rcfile=./.pylintrc $(PYLINT_PATH)

########################################################################################################################

.PHONY: test
test: # Run tests
	PYTHONPATH=$(PYTHON_PATH) pytest \
	--verbose \
	--cov=advent_days \
	--cov=advent_utils \
	--cov-branch \
	--cov-report=html \
	--cov-report=term-missing \
	./tests/
