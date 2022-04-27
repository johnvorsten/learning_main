"""Module is part of a package but does not rely on other modules within the package
This script/module can be executed stand-alone
Execute moduleB.py (standalone) with `python ./src/packageA/moduleB.py`
Execute moduleB.py (as the __main__ module) with `python -m packageA.moduleB`
While inside the packageA directory, execute moduleB.py
    (as the __main__ module) with `python -m moduleB` (Explain why this works)
"""
# Python imports
import sys

# Third party imports

# Local imports

# Declarations

#%%
def print_from_moduleB():
    """Let the user know we are printing from moduleB"""
    print("Printing something from moduleB")
    return None

if __name__ == '__main__':
    print_from_moduleB()
    print("(probably executing directly) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])
    raise SystemExit(0)

elif __name__ == 'moduleB':
    print_from_moduleB()
    print("(probably importing) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])

elif __name__ == "packageA.moduleB":
    print_from_moduleB()
    print("(importing as module within package) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])
