# Python imports
import sys

# Third party imports

# Local imports
# It is required to import via relative imports, or through absolute path like packageA.moduleA
from .moduleA import main # Optional
from packageA.moduleA import main # Preferred

# Declarations

#%%

if __name__ == '__main__':
    print("(probably executing package directly) from file: ", __file__)
    print("Running package as name: ", __name__)
    print("Package name from sys.modules: ", sys.modules[__name__])

else:
    print("(probably importing) this file: ", __file__)
    print("Running module as module name: ", __name__)
    print("Module name from sys.modules: ", sys.modules[__name__])
    
raise SystemExit(main(__name__))