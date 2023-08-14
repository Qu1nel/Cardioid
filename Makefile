path := .

.DEFAULT_GOAL := help
MAKEFLAGS 	  += --silent --no-print-directory

RED			:= \\033[0;31m
GREEN		:= \\033[1;32m
YELLOW		:= \\033[1;33m
BLUE		:= \\033[0;36m
RESET		:= \\033[0m


# Main
##############################################################################


.PHONY: init
init: create-venv  ## Initialises the project (creates a virtual environment) and gives further instructions
	@echo -e "$(GREEN)Now you can activate venv with:"
	@echo -e
	@echo -e "$(BLUE)    1. source ./.venv/bin/activate"
	@echo -e
	@echo -e "$(GREEN)And install requirements:"
	@echo -e
	@echo -e "$(BLUE)    2. make install-requirements"
	@echo -e
	@echo -e "$(GREEN)And run this project with:"
	@echo -e
	@echo -e "$(BLUE)    3. make run$(RESET)"
	@echo -e


.PHONY: install-requirements
install-requirements:  ## Install all requirements from 'requirements.txt'
	@echo -e
	@echo -e "$(GREEN)Applying requirements.txt..."
	@echo -e "============================$(RESET)"
	@echo -e
	pip install -r requirements.txt
	@echo -e


.PHONY: run
run:  ## Launch app (run.py)
	python run.py


.PHONY: create-venv venv env
create-venv:  ## Create virtual enviroment for Python
	@if [ ! -d ".venv/" ]; then \
		virtualenv .venv --prompt Python-TicTacToe 1>/dev/null; \
		echo "$(GREEN)    Virtual env created!$(RESET)\n"; \
	fi


# Alias
venv: create-venv  ## Alias for 'create-venv'
env: create-venv  ## Alias for 'create-venv'


# Lint
##############################################################################


.PHONY: lint-check lint lints check
lint-check: ruff mypy pyright black  ## Complete code base check with linters and formatters


# Alias
lint: lint-check  ## Alias for 'lint-check'
lints: lint-check  ## Alias for 'lint-check'
check: lint-check  ## Alias for 'lint-check'


.PHONY: ruff
ruff:  # Use 'ruff' utilite as linter
	@echo -e
	@echo -e "$(BLUE)Applying ruff..."
	@echo -e "$(GREEN)================$(RESET)"
	@echo -e
	ruff check $(path) --fix
	@echo -e

.PHONY: mypy
mypy:  # Use 'mypy' utilite as linter
	@echo -e
	@echo -e "$(BLUE)Applying mypy..."
	@echo -e "$(GREEN)================$(RESET)"
	@echo -e
	mypy $(path)
	@echo -e

.PHONY: pyright
pyright:  ## Use 'black' utilite as linter
	@echo -e
	@echo -e "$(BLUE)Applying pyright..."
	@echo -e "$(GREEN)===================$(RESET)"
	@echo -e
	pyright $(path)
	@echo -e

.PHONY: black
black:  ## Use 'black' utilite as formatter
	@echo -e
	@echo -e "$(BLUE)Applying black..."
	@echo -e "$(GREEN)=================$(RESET)"
	@echo -e
	black $(path)
	@echo -e


# Clean cache
##############################################################################


.PHONY: clean
clean:  ## Clear linter cache (.mypy_cache .ruff_cache)
	@echo -e "$(RED)Remove:$(RESET) .mypy_cache/"
	@echo -e "$(RED)Remove:$(RESET) .ruff_cache/"
	@rm -rf .mypy_cache
	@rm -rf .ruff_cache


# Other
##############################################################################


.PHONY: help
help:  ## Show this output, i.e. help to use the commands
	grep -E '^[a-zA-Z_-]+:.*?# .*$$' Makefile | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


info-%:
	@make --dry-run --always-make $* | grep -v "info"


print-%:
	@$(info '$*'='$($*)')


.SILENT:
