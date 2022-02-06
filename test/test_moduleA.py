import ml_utils as mlu
#import ml_utils.subpackage1.moduleA as moduleA
#import ml_utils.subpackage2.moduleB as moduleB
import unittest


class TestCV2X(unittest.TestCase): 
    
    def test_moduleA_fun_a1(self):
        self.assertTrue(mlu.subpackage1.moduleA.fun_a1())
    
    def test_moduleA_fun_a2(self):
        self.assertTrue(mlu.subpackage1.moduleA.fun_a2())
    
if __name__ == '__main__':
    unittest.main() 


