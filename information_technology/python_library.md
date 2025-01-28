# Python Library
Guideline on how to create and maintain a Python library.
## Table of Contents
- [Github](#github)
- [Pypi](#pypi)
- [Documentation](#documentation)

## Documentation
### Generate documentation from docstrings
```
pip install sphinx
pip install sphinx_rtd_theme
mkdir docs
cd docs
sphinx-quickstart
sphinx-build -b html . _build
```
### Host documentation on Read the Docs