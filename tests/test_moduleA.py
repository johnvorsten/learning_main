"""Test calling differnet commands to demonstrate python imports"""
#%%
# Python imports
import sys, os
import unittest
import subprocess

# Third party imports

# Local imports

# Declarations
TEST_DIRECTORY = os.getcwd() # /learning_main/
#%%

class moduleATest(unittest.TestCase):
    """Tests for modeulA.py"""
    def setUp(self):
        """Init"""
        # Reset current working directory
        os.chdir(TEST_DIRECTORY)
        return None
    
    def test_moduleA_import_without_package(self):
        """Attempt to import moduleA without importing through a package
        (relative import error)"""
        directory = os.path.join(TEST_DIRECTORY, 'src', 'packageA')
        os.chdir(directory) # /learning_main/src/packageA
        with self.assertRaises(ImportError):
            import moduleA # Relative imports in moduleA result in ImportError

        return None
    
    def test_moduleA_call(self):
        """Call packageA.moduleA thorugh shell as main module"""
        # At learning_main/ depending on how tests are called
        directory = os.path.join(TEST_DIRECTORY, 'src')
        os.chdir(directory)
        args = ['python', '-m', 'packageA.moduleA']
        completed = subprocess.run(args, cwd=dir, capture_output=True, check=False)
        # Process should complete with 0 return code
        self.assertEqual(completed.returncode, 0)

        return None

    def test_moduleA_call_without_package(self):
        """Call moduleA as main module through shell (expected return code of 1)"""
        # At learning_main/ depending on how tests are called
        directory = os.path.join(TEST_DIRECTORY, 'src', 'packageA')
        os.chdir(directory)
        args = ['python', '-m', 'moduleA']
        completed = subprocess.run(args, cwd=dir, capture_output=True, check=False)
        # Process should complete with 1 return code
        self.assertEqual(completed.returncode, 1)
        self.assertTrue('ImportError' in str(completed.stderr))

        return None
    
    def test_packageA_call(self):
        """Call packageA as main module through shell (execpted success)"""
        # At learning_main/ depending on how tests are called
        directory = os.path.join(TEST_DIRECTORY, 'src')
        os.chdir(directory)
        args = ['python', '-m', 'packageA']
        completed = subprocess.run(args, cwd=dir, capture_output=True, check=False)
        # Process should complete with 0 return code
        self.assertEqual(completed.returncode, 0)
        return None

if __name__ == '__main__':
    unittest.main()
# %%
