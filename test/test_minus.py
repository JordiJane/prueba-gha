import sys
sys.path.append('./Calculator')
from Minus import Minus
import pytest

class TestMinus:

    def testMinusPositives(self):
        minus_values = [1,2,3]
        minus = Minus(minus_values)
        result_minus = minus.MinusValues()
        assert result_minus == -6
    
    def testMinusNegatives(self):
        minus_values = [-1,-2,-3]
        minus = Minus(minus_values)
        result_minus = minus.MinusValues()
        assert result_minus == 6
    
    def testMinusMixt(self):
        minus_values = [-10,20,-3]
        minus = Minus(minus_values)
        result_minus = minus.MinusValues()
        assert result_minus == -7
    

    