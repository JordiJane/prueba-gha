import sys
sys.path.append('./Calculator')
from Multiplicate import Multiplicate
import pytest

class TestMultiplicate:

    def testMultiplicatePositives(self):
        mult_values = [4,5,6]
        multiplicate = Multiplicate(mult_values)
        result_mult = multiplicate.MultiplicateValues()
        assert result_mult == 120
    
    def testMultiplicateNegatives(self):
        mult_values = [-4,5,6]
        multiplicate = Multiplicate(mult_values)
        result_mult = multiplicate.MultiplicateValues()
        assert result_mult == -120
    
    def testSumMixt(self):
        mult_values = [-10,20,-3]
        multiplicate = Multiplicate(mult_values)
        result_mult = multiplicate.MultiplicateValues()
        assert result_mult == 600
    

    