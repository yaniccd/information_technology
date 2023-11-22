# A brief introduction to clean code in Python

## Table of Contents
- [Docstrings](#docstrings)
- [Pytest](#pytest)
- [Pylint](#pylint)
- [Black](#black)

## Best practice
Variable naming convention.
Files organisation (source code, init file, test files)

## Docstrings
A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition in Python. It is used to document the purpose, usage, and behavior of the code. Example of docstring :
```python
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
## Pytest
`Pytest` is a testing framework for Python that makes it easy to write and execute unit tests. The name of a test file always starts with 'test'. For example, let's say we want to do unit test on a `Python` file called `example_module.py` that contains a function called `funky_iterator` returning an interator. We know that the size of the iterator is supposed to be equal to the square of the first inputed argument. We also know that the sum of the elements in this interator should be equal to the second inputed argument. Then, in another file called `test_example_module.py`, we might want to have a unit tests to test both these statements. The file would then look something like this
```python
import pytest
from example_module import my_iterator

@pytest.mark.parametrize("n", range(8))
def test_iterator_size(n):
    """Test that the size of the iterator is equal to the square of the first inputed argument"""
    j = 4 #arbitrary value
    output_iterator = my_iterator(n, j)
    assert len(output_iterator) == n**2


@pytest.mark.parametrize("n", range(8))
def test_iterator_sum(n):
    """Test that the size of the iterator is equal to the square of the first inputed argument"""
    i = 5 #arbitrary value
    output_iterator = my_iterator(i, n)
    assert sum(output_iterator) == n
```
The `assert` statement is followed by a boolean variable that should be `True` if the test has passed, and `False` otherwise. In both cases, the unit tests will be done for all values of `n` in `range(8)`.

To install and run a test file,
```
pip install pytest
pytest test_example_module.py
```
If you only want to run a specific test,
```
pytest test_example_module.py -k 'test_iterator_size'
```
The following `numpy` function is really useful to test that two outputs other then scalars (matrices for example) are indentical
```python
assert np.allclose(matrix_1, matrix_2)
```

## Pylint
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

## Black
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