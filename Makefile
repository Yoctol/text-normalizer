.DEFAULT_GOAL := all

.PHONY: installself
installself:
	python setup.py build_ext
	pip install -e .

.PHONY: install
install:
	pip install -U pip wheel setuptools cython
	pip install -r requirements.txt
	make installself

.PHONY: lint
lint:
	flake8

.PHONY: test
test:
	python -m unittest -v

.PHONY: all
all: test lint

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf build
	python setup_utils/remove_so_files.py
	make -C docs clean
	python setup.py clean

.PHONY: dev-test
dev-test:
	rm -rf build
	python utils/setup_utils/remove_so_files.py
	python setup.py build_ext
	pip install -e .
	make lint
	make test

.PHONY: docs
docs:
	make installself
	make -C docs
