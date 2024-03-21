# Python setup on Windows
The following is a guide to set up Python on Windows.

## Table of Contents
- [Python Installation](#python_installation)
- [VS Code](#vs_code)
- [Virtual Environments](#virtual_environments)

## Python Installation
To install Python, simply run the executable download on [Python Download](https://www.python.org/downloads/). Make sure to add Python to PATH variable when installing.

## VS Code
I like to work with VS Code as my IDE but there are many more. To install VS Code:
1. Download and run it from [visualStudio](https://code.visualstudio.com/).
2. Open VS Code and go to the Extensions `Ctrl`+`Shift`+`X`.
3. Download Python.
4. Download code runner.
5. Download Jupyter to work with note books.

## Virtual Environments
To create a virtual environment, in a termal, type `python -m venv VENV_PATH`. For exemple, `python -m venv myenv` would create a virtual environment called myenv hosted in a the same folder as the current projet. Type `myenv\Scripts\activate` to activate the virtual environment, or kill the terminal and open it again. At the left of the terminal, you should see the name of your environment. From the terminal, you can then use `pip` to install packages. For example `pip install numpy` to install `numpy` in the virtual environment.