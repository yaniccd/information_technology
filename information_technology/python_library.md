# Python Library
The following is a guideline on how to build a Python library. It is meant to be as complete and as beginner friendly as possible.
It goes over the initial repository setup on Github, followed by the suggested best practice. It then discusses the first release of the Python library, its maintenance and subsequent releases. I would invite the reader to refer to the Python library [Haarpy](https://github.com/polyquantique/haarpy) for an example of an library implementation based on the following tutorial.

The technicalities of git will not be discussed here. For a git tutorial, refer to `git.md`. The best practice in terms of Python working environments are also leftout of this tutorial. For a tutorial on Python working environment best practice in *Linux*, refer to `linux.md`.

## Table of Contents
- [Github Setup](#github-setup)
- [Best Practice](#best-practice)
- [Documentation](#documentation)
- [First Release](#first-release)
- [Maintenance](#maintenance)

## Github Setup
The first step is to create a new repository on Github. Three files are automatically included in the repo : `README.md`, `LICENSE` and `.gitignore` file. The `README.md` is a markdown file that contains the overview of the repo or the library; it is displayed on the main page of the repo. The `LICENSE` file is simply a copyright file. Finally, the `.gitignore` file is useful to ignore specific types of files from a git standpoint whenever modifications are pushed to a specific branch.

The `requirements.txt` file

The `__init__.py` file

## Best Practice
Actual code files should be placed in a folder with the name of the library. That would be the *haarpy* folder in this example. The modules of the library can then be saved in this folder. A *tests* folder should also be created within this folder where a different test file shall be created for every module of the library. See for instance the `unitary.py` file saved within the *haarpy* folder and its test filed called `test_unitary.py` saved in the *tests* folder.

There are many ways to perform unit tests in Python. The most commun one is throught the *pytest* library that should be part of the developpement required libraries. The idea of the unit test is to validate the well functionning of the functions of eachmodule against known results or expected behavior. All test names shall be named `test_...` or else it will be ignored by the *pytest*. Good unitest should call every single line of the tested module, we then say that the coverage is of 100%. The tests can then be run through the terminal. For instance
```
pytest haarpy/tests/tests_unitary.py
```
will run the test of that specific test file. To run a specific test, one can do
```
pytest haarpy/tests/tests_unitary.py -k test_get_conjugacy_class
```
To other libraries are quite useful from a best practice standpoint : `black` will format the code to the PEP 8 standard, while `pylint` will analysis code statically and give it a score out of 10 with refactoring suggestions. Both should be run on modified modules before pushing to the repo. For instance,
```
black haarpy/unitary.py
pylint haarpy/unitary.py
```

## Documentation

## First release
*Pypi* link


## Maintenance
The following section discuss the maintenance of the library and the procedure to update the library by releasing a new version.


How to look up all instance of a specific string in linux??? (to update version)





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