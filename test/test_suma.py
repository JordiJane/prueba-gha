import sys
sys.path.append('./Calculator')
from Sum import Sum
import pytest

class TestSum:

    def testSumPositives(self):
        sum_values = [1,2,3]
        sum = Sum(sum_values)
        result_sum = sum.SumValues()
        assert result_sum == 6
    
    def testSumNegatives(self):
        sum_values = [-1,-2,-3]
        sum = Sum(sum_values)
        result_sum = sum.SumValues()
        assert result_sum == -6
    
    def testSumMixt(self):
        sum_values = [-10,20,-3]
        sum = Sum(sum_values)
        result_sum = sum.SumValues()
        assert result_sum == 7
    

    