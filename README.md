[![Tests](https://github.com/johnvorsten/learning_main/actions/workflows/python-app.yml/badge.svg)](https://github.com/johnvorsten/learning_main/actions/workflows/python-app.yml) [![Quality Status](https://github.com/johnvorsten/learning_main/actions/workflows/pylint.yml/badge.svg)](https://github.com/johnvorsten/learning_main/actions/workflows/pylint.yml) ![Coverage](https://img.shields.io/badge/Coverage-97%-green)

## Motivational questions
* Why does executing a module within a package like `python -m moduleA` or `python ./packageA/moduleA.py` cause an import error `ImportError: attempted relative import with no known parent package`
    * The solution is to add relative or fully qualified imports (`from .modulaA import main`), but why is this the case?
* Why are relative imports required when trying to execute a module  [as a script](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)? 
    * When executing a module as a package, you must use either relative or fully qualified names when importing modules within a package (see documentation)[https://docs.python.org/3/tutorial/modules.html#intra-package-references]
* What happens if we try to run a package without the -m switch?
* What happens if we try to run a module without the -m switch?
* What happens if we try to run a module without a fully qualified package path? (example: `python -m moduleA` versus `python -m packageA.moduleA`)
* Should I keep the main() function in __main__.py or somewhere else?
    * When a package name is supplied instead of a normal module, the interpreter will execute <pkg>.__main__ as the main module.

## What does the -m switch do?
The [-m switch](https://docs.python.org/3/using/cmdline.html#cmdoption-m) searches your sys.path environment variable (not your system environment variable) for the named module, then executes that module as the __main__ module.\
*sys.path* is not the same as your system *path* environment variable. The *sys.path* environment variable includes locations where python looks for importable packages.

## Documentation reference
Packaging structure: https://docs.python.org/3/tutorial/modules.html#tut-packages

Command line documentation: https://docs.python.org/3/using/cmdline.html#cmdoption-m

## Learning instructions
Example #1 - Impacts of importing modules, packages, and individual files
1. Clone the project
1. Change into the cloned directory `cd learning_main`
1. Navigate to source directory `cd ./src`
1. Import moduleA.py (as a package through __init__.py) with `python -c "import packageA.moduleA"`
1. Import moduleB.py (as a package through __init__.py) with `python -c "import packageA.moduleB"`
1. Import packageA (as a package through __init__.py) with `python -c "import packageA"`
1. Navigate to package directory `cd ./packageA`
1. Import moduleA.py with (as a file individually) `python -c "import moduleA"` (did you expect this to work?)

Example #1 output:
```bash
user@computer:~/learning_main $ cd ./src

user@computer:~/learning_main/src $ python -c "import packageA.moduleA"
(probably importing package) from file:  user@computer:~/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>
Printing something from moduleB
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  packageA.moduleB
Module name from sys.modules:  <module 'packageA.moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleA.py
Running module as module name:  packageA.moduleA
Module name from sys.modules:  <module 'packageA.moduleA' from '/home/user/learning_main/src/packageA/moduleA.py'>

user@computer:~/learning_main/src $ python -c "import packageA.moduleB" 
(probably importing package) from file:  /home/user/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>
Printing something from moduleB
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  packageA.moduleB
Module name from sys.modules:  <module 'packageA.moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>

user@computer:~/learning_main/src $ python -c "import packageA"
(probably importing package) from file:  /home/user/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>

user@computer:~/learning_main/src $ cd ./packageA

user@computer:~/learning_main/src/packageA>python -c "import moduleA"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home/user/learning_main/src/packageA/moduleA.py", line 33, in <module>
    from .moduleB import print_from_moduleB
ImportError: attempted relative import with no known parent package
```

Example #2 - Import a module not reliant on other modules within a package
1. Enter a python interpreter through your command line `python`
1. Import moduleB into your interpreter instance `import moduleB`
1. Print the __name__ variable of the imported moduleB `print(moduleB.__name__)`

Example #2 output:
```python
Python 3.7.10 [MSC v.1916 64 bit (AMD64)]
Type "help", "copyright", "credits" or "license" for more information.
>>> import moduleB
Printing something from moduleB
(probably importing) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  moduleB
Module name from sys.modules:  <module 'moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>   
>>> moduleB.__name__
'moduleB'
```

Example #3 - Using the python interpreter (without -m switch) execute an individual file, module, and package.
1. Change into root directory `cd ../..`
1. Execute moduleA.py (standalone) with `python ./src/packageA/moduleA.py` (did you expect this to work?)
1. Execute moduleB.py (standalone) with `python ./src/packageA/moduleB.py`
1. Execute packageA with `python ./src/packageA` (did you expect this to work?)
1. Change into src directory `cd src`. This is required because src is not a python package. It is not possible to execute `python -m src/packageA/moduleA` or `python -m ./src/packageA/moduleA` or `python -m ./src/packageA/moduleA.py`
1. Execute moduleA.py (as the __main__ module) with `python -m packageA.moduleA`
1. Execute moduleB.py (as the __main__ module) with `python -m packageA.moduleB`
1. Execute packageA (as the __main__ module) with `python -m packageA`
1. Change into packageA directory `cd packageA`. This will be required to demonstrate executing python files as modules outside of a package scope
1. Execute moduleA.py (as the __main__ module) with `python -m moduleA` (did you expect this to work?)
1. Execute moduleB.py (as the __main__ module) with `python -m moduleB` (Explain why this works)

Example #3 output:
```bash
user@computer:~/learning_main/src/packageA>cd ../..

user@computer:~/learning_main>python ./src/packageA/moduleA.py
Traceback (most recent call last):
  File "./src/packageA/moduleA.py", line 33, in <module>
    from .moduleB import print_from_moduleB
ImportError: attempted relative import with no known parent package

user@computer:~/learning_main>python ./src/packageA/moduleB.py 
Printing something from moduleB
(probably executing directly) this file:  ./src/packageA/moduleB.py
Running module as module name:  __main__
Module name from sys.modules:  <module '__main__' from './src/packageA/moduleB.py'>

user@computer:~/learning_main>python ./src/packageA
Traceback (most recent call last):
  File "runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "./src/packageA/__main__.py", line 9, in <module>
    from .moduleA import main # Optional
ImportError: attempted relative import with no known parent package

user@computer:~/learning_main>cd src

user@computer:~/learning_main/src $ python -m packageA.moduleA
(probably importing package) from file:  /home/user/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>
Printing something from moduleB
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  packageA.moduleB
Module name from sys.modules:  <module 'packageA.moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>
(probably executing directly) this file:  /home/user/learning_main/src/packageA/moduleA.py
Running module as module name:  __main__
Module name from sys.modules:  <module 'packageA.moduleA' from '/home/user/learning_main/src/packageA/moduleA.py'>
Hello world from module name __main__ function main()

user@computer:~/learning_main/src $ python -m packageA.moduleB
(probably importing package) from file:  /home/user/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>
Printing something from moduleB
(probably executing directly) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  __main__
Module name from sys.modules:  <module 'packageA.moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>

user@computer:~/learning_main/src $ python -m packageA
(probably importing package) from file:  /home/user/learning_main/src/packageA/__init__.py
Running package as name:  packageA
Package name from sys.modules:  <module 'packageA' from '/home/user/learning_main/src/packageA/__init__.py'>
Printing something from moduleB
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  packageA.moduleB
Module name from sys.modules:  <module 'packageA.moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>
(importing as module within package) this file:  /home/user/learning_main/src/packageA/moduleA.py
Running module as module name:  packageA.moduleA
Module name from sys.modules:  <module 'packageA.moduleA' from '/home/user/learning_main/src/packageA/moduleA.py'>
(probably executing package directly) from file:  /home/user/learning_main/src/packageA/__main__.py
Running package as name:  __main__
Package name from sys.modules:  <module 'packageA.__main__' from '/home/user/learning_main/src/packageA/__main__.py'>
Hello world from module name __main__ function main()

user@computer:~/learning_main/src $ python -m moduleA
Traceback (most recent call last):
  File "runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/user/learning_main/src/packageA/moduleA.py", line 33, in <module>
    from .moduleB import print_from_moduleB
ImportError: attempted relative import with no known parent package

user@computer:~/learning_main/src $ python -m moduleB
Printing something from moduleB
(probably executing directly) this file:  /home/user/learning_main/src/packageA/moduleB.py
Running module as module name:  __main__
Module name from sys.modules:  <module 'moduleB' from '/home/user/learning_main/src/packageA/moduleB.py'>
```

## Testing
python -m unittest tests/test_moduleA.py
coverage run -m unittest tests/test_moduleA.py
pylint -r n src/packageA

## Calling as an installed package
Install this package using `python -m build .`
Call the package once it is installed with `python -m packageA` or `python -m packageA.moduleA`
