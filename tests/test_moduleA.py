"""Test calling differnet commands to demonstrate python imports"""
#%%
# Python imports
import sys, os
import unittest
import subprocess

# Third party imports

# Local imports

# Declarations
TEST_DIRECTORY = os.getcwd()
#%%

class moduleATest(unittest.TestCase):
    
    def setUp(self):
        # Reset current working directory
        os.chdir(TEST_DIRECTORY)
        return None
    
    def test_moduleA_import_without_package(self):
        dir = os.path.join(TEST_DIRECTORY, 'src', 'packageA')
        os.chdir(dir) # /learning_main/src/packageA
        with self.assertRaises(ImportError):
            import moduleA # Relative imports in moduleA result in ImportError

        return None
    
    def test_moduleA_call(self):
        # At learning_main/ depending on how tests are called
        dir = os.path.join(TEST_DIRECTORY, 'src')
        os.chdir(dir)
        args = ['python', '-m', 'packageA.moduleA']
        completed = subprocess.run(args, cwd=dir, capture_output=True)
        # Process should complete with 0 return code
        self.assertEqual(completed.returncode, 0)

        return None

    def test_moduleA_call_without_package(self):
        # At learning_main/ depending on how tests are called
        dir = os.path.join(TEST_DIRECTORY, 'src', 'packageA')
        os.chdir(dir)
        args = ['python', '-m', 'moduleA']
        completed = subprocess.run(args, cwd=dir, capture_output=True)
        # Process should complete with 1 return code
        self.assertEqual(completed.returncode, 1)
        self.assertTrue('ImportError' in str(completed.stderr))

        return None
    
    def test_packageA_call(self):
        # At learning_main/ depending on how tests are called
        dir = os.path.join(TEST_DIRECTORY, 'src')
        os.chdir(dir)
        args = ['python', '-m', 'packageA']
        completed = subprocess.run(args, cwd=dir, capture_output=True)
        # Process should complete with 0 return code
        self.assertEqual(completed.returncode, 0)
        return None

if __name__ == '__main__':
    unittest.main()