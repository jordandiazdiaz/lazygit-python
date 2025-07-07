.PHONY: help install develop uninstall clean build test lint dist upload installer

help:
	@echo "Available commands:"
	@echo "  make install      - Install the package"
	@echo "  make develop      - Install in development mode"
	@echo "  make uninstall    - Uninstall the package"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make build        - Build distribution packages"
	@echo "  make test         - Run tests"
	@echo "  make lint         - Run linters"
	@echo "  make dist         - Build source and wheel distributions"
	@echo "  make upload       - Upload to PyPI"
	@echo "  make installer    - Build platform-specific installer"

install:
	pip install .

develop:
	pip install -e .

uninstall:
	pip uninstall -y lazygit-python

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.spec" -delete
	rm -rf debian/
	rm -f *.dmg *.AppImage *.deb *.rpm

build: clean
	python -m build

test:
	python -m pytest tests/

lint:
	python -m flake8 lazygit/
	python -m black --check lazygit/
	python -m mypy lazygit/

dist: clean
	python -m pip install --upgrade build
	python -m build

upload: dist
	python -m pip install --upgrade twine
	python -m twine upload dist/*

installer:
	python build_installers.py