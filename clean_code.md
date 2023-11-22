# A quick introduction to clean code in Python

## Table of Contents
- [Docstrings](#docstrings)
- [pytest](#pytest)
- [pylint](#pylint)
- [black](#black)

## Best practice
Variable naming convention.
Files organisation (source code, init file, test files)

## Docstrings

## pytest

## pylint
`Pylint` is a static code analyser. It gives your code a score out of 10 based on the PEP 8 and other coding standards. To install and run pylint on a specific `Python` file (for example, with a file called `example_module.py`)
```
pip install pylint
pylint example_module.py
```
The output will look something like this
```
************* Module example_module
example_module.py:10:0: C0326: Exactly one space required around assignment
example_module.py:15:4: W0611: Unused import os
example_module.py:20:4: E0001: Invalid syntax (syntax error)
example_module.py:25:12: R1705: Unnecessary "else" after "return" (no-else-return)
example_module.py:35:4: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.28/10
```
## black