import ml_utils as mlu
import unittest


class TestCV2X(unittest.TestCase): 
    
    def test_moduleB_fun_b(self):
        self.assertTrue(mlu.subpackage2.moduleB.fun_b())
    
if __name__ == '__main__':
    unittest.main() 


