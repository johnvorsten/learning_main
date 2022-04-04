## Build instructions

## What does the -m switch do?
From the [docs](https://docs.python.org/3/using/cmdline.html#cmdoption-m): Search sys.path for the named module and execute its contents as the __main__ module.

## Best documentation reference
(this documentation)[https://docs.python.org/3/tutorial/modules.html#tut-packages]

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
Package names are also permitted. When a package name is supplied instead of a normal module, the interpreter will execute <pkg>.__main__ as the main module. This behavior is deliberately similar to the handling of directories and zip-files that are passed to the interpreter as the script argument.