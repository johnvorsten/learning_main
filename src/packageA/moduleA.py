"""
Print module name, file name, and sys.modules when this module
is run as __main__, imported, or part of a package
"""

# Python imports
import sys

# Third party imports

# Local imports
from .moduleB import print_from_moduleB

# Declarations

#%%

def main(name:str) -> int:
    """Print the module name (maybe it is __main__)"""
    print(f"Hello world from module name {name} function main()")
    return 0

if __name__ == '__main__':
    print("(probably executing directly) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])
    raise SystemExit(main(__name__))

elif __name__ == 'moduleA':
    print("(probably importing) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])

elif __name__ == "packageA.moduleA":
    print("(importing as module within package) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])
