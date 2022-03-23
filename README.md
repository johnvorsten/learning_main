## Build instructions

## What does the -m switch do?
From the [docs](https://docs.python.org/3/using/cmdline.html#cmdoption-m): Search sys.path for the named module and execute its contents as the __main__ module.

## Best documentation reference
(this documentation)[https://docs.python.org/3/tutorial/modules.html#tut-packages]

## Learning instructions
Clone the project
Change into the cloned directory `cd learning_main`
Navigate to source directory `cd ./src`
Import moduleA.py (as a package through __init__.py) with `python -c "import packageA.moduleA"`
Navigate to package directory `cd ./packageA`
Import moduleA.py with (as a file individually) `python -c "import moduleA"`

Change into root directory `cd ../..`
Execute moduleA.py (standalone) with `python ./src/packageA/moduleA.py`
Change into src directory `cd src`. This is required because src is not a python package. It is not possible to execute `python -m src/packageA/moduleA` or `python -m ./src/packageA/moduleA` or `python -m ./src/packageA/moduleA.py`
Execute moduleA.py (as a package module) with `python -m packageA.moduleA`

Execute the package (entry through__main__.py) with `python -m packageA` (the -m switch is required to make __main__.py run as a package module)
Execute __main__.py directly with `python __main__.py`
Execute the __main__.py directly with `python -m __main__.py`

## Issues
* With location at `./src`, and `python -m packageA`, why can I not have `from moduleA import main` in __main__.py?
The solution is to add relative imports `from .modulaA import main`, but why is this the case?
When executing a module as a package, you must use either relative or fully qualified names when importing modules within a package (see documentation)[https://docs.python.org/3/tutorial/modules.html#intra-package-references]
Note that relative imports are based on the name of the current module. Since the name of the main module is always "__main__", modules intended for use as the main module of a Python application must always use absolute imports.

* What happens if we try to run a package without the -m switch?

* Should I keep the main() function in __main__.py or somewhere else?


## Motivation

Calling a module with the -m switch:

Calling a package with the -m switch:
Package names are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute <pkg>.__main__ as the main module. This behaviour is deliberately similar to the handling of directories and zipfiles that are passed to the interpreter as the script argument.