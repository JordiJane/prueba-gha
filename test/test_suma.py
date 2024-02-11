import sys
sys.path.append('./Calculator') 
from Sum import Sum
import pytest

class TestSum:

    def testSum(self):
        sum_values = [1,2,3]
        sum = Sum(sum_values)
        result_sum = sum.SumValues()
        assert result_sum == 6

    