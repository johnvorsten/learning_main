"""
Expected output from running file
module name:
__main__
Module name from sys.modules:
<module '__main__' from 'moduleA.py'>
File name:
moduleA.py
Hello world from moduleA.main()

Expected output from importing file
module name:
moduleA
Module name from sys.modules:
<module 'moduleA' from 'C:\\Users\\Jvorsten\\PythonProjects\\learning_main\\src\\moduleA\\moduleA.py'>
File name:
C:\\Users\\Jvorsten\\PythonProjects\\learning_main\\src\\moduleA\\moduleA.py

Differences
First, the module __name__ is __main__ when run as a module, versus the module
name moduleA when imported
The full file path is displayed when importing as a module


"""

# Python imports
import sys

# Third party imports

# Local imports
from .moduleB import print_from_moduleB

# Declarations

#%%

def main(name:str) -> int:
    print("Hello world from module name {} function main()".format(name))
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
    
