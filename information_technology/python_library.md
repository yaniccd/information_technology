# Python Library
Guideline on how to create and maintain a Python library.
## Table of Contents
- [Github](#github)
- [Pypi](#pypi)
- [Documentation](#documentation)
- [Maintenance](#maintenance)


## Github
Files needed and folder structur.
```
black
pylint
pytest folder\file_name
pytest folder\file_name -k 'test_name'
```

## Pypi
Find name and see if already taken.

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
Add `docs/_build` to the *.gitignore* file.

### Host documentation on Read the Docs

## Maintenance
```
pip install haarpy -upgrade
```
From the terminal, to see which version you are working with
```
python3
import haarpy
haarpy.__version__
haarpy.about()
```