# Python imports

# Third party imports

# Local imports
from moduleA import main

# Declarations

#%%

print("module name:")
print(__name__)
print("Module name from sys.modules:")
print(sys.modules[__name__])
print("File name:")
print(__file__)
    
raise SystemExit(main(__name__))