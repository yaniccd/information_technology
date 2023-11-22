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
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition in Python. It is used to document the purpose, usage, and behavior of the code. Example of docstring :
```{python}
def calculate_area(radius):
    """Calculate the area of a circle.

    This function takes the radius of a circle as a parameter and
    returns the calculated area using the formula: pi * radius^2.

    Parameters:
    - radius (float): The radius of the circle.

    Returns:
    float: The calculated area of the circle.
    """
    pi = 3.14159
    area = pi * radius ** 2
    return area
```
## pytest

## pylint
`Pylint` is a static code analyser. It gives your code a score out of 10 based on the PEP 8 and other coding standards. To install and run pylint on a specific `Python` file (for example, with a file called `example_module.py`)
```
pip install pylint
pylint example_module.py
```
The output will look something like this
```
************* Module example_module.py
example_module.py:10:0: C0326: Exactly one space required around assignment
example_module.py:15:4: W0611: Unused import os
example_module.py:20:4: E0001: Invalid syntax (syntax error)
example_module.py:25:12: R1705: Unnecessary "else" after "return" (no-else-return)
example_module.py:35:4: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.28/10
```

## black
`Black` is a code format. It's a tool that automatically reformats Python code to comply with its style guide, which is known as "Blackened" style (coherent with PEP 8). It reformats the code to adhere to a consistent style while preserving the functionality and logic of the original code. To install it and run it on a specific file,
```
pip install black
black example_module.py
```
To reformat all files in a directory, type (with you directory name)
```
black directory/
```
By default, `Black` will modify the files in place. If you want to see the changes that Black would make without modifying the files, you can use the `--check` option:
```
black --check example_module.py
```