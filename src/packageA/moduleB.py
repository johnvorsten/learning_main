# Python imports
import sys

# Third party imports

# Local imports

# Declarations

#%%
def print_from_moduleB():
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

