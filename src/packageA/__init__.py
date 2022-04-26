"""Demonstrate importing a package"""
# Python imports
import sys

# Third party imports

# Local imports

# Declarations

#%%
if __name__ == 'packageA':
    print("(probably importing package) from file: ", __file__)
    print("Running package as name: ", __name__)
    print("Package name from sys.modules: ", sys.modules[__name__])
